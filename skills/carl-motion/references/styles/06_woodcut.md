# 06 · Black-and-white Woodcut · 黑白木刻版画 (`woodcut`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/woodcut/` (Python (NumPy + OpenCV + Pillow)). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Turn your topic into a black-and-white woodcut print: a solid black block, highlights are white lines cut away by the knife, the image is carved out one cut at a time, with at most one red. Key visuals: white lines cut into a black block, light is carved out, image appears cut by cut with no fade-in, bold cuts in front and fine lines behind, cut lines follow the form, at most one color, paper margin left white, mirrored-lettering print-out transition. Watch out: Hatching on every surface looks like fur and rain; cut only three to six strokes on the lit edge. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：把你的主题做成黑白木刻版画，整块黑版，亮部是刀刻掉的白线，画面一刀一刀刻出来，最多留一种红。画面要点：黑版白刻、光是刻出来的、画面逐刀刻出不淡入、粗刀在前细线在后、刀线顺形体走、最多一种颜色、纸边留白、反字印出转场。注意：每个面都排线会像毛和雨，只在受光边刻三到六刀。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#565656`

## Pipeline · 管线

- 黑是木、白是刀刻掉的部分：天空、海、云、帆、船板全部由独立刀痕组成（钝入口、尖出口，刀与刀间留木）。
- 刀痕方向跟形体：海面沿浪形，云沿等值轮廓（只刻受光一侧），帆沿布纹，船板沿船形；宽度随明度（亮处几乎连成白）。远细密、近粗疏。
- 主体黑块 + 白色刀晕分离；帆为亮面，外沿留黑保持线。
- 印刷：纸边固定不动，版边毛糙；墨色 ±6% 不均 + 木纹条带 + 没吃墨的小白点 + 刀口毛刺；纸墨纹理每 2 帧轻微重印（纸墨微动）。
- 船、帆、绳按 twos（12fps）更新；浪、光、镜头按 ones。只用黑墨与纸白，无彩色版。

## Beats · 节拍

0–1 s 船、桅、海面黑白关系建立｜1.0–3.5 s 帆升起（12fps 姿态更新，顶端回弹）｜2.5–3.5 s 主缆收紧 + 绳结收紧回弹｜3.6–6.6 s 船摇幅加大，云分开，光芒伸长｜5.85–7.7 s 船头转向，镜头随之微移｜全程浪、云、纸墨微动。字幕 0.6 s 起印在纸边：After the storm, the sail goes up again. / 风暴过后，帆重新升起。

## Pitfalls · 踩到的坑

- Hatching on every surface looks like fur and rain, so cut only three to six strokes on the lit edge; if the image fades in it no longer looks carved; keep at most one color.
- 每个面都排线会像毛和雨，只在受光边刻三到六刀；画面用淡入出现就不像刻的；颜色最多留一种。
- The style grammar matches A, but A has figures and close-up carving hands while B is landscape plus boat, so the information density is slightly lower.
- The storm cloud mass is small, leaving a large solid-black area at the top left of the sky.
- The boat turn is a yaw of the 3D hull projection; midway the sail is nearly edge-on to the camera and looks narrow for about 0.3 s.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
