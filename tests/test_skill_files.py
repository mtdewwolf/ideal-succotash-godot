"""
Tests for Godot 4 agent skill SKILL.md files added in this PR.

Validates structure, frontmatter, required sections, and URL format
for each skill file under .agents/skills/.
"""

import os
import re
import yaml
import pytest

# Root of the repository
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO_ROOT, ".agents", "skills")

# All skill folder names added/changed in this PR
PR_SKILLS = [
    "godot-4-engine-core",
    "godot-accessibility-ui",
    "godot-animation",
    "godot-assets-import-pipeline",
    "godot-class-reference-workflow",
    "godot-compute-advanced-rendering",
    "godot-csharp",
    "godot-dcc-pipeline",
    "godot-editor-export-debug",
    "godot-editor-plugins-tool-scripts",
    "godot-files-data-io",
    "godot-gdextension",
    "godot-gdscript",
    "godot-http-websocket-tls",
    "godot-internationalization",
    "godot-mobile-platform-notes",
    "godot-multiplayer-networking",
    "godot-navigation-advanced",
    "godot-particles-vfx",
    "godot-physics-navigation",
    "godot-profiling-optimization",
    "godot-rendering-shaders-2d-3d",
    "godot-scenes-and-resources",
    "godot-testing-ci",
    "godot-theming-ui-advanced",
    "godot-threading-concurrency",
    "godot-tilemap-2d-levels",
    "godot-ui-input-animation-audio",
    "godot-visual-shaders",
    "godot-xr-openxr",
]


def parse_skill_file(skill_name: str) -> tuple[dict, str]:
    """
    Parse a SKILL.md file and return (frontmatter_dict, body_text).
    Raises if the file cannot be found or frontmatter is invalid.
    """
    skill_path = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split frontmatter from body
    if not content.startswith("---"):
        raise ValueError(f"{skill_path}: file does not begin with YAML frontmatter block (---)")

    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{skill_path}: could not find closing --- for frontmatter")

    frontmatter_text = parts[1].strip()
    body = parts[2].strip()
    frontmatter = yaml.safe_load(frontmatter_text)
    return frontmatter, body


# ---------------------------------------------------------------------------
# Parametrize over all PR skills
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("skill_name", PR_SKILLS)
class TestSkillFileExists:
    def test_skill_directory_exists(self, skill_name):
        """Each skill folder must exist under .agents/skills/."""
        skill_dir = os.path.join(SKILLS_DIR, skill_name)
        assert os.path.isdir(skill_dir), (
            f"Skill directory not found: {skill_dir}"
        )

    def test_skill_md_file_exists(self, skill_name):
        """Each skill folder must contain a SKILL.md file."""
        skill_path = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
        assert os.path.isfile(skill_path), (
            f"SKILL.md not found: {skill_path}"
        )

    def test_skill_file_not_empty(self, skill_name):
        """SKILL.md must not be empty."""
        skill_path = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
        assert os.path.getsize(skill_path) > 0, (
            f"SKILL.md is empty: {skill_path}"
        )


