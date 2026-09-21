#!/usr/bin/env python3
"""Tests for pinned-comment.sh — the v3 role-card surface and its v2 compat.

pinned-comment.sh had no test coverage before the v3 role work (its behavior
was pinned only by the workflows that call it), so these tests establish the
contract the two-comment surface depends on: role upserts publish VERBATIM
(no split, no footer restamp, no marker stamping), malformed cards fail loud
at the publish boundary, the v2 sequence path round-trips a v3 author card
without destroying its role marker or REVIEW_STATE block, and `clear` sweeps
both surfaces without double-deleting the author card (which lives in both
lists via its legacy 1/1 alias).

Mechanism: `gh` is stubbed with a PATH-prepended fake that serves canned
comment lists from a fixture dir, executes the script's `--jq` programs with
the real jq (so the jq the script ships is what gets tested), and logs every
mutating call — no network, ever.
"""

from __future__ import annotations

import json
import os
import stat
import subprocess
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "pinned-comment.sh"

GH_STUB = r'''#!/usr/bin/env python3
import json, os, subprocess, sys

stub_dir = os.environ["GH_STUB_DIR"]
args = sys.argv[1:]
with open(os.path.join(stub_dir, "calls.log"), "a") as f:
    f.write(json.dumps(args) + "\n")


def flag_value(name):
    return args[args.index(name) + 1] if name in args else None


def body_from_field():
    for i, a in enumerate(args):
        if a in ("--field", "-f") and args[i + 1].startswith("body=@"):
            return open(args[i + 1][len("body=@"):]).read()
    return None


if args and args[0] == "api":
    if "graphql" in args:
        # isMinimized probe: never minimized in these tests.
        print("false")
        sys.exit(0)
    method = flag_value("-X") or "GET"
    consumed = set()
    for i, a in enumerate(args):
        if a in ("-X", "--jq", "-f", "--field"):
            consumed.add(i + 1)
    path = next(a for i, a in enumerate(args[1:], start=1)
                if i not in consumed and not a.startswith("-") and "=" not in a)
    comments = json.load(open(os.path.join(stub_dir, "comments.json")))
    if method == "GET":
        jq_prog = flag_value("--jq")
        if path.endswith("/comments"):
            payload = json.dumps(comments)
        else:
            cid = int(path.rsplit("/", 1)[1])
            payload = json.dumps(next(c for c in comments if c["id"] == cid))
        out = subprocess.run(["jq", "-r", jq_prog], input=payload,
                             capture_output=True, text=True)
        sys.stdout.write(out.stdout)
        sys.exit(out.returncode)
    if method == "PATCH":
        cid = path.rsplit("/", 1)[1]
        open(os.path.join(stub_dir, f"patched-{cid}.body"), "w").write(body_from_field())
        sys.exit(0)
    if method == "POST":
        open(os.path.join(stub_dir, "posted.body"), "w").write(body_from_field())
        sys.exit(0)
    if method == "DELETE":
        sys.exit(0)
sys.exit(0)
'''

FOOTER = "<!-- CLAUDE_REVIEW_FOOTER -->\n\n---\n\nfooter text\n"


def author_card(sha: str = "a" * 40, extra: str = "") -> str:
    return (
        "<!-- CLAUDE_REVIEW 1/1 -->\n"
        "<!-- CLAUDE_REVIEW_AUTHOR -->\n"
        f"<!-- CLAUDE_REVIEW_HEAD {sha} -->\n"
        "## Review: author action needed — 1 item blocks merge\n\n"
        "### 🚨 Fix or disagree\n\n"
        "| | ID | Where | Finding |\n|---|---|---|---|\n| ⬜ | **F1** | `x.md` L10 | bad claim |\n\n"
        f"{extra}"
        '<!-- REVIEW_STATE {"findings":{},"high_water":1,"schema":1} -->\n\n'
        + FOOTER
    )


def brief_card() -> str:
    return (
        "<!-- CLAUDE_REVIEW_BRIEF -->\n"
        "## Reviewer's guide — Last updated now (head aaaabbbb)\n\n"
        "### ⚠️ Check these before approving\n\n- **F2** thing\n\n" + FOOTER
    )


def comment(cid: int, body: str, created: str = "2026-08-31T10:00:00Z") -> dict:
    return {"id": cid, "body": body, "created_at": created, "node_id": f"node{cid}"}


