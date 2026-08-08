#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Scrape pre-merge review outcomes from pinned review comments.

Closes the feedback loop described in issue #20078 §3.2: the pipeline records
what it *spends* but not what *happens* to its findings. This script derives
per-finding outcomes (fixed / conceded / ignored / disputed) from the pinned
`<!-- CLAUDE_REVIEW N/M -->` comment sequence that the review workflows leave
on every reviewed PR. The comment is frozen once the PR closes, so it IS the
outcome ledger — no new state store, no model calls, no self-report.

Outcome taxonomy (terminal, per finding):
  * fixed                   — bullet in ✅ Resolved without a concede annotation
  * conceded                — ✅ Resolved bullet carrying `concede:`
  * ignored_outstanding     — still in 🚨 Outstanding when the PR merged
  * ignored_low_confidence  — still in ⚠️ Low-confidence when the PR merged
  * unconfirmed_at_merge    — still in 🚨/⚠️ at merge, but the review was stale
                              (last 📜 history SHA is not the merge head), so
                              "ignored" can't be honestly claimed
  * abandoned               — PR closed without merging (excluded from rates)

Orthogonal event flag: a finding is *disputed* when it carries a
`🛡️ **Disputed by <author> on YYYY-MM-DD, model held.**` line (adjudication
"held") or was conceded via a `concede:` annotation (adjudication "conceded").

Advisory style suggestions (`[style]` bullets under `#### Style suggestions`,
spelled `#### Style findings` before 2026-08-03 — this reader keys on the
bullet form, not the heading, so both parse) are
counted separately and never outcome-classified — they are regenerated fresh
on every re-review and never move to ✅ Resolved, so per-finding tracking
would lie. Blocker-tier style findings (`[style-blocker]` bullets in 🚨) are
deliberately NOT matched by STYLE_BULLET_RE (`[style]` is not a substring of
`[style-blocker]`): they persist across re-reviews and move to ✅ Resolved
like any outstanding finding, so they ARE outcome-classified.

This is a telemetry READER, never a gate: unparseable or legacy comment
formats degrade to `parse_confidence: "low"` (counts-only) or
`status: "no_review_data"`, and the aggregate reports how often that happened
so silent degradation stays visible.

Usage:
  scrape-review-outcomes.py --pr 20123 [--repo owner/repo]
      One PR -> one outcome record (JSON to stdout).
  scrape-review-outcomes.py --closed-since 2026-07-02 [--repo owner/repo]
      All review-labeled PRs closed since the date -> per-PR records +
      window aggregate (JSON to stdout). This is what digest.py calls.
  scrape-review-outcomes.py --closed-since 2026-04-01 --stats
      Same scrape, rendered as a markdown tuning report (per-verdict-category
      fix/concede/ignore/dispute rates) for the quarterly outcome review.
  scrape-review-outcomes.py --self-test
      Run embedded smoke checks (no network).

Parsing reuses validate-pinned.py's body helpers (find_section,
extract_bucket_bullets, extract_count_table_row, extract_trail_records,
extract_bullet_prefix) so the comment-format contract has exactly one parser.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Single source of truth for pinned-body parsing. validate-pinned.py's name is
# hyphenated, so import by path; its main() is __main__-guarded, so importing
# has no side effects (same pattern as scripts/content-review/record-review.py
# importing select-articles.py).
_spec = importlib.util.spec_from_file_location("validate_pinned", HERE / "validate-pinned.py")
_vp = importlib.util.module_from_spec(_spec)
# Register before exec: validate-pinned.py defines dataclasses, and the
# dataclass machinery resolves the defining module through sys.modules.
sys.modules["validate_pinned"] = _vp
_spec.loader.exec_module(_vp)

