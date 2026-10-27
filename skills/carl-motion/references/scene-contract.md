# Scene contract

Every engine in `scenes/<slug>/` follows the same contract, so an agent can run, swap or copy any of them the same way.

## Entry

```bash
./render.sh <work_dir> [variant]
python3 <skill>/scripts/deliver.py --frames <work_dir>/frames --out <clip.mp4> [--crf N] [--palette "#hex,…"]
```

- `render.sh` takes the work folder as its first argument and writes the **final** frames to `<work_dir>/frames/0001.png … 0240.png`, 1920×1080. Intermediate passes (raw renders, textures, projections) go to other subfolders of `<work_dir>`.
- `render.sh` never encodes and never writes outside `<work_dir>`. Encoding, spec checks and the verdict all belong to `deliver.py`.
- `engine.json` next to it lists the style IDs, stack, dependencies, fonts, CRF, whether output is verified deterministic, and the known limits.
- Run `python3 <skill>/scripts/doctor.py <slug>` first. It names anything missing before you spend ten minutes rendering.

## Hard rules for new or edited engines

1. **Deterministic.** All randomness takes a fixed seed; the same frame index renders the same pixels twice. Mark `"deterministic": true` in engine.json only after rendering twice and comparing.
2. **Frame-indexed time.** Every frame is a function of `t = (frame - 1) / 30`. No wall-clock, no accumulated state that depends on render order, so frames can render in parallel (`JOBS=8`) and singly (`ONLY=30,120,200` where supported).
3. **Stepped styles step on purpose.** Collage, claymation and risograph animate on 12 fps beats inside the 30 fps container. Hold the drawing between beats; do not reshuffle noise every frame (that reads as flicker).
4. **Material on everything.** The character and the props go through the same medium as the background: torn edges, halftone, ink bleed, brush flow, print misregistration. A clean vector figure on a textured background looks pasted on.
5. **Text in the style's material.** Captions are drawn in the style (ransom-note letters, stencil type, chalk) rather than overlaid as UI text. If you load a font, check the file exists and fall back explicitly; list it in engine.json.
6. **Frame one is a picture.** Frame 0001 must already read as the style. No blank paper, no fade from black; `deliver.py` marks black frames red.
7. **Stay inside the folder.** No absolute paths, no `../../..` out of the skill. Fonts are the only allowed outside dependency, and they are listed.

## Verified so far

Only `risograph` has been checked bit-exact (rendered from the repo, PSNR identical to the published clip on every sampled frame). The others are written to the same rules and rendered once for the published clips; treat them as unverified until someone renders them twice.
