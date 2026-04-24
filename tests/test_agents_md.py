"""
Tests for AGENTS.md and the repository symlink structure added in this PR.

Validates that:
- AGENTS.md exists at the repository root
- AGENTS.md contains a skill index table listing all PR skills
- Tool-specific symlinks (.codex/skills, .cursor/skills, .gemini/skills) exist
- Symlinks resolve to .agents/skills
- AGENTS.md correctly documents canonical paths and symlink locations
"""

import os
import re
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTS_MD = os.path.join(REPO_ROOT, "AGENTS.md")
SKILLS_DIR = os.path.join(REPO_ROOT, ".agents", "skills")

# Symlinks added in the PR: tool-specific locations pointing to .agents/skills
EXPECTED_SYMLINKS = [
    os.path.join(REPO_ROOT, ".codex", "skills"),
    os.path.join(REPO_ROOT, ".cursor", "skills"),
    os.path.join(REPO_ROOT, ".gemini", "skills"),
]

# All skills added in this PR that must appear in the AGENTS.md index
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


# ---------------------------------------------------------------------------
# AGENTS.md existence and basic structure
# ---------------------------------------------------------------------------

class TestAgentsMdExists:
    def test_agents_md_exists(self):
        """AGENTS.md must exist at the repository root."""
        assert os.path.isfile(AGENTS_MD), f"AGENTS.md not found at {AGENTS_MD}"

    def test_agents_md_not_empty(self):
        """AGENTS.md must not be empty."""
        assert os.path.getsize(AGENTS_MD) > 0, "AGENTS.md is empty"

    def test_agents_md_ends_with_newline(self):
        """AGENTS.md must end with a newline character."""
        with open(AGENTS_MD, "rb") as f:
            content = f.read()
        assert content.endswith(b"\n"), "AGENTS.md does not end with a newline"

    def test_agents_md_readable_utf8(self):
        """AGENTS.md must be valid UTF-8."""
        with open(AGENTS_MD, "r", encoding="utf-8") as f:
            content = f.read()
        assert len(content) > 0


class TestAgentsMdContent:
    """Validate the content of AGENTS.md."""

    def _read_agents_md(self) -> str:
        with open(AGENTS_MD, "r", encoding="utf-8") as f:
            return f.read()

    def test_agents_md_has_h1_heading(self):
        """AGENTS.md must have an H1 heading."""
        content = self._read_agents_md()
        h1_lines = [l for l in content.splitlines() if l.startswith("# ")]
        assert h1_lines, "AGENTS.md must have an H1 heading"

    def test_agents_md_h1_references_godot(self):
        """AGENTS.md H1 heading must reference 'Godot' or 'Agent'."""
        content = self._read_agents_md()
        h1_match = re.search(r"^# (.+)$", content, re.MULTILINE)
        assert h1_match, "No H1 heading found in AGENTS.md"
        title = h1_match.group(1)
        assert "Godot" in title or "Agent" in title, (
            f"AGENTS.md H1 does not reference 'Godot' or 'Agent': {title!r}"
        )

    def test_agents_md_documents_canonical_skills_path(self):
        """AGENTS.md must document the canonical .agents/skills/ path."""
        content = self._read_agents_md()
        assert ".agents/skills" in content, (
            "AGENTS.md must document the canonical '.agents/skills' path"
        )

    def test_agents_md_mentions_symlinks(self):
        """AGENTS.md must mention the symlink locations (.cursor/skills, .codex/skills, .gemini/skills)."""
        content = self._read_agents_md()
        assert ".cursor/skills" in content, "AGENTS.md must mention .cursor/skills symlink"
        assert ".codex/skills" in content, "AGENTS.md must mention .codex/skills symlink"
        assert ".gemini/skills" in content, "AGENTS.md must mention .gemini/skills symlink"

    def test_agents_md_has_skill_index_table(self):
        """AGENTS.md must contain a skill index table (markdown table)."""
        content = self._read_agents_md()
        # A markdown table has lines starting with | character
        table_lines = [l for l in content.splitlines() if l.strip().startswith("|")]
        assert len(table_lines) >= 3, (
            "AGENTS.md must contain a skill index table with at least header + separator + one row"
        )

    def test_agents_md_targets_godot_4(self):
        """AGENTS.md must state it targets Godot 4.x."""
        content = self._read_agents_md()
        assert "Godot 4" in content or "Godot 4.x" in content, (
            "AGENTS.md must state it targets Godot 4.x"
        )

    def test_agents_md_mentions_gdscript_preference(self):
        """AGENTS.md must document the GDScript preference."""
        content = self._read_agents_md()
        assert "GDScript" in content, "AGENTS.md must mention GDScript preference"

    def test_agents_md_has_repository_maintenance_section(self):
        """AGENTS.md must include a repository maintenance or similar guidance section."""
        content = self._read_agents_md()
        assert "maintenance" in content.lower() or "Repository" in content, (
            "AGENTS.md must include repository maintenance guidance"
        )

    def test_agents_md_instructs_edit_under_agents_skills(self):
        """AGENTS.md must instruct users to edit files only under .agents/skills."""
        content = self._read_agents_md()
        assert ".agents/skills" in content, (
            "AGENTS.md must instruct users to edit under .agents/skills"
        )


