---
name: godot-editor-plugins-tool-scripts
description: Use for Godot 4 editor extensions—EditorPlugin, docks, bottom panels, EditorInterface, filesystem interaction, and @tool scripts that run in the editor. Not for runtime game logic unless shared tooling is explicitly requested.
---

# Godot 4 — editor plugins and `@tool` scripts

Use with **`godot-scenes-and-resources`** when plugins mutate scenes or resources; with **`godot-gdscript`** / **`godot-csharp`** for language-specific editor APIs; with **`godot-editor-export-debug`** for how plugins ship (or do not ship) in exports.

## When to use this skill

- **`EditorPlugin`**: enabling/disabling, `add_control_to_dock`, `add_control_to_bottom_panel`, shortcuts, **undo/redo** via `get_undo_redo()` for mutating operations.
- **`EditorInterface`**: opening scenes, inspecting nodes, editor selection—respect editor **thread and UI context**; defer work that touches the tree with `call_deferred` when required.
- **`@tool` scripts**: running in editor for gizmos, previews, or data pipelines—know that **`_ready` / `_process` run in editor** unless guarded; use `Engine.is_editor_hint()` when behavior must differ.
- **Inspector plugins** and **property editors**—follow existing patterns in the repo for custom resource inspectors.
- **Editor-only singletons** and **`class_name`** tool types—avoid name collisions with game code.

## Principles

- **Never** silently delete user assets; confirm destructive operations or provide undo entries.
- Keep plugins **scoped**: one feature per plugin folder when possible; document activation steps in the repo README only if the user maintains one.
- C# editor plugins are **possible but heavier**—mirror whatever the project already chose (GDScript vs C#).

## Pitfalls

- Shipping **`tool` code** that assumes `get_tree().current_scene` exists in all editor states.
- Writing to **`res://`** from plugins without team policy—prefer explicit import or generated folders.

## Official reference

- Making plugins: https://docs.godotengine.org/en/stable/tutorials/plugins/editor/making_plugins.html
- Running code in the editor: https://docs.godotengine.org/en/stable/tutorials/plugins/running_code_in_the_editor.html