@pytest.fixture()
def env(tmp_path):
    stub_dir = tmp_path / "stub"
    stub_dir.mkdir()
    gh = stub_dir / "gh"
    gh.write_text(GH_STUB)
    gh.chmod(gh.stat().st_mode | stat.S_IEXEC)
    (stub_dir / "calls.log").write_text("")
    (stub_dir / "comments.json").write_text("[]")
    e = dict(os.environ)
    e["PATH"] = f"{stub_dir}:{e['PATH']}"
    e["GH_STUB_DIR"] = str(stub_dir)
    e.pop("GH_REPO", None)
    e["GITHUB_REPOSITORY"] = "pulumi/docs"
    return stub_dir, e


def run(env_pair, *argv, body: str | None = None, cwd=None):
    stub_dir, e = env_pair
    args = ["bash", str(SCRIPT), *argv]
    if body is not None:
        body_file = stub_dir / "input-body.md"
        body_file.write_text(body)
        args += ["--body-file", str(body_file)]
    return subprocess.run(args, env=e, capture_output=True, text=True,
                          cwd=cwd or stub_dir)


def set_comments(stub_dir: Path, comments: list[dict]) -> None:
    (stub_dir / "comments.json").write_text(json.dumps(comments))


# ---- role upsert -------------------------------------------------------------


def test_role_upsert_creates_verbatim(env):
    stub_dir, _ = env
    card = author_card()
    r = run(env, "upsert", "--pr", "7", "--role", "author", body=card)
    assert r.returncode == 0, r.stderr
    assert (stub_dir / "posted.body").read_text() == card, "role upsert must publish verbatim"


def test_role_upsert_patches_existing_in_place(env):
    stub_dir, _ = env
    set_comments(stub_dir, [comment(11, author_card())])
    card = author_card(extra="edited line\n\n")
    r = run(env, "upsert", "--pr", "7", "--role", "author", body=card)
    assert r.returncode == 0, r.stderr
    assert (stub_dir / "patched-11.body").read_text() == card
    assert not (stub_dir / "posted.body").exists()


def test_role_upsert_never_splits_oversized(env):
    card = author_card(extra="x" * 5000 + "\n\n")
    r = run(env, "upsert", "--pr", "7", "--role", "author", "--max-bytes", "4000", body=card)
    assert r.returncode != 0
    assert "never split" in r.stderr


def test_role_upsert_rejects_missing_footer(env):
    card = author_card().replace(FOOTER, "")
    r = run(env, "upsert", "--pr", "7", "--role", "author", body=card)
    assert r.returncode != 0 and "footer" in r.stderr


def test_role_upsert_rejects_author_without_legacy_alias(env):
    card = author_card().replace("<!-- CLAUDE_REVIEW 1/1 -->\n", "")
    r = run(env, "upsert", "--pr", "7", "--role", "author", body=card)
    assert r.returncode != 0 and "1/1" in r.stderr


def test_role_upsert_rejects_brief_with_sequence_marker(env):
    card = "<!-- CLAUDE_REVIEW 1/1 -->\n" + brief_card()
    r = run(env, "upsert", "--pr", "7", "--role", "brief", body=card)
    assert r.returncode != 0 and "must not carry" in r.stderr


def test_role_upsert_rejects_wrong_marker(env):
    r = run(env, "upsert", "--pr", "7", "--role", "brief", body=author_card())
    assert r.returncode != 0 and "CLAUDE_REVIEW_BRIEF" in r.stderr


def test_role_upsert_never_invokes_spine_floor(env):
    stub_dir, _ = env
    set_comments(stub_dir, [comment(11, author_card())])
    r = run(env, "upsert", "--pr", "7", "--role", "author", body=author_card())
    assert r.returncode == 0, r.stderr
    calls = [json.loads(line) for line
             in (stub_dir / "calls.log").read_text().splitlines() if line.strip()]
    # The v2 spine floor fetches every prior body, one comment at a time, to
    # diff the evidence spine out of them. The role path reads exactly one
    # body — the card it is about to replace, for the stale-publish guard —
    # and never walks a sequence. Counting is the assertion: "reads no body at
    # all" stopped being true when the guard landed, but "reads more than the
    # one card it owns" is still the spine floor leaking in.
    body_gets = [c for c in calls
                 if c[:1] == ["api"] and ".body" in c
                 and any("issues/comments/" in a for a in c)]
    assert len(body_gets) == 1, f"role upsert reads one card body, got {body_gets}"


