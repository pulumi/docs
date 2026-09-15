#!/usr/bin/env python3
"""Enrich queue.json with one verdict per PR, its reason codes, and the
cross-PR analyses nothing else looks at.

    analyze.py --in .pr-review-queue.json --out .pr-review-queue.json
               [--config ~/.pr-review.yml] [--include-infra] [--strict-stances]
               [--owner me|any|@user|<role>] [--domain docs,blog] [--verdict stamp,judge]
               [--judgments .pr-review-judgments.json]

Per PR: `domains` (classify_path via routing.resolve_lanes), the owning
role/team per domain, `verdict` ∈ {stamp, judge, route, blocked}, a
`reasons` list of machine-readable codes (`code[:detail]`, closed vocabulary
in REASON_CODES), and `actions` — the `/pr-review --act …` fragments that
apply to the row.

Cross-PR: collision clusters (union-find over shared paths; a pair is
`overlap` when hunks intersect on the base side, else `same-file`),
directional conflicts (a PR adding links to a URL that exists only as a
Hugo `aliases:` entry while another open PR removes links from it),
duplicate candidates (shared file, similar title, opened within 10
minutes), stale blog dates, self-accepted findings (REVIEW_STATE actor ==
PR author), stale reviews (reviewed SHA not a prefix of head), and stale
brief summaries (a "What this PR changes" bullet naming a value the current
diff no longer contains).

The stamp bar (every gate required):
  label review:no-blockers · zero ⚠️ rows (zero low-confidence on legacy)
  · no self-accepted disposition · review CURRENT · mergeable_state in
  {clean, blocked} with checks green · no overlap collision, directional
  conflict or duplicate · one of the PR's domains is mine · no new file
  under content/blog/ · no layouts/ or .github/ change unless
  --include-infra · changed lines under stamp_max_lines · scrutiny not
  heightened · (with --strict-stances) no editorial stances.
Verdict precedence: blocked > route > stamp/judge. Heightened scrutiny
caps a row at judge.

`--judgments FILE` merges the model's judge output (`judgments[]`,
`fix_draft`, `recommended`) into the matching rows. It never lowers a
verdict below what this script computed; the model only adds the
judgment call. Deterministic, no model calls.
"""

from __future__ import annotations

import argparse
import difflib
import importlib.util
import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_HERE))
import pr_review_config  # noqa: E402
import routing  # noqa: E402
import sentinel  # noqa: E402
from gh_client import norm_login  # noqa: E402

_compose = sentinel._compose
VERDICTS = ("stamp", "judge", "route", "blocked")
STAMP_STATES = ("clean", "blocked")
BLOG_NEW_RE = re.compile(r"^content/blog/")
INFRA_SHAPE_RE = re.compile(r"^(layouts/|\.github/)")
DUPLICATE_WINDOW = timedelta(minutes=10)
DUPLICATE_TITLE_RATIO = 0.8
CONTEXT_LINES = 3
CROSS_CODE_CAP = 6

# code -> meaning; the detail after ':' is free text. Rendered as chips.
REASON_CODES = {
    "risk": "risk tier from the diff shape (typo/minor/standard/major/infra)",
    "scrutiny": "heightened content scrutiny (AI-suspect) — caps at judge",
    "ai-suspect": "which AI-suspect signal fired",
    "review": "pinned review status when not CURRENT (stale/absent/in-progress/error/triage-prose)",
    "label": "the review:* state label",
    "warnings": "⚠️ reviewer-check rows still open on the brief (legacy: low-confidence)",
    "outstanding": "🚨/❓ rows still open on the author card",
    "self-accepted": "a REVIEW_STATE disposition recorded by the PR author",
    "stances": "the brief lists editorial stances (blocks only with --strict-stances)",
    "mergeable": "GitHub mergeable_state when not clean/blocked",
    "checks": "check rollup when not green",
    "collision": "another open PR touches the same path (overlap = hunks intersect)",
    "directional": "adds links to an alias-only URL another open PR removes links from",
    "duplicate": "looks like a duplicate of another open PR",
    "blog": "new post, or a stale publish date",
    "brief": "a 'What this PR changes' bullet names a value absent from the diff",
    "desc": "PR description names a path not in the diff, or is empty",
    "shape": "touches layouts/ or .github/ (needs --include-infra to stamp)",
    "size": "changed lines at or over stamp_max_lines",
    "owner": "the PR's domains and their owning roles",
    "route": "the lane this PR should go to",
    "handed-off": "a human reviewer who isn't me is requested; the row waits on them",
    "merging-over": "an approval or changes-requested review already on the PR",
    "not-governed": "the Sentinel does not gate this PR",
    "author": "author type when human",
    "trust": "membership could not be read",
    "draft": "draft PR (only reachable with an explicit --pr)",
}


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_frontmatter_validate = None


