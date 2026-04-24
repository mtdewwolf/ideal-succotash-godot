# Agent instructions — Godot skills monorepo

This repository packages **Agent Skills** for AI coding assistants (Cursor, OpenAI Codex, Gemini CLI, and other tools that read the shared layout). Skills teach agents how to work effectively with **Godot Engine 4.x** projects.

## Where skills live

- **Canonical path:** `.agents/skills/<skill-id>/SKILL.md`
- **Symlinks** in this repo point the same tree at tool-specific locations (so you do not duplicate content): `.cursor/skills`, `.codex/skills`, and `.gemini/skills` → `.agents/skills`. Edit files only under `.agents/skills/`.

## Default assumptions

- Target **Godot 4.x** unless the user or project files specify Godot 3.
- Prefer **GDScript** for game logic unless the project is clearly C# or GDExtension.
- Respect existing project patterns: node naming, folder layout, autoloads, and input actions already defined in the project.

## How agents should use these skills

1. Match the user task to a skill **description** in each `SKILL.md` frontmatter.
2. When work spans areas (e.g. scene + script + export), combine guidance from multiple skills.
3. After structural edits to `.tscn` / `.tres` files, prefer validating with the editor or CLI if the user has Godot installed; do not invent UIDs or internal format details—copy patterns from existing files in the repo.

## Repository maintenance

- Keep each skill **focused**: one primary concern per folder.
- When updating Godot APIs, align examples with the **current stable 4.x** docs and naming (`Node3D`, `NavigationRegion3D`, etc.).
