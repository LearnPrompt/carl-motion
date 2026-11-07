#!/usr/bin/env python3
"""Decide how a carl-motion request should start, and record what was actually opened.

This is a router and a file probe. It does not render, does not call a model,
and does not fetch the catalog's reference URLs. A passing run is not evidence
that a language model followed SKILL.md.

    python3 resolve_brief.py --request "用 Risograph 做咖啡店"
    python3 resolve_brief.py --request "..." --media ref.png --media-url https://...
    python3 resolve_brief.py --request "..." --search-file results.json
    python3 resolve_brief.py --audit

Search is used only when nothing in the 29 matches and the user did not supply
a file this process could open. A search command or a results file means the
tool is already available: do not ask for permission again. No command, no
file, and no refusal flag means search is unavailable.
"""
import argparse, hashlib, json, os, re, shlex, subprocess, sys, urllib.request
from collections import Counter
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
REMINDER = (
    '当前没有可用的视频检索能力。请开放搜索权限，以便在 X 上查找合适的参考视频。'
    '在真正打开一条视频之前，不会把任何链接记成已读参考。'
)
BANS = [
    '参考只用来学习色彩、布局、节奏和动效，不照搬 logo、配乐或受版权保护的画面',
    '不伪造产品界面，不编造数字；数字需要来源和日期',
    '来源事实和推断分开；没有打开的素材不算已读',
]
REJECT = re.compile(
    r'新画风|自定义画风|不要套|不要用现有|不要硬塞|29\s*种之外|custom style|not one of the',
    re.I,
)
HOUSE = {'width': 1920, 'height': 1080, 'fps': 30, 'frames': 240, 'seconds': 8}


def find_root():
    start = Path.cwd()
    for base in (start, SKILL):
        here = base
        for _ in range(6):
            if (here / 'assets' / 'previews').is_dir() and (here / 'data' / 'styles.zh.json').is_file():
                return here
            if here.parent == here:
                break
            here = here.parent
    return None


def load_catalog():
    path = SKILL / 'references' / 'style-catalog.json'
    if not path.exists():
        sys.exit(f'missing {path}; run python3 scripts/generate.py from the repo')
    return json.loads(path.read_text(encoding='utf-8'))


def cjk(text):
    return ''.join(re.findall(r'[\u4e00-\u9fff]', text or ''))


