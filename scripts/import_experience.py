#!/usr/bin/env python3
"""Pull field notes from a project's carl-motion-log.md into data/experience/<slug>.jsonl.

    python3 scripts/import_experience.py path/to/carl-motion-log.md

Log lines look like:  - 2026-10-27 · risograph · coffee shop opening · yellow · ink too dark at 4 s · lowered blue plate to 0.8
Lines already imported (same date, slug and note) are skipped. Re-run scripts/generate.py afterwards.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
slugs = {s['slug'] for s in json.load(open(os.path.join(ROOT, 'data/styles.zh.json')))}
added = 0
for line in open(sys.argv[1], encoding='utf-8'):
    parts = [p.strip() for p in line.strip().lstrip('-').split('·')]
    if len(parts) < 5 or parts[1] not in slugs: continue
    date, slug, topic, verdict, *rest = parts
    note = ' · '.join(rest)
    p = os.path.join(ROOT, 'data/experience', f'{slug}.jsonl')
    seen = {(d['date'], d['note']) for d in map(json.loads, open(p))} if os.path.exists(p) else set()
    if (date, note) in seen: continue
    with open(p, 'a', encoding='utf-8') as f: f.write(json.dumps({'date': date, 'topic': topic, 'verdict': verdict, 'note': note}, ensure_ascii=False) + '\n')
    added += 1
print('added', added)
