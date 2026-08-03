"""Tests for post-style-suggestions.py validation and payload building.

Pure-function tests only — no network, no gh. The posting path is exercised
in --dry-run form via main() with --patch-file.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent

_spec = importlib.util.spec_from_file_location(
    "post_style_suggestions", HERE / "post-style-suggestions.py")
pss = importlib.util.module_from_spec(_spec)
sys.modules["post_style_suggestions"] = pss
_spec.loader.exec_module(pss)


PATCH = """\
diff --git a/content/docs/foo.md b/content/docs/foo.md
index 1111111..2222222 100644
--- a/content/docs/foo.md
+++ b/content/docs/foo.md
@@ -1,2 +1,3 @@
 # Title
+You can utilize the CLI to deploy.
+This is usually the fastest path.
"""


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    f = tmp_path / "content" / "docs" / "foo.md"
    f.parent.mkdir(parents=True)
    f.write_text("# Title\nYou can utilize the CLI to deploy.\nThis is usually the fastest path.\n")
    return tmp_path


def added() -> dict[str, set[int]]:
    return pss._vff.added_lines_per_file(PATCH)


def entry(**kw) -> dict:
    base = {"file": "content/docs/foo.md", "line": 2,
            "original": "utilize", "replacement": "use",
            "category": "wordiness", "note": "shorter, same meaning"}
    base.update(kw)
    return base


def test_valid_entry_produces_full_replacement_line(repo):
    valid, dropped = pss.validate_entries([entry()], added(), repo)
    assert not dropped
    assert len(valid) == 1
    assert valid[0]["new_line"] == "You can use the CLI to deploy."


def test_original_not_on_line_dropped(repo):
    valid, dropped = pss.validate_entries(
        [entry(original="leverage")], added(), repo)
    assert not valid
    assert "not found on that line" in dropped[0]


def test_non_added_line_dropped(repo):
    # Line 1 is context (" # Title"), not added by the PR.
    valid, dropped = pss.validate_entries(
        [entry(line=1, original="Title", replacement="T")], added(), repo)
    assert not valid
    assert "not a PR-added line" in dropped[0]


def test_noop_and_missing_fields_dropped(repo):
    valid, dropped = pss.validate_entries(
        [entry(replacement="utilize"), {"file": "content/docs/foo.md"}],
        added(), repo)
    assert not valid
    assert len(dropped) == 2


def test_duplicate_anchor_dropped(repo):
    valid, dropped = pss.validate_entries(
        [entry(), entry(original="CLI", replacement="command line")],
        added(), repo)
    assert len(valid) == 1
    assert "duplicate anchor" in dropped[0]


def test_cap_applies(repo):
    f = repo / "content" / "docs" / "foo.md"
    lines = ["# Title"] + [f"filler utilize {i}" for i in range(15)]
    f.write_text("\n".join(lines) + "\n")
    added_lines = {"content/docs/foo.md": set(range(2, 17))}
    entries = [entry(line=n) for n in range(2, 17)]
    valid, dropped = pss.validate_entries(entries, added_lines, repo)
    assert len(valid) == pss.MAX_SUGGESTIONS
    assert any("cap" in d for d in dropped)


def test_payload_shape(repo):
    valid, _ = pss.validate_entries([entry()], added(), repo)
    payload = pss.build_review_payload(valid)
    assert payload["event"] == "COMMENT"
    assert payload["body"].startswith(pss.MARKER)
    c = payload["comments"][0]
    assert c["path"] == "content/docs/foo.md"
    assert c["line"] == 2
    assert c["side"] == "RIGHT"
    assert c["body"].startswith(pss.MARKER)
    assert "```suggestion\nYou can use the CLI to deploy.\n```" in c["body"]


def test_dry_run_end_to_end(repo, tmp_path, capsys, monkeypatch):
    (tmp_path / "sugg.json").write_text(json.dumps([entry()]))
    (tmp_path / "pr.patch").write_text(PATCH)
    monkeypatch.setattr(sys, "argv", [
        "post-style-suggestions.py", "--pr", "1",
        "--in", str(tmp_path / "sugg.json"),
        "--patch-file", str(tmp_path / "pr.patch"),
        "--repo-root", str(repo), "--dry-run",
    ])
    assert pss.main() == 0
    payload = json.loads(capsys.readouterr().out)
    assert len(payload["comments"]) == 1


def test_suggestion_on_blocker_line_dropped(repo):
    """A whole-line suggestion must not re-commit blocking text.

    Regression: fork PR #227 posted a 'Simply' suggestion on line 797, whose
    replacement line still contained the blocker terms 'Pulumi Service' and
    'click'.
    """
    blocked = pss.blocker_lines([
        {"file": "content/docs/foo.md", "line": 2, "blocker": True},
        {"file": "content/docs/foo.md", "line": 3, "blocker": False},
    ])
    valid, dropped = pss.validate_entries([entry()], added(), repo, blocked)
    assert not valid
    assert "carries a blocker finding" in dropped[0]


def test_non_blocker_finding_on_line_does_not_block(repo):
    blocked = pss.blocker_lines([
        {"file": "content/docs/foo.md", "line": 2, "blocker": False}])
    valid, _ = pss.validate_entries([entry()], added(), repo, blocked)
    assert len(valid) == 1


def test_blocker_lines_tolerates_junk():
    assert pss.blocker_lines(None) == set()
    assert pss.blocker_lines("nope") == set()
    assert pss.blocker_lines([{"no_file": 1, "blocker": True}]) == {("", 0)}


def test_repo_defaults_to_github_repository_env(monkeypatch):
    """The repo must come from the environment, not a hardcoded upstream name.

    Regression: the 2026-08-03 fork run POSTed to `pulumi/docs` with the
    fork's GITHUB_TOKEN and 403'd ("Resource not accessible by integration"),
    so no suggestion ever reached the author.
    """
    import importlib
    monkeypatch.setenv("GITHUB_REPOSITORY", "CamSoper/pulumi.docs")
    spec = importlib.util.spec_from_file_location(
        "pss_reload", HERE / "post-style-suggestions.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["pss_reload"] = mod
    spec.loader.exec_module(mod)
    assert mod.DEFAULT_REPO == "CamSoper/pulumi.docs"


def test_missing_file_is_noop(tmp_path, monkeypatch):
    monkeypatch.setattr(sys, "argv", [
        "post-style-suggestions.py", "--pr", "1",
        "--in", str(tmp_path / "absent.json"), "--dry-run",
    ])
    assert pss.main() == 0


DRAFT = """### ⚠️ Low-confidence

