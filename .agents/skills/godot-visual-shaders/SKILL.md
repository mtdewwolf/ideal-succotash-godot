---
name: godot-visual-shaders
description: Use for Godot 4 VisualShader graphs—node-based materials and shaders, organization, and when to switch to text GDShader. Not for gameplay scripting or non-shader VFX unless wiring shader parameters from code.
---

# Godot 4 — visual shaders

Use with **`godot-rendering-shaders-2d-3d`** for GDShader text, render modes, and material parameters; with **`godot-particles-vfx`** when visual shaders drive particle process materials.

## When to use this skill

- **Graph structure**: grouping frames, reroutes, comments for teammates; naming subgraphs or custom nodes if the project uses them.
- **Ports and types**: vector dimensions, color vs vec3, ensuring **shader_type** (`canvas_item`, `spatial`, etc.) matches the material use case.
- **Performance**: excessive texture samples or dependent texture reads in fragment stage—compare against a simpler GDShader when profiling shows hotspots.
- **Version control**: `.tres` visual shaders are verbose diffs—coordinate with artists before mass reformatting.

## Principles

- Prefer **VisualShader** when non-programmers iterate on look; prefer **GDShader** when reviews need grep-friendly text or complex branching.
- Expose **`shader_parameter`** from materials for gameplay-driven toggles instead of duplicating near-identical graphs.

## Pitfalls

- Copy-pasting subgraphs without updating **uniform** names → silent wrong bindings.
- Mixing **per-pixel** and **per-vertex** expectations (lighting, displacement) without verifying the graph output stage.

## Official reference

- Visual shaders: https://docs.godotengine.org/en/stable/tutorials/shaders/visual_shaders.html
