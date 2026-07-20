# Java Mod project bootstrap gate

## Opening route

Ask whether the user has an authorized Mod project and its path before asking the model category.

- Existing project: do not create another one; use `scripts/inspect_runtime_project.py` and preserve its hashes.
- Missing or unknown project: offer a minimal Mod shell through the first route, present exactly these two routes, and wait for the user's explicit choice:
  1. `create_mod_first` — prepare a minimal Mod shell before model production; collect the locked creation brief only after this route is selected.
  2. model-first (`model_first`) — record `project_status: runtime_deferred`; run the runtime risk classification in `model-first-runtime-gate.md`; validate `runtime-contract.json`; proceed only to its production ceiling. A validated `runtime-neutral source` may include editable geometry, textures, adapter-safe groups/origins, and provisional animation/effect/audio contracts. Platform exports stay blocked, runtime integration remains deferred, and no runtime integration claim is allowed.

Do not continue to the model category until the project route is explicitly selected. Do not auto-resolve, recommend as if selected, or treat silence, urgency, model approval, or “decide for me” as the route choice. Record the user's verbatim choice as `route_choice_evidence`.

## Red priority: Minecraft version is first

Immediately after `create_mod_first` is selected, the first question must ask for the target Minecraft version. No loader, Java, workspace, model, GUI, or asset question may appear before it. Ask exactly: `你要做哪个 Minecraft 版本的 Mod？` and explain in plain Chinese that this controls the loader, build tool, Java floor, mappings, and project template. Ask no second decision in the same turn.

If the user already supplied an exact version, record that evidence instead of asking again. If the user does not know, enter the unknown-version route below; do not silently choose a version.

Never create a project from silence, urgency, delegated choice, or model approval. Project creation requires separate explicit project-creation approval and an absolute destination path that does not already exist.

Do not force Mod creation for every asset. For medium/high-risk runtime-dependent assets, present `create_mod_first` as the default recommendation. If the user declines, require separate verbatim decline evidence, explicit risk acceptance, and a validated production ceiling. Unknown critical role/render/animation decisions restrict work to concepts or graybox; they never authorize a speculative final rig.

## When the version is unknown

If the user does not know the Minecraft version, ask whether the target must match an existing server or modpack, other players, or an older world; otherwise offer a latest stable profile suitable for the requested feature set.

Check official primary sources at execution time for Minecraft, loader, mappings, animation library, Java, Gradle/plugin, and generator/template compatibility. Record direct source URLs and the check timestamp. Community tutorials may explain usage but cannot be the compatibility authority. State uncertainty and do not guess compatibility.

Present at most three evidence-backed profiles with tradeoffs. Do not describe “latest” as a version number until verified. Wait for the user to select or approve one profile.

## Locked creation brief

Create `mod-project-brief.json` with:

- explicit route choice and verbatim route-choice evidence;
- Minecraft version;
- loader and loader version;
- mappings;
- animation runtime and version;
- namespace and mod_id plus display name;
- Java and Gradle versions;
- unused absolute destination path;
- official compatibility evidence;
- verbatim creation approval;
- Windows toolchain policy.
- proof that `minecraft_version` was the first Mod-creation question;
- unified project drive/root generated from the drive letter;
- Java minimum, installed JDK inventory, selected Gradle runtime JDK, compile release, and compatibility evidence;
- red `encoding-preflight.json` host-gate status.

Run `scripts/validate_mod_project_brief.py` and fix every error before creating files.

For `runtime_deferred`, the brief must instead reference a validated `runtime-contract.json`, record `runtime_risk`, `production_ceiling`, Mod-first recommendation/decline evidence, risk acceptance, and the `no runtime integration claim` restriction.

## Windows creation rules

Read `windows-utf8-preflight.md` immediately after the Minecraft version is resolved. Its `severity: red` gate runs before project source creation. Use PowerShell 7 and literal absolute paths. Prefer the selected loader's official generator or official template for the exact approved version profile. Review the generated file list before writing.

Use a project-local wrapper and `gradlew.bat`; no global install, global PATH change, JDK replacement, or package-manager switch without separate user approval. Never merge into or overwrite an existing directory during bootstrap.

## Java floor and newer-JDK policy

Derive the required minimum Java major from official compatibility evidence for the exact Minecraft, loader/plugin, and Gradle wrapper combination. The selected Java must not be below the required minimum Java major.

Never uninstall or downgrade a newer JDK. An installed JDK is a candidate, not automatic proof. Prefer an already installed newer JDK such as Java 25 when the pinned Gradle wrapper and loader plugin officially support running on it and the wrapper diagnostics pass. Record compilation release/target separately from the JDK that runs Gradle.

Do not claim that every higher Java version is automatically compatible: newer Java may still be incompatible with the pinned Gradle wrapper or loader plugin. If the existing newer JDK cannot run the exact approved toolchain, keep it installed and use a project-scoped or side-by-side JDK that is supported; do not replace the user's global Java. Any side-by-side JDK installation requires normal installation authority and recorded reason.

Use Gradle toolchains or task-specific launchers when compilation/testing needs a different language level. Record the running JVM, compiler JVM, `--release`/target, Gradle version, official matrix URL, and smoke-test result separately.

Primary Gradle references to verify at execution time:

- Java/Gradle runtime compatibility: https://docs.gradle.org/current/userguide/compatibility.html
- JVM toolchains and side-by-side selection: https://docs.gradle.org/current/userguide/toolchains.html

## Minimal Mod shell

Create only what is required to compile and launch:

- version-pinned build files and wrapper;
- minimal entrypoint and mod metadata;
- `src/main/resources/assets/<namespace>` with model, texture, animation, sound, language, and particle-ready directories;
- required data/server directories for the chosen loader;
- selected animation dependency only when its exact compatibility is verified;
- identity-scoped placeholders/contracts, not speculative gameplay code.

Do not implement the boss, targeting, damage, projectile, particles, or audio behavior merely because the shell exists. Those remain later approved production tasks.

## Smoke evidence

On Windows, run the project-local wrapper diagnostics, then `gradlew.bat build`. If authorized and supported, run `gradlew.bat runClient`, launch the development client, and confirm the empty Mod loads without errors. Record command arguments, exit codes, logs, build artifact hash, Java/Gradle versions, project inspection report, and failures.

A successful shell proves only that the selected toolchain launches. It does not verify the future model or gameplay implementation.

The official empty shell may be created only after the host UTF-8 gate passes. Before writing custom Java, JSON, language, GUI, model, or resource files, configure and pass the project UTF-8 gate from `windows-utf8-preflight.md`; otherwise stop.
