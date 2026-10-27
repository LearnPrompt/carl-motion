# 17 · Claymation Stop-motion · 黏土定格 (`claymation`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/claymation/` (Blender + Python). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use Blender to make a clay stop-motion animation of your topic, with fingerprints and dents on the surface, a pose change every two frames played at 12 fps, and soft studio lighting with shallow depth of field. Key visuals: clay material with fingerprints and dents, on twos 12fps, slight shape change boil on every beat, soft studio light, shallow-depth macro, handmade jump-cut rhythm. Watch out: Smooth motion looks like CG; drop frames on purpose and change the shape slightly on every beat. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Blender 做你的主题的黏土定格动画，表面留指纹和压痕，两帧换一个姿势按 12 帧播放，柔光棚拍浅景深。画面要点：黏土材质指纹压痕、on twos 12fps、每拍形状微变 boil、柔光棚拍、浅景深微距、手工跳切节奏。注意：动作一顺滑就像 CG，要故意抽帧，形状每一拍都微微变。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#b8a83e`

## Pipeline · 管线

- 材质：全部为程序化黏土材质——哑光（roughness≈0.62）、少量次表面、细颗粒噪声凹凸、平滑 Voronoi 拇指压痕、局部斑块化的指纹环纹；泥团/花盆网格另有真实几何压痕（7 个拇指坑）与手工不对称（半径正弦扰动 + Perlin 噪声），形变时压痕跟着泥料走。
- 体积：泥团→泥饼→泥柱→花盆四个关键截面的体积按估算保持在 25–30 cm³ 区间（球 28.7 / 饼 ≈25 / 柱 ≈29.7 / 盆壁 ≈26.5）。
- 场景：真实微缩尺度（厘米建模），40 mm 镜头 f/11 物理景深，黄色无缝背景（色值按 A 实际像素校准，A ≈ RGB 218,190,40；B 背景实测 213–238,179–201,32–62），柔光大面光 + 补光 + 轮廓光。
- 定格节奏：角色、泥料、芽、叶全部按 12 fps 取样（30 fps 输出中 2/3 帧交替保持）；每个 pose 有微小位置抖动与灯光 ±2% 闪烁；相机按 30 fps 连续缓推（不步进，避免抖动）。无长冻结（见 QA）。

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- Motion that is too smooth looks like 3D animation; drop frames to get a stop-motion feel; a material without fingerprints and dents is just plastic; the light should look like a real tabletop shoot.
- 动作太顺就像 3D 动画，要抽帧做出定格感；材质没有指纹和压痕就是塑料；光要像桌面实拍。
- Characters are rounded metaball shapes; the hand-pinched feel comes mostly from bump maps and geometric thumbprints, so detail and lighting realism are a little below a real clay animation.
- Background props (blue watering can, red mushroom) are simplified; the can silhouette is quite abstract.
- Paw-to-clay contact follows positions only, with no physical deformation (fingers do not sink into the clay).

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
