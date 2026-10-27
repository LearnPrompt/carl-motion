# 05 · Watercolor · 水彩手绘 (`watercolor`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/watercolor/` (Python (NumPy + OpenCV + Pillow)). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use Canvas to draw a watercolor journal page that colors itself, with your topic as the subject: transparent strokes layered one on another, dry-brush skips, and paper white kept for highlights. Key visuals: warm cotton paper fibers, transparent wash that deepens as it layers, dry-brush skips, paper white as highlight, handwritten notes with leader lines, stroke-by-stroke coloring, mist-wipe transition, low-saturation ochre and gray-blue. Watch out: Vector shapes with a watercolor texture look fake; use variable-width strokes plus bristle trails. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Canvas 画一页会自己上色的水彩手账，主题是你的主题，透明笔触一层层叠，干笔飞白，纸白留作高光。画面要点：暖色棉纸纤维、透明 wash 越叠越深、dry-brush 飞白、纸白当高光、手写批注加引线、逐笔上色、薄雾擦除转场、赭石灰蓝低饱和。注意：矢量图贴水彩纹理会假，要用变宽笔触加毛刷轨迹。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#b88a3e`

## Pipeline · 管线

- 一切都是笔触：沿路径做变宽色带，再叠一组刷毛轨迹，每根刷毛有自己的墨量、断续和枯竭点；干笔时色带提前收掉，只剩刷毛，出飞白。天空、地面、陶罐、猫身都是宽笔触，没有矢量平涂色块。
- 颜料按透射叠加：画面 = 纸色 × exp(−浓度 × 吸收)，两笔交叠处自然更深，颜色透明。
- 每笔上纸后做水彩处理：边缘积色、低频积水不匀、纸纹颗粒沉淀、湿笔外晕；天空和地面的回流花在晾干时长出来；刚画的笔触偏深，0.8 s 内晾干变浅。
- 纸白当高光：云、太阳底、陶罐高光、猫胸口都是从浓度里提白。
- 猫和老鼠先在背景里留白再上色；同一角色同色的几笔先并成一块再上色，只在外沿积色，内部不起接缝。
- 手写字用 Bradley Hand 粗体，深褐墨，从左往右写出；字幕底下是一笔浅赭色带。

## Beats · 节拍

0–0.8 s 暖白棉纸上，天空两道湿笔从左往右扫开，太阳留白后点上｜0.3–1.3 s 远山、沙地一道道叠下来｜0.7–1.6 s 泥砖房、陶罐、芦苇逐笔画出，0.65 s 起手写字幕 STORED GRAIN DREW MICE｜1.6–4.2 s 四只老鼠一走一停溜向谷堆，到了就低头啃｜3.95–4.4 s 字幕薄雾擦除，4.3 s 起写出 THEN CAME THE WILDCAT｜4.0 s 起芦苇被拨动，4.3–6.6 s 虎斑野猫从右边芦苇里走出来、减速停下｜5.0 s 老鼠停住竖耳，最右边一只回头｜6.05 s 引线画出，6.3 s 手写批注 wildcat · Felis lybica｜6.5–8 s 猫低头盯着老鼠，尾巴摆、芦苇晃、镜头继续推近 3.5%。

## Pitfalls · 踩到的坑

- Vector shapes with a watercolor texture look fake at a glance; use variable-width strokes and bristle edges, leave paper white in the highlights, and do not fill whole areas with color.
- 矢量形状贴水彩纹理一眼就假；要用变宽笔触和毛刷边，亮部留纸白；颜色别填满整块。
- No jump frames flagged; there are no cuts and caption changes use a mist wipe (max frame difference 1.46).
- Frame 1 is blank paper and the sky starts sweeping from frame 1, so it counts as neither black nor still.
- The cat is a side-view walk built from a few strokes, with straight legs and only leg swing and body bob, no fine expressions.
- Granulation and paper texture are slightly heavier than in A, and overall saturation is a little higher.
- The handwritten annotation wildcat Felis lybica has about 36 px capitals, one step smaller than the main caption (about 45 px).

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