def test_unknown_role_and_wrong_subcommand_rejected(env):
    assert run(env, "upsert", "--pr", "7", "--role", "editor", body=author_card()).returncode != 0
    assert run(env, "prune", "--pr", "7", "--keep", "1", "--role", "author").returncode != 0


# ---- find / clear / prune ----------------------------------------------------


def test_find_role_and_bare_find(env):
    stub_dir, _ = env
    set_comments(stub_dir, [
        comment(30, "unrelated comment"),
        comment(31, author_card(), "2026-08-31T10:00:00Z"),
        comment(32, brief_card(), "2026-08-31T10:00:01Z"),
        comment(33, "> quoted reply\n> <!-- CLAUDE_REVIEW_AUTHOR -->\nnice"),
    ])
    assert run(env, "find", "--pr", "7", "--role", "author").stdout.strip() == "31"
    assert run(env, "find", "--pr", "7", "--role", "brief").stdout.strip() == "32"
    # Bare v2 find sees the author card via its legacy alias — and only it.
    assert run(env, "find", "--pr", "7").stdout.split() == ["31"]


def test_quoted_copy_of_marker_never_matches(env):
    stub_dir, _ = env
    set_comments(stub_dir, [comment(40, "> <!-- CLAUDE_REVIEW_BRIEF -->\nquoting you")])
    assert run(env, "find", "--pr", "7", "--role", "brief").stdout.strip() == ""


def test_clear_sweeps_both_surfaces_once(env):
    stub_dir, _ = env
    set_comments(stub_dir, [
        comment(51, author_card()),
        comment(52, brief_card()),
        comment(53, "<!-- CLAUDE_REVIEW 2/2 -->\nlegacy tail\n"),
    ])
    r = run(env, "clear", "--pr", "7")
    assert r.returncode == 0, r.stderr
    deletes = [json.loads(line) for line in (stub_dir / "calls.log").read_text().splitlines()
               if "DELETE" in line]
    deleted_ids = sorted(c[-1].rsplit("/", 1)[1] for c in deletes)
    assert deleted_ids == ["51", "52", "53"], "each comment deleted exactly once"


def test_prune_protects_author_card_as_index_zero(env):
    stub_dir, _ = env
    set_comments(stub_dir, [
        comment(61, author_card()),
        comment(62, "<!-- CLAUDE_REVIEW 2/2 -->\nstale tail\n"),
    ])
    r = run(env, "prune", "--pr", "7", "--keep", "0")
    assert r.returncode == 0, r.stderr
    log = (stub_dir / "calls.log").read_text()
    assert "comments/62" in log and "sacrosanct" in r.stderr
    deletes = [l for l in log.splitlines() if "DELETE" in l]
    assert len(deletes) == 1, "only the tail deleted; the 1/1 author card is sacrosanct"


# ---- last-reviewed-sha -------------------------------------------------------


def test_last_reviewed_sha_prefers_head_marker(env):
    stub_dir, _ = env
    sha = "deadbeef" * 5
    body = author_card(sha=sha, extra="### 📜 Review history\n\n2026-08-30 — earlier (0123abc)\n\n")
    set_comments(stub_dir, [comment(71, body)])
    assert run(env, "last-reviewed-sha", "--pr", "7").stdout.strip() == sha


def test_last_reviewed_sha_falls_back_to_history(env):
    stub_dir, _ = env
    body = ("<!-- CLAUDE_REVIEW 1/1 -->\n## Pre-merge Review\n\n"
            "### 📜 Review history\n\n2026-08-30 — reviewed (0123abcd)\n\n" + FOOTER)
    set_comments(stub_dir, [comment(72, body)])
    assert run(env, "last-reviewed-sha", "--pr", "7").stdout.strip() == "0123abcd"


# ---- v2 round-trip compat ----------------------------------------------------


