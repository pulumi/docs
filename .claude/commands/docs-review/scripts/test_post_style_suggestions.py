"""Tests for post-style-suggestions.py validation and payload building.

Pure-function tests only — no network, no gh. The posting path is exercised
in --dry-run form via main() with --patch-file.
"""

from __future__ import annotations

import importlib.util
import json
import re
import subprocess
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

*Optional polish from pattern-based linting — never blocking, not counted above. Take the ones that read better and ignore the rest. ✏️ marks one you can apply from the Files changed tab — use **Add suggestion to batch** on each, then **Commit suggestions** to take several in a single commit.*

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
    assert sum(l.count("✏️") for l in out.splitlines()
               if l.startswith("- **line ")) == 1
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
    assert sum(l.count("✏️") for l in once.splitlines()
               if l.startswith("- **line ")) == 1


def test_annotate_noop_on_empty_or_missing(tmp_path):
    assert pss.annotate_draft(tmp_path / "absent.md", [{"file": "x", "line": 1}]) == 0
    d = tmp_path / "draft.md"
    d.write_text(DRAFT)
    assert pss.annotate_draft(d, []) == 0


FILES_URL = "https://github.com/pulumi/docs/pull/7/files"

# The banner keys off the count-table VALUES row, so the fixture needs the
# table above the style block, exactly as compose-review.py renders it.
DRAFT_TABLE = ("""### 🤖 Pre-merge review

| 🚨 Outstanding | ⚠️ Low-confidence | 💡 Pre-existing | ✅ Resolved |
| :---: | :---: | :---: | :---: |
| **2** | **1** | **0** | **0** |

<details>
<summary>Verification trail</summary>
</details>

""" + DRAFT).replace(pss._caption_text(""), pss._caption_text(FILES_URL))


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
    # ...and the caption's ✏️ legend goes with them: no marks, no legend.
    assert d.read_text() == DRAFT_TABLE.replace(
        pss._caption_text(FILES_URL), pss._caption_text(FILES_URL, legend=False))


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
    assert stub2.patched[11] == DRAFT_TABLE.replace(
        pss._caption_text(FILES_URL), pss._caption_text(FILES_URL, legend=False))


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
    monkeypatch.setattr(pss, "fetch_prior_suggestions", lambda r, p, *_: existing)
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
    monkeypatch.setattr(pss, "fetch_prior_suggestions", lambda r, p, *_: existing)
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


# --- caption reconciliation -------------------------------------------------
#
# The caption is deterministic on the initial lane (compose-review.py writes
# it) but freehand on the re-entrant one, where it was seen paraphrased away.


CAPTION_BODY = """\
| 🚨 Outstanding | ⚠️ Low-confidence | 💡 Pre-existing | ✅ Resolved |
| :---: | :---: | :---: | :---: |
| **0** | **1** | **0** | **0** |

#### Style suggestions

{caption}

##### content/docs/foo.md

- **line 2:** [style] _wordiness_ — 'utilize' is too wordy.
"""


def _canonical(files_url="", legend=True):
    return pss._caption_text(files_url, legend=legend)


def test_caption_normalized_when_model_paraphrased():
    drifted = ("*Optional polish from pattern-based linting — never blocking. "
               "Apply them from the Files changed tab.*")
    body = CAPTION_BODY.format(caption=drifted)
    out, _ = pss.annotate_text(body, [])
    assert _canonical(legend=False) in out
    assert drifted not in out


def test_caption_left_alone_when_already_canonical():
    """An initial-lane body must reconcile to itself, not churn."""
    body = CAPTION_BODY.format(caption=_canonical())
    lines = body.splitlines()
    assert pss._reconcile_caption(lines, "") is False
    assert "\n".join(lines) == body.rstrip("\n")


def test_caption_inserted_when_model_omitted_it():
    body = CAPTION_BODY.format(caption="").replace("\n\n\n", "\n\n")
    lines = body.splitlines()
    assert pss._reconcile_caption(lines, "") is True
    joined = "\n".join(lines)
    assert _canonical() in joined
    # still exactly one caption, and it precedes the file group
    assert joined.index(_canonical()) < joined.index("##### content/docs/foo.md")


