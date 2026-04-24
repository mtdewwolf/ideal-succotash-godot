---
name: godot-ui-input-animation-audio
description: Use for Godot 4 Control/UI theming, input actions and events, AnimationPlayer/Tween, and AudioStream players. Use for HUD, menus, feel/polish, and input maps.
---

# Godot 4 — UI, input, animation, and audio

## When to use this skill

- **UI**: `Control` layout (anchors, offsets, containers), **themes**, focus and **GUI** input, **popup** menus, **Viewports** for UI-in-3D when needed.
- **Input**: **Input Map** in project settings vs hard-coded keys; `Input.get_axis`, actions, **unhandled input** vs `_input`, consuming events.
- **Animation**: `AnimationPlayer` for clips, **AnimationTree** for state machines, **`Tween`** and **`create_tween()`** for short interpolations.
- **Audio**: `AudioStreamPlayer` (2D/3D), buses, effects, music vs SFX routing.

## Principles

- Prefer **actions** over scancodes so rebinding and gamepads work consistently.
- UI: use **containers** instead of pixel-perfect manual placement when layouts must scale.
- Tweens: chain with **`await tween.finished`** when sequencing; avoid overlapping conflicting property tweens on the same object without care.

## Official reference

- GUI tutorial: https://docs.godotengine.org/en/stable/tutorials/ui/index.html
- Input examples: https://docs.godotengine.org/en/stable/tutorials/inputs/index.html
