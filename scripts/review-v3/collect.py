#!/usr/bin/env python3
"""Collect every open PR the /pr-review queue can act on into queue.json.

    collect.py --out .pr-review-queue.json [--pr N] [--author app/workprentice]
               [--since 7d] [--ai|--no-ai] [--no-cache] [--snapshot-dir DIR]

Facts only — no verdicts. analyze.py adds the verdict, reason codes and the
cross-PR analyses; render.py draws it; act.py acts on it. Per open,
non-draft PR the record carries: number, title, author (with the trust
axes ported from the retired contributor-detection.sh / detect-ai-suspect.sh),
labels, changed files with their patches, head/base SHAs, mergeable_state,
the check rollup, reviews, requested reviewers, the parsed pinned review
(review-worklist.py, the only parser — both surfaces), its REVIEW_STATE,
the triage `<!-- TRIAGE_PROSE -->` comment, the reviewed-head SHA from
`<!-- CLAUDE_REVIEW_HEAD … -->`, the preview deployment URL and per-page
links (ported from the retired test-deployment-guidance.sh), and the risk
tier.

GitHub goes through gh_client.GhClient, so the same code runs on `gh`, on a
bare token (a Claude Code web session), or on a snapshot directory (tests,
or MCP-fetched data handed over by a model session). Author filters use
`gh_client.norm_login`, so `--author WorkPrentice`, `workprentice[bot]` and
`app/workprentice` all mean the same App — the search API alone needs the
`author:app/<slug>` spelling, and `gh_client.search_author_q` owns that.

Cache: `/.pr-review-cache/<pr>/<head_sha>-<updated_at>.json` holds the raw
per-PR responses that only change when the PR does (files, comments,
reviews, commits). `mergeable_state` and the check rollup are transient and
are re-fetched on every run. `--no-cache` bypasses reads; `--gc` drops
entries for PRs no longer open.

Deterministic, no model calls (scripts/review-v3 contract).
"""

from __future__ import annotations

import argparse
import base64
import importlib.util
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_HERE))
import gh_client  # noqa: E402
import review_state  # noqa: E402
import sentinel  # noqa: E402  (also loads compose-review.py as sentinel._compose)
from gh_client import GhClient, GhError, is_bot_login, norm_login  # noqa: E402

SCHEMA_VERSION = 1
DEFAULT_CACHE_DIR = _REPO_ROOT / ".pr-review-cache"
DEFAULT_OUT = _REPO_ROOT / ".pr-review-queue.json"
AI_ALLOWLIST_PATH = Path.home() / ".claude" / "pr-review" / "ai-suspect-authors.txt"
ORG = "pulumi"

_compose = sentinel._compose
AUTHOR_MARKER = _compose.AUTHOR_MARKER
BRIEF_MARKER = _compose.BRIEF_MARKER


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_worklist = None


def worklist():
    """review-worklist.py, loaded lazily (it execs two large siblings)."""
    global _worklist
    if _worklist is None:
        _worklist = _load(
            "collect_review_worklist",
            _REPO_ROOT / ".claude" / "commands" / "docs-review" / "scripts" / "review-worklist.py",
        )
    return _worklist


# ---- trust axes (ported from contributor-detection.sh) ------------------

TRUSTED_BOT_PREFIXES = ("dependabot", "pulumi-bot", "renovate", "copilot", "github-actions", "workprentice")
# Bots that read a review and push a revision. Everything else machine-authored
# (pulumi-bot's content-review / glow-up / regen lanes, dependabot, renovate)
# is a workflow: a changes-requested review lands on a PR nobody will answer,
# so those rows get close-or-fix instead of send-back.
AGENT_BOT_PREFIXES = ("workprentice", "copilot")
INFRA_PATH_RE = re.compile(r"^(scripts/|\.github/workflows/|Makefile$|infrastructure/|package\.json$|webpack\.config\.js$)")
PROGRAMS_PATH_RE = re.compile(r"^static/programs/")


def classify_author(login: str, user_type: str | None, gh: GhClient | None) -> tuple[str, str | None]:
    """(contributor_type, membership_note). Never assumes internal: an
    unreadable membership endpoint yields external + a note."""
    if is_bot_login(login, user_type):
        return "bot", None
    if gh is None:
        return "external", "membership not checked"
    try:
        member = gh.org_member(ORG, login)
    except GhError as exc:
        return "external", f"membership lookup failed: {exc}"
    if member is None:
        return "external", "membership not visible to this token"
    return ("internal" if member else "external"), None


def can_revise(contributor_type: str, login: str) -> bool:
    """Can this author act on a changes-requested review? People always can;
    a bot only when it is an agent that answers reviews."""
    if contributor_type != "bot":
        return True
    return norm_login(login).startswith(AGENT_BOT_PREFIXES)


def etiquette_trust(contributor_type: str, login: str, gh: GhClient | None) -> str:
    if contributor_type == "internal":
        return "high"
    if contributor_type == "bot":
        return "high" if norm_login(login).startswith(TRUSTED_BOT_PREFIXES) else "low"
    if gh is None:
        return "low"
    try:
        return "standard" if gh.merged_pr_count_by_author(login) >= 1 else "low"
    except GhError:
        return "low"


