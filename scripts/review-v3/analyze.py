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
from dataclasses import replace
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
CROSS_CODE_CAP = 6

# code -> meaning; the detail after ':' is free text. Rendered as chips.
def merges_on_stamp(pr: dict) -> bool:
    """Does approving this row also merge it? A bot PR exists to be merged,
    so it does; a person's PR is theirs to merge, so approval stops there
    (act.py applies the same rule, and the row's second button flips it)."""
    return (pr.get("author") or {}).get("type") == "bot"


def stamp_actions(pr: dict, n: int, *, force: bool = False, base: str = "approve") -> list[dict]:
    """Two buttons, so a row never hides what approving does: the default
    first, the other way second. `:merge` / `:no-merge` is a per-PR override
    act.py reads, so a mixed batch stays one command."""
    f = " --force" if force else ""
    if merges_on_stamp(pr):
        return [{"id": "stamp", "label": f"{base} & merge", "cmd": f"--stamp {n}{f}"},
                {"id": "stamp-no-merge", "label": f"{base}, don't merge", "cmd": f"--stamp {n}:no-merge{f}"}]
    return [{"id": "stamp", "label": f"{base}, no merge", "cmd": f"--stamp {n}{f}"},
            {"id": "stamp-merge", "label": f"{base} & merge", "cmd": f"--stamp {n}:merge{f}"}]


def can_revise(pr: dict) -> bool:
    """collect.py stamps `author.can_revise`; older queues fall back to the
    author type, where every bot but an agent is a workflow."""
    a = pr.get("author") or {}
    if "can_revise" in a:
        return bool(a["can_revise"])
    return a.get("type") != "bot"


