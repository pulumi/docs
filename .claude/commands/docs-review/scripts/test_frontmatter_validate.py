#!/usr/bin/env python3
"""Unit tests for frontmatter-validate.py's menu-identifier map.

Self-contained — run with `python3 test_frontmatter_validate.py` (no pytest dep).
Focus: the identifier map must unify content-frontmatter identifiers with the
config-defined ones in `config/_default/menus.yml`, because Hugo resolves menu
parents from either source. The regression this guards: section-level parents
declared only in menus.yml (e.g. `reference-pre-built-policy-packs`) were
reported as missing on every page under those sections.
"""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
FMV_PATH = HERE / "frontmatter-validate.py"

_spec = importlib.util.spec_from_file_location("fmv", FMV_PATH)
fmv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fmv)  # type: ignore[union-attr]


MENUS_YML = """\
# -------------------------------------
# Reference Menus
# -------------------------------------
reference:
  - name: SDKs
    parent: reference-home
    identifier: reference-sdks
    weight: 2
  - name: Pre-built Policy Packs
    parent: reference-home
    identifier: reference-pre-built-policy-packs
    weight: 3
  - name: TypeScript ↗
    parent: reference-sdks
    url: /docs/reference/pkg/nodejs/pulumi/pulumi/
    weight: 1
    identifier: "reference-sdks-javascript"

iac:
  - name: External link, no identifier
    parent: iac-home
    url: /docs/somewhere/
    weight: 1
  - name: Get Started
    parent: iac-home
    identifier: iac-get-started
    weight: 10
"""


def _make_repo(tmp: Path, menus_yml: str | None = MENUS_YML) -> Path:
    """Lay out a minimal repo: config/_default/menus.yml + content/ page(s)."""
    if menus_yml is not None:
        menus_path = tmp / "config" / "_default" / "menus.yml"
        menus_path.parent.mkdir(parents=True)
        menus_path.write_text(menus_yml, encoding="utf-8")
    (tmp / "content").mkdir(exist_ok=True)
    return tmp


def _write_page(repo: Path, rel: str, frontmatter: str) -> str:
    page = repo / rel
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(f"---\n{frontmatter}\n---\n\nBody.\n", encoding="utf-8")
    return rel


def test_config_parser_extracts_identifiers_per_menu():
    with tempfile.TemporaryDirectory() as td:
        repo = _make_repo(Path(td))
        ids = fmv.build_config_menu_identifiers(repo)
        assert ("reference", "reference-pre-built-policy-packs") in ids, ids
        assert ("reference", "reference-sdks") in ids, ids
        assert ("iac", "iac-get-started") in ids, ids
        # Quoted identifier value is unquoted.
        assert ("reference", "reference-sdks-javascript") in ids, ids
        # Identifiers are keyed to their own menu, not leaked across menus.
        assert ("iac", "reference-sdks") not in ids, ids
        # Entries carry a file:line provenance ref.
        refs = ids[("reference", "reference-pre-built-policy-packs")]
        assert refs and refs[0].startswith("config/_default/menus.yml:"), refs


def test_config_parser_missing_file_returns_empty():
    with tempfile.TemporaryDirectory() as td:
        repo = _make_repo(Path(td), menus_yml=None)
        assert fmv.build_config_menu_identifiers(repo) == {}


def test_parent_defined_only_in_menus_yml_resolves():
    with tempfile.TemporaryDirectory() as td:
        repo = _make_repo(Path(td))
        rel = _write_page(
            repo,
            "content/docs/reference/pre-built-policy-packs/hitrust/azure.md",
            "title: Azure\n"
            "menu:\n"
            "  reference:\n"
            "    identifier: hitrust-azure\n"
            "    parent: reference-pre-built-policy-packs",
        )
        identifier_map, _, _ = fmv.build_global_maps(repo)
        fm = fmv.read_frontmatter(repo / rel)
        results = fmv.check_menu_parents(rel, fm, identifier_map)
        assert len(results) == 1, results
        assert results[0]["parent_exists_in_menu"] is True, results


def test_wrong_named_menu_still_flagged():
    # The canonical true positive: parent exists, but only in a different menu.
    with tempfile.TemporaryDirectory() as td:
        repo = _make_repo(Path(td))
        rel = _write_page(
            repo,
            "content/docs/iac/page.md",
            "title: Page\n"
            "menu:\n"
            "  iac:\n"
            "    parent: reference-sdks",
        )
        identifier_map, _, _ = fmv.build_global_maps(repo)
        fm = fmv.read_frontmatter(repo / rel)
        results = fmv.check_menu_parents(rel, fm, identifier_map)
        assert results[0]["parent_exists_in_menu"] is False, results
        assert "reference" in results[0]["found_in_other_menus"], results


def test_nonexistent_parent_still_flagged():
    with tempfile.TemporaryDirectory() as td:
        repo = _make_repo(Path(td))
        rel = _write_page(
            repo,
            "content/docs/iac/page.md",
            "title: Page\n"
            "menu:\n"
            "  iac:\n"
            "    parent: no-such-identifier",
        )
        identifier_map, _, _ = fmv.build_global_maps(repo)
        fm = fmv.read_frontmatter(repo / rel)
        results = fmv.check_menu_parents(rel, fm, identifier_map)
        assert results[0]["parent_exists_in_menu"] is False, results
        assert results[0]["found_in_other_menus"] == [], results


def test_frontmatter_and_config_identifiers_coexist():
    # A parent declared in another page's frontmatter still resolves, and the
    # map merges both sources for the same (menu, identifier) key.
    with tempfile.TemporaryDirectory() as td:
        repo = _make_repo(Path(td))
        _write_page(
            repo,
            "content/docs/iac/section/_index.md",
            "title: Section\n"
            "menu:\n"
            "  iac:\n"
            "    identifier: iac-section",
        )
        rel = _write_page(
            repo,
            "content/docs/iac/section/child.md",
            "title: Child\n"
            "menu:\n"
            "  iac:\n"
            "    parent: iac-section",
        )
        identifier_map, _, _ = fmv.build_global_maps(repo)
        fm = fmv.read_frontmatter(repo / rel)
        results = fmv.check_menu_parents(rel, fm, identifier_map)
        assert results[0]["parent_exists_in_menu"] is True, results


TESTS = [
    test_config_parser_extracts_identifiers_per_menu,
    test_config_parser_missing_file_returns_empty,
    test_parent_defined_only_in_menus_yml_resolves,
    test_wrong_named_menu_still_flagged,
    test_nonexistent_parent_still_flagged,
    test_frontmatter_and_config_identifiers_coexist,
]


def main() -> int:
    failures: list[tuple[str, str]] = []
    for t in TESTS:
        name = t.__name__
        try:
            t()
            print(f"  ok  {name}")
        except AssertionError as e:
            failures.append((name, str(e) or "assertion failed"))
            print(f"  FAIL {name}: {e}")
        except Exception:
            failures.append((name, traceback.format_exc()))
            print(f"  ERROR {name}:\n{traceback.format_exc()}")
    print()
    if failures:
        print(f"{len(failures)}/{len(TESTS)} tests failed")
        return 1
    print(f"{len(TESTS)}/{len(TESTS)} tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
