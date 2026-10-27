#!/usr/bin/env python3
"""Everything that must hold before a release. Exit 0 only when every check passes.

    python3 scripts/check_release.py            # all checks
    python3 scripts/check_release.py --fast     # skip the deliver.py fixtures (no ffmpeg needed)

1. generated files match the data (re-runs scripts/generate.py and compares)
2. every relative link and image in every Markdown file resolves
3. 29 style cards plus INDEX, each card with its six sections
4. the skill folder is self-contained: no paths out of it, a LICENSE inside it
5. every engine has a valid engine.json that covers the styles pointing at it
6. one version: VERSION = SKILL.md metadata.version = marketplace.json
7. deliver.py goes red (exit 2) on a missing frame and on black frames
"""
import glob, hashlib, json, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, 'skills/carl-motion')
fails = []


def fail(msg): fails.append(msg); print('  FAIL', msg)


def digest(paths):
    return {p: hashlib.sha256(open(p, 'rb').read()).hexdigest() for p in paths if os.path.exists(p)}


def generated():
    return ([os.path.join(ROOT, f) for f in ('README.md', 'README_zh.md', '.claude-plugin/marketplace.json')]
            + glob.glob(os.path.join(ROOT, 'docs/styles/*.md')) + glob.glob(os.path.join(SKILL, 'references/styles/*.md'))
            + [os.path.join(SKILL, 'SKILL.md')])


print('1 generated files match data')
before = digest(generated())
r = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts/generate.py')], capture_output=True, text=True)
if r.returncode: fail(f'generate.py failed: {r.stderr.strip()[-300:]}')
after = digest(generated())
for p in sorted(set(before) | set(after)):
    if before.get(p) != after.get(p): fail(f'out of date, re-run scripts/generate.py and commit: {os.path.relpath(p, ROOT)}')

print('2 relative links')
mds = [p for p in glob.glob(os.path.join(ROOT, '**/*.md'), recursive=True) if '/node_modules/' not in p and '/.git/' not in p]
for md in mds:
    text = open(md, encoding='utf-8').read(); text = re.sub(r'```.*?```', '', text, flags=re.S)
    for m in re.finditer(r'\]\(([^)\s]+)\)|src="([^"]+)"|href="([^"]+)"', text):
        u = next(x for x in m.groups() if x)
        if re.match(r'^(https?:|mailto:|#)', u): continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(md), u.split('#')[0]))):
            fail(f'{os.path.relpath(md, ROOT)} → {u}')

print('3 style cards')
styles = json.load(open(os.path.join(ROOT, 'data/styles.zh.json')))
cards = sorted(glob.glob(os.path.join(SKILL, 'references/styles/[0-9][0-9]_*.md')))
if len(cards) != len(styles): fail(f'{len(cards)} cards for {len(styles)} styles')
if not os.path.exists(os.path.join(SKILL, 'references/styles/INDEX.md')): fail('references/styles/INDEX.md missing')
SECTIONS = ['## Status', '## Prompt', '## Pipeline', '## Beats', '## Pitfalls', '## Field notes']
for c in cards:
    t = open(c, encoding='utf-8').read()
    for h in SECTIONS:
        if h not in t: fail(f'{os.path.basename(c)} lacks "{h}"')

print('4 skill is self-contained')
if not os.path.exists(os.path.join(SKILL, 'LICENSE')): fail('skills/carl-motion/LICENSE missing')
for p in glob.glob(os.path.join(SKILL, '**/*'), recursive=True):
    if os.path.isdir(p) or '/node_modules/' in p or p.endswith(('.json', '.png', '.jpg')) and 'engine.json' not in p: continue
    try: t = open(p, encoding='utf-8').read()
    except UnicodeDecodeError: continue
    for pat in (r'\.\./\.\./\.\./', r'/Users/', r'~/Downloads', r'templates/'):
        if re.search(pat, t): fail(f'{os.path.relpath(p, ROOT)} contains {pat}')

print('5 engines')
for d in sorted(glob.glob(os.path.join(SKILL, 'scenes/*/'))):
    slug = os.path.basename(d.rstrip('/')); ej = os.path.join(d, 'engine.json')
    if not os.path.exists(os.path.join(d, 'render.sh')): fail(f'{slug}: render.sh missing')
    if not os.path.exists(ej): fail(f'{slug}: engine.json missing'); continue
    try: e = json.load(open(ej))
    except Exception as ex: fail(f'{slug}: engine.json invalid ({ex})'); continue
    for k in ('slug', 'styles', 'stack', 'entry', 'requires', 'fonts', 'crf', 'deterministic', 'summary_en', 'limits_en'):
        if k not in e: fail(f'{slug}: engine.json lacks {k}')
    want = [s['id'] for s in styles if s['scene'] and s['scene'].rstrip('/').endswith('/' + slug)]
    if sorted(want) != sorted(e.get('styles', [])): fail(f'{slug}: engine.json styles {e.get("styles")} but data points {want} here')

print('6 one version')
v = open(os.path.join(ROOT, 'VERSION')).read().strip()
sk = re.search(r'version: "([^"]+)"', open(os.path.join(SKILL, 'SKILL.md')).read())
mk = {p['version'] for p in json.load(open(os.path.join(ROOT, '.claude-plugin/marketplace.json')))['plugins']}
if not sk or sk.group(1) != v or mk != {v}: fail(f'VERSION {v}, SKILL.md {sk and sk.group(1)}, marketplace {mk}')

if '--fast' not in sys.argv:
    print('7 deliver.py goes red on broken input')
    import numpy as np, cv2
    tmp = tempfile.mkdtemp(prefix='carl-motion-check-')
    deliver = os.path.join(SKILL, 'scripts/deliver.py')
    black = np.zeros((1080, 1920, 3), np.uint8); ok, buf = cv2.imencode('.png', black); blob = buf.tobytes()
    for case, n in (('missing_frame', 239), ('black_frames', 240)):
        d = os.path.join(tmp, case); os.makedirs(d)
        for i in range(1, n + 1): open(os.path.join(d, f'{i:04d}.png'), 'wb').write(blob)
        out = os.path.join(tmp, f'{case}.mp4')
        r = subprocess.run([sys.executable, deliver, '--frames', d, '--out', out], capture_output=True, text=True)
        if r.returncode != 2: fail(f'deliver.py on {case}: exit {r.returncode}, expected 2')
        if os.path.exists(out): fail(f'deliver.py on {case}: wrote a clip on red')

print('\nPASS' if not fails else f'\n{len(fails)} problem(s)')
sys.exit(1 if fails else 0)
