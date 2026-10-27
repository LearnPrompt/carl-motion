# 25 · Editorial Paper Data Story · 纸面编辑式数据叙事

[All styles](README.md) · [← Product Exploded View](exploded-view.md) · [Glassmorphism UI →](glassmorphism-ui.md)

<img src="../../assets/previews/editorial-dataviz.webp" width="100%" alt="Editorial Paper Data Story">

<sub>Preview: layer A by LemoLab · lemo-opuscar, CC BY 4.0. 预览是 LemoLab · lemo-opuscar 的 A，CC BY 4.0。</sub>

**Status 状态:** Upstream implementation, link only · 上游实做，只给链接

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use Canvas to draw the real data of your topic on beige dot-grid paper, with red and blue pencils plotting point by point, handwritten notes pinned beside the data points, and the chart itself acting as the camera. Key visuals: beige dot-grid paper, real data drawn point by point, red and blue pencil strokes, handwritten notes pinned to data points, RdBu diverging color scale, chart as camera, chart type chosen by the data. Watch out: Do not turn it into a dashboard or slide deck; make one point at a time. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 Canvas 在米色点阵纸上画你的主题的真实数据，红蓝铅笔逐点画出，手写批注钉在数据点旁，图表本身当镜头。画面要点：米色点阵纸、真实数据逐点绘制、红蓝铅笔笔触、手写批注钉在数据点、RdBu 发散色阶、图表即镜头、按数据选图型。注意：别做成仪表盘或幻灯片，一次只讲一个观点。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | A colored pencil draws a line chart on off-white paper, marking years and birth events. | 米白纸上彩铅画出一条折线，标出年份和出生事件。 |
| B | Red dots spread across an old map, the printed number 20,000,000+ slams in, and a BANNED stamp lands. | 旧地图上红点扩散，20,000,000+ 印刷数字砸出，盖上 BANNED 印章。 |

## Where it usually breaks · 容易失败的点

Turning it into a dashboard or slide deck loses the editorial feel; make one point at a time; use only changes in the chart itself as transitions.

做成仪表盘或幻灯片就丢了编辑感；一次只讲一个观点；转场只用图表本身的变化。

## Key visuals · 画面要点

beige dot-grid paper, real data drawn point by point, red and blue pencil strokes, handwritten notes pinned to data points, RdBu diverging color scale, chart as camera, chart type chosen by the data

米色点阵纸、真实数据逐点绘制、红蓝铅笔笔触、手写批注钉在数据点、RdBu 发散色阶、图表即镜头、按数据选图型

Palette 主色：`#cfcfcf`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 铅笔温度曲线与冷暖条 | [LemoLab · lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/dataviz) | prompts/code MIT, demo video CC BY 4.0 |
| B | 印刷机传播：地图、数量与报纸叙事 | [X post](https://x.com/maxescu/status/2104898184442962277) | link only |

## Reproduce · 复现

No source in this repo yet. The prompt above is enough to build it from scratch.

本仓库暂时没有这个画风的源码，直接用上面的提示语就能从零做出来。
