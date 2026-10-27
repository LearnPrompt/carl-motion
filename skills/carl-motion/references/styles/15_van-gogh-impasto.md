# 15 · Van Gogh Impasto · 梵高厚涂油画 (`van-gogh-impasto`)

## Status · 状态

**Implemented on an upstream library · 基于上游库实做.** Our scene code on the huashu-art-motion painting library (MIT). Start from it.

Engine: `scenes/huashu-portraits/` (Node + Canvas / headless Chrome). Run `./render.sh <work_dir> <s23_wheat>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use Canvas 2D to draw your topic: lay down flat base colors first, then fill short thick impasto strokes following a flow field, a dozen-plus hues per region, with the strokes changing eight times per second. Key visuals: flat-color underpainting plus flow-field strokes, walls vertical and floor along perspective, starry sky swirling around vortexes, region palettes of a dozen-plus hues, short thick impasto, dark blue outlines, 8fps stroke boil, small objects on their own layers. Watch out: Lay strokes in three separate passes for wall, floor and figure; one parameter set for the whole image blurs into a carpet. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Canvas 2D 画你的主题，先平涂底色，再顺着流场铺短粗厚涂笔触，每块区域十几种色相，笔触每秒换八次。画面要点：平涂底稿加流场笔触、墙竖地沿透视星空绕漩涡、区域色板十几种色相、短粗厚涂、深蓝描边、8fps 笔触沸腾、小物件单独成层。注意：墙、地、人物分三遍铺笔触，一套参数跑全图会糊成地毯。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#3e6cb8`, `#b84e3e`

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

- Changing only colors without laying strokes is just an ordinary illustration; wall, floor and figure need separate layers with their own strokes; strokes shaking across the whole screen cause dizziness.
- 只换颜色不铺笔触就是普通插画；墙、地、人物要分层分别铺笔触；全屏笔触一起抖会晕。
- In the Egyptian version Carl wears a white linen kilt; only the T-shirt, hairstyle, glasses and smile are kept.
- In the Monet version the brush-stroke density on Carl is lower than in the background; the tree-shadow light spots are kept faint so they do not read as dirt.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