DEFAULT_REPO = "pulumi/docs"
MARKER_RE = re.compile(r"^<!-- CLAUDE_REVIEW (\d+)/(\d+) -->")
# Canonical annotation shapes are owned by validate-pinned.py (schema v18's
# `outcome-annotation-shape` rule enforces them going forward); this reader
# additionally accepts a looser legacy dispute form, since old pinned comments
# predate the rule and a telemetry reader must never gate.
DISPUTED_RE = _vp.DISPUTED_ANNOTATION_RE
DISPUTED_LEGACY_RE = re.compile(r"🛡️?\s*\*{0,2}Disputed by\s+@?(\S+?)\s+on\s+(\d{4}-\d{2}-\d{2})")
CONCEDE_RE = _vp.CONCEDE_ANNOTATION_RE
STYLE_BULLET_RE = re.compile(r"^\s*-\s+\*\*line \d+:?\*\*|\[style\]")
# SHA-ish tokens in 📜 history lines. Not anchored to a whole parenthetical:
# the fix-response line renders `(2 new commits, d0c76f0)` (update.md Case 1),
# so the SHA shares its parens with prose. Requiring at least one a-f letter
# keeps pure-digit runs (issue numbers, dates) from matching.
HISTORY_SHA_RE = re.compile(r"\b(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}\b")
# Column-0 finding-paragraph start, mirroring extract_bucket_bullets.
FINDING_START_RE = re.compile(r"^(?:- )?\*\*\S")
# Branch prefixes of the repo's own automation; their PRs' review outcomes are
# reported separately from human-authored PRs.
BOT_BRANCH_PREFIXES = ("content-review/", "fix-broken-links")
BOT_LOGINS = {"pulumi-bot", "dependabot[bot]", "github-actions[bot]"}
OUTCOME_KEYS = (
    "fixed",
    "conceded",
    "ignored_outstanding",
    "ignored_low_confidence",
    "unconfirmed_at_merge",
    "abandoned",
)


def log(msg: str) -> None:
    print(f"scrape-review-outcomes: {msg}", file=sys.stderr)


# ---- gh access ---------------------------------------------------------------


def run_gh(args: list[str]) -> str:
    """Run a gh command; return stdout, or "" on failure (logged to stderr)."""
    try:
        proc = subprocess.run(["gh", *args], capture_output=True, text=True, check=True)
        return proc.stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        detail = exc.stderr.strip() if hasattr(exc, "stderr") and exc.stderr else str(exc)
        log(f"warning: gh {' '.join(args[:4])}... failed: {detail}")
        return ""


def fetch_pr_meta(repo: str, pr: int) -> dict | None:
    out = run_gh(
        [
            "pr", "view", str(pr), "--repo", repo,
            "--json",
            "number,title,url,state,mergedAt,closedAt,headRefOid,headRefName,author,labels",
        ]
    )
    if not out.strip():
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        log(f"warning: could not parse pr view JSON for #{pr}")
        return None


def fetch_pinned_bodies(repo: str, pr: int) -> list[str]:
    """Return the bodies of every CLAUDE_REVIEW N/M comment, ordered by N.

    Mirrors pinned-comment.sh list_pinned_comments/fetch, but keeps the
    filtering in Python (jq compact output = one JSON object per line).
    """
    out = run_gh(
        [
            "api", "--paginate", f"repos/{repo}/issues/{pr}/comments",
            "--jq", '.[] | {id: .id, body: .body} | @json',
        ]
    )
    tagged = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            # --jq '@json' double-encodes: each output line is a JSON string
            # containing a JSON object.
            obj = json.loads(json.loads(line))
        except (json.JSONDecodeError, TypeError):
            continue
        body = obj.get("body") or ""
        m = MARKER_RE.match(body.split("\n", 1)[0])
        if m:
            tagged.append((int(m.group(1)), body))
    tagged.sort(key=lambda t: t[0])
    return [body for _, body in tagged]


def list_closed_prs(repo: str, since: str) -> list[dict]:
    """Closed PRs since `since` (YYYY-MM-DD) that carry any review:* label."""
    out = run_gh(
        [
            "pr", "list", "--repo", repo, "--state", "closed", "--limit", "300",
            "--search", f"closed:>={since}",
            "--json", "number,labels,closedAt",
        ]
    )
    try:
        raw = json.loads(out) if out.strip() else []
    except json.JSONDecodeError:
        log("warning: could not parse pr list JSON")
        return []
    return [
        pr for pr in raw
        if any(lbl.get("name", "").startswith("review:") for lbl in pr.get("labels", []))
    ]


