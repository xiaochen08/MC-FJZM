# Unified Mod and model Windows workspace

## Core invariant

Create one large project folder for the complete Mod, every model, GUI, texture, animation, audio file, particle contract, preview, export, and evidence record. Inside it, use one independent folder per model. Treat each independent `.bbmodel` as one asset even when it is a projectile, companion, variant, or replacement wreck model. Give every such asset its own `asset_id`, model specification, approvals, and sibling folder under `assets/models/`. Geometry, damage groups, and clips stored inside the same `.bbmodel` remain in that model's folder.

Never mix two asset_id values in one asset folder. Project-level indexes and explicitly approved shared libraries live above or beside asset folders, never inside one model's workspace.

## Drive-only intake

Ask only for the Windows drive letter, such as `D:`. Do not ask the user for a parent folder. Do not choose a drive for the user. Normalize only an explicit drive answer, then derive this standard ASCII-safe root automatically:

```text
D:\FJZM-Projects\<project_id>
```

Build `project_id` from the approved Mod/project identity using lowercase ASCII. Chinese remains allowed in display names and UTF-8 content, but the root path stays ASCII-safe to reduce build-tool and archive risk. Show the derived absolute project root in the final project-creation approval; do not ask a separate parent-folder question or separate path-approval question.

Example asset path:

```text
D:\FJZM-Projects\energy_defense\assets\models\crystal_tower__v1
```

State the drive, project root, Mod folder, asset folder, and whether the project root already exists. The user's explicit project-creation approval authorizes this displayed standard root. A model-category choice, concept approval, delegated choice, or silence is not project-creation approval.

## Safe creation

Create the unified project folder only after explicit project-creation approval. Creating it only establishes storage; folder creation is not model-generation approval. Immediately before writing:

1. Resolve the approved drive and project root; verify the resolved destination remains inside the approved root `X:\FJZM-Projects` on that drive.
2. Require an unused destination. If it exists, do not overwrite, merge, or silently reuse it; propose a versioned sibling path and show it in a renewed project-creation approval.
3. Use PowerShell 7 with literal paths and create only the approved project directory:

```powershell
New-Item -ItemType Directory -LiteralPath 'D:\FJZM-Projects\energy_defense'
```

Do not scan or create across other drives. Do not use wildcard paths. Record the created absolute path and path approval evidence.

## Unified project layout

Create these subfolders only inside the approved project root:

```text
mod/                         official loader project and runtime integration
assets/models/               one identity-isolated folder per independent model
design/concepts/             model and GUI A/B/C drafts and manifests
design/image-rounds/         immutable numbered image batches, prompts, reviews, and approvals
design/image-production-index.json  cross-conversation image queue and hashes
design/approved-previews/    approved model and GUI images plus approval-index.json
gui/                         GUI source textures, atlases, manifests, and screenshots
contracts/                   project, runtime, shader, event, and integration contracts
shared/audio/                explicitly approved shared audio library
shared/particles/            explicitly approved shared particle resources
docs/                        decisions and user-facing project notes
evidence/                    validators, hashes, build logs, Blockbench and game proof
backups/                     explicit versioned backups created before risky updates
exports/                     qualified delivery packages
```

Each `assets/models/<asset_id>__v<version>/` contains:

```text
consultation/  requirements, decisions, approval evidence
concepts/      model A/B/C prompts, manifests, and generated previews
specs/         model-spec, animation, particle, and audio contracts
source/        editable .bbmodel after concept approval
textures/      texture atlases and emissive masks
animations/    exported animation/controller files
audio/         identity-scoped sources, processed files, and manifests
particles/     particle contracts and runtime files
previews/      Blockbench screenshots, GIFs, and keyframes
exports/       runtime model exports
evidence/      asset validators, hashes, and runtime evidence
```

Before concept approval, store only consultation and concept materials. Do not create `.bbmodel`, final textures, rigs, or animations before concept approval. After approval, keep every produced file inside the unified project root. Runtime integration copies under `mod/` must retain source hashes and identity mappings back to the owning model/GUI asset.

Every image generation attempt belongs under `design/image-rounds/round-<number>__<scope>/` with its prompt, negative prompt, manifest, image files, review, approval evidence, and SHA-256 hashes. Never overwrite or delete an earlier image round. `design/image-production-index.json` records the current queue and allows a future conversation to resume the next unresolved round without mixing projects or assets. Approved images are copied to `design/approved-previews/`; their original round copies remain authoritative evidence.

## Multi-model rule

Create every approved related model in a sibling folder under `assets/models/`. A separate projectile `.bbmodel`, summon, dropped item, trophy, or replacement wreck is a separate model folder. Never put one model's texture, audio, animation, export, or evidence into another model's folder. Validate the collection through `project-index.json` after each asset bundle passes independently.