def risk_tier(files: list[dict], additions: int, deletions: int) -> str:
    paths = [f.get("filename") or f.get("path") or "" for f in files]
    total = int(additions or 0) + int(deletions or 0)
    if any(INFRA_PATH_RE.search(p) for p in paths):
        return "infra"
    new_files = sum(1 for f in files if (f.get("status") or "") == "added")
    if total > 300 or new_files > 0:
        return "major"
    programs = any(PROGRAMS_PATH_RE.search(p) for p in paths)
    if total <= 5 and len(paths) <= 1 and not programs:
        return "typo"
    if total <= 30 and len(paths) <= 1 and not programs:
        return "minor"
    return "standard"


# ---- AI-suspect (ported from detect-ai-suspect.sh) -----------------------

TRAILER_PATTERNS = (
    (re.compile(r"Co-Authored-By:\s*Claude", re.I), "claude"),
    (re.compile(r"Generated with\s*\[?Claude Code", re.I), "claude-code"),
    (re.compile(r"noreply@anthropic\.com", re.I), "anthropic"),
    (re.compile(r"Co-Authored-By:\s*Cursor", re.I), "cursor"),
    (re.compile(r"Co-Authored-By:\s*(GitHub )?Copilot", re.I), "copilot"),
    (re.compile(r"🤖 Generated with"), "robot-emoji"),
)
CONTRASTIVE_RE = re.compile(r"not [a-z]+,? (but|—|it's)", re.I)
HEDGE_RE = re.compile(
    r"\b(generally|typically|tends to|can often|may sometimes|in many cases|it.{1,3}s worth noting|it.{1,3}s important to note)\b",
    re.I,
)
EM_DASH_THRESHOLD = 0.015
HEDGE_THRESHOLD = 0.012


def added_prose_lines(files: list[dict]) -> list[str]:
    """Added prose lines from .md patches: no frontmatter, no fenced code.
    Same state machine as the shell awk, per file."""
    out: list[str] = []
    for f in files:
        path = f.get("filename") or ""
        patch = f.get("patch") or ""
        if not path.endswith(".md") or not patch:
            continue
        in_fence = in_fm = seen_content = False
        for line in patch.splitlines():
            if line.startswith("@@") or line.startswith("+++") or line.startswith("---"):
                continue
            if line[:1] in "+ " and line[1:].startswith("```"):
                in_fence = not in_fence
                seen_content = True
                continue
            if in_fence:
                continue
            if line[:1] in "+ " and line[1:].strip() == "---" and not seen_content:
                in_fm = not in_fm
                if not in_fm:
                    seen_content = True
                continue
            if in_fm:
                continue
            if line.startswith("+"):
                out.append(line[1:])
                seen_content = True
            elif line.startswith(" ") and line[1:].strip():
                seen_content = True
    return out


