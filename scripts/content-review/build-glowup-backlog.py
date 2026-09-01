#!/usr/bin/env python3
"""Assemble the glow-up worker's backlog from logged content-review feedback.

The fix lane banks its judgment-level material instead of applying it: the
"Findings not applied" section of each review PR, the flag-only "Screenshot
check" and "Rendered content" observations, and the ledger's `clarity_flag` /
`skipped_findings` counters. This deterministic pre-step (run by the workflow
BEFORE the model, like the claim pipeline) collects that record for one page
into `.glowup-backlog.json`, so the glow-up skill starts from the accumulated
backlog rather than a cold read:

    {"schema_version": 1, "slug": ..., "path": ..., "generated": ...,
     "clarity_flag": bool, "skipped_findings": int,
     "source_prs": [{"number": 123, "url": ...}, ...],
     "banked": [{"id": "pr123-findings-1", "section": "Findings not applied",
                 "source_pr": 123, "text": "<the row/bullet>"}, ...],
     "notes": ["<degradation notes, if any>"]}

Sources, in order of authority:

1. The structured findings record (`record-page-findings.py`), when the page has
   one. Forward-only: pages last reviewed before 2026-08-19 have none.
2. Every prior review PR for the page, found by HEAD REF. An earlier version of
   this file asserted that reused branch names made older PRs undiscoverable, and
   so read only the pointer the ledger happened to carry. That was wrong, and it
   is why #20984 recovered nothing: `gh pr list --head <branch> --state all`
   returns every PR that branch has ever carried, closed and merged included
   (`content-review/docs-iac-concepts-providers` returns #20953, #20927 and
   #20503). All three canonical heads are queried — fix, retire and glow-up —
   because a prior glow-up's "Backlog declined" rows are debt too: they are what
   `record-review.py` counts into `skipped_findings`, and the selector re-picks
   the page on that number, so the backlog has to be able to name it.
3. The ledger/queue PR pointer and any `--pr` extras, as defence in depth.

Section extraction is heading-based, tolerant, and lane-aware — a glow-up PR body
uses different headings from a fix PR's. Recovery never fails the run: the
`recovery` block records which of four outcomes happened (`recovered`,
`no_prior_prs`, `gh_unavailable`, `prs_carried_nothing`) and the skill falls back
to its taxonomy-only sweep. When the ledger says findings were banked and none
could be recovered, the backlog is stamped `degraded` and a `::warning::` is
emitted — a silently empty backlog reads exactly like a clean page, which is how
#20984 shipped a PR announcing it had nothing to do while 17 findings waited.

`--pr-json <file|->` injects the discovered PR set for tests (a JSON list of
{number, url, body, headRefName}), replacing every `gh` call.

Self-contained smoke checks: `python3 build-glowup-backlog.py --self-test`.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = 1

BRANCH_PREFIX = "content-review/"

# The banked sections, in the order they appear in the fix-lane PR body
# (compose-pr-body.py). "Fixes applied" is deliberately absent — those landed.
FIX_BANKED_SECTIONS = ("Findings not applied", "Screenshot check", "Rendered content")
# A glow-up PR body uses its own headings. "Backlog executed" is absent for the
# same reason "Fixes applied" is: that work landed. "Backlog declined" is the
# debt — the count record-review.py writes into skipped_findings, which is what
# re-selects the page, so it has to be recoverable or the counter is unbacked.
GLOWUP_BANKED_SECTIONS = ("Backlog declined", "Screenshot check")
BANKED_SECTIONS = FIX_BANKED_SECTIONS  # back-compat alias

# Section content that means "nothing banked here" — composer pre-fills and
# reviewer boilerplate, not findings.
NOISE_LINES = {
    "no images.", "skipped.", "none.", "n/a", "-", "—",
}

# The same thing, matched as a PREFIX. Exact-line matching was enough while
# nothing was ever recovered; the first live run against a real page showed why
# it isn't — the composer's pre-fills and the model's nothing-here lines all
# CONTINUE past the phrase ("No images. The page source references no
# screenshots...", "None — the backlog was empty (...)", "Skipped — the page
# source uses only render-safe chrome..."), so every one of them was banked as
# a finding for the model to dutifully decline.
NOISE_PREFIX_RE = re.compile(
    r"^[-*+_\s|]*(no images|none|n/?a|skipped|"
    r"nothing judgment-level was pre-found)\b", re.I)

# The composer closes "Findings not applied" with a routing trailer telling a
# human where the deferrals go. Its wording has changed over the lane's life
# ("For the judgment-level items above, run ..." became "The items above are
# banked ..."), so match the invariant rather than either phrasing: it is the
# line that points at the /glow-up command instead of describing a finding.
TRAILER_RE = re.compile(r"`?/glow-up\s+content/", re.I)


def log(msg: str) -> None:
    print(f"build-glowup-backlog: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::build-glowup-backlog: {msg}", file=sys.stderr)


def heads_for(slug: str) -> list[str]:
    """The three canonical branch names a review of this page can have used."""
    return [f"{BRANCH_PREFIX}{slug}",
            f"{BRANCH_PREFIX}retire-{slug}",
            f"{BRANCH_PREFIX}glowup-{slug}"]


def sections_for(head: str) -> tuple[str, ...]:
    """The banked-section vocabulary of the lane that opened this PR.

    Keyed off the head ref rather than guessed from the body: the branch name
    is what the publish job derived the lane from in the first place.
    """
    return (GLOWUP_BANKED_SECTIONS if head.startswith(f"{BRANCH_PREFIX}glowup-")
            else FIX_BANKED_SECTIONS)


def extract_sections(body: str,
                     wanted: tuple[str, ...] = FIX_BANKED_SECTIONS
                     ) -> dict[str, list[str]]:
    """Per banked section, the non-noise content lines (rows/bullets/prose)."""
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for raw in (body or "").splitlines():
        line = raw.strip()
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            title = m.group(1).strip()
            current = title if title in wanted else None
            continue
        if current is None or not line:
            continue
        if line.startswith("<!--"):
            continue
        # Table chrome (header/separator rows) is structure, not a finding.
        if re.fullmatch(r"\|?[\s|:-]+\|?", line):
            continue
        if line.lower().rstrip("_* ").lstrip("_* ") in NOISE_LINES:
            continue
        if NOISE_PREFIX_RE.match(line) or TRAILER_RE.search(line):
            continue
        sections.setdefault(current, []).append(line)
    return sections


def fetch_pr(number: int) -> dict | None:
    proc = subprocess.run(
        ["gh", "pr", "view", str(number), "--json", "number,url,body"],
        capture_output=True, text=True, check=False,
    )
    if proc.returncode != 0:
        warn(f"gh pr view {number} failed: {proc.stderr.strip()[:200]}")
        return None
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        warn(f"gh pr view {number} returned unparseable JSON")
        return None


def prs_for_head(head: str) -> list[dict] | None:
    """Every PR that has ever used this head ref, or None if the query failed.

    None and [] are deliberately distinct: "GitHub would not answer" and "this
    page has never been reviewed" degrade the same way but are not the same
    fact, and collapsing them is what made #20984's PR body describe a lookup
    failure that never happened.
    """
    proc = subprocess.run(
        ["gh", "pr", "list", "--head", head, "--state", "all", "--limit", "50",
         "--json", "number,url,body,headRefName,createdAt"],
        capture_output=True, text=True, check=False,
    )
    if proc.returncode != 0:
        warn(f"gh pr list --head {head} failed: {proc.stderr.strip()[:200]}")
        return None
    try:
        found = json.loads(proc.stdout or "[]")
    except json.JSONDecodeError:
        warn(f"gh pr list --head {head} returned unparseable JSON")
        return None
    return [p for p in found if isinstance(p, dict)]


def discover_prs(slug: str, extra_numbers: list[int],
                 pr_json: str | None) -> tuple[list[dict], dict]:
    """Every prior review PR for this page, plus how the search went.

    `pr_json` injects the discovered set for tests and suppresses every `gh`
    call — the property the whole self-test suite depends on.
    """
    heads = heads_for(slug)
    recovery = {"heads_queried": heads, "prs_found": 0, "prs_unreachable": [],
                "prs_without_sections": [], "state": "no_prior_prs"}

    if pr_json is not None:
        raw = sys.stdin.read() if pr_json == "-" else Path(pr_json).read_text()
        prs = [p for p in json.loads(raw or "[]") if isinstance(p, dict)]
        recovery["prs_found"] = len(prs)
        recovery["state"] = "recovered" if prs else "no_prior_prs"
        return prs, recovery

    seen: set[int] = set()
    prs: list[dict] = []
    failed_heads = 0
    for head in heads:
        found = prs_for_head(head)
        if found is None:
            failed_heads += 1
            recovery["prs_unreachable"].append(head)
            continue
        for pr in found:
            n = int(pr.get("number") or 0)
            if n and n not in seen:
                seen.add(n)
                prs.append(pr)
    # Defence in depth: the ledger/queue pointer and any --pr extras. After the
    # head query these are nearly always redundant, which is the point — the
    # pointer is the thing that kept going missing.
    for n in extra_numbers:
        if n in seen:
            continue
        pr = fetch_pr(n)
        if pr is None:
            recovery["prs_unreachable"].append(f"#{n}")
        else:
            seen.add(n)
            prs.append(pr)

    # Belt and braces: a PR that arrives without a body would extract zero
    # sections and be indistinguishable from one that genuinely banked nothing,
    # so fetch it individually rather than let it read as an empty backlog.
    for pr in prs:
        if not pr.get("body"):
            full = fetch_pr(int(pr.get("number") or 0))
            if full and full.get("body"):
                pr["body"] = full["body"]

    prs.sort(key=lambda p: int(p.get("number") or 0))
    recovery["prs_found"] = len(prs)
    if prs:
        recovery["state"] = "recovered"
    elif failed_heads:
        # ANY unanswered head, not just all three. Requiring total failure meant
        # one dead query plus two empty ones reported "no review PR has ever
        # used <all three heads>" — naming heads that were never successfully
        # asked. That is the same collapse this block exists to prevent, just
        # at partial rather than total failure.
        recovery["state"] = "gh_unavailable"
    return prs, recovery


def load_entry(ledger_dir: Path, slug: str) -> dict:
    f = ledger_dir / f"{slug}.json"
    if not f.is_file():
        return {}
    try:
        entry = json.loads(f.read_text())
        return entry if isinstance(entry, dict) else {}
    except (OSError, json.JSONDecodeError) as e:
        warn(f"ledger entry {f} unreadable ({e})")
        return {}


def banked_from_findings(record: dict | None) -> list[dict]:
    """Deferred findings from the structured record, if one exists.

    This is the spine: `record-page-findings.py` writes every finding a review
    produced, with an `applied` flag, next to the ledger. Reading it beats
    scraping the PR body on every count that matters — it cannot be edited by
    someone tidying a markdown table, it does not fail silently when a heading
    is renamed, and it exists for every review rather than only the latest one
    a reused branch happens to point at.

    Only `applied: false` items are banked. An applied finding is done, and
    re-proposing finished work is exactly what erodes trust in the lane.
    """
    if not isinstance(record, dict):
        return []
    out = []
    for f in record.get("findings") or []:
        if not isinstance(f, dict) or f.get("applied"):
            continue
        text = str(f.get("label") or "").strip()
        if not text:
            continue
        detail = str(f.get("detail") or "").strip()
        out.append({
            "id": f"findings-{f.get('id', len(out) + 1)}",
            "section": "Findings not applied",
            "source_pr": None,
            "source": "findings-record",
            "text": text + (f" — {detail}" if detail else ""),
        })
    return out


def build(article: dict, entry: dict, prs: list[dict],
          findings_record: dict | None = None,
          recovery: dict | None = None) -> dict:
    backlog = {
        "schema_version": SCHEMA_VERSION,
        "slug": article.get("slug"),
        "path": article.get("path"),
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "clarity_flag": bool(entry.get("clarity_flag") or article.get("clarity_flag")),
        "skipped_findings": int(entry.get("skipped_findings")
                                or article.get("skipped_findings") or 0),
        "source_prs": [],
        "banked": [],
        "notes": [],
        # True when the ledger says findings were banked and none could be
        # recovered. Always present so a consumer can rely on the key.
        "degraded": False,
    }
    # Structured record first. The PR-body scrape still runs and is still
    # merged in: it is the only place the model's one-line REASON for deferring
    # lives, plus the flag-only screenshot and rendered-content observations,
    # which are prose by nature and have no artifact behind them. So the
    # record is the spine and the prose is enrichment — strictly more than
    # before, never less.
    structured = banked_from_findings(findings_record)
    if structured:
        backlog["banked"].extend(structured)
        backlog["findings_record"] = {
            "slug": (findings_record or {}).get("slug"),
            "reviewed_at": (findings_record or {}).get("reviewed_at"),
            "counts": (findings_record or {}).get("counts"),
        }

    recovery = dict(recovery or {"heads_queried": [], "prs_found": len(prs),
                                 "prs_unreachable": [], "prs_without_sections": [],
                                 "state": "recovered" if prs else "no_prior_prs"})
    recovery["prs_without_sections"] = []

    for pr in prs:
        number = int(pr.get("number") or 0)
        head = str(pr.get("headRefName") or "")
        backlog["source_prs"].append({"number": number, "url": pr.get("url"),
                                      "head": head})
        wanted = sections_for(head)
        sections = extract_sections(pr.get("body") or "", wanted)
        before = len(backlog["banked"])
        for section in wanted:
            declined = section == "Backlog declined"
            for i, text in enumerate(sections.get(section, []), start=1):
                item = {
                    "id": f"pr{number}-{section.lower().split()[0]}-{i}",
                    "section": section,
                    "source_pr": number,
                    # A previously-declined item is re-banked, not dropped —
                    # dropping it makes debt vanish silently, which is the bug
                    # class this file exists to close — but it is tagged so the
                    # model knows it was already turned down once and a human
                    # can see a decline loop forming.
                    "source": "glowup-declined" if declined else "pr-body",
                    "text": text,
                }
                if declined:
                    item["declined_by_pr"] = number
                _bank(backlog["banked"], item)
        if len(backlog["banked"]) == before:
            recovery["prs_without_sections"].append(number)

    if backlog["banked"]:
        if recovery["state"] != "gh_unavailable":
            recovery["state"] = "recovered"
    elif prs:
        recovery["state"] = "prs_carried_nothing"

    backlog["recovery"] = recovery
    if not backlog["banked"]:
        backlog["notes"].append(_recovery_note(recovery))
        # The ledger's counters ARE the selection criterion, so a page selected
        # for 17 banked findings that recovers none is self-contradictory. It
        # used to pass through three programs without a word, and the PR then
        # announced a taxonomy-only glow-up as though the page were clean.
        if backlog["skipped_findings"] > 0 or backlog["clarity_flag"]:
            backlog["degraded"] = True
            warn(f"ledger records {backlog['skipped_findings']} banked finding(s)"
                 f"{' and a clarity flag' if backlog['clarity_flag'] else ''} for "
                 f"{backlog['slug']}, but none could be recovered "
                 f"({recovery['state']}) — this glow-up is taxonomy-only")
    return backlog


_EXTRACT_CLAIMS = (Path(__file__).resolve().parent.parent.parent / ".claude" / "commands"
                   / "docs-review" / "scripts" / "extract-claims.py")


def _stance_patterns() -> list:
    """The extractor's positioning/comparison regexes, imported by path so the
    vocabulary is the pre-merge review's own; unavailable → no filtering."""
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("extract_claims", _EXTRACT_CLAIMS)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return list(mod.POSITIONING_RES) + list(mod.COMPARISON_RES)
    except Exception as e:  # noqa: BLE001
        warn(f"extract-claims.py unavailable ({e}); editorial stances are not filtered from the backlog")
        return []


