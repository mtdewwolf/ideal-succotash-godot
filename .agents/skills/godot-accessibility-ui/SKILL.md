---
name: godot-accessibility-ui
description: Use for Godot 4 UI accessibility—keyboard and gamepad focus, focus neighbors, reading order, contrast and scale, and minimal playable-without-mouse checks. Not a substitute for platform-specific accessibility APIs on consoles.
---

# Godot 4 — UI accessibility

Use with **`godot-ui-input-animation-audio`** for input actions and rebinding; with **`godot-theming-ui-advanced`** for focus rings, sizes, and high-contrast theme variants; with **`godot-internationalization`** when text expansion breaks layouts.

## When to use this skill

- **Focus**: `focus_mode` on controls, **tab order** (`get_focus_neighbor`), opening menus should move focus into popups and return on close.
- **Keyboard / gamepad**: ensure every interactive screen has a **default focused** control on open; avoid traps where focus is `null` or stuck on hidden nodes.
- **Mouse-only affordances**: add keyboard paths for the same actions where feasible (inventory, map, settings).
- **Visual clarity**: minimum font sizes, **contrast** between text and `StyleBox` backgrounds, visible **focus highlight** (theme or override).
- **Scale / DPI**: honor the root **`Window`** stretch and **`content_scale_factor`** (and platform display scale where the project reads `DisplayServer.screen_get_scale`) so UI stays readable on high-DPI displays.
- **Motion**: if the project exposes “reduce motion,” gate camera shake, heavy screen flash, and aggressive full-screen post hits behind that setting.

## Principles

- Test **full critical path** with keyboard only after substantive UI changes.
- Prefer **native Control** behavior (buttons, sliders) over custom-drawn hit regions unless hit testing and focus are implemented deliberately.

## Pitfalls

- **`mouse_filter`** stopping clicks but leaving no keyboard path to the same control.
- **`CanvasLayer`** + separate focus roots confusing tab order—structure layers intentionally.

## Official reference

- GUI tutorial index (focus, input): https://docs.godotengine.org/en/stable/tutorials/ui/index.html
- Accessibility is evolving across Godot versions—verify behavior against the project’s pinned engine minor.
