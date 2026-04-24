---
name: godot-assets-import-pipeline
description: Use for textures, models, audio, and other imported assets—.import files, importers, UID stability, and Godot 4 asset workflow. Use when assets break, reimport loops, or paths change.
---

# Godot 4 — assets and import pipeline

## When to use this skill

- **Import settings**: compression (VRAM normal, etc.), mipmaps, repeat/filter for textures; glTF vs FBX pipeline the project chose.
- **`.import` sidecars**: normally editor-managed; avoid manual edits unless fixing a known, documented issue and the team does this routinely.
- **UIDs**: Godot 4 resource references and UIDs in scenes—preserve stability when moving/renaming; prefer **filesystem move in editor** or coordinated text edits mirroring repo patterns.
- **Large assets**: Git LFS or external art depot—follow what the repo already uses.

## Principles

- **Source art** (`.blend`, PSD, high-res PNG) vs **imported/runtime** assets: keep the pipeline obvious in folder names (`raw/`, `imported/`, etc.) if the project does.
- For batch changes, **`ResourceImporter`** settings in project or presets—prefer one-off editor tools or documented CLI reimport if available.

## Pitfalls

- Renaming files outside Godot without updating references → broken `ext_resource` paths or missing UIDs; use editor rename or scripted refactors that update dependents.

## Official reference

- Import process: https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html