_STANCE_PATTERNS = None


def is_editorial_stance(text: str) -> bool:
    """True for a banked CLAIM row whose finding text is an editorial stance
    ("the recommended approach", "unlike Terraform", "the fastest path").

    Stances are never fixable work: a page's own framing has no external
    ground truth, the verifier lands them `not-a-claim`, and executing one
    as a finding is how PR #21291 rewrote a section's framing off a July
    "recommended approach" verdict. Since merge-claims.py schema v2 they
    never reach the verifier at all; this catches the ones already banked
    from older PR bodies. Only the FINDING half of the row is tested — the
    text before the first dash — never the reviewer's reason, which is free
    to say "the page frames X as primary" without becoming a stance itself.
    """
    global _STANCE_PATTERNS
    head = re.split(r"\s+(?:—|–|--)\s+", str(text or ""), maxsplit=1)[0]
    head = re.sub(r"^[-*+\s|]*(?:`[^`]+`\s*(?:—|–|--)\s*)?\**", "", head)
    if not head.startswith("Claim"):
        return False
    if _STANCE_PATTERNS is None:
        _STANCE_PATTERNS = _stance_patterns()
    return any(rx.search(head) for rx in _STANCE_PATTERNS)


def _dedupe_key(text: str) -> str:
    """A banked line's finding identity, for cross-PR de-duplication.

    Keyed on the LABEL, not the whole row. Every shape the lane produces is
    "<label> — <reason>": the composer renders `- **<label>** — <why it was
    deferred>`, and `banked_from_findings` writes `<label> — <detail>`. The
    label is the finding; the reason is one reviewer's phrasing of why they
    left it, and it differs between every review of the same page. Keying on
    the whole row would therefore dedupe almost nothing.
    """
    head = re.split(r"\s+(?:—|–|--)\s+", str(text or ""), maxsplit=1)[0]
    return re.sub(r"[^a-z0-9]+", " ", head.lower()).strip()


