# 08 · Point-cloud Survey · 点云测绘／剥层

[All styles](README.md) · [← Soft Inflatable 3D](soft-inflatable-3d.md) · [Blueprint Drawing →](blueprint.md)

<img src="../../assets/previews/point-cloud-survey.webp" width="100%" alt="Point-cloud Survey">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

**Status 状态:** Implemented, one scene · 单场景实做

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use Three.js to turn your location into a laser point cloud: real measured points floating on black, a scan plane passes and the points solidify into solid terrain, then peel apart layer by layer by ground, vegetation and buildings. Key visuals: real airborne lidar points, near-black background, scan line or section plane advancing, points condense into a solid lit at grazing angle, layers peeled by ground, vegetation and building classes, hairline measurement readouts, one designed camera move. Watch out: From afar a point cloud looks like a flat carpet; the camera must fly low and close. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 Three.js 把你的地点做成激光点云，黑底悬浮真实测量点，扫描面经过后凝成实体地形，再按地面植被建筑逐层剥开。画面要点：真实机载激光点、近黑底、扫描线或剖切面推进、点凝成掠射光实体、按地面植被建筑分类剥层、发丝线测量读数、一条设计好的运镜。注意：远看点云像平地毯，镜头要贴低穿过去。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | A lidar point-cloud terrain on black; after the scan plane passes it solidifies, old field-ridge lines light up one by one, with Chinese and English subtitles. | 黑底激光点云地形，扫描面过后凝成实体，旧田埂线一条条亮出来，中英字幕。 |
| B | Our render: a sub-canopy point cloud has one layer of tree canopy peeled off, revealing a wall foundation and an arch. | 我们做的制作。林下点云剥掉一层树冠，露出墙基和一座拱门。 |

## Where it usually breaks · 容易失败的点

From afar a point cloud looks like a flat carpet, so the camera must fly low and close; points that are too sparse cannot read as terrain; peel the layers by ground, vegetation and building class.

远看点云像平铺地毯，镜头要贴低穿过去；点太稀读不出地形；剥层要按地面、植被、建筑分类。

## Key visuals · 画面要点

real airborne lidar points, near-black background, scan line or section plane advancing, points condense into a solid lit at grazing angle, layers peeled by ground, vegetation and building classes, hairline measurement readouts, one designed camera move

真实机载激光点、近黑底、扫描线或剖切面推进、点凝成掠射光实体、按地面植被建筑分类剥层、发丝线测量读数、一条设计好的运镜

Palette 主色：`#777777`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 点云测绘：The Fields Under the Forest | [LemoLab · lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/lidar-survey) | prompts/code MIT, demo video CC BY 4.0 |
| B | carl-motion | [this repo](../../skills/carl-motion/scenes/point-cloud-survey) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`skills/carl-motion/scenes/point-cloud-survey`](../../skills/carl-motion/scenes/point-cloud-survey) (Blender + Python). Check dependencies first with `python3 skills/carl-motion/scripts/doctor.py point-cloud-survey`.

```bash
cd skills/carl-motion/scenes/point-cloud-survey
./render.sh /tmp/point-cloud-survey
python3 ../../scripts/deliver.py --frames /tmp/point-cloud-survey/frames --out point-cloud-survey.mp4 --crf 19
```

渲染 B 的完整源码在 [`skills/carl-motion/scenes/point-cloud-survey`](../../skills/carl-motion/scenes/point-cloud-survey)（Blender + Python），渲染命令写在它的 README 里。
