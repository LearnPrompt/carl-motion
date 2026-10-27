# 28 · Risograph Print · Risograph孔版套印 (`risograph`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/risograph/` (Python (NumPy + OpenCV + Pillow)). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: verified.

## Prompt · 提示语

EN: Use code to simulate risograph-style stencil printing of your topic: two or three spot colors multiplied together, with halftone dots and slight misregistration, and color blocks with no outlines. Key visuals: two or three spot ink colors, multiply to produce a third color, misregistration, halftone dots, grain and pinholes, warm white paper, outline-free color blocks, characters at 12fps and camera at 24fps. Watch out: Vector art plus noise does not count; every color must come from separated overprinted plates. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用代码模拟孔版印刷做你的主题，两三种专色正片叠底，带半调网点和轻微套印错位，色块不描边。画面要点：两三种 spot ink 专色、multiply 叠出第三色、套印错位、halftone 网点、颗粒针孔、暖白纸、无轮廓色块、角色 12fps 镜头 24fps。注意：矢量图加噪点不算，每块颜色都得来自分版叠印。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#a8b83e`, `#b83e6c`

## Pipeline · 管线

- 三块印版分开画：黄、荧光粉、蓝，每块是 0–1 的网调图；半调网点网角分别 0°、75°、15°，满版处是实地。
- 合成按油墨正片叠底：黄压蓝出绿，粉压蓝出紫，粉压黄出橙，和 A 的配色同源。
- 套印错位：每块版各自偏移，字砸下时粉版做衰减震荡，6.5 s 全版错开再回正。
- 元素按 12 fps 走，镜头推近按 30 fps 连续；纸纤维、墨量不匀、针孔按拍刷新。

## Beats · 节拍

0.15 s 起 MAKE IT 逐字砸下（蓝实地，粉版回声带套印错位，0.5 s 后淡出）｜0.9 s 起九棵粉色树依次弹出｜1.8–7.6 s 骑车人从左到右穿过公园，轮辐和踏板跟着转，黄围巾飘｜3.35 s 起 MOVE IT 逐字砸下（粉实地，蓝版回声）｜5.6 s 底栏出现 MAKE IT MOVE｜6.5 s 三块版整体错开一次再回正｜全程花瓣飘落，镜头推近 3%。

## Pitfalls · 踩到的坑

- Vector art plus noise does not count, every color must come from separated overprinted plates; without misregistration it does not look right; the screen angles of the three plates must be offset.
- 矢量图加噪点不算，每块颜色都要来自分版叠印；没有套印错位就不像；三块版的网角要错开。
- The 6.5 s whole-plate misregistration kick and every title slam show up as jump frames in deliver.py: by design. Their frame numbers move when you change the beats.
- The cyclist is an assembly of geometric pieces, without the street buildings that A has.

## Field notes · 实测记录

- 2026-10-27 · coffee-shop opening (NOW OPEN / COME IN): jump 124 (last letter slam), 196/199 (6.5s whole-plate misreg), palette drift vs card #a8b83e/#b83e6c (card palette is green/pink, plates are Y/P/B); head skin invisible on yellow ground · knocked out Y ground behind heads, kept flags as designed
