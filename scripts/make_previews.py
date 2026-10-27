#!/usr/bin/env python3
"""从本地成片切出仓库里的预览图：每个画风一张动图 WebP 和一张海报 JPG，外加首屏画风墙。
用法: python3 scripts/make_previews.py <交付根> <1080×608 片段目录>
只用 data/styles.zh.json 里 preview 不为空的画风（我们自己的 B，或允许分发的上游 A）。
"""
import json, os, sys
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont
DEL, CL = sys.argv[1:3]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = json.load(open(os.path.join(ROOT, 'data/styles.zh.json')))
ACC, INK, PAPER, MUTE = (255, 84, 20), (17, 17, 17), (242, 239, 232), (150, 150, 146)
HN = '/System/Library/Fonts/HelveticaNeue.ttc'
f = lambda size, bold=True: ImageFont.truetype(HN, size, index=1 if bold else 0)

def src(s):
    return os.path.join(DEL, f'完成片/{s["id"]}_B_8s.mp4') if s['preview']['layer'] == 'B' else os.path.join(CL, f'{s["id"]}_A.mp4')

def grab(path, t0, t1, fps, size):
    cap = cv2.VideoCapture(path); n0, n1 = int(t0 * 30), int(t1 * 30); step = 30 // fps; out = []
    cap.set(cv2.CAP_PROP_POS_FRAMES, n0)
    for i in range(n0, n1):
        ok, fr = cap.read(); assert ok, (path, i)
        if (i - n0) % step == 0: out.append(cv2.cvtColor(cv2.resize(fr, size, interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2RGB))
    return out

for d in ('assets/previews', 'assets/posters'): os.makedirs(os.path.join(ROOT, d), exist_ok=True)
tiles = {}
for s in S:
    if not s['preview']: continue
    p = src(s); fr = grab(p, 1.5, 5.5, 10, (480, 270))
    Image.fromarray(fr[0]).save(os.path.join(ROOT, f'assets/previews/{s["slug"]}.webp'), save_all=True,
                                append_images=[Image.fromarray(x) for x in fr[1:]], duration=100, loop=0, quality=62, method=4)
    cap = cv2.VideoCapture(p); cap.set(cv2.CAP_PROP_POS_FRAMES, 120); ok, im = cap.read()
    cv2.imwrite(os.path.join(ROOT, f'assets/posters/{s["slug"]}.jpg'), cv2.resize(im, (960, 540), interpolation=cv2.INTER_AREA), [cv2.IMWRITE_JPEG_QUALITY, 84])
    tiles[s['id']] = grab(p, 2.0, 5.0, 10, (320, 180))

# —— 首屏画风墙：6×5，29 格画风 + 1 格标题，单强调色、0 圆角、1px 边 ——
TW, TH, C, R, NF = 320, 180, 6, 5, 30
def label(img, s):
    d = ImageDraw.Draw(img); t = f'{s["order"]:02d}  {s["name_en"]}'; w = f(15).getlength(t)
    d.rectangle([0, TH - 26, w + 16, TH], fill=INK); d.text((8, TH - 22), t, font=f(15), fill=PAPER)
def text_tile(s):
    im = Image.new('RGB', (TW, TH), INK); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, TW - 1, TH - 1], outline=(70, 70, 70)); d.rectangle([16, 20, 40, 24], fill=ACC)
    d.text((16, 40), f'{s["order"]:02d}', font=f(22), fill=ACC)
    words, line, y = s['name_en'].split(), '', 72
    for w_ in words:
        if f(24).getlength(line + ' ' + w_) > TW - 32 and line: d.text((16, y), line, font=f(24), fill=PAPER); y += 30; line = w_
        else: line = (line + ' ' + w_).strip()
    d.text((16, y), line, font=f(24), fill=PAPER); d.text((16, TH - 30), 'prompt + source link', font=f(15, False), fill=MUTE)
    return im
def title_tile():
    im = Image.new('RGB', (TW, TH), ACC); d = ImageDraw.Draw(im)
    d.text((16, 22), 'carl-motion', font=f(34), fill=INK); d.text((16, 70), '29 motion styles', font=f(22), fill=INK)
    d.text((16, 98), 'one prompt each, 8 s', font=f(22, False), fill=INK); d.text((16, TH - 30), 'github.com/LearnPrompt/carl-motion', font=f(13, False), fill=INK)
    return im
static = {s['id']: text_tile(s) for s in S if s['id'] not in tiles}; tt = title_tile()
frames = []
for i in range(NF):
    wall = Image.new('RGB', (TW * C, TH * R), INK); cells = S + [None]
    for k, s in enumerate(cells):
        x, y = (k % C) * TW, (k // C) * TH
        if s is None: wall.paste(tt, (x, y)); continue
        if s['id'] in tiles: im = Image.fromarray(tiles[s['id']][i]); label(im, s)
        else: im = static[s['id']]
        wall.paste(im, (x, y))
    d = ImageDraw.Draw(wall)
    for c in range(1, C): d.line([(c * TW, 0), (c * TW, TH * R)], fill=INK, width=1)
    for r in range(1, R): d.line([(0, r * TH), (TW * C, r * TH)], fill=INK, width=1)
    frames.append(wall)
frames[0].save(os.path.join(ROOT, 'assets/style-wall.webp'), save_all=True, append_images=frames[1:], duration=100, loop=0, quality=55, method=4)
frames[15].convert('RGB').save(os.path.join(ROOT, 'assets/style-wall.jpg'), quality=82)
print(len(tiles), 'motion tiles,', len(static), 'text tiles')
