#!/usr/bin/env python3
"""Deterministic publish gate for the content-review worker.

The worker's model job runs unprivileged and hands its work to the publish
job as data (a verdict sentinel plus a staged-changes patch). This script is
the code-enforced boundary between that model output and anything
credentialed: the publish job runs it before creating a branch, and again —
with `--paths-from` — after `git apply`, so the scope check runs against the
tree that actually ships rather than against patch text.

Checks (all deterministic; the gate fails closed):

- The queue parses and carries exactly one article with `path` and `slug`.
- The verdict sentinel parses, uses the canonical verdict vocabulary, and is
  consistent with the patch: `fixed` requires a non-empty patch, `clean`,
  `skipped`, and `reported` require an empty (or absent) one.
- `reported` (the report-only lane) additionally may not propose retirement:
  it is the verdict for a page this repo cannot edit at all.
- `no_retire` backstop: a retirement verdict on a page the queue stamps
  `no_retire: true` is a hard failure, regardless of what the model wrote in
  the PR body. A queue entry missing the field counts as `no_retire: true`.
- Diff scope (`--paths-from`, NUL-separated as produced by
  `git diff --cached --name-only -z`): every changed path must fall inside
  the allowed set for the review kind —
    fix PR:        the queued article itself, plus the shared render-time
                   sources the skill's rendered-content pass may correct
                   (`layouts/shortcodes/`, `layouts/partials/`, `data/`);
    retirement PR: `content/**` (the page, its inbound links, the redirect
                   target's aliases), `scripts/redirects/**`, and the docs
                   menu data file.

Outputs (to $GITHUB_OUTPUT when set, always echoed):

- `publish` — "true" only for a consistent `fixed` verdict; "false" for
  clean/skipped/absent verdicts (exit 0 — nothing to publish is a normal
  outcome, recorded by the ledger step).
- `branch` — the canonical branch name, derived here from the queue slug and
  the verdict's `retirement` flag so the model never chooses it.
- `retirement` — "true"/"false".
- `class` — the PR's auto-merge class, derived from the verdict's own
  `applied[]` categories (see `classify`): "deterministic" (the workflow arms
  GitHub auto-merge at publish; Robo-Cam's stamp merges it), "judgment" (opens
  un-armed; the review sweep arms it only when its gates pass), or "none"
  (nothing publishable). The class also lands on the PR as a
  `content-review/<class>` label.

Exit codes: 0 = pass (publish may be true or false), 1 = violation.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BRANCH_PREFIX = "content-review/"
# "reported" is the report-only lane's verdict (pulumi/docs#20996): the worker
# extracted and verified the page's claims, recorded them to the claims index,
# and changed nothing. It is a NON-PUBLISHING verdict whose patch must be
# empty — the pages it runs on are generated, so an edit is both out of scope
# and guaranteed to be overwritten by the generator.
VERDICTS = {"fixed", "clean", "skipped", "glowup", "reported"}

# Shared render-time sources the skill's rendered-content pass (SKILL.md
# step 6) may correct on any fix PR, beyond the article itself.
FIX_SHARED_PREFIXES = (
    "layouts/shortcodes/",
    "layouts/partials/",
    "data/",
)

# A retirement PR (SKILL.md "Retirement proposals") removes the page, adds
# the redirect (target-page aliases or an S3 redirect), updates inbound
# links, and drops the menu entry.
RETIRE_PREFIXES = (
    "content/",
    "scripts/redirects/",
)
RETIRE_FILES = ("data/docs_menu_sections.yml",)

# Auto-merge classing. A PR is "deterministic" — safe to arm auto-merge at
# publish, so an approving review (including Robo-Cam's rubber stamp) merges
# it — only when every applied fix is in a category whose correction the
# pipeline itself authored (a dead-link path, a Vale-named replacement, a
# frontmatter repair) AND the diff is small. Claim corrections and
# readthrough repairs are judgment calls however confident, so they class
# "judgment": the PR opens un-armed and the review sweep arms it only after
# its own gate stack passes. Retirements are always "judgment" — a page
# removal never merges on a bot stamp.
DETERMINISTIC_CATEGORIES = {"link", "vale", "frontmatter"}
# Added+deleted lines, counted from the patch. Deterministic fixes are
# line-scoped replacements; 40 covers a link/Vale sweep across a long page
# while excluding anything shaped like a rewrite. Tuning knob, not physics.
DETERMINISTIC_MAX_CHURN = 40


def fail(msg: str) -> None:
    print(f"::error::publish-gate: {msg}")


def emit(outputs: dict[str, str]) -> None:
    lines = [f"{k}={v}" for k, v in outputs.items()]
    out_path = os.environ.get("GITHUB_OUTPUT")
    if out_path:
        with open(out_path, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    for line in lines:
        print(line)


def load_article(queue_path: Path) -> dict | None:
    try:
        queue = json.loads(queue_path.read_text(encoding="utf-8"))
        articles = queue.get("articles") or []
    except (OSError, json.JSONDecodeError, AttributeError) as e:
        fail(f"queue {queue_path} is missing or unreadable ({e})")
        return None
    if len(articles) != 1:
        fail(f"queue must carry exactly one article, found {len(articles)}")
        return None
    article = articles[0]
    if not article.get("path") or not article.get("slug"):
        fail("queue article is missing 'path' or 'slug'")
        return None
    return article


def load_verdict(verdict_path: Path) -> tuple[dict | None, bool]:
    """Return (verdict, ok). An absent sentinel is ok (nothing to publish);
    an unreadable or malformed one is a violation."""
    if not verdict_path.is_file():
        return None, True
    try:
        verdict = json.loads(verdict_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        fail(f"verdict {verdict_path} is unreadable ({e})")
        return None, False
    if not isinstance(verdict, dict):
        fail("verdict sentinel is not a JSON object")
        return None, False
    v = verdict.get("verdict")
    if v not in VERDICTS:
        fail(f"unrecognized verdict {v!r} (expected one of {sorted(VERDICTS)})")
        return None, False
    for field in ("fixes", "skipped_findings"):
        if not isinstance(verdict.get(field, 0), int):
            fail(f"verdict field {field!r} is not an integer")
            return None, False
    if v in ("clean", "skipped") and not (verdict.get("reason") or "").strip():
        # The skill requires a reason for these; nag, don't block.
        print(f"::warning::publish-gate: verdict '{v}' carries no reason")
    return verdict, True


def patch_is_empty(patch_path: Path) -> bool:
    try:
        return patch_path.stat().st_size == 0
    except OSError:
        return True


def read_paths(paths_file: Path) -> list[str] | None:
    try:
        raw = paths_file.read_bytes()
    except OSError as e:
        fail(f"paths file {paths_file} is unreadable ({e})")
        return None
    return [p.decode("utf-8") for p in raw.split(b"\0") if p]


def patch_churn(patch_path: Path) -> int:
    """Added + deleted line count from a git patch (context lines excluded)."""
    try:
        text = patch_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return 0
    churn = 0
    for line in text.splitlines():
        if line.startswith(("+++", "---")):
            continue
        if line.startswith(("+", "-")):
            churn += 1
    return churn


def classify(verdict: dict | None, patch_path: Path, publish: bool) -> str:
    """The PR's auto-merge class — see the constants above for the policy.

    A glow-up is its own class: never armed at publish AND never stamped by
    the review sweep — human review is the lane's product.
    """
    if not publish or verdict is None:
        return "none"
    if verdict.get("verdict") == "glowup":
        return "glow-up"
    if verdict.get("retirement"):
        return "judgment"
    if verdict.get("clarity_flag"):
        return "judgment"
    applied = verdict.get("applied")
    if not isinstance(applied, list) or not applied:
        return "judgment"
    categories = {str(a.get("category")) for a in applied if isinstance(a, dict)}
    if not categories or not categories <= DETERMINISTIC_CATEGORIES:
        return "judgment"
    if patch_churn(patch_path) > DETERMINISTIC_MAX_CHURN:
        return "judgment"
    return "deterministic"


def check_scope(paths: list[str], article_path: str, retirement: bool,
                glowup: bool = False) -> bool:
    """True when every changed path is inside the allowed set."""
    ok = True
    art_dir = article_path.rsplit("/", 1)[0] + "/"
    for p in paths:
        if p == article_path:
            continue
        if glowup:
            # A glow-up rehabs ONE page: the article plus its page-bundle's
            # non-markdown assets. Never sibling articles, never the shared
            # render sources a fix PR may touch. verify-glowup-scope.py
            # re-checks this with the frontmatter/churn rules.
            allowed = p.startswith(art_dir) and not p.endswith(".md")
        elif retirement:
            allowed = p.startswith(RETIRE_PREFIXES) or p in RETIRE_FILES
        else:
            allowed = p.startswith(FIX_SHARED_PREFIXES)
        if not allowed:
            kind = "glow-up" if glowup else ("retirement" if retirement else "fix")
            fail(f"changed path {p!r} is outside the {kind}-PR scope for {article_path!r}")
            ok = False
    return ok


def check_glowup_body(body_file: Path, backlog_file: Path, verdict: dict | None) -> bool:
    """Every row the composer stubbed — banked findings and this run's fresh
    contradicted/mismatch verdicts — must sit in exactly one of the body's
    Backlog executed / Backlog declined tables, with no `<TODO` left in
    either. The glow-up analogue of the fix lane's per-hunk scope gate: a
    row the model silently dropped is work that vanished. The sentinel's
    executed_ids/declined_ids partition is checked too, but only warned on;
    record-page-findings.py already handles a partial list."""
    try:
        body = body_file.read_text()
        backlog = json.loads(backlog_file.read_text())
    except (OSError, json.JSONDecodeError) as e:
        fail(f"glow-up body check: input unreadable ({e})")
        return False
    spec = importlib.util.spec_from_file_location("compose_pr_body", HERE / "compose-pr-body.py")
    cpb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cpb)
    problems = cpb.glowup_body_accounting(body, backlog)
    for pr in problems:
        fail(f"glow-up body: {pr}")
    ids = {str(b.get("id")) for b in (backlog.get("banked") or []) if isinstance(b, dict)}
    ids |= {str(s.get("id")) for s in ((backlog.get("reconciled") or {}).get("fresh_stubs") or [])}
    v = verdict or {}
    listed = {str(i) for i in (v.get("executed_ids") or [])} | {str(i) for i in (v.get("declined_ids") or [])}
    both = {str(i) for i in (v.get("executed_ids") or [])} & {str(i) for i in (v.get("declined_ids") or [])}
    if ids - listed:
        print(f"::warning::publish-gate: sentinel lists neither executed nor declined for "
              f"{', '.join(sorted(ids - listed))}", file=sys.stderr)
    if both:
        print(f"::warning::publish-gate: sentinel lists {', '.join(sorted(both))} as both "
              "executed and declined", file=sys.stderr)
    return not problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--queue", required=True, type=Path)
    ap.add_argument("--verdict", required=True, type=Path)
    ap.add_argument("--patch", required=True, type=Path)
    ap.add_argument("--paths-from", type=Path, default=None,
                    help="NUL-separated changed-path list (git diff --name-only -z); "
                         "when given, also enforce the diff-scope rules")
    ap.add_argument("--body-file", type=Path, default=None,
                    help="glow-up only: the PR body draft; every composer-stubbed row "
                         "must land in Backlog executed or Backlog declined")
    ap.add_argument("--backlog", type=Path, default=None,
                    help="glow-up only: the reconciled .glowup-backlog.json the body "
                         "was composed from (the snapshot copy)")
    args = ap.parse_args()

    article = load_article(args.queue)
    if article is None:
        return 1

    verdict, ok = load_verdict(args.verdict)
    if not ok:
        return 1

    slug = article["slug"]
    retirement = bool(verdict.get("retirement")) if verdict else False
    glowup = bool(verdict and verdict.get("verdict") == "glowup")
    if glowup:
        branch = f"{BRANCH_PREFIX}glowup-{slug}"
    else:
        branch = f"{BRANCH_PREFIX}{'retire-' if retirement else ''}{slug}"
    empty = patch_is_empty(args.patch)

    violations = 0
    publish = False
    if verdict is None:
        print("publish-gate: no verdict sentinel; nothing to publish")
    elif verdict["verdict"] in ("fixed", "glowup"):
        if empty:
            fail(f"verdict is '{verdict['verdict']}' but the change patch is empty or absent")
            violations += 1
        else:
            publish = True
        if glowup and retirement:
            fail("a glowup verdict cannot also propose retirement")
            violations += 1
    else:  # clean / skipped / reported
        if not empty:
            fail(f"verdict is '{verdict['verdict']}' but the change patch is non-empty")
            violations += 1
        if verdict["verdict"] == "reported" and retirement:
            fail("a reported verdict cannot propose retirement — the report-only "
                 "lane runs on pages this repo does not own")
            violations += 1

    if retirement:
        # Fail closed: a queue entry that doesn't say no_retire: false is
        # treated as protected.
        if bool(article.get("no_retire", True)):
            fail(f"retirement proposed for {article['path']!r}, which the queue "
                 "stamps no_retire — this page must never be retired")
            violations += 1

    if args.paths_from is not None:
        paths = read_paths(args.paths_from)
        if paths is None:
            violations += 1
        elif not check_scope(paths, article["path"], retirement, glowup):
            violations += 1

    if glowup and publish and args.body_file is not None and args.backlog is not None:
        if not check_glowup_body(args.body_file, args.backlog, verdict):
            violations += 1

    if violations:
        return 1
    emit({
        "publish": "true" if publish else "false",
        "branch": branch,
        "retirement": "true" if retirement else "false",
        "glowup": "true" if glowup else "false",
        "class": classify(verdict, args.patch, publish),
    })
    return 0


if __name__ == "__main__":
    sys.exit(main())
