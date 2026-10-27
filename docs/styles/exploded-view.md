# 24 · Product Exploded View · 产品爆炸拆解

[All styles](README.md) · [← Ancient Egyptian Mural](egyptian-mural.md) · [Editorial Paper Data Story →](editorial-dataviz.md)

<img src="../../assets/previews/exploded-view.webp" width="100%" alt="Product Exploded View">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

**Status 状态:** Implemented, one scene · 单场景实做

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use Blender to make an exploded teardown of your product: parts lift evenly spaced in layers along one axis, studio key light plus a cool rim light, leader lines labeling real specs, and everything closes back into one piece at the end. Key visuals: real CAD/PCB/BOM, evenly spaced layers along one axis, PBR studio key light plus cool rim light, HDRI reflections, leader lines and dimension lines, camera moving between layers, closing back together at the end. Watch out: Annotate only numbers that appear in the drawings; never estimate dimensions. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 Blender 做你的产品爆炸拆解，零件沿一根轴等距分层抬起，棚拍主光加冷色轮廓光，引线标真实参数，最后合回一体。画面要点：真实 CAD／PCB／BOM、沿一轴等距分层、PBR 棚拍主光加冷轮廓光、HDRI 反射、引线与尺寸线、镜头在层间穿行、最后合拢。注意：标注只写图纸里有的数，尺寸不许估。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | An exploded teardown of a PCB, with the RP2040 chip and components rising layer by layer, with Chinese and English subtitles. | PCB 电路板爆炸拆解，RP2040 芯片和元件一层层升起，中英字幕。 |
| B | Our render: The camera is taken apart layer by layer, the aperture blades open and close, with Chinese and English subtitles. | 我们做的。相机一层层拆开，光圈叶片收放，中英字幕。 |

## Where it usually breaks · 容易失败的点

Made-up model numbers and figures give it away; parts must separate along the assembly axis; materials must distinguish metal, plastic and PCB.

型号和数字瞎编会露馅；零件要沿装配轴拆开；材质要分出金属、塑料和 PCB。

## Key visuals · 画面要点

real CAD/PCB/BOM, evenly spaced layers along one axis, PBR studio key light plus cool rim light, HDRI reflections, leader lines and dimension lines, camera moving between layers, closing back together at the end

真实 CAD／PCB／BOM、沿一轴等距分层、PBR 棚拍主光加冷轮廓光、HDRI 反射、引线与尺寸线、镜头在层间穿行、最后合拢

Palette 主色：`#4eb83e` `#b88a3e`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 产品拆解：21 Keys, Opened | [LemoLab · lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/teardown) | prompts/code MIT, demo video CC BY 4.0 |
| B | carl-motion | [this repo](../../skills/carl-motion/scenes/exploded-view) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`skills/carl-motion/scenes/exploded-view`](../../skills/carl-motion/scenes/exploded-view) (Blender + Python). Check dependencies first with `python3 skills/carl-motion/scripts/doctor.py exploded-view`.

```bash
cd skills/carl-motion/scenes/exploded-view
./render.sh /tmp/exploded-view
python3 ../../scripts/deliver.py --frames /tmp/exploded-view/frames --out exploded-view.mp4
```

渲染 B 的完整源码在 [`skills/carl-motion/scenes/exploded-view`](../../skills/carl-motion/scenes/exploded-view)（Blender + Python），渲染命令写在它的 README 里。
