---
name: godot-rendering-shaders-2d-3d
description: Use for Godot 4 rendering—CanvasItem/Control 2D, MeshInstance3D, lights, materials, environment, post-processing, and ShaderMaterial / GDShader. Not for gameplay logic unless tied to visuals.
---

# Godot 4 — rendering, materials, and shaders

## When to use this skill

- **2D**: `CanvasItem` draw order, modulate, materials on sprites, **tilemaps**, parallax.
- **3D**: meshes, **StandardMaterial3D**, **ORMMaterial3D**, lights (directional, omni, spot), shadows, **WorldEnvironment**, fog, **tonemap**.
- **Shaders**: `.gdshader` with `shader_type canvas_item | spatial | sky | fog | particles`; prefer built-ins and **visual shader** only if the project already uses them.
- **Performance**: instancing, LOD, occlusion, batching considerations; profile on target hardware when in doubt.

## Principles

- Prefer **material parameters** and **AnimationPlayer** over per-frame shader uniform spam unless needed.
- Keep **shader variants** under control; branching on uniforms is cheaper than duplicating entire shader graphs unnecessarily.

## Official reference

- Shaders intro: https://docs.godotengine.org/en/stable/tutorials/shaders/shaders_intro.html
- 3D rendering: https://docs.godotengine.org/en/stable/tutorials/3d/introduction_to_3d.html
