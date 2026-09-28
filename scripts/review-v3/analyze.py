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
minutes), stale blog dates, stale reviews (reviewed SHA not a prefix of head), and stale
brief summaries (a "What this PR changes" bullet naming a value the current
diff no longer contains).

A row with unanswered 🚨 blocking findings is `blocked`, not `judge`: it
cannot merge until the review is answered, and `blocked` is the one lane
--force never reaches. Answering them is the author's job (a fix, or
`@claude <why> #update-review`); the approver's judgments are board notes
and never answer a finding.

The stamp bar (every gate required):
  label review:no-blockers (or, after a base merge, the card itself saying
  nothing blocks with no open ⚠️ row) · zero ⚠️ rows (zero low-confidence on
  legacy; a v3 ⚠️ row counts whatever its disposition) · review CURRENT · mergeable_state
  in {clean, blocked} with checks green (the Sentinel is left out, as
  act.py's preflight leaves it out: it concludes failure until an approval
  exists) · no overlap collision, directional conflict or duplicate · one
  of the PR's domains is mine · not my own PR · no new file under
  content/blog/ · no stale blog `date:` set by this diff (older than
  stale_date_days) · no layouts/ or .github/ change unless --include-infra
  · changed lines under stamp_max_lines · scrutiny not heightened · (with
  --strict-stances) no editorial stances.
Verdict precedence: blocked > route > stamp/judge. Heightened scrutiny
caps a row at judge.

Every verdict leaves the approver a button that addresses it. A blocked
row names its blocker and carries the mechanical unblock (`--unblock`,
`--refresh`, `--rerun`, `--rerun-checks`), or — where act.py would refuse
to push (`unblock:refused:*`) — a route, send-back or close instead. A
blocked row never carries a stamp button; act.py refuses those, and one
refusal used to sink the whole batch.

The approver's own CHANGES_REQUESTED review is not a blocker (act.py's
preflight ignores it: the approval about to post supersedes it). The row
carries `sent-back:<date>` and, when the head has not moved since that
review and the author can answer it, `waiting_on_author: true` with every
decision button removed — it is the author's turn, and the board groups
those rows the way it groups handed-off ones. My own PR (`author:self`)
gets no stamp or send-back either, since GitHub rejects both (422); it
routes to the lane team and points at `/address-review`.

`--judgments FILE` merges the model's judge output (`judgments[]`,
`fix_draft`, `recommended`) into the matching rows and recomputes each
row. It never lowers a
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
from collections import Counter
from dataclasses import replace
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_HERE))
import act  # noqa: E402  (push policy, so the board and the act layer can't disagree)
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
# The row buttons that are decisions (a row takes one); everything else is a
# side action. A row that is waiting on its author keeps only the side ones.
DECISION_IDS = ("stamp", "stamp-merge", "stamp-no-merge", "request-changes", "close", "route", "chain", "consolidate", "ask-fix")
SENTINEL_CHECK = act.SENTINEL_CHECK

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
    "review": "pinned review status when not CURRENT (stale/absent/in-progress/error/triage-prose); base-merged: the head moved only by merging the base, so the reviewed diff still stands; unreadable:<why>: the review did not arrive whole (a missing page of a split review, or a tally declaring more findings than parsed) — blocked, never judge; parse-confidence:low: it parsed into no findings and nothing corroborates that",
    "label": "the review:* state label; `card-clean`: the label lags a base merge, but the card itself says nothing blocks, so it stands in for review:no-blockers",
    "warnings": "⚠️ reviewer-check rows still open on the brief (legacy: low-confidence)",
    "outstanding": "🚨/❓ rows still open on the author card",
    "sent-back": "the approver's own changes-requested review, by date; not a blocker (the approval supersedes it). With no push since, the row waits on the author",
    "unblock": "refused:<why>: act.py will not push to this head (dependabot, a generated-docs regen, a fork), so the conflict is the author's to resolve",
    "stances": "the brief lists editorial stances (blocks only with --strict-stances)",
    "mergeable": "GitHub mergeable_state when not clean/blocked",
    "checks": "check rollup when not green; `sentinel:failing`: only the Sentinel is red, which it is until an approval exists, so it is not a CI failure",
    "cluster": "member of a collision cluster: overlap (hunks intersect; position in the merge order), same-file (any order), or theirs",
    "directional": "adds links to an alias-only URL another open PR removes links from",
    "duplicate": "looks like a duplicate of another open PR",
    "blog": "new post, or a stale publish date",
    "brief": "a 'What this PR changes' bullet names a value absent from the diff",
    "desc": "PR description names a path not in the diff, or is empty",
    "shape": "infra: touches layouts/ or .github/ (needs --include-infra to stamp); link-only: every changed line differs only in a link",
    "link-fixes": "mine: a link-only diff bypassed the lane check (`link_fixes: mine` in ~/.pr-review.yml)",
    "gate": "any-team: a link-only sweep, which any review team may approve, so the row is any approver's either way",
    "size": "changed lines at or over stamp_max_lines",
    "owner": "the PR's domains and their owning roles",
    "route": "the lane this PR should go to; `no-team`: GitHub says the lane's team doesn't exist, so the SLA person is the target; `team-unverified`: the token couldn't read teams, so the config's team is used unchecked",
    "handed-off": "a human reviewer who isn't me is requested; the row waits on them",
    "merging-over": "an approval or changes-requested review already on the PR",
    "not-governed": "the Sentinel does not gate this PR",
    "author": "author type when human; `generated`: a workflow opened this PR and cannot answer a review, so the row closes rather than goes back; `self`: my own PR, which GitHub lets me neither approve nor send back — it routes to the lane team",
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
    return set(link_counts(lines))


def link_counts(lines: list[str]) -> Counter:
    """How many times each site path is linked across `lines`."""
    out: Counter = Counter()
    for line in lines:
        for m in LINK_RE.finditer(line):
            out[_norm_path((m.group(1) or m.group(2)))] += 1
    return out


def net_link_changes(pr: dict) -> Counter:
    """Per URL, links added minus links removed by this PR's diff. Editing a
    line that merely contains a link puts that link in both the added and
    the removed set, so a per-PR set says the PR both adds and removes it;
    the net says what actually changed (0 for an untouched link that rode
    along on a rewritten line)."""
    added, removed = added_removed_lines(pr)
    net = link_counts(added)
    net.subtract(link_counts(removed))
    return net


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
    """A PR with a net gain of links to an alias-only URL against another
    with a net loss of links to it. Counted per URL, not per set: a sweep
    that rewrites a line containing an alias link it doesn't touch is not
    adding that link, and on the 2026-09-17 queue 18 of 27 set-based pairs
    had a net change of zero or less on one side."""
    net: dict[int, dict[str, int]] = {}
    for pr in prs:
        net[pr["number"]] = {u: v for u, v in net_link_changes(pr).items() if u in aliases and v != 0}
    out = []
    for na, urls in net.items():
        for url in sorted(u for u, v in urls.items() if v > 0):
            for nb, theirs in net.items():
                if nb != na and theirs.get(url, 0) < 0:
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


