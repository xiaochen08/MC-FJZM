# Gameplay attribute profiles

Choose one primary profile per asset. Add optional modules only when the design needs them. Ask exactly one unresolved decision per user turn, explain it in plain Chinese, and store field-level evidence. A recommended default is a proposal, never an answer.

## Common identity and lifecycle

Every profile records stable `project_id`, `asset_id`, `asset_version`, registry identity, display/localization keys, acquisition or spawn path, ownership/permission rules, persistence, removal/destruction behavior, difficulty/config scaling, and explicit non-goals.

## `entity_pet_boss`

Required foundation:

- `max_health`: base maximum health and difficulty scaling.
- `armor`: armor points and toughness when applicable.
- `attack_damage`: base damage, damage source, friendly-fire policy, and server authority.
- `movement_speed`: ground/flying/swimming values and acceleration expectations.
- `follow_range`: perception/target acquisition distance.
- `knockback_resistance`: resistance and intentional launch reactions.
- `hitbox`: width, height, eye height, pose-dependent dimensions, and model-scale comparison.
- `faction_and_targets`: faction, allies, enemies, retaliation, owner protection, and target priority.
- `spawn_rules`: natural/structure/item/command/tamed-only mode, biome, light, height, cap, rarity, and despawn relevance.
- `drops_and_xp`: loot table, conditions, looting behavior, XP, and owner/PvP exceptions.
- `persistence_and_despawn`: save fields, tame/name persistence, wild despawn, chunk unload, and duplicate prevention.
- `taming_and_breeding`: tameable/breedable applicability, items, chance, cooldown, inheritance, owner transfer, sitting/follow modes.

Also resolve attack speed/range, collision/pushability, fall/fire/water/status immunities, regeneration, sounds, animations/events, interaction items, inventory/equipment, navigation, goals, death/removal, and—when applicable—Boss phases, boss bar, arena leash, rewards, multiplayer scaling, interrupt rules, and anti-cheese behavior.

## `item_weapon_tool_armor`

Require `stack_size`, durability or consumable count, rarity, creative tab, use action, cooldown, attribute modifiers, damage/mining/armor values, attack speed, reach, enchantability, repair ingredient, equip slot, fire resistance, crafting/acquisition, tooltip/localization, model predicates/state, server validation, and loss/persistence rules. Resolve projectile, charge, combo, ability, mana/energy, and set-bonus modules only when used.

## `block_machine_turret`

Require hardness, blast resistance, harvest tool/tier, collision/occlusion, light, render layer, rotation/placement, waterlogging, drops, redstone behavior, interaction, block-entity need, tick policy, state persistence, ownership/permissions, GUI/menu, inventory/capacity, energy/fluid/item sides, range, targeting, damage/friendly fire, chunk unload, removal drops, comparator output, and performance budget. Turrets additionally resolve projectile/beam truth, cooldown, aim limits, line of sight, target filters, and server authority.

## `projectile`

Require owner, spawn source, speed, gravity, drag, lifetime/range, collision size, damage source/value, knockback, pierce/bounce, block interaction, entity filters, friendly fire, tracking/turn rate, impact behavior, particles/audio, network spawn/sync, save policy, and cleanup. Explosion, area effect, chain, status, and return-to-owner are optional modules.

## `gui_menu`

Require opening condition, server menu/container, slot layout and rules, data fields, synchronization source/rate, permissions, distance validity, close behavior, shift-click rules, ghost/filter slots, localization, screen scaling, narration/accessibility, error feedback, and disconnect/reload behavior. GUI artwork approval never substitutes for slot and sync design.

## `world_generation_structure`

Require dimension, biome/tag filters, placement method, frequency/separation, height, terrain adaptation, rotation/mirroring, processors, bounding box, spawn protection, loot, mobs, data-driven registration, seed determinism, retrogen policy, performance, conflicts, and datapack/config overrides.

## Evidence rule

`gameplay-spec.json` contains `attributes` and a matching `attribute_evidence` entry for every required field. Evidence may quote the user or record explicit acceptance of a shown recommendation. `unknown`, silence, inferred intent, and an unlabeled code default do not pass.
