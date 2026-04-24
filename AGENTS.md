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

## Skill index (folder name under `.agents/skills/`)

| Skill folder | Scope |
|--------------|--------|
| `godot-4-engine-core` | Scene tree, lifecycle, groups, pausing |
| `godot-gdscript` | GDScript language and common APIs |
| `godot-scenes-and-resources` | PackedScene, `.tscn` / `.tres`, resources |
| `godot-editor-export-debug` | Editor, CLI, export, debugging, `project.godot` |
| `godot-rendering-shaders-2d-3d` | Materials, environment, shaders |
| `godot-physics-navigation` | Physics bodies, areas, queries; light nav agent use |
| `godot-navigation-advanced` | NavigationServer, baking, links, avoidance, multi-map |
| `godot-ui-input-animation-audio` | Control UI, input map, tweens, audio |
| `godot-multiplayer-networking` | ENet / high-level multiplayer, RPCs, authority |
| `godot-csharp` | C# scripts and .NET interop with Godot 4 |
| `godot-gdextension` | Native extensions, `.gdextension`, bindings |
| `godot-assets-import-pipeline` | Imported assets, `.import`, UID-safe moves |
| `godot-testing-ci` | Automated tests, headless runs, CI |
| `godot-animation` | AnimationPlayer, AnimationTree, blending, retargeting basics |
| `godot-tilemap-2d-levels` | TileSet, TileMap layers, 2D level / nav from tiles |
| `godot-files-data-io` | FileAccess, user://, JSON, ConfigFile, saves |
| `godot-internationalization` | Translations, tr(), locales, fonts, RTL |
| `godot-http-websocket-tls` | HTTPRequest, WebSocketPeer, TLS for web APIs |
| `godot-particles-vfx` | GPU/CPU particles, process materials, VFX performance |
| `godot-editor-plugins-tool-scripts` | EditorPlugin, @tool, editor-only tooling |
| `godot-theming-ui-advanced` | Theme resources, type variations, style overrides |
| `godot-accessibility-ui` | Focus, keyboard/gamepad UI, contrast, scale |
| `godot-profiling-optimization` | Profiler, hotspots, CPU/GPU/physics/script cost |
| `godot-threading-concurrency` | WorkerThreadPool, threads, mutexes, thread-safe APIs |
| `godot-xr-openxr` | XR setup, OpenXR, performance and comfort notes |
| `godot-visual-shaders` | VisualShader graphs vs GDShader tradeoffs |
| `godot-compute-advanced-rendering` | Compute shaders, RenderingDevice, GPU pipelines |
| `godot-mobile-platform-notes` | Android / iOS export, permissions, safe area, perf |
| `godot-dcc-pipeline` | Blender / glTF, scale, materials, naming, LOD |
| `godot-class-reference-workflow` | Docs lookup, version pinning, avoid invented APIs |

## Repository maintenance

- Keep each skill **focused**: one primary concern per folder.
- When updating Godot APIs, align examples with the **current stable 4.x** docs and naming (`Node3D`, `NavigationRegion3D`, etc.).
