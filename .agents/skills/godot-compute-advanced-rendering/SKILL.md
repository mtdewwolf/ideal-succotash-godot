---
name: godot-compute-advanced-rendering
description: Use for Godot 4 compute shaders and low-level GPU work—general-purpose GPU passes, RenderingDevice usage patterns, and when built-in materials suffice. High complexity; prefer simpler rendering skills unless the task explicitly needs compute or RD.
---

# Godot 4 — compute shaders and advanced rendering

Use with **`godot-rendering-shaders-2d-3d`** for standard materials and fragment/vertex shaders; with **`godot-profiling-optimization`** when debugging GPU stalls or barriers.

## When to use this skill

- **Compute shaders**: dispatch groups, shared local memory, barriers, reading/writing textures and buffers—only when the pipeline cannot be expressed cleanly with existing **RenderingServer** helpers or fragment shaders.
- **`RenderingDevice`**: creating pipelines, uniform sets, and synchronization—**expert-level**; easy to leak RIDs or mismatch formats across Godot minors.
- **Fallbacks**: editor-only debug visualization vs shipping path; feature detection when export targets lack extensions.

## Principles

- **Prove necessity**: try `MultiMesh`, particles, or a simpler shader first; add compute only with measured benefit.
- Keep **resource lifetimes** explicit; pair allocations with `free_rid` or scoped helpers the project already uses.
- Document **required GPU features** next to the shader in-repo so exports do not silently fail on low-end hardware.

## Pitfalls

- Assuming **Vulkan-only** behavior on all export targets (mobile GL differences).
- Debugging without **GPU validation** layers when available—spend hours on wrong barrier assumptions.

## Official reference

- Compute shaders: https://docs.godotengine.org/en/stable/tutorials/shaders/compute_shaders.html
- RenderingDevice class: https://docs.godotengine.org/en/stable/classes/class_renderingdevice.html