REASON_CODES = {
    "risk": "risk tier from the diff shape (typo/minor/standard/major/infra)",
    "scrutiny": "heightened content scrutiny (AI-suspect) — caps at judge",
    "ai-suspect": "which AI-suspect signal fired",
    "review": "pinned review status when not CURRENT (stale/absent/in-progress/error/triage-prose); base-merged: the head moved only by merging the base, so the reviewed diff still stands",
    "label": "the review:* state label",
    "warnings": "⚠️ reviewer-check rows still open on the brief (legacy: low-confidence)",
    "outstanding": "🚨/❓ rows still open on the author card",
    "self-accepted": "a REVIEW_STATE disposition recorded by the PR author",
    "stances": "the brief lists editorial stances (blocks only with --strict-stances)",
    "mergeable": "GitHub mergeable_state when not clean/blocked",
    "checks": "check rollup when not green",
    "cluster": "member of a collision cluster: overlap (hunks intersect; position in the merge order), same-file (any order), or theirs",
    "directional": "adds links to an alias-only URL another open PR removes links from",
    "duplicate": "looks like a duplicate of another open PR",
    "blog": "new post, or a stale publish date",
    "brief": "a 'What this PR changes' bullet names a value absent from the diff",
    "desc": "PR description names a path not in the diff, or is empty",
    "shape": "infra: touches layouts/ or .github/ (needs --include-infra to stamp); link-only: every changed line differs only in a link",
    "link-fixes": "mine: a link-only diff bypassed the lane check (`link_fixes: mine` in ~/.pr-review.yml)",
    "gate": "none: the routing matrix requires no team approval for this change; any-team: a link-only sweep, which any review team may approve, so the row is any approver's either way",
    "size": "changed lines at or over stamp_max_lines",
    "owner": "the PR's domains and their owning roles",
    "route": "the lane this PR should go to; `no-team`: GitHub says the lane's team doesn't exist, so the SLA person is the target; `team-unverified`: the token couldn't read teams, so the config's team is used unchecked",
    "handed-off": "a human reviewer who isn't me is requested; the row waits on them",
    "merging-over": "an approval or changes-requested review already on the PR",
    "not-governed": "the Sentinel does not gate this PR",
    "author": "author type when human; `generated`: a workflow opened this PR and cannot answer a review, so the row closes rather than goes back",
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


def touched_lines(patch: str | None) -> set[int] | None:
    """Base-side line numbers a patch changes: every removed line, and for a
    pure insertion the two lines it lands between. None when there is no
    patch (binary or too large: whole file). This is what git conflicts on,
    not the hunk's span: two edits inside one hunk that leave a line between
    them merge cleanly, so a range-based rule over-flags (PR pairs that
    merged a minute apart) and under-flags (edits on neighbouring lines in
    different hunks, which git rejects)."""
    if not patch:
        return None
    out: set[int] = set()
    for h in parse_hunks(patch):
        if h["removed"]:
            out.update(ln for ln, _ in h["removed"])
        else:
            out.update((h["old_start"], h["old_start"] + 1))
    return out


def lines_overlap(a: set[int] | None, b: set[int] | None) -> bool:
    """git's rule, near enough: changes conflict when they touch the same
    or adjacent base lines. Checked on the 2026-09-15 queue against the
    conflicts a real base merge produced (3 of 3 files, 0 false pairs)."""
    if a is None or b is None:
        return True  # a whole-file change overlaps anything
    return any(x in b or x - 1 in b or x + 1 in b for x in a)


# ---- links -----------------------------------------------------------------

LINK_RE = re.compile(r"\]\((/[^)\s#?]+)|href=\"(/[^\"#?]+)\"")


# A whole markdown link (text and target), an href, a bare URL, or a bare
# site path — everything a redirect sweep is allowed to rewrite.
# The link-only bar lives in sentinel.py, because the merge gate and the
# queue have to agree on what a link sweep is: the Sentinel uses it to
# decide that any review team may approve one, and the board renders it as
# `shape:link-only`.
link_only_diff = sentinel.link_only_diff
URL_TOKEN_RE = sentinel.URL_TOKEN_RE


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
            ranges[(pr["number"], f["path"])] = touched_lines(f.get("patch"))
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
                kind = "overlap" if lines_overlap(ranges[(a, path)], ranges[(b, path)]) else "same-file"
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
    pr.pop("recommended", None)  # a judgments merge re-adds it on judge rows; a stale one must not outlive a verdict change
    pr["handed_off_to"] = handed_off_to(pr, ctx.get("approver"), config, cfg.me)
    pr["handed_off"] = bool(pr["handed_off_to"])
    lanes = domains_and_owner(pr, config)
    pr.update(lanes)
    is_mine = mine is None or bool(set(lanes["domains"]) & mine)
    for d in lanes["domains"]:
        reasons.append(f"owner:{d}:{lanes['owners'][d]['role']}")
    # No required role at all: every subject's cell for this change type is
    # `none`, so the Sentinel asks for no team approval and there is nobody
    # to wait for. Routing it would be inventing a gate GitHub doesn't have,
    # so an ungated PR is any approver's to take.
    if not lanes["roles"]:
        reasons.append("gate:none")
        is_mine = True
    if link_only_diff(pr.get("files") or []):
        reasons.append("shape:link-only")
        # The routing config decides who may approve a link sweep. With
        # `link_only.approval: any-team` the Sentinel takes any review team,
        # so the row is genuinely anyone's and the board says so. Where the
        # lane still owns it, `link_fixes: mine` is the local override that
        # takes it anyway.
        if (config.link_only or {}).get("approval") == "any-team":
            reasons.append("gate:any-team")
            is_mine = True
        elif cfg.link_fixes == "mine" and not is_mine:
            is_mine = True
            reasons.append("link-fixes:mine")

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
    elif not can_revise(pr):
        reasons.append("author:generated")
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
    if review.get("base_merged"):
        reasons.append("review:base-merged")
    if status != "CURRENT":
        reasons.append(f"review:{status.lower().replace('_', '-')}")
        stamp_ok = False
    if status == "STALE":
        blocked.append("review:stale")
        actions.append({"id": "refresh", "label": "refresh review", "cmd": f"--refresh {n}"})
    elif status == "ERROR":
        # The pipeline's own escape hatch: `#new-review` clears the cards
        # and dispatches a fresh initial review, bypassing the skips.
        blocked.append("review:error")
        actions.append({"id": "rerun", "label": "re-run the review", "cmd": f"--rerun {n}"})
    elif status == "IN_PROGRESS":
        blocked.append("review:in-progress")
    elif status in ("ABSENT", "TRIAGE_PROSE"):
        # No review ran (trivial / frontmatter-only / draft / bot skip);
        # a full one is a side action the approver can ask for.
        actions.append({"id": "rerun", "label": "run a full review", "cmd": f"--rerun {n}"})
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
    # Cross-PR codes. A directional/duplicate pair with a PR that is handed
    # off to someone else is advisory (`:theirs`): if mine merges first, the
    # conflict is theirs to resolve. Cluster codes already carry their kind.
    cross_codes = [c + ":theirs" if (c.startswith(("directional:", "duplicate:")) and _other_pr(c) in ctx["handed_off"]) else c
                   for c in ctx["cross"].get(n, [])]
    directional_codes = [c for c in cross_codes if c.startswith("directional:")]
    other_codes = [c for c in cross_codes if not c.startswith("directional:")]
    shown = other_codes + directional_codes[:1]
    if len(directional_codes) > 1:
        shown.append(f"directional:+{len(directional_codes) - 1}-more")
    for code in cross_codes:
        gating = (code.startswith("cluster:") and ":overlap:" in code) or \
                 (code.startswith(("directional:", "duplicate:")) and not code.endswith(":theirs"))
        if gating:
            stamp_ok = False
        if code.startswith("duplicate:") and not code.endswith(":theirs"):
            other = code.split(":")[1].lstrip("#")
            actions.append({"id": "close", "label": f"close as duplicate of #{other}", "cmd": f"--close {n} --superseded-by {other}"})
    reasons.extend(shown)

    # -- ownership / verdict
    if not is_mine:
        route = next((lanes["owners"][d] for d in lanes["domains"] if mine is not None and d not in mine), None)
        if route:
            # The team when GitHub has it (collect.py asked), else the SLA
            # person; a team that lands later is picked up on the next run.
            team = route.get("team")
            known = (ctx.get("teams") or {}).get(team) if team else None
            if team and known is not False:
                # True: GitHub has it. None: the token can't read teams (403),
                # which is not evidence the team is missing — route to the team
                # the config names and say the check didn't run, rather than
                # quietly demoting every lane to its SLA person.
                target = f"@{team}"
                if known is None:
                    reasons.append("route:team-unverified")
            else:
                target = f"@{route['person']}" if route.get("person") else f"@{team}"
                if team:
                    reasons.append("route:no-team")
            reasons.append(f"route:{route['role']}")
            actions.append({"id": "route", "label": f"request review from {target}", "cmd": f"--route {n}:{target}"})
            # The lane is a default, not a lock: the approver can still take
            # the row. act.py accepts --force on any non-blocked verdict.
            actions.extend(stamp_actions(pr, n, force=True, base="approve anyway"))
    if blocked:
        verdict = "blocked"
    elif not is_mine:
        verdict = "route"
    elif stamp_ok:
        verdict = "stamp"
    else:
        verdict = "judge"
    if verdict == "stamp":
        for i, a in enumerate(stamp_actions(pr, n)):
            actions.insert(i, a)
    elif verdict == "judge":
        for i, a in enumerate(stamp_actions(pr, n, force=True, base="approve as-is")):
            actions.insert(i, a)
        if can_revise(pr):
            actions.insert(2, {"id": "request-changes", "label": "send back to author", "cmd": f"--request-changes {n}"})
        else:
            # pulumi-bot's lanes open the PR from a workflow run; there is no
            # author to send it back to. Fix it here or close it and let the
            # lane re-queue the page.
            actions.insert(2, {"id": "close", "label": "close it out", "cmd": f"--close {n}"})
        if pr.get("risk_tier") == "infra":
            actions.append({"id": "deploy", "label": "deploy to pulumi-test.io", "cmd": f"--deploy {n}"})
        if pr.get("one_click_suggestions") or any(r.startswith("desc:") for r in reasons):
            actions.append({"id": "fix", "label": "apply fixes", "cmd": f"--fix {n}"})
        if (pr.get("preview") or {}).get("pages"):
            actions.append({"id": "render", "label": "screenshot the preview", "cmd": f"--render {n}"})
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


CONSOLIDATE_SHARE = 0.6  # a cluster this dominated by one bot author's sweeps should be one PR


def cluster_recommendation(c: dict, by: dict[int, dict]) -> dict:
    """The one move a cluster asks of the approver, in words, with the
    action that does it: `ignore` (same-file only: any order works),
    `consolidate` (mostly one bot's overlapping sweeps: one request-changes
    beats N serial merges), or `chain` (merge the first, unblock the next)."""
    mine = c.get("mine") or []
    order = c.get("merge_order") or []
    if len(mine) <= 1:
        return {"kind": "theirs", "say": f"{c['id']}: waiting on others; nothing of yours to sequence.", "cmd": None}
    if c.get("kind") != "overlap":
        return {"kind": "ignore", "say": f"{c['id']}: {len(mine)} PRs share files but no hunks overlap; merge in any order.", "cmd": None}
    # Only members whose hunks actually overlap count toward a consolidation:
    # a same-file neighbour merges in any order and has nothing to fold in.
    degree: dict[int, int] = {}
    for p in c.get("pairs") or []:
        if p.get("kind") == "overlap" and p["a"] in mine and p["b"] in mine:
            degree[p["a"]] = degree.get(p["a"], 0) + 1
            degree[p["b"]] = degree.get(p["b"], 0) + 1
    # A leaf that overlaps one neighbour is a merge-order problem; only a
    # member entangled with two or more is a sweep worth folding together.
    overlapping = sorted(n for n, d in degree.items() if d >= 2)
    authors = [(by.get(n) or {}).get("author", {}).get("norm") for n in overlapping]
    top = max(set(authors), key=authors.count) if authors else None
    bots = sum(1 for n in overlapping if (by.get(n) or {}).get("author", {}).get("type") == "bot" and (by.get(n) or {}).get("author", {}).get("norm") == top)
    # A consolidation is an ask, so it needs an author who can answer one.
    # A workflow-authored pile falls through to the chain.
    answers = can_revise(by.get(max(overlapping)) or {}) if overlapping else False
    if top and answers and len(overlapping) >= 3 and bots / len(overlapping) >= CONSOLIDATE_SHARE:
        newest = max(overlapping)
        members = ", ".join(f"#{n}" for n in overlapping)
        reason = f"These {len(overlapping)} PRs edit overlapping lines in the same files ({members}); please consolidate them into one PR so they can merge without a chain of conflicts."
        return {"kind": "consolidate", "target": top, "on": newest,
                "say": f"{c['id']}: {len(overlapping)} overlapping sweeps by {top}. Ask for one consolidated PR instead of {len(overlapping)} serial merges.",
                "cmd": f"--request-changes {newest} --reason \"{reason}\""}
    first = next((n for n in order if (by.get(n) or {}).get("verdict") in ("stamp", "judge")), None)
    nxt = next((n for n in order if n != first), None)
    if first is None:
        return {"kind": "blocked", "say": f"{c['id']}: every member is blocked; unblock one to start.", "cmd": None}
    others = f" and {len(order) - 1} other{'s' if len(order) != 2 else ''}" if len(order) > 1 else ""
    say = (f"#{first}{others} edit the same lines in the same files, so they can only merge in order "
           f"(cluster {c['id']}, {len(order)} PRs).")
    return {"kind": "chain", "first": first, "next": nxt, "say": say, "cmd": f"--chain {c['id']}"}


def pr_list(nums: list[int], limit: int = 3) -> str:  # noqa: D401
    """`#1`, `#1 and #2`, `#1, #2 and #3`, `#1, #2 and 4 more` — a card names
    the PRs it will act on, because "3 rows" is not something you can check."""
    tags = [f"#{n}" for n in nums]
    if len(tags) > limit:
        return ", ".join(tags[:limit]) + f" and {len(tags) - limit} more"
    if len(tags) > 1:
        return ", ".join(tags[:-1]) + f" and {tags[-1]}"
    return tags[0] if tags else ""


def do_next(prs: list[dict], clusters: list[dict], directional: list[dict]) -> list[dict]:
    """The board's opening: at most a handful of moves, each one sentence of
    what is true, one sentence of what pressing the button does, and the PRs
    it does it to. Ordered by leverage: consolidations, chains, then the
    batches (send back / close / route / stamp).

    `targets` maps a PR to the row button the card would press, so the board
    can keep the card and the rows in agreement instead of letting a card and
    a contrary row decision both sit lit. A card with no `targets` (a chain,
    a consolidation) `claims` its PRs instead: picking a different decision on
    one of them puts the card out."""
    cards: list[dict] = []
    for c in clusters:
        r = c.get("recommendation") or {}
        if r.get("kind") == "chain":
            first, nxt = r.get("first"), r.get("next")
            # The chain is the two row buttons it would press: approve the
            # first link, unblock the next. Saying that in `targets` keeps the
            # card and those rows in agreement, the same as every other card.
            by_n = {p["number"]: p for p in prs}
            stamp = next((a["cmd"] for a in (by_n.get(first) or {}).get("actions") or [] if a["id"] == "stamp"), None)
            targets, claimed = {}, []
            if stamp:
                targets[str(first)] = stamp
            if nxt:
                # The follow-up only has a row button of its own once that row
                # is actually stuck. Until then it is a row this card covers,
                # not a row it presses -- and treating it as a target would
                # leave the card permanently unlit, since nothing could press
                # a button that is not there.
                unblock = next((a["cmd"] for a in (by_n.get(nxt) or {}).get("actions") or [] if a["id"] == "unblock"), None)
                if unblock:
                    targets[str(nxt)] = unblock
                else:
                    claimed.append(nxt)
            cmd = " ".join(list(targets.values()) + [f"--unblock {n}" for n in claimed])
            does = f"Approves and squash-merges #{first}" + (
                f", then merges master into #{nxt} so it can follow." if nxt else ".")
            cards.append({"kind": "chain", "cluster": c["id"], "say": r["say"], "does": does + " One link per run; the next one waits on CI.",
                          "cmd": cmd or r["cmd"],
                          "label": f"approve & merge #{first}",
                          "claims": claimed,
                          # The unblock is a consequence of the merge, not a
                          # separate choice, so the lead row button and this
                          # card are one decision pressed from two places.
                          "lead": str(first) if stamp else None,
                          "targets": targets})
        elif r.get("kind") == "consolidate":
            on = r.get("on")
            cards.append({"kind": "consolidate", "cluster": c["id"], "say": r["say"],
                          "does": f"Posts a changes-requested review on #{on} asking {r.get('target')} for one consolidated PR. Nothing merges.",
                          "cmd": r["cmd"], "label": f"send #{on} back", "claims": [on] if on else []})
    visible = [p for p in prs if not p.get("handed_off")]
    rejected = [p for p in visible if p.get("recommended") in ("request-changes", "close")]
    back = sorted(p["number"] for p in rejected if can_revise(p))
    if back:
        cards.append({"kind": "request-changes",
                      "say": f"{pr_list(back)} need{'' if len(back) != 1 else 's'} {'their' if len(back) != 1 else 'its'} author, not you.",
                      "does": "Posts a changes-requested review on each, written from the judgments on those rows, and labels them needs-author-response. Nothing merges.",
                      "cmd": " ".join(f"--request-changes {n}" for n in back),
                      "label": "send back" + (" all" if len(back) != 1 else ""),
                      "targets": {str(n): f"--request-changes {n}" for n in back}})
    # A workflow-authored row has nobody to send it back to: close it and the
    # lane re-queues the page on its next run.
    shut = sorted(p["number"] for p in rejected if not can_revise(p))
    if shut:
        cards.append({"kind": "close",
                      "say": f"{pr_list(shut)} {'were' if len(shut) != 1 else 'was'} opened by a workflow run, so no author will ever answer a review.",
                      "does": "Closes each with a comment carrying the judgments on those rows. The lane re-queues the page on its next run.",
                      "cmd": " ".join(f"--close {n}" for n in shut),
                      "label": "close " + ("them out" if len(shut) != 1 else "it out"),
                      "targets": {str(n): f"--close {n}" for n in shut}})
    routes: dict[str, list[int]] = {}
    for p in visible:
        if p.get("verdict") == "route":
            act = next((a for a in p.get("actions") or [] if a["id"] == "route"), None)
            if act:
                routes.setdefault(act["cmd"].split(":", 1)[1], []).append(p["number"])
    for target, nums in ((t, sorted(ns)) for t, ns in routes.items()):
        cards.append({"kind": "route", "say": f"{pr_list(nums)} {'are' if len(nums) != 1 else 'is'} not your lane.",
                      "does": f"Requests a review from {target} on each and posts what the queue flagged as a comment. Nothing merges.",
                      "cmd": " ".join(f"--route {n}:{target}" for n in nums), "label": f"route to {target}",
                      "targets": {str(n): f"--route {n}:{target}" for n in nums}})
    stamped = [p for p in visible if p.get("verdict") == "stamp"]
    stamps = sorted(p["number"] for p in stamped)
    if stamps:
        held = sorted(p["number"] for p in stamped if not merges_on_stamp(p))
        merged = [n for n in stamps if n not in held]
        does = "Approves each, records the judged findings, and squash-merges " + (
            "them." if not held else f"the {len(merged)} bot-authored one{'s' if len(merged) != 1 else ''}; {pr_list(held)} {'are' if len(held) != 1 else 'is'} human-authored, so approval stops there.")
        cards.append({"kind": "stamp", "say": f"{pr_list(stamps)} pass{'' if len(stamps) != 1 else 'es'} every gate.",
                      "does": does,
                      "cmd": "--stamp " + ",".join(str(n) for n in stamps),
                      "label": "approve the set" if held else "approve & merge the set",
                      "targets": {str(n): f"--stamp {n}" for n in stamps}})
    # Blocked rows are off the board by default, which would hide the ones
    # you can actually unstick. Each mechanical unblock gets a card, so the
    # opening says what is stuck and how many, without unhiding nineteen rows.
    STUCK = {
        "unblock": ("stuck behind a merge conflict",
                    "Merges master into each branch as a merge commit and pushes, so CI re-runs. A conflicted merge is aborted and reported, never resolved blind."),
        "refresh": ("carrying a review that describes an older commit",
                    "Asks each review to update itself against the current head (@claude #update-review). Nothing merges."),
        "rerun": ("carrying a review that errored",
                  "Throws each stale card away and runs a fresh review from scratch (@claude #new-review). Nothing merges."),
    }
    for kind, (why, does) in STUCK.items():
        rows = {}
        for p in visible:
            if p.get("verdict") != "blocked":
                continue
            act = next((a for a in p.get("actions") or [] if a["id"] == kind), None)
            if act:
                rows[p["number"]] = act["cmd"]
        if not rows:
            continue
        nums = sorted(rows)
        cards.append({"kind": kind,
                      "say": f"{pr_list(nums)} {'are' if len(nums) != 1 else 'is'} {why}.",
                      "does": does,
                      "cmd": " ".join(rows[n] for n in nums),
                      "label": {"unblock": "merge base & retry", "refresh": "refresh the reviews",
                                "rerun": "re-run the reviews"}[kind] + (f" ({len(nums)})" if len(nums) > 1 else ""),
                      "targets": {str(n): rows[n] for n in nums}})
    return cards


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


# The brief writes one orientation sentence for the approver; that sentence
# is the summary, however long it runs. Only a PR-body fallback gets cut,
# and then at a sentence, because a body's first line is prose nobody wrote
# for this row. The ceiling is a guard against a pathological line, not a
# style: a row is allowed to be two lines tall.
SUMMARY_MAX = 600


def clip(text: str, limit: int = SUMMARY_MAX) -> str:
    """Never mid-word: "…follow-through for existin…" reads as a bug,
    because it is one. Prefer ending on a sentence, else on a word."""
    t = " ".join(text.split())
    if len(t) <= limit:
        return t
    window = t[:limit]
    stop = max(window.rfind(". "), window.rfind("? "), window.rfind("! "))
    if stop >= limit // 2:
        return window[:stop + 1]
    cut = window.rfind(" ")
    return (window[:cut] if cut > 0 else window).rstrip(",;:—- ") + "…"


BOILERPLATE = (
    "do not edit",
    "composed deterministically",
    "generated by",
    "this section is",
    "automatically generated",
)


def is_boilerplate(line: str) -> bool:
    """A line a machine wrote for a machine. A generated PR body carries
    several of these, and one of them is often the first line that survives
    the structural filters below -- so it lands on the board as the row's
    one-line summary, where it tells the approver nothing about the change.
    Wholly italic lines are the tell (they are captions, not prose), as are
    the fixed phrases the templates use."""
    stripped = line.strip()
    italic = len(stripped) > 2 and (
        (stripped.startswith("_") and stripped.endswith("_"))
        or (stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**"))
    )
    low = stripped.lower()
    return italic or any(phrase in low for phrase in BOILERPLATE)


CHANGE_HEADINGS = ("fixes applied", "what changed", "changes", "summary", "what this pr changes")


def changes_section(body: str) -> str:
    """The first item under a body's own 'what changed' heading. A generated
    body puts the substance in a bulleted list, which the prose scan below
    skips, so without this the row summarizes whichever stray paragraph
    happened to come first."""
    taking = False
    rows: list[list[str]] = []
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("#"):
            taking = s.lstrip("#").strip().strip(":").lower() in CHANGE_HEADINGS
            rows = []
            continue
        if taking and s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not cells or set("".join(cells)) <= set("-: "):
                continue
            rows.append(cells)
            # The header names the columns; the row after it is the change.
            if len(rows) >= 2:
                last = next((c for c in reversed(rows[1]) if c), "")
                if last:
                    return " ".join(last.split())
            continue
        if not taking or not s or is_boilerplate(s) or s.startswith(("<!--", ">", "[!")):
            continue
        s = re.sub(r"^[-*]\s+", "", s)
        s = re.sub(r"^\*\*(.+?)\*\*[:.]?\s*", r"\1: ", s)
        return " ".join(s.split())
    return ""


def one_line_summary(pr: dict) -> str:
    """The brief's italic one-sentence orientation line when present, else
    the first non-empty body line, else the title."""
    body = (pr.get("review") or {}).get("author_body") or ""
    for line in body.splitlines():
        s = line.strip()
        if (s.startswith("_") and s.endswith("_") and len(s) > 2 and "TODO" not in s
                and not any(phrase in s.lower() for phrase in BOILERPLATE)):
            # The brief's own sentence, whole: it was written to orient an
            # approver, and cutting it mid-thought defeats the point.
            return " ".join(s.strip("_").split())
    said = changes_section(pr.get("body") or "")
    if said:
        return clip(said)
    for line in (pr.get("body") or "").splitlines():
        s = line.strip()
        if s and not s.startswith(("#", "<!--", "-", "|", ">", "🤖", "http", "[!")) and not is_boilerplate(s):
            return clip(s)
    return pr.get("title") or ""


# ---- queue ------------------------------------------------------------------


def analyze(queue: dict, cfg: pr_review_config.UserConfig, *, config: routing.Config,
            repo_root: Path = _REPO_ROOT, include_infra: bool = False, strict_stances: bool = False,
            owner: str | None = None, aliases: set[str] | None = None, today: date | None = None) -> dict:
    prs = queue.get("prs") or []
    # No config file: take the lanes from the teams this approver is actually
    # on before falling back to "everything is mine". The org chart is a
    # better first guess than the whole queue, and it needs no local setup.
    if cfg.source == "defaults":
        from_teams = pr_review_config.lanes_from_teams(queue.get("my_teams") or {}, config)
        if from_teams:
            cfg = replace(cfg, me=from_teams, source="github-teams",
                          warnings=[f"no config file — lanes taken from your GitHub teams: {', '.join(from_teams)}"])
    if aliases is None:
        aliases = alias_only_urls(repo_root)
    clusters = collision_clusters(prs)
    directional = directional_conflicts(prs, aliases)
    duplicates = duplicate_candidates(prs)
    approver = queue.get("approver")
    handed = {p["number"] for p in prs if handed_off_to(p, approver, config, cfg.me)}
    cross: dict[int, list[str]] = {}
    for c in clusters:
        c["handed_off"] = [n for n in c["prs"] if n in handed]
        c["mine"] = [n for n in c["prs"] if n not in handed]
        c["merge_order"] = [n for n in c["merge_order"] if n not in handed]
        # One chip per cluster per row: `cluster:C1:overlap:2/19` (this PR's
        # place in the merge order), `cluster:C1:same-file` (no hunk overlap,
        # merges in any order) or `cluster:C1:theirs` (at most one of mine).
        overlap_with: dict[int, bool] = {}
        for p in c["pairs"]:
            if p["kind"] == "overlap":
                overlap_with[p["a"]] = overlap_with[p["b"]] = True
        for n in c["prs"]:
            if len(c["mine"]) <= 1:
                cross.setdefault(n, []).append(f"cluster:{c['id']}:theirs")
            elif overlap_with.get(n) and n in c["merge_order"]:
                cross.setdefault(n, []).append(f"cluster:{c['id']}:overlap:{c['merge_order'].index(n) + 1}/{len(c['merge_order'])}")
            else:
                cross.setdefault(n, []).append(f"cluster:{c['id']}:same-file")
    for d in directional:
        cross.setdefault(d["adds_links_pr"], []).append(f"directional:#{d['removes_links_pr']}:{d['path']}")
    for d in duplicates:
        cross.setdefault(d["newer"], []).append(f"duplicate:#{d['older']}")
    ctx = {
        "cfg": cfg, "config": config, "mine": lanes_for_owner(owner, config, cfg.me),
        "include_infra": include_infra, "strict_stances": strict_stances, "cross": cross,
        "today": today or datetime.now(timezone.utc).date(), "approver": approver, "handed_off": handed, "teams": queue.get("teams") or {},
    }
    for pr in prs:
        analyze_pr(pr, ctx)
    for d in directional:
        d["theirs"] = d["adds_links_pr"] in handed or d["removes_links_pr"] in handed
    by_number = {p["number"]: p for p in prs}
    for c in clusters:
        c["recommendation"] = cluster_recommendation(c, by_number)
    queue["do_next"] = do_next(prs, clusters, directional)
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
        if rec == "request-changes" and not can_revise(pr):
            rec = "close"  # nobody to send it back to; the lane re-queues
        if rec in VERDICTS + ("request-changes", "close") and pr.get("verdict") == "judge":
            pr["recommended"] = rec
    # Recommendations feed the "send back" card, so the opening is rebuilt.
    if "do_next" in queue:
        queue["do_next"] = do_next(queue.get("prs") or [], queue.get("clusters") or [], queue.get("directional") or [])
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
