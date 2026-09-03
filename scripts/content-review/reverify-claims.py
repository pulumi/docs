#!/usr/bin/env python3
"""Nightly re-verification of volatile claims from the S3 claims index.

Consumes the per-page claims snapshots `record-claims.py` persists (one JSON
object per page under the ledger bucket's `claims/` prefix) and re-checks the
*volatile* entities — version pins, prices, limits — straight from the index:
no page diff, no re-extraction, one verifier call per entity. This is the
event-driven-freshness consumer from pulumi/docs#20078 §4.1: a claim that
drifted (the provider released v9, the price changed) is caught within a
night instead of waiting for the page's next staleness-driven sweep.

How a stale finding flows (no new human burden, no prose generation):
  1. An entity re-verifies `contradicted`/`mismatch`.
  2. Every page stating that claim gets a `stale_claims` marker written into
     its LEDGER object (`ledger/<slug>.json`) — evidence and the claim text
     attached, so the reviewing worker looks for that sentence rather than
     re-deriving the finding. A page that words a different fact under the
     same entity key is not marked (see `claim_groups`); neither is a page a
     PR here cannot edit (`editable: false` in strategic-tiers.yaml). A page
     with no ledger object yet is skipped rather than stubbed: the marker
     write is a whole-object overwrite of a key `record-review.py` owns.
  3. `select-articles.py` adds a large additive boost for marked pages, so
     the next daily content-review sweep picks them up; the normal worker
     re-reviews the page, fixes it through the existing PR machinery, and
     its ledger/claims rewrites clear the marker automatically.

Selection (deterministic, stateless): volatile keyed entities are grouped
across pages, entities with nothing live to check are held out (every claim
already marked stale — waiting on a review, not on another check — or
superseded by a newer review), the rest are sorted by entity key and swept in
day-rotated chunks of `--count` — days-since-epoch modulo the chunk count
picks tonight's chunk, so the whole volatile set is covered every
ceil(N/count) nights with no persisted cursor.

Inside a due entity, the unit of verification is each DISTINCT CLAIM TEXT
(`claim_groups`): the entity key names the subject and drops the value, so
`version/pulumi-cli` legitimately holds several different facts, and a
verdict on one must reach only the pages that state it. Identical wording on
several pages is still one call, fanned back out to all of them.

Verification reuses `verify-claims.py`'s per-claim machinery (routing +
agent-loop verifier) by module import; each group's freshest claim record is
the input, with the page path and the heading + surrounding prose the claim
sits under (`page_context`), so the verifier judges the claim as the page
scopes it. `contradicted`/`mismatch` → stale; `framing-drift` → soft
(reported, never marked — see SOFT_VERDICTS); `verified`/`matches` → fresh;
anything else (`unverifiable`, errors) → inconclusive, reported but never
marked — a flaky check must not burn review-queue slots.

Evidence independence: a verdict whose only cited source is Pulumi's own
published docs — a www.pulumi.com URL, or a `content/` source file — is
demoted to `unverifiable` before that mapping (see `source_is_own_corpus`).
The site is this repo rendered, so such a check has confirmed the page
against itself and cannot detect drift in either direction.

Writes `.claims-reverify-report.json` (plus `n_checked`/`n_stale`/`has_stale`
to $GITHUB_OUTPUT) and, when CONTENT_REVIEW_LEDGER_URI is set, uploads each
marked ledger object. Degrades gracefully: no API key, no claims dir, or no
volatile entities → empty report, exit 0.

Usage:
    reverify-claims.py --claims-dir .claims-cache --ledger-dir .ledger-cache \
        --count 25 [--today YYYY-MM-DD] [--repo-root .] [--model <m>]
        [--out .claims-reverify-report.json] [--dry-run]

Self-contained smoke checks: `python3 reverify-claims.py --self-test`.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parents[2]
VERIFY_CLAIMS = HERE / ".claude/commands/docs-review/scripts/verify-claims.py"
ENTITY_KEY = HERE / ".claude/commands/docs-review/scripts/entity_key.py"

SCHEMA_VERSION = 1
DEFAULT_COUNT = 25
MAX_CONCURRENCY = 8
STALE_VERDICTS = {"contradicted", "mismatch"}
# `framing-drift` says the claim is true but drawn too broadly. Reported, never
# marked. This lane hands the verifier one extracted sentence, and extraction
# routinely drops the scope the enclosing heading establishes: "add awssdk=v2
# to the query string" under an "AWS KMS" heading came out of the index as a
# claim about every AWS query string, and on 2026-09-03 its framing verdict
# marked two pages — one of which never made the claim — and both burned a
# review slot. A framing verdict here is a verdict on the extraction as often
# as on the page. The PR-review pipeline keeps it because it reads the diff.
SOFT_VERDICTS = {"framing-drift"}
FRESH_VERDICTS = {"verified", "matches"}
# Verdicts that assert something either way, and so have to rest on evidence
# from outside the docs corpus to mean anything.
DECIDED_VERDICTS = STALE_VERDICTS | SOFT_VERDICTS | FRESH_VERDICTS
# Lines of page read around a claim for the verifier's context: the enclosing
# heading plus this many lines either side of the claim's own line range.
CONTEXT_LINES = 6

# Lazily-imported select-articles module (tier semantics live there).
_SELECT = None


def log(msg: str) -> None:
    print(f"reverify-claims: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::reverify-claims: {msg}", file=sys.stderr)


def _load_verify_claims():
    """Import verify-claims.py by path (hyphenated filename; main() is guarded,
    so importing has no side effects). Same pattern record-review.py uses for
    select-articles.py."""
    spec = importlib.util.spec_from_file_location("verify_claims", VERIFY_CLAIMS)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _policy_for(path: str, rules: list[dict]):
    """select-articles.policy_for, imported by path so the tier semantics have
    exactly one definition (same pattern check-retire-veto.py uses)."""
    global _SELECT
    if _SELECT is None:
        spec = importlib.util.spec_from_file_location(
            "select_articles", Path(__file__).resolve().parent / "select-articles.py")
        _SELECT = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_SELECT)
    return _SELECT.policy_for(path, rules)


def load_tier_rules(tiers_file: Path | None) -> list[dict]:
    """Tier rules, or [] when unreadable. Failing to [] means every page looks
    editable, i.e. today's file-existence-only behavior — noisier for
    generated trees, never blinder."""
    if tiers_file is None or not tiers_file.is_file():
        return []
    try:
        _policy_for("content/docs/x.md", [])  # force the import, surface errors here
        return _SELECT.load_tiers(tiers_file)
    except Exception as e:  # noqa: BLE001
        warn(f"could not load tiers from {tiers_file} ({e}); "
             f"generated trees will route by file existence alone")
        return []


def _load_is_volatile():
    """entity_key.is_volatile, or None if the module can't be loaded.

    Re-deriving beats trusting the snapshot's stored `volatile` flag: the flag
    was stamped whenever the page was last reviewed, so a narrowing of the
    policy would otherwise only reach the index page by page over months. None
    falls the caller back to the stored flag — a stale policy is a much smaller
    problem than a lane that stops selecting anything."""
    try:
        spec = importlib.util.spec_from_file_location("entity_key", ENTITY_KEY)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.is_volatile
    except Exception as e:  # noqa: BLE001 - never break the lane over this
        warn(f"entity_key module unavailable ({e}); using stored volatile flags")
        return None


# ---- evidence independence ---------------------------------------------------

# www.pulumi.com is this repo rendered and `content/` is its source, so a
# verdict citing only those has checked the page against itself: it can never
# go stale, and a `contradicted` from the same place is equally meaningless.
# Demoted to `unverifiable` — reported, never counted fresh, never marked.
_URL_RE = re.compile(r"https?://[^\s,;)\]]+", re.IGNORECASE)
_OWN_HOST_RE = re.compile(r"^https?://(?:[\w-]+\.)*pulumi\.com(?:[/:?#]|$)", re.IGNORECASE)
_PATH_RE = re.compile(
    r"(?<![\w/-])[\w][\w./-]*\.(?:json|ya?ml|md|mdx|go|ts|tsx|js|py|cs|java|tf|toml)\b"
)


def source_is_own_corpus(source: str) -> bool:
    """True when every source the verifier cited is our own published docs.

    Positive evidence only: a source naming nothing identifiable (no URL, no
    file path) is left alone rather than demoted — unrecognized is not the
    same as circular.
    """
    src = source or ""
    urls = _URL_RE.findall(src)
    if any(not _OWN_HOST_RE.match(u) for u in urls):
        return False
    paths = _PATH_RE.findall(_URL_RE.sub(" ", src))
    own_paths = [p for p in paths if p.startswith("content/") or "/content/" in p]
    if len(paths) > len(own_paths):
        return False
    return bool(urls) or bool(own_paths)


# ---- index loading -----------------------------------------------------------


def load_snapshots(claims_dir: Path) -> list[dict]:
    """All parseable per-page claims snapshots under the synced claims/ prefix."""
    out: list[dict] = []
    if not claims_dir.is_dir():
        return out
    for f in sorted(claims_dir.glob("*.json")):
        try:
            snap = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            warn(f"unreadable claims snapshot {f}")
            continue
        if isinstance(snap, dict) and snap.get("path") and snap.get("slug"):
            out.append(snap)
    return out


def volatile_entities(snapshots: list[dict], is_volatile=None) -> dict[str, list[dict]]:
    """{entity_key: [assertion, ...]} over every volatile keyed claim.

    Each assertion carries the claim record plus its page provenance
    (path/slug/reviewed_at), so a stale verdict can fan back out to every
    page asserting the entity.

    `is_volatile` re-derives the flag under today's policy (see
    `_load_is_volatile`); omitting it reads the snapshot's stored flag."""
    decide = is_volatile or (lambda c: bool(c.get("volatile")))
    entities: dict[str, list[dict]] = {}
    for snap in snapshots:
        for c in snap.get("claims") or []:
            if not isinstance(c, dict) or not c.get("entity_key") or not decide(c):
                continue
            entities.setdefault(c["entity_key"], []).append({
                "claim": c,
                "path": snap["path"],
                "slug": snap["slug"],
                "reviewed_at": snap.get("reviewed_at") or "",
            })
    return entities