# ---------------------------------------------------------------------------
# Skill index completeness: every PR skill must appear in AGENTS.md
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("skill_name", PR_SKILLS)
class TestAgentsMdSkillIndex:
    def test_skill_listed_in_agents_md(self, skill_name):
        """Every PR skill folder name must appear in AGENTS.md skill index."""
        with open(AGENTS_MD, "r", encoding="utf-8") as f:
            content = f.read()
        assert skill_name in content, (
            f"Skill '{skill_name}' is not listed in AGENTS.md skill index"
        )

    def test_skill_appears_in_table_row(self, skill_name):
        """Each PR skill must appear in a markdown table row in AGENTS.md."""
        with open(AGENTS_MD, "r", encoding="utf-8") as f:
            content = f.read()
        # A table row containing the skill name starts with |
        table_rows = [
            l for l in content.splitlines()
            if l.strip().startswith("|") and skill_name in l
        ]
        assert table_rows, (
            f"Skill '{skill_name}' not found in any table row in AGENTS.md"
        )


# ---------------------------------------------------------------------------
# Symlink tests
# ---------------------------------------------------------------------------

class TestSymlinks:
    def test_codex_skills_symlink_exists(self):
        """'.codex/skills' must exist (as a symlink or directory)."""
        path = os.path.join(REPO_ROOT, ".codex", "skills")
        assert os.path.exists(path), f"'.codex/skills' not found: {path}"

    def test_cursor_skills_symlink_exists(self):
        """'.cursor/skills' must exist (as a symlink or directory)."""
        path = os.path.join(REPO_ROOT, ".cursor", "skills")
        assert os.path.exists(path), f"'.cursor/skills' not found: {path}"

    def test_gemini_skills_symlink_exists(self):
        """'.gemini/skills' must exist (as a symlink or directory)."""
        path = os.path.join(REPO_ROOT, ".gemini", "skills")
        assert os.path.exists(path), f"'.gemini/skills' not found: {path}"

    def test_codex_skills_is_symlink(self):
        """'.codex/skills' must be a symbolic link."""
        path = os.path.join(REPO_ROOT, ".codex", "skills")
        assert os.path.islink(path), f"'.codex/skills' is not a symlink: {path}"

    def test_cursor_skills_is_symlink(self):
        """'.cursor/skills' must be a symbolic link."""
        path = os.path.join(REPO_ROOT, ".cursor", "skills")
        assert os.path.islink(path), f"'.cursor/skills' is not a symlink: {path}"

    def test_gemini_skills_is_symlink(self):
        """'.gemini/skills' must be a symbolic link."""
        path = os.path.join(REPO_ROOT, ".gemini", "skills")
        assert os.path.islink(path), f"'.gemini/skills' is not a symlink: {path}"

    def test_codex_skills_symlink_resolves(self):
        """'.codex/skills' symlink must resolve to a valid directory."""
        path = os.path.join(REPO_ROOT, ".codex", "skills")
        resolved = os.path.realpath(path)
        assert os.path.isdir(resolved), (
            f"'.codex/skills' symlink resolves to non-directory: {resolved}"
        )

    def test_cursor_skills_symlink_resolves(self):
        """'.cursor/skills' symlink must resolve to a valid directory."""
        path = os.path.join(REPO_ROOT, ".cursor", "skills")
        resolved = os.path.realpath(path)
        assert os.path.isdir(resolved), (
            f"'.cursor/skills' symlink resolves to non-directory: {resolved}"
        )

    def test_gemini_skills_symlink_resolves(self):
        """'.gemini/skills' symlink must resolve to a valid directory."""
        path = os.path.join(REPO_ROOT, ".gemini", "skills")
        resolved = os.path.realpath(path)
        assert os.path.isdir(resolved), (
            f"'.gemini/skills' symlink resolves to non-directory: {resolved}"
        )

    def test_symlinks_all_point_to_same_target(self):
        """All three symlinks must resolve to the same canonical target directory."""
        targets = set()
        for symlink_path in EXPECTED_SYMLINKS:
            if os.path.islink(symlink_path):
                targets.add(os.path.realpath(symlink_path))
        assert len(targets) == 1, (
            f"Symlinks resolve to different targets: {targets}. "
            f"All should point to .agents/skills"
        )

    def test_symlinks_point_to_agents_skills(self):
        """All symlinks must ultimately resolve to .agents/skills."""
        expected_target = os.path.realpath(SKILLS_DIR)
        for symlink_path in EXPECTED_SYMLINKS:
            if os.path.islink(symlink_path):
                resolved = os.path.realpath(symlink_path)
                assert resolved == expected_target, (
                    f"Symlink {symlink_path!r} resolves to {resolved!r}, "
                    f"expected {expected_target!r}"
                )

    def test_symlinks_provide_access_to_skills(self):
        """Accessing skills through a symlink path must work (sanity check)."""
        cursor_skills = os.path.join(REPO_ROOT, ".cursor", "skills")
        if os.path.isdir(cursor_skills):
            entries = os.listdir(cursor_skills)
            assert len(entries) > 0, (
                "'.cursor/skills' directory is accessible but empty"
            )

    def test_symlinks_expose_pr_skills(self):
        """Symlinked paths must expose the PR skill folders."""
        cursor_skills = os.path.join(REPO_ROOT, ".cursor", "skills")
        if os.path.isdir(cursor_skills):
            entries = set(os.listdir(cursor_skills))
            for skill in PR_SKILLS:
                assert skill in entries, (
                    f"Skill '{skill}' not accessible via .cursor/skills symlink"
                )


