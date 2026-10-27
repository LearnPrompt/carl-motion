# Workflow notes

## A/B pairs
Each style is shown as two 8-second clips in the same look on different subjects. A is an upstream reference, B is a second example. When you make a new example for a style, keep material, line quality and dominant colour consistent with A and change only the subject. That is what proves the style transfers.

## House spec
1920×1080, 30 fps, 240 frames, H.264 High, yuv420p, no audio track. Stepped styles (paper collage, claymation, risograph) animate on 12 fps beats inside the 30 fps container; do not smooth them back to full frame rate.

## QA
`python3 scripts/deliver.py --frames <dir> --out clip.mp4` checks the spec, black frames and frame-difference jumps and returns red, yellow or green; no A clip is needed. A flagged jump is fine when it is a designed cut or a beat change; say which it is.

## Ordering many styles
`pipeline/color_order_v4.py` measures each clip's dominant hue in CIELAB and orders styles so neighbours sit roughly complementary, then `color_stitch_verify.py` re-measures every cut on the finished video and rates it good, fair or weak.

## 9:16 explainer layout
`pipeline/script_layout.py` stacks A (top) and B (middle), keeps a title bar on top and puts the result first: from frame 0 the style name and a prompt card already half written are on screen, the rest streams in by 5.0 s like model output, and a warning strip appears at 5.4 s. The right-hand box is a presenter placeholder.
