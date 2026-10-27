# 24 · Product Exploded View · 产品爆炸拆解 (`exploded-view`)

## Status · 状态

**Implemented, one scene · 单场景实做.** Our engine rendered the B clip. Start from it and change the subject.

Engine: `scenes/exploded-view/` (Blender + Python). Run `./render.sh <work_dir>`, then `scripts/deliver.py --frames <work_dir>/frames --out clip.mp4`. Deterministic: not verified.

## Prompt · 提示语

EN: Use Blender to make an exploded teardown of your product: parts lift evenly spaced in layers along one axis, studio key light plus a cool rim light, leader lines labeling real specs, and everything closes back into one piece at the end. Key visuals: real CAD/PCB/BOM, evenly spaced layers along one axis, PBR studio key light plus cool rim light, HDRI reflections, leader lines and dimension lines, camera moving between layers, closing back together at the end. Watch out: Annotate only numbers that appear in the drawings; never estimate dimensions. Output 1920×1080, 30 fps, 8 seconds, as reproducible source code rendered to MP4.

中：用 Blender 做你的产品爆炸拆解，零件沿一根轴等距分层抬起，棚拍主光加冷色轮廓光，引线标真实参数，最后合回一体。画面要点：真实 CAD／PCB／BOM、沿一轴等距分层、PBR 棚拍主光加冷轮廓光、HDRI 反射、引线与尺寸线、镜头在层间穿行、最后合拢。注意：标注只写图纸里有的数，尺寸不许估。输出 1920×1080、30fps、8 秒，写成可复现的源码并渲染成 MP4。

Palette: `#4eb83e`, `#b88a3e`

## Pipeline · 管线

No engine yet. Build it from these visual keys, one pass per element:

real CAD/PCB/BOM, evenly spaced layers along one axis, PBR studio key light plus cool rim light, HDRI reflections, leader lines and dimension lines, camera moving between layers, closing back together at the end

真实 CAD／PCB／BOM、沿一轴等距分层、PBR 棚拍主光加冷轮廓光、HDRI 反射、引线与尺寸线、镜头在层间穿行、最后合拢

## Beats · 节拍

—

## Pitfalls · 踩到的坑

- Made-up model numbers and figures give it away; parts must separate along the assembly axis; materials must distinguish metal, plastic and PCB.
- 型号和数字瞎编会露馅；零件要沿装配轴拆开；材质要分出金属、塑料和 PCB。
- Lens elements are parabolic-approximation solids of revolution, not designed from a real optical prescription; EEVEE screen-space refraction is less accurate than path tracing for stacked lenses.
- Components are boxes plus solder-fillet prisms, without real rounded packages or lead bend radii; BGA models only the outer two ball rings.
- The nine aperture blades are layered one per level, so the overlap order differs from a real iris (not visible from the front).
- The shutter only opens and closes its blades; the drive linkage is not modelled.
- No-clipping relies on assembly-axis, timing and size design plus frame review, not per-frame collision detection.
- Macro depth of field is shallow; components away from the chip are blurred on purpose.
- The two macro transitions (about 4.8 s and 6.0 s) are fast continuous camera moves over a dense board and were flagged as jumps by the automated check (frames 145-146 and 179-184); reviewed frames show continuous parallax, no cut, no clipping and no black frames.

## Field notes · 实测记录

None yet. After using this style, append what broke and how you fixed it to `carl-motion-log.md` in the project (format in SKILL.md).
