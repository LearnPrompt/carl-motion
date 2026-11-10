#!/usr/bin/env python3
"""doctor.py accepts a scene slug or a path to an engine directory."""
import json, os, subprocess, sys, tempfile, unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
DOCTOR = SKILL / 'scripts' / 'doctor.py'


def run(args):
    return subprocess.run([sys.executable, str(DOCTOR), *args], capture_output=True, text=True)


class DoctorPathTest(unittest.TestCase):
    def test_slug_still_resolves_under_scenes(self):
        proc = run(['retro-paper-collage'])
        self.assertNotIn('no engine', proc.stderr + proc.stdout)
        self.assertIn('retro-paper-collage', proc.stdout)

    def test_engine_directory_is_not_treated_as_a_slug(self):
        missing = run(['run-case/engine'])
        text = missing.stderr + missing.stdout
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn('run-case/engine', text)
        self.assertNotIn('scenes/run-case/engine', text.replace('\\', '/'))

        with tempfile.TemporaryDirectory() as tmp:
            engine = Path(tmp) / 'run-case' / 'engine'
            engine.mkdir(parents=True)
            (engine / 'engine.json').write_text(json.dumps({
                'slug': 'copied', 'stack': 'python',
                'requires': {'pip': ['numpy'], 'binaries': []}, 'fonts': [],
            }), encoding='utf-8')
            proc = run([str(engine)])
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            self.assertIn('OK   engine (python)', proc.stdout)
            self.assertNotIn('scenes/run-case/engine', proc.stdout + proc.stderr)

    def test_engine_json_file_is_accepted(self):
        src = SKILL / 'scenes' / 'retro-paper-collage' / 'engine.json'
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'engine.json'
            dest.write_text(src.read_text(encoding='utf-8'), encoding='utf-8')
            proc = run([str(dest)])
            self.assertNotIn('no engine', proc.stdout + proc.stderr)
            self.assertIn(os.path.basename(tmp), proc.stdout)


if __name__ == '__main__':
    unittest.main(verbosity=2)