def open_warnings(pr: dict) -> list[str]:
    """⚠️ rows (v3 brief) or low-confidence items (legacy) with no disposition.

    A v3 brief row is open whatever REVIEW_STATE says about it. The brief is
    the approver's checklist, and a disposition there is the author's answer
    (an update-lane `accept` or a held dispute moves the row onto it), not
    the approver's — so it is exactly what a stamp must not skip reading."""
    review = pr.get("review") or {}
    items = review.get("items") or []
    if review.get("surface") == "v3":
        return [w["id"] for w in review.get("warning_rows") or []]
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


def own_send_back(pr: dict, approver: str | None) -> dict | None:
    """The approver's own changes-requested review, when it is their latest
    review on the PR: `{at: YYYY-MM-DD, by, commit_id, head_moved}`. It is
    not a blocker — act.py's preflight ignores it, since the approval about
    to post supersedes it — but it is the record that the row was sent back,
    and `head_moved` (the review's `commit_id` against the live head) says
    whether the author has pushed since. A queue whose reviews carry no
    `commit_id` (an older collect) reads as not moved, so a second send-back
    is never offered on a guess."""
    me = norm_login(approver) if approver else ""
    if not me:
        return None
    latest = None
    for r in sorted(pr.get("reviews") or [], key=lambda r: r.get("submitted_at") or ""):
        if (r.get("user_type") or "") == "Bot" or r.get("state") in ("COMMENTED", "PENDING"):
            continue
        if norm_login(r.get("user")) == me:
            latest = r  # a DISMISSED record clears an earlier CHANGES_REQUESTED
    if not latest or latest.get("state") != "CHANGES_REQUESTED":
        return None
    head = (pr.get("head") or {}).get("sha") or ""
    cid = latest.get("commit_id") or None
    return {"at": (latest.get("submitted_at") or "")[:10] or "unknown", "by": latest.get("user") or "",
            "commit_id": cid, "head_moved": bool(cid and head and cid != head)}


def unblock_refusal(pr: dict) -> str | None:
    """Why act.py would refuse `--unblock` on this row, as a short slug for
    the `unblock:refused:<why>` chip, or None when a push is allowed.

    A conflict act.py already hit on this head counts. The merge is
    mechanical or it is nobody's: offering the button a second time asks the
    approver to re-run a merge that stopped on the same files and reported
    it, which is how "merge base & retry" became a button that did nothing.
    Collect only carries the record while it describes the current head, so
    a push that settles the conflict brings the button back on its own."""
    if pr.get("unblock_conflict"):
        return "conflict"
    ok, why = act.push_allowed(pr)
    if ok:
        return None
    low = why.lower()
    if "dependabot" in low:
        return "dependabot"
    if "fork" in low:
        return "fork"
    if "regenerated" in low:
        return "generated"
    return re.sub(r"[^a-z0-9]+", "-", low).strip("-")[:40]


def route_targets(domains: list[str], owners: dict, ctx: dict) -> tuple[list[str], list[str]]:
    """One review target per owning role among `domains`, and the reason
    codes that explain them. The team when GitHub has it (collect.py asked),
    else the SLA person; a team that lands later is picked up on the next
    run. Two domains owned by one team are one target."""
    targets: list[str] = []
    reasons: list[str] = []
    for d in domains:
        route = owners.get(d)
        if not route:
            continue
        team = route.get("team")
        known = (ctx.get("teams") or {}).get(team) if team else None
        if team and known is not False:
            # True: GitHub has it. None: the token can't read teams (403),
            # which is not evidence the team is missing — route to the team
            # the config names and say the check didn't run, rather than
            # quietly demoting every lane to its SLA person.
            target = f"@{team}"
            if known is None and "route:team-unverified" not in reasons:
                reasons.append("route:team-unverified")
        else:
            target = f"@{route['person']}" if route.get("person") else f"@{team}"
            if team and "route:no-team" not in reasons:
                reasons.append("route:no-team")
        if target and target != "@" and target not in targets:
            targets.append(target)
        code = f"route:{route['role']}"
        if code not in reasons:
            reasons.append(code)
    return targets, reasons


def route_action(n: int, targets: list[str]) -> dict:
    """`--route` is repeatable in act.py, so a row that needs two teams asks
    both in one command (#21554 needs blog and marketing)."""
    return {"id": "route", "label": f"request review from {' and '.join(targets)}",
            "cmd": " ".join(f"--route {n}:{t}" for t in targets), "targets": list(targets)}


def ownership(pr: dict, ctx: dict) -> dict:
    """Whose row this is: lanes, `is_mine`, the chips that explain it, and
    who it is handed off to. A pre-pass, because the cross-PR analysis needs
    to know which cluster members are mine before any verdict exists."""
    cfg: pr_review_config.UserConfig = ctx["cfg"]
    config: routing.Config = ctx["config"]
    mine: set[str] | None = ctx["mine"]
    reasons: list[str] = []
    lanes = domains_and_owner(pr, config)
    is_mine = mine is None or bool(set(lanes["domains"]) & mine)
    for d in lanes["domains"]:
        reasons.append(f"owner:{d}:{lanes['owners'][d]['role']}")
    # There is no "no required role" case any more: `none` matrix cells are
    # a config error, so every governed PR resolves to an approver team and
    # every row has somebody on the hook. The `gate:none` reason code this
    # branch used to emit is gone with it — it described a state that rested
    # on the Sentinel being the merge gate, which it is not.
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
    approver = ctx.get("approver")
    author_self = bool(approver) and norm_login((pr.get("author") or {}).get("login")) == norm_login(approver)
    if author_self:
        # GitHub rejects an approval or a changes-requested review on your
        # own PR (422), so this row is never mine to stamp: it routes to the
        # lane team, whatever the lane.
        reasons.append("author:self")
        is_mine = False
    return {"lanes": lanes, "is_mine": is_mine, "reasons": reasons, "author_self": author_self,
            "handed_off_to": handed_off_to(pr, approver, config, cfg.me)}


def _quote_safe(text: str) -> str:
    return " ".join(text.replace('"', "'").split())


