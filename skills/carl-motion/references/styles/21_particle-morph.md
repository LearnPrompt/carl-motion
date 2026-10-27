# 21 · Particle Morph · 粒子聚散造型 (`particle-morph`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/particle-morph/` (Python (NumPy + OpenCV + Pillow)). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Make a particle animation: hundreds of thousands of glowing particles gather on a dark background into the shape and text of your topic, then scatter and become the next shape. Key visuals: hundreds of thousands of glowing particles, gather into shape then scatter, deep blue-black background, lines connecting into a relationship network, big number counter, one English conclusion line as subtitle. Watch out: Too few particles or no target shape, and the form cannot be read. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：做一支粒子动画，几十万发光粒子在深色背景上聚成你的主题的形状和文字，再散开变成下一个形状。画面要点：数十万发光粒子、聚拢成形再散开、深蓝黑底、连线成关系网络、大数字计数器、一句英文结论字幕。注意：粒子太少或不给目标形状，就读不出造型。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#3e6cb8`, `#b88a3e`

## Pipeline · 管线

- 60,000 颗粒子，暖琥珀、金色、暖白、深橙四档颜色，2% 的粒子亮三倍当闪点；背景是冷色深蓝径向渐变加少量冷色星点。
- 每个目标形状都先画成实心遮罩（村子、猫和人、两行字幕），再从遮罩采样目标点，三成采在轮廓带上，让剪影边缘清楚。
- 运动是嵌套插值：星云 → 村子 → 旋涡 → 终形。每段每颗粒子错开起点，用带回弹的弹簧缓动，路径加垂直方向的弧形偏移；未锁定时叠大幅 curl noise 漂移，锁定后只剩约 2 px 的呼吸。
- 渲染全用 numpy：每帧三个子时刻做运动模糊，双线性 splat 进累加缓冲（bincount 加法混合），再叠 2、8、30 px 三层模糊做辉光，按亮度做指数色调映射保住琥珀色相。
- 右上角计数器显示当前锁定在形状里的粒子数，下面一条进度线同步伸缩，对应 A 参考片的大数字计数。

## Beats · 节拍

0–0.8 s 两条旋臂的暖色星云逐渐亮起，右上计数从 0 开始｜0.15–1.9 s 星云聚成村子剪影（两座圆屋、三个陶罐、谷仓穹顶、麦穗，门洞窗洞挖空），计数涨到 60,000｜1.9–2.9 s 村子停住，只有呼吸漂移和闪烁｜2.85–3.9 s 村子从左到右被卷走，汇成三臂旋涡，计数回落到 0｜3.75–5.3 s 旋涡里的四万多颗粒子聚成坐着的猫和伸手的人｜4.95–6.0 s 剩下的粒子从旋涡飞出拼成 MAYBE…，到位后叠一层实体字｜5.85–6.9 s 再拼出 THE CAT CHOSE US｜6.9–8 s 全部锁定，轻微呼吸，停到结尾。

## Pitfalls · 踩到的坑

- Too few particles or no target shape and the form cannot be read; provide a defined shape and enough particles; the gathering and scattering needs rhythm, so do not let them drift all the time.
- 粒子太少或没给目标形状就读不出造型；要给定形状并让粒子够多；聚和散要有节奏，别一直飘。
- No jump frames flagged; the darkest frame averages about 24/255, so there are no black frames.
- The village hold (1.9-2.9 s) and the ending (6.9-8 s) only breathe and twinkle, so frame differences are tiny (ending minimum 0.017); one near-still pair, longest still stretch 1 frame.
- At 4.9-5.9 s the caption particles still swirl and the vortex centre sits between the person and cat, so their silhouettes are partly covered by light dust.
- Frames mid-gathering (for example 1.0 s and 3.5 s) are a light haze; the shape only reads once the spring settles, which is part of the rhythm.
- The count is 60,000 particles, not the hundreds of thousands of the reference; more would only be slower, and the silhouettes already read.
- A solid text layer is overlaid after the particles land so the caption stays readable when shrunk, so the text is not purely particles.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
