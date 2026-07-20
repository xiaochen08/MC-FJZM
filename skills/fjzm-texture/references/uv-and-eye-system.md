# UV, seams, and eye states

## Step 2: UV and spatial planning

Maintain uniform texel density unless an approved identity anchor receives explicitly documented extra density. Record atlas dimensions, texels per Blockbench unit, occupancy, mirrored faces, rotations, and shared regions.

Use padding and bleed between UV islands to prevent sampling contamination. Padding is not a substitute for correct UV bounds. Define seam-pair validation for every visible join: name both edges, their orientation, expected ramp continuity, and actual evidence. Adjacent 3D faces do not need to sit beside each other in the atlas, but their paired edge pixels must agree logically.

Check UV overlap, unintended mirror reuse, face index, negative/out-of-bounds coordinates, pixel stretching, density changes, and asymmetric anchors. Freeze `uv_signature` after approval.

## Step 4: eyes and animation adaptation

Treat eyes as identity-critical regions. At sufficient density, each open-eye state defines:

- sclera/base when present;
- iris hue ramp;
- pupil value ramp;
- gaze direction;
- a one-pixel catchlight placed consistently with the approved gaze and material style;
- eyelid and brow pixels where the model supports them.

Support two or three approved states, normally `normal`, `closed`, and `angry`. Other names require an explicit state contract. Every atlas-frame state records frame coordinates `(x, y, width, height)` and must remain inside the approved atlas. Separate-texture states record contained texture paths instead.

Reserve eye frames in a low-conflict atlas region with padding and no overlap. Do not call an arbitrary unused patch “hidden” unless UVs and runtime animation cannot expose it accidentally.

## Runtime support gate

Choose one mode:

- `static`: one eye texture; no switching claim;
- `atlas_frames`: exact frame coordinates plus a named, verified runtime support adapter;
- `separate_textures`: one PNG or material reference per state plus a named runtime controller;
- `geometry_eyelid`: approved eyelid bones/cubes controlled by animation, requiring `$fjzm` and possibly `$fjzm-animation` approval.

Blockbench preview does not prove runtime support for texture swapping or UV animation. Lock Minecraft edition/version, loader/runtime, adapter/controller, state event IDs, fallback, and real-game validation. When runtime support is unresolved, deliver `static` or mark eye animation unintegrated; do not pretend sequence frames will play automatically.