def test_caption_not_invented_without_style_block():
    body = "## Review\n\nNo style findings here.\n"
    lines = body.splitlines()
    assert pss._reconcile_caption(lines, "") is False
    assert "\n".join(lines) == body.rstrip("\n")


def test_caption_carries_files_url_when_known():
    body = CAPTION_BODY.format(caption="*stale*")
    path = next(ln.split()[1] for ln in body.splitlines() if ln.startswith("##### "))
    n = int(re.search(r"\*\*line (\d+):", body).group(1))
    out, _ = pss.annotate_text(body, [{"file": path, "line": n}], files_url="https://x/pull/1/files")
    assert "[Files changed](https://x/pull/1/files)" in out


def test_caption_matches_composer():
    """Pin the two copies together — drift here is invisible in production.

    compose-review.py writes this caption on the initial lane; annotate_text
    rewrites it on both. If they disagree, every initial-lane review churns
    its own caption on first refresh.
    """
    spec = importlib.util.spec_from_file_location(
        "compose_review", HERE / "compose-review.py")
    cr = importlib.util.module_from_spec(spec)
    sys.modules["compose_review"] = cr
    spec.loader.exec_module(cr)

    # Both variants: v2's, and v3's, which also names the review's own
    # `[nit]` bullets. Pinning only the first let the second be reverted by
    # the annotator on every published v3 card.
    for nits in (False, True):
        for url in ("", "https://github.com/o/r/pull/7/files"):
            block = cr._render_style_findings(
                [{"file": "content/docs/foo.md", "line": 2,
                  "category": "wordiness", "message": "'utilize' is too wordy."}],
                files_url=url, allow_nits=nits)
            caption = next(ln for ln in block.splitlines()
                           if ln.startswith("*Optional polish"))
            assert caption == pss._caption_text(url, nits), (
                f"caption drift for files_url={url!r}, nits={nits}:\n"
                f"  composer: {caption}\n  annotator: {pss._caption_text(url, nits)}")


def test_annotator_keeps_the_v3_caption():
    """Regression: the annotator runs on the v3 author draft before publish and
    reconciles the caption authoritatively — so it has to reconcile TO the v3
    caption on a v3 card, not back to the v2 one."""
    card = ("<!-- CLAUDE_REVIEW 1/1 -->\n<!-- CLAUDE_REVIEW_AUTHOR -->\n\n"
            "#### Style suggestions\n\n" + pss._caption_text("", nits=True) + "\n\n"
            "##### content/docs/foo.md\n\n- **line 2:** [nit] _typo_ — x.\n")
    out, _ = pss.annotate_text(card, [])
    assert pss._caption_text("", nits=True, legend=False) in out
    assert pss._caption_text("", nits=False, legend=False) not in out
    # ...and a v2 body keeps the v2 caption.
    v2 = card.replace("<!-- CLAUDE_REVIEW_AUTHOR -->\n", "")
    out2, _ = pss.annotate_text(v2, [])
    assert pss._caption_text("", nits=False, legend=False) in out2


def test_key_ignores_note_but_not_replacement():
    """The note churns every run; the replacement is the real identity."""
    a = pss.comment_body(dict(entry(), new_line="You can use the CLI.",
                              note="'utilize' means 'use'"))
    b = pss.comment_body(dict(entry(), new_line="You can use the CLI.",
                              note="utilize -> use"))
    c = pss.comment_body(dict(entry(), new_line="You may use the CLI.",
                              note="utilize -> use"))
    k = pss.suggestion_key
    assert k("f.md", 2, a) == k("f.md", 2, b)
    assert k("f.md", 2, a) != k("f.md", 2, c)


