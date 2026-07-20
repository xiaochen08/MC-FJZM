# High-fidelity pixel texture rules

## Step 3: high-fidelity pixel texturing

Use native-resolution nearest-neighbor pixels and no antialiasing blur. “Gradient” means deliberate stepped pixel clusters, not a smooth airbrush or blurred band.

### Material ramps

- Major surfaces use a 3-5 color ramp with value and hue shift. Add more colors only when atlas density and material complexity justify them.
- Metal uses tighter dark values, sharp selective highlights, cool or environment-neutral hue movement, and controlled reflection cues without painting a fixed room reflection.
- Cloth uses lower highlight contrast, soft clustered transitions, sparse weave/noise at readable scale, and no metallic rim.
- Skin uses warm midtone transitions and restrained subsurface-scattering cues near thin or flushed areas; it does not receive photoreal skin pores at Minecraft scale.
- Leather uses warm hue movement, crease/contact darks, selective worn edges, and buckle/contact definition.
- Fur uses clustered value breakup that follows form without strand rendering or random salt-and-pepper noise.

### AO and edges

Use local contact AO only where surfaces actually meet: under a chin, beneath a strap, between armor layers, inside a socket, or at a deep seam. For opaque materials, paint AO with opaque pixel colors; semi-transparent dark overlays can produce unintended alpha/render-layer behavior. Keep AO local and neutral rather than turning it into global directional shadow.

Use conditional 1-2 pixel edge accents according to density, material, face orientation, and gameplay readability. Highlight or darken selected bevel-like boundaries—not every edge. Reject universal outlines, glowing rims, and pillow shading that brightens every center and darkens every border regardless of form.

### Completeness and evidence

- Verify every UV face has the intended texture index and path.
- Run seam-pair validation at native zoom and on the assembled model.
- Check front, side, back, top, and three-quarter views in actual Blockbench.
- Inspect identity anchors close up and at gameplay distance.
- Compare against the approved reference using an anchor checklist, not one vague similarity score.
- Keep preview lighting neutral; also inspect an unlit/flat or no-shader baseline when available.
- Reopen the saved `.bbmodel` and PNGs before evidence capture.

`reference-fidelity-report.json` records each anchor's expected appearance, actual appearance, geometry dependency, UV region, preview evidence, and pass/fail. Any identity-critical failure blocks approval.
