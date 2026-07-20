# Mod asset presentation and themed text contract

Use this contract for every generated Mod asset that players can inspect, equip, place, encounter, configure, or read about. The text shown in concept images is a preview; the final implementation must use Minecraft runtime text and localization resources.

## Required information hierarchy

Every asset presentation contains these four layers in this exact semantic order:

1. **item or asset display name** — the most prominent line, using the approved theme color and optional bold weight;
2. **gray and italic Mod display name** — a quieter ownership/source line immediately below the name;
3. **usage instruction** — a readable colored line explaining the actual interaction in plain language;
4. **theme-consistent flavor text** — a short hint, warning, joke, lore fragment, or mysterious sentence selected from an approved pool.

Example visual hierarchy:

```text
[aqua + bold] 裂界核心
[gray + italic] 方界能源
[yellow] 使用：右键部署；潜行右键切换模式
[dark_purple + italic] “当第七码环苏醒，沉默也会成为武器。”
```

The Mod name line remains gray and italic even when other lines use rich colors. Color, italic, bold, indentation, spacing, line order, and wrap width are design tokens recorded in the manifest; do not scatter raw formatting codes through Java source.

## Player-facing tone decision

Ask the tone in one plain-language question before final GUI/tooltip previews:

1. `themed serious`（推荐）— professional theme lore with restrained mystery;
2. `light chuunibyou` — occasional dramatic lines without obscuring usage;
3. `full chuunibyou` — deliberately theatrical names and hints while keeping the usage line factual.

Middle-school-fantasy or “中二” writing is allowed, but it cannot replace the usage instruction, hide a safety warning, or make the asset's function unclear.

## Flavor pool and stable randomness

Create an **approved curated pool** of **4 to 8** flavor entries per asset. Entries must match the asset theme and avoid repeated wording. The user may approve the pool as part of the asset presentation preview.

Use a stable rule such as `stable_per_stack`, `stable_per_asset_instance`, or `stable_per_session`. The chosen line must not change every rendered frame, every tooltip refresh, or every GUI tick. `stable_per_stack` is the default for inventory items because it feels varied without flicker. Never generate fresh unreviewed text at runtime.

## Presentation surfaces

Not every asset has an inventory tooltip. Record one or more appropriate surfaces:

- `tooltip` for items, blocks, equipment, spawn items, and inspectable icons;
- `gui_info_panel` for machines, control panels, quests, and configuration screens;
- `hud` for equipped tools, abilities, vehicles, and live state;
- `boss_bar` for Boss identity and phase hints;
- `catalog` for structures, environments, entities, lore entries, and assets otherwise lacking a hover surface;
- `multiple` only when the same identity is intentionally represented on several surfaces.

All four semantic layers must be available somewhere appropriate, but compact surfaces may show only the display name and state while linking to a full tooltip or panel.

## Localization and runtime boundary

Use stable translation keys:

```text
item.<mod_id>.<asset_id>
tooltip.<mod_id>.<asset_id>.mod
tooltip.<mod_id>.<asset_id>.use
tooltip.<mod_id>.<asset_id>.flavor.01
tooltip.<mod_id>.<asset_id>.flavor.02
```

The exact registry prefix may become `block`, `entity`, or another valid Minecraft namespace for non-item assets, but the asset ID stays stable. Store Chinese source text as UTF-8 and create localization entries through the chosen Mod runtime.

All final names, instructions, and flavor lines are **runtime-rendered**. Do not bake final UI text into model or GUI textures. GUI previews may visually demonstrate the approved typography and layout, but the implementation must render localized text so language changes, GUI scale, accessibility, and keybind names continue to work.

## Manifest

Create one `asset-presentation.json` per asset before final GUI previews or runtime registration:

```json
{
  "schema_version": 1,
  "project_id": "energy_defense",
  "asset_id": "rift_core",
  "mod_id": "fjzm_energy",
  "presentation_surface": ["tooltip", "gui_info_panel"],
  "display_name": {
    "translation_key": "item.fjzm_energy.rift_core",
    "style": {"color": "aqua", "bold": true, "italic": false}
  },
  "mod_line": {
    "translation_key": "tooltip.fjzm_energy.rift_core.mod",
    "style": {"color": "gray", "bold": false, "italic": true}
  },
  "usage": {
    "translation_key": "tooltip.fjzm_energy.rift_core.use",
    "style": {"color": "yellow", "bold": false, "italic": false}
  },
  "flavor": {
    "style_mode": "light_chuunibyou",
    "selection_rule": "stable_per_stack",
    "style": {"color": "dark_purple", "bold": false, "italic": true},
    "entries": [
      {"translation_key": "tooltip.fjzm_energy.rift_core.flavor.01", "text_zh": "第七码环正在低语。"},
      {"translation_key": "tooltip.fjzm_energy.rift_core.flavor.02", "text_zh": "别盯着核心看太久。"},
      {"translation_key": "tooltip.fjzm_energy.rift_core.flavor.03", "text_zh": "沉默也会成为武器。"},
      {"translation_key": "tooltip.fjzm_energy.rift_core.flavor.04", "text_zh": "权限不足，但命运已批准。"}
    ]
  },
  "layout": {
    "line_order": ["display_name", "mod_line", "usage", "flavor"],
    "wrap_width": 220,
    "gui_scale_tested": [2, 3, 4],
    "color_only_meaning": false
  }
}
```

Use named color tokens that the runtime adapter maps to supported Minecraft text styles. Do not use legacy `§` formatting codes in manifest text. Validate with `scripts/validate_asset_presentation.py` before runtime integration and release.

## Readability gate

- Keep the usage line literal and testable; themed language belongs in the flavor line.
- Do not rely on color alone to convey rarity, danger, state, or usability.
- Test the chosen wrap width at every approved GUI scale and with longer localization strings.
- Keep contrast readable with vanilla UI and the approved GUI theme.
- Prevent tooltip overflow, clipped glyphs, and lines hidden beyond the screen edge.
- Treat any text, order, color, or tone change shown in a later preview as a revision requiring its own approval evidence.
