# 22 · White-model Projection · 实体白模投影 (`white-model-projection`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/white-model-projection/` (Blender + Python). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use Three.js to make a white-model city: pure white blocks on a dark-room display plinth, with data added only as projected light layer by layer, soft light edges spilling over the base. Key visuals: pure white block model, dark-room plinth, data as projected light, only faces toward the projector light up, soft light edges spilling over the base, one question per layer, lights on and off as opener and closer, real building data. Watch out: Do not paint color into the material; warm ambient light will also tint the white model yellow. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Three.js 做你的城市白模，纯白体块放在暗房展台上，数据只以投影光一层层打上去，光边柔和、溢出底座。画面要点：纯白体块模型、暗房展台、数据即投影光、只亮朝向投影仪的面、柔和光边溢出底座、一层一个问题、开灯关灯作开场收尾、真实建筑数据。注意：颜色别画进材质，暖色环境光还会把白模染黄。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#3e6cb8`, `#b86c3e`

## Pipeline · 管线

- 主体始终是哑光全白实体；颜色不写进材质，只来自投影机光。
- 投影遮挡真实：投影遍只开一盏投影聚光灯（EEVEE 阴影贴图），面向投影机的面亮、背向面暗、被遮挡处无光。
- 字：身份标签、左侧读数大字、两枚图钉、近/中/远图例、居中双语字幕；无数字、无伪造数据。

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- If the white model carries its own color it is no longer a projection; color may only come from the projected light; text should be projected onto the model, not float on the screen.
- 白模本身带了颜色就不是投影了，颜色只能来自投影光；字要投在模型上，别浮在屏幕上。
- The city uses procedural boxes (flat, gabled, tower plus rooftop plant), not irregular footprints from real building data; single buildings are simpler than real open data.
- Projection shadows come from EEVEE shadow maps, not path tracing; at closest approach the seams under eaves are softer than Cycles.
- At 32 samples the dark areas show slight grain, so uniform grain was added in post to unify the texture.
- The projector start-up flicker (frames 31-35) is a designed effect and was not counted as a jump.
- The walkable-reach layer has only three bands, not a continuous gradient.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