def test_v2_upsert_preserves_role_marker_and_review_state(env):
    """A v2 (no --role) upsert over a v3 author card must not destroy the v3
    markers: only the N/M page markers and the footer are strip-and-restamp
    material. This is the transition guarantee for the update lane while it
    still publishes through the v2 path."""
    stub_dir, _ = env
    set_comments(stub_dir, [comment(81, author_card())])
    r = run(env, "upsert", "--pr", "7", body=author_card())
    assert r.returncode == 0, r.stderr
    published = (stub_dir / "patched-81.body").read_text()
    assert published.startswith("<!-- CLAUDE_REVIEW 1/1 -->\n"), "restamped as page 1/1"
    assert published.count("<!-- CLAUDE_REVIEW 1/1 -->") == 1, "no marker accumulation"
    assert "<!-- CLAUDE_REVIEW_AUTHOR -->" in published
    assert '<!-- REVIEW_STATE {"findings":{},"high_water":1,"schema":1} -->' in published
    assert "<!-- CLAUDE_REVIEW_HEAD " in published


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-q"]))


def test_banner_body_set_clear_roundtrip():
    """banner-body: set inserts after the last leading marker, re-set is
    idempotent, clear restores the original byte-for-byte."""
    fixture = (HERE / "testdata" / "v3-fixture-author.md.txt").read_text()

    def run(args, body):
        p = subprocess.run(["bash", str(SCRIPT), "banner-body", *args],
                           input=body, capture_output=True, text=True)
        assert p.returncode == 0, p.stderr
        return p.stdout

    stamped = run(["--set", "4c70141"], fixture)
    lines = stamped.splitlines()
    assert lines[3].startswith("> 🔄 **Re-review in progress** for your push `4c70141`")
    assert lines[4] == "" and lines[5].startswith("## Author action guide")
    assert stamped.count("Re-review in progress") == 1
    restamped = run(["--set", "beefcaf"], stamped)
    assert restamped.count("Re-review in progress") == 1
    assert "beefcaf" in restamped and "4c70141" not in restamped.splitlines()[3]
    assert run(["--clear"], restamped) == fixture
    assert run(["--clear"], fixture) == fixture


# ---- stale-publish guard -----------------------------------------------------
#
# Regression cover for the card race observed twice on pulumi/docs#21785: two
# runs at the SAME head published concurrently, the one that finished writing
# last won regardless of when it composed, and the author card's REVIEW_STATE
# — the Sentinel's G2 input — lost a recorded disposition with no trace.


def stamped_author_card(updated: str, rev: int = 1, state: str = '{"findings":{},"high_water":1,"schema":1}') -> str:
    return (
        "<!-- CLAUDE_REVIEW 1/1 -->\n"
        "<!-- CLAUDE_REVIEW_AUTHOR -->\n"
        f"<!-- CLAUDE_REVIEW_HEAD {'a' * 40} -->\n"
        f"## Author action guide v{rev} — nothing blocks merge\n\n"
        "### 🚨 Fix or disagree\n\n_Nothing to fix._\n\n"
        f"<!-- REVIEW_STATE {state} -->\n\n"
        f"<sub>Review v{rev} · updated {updated} · head commit aaaaaaa</sub>\n\n"
        + FOOTER
    )


def test_stale_card_does_not_overwrite_newer_one(env):
    """The #21785 loss, verbatim: a card carrying `F1: fixed` must survive a
    concurrent run whose card was composed a minute earlier."""
    stub_dir, _ = env
    published = stamped_author_card(
        "2026-09-21T20:49:07Z", rev=2,
        state='{"findings":{"F1":{"disposition":"fixed","sha":"1508820834ad"}},"high_water":1,"schema":1}')
    set_comments(stub_dir, [comment(11, published)])
    stale = stamped_author_card("2026-09-21T20:48:08Z", rev=1)

    r = run(env, "upsert", "--pr", "21785", "--role", "author", body=stale)

    assert r.returncode == 0, r.stderr
    assert not (stub_dir / "patched-11.body").exists(), \
        "a card composed earlier must not overwrite the newer one on the PR"
    assert "not overwriting" in r.stdout + r.stderr


def test_newer_card_still_publishes_over_older(env):
    stub_dir, _ = env
    set_comments(stub_dir, [comment(11, stamped_author_card("2026-09-21T20:48:08Z"))])
    fresh = stamped_author_card("2026-09-21T20:49:07Z", rev=2)

    r = run(env, "upsert", "--pr", "21785", "--role", "author", body=fresh)

    assert r.returncode == 0, r.stderr
    assert (stub_dir / "patched-11.body").read_text() == fresh


