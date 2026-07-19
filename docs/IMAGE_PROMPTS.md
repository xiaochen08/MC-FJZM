# 专业宣传图 AI 生图提示词

本套包含一张内部视觉基准图和六张正式宣传图。逐张生成，先完成 P00，再把 P00 作为 P01–P06 的第一张参考图。P03 还需要上传真实 Blockbench 截图。

## 推荐参数

- 比例：16:9
- 分辨率：优先 3840×2160，其次 2048×1152
- 质量：High
- 格式：PNG、sRGB
- 一次只生成一张不同用途的图片

## P00：视觉基准图

文件名：`P00-visual-anchor.png`

```text
Use case: stylized-concept
Asset type: internal visual identity anchor and Blockbench-compatible model sheet

Primary request:
Create a clean, highly consistent model sheet for one original Minecraft-compatible crystal defense tower. The complete asset must be realistically reproducible in Blockbench using cuboids and simple rotated rectangular panels.

Scene/backdrop:
Near-black Blockbench-style checker grid with subtle cold studio floor lines. No environmental scenery and no cinematic battlefield.

Subject:
A tall square black-iron defense tower with a broad layered square base, four symmetrical corner pylons, an open framed central column, exactly four cyan cuboid energy cells inside the column, visible vertical energy delivery from bottom to top, a compact mechanical crown, a stepped luminous cyan crystal emitter on top, and exactly two identical long black-iron protective shield panels.

Critical shield geometry:
The two shield panels remain exactly 180 degrees apart, orbit around the upper crystal in the same direction, face toward the crystal while orbiting, use the same orientation logic, remain at a visibly wide orbital radius, keep a clear air gap, never touch the crystal, never overlap each other, never intersect the tower, and never spin around their own centers.

Style/medium:
Premium voxel and cuboid game asset. Authentic Blockbench viewport presentation. Dark science-fantasy industrial design. Polished Minecraft-style pixel textures. No freeform sculpting and no smooth organic surfaces.

Composition/framing:
Landscape model sheet. One large three-quarter hero view in the center. Smaller front, side, rear, top, idle-state and attack-state views around it. Every view shows exactly the same geometry, proportions, shield count and energy-cell count.

Lighting/mood:
Controlled cool-gray studio key light, cyan emissive rim light and restrained shadows. Every joint, shield, frame and energy cell remains readable.

Color palette:
Near black #070A0F, black iron #171D25, gunmetal #465262, cyan energy #46EAF7, deep energy blue #1584D8.

Materials/textures:
Matte black iron, gunmetal trims, subtle scratches and edge wear, pixel-painted highlights and shadows, cyan cuboid energy glass. Emissive areas remain separated from ordinary metal.

Constraints:
Cuboids and simple Blockbench rotations only. Exactly two shield panels. Exactly four central energy cells. No smooth curves, extra floating parts, arrows, annotations, transform gizmos, text, logos or watermark. No smoke hiding geometry. Strong cross-view consistency is mandatory.
```

## P01：官方主视觉

文件名：`P01-official-hero.png`

上传：`P00-visual-anchor.png`

```text
Use case: ads-marketing
Asset type: official 16:9 campaign hero for a professional Minecraft Blockbench production workflow

Input images:
Image 1 is the immutable visual identity reference. Preserve the tower geometry, layered base, four energy cells, stepped cyan crystal, black-iron materials and exactly two separated shield panels.

Primary request:
Create a premium dark game advertising hero for the Chinese brand “方界造模”.

Scene/backdrop:
Cavernous black industrial game-development chamber, subtle Blockbench grid, faint cuboid wireframe architecture and restrained cyan haze. No battlefield or unrelated fantasy scenery.

Subject:
Place the same crystal tower slightly right of center. Its left half transitions into clean cuboid wireframe, modeling groups, rotation pivots and construction grid. Its right half becomes the complete pixel-textured game asset. Both halves align perfectly as the same model, proportions and camera angle.

Style/medium:
Premium AAA dark science-fantasy campaign art combined with credible Blockbench development visualization. Professional game-production advertising, not generic AI technology art.

Composition/framing:
Wide 16:9, strong central silhouette, clean upper-left headline space, fully visible tower, base and shields.

Lighting/mood:
Deep black environment, cold cyan rim light, controlled white edge light, sparse red status accents and subtle dark-metal floor reflection.

Text (verbatim):
“方界造模”
“让想象，按确认过的样子进入游戏。”

Typography:
Exact Chinese text once each. Bold condensed modern Chinese sans-serif. Crisp white headline with a restrained cyan accent in the upper-left. No extra text.

Constraints:
Preserve Image 1 identity. Exactly two shields with clear distance from the crystal. Cuboid geometry only. Wireframe and finished model match. No Minecraft or Blockbench logo, watermark, fake code, excessive smoke, extra towers or misspelled characters.
```

