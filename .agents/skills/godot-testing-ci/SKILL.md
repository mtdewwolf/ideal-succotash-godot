---
name: godot-testing-ci
description: Use for automated tests, headless runs, CI jobs, and static checks on Godot 4 projects. Use when adding GitHub Actions, fixing flaky tests, or structuring test scenes.
---

# Godot 4 — testing and CI

## When to use this skill

- **Headless / batch**: run the project or specific scenes with documented Godot CLI flags; keep **engine version** pinned in CI (same as `export_presets.cfg` / team policy).
- **Unit and integration tests**: if the repo uses **GdUnit**, **WAT**, or custom test harnesses, extend those—do not introduce a second framework without explicit user direction.
- **Test scenes**: minimal scenes that autoload a test runner or quit with exit code on failure—match how this repository (or parent game repo) already signals success/failure.
- **Determinism**: seed RNG for tests; avoid real-time `await` without caps; mock network for multiplayer tests.

## Principles

- CI should **fail fast** on script errors: use `--quit` patterns or test addons that exit nonzero on failure.
- Cache **export templates** or engine downloads in CI when builds are slow—document in the workflow comments if non-obvious.

## What agents should avoid

- Assuming `godot` is on PATH with a specific name—use the binary name the workflow defines (`godot4`, `Godot_v4.x`, etc.).

## Official reference

- Command line: https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html
- Unit testing (engine overview): https://docs.godotengine.org/en/stable/tutorials/scripting/unit_testing.html
