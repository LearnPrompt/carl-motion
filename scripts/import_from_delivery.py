#!/usr/bin/env python3
"""一次性导入：把交付目录里的 29 画风数据整理成 data/styles.zh.json。
用法: python3 scripts/import_from_delivery.py <交付根> <交接包根>
只在维护者本机跑；公开仓库里只放导出的 JSON。
"""
import json, os, re, sys
DEL, PKG = sys.argv[1:3]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEL, '源码/common'))
import script_data as D

EN = {  # 编号 → (slug, 英文名)
    'S05': ('retro-paper-collage', 'Retro Paper Collage'), 'S20': ('product-ui-2-5d', 'Product UI 2.5D Camera'),
    'S08': ('neon-synthwave', 'Neon Synthwave'), 'S17': ('hand-drawn-notes', 'Hand-drawn Paper Notes'),
    'S19': ('watercolor', 'Watercolor'), 'S30': ('woodcut', 'Black-and-white Woodcut'),
    'S34': ('soft-inflatable-3d', 'Soft Inflatable 3D'), 'S27': ('point-cloud-survey', 'Point-cloud Survey'),
    'S04': ('blueprint', 'Blueprint Drawing'), 'S14': ('sticker-explainer', 'Die-cut Sticker Explainer'),
    'S13': ('feature-3d-character', 'Feature-film 3D Character'), 'S03': ('chinese-ink-wash', 'Chinese Ink Wash'),
    'S10': ('ascii-crt', 'ASCII Character Visuals'), 'S01': ('isometric-world', 'Isometric 2.5D World'),
    'S23': ('van-gogh-impasto', 'Van Gogh Impasto'), 'S37': ('psychedelic-shader', 'Iridescent Psychedelic Shader'),
    'S12': ('claymation', 'Claymation Stop-motion'), 'S02': ('pixel-game', 'Pixel Game'),
    'S07': ('flat-vector', 'Flat Vector'), 'S24': ('monet-impressionist', 'Impressionist Oil (Monet)'),
    'S35': ('particle-morph', 'Particle Morph'), 'S28': ('white-model-projection', 'White-model Projection'),
    'S22': ('egyptian-mural', 'Ancient Egyptian Mural'), 'S29': ('exploded-view', 'Product Exploded View'),
    'S16': ('editorial-dataviz', 'Editorial Paper Data Story'), 'S06': ('glassmorphism-ui', 'Glassmorphism UI'),
    'S33': ('brick-toy', 'Brick Toy'), 'S11': ('risograph', 'Risograph Print'), 'S15': ('scifi-hud', 'Sci-fi Scan HUD'),
}
SCENE_DIR = {'S22': 'S22-S25_carl', 'S23': 'S22-S25_carl', 'S24': 'S22-S25_carl'}

def lic(url):
    """按来源域名给出媒体可否随仓库分发。"""
    if not url: return ('carl-motion', 'MIT', True)
    if 'lemomo-ai' in url: return ('LemoLab · lemo-opuscar', 'prompts/code MIT, demo video CC BY 4.0', True)
    if 'huashu' in url: return ('alchaincyf · huashu-art-motion', 'MIT (re-rendered from source)', True)
    if 'mg-styles-15' in url: return ('Vincentwei1021 · mg-styles-15', 'prompts/code MIT; demo video not redistributed', False)
    if 'video-shotcraft' in url: return ('Vincentwei1021 · video-shotcraft', 'link only', False)
    if 'prompt-motion' in url: return ('prompt-motion.com', 'link only', False)
    if 'x.com' in url: return ('X post', 'link only', False)
    if 'yasue' in url: return ('yasue.org', 'link only', False)
    return (url, 'link only', False)

clean = lambda t: re.sub(r'本轮(补做|做的|新做)?', lambda m: '我们' + (m.group(1) or '做的'), t)
idx = {s['id']: s for s in json.load(open(os.path.join(PKG, '30画风色序参考/30画风_颜色与来源索引.json')))}
out = []
for k, s in enumerate(D.S):
    sid = s['id']; ours_b = os.path.exists(os.path.join(DEL, f'完成片/{sid}_B_8s.mp4'))
    cases = idx[sid]['cases']; ref = []
    for L in 'ab':
        c = cases.get(L) or {}
        if L == 'b' and ours_b:
            ref.append({'layer': 'B', 'title': '', 'url': '', 'by': 'carl-motion', 'license': 'MIT', 'media_ok': True,
                        'inspired_by': c.get('source_url') or ''})
            continue
        by, li, ok = lic(c.get('source_url'))
        ref.append({'layer': L.upper(), 'title': c.get('title') or '', 'url': c.get('source_url') or '', 'by': by, 'license': li, 'media_ok': ok})
    if ours_b: prev = {'layer': 'B', 'by': 'carl-motion'}
    elif ref[0]['media_ok']: prev = {'layer': 'A', 'by': ref[0]['by']}
    else: prev = None
    sd = SCENE_DIR.get(sid, sid)
    out.append({'order': k + 1, 'id': sid, 'slug': EN[sid][0], 'name_en': EN[sid][1], 'name_zh': s['name'],
                'card': s['card'], 'keywords': s['kw'], 'warn': s['warn'], 'fail': s['fail'],
                'fx_a': s['fx_a'], 'fx_b': clean(s['fx_b']), 'full_prompt': D.full_prompt(s),
                'palette': idx[sid]['palette']['colors'], 'refs': ref, 'preview': prev,
                'scene': f'templates/scenes/{EN[sid][0]}' if ours_b else None, 'scene_src': sd if ours_b else None})
json.dump(out, open(os.path.join(ROOT, 'data/styles.zh.json'), 'w'), ensure_ascii=False, indent=1)
for x in out: print(x['order'], x['id'], x['slug'], 'prev=', x['preview'] and x['preview']['layer'], [r['by'][:14] for r in x['refs']])
