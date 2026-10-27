# 25 · Editorial Paper Data Story · 纸面编辑式数据叙事 (`editorial-dataviz`)

## Status · 状态

**Upstream implementation, link only · 上游实做，只给链接.** LemoLab built it; we only link their code. Read their recipe, then build.

Engine: none in this skill. Upstream code and recipe: see the source column in INDEX.md.

## Prompt · 提示语

EN: Use Canvas to draw the real data of your topic on beige dot-grid paper, with red and blue pencils plotting point by point, handwritten notes pinned beside the data points, and the chart itself acting as the camera. Key visuals: beige dot-grid paper, real data drawn point by point, red and blue pencil strokes, handwritten notes pinned to data points, RdBu diverging color scale, chart as camera, chart type chosen by the data. Watch out: Do not turn it into a dashboard or slide deck; make one point at a time. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Canvas 在米色点阵纸上画你的主题的真实数据，红蓝铅笔逐点画出，手写批注钉在数据点旁，图表本身当镜头。画面要点：米色点阵纸、真实数据逐点绘制、红蓝铅笔笔触、手写批注钉在数据点、RdBu 发散色阶、图表即镜头、按数据选图型。注意：别做成仪表盘或幻灯片，一次只讲一个观点。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#cfcfcf`

## Pipeline · 管线

No engine yet. Build it from these visual keys, one pass per element:

beige dot-grid paper, real data drawn point by point, red and blue pencil strokes, handwritten notes pinned to data points, RdBu diverging color scale, chart as camera, chart type chosen by the data

米色点阵纸、真实数据逐点绘制、红蓝铅笔笔触、手写批注钉在数据点、RdBu 发散色阶、图表即镜头、按数据选图型

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- Turning it into a dashboard or slide deck loses the editorial feel; make one point at a time; use only changes in the chart itself as transitions.
- 做成仪表盘或幻灯片就丢了编辑感；一次只讲一个观点；转场只用图表本身的变化。

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