def _bank(banked: list[dict], item: dict) -> None:
    """Append `item` unless the same finding is already banked, or it is an
    editorial stance (never work — see `is_editorial_stance`).

    One unresolved finding is now discoverable from several PRs at once, which
    it never was while only the latest PR was readable. A page reviewed three
    times carries the same unactioned Vale nag in all three bodies (see
    content-review/docs-iac-concepts-providers, #20953/#20927/#20503, each
    deferring `'all of' is too wordy` in its own words), and a glow-up that
    declines it adds a fourth. Undeduped, the model's execute-or-decline table
    grows by a row per review for a single piece of debt — an expanding backlog
    that reads as new findings when nothing new has been found.

    Two preferences on collision. A `glowup-declined` variant always wins: it
    carries decline history the plain row doesn't, the model needs to know this
    was already turned down once, and a human needs to be able to see a decline
    loop forming. Otherwise the later PR wins, so the reason shown is the most
    recent reviewer's judgment rather than the oldest.
    """
    if is_editorial_stance(item.get("text")):
        log(f"not banking editorial stance {item.get('id')}: {str(item.get('text'))[:80]!r}")
        return
    key = _dedupe_key(item.get("text"))
    if not key:
        banked.append(item)
        return
    for i, existing in enumerate(banked):
        if _dedupe_key(existing.get("text")) != key:
            continue
        was_declined = existing.get("source") == "glowup-declined"
        is_declined = item.get("source") == "glowup-declined"
        newer = int(item.get("source_pr") or 0) > int(existing.get("source_pr") or 0)
        if (is_declined and not was_declined) or (is_declined == was_declined and newer):
            banked[i] = item
        return
    banked.append(item)