def test_unchanged_set_skips_repost_despite_reworded_note(repo, tmp_path, monkeypatch):
    """The production case the body-keyed version could never hit.

    Regression: fork #232 re-posted on all three runs because the editorial
    pass reworded its note each time, so `have == wanted` never held.
    """
    (tmp_path / "sugg.json").write_text(json.dumps([entry(note="utilize -> use")]))
    (tmp_path / "pr.patch").write_text(PATCH)
    existing = [{"id": 1, "path": "content/docs/foo.md", "line": 2,
                 "body": pss.comment_body(dict(entry(), new_line="You can use the CLI to deploy.",
                                               note="'utilize' means 'use'"))}]
    calls = []
    monkeypatch.setattr(pss, "fetch_prior_suggestions", lambda r, p, *_: existing)
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


def test_changed_replacement_still_reposts(repo, tmp_path, monkeypatch):
    (tmp_path / "sugg.json").write_text(json.dumps([entry()]))
    (tmp_path / "pr.patch").write_text(PATCH)
    existing = [{"id": 1, "path": "content/docs/foo.md", "line": 2,
                 "body": pss.comment_body(dict(entry(), new_line="Something else entirely."))}]
    deleted, posts = [], []
    monkeypatch.setattr(pss, "fetch_prior_suggestions", lambda r, p, *_: existing)
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


# --- absent/unreadable sidecar is UNKNOWN, not "none" ------------------------
#
# Regression: fork #233 refresh 2. The model wrote no sidecar at all, the
# script read that as an authoritative empty set, and deleted three live
# buttons out from under the author.


def _prior(n=3):
    return [{"id": 100 + i, "path": "content/docs/foo.md", "line": 2 + i,
             "body": pss.comment_body(dict(entry(line=2 + i),
                                           new_line=f"line {2 + i} rewritten"))}
            for i in range(n)]


def _run(tmp_path, repo, monkeypatch, sidecar, prior, extra_argv=()):
    calls = []
    monkeypatch.setattr(pss, "fetch_prior_suggestions", lambda r, p, *_: prior)
    monkeypatch.setattr(pss, "delete_comments",
                        lambda r, ids: calls.append(("delete", list(ids))))
    monkeypatch.setattr(pss, "gh_api", lambda *a, **k: calls.append(("api", a)) or
                        SimpleNamespace(returncode=1, stdout="", stderr=""))
    infile = tmp_path / "sugg.json"
    if sidecar is not None:
        infile.write_text(sidecar)
    (tmp_path / "pr.patch").write_text(PATCH)
    monkeypatch.setattr(sys, "argv", [
        "post-style-suggestions.py", "--pr", "1", "--in", str(infile),
        "--patch-file", str(tmp_path / "pr.patch"), "--repo-root", str(repo),
        "--vale-findings", str(tmp_path / "absent.json"), *extra_argv])
    assert pss.main() == 0
    return calls


def test_absent_sidecar_leaves_existing_suggestions_alone(tmp_path, repo, monkeypatch):
    calls = _run(tmp_path, repo, monkeypatch, sidecar=None, prior=_prior())
    assert calls == [], f"expected no GitHub writes, got {calls}"


def test_explicit_empty_array_still_deletes(tmp_path, repo, monkeypatch):
    """`[]` is authoritative: the author fixed everything, clear the buttons."""
    calls = _run(tmp_path, repo, monkeypatch, sidecar="[]", prior=_prior())
    assert calls == [("delete", [100, 101, 102])]


def test_unreadable_sidecar_leaves_existing_suggestions_alone(tmp_path, repo, monkeypatch):
    calls = _run(tmp_path, repo, monkeypatch, sidecar="{not json", prior=_prior())
    assert calls == []


def test_non_array_sidecar_leaves_existing_suggestions_alone(tmp_path, repo, monkeypatch):
    calls = _run(tmp_path, repo, monkeypatch, sidecar='{"file": "x"}', prior=_prior())
    assert calls == []


