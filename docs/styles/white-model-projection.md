# 22 · White-model Projection · 实体白模投影

[All styles](README.md) · [← Particle Morph](particle-morph.md) · [Ancient Egyptian Mural →](egyptian-mural.md)

<img src="../../assets/previews/white-model-projection.webp" width="100%" alt="White-model Projection">

<sub>Preview: our render (layer B), MIT. 预览是我们渲染的 B，MIT 许可。</sub>

**Status 状态:** Implemented, one scene · 单场景实做

## Prompt (copy this)

Paste into Claude, GPT or any coding model. Swap *your topic* for your own subject.

```text
Use Three.js to make a white-model city: pure white blocks on a dark-room display plinth, with data added only as projected light layer by layer, soft light edges spilling over the base. Key visuals: pure white block model, dark-room plinth, data as projected light, only faces toward the projector light up, soft light edges spilling over the base, one question per layer, lights on and off as opener and closer, real building data. Watch out: Do not paint color into the material; warm ambient light will also tint the white model yellow. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.
```

## 提示语（复制这段）

发给 Opus 5.5 或任意能写代码的模型，把你的主题换成自己的内容。

```text
用 Three.js 做你的城市白模，纯白体块放在暗房展台上，数据只以投影光一层层打上去，光边柔和、溢出底座。画面要点：纯白体块模型、暗房展台、数据即投影光、只亮朝向投影仪的面、柔和光边溢出底座、一层一个问题、开灯关灯作开场收尾、真实建筑数据。注意：颜色别画进材质，暖色环境光还会把白模染黄。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。
```

## What the two examples show · 两个示例

| | English | 中文 |
|---|---|---|
| A | Blue-purple era color blocks are projected onto a gray-white city model, switching between the years 1971 and 2015. | 灰白城市白模上投出蓝紫年代色块，1971、2015 年份切换。 |
| B | Our render: The white model changes from an old factory into a public library, and projected light draws the routes. | 我们做的。白模从老工厂变成公共图书馆，投影光画出路线。 |

## Where it usually breaks · 容易失败的点

If the white model carries its own color it is no longer a projection; color may only come from the projected light; text should be projected onto the model, not float on the screen.

白模本身带了颜色就不是投影了，颜色只能来自投影光；字要投在模型上，别浮在屏幕上。

## Key visuals · 画面要点

pure white block model, dark-room plinth, data as projected light, only faces toward the projector light up, soft light edges spilling over the base, one question per layer, lights on and off as opener and closer, real building data

纯白体块模型、暗房展台、数据即投影光、只亮朝向投影仪的面、柔和光边溢出底座、一层一个问题、开灯关灯作开场收尾、真实建筑数据

Palette 主色：`#3e6cb8` `#b86c3e`

## References · 参考来源

| Layer | Title | Source | License |
|---|---|---|---|
| A | 白模投影：How a Flattened City Grew Back | [LemoLab · lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/white-model) | prompts/code MIT, demo video CC BY 4.0 |
| B | carl-motion | [this repo](../../skills/carl-motion/scenes/white-model-projection) | MIT |

## Reproduce · 复现

Source that rendered the B clip: [`skills/carl-motion/scenes/white-model-projection`](../../skills/carl-motion/scenes/white-model-projection) (Blender + Python). Check dependencies first with `python3 skills/carl-motion/scripts/doctor.py white-model-projection`.

```bash
cd skills/carl-motion/scenes/white-model-projection
./render.sh /tmp/white-model-projection
python3 ../../scripts/deliver.py --frames /tmp/white-model-projection/frames --out white-model-projection.mp4
```

渲染 B 的完整源码在 [`skills/carl-motion/scenes/white-model-projection`](../../skills/carl-motion/scenes/white-model-projection)（Blender + Python），渲染命令写在它的 README 里。