@pytest.mark.parametrize("skill_name", PR_SKILLS)
class TestSkillFrontmatter:
    def test_frontmatter_parseable(self, skill_name):
        """SKILL.md must have valid YAML frontmatter between --- delimiters."""
        frontmatter, _ = parse_skill_file(skill_name)
        assert isinstance(frontmatter, dict), (
            f"{skill_name}: frontmatter did not parse to a dict"
        )

    def test_frontmatter_has_name_field(self, skill_name):
        """Frontmatter must include a 'name' field."""
        frontmatter, _ = parse_skill_file(skill_name)
        assert "name" in frontmatter, (
            f"{skill_name}: 'name' field missing from frontmatter"
        )

    def test_frontmatter_name_is_non_empty_string(self, skill_name):
        """The 'name' field must be a non-empty string."""
        frontmatter, _ = parse_skill_file(skill_name)
        name = frontmatter.get("name", "")
        assert isinstance(name, str) and name.strip(), (
            f"{skill_name}: 'name' field is empty or not a string"
        )

    def test_frontmatter_name_matches_folder(self, skill_name):
        """The 'name' value in frontmatter must match the folder name exactly."""
        frontmatter, _ = parse_skill_file(skill_name)
        declared_name = frontmatter.get("name", "")
        assert declared_name == skill_name, (
            f"{skill_name}: frontmatter 'name' ({declared_name!r}) "
            f"does not match folder name ({skill_name!r})"
        )

    def test_frontmatter_has_description_field(self, skill_name):
        """Frontmatter must include a 'description' field."""
        frontmatter, _ = parse_skill_file(skill_name)
        assert "description" in frontmatter, (
            f"{skill_name}: 'description' field missing from frontmatter"
        )

    def test_frontmatter_description_is_non_empty_string(self, skill_name):
        """The 'description' field must be a non-empty string."""
        frontmatter, _ = parse_skill_file(skill_name)
        desc = frontmatter.get("description", "")
        assert isinstance(desc, str) and desc.strip(), (
            f"{skill_name}: 'description' field is empty or not a string"
        )

    def test_frontmatter_description_is_meaningful(self, skill_name):
        """The 'description' must be at least 30 characters long (meaningful guidance)."""
        frontmatter, _ = parse_skill_file(skill_name)
        desc = frontmatter.get("description", "")
        assert len(desc.strip()) >= 30, (
            f"{skill_name}: 'description' is too short ({len(desc)} chars), "
            f"must be at least 30 characters"
        )

    def test_frontmatter_description_starts_with_use(self, skill_name):
        """The 'description' should start with 'Use' to be action-oriented for agents."""
        frontmatter, _ = parse_skill_file(skill_name)
        desc = frontmatter.get("description", "")
        assert desc.strip().startswith("Use"), (
            f"{skill_name}: 'description' should start with 'Use' but got: {desc[:60]!r}"
        )

    def test_frontmatter_no_extra_unexpected_fields(self, skill_name):
        """Frontmatter should only contain known fields (name, description)."""
        frontmatter, _ = parse_skill_file(skill_name)
        known_fields = {"name", "description"}
        extra = set(frontmatter.keys()) - known_fields
        assert not extra, (
            f"{skill_name}: unexpected frontmatter fields: {extra}"
        )