def frontmatter_validate():
    global _frontmatter_validate
    if _frontmatter_validate is None:
        _frontmatter_validate = _load(
            "analyze_frontmatter_validate",
            _REPO_ROOT / ".claude" / "commands" / "docs-review" / "scripts" / "frontmatter-validate.py",
        )
    return _frontmatter_validate


# ---- hunks ---------------------------------------------------------------

HUNK_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def parse_hunks(patch: str | None) -> list[dict]:
    """[{old_start, old_len, new_start, new_len, added:[(new_lineno, text)],
    removed:[(old_lineno, text)]}] from a GitHub `patch` field (hunks only,
    no `diff --git` header)."""
    hunks: list[dict] = []
    cur = None
    old_no = new_no = 0
    for line in (patch or "").splitlines():
        m = HUNK_RE.match(line)
        if m:
            cur = {
                "old_start": int(m.group(1)), "old_len": int(m.group(2) or 1),
                "new_start": int(m.group(3)), "new_len": int(m.group(4) or 1),
                "added": [], "removed": [],
            }
            old_no, new_no = cur["old_start"], cur["new_start"]
            hunks.append(cur)
            continue
        if cur is None or line.startswith("\\"):
            continue
        if line.startswith("+"):
            cur["added"].append((new_no, line[1:]))
            new_no += 1
        elif line.startswith("-"):
            cur["removed"].append((old_no, line[1:]))
            old_no += 1
        else:
            old_no += 1
            new_no += 1
    return hunks


def base_ranges(patch: str | None) -> list[tuple[int, int]] | None:
    """Base-side (old) line ranges a patch changes, context trimmed; None
    when there is no patch (binary or too large: whole file)."""
    if not patch:
        return None
    out = []
    for h in parse_hunks(patch):
        lo = h["old_start"] + CONTEXT_LINES if h["old_start"] > 1 else h["old_start"]
        hi = h["old_start"] + max(h["old_len"], 1) - 1
        hi = hi - CONTEXT_LINES if hi > lo else hi
        if hi < lo:
            lo = hi = h["old_start"] + max(h["old_len"], 1) // 2
        out.append((lo, hi))
    return out


def ranges_overlap(a: list[tuple[int, int]] | None, b: list[tuple[int, int]] | None) -> bool:
    if a is None or b is None:
        return True  # a whole-file change overlaps anything
    return any(x0 <= y1 and y0 <= x1 for x0, x1 in a for y0, y1 in b)


# ---- links -----------------------------------------------------------------

LINK_RE = re.compile(r"\]\((/[^)\s#?]+)|href=\"(/[^\"#?]+)\"")


def links_in(lines: list[str]) -> set[str]:
    out = set()
    for line in lines:
        for m in LINK_RE.finditer(line):
            out.add(_norm_path((m.group(1) or m.group(2))))
    return out


def _norm_path(p: str) -> str:
    p = p.strip().lower()
    if not p.endswith("/") and "." not in p.rsplit("/", 1)[-1]:
        p += "/"
    return p


def added_removed_lines(pr: dict) -> tuple[list[str], list[str]]:
    added, removed = [], []
    for f in pr.get("files") or []:
        for h in parse_hunks(f.get("patch")):
            added += [t for _, t in h["added"]]
            removed += [t for _, t in h["removed"]]
    return added, removed


def alias_only_urls(repo_root: Path) -> set[str]:
    """Every URL some content file declares under `aliases:` (Hugo only —
    S3 redirects are a different mechanism and never a link target)."""
    try:
        _, _, ownership = frontmatter_validate().build_global_maps(repo_root)
    except Exception:  # noqa: BLE001 — a broken tree map degrades to "no alias data"
        return set()
    return {_norm_path(url) for url, owners in ownership.items() if any(o.get("scope") == "hugo-alias" for o in owners)}


# ---- cross-PR --------------------------------------------------------------


