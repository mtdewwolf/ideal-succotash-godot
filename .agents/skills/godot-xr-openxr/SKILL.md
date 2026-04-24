---
name: godot-xr-openxr
description: Use for Godot 4 XR and OpenXR—viewports, trackers, action maps, comfort options, and export/platform notes. Not for flat-screen UI polish unless discussing XR UI overlays.
---

# Godot 4 — XR (OpenXR)

Use with **`godot-editor-export-debug`** for export templates and platform presets; with **`godot-physics-navigation`** for room-scale or teleport locomotion that uses physics; with **`godot-ui-input-animation-audio`** for laser-pointer or wrist UI.

## When to use this skill

- **OpenXR** project setup: runtimes on PC and Android; feature flags the team already uses (`project.godot` / XR-related settings)—mirror the repo’s existing XR scene root (`XROrigin3D`, `XRCamera3D`, controllers).
- **Input**: action maps / poses for grab, aim, haptics; avoid hard-coding device-specific button indices where the XR map abstracts them.
- **Comfort**: vignette, snap vs smooth turn, teleport arcs—document tunables for QA and accessibility (see **`godot-accessibility-ui`** for non-XR overlap).
- **Performance**: stereo rendering, foveation (if used), MSAA vs mobile GPU limits—profile on **headset hardware**, not only desktop editor mirror.
- **UI in XR**: `SubViewport` + 3D quad or dedicated XR UI nodes per project pattern—follow existing scenes.

## Principles

- Treat **play space** and **stage** transforms carefully; test seated and room-scale if both are supported.
- Version-sensitive: XR APIs evolve across Godot 4 minors—**confirm engine version** before suggesting renamed nodes or properties.

## Pitfalls

- Forgetting **origin recentering** flows users expect on PCVR.
- Shipping without **fallback** for missing runtime (clear error or graceful disable).

## Official reference

- XR documentation index: https://docs.godotengine.org/en/stable/tutorials/xr/index.html