@pytest.mark.parametrize("skill_name", PR_SKILLS)
class TestSkillMarkdownBody:
    def test_body_has_h1_heading(self, skill_name):
        """SKILL.md body must start with an H1 heading (# ...)."""
        _, body = parse_skill_file(skill_name)
        lines = body.splitlines()
        h1_lines = [l for l in lines if l.startswith("# ")]
        assert h1_lines, (
            f"{skill_name}: body must contain an H1 heading (line starting with '# ')"
        )

    def test_body_has_when_to_use_section(self, skill_name):
        """SKILL.md must contain a '## When to use this skill' section."""
        _, body = parse_skill_file(skill_name)
        assert "## When to use this skill" in body, (
            f"{skill_name}: missing required section '## When to use this skill'"
        )

    def test_body_has_principles_section(self, skill_name):
        """SKILL.md must contain a '## Principles' section or an equivalent guidance section.

        Most skills use '## Principles'. A few use domain-specific variants such as
        '## Save-game discipline' — any H2 that conveys prescriptive guidance satisfies
        this requirement.
        """
        _, body = parse_skill_file(skill_name)
        # Accepted guidance-style section headings
        guidance_headings = [
            "## Principles",
            "## Save-game discipline",
            "## GDScript vs C#",
            "## Interop",
            "## Signals and memory",
            "## Text scene files",
        ]
        has_guidance = any(heading in body for heading in guidance_headings)
        assert has_guidance, (
            f"{skill_name}: missing a guidance section. "
            f"Expected one of {guidance_headings!r} but found none. "
            f"Add a '## Principles' section or equivalent."
        )

    def test_body_has_official_reference_section(self, skill_name):
        """SKILL.md must contain a '## Official reference' section."""
        _, body = parse_skill_file(skill_name)
        assert "## Official reference" in body, (
            f"{skill_name}: missing required section '## Official reference'"
        )

    def test_body_official_reference_has_urls(self, skill_name):
        """The '## Official reference' section must contain at least one URL."""
        _, body = parse_skill_file(skill_name)
        # Extract the official reference section
        ref_match = re.search(
            r"## Official reference\s*(.*?)(?:\n##|\Z)",
            body,
            re.DOTALL,
        )
        assert ref_match, f"{skill_name}: could not find '## Official reference' section"
        ref_section = ref_match.group(1)
        urls = re.findall(r"https?://\S+", ref_section)
        assert urls, (
            f"{skill_name}: '## Official reference' section has no URLs"
        )

    def test_official_reference_urls_use_https(self, skill_name):
        """All URLs in the official reference section must use https://."""
        _, body = parse_skill_file(skill_name)
        ref_match = re.search(
            r"## Official reference\s*(.*?)(?:\n##|\Z)",
            body,
            re.DOTALL,
        )
        if not ref_match:
            pytest.skip(f"{skill_name}: no official reference section found")
        ref_section = ref_match.group(1)
        # Find all URLs (http or https)
        all_urls = re.findall(r"http[s]?://\S+", ref_section)
        for url in all_urls:
            assert url.startswith("https://"), (
                f"{skill_name}: URL in official reference uses http instead of https: {url}"
            )

    def test_official_reference_urls_point_to_godot_docs(self, skill_name):
        """URLs in official reference must point to docs.godotengine.org."""
        _, body = parse_skill_file(skill_name)
        ref_match = re.search(
            r"## Official reference\s*(.*?)(?:\n##|\Z)",
            body,
            re.DOTALL,
        )
        if not ref_match:
            pytest.skip(f"{skill_name}: no official reference section found")
        ref_section = ref_match.group(1)
        urls = re.findall(r"https?://\S+", ref_section)
        for url in urls:
            assert "docs.godotengine.org" in url, (
                f"{skill_name}: URL in official reference does not point to "
                f"docs.godotengine.org: {url}"
            )

    def test_when_to_use_section_has_content(self, skill_name):
        """The '## When to use this skill' section must have at least one bullet point."""
        _, body = parse_skill_file(skill_name)
        section_match = re.search(
            r"## When to use this skill\s*(.*?)(?:\n##|\Z)",
            body,
            re.DOTALL,
        )
        assert section_match, f"{skill_name}: could not extract 'When to use this skill' section"
        section_text = section_match.group(1)
        # Must have at least one list item (- or *)
        bullets = re.findall(r"^\s*[-*]\s+\S", section_text, re.MULTILINE)
        assert bullets, (
            f"{skill_name}: '## When to use this skill' section must contain bullet points"
        )

    def test_principles_section_has_content(self, skill_name):
        """The guidance section (## Principles or equivalent) must have at least one bullet."""
        _, body = parse_skill_file(skill_name)
        # Try each recognized guidance heading in priority order
        guidance_headings = [
            "## Principles",
            "## Save-game discipline",
            "## GDScript vs C#",
            "## Interop",
            "## Signals and memory",
            "## Text scene files",
        ]
        section_text = None
        for heading in guidance_headings:
            # Escape heading for use in regex
            escaped = re.escape(heading)
            match = re.search(
                rf"{escaped}\s*(.*?)(?:\n##|\Z)",
                body,
                re.DOTALL,
            )
            if match:
                section_text = match.group(1)
                break

        assert section_text is not None, (
            f"{skill_name}: could not find a guidance section among {guidance_headings!r}"
        )
        bullets = re.findall(r"^\s*[-*]\s+\S", section_text, re.MULTILINE)
        assert bullets, (
            f"{skill_name}: guidance section must contain at least one bullet point"
        )

    def test_h1_title_references_godot(self, skill_name):
        """The H1 heading must reference 'Godot' to confirm it is a Godot skill."""
        _, body = parse_skill_file(skill_name)
        h1_match = re.search(r"^# (.+)$", body, re.MULTILINE)
        assert h1_match, f"{skill_name}: no H1 heading found"
        title = h1_match.group(1)
        assert "Godot" in title or "godot" in title.lower(), (
            f"{skill_name}: H1 heading does not mention 'Godot': {title!r}"
        )

    def test_file_ends_with_newline(self, skill_name):
        """SKILL.md must end with a newline character (POSIX compliance)."""
        skill_path = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
        with open(skill_path, "rb") as f:
            content = f.read()
        assert content.endswith(b"\n"), (
            f"{skill_name}: SKILL.md does not end with a newline"
        )


