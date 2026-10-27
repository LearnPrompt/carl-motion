# 14 · Isometric 2.5D World · 等轴2.5D世界

[All styles](README.md) · [← ASCII Character Visuals](ascii-crt.md) · [Van Gogh Impasto →](van-gogh-impasto.md)

<img src="../../assets/previews/isometric-world.webp" width="100%" alt="Isometric 2.5D World">

<sub>Preview: layer A by LemoLab · lemo-opuscar, CC BY 4.0. 预览是 LemoLab · lemo-opuscar 的 A，CC BY 4.0。</sub>

**Status 状态:** Upstream implementation, link only · 上游实做，只给链接

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use Canvas or a Three.js orthographic camera to turn your topic into an isometric miniature world, with flat three-tone shading on every face and small icons with leader lines labeling the data. Key visuals: true isometric 30 degrees, flat three-tone shading per face, floating base with cross-section, Isotype icon counting, label leader lines, cutaway, buildings growing with overshoot, camera following a route. Watch out: Keep a fixed 30 degree isometric; adding perspective or outlines turns it into low-poly 3D. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 Canvas 或 Three.js 正交相机把你的主题做成等轴测微缩世界，每个面三色调平涂，用小图标和引线标数据。画面要点：true isometric 30 度、每面三色调平涂、悬浮底座带剖面、Isotype 图标计数、标签引线、剖开 cutaway、建筑生长带过冲、沿路线带镜头。注意：固定 30 度等轴，一加透视或描边就变成低多边形 3D。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | An isometric hillside coffee plantation, small trucks hauling cargo, coffee bean cross-section round badges, with English subtitles. | 等轴视角的山坡咖啡园，小卡车运货，咖啡豆剖面圆标，英文字幕。 |
| B | A pale lavender-white isometric city rises tile by tile, the central tower lights up, and the city name title is slammed out at the end. | 淡紫白的等轴城市一格格升起，中央高塔亮起，最后打出城市名标题。 |

## Where it usually breaks · 容易失败的点

Slipping in perspective turns it into low-poly 3D; use a fixed 30 degree projection with no outlines; a camera that spins around breaks the isometric feel.

夹带透视就变成低多边形 3D；固定 30 度投影、不描边；镜头乱转会破坏等轴感。

## Key visuals · 画面要点

true isometric 30 degrees, flat three-tone shading per face, floating base with cross-section, Isotype icon counting, label leader lines, cutaway, buildings growing with overshoot, camera following a route

true isometric 30 度、每面三色调平涂、悬浮底座带剖面、Isotype 图标计数、标签引线、剖开 cutaway、建筑生长带过冲、沿路线带镜头

Palette 主色：`#6cb83e` `#b84e3e`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 咖啡从农田到咖啡机的等轴旅程 | [LemoLab · lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/iso-infographic) | prompts/code MIT, demo video CC BY 4.0 |
| B | 等轴城市从空地长出 | [Vincentwei1021 · mg-styles-15](https://vincentwei1021.github.io/mg-styles-15/?lang=zh#03-isometric) | prompts/code MIT; demo video not redistributed |

## Reproduce · 复现

No source in this repo yet. The prompt above is enough to build it from scratch.

本仓库暂时没有这个画风的源码，直接用上面的提示语就能从零做出来。
