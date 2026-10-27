# 01 · Retro Paper Collage · 复古纸张拼贴

[All styles](README.md) · [← Sci-fi Scan HUD](scifi-hud.md) · [Product UI 2.5D Camera →](product-ui-2-5d.md)

<img src="../../assets/previews/retro-paper-collage.webp" width="100%" alt="Retro Paper Collage">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use HTML to turn your topic into a retro paper collage: cut-out assets with white scissor edges and halftone dots, motion dropped to 12 fps, with a slight hand jitter. Key visuals: newspaper and kraft paper background, cut-outs with a 2 to 4px white scissor edge, halftone dots, 12fps down to 6fps, plus or minus 2px hand-moved jitter, slap-on and page-flip transitions, red and black constructivist type, ransom-note lettering. Watch out: Full-frame smooth motion loses the handmade feel; drop to 12 fps and add 2px of jitter. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 HTML 做你的主题的复古纸张拼贴，素材抠图加白色剪刀边和半调网点，运动降到 12 帧，加轻微手抖。画面要点：报纸牛皮纸底、抠图加 2 到 4px 白剪刀边、halftone 网点、12fps 乃至 6fps、正负 2px 手摆抖动、拍上来与翻页转场、红黑构成主义字、勒索信拼字。注意：满帧顺滑就没有手作感，降到 12 帧再加 2px 抖动。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | A Victorian vintage photo portrait with the top of the head cut open; a universe, rockets, flowers and birds grow out of the skull, on a red circle over old newspaper, closing on a NOGGIN magazine cover. | 维多利亚老照片人像被剪开头顶，宇宙、火箭、花鸟从脑壳里长出来，红圆底配旧报纸，收在 NOGGIN 杂志封面。 |
| B | Our render: an English explainer version. Ransom-note letters on kraft paper spell Why did cats move in with us; the village, clay jars, mice and a tabby wildcat are all torn-paper cut-outs, moving at one step per 12 fps beat. | 我们做的英文讲解版。牛皮纸上勒索信字拼出 Why did cats move in with us，村子、陶罐、老鼠和虎斑野猫都是撕纸剪片，按 12 帧一拍走。 |

## Where it usually breaks · 容易失败的点

Full-frame smooth motion looks like PowerPoint animation; drop to 12 fps and add a light jitter on every beat. Cut-outs without torn edges and drop shadows fall back to flat vector. Using only one typeface loses the ransom-note collage feel.

满帧顺滑运动像 PPT 动画，要降到 12 帧再加每拍轻抖；剪片缺撕边和投影就退成扁平矢量；字体只用一种就没有勒索信的拼贴味。

## Key visuals · 画面要点

newspaper and kraft paper background, cut-outs with a 2 to 4px white scissor edge, halftone dots, 12fps down to 6fps, plus or minus 2px hand-moved jitter, slap-on and page-flip transitions, red and black constructivist type, ransom-note lettering

报纸牛皮纸底、抠图加 2 到 4px 白剪刀边、halftone 网点、12fps 乃至 6fps、正负 2px 手摆抖动、拍上来与翻页转场、红黑构成主义字、勒索信拼字

Palette 主色：`#b88a3e` `#3e8ab8`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 男子打开脑盖喷出宇宙 | [Vincentwei1021 · mg-styles-15](https://vincentwei1021.github.io/mg-styles-15/?lang=zh#06-collage) | prompts/code MIT; demo video not redistributed |
| B | carl-motion | [this repo](../../templates/scenes/retro-paper-collage) · story idea: [en.yasue.org](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`templates/scenes/retro-paper-collage`](../../templates/scenes/retro-paper-collage) (Python (NumPy + OpenCV + Pillow)). Its README has the exact render command.

渲染 B 的完整源码在 [`templates/scenes/retro-paper-collage`](../../templates/scenes/retro-paper-collage)（Python (NumPy + OpenCV + Pillow)），渲染命令写在它的 README 里。