def analyze_pr(pr: dict, ctx: dict) -> None:
    """Mutates `pr`: domains/owners, reasons, verdict, actions. Re-entrant:
    merge_judgments() runs it again on a row after the judgments land."""
    cfg: pr_review_config.UserConfig = ctx["cfg"]
    mine: set[str] | None = ctx["mine"]
    n = pr["number"]
    own = (ctx.get("ownership") or {}).get(n) or ownership(pr, ctx)
    lanes = own["lanes"]
    is_mine = own["is_mine"]
    author_self = own["author_self"]
    reasons: list[str] = list(own["reasons"])
    review = pr.get("review") or {}
    labels = set(pr.get("labels") or [])
    pr.pop("recommended", None)  # a judgments merge re-adds it on judge rows; a stale one must not outlive a verdict change
    pr.pop("rejected_recommendation", None)
    pr["handed_off_to"] = own["handed_off_to"]
    pr["handed_off"] = bool(pr["handed_off_to"])
    pr["author_self"] = author_self
    pr.update(lanes)

    blocked: list[str] = []      # (reason, action) pairs collapse into reasons + actions
    actions: list[dict] = []
    stamp_ok = True

    # Every stamp gate this row missed, recorded as well as cleared, because
    # "judge" alone does not say whether a person has to read the PR or
    # whether it merely has to merge after another one. `chip=False` where
    # the reason code is already on the row from somewhere else.
    fails: list[str] = []

    def gate_fail(code: str, *, chip: bool = True):
        nonlocal stamp_ok
        stamp_ok = False
        fails.append(code)
        if chip and code not in reasons:
            reasons.append(code)

    def add_action(a: dict):
        if not any(x["id"] == a["id"] for x in actions):
            actions.append(a)

    revisable = can_revise(pr)

    # -- trust / risk
    reasons.append(f"risk:{pr.get('risk_tier')}")
    if pr.get("scrutiny") == "heightened":
        gate_fail("scrutiny:heightened")
        for r in (pr.get("ai_suspect") or {}).get("reasons") or []:
            reasons.append(f"ai-suspect:{r}")
    author = pr.get("author") or {}
    if author.get("type") != "bot":
        reasons.append(f"author:{author.get('type')}")
    elif not revisable:
        reasons.append("author:generated")
    if author.get("membership_note"):
        reasons.append("trust:membership-unreadable")
    if pr.get("draft"):
        reasons.append("draft")
        blocked.append("draft")
    if pr["handed_off"]:
        reasons.append("handed-off:" + ",".join(pr["handed_off_to"]))

    # -- my own send-back. Not a blocker; the row is the author's turn until
    # they push, and a second send-back is only offered once they have.
    sent = own_send_back(pr, ctx.get("approver"))
    pr["sent_back"] = sent
    waiting = False
    if sent:
        reasons.append(f"sent-back:{sent['at']}")
        waiting = revisable and not author_self and not sent["head_moved"]

    def send_back(label: str, reason: str | None = None):
        """The author's turn, said once per row. A generated row has no
        author to answer, so it closes instead; my own PR takes neither
        (GitHub refuses both), and a row already waiting on its author is
        not sent back twice."""
        if author_self or waiting:
            return
        if revisable:
            cmd = f"--request-changes {n}"
            if reason:
                cmd += f' --reason "{n}={_quote_safe(reason)}"'
            add_action({"id": "request-changes", "label": label, "cmd": cmd})
        else:
            add_action({"id": "close", "label": "close it out", "cmd": f"--close {n}"})

    # -- review surface
    status = review.get("status") or "ABSENT"
    for l in sorted(labels):
        if l.startswith("review:"):
            reasons.append(f"label:{l}")
    if review.get("base_merged"):
        reasons.append("review:base-merged")
    if status != "CURRENT":
        gate_fail(f"review:{status.lower().replace('_', '-')}")
    if status == "STALE":
        blocked.append("review:stale")
        add_action({"id": "refresh", "label": "refresh review", "cmd": f"--refresh {n}"})
    elif status == "ERROR":
        # The pipeline's own escape hatch: `#new-review` clears the cards
        # and dispatches a fresh initial review, bypassing the skips.
        blocked.append("review:error")
        add_action({"id": "rerun", "label": "re-run the review", "cmd": f"--rerun {n}"})
    elif status == "IN_PROGRESS":
        # Usually a wait. But a crashed run leaves the label with no run
        # behind it (test_handoff_guard.py), so the fresh review is the way
        # out when the wait never ends.
        blocked.append("review:in-progress")
        add_action({"id": "rerun", "label": "re-run the review (if it never lands)", "cmd": f"--rerun {n}"})
    elif status in ("ABSENT", "TRIAGE_PROSE"):
        # No review ran (trivial / frontmatter-only / draft / bot skip);
        # a full one is a side action the approver can ask for.
        add_action({"id": "rerun", "label": "run a full review", "cmd": f"--rerun {n}"})
    # A review nobody could read whole is not a review, and a row carrying
    # one must never be a `judge` row: `--force` would then merge over the
    # findings that never arrived. Two ways to know: GitHub did not return a
    # page the `k/N` markers promise, or the card's own tally declares more
    # findings than parsed out of its sections. Both say the same thing --
    # the findings may not be here -- so the row is blocked and the unblock
    # is a fresh review, not a judgment call over a body with holes in it.
    unreadable = []
    if review.get("pages_missing"):
        unreadable.append("pages:" + ",".join(str(k) for k in review["pages_missing"]))
    if review.get("counts_shortfall"):
        unreadable.append("tally:" + ",".join(sorted(review["counts_shortfall"])))
    if unreadable:
        gate_fail("review:unreadable:" + ";".join(unreadable))
        blocked.append("review:unreadable")
        add_action({"id": "rerun", "label": "re-run the review", "cmd": f"--rerun {n}"})
    elif (review.get("surface") or "none") != "none" and review.get("parse_confidence") != "high":
        # Weaker, and not a blocker: the body parsed into no findings and
        # nothing contradicts that, but nothing corroborates it either (a v2
        # card with no tally table; a v3 card with no head sentinel or a
        # broken REVIEW_STATE). Not stampable, and a person reads it.
        gate_fail("review:parse-confidence:low")
    blockers = open_blockers(pr)
    warnings = open_warnings(pr)
    label_ok = "review:no-blockers" in labels
    if not label_ok and review.get("base_merged") and review.get("nothing_blocks") and not warnings and not blockers:
        # A base merge swaps review:no-blockers for review:stale on any push,
        # while the card still describes this diff and says nothing blocks.
        # The card is the evidence; the label only lags it.
        label_ok = True
        reasons.append("label:card-clean")
    if not label_ok:
        gate_fail("label:no-blockers-missing", chip=False)
        if review.get("base_merged") and status == "CURRENT":
            add_action({"id": "refresh", "label": "refresh review", "cmd": f"--refresh {n}"})
    if blockers:
        # Blocked, not judge. An unanswered 🚨 is the review still waiting on
        # the author, and no approver's call substitutes for their answer —
        # so the row must not sit in a lane --force can reach. The author
        # answers with a fix or `@claude <why> #update-review`; the row
        # leaves this lane on the next collect.
        gate_fail(f"outstanding:{len(blockers)}:{','.join(blockers)}")
        blocked.append(f"outstanding:{len(blockers)}")
        send_back("send back to author")
    if warnings:
        gate_fail(f"warnings:{len(warnings)}:{','.join(warnings)}")
    if review.get("stances"):
        reasons.append("stances:present")
        if ctx["strict_stances"]:
            gate_fail("stances:present", chip=False)

    # -- merge state
    ms = pr.get("mergeable_state") or "unknown"
    refused = unblock_refusal(pr)
    if ms not in STAMP_STATES:
        gate_fail(f"mergeable:{ms}")
        if ms == "dirty":
            blocked.append("mergeable:dirty")
        if ms in ("dirty", "behind"):
            if refused is None:
                add_action({"id": "unblock", "label": "merge base & retry" if ms == "dirty" else "merge base", "cmd": f"--unblock {n}"})
            elif ms == "dirty":
                # act.py won't push here, so the conflict is the author's: say
                # so, and offer the ways to hand it to them.
                reasons.append(f"unblock:refused:{refused}")
                send_back("ask the author to merge master",
                          "This branch conflicts with master and can't be updated from here; please merge master into it.")
    checks = pr.get("checks") or {}
    failing = list(checks.get("failing") or [])
    real_failures = [f for f in failing if (f or "").strip().lower() != SENTINEL_CHECK]
    if checks.get("state") == "red" and not real_failures:
        # The Sentinel concludes failure until an approval exists, so it can't
        # gate the approval it waits for. act.py's preflight leaves it out
        # and polls it between the approval and the merge; the board agrees.
        reasons.append("checks:sentinel:failing")
    elif checks.get("state") != "green":
        gate_fail(f"checks:{checks.get('state')}:{','.join((real_failures or checks.get('pending') or [])[:3])}")
        if checks.get("state") == "red":
            blocked.append("checks:red")
            named = ", ".join(real_failures[:3]) + (f" and {len(real_failures) - 3} more" if len(real_failures) > 3 else "")
            add_action({"id": "rerun-checks", "label": f"re-run failed checks ({named})", "cmd": f"--rerun-checks {n}"})
            send_back(f"send back: CI is red ({named})", f"CI is red ({named}); please fix the failing checks.")
    me = norm_login(ctx.get("approver")) if ctx.get("approver") else ""
    for user, state in latest_reviews(pr).items():
        if state == "CHANGES_REQUESTED":
            if me and norm_login(user) == me:
                continue  # mine: `sent-back:` above, and act.py's preflight ignores it
            gate_fail(f"merging-over:changes-requested:{user}")
            blocked.append("changes-requested")
            # Their call, not mine: asking them to look again is the one
            # button that addresses it, and it parks the row with them.
            add_action({"id": "route", "label": f"ask @{user} to re-review", "cmd": f"--route {n}:@{user}", "targets": [f"@{user}"]})
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
            gate_fail("shape:infra", chip=False)
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
    ng = routing.not_governed_reason(ctx["config"], author.get("login") or "", labels)
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
            gate_fail(code, chip=False)
        if code.startswith("duplicate:") and not code.endswith(":theirs"):
            other = code.split(":")[1].lstrip("#")
            add_action({"id": "close", "label": f"close as duplicate of #{other}", "cmd": f"--close {n} --superseded-by {other}"})
    reasons.extend(shown)

    # -- ownership / verdict
    if not is_mine:
        # One target per missing role. My own PR is missing every role, since
        # I can't supply any of them.
        missing = [d for d in lanes["domains"] if author_self or mine is None or d not in mine]
        targets, route_reasons = route_targets(missing, lanes["owners"], ctx)
        reasons.extend(r for r in route_reasons if r not in reasons)
        existing = next((a for a in actions if a["id"] == "route"), None)
        if existing:
            # Someone else's changes-requested already asks them to look
            # again; the lane team rides along in the same request.
            targets = [t for t in (existing.get("targets") or []) + targets if t]
            targets = list(dict.fromkeys(targets))
            actions[actions.index(existing)] = route_action(n, targets)
        elif targets:
            add_action(route_action(n, targets))
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
        if revisable:
            # Only when there is something to send: act.py refuses an empty
            # review, and a row judged on size alone has no finding to
            # carry. The judge step's asks bring the button back on recompute.
            if act.ask_lines(pr) and not author_self:
                actions.insert(2, {"id": "request-changes", "label": "send back to author", "cmd": f"--request-changes {n}"})
        else:
            # pulumi-bot's lanes open the PR from a workflow run; there is no
            # author to send it back to. Fix it here or close it and let the
            # lane re-queue the page.
            actions.insert(2, {"id": "close", "label": "close it out", "cmd": f"--close {n}"})
    elif verdict == "route" and not author_self:
        # The lane is a default, not a lock: the approver can still take the
        # row. act.py accepts --force on any non-blocked verdict — and only
        # on those, which is why a blocked row never carries these.
        actions.extend(stamp_actions(pr, n, force=True, base="approve anyway"))
    if verdict in ("judge", "route"):
        if pr.get("risk_tier") == "infra":
            add_action({"id": "deploy", "label": "deploy to pulumi-test.io", "cmd": f"--deploy {n}"})
        if pr.get("one_click_suggestions") or any(r.startswith("desc:") for r in reasons):
            add_action({"id": "fix", "label": "apply fixes", "cmd": f"--fix {n}"})
        if (pr.get("preview") or {}).get("pages"):
            add_action({"id": "render", "label": "screenshot the preview", "cmd": f"--render {n}"})
    # A workflow opened this PR, so no author will ever answer its review:
    # the send-back is unread and closing it only re-queues the same page on
    # the next run. The remaining way out is to fix the branch yourself --
    # which is a session on the branch, not an act.py write -- so it rides
    # on the row as a handoff instead of a fragment of the composed command.
    # Only where the fix would survive: dependabot and the generated-docs
    # regens are rebuilt from source, and a fork head has no push access.
    open_count = len(blockers) + len(warnings)
    pr["handoffs"] = []
    if not revisable and open_count and act.push_allowed(pr)[0]:
        pr["handoffs"].append({
            "id": "handfix", "label": "fix it yourself", "run": f"/address-review {n}", "exclusive": "fix",
            "why": f"{open_count} open finding{'s' if open_count != 1 else ''} and an author who will never read a "
                   f"review: this hands #{n} to /address-review, which walks the findings with you and pushes the "
                   f"fixes to the branch. It is a separate, interactive run -- it is not part of the --act command "
                   f"at the foot of this page, and this page still writes nothing."})
        # The same job, handed to the agent already watching the PR instead
        # of to you. It is one comment, so unlike the handoff it is an
        # ordinary act.py fragment and rides in the batch; the two are
        # alternatives, and the board's toggles put one out when the other
        # lights. Offered only when there are ids to name -- an `@claude fix`
        # with nothing after it asks for nothing.
        if act.ask_fix_items(pr):
            add_action({"id": "ask-fix", "label": "ask @claude to fix them", "cmd": f"--ask-fix {n}",
                        "exclusive": "fix"})

    if author_self:
        pr["self_note"] = (f"Your own PR: GitHub takes neither your approval nor your send-back. "
                           f"Run /address-review {n} to answer the review, then the lane team approves.")
    else:
        pr.pop("self_note", None)
    if waiting:
        # The author's turn: no decision is offered, only the side actions
        # that still apply (a CI re-run, a base merge, a refresh).
        actions = [a for a in actions if a["id"] not in DECISION_IDS]
    pr["waiting_on_author"] = waiting
    pr["blockers"] = blocked
    pr["is_mine"] = is_mine
    pr["verdict"] = verdict
    pr["gate_fails"] = fails
    pr["reasons"] = reasons
    pr["actions"] = actions
    pr["route_targets"] = next((a.get("targets") or [] for a in actions if a["id"] == "route"), [])
    pr["open_warning_ids"] = warnings
    pr["open_blocker_ids"] = blockers
    pr.setdefault("judgments", [])
    pr.setdefault("fix_draft", None)
    pr["summary"] = one_line_summary(pr)