# ---------------------------------------------------------------------------
# Skill directory vs AGENTS.md consistency
# ---------------------------------------------------------------------------

class TestSkillDirectoryConsistency:
    """Check that the skill directories on disk match what AGENTS.md documents."""

    def test_all_skills_on_disk_are_in_agents_md(self):
        """Every skill directory under .agents/skills/ must be listed in AGENTS.md."""
        with open(AGENTS_MD, "r", encoding="utf-8") as f:
            agents_content = f.read()

        skill_dirs = [
            d for d in os.listdir(SKILLS_DIR)
            if os.path.isdir(os.path.join(SKILLS_DIR, d)) and d.startswith("godot-")
        ]

        missing = [d for d in skill_dirs if d not in agents_content]
        assert not missing, (
            f"These skill directories exist on disk but are missing from AGENTS.md: {missing}"
        )

    def test_skills_in_agents_md_exist_on_disk(self):
        """Every skill listed in the AGENTS.md index table must have a directory on disk."""
        with open(AGENTS_MD, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract skill names from table rows: lines like | `godot-xxx` | ... |
        table_skill_names = re.findall(r"`(godot-[a-z0-9-]+)`", content)

        missing_dirs = [
            name for name in table_skill_names
            if not os.path.isdir(os.path.join(SKILLS_DIR, name))
        ]
        assert not missing_dirs, (
            f"These skills are listed in AGENTS.md but missing from .agents/skills/: {missing_dirs}"
        )

    def test_skill_count_in_agents_md_matches_disk(self):
        """The number of skill dirs on disk must match skills listed in AGENTS.md table."""
        with open(AGENTS_MD, "r", encoding="utf-8") as f:
            content = f.read()

        disk_skills = sorted([
            d for d in os.listdir(SKILLS_DIR)
            if os.path.isdir(os.path.join(SKILLS_DIR, d)) and d.startswith("godot-")
        ])
        agents_md_skills = sorted(set(re.findall(r"`(godot-[a-z0-9-]+)`", content)))

        assert len(disk_skills) == len(agents_md_skills), (
            f"Skill count mismatch: {len(disk_skills)} dirs on disk vs "
            f"{len(agents_md_skills)} listed in AGENTS.md.\n"
            f"On disk only: {sorted(set(disk_skills) - set(agents_md_skills))}\n"
            f"In AGENTS.md only: {sorted(set(agents_md_skills) - set(disk_skills))}"
        )