## P02：需求确认与三套方案

文件名：`P02-approval-workflow.png`

上传：`P00-visual-anchor.png`

```text
Use case: ads-marketing
Asset type: professional 16:9 approval-first workflow campaign slide

Input images:
Image 1 is the visual identity reference for the crystal defense tower.

Primary request:
Visualize a strict user-approval workflow before Blockbench production: Chinese requirement intake, structured design brief, three separate buildable concept options A/B/C, explicit user selection of option B, then permission to enter formal modeling.

Scene/backdrop:
Dark professional game-development interface, near-black and gunmetal panels, subtle cyan modeling grid, no fantasy landscape.

Layout:
Four stages from left to right. Stage 1 is a minimal conversation card with short neutral line symbols and a tower silhouette. Stage 2 is a structured specification card with geometry, texture, animation, particle and sound icons. Stage 3 contains exactly three concept cards labeled A, B and C, all from the same cuboid tower family with meaningful buildable variations. Stage 4 enlarges option B with a cyan approval border and check mark.

Style/medium:
Premium dark game product campaign, practical UI visualization, crisp professional art direction and restrained cyan glow.

Text (verbatim):
“先确认，再生产”
“需求问诊 → 三套方案 → 用户选择 → 正式建模”

Typography:
Exact Chinese headline once and workflow line once. Labels A, B and C exact.

Constraints:
B clearly selected. Exactly three concepts. No fourth option and no production before approval. Cuboid geometry only. No unrelated characters, logos, watermark, gibberish text, fake code or extra paragraphs.
```

## P03：Blockbench 直观建模演示

文件名：`P03-blockbench-demonstration.png`

上传：`P00-visual-anchor.png` 和真实 Blockbench 截图。

```text
Use case: ads-marketing
Asset type: professional Blockbench modeling demonstration campaign slide

Input images:
Image 1 is the approved crystal-tower identity reference. Image 2 is a real Blockbench screenshot and must remain technically recognizable.

Primary request:
Create a direct, credible comparison between an actual Blockbench production workspace and the finished in-game crystal defense tower. Preserve the software credibility of Image 2. Do not redesign Blockbench into a fictional holographic interface.

Scene/backdrop:
Dark black-and-gunmetal campaign background, subtle cyan modeling grid and minimal industrial framing around the real screenshot.

Layout:
Left 60 percent shows the authentic Blockbench modeling viewport, cuboid geometry, Outliner or hierarchy, UV panel, animation timeline, bone groups and rotation pivots. Right 40 percent shows the same finished tower with matching geometry, black-iron texture, cyan energy cells, emissive crystal and fully visible shields. Thin cyan connectors map geometry, texture, skeleton and animation to the result.

Style/medium:
Professional game-development case study and dark science-fantasy campaign design, not cinematic concept art pretending to be software.

Text (verbatim):
“概念图 ≈ Blockbench 成果”
“结构可还原”
“骨骼可控制”
“动画可验证”
“资产可导出”

Constraints:
Keep the real interface recognizable. Do not invent random menus or code. Preserve the tower identity, exactly two shields, safe spacing and cuboid geometry. No watermark or gibberish text.
```

## P04：完整动画系统

文件名：`P04-animation-system.png`

上传：`P00-visual-anchor.png`

