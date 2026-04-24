---
name: godot-physics-navigation
description: Use for Godot 4 physics (2D/3D bodies, areas, joints, raycasts) and navigation (NavigationServer2D/3D, regions, agents, avoidance). Use when movement, collision, or pathfinding is involved.
---

# Godot 4 — physics and navigation

## When to use this skill

- **Character movement**: `CharacterBody2D` / `CharacterBody3D`, `move_and_slide`, snap, floors, `Platform` layers.
- **Rigid bodies**: forces, impulses, damping, sleeping, **joints** for constraints.
- **Areas**: overlap signals, monitoring modes, layers/masks.
- **Queries**: `PhysicsRayQueryParameters`, shape casts, picking.
- **Navigation**: baking meshes or tilemaps, `NavigationRegion*`, `NavigationAgent*`, avoidance in Godot 4.x navigation stack.

## Principles

- Align **collision layers and masks** with project conventions; document new layers in a single place (comment or small doc in repo if the team does that).
- Use **`collision_shape`** disabled or removed when pooling objects off-screen—avoid invisible colliders accumulating cost.
- Pathfinding: prefer **navigation** APIs over manual waypoint graphs unless the game already uses custom AI graphs.

## Official reference

- Physics intro: https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html
- Navigation: https://docs.godotengine.org/en/stable/tutorials/navigation/index.html
