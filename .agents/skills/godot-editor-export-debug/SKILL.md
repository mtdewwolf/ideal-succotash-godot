---
name: godot-editor-export-debug
description: Use for Godot editor workflows, export presets, headless or CLI runs, debugging, profiling, and project settings (project.godot). Use when the user asks how to run, test, or ship a Godot build.
---

# Godot 4 — editor, export, and debugging

## When to use this skill

- **Running from CLI** (CI or agents): `godot4 --path /path/to/project` with appropriate flags; use **`--headless`** for servers or import-only steps when supported.
- **Export**: `export_presets.cfg`, platform templates, version pinning in pipelines.
- **Project settings**: `project.godot`—input map, layers, autoload list, renderer and physics settings; change only what the task needs.
- **Debugging**: breakpoints in editor, remote debug, print vs `push_error` / `push_warning`, **Debugger** profiler for frame spikes.
- **Import pipeline**: first-open or reimport after asset changes; agents should not hand-edit `.import` unless the team already does.

## Principles

- Document **exact Godot version** in CI when exports must be reproducible.
- For automated tests, prefer **GdUnit**, **WAT**, or project-native test scenes if already present—do not add a framework without user direction.

## Official reference

- Command line: https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html
- Exporting: https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html
