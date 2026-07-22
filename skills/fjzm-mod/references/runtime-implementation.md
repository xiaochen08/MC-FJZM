# Runtime implementation and evidence

## Vertical slice order

Implement registration and acquisition/spawn first, then approved base attributes, renderer/model binding, one representative behavior, save/reload, and multiplayer authority. Expand AI, attacks, projectiles, GUI, particles, audio, loot, recipes, configuration, and progression only after the slice works.

## Ownership map

Assign an owner to every state:

- server: health, damage, cooldowns, AI decisions, inventory, ownership, taming, drops, progression, persistent state;
- client: renderer, interpolation, camera-local presentation, approved particles and audio;
- synchronized: only bounded values needed for presentation or GUI.

Validate packet direction, sender permissions, ranges, enum/ID bounds, rate limits, world/thread access, and disconnect cleanup. Never trust client-authored damage, ownership, inventory, or reward claims.

## Mandatory scenario matrix

For applicable assets test spawn/acquisition, interaction, combat/use, death/destruction, chunk unload/reload, world save/reload, server restart, multiplayer join/leave, dimension change, config migration, missing dependency behavior, and dedicated-server class loading. Record logs and screenshots/video only as supporting evidence; commands, hashes, assertions, and runtime observations remain authoritative.

## Release status

Use precise labels: `spec_validated`, `source_implemented`, `build_passed`, `client_smoke_passed`, `server_smoke_passed`, `runtime_verified`, or `release_qualified`. Never promote a lower state merely because compilation succeeded.
