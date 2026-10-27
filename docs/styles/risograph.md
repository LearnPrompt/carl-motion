# 28 · Risograph Print · Risograph孔版套印

[All styles](README.md) · [← Brick Toy](brick-toy.md) · [Sci-fi Scan HUD →](scifi-hud.md)

<img src="../../assets/previews/risograph.webp" width="100%" alt="Risograph Print">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use code to simulate risograph-style stencil printing of your topic: two or three spot colors multiplied together, with halftone dots and slight misregistration, and color blocks with no outlines. Key visuals: two or three spot ink colors, multiply to produce a third color, misregistration, halftone dots, grain and pinholes, warm white paper, outline-free color blocks, characters at 12fps and camera at 24fps. Watch out: Vector art plus noise does not count; every color must come from separated overprinted plates. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用代码模拟孔版印刷做你的主题，两三种专色正片叠底，带半调网点和轻微套印错位，色块不描边。画面要点：两三种 spot ink 专色、multiply 叠出第三色、套印错位、halftone 网点、颗粒针孔、暖白纸、无轮廓色块、角色 12fps 镜头 24fps。注意：矢量图加噪点不算，每块颜色都得来自分版叠印。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | A street printed in yellow, blue and pink halftone dots, a cyclist rides through a park and pigeons take off. | 黄、蓝、粉三色网点印出的街道，骑车人穿过公园，鸽子飞起。 |
| B | Our render: big MAKE IT and MOVE IT type slams down with misregistration, and a cyclist rides through a park. | 我们补做。MAKE IT、MOVE IT 大字砸下带套印错位，骑车人穿过公园。 |

## Where it usually breaks · 容易失败的点

Vector art plus noise does not count, every color must come from separated overprinted plates; without misregistration it does not look right; the screen angles of the three plates must be offset.

矢量图加噪点不算，每块颜色都要来自分版叠印；没有套印错位就不像；三块版的网角要错开。

## Key visuals · 画面要点

two or three spot ink colors, multiply to produce a third color, misregistration, halftone dots, grain and pinholes, warm white paper, outline-free color blocks, characters at 12fps and camera at 24fps

两三种 spot ink 专色、multiply 叠出第三色、套印错位、halftone 网点、颗粒针孔、暖白纸、无轮廓色块、角色 12fps 镜头 24fps

Palette 主色：`#a8b83e` `#b83e6c`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 错版街道与公园骑行 | [LemoLab · lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/risograph) | prompts/code MIT, demo video CC BY 4.0 |
| B | carl-motion | [this repo](../../templates/scenes/risograph) · story idea: [github.com](https://github.com/Vincentwei1021/video-shotcraft/blob/main/demos/effects/riso-print-hits/RisoMisregistrationHit.tsx) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`templates/scenes/risograph`](../../templates/scenes/risograph) (Python (NumPy + OpenCV + Pillow)). Its README has the exact render command.

渲染 B 的完整源码在 [`templates/scenes/risograph`](../../templates/scenes/risograph)（Python (NumPy + OpenCV + Pillow)），渲染命令写在它的 README 里。