# ---- body parsing --------------------------------------------------------------


def first_line(paragraph: str, limit: int = 200) -> str:
    text = paragraph.strip().splitlines()[0] if paragraph.strip() else ""
    return text[:limit]


def extract_finding_paragraphs(body: str, heading_substring: str) -> list[str]:
    """Group a bucket section into per-finding paragraphs.

    A paragraph starts at a column-0 `**`-prefixed line (the same shape
    extract_bucket_bullets counts) and runs until the next one or the section
    end, so annotation lines rendered under the finding (🛡️ Disputed,
    concede reasons, suggestion blocks) stay attached to their finding.
    """
    span = _vp.find_section(body, heading_substring)
    if span is None:
        return []
    start, end = span
    lines = body.splitlines()[start + 1 : end]
    paragraphs: list[str] = []
    current: list[str] = []
    for line in lines:
        if FINDING_START_RE.match(line):
            if current:
                paragraphs.append("\n".join(current))
            current = [line]
        elif current:
            current.append(line)
    if current:
        paragraphs.append("\n".join(current))
    return paragraphs


def build_verdict_index(body: str) -> dict[str, str]:
    """Map every L-anchor in the 🔍 trail to its canonical verdict word."""
    index: dict[str, str] = {}
    for rec in _vp.extract_trail_records(body):
        word = rec.get("verdict_word")
        if not word:
            continue
        for ref in rec.get("line_refs", []):
            index.setdefault(ref, word)
    return index


def verdict_for(paragraph: str, verdict_index: dict[str, str]) -> str | None:
    prefix = _vp.extract_bullet_prefix(paragraph.splitlines()[0])
    if prefix and prefix in verdict_index:
        return verdict_index[prefix]
    if prefix:
        # Fall back to matching on the start line number (a bucket range can
        # differ slightly from the trail's collapsed refs).
        start = prefix.split("-")[0]
        for ref, word in verdict_index.items():
            if ref.split("-")[0] == start:
                return word
    return None


def parse_history(body: str) -> dict:
    text = _vp.section_text(body, "📜 Review history")
    entries = [ln for ln in text.splitlines() if ln.strip().startswith("- ")]
    shas = HISTORY_SHA_RE.findall(text)
    return {"entries": len(entries), "last_sha": shas[-1] if shas else None}


def classify_finding(paragraph: str, bucket: str, merged: bool, review_current: bool) -> dict:
    is_style = bool(STYLE_BULLET_RE.search(paragraph.splitlines()[0]))
    disputed = DISPUTED_RE.search(paragraph) or DISPUTED_LEGACY_RE.search(paragraph)
    conceded = bool(CONCEDE_RE.search(paragraph))
    if bucket == "resolved":
        outcome = "conceded" if conceded else "fixed"
    elif not merged:
        outcome = "abandoned"
    elif not review_current:
        outcome = "unconfirmed_at_merge"
    elif bucket == "outstanding":
        outcome = "ignored_outstanding"
    else:
        outcome = "ignored_low_confidence"
    record = {
        "bucket": bucket,
        "style": is_style,
        "text": first_line(paragraph),
        "outcome": outcome,
    }
    if disputed:
        record["disputed"] = {
            "by": disputed.group(1).rstrip(",.*"),
            "on": disputed.group(2),
            "adjudication": "conceded" if bucket == "resolved" else "held",
        }
    elif bucket == "resolved" and conceded:
        record["disputed"] = {"by": None, "on": None, "adjudication": "conceded"}
    return record