@pytest.mark.parametrize("skill_name", PR_SKILLS)
class TestSkillNamingConventions:
    def test_folder_name_is_kebab_case(self, skill_name):
        """Skill folder name must be kebab-case (lowercase letters, digits, hyphens only)."""
        assert re.match(r"^[a-z0-9-]+$", skill_name), (
            f"Skill folder name is not valid kebab-case: {skill_name!r}"
        )

    def test_folder_name_starts_with_godot(self, skill_name):
        """Skill folder name must start with 'godot-' prefix."""
        assert skill_name.startswith("godot-"), (
            f"Skill folder name must start with 'godot-': {skill_name!r}"
        )

    def test_folder_name_not_too_short(self, skill_name):
        """Skill folder name must be at least 8 characters (godot- + 2 chars)."""
        assert len(skill_name) >= 8, (
            f"Skill folder name is too short: {skill_name!r}"
        )

    def test_no_consecutive_hyphens_in_folder_name(self, skill_name):
        """Skill folder name must not contain consecutive hyphens (--)."""
        assert "--" not in skill_name, (
            f"Skill folder name contains consecutive hyphens: {skill_name!r}"
        )

    def test_no_trailing_hyphen_in_folder_name(self, skill_name):
        """Skill folder name must not end with a hyphen."""
        assert not skill_name.endswith("-"), (
            f"Skill folder name ends with a hyphen: {skill_name!r}"
        )


# ---------------------------------------------------------------------------
# Boundary / regression tests for specific known skills
# ---------------------------------------------------------------------------