def collision_clusters(prs: list[dict]) -> list[dict]:
    by_path: dict[str, list[int]] = {}
    ranges: dict[tuple[int, str], list | None] = {}
    lines: dict[int, int] = {}
    for pr in prs:
        lines[pr["number"]] = pr.get("changed_lines") or 0
        for f in pr.get("files") or []:
            by_path.setdefault(f["path"], []).append(pr["number"])
            ranges[(pr["number"], f["path"])] = base_ranges(f.get("patch"))
    parent: dict[int, int] = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    pairs: dict[tuple[int, int], dict] = {}
    for path, members in by_path.items():
        members = sorted(set(members))
        if len(members) < 2:
            continue
        for i, a in enumerate(members):
            for b in members[i + 1:]:
                union(a, b)
                kind = "overlap" if ranges_overlap(ranges[(a, path)], ranges[(b, path)]) else "same-file"
                p = pairs.setdefault((a, b), {"a": a, "b": b, "kind": "same-file", "paths": []})
                p["paths"].append(path)
                if kind == "overlap":
                    p["kind"] = "overlap"
    groups: dict[int, set[int]] = {}
    for (a, b) in pairs:
        groups.setdefault(find(a), set()).update((a, b))
    clusters = []
    for i, members in enumerate(sorted(groups.values(), key=lambda s: min(s)), 1):
        ms = sorted(members)
        cpairs = [p for (a, b), p in sorted(pairs.items()) if a in members and b in members]
        paths = sorted({p for pr in cpairs for p in pr["paths"]})
        order = sorted(ms, key=lambda n: (lines[n], n))
        clusters.append({
            "id": f"C{i}", "prs": ms, "paths": paths, "pairs": cpairs,
            "kind": "overlap" if any(p["kind"] == "overlap" for p in cpairs) else "same-file",
            "merge_order": order,
        })
    return clusters


def directional_conflicts(prs: list[dict], aliases: set[str]) -> list[dict]:
    adds: dict[int, set[str]] = {}
    rems: dict[int, set[str]] = {}
    for pr in prs:
        a, r = added_removed_lines(pr)
        adds[pr["number"]] = links_in(a) & aliases
        rems[pr["number"]] = links_in(r) & aliases
    out = []
    for na, urls in adds.items():
        for url in sorted(urls):
            for nb, removed in rems.items():
                if nb != na and url in removed:
                    out.append({"path": url, "adds_links_pr": na, "removes_links_pr": nb})
    return out


def _dt(s: str | None) -> datetime | None:
    if not s:
        return None
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def duplicate_candidates(prs: list[dict]) -> list[dict]:
    out = []
    for i, a in enumerate(prs):
        for b in prs[i + 1:]:
            shared = {f["path"] for f in a.get("files") or []} & {f["path"] for f in b.get("files") or []}
            if not shared:
                continue
            ratio = difflib.SequenceMatcher(None, (a.get("title") or "").lower(), (b.get("title") or "").lower()).ratio()
            ta, tb = _dt(a.get("created_at")), _dt(b.get("created_at"))
            if ratio >= DUPLICATE_TITLE_RATIO and ta and tb and abs(ta - tb) <= DUPLICATE_WINDOW:
                older, newer = (a, b) if a["number"] < b["number"] else (b, a)
                out.append({"newer": newer["number"], "older": older["number"], "title_ratio": round(ratio, 2),
                            "minutes_apart": round(abs(ta - tb).total_seconds() / 60, 1), "shared_files": sorted(shared)})
    return out


# ---- per PR ----------------------------------------------------------------

# Backticked spans, versions, and 3+ digit numbers. Quoted prose is left
# alone: a bullet paraphrases, and the diff quotes the page.
TOKEN_RE = re.compile(r"`([^`]+)`|\b(\d+(?:\.\d+)+|\d{3,})\b")
PLACEHOLDER_RE = re.compile(r"\.\.\.|…|<[^>]+>|\*$")
# Repo-relative paths only: a body that names `scripts/lint.sh` as the check
# it ran is not claiming to have changed it, and an external repo's README
# is not this diff's business.
REPO_DIRS = ("content/", "static/", "data/", "layouts/", "assets/", "theme/", "config/", ".github/", "infrastructure/")
PATHISH_RE = re.compile(r"`?((?:content|static|data|layouts|assets|theme|config|\.github|infrastructure)/(?:[\w.-]+/)*[\w.-]+\.(?:md|ya?ml|py|sh|js|ts|mjs|json|scss|html|toml|png|svg))`?")