```text
Use case: infographic-diagram
Asset type: professional dark-game animation-system campaign slide

Input images:
Image 1 is the immutable tower identity reference. Every state shows the same tower, proportions, shields and energy cells.

Primary request:
Create a six-stage animation sequence: Idle, Activation, Charging, Attack, Cooldown and Return. Add a lower damage branch: Damaged, Critical Damage and Collapse/Wreck.

Visual behavior:
Idle keeps the shields symmetrically beside the crystal with low glow. Activation deploys them immediately without collision. Charging moves cyan cuboid energy cells from the bottom upward. Attack makes both shields orbit in the same direction, 180 degrees apart, facing the crystal without self-spin. Cooldown keeps them orbiting for three to five seconds. Return smoothly slows and restores idle positions. Damage states show cracked iron, cyan leakage and final collapse or wreck.

Style/medium:
Professional dark science-fantasy animation infographic, Blockbench-compatible cuboid asset and clear keyframe presentation.

Composition/framing:
Wide 16:9. Six large frames across the main row and three smaller damage frames below. Clean arrows and readable state path.

Text (verbatim):
“完整动画，不只是几个关键帧”
“待机” “启动” “蓄力” “攻击” “冷却” “归位”
“受损” “严重损毁” “残骸”

Constraints:
Exactly two shields in every intact state. Same orbit direction and orientation logic. Wide safety distance, no overlap, penetration or instant return. No tower identity drift, extra states, logos, watermark or gibberish text.
```

## P05：完整系统联动

文件名：`P05-full-system-integration.png`

上传：`P00-visual-anchor.png`

```text
Use case: infographic-diagram
Asset type: professional full-system game-asset integration campaign slide

Input images:
Image 1 is the immutable crystal defense tower identity reference.

Primary request:
Show the complete runtime relationship between model, animation, particles, sound events, projectile and Minecraft Java Mod logic.

Central subject:
The approved black-iron tower with exactly two separated shields, four internal cyan energy cells and stepped crystal.

Surrounding modules:
Model and skeleton; animation state machine; particle and energy effects; sound-event mapping; Mod runtime logic; independent energy projectile.

Event chain:
Target detected → Activation → Charging → Projectile fired → Impact → Cooldown.

Visual behavior:
Energy cells move upward, the crystal brightens, shields orbit during attack, one cyan cuboid projectile launches, impact creates a controlled cyan burst, sound uses clean waveform icons and Mod logic uses event nodes rather than fake code.

Style/medium:
Premium dark science-fantasy technical campaign and professional game-production infographic. Readable and restrained.

Text (verbatim):
“模型 × 动画 × 粒子 × 音效 × Mod”
“每一次动作，都能被准确触发。”
“发现目标” “启动” “蓄力” “发射” “命中” “冷却”

Constraints:
Preserve tower identity. Exactly two shields and one projectile in the launch demonstration. No fake code, random labels, unrelated UI, logos, watermark or gibberish text.
```

## P06：独立工作区与交付

文件名：`P06-asset-delivery.png`

上传：`P00-visual-anchor.png`

```text
Use case: infographic-diagram
Asset type: professional asset-isolation and delivery campaign slide

Input images:
Image 1 is the crystal defense tower identity reference.

Primary request:
Visualize the principle: one independent model, one independent workspace, no file mixing, no silent overwriting, full verification and delivery.

Scene/backdrop:
Dark near-black professional game-asset interface, gunmetal cards and subtle cyan grid.

Left-side assets:
Main crystal tower, independent cyan energy projectile, destroyed-tower wreck model and crystal-core dropped item. Each has a separate silhouette, identity marker and folder card.

Right-side folders:
Four separated professional folder containers with icons representing source model, textures, animations, audio, particles, previews, exports and evidence.

Bottom delivery chain:
.bbmodel, texture atlas, animation files, audio events, particle contract, runtime exports and validation report.

Style/medium:
Premium dark technical game campaign, organized and trustworthy asset-pipeline infographic.

Text (verbatim):
“一个模型，一个独立工作区”
“不混放 · 不覆盖 · 可追踪 · 可验证 · 可交付”

Constraints:
One asset maps to one folder. No cross-asset mixing, duplicate tower, fake Windows Explorer, unreadable filenames, random code, logos, watermark or gibberish text.
```

## 通用负面约束

```text
low quality, blurry model, rough geometry, smooth organic sculpting, curved surfaces, inconsistent tower design, different model across panels, extra shields, missing shields, overlapping shields, shields touching crystal, self-spinning shields, intersecting geometry, broken perspective, random floating parts, excessive bloom, excessive fog, hidden details, unreadable interface, fake source code, garbled Chinese text, misspelled text, extra paragraphs, duplicated objects, Minecraft logo, Blockbench logo, watermark, signature, stock-photo look, generic AI cyberpunk art
```

## 推荐顺序

```text
P00 → P01 → P03 → P04 → P02 → P05 → P06
```

中文排版如果无法稳定生成，先输出无文字底图，再使用可靠排版工具加入准确文案。不要用错误中文作为正式宣传图。
