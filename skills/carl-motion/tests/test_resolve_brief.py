#!/usr/bin/env python3
"""Behavior tests for the brief resolver. They call the CLI, not a mocked model.

Passing these tests does not mean an LLM followed SKILL.md. It means the
CLI classified the request and probed real files. A failure while
resolve_brief.py is absent only shows that entry was added; it is not a
regression test of the previous skill text.
"""
import hashlib, json, os, subprocess, sys, tempfile, unittest
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
SKILL = Path(__file__).resolve().parents[1]
SCRIPT = SKILL / 'scripts' / 'resolve_brief.py'
CATALOG = SKILL / 'references' / 'style-catalog.json'
PREVIEW = ROOT / 'assets' / 'previews' / 'risograph.webp'


def run(args, env_drop=('CARL_MOTION_SEARCH_CMD',)):
    env = os.environ.copy()
    for key in env_drop:
        env.pop(key, None)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True, text=True, env=env, cwd=str(ROOT),
    )
    return proc


def brief(args):
    proc = run(args)
    if proc.returncode != 0:
        raise AssertionError(f'exit {proc.returncode}\n{proc.stderr}\n{proc.stdout}')
    return json.loads(proc.stdout), proc


class ResolveBriefTest(unittest.TestCase):
    def test_known_style_decodes_preview_and_does_not_fetch_source_url(self):
        out, proc = brief(['--request', '用 Risograph 孔版套印做一家咖啡店开业'])
        self.assertEqual(out['decision'], 'exact')
        self.assertFalse(out['forced_preset'])
        self.assertEqual(len(out['styles']), 1)
        style = out['styles'][0]
        self.assertEqual(style['slug'], 'risograph')
        self.assertEqual(style['engine']['slug'], 'risograph')
        self.assertEqual(style['engine']['stack'], 'python')
        self.assertIsNone(out['retargeted_framework'])
        layer_a = next(r for r in style['references'] if r['layer'] == 'A')
        self.assertEqual(
            layer_a['url'],
            'https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles/risograph',
        )
        self.assertFalse(layer_a['fetched'])
        self.assertFalse(layer_a['decoded'])
        preview = style['local_preview']
        self.assertTrue(preview['exists'])
        self.assertTrue(preview['decoded'])
        self.assertEqual(preview['layer'], 'B')
        self.assertEqual(preview['by'], 'carl-motion')
        self.assertEqual(preview['frame_count'], 40)
        self.assertGreater(preview['canvas'][0], 0)
        self.assertGreater(preview['motion_mean_abs'], 1)
        self.assertTrue(preview['temporal'])
        self.assertFalse(preview['original_url_fetched'])
        self.assertFalse(preview['full_source_video'])
        self.assertFalse(preview['copied_frames_into_engine'])
        self.assertEqual(preview['application'], 'measured_color_and_motion_only')
        self.assertFalse(preview['used_as_video_reference'])
        self.assertFalse(out['claims']['video_guided_generation'])
        self.assertFalse(out['claims']['engine_consumes_reference_video'])
        self.assertFalse(out['claims']['may_claim_referenced_video'])
        self.assertFalse(out['claims']['may_claim_watched_link'])
        self.assertGreaterEqual(len(preview['colors']), 1)
        self.assertLessEqual(len(preview['colors']), 4)
        self.assertTrue(preview['path'].endswith('assets/previews/risograph.webp'))
        self.assertIsNone(out['search']['reminder'])
        self.assertFalse(out['steps']['style_parameters']['blocked'])
        self.assertIn('孔版套印', proc.stdout)
        # The prompt text of the card is not a substitute for the probe.
        self.assertNotEqual(preview['evidence'], 'prompt_text')

    def test_named_style_without_a_clip_does_not_pretend_the_poster_is_video(self):
        out, _ = brief(['--request', '虹彩迷幻Shader'])
        self.assertEqual(out['decision'], 'exact')
        self.assertEqual(out['styles'][0]['slug'], 'psychedelic-shader')
        self.assertIsNone(out['styles'][0]['engine'])
        preview = out['styles'][0]['local_preview']
        self.assertFalse(preview['decoded'])
        self.assertFalse(preview['used_as_video_reference'])
        self.assertEqual(preview['kind'], 'text_poster_not_a_reference')
        layer_b = next(r for r in out['styles'][0]['references'] if r['layer'] == 'B')
        self.assertIn('x.com/yama_kiyo', layer_b['url'])
        self.assertFalse(layer_b['fetched'])
        self.assertFalse(layer_b['decoded'])

    def test_flat_vector_keeps_its_python_engine(self):
        out, _ = brief(['--request', '扁平矢量讲解'])
        self.assertEqual(out['decision'], 'exact')
        self.assertEqual(out['styles'][0]['slug'], 'flat-vector')
        self.assertEqual(out['styles'][0]['engine']['stack'], 'python')

    def test_new_style_with_user_image_is_not_forced_onto_a_preset(self):
        fd, path = tempfile.mkstemp(suffix='.png')
        os.close(fd)
        try:
            img = Image.new('RGB', (32, 16), (10, 20, 200))
            for x in range(16, 32):
                for y in range(16):
                    img.putpixel((x, y), (200, 30, 40))
            img.save(path)
            digest = hashlib.sha256(Path(path).read_bytes()).hexdigest()
            out, _ = brief([
                '--request', '新画风：液态铬金属广告，镜面往下流，不要套进已有画风',
                '--media', path,
            ])
        finally:
            os.remove(path)
        self.assertEqual(out['decision'], 'custom')
        self.assertFalse(out['forced_preset'])
        self.assertEqual(out['styles'], [])
        ref = out['user_reference']
        self.assertTrue(ref['decoded'])
        self.assertEqual(ref['sha256'], digest)
        self.assertEqual(ref['kind'], 'still_image')
        self.assertFalse(ref['temporal'])
        self.assertCountEqual(out['style_parameters']['colors'], ['#0a14c8', '#c81e28'])
        self.assertIsNone(out['style_parameters']['type_px'])
        self.assertIsNone(out['style_parameters']['grid'])
        self.assertIsNone(out['style_parameters']['ease'])
        self.assertGreaterEqual(len(out['style_parameters']['bans']), 3)
        self.assertTrue(any(item['sha256'] == digest for item in out['facts']))
        self.assertFalse(any('0a14c8' in json.dumps(item, ensure_ascii=False) for item in out['inferences']))
        self.assertIsNone(out['retargeted_framework'])

    def test_new_style_without_media_asks_for_search_only_when_unavailable(self):
        out, _ = brief(['--request', '新画风：液态铬金属广告，镜面往下流'])
        self.assertEqual(out['decision'], 'no_preset')
        self.assertFalse(out['search']['available'])
        self.assertFalse(out['search']['attempted'])
        self.assertEqual(out['search']['results'], [])
        reminder = out['search']['reminder']
        self.assertIn('开放搜索权限', reminder)
        self.assertIn('X', reminder)
        self.assertIn('参考视频', reminder)
        self.assertTrue(out['steps']['style_parameters']['blocked'])
        self.assertFalse(out['steps']['house_spec']['blocked'])
        self.assertTrue(out['steps']['house_spec']['draft'])
        self.assertEqual(out['steps']['house_spec']['label'], '草稿')
        self.assertTrue(out['steps']['render']['blocked'])
        self.assertNotIn('https://x.com/', json.dumps(out['search']))
        self.assertFalse(out['claims']['may_claim_referenced_video'])
        self.assertFalse(out['claims']['video_guided_generation'])

    def test_authorized_search_is_used_without_asking_again(self):
        fd, path = tempfile.mkstemp(suffix='.json')
        os.close(fd)
        payload = {
            'results': [{
                'url': 'https://x.com/example/status/1',
                'title': 'liquid metal study',
                'source': 'x',
            }],
        }
        Path(path).write_text(json.dumps(payload), encoding='utf-8')
        try:
            out, _ = brief([
                '--request', '新画风：液态铬金属广告，镜面往下流',
                '--search-file', path,
            ])
        finally:
            os.remove(path)
        self.assertTrue(out['search']['available'])
        self.assertTrue(out['search']['attempted'])
        self.assertFalse(out['search']['refused'])
        self.assertIsNone(out['search']['reminder'])
        self.assertEqual(out['search']['result_count'], 1)
        self.assertEqual(out['search']['results'][0]['url'], 'https://x.com/example/status/1')
        self.assertFalse(out['search']['results'][0]['decoded'])
        self.assertFalse(out['search']['results'][0]['opened'])
        self.assertTrue(out['steps']['style_parameters']['blocked'])
        self.assertFalse(out['steps']['house_spec']['blocked'])
        blob = json.dumps(out, ensure_ascii=False)
        self.assertNotIn('开放搜索权限', blob)

    def test_search_command_runs_and_empty_or_refused_stays_honest(self):
        fd, script = tempfile.mkstemp(suffix='.py')
        os.close(fd)
        Path(script).write_text(
            'import json,sys\n'
            'json.dump({"query": sys.stdin.read(), "results": []}, sys.stdout)\n',
            encoding='utf-8',
        )
        try:
            empty, _ = brief([
                '--request', '新画风：液态铬金属广告',
                '--search-cmd', f'{sys.executable} {script}',
            ])
        finally:
            os.remove(script)
        self.assertTrue(empty['search']['attempted'])
        self.assertEqual(empty['search']['result_count'], 0)
        self.assertIn('没有结果', empty['search']['message'])
        self.assertIsNone(empty['search']['reminder'])
        self.assertTrue(empty['steps']['style_parameters']['blocked'])
        self.assertNotIn('开放搜索权限', json.dumps(empty, ensure_ascii=False))

        refused, _ = brief([
            '--request', '新画风：液态铬金属广告',
            '--search-refused', 'permission denied',
        ])
        self.assertTrue(refused['search']['refused'])
        self.assertTrue(refused['search']['attempted'])
        self.assertEqual(refused['search']['results'], [])
        self.assertIn('permission denied', refused['search']['message'])
        self.assertIsNone(refused['search']['reminder'])
        self.assertTrue(refused['steps']['style_parameters']['blocked'])
        self.assertTrue(refused['steps']['house_spec']['draft'])

    def test_mixed_styles_and_dead_link_are_not_an_exact_read(self):
        out, _ = brief([
            '--request', '既要玻璃拟态也要霓虹复古',
            '--media-url', 'http://127.0.0.1:1/missing-reference.mp4',
        ])
        self.assertEqual(out['decision'], 'mixed')
        self.assertFalse(out['forced_preset'])
        slugs = {s['slug'] for s in out['styles']}
        self.assertEqual(slugs, {'glassmorphism-ui', 'neon-synthwave'})
        self.assertTrue(all(s['match'] != 'exact' for s in out['styles']))
        self.assertFalse(out['user_reference']['opened'])
        self.assertFalse(out['user_reference']['decoded'])
        self.assertTrue(out['user_reference']['error'])
        self.assertTrue(out['steps']['render']['blocked'])
        for style in out['styles']:
            for ref in style['references']:
                self.assertFalse(ref['fetched'])
                self.assertFalse(ref['decoded'])

    def test_keyword_overlap_is_a_candidate_not_an_exact_match(self):
        out, _ = brief(['--request', '标题用勒索信拼字'])
        self.assertEqual(out['decision'], 'candidate')
        self.assertEqual(out['styles'][0]['slug'], 'retro-paper-collage')
        self.assertEqual(out['styles'][0]['match'], 'keyword')
        self.assertFalse(out['forced_preset'])
        self.assertTrue(out['steps']['render']['blocked'])

    def test_user_can_approve_a_draft_without_claiming_a_video(self):
        blocked, _ = brief(['--request', '新画风：液态铬金属广告，镜面往下流'])
        self.assertTrue(blocked['steps']['render']['blocked'])
        out, _ = brief([
            '--request', '新画风：液态铬金属广告，镜面往下流',
            '--approve-unreferenced-draft',
        ])
        self.assertEqual(out['decision'], 'no_preset')
        self.assertTrue(out['approved_unreferenced_draft'])
        self.assertFalse(out['steps']['render']['blocked'])
        self.assertEqual(out['steps']['house_spec']['label'], '用户已批准的无参考草稿')
        self.assertTrue(out['steps']['style_parameters']['blocked'])
        self.assertEqual(out['style_parameters']['colors'], [])
        self.assertFalse(out['claims']['may_claim_referenced_video'])
        self.assertFalse(out['claims']['video_guided_generation'])
        self.assertFalse(out['claims']['engine_consumes_reference_video'])

    def test_rejecting_presets_does_not_lock_a_named_style(self):
        out, _ = brief(['--request', '新画风，不要套进已有画风，即使有人提到 risograph'])
        self.assertNotEqual(out['decision'], 'exact')
        self.assertFalse(out['forced_preset'])
        self.assertEqual(out['decision'], 'no_preset')
        self.assertIn('risograph', out['nearby_not_selected'])

    def test_audit_covers_every_style_and_leaves_engines_alone(self):
        before = (SKILL / 'scenes' / 'risograph' / 'engine.json').read_bytes()
        out, _ = brief(['--audit'])
        after = (SKILL / 'scenes' / 'risograph' / 'engine.json').read_bytes()
        self.assertEqual(before, after)
        self.assertEqual(out['styles'], 29)
        self.assertEqual(out['with_engine'], 20)
        self.assertEqual(out['exact_on_own_name'], 29)
        self.assertEqual(out['hyperframes_engines'], 0)
        self.assertGreaterEqual(out['decoded_previews'], 20)
        self.assertGreaterEqual(out['text_posters_not_used_as_video'], 1)
        urls = {item['url'] for item in out['reference_links'] if item['url']}
        self.assertIn('https://x.com/yama_kiyo/status/2103740786177134910', urls)
        self.assertIn('https://x.com/maxescu/status/2104898184442962277', urls)
        self.assertTrue(all(item['fetched'] is False for item in out['reference_links']))
        self.assertTrue(PREVIEW.exists())
        self.assertTrue(CATALOG.exists())


if __name__ == '__main__':
    unittest.main(verbosity=2)
