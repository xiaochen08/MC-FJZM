# Persistent image production system

Use this system whenever concept approval needs more than one image, more than one asset, a GUI, damage states, or animation previews. Its core rule is: generate the right bounded batch, show it, record the decision, and resume from evidence instead of restarting or guessing.

## Production order

For a multi-asset Mod scope, create a **full asset overview** before any per-asset detail round. The overview is a catalog and scale-comparison sheet containing the primary model, all approved related assets, approved GUI screens, and approved state families such as projectiles, drops, wrecks, or damage variants. It shows scope and visual unity; it does not approve the final geometry of every entry.

Use this order:

1. `asset_overview`: show the whole approved asset family and GUI presence at a readable scale.
2. `model_theme`: generate three distinct A/B/C primary-model directions.
3. `theme_lock`: obtain explicit user selection or revision of one direction.
4. `asset_detail`: run per-asset detail rounds, one bounded asset or tightly coupled asset family at a time.
5. `model_views`: after shape and style stabilize, generate the complete build-reference view matrix.
6. `model_actions`: generate action/keyframe sheets for every approved animation or state transition.
7. `gui_theme`: independently generate GUI A/B/C theme previews.
8. `gui_detail`: after GUI theme approval, run screen-specific GUI detail rounds and state sheets.
9. `final_visual_lock`: archive only explicitly approved outputs as production anchors.

Do not treat a full asset overview, theme lock, model approval, GUI approval, texture approval, or action preview as approval for another gate. Theme lock establishes one shared art direction; it does not silently approve every asset.

## Complete model view contract

Every final model reference package must show:

- front;
- back;
- left side;
- right side;
- top;
- bottom;
- three-quarter;
- an action/keyframe sheet for every approved action, attack, transformation, damage stage, destruction route, or important transition.

Use orthographic projection for front, back, left side, right side, top, and bottom. Use a restrained fixed camera for three-quarter. Every view must depict the **exact same geometry, proportions, cube inventory, and texture**. Keep scale, ground line, part count, attachment state, material palette, and lighting consistent. Reject and regenerate any sheet with invented rear parts, changed limb length, mirrored asymmetry, missing attachments, hidden bottom geometry, or inconsistent texture markings.

An action/keyframe sheet is a visual animation plan, not proof that the clip runs in Blockbench or Minecraft. Runtime proof still requires the real model, rig, exported clip, and in-game evidence.

Do not combine model sheets and GUI screens in one image. A model view sheet, action sheet, GUI screen, GUI component/state sheet, effect sheet, and damage sheet each receive their own round entries and files. This preserves readable scale and prevents one image from hiding implementation gaps.

## One active decision per conversation turn

Keep the complete queue internal. Show only the current image batch and ask one active approval question. Examples:

- choose A, B, or C for the primary model;
- approve or revise the current asset;
- approve or revise the current GUI theme;
- choose the most important detail to change.

Do not ask the user to approve several assets and several GUI screens in one turn. If the user lists many changes at once, record all of them, apply them to the queue, and ask only the highest-impact unresolved decision next.

## Persistent project archive

Create this structure inside the approved unified project root:

```text
design/
  image-production-index.json
  image-rounds/
    round-001__asset-overview/
      prompt.md
      negative-prompt.md
      manifest.json
      images/
      review.json
      approval-evidence.txt
    round-002__model-theme/
      prompt.md
      negative-prompt.md
      manifest.json
      images/
      review.json
      approval-evidence.txt
    round-003__asset__<asset_id>/
    round-004__gui__<screen_id>/
  approved-previews/
    approval-index.json
```

Every generated image, input reference, prompt, negative prompt, manifest, critique, user revision, approval evidence, and superseded result stays inside its numbered round. Calculate and record SHA-256 for every prompt, manifest, and image. Never overwrite, rename in place, delete, or reuse an earlier round file. A revision creates a new round or a new versioned file with a new hash. `superseded` means retained but no longer authoritative.

Use only these round states:

```text
queued | generated | shown | revision_requested | approved | superseded
```

`image-production-index.json` is the cross-conversation source of truth. Each entry records:

```json
{
  "round_id": "round-003",
  "round_type": "asset_detail",
  "project_id": "energy_defense",
  "asset_id": "crystal_tower",
  "screen_id": null,
  "status": "shown",
  "depends_on": ["round-002"],
  "prompt_path": "design/image-rounds/round-003__asset__crystal_tower/prompt.md",
  "negative_prompt_path": "design/image-rounds/round-003__asset__crystal_tower/negative-prompt.md",
  "manifest_path": "design/image-rounds/round-003__asset__crystal_tower/manifest.json",
  "image_sha256": [],
  "approval_evidence": null,
  "next_round": "round-004"
}
```

At the start of a future conversation, read `image-production-index.json`, verify referenced files and hashes, restate the current project/asset header, and continue only the highest-priority unresolved round. Do not regenerate an approved or superseded round unless the user explicitly reopens it. If the index and files disagree, stop image production and repair traceability before continuing.

Run `scripts/validate_image_production_index.py` before resuming a later conversation, before copying an approved anchor, and before final delivery. A failing index blocks further generation because asset identity or approval history may be ambiguous.

## Prompt and review discipline

Compile `concept-prompt.md` for model rounds and `gui-design.md` for GUI rounds. Keep the approved theme token, palette, material language, texture tier, view contract, and asset identity in every later prompt. Never rely on the image model to remember a previous round; inject the approved image hashes and frozen manifest into the next prompt.

Before showing a batch:

1. verify every requested asset or screen is present and no unapproved asset was invented;
2. verify model cross-view consistency and Blockbench feasibility;
3. verify GUI scale, text-safe regions, states, and Minecraft style;
4. record visible defects in `review.json`;
5. regenerate internally when a blocking defect is obvious;
6. show images in their recorded order, then ask one approval question.

Copy approved anchors to `design/approved-previews/` without removing their original round copies. The approval index points to both locations, hashes, manifest, exact user evidence, and superseded versions.
