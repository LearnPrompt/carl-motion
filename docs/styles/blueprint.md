# 09 · Blueprint Drawing · 蓝图工程制图

[All styles](README.md) · [← Point-cloud Survey](point-cloud-survey.md) · [Die-cut Sticker Explainer →](sticker-explainer.md)

<img src="../../assets/previews/blueprint.webp" width="100%" alt="Blueprint Drawing">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use Canvas to draw your topic on Prussian-blue blueprint paper in thin white lines, in drawing order, with dimension lines, numbered balloons and a drawing frame. Key visuals: cyanotype blueprint paper, thin white engineering lines, layer-by-layer drawing order, dimension lines and leader lines, numbered balloons, title block frame, section hatching, pan and zoom of the whole sheet. Watch out: Keep it a 2D line drawing in blue and white only; once it becomes 3D or a glowing wireframe it no longer fits. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 Canvas 在普鲁士蓝晒图纸上，用白色细线按绘图顺序画出你的主题，配尺寸线、编号气泡和图框。画面要点：cyanotype 蓝晒纸、白色工程细线、逐层绘制顺序、尺寸线与引线、编号气泡、title block 图框、剖面线、整张图纸平移缩放。注意：只用蓝白两色的 2D 线稿，一做成 3D 或发光线框就不像了。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | On Prussian-blue paper, white lines draw a machine and a crane in drawing order, with numbered balloons, dimension lines and a drawing frame. | 普鲁士蓝图纸上，白线按绘图顺序画出机器和吊车，带编号气泡、尺寸线和图框。 |
| B | Our render: an English explainer version. White lines draw FIG. 1 granary, FIG. 2 mouse, FIG. 3 wildcat in figure order, with dimension lines, numbered balloons and an enlarged detail view, and the drawing frame is added at the end. | 我们做的英文讲解版。白线按图号依次画出 FIG. 1 粮仓、FIG. 2 老鼠、FIG. 3 野猫，带尺寸线、编号气泡和放大详图，最后补上图框。 |

## Where it usually breaks · 容易失败的点

Once it becomes 3D or a glowing wireframe it no longer fits; use a 2D line drawing in blue and white only; if all lines appear at once the sense of drawing is lost.

做成 3D 或发光线框就不像了；只用蓝白两色的 2D 线稿；线条一次全出现会丢掉绘制感。

## Key visuals · 画面要点

cyanotype blueprint paper, thin white engineering lines, layer-by-layer drawing order, dimension lines and leader lines, numbered balloons, title block frame, section hatching, pan and zoom of the whole sheet

cyanotype 蓝晒纸、白色工程细线、逐层绘制顺序、尺寸线与引线、编号气泡、title block 图框、剖面线、整张图纸平移缩放

Palette 主色：`#3e6cb8`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 捕云机器专利图 | [LemoLab · lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/blueprint) | prompts/code MIT, demo video CC BY 4.0 |
| B | carl-motion | [this repo](../../templates/scenes/blueprint) · story idea: [en.yasue.org](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`templates/scenes/blueprint`](../../templates/scenes/blueprint) (Python (NumPy + OpenCV + Pillow)). Its README has the exact render command.

渲染 B 的完整源码在 [`templates/scenes/blueprint`](../../templates/scenes/blueprint)（Python (NumPy + OpenCV + Pillow)），渲染命令写在它的 README 里。
