---
name: godot-theming-ui-advanced
description: Use for Godot 4 Theme resources, type variations, style overrides, icon fonts, and scalable UI systems beyond basic containers. Pair with godot-ui-input-animation-audio for layout and input. Not for 3D HUD in world space unless theming Control nodes in SubViewport.
---

# Godot 4 — advanced UI theming

Use with **`godot-ui-input-animation-audio`** for anchors, containers, focus, and input actions; with **`godot-internationalization`** when translated strings change minimum sizes.

## When to use this skill

- **`Theme`**: colors, constants, fonts, icons, **styleboxes** per control type and state (hover, pressed, disabled).
- **Type variations**: `theme_type_variation` on `Control` nodes for semantic styles (“PanelAccent”, “ButtonDanger”) instead of duplicating overrides everywhere.
- **Local overrides**: `add_theme_*_override` in code vs scene defaults—prefer theme resources for consistency across scenes.
- **Scaling**: default theme font sizes, `theme_*` scale factors, high-DPI / large accessibility text (see **`godot-accessibility-ui`**).
- **Icons and fonts**: dynamic font fallbacks, atlas icons, alignment with RTL layouts.

## Principles

- Build a **small set of semantic variations** rather than dozens of one-off overrides.
- Keep **spacing and corner radii** in theme constants so global polish is one edit.
- For complex screens, **root `Control` + child theme** inheritance beats repeating the same six overrides on every leaf node.

## Pitfalls

- Overriding **every** sub-property on each node → unmaintainable; consolidate into `Theme`.
- Forgetting **disabled / focus** states for interactive controls—keyboard users depend on visible focus.

## Official reference

- GUI skinning and themes: https://docs.godotengine.org/en/stable/tutorials/ui/gui_skinning.html
- Custom GUI controls: https://docs.godotengine.org/en/stable/tutorials/ui/gui_using_theme_editor.html