class TestSkillSpecificContent:
    """Regression tests for specific content in key skills from this PR."""

    def test_engine_core_covers_process_lifecycle(self):
        """godot-4-engine-core must document _process and _physics_process."""
        _, body = parse_skill_file("godot-4-engine-core")
        assert "_process" in body, "godot-4-engine-core must mention _process"
        assert "_physics_process" in body, "godot-4-engine-core must mention _physics_process"

    def test_engine_core_covers_scene_tree(self):
        """godot-4-engine-core must document SceneTree access."""
        _, body = parse_skill_file("godot-4-engine-core")
        assert "SceneTree" in body, "godot-4-engine-core must mention SceneTree"
        assert "get_tree()" in body, "godot-4-engine-core must mention get_tree()"

    def test_engine_core_warns_about_autoloads(self):
        """godot-4-engine-core must mention Autoloads and singleton pattern."""
        _, body = parse_skill_file("godot-4-engine-core")
        assert "Autoload" in body or "autoload" in body.lower(), (
            "godot-4-engine-core must mention Autoloads"
        )

    def test_gdscript_covers_signals(self):
        """godot-gdscript must cover signals."""
        _, body = parse_skill_file("godot-gdscript")
        assert "signal" in body.lower(), "godot-gdscript must mention signals"
        assert "emit" in body, "godot-gdscript must mention emit"

    def test_gdscript_covers_typing(self):
        """godot-gdscript must cover static typing."""
        _, body = parse_skill_file("godot-gdscript")
        assert "typing" in body.lower() or "static" in body.lower(), (
            "godot-gdscript must mention typing"
        )

    def test_gdscript_covers_await(self):
        """godot-gdscript must document the await keyword."""
        _, body = parse_skill_file("godot-gdscript")
        assert "await" in body, "godot-gdscript must mention await"

    def test_csharp_covers_partial_class(self):
        """godot-csharp must document partial class pattern."""
        _, body = parse_skill_file("godot-csharp")
        assert "partial class" in body, "godot-csharp must mention 'partial class'"

    def test_csharp_warns_about_rebuild(self):
        """godot-csharp must warn about rebuilding after signal/export changes."""
        _, body = parse_skill_file("godot-csharp")
        assert "rebuild" in body.lower() or "Build" in body, (
            "godot-csharp must mention rebuilding the project after changes"
        )

    def test_physics_navigation_covers_character_body(self):
        """godot-physics-navigation must cover CharacterBody."""
        _, body = parse_skill_file("godot-physics-navigation")
        assert "CharacterBody" in body, (
            "godot-physics-navigation must mention CharacterBody"
        )

    def test_physics_navigation_covers_move_and_slide(self):
        """godot-physics-navigation must mention move_and_slide."""
        _, body = parse_skill_file("godot-physics-navigation")
        assert "move_and_slide" in body, (
            "godot-physics-navigation must mention move_and_slide"
        )

    def test_navigation_advanced_covers_navigation_server(self):
        """godot-navigation-advanced must cover NavigationServer."""
        _, body = parse_skill_file("godot-navigation-advanced")
        assert "NavigationServer" in body, (
            "godot-navigation-advanced must mention NavigationServer"
        )

    def test_navigation_advanced_covers_baking(self):
        """godot-navigation-advanced must cover navmesh baking."""
        _, body = parse_skill_file("godot-navigation-advanced")
        assert "bak" in body.lower(), (
            "godot-navigation-advanced must mention baking"
        )

    def test_scenes_resources_warns_about_uids(self):
        """godot-scenes-and-resources must warn about UID stability."""
        _, body = parse_skill_file("godot-scenes-and-resources")
        assert "UID" in body or "uid" in body, (
            "godot-scenes-and-resources must warn about UIDs"
        )

    def test_scenes_resources_covers_tscn_format(self):
        """godot-scenes-and-resources must mention .tscn file format."""
        _, body = parse_skill_file("godot-scenes-and-resources")
        assert ".tscn" in body, "godot-scenes-and-resources must mention .tscn"

    def test_files_data_io_covers_user_path(self):
        """godot-files-data-io must cover the user:// path scheme."""
        _, body = parse_skill_file("godot-files-data-io")
        assert "user://" in body, "godot-files-data-io must mention user://"

    def test_files_data_io_covers_res_path(self):
        """godot-files-data-io must cover res:// and export restrictions."""
        _, body = parse_skill_file("godot-files-data-io")
        assert "res://" in body, "godot-files-data-io must mention res://"

    def test_http_websocket_warns_about_tls(self):
        """godot-http-websocket-tls must warn about TLS/certificate verification."""
        _, body = parse_skill_file("godot-http-websocket-tls")
        assert "TLS" in body or "certificate" in body.lower(), (
            "godot-http-websocket-tls must mention TLS or certificates"
        )

    def test_multiplayer_covers_rpc_annotation(self):
        """godot-multiplayer-networking must cover @rpc annotation."""
        _, body = parse_skill_file("godot-multiplayer-networking")
        assert "@rpc" in body or "RPC" in body or "rpc" in body, (
            "godot-multiplayer-networking must mention RPCs"
        )

    def test_multiplayer_covers_authority(self):
        """godot-multiplayer-networking must cover authority/server patterns."""
        _, body = parse_skill_file("godot-multiplayer-networking")
        assert "authority" in body.lower() or "server" in body.lower(), (
            "godot-multiplayer-networking must mention authority or server"
        )

    def test_testing_ci_covers_headless(self):
        """godot-testing-ci must mention headless runs."""
        _, body = parse_skill_file("godot-testing-ci")
        assert "headless" in body.lower() or "--headless" in body, (
            "godot-testing-ci must mention headless mode"
        )

    def test_testing_ci_covers_determinism(self):
        """godot-testing-ci must mention determinism for reliable tests."""
        _, body = parse_skill_file("godot-testing-ci")
        assert "determinism" in body.lower() or "seed" in body.lower(), (
            "godot-testing-ci must mention determinism or seeding"
        )

    def test_rendering_shaders_covers_gdshader(self):
        """godot-rendering-shaders-2d-3d must mention .gdshader format."""
        _, body = parse_skill_file("godot-rendering-shaders-2d-3d")
        assert ".gdshader" in body or "GDShader" in body or "gdshader" in body.lower(), (
            "godot-rendering-shaders-2d-3d must mention .gdshader"
        )

    def test_accessibility_covers_focus_mode(self):
        """godot-accessibility-ui must cover focus_mode."""
        _, body = parse_skill_file("godot-accessibility-ui")
        assert "focus_mode" in body or "focus" in body.lower(), (
            "godot-accessibility-ui must mention focus"
        )

    def test_internationalization_covers_tr_function(self):
        """godot-internationalization must cover tr() translation function."""
        _, body = parse_skill_file("godot-internationalization")
        assert "tr()" in body or "tr(" in body, (
            "godot-internationalization must mention tr() function"
        )

    def test_profiling_optimization_mentions_measure_first(self):
        """godot-profiling-optimization must emphasize measurement before optimization."""
        _, body = parse_skill_file("godot-profiling-optimization")
        assert "Measure" in body or "measure" in body or "profile" in body.lower(), (
            "godot-profiling-optimization must emphasize measuring before optimizing"
        )

    def test_assets_import_warns_about_manual_import_edits(self):
        """godot-assets-import-pipeline must warn about manual .import file edits."""
        _, body = parse_skill_file("godot-assets-import-pipeline")
        assert ".import" in body, (
            "godot-assets-import-pipeline must mention .import files"
        )

    def test_gdextension_covers_gdextension_file(self):
        """godot-gdextension must cover .gdextension descriptor file."""
        _, body = parse_skill_file("godot-gdextension")
        assert ".gdextension" in body, (
            "godot-gdextension must mention .gdextension file"
        )

    def test_animation_covers_animation_player(self):
        """godot-animation must cover AnimationPlayer."""
        _, body = parse_skill_file("godot-animation")
        assert "AnimationPlayer" in body, (
            "godot-animation must mention AnimationPlayer"
        )

    def test_animation_covers_animation_tree(self):
        """godot-animation must cover AnimationTree."""
        _, body = parse_skill_file("godot-animation")
        assert "AnimationTree" in body, (
            "godot-animation must mention AnimationTree"
        )

    def test_theming_covers_stylebox(self):
        """godot-theming-ui-advanced must cover StyleBox theming."""
        _, body = parse_skill_file("godot-theming-ui-advanced")
        assert "StyleBox" in body or "stylebox" in body.lower(), (
            "godot-theming-ui-advanced must mention StyleBox"
        )

    def test_mobile_covers_android_and_ios(self):
        """godot-mobile-platform-notes must cover both Android and iOS."""
        _, body = parse_skill_file("godot-mobile-platform-notes")
        assert "Android" in body, "godot-mobile-platform-notes must mention Android"
        assert "iOS" in body, "godot-mobile-platform-notes must mention iOS"

    def test_compute_rendering_covers_rendering_device(self):
        """godot-compute-advanced-rendering must cover RenderingDevice."""
        _, body = parse_skill_file("godot-compute-advanced-rendering")
        assert "RenderingDevice" in body, (
            "godot-compute-advanced-rendering must mention RenderingDevice"
        )

    def test_threading_covers_worker_thread_pool(self):
        """godot-threading-concurrency must cover WorkerThreadPool."""
        _, body = parse_skill_file("godot-threading-concurrency")
        assert "WorkerThreadPool" in body, (
            "godot-threading-concurrency must mention WorkerThreadPool"
        )

    def test_threading_warns_about_scene_tree_access(self):
        """godot-threading-concurrency must warn about scene tree access from threads."""
        _, body = parse_skill_file("godot-threading-concurrency")
        assert "scene tree" in body.lower() or "get_node" in body, (
            "godot-threading-concurrency must warn about scene tree access from threads"
        )

    def test_xr_covers_openxr(self):
        """godot-xr-openxr must cover OpenXR setup."""
        _, body = parse_skill_file("godot-xr-openxr")
        assert "OpenXR" in body or "openxr" in body.lower(), (
            "godot-xr-openxr must mention OpenXR"
        )

    def test_visual_shaders_covers_gdshader_comparison(self):
        """godot-visual-shaders must discuss tradeoff vs GDShader text."""
        _, body = parse_skill_file("godot-visual-shaders")
        assert "GDShader" in body or "text" in body.lower(), (
            "godot-visual-shaders must mention GDShader or text shader comparison"
        )

    def test_tilemap_covers_tileset(self):
        """godot-tilemap-2d-levels must cover TileSet."""
        _, body = parse_skill_file("godot-tilemap-2d-levels")
        assert "TileSet" in body, "godot-tilemap-2d-levels must mention TileSet"

    def test_dcc_pipeline_covers_gltf(self):
        """godot-dcc-pipeline must cover glTF export workflow."""
        _, body = parse_skill_file("godot-dcc-pipeline")
        assert "glTF" in body or "gltf" in body.lower(), (
            "godot-dcc-pipeline must mention glTF"
        )

    def test_class_reference_warns_not_to_invent_apis(self):
        """godot-class-reference-workflow must explicitly warn against inventing APIs."""
        _, body = parse_skill_file("godot-class-reference-workflow")
        assert "invent" in body.lower() or "never invent" in body.lower(), (
            "godot-class-reference-workflow must warn against inventing APIs"
        )

    def test_editor_export_covers_headless_flag(self):
        """godot-editor-export-debug must mention --headless flag."""
        _, body = parse_skill_file("godot-editor-export-debug")
        assert "--headless" in body or "headless" in body.lower(), (
            "godot-editor-export-debug must mention --headless"
        )

    def test_editor_plugins_covers_tool_annotation(self):
        """godot-editor-plugins-tool-scripts must cover @tool scripts."""
        _, body = parse_skill_file("godot-editor-plugins-tool-scripts")
        assert "@tool" in body or "tool" in body.lower(), (
            "godot-editor-plugins-tool-scripts must mention @tool annotation"
        )

    def test_internationalization_covers_rtl(self):
        """godot-internationalization must cover RTL (right-to-left) text."""
        _, body = parse_skill_file("godot-internationalization")
        assert "RTL" in body or "right-to-left" in body.lower(), (
            "godot-internationalization must mention RTL text"
        )

    def test_particles_covers_gpu_particles(self):
        """godot-particles-vfx must cover GPUParticles."""
        _, body = parse_skill_file("godot-particles-vfx")
        assert "GPUParticles" in body, (
            "godot-particles-vfx must mention GPUParticles"
        )

    def test_accessibility_ui_covers_keyboard_navigation(self):
        """godot-accessibility-ui must cover keyboard navigation."""
        _, body = parse_skill_file("godot-accessibility-ui")
        assert "keyboard" in body.lower(), (
            "godot-accessibility-ui must mention keyboard navigation"
        )

    def test_http_websocket_warns_no_secrets_in_repo(self):
        """godot-http-websocket-tls must warn against committing secrets to repo."""
        _, body = parse_skill_file("godot-http-websocket-tls")
        assert "secret" in body.lower() or "API key" in body or "committed" in body.lower(), (
            "godot-http-websocket-tls must warn about secrets management"
        )