CONSOLIDATE_SHARE = 0.6  # a cluster this dominated by one bot author's sweeps should be one PR


def _tally(nums: list[int], by: dict[int, dict]) -> str:
    """`4 blocked, 2 waiting on author, 1 to route` — what a cluster's
    members actually are, so a card never calls a route row blocked."""
    words = {"blocked": "blocked", "route": "to route", "judge": "needing a decision", "stamp": "stampable"}
    counts: Counter = Counter()
    for n in nums:
        p = by.get(n) or {}
        if p.get("handed_off"):
            counts["handed off"] += 1
        elif p.get("waiting_on_author"):
            counts["waiting on author"] += 1
        else:
            counts[words.get(p.get("verdict"), p.get("verdict") or "unknown")] += 1
    return ", ".join(f"{k} {v}" for v, k in sorted(((v, k) for k, v in counts.items()), reverse=True))


def cluster_recommendation(c: dict, by: dict[int, dict]) -> dict:
    """The one move a cluster asks of the approver, in words, with the
    action that does it: `ignore` (same-file only: any order works),
    `consolidate` (mostly one bot's overlapping sweeps: one request-changes
    beats N serial merges), or `chain` (merge the first, unblock the next).
    `mine` here is the members that are mine to sequence: not handed off,
    and in my lanes."""
    mine = c.get("mine") or []
    order = c.get("merge_order") or []
    others = [n for n in c.get("prs") or [] if n not in mine]
    if len(mine) <= 1:
        what = _tally(others, by)
        return {"kind": "theirs", "say": f"{c['id']}: nothing of yours to sequence ({what})." if what else f"{c['id']}: nothing of yours to sequence.", "cmd": None}
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
    # The first link is a member I could approve now; the next is one whose
    # hunks actually overlap it, since that is the one the merge will dirty.
    first = next((n for n in order if (by.get(n) or {}).get("verdict") in ("stamp", "judge")
                  and not (by.get(n) or {}).get("waiting_on_author")), None)
    if first is None:
        return {"kind": "blocked", "say": f"{c['id']}: none of your {len(mine)} PRs can lead the chain yet ({_tally(mine, by)}); unblock one to start.", "cmd": None}
    overlaps_first = {p["b"] if p["a"] == first else p["a"] for p in c.get("pairs") or []
                      if p.get("kind") == "overlap" and first in (p["a"], p["b"])}
    nxt = next((n for n in order if n != first and n in overlaps_first), None)
    others_n = f" and {len(order) - 1} other{'s' if len(order) != 2 else ''}" if len(order) > 1 else ""
    say = (f"#{first}{others_n} edit the same lines in the same files, so they can only merge in order "
           f"(cluster {c['id']}, {len(order)} PRs).")
    return {"kind": "chain", "first": first, "next": nxt, "say": say, "cmd": f"--chain {c['id']}"}