def scrape_body(body: str, merged: bool, head_sha: str | None) -> dict:
    """Parse one concatenated pinned-comment body into an outcome record core."""
    counts = _vp.extract_count_table_row(body)
    history = parse_history(body)
    review_current = True
    if merged and head_sha and history["last_sha"]:
        review_current = head_sha.startswith(history["last_sha"])
    verdict_index = build_verdict_index(body)

    buckets = {
        "outstanding": "🚨 Outstanding",
        "low_confidence": "⚠️ Low-confidence",
        "resolved": "✅ Resolved",
    }
    findings: list[dict] = []
    style_count = 0
    for bucket, heading in buckets.items():
        for paragraph in extract_finding_paragraphs(body, heading):
            record = classify_finding(paragraph, bucket, merged, review_current)
            if record["style"]:
                style_count += 1
                continue
            word = verdict_for(paragraph, verdict_index)
            if word:
                record["verdict"] = word
            findings.append(record)

    outcome_counts = {k: 0 for k in OUTCOME_KEYS}
    for f in findings:
        outcome_counts[f["outcome"]] += 1
    disputes = [
        {**f["disputed"], "finding": f["text"]} for f in findings if f.get("disputed")
    ]

    parsed_anything = counts is not None or findings or history["entries"]
    return {
        "counts_table": counts,
        "findings": findings,
        "style_findings": style_count,
        "outcomes": outcome_counts,
        "disputes": disputes,
        "review_events": history["entries"],
        "review_current_at_merge": review_current,
        "pre_existing": len(extract_finding_paragraphs(body, "💡 Pre-existing")),
        "parse_confidence": "high" if counts is not None else ("low" if parsed_anything else "none"),
    }


# ---- per-PR record --------------------------------------------------------------


def author_kind(meta: dict) -> str:
    login = ((meta.get("author") or {}).get("login") or "").lower()
    branch = meta.get("headRefName") or ""
    if login in BOT_LOGINS or login.endswith("[bot]"):
        return "bot"
    if any(branch.startswith(p) for p in BOT_BRANCH_PREFIXES):
        return "bot"
    return "human"


def scrape_pr(repo: str, pr: int) -> dict:
    meta = fetch_pr_meta(repo, pr)
    if meta is None:
        return {"pr": pr, "status": "pr_unavailable"}
    merged = bool(meta.get("mergedAt"))
    record = {
        "pr": pr,
        "title": meta.get("title"),
        "url": meta.get("url"),
        "merged": merged,
        "closed_at": meta.get("mergedAt") or meta.get("closedAt"),
        "author_kind": author_kind(meta),
    }
    bodies = fetch_pinned_bodies(repo, pr)
    if not bodies:
        # Short-circuited (review:trivial etc.), comment deleted, or never
        # reviewed. Counted, never rated.
        record["status"] = "no_review_data"
        return record
    body = "\n".join(bodies)
    record.update(scrape_body(body, merged, meta.get("headRefOid")))
    record["status"] = "scraped"
    record["comment_count"] = len(bodies)
    return record


# ---- aggregation --------------------------------------------------------------


def empty_outcomes() -> dict:
    return {k: 0 for k in OUTCOME_KEYS}


def aggregate(records: list[dict]) -> dict:
    agg = {
        "prs_scraped": 0,
        "prs_no_review_data": 0,
        "prs_parse_low": 0,
        "outcomes": {"human": empty_outcomes(), "bot": empty_outcomes()},
        "style_findings": 0,
        "disputes": [],
        "merged_with_outstanding": [],
        "by_verdict": {},
    }
    for rec in records:
        if rec.get("status") != "scraped":
            agg["prs_no_review_data"] += 1
            continue
        agg["prs_scraped"] += 1
        if rec.get("parse_confidence") != "high":
            agg["prs_parse_low"] += 1
        kind = rec.get("author_kind", "human")
        for key, n in rec.get("outcomes", {}).items():
            agg["outcomes"][kind][key] += n
        agg["style_findings"] += rec.get("style_findings", 0)
        for dispute in rec.get("disputes", []):
            agg["disputes"].append({"pr": rec["pr"], **dispute})
        outstanding = [
            f["text"] for f in rec.get("findings", [])
            if f["outcome"] == "ignored_outstanding"
        ]
        if outstanding:
            agg["merged_with_outstanding"].append(
                {"pr": rec["pr"], "title": rec.get("title"), "url": rec.get("url"), "findings": outstanding}
            )
        for f in rec.get("findings", []):
            word = f.get("verdict")
            if not word:
                continue
            per = agg["by_verdict"].setdefault(word, empty_outcomes())
            per[f["outcome"]] += 1
    return agg


