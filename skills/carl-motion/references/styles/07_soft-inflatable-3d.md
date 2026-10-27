# 07 · Soft Inflatable 3D · 软体充气3D (`soft-inflatable-3d`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/soft-inflatable-3d/` (Blender + Python). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use Blender to make your topic as soft inflatable 3D: candy-colored soft rubber with subsurface scattering, squashing flat on landing then bouncing back fast, studio three-point lighting, shallow depth of field. Key visuals: SSS soft rubber, candy colors, AO plus HDRI three-point lighting, cloner arrays, soft-body collision squash, long-tail easing, shallow depth of field and motion blur, 24fps cinematic frame rate. Watch out: A slow rebound has no weight: accelerate on the fall, squash on contact, and bounce back fast. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Blender 做你的主题的软体充气 3D，糖果色软胶带次表面散射，落地压扁再快速弹起，棚拍三点光，浅景深。画面要点：SSS 软胶、糖果色、AO 加 HDRI 三点光、克隆阵列、软体碰撞挤压、长尾缓动、浅景深与运动模糊、24fps 电影帧率。注意：回弹一慢就没重量，下落加速、触地压扁、弹起要快。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#b83e6c`, `#b86c3e`

## Pipeline · 管线

No engine yet. Build it from these visual keys, one pass per element:

SSS soft rubber, candy colors, AO plus HDRI three-point lighting, cloner arrays, soft-body collision squash, long-tail easing, shallow depth of field and motion blur, 24fps cinematic frame rate

SSS 软胶、糖果色、AO 加 HDRI 三点光、克隆阵列、软体碰撞挤压、长尾缓动、浅景深与运动模糊、24fps 电影帧率

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- A slow rebound has no weight; a material without subsurface scattering looks like hard plastic; flat lighting looks like a web illustration.
- 回弹一慢就没重量；材质缺次表面散射会像硬塑料；光打平了就像网页插图。
- Full render verified: 240 frames from the current scene.py, ffprobe, full decode, per-frame motion statistics, spot frames against A, a contact strip, and frame-by-frame review of frames 120-124 and 182-184 (fast jump motion plus stretch plus motion blur, not dropped frames); physics numbers checked numerically; real-time playback not reviewed.
- Colours were changed to the complement of A at the maker's request, departing from the brief's "A and B keep the same main colours"; re-check A/B colour pairing when finalising the playing order.
- Mean frame difference is 1.99 (v1 0.73, A 6.49): A has many surging beads, while B's motion is concentrated in two letters, the cushion and the camera orbit.
- The letters start slightly out of frame at the top (they fall from above); the soft upper-middle background has a near-white highlight region.
- Cushion deformation is an analytic approximation (Gaussian kernel with distance delay), not a volume-preserving soft-body simulation; the cushion itself gets no motion blur.
- The letter-cushion contact is hidden by a slight 0.05 sink, so a faint overlap may be visible at extreme close range.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
