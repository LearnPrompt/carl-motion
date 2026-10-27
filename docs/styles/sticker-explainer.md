# 10 · Die-cut Sticker Explainer · 贴纸科普

[All styles](README.md) · [← Blueprint Drawing](blueprint.md) · [Feature-film 3D Character →](feature-3d-character.md)

<img src="../../assets/previews/sticker-explainer.webp" width="100%" alt="Die-cut Sticker Explainer">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use HTML on a large canvas to make a science-explainer animation of your topic: photo cut-outs with a 10px white border become stickers, a blue-gray background uses only two or three colors, and the camera pans and zooms across the canvas. Key visuals: photo cut-out stickers with white outline, blue-gray and off-white background, two or three colors plus one accent, flat icons with precise charts, oversized canvas, long-eased pan and zoom, bar growth and number roll-ups. Watch out: With too many colors or inaccurate chart proportions, the science-explainer seriousness is lost. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 HTML 大画布做你的主题的科普动画，照片抠图加 10px 白边做成贴纸，蓝灰底只用两三种颜色，镜头在画布上平移缩放。画面要点：照片抠图白描边贴纸、蓝灰米白底、两三色加一个强调色、扁平图标配精确图表、超大画布、长缓动平移缩放、柱状生长与数字滚动。注意：配色一多、图表比例不准，就没有科普的严肃感。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | A periodic table, a world map and a phone, photo cut-outs with white borders made into stickers, and a big 70/118 number slams in. | 元素周期表、世界地图和手机，照片抠图加白边做成贴纸，70/118 大数字砸出。 |
| B | Our render: an English explainer version. Clay jar and mouse stickers slap on, a bar chart grows to 48 mice, the camera pushes in to THEN THE WILDCAT ARRIVED, a wildcat sticker slaps down, and a Felis lybica label is hung. | 我们做的英文讲解版。陶罐和老鼠贴纸拍上来，柱状图涨到 48 只，镜头推到 THEN THE WILDCAT ARRIVED，野猫贴纸拍下，挂出 Felis lybica 标签。 |

## Where it usually breaks · 容易失败的点

More than three colors falls apart; bar heights and numbers must be proportionally accurate or the seriousness is lost; stickers without a white border and drop shadow are just ordinary cut-outs.

配色超过三种就散；柱高和数字比例要准，不然没有科普的严肃感；贴纸缺白边和投影就是普通抠图。

## Key visuals · 画面要点

photo cut-out stickers with white outline, blue-gray and off-white background, two or three colors plus one accent, flat icons with precise charts, oversized canvas, long-eased pan and zoom, bar growth and number roll-ups

照片抠图白描边贴纸、蓝灰米白底、两三色加一个强调色、扁平图标配精确图表、超大画布、长缓动平移缩放、柱状生长与数字滚动

Palette 主色：`#b88a3e`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 手机与元素周期表拆解 | [Vincentwei1021 · mg-styles-15](https://vincentwei1021.github.io/mg-styles-15/?lang=zh#19-paperclip) | prompts/code MIT; demo video not redistributed |
| B | carl-motion | [this repo](../../templates/scenes/sticker-explainer) · story idea: [en.yasue.org](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`templates/scenes/sticker-explainer`](../../templates/scenes/sticker-explainer) (Python (NumPy + OpenCV + Pillow)). Its README has the exact render command.

渲染 B 的完整源码在 [`templates/scenes/sticker-explainer`](../../templates/scenes/sticker-explainer)（Python (NumPy + OpenCV + Pillow)），渲染命令写在它的 README 里。
