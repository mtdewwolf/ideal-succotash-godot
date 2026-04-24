---
name: godot-tilemap-2d-levels
description: Use for Godot 4 2D tile workflows—TileSet, layers, physics from tiles, navigation baking, Y-sort, and level design pitfalls. Not for 3D terrain or pure sprite placement without tiles.
---

# Godot 4 — TileMap / 2D levels

Use with **`godot-physics-navigation`** for collision layers on bodies that interact with tiles, **`godot-scenes-and-resources`** for scene structure, and **`godot-assets-import-pipeline`** for atlas/source art import.

## When to use this skill

- **`TileSet`**: sources (atlas, scenes-as-tiles), collision shapes per tile, navigation polygons, custom data layers, terrains/peering if the project uses autotiling.
- **Layers**: stacked draw order, parallax siblings, **`y_sort_enabled`** on parent `Node2D` when the game needs depth sorting by Y.
- **Navigation**: baking regions from tile navigation layers; aligning with `NavigationRegion2D` or `NavigationObstacle2D` the project already uses.
- **Changing tiles at runtime**: `set_cells`, animated tiles, destructible terrain—watch performance on large maps.

## Principles

- Match **collision layer/mask** conventions from the rest of the project for tile physics.
- Prefer **tile custom data** for gameplay metadata (spawn points, biome ids) over magic tile IDs in code when designers iterate often.
- For very large worlds, consider **chunking / multiple TileMaps** or streaming patterns the repo already documents—do not invent a chunk system without user direction.

## Version note

Tile APIs evolved across early Godot 4 releases; **confirm minor version** (`project.godot` `config/features`) when suggesting node names (`TileMap` vs layered setups in newer docs). Mirror patterns already in the project’s scenes.

## Official reference

- Using Tilemaps: https://docs.godotengine.org/en/stable/tutorials/2d/using_tilemaps.html
- 2D navigation mesh from tiles: follow navigation docs for your engine minor version.
