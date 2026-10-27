# 10 · Die-cut Sticker Explainer · 贴纸科普 (`sticker-explainer`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/sticker-explainer/` (Python (NumPy + OpenCV + Pillow)). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use HTML on a large canvas to make a science-explainer animation of your topic: photo cut-outs with a 10px white border become stickers, a blue-gray background uses only two or three colors, and the camera pans and zooms across the canvas. Key visuals: photo cut-out stickers with white outline, blue-gray and off-white background, two or three colors plus one accent, flat icons with precise charts, oversized canvas, long-eased pan and zoom, bar growth and number roll-ups. Watch out: With too many colors or inaccurate chart proportions, the science-explainer seriousness is lost. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 HTML 大画布做你的主题的科普动画，照片抠图加 10px 白边做成贴纸，蓝灰底只用两三种颜色，镜头在画布上平移缩放。画面要点：照片抠图白描边贴纸、蓝灰米白底、两三色加一个强调色、扁平图标配精确图表、超大画布、长缓动平移缩放、柱状生长与数字滚动。注意：配色一多、图表比例不准，就没有科普的严肃感。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#b88a3e`

## Pipeline · 管线

- 蓝灰底 #E9EEF2 加 40 单位点阵；界面只用三色加一个强调色：深靛（字、柱、坐标轴）、灰蓝（辅助字、网格）、红色强调（MICE、WILDCAT、最后一根柱、计数器、标签红点）。
- 贴纸是程序画的仿照片抠图：陶罐、老鼠、野猫各自分层上色，底色叠细噪声当毛发和陶土质感，再按遮罩模糊做左上受光的体积明暗。外面一圈约 10 px 的白色模切边：先闭运算抹平凹口，再膨胀，边缘一道极细的灰边，表面一道很淡的覆膜反光，底下小投影。
- 贴纸拍下：从放大 1.25–1.4 倍、倾斜、悬空落到原位，back.out 收尾；投影由远、虚、淡变成近、实、深；前 3 帧淡入，避免整张贴纸一帧蹦出。
- 图表精确：每只老鼠 7.4 px，柱高严格按数值成比例，网格每 10 只一条，数值是滚动整数；副标题写明 Illustrative counts，不冒充实测数据。
- 野猫按非洲野猫画：沙黄底毛、淡虎斑、额头 M 形纹、环纹尾巴加黑尾尖、绿黄眼、耳背偏红；老鼠突出大圆耳、尖嘴和长尾，小尺寸也认得出。
- 大画布约 3700×1200，镜头 30 fps 连续：开场慢拉远，过场用 van Wijk–Nuij 平滑缩放平移（先退到总览再推进，屏幕上的感知速度恒定），最后匀速慢推。

## Beats · 节拍

0–0.5 s 陶罐贴纸拍下，左上角 03 THE GRAIN STORE 和大标题 MICE FOUND THE GRAIN 擦出｜0.4–1.5 s 五只老鼠贴纸依次拍在罐子周围｜0.8–1.6 s 图表标题、网格线自左向右画出｜1.2–3.1 s 五根柱子逐根长高（2、5、11、23、48），数值和右上角红色大计数器 0→48 跟着滚动｜0–2.8 s 镜头从 1.06 慢慢拉到 1.0｜2.8–5.8 s 镜头沿平滑缩放路径退到全画布总览（约 0.5 倍）再推进右半｜3.85–4.8 s 04 ENTER THE PREDATOR 和标题 THEN THE WILDCAT ARRIVED 擦出｜5.0 s 两只老鼠贴纸拍上｜5.78 s 虎斑野猫贴纸拍下，6.0 s 镜头轻震｜6.06–6.7 s 老鼠往右逃出画外｜6.38 s 引线从猫胸口画出｜6.52 s 拍上标签 Felis lybica · African wildcat｜6.95–7.6 s 补两行说明 Ancestor of today's house cats 和体貌特征｜5.8–8 s 匀速慢推。

## Pitfalls · 踩到的坑

- More than three colors falls apart; bar heights and numbers must be proportionally accurate or the seriousness is lost; stickers without a white border and drop shadow are just ordinary cut-outs.
- 配色超过三种就散；柱高和数字比例要准，不然没有科普的严肃感；贴纸缺白边和投影就是普通抠图。
- The automated check passes with no jump frames; the largest frame difference (6.58 at 6.52 s) is the label slapping on, by design.
- Stickers are procedurally painted photo-style illustrations, not real photo cut-outs; the cat's tabby is a few rough stripes and looks cartoonish up close.
- The bar chart numbers are illustrative (the frame says Illustrative counts), not archaeological statistics.
- During the overview (about 4.0-4.6 s) the UI text is very small; it is only a transition to show the full canvas.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
