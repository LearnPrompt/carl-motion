# Workflow notes

## A/B pairs
Each style is shown as two 8-second clips in the same look on different subjects. A is an upstream reference, B is a second example. When you make a new example for a style, keep material, line quality and dominant colour consistent with A and change only the subject. That is what proves the style transfers.

## House spec
1920×1080, 30 fps, 240 frames, H.264 High, yuv420p, no audio track. Stepped styles (paper collage, claymation, risograph) animate on 12 fps beats inside the 30 fps container; do not smooth them back to full frame rate.

## QA
`python3 templates/pipeline/qa.py <ID> <B.mp4> <A.mp4> <out_dir>` reports resolution, frame count, black frames and frame-difference jumps. A flagged jump is fine when it is a designed cut or a beat change; say which it is.

## Ordering many styles
`templates/pipeline/color_order_v4.py` measures each clip's dominant hue in CIELAB and orders styles so neighbours sit roughly complementary, then `color_stitch_verify.py` re-measures every cut on the finished video and rates it good, fair or weak.

## 9:16 explainer layout
`templates/pipeline/script_layout.py` stacks A (top) and B (middle), keeps a title bar on top and runs four beats per style underneath: question bubble 0 to 1.6 s, style name 1.6 to 3.6 s, prompt typed out 3.6 to 5.4 s, warning strip 5.4 to 8 s. The right-hand box is a presenter placeholder.
