---
name: godot-physics-navigation
description: Use for Godot 4 physics—CharacterBody and RigidBody movement, areas, joints, raycasts, and shape queries. Use for simple follow-the-navmesh agent wiring only; use godot-navigation-advanced for NavigationServer baking, layers, links, avoidance tuning, and multi-map setups.
---

# Godot 4 — physics and basic navigation touchpoints

For **deep navigation** (servers, baking, links, crowds, avoidance), use **`godot-navigation-advanced`**. For **tile-based** nav authoring, combine with **`godot-tilemap-2d-levels`**.

## When to use this skill

- **Character movement**: `CharacterBody2D` / `CharacterBody3D`, `move_and_slide`, snap, floors, `Platform` layers.
- **Rigid bodies**: forces, impulses, damping, sleeping, **joints** for constraints.
- **Areas**: overlap signals, monitoring modes, layers/masks.
- **Queries**: `PhysicsRayQueryParameters`, shape casts, picking.
- **Navigation (light)**: attaching `NavigationAgent*` to a body, feeding a target, reading the next path position—without restructuring global nav maps or server RIDs (hand that to **`godot-navigation-advanced`**).

## Principles

- Align **collision layers and masks** with project conventions; document new layers in a single place (comment or small doc in repo if the team does that).
- Use **`collision_shape`** disabled or removed when pooling objects off-screen—avoid invisible colliders accumulating cost.
- Pathfinding: prefer **navigation** APIs over manual waypoint graphs unless the game already uses custom AI graphs; escalate tuning to **`godot-navigation-advanced`** when agents crowd or paths fail near edges.

## Official reference

- Physics intro: https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html
- Navigation overview (for cross-links): https://docs.godotengine.org/en/stable/tutorials/navigation/index.html