# A cross-PR gate is not a judgment call: it says this PR has to merge after
# another one, which is precisely what the chain card does. Every other gate
# means a person has to read something before approving.
COLLISION_GATES = ("cluster:", "directional:", "duplicate:")


def only_collisions_hold(pr: dict) -> bool:
    """True when the row cleared every stamp gate except the cross-PR ones.
    An overlapping member of a cluster is always a `judge` row -- the overlap
    is itself a gate -- so "is the lead stampable" cannot be read off the
    verdict; this is the question the chain button actually asks."""
    fails = pr.get("gate_fails")
    if fails is None:                       # a queue analyzed before gate_fails existed
        return pr.get("verdict") == "stamp"
    return bool(fails) and all(f.startswith(COLLISION_GATES) for f in fails)


CLUSTER_ACTION_IDS = ("chain", "consolidate")


def attach_cluster_actions(prs: list[dict], clusters: list[dict]) -> None:
    """A cluster's recommendation as a button on the row it belongs to, so
    the move sits next to the evidence for it instead of in a strip at the
    top of the page naming rows you can't see.

    The chain goes on its lead: `--chain C1` approves the lead through the
    stamp gates and then merges master into the next link, so the button
    `covers` that link -- the board marks the covered row and puts the chain
    out if a decision is picked there instead. It covers nothing when the
    lead is human-authored: approving it does not merge it, so act.py skips
    the unblock and the next link waits for a later run. `--chain` approves the lead
    with `--force`, so it is offered only where the collision is the *only*
    thing holding the lead back (`only_collisions_hold`); a lead held up by
    anything else keeps its own approve-as-is button, next to the findings,
    and nothing pretends the chain is mechanical. A consolidation goes on
    the newest sweep, which is the PR its request is posted on.

    Idempotent: every row's earlier cluster action is dropped first, since
    `merge_judgments` rebuilds rows and recommendations move."""
    by = {p["number"]: p for p in prs}
    for p in prs:
        p["actions"] = [a for a in p.get("actions") or [] if a["id"] not in CLUSTER_ACTION_IDS]
    for c in clusters:
        r = c.get("recommendation") or {}
        if r.get("kind") == "chain":
            first, nxt = r.get("first"), r.get("next")
            lead = by.get(first)
            if not lead or not nxt or lead.get("waiting_on_author") or lead.get("handed_off"):
                continue
            if lead.get("verdict") != "stamp" and not only_collisions_hold(lead):
                continue
            merges = merges_on_stamp(lead)
            if merges:
                label = f"approve & merge, then unblock #{nxt}"
                help_ = (f"Approves and squash-merges #{first} through the same gates as a stamp, then merges master into "
                         f"#{nxt} so it can follow (cluster {c['id']}). One link per run; the next one waits on CI.")
            else:
                label = f"approve, then unblock #{nxt}"
                help_ = (f"Approves #{first}; it is human-authored, so the author merges it, and the next run merges master "
                         f"into #{nxt} once it has landed (cluster {c['id']}). One link per run.")
            # `covers` only where the unblock actually runs this time. act.py
            # gates the unblock step on `requires=["stamp", first]` and skips
            # it unless that stamp merged, so a human-authored lead -- approved
            # and left for its author to merge -- never reaches #nxt in this
            # run. The label and help already say the next run does it; a
            # `covers` here would have the board contradict them, marking the
            # covered row decided for a write nothing will perform.
            lead["actions"].insert(0, {"id": "chain", "label": label, "cmd": r["cmd"], "cluster": c["id"],
                                       "covers": [nxt] if merges else [], "help": help_})
        elif r.get("kind") == "consolidate":
            on = by.get(r.get("on"))
            if not on or on.get("waiting_on_author") or on.get("handed_off"):
                continue
            on["actions"].insert(0, {"id": "consolidate", "label": f"ask {r.get('target')} for one consolidated PR",
                                     "cmd": r["cmd"], "cluster": c["id"],
                                     "help": (f"Posts a changes-requested review on #{on['number']} asking {r.get('target')} to fold "
                                              f"the overlapping sweeps in cluster {c['id']} into one PR, instead of N serial "
                                              f"merges. Nothing merges.")})


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
    """The batch moves, as `--terminal` prints them after the table: at most
    a handful, each one sentence of what is true, one sentence of what the
    command does, and the PRs it does it to. Ordered by leverage:
    consolidations, chains, then the batches (send back / close / route /
    stamp). The board does not render these: every one of them is the row
    buttons it names, and a row is where the evidence for the decision is,
    so the board keeps each decision on its row (`attach_cluster_actions`
    puts the chain and the consolidation there too).

    `targets` maps a PR to the row action the entry batches, and an entry
    with no `targets` (a chain, a consolidation) `claims` its PRs instead,
    so a reader can check an entry against the rows above it.

    Two invariants hold over every entry here. It never names a row the board
    does not render (`visible` is exactly `render_board`'s row set). And it
    never carries an approval that needed a judgment call: the stamp entry is
    the rows that cleared every gate mechanically, and a chain whose lead did
    not states the fact without a command."""
    cards: list[dict] = []
    by_n = {p["number"]: p for p in prs}
    for c in clusters:
        r = c.get("recommendation") or {}
        if r.get("kind") == "chain":
            first, nxt = r.get("first"), r.get("next")
            lead = by_n.get(first) or {}
            merges = merges_on_stamp(lead)
            # The opening never offers an approval that needs reading first.
            # `--chain` approves the lead with --force, so it is offered only
            # where the lead cleared every gate but the collision itself --
            # the thing the chain is for. A lead held up by anything else (an
            # open ⚠️ row, a stale review, a new blog post, a
            # diff over the cap) states the fact and stops: that decision
            # belongs on #first's own row, next to the findings behind it.
            if lead.get("verdict") != "stamp" and not only_collisions_hold(lead):
                held = [f for f in lead.get("gate_fails") or [] if not f.startswith(COLLISION_GATES)]
                cards.append({"kind": "chain", "cluster": c["id"], "say": r["say"], "merges": merges,
                              "does": f"#{first} leads the chain, but it needs a call of its own first "
                                      f"({', '.join(held[:3]) or lead.get('verdict') or 'judge'}). Decide it on its row "
                                      f"below; the next run unblocks" + (f" #{nxt}." if nxt else " whatever follows."),
                              "cmd": None, "claims": [], "targets": {}})
                continue
            # `--chain C1` is one command act.py runs through the stamp gates
            # (plan-time blocker check, preflight) before it merges
            # base into the next link, so the card is that command and the
            # rows it covers defer to it (`claims`) rather than mapping to a
            # row button of their own.
            if merges:
                label = f"approve & merge #{first}"
                does = f"Approves and squash-merges #{first}" + (
                    f", then merges master into #{nxt} so it can follow." if nxt else ".")
            else:
                label = f"approve #{first}, then unblock the next"
                does = (f"Approves #{first}; it is human-authored, so the author merges it, and "
                        + (f"the next run merges master into #{nxt} once it has landed." if nxt else "nothing follows."))
            cards.append({"kind": "chain", "cluster": c["id"], "say": r["say"], "does": does + " One link per run; the next one waits on CI.",
                          "cmd": r["cmd"], "label": label, "merges": merges,
                          "claims": [n for n in (first, nxt) if n], "targets": {}})
        elif r.get("kind") == "consolidate":
            on = r.get("on")
            cards.append({"kind": "consolidate", "cluster": c["id"], "say": r["say"],
                          "does": f"Posts a changes-requested review on #{on} asking {r.get('target')} for one consolidated PR. Nothing merges.",
                          "cmd": r["cmd"], "label": f"send #{on} back", "claims": [on] if on else []})
    # Waiting on someone (a requested reviewer, or the author after a
    # send-back) means no decision card names the row; the mechanical
    # unblocks below still do, since those are still the approver's to press.
    on_deck = [p for p in prs if not p.get("handed_off")]
    visible = [p for p in on_deck if not p.get("waiting_on_author")]
    rejected = [p for p in visible if p.get("recommended") in ("request-changes", "close")]
    back = sorted(p["number"] for p in rejected if p.get("recommended") == "request-changes")
    if back:
        cards.append({"kind": "request-changes",
                      "say": f"{pr_list(back)} need{'' if len(back) != 1 else 's'} {'their' if len(back) != 1 else 'its'} author, not you.",
                      "does": "Posts a changes-requested review on each, written from the judgments on those rows, and labels them needs-author-response. Nothing merges.",
                      "cmd": " ".join(f"--request-changes {n}" for n in back),
                      "label": "send back" + (" all" if len(back) != 1 else ""),
                      "targets": {str(n): f"--request-changes {n}" for n in back}})
    # A close recommendation: a workflow-authored row has nobody to send it
    # back to, so the lane re-queues the page; a person's closes with the
    # judgments as the stated reason (the row's close button carries it).
    closes = {p["number"]: next((a["cmd"] for a in p.get("actions") or [] if a["id"] == "close"), None)
              for p in rejected if p.get("recommended") == "close"}
    closes = {n: c for n, c in closes.items() if c}
    if closes:
        shut = sorted(closes)
        gen = [n for n in shut if not can_revise(by_n.get(n) or {})]
        if len(gen) == len(shut):
            say = f"{pr_list(shut)} {'were' if len(shut) != 1 else 'was'} opened by a workflow run, so no author will ever answer a review."
            does = "Closes each with a comment carrying the judgments on those rows. The lane re-queues the page on its next run."
        else:
            say = f"{pr_list(shut)} {'are' if len(shut) != 1 else 'is'} better closed than fixed, per the judgments."
            does = "Closes each with a comment saying why: the judgments' asks on a person's PR, the full judgments on a workflow's."
        cards.append({"kind": "close", "say": say, "does": does,
                      "cmd": " ".join(closes[n] for n in shut),
                      "label": "close " + ("them out" if len(shut) != 1 else "it out"),
                      "targets": {str(n): closes[n] for n in shut}})
    routes: dict[tuple[str, ...], dict[int, str]] = {}
    for p in visible:
        if p.get("verdict") == "route":
            a = next((a for a in p.get("actions") or [] if a["id"] == "route"), None)
            if a:
                routes.setdefault(tuple(a.get("targets") or [a["cmd"].split(":", 1)[1]]), {})[p["number"]] = a["cmd"]
    for targets, rows in routes.items():
        nums = sorted(rows)
        target = " and ".join(targets)
        cards.append({"kind": "route", "say": f"{pr_list(nums)} {'are' if len(nums) != 1 else 'is'} not your lane.",
                      "does": f"Requests a review from {target} on each and posts what the queue flagged as a comment. Nothing merges.",
                      "cmd": " ".join(rows[n] for n in nums), "label": f"route to {target}",
                      "targets": {str(n): rows[n] for n in nums}})
    stamped = [p for p in visible if p.get("verdict") == "stamp"]
    stamps = sorted(p["number"] for p in stamped)
    if stamps:
        held = sorted(p["number"] for p in stamped if not merges_on_stamp(p))
        merged = [n for n in stamps if n not in held]
        does = "Approves each and squash-merges " + (
            "them." if not held else f"the {len(merged)} bot-authored one{'s' if len(merged) != 1 else ''}; {pr_list(held)} {'are' if len(held) != 1 else 'is'} human-authored, so approval stops there.")
        cards.append({"kind": "stamp", "say": f"{pr_list(stamps)} pass{'' if len(stamps) != 1 else 'es'} every gate.",
                      "does": does,
                      "cmd": "--stamp " + ",".join(str(n) for n in stamps),
                      "label": "approve the set" if held else "approve & merge the set",
                      "targets": {str(n): f"--stamp {n}" for n in stamps}})
    # Each mechanical unblock gets a card, so the opening says what is stuck
    # and how many without making you read nineteen blocked rows to find it.
    # `visible`, not `on_deck`: a row parked under "Waiting on the author"
    # has no row on the board, and a card that names one can never light,
    # because the button it would press is not on the page.
    STUCK = {
        "unblock": ("stuck behind a merge conflict",
                    "Merges master into each branch as a merge commit and pushes, so CI re-runs. A conflicted merge is aborted and reported, never resolved blind."),
        "refresh": ("carrying a review that describes an older commit",
                    "Asks each review to update itself against the current head (@claude #update-review). Nothing merges."),
        "rerun": ("carrying a review that errored",
                  "Throws each stale card away and runs a fresh review from scratch (@claude #new-review). Nothing merges."),
        "rerun-checks": ("stuck behind red CI",
                         "Re-runs the failed jobs of each head's workflow runs. Nothing merges; a real failure comes back red."),
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
                                "rerun": "re-run the reviews", "rerun-checks": "re-run failed checks"}[kind] + (f" ({len(nums)})" if len(nums) > 1 else ""),
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


