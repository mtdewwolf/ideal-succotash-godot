---
name: godot-internationalization
description: Use for Godot 4 localization—translations, CSV/PO workflows, tr(), locales, fonts, and RTL. Use when adding languages, fixing missing strings, or layout issues with translated UI.
---

# Godot 4 — internationalization (i18n)

Use with **`godot-ui-input-animation-audio`** for Control layout that must reflow when text length changes, and **`godot-assets-import-pipeline`** for font and locale-specific assets.

## When to use this skill

- **Project settings**: locale fallbacks, test locale, translation project list.
- **Translation resources**: `.po`, `.csv`, or Godot translation files; keeping **message ids** stable when designers rephrase English.
- **Code and scenes**: `tr()`, `tr_n()` for pluralization where applicable; avoiding string concatenation that breaks translation order.
- **Fonts**: dynamic fonts, fallback glyphs, **RTL** and bidirectional text in `TextEdit` / `Label`—verify in editor with a RTL test locale.
- **Audio/voice**: per-locale packs if the project uses them—naming and load paths.

## Principles

- **Context comments** for translators on ambiguous strings (weapon “bow” vs verb “bow”).
- Design UI with **extra horizontal space** or containers that grow; German and Finnish often need more room than English.
- Do not bake localized text into **resource paths** or filenames—use ids and map to display strings.

## Pitfalls

- Duplicating the same English string with different meanings → one translation entry; use **context** or disambiguation keys per project convention.
- Forgetting to mark **exported strings** or scene labels that are set only in code.

## Official reference

- Internationalizing games: https://docs.godotengine.org/en/stable/tutorials/i18n/internationalizing_games.html
- Locales: https://docs.godotengine.org/en/stable/tutorials/i18n/locales.html
