---
name: godot-profiling-optimization
description: Use when improving Godot 4 performance or diagnosing spikes—Profiler, Debugger monitors, rendering vs physics vs scripting cost, allocation habits, and measurement-first workflow. Not for replacing correct architecture with micro-optimizations without profiling data.
---

# Godot 4 — profiling and optimization

Use with **`godot-editor-export-debug`** for running debug vs release builds; with **`godot-rendering-shaders-2d-3d`** / **`godot-particles-vfx`** when the hotspot is draw-related; with **`godot-csharp`** for managed allocation and interop hotspots.

## When to use this skill

- **Editor Profiler**: frame time breakdown (process, physics, idle, **rendering**); identifying single-frame spikes vs sustained load.
- **Remote profiling** on device builds when desktop editor numbers lie (mobile GPUs, thermal throttling).
- **Physics cost**: broad-phase vs narrow-phase symptoms; too many active bodies; collision shape complexity; physics tick rate implications (`Engine.physics_ticks_per_second`—change only with care).
- **Scripting cost**: per-frame allocations in GDScript hot loops; `print` spam in shipping paths; expensive `find_child` / full-tree scans each frame.
- **Rendering**: overdraw, lights, shadows, post stack; instancing vs individual draw calls; particle and shader cost.

## Principles

- **Measure before rewriting**; fix the category that actually dominates the frame (CPU script vs GPU vs physics).
- Keep optimizations **localized** with comments only when the non-obvious trick needs future readers (avoid narrating obvious changes).
- Compare **export templates** and **renderer** settings to what ships—debug overlays and editor overhead are not player FPS.

## Pitfalls

- Optimizing **cold paths** first (title screen) while gameplay stutters.
- Lowering **physics rate** or **render scale** as a band-aid without exposing quality settings to players when appropriate.

## Official reference

- Performance tutorials index: https://docs.godotengine.org/en/stable/tutorials/performance/index.html
- CPU optimization: https://docs.godotengine.org/en/stable/tutorials/performance/cpu_optimization.html
- 3D performance: https://docs.godotengine.org/en/stable/tutorials/performance/optimizing_3d_performance.html
- Debugger overview: https://docs.godotengine.org/en/stable/tutorials/scripting/debug/overview_of_debugging_tools.html
