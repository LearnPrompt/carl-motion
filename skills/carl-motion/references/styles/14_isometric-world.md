# 14 · Isometric 2.5D World · 等轴2.5D世界 (`isometric-world`)

## Status · 状态

**Upstream implementation, link only · 上游实做，只给链接.** LemoLab built it; we only link their code. Read their recipe, then build.

Engine: none in this skill. Upstream code and recipe: see the source column in INDEX.md.

## Prompt · 提示语

EN: Use Canvas or a Three.js orthographic camera to turn your topic into an isometric miniature world, with flat three-tone shading on every face and small icons with leader lines labeling the data. Key visuals: true isometric 30 degrees, flat three-tone shading per face, floating base with cross-section, Isotype icon counting, label leader lines, cutaway, buildings growing with overshoot, camera following a route. Watch out: Keep a fixed 30 degree isometric; adding perspective or outlines turns it into low-poly 3D. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Canvas 或 Three.js 正交相机把你的主题做成等轴测微缩世界，每个面三色调平涂，用小图标和引线标数据。画面要点：true isometric 30 度、每面三色调平涂、悬浮底座带剖面、Isotype 图标计数、标签引线、剖开 cutaway、建筑生长带过冲、沿路线带镜头。注意：固定 30 度等轴，一加透视或描边就变成低多边形 3D。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#6cb83e`, `#b84e3e`

## Pipeline · 管线

No engine yet. Build it from these visual keys, one pass per element:

true isometric 30 degrees, flat three-tone shading per face, floating base with cross-section, Isotype icon counting, label leader lines, cutaway, buildings growing with overshoot, camera following a route

true isometric 30 度、每面三色调平涂、悬浮底座带剖面、Isotype 图标计数、标签引线、剖开 cutaway、建筑生长带过冲、沿路线带镜头

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- Slipping in perspective turns it into low-poly 3D; use a fixed 30 degree projection with no outlines; a camera that spins around breaks the isometric feel.
- 夹带透视就变成低多边形 3D；固定 30 度投影、不描边；镜头乱转会破坏等轴感。

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
