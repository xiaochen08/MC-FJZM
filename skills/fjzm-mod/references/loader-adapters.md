# Loader adapters

Maintain Forge, NeoForge, and Fabric adapters inside one Mod workshop. Do not create separate loader skills unless independent maintenance evidence later proves necessary.

For the chosen Minecraft version, verify official primary sources for the loader version, official generator/template, mappings, Java floor, Gradle wrapper/plugin, event/registry API, networking, data generation, access wideners/transformers, mixin use, animation library, and run tasks. Record source URLs and timestamps.

- **Forge**: use the exact supported MDK/toolchain and Forge registration/event conventions for the pinned version.
- **NeoForge**: treat it as a distinct platform; do not assume Forge packages, events, metadata, or Gradle configuration are interchangeable.
- **Fabric**: use Fabric Loader, Fabric API, Loom, mappings, entrypoints, networking, and data generation that match the pinned version.

Do not silently substitute a loader, Minecraft version, mapping set, dependency, Gradle plugin, or Java runtime. If the requested combination is unsupported or uncertain, stop production, show the official evidence in plain language, and return a single choice to `$fjzm`.

Keep shared gameplay specifications platform-neutral. Put loader-specific code behind adapter-owned packages and tests so a later port does not rewrite the asset identity or approved attributes.