def _counts(prs: list[dict]) -> dict:
    """Per verdict, the rows that are on deck: not handed off and not waiting
    on their author. Those two are counted on their own."""
    deck = [p for p in prs if not p.get("handed_off") and not p.get("waiting_on_author")]
    counts = {v: sum(1 for p in deck if p.get("verdict") == v) for v in VERDICTS}
    counts["handed-off"] = sum(1 for p in prs if p.get("handed_off"))
    counts["waiting-on-author"] = sum(1 for p in prs if p.get("waiting_on_author") and not p.get("handed_off"))
    return counts


def lanes_from_memberships(cfg: pr_review_config.UserConfig, memberships: dict, config: routing.Config) -> pr_review_config.UserConfig:
    """No config file: take the lanes from the teams this approver is actually
    on. Three answers, each said out loud, because "every lane is mine" and
    "no lane is mine" are opposite boards:
      - unreadable (no team answered True, and at least one answered None):
        every lane, the old fallback, and the warning says why;
      - readable and on none of the teams: no lane, so every row routes;
      - on some: those teams' lanes.
    gh_client.team_member maps a 404 to False, and GitHub answers 404 for a
    team the token can't see, so "member of nothing" can also mean "the
    token sees nothing"; the warning says so."""
    from_teams = pr_review_config.lanes_from_teams(memberships, config)
    hidden = sorted(t for t, v in (memberships or {}).items() if v is None)
    if from_teams is None:
        return replace(cfg, warnings=[
            "no config file, and your GitHub team memberships are unreadable (the token lacks read:org, or GitHub answers "
            "404 for a team it hides from it) — every lane counts as mine; create ~/.pr-review.yml to pin your lanes"])
    if not from_teams:
        return replace(cfg, me=[], source="github-teams", warnings=[
            "no config file — you are on none of the routing teams, so every row routes (GitHub answers 404 for a team the "
            "token can't see, which reads as 'not a member'); create ~/.pr-review.yml to pin your lanes"])
    note = f" ({', '.join(hidden)} unreadable)" if hidden else ""
    return replace(cfg, me=from_teams, source="github-teams",
                   warnings=[f"no config file — lanes taken from your GitHub teams: {', '.join(from_teams)}{note}"])