def test_absent_sidecar_marks_from_what_is_actually_posted(tmp_path, repo, monkeypatch):
    """Unknown must not mean unmarked — the marks track live buttons."""
    d = tmp_path / "draft.md"
    d.write_text(DRAFT)
    live = [{"id": 1, "path": "content/docs/foo.md", "line": 2,
             "body": pss.comment_body(dict(entry(), new_line="You can use the CLI to deploy."))}]
    _run(tmp_path, repo, monkeypatch, sidecar=None, prior=live,
         extra_argv=("--annotate-draft", str(d)))
    out = d.read_text()
    assert "- **line 2:** [style] _wordiness_ — 'utilize' is too wordy. ✏️" in out
    assert "'usually' is a weasel word!\n" in out      # no live button, no mark


def test_live_posted_drops_outdated_comments(monkeypatch):
    """An outdated comment reports line: null and cannot be marked."""
    monkeypatch.setattr(pss, "fetch_prior_suggestions", lambda r, p, *_: [
        {"id": 1, "path": "a.md", "line": 5, "body": "x"},
        {"id": 2, "path": "a.md", "line": None, "body": "x"},
    ])
    assert pss.live_posted("o/r", "1") == [{"file": "a.md", "line": 5}]


def test_live_posted_returns_none_when_listing_fails():
    """None means "we could not look", which is not "there is nothing"."""
    saved = pss.fetch_prior_suggestions
    try:
        pss.fetch_prior_suggestions = lambda r, p: None
        assert pss.live_posted("o/r", "1") is None
        pss.fetch_prior_suggestions = lambda r, p: []
        assert pss.live_posted("o/r", "1") == []
    finally:
        pss.fetch_prior_suggestions = saved


def test_absent_sidecar_with_failed_listing_touches_nothing(tmp_path, repo, monkeypatch):
    """Unknown sidecar + unknown comment list must not strip live marks.

    Annotating from a wrongly-empty set would zero the banner and strip every
    ✏️ while the real comments stayed live — nothing is deleted on this path.
    """
    d = tmp_path / "draft.md"
    before = DRAFT.replace(
        "- **line 2:** [style] _wordiness_ — 'utilize' is too wordy.",
        "- **line 2:** [style] _wordiness_ — 'utilize' is too wordy. ✏️")
    d.write_text(before)
    calls = _run(tmp_path, repo, monkeypatch, sidecar=None, prior=None,
                 extra_argv=("--annotate-draft", str(d)))
    assert calls == []
    assert d.read_text() == before, "draft must be left exactly as found"


def test_caption_replaced_when_model_wrapped_it_in_bold(tmp_path):
    """A column-0 **bold** line is the one shape the render contract forbids.

    Shape-sniffing for single asterisks missed it and inserted a second
    caption above it, leaving the forbidden line in place — where
    extract_bucket_bullets counts it as a bucket finding.
    """
    bold = "**Optional polish from pattern-based linting. Apply what reads better.**"
    body = CAPTION_BODY.format(caption=bold)
    out, _ = pss.annotate_text(body, [])
    assert bold not in out
    assert out.count("Optional polish") == 1
    assert _canonical(legend=False) in out


def test_caption_replaced_when_model_wrote_plain_prose(tmp_path):
    body = CAPTION_BODY.format(caption="Some optional polish suggestions follow.")
    out, _ = pss.annotate_text(body, [])
    assert "Some optional polish suggestions follow." not in out
    assert out.count("Optional polish") == 1


def test_caption_legend_only_when_a_mark_is_on_the_page():
    """A legend for ✏️ marks that aren't there sends the reader to the Files
    tab for nothing — and with REVIEW_STYLE_INLINE off, none ever are."""
    body = CAPTION_BODY.format(caption=_canonical())
    bare, marked = pss.annotate_text(body, [])
    assert marked == 0 and "✏️" not in bare and _canonical(legend=False) in bare
    lines = bare.splitlines()
    path = next(ln.split()[1] for ln in lines if ln.startswith("##### "))
    n = int(re.search(r"\*\*line (\d+):", bare).group(1))
    with_mark, marked = pss.annotate_text(bare, [{"file": path, "line": n}])
    assert marked == 1 and _canonical() in with_mark


# ---- blocking-fix mode ------------------------------------------------------