def _norm_text(text) -> str:
    """Whitespace-collapsed, case-folded claim text — the grouping key."""
    return " ".join(str(text or "").split()).lower()


def claim_groups(assertions: list[dict]) -> list[tuple[str, list[dict]]]:
    """One entity's assertions split by what they actually say.

    The entity key names the SUBJECT ("version/pulumi-cli"), and by design
    drops the value, so it joins claims across pages and across time — that is
    what lets a price change be caught on every page that quotes it. But the
    same key also collects DIFFERENT facts about one subject: on 2026-09-03
    `version/pulumi-cli` held "as of v3.33.1 the awskms URL takes
    awssdk=v2&profile=" on one page and "since v3.35.3 pluginDownloadURL
    understands github://" on another. Verifying one and fanning the verdict
    out to both marked a page for a claim it never made.

    So the unit of verification is the claim text, not the entity: each group
    is verified on its own and only its own pages can be marked. Identical
    wording on several pages still costs one call. Returns [(text, assertions)]
    in first-seen order; `text` is the freshest assertion's original wording.
    """
    by_key: dict[str, list[dict]] = {}
    for a in assertions:
        by_key.setdefault(_norm_text(a["claim"].get("text")), []).append(a)
    return [(representative(group).get("text") or "", group) for group in by_key.values()]


def already_marked(key: str, assertions: list[dict], ledger: dict[str, dict]) -> bool:
    """True when some page asserting this claim already carries its stale
    marker — the claim is waiting on a review, not on another check.

    `assertions` is one entity's assertions of ONE claim text (see
    `claim_groups`). A marker written since 2026-09 carries `claim_text`, and
    only a marker for the same text counts: a marker for one claim under
    `version/pulumi-cli` must not hold a different claim under the same key on
    another page out of the rotation. A legacy marker with no `claim_text`
    matches on the key alone, as it always did.
    """
    texts = {_norm_text(a["claim"].get("text")) for a in assertions}
    for a in assertions:
        entry = ledger.get(a["path"]) or {}
        for m in entry.get("stale_claims") or []:
            if not isinstance(m, dict) or m.get("entity_key") != key:
                continue
            if not m.get("claim_text") or _norm_text(m["claim_text"]) in texts:
                return True
    return False


_HEADING_RE = re.compile(r"^#{1,6}\s")
_LINE_RANGE_RE = re.compile(r"L(\d+)(?:-(\d+))?")


def page_context(repo_root: Path | None, path: str, line_range: str) -> str:
    """The heading a claim sits under plus the prose around it, for the verifier.

    The claims index persists each claim's `line_range` ("L676-680", or
    several ranges "L90, L93-94"), and the runner has the checkout, so the
    scope extraction dropped is recoverable at verification time: the nearest
    heading above the first cited line, then CONTEXT_LINES either side of the
    cited span. Empty when anything is missing — the verifier then sees the
    claim exactly as it did before this existed, never a wrong excerpt.
    """
    if repo_root is None or not path:
        return ""
    spans = [(int(a), int(b or a)) for a, b in _LINE_RANGE_RE.findall(line_range or "")]
    if not spans:
        return ""
    try:
        lines = (repo_root / path).read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return ""
    first = min(s[0] for s in spans)
    last = max(s[1] for s in spans)
    if first < 1 or first > len(lines):
        return ""
    heading = ""
    for i in range(first - 1, -1, -1):
        if _HEADING_RE.match(lines[i]):
            heading = lines[i].strip()
            break
    lo = max(first - 1 - CONTEXT_LINES, 0)
    hi = min(last + CONTEXT_LINES, len(lines))
    body = "\n".join(lines[lo:hi]).strip()
    return f"{heading}\n\n{body}".strip() if heading else body


def superseded_by_review(assertions: list[dict], ledger: dict[str, dict]) -> bool:
    """True when every asserting page was re-reviewed AFTER its snapshot.

    The claims index records the PRE-fix page, so right after a fix lands the
    snapshot still asserts the old value — re-checking it would re-flag a
    claim the merged fix already corrected (the echo that used to buy every
    stale-claim fix a redundant next-day review). A completed ledger review
    (status != "incomplete", record-review.py's vocabulary) dated strictly
    after the snapshot means fresher evidence is on its way: the reviewing
    worker rewrites the claims snapshot, and the entity re-enters the rotation
    then. Any page lacking that newer completed review keeps the entity due.
    """
    for a in assertions:
        snap_day = str(a.get("reviewed_at") or "")
        entry = ledger.get(a["path"]) or {}
        reviewed = str(entry.get("reviewed_at") or "")
        completed = bool(reviewed) and entry.get("status") != "incomplete"
        # ISO dates compare correctly as strings; empty strings fail safe.
        if not (completed and snap_day and reviewed > snap_day):
            return False
    return True


def fix_route(assertions: list[dict], repo_root: Path | None,
              tier_rules: list[dict] | None = None) -> str:
    """Where a contradicted claim about these pages can actually be fixed.

    Returns "local", "generated", or "missing". Only "local" may become a
    marker — the mark/boost/fix/retire loop needs a page a PR can edit, and
    the other two have none, so a marker there can never be retired and
    `already_marked()` then drops the entity from the rotation for good.

    Two distinct ways to have no such page, and the file check alone catches
    only the first:

    * "missing" — no markdown in the tree. A Hugo content adapter builds the
      page from `data/` at request time (the pre-built policy packs), or the
      page was deleted and its claims snapshot outlived it.
    * "generated" — the markdown exists but is machine-written and clobbered
      on the next generator run, so an edit to it is thrown away. The CLI
      command reference is 248 such files. `strategic-tiers.yaml` already
      states exactly this as `editable: false`, so that file is the authority
      rather than a second list to keep in sync. Note it is the EDITABLE flag,
      not the tier: since #20996 the CLI tree is tier 3 and `reviewable: true`
      (the report-only lane records its claims), and those claims must still
      route upstream rather than to a marker no PR here could retire.

    A claim asserted on several pages is fixable if ANY of them is, which is
    the permissive direction: worst case we mark a page and the review finds
    nothing to do, versus routing a fixable claim away from the lane that
    would have fixed it.

    `repo_root=None` (and no rules) means "assume local", so pure-logic
    callers and the self-tests keep today's behavior.
    """
    if repo_root is None and not tier_rules:
        return "local"
    reasons: list[str] = []
    for a in assertions:
        path = a["path"]
        editable = True
        if tier_rules:
            editable = _policy_for(path, tier_rules).editable
        exists = repo_root is None or (repo_root / path).is_file()
        if exists and editable:
            return "local"
        reasons.append("generated" if not editable else "missing")
    # Prefer the more specific reason when a claim spans both kinds.
    return "generated" if "generated" in reasons else "missing"


