# 23 · Ancient Egyptian Mural · 古埃及壁画 (`egyptian-mural`)

## Status · 状态

**Implemented on an upstream library · 基于上游库实做.** Our scene code on the huashu-art-motion painting library (MIT). Start from it.

Engine: `scenes/huashu-portraits/` (Node + Canvas / headless Chrome). Run `./render.sh <work_dir> <s22_egypt>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use Canvas 2D to paint your topic as an ancient Egyptian tomb mural: figures with profile faces and frontal eyes, register bands composed with hieroglyph columns, flat ochre and lapis fills with black outlines. Key visuals: profile-face frontal-eye convention, column-divided horizontal registers, hieroglyph columns, flat fills of ochre, lapis, peacock green and earth yellow, black outlines, small hands at the ends of sun rays, lime plaster wall texture. Watch out: A mural is flat, so add no perspective or shadows, and animate the river and light so it is not too static. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Canvas 2D 把你的主题画成古埃及墓室壁画，人物侧脸正眼，分栏横带构图配象形文字栏，赭石青金平涂加黑描边。画面要点：侧脸正眼程式、分栏横带 register、象形文字栏、赭石青金孔雀绿土黄平涂、黑色描边、太阳光线末端小手、墙面石灰质感。注意：壁画是平的，别加透视和阴影，再让河水和光线动起来免得太静。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#b88a3e`

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

- Adding perspective and shadows no longer looks like a mural; figures must use the canonical pose with frontal torso and profile head; use only mineral colors such as ochre red, earth yellow and blue-green.
- 加透视和阴影就不像壁画；人物要正身侧脸的规范姿势；颜色只用赭红、土黄、青绿这类矿物色。
- In the Egyptian version Carl wears a white linen kilt; only the T-shirt, hairstyle, glasses and smile are kept.
- In the Monet version the brush-stroke density on Carl is lower than in the background; the tree-shadow light spots are kept faint so they do not read as dirt.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