def analyze(queue: dict, cfg: pr_review_config.UserConfig, *, config: routing.Config,
            repo_root: Path = _REPO_ROOT, include_infra: bool = False, strict_stances: bool = False,
            owner: str | None = None, aliases: set[str] | None = None, today: date | None = None) -> dict:
    prs = queue.get("prs") or []
    if cfg.source == "defaults":
        cfg = lanes_from_memberships(cfg, queue.get("my_teams") or {}, config)
    if aliases is None:
        aliases = alias_only_urls(repo_root)
    approver = queue.get("approver")
    ctx = {
        "cfg": cfg, "config": config, "mine": lanes_for_owner(owner, config, cfg.me),
        "include_infra": include_infra, "strict_stances": strict_stances, "cross": {},
        "today": today or datetime.now(timezone.utc).date(), "approver": approver, "handed_off": set(),
        "teams": queue.get("teams") or {}, "ownership": {},
    }
    # Ownership first: a cluster's `mine` members are the rows that are mine
    # to sequence, which the per-row pass needs to already know.
    for pr in prs:
        ctx["ownership"][pr["number"]] = ownership(pr, ctx)
    handed = {n for n, o in ctx["ownership"].items() if o["handed_off_to"]}
    ctx["handed_off"] = handed
    clusters = collision_clusters(prs)
    directional = directional_conflicts(prs, aliases)
    duplicates = duplicate_candidates(prs)
    cross: dict[int, list[str]] = {}
    for c in clusters:
        c["handed_off"] = [n for n in c["prs"] if n in handed]
        c["mine"] = [n for n in c["prs"] if n not in handed and ctx["ownership"][n]["is_mine"]]
        c["theirs"] = [n for n in c["prs"] if n not in c["mine"]]
        c["merge_order"] = [n for n in c["merge_order"] if n in c["mine"]]
        # One chip per cluster per row: `cluster:C1:overlap:2/19` (this PR's
        # place in the merge order), `cluster:C1:same-file` (no hunk overlap,
        # merges in any order) or `cluster:C1:theirs` (not mine to sequence:
        # at most one of mine in the cluster, or this row isn't mine). An
        # overlap with a handed-off or routed PR is advisory: it must not
        # gate a stamp, so only pairs with both sides mine count.
        mine = set(c["mine"])
        overlap_with: dict[int, bool] = {}
        for p in c["pairs"]:
            if p["kind"] == "overlap" and p["a"] in mine and p["b"] in mine:
                overlap_with[p["a"]] = overlap_with[p["b"]] = True
        for n in c["prs"]:
            if len(c["mine"]) <= 1 or n not in mine:
                cross.setdefault(n, []).append(f"cluster:{c['id']}:theirs")
            elif overlap_with.get(n):
                cross.setdefault(n, []).append(f"cluster:{c['id']}:overlap:{c['merge_order'].index(n) + 1}/{len(c['merge_order'])}")
            else:
                cross.setdefault(n, []).append(f"cluster:{c['id']}:same-file")
    for d in directional:
        cross.setdefault(d["adds_links_pr"], []).append(f"directional:#{d['removes_links_pr']}:{d['path']}")
    for d in duplicates:
        cross.setdefault(d["newer"], []).append(f"duplicate:#{d['older']}")
    ctx["cross"] = cross
    for pr in prs:
        analyze_pr(pr, ctx)
    for d in directional:
        d["theirs"] = d["adds_links_pr"] in handed or d["removes_links_pr"] in handed
    by_number = {p["number"]: p for p in prs}
    for c in clusters:
        c["recommendation"] = cluster_recommendation(c, by_number)
    attach_cluster_actions(prs, clusters)
    queue["do_next"] = do_next(prs, clusters, directional)
    queue["clusters"] = clusters
    queue["directional"] = directional
    queue["duplicates"] = duplicates
    queue["config"] = {**cfg.to_json(), "include_infra": include_infra, "strict_stances": strict_stances, "owner": owner or "me"}
    queue["counts"] = _counts(prs)
    queue["analyzed_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    queue["reason_codes"] = REASON_CODES
    # Kept in memory for merge_judgments(), which re-runs a row once the
    # judgments land; main() drops it before the queue is written.
    queue["_ctx"] = ctx
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


def _close_with_judgments(pr: dict) -> dict | None:
    """The close button a `close` recommendation adds. A generated row's
    closing comment is written by act.py from the judgments; anyone else's
    close needs a reason, which is the judgments' asks — so a row with none
    can't carry the recommendation."""
    n = pr["number"]
    if not can_revise(pr):
        return {"id": "close", "label": "close it out", "cmd": f"--close {n}"}
    asks = [(j.get("ask") or j.get("decision") or "").strip() for j in pr.get("judgments") or []]
    asks = [a for a in asks if a]
    if not asks:
        return None
    return {"id": "close", "label": "close with the judgments", "cmd": f'--close {n} --reason "{n}={_quote_safe("; ".join(asks))}"'}


def merge_judgments(queue: dict, judgments: dict, *, ctx: dict | None = None) -> dict:
    """Fold the model's judge output into the rows. Keys are PR numbers (as
    strings or ints); each value may carry `judgments` (list), `fix_draft`
    (dict) and `recommended` (verdict). Each touched row is recomputed. A
    judgment never answers a finding, so it never lifts a row out of
    `blocked`. A recommendation never
    lowers the computed verdict: blocked stays blocked, route stays route —
    and one the row can't carry (a close with nothing to say, a route with
    no team, a send-back on my own PR) is recorded as rejected rather than
    rendered as a button that would fail."""
    ctx = ctx or queue.get("_ctx")
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
        if ctx:
            analyze_pr(pr, ctx)
        if isinstance(pr.get("fix_draft"), dict) and not any(a["id"] == "fix" for a in pr.get("actions") or []):
            pr["actions"].append({"id": "fix", "label": "apply fixes", "cmd": f"--fix {n}"})
        rec = val.get("recommended")
        rejected = None
        if rec == "request-changes" and not can_revise(pr):
            rec = "close"  # nobody to send it back to; the lane re-queues
        if rec == "request-changes" and pr.get("author_self"):
            rejected = "request-changes: GitHub refuses a send-back on your own PR"
        elif rec in VERDICTS + ("request-changes", "close") and pr.get("verdict") == "judge":
            if rec == "close" and not any(a["id"] == "close" for a in pr["actions"]):
                a = _close_with_judgments(pr)
                if a:
                    pr["actions"].append(a)
                else:
                    rejected = "close: no judgment carries an ask to close with"
            elif rec == "route" and not any(a["id"] == "route" for a in pr["actions"]):
                targets, _ = route_targets(pr.get("domains") or [], pr.get("owners") or {}, ctx or {})
                if targets:
                    pr["actions"].append(route_action(n, targets))
                    pr["route_targets"] = targets
                else:
                    rejected = "route: no owning team for this row's lanes"
            if not rejected:
                pr["recommended"] = rec
        elif rec:
            rejected = f"{rec}: the row is {pr.get('verdict')}, not judge"
        if rejected:
            pr["rejected_recommendation"] = rejected
    # A judged row can change verdict, which can change which member leads a
    # chain; the recommendations, the cluster buttons on the rows, and the
    # terminal's batch list are all rebuilt from the rows as they stand now.
    prs = queue.get("prs") or []
    clusters = queue.get("clusters") or []
    by_number = {p["number"]: p for p in prs}
    for c in clusters:
        c["recommendation"] = cluster_recommendation(c, by_number)
    attach_cluster_actions(prs, clusters)
    if "do_next" in queue:
        queue["do_next"] = do_next(prs, clusters, queue.get("directional") or [])
    queue["counts"] = _counts(queue.get("prs") or [])
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
    queue.pop("_ctx", None)
    out = Path(args.out or args.inp)
    out.write_text(json.dumps(queue, indent=1, sort_keys=True) + "\n")
    c = queue["counts"]
    print(f"analyzed {len(queue['prs'])} PR(s): {c['stamp']} stamp · {c['judge']} judge · {c['route']} route · {c['blocked']} blocked → {out}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