def stale_brief_tokens(bullets: list[str], pr: dict) -> list[str]:
    """Tokens named by the brief's change bullets that the current diff no
    longer contains: backticked spans, quoted spans, versions and numbers,
    checked case-insensitively against the added lines and the file paths."""
    added, removed = added_removed_lines(pr)
    haystack = "\n".join(added + removed + [f["path"] for f in pr.get("files") or []]).lower()
    stale = []
    for b in bullets:
        if "TODO" in b:
            continue
        for m in TOKEN_RE.finditer(b):
            tok = next(g for g in m.groups() if g)
            if PLACEHOLDER_RE.search(tok) or len(tok) < 3:
                continue
            if tok.lower() not in haystack and tok not in stale:
                stale.append(tok)
    return stale


def desc_findings(pr: dict) -> list[str]:
    body = pr.get("body") or ""
    text = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    text = re.sub(r"^#+ .*$", "", text, flags=re.M)
    text = re.sub(r"^(🤖 Generated with|https://claude\.ai/code/).*$", "", text, flags=re.M)
    reasons = []
    if len(text.strip()) < 20:
        reasons.append("desc:empty")
    paths = {f["path"] for f in pr.get("files") or []} | {f.get("previous_filename") for f in pr.get("files") or [] if f.get("previous_filename")}
    for m in PATHISH_RE.finditer(body):
        p = m.group(1)
        if p not in paths and not any(path.endswith(p) or p.endswith(path) for path in paths):
            code = f"desc:stale:path:{p}"
            if code not in reasons:
                reasons.append(code)
    return reasons


def self_accepted(pr: dict) -> list[str]:
    state = (pr.get("review") or {}).get("review_state") or {}
    author = norm_login((pr.get("author") or {}).get("login"))
    out = []
    for fid, entry in sorted((state.get("findings") or {}).items()):
        if norm_login(entry.get("actor")) == author and entry.get("disposition") != "fixed":
            out.append(fid)
    return out


def open_warnings(pr: dict) -> list[str]:
    """⚠️ rows (v3 brief) or low-confidence items (legacy) with no disposition."""
    review = pr.get("review") or {}
    items = review.get("items") or []
    disposed = {i["id"] for i in items if i.get("disposition")}
    if review.get("surface") == "v3":
        return [w["id"] for w in review.get("warning_rows") or [] if w["id"] not in disposed]
    return [i["id"] for i in items if i.get("bucket") == "low" and not i.get("disposition")]


def open_blockers(pr: dict) -> list[str]:
    items = (pr.get("review") or {}).get("items") or []
    return [i["id"] for i in items if i.get("blocking") and not i.get("disposition")]


def latest_reviews(pr: dict) -> dict[str, str]:
    latest: dict[str, str] = {}
    for r in sorted(pr.get("reviews") or [], key=lambda r: r.get("submitted_at") or ""):
        if (r.get("user_type") or "") == "Bot" or r.get("state") in ("COMMENTED", "PENDING", "DISMISSED"):
            continue
        latest[r["user"]] = r["state"]
    return latest


def domains_and_owner(pr: dict, config: routing.Config) -> dict:
    files = [{"filename": f["path"], "patch": f.get("patch"), "status": f.get("status"),
              "previous_filename": f.get("previous_filename")} for f in pr.get("files") or []]
    detail = {"additions": pr.get("additions") or 0, "deletions": pr.get("deletions") or 0}
    mechanical, claims, _ = sentinel._mechanical_and_claims(detail, files, set(pr.get("labels") or []))
    res = routing.resolve_lanes([f["filename"] for f in files], mechanical, claims, config)
    change_type = "mechanical" if (mechanical and not claims) else "substantive"
    domains = sorted(set(res.subjects.values()))
    owners = {}
    for d in domains:
        role = config.matrix[d][change_type]
        if role == "none":
            role = config.matrix[d]["substantive"]
        owners[d] = {"role": role, "team": config.teams.get(role), "person": (config.sla.get(role) or {}).get("escalate_to")}
    return {"domains": domains, "owners": owners, "roles": sorted(res.roles), "mechanical": mechanical, "claims": claims,
            "staging_required": res.staging_evidence_required}


def team_lanes(slug: str, config: routing.Config) -> set[str]:
    """Lanes a requested team owns, via review-routing.yml (`teams:` maps a
    role to `org/slug`; the matrix maps subjects to roles)."""
    role = next((r for r, full in config.teams.items() if full.split("/", 1)[-1] == slug or full == slug), None)
    if role is None:
        return set()
    return {d for d, cell in config.matrix.items() if role in (cell.get("mechanical"), cell.get("substantive"))}


