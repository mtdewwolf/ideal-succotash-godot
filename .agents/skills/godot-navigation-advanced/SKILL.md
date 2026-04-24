---
name: godot-navigation-advanced
description: Use for Godot 4 advanced navigation—NavigationServer2D/3D, baking, navigation layers, links, obstacles, avoidance, and multi-region setups. Use when pathfinding, crowd movement, or navmesh tuning is the main problem; use godot-physics-navigation for bodies, raycasts, and simple agent follow.
---

# Godot 4 — advanced navigation

Use with **`godot-physics-navigation`** for character controllers and physics queries; with **`godot-tilemap-2d-levels`** when navigation is baked from tiles; with **`godot-profiling-optimization`** when many agents cost too much per frame.

## When to use this skill

- **Servers**: `NavigationServer2D` / `NavigationServer3D` maps, regions, and synchronous map operations—know that many APIs expect **RIDs** and valid region setup before queries return useful paths.
- **Baking**: mesh sources, geometry parsing, cell size / agent radius tradeoffs; rebaking after level geometry changes.
- **Layers and masks**: separating AI factions, terrain types, or off-mesh connections via project conventions.
- **Navigation links** (“jump down”, ladders, doors) and **obstacles** that carve or block dynamically.
- **NavigationAgent2D/3D**: target setting, path postprocessing, **`avoidance_enabled`** and parameter tuning when many agents overlap.
- **Multiple maps**: switching maps for streaming worlds or stacked floors—avoid cross-talk between unrelated `NavigationRegion*` trees.

## Principles

- **One source of truth** for walkable geometry: prefer navmesh from level art (or tiles) over hand-placed polys unless the game is small and designer-driven.
- Tune **agent radius / height** (3D) or equivalent 2D clearance to match the **`CharacterBody`** capsule or hitbox—mismatches cause edge-stuck or clipping.
- When avoidance fights desired velocity, reduce oscillation by adjusting **time horizons** and max speeds before disabling avoidance entirely.

## Pitfalls

- Querying paths **before** regions finish baking or while RIDs are invalid → empty paths or errors.
- Running heavy **`NavigationServer`** sync calls every frame without caching—profile and throttle.

## Official reference

- Navigation overview: https://docs.godotengine.org/en/stable/tutorials/navigation/index.html
- Introduction (2D): https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_2d.html
- Introduction (3D): https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html
