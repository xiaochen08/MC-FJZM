# Mod handoff and result contract

`mod-handoff.json` is written by `$fjzm`, consumed by `$fjzm-mod`, and immutable for one attempt. Required fields include:

The `stage` is exactly one of `project_bootstrap`, `gameplay_design`, or `runtime_integration`. Run `scripts/validate_mod_handoff.py` before every delegated write. A later stage is a new immutable handoff, never an in-place reinterpretation of an earlier one.

- ContractFlow envelope, `project_id`, `asset_id`, `asset_version`, attempt, sender, recipient, and single writer;
- exact `minecraft_version`, `loader`, loader version, mappings, Java, Gradle/plugin, namespace, and mod ID;
- authorized project root, `allowed_write_roots`, forbidden roots, output version, rollback/checkpoint evidence;
- `gameplay_spec_path` and `gameplay_spec_sha256`;
- approved model/texture/animation paths and hashes including `model_sha256`, geometry signature, `rig_signature`, UV signature, locator signature, animation/event IDs, particle/audio/GUI contracts;
- requested registrations, runtime systems, configuration, networking, persistence, data generation, tests, and explicit non-goals;
- `approval_evidence` for project writes, downloads/installations when applicable, builds, and launches.

Reject path traversal, missing identities, mismatched hashes/signatures, unapproved dependencies, ambiguous registry names, and writes outside `allowed_write_roots`.

Return `mod-result.json` with the same identity envelope, input/output hashes, exact changed-file list, generated resources, registrations, dependency changes, commands and exit codes, test/build/client/server evidence, JAR hash, runtime-verified claims, unverified claims, warnings, migrations, rollback notes, and re-handoff requirements.

`$fjzm-mod` never declares final release approval. `$fjzm` validates and integrates the result.
