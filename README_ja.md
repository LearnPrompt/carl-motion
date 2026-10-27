[English](./README.md) | [中文](./README_zh.md) | **[日本語](./README_ja.md)**

<img src="./assets/style-wall.webp" width="100%" alt="carl-motion スタイルウォール：29 種類のモーショングラフィックスが同時に再生">

# carl-motion

**29 種類のモーショングラフィックス・スタイル、それぞれにコピペで使えるプロンプト付き。** 紙コラージュ、シンセウェイヴ、水墨画、木版画、点群、クレイアニメ、リソグラフ、グラスUI など。どのスタイルにも 8 秒のサンプル、プロンプト、崩れやすいポイントがあり、そのうち 20 種類はサンプルをレンダリングしたソースコードも同梱しています。

Skill を入れて、エージェントに「リソグラフ風で私のテーマを作って」と頼むだけです：

```bash
npx skills add LearnPrompt/carl-motion
```

Claude Code ではプラグインとしても使えます：`/plugin marketplace add LearnPrompt/carl-motion` のあと `/plugin install carl-motion@carl-motion`。

## 目次

- [まず試す](#まず試す)
- [29 のスタイル](#29-のスタイル)
- [Skill](#skill)
- [テンプレートとソース](#テンプレートとソース)
- [サンプルの作り方](#サンプルの作り方)
- [上流の Skill と参考](#上流の-skill-と参考)
- [素材とライセンス](#素材とライセンス)
- [謝辞](#謝辞)
- [作者](#作者)

## まず試す

最初はインストール不要です。下のギャラリーから好きな見た目を選んでページを開き、プロンプトをコピーして「your topic / 你的主题」の部分を自分のテーマに置き換えます。Claude、ChatGPT などコードを書けるモデルに貼り、1920×1080、30 fps、8 秒の MP4 を頼んでください。うまくいかなければ、そのページの「崩れやすいポイント」を読んでもう一度。スタイル別ページは英語と中国語です。

## 29 のスタイル

並び順は、これらをまとめた紹介動画と同じです。隣り合うスタイルはおおむね補色関係になるよう並べてあり、切り替わりがひと目でわかります。29 種類のうち 24 種類はここで動きを見られます。残りの 5 種類は再配布できない第三者のサンプルしかないため、ページから出典にリンクしています。

<table>
<tr>
<td width="33%" valign="top" align="center"><a href="./docs/styles/retro-paper-collage.md"><img src="./assets/previews/retro-paper-collage.webp" width="260" alt="Retro Paper Collage"></a><br><b>01 · レトロ紙コラージュ</b><br><sub>Retro Paper Collage</sub><br><sub>ソースあり</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/product-ui-2-5d.md"><img src="./assets/posters/product-ui-2-5d.jpg" width="260" alt="Product UI 2.5D Camera"></a><br><b>02 · プロダクトUI 2.5Dカメラ</b><br><sub>Product UI 2.5D Camera</sub><br><sub>プロンプト＋出典</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/neon-synthwave.md"><img src="./assets/previews/neon-synthwave.webp" width="260" alt="Neon Synthwave"></a><br><b>03 · ネオン・シンセウェイヴ</b><br><sub>Neon Synthwave</sub><br><sub>ソースあり</sub></td>
</tr>
<tr>
<td width="33%" valign="top" align="center"><a href="./docs/styles/hand-drawn-notes.md"><img src="./assets/posters/hand-drawn-notes.jpg" width="260" alt="Hand-drawn Paper Notes"></a><br><b>04 · 手描きペーパーノート</b><br><sub>Hand-drawn Paper Notes</sub><br><sub>プロンプト＋出典</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/watercolor.md"><img src="./assets/previews/watercolor.webp" width="260" alt="Watercolor"></a><br><b>05 · 水彩</b><br><sub>Watercolor</sub><br><sub>ソースあり</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/woodcut.md"><img src="./assets/previews/woodcut.webp" width="260" alt="Black-and-white Woodcut"></a><br><b>06 · 白黒木版画</b><br><sub>Black-and-white Woodcut</sub><br><sub>ソースあり</sub></td>
</tr>
<tr>
<td width="33%" valign="top" align="center"><a href="./docs/styles/soft-inflatable-3d.md"><img src="./assets/previews/soft-inflatable-3d.webp" width="260" alt="Soft Inflatable 3D"></a><br><b>07 · ふわふわインフレータブル3D</b><br><sub>Soft Inflatable 3D</sub><br><sub>ソースあり</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/point-cloud-survey.md"><img src="./assets/previews/point-cloud-survey.webp" width="260" alt="Point-cloud Survey"></a><br><b>08 · 点群測量</b><br><sub>Point-cloud Survey</sub><br><sub>ソースあり</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/blueprint.md"><img src="./assets/previews/blueprint.webp" width="260" alt="Blueprint Drawing"></a><br><b>09 · 青図ドローイング</b><br><sub>Blueprint Drawing</sub><br><sub>ソースあり</sub></td>
</tr>
<tr>
<td width="33%" valign="top" align="center"><a href="./docs/styles/sticker-explainer.md"><img src="./assets/previews/sticker-explainer.webp" width="260" alt="Die-cut Sticker Explainer"></a><br><b>10 · ダイカットステッカー解説</b><br><sub>Die-cut Sticker Explainer</sub><br><sub>ソースあり</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/feature-3d-character.md"><img src="./assets/posters/feature-3d-character.jpg" width="260" alt="Feature-film 3D Character"></a><br><b>11 · 長編アニメ風3Dキャラクター</b><br><sub>Feature-film 3D Character</sub><br><sub>プロンプト＋出典</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/chinese-ink-wash.md"><img src="./assets/previews/chinese-ink-wash.webp" width="260" alt="Chinese Ink Wash"></a><br><b>12 · 水墨画</b><br><sub>Chinese Ink Wash</sub><br><sub>ソースあり</sub></td>
</tr>
<tr>
<td width="33%" valign="top" align="center"><a href="./docs/styles/ascii-crt.md"><img src="./assets/previews/ascii-crt.webp" width="260" alt="ASCII Character Visuals"></a><br><b>13 · ASCII文字ビジュアル</b><br><sub>ASCII Character Visuals</sub><br><sub>プロンプト＋出典</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/isometric-world.md"><img src="./assets/previews/isometric-world.webp" width="260" alt="Isometric 2.5D World"></a><br><b>14 · アイソメトリック2.5Dワールド</b><br><sub>Isometric 2.5D World</sub><br><sub>プロンプト＋出典</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/van-gogh-impasto.md"><img src="./assets/previews/van-gogh-impasto.webp" width="260" alt="Van Gogh Impasto"></a><br><b>15 · ゴッホ風厚塗り</b><br><sub>Van Gogh Impasto</sub><br><sub>ソースあり</sub></td>
</tr>
<tr>
<td width="33%" valign="top" align="center"><a href="./docs/styles/psychedelic-shader.md"><img src="./assets/posters/psychedelic-shader.jpg" width="260" alt="Iridescent Psychedelic Shader"></a><br><b>16 · 虹色サイケデリック・シェーダー</b><br><sub>Iridescent Psychedelic Shader</sub><br><sub>プロンプト＋出典</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/claymation.md"><img src="./assets/previews/claymation.webp" width="260" alt="Claymation Stop-motion"></a><br><b>17 · クレイアニメ</b><br><sub>Claymation Stop-motion</sub><br><sub>ソースあり</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/pixel-game.md"><img src="./assets/posters/pixel-game.jpg" width="260" alt="Pixel Game"></a><br><b>18 · ピクセルゲーム</b><br><sub>Pixel Game</sub><br><sub>プロンプト＋出典</sub></td>
</tr>
<tr>
<td width="33%" valign="top" align="center"><a href="./docs/styles/flat-vector.md"><img src="./assets/previews/flat-vector.webp" width="260" alt="Flat Vector"></a><br><b>19 · フラットベクター</b><br><sub>Flat Vector</sub><br><sub>ソースあり</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/monet-impressionist.md"><img src="./assets/previews/monet-impressionist.webp" width="260" alt="Impressionist Oil (Monet)"></a><br><b>20 · 印象派油彩（モネ）</b><br><sub>Impressionist Oil (Monet)</sub><br><sub>ソースあり</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/particle-morph.md"><img src="./assets/previews/particle-morph.webp" width="260" alt="Particle Morph"></a><br><b>21 · パーティクルモーフ</b><br><sub>Particle Morph</sub><br><sub>ソースあり</sub></td>
</tr>
<tr>
<td width="33%" valign="top" align="center"><a href="./docs/styles/white-model-projection.md"><img src="./assets/previews/white-model-projection.webp" width="260" alt="White-model Projection"></a><br><b>22 · ホワイトモデル・プロジェクション</b><br><sub>White-model Projection</sub><br><sub>ソースあり</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/egyptian-mural.md"><img src="./assets/previews/egyptian-mural.webp" width="260" alt="Ancient Egyptian Mural"></a><br><b>23 · 古代エジプト壁画</b><br><sub>Ancient Egyptian Mural</sub><br><sub>ソースあり</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/exploded-view.md"><img src="./assets/previews/exploded-view.webp" width="260" alt="Product Exploded View"></a><br><b>24 · 製品分解図</b><br><sub>Product Exploded View</sub><br><sub>ソースあり</sub></td>
</tr>
<tr>
<td width="33%" valign="top" align="center"><a href="./docs/styles/editorial-dataviz.md"><img src="./assets/previews/editorial-dataviz.webp" width="260" alt="Editorial Paper Data Story"></a><br><b>25 · 紙のエディトリアル・データストーリー</b><br><sub>Editorial Paper Data Story</sub><br><sub>プロンプト＋出典</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/glassmorphism-ui.md"><img src="./assets/previews/glassmorphism-ui.webp" width="260" alt="Glassmorphism UI"></a><br><b>26 · グラスモーフィズムUI</b><br><sub>Glassmorphism UI</sub><br><sub>ソースあり</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/brick-toy.md"><img src="./assets/previews/brick-toy.webp" width="260" alt="Brick Toy"></a><br><b>27 · ブロック玩具</b><br><sub>Brick Toy</sub><br><sub>ソースあり</sub></td>
</tr>
<tr>
<td width="33%" valign="top" align="center"><a href="./docs/styles/risograph.md"><img src="./assets/previews/risograph.webp" width="260" alt="Risograph Print"></a><br><b>28 · リソグラフ印刷</b><br><sub>Risograph Print</sub><br><sub>ソースあり</sub></td>
<td width="33%" valign="top" align="center"><a href="./docs/styles/scifi-hud.md"><img src="./assets/previews/scifi-hud.webp" width="260" alt="Sci-fi Scan HUD"></a><br><b>29 · SFスキャンHUD</b><br><sub>Sci-fi Scan HUD</sub><br><sub>プロンプト＋出典</sub></td>
</tr>
</table>

## Skill

`carl-motion` はこのライブラリをコーディングエージェントで使える形にしたものです。スタイル名でも、「フラット、あたたかい、手作り感」のような雰囲気でも頼めます。エージェントは一番近いスタイルを選び、プロンプトにテーマを入れ、既知の崩れポイントと照らし合わせます。ソースがあるスタイルは、白紙からではなくそのエンジンから作り始めます。各カードにはそのスタイルがどこまで検証済みか（実装済み、上流のみ、研究段階）が書かれていて、完成したクリップは同じ納品ゲートを通ります。

| | スタイルページ | Skill |
|---|---|---|
| 対象 | どなたでも、インストール不要 | Claude Code、Codex などのコーディングエージェント |
| 使い方 | コピーしてテーマを差し替えて貼るだけ | `npx skills add LearnPrompt/carl-motion` のあと頼むだけ |
| 得られるもの | プロンプト 1 本 | プロンプト、レンダリング計画、崩れポイントのチェック |

## テンプレートとソース

**スタイルエンジン。** 20 種類のスタイルに、B クリップをレンダリングしたコードが付いています。すべて 1920×1080、30 fps、240 フレームです。どのエンジンも入口は同じ `./render.sh <作業フォルダ>` で、240 枚の PNG を書き出し、`scripts/deliver.py` がエンコードして赤・黄・緑の判定を返します。始める前に `scripts/doctor.py <エンジン>` で環境を確認できます。取り決めは [scene-contract.md](skills/carl-motion/references/scene-contract.md) にあります。

| フォルダ | スタイル | 技術スタック |
|---|---|---|
| [`retro-paper-collage`](skills/carl-motion/scenes/retro-paper-collage) | レトロ紙コラージュ | Python (NumPy + OpenCV + Pillow) |
| [`neon-synthwave`](skills/carl-motion/scenes/neon-synthwave) | ネオン・シンセウェイヴ | Blender + Python |
| [`watercolor`](skills/carl-motion/scenes/watercolor) | 水彩 | Python (NumPy + OpenCV + Pillow) |
| [`woodcut`](skills/carl-motion/scenes/woodcut) | 白黒木版画 | Python (NumPy + OpenCV + Pillow) |
| [`soft-inflatable-3d`](skills/carl-motion/scenes/soft-inflatable-3d) | ふわふわインフレータブル3D | Blender + Python |
| [`point-cloud-survey`](skills/carl-motion/scenes/point-cloud-survey) | 点群測量 | Blender + Python |
| [`blueprint`](skills/carl-motion/scenes/blueprint) | 青図ドローイング | Python (NumPy + OpenCV + Pillow) |
| [`sticker-explainer`](skills/carl-motion/scenes/sticker-explainer) | ダイカットステッカー解説 | Python (NumPy + OpenCV + Pillow) |
| [`chinese-ink-wash`](skills/carl-motion/scenes/chinese-ink-wash) | 水墨画 | Python (NumPy + OpenCV + Pillow) |
| [`huashu-portraits`](skills/carl-motion/scenes/huashu-portraits) | ゴッホ風厚塗り / 印象派油彩（モネ） / 古代エジプト壁画 | Node + Canvas / headless Chrome |
| [`claymation`](skills/carl-motion/scenes/claymation) | クレイアニメ | Blender + Python |
| [`flat-vector`](skills/carl-motion/scenes/flat-vector) | フラットベクター | Python (NumPy + OpenCV + Pillow) |
| [`particle-morph`](skills/carl-motion/scenes/particle-morph) | パーティクルモーフ | Python (NumPy + OpenCV + Pillow) |
| [`white-model-projection`](skills/carl-motion/scenes/white-model-projection) | ホワイトモデル・プロジェクション | Blender + Python |
| [`exploded-view`](skills/carl-motion/scenes/exploded-view) | 製品分解図 | Blender + Python |
| [`glassmorphism-ui`](skills/carl-motion/scenes/glassmorphism-ui) | グラスモーフィズムUI | Node + Canvas / headless Chrome |
| [`brick-toy`](skills/carl-motion/scenes/brick-toy) | ブロック玩具 | Blender + Python |
| [`risograph`](skills/carl-motion/scenes/risograph) | リソグラフ印刷 | Python (NumPy + OpenCV + Pillow) |

**9:16 解説レイアウト。** [`skills/carl-motion/pipeline/script_layout.py`](skills/carl-motion/pipeline/script_layout.py) は同じスタイルの 2 本のクリップを上下に重ね、上にタイトルバーを固定します。結果を先に見せる作りで、各スタイルの 0 フレーム目からスタイル名と、すでに半分まで書かれたプロンプトカードが表示され、残りはモデルの出力のように流れ込み、5.4 秒で注意帯が入ります。右側の枠は話し手の撮影用プレースホルダーです。

<img src="./assets/layout-9x16.jpg" width="300" alt="9:16 レイアウト：A と B を上下に重ね、下にプロンプトカードと注意帯">

**パイプライン。** [`skills/carl-motion/pipeline`](skills/carl-motion/pipeline) には紹介動画を作ったツールもあります。補色で並べる `color_order_v4.py`、完成動画の切り替わりを測り直す `color_stitch_verify.py`、CIELAB でオープニング候補を採点する `opener_salience.py` など。詳しくは [README](skills/carl-motion/pipeline/README.md) を参照してください。

## サンプルの作り方

各スタイルは 8 秒のクリップ 2 本の組です。A は上流の参考、B は同じスタイルで題材を変えた 2 本目で、見た目が別のテーマにも移せることを示します。B のうち 20 本はこのリポジトリのために Claude Opus 5.5 がゼロからコードを書いてレンダリングしたもので、スタイルプロンプトと A を参考にしています。そのうち 7 本は、猫が最初の農村に住みついた話を、それぞれのスタイルでリレーしています。どのクリップも同じチェックを通しています：1920×1080、30 fps、ちょうど 240 フレーム、完全デコード、黒フレームなし、検出されたジャンプフレームは目視で確認済み。

## 上流の Skill と参考

このライブラリは以下のオープンなスタイル Skill と公開ギャラリーの上に作られています。各スタイルページから対応する上流プロンプトにリンクしています。

| 上流 | 使ったもの | ライセンス |
|---|---|---|
| [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 29 スタイルのうち 13 のレシピとデモ映像（青図、水彩、水墨、木版、点群、ホワイトモデル、分解図、ブロック玩具、リソグラフ、ASCII、アイソメトリック、データ、HUD） | プロンプトとコードは MIT、デモ映像は CC BY 4.0 |
| [Vincentwei1021/mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15) | コラージュ、フラットベクター、ステッカー解説、グラスUI、シンセウェイヴ、ソフト3D、アイソメトリック、HUD のスタイルプロンプト | MIT（プロンプトとコード） |
| [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | エジプト壁画、ゴッホ、モネの描画エンジン。A クリップはこのソースから再レンダリング | MIT |
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | プロダクトUIのプロモーションとリソグラフのズレの参考 | 上流に準拠 |
| [prompt-motion.com](https://prompt-motion.com) | ピクセル、クレイ、3Dキャラクター、手描きノート、シェーダー、パーティクル、ASCII の公開参考 | リンクのみ |
| [yasue.org の Opus 5.5 動画生成の限界を試す記事](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits) | 英語解説クリップ 7 本が語り直している、猫が村に住みついた話 | リンクのみ |

## 素材とライセンス

コード、プロンプト、私たちがレンダリングしたクリップは MIT です（`skills/` 以下すべてと、「ソースあり」のスタイルの `assets/` プレビュー）。4 種類のスタイルのプレビューは LemoLab のデモ映像で、CC BY 4.0 に従いページでクレジットしています。prompt-motion.com、X、yasue.org、video-shotcraft のクリップはリポジトリに複製せず、リンクのみです。9:16 のサンプルフレームは huashu（MIT）の A と私たちの B を使っています。

## 謝辞

- オープンなスタイルレシピ：[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)、[Vincentwei1021/mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15)、[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)
- 公開参考：[prompt-motion.com](https://prompt-motion.com)、[yasue.org](https://en.yasue.org/article/pushing-opus-5-5-video-generation-limits)
- ギャラリー＋Skill の構成：[LearnPrompt/awesome-seedance](https://github.com/LearnPrompt/awesome-seedance)

## 作者

**Carl（@卡尔的AI沃茨）** は GoodCase の発起人で、このリポジトリのメンテナーです。ByteDance、Alibaba、Baidu で 6 年間大規模モデルの研究開発に携わったあと AI 映像に転向し、AI 短編は中国のテレビ局でも放送されました。各プラットフォームの合計フォロワーは 50 万人以上。[X @aiwarts](https://x.com/aiwarts) で発信しています。お問い合わせや協業は [carl@goodcase.ai](mailto:carl@goodcase.ai) まで。
