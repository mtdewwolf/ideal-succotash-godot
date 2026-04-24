---
name: godot-gdextension
description: Use for native GDExtension (C++, Rust, etc.)—gextension files, class registration, binding layers, and interop with GDScript/C#. Not for pure GDScript gameplay unless calling into extensions.
---

# Godot 4 — GDExtension

## When to use this skill

- **Entry and discovery**: `.gdextension` TOML pointing at the compiled library for each platform; version compatibility with the **exact Godot minor** the team pins.
- **Build layout**: separate build artifacts per OS/arch; never commit huge binaries unless the repo policy allows—often CI builds them.
- **Class registration**: exposing `Node`-derived types, methods, properties, and signals to the engine; match Godot’s threading and **pointer lifetime** rules for native code.
- **Hot reload / iteration**: know that native changes require rebuild and editor restart depending on platform and loader behavior.

## Principles

- Treat GDExtension as a **narrow performance or integration boundary** (physics, third-party SDKs, heavy SIMD)—keep game design logic in GDScript/C# unless the project standard says otherwise.
- When agents cannot compile native code in the environment, **edit sources and build scripts** but flag that the user must run the project’s documented build (cmake, scons, cargo, etc.).

## Interop

- From GDScript, call registered methods like any other node API; respect **thread affinity** documented for the extension.

## Official reference

- GDExtension intro: https://docs.godotengine.org/en/stable/tutorials/scripting/gdextension/what_is_gdextension.html
