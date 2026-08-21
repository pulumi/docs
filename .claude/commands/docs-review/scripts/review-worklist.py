#!/usr/bin/env python3
"""review-worklist.py — turn a pinned pre-merge review into an author worklist.

The pinned `<!-- CLAUDE_REVIEW N/M -->` comment is written for reading, not for
working: findings live in four H3 buckets plus an H4 style block, the one-click
suggestions live in a separate review-comment thread, and nothing in either
place tracks whether the author actually did something about an item. An author
(or an agent working with one) who clears 🚨 and stops reading leaves the rest
silently unaddressed — which is exactly what the `ignored_low_confidence` column
in scrape-review-outcomes.py keeps measuring.

This script enumerates every item that needs a disposition, assigns each a
stable id, and — given a state file recording what was decided — reports what is
left. It is the deterministic half of the `/address-review` skill: the model
decides *what* to do with a finding, this decides *whether anything is still
undecided*. Nothing here writes to GitHub.

Disposition vocabulary (closed set, see `address-review:references:dispositions`):

    fixed       — the diff changed; the finding no longer applies
    refuted     — disputed with evidence via `@claude #update-review`
    deferred    — real but out of scope; tracked in a filed issue (note required)
    accepted    — knowingly shipping as-is (note required)
    not-applicable — the finding misreads the change; nothing to do (note required)

`fixed` and `refuted` are self-evidencing — the diff or the dispute comment is
the record. The other three are judgment calls someone has to own, so they carry
a mandatory note that `--require-clean` enforces.

Usage:
  review-worklist.py --pr 20123 [--repo owner/repo]
      Fetch the pinned review + inline style suggestions; print a markdown
      checklist.
  review-worklist.py --pr 20123 --format json
      Same, as JSON (what the skill parses).
  review-worklist.py --body-file pinned.md [--suggestions-file comments.json]
      Offline: parse a body already on disk. `--suggestions-file` takes the raw
      `gh api .../pulls/N/comments` JSON array.
  review-worklist.py --pr 20123 --state .review-state.json --require-clean
      Exit 1 when any non-optional item has no disposition (or a note-requiring
      disposition has no note). This is the "is the PR actually done?" check.
  review-worklist.py --self-test
      Run embedded parse checks (no network).

Parsing reuses validate-pinned.py's body helpers (find_section,
extract_bucket_bullets, extract_count_table_row, extract_trail_records,
extract_bullet_prefix) so the comment-format contract keeps exactly one parser —
same import-by-path pattern as scrape-review-outcomes.py.

Fail-open on inputs, fail-closed on completeness. Three things independently
block a "clean" verdict, so --require-clean can only pass when the whole list
was actually seen: an unparseable body (`parse_confidence: "low"`), a failed
inline-suggestions fetch (`suggestions_ok: false` — distinct from a PR that
genuinely has none), and any parsed item without a recorded disposition.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Single source of truth for pinned-body parsing. validate-pinned.py's name is
# hyphenated, so import by path; its main() is __main__-guarded, so importing
# has no side effects.
_spec = importlib.util.spec_from_file_location("validate_pinned", HERE / "validate-pinned.py")
_vp = importlib.util.module_from_spec(_spec)
# Register before exec: validate-pinned.py defines dataclasses, and the
# dataclass machinery resolves the defining module through sys.modules.
sys.modules["validate_pinned"] = _vp
_spec.loader.exec_module(_vp)

DEFAULT_REPO = "pulumi/docs"
PAGE_DELIMITER = "----- PINNED-COMMENT-DELIMITER -----"
MARKER_RE = re.compile(r"^<!-- CLAUDE_REVIEW \d+/\d+ -->\s*$", re.M)
HEAD_SENTINEL_RE = re.compile(r"<!-- CLAUDE_REVIEW_HEAD ([0-9a-f]{7,40}) -->")
# Inline one-click suggestions are posted by post-style-suggestions.py; every
# comment body it writes starts with this marker.
SUGGESTION_MARKER = "<!-- CLAUDE_STYLE_SUGGESTION -->"
STYLE_BULLET_RE = re.compile(r"^\s*-\s+\*\*line (\d+):?\*\*\s*(.*)$")
STYLE_FILE_HEADING_RE = re.compile(r"^#####\s+`?([^`\s]+)`?\s*$")
FINDING_START_RE = re.compile(r"^(?:- )?\*\*\S")

DISPOSITIONS = ("fixed", "refuted", "deferred", "accepted", "not-applicable")
# Dispositions that are a judgment call rather than a change in the diff. The
# review record can't evidence these on its own, so a human-readable reason is
# mandatory — otherwise "accepted" becomes an unaudited way to close the loop.
NOTE_REQUIRED = ("deferred", "accepted", "not-applicable")

# Every bucket's configuration, read by both extraction paths — the plain-H3
# loop and the ⚠️ split. `low` and `style` share a heading because the style
# block is an H4 *inside* the ⚠️ Low-confidence H3; _split_low_confidence
# divides them. Nothing hard-codes a heading string outside this table.
BUCKETS = {
    # id prefix        heading substring         blocking  optional
    "outstanding": ("🚨 Outstanding", True, False),
    "low": ("⚠️ Low-confidence", False, False),
    "style": ("⚠️ Low-confidence", False, False),
    "pre-existing": ("💡 Pre-existing", False, True),
}
# Buckets whose bullets sit directly under their own H3, with no H4 split.
PLAIN_BUCKETS = ("outstanding", "pre-existing")


def log(msg: str) -> None:
    print(f"review-worklist: {msg}", file=sys.stderr)


# ---- gh access ---------------------------------------------------------------


def run(args: list[str]) -> str:
    """Run a command; return stdout, or "" on failure (logged to stderr)."""
    try:
        proc = subprocess.run(args, capture_output=True, text=True, check=True)
        return proc.stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        detail = exc.stderr.strip() if getattr(exc, "stderr", "") else str(exc)
        log(f"warning: {' '.join(args[:4])}... failed: {detail}")
        return ""


def fetch_pinned_body(repo: str, pr: int) -> str:
    return run(["bash", str(HERE / "pinned-comment.sh"), "fetch", "--pr", str(pr), "--repo", repo])


def fetch_inline_suggestions(repo: str, pr: int) -> tuple[list[dict], bool]:
    """Return (suggestions, ok). `ok=False` means the fetch failed.

    The distinction is the whole point: "this PR has no ✏️ suggestions" and "I
    couldn't ask" both produce an empty list, and only one of them means the
    worklist is complete. `run()` swallows every gh failure (auth, rate limit,
    network) into "", so without this flag a --require-clean run could answer
    "clean" for a PR whose style items were never enumerated.
    """
    out = run([
        "gh", "api", f"repos/{repo}/pulls/{pr}/comments",
        "--paginate",
        "--jq", f'[.[] | select(.body | startswith("{SUGGESTION_MARKER}"))]',
    ])
    # `--jq '[...]'` prints at least `[]` per page on success, so silence is failure.
    if not out.strip():
        return [], False
    # --paginate --jq emits one JSON document per page; concatenate the arrays.
    merged: list[dict] = []
    decoded_any = False
    for chunk in out.strip().splitlines():
        try:
            parsed = json.loads(chunk)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, list):
            decoded_any = True
            merged.extend(x for x in parsed if isinstance(x, dict))
    # Bytes came back but nothing decoded — a format change or a truncated
    # response, not an empty suggestion set.
    return merged, decoded_any


# ---- body normalization ------------------------------------------------------


def join_pages(raw: str) -> str:
    """Fold a multi-comment fetch into one logical body.

    `pinned-comment.sh fetch` prints every page separated by a delimiter line,
    each still carrying its `<!-- CLAUDE_REVIEW N/M -->` marker. Sections can
    straddle a page boundary, so the parser needs them joined back together.
    """
    pages = raw.split(PAGE_DELIMITER)
    return MARKER_RE.sub("", "\n".join(p.strip("\n") for p in pages if p.strip()))


# ---- item extraction ---------------------------------------------------------


def _split_low_confidence(body: str) -> tuple[list[str], list[str]]:
    """Return (low-confidence bullets, style-block lines) from the ⚠️ section.

    The `#### Style suggestions` H4 lives *inside* the ⚠️ Low-confidence H3, and
    its bullets are uncounted advisory polish rather than reviewer burden — so
    they are their own bucket here, not low-confidence findings.

    Returns (low-confidence bullet blocks, raw style-block lines).
    """
    span = _vp.find_section(body, BUCKETS["low"][0])
    if span is None:
        return [], []
    start, end = span
    lines = body.splitlines()[start:end]
    style_idx = None
    for i, line in enumerate(lines):
        if line.strip() in _vp.STYLE_HEADINGS:
            style_idx = i
            break
    head = lines[:style_idx] if style_idx is not None else lines
    style = lines[style_idx:] if style_idx is not None else []
    blocks = [b for b in _bullet_blocks(head) if not STYLE_BULLET_RE.match(b[0])]
    return blocks, style


def _bullet_blocks(lines: list[str]) -> list[tuple[str, str]]:
    """Group each column-0 finding bullet with its continuation lines.

    `extract_bucket_bullets` returns first lines only ("Sub-bullets (indented)
    and continuation paragraphs (no leading `**`) are not counted"), which is
    right for counting and wrong for working: a 🚨 bullet's fix prose and
    suggested patch all live below its first line, and that is the part the
    author has to act on. One block per bullet, so the count still matches.
    """
    blocks: list[list[str]] = []
    current: list[str] | None = None
    for line in lines:
        if FINDING_START_RE.match(line):
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is not None:
            if line.startswith("#"):  # a nested heading ends the block
                blocks.append(current)
                current = None
            else:
                current.append(line)
    if current is not None:
        blocks.append(current)
    return [(b[0], "\n".join(b).strip()) for b in blocks]


def _first_sentence(bullet: str, limit: int = 160) -> str:
    """A one-line summary for the checklist view; `text` carries the whole bullet."""
    text = re.sub(r"^\s*-\s+", "", bullet).strip()
    text = re.sub(r"\s+", " ", text)
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def extract_items(body: str, suggestions: list[dict]) -> list[dict]:
    trail = {}
    for rec in _vp.extract_trail_records(body):
        for ref in rec.get("line_refs") or []:
            trail.setdefault(ref, rec.get("raw", "").strip())

    items: list[dict] = []
    seen: set[str] = set()

    def add(item: dict) -> None:
        # Two findings can share a line anchor (a contradicted claim and a
        # readthrough flag on the same range). Suffix rather than collapse:
        # dropping one would under-report the worklist.
        base = item["id"]
        n = 2
        while item["id"] in seen:
            item["id"] = f"{base}#{n}"
            n += 1
        seen.add(item["id"])
        items.append(item)

    for prefix in PLAIN_BUCKETS:
        heading, blocking, optional = BUCKETS[prefix]
        span = _vp.find_section(body, heading)
        section = body.splitlines()[span[0]:span[1]] if span else []
        for first, full in _bullet_blocks(section):
            anchor = _vp.extract_bullet_prefix(first) or "L?"
            add({
                "id": f"{prefix}:{anchor}",
                "bucket": prefix,
                "anchor": anchor,
                "blocking": blocking,
                "optional": optional,
                "summary": _first_sentence(first),
                "text": full,
                "trail": trail.get(anchor, ""),
            })

    low_blocks, style_lines = _split_low_confidence(body)
    _, low_blocking, low_optional = BUCKETS["low"]
    for first, full in low_blocks:
        anchor = _vp.extract_bullet_prefix(first) or "L?"
        add({
            "id": f"low:{anchor}",
            "bucket": "low",
            "anchor": anchor,
            "blocking": low_blocking,
            "optional": low_optional,
            "summary": _first_sentence(first),
            "text": full,
            "trail": trail.get(anchor, ""),
        })

    # Style bullets are grouped under an `##### <path>` H5 per file, so this
    # walk tracks the heading rather than reusing _bullet_blocks wholesale;
    # continuation lines still fold into the bullet they belong to.
    _, style_blocking, style_optional = BUCKETS["style"]
    current_file = ""
    last: dict | None = None
    for line in style_lines:
        heading = STYLE_FILE_HEADING_RE.match(line.strip())
        if heading:
            current_file = heading.group(1)
            last = None
            continue
        m = STYLE_BULLET_RE.match(line)
        if m:
            last = {
                "id": f"style:{current_file or '?'}:L{m.group(1)}",
                "bucket": "style",
                "anchor": f"L{m.group(1)}",
                "file": current_file,
                "blocking": style_blocking,
                "optional": style_optional,
                "one_click": False,
                "summary": _first_sentence(line),
                "text": line.strip(),
                "trail": "",
            }
            add(last)
            continue
        if last is not None and line.strip() and not line.startswith("#"):
            last["text"] += "\n" + line.rstrip()

    # Mark the style items that have a live one-click button, and surface any
    # posted suggestion the pinned block doesn't carry (a stale ✏️ annotation
    # would otherwise hide it).
    by_key = {it["id"]: it for it in items}
    for sug in suggestions:
        path = str(sug.get("path") or "")
        line_no = sug.get("line") or sug.get("original_line")
        if not path or not line_no:
            continue
        key = f"style:{path}:L{line_no}"
        target = by_key.get(key)
        if target is not None:
            target["one_click"] = True
            target["comment_id"] = sug.get("id")
            continue
        add({
            "id": key,
            "bucket": "style",
            "anchor": f"L{line_no}",
            "file": path,
            "blocking": False,
            "optional": False,
            "one_click": True,
            "comment_id": sug.get("id"),
            "summary": _first_sentence(str(sug.get("body") or "").replace(SUGGESTION_MARKER, "")),
            "text": str(sug.get("body") or ""),
            "trail": "",
        })

    return items


# ---- state -------------------------------------------------------------------


def load_state(path: Path) -> dict[str, dict]:
    """Read a disposition state file.

    Accepts both the full form (`{"items": {id: {disposition, note}}}`) and the
    shorthand a hand-edit tends to produce (`{id: "fixed"}`).
    """
    # A missing file is the first run, not an error: the skill passes --state on
    # every invocation, including the one that builds the list to begin with.
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"review-worklist: cannot read state file {path}: {exc}")
    if isinstance(data, dict) and isinstance(data.get("items"), dict):
        data = data["items"]
    if not isinstance(data, dict):
        raise SystemExit(f"review-worklist: state file {path} is not an object")
    out: dict[str, dict] = {}
    for key, value in data.items():
        if isinstance(value, str):
            value = {"disposition": value}
        if not isinstance(value, dict):
            raise SystemExit(f"review-worklist: state entry {key!r} is not an object or string")
        disp = value.get("disposition")
        if disp not in DISPOSITIONS:
            raise SystemExit(
                f"review-worklist: state entry {key!r} has disposition {disp!r}; "
                f"expected one of {', '.join(DISPOSITIONS)}"
            )
        out[key] = {"disposition": disp, "note": str(value.get("note") or "").strip()}
    return out


def apply_state(items: list[dict], state: dict[str, dict]) -> list[dict]:
    """Attach dispositions to items and flag the ones that don't hold up."""
    for item in items:
        rec = state.get(item["id"])
        item["disposition"] = rec["disposition"] if rec else None
        item["note"] = rec["note"] if rec else ""
        if rec and rec["disposition"] in NOTE_REQUIRED and not rec["note"]:
            item["problem"] = f"disposition `{rec['disposition']}` requires a note"
        else:
            item.pop("problem", None)
    known = {it["id"] for it in items}
    stale = [
        {"id": key, "disposition": rec["disposition"], "note": rec["note"]}
        for key, rec in state.items()
        if key not in known
    ]
    return stale


def summarize(items: list[dict], parse_confidence: str, suggestions_ok: bool = True) -> dict:
    remaining = [
        it for it in items
        if not it.get("optional") and (not it.get("disposition") or it.get("problem"))
    ]
    counts: dict[str, int] = {}
    for it in items:
        counts[it["bucket"]] = counts.get(it["bucket"], 0) + 1
    return {
        "counts": counts,
        "total": len(items),
        "resolved": sum(1 for it in items if it.get("disposition") and not it.get("problem")),
        "remaining": len(remaining),
        "remaining_ids": [it["id"] for it in remaining],
        # Clean means "everything was seen and everything was decided". A body
        # that didn't parse or a suggestions fetch that failed means the first
        # half is unproven, whatever the dispositions say.
        "clean": not remaining and parse_confidence == "high" and suggestions_ok,
    }


# ---- rendering ---------------------------------------------------------------

BUCKET_LABEL = {
    "outstanding": "🚨 Outstanding — must be fixed or refuted before merge",
    "low": "⚠️ Low-confidence — each needs a decision, none block the PR",
    "style": "✏️ Style suggestions — advisory; ✏️ marks a one-click apply",
    "pre-existing": "💡 Pre-existing — optional; not introduced by this PR",
}


def render_markdown(report: dict) -> str:
    out: list[str] = []
    s = report["summary"]
    header = f"# Review worklist — {report['remaining_label']}"
    out.append(header)
    out.append("")
    if report["parse_confidence"] != "high":
        out.append("> **Parse confidence: low.** The pinned review did not parse into buckets; "
                   "work from the comment itself and treat this list as incomplete.")
        out.append("")
    if not report.get("suggestions_ok", True):
        out.append("> **Inline suggestions could not be fetched.** Any ✏️ one-click suggestions on "
                   "the Files-changed tab are missing from this list — check them by hand.")
        out.append("")
    out.append(f"{s['resolved']} of {s['total']} items dispositioned · "
               f"{s['remaining']} still needing a decision")
    out.append("")
    for bucket in ("outstanding", "low", "style", "pre-existing"):
        rows = [it for it in report["items"] if it["bucket"] == bucket]
        if not rows:
            continue
        out.append(f"## {BUCKET_LABEL[bucket]}")
        out.append("")
        for it in rows:
            box = "x" if it.get("disposition") and not it.get("problem") else " "
            tail = ""
            if it.get("disposition"):
                tail = f" — **{it['disposition']}**"
                if it.get("note"):
                    tail += f" ({it['note']})"
            if it.get("problem"):
                tail += f" ⚠️ {it['problem']}"
            if it.get("one_click"):
                tail += " ✏️"
            out.append(f"- [{box}] `{it['id']}` {it['summary']}{tail}")
        out.append("")
    if report["stale_state"]:
        out.append("## Recorded against findings no longer in the review")
        out.append("")
        for row in report["stale_state"]:
            out.append(f"- `{row['id']}` — {row['disposition']} (gone from the current review)")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def _remaining_label(summary: dict, items: list[dict]) -> str:
    if not summary["clean"]:
        if not summary["remaining"]:
            # Everything listed was decided, but the list itself isn't trustworthy.
            return "every listed item decided — but the list is incomplete"
        return f"{summary['remaining']} item(s) still open"
    untouched_optional = sum(1 for it in items if it.get("optional") and not it.get("disposition"))
    if untouched_optional:
        return f"all required items dispositioned ✅ ({untouched_optional} optional left alone)"
    return "all items dispositioned ✅"


def build_report(body: str, suggestions: list[dict], state: dict[str, dict], pr: int | None,
                 repo: str, suggestions_ok: bool = True) -> dict:
    parse_confidence = "high" if _vp.extract_count_table_row(body) else "low"
    items = extract_items(body, suggestions)
    stale = apply_state(items, state)
    summary = summarize(items, parse_confidence, suggestions_ok)
    head = HEAD_SENTINEL_RE.search(body)
    return {
        "pr": pr,
        "repo": repo,
        "reviewed_sha": head.group(1) if head else None,
        "parse_confidence": parse_confidence,
        "suggestions_ok": suggestions_ok,
        "counts_table": _vp.extract_count_table_row(body),
        "items": items,
        "stale_state": stale,
        "summary": summary,
        "remaining_label": _remaining_label(summary, items),
    }


# ---- self-test ---------------------------------------------------------------

_FIXTURE = """<!-- CLAUDE_REVIEW 1/1 -->
## Pre-merge Review — Last updated 2026-08-20T10:00:00Z
<!-- CLAUDE_REVIEW_HEAD abc1234 -->

| 🚨 Outstanding | ⚠️ Low-confidence | 💡 Pre-existing | ✅ Resolved |
| :---: | :---: | :---: | :---: |
| **1** | **1** | **1** | **0** |

### 🔍 Verification trail

<details>
<summary><strong>2 claims extracted</strong></summary>

- L40 in `content/docs/a.md` "Pulumi supports 9 languages." → ❌ contradicted (evidence: six)
- L12 in `content/docs/a.md` "Teams often do X." → 🤷 unverifiable (evidence: none)

</details>

### 🚨 Outstanding in this PR

*These must be resolved or refuted before merging.*

- **[L40]** The language count is wrong; the docs say six.

  Suggested fix:

  ```diff
  - nine languages
  + six languages
  ```

### ⚠️ Low-confidence

*Review each and resolve as appropriate — these don't block the PR.*

- **[L12]** Unattributed "teams often" claim — can you cite it?

#### Style suggestions

*Pattern-based linting; advisory.*

##### `content/docs/a.md`

- **line 88:** "Simply run" → "Run" ✏️
- **line 91:** "utilize" → "use"

### 💡 Pre-existing issues in touched files

- **[L7]** Heading is title case; house style is sentence case.

### 📜 Review history

- 2026-08-20T10:00:00Z — initial review (abc1234)
"""


def self_test() -> int:
    failures: list[str] = []

    def check(label: str, cond: bool) -> None:
        if not cond:
            failures.append(label)

    body = join_pages(_FIXTURE)
    check("marker stripped", "<!-- CLAUDE_REVIEW 1/1 -->" not in body)

    items = extract_items(body, [])
    ids = [it["id"] for it in items]
    check("outstanding parsed", "outstanding:L40" in ids)
    check("low-confidence parsed", "low:L12" in ids)
    check("style bullets parsed", "style:content/docs/a.md:L88" in ids)
    check("second style bullet parsed", "style:content/docs/a.md:L91" in ids)
    check("pre-existing parsed", "pre-existing:L7" in ids)
    check("style not counted as low-confidence", sum(1 for i in items if i["bucket"] == "low") == 1)
    check("four buckets, five items", len(items) == 5)

    outstanding = next(i for i in items if i["id"] == "outstanding:L40")
    check("trail attached", "contradicted" in outstanding["trail"])
    check("outstanding blocks", outstanding["blocking"] is True)
    # The fix prose and patch below a bullet's first line are the part the
    # author has to act on — they must survive into `text`.
    check("multi-line bullet captured", "+ six languages" in outstanding["text"])
    check("summary stays one line", "\n" not in outstanding["summary"])
    check("block stops at the next bullet",
          "Unattributed" not in outstanding["text"])
    check("pre-existing optional",
          next(i for i in items if i["bucket"] == "pre-existing")["optional"] is True)

    # Inline suggestion marks its bullet and adds an unlisted one.
    sugs = [
        {"id": 1, "path": "content/docs/a.md", "line": 88, "body": SUGGESTION_MARKER + "\nx"},
        {"id": 2, "path": "content/docs/b.md", "line": 5, "body": SUGGESTION_MARKER + "\ny"},
    ]
    items2 = extract_items(body, sugs)
    marked = next(i for i in items2 if i["id"] == "style:content/docs/a.md:L88")
    check("one-click marked", marked["one_click"] is True and marked["comment_id"] == 1)
    check("orphan suggestion surfaced", "style:content/docs/b.md:L5" in [i["id"] for i in items2])

    # Nothing dispositioned → nothing clean; optional items don't hold it back.
    r0 = build_report(body, [], {}, 20123, DEFAULT_REPO)
    check("all open initially", r0["summary"]["remaining"] == 4)
    check("not clean when open", r0["summary"]["clean"] is False)
    check("sha sentinel read", r0["reviewed_sha"] == "abc1234")

    state = {
        "outstanding:L40": {"disposition": "fixed", "note": ""},
        "low:L12": {"disposition": "refuted", "note": ""},
        "style:content/docs/a.md:L88": {"disposition": "fixed", "note": ""},
        "style:content/docs/a.md:L91": {"disposition": "accepted", "note": ""},
    }
    r1 = build_report(body, [], state, 20123, DEFAULT_REPO)
    check("note-required flagged",
          r1["summary"]["remaining_ids"] == ["style:content/docs/a.md:L91"])
    state["style:content/docs/a.md:L91"]["note"] = "term of art in this page"
    r2 = build_report(body, [], state, 20123, DEFAULT_REPO)
    check("clean once noted", r2["summary"]["clean"] is True)
    check("optional item stays optional", r2["summary"]["remaining"] == 0)

    state["outstanding:L999"] = {"disposition": "fixed", "note": ""}
    r3 = build_report(body, [], state, 20123, DEFAULT_REPO)
    check("stale state reported", [s["id"] for s in r3["stale_state"]] == ["outstanding:L999"])

    # State-file handling: absent is a first run, shorthand parses, junk is loud.
    check("missing state file is empty", load_state(HERE / "no-such-state-file.json") == {})
    with tempfile.TemporaryDirectory() as tmp:
        shorthand = Path(tmp) / "s.json"
        shorthand.write_text('{"outstanding:L40": "fixed"}', encoding="utf-8")
        check("shorthand state parses",
              load_state(shorthand) == {"outstanding:L40": {"disposition": "fixed", "note": ""}})
        bad = Path(tmp) / "bad.json"
        bad.write_text('{"outstanding:L40": "wontfix"}', encoding="utf-8")
        try:
            load_state(bad)
            check("invalid disposition rejected", False)
        except SystemExit:
            check("invalid disposition rejected", True)

    # An unparseable body must never read as an all-clear.
    r4 = build_report("nothing to see here", [], {}, 20123, DEFAULT_REPO)
    check("low parse confidence", r4["parse_confidence"] == "low")
    check("low parse is never clean", r4["summary"]["clean"] is False)

    # Nor may a failed suggestions fetch: every item decided, list unproven.
    r5 = build_report(body, [], state, 20123, DEFAULT_REPO, suggestions_ok=False)
    check("failed suggestions fetch blocks clean", r5["summary"]["clean"] is False)
    check("failed fetch reported", r5["suggestions_ok"] is False)
    check("label says incomplete, not open",
          "incomplete" in r5["remaining_label"] and "still open" not in r5["remaining_label"])
    check("markdown warns about the gap", "could not be fetched" in render_markdown(r5))

    check("markdown renders", "🚨 Outstanding" in render_markdown(r1))

    for f in failures:
        print(f"FAIL: {f}", file=sys.stderr)
    print(f"review-worklist self-test: {'FAILED' if failures else 'passed'}", file=sys.stderr)
    return 1 if failures else 0


# ---- entry point -------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pr", type=int, help="PR number to fetch the pinned review from")
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--body-file", help="parse this pinned body instead of fetching")
    ap.add_argument("--suggestions-file",
                    help="raw `gh api .../pulls/N/comments` JSON array (offline mode)")
    ap.add_argument("--state", help="JSON file of recorded dispositions")
    ap.add_argument("--format", choices=("markdown", "json"), default="markdown")
    ap.add_argument("--require-clean", action="store_true",
                    help="exit 1 when any non-optional item is still undecided")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()
    if not args.pr and not args.body_file:
        ap.error("one of --pr, --body-file, --self-test is required")

    if args.body_file:
        raw = Path(args.body_file).read_text(encoding="utf-8")
    else:
        raw = fetch_pinned_body(args.repo, args.pr)
    if not raw.strip():
        log("no pinned review found — is the PR still a draft, or did review short-circuit?")
        return 1 if args.require_clean else 0
    body = join_pages(raw)

    if args.suggestions_file:
        try:
            loaded = json.loads(Path(args.suggestions_file).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SystemExit(f"review-worklist: cannot read {args.suggestions_file}: {exc}")
        suggestions = [x for x in loaded if isinstance(x, dict)] if isinstance(loaded, list) else []
        suggestions_ok = isinstance(loaded, list)
    elif args.pr:
        suggestions, suggestions_ok = fetch_inline_suggestions(args.repo, args.pr)
        if not suggestions_ok:
            log("warning: could not fetch inline style suggestions — worklist is incomplete")
    else:
        # --body-file with no --pr: the caller opted out of the suggestions lane
        # deliberately, so completeness is theirs to assert, not ours to doubt.
        suggestions, suggestions_ok = [], True

    state = load_state(Path(args.state)) if args.state else {}
    report = build_report(body, suggestions, state, args.pr, args.repo, suggestions_ok)

    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_markdown(report), end="")

    if args.require_clean and not report["summary"]["clean"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
