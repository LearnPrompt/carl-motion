# 19 · Flat Vector · 扁平矢量 (`flat-vector`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/flat-vector/` (Python (NumPy + OpenCV + Pillow)). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use SVG plus GSAP to make a flat vector explainer of your topic: solid colors with no gradients, five or six high-saturation colors, elements entering with springy motion, in one continuous shot. Key visuals: SVG plus GSAP, large solid color blocks, five-or-six-color high-saturation palette, overshoot elastic easing, anticipation then burst then rebound, about 10% squash and stretch, stagger of two to four frames, shape-wipe transitions. Watch out: Adding gradients or moving several subjects at once falls apart; move only one hero at any moment. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 SVG 加 GSAP 做你的主题的扁平矢量讲解，纯色无渐变，五六种高饱和色，元素弹性入场，一镜到底。画面要点：SVG 加 GSAP、纯色大色块、五六色高饱和色板、overshoot 弹性缓动、预备冲出回弹、约 10% 挤压拉伸、stagger 两到四帧、形状擦除转场。注意：加渐变或几个主体同时动就散了，同一时刻只动一个主角。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#b88a3e`, `#3eb8a8`

## Pipeline · 管线

- 纯色多边形，无渐变、无纹理、无描边；六个高饱和色相：钴蓝天空、薄荷绿地面、明黄太阳和麦子、珊瑚红屋顶和陶罐、奶油白墙和云、深靛字和门窗。每个色相最多再配一档更深的平涂色做体积（远山、侧墙、罐子暗面、田垄）。
- 一镜到底：整条场景摆在世界坐标里，镜头 30 fps 连续推拉平移，天空层和远山层带视差（0.18、0.6），太阳不会挡住左上角时间签。
- 动作用 GSAP 的缓动公式：入场 back.out（带约 10% 挤压拉伸），退场 back.in，太阳 elastic.out，运镜 power3.inOut 和正弦缓动；stagger 两帧。
- 同一时刻只有一个主体做主动作，顺序是太阳 → 标题 → 田垄 → 麦子 → 房子 → 农人 → 陶罐 → 粮筐；云、麦浪、太阳光芒、树冠只做背景微动，保证画面每帧都在动。
- 开场第一帧就是满屏蓝天绿地和太阳，接在莫奈和像素游戏之后能马上亮起来。
- PIL 2 倍超采样画多边形，再 INTER_AREA 缩回 1920×1080，边缘干净。

## Beats · 节拍

0–0.9 s 太阳 elastic 弹出，标题 10,000 YEARS AGO… 逐字弹出（每字隔两帧）｜1.35–1.75 s 标题缩进左上角，黄色时间签横向擦出，盖到哪个字哪个字换深靛色｜1.7 s 底部字幕胶囊弹出 PEOPLE BEGAN TO FARM，镜头下移看田｜1.85–2.6 s 五条田垄依次从左擦出｜2.4–3.5 s 麦子一列列弹起，之后随风轻摆｜3.4–3.9 s 两间房子落地｜3.9–4.6 s 农人弹出招手｜3.7–5.9 s 镜头正弦缓动横移到粮仓｜5.1 s 字幕胶囊变宽，换成 …AND STORED THEIR GRAIN｜5.3–5.9 s 三只陶罐依次弹出｜5.7 s 粮筐落下｜6.0、6.7、7.4 s 粮筐预备回拉再倾倒，谷粒流进三只罐子，罐口粮堆鼓起，罐与罐之间粮筐弧线跳过去｜7.74–7.96 s 粮筐飞出画外，镜头慢推到 8 s。

## Pitfalls · 踩到的坑

- Adding gradients or moving several subjects at once falls apart; let only one hero move at a time; keep solid colors to five or six.
- 加了渐变或几个主体同时动就散；一次只让一个主角动；纯色控制在五六种以内。
- The automated check passes with an empty jump list; the largest frame difference (6.96, frame 156, 5.17 s) is the designed caption change during the pan.
- There is a single simple farmer figure with no facial animation; grain pouring is shown by heaps rising at the jar mouths, not by a visible level inside.
- The farmer and field on the left are cropped out during the pan; this is the cost of a one-take shot.
- The farmer skin tone is a lighter step of coral, strictly a seventh colour value.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