def handed_off_to(pr: dict, approver: str | None, config: routing.Config, me: list[str]) -> list[str]:
    """Who this PR is waiting on, when it is not me: the requested human
    reviewers and teams that aren't the approver or one of the approver's
    lanes. Empty when the approver is among the requested reviewers, or when
    nobody is requested. Bots were already dropped by collect.py.

    The review request is the hand-off record: it lives on the PR, every
    session and machine sees it, and GitHub clears it when the reviewer
    acts, which is exactly when the row should come back."""
    rr = pr.get("requested_reviewers") or {}
    users = [u for u in rr.get("users") or [] if u]
    teams = [t for t in rr.get("teams") or [] if t]
    mine = norm_login(approver) if approver else ""
    if mine and any(norm_login(u) == mine for u in users):
        return []
    others = [f"@{u}" for u in users]
    others += [f"@{t}" for t in teams if not (set(me) & team_lanes(t, config))]
    return others


def lanes_for_owner(spec: str | None, config: routing.Config, me: list[str]) -> set[str] | None:
    """Which domains count as "mine" for `--owner`: me (default), any, a
    role name, or @login (the role whose sla.escalate_to is that person)."""
    if not spec or spec == "me":
        return set(me)
    if spec == "any":
        return None
    role = spec
    if spec.startswith("@"):
        who = spec[1:].lower()
        role = next((r for r, s in config.sla.items() if (s.get("escalate_to") or "").lower() == who), None)
        if role is None:
            return set()
    return {d for d, cell in config.matrix.items() if role in (cell.get("mechanical"), cell.get("substantive"))}


