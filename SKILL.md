---
name: fjzm
description: "Use when users ask for 方界造模 or FJZM, or when creating, revising, texturing, animating, sonifying, exporting, or validating Minecraft Blockbench .bbmodel assets: entities, weapons, items, machines, furniture, structures, vehicles, or environments."
---

# 方界造模（FJZM）

## Category routing

Read [user-dialogue.md](references/user-dialogue.md) before asking anything. Ask exactly one user-facing question per turn; keep all later questions in the internal queue and use plain numbered choices. Read [asset-identity.md](references/asset-identity.md); lock the target asset before creating or binding files. Ask whether an authorized Minecraft project exists. If absent/unknown, Read [mod-project-bootstrap.md](references/mod-project-bootstrap.md). Require an explicit project route choice before the model category: `create_mod_first` or `model_first`. Do not auto-resolve this choice.

When `create_mod_first` is selected, the target Minecraft version is the first Mod-creation question and blocks every loader, Java, drive, folder, category, model, GUI, and asset question. After the version is answered or the user selects the documented unknown-version route, Read [windows-utf8-preflight.md](references/windows-utf8-preflight.md). Read [asset-workspace.md](references/asset-workspace.md) before concepts. Ask only for the Windows drive letter in its own turn; derive the unified project root automatically. Pass the red host UTF-8 gate before creating the Mod shell, then pass the project UTF-8 gate before writing any custom Mod source or localized resource. Read [image-production-system.md](references/image-production-system.md) before planning or generating any preview batch; use its persistent index to continue the correct round across conversations.

Read [model-categories.md](references/model-categories.md). After the applicable Mod gate is resolved, Start by asking which top-level model category. Show only the compact top-level menu; accept a number, name, or free-text description, then expand only the selected branch in a later turn. If `model_first`, Read [model-first-runtime-gate.md](references/model-first-runtime-gate.md); classify runtime risk and lock the provisional production ceiling before images. For model-first storage, still use the unified project root from [asset-workspace.md](references/asset-workspace.md). Read [asset-ecosystem.md](references/asset-ecosystem.md); lock scope through separate single-decision turns. For every player-facing runtime asset, Read [asset-presentation.md](references/asset-presentation.md) before GUI/image prompts and runtime integration. Read [shader-compatibility.md](references/shader-compatibility.md) before concepts; lock the no-shader fallback and any named loader, shader-pack, PBR, emissive, transparency, and performance targets before image generation, one unresolved choice at a time. If GUI screens, menus, HUDs, inventories, control panels, or configuration screens are requested or implied, Read [gui-design.md](references/gui-design.md) before image generation and implementation.

## Approval gate

For a new model without an approved anchor:

1. Build an internal queue for use, runtime, scale, shape, materials, signature parts, motion, references, and texture resolution and texel density. Ask exactly one unresolved decision per turn through [user-dialogue.md](references/user-dialogue.md); never dump this list on the user. Explain what low resolution loses and what high resolution costs only when asking the texture-level question. Assess whether high resolution is necessary. Recommendations state atlas dimensions, texels per Blockbench unit, tradeoffs, necessity rationale, and quality commitment. Use exactly: 64x64 minimum/1 texel per unit; 128x128 standard/1; 256x256 detailed/2; 512x512 ultra/4. Do not recommend below 64x64. Lock the shader-compatibility tier, no-shader fallback, exact named targets, PBR convention, emissive/world-light behavior, render layer, and evidence burden through separate single-decision turns. If animation is requested or implied, **REQUIRED SUB-SKILL:** Use fjzm-animation and Read [animation-system.md](references/animation-system.md) before concepts. If `fjzm-animation` is unavailable, stop animation production; continue only with the explicitly approved non-animation scope. If particles or runtime effects are requested or implied, Read [particle-design.md](references/particle-design.md). If sound is requested/implied or audio files are attached, Read [audio-system.md](references/audio-system.md); inventory and obtain mapping approval before processing/binding. Do not invoke imagegen until related-asset scope and damage/destruction scope are explicitly answered. Shader/lighting scope must also be explicitly answered.
2. Follow [image-production-system.md](references/image-production-system.md) and run `scripts/validate_image_production_index.py` whenever an index already exists. For multi-asset scope, generate and archive the full asset overview before any per-asset detail round. Then Read [concept-prompt.md](references/concept-prompt.md) before invoking imagegen; compile its manifest. **REQUIRED SUB-SKILL:** use imagegen for three distinct Blockbench-feasible concept previews. Generate separately; label A/B/C outside images. After the theme lock, continue one asset, complete view matrix, action/keyframe sheet, or GUI screen at a time; persist every round, prompt, image, review, hash, and approval. Pause if imagegen is unavailable.
   When GUI is in scope, independently follow [gui-design.md](references/gui-design.md): use imagegen for three Minecraft-faithful GUI themes, obtain explicit GUI approval, then continue screen-specific GUI detail/state rounds. Archive approved model and GUI previews together under `design/approved-previews/` with `approval-index.json` while retaining their original immutable round copies.
