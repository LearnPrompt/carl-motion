# Changelog

## 0.2.0 · 2026-10-27

- Skill moved to `skills/carl-motion/` and made self-contained: engines (`scenes/`), video tooling (`pipeline/`), `scripts/deliver.py`, `scripts/doctor.py` and a LICENSE now install with it.
- One entry for every engine: `./render.sh <work_dir>` writes 240 frames; `deliver.py` encodes and returns red / yellow / green. Red never leaves a clip behind.
- 29 style cards (`references/styles/`) with status, prompt, pipeline, beats, pitfalls and field notes, plus an INDEX. Status tiers: implemented, implemented on an upstream library, upstream only, research.
- SKILL.md split into an open track and a numbered rail for other models.
- Field notes: projects log to `carl-motion-log.md`; `scripts/import_experience.py` pulls them into `data/experience/`.
- `scripts/check_release.py` plus a GitHub Actions workflow.
- Removed the rubber-hose scene that is not one of the 29 styles.

## 0.1.0 · 2026-10-27

- First version: 29 style pages, 24 animated previews, 20 engines, prompt library skill, bilingual README.
