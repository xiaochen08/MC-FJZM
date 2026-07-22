---
name: fjzm-mod
description: "Use when creating, inspecting, repairing, integrating, testing, or packaging Minecraft Java Mods for Forge, NeoForge, or Fabric, including entities, pets, bosses, items, weapons, blocks, machines, turrets, projectiles, GUIs, structures, world generation, networking, saves, and runtime asset binding."
---

# 方界造模·Mod 工坊

`$fjzm-mod` owns Java Mod project implementation and Minecraft runtime integration. `$fjzm` remains the approval, identity, orchestration, and release owner. Do not modify model geometry, UVs, textures, or animation curves; return interface defects to `$fjzm`.

## Entry and authority

Accept either an identity-scoped `mod-handoff.json` from `$fjzm` or a standalone request to inspect an existing Mod. Read [mod-handoff.md](references/mod-handoff.md). In delegated production, run `scripts/validate_mod_handoff.py` before writing. In standalone mode, allow read-only inspection and consultation; obtain explicit write approval and create a handoff before modifying files.

Minecraft version and Mod loader answers are intake evidence, not permission to create, download, install, edit, build, or launch. Preserve the main skill's version-first and loader-second gate. Never treat an example, demonstration, model approval, urgency, or “decide for me” as execution authority.

## One-question attribute intake

Read [gameplay-attributes.md](references/gameplay-attributes.md) before asking gameplay questions. Classify the runtime asset profile, build an internal queue from only that profile plus declared optional systems, and Ask exactly one user-facing question per turn. Use plain Chinese, short explanations, and numbered choices. Never dump the complete attribute checklist. Accept a number, name, or free text.

In delegated mode, return the next unresolved decision to `$fjzm` instead of bypassing the main conversation. `$fjzm` remains the only approval owner and records the answer before re-delegating. In standalone consultation, follow the same one-question protocol but do not claim suite-level approval.

Explain the direct gameplay effect before asking. Offer a concrete recommended value with a vanilla comparison when evidence supports it, but never insert that value silently. Record field-level answer evidence. Silence and guessed defaults are not approval.

Create `gameplay-spec.json` only after the applicable queue is resolved. Run `scripts/validate_gameplay_spec.py`. Do not write gameplay code before the type-specific attribute gate passes. For a creature, pet, or Boss, this gate includes health, armor, damage, movement, perception, knockback, hitbox, faction/targets, spawn, drops/XP, persistence/despawn, and taming/breeding applicability.

## Project and loader gate

Read [loader-adapters.md](references/loader-adapters.md). Keep Forge, NeoForge, and Fabric as adapters inside this one Mod workshop. Verify exact Minecraft, loader, mappings, Java, Gradle/plugin, animation-runtime, and API compatibility from official primary sources at execution time. Do not silently substitute a version, loader, dependency, mapping set, or generator.

Before creation or custom source writes, require the main suite's validated `mod-project-brief.json` and red UTF-8 host/project gates. Use PowerShell 7, UTF-8, literal absolute paths, the project-local wrapper, and the approved destination. Do not overwrite or merge an unknown project.

## Implementation workflow

Read [runtime-implementation.md](references/runtime-implementation.md), then:

1. Inspect the authorized project and freeze its manifest, loader, namespace, source roots, dependencies, and hashes.
2. Validate `gameplay-spec.json`, `mod-handoff.json`, model/rig/UV signatures, event IDs, locators, and allowed write roots.
3. Produce a registration and ownership map for assets, gameplay state, server authority, client rendering, networking, saves, data generation, localization, and configuration.
4. Implement the smallest vertical slice first: registration, spawn/acquisition, attributes, rendering, one behavior, save/reload, then expand only approved systems.
5. Bind models, animations, particles, audio, GUI, projectiles, loot, recipes, and damage events by stable IDs. Never infer a missing locator or animation event.
6. Run loader-specific tests, project-local build, data generation when applicable, and authorized `runClient`/server checks.
7. Return identity-scoped `mod-result.json` with changed files, hashes, commands, logs, build artifact, runtime evidence, unresolved risks, and rollback notes.

## Required quality gates

- Base attributes and field-level evidence complete for every runtime asset.
- Server owns damage, inventory, ownership, cooldown, progression, drops, and persistent state; clients own presentation unless the approved design says otherwise.
- Entity dimensions match the approved model and collision intent; visual scale never silently replaces the hitbox.
- Spawn/despawn, death/removal, chunk unload/reload, world save/reload, multiplayer join, and disconnect cleanup are covered when applicable.
- GUI values have an explicit sync source and permission model.
- Networking is bounded, validated, and never trusts arbitrary client damage or inventory claims.
- Config/default migration and registry-name stability are addressed before release.
- Passing compilation is not gameplay proof. Require actual Minecraft evidence for claims about behavior, visuals, animation, networking, saves, shaders, or performance.

## Stop conditions

Stop and return to `$fjzm` when identity, approved behavior, gameplay attributes, model hash, rig signature, event mapping, loader compatibility, write scope, or execution approval is missing or contradictory. Do not repair those gaps by guessing.

## Quick reference

| State | Allowed action |
|---|---|
| No handoff/write approval | Inspect and advise only |
| Asset profile unresolved | Ask only the profile question |
| Required attribute unresolved | Ask one attribute question; write no gameplay code |
| `gameplay-spec.json` invalid | Fix the brief; no production |
| Loader/toolchain unverified | Research official sources; do not generate a project |
| Model/event contract invalid | Return to `$fjzm`; do not bind assets |
| Contracts valid | Implement only the approved write scope |
| Build passes, runtime untested | Report build-only status; make no gameplay claim |