def ai_suspect(
    login: str, body: str, commit_messages: list[str], files: list[dict],
    override: str | None = None, allowlist_path: Path | None = None,
    contributor_type: str = "external",
) -> tuple[bool, list[str]]:
    """The AI-suspect signals apply to humans. A bot author (the content
    pipelines, workprentice) is an AI by construction and carries the
    trailers on purpose, so only the manual override and the allowlist can
    flag one — otherwise every pipeline PR would sit at heightened scrutiny
    and the axis would say nothing."""
    if override == "no-ai":
        return False, ["manual:no-ai"]
    if override == "ai":
        return True, ["manual"]
    reasons: list[str] = []
    allow = allowlist_path or AI_ALLOWLIST_PATH
    if login and allow.is_file():
        for raw in allow.read_text(errors="replace").splitlines():
            if raw.strip() == login:
                reasons.append("allowlist")
                break
    if contributor_type == "bot":
        return bool(reasons), reasons
    haystack = (body or "") + "\n" + "\n".join(commit_messages)
    for rx, label in TRAILER_PATTERNS:
        if rx.search(haystack) and f"trailer:{label}" not in reasons:
            reasons.append(f"trailer:{label}")
    if not reasons:
        prose = added_prose_lines(files)
        words = sum(len(l.split()) for l in prose)
        if len(prose) >= 10 and words > 50:
            if sum(l.count("—") for l in prose) / words > EM_DASH_THRESHOLD:
                reasons.append("prose-pattern:em-dash")
            contrastive = sum(1 for l in prose if CONTRASTIVE_RE.search(l))
            paras = max(len(prose) // 4, 1)
            if contrastive > 0 and contrastive * 3 > paras:
                reasons.append("prose-pattern:contrastive")
            hedges = sum(1 for l in prose if HEDGE_RE.search(l))
            if hedges / words > HEDGE_THRESHOLD:
                reasons.append("prose-pattern:hedge")
    return bool(reasons), reasons


# ---- review surface -----------------------------------------------------

REVIEW_STATE_LABELS = ("review:in-progress", "review:outstanding-issues", "review:no-blockers", "review:stale", "review:error")


def find_review_comments(comments: list[dict]) -> tuple[dict | None, dict | None, str]:
    """(author/legacy comment, brief comment, surface) — surface is v3 | v2 | none."""
    author = sentinel._find_comment(comments, AUTHOR_MARKER)
    if author:
        return author, sentinel._find_comment(comments, BRIEF_MARKER), "v3"
    legacy = sentinel._find_legacy_comment(comments)
    if legacy:
        return legacy, None, "v2"
    return None, None, "none"


# 💡/📎 are the pre-2026-09-25 prefixes of the two lines after the list.
RUBBER_RE = re.compile(r"### ✅ What you can rubber-stamp\s*(.*?)"
                       r"(?=\n#{2,3} |\n💡|\n📎|\n\*\*Pre-existing issues|\n\*\*Full evidence:|\Z)", re.S)
EVIDENCE_RE = re.compile(r"\[([^\]]+)\]\((https://[^)\s]*review-evidence[^)\s]*)\)")


def rubber_stamp_lines(brief_body: str) -> list[str]:
    """The brief's "what you can rubber-stamp" bullets: what the review
    already checked, so the approver knows what not to re-check."""
    m = RUBBER_RE.search(brief_body or "")
    if not m:
        return []
    return [ln.strip().lstrip("-").strip() for ln in m.group(1).splitlines() if ln.strip().startswith("-")]


def evidence_url(brief_body: str, author_body: str = "") -> str | None:
    """The verification trail the review published for this PR."""
    for body in (brief_body or "", author_body or ""):
        m = EVIDENCE_RE.search(body)
        if m:
            return m.group(2)
    return None


def review_status(labels: set[str], surface: str, review_body: str, head_sha: str, triage_prose: bool) -> str:
    """CURRENT | STALE | IN_PROGRESS | ERROR | ABSENT | TRIAGE_PROSE.

    Labels alone are not a freshness signal (pushes via GITHUB_TOKEN skip
    `synchronize`), so CURRENT additionally needs the card's
    CLAUDE_REVIEW_HEAD to prefix-match the live head.
    """
    if "review:error" in labels:
        return "ERROR"
    if "review:in-progress" in labels:
        return "IN_PROGRESS"
    if surface == "none":
        return "TRIAGE_PROSE" if triage_prose else "ABSENT"
    if "review:stale" in labels:
        return "STALE"
    if head_sha and not sentinel._body_matches_head(review_body, head_sha):
        return "STALE"
    return "CURRENT"


def only_merges_since(commits: list[dict], review_body: str) -> bool:
    """True when the reviewed head (the card's CLAUDE_REVIEW_HEAD) is in the
    PR's commit list and every later commit has two parents."""
    m = sentinel.HEAD_MARKER_RE.search(review_body or "")
    if not m:
        return False
    reviewed = m.group(1)
    shas = [c.get("sha") or "" for c in commits]
    idx = next((i for i, sha in enumerate(shas) if sha.startswith(reviewed) or reviewed.startswith(sha)), None)
    if idx is None or idx == len(shas) - 1:
        return False
    return all(len(c.get("parents") or []) >= 2 for c in commits[idx + 1:])


def reviewed_head(review_body: str) -> str | None:
    m = sentinel.HEAD_MARKER_RE.search(review_body or "")
    return m.group(1) if m else None


def changed_lines(files: list[dict]) -> dict[str, list[str]]:
    """Per file, the sorted `+`/`-` lines of its patch. Hunk headers and
    context are left out because they move whenever the base moves; the
    changed lines themselves only move when the PR's content does."""
    out: dict[str, list[str]] = {}
    for f in files:
        name = f.get("filename") or f.get("path") or ""
        lines = [ln for ln in (f.get("patch") or "").splitlines()
                 if ln[:1] in "+-" and not ln.startswith(("+++", "---"))]
        out[name] = sorted(lines)
    return out


def same_diff(files_then: list[dict], files_now: list[dict]) -> bool:
    """Whether two snapshots of a PR's files carry the same changes. A merge
    of the base that resolved a conflict by editing a line the PR adds
    changes the content the review read, and must not count as base-only."""
    return changed_lines(files_then) == changed_lines(files_now)


def parse_review(author_body: str, brief_body: str, pr: int, repo: str) -> dict:
    """review-worklist.py's report, plus the raw REVIEW_STATE and the ⚠️ rows."""
    wl = worklist()
    report = wl.build_report(wl.join_pages(author_body) if author_body else "", [], {}, pr, repo,
                             suggestions_ok=True, brief_body=brief_body or "")
    state = None
    if AUTHOR_MARKER in author_body:
        try:
            state = review_state.parse_state(author_body)
        except ValueError:
            state = None
    checks_prefix = _compose.CHECKS_HEADING[len("### "):]
    warning_rows = sentinel._card_rows(brief_body, (checks_prefix,)) if brief_body else []
    stances = bool(brief_body) and _compose.STANCES_HEADING in brief_body
    nothing_blocks = sentinel._author_card_nothing_blocks(author_body) if author_body else False
    return {
        "surface": report["surface"] if author_body else "none",
        "reviewed_sha": report["reviewed_sha"],
        "parse_confidence": report["parse_confidence"],
        # Buckets whose count the card's own tally declares higher than what
        # parsed out of its sections: a body that arrived incomplete.
        "counts_shortfall": report.get("counts_shortfall") or {},
        "items": report["items"],
        "summary": report["summary"],
        "review_state": state,
        "warning_rows": warning_rows,
        "stances": stances,
        "nothing_blocks": nothing_blocks,
        "brief_summary_bullets": brief_change_bullets(brief_body) if brief_body else [],
        "rubber_stamp": rubber_stamp_lines(brief_body or ""),
        "evidence_url": evidence_url(brief_body or "", author_body or ""),
    }


_CHANGES_LABEL = "**What this PR changes:**"


def brief_change_bullets(brief_body: str) -> list[str]:
    """The `- ` bullets under the brief's "What this PR changes" label
    (inside a `> [!NOTE]` blockquote, so the `> ` prefix is stripped)."""
    out: list[str] = []
    seen = False
    for raw in brief_body.splitlines():
        line = raw[2:] if raw.startswith("> ") else (raw[1:] if raw.startswith(">") else raw)
        if not seen:
            if _CHANGES_LABEL in line:
                seen = True
            continue
        s = line.strip()
        if s.startswith("- "):
            out.append(s[2:].strip())
        elif s == "":
            if out:
                break
        else:
            break
    return out


# ---- preview (ported from test-deployment-guidance.sh) -------------------

PREVIEW_URL_RE = re.compile(r"https?://www-testing-pulumi-docs-origin-pr-\d+-[a-f0-9]+\.s3-website[.-]us-west-2\.amazonaws\.com")
TITLE_RE = re.compile(r"^\+?title:\s*[\"']?(.*?)[\"']?\s*$", re.M)


def content_path_to_url(path: str) -> str:
    p = path
    if p.startswith("content/"):
        p = p[len("content/"):]
    if p.endswith(".md"):
        p = p[:-3]
    if p.endswith("_index"):
        p = p[: -len("_index")]
    elif p.endswith("/index"):
        p = p[: -len("index")]
    if not p.endswith("/"):
        p += "/"
    return "/" + p.lstrip("/")


def page_title(path: str, patch: str, repo_root: Path) -> str:
    m = re.search(r"^\+title:\s*[\"']?(.*?)[\"']?\s*$", patch or "", re.M)
    if m and m.group(1):
        return m.group(1)
    local = repo_root / path
    if local.is_file():
        try:
            head = local.read_text(errors="replace")[:4096]
        except OSError:
            head = ""
        m = re.search(r"^title:\s*[\"']?(.*?)[\"']?\s*$", head, re.M)
        if m and m.group(1):
            return m.group(1)
    stem = Path(path).stem
    if stem in ("_index", "index"):
        stem = Path(path).parent.name
    return stem.replace("-", " ").title()


def preview_info(comments: list[dict], files: list[dict], repo_root: Path) -> dict:
    url = None
    for c in comments:
        if (c.get("user") or {}).get("login") != "pulumi-bot":
            continue
        found = PREVIEW_URL_RE.findall(c.get("body") or "")
        if found:
            url = found[-1]
    pages = []
    non_content = []
    for f in files:
        path = f.get("filename") or ""
        if path.startswith("content/") and path.endswith(".md"):
            page_url = content_path_to_url(path)
            pages.append({
                "file": path,
                "title": page_title(path, f.get("patch") or "", repo_root),
                "url": page_url,
                "preview_url": (url.rstrip("/") + page_url) if url else None,
            })
        else:
            non_content.append(path)
    return {"url": url, "status": "ready" if url else "pending", "pages": pages, "non_content_files": non_content}


BLOG_INDEX_RE = re.compile(r"^content/blog/[^/]+/index\.md$")
DATE_LINE_RE = re.compile(r"^\+?date:\s*[\"']?([0-9]{4}-[0-9]{2}-[0-9]{2}[^\"'\s]*)", re.M)


def blog_date(f: dict, head_sha: str, gh: GhClient | None, repo_root: Path) -> str | None:
    """The post's `date:` at the PR head, for content/blog/<slug>/index.md
    only: from the patch's added lines first, then the local checkout (the
    date rarely changes), then the file at the head SHA."""
    path = f.get("filename") or ""
    if not BLOG_INDEX_RE.match(path) or (f.get("status") or "") == "removed":
        return None
    m = re.search(r"^\+date:\s*[\"']?([0-9]{4}-[0-9]{2}-[0-9]{2}[^\"'\s]*)", f.get("patch") or "", re.M)
    if m:
        return m.group(1)
    local = repo_root / path
    if local.is_file():
        try:
            m = DATE_LINE_RE.search(local.read_text(errors="replace")[:4096])
        except OSError:
            m = None
        if m:
            return m.group(1)
    if gh is not None and head_sha:
        try:
            text = gh.contents(path, head_sha) or ""
        except GhError:
            text = ""
        m = DATE_LINE_RE.search(text[:4096])
        if m:
            return m.group(1)
    return None


# ---- checks rollup ------------------------------------------------------

FAILED_CONCLUSIONS = {"failure", "timed_out", "cancelled", "action_required", "startup_failure"}


def _run_order(run: dict) -> tuple:
    return (run.get("started_at") or "", run.get("completed_at") or "", run.get("id") or 0)


def checks_rollup(check_runs: list[dict], statuses: list[dict], workflows: dict[int, str] | None = None) -> dict:
    """green | red | pending, with the failing/pending names. Neutral and
    skipped runs count as green (the report-only Sentinel is neutral).

    Only the newest run of each check in each workflow counts. The API's
    default `filter=latest` is per check suite, and every workflow run is its
    own suite, so a run a concurrency group cancelled stays in the list beside
    the run that replaced it. Counting it would turn a green PR red.

    The workflow is part of the key because job names repeat across
    workflows: pull-request.yml and testing-build-and-deploy.yml both run
    "Install deps and build site", master's required check, and a passing
    deploy must never stand in for a failed PR build. `workflows` maps
    check_suite_id → workflow (`GhClient.workflow_paths`); a suite it doesn't
    know keys on the suite itself, which dedupes nothing and so errs red."""
    workflows = workflows or {}
    newest: dict[tuple, dict] = {}
    for run in check_runs:
        suite = (run.get("check_suite") or {}).get("id")
        owner = workflows.get(suite) if suite in workflows else f"suite:{suite}"
        key = (owner, run.get("name") or "?")
        seen = newest.get(key)
        if seen is None or _run_order(run) >= _run_order(seen):
            newest[key] = run
    check_runs = list(newest.values())
    failing, pending = [], []
    for run in check_runs:
        name = run.get("name") or "?"
        if run.get("status") != "completed":
            pending.append(name)
        elif (run.get("conclusion") or "") in FAILED_CONCLUSIONS:
            failing.append(name)
    latest: dict[str, str] = {}
    for s in statuses:  # newest first from the API; keep the first seen per context
        latest.setdefault(s.get("context") or "?", s.get("state") or "")
    for ctx, state in latest.items():
        if state in ("failure", "error"):
            failing.append(ctx)
        elif state == "pending":
            pending.append(ctx)
    state = "red" if failing else ("pending" if pending else "green")
    return {"state": state, "failing": sorted(set(failing)), "pending": sorted(set(pending)),
            "total": len(check_runs) + len(latest)}


# ---- per-PR collection --------------------------------------------------


def _cache_key(pr: dict) -> str:
    updated = (pr.get("updated_at") or "").replace(":", "").replace("-", "")
    return f"{pr['head']['sha']}-{updated}"


def _read_cache(cache_dir: Path | None, number: int, key: str) -> dict | None:
    if not cache_dir:
        return None
    f = cache_dir / str(number) / f"{key}.json"
    if f.is_file():
        try:
            return json.loads(f.read_text())
        except (OSError, ValueError):
            return None
    return None


def _write_cache(cache_dir: Path | None, number: int, key: str, data: dict) -> None:
    if not cache_dir:
        return
    d = cache_dir / str(number)
    d.mkdir(parents=True, exist_ok=True)
    for stale in d.glob("*.json"):
        if stale.stem != key:
            stale.unlink(missing_ok=True)
    (d / f"{key}.json").write_text(json.dumps(data))


def fetch_detail(gh: GhClient, number: int, retries: int = 3, delay: float = 1.5) -> dict:
    """`GET pulls/N`, re-asked while `mergeable_state` is `unknown`: GitHub
    computes mergeability lazily and the first read after a quiet spell
    returns `unknown` with `mergeable: null`. Snapshots are never retried."""
    detail = gh.pr(number)
    if gh.backend == "snapshot":
        return detail
    for _ in range(retries):
        if detail.get("mergeable") is not None or (detail.get("mergeable_state") or "unknown") != "unknown":
            break
        time.sleep(delay)
        detail = gh.pr(number)
    return detail


def collect_pr(gh: GhClient, listed: dict, *, cache_dir: Path | None, repo_root: Path,
               ai_override: str | None = None, allowlist_path: Path | None = None,
               approver: str | None = None) -> dict:
    number = listed["number"]
    detail = fetch_detail(gh, number)  # always live: mergeable_state is transient
    head_sha = (detail.get("head") or {}).get("sha") or ""
    key = _cache_key(detail)
    raw = _read_cache(cache_dir, number, key)
    if raw is None:
        raw = {
            "files": gh.pr_files(number),
            "comments": gh.issue_comments(number),
            "reviews": gh.reviews(number),
            "commits": gh.pr_commits(number),
            "review_comments": gh.review_comments(number),
        }
        _write_cache(cache_dir, number, key, raw)
    check_runs = gh.check_runs(head_sha) if head_sha else []
    statuses = gh.commit_statuses(head_sha) if head_sha else []
    workflows = gh.workflow_paths(head_sha) if head_sha else {}
    requested = gh.requested_reviewers(number)

    files = raw["files"]
    comments = raw["comments"]
    labels = {(l.get("name") or "") for l in (detail.get("labels") or [])}
    user = detail.get("user") or {}
    login = user.get("login") or ""
    ctype, membership_note = classify_author(login, user.get("type"), gh)
    if ctype == "external" and membership_note and not sentinel._is_external(detail):
        # Only write access can push a branch into this repo, so a same-repo
        # head is an internal author even when the token can't read the org.
        ctype, membership_note = "internal", membership_note + "; same-repo branch => internal"
    trust = etiquette_trust(ctype, login, gh)
    commit_messages = [((c.get("commit") or {}).get("message") or "") for c in raw["commits"]]
    suspect, reasons = ai_suspect(login, detail.get("body") or "", commit_messages, files,
                                  override=ai_override, allowlist_path=allowlist_path, contributor_type=ctype)

    author_c, brief_c, surface = find_review_comments(comments)
    author_body = (author_c or {}).get("body") or ""
    brief_body = (brief_c or {}).get("body") or ""
    triage_c = sentinel._find_comment(comments, sentinel.TRIAGE_PROSE_MARKER)
    status = review_status(labels, surface, author_body, head_sha, triage_c is not None)
    base_merged = False
    if status == "STALE" and surface != "none":
        # --unblock (and any hand merge of the base) moves the head without
        # changing the diff the review read. When every commit after the
        # reviewed head is a merge commit, the review still describes the
        # PR; a real push would need the pipeline's refresh.
        # A merge commit can still carry a content change (a conflict
        # resolved by hand), so the shape of the history isn't enough: the
        # `+`/`-` lines at the reviewed head have to match the ones now.
        base_merged = only_merges_since(raw["commits"], author_body)
        if base_merged:
            then = reviewed_head(author_body) or ""
            base_ref = (detail.get("base") or {}).get("ref") or ""
            try:
                base_merged = same_diff(gh.compare_files(base_ref, then), raw["files"])
            except GhError:
                base_merged = False  # can't prove the diff is unchanged, so it isn't
        if base_merged:
            status = "CURRENT"
    review = parse_review(author_body, brief_body, number, gh.repo) if author_body else {
        "surface": "none", "reviewed_sha": None, "parse_confidence": "low", "items": [],
        "summary": None, "review_state": None, "warning_rows": [], "stances": False,
        "nothing_blocks": False, "brief_summary_bullets": [], "rubber_stamp": [], "evidence_url": None,
        "counts_shortfall": {},
    }
    # How many comments the review is spread over, and which of them GitHub
    # did not return. A legacy (v2) review over one comment's size limit is
    # split, and its findings sections are the tail of the document — so a
    # missing page is a review whose 🚨 rows may simply not be here. The
    # analyzer fails closed on it rather than parsing what happens to exist.
    review["pages"] = (author_c or {}).get("review_pages") or 1
    review["pages_missing"] = (author_c or {}).get("review_pages_missing") or []
    review["status"] = status
    review["base_merged"] = base_merged
    review["author_comment_id"] = (author_c or {}).get("id")
    review["brief_comment_id"] = (brief_c or {}).get("id")
    review["author_body"] = author_body
    review["brief_body"] = brief_body

    additions = int(detail.get("additions") or 0)
    deletions = int(detail.get("deletions") or 0)
    head = detail.get("head") or {}
    head_repo = head.get("repo") or {}
    base_repo = ((detail.get("base") or {}).get("repo") or {})
    return {
        "number": number,
        "title": detail.get("title") or "",
        "url": detail.get("html_url") or f"https://github.com/{gh.repo}/pull/{number}",
        "body": detail.get("body") or "",
        "author": {
            "login": login,
            "norm": norm_login(login),
            "type": ctype,
            "etiquette_trust": trust,
            "can_revise": can_revise(ctype, login),
            "membership_note": membership_note,
        },
        "head": {
            "sha": head_sha,
            "ref": head.get("ref") or "",
            "repo_full_name": head_repo.get("full_name") if head_repo else None,
            "is_fork": sentinel._is_external(detail),
        },
        "base_ref": (detail.get("base") or {}).get("ref") or "",
        "base_sha": (detail.get("base") or {}).get("sha") or "",
        "base_repo": base_repo.get("full_name"),
        "draft": bool(detail.get("draft")),
        "created_at": detail.get("created_at"),
        "updated_at": detail.get("updated_at"),
        "labels": sorted(labels),
        "mergeable": detail.get("mergeable"),
        "mergeable_state": detail.get("mergeable_state") or "unknown",
        "checks": checks_rollup(check_runs, statuses, workflows),
        "files": [
            {
                "path": f.get("filename") or "",
                "status": f.get("status") or "",
                "additions": int(f.get("additions") or 0),
                "deletions": int(f.get("deletions") or 0),
                "patch": f.get("patch"),
                "previous_filename": f.get("previous_filename"),
                "blog_date": blog_date(f, head_sha, gh, repo_root),
            }
            for f in files
        ],
        "additions": additions,
        "deletions": deletions,
        "changed_lines": additions + deletions,
        "reviews": [
            {"user": ((r.get("user") or {}).get("login") or ""), "state": r.get("state") or "",
             "submitted_at": r.get("submitted_at"), "user_type": (r.get("user") or {}).get("type"),
             # the head the review was left on: analyze.own_send_back compares
             # it with the live head to tell "waiting on the author" from
             # "they pushed since"
             "commit_id": r.get("commit_id")}
            for r in raw["reviews"]
        ],
        "requested_reviewers": {
            "users": [u.get("login") for u in (requested.get("users") or [])
                      if not is_bot_login(u.get("login"), u.get("type"))],
            "teams": [t.get("slug") for t in (requested.get("teams") or [])],
        },
        "one_click_suggestions": [
            {"id": c.get("id"), "path": c.get("path"), "line": c.get("line") or c.get("original_line"),
             "body": c.get("body"), "diff_hunk": c.get("diff_hunk")}
            for c in raw["review_comments"]
            if (c.get("body") or "").startswith("<!-- CLAUDE_STYLE_SUGGESTION -->")
        ],
        "risk_tier": risk_tier(files, additions, deletions),
        "scrutiny": "heightened" if suspect else "standard",
        "ai_suspect": {"flag": suspect, "reasons": reasons},
        "review": review,
        "triage_prose": (triage_c or {}).get("body"),
        "unblock_conflict": unblock_conflict(comments, head_sha, _unblock_conflict_authors(approver)),
        "preview": preview_info(comments, files, repo_root),
        "cache_key": key,
    }


# ---- queue --------------------------------------------------------------


UNBLOCK_CONFLICT_MARKER = "<!-- PR_REVIEW_UNBLOCK_CONFLICT -->"


def _unblock_conflict_authors(approver: str | None) -> set[str]:
    """Who may write the conflict record: the review bot, or the approver --
    the one who ran the merge that failed.

    `collect()` has already resolved the approver (`--approver`, else
    `gh.me()`), so this takes it rather than asking the token again. Asking
    again was wrong twice over: a run started with `--approver` would check
    a different login than the one the rest of the queue uses, and a backend
    that cannot answer `GET /user` would check nothing at all -- either way
    the record goes unseen and the board re-offers the dead button this
    reader exists to withhold."""
    return {norm_login(sentinel.BOT_LOGIN)} | ({norm_login(approver)} - {""})
_UNBLOCK_CONFLICT_HEAD_RE = re.compile(r"the branch is exactly as it was at `([0-9a-f]{7,40})`")


def unblock_conflict(comments: list[dict], head_sha: str, authors: set[str] | None = None) -> dict | None:
    """The record `act.py` leaves when a `--unblock` base merge stops on
    conflicts, but only while it still describes *this* head.

    Without it the board had no memory of a refused merge: the row came back
    `mergeable:dirty` with the same "merge base & retry" button, and pressing
    it re-ran the same conflict. A push after the report settles the question
    one way or the other, so a marker recorded against an older head is spent
    and this returns None.

    Provenance, for the same reason `sentinel._find_comment` cares: the
    marker withholds a button, so a forged one is a (mild) denial of
    service. It cannot go through that reader, though -- act.py comments as
    whoever ran `/pr-review`, not as the review app -- so the rule is the
    same shape with a different roster: the marker on an exact line among
    the body's first three, from the review bot or from the approver whose
    run wrote it. `authors` is that roster, already normalized by
    `_unblock_conflict_authors`; None means don't check, which is only for
    callers with no identity to check against."""
    for c in reversed(comments):  # newest first: a re-tried merge supersedes
        login = (c.get("user") or {}).get("login") or ""
        if authors is not None and norm_login(login) not in authors:
            continue
        body = c.get("body") or ""
        if UNBLOCK_CONFLICT_MARKER not in [ln.strip() for ln in body.splitlines()[:3]]:
            continue
        m = _UNBLOCK_CONFLICT_HEAD_RE.search(body)
        if not head_sha or not m or not head_sha.startswith(m.group(1)):
            continue
        files = [l.strip("- ").strip("`") for l in body.splitlines()
                 if l.startswith("- `") and l.rstrip().endswith("`")]
        return {"head": head_sha, "files": files, "by": login, "url": c.get("html_url") or ""}
    return None


def parse_since(spec: str | None, now: datetime | None = None) -> datetime | None:
    if not spec:
        return None
    now = now or datetime.now(timezone.utc)
    m = re.fullmatch(r"(\d+)([dhw])", spec.strip())
    if m:
        n, unit = int(m.group(1)), m.group(2)
        delta = {"d": timedelta(days=n), "h": timedelta(hours=n), "w": timedelta(weeks=n)}[unit]
        return now - delta
    try:
        dt = datetime.fromisoformat(spec.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"--since wants 7d / 12h / 2w or an ISO date, got {spec!r}") from exc
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def select_prs(listed: list[dict], *, numbers: list[int] | None, authors: list[str] | None,
               since: datetime | None, include_drafts: bool = False) -> list[dict]:
    want_authors = {norm_login(a) for a in (authors or []) if a and a != "any"}
    out = []
    for pr in listed:
        if numbers and pr["number"] not in numbers:
            continue
        if pr.get("draft") and not include_drafts and not numbers:
            continue
        if want_authors and norm_login((pr.get("user") or {}).get("login")) not in want_authors:
            continue
        if since:
            created = datetime.fromisoformat((pr.get("created_at") or "").replace("Z", "+00:00"))
            if created < since:
                continue
        out.append(pr)
    return out


def routing_teams(gh: GhClient, repo_root: Path | None) -> dict[str, bool | None]:
    """`{"org/slug": exists}` for every team review-routing.yml names, so the
    analyzer can route to the team when it is real and to the SLA person when
    it isn't yet. An unreadable config yields {} (route to people)."""
    path = (repo_root or _REPO_ROOT) / ".github" / "review-routing.yml"
    try:
        import routing  # noqa: PLC0415  (sibling module; loaded here so a broken config can't break collect)
        teams = routing.load_config(path).teams
    except Exception:  # noqa: BLE001
        return {}
    out: dict[str, bool | None] = {}
    for full in sorted(set(teams.values())):
        org, _, slug = full.partition("/")
        out[full] = gh.team_exists(org, slug) if org and slug else None
    return out


def my_team_memberships(gh: GhClient, repo_root: Path | None, login: str | None) -> dict[str, bool | None]:
    """`{"org/slug": am I on it}` for every team review-routing.yml names, so
    a run with no `~/.pr-review.yml` can take its lanes from the org chart
    instead of claiming all of them. None means the token couldn't read it."""
    if not login:
        return {}
    path = (repo_root or _REPO_ROOT) / ".github" / "review-routing.yml"
    try:
        import routing  # noqa: PLC0415
        teams = routing.load_config(path).teams
    except Exception:  # noqa: BLE001
        return {}
    out: dict[str, bool | None] = {}
    for full in sorted(set(teams.values())):
        org, _, slug = full.partition("/")
        out[full] = gh.team_member(org, slug, login) if org and slug else None
    return out


def collect(gh: GhClient, *, numbers: list[int] | None = None, authors: list[str] | None = None,
            since: str | None = None, cache_dir: Path | None = DEFAULT_CACHE_DIR,
            repo_root: Path = _REPO_ROOT, ai_override: str | None = None, workers: int = 6,
            allowlist_path: Path | None = None, approver: str | None = None) -> dict:
    listed = gh.list_open_prs()
    chosen = select_prs(listed, numbers=numbers, authors=authors, since=parse_since(since))
    if not approver:
        approver = gh.me()  # who "me" is for the handed-off rule; None on a snapshot without GET/user.json
    errors: list[dict] = []

    def one(pr):
        try:
            return collect_pr(gh, pr, cache_dir=cache_dir, repo_root=repo_root,
                              ai_override=ai_override, allowlist_path=allowlist_path, approver=approver)
        except GhError as exc:
            errors.append({"pr": pr["number"], "error": str(exc)})
            return None

    if workers > 1 and gh.backend != "snapshot":
        with ThreadPoolExecutor(max_workers=workers) as pool:
            records = list(pool.map(one, chosen))
    else:
        records = [one(p) for p in chosen]
    prs = sorted((r for r in records if r), key=lambda r: -r["number"])
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "repo": gh.repo,
        "backend": gh.backend,
        "approver": approver,
        "my_teams": my_team_memberships(gh, repo_root, approver),
        "teams": routing_teams(gh, repo_root),
        "filters": {"pr": numbers or [], "author": authors or [], "since": since},
        "open_count": len(listed),
        "prs": prs,
        "errors": errors,
    }


