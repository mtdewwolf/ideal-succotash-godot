---
name: godot-dcc-pipeline
description: Use for DCC-to-Godot workflows—Blender and glTF, scale and forward axis, materials, naming, and LOD. Complements godot-assets-import-pipeline (import settings, UIDs). Not a Blender modeling tutorial.
---

# Godot 4 — DCC and 3D scene pipeline

Use with **`godot-assets-import-pipeline`** for `.import` behavior and UID stability; with **`godot-rendering-shaders-2d-3d`** for how imported materials map to Godot shaders.

## When to use this skill

- **glTF** (recommended default for Blender → Godot): separate vs embedded textures, **scale** (`0.01` vs `1.0` conventions), **+Y up** vs engine expectations—standardize per team doc.
- **Naming**: stable object names for point caches, sockets, or script lookups; avoid characters that complicate paths on all OSes.
- **Materials**: metallic/roughness PBR workflow; how double-sided, alpha blend, and normal maps import; when to **reimport** after Blender material renames.
- **Rigging / animation**: NLA strips vs single-take export; **bone naming** consistency with retargeting if used (see **`godot-animation`**).
- **LOD and meshoptimizer** options when the importer exposes them—verify visually after batch changes.

## Principles

- **Single export preset** checked into docs or a pinned Blender addon version when artists must reproduce results.
- After moving `.glb` paths, fix dependents or reassign in editor to avoid **broken external resources**.

## Pitfalls

- Applying scale in **both** Blender and Godot import transform → double-scaled meshes.
- Huge single `.blend` as the only source—prefer **exported glTF** committed unless the team agreed otherwise.

## Official reference

- Importing 3D scenes (index): https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/index.html
- Assets pipeline overview: https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/index.html