def hex_of(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


def pil_image():
    from PIL import Image
    return Image


def dominant_colors(frames):
    Image = pil_image()
    try:
        nearest = Image.Resampling.NEAREST
    except AttributeError:
        nearest = Image.NEAREST
    pixels = []
    for frame in frames:
        small = frame.resize((48, 27), nearest)
        raw = small.tobytes()
        pixels.extend(tuple(raw[i:i + 3]) for i in range(0, len(raw), 3))
    counts = Counter(pixels)
    if not counts:
        return []
    if len(counts) <= 4:
        chosen = counts.most_common(4)
    else:
        buckets = Counter()
        for (r, g, b), n in counts.items():
            buckets[(r // 32 * 32, g // 32 * 32, b // 32 * 32)] += n
        chosen = buckets.most_common(4)
    return [hex_of(rgb) for rgb, _ in chosen]


def mean_abs(a, b):
    Image = pil_image()
    try:
        bilinear = Image.Resampling.BILINEAR
    except AttributeError:
        bilinear = Image.BILINEAR
    left, right = a.resize((32, 18), bilinear).tobytes(), b.resize((32, 18), bilinear).tobytes()
    return round(sum(abs(x - y) for x, y in zip(left, right)) / len(left), 3)


def probe_path(path):
    """Open a local image or animation and measure it. Never treats a missing file as read."""
    file = Path(path)
    info = {
        'provided': True, 'path': str(file), 'opened': False, 'decoded': False,
        'error': None, 'sha256': None, 'kind': None, 'temporal': False,
        'frame_count': 0, 'canvas': None, 'duration_s': None, 'motion_mean_abs': None,
        'colors': [], 'evidence': 'unopened',
    }
    if not file.is_file():
        info['error'] = 'file not found'
        return info
    info['sha256'] = hashlib.sha256(file.read_bytes()).hexdigest()
    try:
        PILImage = pil_image()
    except ImportError:
        info['error'] = 'Pillow is not installed; file bytes were hashed but frames were not decoded'
        return info
    try:
        image = PILImage.open(file)
        frames_n = getattr(image, 'n_frames', 1)
        indexes = [0] if frames_n <= 1 else [0, frames_n // 2, frames_n - 1]
        frames = []
        duration_ms = None
        for index in indexes:
            image.seek(index)
            duration_ms = image.info.get('duration', duration_ms)
            frames.append(image.copy().convert('RGB'))
        motion = mean_abs(frames[0], frames[-1]) if len(frames) > 1 else None
        temporal = bool(motion is not None and motion > 1)
        info.update({
            'opened': True, 'decoded': True, 'error': None,
            'kind': 'video' if temporal or frames_n > 1 else 'still_image',
            'temporal': temporal, 'frame_count': frames_n, 'canvas': list(image.size),
            'duration_s': round(frames_n * duration_ms / 1000.0, 3) if duration_ms else None,
            'motion_mean_abs': motion, 'colors': dominant_colors(frames),
            'evidence': 'decoded_frames',
        })
        if info['kind'] == 'video' and not temporal:
            info['kind'] = 'video'
        if frames_n <= 1:
            info['kind'] = 'still_image'
            info['temporal'] = False
    except Exception as exc:
        info['error'] = f'{type(exc).__name__}: {exc}'
    return info


def probe_url(url):
    """Record whether a connection opened. Do not download or decode the body."""
    out = {
        'provided': True, 'url': url, 'path': None, 'opened': False, 'decoded': False,
        'error': None, 'sha256': None, 'kind': None, 'temporal': None, 'colors': [],
        'evidence': 'unopened',
    }
    request = urllib.request.Request(url, headers={'User-Agent': 'carl-motion-resolve/0.2'})
    try:
        with urllib.request.urlopen(request, timeout=3) as response:
            out['opened'] = True
            out['status'] = getattr(response, 'status', None)
            out['content_type'] = response.headers.get('Content-Type')
            out['error'] = 'connection opened; body not downloaded or decoded'
            out['evidence'] = 'headers_only'
    except Exception as exc:
        out['error'] = f'{type(exc).__name__}: {exc}'
    return out


def empty_user_reference():
    return {
        'provided': False, 'opened': False, 'decoded': False, 'error': None,
        'path': None, 'url': None, 'sha256': None, 'kind': None, 'temporal': None,
        'colors': [], 'evidence': 'none',
    }


def name_owners(styles, request):
    """Styles whose name or slug is actually written in the request.

    A Chinese fragment counts only when it belongs to one style, so a shared
    word such as 复古 cannot mark two styles at once. Two real hits stay mixed.
    """
    hits = {}
    lowered = request.lower()
    owners = {}
    for style in styles:
        name = cjk(style['name_zh'])
        for length in range(len(name), 1, -1):
            for start in range(0, len(name) - length + 1):
                frag = name[start:start + length]
                if frag in request:
                    owners.setdefault(frag, set()).add(style['slug'])
        tokens = set(re.findall(r'[a-z0-9]+', style['name_en'].lower())) | set(style['slug'].split('-'))
        for token in tokens:
            if len(token) >= 4:
                owners.setdefault(token, set()).add(style['slug'])
    for style in styles:
        reasons = []
        if re.search(r'(?<![a-z0-9])' + re.escape(style['slug']) + r'(?![a-z0-9])', lowered):
            reasons.append('slug')
        if style['name_en'].lower() in lowered:
            reasons.append('name_en')
        name = cjk(style['name_zh'])
        if name and name in request:
            reasons.append('name_zh')
        if reasons:
            hits[style['slug']] = reasons
    for frag, slugs in owners.items():
        if len(slugs) != 1:
            continue
        if frag not in request and frag not in lowered:
            continue
        slug = next(iter(slugs))
        hits.setdefault(slug, [])
        if not any(item.startswith('name') or item == 'slug' for item in hits[slug]):
            hits[slug].append('name_fragment')
    return hits


def keyword_owners(styles, request):
    hits = {}
    blob = request.lower()
    for style in styles:
        phrases = re.split(r'[、,，]', (style.get('keywords_zh') or '') + ',' + (style.get('keywords_en') or ''))
        found = [part.strip() for part in phrases if len(part.strip()) >= 4 and part.strip().lower() in blob]
        if found:
            hits[style['slug']] = found
    return hits


def classify(styles, request, decoded):
    reject = REJECT.search(request or '') is not None
    names = name_owners(styles, request or '')
    keywords = keyword_owners(styles, request or '')
    nearby = list(dict.fromkeys([*names, *keywords]))
    if reject:
        decision = 'custom' if decoded else 'no_preset'
        return decision, [], nearby
    if len(names) >= 2:
        return 'mixed', list(names), []
    if len(names) == 1:
        return 'exact', list(names), []
    if len(keywords) >= 2:
        return 'mixed', list(keywords), []
    if len(keywords) == 1:
        return 'candidate', list(keywords), []
    if decoded:
        return 'custom', [], []
    return 'no_preset', [], []


def engine_of(style):
    slug = style.get('engine_slug')
    if not slug:
        return None
    path = SKILL / 'scenes' / slug / 'engine.json'
    data = json.loads(path.read_text(encoding='utf-8')) if path.is_file() else {}
    return {
        'slug': slug,
        'stack': data.get('stack') or style.get('engine_stack'),
        'entry': data.get('entry') or style.get('engine_entry'),
        'scene': f'scenes/{slug}',
    }


def preview_of(style, root):
    meta = style.get('preview') or {}
    rel = meta.get('file')
    base = {
        'path': rel, 'exists': False, 'layer': meta.get('layer'), 'by': meta.get('by'),
        'decoded': False, 'used_as_video_reference': False, 'kind': 'absent',
        'frame_count': 0, 'canvas': None, 'duration_s': None, 'motion_mean_abs': None,
        'temporal': False, 'colors': [], 'original_url_fetched': False,
        'full_source_video': False, 'copied_frames_into_engine': False,
        'application': 'not_opened', 'evidence': 'none',
        'excerpt_claim': meta.get('excerpt'),
    }
    if not rel:
        base['kind'] = 'text_poster_not_a_reference'
        base['text_poster'] = meta.get('text_poster')
        base['evidence'] = 'no_redistributable_clip'
        return base
    if root is None:
        base['error'] = 'repo asset root not found'
        return base
    path = root / rel
    base['exists'] = path.is_file()
    if not base['exists']:
        base['error'] = 'preview file missing'
        return base
    probed = probe_path(path)
    full = bool(
        probed.get('canvas') and probed['canvas'][0] >= 1280
        and probed.get('duration_s') and probed['duration_s'] >= 7.5
    )
    base.update({
        'exists': True, 'decoded': probed['decoded'], 'error': probed['error'],
        'kind': 'animated_excerpt' if probed.get('frame_count', 0) > 1 else 'still',
        'frame_count': probed['frame_count'], 'canvas': probed['canvas'],
        'duration_s': probed['duration_s'], 'motion_mean_abs': probed['motion_mean_abs'],
        'temporal': probed['temporal'], 'colors': probed['colors'],
        'full_source_video': full,
        'evidence': probed['evidence'] if probed['decoded'] else 'unopened',
        'sha256': probed['sha256'],
    })
    if probed['decoded']:
        base['application'] = 'decoded_not_selected'
    return base


def catalog_refs(style):
    rows = []
    for ref in style.get('refs') or []:
        rows.append({
            'layer': ref.get('layer'), 'title': ref.get('title') or '',
            'url': ref.get('url') or '', 'by': ref.get('by'),
            'license': ref.get('license'), 'media_ok': ref.get('media_ok'),
            'fetched': False, 'decoded': False, 'role': 'catalog_link',
        })
    return rows


def style_view(style, root, match):
    preview = preview_of(style, root)
    return {
        'order': style['order'], 'id': style['id'], 'slug': style['slug'],
        'name_en': style['name_en'], 'name_zh': style['name_zh'],
        'status': style['status'], 'match': match, 'card': style['card'],
        'engine': engine_of(style), 'palette_catalog': style.get('palette') or [],
        'references': catalog_refs(style), 'local_preview': preview,
    }


def match_label(decision, slug, names, keywords):
    if decision == 'candidate':
        return 'keyword'
    if decision == 'exact':
        return 'name'
    if slug in names:
        return 'name'
    if slug in keywords:
        return 'keyword'
    return decision


def run_search(args, request):
    """Return a search record. Does not invent posts."""
    if args.search_refused:
        return {
            'available': True, 'attempted': True, 'refused': True, 'result_count': 0,
            'results': [], 'reminder': None,
            'message': f'检索被拒绝：{args.search_refused}。没有搜索结果。风格参数停在依赖这一步，规格保持草稿。',
        }
    if args.search_file:
        payload = json.loads(Path(args.search_file).read_text(encoding='utf-8'))
        results = payload.get('results', payload if isinstance(payload, list) else [])
        return normalize_search(results, attempted=True, via='search_file')
    if args.search_cmd:
        proc = subprocess.run(
            shlex.split(args.search_cmd), input=request, text=True,
            capture_output=True, timeout=60,
        )
        if proc.returncode != 0:
            reason = (proc.stderr or proc.stdout or f'exit {proc.returncode}').strip()[:300]
            return {
                'available': True, 'attempted': True, 'refused': True, 'result_count': 0,
                'results': [], 'reminder': None,
                'message': f'检索被拒绝：{reason}。没有搜索结果。风格参数停在依赖这一步，规格保持草稿。',
            }
        try:
            payload = json.loads(proc.stdout or '{}')
        except json.JSONDecodeError as exc:
            return {
                'available': True, 'attempted': True, 'refused': True, 'result_count': 0,
                'results': [], 'reminder': None,
                'message': f'检索被拒绝：结果不是 JSON（{exc}）。没有可用参考。',
            }
        results = payload.get('results', [])
        record = normalize_search(results, attempted=True, via='search_cmd')
        record['query_seen_by_command'] = payload.get('query')
        return record
    return {
        'available': False, 'attempted': False, 'refused': False, 'result_count': 0,
        'results': [], 'reminder': REMINDER,
        'message': REMINDER,
    }


def normalize_search(results, attempted, via):
    rows = []
    for item in results:
        row = {
            'url': item.get('url'), 'title': item.get('title'), 'source': item.get('source'),
            'opened': False, 'decoded': False, 'local_path': item.get('local_path'),
        }
        if item.get('local_path'):
            probed = probe_path(item['local_path'])
            row['opened'] = probed['opened']
            row['decoded'] = probed['decoded']
            row['colors'] = probed['colors']
            row['sha256'] = probed['sha256']
            row['kind'] = probed['kind']
            row['error'] = probed['error']
        rows.append(row)
    count = len(rows)
    if count == 0:
        message = '检索已执行，没有结果。风格参数停在依赖这一步，上面的规格是草稿。没有把检索说成已经看过参考视频。'
    else:
        message = f'检索到 {count} 条链接。这些链接没有打开，也不能当作已读参考。'
        if any(row['decoded'] for row in rows):
            message = f'检索到 {count} 条。其中已打开的本地文件测量了色彩；没打开的链接仍不算已读参考。'
    return {
        'available': True, 'attempted': attempted, 'refused': False, 'result_count': count,
        'results': rows, 'reminder': None, 'message': message, 'via': via,
    }


def decoded_search_media(search):
    for row in search.get('results') or []:
        if row.get('decoded') and row.get('local_path'):
            return probe_path(row['local_path'])
    return None


def parameters_from(source, colors, draft):
    return {
        'source': source, 'colors': colors[:4], 'type_px': None, 'grid': None,
        'stroke_px': None, 'radius_px': None, 'ease': None, 'motion_duration_s': None,
        'bans': list(BANS), 'draft': draft,
    }


def blocked_style(reason):
    return {'blocked': True, 'reason': reason, 'label': '缺素材'}


def resolve(catalog, request, media, url, search, root):
    styles = catalog['styles']
    by_slug = {style['slug']: style for style in styles}
    user = empty_user_reference()
    facts, inferences = [], []
    if media:
        probed = probe_path(media[0])
        user = probed
        user['url'] = None
        if probed['decoded']:
            facts.append({
                'kind': 'user_file', 'path': probed['path'], 'sha256': probed['sha256'],
                'colors': probed['colors'], 'kind_media': probed['kind'],
                'frame_count': probed['frame_count'],
            })
    elif url:
        user = probe_url(url)
        facts.append({'kind': 'user_url_not_decoded', 'url': url, 'error': user['error']})
    decoded = bool(user.get('decoded'))
    decision, chosen, nearby = classify(styles, request, decoded)
    if decision == 'no_preset' and not decoded:
        found = decoded_search_media(search) if search and search.get('attempted') else None
        if found and found.get('decoded'):
            decision = 'custom'
            decoded = True
            facts.append({
                'kind': 'search_local_file', 'path': found['path'], 'sha256': found['sha256'],
                'colors': found['colors'],
            })
            user = found
            user['url'] = None
    names = name_owners(styles, request or '')
    keywords = keyword_owners(styles, request or '')
    views = []
    for slug in chosen:
        label = match_label(decision, slug, names, keywords)
        views.append(style_view(by_slug[slug], root, label))
    for view in views:
        preview = view['local_preview']
        if decision == 'exact' and preview.get('decoded') and preview.get('frame_count', 0) > 1:
            preview['used_as_video_reference'] = True
            preview['application'] = 'measured_color_and_motion_only'
        elif preview.get('decoded'):
            preview['used_as_video_reference'] = False
            preview['application'] = 'decoded_not_selected'
        if preview.get('decoded'):
            facts.append({
                'kind': 'decoded_preview_excerpt', 'slug': view['slug'], 'path': preview['path'],
                'layer': preview['layer'], 'by': preview['by'], 'frames': preview['frame_count'],
                'motion_mean_abs': preview['motion_mean_abs'], 'duration_s': preview['duration_s'],
                'full_source_video': preview['full_source_video'],
            })
        for ref in view['references']:
            if ref['url']:
                facts.append({
                    'kind': 'catalog_link_not_fetched', 'slug': view['slug'],
                    'layer': ref['layer'], 'url': ref['url'],
                })
        if view['palette_catalog']:
            facts.append({'kind': 'catalog_palette', 'slug': view['slug'], 'colors': view['palette_catalog']})
    if decision == 'custom' and user.get('colors'):
        params = parameters_from('measured_user_media', user['colors'], draft=True)
        style_step = {'blocked': False, 'reason': None, 'label': '已测量'}
    elif decision == 'exact':
        params = parameters_from('catalog_palette', views[0]['palette_catalog'] if views else [], draft=False)
        style_step = {'blocked': False, 'reason': None, 'label': '预设卡'}
    else:
        params = parameters_from('blocked', [], draft=True)
        if decision == 'no_preset':
            style_step = blocked_style('没有预设命中，也没有已打开的参考图或视频，风格参数不能测量')
        elif decision in ('mixed', 'candidate'):
            style_step = blocked_style('相近或混合，不能当成唯一精确画风；等用户选定之前不套用引擎')
        else:
            style_step = blocked_style('风格还不能测量')
    render_blocked = decision in ('no_preset', 'mixed', 'candidate') or style_step['blocked']
    house_draft = decision != 'exact'
    brief = {
        'decision': decision,
        'forced_preset': False,
        'retargeted_framework': None,
        'request': request,
        'styles': views,
        'nearby_not_selected': nearby if decision in ('no_preset', 'custom') and nearby else [],
        'user_reference': {
            'provided': bool(media or url or user.get('decoded')),
            'opened': bool(user.get('opened')),
            'decoded': bool(user.get('decoded')),
            'error': user.get('error'),
            'path': user.get('path'),
            'url': url or user.get('url'),
            'sha256': user.get('sha256'),
            'kind': user.get('kind'),
            'temporal': user.get('temporal'),
            'colors': user.get('colors') or [],
            'evidence': user.get('evidence') or 'none',
        },
        'style_parameters': params,
        'search': search or {
            'available': False, 'attempted': False, 'refused': False, 'result_count': 0,
            'results': [], 'reminder': None, 'message': None,
        },
        'steps': {
            'house_spec': {
                'blocked': False, 'draft': house_draft,
                'label': '草稿' if house_draft else '规格',
                'value': dict(catalog.get('house') or HOUSE),
            },
            'style_parameters': style_step,
            'render': {
                'blocked': render_blocked,
                'reason': style_step['reason'] if render_blocked else None,
                'still_first': decision == 'custom',
            },
        },
        'facts': facts,
        'inferences': inferences,
        'material_rules': list(BANS),
        'limits': {
            'llm_compliance_proven': False,
            'what_this_is': 'router and file probe',
            'engines_rewritten': False,
            'catalog_urls_fetched': False,
        },
    }
    if decision != 'no_preset':
        # Search permission is not part of a matched, mixed, or measured brief.
        if brief['search'].get('reminder') and not brief['search'].get('attempted'):
            brief['search'] = {
                'available': brief['search'].get('available', False), 'attempted': False,
                'refused': False, 'result_count': 0, 'results': [], 'reminder': None,
                'message': None,
            }
    return brief


def audit(catalog, root):
    decoded = posters = exact = engines = 0
    stacks = Counter()
    links = []
    seen = set()
    for style in catalog['styles']:
        brief = resolve(catalog, style['name_zh'], None, None, None, root)
        if brief['decision'] == 'exact' and [item['slug'] for item in brief['styles']] == [style['slug']]:
            exact += 1
        if style.get('engine_slug'):
            engines += 1
            stack = (brief['styles'][0]['engine'] or {}).get('stack') if brief['styles'] else None
            stacks[stack or 'missing'] += 1
            if stack in ('hyperframes', 'gsap'):
                pass
        preview = brief['styles'][0]['local_preview'] if brief['styles'] else {}
        if preview.get('decoded') and preview.get('frame_count', 0) > 1:
            decoded += 1
        if preview.get('kind') == 'text_poster_not_a_reference':
            posters += 1
        for ref in style.get('refs') or []:
            key = (style['slug'], ref.get('layer'), ref.get('url'))
            if key in seen:
                continue
            seen.add(key)
            links.append({
                'slug': style['slug'], 'layer': ref.get('layer'), 'url': ref.get('url') or '',
                'by': ref.get('by'), 'media_ok': ref.get('media_ok'), 'fetched': False,
                'preview_file': (style.get('preview') or {}).get('file'),
                'preview_layer': (style.get('preview') or {}).get('layer'),
            })
    hyper = sum(n for stack, n in stacks.items() if stack in ('hyperframes', 'gsap'))
    return {
        'styles': len(catalog['styles']), 'with_engine': engines, 'exact_on_own_name': exact,
        'decoded_previews': decoded, 'text_posters_not_used_as_video': posters,
        'hyperframes_engines': hyper, 'stacks': dict(stacks), 'reference_links': links,
        'limits': {'llm_compliance_proven': False, 'what_this_is': 'audit of the router on catalog names'},
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description='Resolve a carl-motion style brief')
    parser.add_argument('--request', default='')
    parser.add_argument('--media', action='append', default=[])
    parser.add_argument('--media-url', default='')
    parser.add_argument('--search-file', default='')
    parser.add_argument('--search-cmd', default=os.environ.get('CARL_MOTION_SEARCH_CMD', ''))
    parser.add_argument('--search-refused', default='')
    parser.add_argument('--audit', action='store_true')
    args = parser.parse_args(argv)
    catalog = load_catalog()
    root = find_root()
    if args.audit:
        payload = audit(catalog, root)
    else:
        if not args.request:
            parser.error('--request is required unless --audit')
        # An exact, mixed, or measured brief must not trigger a search.
        preliminary = resolve(catalog, args.request, args.media, args.media_url or '', None, root)
        needs_search = preliminary['decision'] == 'no_preset' and not preliminary['user_reference']['decoded']
        if needs_search:
            payload = resolve(
                catalog, args.request, args.media, args.media_url or '',
                run_search(args, args.request), root,
            )
        else:
            payload = preliminary
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write('\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