def _recovery_note(recovery: dict) -> str:
    """One sentence naming which recovery outcome happened.

    Four states, four sentences. The single collapsed note these replace said
    "no prior review PRs reachable" for all of them, including the case where
    no lookup was attempted at all — sending anyone who read it looking for an
    API failure instead of a missing pointer.
    """
    state = recovery.get("state")
    heads = ", ".join(recovery.get("heads_queried") or []) or "none"
    tail = "; run the taxonomy-only sweep"
    if state == "gh_unavailable":
        # Name the heads that actually went unanswered, not every head queried:
        # the failure can be partial, and a sentence listing branches that WERE
        # successfully asked is the same untrue-by-collapse note this replaces.
        unreachable = ", ".join(recovery.get("prs_unreachable") or []) or heads
        return (f"GitHub would not answer for {unreachable}, so prior review PRs "
                f"could not be read{tail}")
    if state == "prs_carried_nothing":
        found = ", ".join(f"#{n}" for n in recovery.get("prs_without_sections") or [])
        return (f"reviewed {recovery.get('prs_found', 0)} prior PR(s) ({found}); "
                f"none carried banked sections{tail}")
    return f"no review PR has ever used {heads}{tail}"


def run(args) -> int:
    queue = json.loads(Path(args.queue).read_text())
    articles = queue.get("articles") or []
    if len(articles) != 1:
        warn(f"queue must carry exactly one article, found {len(articles)}")
        return 1
    article = articles[0]
    entry = load_entry(Path(args.ledger_dir), article.get("slug") or "")

    numbers: list[int] = []
    # Ledger entry when a cache is present (dispatcher-side runs); the queue
    # article's carried pointer otherwise (the worker has no ledger cache —
    # select-glowup.py stamps source_pr_number for exactly this). `last_pr_number`
    # is record-review.py's durable pointer, which survives a review that opened
    # no PR; `pr_number` is only set when that review opened one.
    for n in (entry.get("pr_number"), entry.get("last_pr_number"),
              article.get("source_pr_number")):
        if n and int(n) not in numbers:
            numbers.append(int(n))
    for extra in args.pr or []:
        n = int(extra)
        if n not in numbers:
            numbers.append(n)

    prs, recovery = discover_prs(article.get("slug") or "", numbers, args.pr_json)

    # The queue article carries the record when the dispatcher had S3 access
    # (select-glowup.py stamps it); --findings-dir covers a dispatcher-side or
    # manual run that can read the prefix directly.
    findings_record = article.get("findings_record")
    if findings_record is None and args.findings_dir:
        fr = Path(args.findings_dir) / f"{article.get('slug') or ''}.json"
        if fr.is_file():
            try:
                findings_record = json.loads(fr.read_text())
            except (OSError, json.JSONDecodeError) as e:
                warn(f"{fr} unreadable ({e}); falling back to the PR-body scrape")
        else:
            log(f"no findings record at {fr}; PR-body scrape only "
                f"(expected for pages last reviewed before the record existed)")

    backlog = build(article, entry, prs, findings_record, recovery)
    Path(args.out).write_text(json.dumps(backlog, indent=2) + "\n")
    log(f"{len(backlog['banked'])} banked finding(s) from "
        f"{len(backlog['source_prs'])} PR(s) "
        f"[{backlog['recovery']['state']}] -> {args.out}")
    # Fail-open by default: the review job is unprivileged, a red X here reads
    # as "the lane is broken" when the true state is "the evidence is out of
    # reach", and record-review.py now preserves the backlog either way, so a
    # degraded run costs a slot rather than the data. --strict exists so the
    # workflow can be flipped fail-closed without another change here.
    return 2 if (args.strict and backlog["degraded"]) else 0


