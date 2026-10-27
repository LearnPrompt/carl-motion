# 20 · Impressionist Oil (Monet) · 印象派油画／莫奈 (`monet-impressionist`)

## Status · 状态

**Implemented on an upstream library · 基于上游库实做.** Our scene code on the huashu-art-motion painting library (MIT). Start from it.

Engine: `scenes/huashu-portraits/` (Node + Canvas / headless Chrome). Run `./render.sh <work_dir> <s24_bridge>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use Canvas 2D to draw your topic with no outlines, short horizontal strokes for the water, warm yellow layered on the lit side and pale purple on the shadow side, with light flecks that flicker. Key visuals: impressionist with no outlines, horizontal water strokes, colored shadows with warm yellow in light and pale purple in shade, bright short-stroke light flecks trembling, 6fps local stroke boil, water lily and Japanese bridge motifs. Watch out: Boiling across the whole screen turns into full-screen noise; keep large areas like the floor and bridge still. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Canvas 2D 画你的主题，不勾边，水面用横向短笔触，受光侧叠暖黄、背光侧叠淡紫，光斑一闪一闪。画面要点：印象派不勾边、横向水面笔触、受光暖黄背光淡紫的色彩阴影、亮色短笔光斑颤动、6fps 局部笔触沸腾、睡莲日本桥母题。注意：全屏一起沸腾会变满屏噪点，地板和桥这类大面保持不动。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#b86c3e`, `#3e6cb8`

## Pipeline · 管线

- **古埃及**：字形库、四色彩块边框、壁画表面（斑驳 multiply、发丝裂纹、颗粒）、阿顿小手、圣甲虫画法和铭文写出的动画，直接取自 `upstream/02_egypt.js`（MIT），构图改成上下两栏加河带。
- **梵高、莫奈**：先平涂底稿，再加分区流场笔触与区域色板。角色先平涂，再用 source-atop 补细笔触，最后补五官。莫奈的笔触以 6 fps 重绘（boil）。

## Beats · 节拍

| 场景 | 内容 | 0–2 s | 2–5 s | 5–8 s |
|---|---|---|---|---|
| s22_egypt 古埃及 | 卡尔按埃及程式侧身迈步（侧脸配正面眼、正面双肩、侧身腿，方框眼镜按正面眼的程式画），圣甲虫推红日盘，河带展开 | 河带从左向右展开，铭文逐个写出，卡尔站定 | 卡尔侧步走过下栏，圣甲虫把日盘推到地平线山口 | 日盘落进山口、升起成阿顿，光线末端的小手张合，一只手把安卡递到卡尔面前，卡尔举起双手致敬 |
| s23_wheat 梵高 | 卡尔走过旋涡星空下的麦田，麦浪随风起伏，柏树像火焰 | 进画 | 走过麦田，麦浪分开 | 停步回头看 |
| s24_bridge 莫奈 | 卡尔走上睡莲池上的绿色拱桥，树影和碎光斑掠过衣服 | 上桥 | 过桥顶 | 停步，手扶栏杆，低头看水，涟漪变大 |

## Pitfalls · 踩到的坑

- Strokes shaking across the whole screen cause dizziness, so animate only the water and light flecks; strokes that are too large blur the figures; juxtapose complementary colors and do not mix them into gray.
- 全屏笔触一起抖会晕，只让水面和光斑动；笔触太大人物会糊掉；颜色要补色并置，别调成灰。
- In the Egyptian version Carl wears a white linen kilt; only the T-shirt, hairstyle, glasses and smile are kept.
- In the Monet version the brush-stroke density on Carl is lower than in the background; the tree-shadow light spots are kept faint so they do not read as dirt.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