FIX_SRC = [
    "# Title",
    "Pulumi Service stores your state.",               # L2: backtick quote, phrase fence
    "The CLI ships 400 providers and 90 languages.",   # L3: two findings, one line
    "social:",
    "    bluesky: Read the Pulumi Service guide.",     # L5: indented YAML, bare labels
    "It runs everywhere.",                             # L6: multi-line fence (skip)
    "Nothing to see.",                                 # L7: quote not on the line (skip)
    "A question line.",                                # L8: ❓ row (never converted)
]


def _fix_patch() -> str:
    body = "".join(f"+{ln}\n" for ln in FIX_SRC)
    return ("diff --git a/content/docs/fix.md b/content/docs/fix.md\nnew file mode 100644\n"
            "--- /dev/null\n+++ b/content/docs/fix.md\n"
            f"@@ -0,0 +1,{len(FIX_SRC)} @@\n{body}")


def _row(fid: str, ref: str, text: str = '*"claim"* — verdict: contradicted') -> str:
    return f"| **{fid}** | `content/docs/fix.md` {ref} | {text} |"


def _block(fid: str, quote: str, why: str, fence: list[str], bullets: bool = True) -> list[str]:
    d = "- " if bullets else ""
    return [f"#### {fid} · Do this", "", f"{d}**Line (verbatim):** {quote}", f"{d}**Why:** {why}",
            f"{d}**Fix:** Replace it:", "", "```text", *fence, "```", ""]


FIX_CARD = "\n".join([
    "<!-- CLAUDE_REVIEW_AUTHOR -->", "## Author action guide v1 — 6 items block merge", "",
    "### 🚨 Fix or disagree", "", "| ID | Where | Finding |", "|---|---|---|",
    _row("F1", "L2"), _row("F2", "L3"), _row("F3", "L3"), _row("F4", "L5"),
    _row("F5", "L6"), _row("F6", "L7"), "",
    *_block("F1", "`Pulumi Service`", "The product is Pulumi Cloud now.", ["Pulumi Cloud"]),
    *_block("F2", '"400 providers"', "The registry lists 300.", ["300 providers"]),
    *_block("F3", '"90 languages"', "It's six languages.", ["six languages"]),
    *_block("F4", '"bluesky: Read the Pulumi Service guide."', "Retired name.",
            ["bluesky: Read the Pulumi Cloud guide."], bullets=False),
    *_block("F5", "`It runs everywhere.`", "Overclaims.", ["It runs on", "most platforms."]),
    *_block("F6", "`Something else entirely`", "Paraphrased quote.", ["x"]),
    "### ❓ Questions for you", "", "| ID | Where | Finding |", "|---|---|---|",
    _row("F7", "L8", '*"q"* — verdict: unverifiable'), "",
    *_block("F7", "`A question line.`", "Only you know.", ["An answered line."]),
    "**Full evidence:** [trail](https://x).", "",
])


@pytest.fixture
def fix_repo(tmp_path: Path) -> Path:
    f = tmp_path / "content" / "docs" / "fix.md"
    f.parent.mkdir(parents=True)
    f.write_text("\n".join(FIX_SRC) + "\n")
    return tmp_path


def test_fix_entries_splice_the_fence_into_the_quoted_span(fix_repo):
    entries, skipped = pss.derive_fix_entries(FIX_CARD, fix_repo)
    by_line = {e["line"]: e for e in entries}
    assert by_line[2]["replacement"] == "Pulumi Cloud stores your state."
    assert by_line[2]["ids"] == ["F1"]
    # Two findings on one line merge into ONE suggestion (GitHub replaces
    # whole lines, so two separate ones would each undo the other).
    assert by_line[3]["replacement"] == "The CLI ships 300 providers and six languages."
    assert by_line[3]["ids"] == ["F2", "F3"]
    # Unbulleted labels + double quotes; the indentation outside the quote stays.
    assert by_line[5]["replacement"] == "    bluesky: Read the Pulumi Cloud guide."
    assert set(by_line) == {2, 3, 5}, "multi-line fence, missing quote, and ❓ are all skipped"
    assert any(r.startswith("F5: multi-line") for r in skipped)
    assert any(r.startswith("F6: quote found on 0") for r in skipped)
    assert not any("F7" in r for r in skipped), "❓ rows are never even considered"