*Review each and resolve as appropriate — these don't block the PR.*

#### Style suggestions

*Optional polish from pattern-based linting.*

##### content/docs/foo.md

- **line 2:** [style] _wordiness_ — 'utilize' is too wordy.
- **line 3:** [style] _weasel word_ — 'usually' is a weasel word!

##### content/docs/bar.md

- **line 2:** [style] _filler_ — 'so' is filler.

### 📋 Triaged verifier findings
"""


def test_annotate_marks_only_posted_bullets(tmp_path):
    d = tmp_path / "draft.md"
    d.write_text(DRAFT)
    n = pss.annotate_draft(d, [{"file": "content/docs/foo.md", "line": 2}])
    out = d.read_text()
    assert n == 1
    assert "- **line 2:** [style] _wordiness_ — 'utilize' is too wordy. ✏️" in out
    assert "'usually' is a weasel word!\n" in out          # untouched
    assert "- **line 2:** [style] _filler_ — 'so' is filler." in out  # other file untouched


def test_annotate_disambiguates_same_line_across_files(tmp_path):
    d = tmp_path / "draft.md"
    d.write_text(DRAFT)
    pss.annotate_draft(d, [{"file": "content/docs/bar.md", "line": 2}])
    out = d.read_text()
    assert "'so' is filler. ✏️" in out
    assert "'utilize' is too wordy.\n" in out              # foo.md line 2 NOT marked


def test_annotate_is_idempotent(tmp_path):
    d = tmp_path / "draft.md"
    d.write_text(DRAFT)
    posted = [{"file": "content/docs/foo.md", "line": 2}]
    pss.annotate_draft(d, posted)
    second = pss.annotate_draft(d, posted)
    assert second == 0
    assert d.read_text().count("✏️") == 1


def test_annotate_noop_on_empty_or_missing(tmp_path):
    assert pss.annotate_draft(tmp_path / "absent.md", [{"file": "x", "line": 1}]) == 0
    d = tmp_path / "draft.md"
    d.write_text(DRAFT)
    assert pss.annotate_draft(d, []) == 0