3. Explain differences; invite revision.
4. Wait for explicit user approval naming the concept and authorizing model generation. Silence is not approval. Never auto-resolve this gate.
5. Do not open or control Blockbench before approval. Do not create a `.bbmodel`, final texture, rig, geometry, or animation before approval.

“Do it now”/“surprise me,” urgency, and references are not approval.

Bypass only for an already-approved design anchor plus explicit generation permission; redesigns require approval.

## Production workflow

1. For `create_mod_first`, validate `mod-project-brief.json`, validate `encoding-preflight.json --required-phase host`, create only the approved minimal official shell, then validate `encoding-preflight.json --required-phase project`. Custom project files remain blocked until the red project gate passes.
2. Read [model-brief.md](references/model-brief.md); save an identity-scoped `model-spec.json`. Create each applicable `asset-presentation.json`, run `scripts/validate_asset_presentation.py`, and block final GUI previews, runtime registration, bundling, and release when it is invalid. Create `shader-contract.json`, run `scripts/validate_shader_contract.py`, and stop before detailed texturing when it is invalid. For `model_first`, create `runtime-contract.json`, run `scripts/validate_runtime_contract.py`, and obey its validated stage ceiling before detailed work.
3. Never reinterpret the approved model or GUI concept.
4. Build clean groups, stable UUIDs, correct origins, and a manifest-matched graybox. Reopen it in actual Blockbench and pass the explicit graybox approval gate in [quality-gates.md](references/quality-gates.md); then freeze `geometry_signature` and the approved `uv_signature`.
5. For detailed texturing, **REQUIRED SUB-SKILL:** Use fjzm-texture. Create identity-scoped `texture-handoff.json` containing `project_id`, `asset_id`, `asset_version`, `model_sha256`, `geometry_signature`, `uv_signature`, approved reference hashes, and shader-contract hash; run the bundled `fjzm-texture/scripts/validate_texture_handoff.py`. If `fjzm-texture` is unavailable, stop detailed texture production. Require a passing, user-approved `texture-result.json` before shader qualification, bundling, or release.
6. For animation, create identity-scoped `animation-handoff.json` containing `project_id`, `asset_id`, `asset_version`, `model_sha256`, and `rig_signature`; run the bundled `fjzm-animation/scripts/validate_animation_handoff.py`. Delegate only the approved clips, then require a passing `animation-result.json` before integrating any changed rig or animation.
7. Apply the returned texture, animation, particle, approved audio, and approved GUI contracts through their declared owners and the central event table.
8. Use [quality-gates.md](references/quality-gates.md), `scripts/validate_bbmodel.py`, and interpolated-frame tests; execute the applicable no-shader, named-shader, PBR, emissive, bloom, and transparency rows from `shader-contract.json` in the actual runtime.
9. For audio use `scripts/audio_pipeline.py`, `scripts/migrate_audio_manifest.py`, Read [audio-runtime-adapters.md](references/audio-runtime-adapters.md), then run `scripts/validate_audio_manifest.py`.
10. Run `scripts/validate_asset_bundle.py`; for multiple models Read [project-integration.md](references/project-integration.md) and run `scripts/validate_project_index.py`.
11. Use `scripts/inspect_runtime_project.py`; Read [runtime-delivery.md](references/runtime-delivery.md), run `scripts/scaffold_runtime_delivery.py` and `scripts/validate_release_evidence.py`, then Read [release-qualification.md](references/release-qualification.md).

## Quick reference

| State | Allowed action |
|---|---|
| Brief incomplete | Ask; create nothing |
| `create_mod_first`, Minecraft version unanswered | Ask only the Minecraft version question |
| Red host UTF-8 gate not passed | Create no Mod shell or production artifact |
| Red project UTF-8 gate not passed | Official empty shell only; custom files blocked |
| Multi-asset overview unapproved | Generate/show only the full asset overview round |
| Theme unapproved | Generate/iterate A/B/C images only |
| Image queue active | Resume the highest-priority unresolved indexed round |
| Asset presentation invalid | No final GUI preview, runtime registration, bundling, or release |
| Audio mapping unapproved | Inventory and propose mappings only |
| Shader/lighting scope unresolved | Ask; concept generation is blocked |
| Concept approved, runtime contract missing/invalid | Stop before detailed production |
| Shader contract missing/invalid | Stop before detailed texturing and any compatibility claim |
| Graybox not explicitly approved | Stop before UV freeze and texture production |
| Texture handoff/result missing or invalid | Stop before texture integration, shader qualification, bundling, and release |
| Model-first critical runtime fields unresolved | Concept or graybox only |
| Concept and runtime gate approved | Build only through the validated production ceiling |
