#!/usr/bin/env python3
"""Render the content-review PR body's "Why this page" section deterministically.

The per-article worker (`.github/workflows/content-review-article.yml`) used to
let the review model narrate this provenance block from its local queue. That
queue was rebuilt traffic-blind, so the model wrote "traffic unavailable" even
when the dispatcher had selected the page using live traffic — the facts were
self-reported, not composed. This script composes them from the dispatcher's
queue entry instead (the same split the pre-merge review uses via
`compose-review.py`): code emits the facts, the model only writes judgment.

Input is the single-article queue the dispatcher handed the worker
(`.content-review-queue.json`): `traffic` and `reader_signals` meta blocks plus
one `articles[0]` entry carrying `monthly_visits`, `signals`, `tier`,
`no_retire`, `last_reviewed`, `attempts`, and `score`. Output is the exact
`## Why this page` Markdown the worker pastes verbatim into the PR body.

Usage:
    render-provenance.py --queue .content-review-queue.json --out .provenance.md
    render-provenance.py --queue .content-review-queue.json   # to stdout
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def _fmt_int(n) -> str:
    try:
        return f"{int(n):,}"
    except (TypeError, ValueError):
        return str(n)


def _period_str(traffic: dict) -> str | None:
    """Normalize the traffic period (a string, or a {start,end} object)."""
    period = traffic.get("period")
    if isinstance(period, dict):
        start, end = period.get("start"), period.get("end")
        if start and end:
            return f"{start} to {end}"
        return start or end
    return period or traffic.get("generated")


def _signal_lines(queue: dict, a: dict) -> list[str]:
    """Search + Reader-feedback lines, present only when the reader-signals
    export was available for the run (absent export -> no lines, matching the
    pre-signals PR body byte-for-byte)."""
    meta = queue.get("reader_signals") or {}
    if not meta.get("available"):
        return []
    signals = a.get("signals") or {}
    lines = []

    gsc_meta = meta.get("gsc") or {}
    if gsc_meta.get("available"):
        g = signals.get("gsc")
        if g:
            parts = [f"{_fmt_int(g['impressions'])} impressions", f"{g['ctr'] * 100:.2f}% CTR"]
            median = gsc_meta.get("median_ctr")
            if median:
                parts.append(f"corpus median {median * 100:.2f}%")
            period = _period_str(gsc_meta)
            if period:
                parts.append(f"period {period}")
            flag_s = " — **low-CTR flag**" if g.get("low_ctr_flag") else ""
            lines.append(f"- **Search:** {', '.join(parts)}{flag_s}")
        else:
            lines.append("- **Search:** no Search Console data for this page")

    fb_meta = meta.get("feedback") or {}
    if fb_meta.get("available"):
        f = signals.get("feedback")
        if f:
            total = f["yes"] + f["no"]
            neg = f" ({f['no'] / total:.0%} negative)" if total else ""
            lines.append(f"- **Reader feedback:** {f['yes']} yes / {f['no']} no{neg}")
        else:
            lines.append("- **Reader feedback:** none recorded")

    return lines


def render(queue: dict) -> str:
    articles = queue.get("articles") or []
    if not articles:
        raise SystemExit("render-provenance: no articles in queue")
    a = articles[0]
    traffic = queue.get("traffic") or {}

    path = a.get("path", "")
    url = a.get("url") or ""
    lane = a.get("lane") or "priority"
    tier = a.get("tier")
    no_retire = bool(a.get("no_retire"))
    visits = a.get("monthly_visits")
    last_reviewed = a.get("last_reviewed")
    attempts = int(a.get("attempts") or 0)
    score = a.get("score")

    # Traffic line: a real per-page figure when the snapshot resolved and the
    # page appeared in it; otherwise say so plainly (selection fell back to
    # tier + age). `available` is the queue-level snapshot-presence flag.
    if traffic.get("available") and visits is not None:
        period = _period_str(traffic)
        source = traffic.get("source")
        suffix = []
        if period:
            suffix.append(f"period {period}")
        if source:
            suffix.append(f"source `{source}`")
        tail = f" ({'; '.join(suffix)})" if suffix else ""
        traffic_line = f"{_fmt_int(visits)} monthly visits{tail}"
    elif traffic.get("available"):
        traffic_line = "not in the traffic snapshot this run (selected on tier + age)"
    else:
        traffic_line = "snapshot unavailable this run (selected on tier + age)"

    reviewed_line = (
        f"{last_reviewed} (`attempts: {attempts}`)"
        if last_reviewed
        else f"never (`attempts: {attempts}`)"
    )

    tier_line = f"{tier}" if tier is not None else "unclassified"
    tier_line += f" (`no_retire: {'true' if no_retire else 'false'}`)"

    score_line = f"{score}" if score is not None else "n/a (explicit dispatch)"

    page_line = f"`{path}`" + (f" → [{url}]({url})" if url else "")

    signal_lines = "".join(line + "\n" for line in _signal_lines(queue, a))

    return (
        "## Why this page\n\n"
        f"- **Page:** {page_line}\n"
        f"- **Lane:** {lane}\n"
        f"- **Strategic tier:** {tier_line}\n"
        f"- **Traffic:** {traffic_line}\n"
        f"{signal_lines}"
        f"- **Last reviewed:** {reviewed_line}\n"
        f"- **Selection score:** {score_line}\n"
        "\n_This section is composed deterministically from the selection queue;"
        " do not edit it._\n"
    )


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--queue", required=True, help="single-article queue JSON")
    p.add_argument("--out", help="output Markdown path (default: stdout)")
    args = p.parse_args()

    queue = json.loads(Path(args.queue).read_text())
    body = render(queue)
    if args.out:
        Path(args.out).write_text(body)
        print(f"render-provenance: wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
