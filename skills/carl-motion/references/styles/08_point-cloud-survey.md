# 08 · Point-cloud Survey · 点云测绘／剥层 (`point-cloud-survey`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/point-cloud-survey/` (Blender + Python). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4 --crf 19`. Deterministic: not verified.

## Prompt · 提示语

EN: Use Three.js to turn your location into a laser point cloud: real measured points floating on black, a scan plane passes and the points solidify into solid terrain, then peel apart layer by layer by ground, vegetation and buildings. Key visuals: real airborne lidar points, near-black background, scan line or section plane advancing, points condense into a solid lit at grazing angle, layers peeled by ground, vegetation and building classes, hairline measurement readouts, one designed camera move. Watch out: From afar a point cloud looks like a flat carpet; the camera must fly low and close. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Three.js 把你的地点做成激光点云，黑底悬浮真实测量点，扫描面经过后凝成实体地形，再按地面植被建筑逐层剥开。画面要点：真实机载激光点、近黑底、扫描线或剖切面推进、点凝成掠射光实体、按地面植被建筑分类剥层、发丝线测量读数、一条设计好的运镜。注意：远看点云像平地毯，镜头要贴低穿过去。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#777777`

## Pipeline · 管线

No engine yet. Build it from these visual keys, one pass per element:

real airborne lidar points, near-black background, scan line or section plane advancing, points condense into a solid lit at grazing angle, layers peeled by ground, vegetation and building classes, hairline measurement readouts, one designed camera move

真实机载激光点、近黑底、扫描线或剖切面推进、点凝成掠射光实体、按地面植被建筑分类剥层、发丝线测量读数、一条设计好的运镜

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- From afar a point cloud looks like a flat carpet, so the camera must fly low and close; points that are too sparse cannot read as terrain; peel the layers by ground, vegetation and building class.
- 远看点云像平铺地毯，镜头要贴低穿过去；点太稀读不出地形；剥层要按地面、植被、建筑分类。
- Points are EEVEE point-cloud sprites, not strict soft discs; a slight squareness is visible up close.
- Terrain micro-relief is procedural noise; it resembles hillshade of a real DEM but lacks its randomness.
- The closing shot is a little farther away than in A (A ends close to the ground); the subject is kept mid-frame for 9:16 readability.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
