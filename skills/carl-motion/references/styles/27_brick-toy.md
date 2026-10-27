# 27 · Brick Toy · 积木玩具 (`brick-toy`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/brick-toy/` (Blender + Python). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use Blender to make a toy-brick stop-motion of your topic, macro-shot on a real wooden table, glossy plastic with studs, characters posed on twos, with a smooth camera. Key visuals: real tabletop, macro shallow depth of field, glossy ABS rectangular highlights, studs on top faces, contact shadows in the seams, characters stop-motion on twos, camera smooth frame by frame, neutral studio HDRI. Watch out: No brand names or minifigure silhouettes; build the characters out of bricks. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Blender 做你的主题的积木定格，真实木桌上微距拍，亮面塑料带凸点，角色两帧一拍定格，镜头保持顺滑。画面要点：真实桌面、微距浅景深、亮面 ABS 矩形高光、顶面凸点、缝隙接触阴影、角色 on twos 定格、镜头逐帧顺滑、中性棚拍 HDRI。注意：别出现品牌字样和小人轮廓，角色用积木拼出来。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#4eb83e`, `#b86c3e`

## Pipeline · 管线

- 真实尺度：1 凸点 = 8 mm，砖高 1.2、板高 0.4；50 mm 镜头 f/8 物理景深（f/4 时近景桥面虚化过强会在 EEVEE 中出现前景半透明，故收小），低机位接近玩具视线，后景杯子/书本虚化（不用 A 的茶壶）。
- 塑料：clearcoat 0.8 / coat roughness 0.07，粗糙度通道叠加指纹/划痕噪声，倒角 0.045 凸点让边缘吃高光；凸点无字；底板为低光泽绿。
- 灯光：暖白主光（太阳）+ 前方柔光箱 + 冷色轮廓 + 顶光，环境 0.32。
- 动作语法：角色与积木按 12 fps 步进（on twos），相机、对焦、小车按 30 fps 连续；积木走弧线、卡入时小回弹；不变形（刚体）。机器人手臂姿态由所搬积木的位置反解，手始终扣在积木后缘。
- 字幕：深色胶囊 + 小积木图标 + 白字（Arial Rounded Bold，系统字体），按 12 fps 弹入，位于下方安全区内。

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- Using branded minifigures carries copyright risk; bricks need studs and plastic highlights; deep depth of field no longer looks like a real macro shot.
- 用品牌小人会有版权风险；积木要有凸点和塑料高光；景深一深就不像微距实拍。
- No 2x supersampling (32 TAA samples used to keep render time down); fine stud edges may shimmer slightly when viewed small.
- The robot places bricks with position constraints and no finger grip; the bridge rebound under the car is tiny (about 0.5 mm).
- Captions use Arial Rounded instead of the upstream-suggested Fredoka, which is not installed locally.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
