# 26 · Glassmorphism UI · 玻璃拟态UI (`glassmorphism-ui`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/glassmorphism-ui/` (Node + Canvas / headless Chrome). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use HTML to make a glassmorphism animation of your topic: three to five large Gaussian-blurred color blobs drift slowly underneath, with frosted glass cards floating on top, with a 1px translucent white border. Key visuals: aurora color blobs with blur 80 to 150px, backdrop-filter frosted cards, white fill at 5 to 10%, 1px white border, two or three adjacent hues, 3 to 5% noise to prevent banding, sine breathing easing. Watch out: Clashing colors get muddy and fast motion looks cheap; keep a slow breathing pace throughout. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 HTML 做你的主题的玻璃拟态动画，底层三到五个大色斑高斯模糊慢慢漂，上面浮磨砂玻璃卡片，1px 半透明白描边。画面要点：aurora 大色斑 blur 80 到 150px、backdrop-filter 磨砂卡片、白色 5 到 10% 填充、1px 白描边、邻近色两三色、3 到 5% 噪点防色带、sine 呼吸缓动。注意：撞色会脏，动作一快就廉价，全程慢呼吸。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#3e4eb8`

## Pipeline · 管线

- 背景：5 个邻近色大光斑。2026-10-26 按卡尔审核意见改为 A 的互补色：A 的紫/蓝/青/洋红分别换成琥珀/橙/珊瑚红/青柠，底色从深蓝改为深暖棕红；复选框、透镜、进度环、Focus 球、高光扫过一并改为暖色。这一改动偏离了任务提示语中同画风 A/B 保持主色体系一致的要求，由用户明确决定。改前的蓝紫版源码存档在 `index_A色版.html`。原句：5 个邻近色（紫/蓝/青/洋红）大光斑沿贝塞尔路径漂移 + 光点 + 暗角 + 逐帧颗粒（防 banding）。
- 玻璃：真实 `backdrop-filter: blur(34px) saturate(150%)`，白色 5–16% 渐变填充，1.5px 内高光描边，大圆角，投影。
- 透镜：SVG `feDisplacementMap` 球冠位移图做真折射，R/G/B 三通道不同位移量形成色散边缘，作为 `backdrop-filter: url(#lensFilter)`。
- 缓动：sine / cubic / 阻尼弹簧；无 CSS transition/animation，每帧是 t 的纯函数。

## Beats · 节拍

0–1 s 卡束入场（opacity + 小位移，帧0即有画面）｜1–3 s 卡束展开、主卡前移、行项逐条浮现、整体浅推近｜3.35 / 4.25 / 5.15 s 三次勾选｜5.4 s 主卡边缘高光扫过｜5.9–7.0 s 主卡收拢为 Focus 卡｜7–8 s 文案浮现，卡片呼吸微动。

## Pitfalls · 踩到的坑

- Contrasting colors look cheap, so use only adjacent hues; keep motion slow; glass without a 1px translucent white edge and background blur looks like an ordinary card.
- 用对比色会显廉价，只用邻近色；动作要慢；玻璃缺 1px 半透明白边和背景模糊就像普通卡片。
- No audio track (silent by spec).
- The lens interior is fairly dark (displacement samples the dark background), so it reads as a glass bubble rather than a magnifier; the dispersion edge is clear.
- From 0 to 1.5 s the main-card content fades in progressively, so the lower half of the card is empty at the start.
- Chrome for Testing 155 must be reinstalled (npx @puppeteer/browsers install chrome@155.0.8059.79) or CHROME_PATH must point to a Chrome; the system Chrome was only verified for opening the review page, not for re-rendering the clip.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
