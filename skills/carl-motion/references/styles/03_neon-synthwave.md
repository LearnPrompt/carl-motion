# 03 · Neon Synthwave · 霓虹复古Synthwave (`neon-synthwave`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/neon-synthwave/` (Blender + Python). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Make your topic into an 80s Synthwave: a one-point-perspective neon grid rolling forward, a layered sunset on the horizon, double-layer glow on the lines, with scanlines and chromatic aberration on top. Key visuals: one-point-perspective grid scrolling, multi-layer gradient sunset, double-layer glow, scanlines and RGB color shift, chrome lettering, palm tree silhouettes, tape stutter at 15fps in selected spots. Watch out: Without the grid rolling there is no sense of speed; the camera must keep rushing forward. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：做你的主题的 80 年代 Synthwave，一点透视霓虹网格往前滚，地平线放分层落日，线条双层辉光，叠扫描线和色偏。画面要点：一点透视网格滚动、多层渐变落日、双层辉光、扫描线与 RGB 色偏、镀铬字、棕榈剪影、局部抽到 15fps 的磁带卡顿。注意：网格不滚就没速度感，镜头要一直往前冲。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#b83ea8`

## Pipeline · 管线

深紫夜空 + 星点、分段落日、青色线框山、洋红发光透视网格、棕榈剪影、路灯、镀铬多段渐变大标题 + 洋红侧边、双层辉光（Bloom）+ 星芒（Streaks）、轻扫描线与 1 px RGB 偏移。按需求不出现 VHS「PLAY ▶」与时间码等播放器 UI；不做 A 的汽车。

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- A grid that does not roll forward becomes a static wallpaper; colors outside magenta, cyan and orange look muddy; stacking too many glow layers blurs everything together.
- 网格不往前滚就成了静态壁纸；颜色跑出品红、青、橙会发脏；辉光叠太多层会糊成一片。
- Full render verified: 240 frames from the current scene.py, ffprobe spec, full decode, per-frame motion statistics, spot frames against A, a contact strip and a full-resolution consecutive-frame check; real-time playback was not reviewed.
- Mean frame difference is 17.5, above A at 9.65 (target at least 7), because the high-contrast grid surges forward all the time; lowering SPEED from 30 to about 18 gives a gentler look.
- The title is parented to the camera, so it stays screen-stable during road shake and banking; chosen for 9:16 readability.
- The handwritten neon script second line of A is not reproduced, and A's car is not made (per the brief).
- A warm sunset reflection sits on the ground under the boombox; it is an intentional wet-ground reflection.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