def analyze_pr(pr: dict, ctx: dict) -> None:
    """Mutates `pr`: domains/owners, reasons, verdict, actions."""
    cfg: pr_review_config.UserConfig = ctx["cfg"]
    config: routing.Config = ctx["config"]
    mine: set[str] | None = ctx["mine"]
    n = pr["number"]
    reasons: list[str] = []
    review = pr.get("review") or {}
    labels = set(pr.get("labels") or [])
    pr["handed_off_to"] = handed_off_to(pr, ctx.get("approver"), config, cfg.me)
    pr["handed_off"] = bool(pr["handed_off_to"])
    lanes = domains_and_owner(pr, config)
    pr.update(lanes)
    is_mine = mine is None or bool(set(lanes["domains"]) & mine)
    for d in lanes["domains"]:
        reasons.append(f"owner:{d}:{lanes['owners'][d]['role']}")

    blocked: list[str] = []      # (reason, action) pairs collapse into reasons + actions
    actions: list[dict] = []
    stamp_ok = True

    def gate_fail(code: str):
        nonlocal stamp_ok
        stamp_ok = False
        if code not in reasons:
            reasons.append(code)

    # -- trust / risk
    reasons.append(f"risk:{pr.get('risk_tier')}")
    if pr.get("scrutiny") == "heightened":
        gate_fail("scrutiny:heightened")
        for r in (pr.get("ai_suspect") or {}).get("reasons") or []:
            reasons.append(f"ai-suspect:{r}")
    author = pr.get("author") or {}
    if author.get("type") != "bot":
        reasons.append(f"author:{author.get('type')}")
    if author.get("membership_note"):
        reasons.append("trust:membership-unreadable")
    if pr.get("draft"):
        reasons.append("draft")
        blocked.append("draft")
    if pr["handed_off"]:
        reasons.append("handed-off:" + ",".join(pr["handed_off_to"]))

    # -- review surface
    status = review.get("status") or "ABSENT"
    for l in sorted(labels):
        if l.startswith("review:"):
            reasons.append(f"label:{l}")
    if status != "CURRENT":
        reasons.append(f"review:{status.lower().replace('_', '-')}")
        stamp_ok = False
    if status == "STALE":
        blocked.append("review:stale")
        actions.append({"id": "refresh", "label": "refresh review", "cmd": f"--refresh {n}"})
    elif status in ("IN_PROGRESS", "ERROR"):
        blocked.append(f"review:{status.lower().replace('_', '-')}")
    if "review:no-blockers" not in labels:
        stamp_ok = False
    blockers = open_blockers(pr)
    if blockers:
        gate_fail(f"outstanding:{len(blockers)}:{','.join(blockers)}")
    warnings = open_warnings(pr)
    if warnings:
        gate_fail(f"warnings:{len(warnings)}:{','.join(warnings)}")
    for fid in self_accepted(pr):
        gate_fail(f"self-accepted:{fid}")
    if review.get("stances"):
        reasons.append("stances:present")
        if ctx["strict_stances"]:
            stamp_ok = False

    # -- merge state
    ms = pr.get("mergeable_state") or "unknown"
    if ms not in STAMP_STATES:
        gate_fail(f"mergeable:{ms}")
        if ms == "dirty":
            blocked.append("mergeable:dirty")
            actions.append({"id": "unblock", "label": "merge base & retry", "cmd": f"--unblock {n}"})
        elif ms == "behind":
            actions.append({"id": "unblock", "label": "merge base", "cmd": f"--unblock {n}"})
    checks = pr.get("checks") or {}
    if checks.get("state") != "green":
        gate_fail(f"checks:{checks.get('state')}:{','.join((checks.get('failing') or checks.get('pending') or [])[:3])}")
        if checks.get("state") == "red":
            blocked.append("checks:red")
    for user, state in latest_reviews(pr).items():
        if state == "CHANGES_REQUESTED":
            gate_fail(f"merging-over:changes-requested:{user}")
            blocked.append("changes-requested")
        elif state == "APPROVED":
            reasons.append(f"merging-over:approved-by:{user}")

    # -- shape
    for f in pr.get("files") or []:
        if f.get("status") == "added" and BLOG_NEW_RE.match(f["path"]):
            gate_fail("blog:new-post")
            break
    if any(INFRA_SHAPE_RE.match(f["path"]) for f in pr.get("files") or []):
        reasons.append("shape:infra")
        if not ctx["include_infra"]:
            stamp_ok = False
    if (pr.get("changed_lines") or 0) >= cfg.stamp_max_lines:
        gate_fail(f"size:{pr.get('changed_lines')}>={cfg.stamp_max_lines}")
    for f in pr.get("files") or []:
        d = f.get("blog_date")
        # Only a date this PR sets — a new post, or a `date:` line in the
        # diff — can be stale. A link fix in a 2024 post is not a backdate.
        sets_date = f.get("status") == "added" or re.search(r"^\+date:", f.get("patch") or "", re.M)
        if d and sets_date:
            day = _day(d)
            if day and (ctx["today"] - day).days > cfg.stale_date_days:
                gate_fail(f"blog:stale-date:{day.isoformat()}")
    for tok in stale_brief_tokens(review.get("brief_summary_bullets") or [], pr)[:3]:
        reasons.append(f"brief:stale-summary:{tok}")
    reasons.extend(desc_findings(pr))
    ng = routing.not_governed_reason(config, author.get("login") or "", labels)
    if ng:
        reasons.append("not-governed")

    # -- cross-PR (filled by analyze(); read here). Capped: a link-sweep PR
    # can collide with twenty others, and the cluster card carries the rest.
    # A collision with a PR that is handed off to someone else is advisory
    # (`:theirs`): if mine merges first, the conflict is theirs to resolve;
    # it neither gates my stamp nor pins the cluster for me.
    cross_codes = [c + ":theirs" if _other_pr(c) in ctx["handed_off"] else c for c in ctx["cross"].get(n, [])]
    shown = cross_codes[:CROSS_CODE_CAP]
    for code in cross_codes:
        if code not in shown:
            if code.startswith(("collision:", "directional:", "duplicate:")) and not code.endswith((":same-file", ":theirs")):
                stamp_ok = False
            continue
        reasons.append(code)
        if code.startswith(("collision:", "directional:", "duplicate:")) and not code.endswith((":same-file", ":theirs")):
            stamp_ok = False
        if code.startswith("duplicate:") and not code.endswith(":theirs"):
            other = code.split(":")[1].lstrip("#")
            actions.append({"id": "close", "label": f"close as duplicate of #{other}", "cmd": f"--close {n} --superseded-by {other}"})
    if len(cross_codes) > CROSS_CODE_CAP:
        reasons.append(f"collision:+{len(cross_codes) - CROSS_CODE_CAP}-more")

    # -- ownership / verdict
    if not is_mine:
        route = next((lanes["owners"][d] for d in lanes["domains"] if mine is not None and d not in mine), None)
        if route:
            target = f"@{route['person']}" if route.get("person") else f"@{route['team']}"
            reasons.append(f"route:{route['role']}")
            actions.append({"id": "route", "label": f"request review from {target}", "cmd": f"--route {n}:{target}"})
    if blocked:
        verdict = "blocked"
    elif not is_mine:
        verdict = "route"
    elif stamp_ok:
        verdict = "stamp"
    else:
        verdict = "judge"
    if verdict == "stamp":
        actions.insert(0, {"id": "stamp", "label": "approve & merge", "cmd": f"--stamp {n}"})
    elif verdict == "judge":
        actions.insert(0, {"id": "stamp", "label": "approve as-is", "cmd": f"--stamp {n} --force"})
        if pr.get("risk_tier") == "infra":
            actions.append({"id": "deploy", "label": "deploy to pulumi-test.io", "cmd": f"--deploy {n}"})
        if pr.get("one_click_suggestions") or any(r.startswith("desc:") for r in reasons):
            actions.append({"id": "fix", "label": "apply fixes", "cmd": f"--fix {n}"})
        if (pr.get("preview") or {}).get("pages"):
            actions.append({"id": "render", "label": "render preview", "cmd": f"--render {n}"})
    pr["blockers"] = blocked
    pr["is_mine"] = is_mine
    pr["verdict"] = verdict
    pr["reasons"] = reasons
    pr["actions"] = actions
    pr["open_warning_ids"] = warnings
    pr["open_blocker_ids"] = blockers
    pr["self_accepted_ids"] = self_accepted(pr)
    pr.setdefault("judgments", [])
    pr.setdefault("fix_draft", None)
    pr["summary"] = one_line_summary(pr)