def gc_cache(cache_dir: Path, open_numbers: set[int]) -> int:
    removed = 0
    if not cache_dir.is_dir():
        return 0
    for d in cache_dir.iterdir():
        if d.is_dir() and d.name.isdigit() and int(d.name) not in open_numbers:
            for f in d.glob("*.json"):
                f.unlink()
                removed += 1
            d.rmdir()
    return removed


# ---- CLI ----------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=gh_client.DEFAULT_REPO)
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--pr", type=int, action="append", help="only this PR (repeatable)")
    ap.add_argument("--author", action="append", help="author filter, any spelling of an App login (repeatable)")
    ap.add_argument("--since", help="7d / 12h / 2w or an ISO date; PRs created before it are skipped")
    ap.add_argument("--ai", dest="ai_override", action="store_const", const="ai")
    ap.add_argument("--no-ai", dest="ai_override", action="store_const", const="no-ai")
    ap.add_argument("--backend", default="auto", choices=("auto", "gh", "rest", "snapshot"))
    ap.add_argument("--snapshot-dir")
    ap.add_argument("--record-dir", help="mirror live responses into a snapshot dir")
    ap.add_argument("--cache-dir", default=str(DEFAULT_CACHE_DIR))
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--gc", action="store_true", help="drop cache entries for PRs no longer open")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--approver", help="the approver's login, echoed into queue.json")
    ap.add_argument("--self-test", action="store_true")
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.self_test:
        import test_collect  # noqa: PLC0415 — the pytest file doubles as the harness
        return test_collect.run_standalone()
    gh = GhClient(args.repo, args.backend, snapshot_dir=args.snapshot_dir, record_dir=args.record_dir)
    cache_dir = None if args.no_cache else Path(args.cache_dir)
    queue = collect(gh, numbers=args.pr, authors=args.author, since=args.since, cache_dir=cache_dir,
                    ai_override=args.ai_override, workers=args.workers, approver=args.approver)
    if args.gc and cache_dir:
        n = gc_cache(cache_dir, {p["number"] for p in gh.list_open_prs()})
        print(f"cache: removed {n} stale file(s)", file=sys.stderr)
    Path(args.out).write_text(json.dumps(queue, indent=1, sort_keys=True) + "\n")
    print(f"collected {len(queue['prs'])} PR(s) → {args.out}" + (f" ({len(queue['errors'])} error(s))" if queue["errors"] else ""),
          file=sys.stderr)
    for e in queue["errors"]:
        print(f"  #{e['pr']}: {e['error']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
