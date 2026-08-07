"""Tests for post-style-suggestions.py validation and payload building.

Pure-function tests only — no network, no gh. The posting path is exercised
in --dry-run form via main() with --patch-file.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

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


def test_annotate_overwrites_model_authored_marks(tmp_path):
    """The workflow owns the mark; a mark the model wrote is corrected, not kept.

    Regression: fork PR #229's editorial pass wrote four mid-line ✏️ of its
    own. They happened to match what posted, but a model-authored mark on an
    entry that was later dropped would promise a button that doesn't exist.
    """
    d = tmp_path / "draft.md"
    # model marked BOTH foo.md bullets mid-line; only line 2 actually posted
    d.write_text(DRAFT
                 .replace("- **line 2:** [style] _wordiness_", "- **line 2:** ✏️ [style] _wordiness_")
                 .replace("- **line 3:** [style] _weasel word_", "- **line 3:** ✏️ [style] _weasel word_"))
    n = pss.annotate_draft(d, [{"file": "content/docs/foo.md", "line": 2}])
    out = d.read_text()
    assert n == 1
    assert out.count("✏️") == 1
    # the surviving mark is the workflow's, appended at end of line
    assert "- **line 2:** [style] _wordiness_ — 'utilize' is too wordy. ✏️" in out
    # the unposted one lost its mark entirely
    assert "- **line 3:** [style] _weasel word_ — 'usually' is a weasel word!" in out


def test_annotate_is_idempotent(tmp_path):
    """Re-running must not change the body. The return is marks PRESENT, not
    marks newly added, so it stays 1 on the second pass."""
    d = tmp_path / "draft.md"
    d.write_text(DRAFT)
    posted = [{"file": "content/docs/foo.md", "line": 2}]
    assert pss.annotate_draft(d, posted) == 1
    once = d.read_text()
    assert pss.annotate_draft(d, posted) == 1
    assert d.read_text() == once
    assert once.count("✏️") == 1


def test_annotate_noop_on_empty_or_missing(tmp_path):
    assert pss.annotate_draft(tmp_path / "absent.md", [{"file": "x", "line": 1}]) == 0
    d = tmp_path / "draft.md"
    d.write_text(DRAFT)
    assert pss.annotate_draft(d, []) == 0


FILES_URL = "https://github.com/pulumi/docs/pull/7/files"

# The banner keys off the count-table VALUES row, so the fixture needs the
# table above the style block, exactly as compose-review.py renders it.
DRAFT_TABLE = """### 🤖 Pre-merge review

| 🚨 Outstanding | ⚠️ Low-confidence | 💡 Pre-existing | ✅ Resolved |
| :---: | :---: | :---: | :---: |
| **2** | **1** | **0** | **0** |

<details>
<summary>Verification trail</summary>
</details>