def test_new_review_regeneration_is_not_blocked(env):
    """`#new-review` legitimately republishes v1 over a v2 card. The guard
    compares composition time, not revision, so the reset still lands."""
    stub_dir, _ = env
    set_comments(stub_dir, [comment(11, stamped_author_card("2026-09-21T20:49:07Z", rev=2))])
    regenerated = stamped_author_card("2026-09-21T21:10:00Z", rev=1)

    r = run(env, "upsert", "--pr", "21785", "--role", "author", body=regenerated)

    assert r.returncode == 0, r.stderr
    assert (stub_dir / "patched-11.body").read_text() == regenerated


def test_unstamped_cards_fail_open(env):
    """A body with no parseable stamp (legacy, fixture, changed format) must
    never lose its publish to the guard."""
    stub_dir, _ = env
    set_comments(stub_dir, [comment(11, author_card())])
    card = author_card(extra="edited\n\n")

    r = run(env, "upsert", "--pr", "7", "--role", "author", body=card)

    assert r.returncode == 0, r.stderr
    assert (stub_dir / "patched-11.body").read_text() == card


def test_allow_stale_overwrite_is_the_break_glass(env):
    stub_dir, _ = env
    set_comments(stub_dir, [comment(11, stamped_author_card("2026-09-21T20:49:07Z", rev=2))])
    stale = stamped_author_card("2026-09-21T20:48:08Z")

    r = run(env, "upsert", "--pr", "21785", "--role", "author",
            "--allow-stale-overwrite", body=stale)

    assert r.returncode == 0, r.stderr
    assert (stub_dir / "patched-11.body").read_text() == stale


def test_guard_covers_the_brief_too(env):
    stub_dir, _ = env
    newer = (
        "<!-- CLAUDE_REVIEW_BRIEF -->\n## Reviewer's guide v2 — not for the author\n\n"
        "<sub>Review v2 · updated 2026-09-21T20:49:07Z · head commit aaaaaaa</sub>\n\n" + FOOTER
    )
    older = (
        "<!-- CLAUDE_REVIEW_BRIEF -->\n## Reviewer's guide v1 — not for the author\n\n"
        "<sub>Review v1 · updated 2026-09-21T20:48:08Z · head commit aaaaaaa</sub>\n\n" + FOOTER
    )
    set_comments(stub_dir, [comment(12, newer)])

    r = run(env, "upsert", "--pr", "21785", "--role", "brief", body=older)

    assert r.returncode == 0, r.stderr
    assert not (stub_dir / "patched-12.body").exists()


def test_refused_notice_names_iso_times_not_epochs(env):
    """The stand-down notice is the only diagnostic a refused publish leaves,
    so it has to name times a human recognizes."""
    stub_dir, _ = env
    set_comments(stub_dir, [comment(11, stamped_author_card("2026-09-21T20:49:07Z", rev=2))])
    stale = stamped_author_card("2026-09-21T20:48:08Z")

    r = run(env, "upsert", "--pr", "21785", "--role", "author", body=stale)

    out = r.stdout + r.stderr
    assert "2026-09-21T20:49:07Z" in out and "2026-09-21T20:48:08Z" in out
    assert "1758" not in out, "raw epoch seconds are not a diagnostic"


def test_unreadable_published_card_warns_before_failing_open(env):
    """Fail open, but say so: 'no newer card' and 'could not look' must not
    be indistinguishable in the log."""
    stub_dir, e = env
    # A comment id the list reports but the single-comment GET cannot serve.
    card = stamped_author_card("2026-09-21T20:48:08Z")
    set_comments(stub_dir, [comment(11, card)])
    broken = stub_dir / "gh"
    broken.write_text(GH_STUB.replace(
        'payload = json.dumps(next(c for c in comments if c["id"] == cid))',
        'sys.exit(1)'))
    broken.chmod(broken.stat().st_mode | stat.S_IEXEC)

    r = run((stub_dir, e), "upsert", "--pr", "21785", "--role", "author", body=card)

    assert r.returncode == 0, r.stderr
    assert "could not read the published" in r.stdout + r.stderr
    assert (stub_dir / "patched-11.body").exists(), "must still publish"
