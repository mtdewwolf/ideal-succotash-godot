---
name: godot-mobile-platform-notes
description: Use for Godot 4 Android and iOS export—permissions, plugins at a high level, safe areas, input, and mobile performance habits. Not legal or store compliance advice; link platform docs when policies matter.
---

# Godot 4 — mobile platforms (Android / iOS)

Use with **`godot-editor-export-debug`** for `export_presets.cfg`, keystores, and templates; with **`godot-profiling-optimization`** for thermal/GPU limits; with **`godot-gdextension`** or Gradle/Xcode notes only when the repo already uses native plugins.

## When to use this skill

- **Android**: `USE_*` permissions in export preset vs runtime `OS.request_permission`; **Gradle** custom templates if the project has them; notches, **immersive** vs **fullscreen** behaviors.
- **iOS**: capabilities, plist keys via export options, **safe area** for Dynamic Island / home indicator; C# on iOS may still carry experimental caveats—check current Godot release notes for the pinned version.
- **Input**: touch vs mouse emulation, **gesture** handling, on-screen controls sizing for different aspect ratios.
- **Performance**: thermal throttling, backgrounding, aggressive OS kills—save often to `user://` (see **`godot-files-data-io`**).

## Principles

- Match **minimum SDK / deployment target** to what Godot’s export dialog documents for the engine version in use.
- Prefer **existing project plugins** over inventing new native bridges without user approval.

## Pitfalls

- Shipping with **debug keystore** or **verbose logging** enabled unintentionally.
- Assuming **desktop-class** draw call and particle budgets on mid-tier phones.

## Official reference

- Exporting for Android: https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html
- Exporting for iOS: https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_ios.html
