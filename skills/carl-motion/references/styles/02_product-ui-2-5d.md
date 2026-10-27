# 02 · Product UI 2.5D Camera · 产品界面2.5D运镜 (`product-ui-2-5d`)

## Status · 状态

**Research recipe, prompt only · 研究配方，只有提示语.** No implementation yet. Show the user a still frame before animating.

Engine: none in this skill. Build from the prompt; show a still frame before animating.

## Prompt · 提示语

EN: Use Remotion to turn real screenshots of your product's pages into a promo video: tilt the screenshots in 3D for a 2.5D camera move, and hold key information for more than one second. Key visuals: Remotion, real page screenshots, 2.5D page camera, pages tilted then layered, beat-synced cuts, number roll-ups, flash frames, key information held for one second. Watch out: Pacing that is too fast, with the whole screen shaking on every beat, looks cheap; slow it down one notch. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Remotion 把你的产品真实页面截图做成宣传片，截图 3D 倾斜做 2.5D 运镜，关键信息停留一秒以上。画面要点：Remotion、真实页面截图、2.5D 页面相机、页面倾斜后分层、卡点剪辑、数字滚动、闪帧、关键信息停留一秒。注意：节奏太快、整屏一拍一抖会廉价，放慢一档。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#d2d2d2`

## Pipeline · 管线

No engine yet. Build it from these visual keys, one pass per element:

Remotion, real page screenshots, 2.5D page camera, pages tilted then layered, beat-synced cuts, number roll-ups, flash frames, key information held for one second

Remotion、真实页面截图、2.5D 页面相机、页面倾斜后分层、卡点剪辑、数字滚动、闪帧、关键信息停留一秒

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- Fast pacing with the whole screen shaking together looks cheap; slow it down one notch. UI text must be real and readable, since gray blurred bars look like placeholders. A perspective angle that keeps changing causes dizziness.
- 节奏快、整屏一起抖会显廉价，要放慢一档；界面字要真实可读，糊成灰条就像占位图；透视角度来回变会晕。

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
