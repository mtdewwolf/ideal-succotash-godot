---
name: godot-class-reference-workflow
description: Use when agents must look up Godot 4 APIs correctly—class reference, version pinning, search habits, and not inventing methods or signals. Invoke alongside domain skills; does not replace them.
---

# Godot 4 — class reference and lookup discipline

Use this skill **together with** the domain skill (physics, UI, networking, etc.) whenever the implementation depends on exact **method names**, **signal signatures**, or **enum values**.

## When to use this skill

- **Before coding**: open the official class page for the node or singleton you touch (`CharacterBody3D`, `NavigationServer3D`, `HTTPRequest`, …).
- **Version pinning**: read docs for the **same major.minor** as `config/features` in `project.godot` (or the user-stated engine). Stable docs default to latest—watch for “deprecated since” banners.
- **Search**: prefer site search on docs.godotengine.org or your IDE’s Godot integration over guessing GDScript names from other engines.
- **Signals and properties**: confirm exact spellings; GDScript uses **snake_case**; C# exposes **PascalCase** wrappers but stringly `Call` paths may still need **snake_case** (see **`godot-csharp`**).

## Principles

- **Never invent** APIs—if unsure, say so and point to the class reference section to verify.
- Prefer **linked stable docs** in PRs or comments only when it helps future readers, not for every line.
- When docs and editor disagree, **trust the installed editor** for the project’s version and reconcile with a release note link if needed.

## Pitfalls

- Copying snippets from **Godot 3** blogs without adapting node names (`KinematicBody` → `CharacterBody3D`, etc.).
- Using **latest-only** features while the project targets an older 4.x—CI will not catch editor-only mistakes until export.

## Official reference

- Class reference index: https://docs.godotengine.org/en/stable/classes/index.html
- Godot editor online help (same content as built-in): browse from the class index above.
