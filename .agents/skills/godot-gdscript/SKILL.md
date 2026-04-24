---
name: godot-gdscript
description: Use when writing or refactoring GDScript in Godot 4—typing, signals, await/async, Resources, lambdas, style, and common APIs. Use for script-only tasks or when pairing scripts with scenes.
---

# Godot 4 — GDScript

## When to use this skill

- New scripts, **static typing** (`var x: int`, `-> void`), and **class_name** / `@icon` when defining reusable types.
- **Signals**: `signal name(args)`, `emit`, `connect`, lambdas, and disconnecting to avoid leaks.
- **Coroutines**: `await` on signals, `SceneTreeTimer`, or `async` methods; know that `await` yields and can invalidate `is_instance_valid(self)` assumptions.
- **Resources** vs **Nodes**: data in `.tres` / custom `Resource` scripts; behavior on `Node`.
- **Enums**, **match**, **dictionaries**, and **PackedArrays** for performance-sensitive hot paths.

## Principles

- Enable **typed GDScript** where it helps readability and catches errors early.
- Prefer **`@export`** for designer-tunable values; use **`@export_group`** / **`@export_subgroup`** for inspector organization.
- Use **`super()`** when overriding `_ready` / virtual methods in subclasses.
- For optional nodes, **`@onready var n = $Path as Type`** and null-check before use.

## Signals and memory

- Connecting with **callable lambdas** that capture `self` is fine for object lifetime; for long-lived singletons listening to short-lived nodes, disconnect in `_exit_tree` or use **weak refs** patterns where appropriate.

## Anti-patterns

- Stringly-typed `get("property")` everywhere—use typed access or small interfaces.
- Huge `_ready` blocks—split into private methods or child components.

## Official reference

- GDScript basics: https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html
- GDScript style: https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html
