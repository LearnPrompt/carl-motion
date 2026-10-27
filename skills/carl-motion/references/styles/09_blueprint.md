# 09 · Blueprint Drawing · 蓝图工程制图 (`blueprint`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/blueprint/` (Python (NumPy + OpenCV + Pillow)). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use Canvas to draw your topic on Prussian-blue blueprint paper in thin white lines, in drawing order, with dimension lines, numbered balloons and a drawing frame. Key visuals: cyanotype blueprint paper, thin white engineering lines, layer-by-layer drawing order, dimension lines and leader lines, numbered balloons, title block frame, section hatching, pan and zoom of the whole sheet. Watch out: Keep it a 2D line drawing in blue and white only; once it becomes 3D or a glowing wireframe it no longer fits. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Canvas 在普鲁士蓝晒图纸上，用白色细线按绘图顺序画出你的主题，配尺寸线、编号气泡和图框。画面要点：cyanotype 蓝晒纸、白色工程细线、逐层绘制顺序、尺寸线与引线、编号气泡、title block 图框、剖面线、整张图纸平移缩放。注意：只用蓝白两色的 2D 线稿，一做成 3D 或发光线框就不像了。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#3e6cb8`

## Pipeline · 管线

- 普鲁士蓝晒图纸：底色加低频曝光不匀、中频斑驳、细颗粒和横竖两道折痕；网格每 20 单位一条细线、每 100 单位一条粗线，每帧按矢量重画，推近时不会糊。
- 白色细线按绘图顺序逐笔画出：每条折线有起止时间，按弧长推进，笔尖有一个白点；虚线、点划线在弧长上切段；箭头画完后才填实。
- 尺寸线带尺寸界线和双箭头，编号气泡带引线和落点小圆点，剖面用 45° 斜线，中心线用点划线，右下角是标准 title block。
- 只用蓝白两色、只做 2D：没有发光、没有 3D 线框、没有渐变色，墨线只有 1.6 px 的轻微晕开。
- 猫和老鼠先用椭圆、多边形和粗线拼成实心遮罩，再取外轮廓当一笔画；条纹、尾环用遮罩裁剪只留在身体里，放大圆里的老鼠用圆形裁剪。

## Beats · 节拍

0–0.7 s 图框双线、分区刻度、地面线先画出，左上图题条打字 FIG. 1 — GRANARY, c. 8000 BCE｜0.3–1.9 s 圆屋墙体、锥形屋顶、门洞、砖缝、茅草线依次画出｜0.9–2.5 s 三个陶罐，中间一个做半剖面（内壁、剖面斜线、点划中心线、谷粒）｜2.0–2.9 s 尺寸线 Ø 0.5 m、1.1 m 和编号气泡 1 HUT、2 STORAGE JAR、3 GRAIN · SECTION A–A｜2.85–3.6 s 图题换成 FIG. 2 — MOUSE (Mus musculus)｜3.0–4.3 s 四只老鼠逐只画出，引线汇到 HOUSE MOUSE 标注，QTY 从 01 跳到 04｜3.95–4.9 s 罐顶老鼠圈出 B，右上画 DETAIL B · 2 : 1 放大圆｜4.65–5.3 s 图题换成 FIG. 3 — WILDCAT (Felis lybica)｜4.8–6.4 s 野猫侧视外轮廓一笔画完，再画眼鼻胡须、虎斑条纹、尾环和深色尾尖｜6.05 s 气泡 5 WILDCAT · Felis lybica｜6.25–6.8 s 虚线箭头从猫鼻子划向谷仓，标 REACHES THE GRANARY｜6.6–7.5 s 右下画图框 WHY CATS MOVED IN · SHEET 1 OF 1｜7.3–8 s 镜头拉到整张图纸并继续极慢拉远。

镜头全程只平移和缩放：FIG.1 停在谷仓左侧（1.32 倍），FIG.2 移到老鼠和放大圆（1.3 倍），FIG.3 移到猫（1.28 倍），最后拉远到 1.0 倍看全图。

## Pitfalls · 踩到的坑

- Once it becomes 3D or a glowing wireframe it no longer fits; use a 2D line drawing in blue and white only; if all lines appear at once the sense of drawing is lost.
- 做成 3D 或发光线框就不像了；只用蓝白两色的 2D 线稿；线条一次全出现会丢掉绘制感。
- No jump frames flagged by the automated check; the longest still stretch is 0 frames.
- The first 0.2 s shows only the frame and ground line starting to draw, so the picture is sparse.
- When zoomed out the mice are only about 50 px wide at 1080x608, so a DETAIL B magnifier circle was added.
- Mouse leader lines cross the jars and ground hatching; common in engineering drawings but slightly dense.
- Small annotations are about 12 px tall at 1080x608: readable but not large; main figure titles are 44 px cap height.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
