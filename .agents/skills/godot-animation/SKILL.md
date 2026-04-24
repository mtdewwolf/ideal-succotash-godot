---
name: godot-animation
description: Use for Godot 4 animation systems—AnimationPlayer clips, AnimationTree state machines, blending, AnimationMixer-style workflows, and retargeting basics. Not for one-off tweens (see godot-ui-input-animation-audio).
---

# Godot 4 — animation (AnimationPlayer / AnimationTree)

Use with **`godot-scenes-and-resources`** for `.tres` animation libraries, **`godot-physics-navigation`** when root motion or physical bones are involved, and **`godot-ui-input-animation-audio`** for simple `Tween` / UI motion only.

## When to use this skill

- **`AnimationPlayer`**: tracks (property, method, Bezier, audio), blending modes, autoplay, capturing reset-on-save poses.
- **`AnimationTree`**: state machine vs blend tree, one-shot vs looping states, filters on which properties blend.
- **Mixing**: multiple players on a subtree; which node owns playback when scenes are instanced.
- **Retargeting / skeletons**: humanoid-style reuse across meshes—follow the project’s existing rig naming and import presets.
- **Code-driven vs data-driven**: when to keyframe vs when to drive bones or properties from script each frame.

## Principles

- Prefer **named animations** and constants for animation names the codebase references often (avoid scattered string literals).
- Keep **animation libraries** as resources when the same clips are shared across scenes.
- For gameplay-critical timing (combo windows, invulnerability), prefer **signals** (`animation_finished`, custom method tracks) or **state machines** over guessing frame numbers in code.

## Pitfalls

- Editing transforms in **both** animation and `_physics_process` without clear ownership → fighting overrides.
- Huge blend trees without **debug visualization** in editor → hard to reason about; document transitions the team relies on.

## Official reference

- Animation introduction: https://docs.godotengine.org/en/stable/tutorials/animation/introduction.html
- AnimationTree: https://docs.godotengine.org/en/stable/tutorials/animation/animation_tree.html