def test_fix_collision_keeps_the_first_and_skips_the_rest(fix_repo):
    card = FIX_CARD.replace(_row("F3", "L3"), _row("F3", "L3")).replace(
        '**Line (verbatim):** "90 languages"', '**Line (verbatim):** "400 providers"')
    entries, skipped = pss.derive_fix_entries(card, fix_repo)
    line3 = next(e for e in entries if e["line"] == 3)
    assert line3["ids"] == ["F2"] and line3["replacement"] == "The CLI ships 300 providers and 90 languages."
    assert any(r.startswith("F3: collides") for r in skipped)


def test_fix_mode_dry_run_payload(fix_repo, capsys, monkeypatch):
    (fix_repo / "card.md").write_text(FIX_CARD)
    (fix_repo / "pr.patch").write_text(_fix_patch())
    monkeypatch.setattr(sys, "argv", [
        "post-style-suggestions.py", "--pr", "7", "--repo", "o/r", "--repo-root", str(fix_repo),
        "--fixes-from-author-card", str(fix_repo / "card.md"),
        "--patch-file", str(fix_repo / "pr.patch"), "--dry-run"])
    assert pss.main() == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["body"] == pss.FIX_REVIEW_BODY
    bodies = [c["body"] for c in payload["comments"]]
    assert len(bodies) == 3 and all(b.startswith(pss.FIX_MARKER + "\n") for b in bodies)
    assert "**F2**, **F3** block merge — The registry lists 300. It's six languages." in bodies[1]
    assert "```suggestion\nThe CLI ships 300 providers and six languages.\n```" in bodies[1]
    assert pss.MARKER not in "".join(bodies), "fix comments never carry the style marker"


def test_fix_mode_removes_resolved_fixes_without_a_new_review(fix_repo, monkeypatch):
    """A fix landed: its suggestion goes, the survivors stay live, and no new
    (undeletable) review event is created."""
    entries, _ = pss.derive_fix_entries(FIX_CARD, fix_repo)
    valid, _ = pss.validate_entries(entries, pss._vff.added_lines_per_file(_fix_patch()), fix_repo)
    posted = [{"id": 100 + i, "path": e["file"], "line": e["line"], "body": pss.comment_body(e)}
              for i, e in enumerate(valid)]
    calls: list[list[str]] = []
    monkeypatch.setattr(pss, "fetch_prior_suggestions", lambda r, p, *_: posted)
    monkeypatch.setattr(pss, "gh_api", lambda args, input_json=None: calls.append(args) or
                        subprocess.CompletedProcess(args, 0, "", ""))
    live = pss.sync_posted("o/r", "7", valid[1:], pss.FIX_MARKER, pss.FIX_REVIEW_BODY)
    assert live == valid[1:]
    assert calls == [["-X", "DELETE", "repos/o/r/pulls/comments/100"]]


def test_fix_mode_skips_findings_the_author_already_answered(fix_repo):
    rs = pss.sys.modules.get("pss_review_state")
    if rs is None:
        pss._dispositioned_ids("")
        rs = pss.sys.modules["pss_review_state"]
    state = rs.set_disposition(dict(rs.empty_state(), high_water=7), "F1", "accepted",
                               actor="alice", note="shipping as-is")
    entries, skipped = pss.derive_fix_entries(FIX_CARD + rs.serialize_block(state) + "\n", fix_repo)
    assert 2 not in {e["line"] for e in entries}
    assert "F1: already answered on the card" in skipped


def test_fix_mode_posts_nothing_over_a_corrupt_state_block(fix_repo):
    entries, skipped = pss.derive_fix_entries(FIX_CARD + "<!-- REVIEW_STATE {not json} -->\n", fix_repo)
    assert entries == [] and skipped == ["REVIEW_STATE block is corrupt; posting no fixes"]