def load_known_upstream(path: Path | None) -> dict[str, dict]:
    """{entity_key: entry} from upstream-claims.yaml, or {} when absent.

    Never raises: a malformed or missing file means "nothing is known yet",
    which costs a duplicate Slack line and never suppresses a real finding.
    That is the safe direction — this file can only ever quiet a notification,
    so failing open on it can only make the lane noisier, not blinder.
    """
    if path is None or not path.is_file():
        return {}
    try:
        import yaml  # local: only this path needs it
        data = yaml.safe_load(path.read_text()) or {}
    except Exception as e:  # noqa: BLE001 - any parse failure is non-fatal
        warn(f"could not read {path} ({e}); every upstream finding will report as new")
        return {}
    out: dict[str, dict] = {}
    for entry in (data.get("known") or []):
        if isinstance(entry, dict) and entry.get("entity_key"):
            out[str(entry["entity_key"])] = entry
    return out


def load_upstream_repos(path: Path | None) -> list[dict]:
    """[{prefix, repo}, ...] from upstream-claims.yaml, longest prefix first."""
    if path is None or not path.is_file():
        return []
    try:
        import yaml
        data = yaml.safe_load(path.read_text()) or {}
    except Exception:  # noqa: BLE001 - a missing link is not worth a failed run
        return []
    rows = [r for r in (data.get("repos") or [])
            if isinstance(r, dict) and r.get("prefix") and r.get("repo")]
    return sorted(rows, key=lambda r: len(r["prefix"]), reverse=True)


def file_issue_url(finding: dict, claim_text: str, repos: list[dict],
                   origin: str = "nightly claims re-verify") -> str | None:
    """A prefilled GitHub new-issue URL for an unfiled upstream finding.

    Returns None when no mapping owns the page — the finding still reports and
    still pages #docs-ops, it just arrives without a one-click filing.

    `origin` names the lane that found it, because the reader of the issue
    should know: the nightly re-verify re-checks a claim already in the index,
    while the report-only lane (pulumi/docs#20996) is the FIRST check that page
    has ever had.

    Everything the reader needs to judge the finding rides in the body, so the
    human decision is "is this right?" rather than "let me go reconstruct what
    the bot saw". Fields are truncated because the whole thing travels as a
    query string; GitHub starts dropping it a few KB in, and a link that
    silently loses its body is worse than a short one.
    """
    page = finding["pages"][0]["path"] if finding.get("pages") else ""
    repo = next((r["repo"] for r in repos if page.startswith(r["prefix"])), None)
    if not repo:
        return None

    def clip(s: str, n: int) -> str:
        s = " ".join(str(s or "").split())
        return s if len(s) <= n else s[: n - 1] + "…"

    title = f"Docs claim contradicted: {clip(finding['entity_key'], 90)}"
    body = (
        f"Found by the pulumi/docs {origin}. The page is generated, "
        f"so there is nothing to fix in pulumi/docs — the text comes from here.\n\n"
        f"**Claim as published:** {clip(claim_text, 600)}\n\n"
        f"**What the check found:** {clip(finding.get('evidence'), 900)}\n\n"
        f"**Source consulted:** {clip(finding.get('source'), 300)}\n\n"
        f"**Rendered from:** `{page}`\n"
        f"**Entity key:** `{finding['entity_key']}`\n\n"
        f"---\n"
        f"Filed by a human from a #docs-ops notification; the check is automated, "
        f"the judgment is not. If this is wrong, say so on the issue — that is a "
        f"useful signal for the verifier's targeting."
    )
    from urllib.parse import urlencode
    return (f"https://github.com/{repo}/issues/new?"
            + urlencode({"title": title, "body": body}))


