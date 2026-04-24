---
name: godot-scenes-and-resources
description: Use when editing or creating .tscn/.tres, PackedScene, instancing, inheritance, preloads, or resource pipelines. Use when agents must not break scene file format or UIDs.
---

# Godot 4 — scenes and resources

## When to use this skill

- **PackedScene** instantiation: `instantiate()`, ownership, and when to `queue_free` instances.
- **Scene inheritance**: extending a base `.tscn` for variants (characters, levels).
- **Preload vs load**: `preload()` for constants known at parse time; `load()` for dynamic paths.
- **Custom Resources**: `class_name` + `extends Resource`, `@export` data driving gameplay or tuning.
- **Editing `.tscn` / `.tres` in text**: preserve **existing UIDs** and structure; follow patterns already in the repository.

## Text scene files (critical for agents)

- Godot 4 scenes use **`[gd_scene`** headers, **`ext_resource`** / **`sub_resource`**, and **`[node]`** blocks with **`parent`** paths.
- **Do not invent UIDs**; duplicate or copy from sibling resources the project already uses, or let the editor regenerate when the user saves.
- When unsure about format details, **prefer minimal diffs** and mirror neighboring nodes in the same file.

## Principles

- Keep scenes **shallow** where possible; move repeated logic to scripts or sub-scenes.
- Use **`%UniqueNodeName`** in large scenes sparingly; prefer groups or exports for cross-references.

## Official reference

- Scenes vs scripts: https://docs.godotengine.org/en/stable/getting_started/step_by_step/scripting_first_script.html
- Resources: https://docs.godotengine.org/en/stable/tutorials/scripting/resources.html
