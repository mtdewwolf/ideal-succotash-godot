---
name: godot-files-data-io
description: Use for Godot 4 file and data I/O—FileAccess, DirAccess, user:// vs res://, JSON, ConfigFile, save-game versioning, and atomic writes. Not for networking payloads (see godot-http-websocket-tls or godot-multiplayer-networking).
---

# Godot 4 — files and data I/O

Use with **`godot-editor-export-debug`** for export sandbox paths and **`godot-internationalization`** when reading locale-specific text files.

## When to use this skill

- **`user://`**: persistent writable location per project; use for saves, caches, downloaded content. **`res://`** is generally read-only in exported builds—do not assume you can write there after export.
- **`FileAccess`**: open, read, write, binary vs text, `get_as_text()`, `eof_reached()`.
- **`DirAccess`**: listing, making/removing directories—handle missing paths gracefully.
- **`JSON`**: `parse` / `stringify`—validate types after parse; never trust file contents from untrusted sources.
- **`ConfigFile`**: INI-style sections for settings; good for human-editable local config.

## Save-game discipline

- Include **`version`** field in save JSON/dictionary and **migrate** old saves with small functions per version bump.
- Prefer **write-then-rename** (temp file in `user://`, then replace) to reduce torn writes if the game crashes mid-save—only if the platform allows; keep it simple if the project already uses a proven pattern.

## Pitfalls

- Blocking the main thread on **large file I/O**—for big loads, profile first; avoid naive **background threads** around `FileAccess` and the scene tree unless the project already uses a vetted threading pattern.
- Hard-coded absolute OS paths—use **`ProjectSettings.globalize_path`** / `user://` patterns consistent with the codebase.

## Official reference

- File system introduction: https://docs.godotengine.org/en/stable/tutorials/io/index.html
- Saving and loading data: https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html