def tonight_chunk(keys: list[str], count: int, today: date) -> list[str]:
    """Day-rotated chunk of the sorted entity keys: full coverage every
    ceil(N/count) nights, deterministic from the date alone.

    The slice is STRIDED (`keys[idx::n_chunks]`), not contiguous. Contiguous
    slicing gives the last chunk `len(keys) % count` entities, so the nightly
    workload is a lottery on the pool size: at count=25 a pool of 51 splits
    25/25/1, and one night in three checks a single entity. That is not a
    quiet night — it is the same rotation spending 4% of its budget and then
    reporting a sample of one, which `signal-health.py` reads as a lane-wide
    verdict (an all-inconclusive n=1 degraded the reverify signal on
    2026-08-19). Striding gives every chunk floor or ceil of len/n_chunks,
    so the count only ever varies by one.

    Coverage and determinism are unchanged: the chunks still partition the
    key list exactly, and the day still picks the chunk. Only the grouping
    differs — entities that used to travel together now interleave, which
    nothing downstream depends on (each entity is verified independently).
    """
    if not keys or count <= 0:
        return []
    n_chunks = -(-len(keys) // count)  # ceil
    idx = today.toordinal() % n_chunks
    return keys[idx::n_chunks]


def representative(assertions: list[dict]) -> dict:
    """The freshest assertion's claim record — the input to the verifier."""
    return max(assertions, key=lambda a: a["reviewed_at"])["claim"]


# ---- ledger markers ----------------------------------------------------------


def load_ledger(ledger_dir: Path) -> dict[str, dict]:
    entries: dict[str, dict] = {}
    if not ledger_dir.is_dir():
        return entries
    for f in sorted(ledger_dir.glob("*.json")):
        try:
            entry = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(entry, dict) and entry.get("path"):
            entry["_file"] = str(f)
            entries[entry["path"]] = entry
    return entries


def apply_markers(ledger: dict[str, dict], stale: list[dict], today: date,
                  repo_root: Path | None = None,
                  tier_rules: list[dict] | None = None) -> dict[str, dict]:
    """Fold stale claim verdicts into the affected pages' ledger entries.

    Returns {slug: updated entry (without bookkeeping keys)} for every entry
    that changed. Idempotent: a marker for an already-marked entity_key is
    replaced, not duplicated. A page missing from the local ledger cache
    (shouldn't happen — the same worker run writes both objects) is SKIPPED,
    not synthesized: every changed entry is uploaded to the same S3 key
    record-review.py owns, so a two-field stub would silently destroy that
    page's status / reviewed_at / attempts / tier / score. The entity simply
    stays unmarked and comes back around on a later rotation.

    A page with no markdown source on disk is skipped for a different and more
    important reason. `select-articles.py` builds its candidate set by globbing
    `content/docs/**/*.md`, so a page rendered by a Hugo content adapter (the
    pre-built policy-pack tables, generated from `data/`) can never be selected
    for review — which means a marker written there can never be cleared, and
    `already_marked()` would then exclude that entity from re-verification
    permanently. Three entities were lost that way over five nights before this
    guard existed. Such a contradiction is real and worth acting on, but the
    action is upstream of this repo (fix the `data/` source or the product
    metadata behind it), so the verdict is reported and left in the pool rather
    than converted into a marker nothing can retire.

    The same guard has to cover a page that IS on disk but that no PR may
    edit — `editable: false` in strategic-tiers.yaml, the 254-file CLI command
    reference being the big one. `fix_route()` already routes a claim whose
    every page is such a tree upstream, but a claim that spans one editable
    page and one generated page routes `local`, and the file check alone would
    then mark the generated page too. The fix lane selects only editable pages,
    so that marker could never be resolved there, and `already_marked()`
    would hold the claim out of the rotation until the report lane happened
    to rewrite the page's ledger entry. `tier_rules` is the same list
    `fix_route()` reads; None (the pure-logic callers) checks files only."""
    changed: dict[str, dict] = {}
    for s in stale:
        marker = {
            "entity_key": s["entity_key"],
            # The sentence the verdict is about. record-review.py carries every
            # marker field forward, and the worker skill reads markers in
            # full, so this reaches the reviewer as "find THIS sentence"
            # rather than "find something about this entity".
            "claim_text": s.get("claim_text") or "",
            "verdict": s["verdict"],
            "evidence": s.get("evidence") or "",
            "source": s.get("source") or "",
            "checked_at": today.isoformat(),
        }
        for page in s["pages"]:
            if repo_root is not None and not (repo_root / page["path"]).is_file():
                warn(
                    f"{page['path']} has no source file (generated page); reporting "
                    f"{s['entity_key']} without a marker no review could ever clear"
                )
                continue
            if tier_rules and not _policy_for(page["path"], tier_rules).editable:
                warn(
                    f"{page['path']} is generated (editable: false); reporting "
                    f"{s['entity_key']} without a marker no fix-lane review could clear"
                )
                continue
            entry = ledger.get(page["path"])
            if entry is None:
                warn(
                    f"no ledger entry for {page['path']}; skipping its stale-claims "
                    "marker rather than overwriting the ledger object with a stub"
                )
                continue
            markers = [m for m in (entry.get("stale_claims") or [])
                       if isinstance(m, dict) and m.get("entity_key") != s["entity_key"]]
            markers.append(marker)
            entry["stale_claims"] = markers
            slug = entry.get("slug") or page["slug"]
            changed[slug] = {k: v for k, v in entry.items() if k != "_file"}
    return changed


def upload_entry(entry: dict, slug: str, uri: str) -> None:
    import subprocess
    key = f"{uri.rstrip('/')}/{slug}.json"
    try:
        subprocess.run(
            ["aws", "s3", "cp", "-", key],
            input=json.dumps(entry, indent=2) + "\n",
            text=True, check=True,
        )
        log(f"uploaded stale-claims marker to {key}")
    except FileNotFoundError:
        warn("aws CLI not available; ledger markers not uploaded")
    except subprocess.CalledProcessError as e:
        warn(f"marker upload failed for {slug} ({e})")


# ---- outputs -----------------------------------------------------------------


def write_outputs(report: dict) -> None:
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if not gh_out:
        return
    with open(gh_out, "a") as fh:
        # Only the gating flags: claims-reverify.yml reads the counts straight
        # out of the report JSON for its Slack summaries.
        m = report["meta"]
        fh.write(f"has_stale={'true' if m['n_stale'] else 'false'}\n")
        # Upstream findings page #docs-ops only on a CHANGE — a finding nobody
        # has filed yet, or one that started verifying clean because the
        # upstream fix landed. A known finding still coming back contradicted
        # is in the report and the artifact, and says nothing in Slack.
        news = bool(m.get("n_upstream_new")) or bool(m.get("n_upstream_resolved"))
        fh.write(f"has_upstream_news={'true' if news else 'false'}\n")


def inconclusive_breakdowns(results: list[dict]) -> tuple[dict, dict]:
    """Two count maps over the non-decided results, for diagnosing WHY the
    inconclusive rate is what it is (76% on the night this was added):

    - by_type:   the entity_key's ctype prefix (the part before the first
                 "/", per entity_key.py) — which kinds of fact can't verify.
    - by_reason: "demoted" (decided, but only own-corpus evidence), "error"
                 (verifier crashed), else the raw verdict ("unverifiable",
                 "no_verdict" for a missing one).

    Instrumentation only — nothing downstream keys on these; the routing
    fixes they motivate are follow-up work.
    """
    by_type: dict[str, int] = {}
    by_reason: dict[str, int] = {}
    for r in results:
        if r.get("verdict") in DECIDED_VERDICTS:
            continue
        ctype = str(r.get("entity_key") or "").split("/", 1)[0] or "unknown"
        by_type[ctype] = by_type.get(ctype, 0) + 1
        if r.get("demoted_from"):
            reason = "demoted"
        elif r.get("error"):
            reason = "error"
        else:
            reason = str(r.get("verdict") or "no_verdict")
        by_reason[reason] = by_reason.get(reason, 0) + 1
    return (dict(sorted(by_type.items())), dict(sorted(by_reason.items())))


def tally(results: list[dict], known_upstream: dict[str, dict],
          upstream_repos: list[dict], repo_root: Path | None,
          tier_rules: list[dict] | None) -> tuple[dict, list[dict]]:
    """The report's verdict counts and the markable `stale` list, from the
    verified results. Pure, so the accounting — which verdicts mark, which
    only report, what counts as inconclusive — is pinned by the self-test
    without a verifier in the loop. Annotates each result with `fix_route` /
    `upstream` (and the upstream issue pointer or filing link) in place.
    """
    # Split contradicted results by whether anything in this repo could act on
    # them. `upstream` findings are real and stay in the rotation forever: no
    # marker (nothing could ever retire it), no queue boost (no page to boost),
    # but reported every run so they never go quiet the way the three
    # policy-pack findings did in August.
    contradicted = [r for r in results if r["verdict"] in STALE_VERDICTS]
    soft = [r for r in results if r["verdict"] in SOFT_VERDICTS]
    for r in results:
        r["fix_route"] = fix_route(
            [{"path": p["path"]} for p in r["pages"]], repo_root, tier_rules)
        r["upstream"] = r["fix_route"] != "local"
    stale = [r for r in contradicted if not r["upstream"]]
    upstream = [r for r in contradicted if r["upstream"]]
    # New = we have not told anyone yet. Resolved = a finding we had filed
    # upstream now verifies clean, i.e. the upstream fix landed. The second is
    # the event the marker scheme structurally could not report, because a
    # marked entity was never re-checked.
    upstream_new = [r for r in upstream if r["entity_key"] not in known_upstream]
    upstream_resolved = [r for r in results
                         if r["entity_key"] in known_upstream
                         and r["verdict"] in FRESH_VERDICTS]
    for r in upstream:
        entry = known_upstream.get(r["entity_key"])
        if entry:
            r["upstream_issue"] = entry.get("issue")
        else:
            r["file_issue_url"] = file_issue_url(
                r, r.get("claim_text") or "", upstream_repos)

    fresh = [r for r in results if r["verdict"] in FRESH_VERDICTS]
    by_type, by_reason = inconclusive_breakdowns(results)
    return {
        "n_checked": len(results),
        "n_stale": len(stale),
        # Framing verdicts: decided, evidence-bearing, reported — never marked.
        "n_soft": len(soft),
        "soft_entities": [
            {"entity_key": r["entity_key"], "pages": [p["path"] for p in r["pages"]]}
            for r in sorted(soft, key=lambda x: x["entity_key"])],
        "n_upstream": len(upstream),
        "n_upstream_new": len(upstream_new),
        "n_upstream_resolved": len(upstream_resolved),
        "upstream_entities": [
            {"entity_key": r["entity_key"], "issue": r.get("upstream_issue"),
             "file_issue_url": r.get("file_issue_url"),
             # Explicit, so the Slack step filters on the SAME property the
             # count is computed from. Deriving "new" a second time from
             # `issue == null` made the workflow depend on --self-test (in
             # another file) rejecting a registry entry with no issue, to keep
             # its own two numbers agreeing. One field, one definition.
             "new": r["entity_key"] not in known_upstream,
             "reason": r["fix_route"], "pages": [p["path"] for p in r["pages"]]}
            for r in sorted(upstream, key=lambda x: x["entity_key"])],
        "upstream_resolved_entities": sorted(r["entity_key"] for r in upstream_resolved),
        "n_fresh": len(fresh),
        # Against `contradicted`, not `stale`: an upstream finding is a decided
        # verdict that simply routes elsewhere. Subtracting only the markable
        # ones would book every upstream contradiction as inconclusive,
        # inflating the rate the health signal watches and eventually
        # degrading the lane for doing its job. Soft verdicts are decided too.
        "n_inconclusive": len(results) - len(contradicted) - len(soft) - len(fresh),
        "n_demoted": sum(1 for r in results if r.get("demoted_from")),
        "inconclusive_by_type": by_type,
        "inconclusive_by_reason": by_reason,
    }, stale


def finish(report: dict, out_path: Path) -> int:
    out_path.write_text(json.dumps(report, indent=2) + "\n")
    m = report["meta"]
    log(f"checked={m['n_checked']} stale={m['n_stale']} soft={m.get('n_soft', 0)} "
        f"fresh={m['n_fresh']} "
        f"inconclusive={m['n_inconclusive']} (of which {m['n_demoted']} demoted for "
        f"own-corpus evidence) (volatile entities={m['n_entities']}, "
        f"eligible={m.get('n_eligible', 0)}, marked={m.get('n_marked', 0)}, "
        f"superseded={m.get('n_superseded', 0)}) -> {out_path}")
    for label in ("inconclusive_by_type", "inconclusive_by_reason"):
        if m.get(label):
            log(f"{label}: " + " ".join(f"{k}={v}" for k, v in m[label].items()))
    if m.get("n_upstream"):
        log(f"upstream (generated pages, not markable): {m['n_upstream']} "
            f"({m.get('n_upstream_new', 0)} not yet filed)")
        for e in m.get("upstream_entities") or []:
            log(f"  [{e.get('reason', '?')}] {e['entity_key']} "
                f"-> {e.get('issue') or 'NOT YET FILED'}")
    for k in m.get("upstream_resolved_entities") or []:
        log(f"upstream RESOLVED (now verifies clean, retire its upstream-claims.yaml entry): {k}")
    for e in m.get("soft_entities") or []:
        log(f"soft (framing-drift, reported not marked): {e['entity_key']} "
            f"-> {', '.join(e.get('pages') or [])}")
    write_outputs(report)
    return 0


# ---- main --------------------------------------------------------------------


def run(args) -> int:
    today = None
    if args.today:
        today = datetime.strptime(args.today, "%Y-%m-%d").date()
    today = today or datetime.now(timezone.utc).date()

    report = {
        "schema_version": SCHEMA_VERSION,
        "checked_at": today.isoformat(),
        "entities": [],
        "meta": {"n_snapshots": 0, "n_entities": 0, "n_marked": 0, "n_eligible": 0,
                 "n_due": 0, "n_checked": 0, "n_stale": 0, "n_soft": 0, "n_fresh": 0,
                 "n_inconclusive": 0, "n_demoted": 0, "marked_pages": []},
    }
    out_path = Path(args.out)

    # The meta block doubles as the health observation consumed by
    # signal-health.py's reverify signal: `skipped` distinguishes "couldn't
    # run" (degraded) from the quiet-night n_due=0 (healthy), an
    # all-inconclusive n_checked is the no-drift-detected tell, and n_demoted
    # says how much of that was own-corpus evidence rather than broken
    # plumbing — the two want opposite fixes. Keep those semantics intact when
    # touching the early-exit paths below.
    snapshots = load_snapshots(Path(args.claims_dir))
    report["meta"]["n_snapshots"] = len(snapshots)
    if not snapshots:
        log("no claims snapshots; nothing to re-verify")
        report["meta"]["skipped"] = "no_snapshots"
        return finish(report, out_path)

    ledger = load_ledger(Path(args.ledger_dir))
    entities = volatile_entities(snapshots, _load_is_volatile())
    report["meta"]["n_entities"] = len(entities)

    # The rotation is over entity keys; inside a due entity the unit of
    # verification is each distinct claim text (`claim_groups`). A group is
    # live unless already marked or superseded. An entity with no live group
    # is held out: "marked" when a marker is what holds it (waiting on a
    # review), otherwise "superseded" (fresher evidence is on its way).
    groups = {k: claim_groups(v) for k, v in entities.items()}
    live = {k: [(text, asrt) for text, asrt in gs
                if not already_marked(k, asrt, ledger)
                and not superseded_by_review(asrt, ledger)]
            for k, gs in groups.items()}
    marked = {k for k, gs in groups.items() if not live[k]
              and any(already_marked(k, asrt, ledger) for _, asrt in gs)}
    superseded = {k for k in entities if not live[k] and k not in marked}
    unmarked = sorted(k for k in entities if live[k])
    # n_eligible is the pool the rotation actually divides, and n_marked is
    # the backlog held out of it. Without both, a small n_due is ambiguous
    # between "the pool is nearly empty" and "the rotation handed tonight a
    # short chunk" — the two want opposite responses, and reading the report
    # for 2026-08-19 (n_due=1) could not tell them apart.
    report["meta"]["n_marked"] = len(marked)
    report["meta"]["n_superseded"] = len(superseded)
    report["meta"]["n_eligible"] = len(unmarked)
    keys = tonight_chunk(unmarked, args.count, today)
    # n_due counts entities; n_checked (below) counts verifier calls, one per
    # live claim text, so n_checked >= n_due whenever a due entity is worded
    # more than one way across the pages that assert it.
    work = [(k, text, asrt) for k in keys for text, asrt in live[k]]
    report["meta"]["n_due"] = len(keys)
    if not work:
        log("no volatile entities due tonight")
        return finish(report, out_path)

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key and not args.dry_run:
        warn("ANTHROPIC_API_KEY not set; re-verification skipped")
        report["meta"]["skipped"] = "no_api_key"
        return finish(report, out_path)

    vc = _load_verify_claims()
    repo_root = Path(args.repo_root).resolve()
    known_upstream = load_known_upstream(
        Path(args.known_upstream) if args.known_upstream else None)
    tier_rules = load_tier_rules(Path(args.tiers) if args.tiers else None)
    upstream_repos = load_upstream_repos(
        Path(args.known_upstream) if args.known_upstream else None)
    # A key that matches nothing in the index is a typo, or a claim that has
    # since been re-extracted under a different key — either way it is silently
    # muting nothing while looking like it mutes something. Warn, never fail:
    # this file must not be able to break the nightly run.
    for key in sorted(set(known_upstream) - set(entities)):
        warn(f"upstream-claims.yaml lists {key}, which matches no volatile entity "
             f"in the claims index; stale entry or a re-keyed claim")

    def check_claim(item: tuple[str, str, list[dict]]) -> dict:
        key, _, assertions = item
        freshest = max(assertions, key=lambda a: a["reviewed_at"])
        claim = dict(freshest["claim"])
        claim["__id"] = key
        # The verifier's pass1 lane reads files, and without `file` it was
        # told `file: ?` and could not open the page the claim came from.
        claim["file"] = freshest["path"]
        claim["context"] = page_context(repo_root, freshest["path"],
                                        str(claim.get("line_range") or ""))
        claim["__route"] = vc.route_claim(claim, {})
        rec, err = vc.process_claim(api_key, claim, {}, args.model, repo_root, args.dry_run)
        verdict = rec.get("verdict")
        demoted_from = None
        if verdict in DECIDED_VERDICTS and source_is_own_corpus(rec.get("source") or ""):
            demoted_from, verdict = verdict, "unverifiable"
        return {
            "entity_key": key,
            "claim_text": claim.get("text") or "",
            "verdict": verdict,
            "demoted_from": demoted_from,
            "confidence": rec.get("confidence"),
            "evidence": rec.get("evidence"),
            "source": rec.get("source"),
            "route": rec.get("route"),
            "error": err,
            "pages": [{"path": a["path"], "slug": a["slug"]} for a in assertions],
        }

    with ThreadPoolExecutor(max_workers=min(MAX_CONCURRENCY, len(work))) as pool:
        results = list(pool.map(check_claim, work))

    report["entities"] = results
    counts, stale = tally(results, known_upstream, upstream_repos, repo_root, tier_rules)
    report["meta"].update(counts)

    if stale:
        changed = apply_markers(ledger, stale, today, repo_root, tier_rules)
        # What was actually marked, after the ledger-gap and editability
        # guards — the Slack summary lists these so a wrong page is visible
        # at a glance rather than three review slots later.
        report["meta"]["marked_pages"] = sorted(e["path"] for e in changed.values())
        uri = os.environ.get("CONTENT_REVIEW_LEDGER_URI", "").strip()
        for slug, entry in sorted(changed.items()):
            local = Path(args.ledger_dir) / f"{slug}.json"
            local.parent.mkdir(parents=True, exist_ok=True)
            local.write_text(json.dumps(entry, indent=2) + "\n")
            if uri and not args.dry_run:
                upload_entry(entry, slug, uri)
        if not uri:
            warn("CONTENT_REVIEW_LEDGER_URI unset; markers written locally only")

    return finish(report, out_path)


# ---- self-test ---------------------------------------------------------------


def self_test() -> int:
    import tempfile
    from urllib.parse import unquote_plus
    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    def snap(slug, reviewed_at, *claims):
        return {"schema_version": 1, "path": f"content/docs/{slug}.md",
                "slug": f"docs-{slug}", "reviewed_at": reviewed_at,
                "claims": list(claims)}

    ver = {"entity_key": "version/pulumi-gcp", "volatile": True, "type": "version",
           "text": "pulumi-gcp v8.2.0", "line_range": "L10", "verdict": "verified"}
    price = {"entity_key": "numerical/team-plan-price", "volatile": True,
             "type": "numerical", "text": "the Team plan costs $75", "line_range": "L5",
             "verdict": "verified"}
    stable = {"entity_key": "api-surface/versioning", "volatile": False,
              "type": "api-surface", "text": "`versioning` argument", "line_range": "L7",
              "verdict": "verified"}
    unkeyed = {"entity_key": None, "volatile": True, "type": "numerical",
               "text": "40x", "line_range": "L9", "verdict": "verified"}

    snaps = [snap("a", "2026-07-01", ver, stable),
             snap("b", "2026-07-05", dict(ver, text="pulumi-gcp v8.3.0"), price, unkeyed)]

    ents = volatile_entities(snaps)
    check("volatile keyed entities only",
          set(ents) == {"version/pulumi-gcp", "numerical/team-plan-price"})

    check("entity fans out across pages", len(ents["version/pulumi-gcp"]) == 2)
    check("representative is the freshest assertion",
          representative(ents["version/pulumi-gcp"])["text"] == "pulumi-gcp v8.3.0")

    # Supersession: an entity whose every asserting page has a completed
    # review newer than its snapshot is stale evidence — skip, don't re-check.
    def entry(path, reviewed_at, status="reviewed"):
        return {"path": path, "reviewed_at": reviewed_at, "status": status}

    both_newer = {"content/docs/a.md": entry("content/docs/a.md", "2026-07-10"),
                  "content/docs/b.md": entry("content/docs/b.md", "2026-07-11")}
    one_stale = {"content/docs/a.md": entry("content/docs/a.md", "2026-07-10"),
                 "content/docs/b.md": entry("content/docs/b.md", "2026-07-02")}
    incomplete = {"content/docs/a.md": entry("content/docs/a.md", "2026-07-10"),
                  "content/docs/b.md": entry("content/docs/b.md", "2026-07-11", "incomplete")}
    check("superseded when every page re-reviewed after its snapshot",
          superseded_by_review(ents["version/pulumi-gcp"], both_newer) is True)
    check("not superseded while any page's snapshot is the freshest evidence",
          superseded_by_review(ents["version/pulumi-gcp"], one_stale) is False)
    check("an incomplete review never supersedes",
          superseded_by_review(ents["version/pulumi-gcp"], incomplete) is False)
    check("missing ledger entries never supersede",
          superseded_by_review(ents["version/pulumi-gcp"], {}) is False)

    # Inconclusive breakdowns: decided results excluded, reasons bucketed.
    mixed = [
        {"entity_key": "version/a", "verdict": "verified"},
        {"entity_key": "version/b", "verdict": "unverifiable", "demoted_from": "matches"},
        {"entity_key": "numerical/c", "verdict": "unverifiable"},
        {"entity_key": "numerical/d", "verdict": None, "error": "boom"},
        {"entity_key": None, "verdict": "unverifiable"},
    ]
    b_type, b_reason = inconclusive_breakdowns(mixed)
    check("breakdown by type buckets on the ctype prefix",
          b_type == {"numerical": 2, "unknown": 1, "version": 1})
    check("breakdown by reason splits demoted/error/verdict",
          b_reason == {"demoted": 1, "error": 1, "unverifiable": 2})

    # Re-derived volatility overrides the snapshot's stored flag, so a
    # narrowed policy reaches the whole index the night it ships.
    stale_flag = {"entity_key": "numerical/example-resources-created", "volatile": True,
                  "type": "numerical", "line_range": "L3", "verdict": "verified",
                  "text": "The example update creates 3 resources."}
    rederived = volatile_entities(
        snaps + [snap("c", "2026-07-06", stale_flag)], _load_is_volatile())
    check("re-derive drops a self-describing claim stamped volatile",
          "numerical/example-resources-created" not in rederived)
    check("re-derive keeps genuinely volatile entities",
          set(rederived) == {"version/pulumi-gcp", "numerical/team-plan-price"})
    check("no re-derive falls back to the stored flag",
          "numerical/example-resources-created"
          in volatile_entities(snaps + [snap("c", "2026-07-06", stale_flag)]))

    # Evidence independence: only own-corpus-sourced verdicts are demoted, and
    # an unrecognizable source is never treated as circular.
    own = ["https://www.pulumi.com/docs/iac/get-started/aws/modify-program/",
           "https://www.pulumi.com/docs/a/ and https://www.pulumi.com/docs/b/",
           "repo:content/docs/iac/concepts/providers/_index.md"]
    independent = ["https://docs.aws.amazon.com/config/latest/developerguide/x.html",
                   "gh api repos/pulumi/pulumi/contents/pkg/resource/deploy/retries.go",
                   "repo:data/policy_pack_policies/cis-aws.json (line 2872)",
                   "https://github.com/pulumi/pulumi/blob/master/.goreleaser.yml",
                   "https://www.pulumi.com/docs/a/ and https://docs.aws.amazon.com/x.html",
                   "N/A - author's own estimate of their tutorial content",
                   ""]
    for s in own:
        check(f"own-corpus source: {s[:44]}", source_is_own_corpus(s) is True)
    for s in independent:
        check(f"independent source: {s[:44] or '(empty)'}", source_is_own_corpus(s) is False)

    # Chunk rotation: deterministic, complete coverage across consecutive days.
    keys = [f"k{i}" for i in range(5)]
    d0 = date(2026, 7, 6)
    chunks = [tonight_chunk(keys, 2, date.fromordinal(d0.toordinal() + i)) for i in range(3)]
    check("chunks cover all keys over the rotation",
          sorted(k for ch in chunks for k in ch) == sorted(keys))
    check("same day -> same chunk", tonight_chunk(keys, 2, d0) == chunks[0])
    check("count of zero -> empty chunk", tonight_chunk(keys, 0, d0) == [])
    check("empty keys -> empty chunk", tonight_chunk([], 3, d0) == [])
    check("chunks partition the key list (no key checked twice a rotation)",
          len([k for ch in chunks for k in ch]) == len(keys))
    # The remainder night: 51 keys at count=25 used to split 25/25/1, so one
    # night in three checked a single entity. Every chunk is now within one.
    wide = [f"k{i:03d}" for i in range(51)]
    sizes = sorted(len(tonight_chunk(wide, 25, date.fromordinal(d0.toordinal() + i)))
                   for i in range(3))
    check(f"no starved night in the rotation (sizes={sizes})", max(sizes) - min(sizes) <= 1)
    check("strided rotation still covers every key",
          sorted(k for i in range(3)
                 for k in tonight_chunk(wide, 25, date.fromordinal(d0.toordinal() + i)))
          == wide)
    check("chunk never exceeds the requested count",
          all(len(tonight_chunk(wide, 25, date.fromordinal(d0.toordinal() + i))) <= 25
              for i in range(3)))

    # Upstream routing: a finding whose every asserting page is generated
    # (no markdown source) must never become a marker, because nothing could
    # ever retire it — that is how three real policy-pack findings removed
    # themselves from the rotation in August 2026.
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "content/docs").mkdir(parents=True)
        (root / "content/docs/real.md").write_text("# real\n")
        (root / "content/docs/iac/cli/commands").mkdir(parents=True)
        (root / "content/docs/iac/cli/commands/pulumi-up.md").write_text("# gen\n")
        rules = [{"prefix": "content/docs/iac/cli/commands/", "tier": 0}]
        local = [{"path": "content/docs/real.md"}]
        absent = [{"path": "content/docs/reference/pre-built-policy-packs/cis/aws.md"}]
        gen = [{"path": "content/docs/iac/cli/commands/pulumi-up.md"}]
        check("an editable page routes local", fix_route(local, root, rules) == "local")
        check("a page with no source routes missing",
              fix_route(absent, root, rules) == "missing")
        # The case the file check alone gets wrong: the markdown is right there,
        # but the generator overwrites it, so a PR against it is thrown away.
        check("a tier-0 page with a real file still routes generated",
              fix_route(gen, root, rules) == "generated")
        check("one fixable asserting page wins", fix_route(gen + local, root, rules) == "local")
        check("generated beats missing when a claim spans both",
              fix_route(gen + absent, root, rules) == "generated")
        # The shape the CLI reference actually carries since #20996: the report
        # lane reads it (`reviewable: true`) but no PR here may edit it, and it
        # is `editable`, not the tier, that decides where a finding goes.
        report_rules = [{"prefix": "content/docs/iac/cli/commands/", "tier": 3,
                         "editable": False, "reviewable": True}]
        check("a reviewable-but-not-editable page routes generated, not local",
              fix_route(gen, root, report_rules) == "generated")
        check("no root and no rules -> assume local (pure-logic callers)",
              fix_route(absent, None, None) == "local")
        check("unreadable tiers file -> no rules, never fatal",
              load_tier_rules(root / "nope.yaml") == [])

        # The known-upstream file only ever quiets a repeat notification.
        ku = root / "upstream-claims.yaml"
        ku.write_text(
            "known:\n"
            "  - entity_key: numerical/known-one\n"
            "    issue: https://github.com/pulumi/policy-packs-internal/issues/204\n")
        loaded = load_known_upstream(ku)
        check("known-upstream parses to a key map", set(loaded) == {"numerical/known-one"})
        check("missing known-upstream file is empty, not fatal",
              load_known_upstream(root / "nope.yaml") == {})
        (root / "bad.yaml").write_text("known: [{{{\n")
        check("malformed known-upstream fails open (noisier, never blinder)",
              load_known_upstream(root / "bad.yaml") == {})

    # Prefilled filing links: mapped tree gets one, unmapped tree gets None
    # (still reported, still paged — just no one-click).
    repos = [{"prefix": "content/docs/reference/pre-built-policy-packs/",
              "repo": "pulumi/policy-packs-internal"}]
    finding = {"entity_key": "numerical/iam-user-unused-credentials-90",
               "evidence": "AWS Config's rule covers UNUSED credentials, not rotation.",
               "source": "https://docs.aws.amazon.com/config/latest/developerguide/x.html",
               "pages": [{"path": "content/docs/reference/pre-built-policy-packs/cis/aws.md"}]}
    url = file_issue_url(finding, "The policy ensures credentials are rotated within 90 days.", repos)
    check("mapped tree yields a filing link",
          url is not None and url.startswith("https://github.com/pulumi/policy-packs-internal/issues/new?"))
    check("link carries the claim, the finding, and the source",
          all(t in unquote_plus(url) for t in
              ("rotated within 90 days", "UNUSED credentials", "docs.aws.amazon.com")))
    check("link names the generated page it renders from",
          "content/docs/reference/pre-built-policy-packs/cis/aws.md" in unquote_plus(url))
    check("unmapped tree yields no link",
          file_issue_url({**finding, "pages": [{"path": "content/docs/iac/concepts/x.md"}]},
                         "t", repos) is None)
    check("a finding with no pages yields no link",
          file_issue_url({**finding, "pages": []}, "t", repos) is None)
    # A body that silently loses its tail is worse than a short one, so the
    # fields are clipped; guard the total against GitHub's query-string limit.
    huge = file_issue_url({**finding, "evidence": "E" * 20000, "source": "S" * 20000},
                          "C" * 20000, repos)
    check(f"oversized finding still yields a usable URL ({len(huge)} chars)", len(huge) < 8000)
    check("shipped repo map parses and covers the policy-pack tree",
          any(r["prefix"] == "content/docs/reference/pre-built-policy-packs/"
              for r in load_upstream_repos(
                  HERE / ".claude/commands/review-existing-content/references/upstream-claims.yaml")))

    # The shipped file itself: every entry needs a tracking issue, or it is a
    # mute button with nobody behind it. (Key-vs-index validation needs the
    # claims index and so runs at runtime, as a warning.)
    shipped = HERE / ".claude/commands/review-existing-content/references/upstream-claims.yaml"
    if shipped.is_file():
        entries = load_known_upstream(shipped)
        check("shipped upstream-claims.yaml parses", bool(entries))
        check("every shipped entry cites an upstream issue",
              all(str(e.get("issue") or "").startswith("http") for e in entries.values()))
        check("every shipped entry says what is wrong",
              all(str(e.get("what") or "").strip() for e in entries.values()))

    # The Slack step filters the "new" bullet list on `.new`, which is the same
    # property n_upstream_new counts. Pin that they cannot drift apart: the
    # earlier form derived "new" a second time from `issue == null`, which made
    # the workflow's own two numbers depend on the self-test above rejecting a
    # register entry with no issue.
    _known = {"numerical/filed": {"issue": "https://x/1"}}
    _rows = [{"entity_key": "numerical/filed"}, {"entity_key": "numerical/unfiled"}]
    _flags = [r["entity_key"] not in _known for r in _rows]
    check("`new` means absent from the register, same as n_upstream_new",
          _flags == [False, True] and sum(_flags) == 1)

    # Markers: fan-out, idempotence, minimal entry for a ledger gap.
    ledger = {"content/docs/a.md": {"path": "content/docs/a.md", "slug": "docs-a",
                                    "status": "clean", "_file": "x"}}
    stale = [{"entity_key": "version/pulumi-gcp", "verdict": "contradicted",
              "claim_text": "pulumi-gcp v8.3.0",
              "evidence": "v9.0 released", "source": "gh release view",
              "pages": [{"path": "content/docs/a.md", "slug": "docs-a"},
                        {"path": "content/docs/b.md", "slug": "docs-b"}]}]
    today = date(2026, 7, 9)
    changed = apply_markers(ledger, stale, today)
    check("marker lands on the page with a ledger entry", set(changed) == {"docs-a"})
    check("existing entry keeps its fields",
          changed["docs-a"]["status"] == "clean" and "_file" not in changed["docs-a"])
    check("marker shape", changed["docs-a"]["stale_claims"][0] == {
        "entity_key": "version/pulumi-gcp", "claim_text": "pulumi-gcp v8.3.0",
        "verdict": "contradicted",
        "evidence": "v9.0 released", "source": "gh release view",
        "checked_at": "2026-07-09"})
    check("ledger gap is skipped, not stubbed over",
          "docs-b" not in changed and "content/docs/b.md" not in ledger)

    changed2 = apply_markers(ledger, stale, today)
    check("re-marking is idempotent",
          len(changed2["docs-a"]["stale_claims"]) == 1)

    # Generated pages have no markdown source, so select-articles.py can never
    # queue them and a marker there could never be cleared. Report, don't mark.
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "content/docs").mkdir(parents=True)
        (root / "content/docs/a.md").write_text("real page\n")
        gen = [{"entity_key": "numerical/pack-count", "verdict": "contradicted",
                "evidence": "", "source": "",
                "pages": [{"path": "content/docs/reference/generated.md",
                           "slug": "docs-reference-generated"}]}]
        led = {"content/docs/reference/generated.md": {
            "path": "content/docs/reference/generated.md",
            "slug": "docs-reference-generated", "status": "clean"}}
        check("sourceless page gets no marker",
              apply_markers(led, gen, today, root) == {})
        check("sourceless page's ledger entry is left untouched",
              "stale_claims" not in led["content/docs/reference/generated.md"])
        # ...while a page that does exist on disk is still marked normally.
        led2 = {"content/docs/a.md": {"path": "content/docs/a.md",
                                      "slug": "docs-a", "status": "clean"}}
        on_disk = [{**gen[0], "pages": [{"path": "content/docs/a.md",
                                         "slug": "docs-a"}]}]
        check("page with a source file is still marked",
              set(apply_markers(led2, on_disk, today, root)) == {"docs-a"})
        # A generated page that IS on disk (the CLI command reference) is
        # `editable: false`: the fix lane can never select it, so a marker
        # there could never be resolved. The tier rules, not the file check,
        # are what catch it — and only when a claim spans an editable page too,
        # since fix_route() already routes an all-generated claim upstream.
        (root / "content/docs/iac/cli/commands").mkdir(parents=True)
        (root / "content/docs/iac/cli/commands/pulumi-up.md").write_text("# gen\n")
        gen_rules = [{"prefix": "content/docs/iac/cli/commands/", "tier": 0}]
        led3 = {"content/docs/a.md": {"path": "content/docs/a.md",
                                      "slug": "docs-a", "status": "clean"},
                "content/docs/iac/cli/commands/pulumi-up.md": {
                    "path": "content/docs/iac/cli/commands/pulumi-up.md",
                    "slug": "docs-iac-cli-commands-pulumi-up", "status": "clean"}}
        spanning = [{**gen[0], "pages": [
            {"path": "content/docs/a.md", "slug": "docs-a"},
            {"path": "content/docs/iac/cli/commands/pulumi-up.md",
             "slug": "docs-iac-cli-commands-pulumi-up"}]}]
        check("a non-editable page on disk gets no marker under the tier rules",
              set(apply_markers(led3, spanning, today, root, gen_rules)) == {"docs-a"})
        check("without tier rules the file check alone still marks it",
              set(apply_markers(led3, spanning, today, root))
              == {"docs-a", "docs-iac-cli-commands-pulumi-up"})

    check("already_marked sees the marker",
          already_marked("version/pulumi-gcp", ents["version/pulumi-gcp"], ledger))
    check("already_marked ignores other entities",
          not already_marked("numerical/team-plan-price",
                             ents["numerical/team-plan-price"], ledger))

    # Per-text grouping: the two pages word the pin differently, so they are
    # two claims under one key — each verified on its own, each marking only
    # its own pages. Identical wording on several pages stays one call.
    gcp_groups = claim_groups(ents["version/pulumi-gcp"])
    check("claim_groups splits distinct wordings", len(gcp_groups) == 2)
    check("claim_groups keeps identical wording together",
          len(claim_groups(ents["version/pulumi-gcp"] * 2)) == 2
          and all(len(g) == 2 for _, g in claim_groups(ents["version/pulumi-gcp"] * 2)))
    check("group text is the freshest wording of that group",
          [t for t, _ in gcp_groups] == ["pulumi-gcp v8.2.0", "pulumi-gcp v8.3.0"])
    g82 = [a for a in ents["version/pulumi-gcp"] if a["claim"]["text"] == "pulumi-gcp v8.2.0"]
    g83 = [a for a in ents["version/pulumi-gcp"] if a["claim"]["text"] == "pulumi-gcp v8.3.0"]
    text_marked = {"content/docs/b.md": {"path": "content/docs/b.md", "stale_claims": [
        {"entity_key": "version/pulumi-gcp", "claim_text": "Pulumi-GCP  v8.2.0"}]}}
    check("a text-bearing marker does not hold out a different wording",
          not already_marked("version/pulumi-gcp", g83, text_marked))
    check("a text-bearing marker holds out its own wording (case/space-insensitive)",
          already_marked("version/pulumi-gcp", g82 + g83, text_marked))
    legacy = {"content/docs/b.md": {"path": "content/docs/b.md", "stale_claims": [
        {"entity_key": "version/pulumi-gcp"}]}}
    check("a legacy marker with no claim_text holds out every wording",
          already_marked("version/pulumi-gcp", g83, legacy))

    # Page context: the heading the claim sits under plus the prose around it.
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "content/docs").mkdir(parents=True)
        (root / "content/docs/ctx.md").write_text(
            "# Secrets\n\nintro\n\n#### AWS KMS\n\nThe awskms provider.\n\n"
            "As of v3.33.1, add awssdk=v2 to the query string.\n\n1. By ID\n")
        ctx = page_context(root, "content/docs/ctx.md", "L9")
        check("page_context leads with the enclosing heading", ctx.startswith("#### AWS KMS"))
        check("page_context carries the claim's own line", "awssdk=v2" in ctx)
        check("page_context reads a multi-range line_range",
              "awssdk=v2" in page_context(root, "content/docs/ctx.md", "L3, L9-9"))
        check("page_context is empty, never wrong, when it cannot read",
              page_context(root, "content/docs/ctx.md", "") == ""
              and page_context(root, "content/docs/missing.md", "L1") == ""
              and page_context(root, "content/docs/ctx.md", "L400") == ""
              and page_context(None, "content/docs/ctx.md", "L9") == "")

    # Accounting: which verdicts mark, which only report, what is inconclusive.
    page_a = [{"path": "content/docs/a.md", "slug": "docs-a"}]
    rows = [
        {"entity_key": "numerical/x", "verdict": "contradicted", "pages": page_a},
        {"entity_key": "version/y", "verdict": "framing-drift", "pages": page_a},
        {"entity_key": "version/z", "verdict": "verified", "pages": page_a},
        {"entity_key": "numerical/w", "verdict": "unverifiable",
         "demoted_from": "verified", "pages": page_a},
    ]
    counts, markable = tally(rows, {}, [], None, None)
    check("framing-drift is soft: reported, never markable",
          counts["n_soft"] == 1 and [r["entity_key"] for r in markable] == ["numerical/x"])
    check("soft verdicts are decided, not inconclusive",
          (counts["n_stale"], counts["n_fresh"], counts["n_inconclusive"],
           counts["n_demoted"]) == (1, 1, 1, 1))
    check("soft entities name their pages",
          counts["soft_entities"] == [{"entity_key": "version/y",
                                       "pages": ["content/docs/a.md"]}])

    # Health-observation meta: the early-exit paths must say why they stopped
    # (signal-health.py's reverify signal reads these fields).

    def run_report(d: Path, extra_env_unset: list[str], dry_run: bool = False) -> dict:
        saved = {k: os.environ.pop(k) for k in extra_env_unset if k in os.environ}
        try:
            argv = ["--claims-dir", str(d / "claims"), "--ledger-dir", str(d / "ledger"),
                    "--out", str(d / "report.json"), "--today", "2026-07-06"]
            if dry_run:
                argv.append("--dry-run")
            args = build_parser().parse_args(argv)
            run(args)
            return json.loads((d / "report.json").read_text())
        finally:
            os.environ.update(saved)

    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "claims").mkdir()
        (d / "ledger").mkdir()
        rep = run_report(d, [])
        check("empty claims dir -> skipped=no_snapshots",
              rep["meta"]["skipped"] == "no_snapshots" and rep["meta"]["n_due"] == 0)

        (d / "claims" / "docs-a.json").write_text(json.dumps(snap("a", "2026-07-01", ver)))
        rep = run_report(d, ["ANTHROPIC_API_KEY"])
        check("due entities without API key -> skipped=no_api_key",
              rep["meta"]["skipped"] == "no_api_key" and rep["meta"]["n_due"] == 1)

        # End to end (dry run, placeholder verdicts): one due entity worded two
        # ways across two pages is one rotation slot and two verifier calls,
        # and each result carries only the pages that share its wording.
        (d / "claims" / "docs-b.json").write_text(
            json.dumps(snap("b", "2026-07-05", dict(ver, text="pulumi-gcp v8.3.0"))))
        rep = run_report(d, ["ANTHROPIC_API_KEY"], dry_run=True)
        check("dry run verifies every distinct wording of a due entity",
              (rep["meta"]["n_due"], rep["meta"]["n_checked"]) == (1, 2)
              and "skipped" not in rep["meta"])
        check("each result carries only the pages sharing its wording",
              sorted((e["claim_text"], [p["slug"] for p in e["pages"]])
                     for e in rep["entities"])
              == [("pulumi-gcp v8.2.0", ["docs-a"]), ("pulumi-gcp v8.3.0", ["docs-b"])])

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall reverify-claims self-tests passed")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--claims-dir", default=".claims-cache",
                   help="local sync of the claims/ prefix")
    p.add_argument("--ledger-dir", default=".ledger-cache",
                   help="local sync of the ledger/ prefix (markers are written here)")
    p.add_argument("--count", type=int, default=DEFAULT_COUNT,
                   help="entities to re-verify tonight (chunk size of the rotation)")
    p.add_argument("--today", help="override today's date YYYY-MM-DD (testing)")
    p.add_argument("--repo-root", default=str(HERE), help="repo root for the verifier's read_file")
    p.add_argument("--tiers",
                   default=str(HERE / ".claude/commands/review-existing-content"
                                      "/references/strategic-tiers.yaml"),
                   help="tier rules; tier 0 (generated) routes findings upstream, not to a marker")
    p.add_argument("--known-upstream",
                   default=str(HERE / ".claude/commands/review-existing-content"
                                      "/references/upstream-claims.yaml"),
                   help="findings already filed upstream (suppresses the repeat Slack line only)")
    p.add_argument("--model", default=None, help="verifier model (default: verify-claims.py's)")
    p.add_argument("--out", default=".claims-reverify-report.json")
    p.add_argument("--dry-run", action="store_true",
                   help="no API calls, no uploads; placeholder verdicts (testing)")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    return p


def main() -> int:
    args = build_parser().parse_args()

    if args.self_test:
        return self_test()
    if args.model is None:
        args.model = _load_verify_claims().DEFAULT_MODEL
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