""" + DRAFT


def test_banner_announces_posted_count_under_the_table(tmp_path):
    d = tmp_path / "draft.md"
    d.write_text(DRAFT_TABLE)
    pss.annotate_draft(d, [{"file": "content/docs/foo.md", "line": 2},
                           {"file": "content/docs/bar.md", "line": 2}], FILES_URL)
    lines = d.read_text().splitlines()
    i = lines.index("| **2** | **1** | **0** | **0** |")
    assert lines[i + 1] == ""
    assert lines[i + 2] == (
        "✏️ **2 one-click style suggestions** are posted inline — apply them from the "
        f"[Files changed]({FILES_URL}) tab, individually or with "
        "**Add suggestion to batch**.")
    assert lines[i + 3] == ""          # the table's original trailing blank survives


def test_banner_singular(tmp_path):
    d = tmp_path / "draft.md"
    d.write_text(DRAFT_TABLE)
    pss.annotate_draft(d, [{"file": "content/docs/foo.md", "line": 2}], FILES_URL)
    assert ("✏️ **1 one-click style suggestion** is posted inline — apply it from the "
            f"[Files changed]({FILES_URL}) tab.") in d.read_text()


def test_banner_is_idempotent(tmp_path):
    """Re-running must not stack banners or grow the gap under the table."""
    d = tmp_path / "draft.md"
    d.write_text(DRAFT_TABLE)
    posted = [{"file": "content/docs/foo.md", "line": 2}]
    pss.annotate_draft(d, posted, FILES_URL)
    once = d.read_text()
    pss.annotate_draft(d, posted, FILES_URL)
    assert d.read_text() == once
    assert once.count("✏️ **") == 1


def test_banner_removed_when_nothing_posts(tmp_path):
    """The re-entrant case: last run's banner must not outlive its buttons.

    A refresh that converts nothing deletes the prior suggestion comments, so
    a surviving 'N suggestions are posted inline' would point at nothing.
    """
    d = tmp_path / "draft.md"
    d.write_text(DRAFT_TABLE)
    pss.annotate_draft(d, [{"file": "content/docs/foo.md", "line": 2}], FILES_URL)
    assert pss.annotate_draft(d, [], FILES_URL) == 0
    assert d.read_text() == DRAFT_TABLE


def test_banner_skipped_without_a_count_table(tmp_path):
    """Degrade quietly: marks still land, no banner, no crash."""
    d = tmp_path / "draft.md"
    d.write_text(DRAFT)
    assert pss.annotate_draft(d, [{"file": "content/docs/foo.md", "line": 2}],
                              FILES_URL) == 1
    assert "one-click style suggestion" not in d.read_text()


class _GhStub:
    """Minimal `gh api` double for the annotate-pinned round trip."""

    def __init__(self, parts):
        self.parts = parts               # [(id, body), ...]
        self.patched = {}

    def __call__(self, args, input_json=None):
        joined = " ".join(args)
        out = ""
        rc = 0
        if "/comments" in joined and "--jq" in joined:
            out = "\n".join(json.dumps({"id": i, "body": b}) for i, b in self.parts)
        elif "PATCH" in joined:
            cid = int(joined.split("issues/comments/")[1].split()[0])
            self.patched[cid] = input_json["body"]
        return SimpleNamespace(returncode=rc, stdout=out, stderr="")


def test_annotate_pinned_patches_only_changed_parts(monkeypatch):
    """Split reviews: the banner lives in part 1, the style bullets in part 2.

    Each part is PATCHed independently — no fetch/concatenate/re-upsert, which
    would re-run the splitter over its own continuation-<details> artifacts.
    """
    head, tail = DRAFT_TABLE.split("#### Style suggestions")
    stub = _GhStub([(11, head), (12, "#### Style suggestions" + tail)])
    monkeypatch.setattr(pss, "gh_api", stub)
    n = pss.annotate_pinned("o/r", "7", [{"file": "content/docs/foo.md", "line": 2}],
                            FILES_URL)
    assert n == 1
    assert "one-click style suggestion" in stub.patched[11]      # banner → part 1
    assert "'utilize' is too wordy. ✏️" in stub.patched[12]      # mark → part 2
    assert "one-click style suggestion" not in stub.patched[12]


def test_annotate_pinned_skips_unchanged_part(monkeypatch):
    """An already-correct part must not be PATCHed — every PATCH re-notifies."""
    stub = _GhStub([(11, DRAFT_TABLE)])
    monkeypatch.setattr(pss, "gh_api", stub)
    posted = [{"file": "content/docs/foo.md", "line": 2}]
    pss.annotate_pinned("o/r", "7", posted, FILES_URL)
    settled = stub.patched[11]
    stub2 = _GhStub([(11, settled)])
    monkeypatch.setattr(pss, "gh_api", stub2)
    assert pss.annotate_pinned("o/r", "7", posted, FILES_URL) == 1
    assert stub2.patched == {}


def test_annotate_pinned_tolerates_crlf(monkeypatch):
    """GitHub returns bodies CRLF-normalized; that alone isn't a change."""
    stub = _GhStub([(11, DRAFT_TABLE)])
    monkeypatch.setattr(pss, "gh_api", stub)
    posted = [{"file": "content/docs/foo.md", "line": 2}]
    pss.annotate_pinned("o/r", "7", posted, FILES_URL)
    crlf = stub.patched[11].replace("\n", "\r\n")
    stub2 = _GhStub([(11, crlf)])
    monkeypatch.setattr(pss, "gh_api", stub2)
    pss.annotate_pinned("o/r", "7", posted, FILES_URL)
    assert stub2.patched == {}


def test_annotate_pinned_strips_when_nothing_posted(monkeypatch):
    """A refresh that converts nothing must clear last run's marks and banner."""
    stub = _GhStub([(11, DRAFT_TABLE)])
    monkeypatch.setattr(pss, "gh_api", stub)
    pss.annotate_pinned("o/r", "7", [{"file": "content/docs/foo.md", "line": 2}], FILES_URL)
    stub2 = _GhStub([(11, stub.patched[11])])
    monkeypatch.setattr(pss, "gh_api", stub2)
    assert pss.annotate_pinned("o/r", "7", [], FILES_URL) == 0
    assert stub2.patched[11] == DRAFT_TABLE


def test_post_individually_returns_only_landed(monkeypatch):
    """Batch POST is atomic (422 kills all), so the fallback must report which
    individual comments actually landed — that set drives the ✏️ marks."""
    calls = []

    class R:
        def __init__(self, rc): self.returncode = rc; self.stderr = "422 Line could not be resolved"

    def fake(args, input_json=None):
        calls.append(args)
        # reject the second entry only
        return R(1) if "line=3" in " ".join(args) else R(0)

    monkeypatch.setattr(pss, "gh_api", fake)
    entries = [
        {"file": "content/docs/foo.md", "line": 2, "new_line": "a", "category": "wordiness"},
        {"file": "content/docs/foo.md", "line": 3, "new_line": "b", "category": "weasel word"},
    ]
    landed = pss.post_individually("o/r", "1", "deadbeef", entries)
    assert [e["line"] for e in landed] == [2]
    assert len(calls) == 2


