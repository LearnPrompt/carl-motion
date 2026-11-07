# Changelog

## Unreleased

- `skills/carl-motion/scripts/resolve_brief.py` decides an exact preset, a near match, a custom style, or a missing reference, and records whether a preview or a user file was actually decoded. Catalog URLs are not fetched. The 29 styles and the existing engines stay on their own stacks. Search is invoked only when nothing matches and no reference file opened; if no search command is configured the brief asks for search permission instead of pretending to have looked on X.
- The material rules are general (source, time, measured style parameters, block only the step that needs the missing file, keep facts apart from inferences). They are not a recovered client prompt and they do not switch the library to HyperFrames or GSAP.
- Both skill tracks have to run the brief before copying an engine. A decoded preview is not an engine input. Unread links cannot be described as a watched reference. `--approve-unreferenced-draft` continues only as a labeled draft after the user agrees.

## 0.2.0 · 2026-10-27

- Skill moved to `skills/carl-motion/` and made self-contained: engines (`scenes/`), video tooling (`pipeline/`), `scripts/deliver.py`, `scripts/doctor.py` and a LICENSE now install with it.
- One entry for every engine: `./render.sh <work_dir>` writes 240 frames; `deliver.py` encodes and returns red / yellow / green. Red never leaves a clip behind.
- 29 style cards (`references/styles/`) with status, prompt, pipeline, beats, pitfalls and field notes, plus an INDEX. Status tiers: implemented, implemented on an upstream library, upstream only, research.
- SKILL.md split into an open track and a numbered rail for other models.
- Field notes: projects log to `carl-motion-log.md`; `scripts/import_experience.py` pulls them into `data/experience/`.
- `scripts/check_release.py` plus a GitHub Actions workflow.
- Removed the rubber-hose scene that is not one of the 29 styles.
- README in English (default), Chinese and Japanese.

## 0.1.0 · 2026-10-27

- First version: 29 style pages, 24 animated previews, 20 engines, prompt library skill, bilingual README.