def render_stats(agg: dict, since: str) -> str:
    """Markdown tuning report for the quarterly outcome review."""

    def rate(n: int, d: int) -> str:
        return f"{100 * n / d:.0f}%" if d else "–"

    lines = [
        f"# Review outcome stats since {since}",
        "",
        f"PRs with scraped reviews: **{agg['prs_scraped']}** "
        f"(+{agg['prs_no_review_data']} with no review data, "
        f"{agg['prs_parse_low']} parsed at low confidence)",
        "",
        "| Author | Fixed | Conceded | Ignored 🚨 | Ignored ⚠️ | Unconfirmed | Abandoned |",
        "| :--- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for kind in ("human", "bot"):
        o = agg["outcomes"][kind]
        lines.append(
            f"| {kind} | {o['fixed']} | {o['conceded']} | {o['ignored_outstanding']} "
            f"| {o['ignored_low_confidence']} | {o['unconfirmed_at_merge']} | {o['abandoned']} |"
        )
    lines += [
        "",
        "## Per verdict category",
        "",
        "High concede/ignore rates mark carve-outs to demote or prune;",
        "high fix rates on recurring findings mark Vale-promotion candidates.",
        "",
        "| Verdict | Total | Fix rate | Concede rate | Ignored-at-merge rate |",
        "| :--- | ---: | ---: | ---: | ---: |",
    ]
    for word in sorted(agg["by_verdict"]):
        o = agg["by_verdict"][word]
        total = sum(o.values())
        ignored = o["ignored_outstanding"] + o["ignored_low_confidence"]
        lines.append(
            f"| {word} | {total} | {rate(o['fixed'], total)} "
            f"| {rate(o['conceded'], total)} | {rate(ignored, total)} |"
        )
    if agg["merged_with_outstanding"]:
        lines += ["", "## Merged over 🚨 Outstanding findings", ""]
        for item in agg["merged_with_outstanding"]:
            lines.append(f"- #{item['pr']} {item['title']}")
            for text in item["findings"]:
                lines.append(f"  - {text}")
    if agg["disputes"]:
        lines += ["", "## Disputes", ""]
        for d in agg["disputes"]:
            who = f"@{d['by']}" if d.get("by") else "author"
            lines.append(f"- #{d['pr']} {who} → **{d['adjudication']}** — {d['finding']}")
    lines.append("")
    return "\n".join(lines)


# ---- self-test --------------------------------------------------------------

FIXTURE = """\
<!-- CLAUDE_REVIEW 1/1 -->
## Pre-merge Review — Last updated 2026-07-01T00:00:00Z

| 🚨 Outstanding | ⚠️ Low-confidence | 💡 Pre-existing | ✅ Resolved |
| :---: | :---: | :---: | :---: |
| **1** | **2** | **0** | **2** |

### 🔍 Verification trail

<details>
<summary><strong>3</strong> claims extracted · <strong>1</strong> verified · <strong>1</strong> unverifiable · <strong>1</strong> contradicted</summary>

- L10 "the flag defaults to true" → ❌ contradicted (docs say false)
- L20 "supports 3 clouds" → 🤷 unverifiable (no citation)
- L30 "released in v3.0" → ✅ verified (changelog)
</details>

### 🚨 Outstanding in this PR

*These must be resolved or refuted before merging.*

- **[L10]** The flag default is wrong.
  🛡️ **Disputed by alice on 2026-06-30, model held.** Docs contradict.

### ⚠️ Low-confidence

*Review each and resolve as appropriate — these don't block the PR.*

- **[L20]** Please cite a source for the cloud count.

#### Style findings

- **line 42:** [style] _substitution_ — Use 'select' instead of 'click'.

### ✅ Resolved since last review

- **[L30]** Version claim corrected. (resolved in abc1234)

- **[L44]** concede: author confirms intentional pattern.

### 📜 Review history

- 2026-06-29T00:00:00Z — initial review (abc1234)
- 2026-07-01T00:00:00Z — re-reviewed after fix push (deadbee)
"""


def self_test() -> int:
    failures = []

    def check(name: str, cond: bool) -> None:
        (print(f"  ok  {name}") if cond else failures.append(name))
        if not cond:
            print(f"  FAIL {name}")

    merged_head = "deadbee0000000000000000000000000000000ff"
    rec = scrape_body(FIXTURE, merged=True, head_sha=merged_head)
    check("parse_confidence high", rec["parse_confidence"] == "high")
    check("counts table parsed", rec["counts_table"] == {"outstanding": 1, "low_confidence": 2, "pre_existing": 0, "resolved": 2})
    check("one ignored_outstanding", rec["outcomes"]["ignored_outstanding"] == 1)
    check("one ignored_low_confidence", rec["outcomes"]["ignored_low_confidence"] == 1)
    check("one fixed", rec["outcomes"]["fixed"] == 1)
    check("one conceded", rec["outcomes"]["conceded"] == 1)
    check("style counted separately", rec["style_findings"] == 1)
    check("two disputes", len(rec["disputes"]) == 2)
    held = [d for d in rec["disputes"] if d["adjudication"] == "held"]
    check("held dispute names disputer", held and held[0]["by"] == "alice")
    check("verdict joined from trail", any(f.get("verdict") == "contradicted" for f in rec["findings"]))
    check("review current at merge", rec["review_current_at_merge"] is True)

    stale = scrape_body(FIXTURE, merged=True, head_sha="0123456789abcdef0123456789abcdef01234567")
    check("stale review -> unconfirmed", stale["outcomes"]["unconfirmed_at_merge"] == 2)
    check("stale review -> no ignored", stale["outcomes"]["ignored_outstanding"] == 0)

    closed = scrape_body(FIXTURE, merged=False, head_sha=None)
    check("unmerged -> abandoned", closed["outcomes"]["abandoned"] == 2)
    check("resolved still fixed on unmerged", closed["outcomes"]["fixed"] == 1)

    empty = scrape_body("no review here", merged=True, head_sha=None)
    check("garbage -> parse none", empty["parse_confidence"] == "none")

    agg = aggregate([
        {"status": "scraped", "pr": 1, "author_kind": "human", "parse_confidence": "high",
         **{k: rec[k] for k in ("outcomes", "style_findings", "disputes", "findings")}},
        {"status": "no_review_data", "pr": 2},
    ])
    check("aggregate scraped count", agg["prs_scraped"] == 1)
    check("aggregate no-data count", agg["prs_no_review_data"] == 1)
    check("aggregate human fixed", agg["outcomes"]["human"]["fixed"] == 1)
    check("merged_with_outstanding listed", len(agg["merged_with_outstanding"]) == 1)
    check("by_verdict contradicted", "contradicted" in agg["by_verdict"])
    check("stats renders", "Per verdict category" in render_stats(agg, "2026-01-01"))

    if failures:
        print(f"{len(failures)} self-test failure(s)")
        return 1
    print("self-test passed")
    return 0


# ---- main --------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--pr", type=int, help="scrape a single PR")
    ap.add_argument("--closed-since", help="scrape review-labeled PRs closed since YYYY-MM-DD")
    ap.add_argument("--stats", action="store_true", help="render a markdown tuning report instead of JSON")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()
    if args.pr:
        json.dump(scrape_pr(args.repo, args.pr), sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
        return 0
    if args.closed_since:
        try:
            datetime.strptime(args.closed_since, "%Y-%m-%d")
        except ValueError:
            ap.error("--closed-since must be YYYY-MM-DD")
        candidates = list_closed_prs(args.repo, args.closed_since)
        log(f"{len(candidates)} review-labeled PRs closed since {args.closed_since}")
        records = [scrape_pr(args.repo, pr["number"]) for pr in candidates]
        agg = aggregate(records)
        if args.stats:
            sys.stdout.write(render_stats(agg, args.closed_since))
            return 0
        json.dump(
            {
                "since": args.closed_since,
                "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "aggregate": agg,
                "prs": records,
            },
            sys.stdout, indent=2, ensure_ascii=False,
        )
        sys.stdout.write("\n")
        return 0
    ap.error("one of --pr, --closed-since, --self-test is required")
    return 2


if __name__ == "__main__":
    sys.exit(main())