def test_suggestion_key_normalizes_crlf_and_outdated_lines():
    """Body newline style must not force a repost; an outdated anchor must."""
    assert (pss.suggestion_key("a.md", 2, "x\r\ny")
            == pss.suggestion_key("a.md", 2, "x\ny"))
    # GitHub reports line: null once a comment goes outdated -- never equal to
    # a live anchor, so a moved suggestion is correctly seen as changed.
    assert pss.suggestion_key("a.md", None, "x") != pss.suggestion_key("a.md", 2, "x")


def test_unchanged_set_skips_repost(repo, tmp_path, monkeypatch):
    """A refresh that would re-post the identical set must not touch GitHub.

    Reposting deletes the live buttons, re-notifies every subscriber, and
    strands another undeletable review event in the timeline -- all to arrive
    at the state we were already in.
    """
    (tmp_path / "sugg.json").write_text(json.dumps([entry()]))
    (tmp_path / "pr.patch").write_text(PATCH)
    existing = [{"id": 1, "path": "content/docs/foo.md", "line": 2,
                 "body": pss.comment_body(dict(entry(), new_line="You can use the CLI to deploy."))}]
    calls = []
    monkeypatch.setattr(pss, "fetch_prior_suggestions", lambda r, p: existing)
    monkeypatch.setattr(pss, "delete_comments", lambda r, ids: calls.append(("delete", ids)))
    monkeypatch.setattr(pss, "gh_api", lambda *a, **k: calls.append(("api", a)) or SimpleNamespace(
        returncode=1, stdout="", stderr=""))
    monkeypatch.setattr(sys, "argv", [
        "post-style-suggestions.py", "--pr", "1",
        "--in", str(tmp_path / "sugg.json"), "--patch-file", str(tmp_path / "pr.patch"),
        "--repo-root", str(repo), "--vale-findings", str(tmp_path / "absent.json"),
    ])
    assert pss.main() == 0
    assert calls == [], f"expected no GitHub writes, got {calls}"


def test_changed_set_does_repost(repo, tmp_path, monkeypatch):
    existing = [{"id": 1, "path": "content/docs/foo.md", "line": 2, "body": "stale body"}]
    (tmp_path / "sugg.json").write_text(json.dumps([entry()]))
    (tmp_path / "pr.patch").write_text(PATCH)
    deleted, posts = [], []
    monkeypatch.setattr(pss, "fetch_prior_suggestions", lambda r, p: existing)
    monkeypatch.setattr(pss, "delete_comments", lambda r, ids: deleted.extend(ids))
    monkeypatch.setattr(pss, "gh_api", lambda *a, **k: posts.append(a) or SimpleNamespace(
        returncode=0, stdout="", stderr=""))
    monkeypatch.setattr(sys, "argv", [
        "post-style-suggestions.py", "--pr", "1",
        "--in", str(tmp_path / "sugg.json"), "--patch-file", str(tmp_path / "pr.patch"),
        "--repo-root", str(repo), "--vale-findings", str(tmp_path / "absent.json"),
    ])
    assert pss.main() == 0
    assert deleted == [1]
    assert any("reviews" in str(a) for a in posts)


def test_orphaned_bullet_loses_stale_mark(tmp_path):
    """Page 2 of a split review: no `##### <path>` heading to attribute bullets.

    The mark cannot be re-earned there, so it must still be removed -- the
    comments it pointed at were deleted moments earlier.
    """
    page2 = ("<!-- CLAUDE_REVIEW 2/2 -->\n\n"
             "- **line 12:** [style] _wordiness_ — 'utilize' is too wordy. ✏️\n")
    out, marked = pss.annotate_text(page2, posted=[])
    assert marked == 0
    assert "✏️" not in out


def test_annotate_preserves_trailing_newline_state(tmp_path):
    """GitHub bodies have no trailing newline; adding one forces a needless PATCH."""
    body = "##### a.md\n\n- **line 2:** [style] _x_ — y."
    assert pss.annotate_text(body, posted=[])[0] == body
    assert pss.annotate_text(body + "\n", posted=[])[0] == body + "\n"


def test_annotate_preserves_double_space_in_message():
    msg = "##### a.md\n\n- **line 2:** [style] _x_ — 'a.  b' is wordy.\n"
    assert "'a.  b'" in pss.annotate_text(msg, posted=[])[0]
