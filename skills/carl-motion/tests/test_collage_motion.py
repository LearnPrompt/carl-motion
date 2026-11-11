#!/usr/bin/env python3
"""The collage page-pull moves every frame, not once per 12 fps beat."""
import importlib.util, unittest
from pathlib import Path

SCENE = Path(__file__).resolve().parents[1] / 'scenes' / 'retro-paper-collage' / 'scene.py'


def load():
    spec = importlib.util.spec_from_file_location('retro_scene', SCENE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class CollagePullTest(unittest.TestCase):
    def test_title_sheet_step_stays_under_the_jump_budget(self):
        # deliver.py flags a frame when the 192×108 mean absdiff exceeds 8.
        # A full-frame textured slide stays under that near 120 px/frame at 1080p
        # once motion blur covers the step. The old 12 fps ease jumped ~1200 px.
        scene = load()
        xs = scene.pull_offsets()
        steps = [abs(xs[i + 1] - xs[i]) for i in range(len(xs) - 1)]
        self.assertGreater(len(steps), 20)          # 30 fps across the pull, not four beats
        self.assertLess(max(steps), 140)
        self.assertLess(steps[0], 20)               # ease-in, no first-frame yank
        self.assertAlmostEqual(xs[0], 0, delta=1)
        self.assertAlmostEqual(xs[-1], -scene.PULL_TRAVEL, delta=1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