def self_test() -> int:
    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    body = "\n".join([
        "> [!IMPORTANT]",
        "> notice",
        "",
        "## Why this page",
        "Selected by score.",
        "",
        "## Fixes applied",
        "| link | L88 | fixed |",
        "",
        "## Findings not applied",
        "| claim | L42 | needs interpretation |",
        "| ---- | --- | --- |",
        "- Consider restructuring the intro (readthrough L10-30)",
        "",
        "## Screenshot check",
        "No images.",
        "",
        "## Rendered content",
        "Skipped.",
        "",
        "## Verification",
        "- `make lint`: passed",
    ])
    sections = extract_sections(body)
    check("findings section extracted",
          len(sections.get("Findings not applied", [])) == 2)
    check("an editorial stance is never banked",
          is_editorial_stance("- **Claim (c23, L1115): Using the Pulumi MCP server is the recommended "
                              "approach for AI-assisted conversion — contradicted (medium).** — editorial.")
          and is_editorial_stance("Claim (c9): Unlike Terraform, Pulumi uses real languages — unverifiable"))
    check("a stance word in the REASON does not make a finding a stance",
          not is_editorial_stance("- **Claim (c3, L21): Terraform HCL lacks unit testing capabilities — "
                                  "contradicted.** — the page frames `pulumi convert` as primary"))
    check("a Vale or readthrough row is never a stance",
          not is_editorial_stance("- **Vale weasel word (L18): 'the only' is a weasel word.** — nag")
          and not is_editorial_stance("- **Readthrough self-redundancy (L36): the recommended path restated.** — x"))
    _stance_bank: list = []
    _bank(_stance_bank, {"id": "s1", "text": "- **Claim (c23): X is the recommended approach — contradicted.** — r",
                         "source_pr": 1, "source": "pr-body"})
    _bank(_stance_bank, {"id": "s2", "text": "- **Claim (c3): the price is $5 — contradicted.** — r",
                         "source_pr": 1, "source": "pr-body"})
    check("_bank drops the stance and keeps the fact", [b["id"] for b in _stance_bank] == ["s2"])
    check("table separator rows dropped",
          all("----" not in t for t in sections["Findings not applied"]))
    check("pre-filled noise sections empty",
          not sections.get("Screenshot check") and not sections.get("Rendered content"))
    check("fixes/verification never banked",
          "Fixes applied" not in sections and "Verification" not in sections)

    # --- boilerplate is not a finding ----------------------------------
    # Exact-line noise matching was enough while nothing was ever recovered.
    # The first live run against a real page (#19885) banked 5 boilerplate
    # lines out of 13, each of which the model would have had to execute or
    # decline in the PR body's tables.
    real = "- **Vale cliché (L710): avoid clichés like 'a clean slate'.** — Stylistic."
    noisy = "\n".join([
        "## Findings not applied",
        real,
        "For the judgment-level items above, run "
        "`/glow-up content/docs/iac/get-started/kubernetes/create-component.md`.",
        "The items above are banked for the automated glow-up lane, which executes a "
        "page's accumulated deferrals under human review — or run "
        "`/glow-up content/docs/x.md` to work them now.",
        "- _Nothing judgment-level was pre-found. Add any finding you chose not to apply._",
        "",
        "## Screenshot check",
        "No images. The page source references no screenshots, diagrams, or other content "
        "images (only the generic shared `meta_image` card, if any), so there is nothing "
        "to verify. _(Determined from the source; the screenshot pass was skipped.)_",
        "",
        "## Rendered content",
        "Skipped — the page source uses only render-safe chrome (`choosable`), so the "
        "rendered HTML carries no content beyond the source prose. "
        "_(Determined from the source.)_",
    ])
    noisy_sections = extract_sections(noisy)
    check("the composer's /glow-up routing trailer is not a finding",
          noisy_sections.get("Findings not applied") == [real])
    check("both historical trailer phrasings are dropped",
          not any("glow-up" in t for t in
                  noisy_sections.get("Findings not applied", [])))
    check("the empty-deferrals placeholder is not a finding",
          not any("pre-found" in t for t in
                  noisy_sections.get("Findings not applied", [])))
    check("a pre-fill that continues past 'No images.' is still noise",
          not noisy_sections.get("Screenshot check"))
    check("a pre-fill that continues past 'Skipped' is still noise",
          not noisy_sections.get("Rendered content"))
    check("a glow-up's 'None — the backlog was empty' declines nothing",
          not extract_sections(
              "## Backlog declined\nNone — the backlog was empty (`banked: []`).",
              GLOWUP_BANKED_SECTIONS).get("Backlog declined"))
    check("a real finding starting with a normal word survives",
          extract_sections("## Findings not applied\n- **Nonetheless the claim holds**"
                           )["Findings not applied"] == ["- **Nonetheless the claim holds**"])

    article = {"slug": "docs-x", "path": "content/docs/x.md"}
    entry = {"skipped_findings": 2, "clarity_flag": True, "pr_number": 123}
    prs = [{"number": 123, "url": "https://example.test/123", "body": body}]
    backlog = build(article, entry, prs)
    check("banked items carry section + source PR",
          all(b["section"] == "Findings not applied" and b["source_pr"] == 123
              for b in backlog["banked"]))
    check("ids are stable and unique",
          len({b["id"] for b in backlog["banked"]}) == len(backlog["banked"]) == 2)
    check("ledger counters carried", backlog["clarity_flag"] is True
          and backlog["skipped_findings"] == 2)

    empty = build(article, entry, [])
    check("no PRs degrades to a noted empty backlog",
          empty["banked"] == [] and any("taxonomy-only" in n for n in empty["notes"]))
    blank = build(article, entry, [{"number": 5, "url": "u", "body": "## Why this page\nx"}])
    # The structured record is the spine: it works with no PR at all, which is
    # the case the PR-body scrape can never cover (reused branches make older
    # reviews unreachable).
    rec = {"slug": "docs-x", "reviewed_at": "2026-08-19",
           "counts": {"total": 3, "applied": 1, "deferred": 2},
           "findings": [
               {"id": "f1", "label": "Claim (c1): thing is v7", "detail": "actually v9",
                "applied": True},
               {"id": "f2", "label": "Vale filler (L48)", "detail": "", "applied": False},
               {"id": "f3", "label": "Claim (c9): other thing", "detail": "unverifiable",
                "applied": False}]}
    from_rec = build(article, entry, [], rec)
    check("structured findings bank with no PR at all",
          len(from_rec["banked"]) == 2)
    check("an APPLIED finding is never re-banked",
          all("thing is v7" not in b["text"] for b in from_rec["banked"]))
    check("the detail rides along for context",
          any("unverifiable" in b["text"] for b in from_rec["banked"]))
    check("a record-only backlog carries no degradation note",
          from_rec["notes"] == [])
    check("the record's provenance is recorded",
          from_rec.get("findings_record", {}).get("counts", {}).get("deferred") == 2)
    both = build(article, entry, [{"number": 7, "url": "u",
                                   "body": "## Findings not applied\n\n- **Claim (c9)** — judgment call\n"}],
                 rec)
    check("record and PR prose merge rather than compete",
          len(both["banked"]) == 3
          and {b.get("source") for b in both["banked"]} == {"findings-record", "pr-body"})
    check("a missing record falls back to the PR scrape cleanly",
          len(build(article, entry, [{"number": 7, "url": "u",
                                      "body": "## Findings not applied\n\n- x\n"}], None)["banked"]) == 1)

    check("PR without banked sections degrades with a note",
          blank["banked"] == [] and any("taxonomy-only" in n for n in blank["notes"]))

    # --- lane-aware section vocabulary ---------------------------------
    heads = heads_for("docs-x")
    check("all three canonical heads are queried",
          heads == ["content-review/docs-x", "content-review/retire-docs-x",
                    "content-review/glowup-docs-x"])
    check("the glow-up head selects the glow-up vocabulary",
          sections_for("content-review/glowup-docs-x") == GLOWUP_BANKED_SECTIONS
          and sections_for("content-review/docs-x") == FIX_BANKED_SECTIONS
          and sections_for("content-review/retire-docs-x") == FIX_BANKED_SECTIONS)

    glow_body = "\n".join([
        "## Backlog executed",
        "| already fixed | #1 | done |",
        "",
        "## Backlog declined",
        "- **Claim (c9)** — needs an SME",
        "- **Vale weasel (L472)** — accurate as written",
        "",
        "## Secondary sweep",
        "- **Style improvements**: none",
    ])
    gpr = [{"number": 20984, "url": "u", "headRefName": "content-review/glowup-docs-x",
            "body": glow_body}]
    gback = build(article, entry, gpr)
    check("a glow-up PR's declined items are banked",
          len(gback["banked"]) == 2)
    check("they are tagged so the model knows they were turned down once",
          all(b["source"] == "glowup-declined" and b["declined_by_pr"] == 20984
              for b in gback["banked"]))
    check("a glow-up PR's EXECUTED items are never re-banked",
          all("already fixed" not in b["text"] for b in gback["banked"]))
    check("fix-lane sections are not read out of a glow-up PR",
          build(article, entry, [{"number": 1, "url": "u",
                                  "headRefName": "content-review/glowup-docs-x",
                                  "body": "## Findings not applied\n- x\n"}])["banked"] == [])
    check("glow-up sections are not read out of a fix PR",
          build(article, entry, [{"number": 1, "url": "u",
                                  "headRefName": "content-review/docs-x",
                                  "body": "## Backlog declined\n- x\n"}])["banked"] == [])
    check("a PR with no head ref falls back to the fix vocabulary",
          len(build(article, entry, [{"number": 1, "url": "u",
                                      "body": "## Findings not applied\n- x\n"}]
                    )["banked"]) == 1)

    # --- recovery states: four outcomes, four distinct notes ------------
    def state_of(prs, rec=None, art=None):
        return build(art or article, {}, prs, None, rec)

    none_ever = state_of([], {"heads_queried": heads, "prs_found": 0,
                              "prs_unreachable": [], "prs_without_sections": [],
                              "state": "no_prior_prs"})
    gh_down = state_of([], {"heads_queried": heads, "prs_found": 0,
                            "prs_unreachable": heads, "prs_without_sections": [],
                            "state": "gh_unavailable"})
    carried_nothing = state_of([{"number": 5, "url": "u",
                                 "headRefName": "content-review/docs-x",
                                 "body": "## Why this page\nx"}])
    states = [none_ever["recovery"]["state"], gh_down["recovery"]["state"],
              carried_nothing["recovery"]["state"]]
    check("the three empty outcomes are distinguished, not collapsed",
          states == ["no_prior_prs", "gh_unavailable", "prs_carried_nothing"])
    check("each carries its own note",
          len({none_ever["notes"][0], gh_down["notes"][0],
               carried_nothing["notes"][0]}) == 3)
    check("the gh-failure note says GitHub would not answer",
          "would not answer" in gh_down["notes"][0])
    check("the never-reviewed note does not claim a lookup failed",
          "no review PR has ever used" in none_ever["notes"][0]
          and "unreachable" not in none_ever["notes"][0])
    check("prs_carried_nothing names the PRs it read",
          "#5" in carried_nothing["notes"][0])
    check("a recovered backlog reports recovered",
          gback["recovery"]["state"] == "recovered")

    # --- the #20984 contradiction --------------------------------------
    debt = {"skipped_findings": 17, "clarity_flag": True}
    stranded = build(article, debt, [], None,
                     {"heads_queried": heads, "prs_found": 0, "prs_unreachable": [],
                      "prs_without_sections": [], "state": "no_prior_prs"})
    check("#20984: debt with an empty backlog is flagged degraded",
          stranded["degraded"] is True and stranded["banked"] == [])
    check("#20984: the counters ride along so the composer can name them",
          stranded["skipped_findings"] == 17 and stranded["clarity_flag"] is True)
    check("no debt and no backlog is NOT degraded",
          build(article, {"skipped_findings": 0}, [])["degraded"] is False)
    check("a clarity flag alone is enough to count as debt",
          build(article, {"skipped_findings": 0, "clarity_flag": True},
                [])["degraded"] is True)
    check("debt that DID recover is not degraded",
          build(article, debt, gpr)["degraded"] is False)
    check("degraded is always present, even on the happy path",
          "degraded" in gback and "recovery" in gback)

    # --- partial head-query failure is still a failure ------------------
    part = {"heads_queried": heads, "prs_found": 0,
            "prs_unreachable": ["content-review/glowup-docs-x"],
            "prs_without_sections": [], "state": "gh_unavailable"}
    part_note = build(article, {}, [], None, part)["notes"][0]
    check("a partly-failed query never claims the page was never reviewed",
          "has ever used" not in part_note)
    check("the note names only the heads that actually went unanswered",
          "glowup-docs-x" in part_note
          and "content-review/retire-docs-x" not in part_note)

    # --- one finding, one row, however many PRs carry it ----------------
    # A page reviewed three times defers the same Vale nag in all three bodies,
    # each in its own words; a glow-up declining it adds a fourth. Undeduped
    # the model gets four rows for one piece of debt.
    same = "Vale wordiness (L84): 'all of' is too wordy."
    multi = [
        {"number": 20503, "url": "u", "headRefName": "content-review/docs-x",
         "body": f"## Findings not applied\n- **{same}** — Style nag; a prose judgment."},
        {"number": 20927, "url": "u", "headRefName": "content-review/docs-x",
         "body": f"## Findings not applied\n- **{same}** — `write-good` heuristic; a style call."},
        {"number": 20953, "url": "u", "headRefName": "content-review/docs-x",
         "body": f"## Findings not applied\n- **{same}** — Style nag; reads naturally here."},
    ]
    dd = build(article, {}, multi)
    check("the same finding deferred by three reviews banks once",
          len(dd["banked"]) == 1)
    check("and it keeps the most recent reviewer's reason",
          dd["banked"][0]["source_pr"] == 20953)
    declined_too = build(article, {}, multi + [
        {"number": 21000, "url": "u", "headRefName": "content-review/glowup-docs-x",
         "body": f"## Backlog declined\n- **{same}** — declined: accurate as written."}])
    check("a later decline replaces the plain row rather than adding one",
          len(declined_too["banked"]) == 1
          and declined_too["banked"][0]["source"] == "glowup-declined")
    check("distinct findings are never collapsed",
          len(build(article, {}, [{"number": 1, "url": "u",
                                   "headRefName": "content-review/docs-x",
                                   "body": "## Findings not applied\n"
                                           "- **Vale wordiness (L84): 'all of'.** — a\n"
                                           "- **Vale wordiness (L99): 'all of'.** — b"}]
                    )["banked"]) == 2)

    # The property every test above depends on: fixtures mean zero gh calls.
    import unittest.mock as _mock
    with _mock.patch.object(subprocess, "run",
                            side_effect=AssertionError("subprocess called")):
        fx = Path(__file__).parent / ".selftest-prs.json"
        fx.write_text(json.dumps(gpr))
        try:
            prs, rec = discover_prs("docs-x", [123], str(fx))
            check("--pr-json performs zero subprocess calls",
                  len(prs) == 1 and rec["state"] == "recovered")
            fx.write_text("[]")
            _, rec_empty = discover_prs("docs-x", [123], str(fx))
            check("an empty fixture set reads as no_prior_prs, not a failure",
                  rec_empty["state"] == "no_prior_prs")
        finally:
            fx.unlink(missing_ok=True)

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall build-glowup-backlog self-tests passed")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--queue", help="single-article glow-up queue JSON")
    p.add_argument("--ledger-dir", default=".ledger-cache",
                   help="synced ledger cache (source of pr_number / counters)")
    p.add_argument("--pr", action="append",
                   help="extra PR number(s) to read bodies from (repeatable)")
    p.add_argument("--pr-json",
                   help="PR view fixtures (JSON list of {number,url,body}; '-' = stdin) "
                        "— replaces gh calls (testing)")
    p.add_argument("--findings-dir", default="",
                   help="synced findings/ prefix; the structured spine, "
                        "preferred over scraping PR bodies")
    p.add_argument("--strict", action="store_true",
                   help="exit 2 when the ledger says findings were banked and none "
                        "could be recovered (default: warn and continue)")
    p.add_argument("--out", default=".glowup-backlog.json")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()
    if args.self_test:
        return self_test()
    if not args.queue:
        p.error("--queue is required (or --self-test)")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
