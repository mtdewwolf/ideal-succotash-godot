---
name: godot-particles-vfx
description: Use for Godot 4 GPU (and CPU) particles—GPUParticles2D/3D, process materials, trails, attractors, collision hints, and VFX performance. Not for general materials or post-processing (see godot-rendering-shaders-2d-3d).
---

# Godot 4 — particles and VFX

Use with **`godot-rendering-shaders-2d-3d`** for materials and shaders on meshes; with **`godot-animation`** when VFX must sync tightly to skeletal animation; with **`godot-physics-navigation`** when particles interact with physical collision (limited use cases).

## When to use this skill

- **`GPUParticles2D` / `GPUParticles3D`**: amount, lifetime, explosiveness, one-shot vs looping, visibility AABB / fixed size tuning.
- **`ParticleProcessMaterial`** (or custom process material): direction, spread, gravity, color ramps, scale curves, subemitters if used.
- **`CPUParticles2D` / `CPUParticles3D`**: when GPU particles are unsupported or debugging requires simpler behavior—know the performance tradeoff (often more CPU cost per particle at scale).
- **Trails**, **collision** (where supported), **attractors**—match renderer and project render method (forward+, mobile compatibility) per team policy.
- **Pooling / one-shots**: bursts for impacts; avoid spawning thousands of new particle nodes per frame without reuse patterns the project already uses.

## Principles

- Profile on **target hardware**; mobile GPUs punish overdraw and high particle counts.
- Prefer **fewer, richer** particles (textures, curves) over brute particle count.
- Keep VFX **authored in scenes** where designers iterate; expose tunables with **`@export`** on wrapper nodes if the codebase uses that pattern.

## Pitfalls

- **Huge visibility AABB** or mis-sized bounds → particles culled incorrectly or never culled.
- Mixing **particles** with **forced transparency** stacks that tank fill rate—check overdraw in profiler.

## Official reference

- Particle systems (2D): https://docs.godotengine.org/en/stable/tutorials/2d/particle_systems_2d.html
- Particle systems (3D): https://docs.godotengine.org/en/stable/tutorials/3d/particles/index.html