def _other_pr(code: str) -> int | None:
    m = re.match(r"^(?:collision|directional|duplicate):#(\d+)", code)
    return int(m.group(1)) if m else None


def _day(s: str) -> date | None:
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).date()
    except ValueError:
        try:
            return datetime.strptime(s[:10], "%Y-%m-%d").date()
        except ValueError:
            return None


def one_line_summary(pr: dict) -> str:
    """The brief's italic one-sentence orientation line when present, else
    the first non-empty body line, else the title."""
    body = (pr.get("review") or {}).get("author_body") or ""
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("_") and s.endswith("_") and len(s) > 2 and "TODO" not in s:
            return s.strip("_")
    for line in (pr.get("body") or "").splitlines():
        s = line.strip()
        if s and not s.startswith(("#", "<!--", "-", "|", "🤖", "http")):
            return s[:200]
    return pr.get("title") or ""


# ---- queue ------------------------------------------------------------------


def analyze(queue: dict, cfg: pr_review_config.UserConfig, *, config: routing.Config,
            repo_root: Path = _REPO_ROOT, include_infra: bool = False, strict_stances: bool = False,
            owner: str | None = None, aliases: set[str] | None = None, today: date | None = None) -> dict:
    prs = queue.get("prs") or []
    if aliases is None:
        aliases = alias_only_urls(repo_root)
    clusters = collision_clusters(prs)
    directional = directional_conflicts(prs, aliases)
    duplicates = duplicate_candidates(prs)
    cross: dict[int, list[str]] = {}
    for c in clusters:
        for p in c["pairs"]:
            suffix = "" if p["kind"] == "overlap" else ":same-file"
            cross.setdefault(p["a"], []).append(f"collision:#{p['b']}{suffix}")
            cross.setdefault(p["b"], []).append(f"collision:#{p['a']}{suffix}")
    for d in directional:
        cross.setdefault(d["adds_links_pr"], []).append(f"directional:#{d['removes_links_pr']}:{d['path']}")
    for d in duplicates:
        cross.setdefault(d["newer"], []).append(f"duplicate:#{d['older']}")
    approver = queue.get("approver")
    handed = {p["number"] for p in prs if handed_off_to(p, approver, config, cfg.me)}
    ctx = {
        "cfg": cfg, "config": config, "mine": lanes_for_owner(owner, config, cfg.me),
        "include_infra": include_infra, "strict_stances": strict_stances, "cross": cross,
        "today": today or datetime.now(timezone.utc).date(), "approver": approver, "handed_off": handed,
    }
    for pr in prs:
        analyze_pr(pr, ctx)
    for c in clusters:
        c["handed_off"] = [n for n in c["prs"] if n in handed]
        c["mine"] = [n for n in c["prs"] if n not in handed]
        c["merge_order"] = [n for n in c["merge_order"] if n not in handed]
    for d in directional:
        d["theirs"] = d["adds_links_pr"] in handed or d["removes_links_pr"] in handed
    queue["clusters"] = clusters
    queue["directional"] = directional
    queue["duplicates"] = duplicates
    queue["config"] = {**cfg.to_json(), "include_infra": include_infra, "strict_stances": strict_stances, "owner": owner or "me"}
    queue["counts"] = {v: sum(1 for p in prs if p.get("verdict") == v and not p.get("handed_off")) for v in VERDICTS}
    queue["counts"]["handed-off"] = sum(1 for p in prs if p.get("handed_off"))
    queue["analyzed_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    queue["reason_codes"] = REASON_CODES
    return queue


def apply_filters(queue: dict, *, domains: list[str] | None = None, verdicts: list[str] | None = None,
                  authors: list[str] | None = None) -> dict:
    """Drop rows outside the requested domains/verdicts/authors. Cross-PR
    facts were computed over the full set and are kept as-is."""
    keep = []
    want_auth = {norm_login(a) for a in (authors or []) if a and a != "any"}
    for pr in queue.get("prs") or []:
        if domains and not (set(pr.get("domains") or []) & set(domains)):
            continue
        if verdicts and pr.get("verdict") not in verdicts:
            continue
        if want_auth and (pr.get("author") or {}).get("norm") not in want_auth:
            continue
        keep.append(pr)
    queue["prs"] = keep
    queue["filters"] = {**(queue.get("filters") or {}), "domain": domains or [], "verdict": verdicts or [], "author": authors or []}
    return queue


def merge_judgments(queue: dict, judgments: dict) -> dict:
    """Fold the model's judge output into the rows. Keys are PR numbers (as
    strings or ints); each value may carry `judgments` (list), `fix_draft`
    (dict) and `recommended` (verdict). A recommendation never lowers the
    computed verdict: blocked stays blocked, route stays route."""
    by = {p["number"]: p for p in queue.get("prs") or []}
    for key, val in (judgments or {}).items():
        try:
            n = int(key)
        except (TypeError, ValueError):
            continue
        pr = by.get(n)
        if not pr or not isinstance(val, dict):
            continue
        if isinstance(val.get("judgments"), list):
            pr["judgments"] = val["judgments"]
        if isinstance(val.get("fix_draft"), dict):
            pr["fix_draft"] = val["fix_draft"]
            if not any(a["id"] == "fix" for a in pr.get("actions") or []):
                pr["actions"].append({"id": "fix", "label": "apply fixes", "cmd": f"--fix {n}"})
        rec = val.get("recommended")
        if rec in VERDICTS and pr.get("verdict") == "judge":
            pr["recommended"] = rec
    return queue


# ---- CLI --------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--in", dest="inp", default=".pr-review-queue.json")
    ap.add_argument("--out", default=None, help="default: overwrite --in")
    ap.add_argument("--config", help="~/.pr-review.yml path")
    ap.add_argument("--routing", default=str(routing.DEFAULT_CONFIG_PATH))
    ap.add_argument("--include-infra", action="store_true")
    ap.add_argument("--strict-stances", action="store_true")
    ap.add_argument("--owner", default="me", help="me | any | <role> | @login")
    ap.add_argument("--domain", help="comma list to keep")
    ap.add_argument("--verdict", help="comma list to keep")
    ap.add_argument("--author", help="comma list to keep (any App spelling)")
    ap.add_argument("--judgments", help="merge this judge-output JSON")
    ap.add_argument("--no-aliases", action="store_true", help="skip the content-tree alias map (directional conflicts)")
    ap.add_argument("--self-test", action="store_true")
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.self_test:
        import test_analyze  # noqa: PLC0415 — the pytest file doubles as the harness
        return test_analyze.run_standalone()
    queue = json.loads(Path(args.inp).read_text())
    cfg = pr_review_config.load_user_config(args.config)
    for w in cfg.warnings:
        print(f"config: {w}", file=sys.stderr)
    config = routing.load_config(args.routing)
    queue = analyze(queue, cfg, config=config, include_infra=args.include_infra, strict_stances=args.strict_stances,
                    owner=args.owner, aliases=set() if args.no_aliases else None)
    if args.judgments:
        queue = merge_judgments(queue, json.loads(Path(args.judgments).read_text()))
    split = lambda s: [x.strip() for x in s.split(",") if x.strip()] if s else None  # noqa: E731
    queue = apply_filters(queue, domains=split(args.domain), verdicts=split(args.verdict), authors=split(args.author))
    out = Path(args.out or args.inp)
    out.write_text(json.dumps(queue, indent=1, sort_keys=True) + "\n")
    c = queue["counts"]
    print(f"analyzed {len(queue['prs'])} PR(s): {c['stamp']} stamp · {c['judge']} judge · {c['route']} route · {c['blocked']} blocked → {out}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
