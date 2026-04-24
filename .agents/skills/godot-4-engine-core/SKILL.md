---
name: godot-4-engine-core
description: Use when working with Godot 4 scene tree, nodes, lifecycle (_ready, _process, _physics_process), groups, pausing, threading basics, or engine architecture. Covers how the engine runs frames and where logic belongs.
---

# Godot 4 — engine core and scene tree

## When to use this skill

- Adding or reorganizing **nodes**, **parents**, and **scene ownership**.
- Choosing between `_process` (every frame, variable delta) and `_physics_process` (fixed timestep, physics-safe).
- **SceneTree** access: `get_tree()`, changing scenes, `call_deferred` for order-safe reparenting or queue_free.
- **Groups** for decoupled lookups (`add_to_group`, `get_nodes_in_group`).
- **Pausing** (`process_mode`, `SceneTree.paused`) and which nodes should keep running (e.g. UI overlays).

## Principles

- Prefer **composition** (child nodes) over deep inheritance for gameplay objects.
- Use **`call_deferred`** when modifying the tree in response to signals or physics callbacks that might conflict with iteration order.
- **Physics bodies** (`CharacterBody*`, `RigidBody*`, `StaticBody*`) should move or apply forces in `_physics_process` or physics callbacks, not `_process`, unless you have a deliberate reason.
- **Autoloads** are singletons; use them for cross-cutting services, not as a dump for all global state—inject references where it keeps tests and scenes clearer.

## Anti-patterns

- Frequent `get_node()` with string paths from deep nodes—cache `@onready` references or use groups / exported `NodePath`.
- Running heavy logic every frame without checking visibility or game state.

## Official reference

- Scene tree: https://docs.godotengine.org/en/stable/tutorials/scripting/scene_tree.html
- Idle vs physics processing: https://docs.godotengine.org/en/stable/tutorials/scripting/idle_and_physics_processing.html
