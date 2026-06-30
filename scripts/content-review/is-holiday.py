#!/usr/bin/env python3
"""Decide whether a date is a company holiday, per an iCalendar (ICS) feed.

The content-review dispatcher uses this to skip its scheduled run on company
holidays. It reads an ICS feed (the Pulumi BambooHR "Company Holidays" feed) and
exits 0 when the target date — today in --tz by default — falls on a holiday,
and 1 otherwise. The dispatcher runs `if this exits 1`, so:

    exit 0  -> today IS a holiday   -> dispatcher skips
    exit 1  -> not a holiday/error  -> dispatcher runs

Errors FAIL OPEN (treated as "not a holiday", exit 1) so a calendar fetch or
parse hiccup never silently halts the pipeline — at worst it runs on a holiday
and opens PRs nobody reads until the next workday.

Only all-day VEVENTs whose CATEGORIES contains --category (default
"Company Holidays", case-insensitive) count. So even if the feed is ever
repointed at a broader calendar that also carries individual time off, this only
ever skips on real company holidays, never on someone's PTO. Pass --any-category
to match every event regardless.

All-day events use `VALUE=DATE` with an EXCLUSIVE DTEND (the morning after), so a
single-day holiday is DTSTART=D, DTEND=D+1, and the match is DTSTART <= day < DTEND.

Usage:
    is-holiday.py --ics feed.ics [--tz America/Chicago] [--date 2026-07-03]
    is-holiday.py --self-test
"""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime, timedelta

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover - py<3.9
    ZoneInfo = None


def unfold(text: str) -> list[str]:
    """Undo RFC 5545 line folding (continuation lines start with space/tab)."""
    out: list[str] = []
    for raw in text.splitlines():
        if raw[:1] in (" ", "\t") and out:
            out[-1] += raw[1:]
        else:
            out.append(raw)
    return out


def _parse_date(val: str) -> date | None:
    val = val.strip()[:8]
    try:
        return datetime.strptime(val, "%Y%m%d").date()
    except ValueError:
        return None


def parse_events(text: str) -> list[dict]:
    """Return [{start, end, summary, categories}] for all-day VEVENTs."""
    events: list[dict] = []
    cur: dict | None = None
    for line in unfold(text):
        if line == "BEGIN:VEVENT":
            cur = {"start": None, "end": None, "summary": "", "categories": ""}
        elif line == "END:VEVENT":
            if cur and cur["start"]:
                if cur["end"] is None:           # no DTEND -> single all-day event
                    cur["end"] = cur["start"] + timedelta(days=1)
                events.append(cur)
            cur = None
        elif cur is not None:
            name, _, value = line.partition(":")
            key = name.split(";", 1)[0].upper()
            if key == "DTSTART":
                cur["start"] = _parse_date(value)
            elif key == "DTEND":
                cur["end"] = _parse_date(value)
            elif key == "SUMMARY":
                cur["summary"] = value.strip()
            elif key == "CATEGORIES":
                cur["categories"] = value.strip()
    return events


def holiday_on(text: str, day: date, category: str | None) -> dict | None:
    """The first matching holiday event covering `day`, or None."""
    for ev in parse_events(text):
        if not ev["start"] or not ev["end"]:
            continue
        if category and category.lower() not in ev["categories"].lower():
            continue
        if ev["start"] <= day < ev["end"]:
            return ev
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--ics", help="path to the ICS feed file")
    ap.add_argument("--tz", default="America/Chicago", help="timezone defining 'today'")
    ap.add_argument("--date", help="override target date (YYYY-MM-DD); default: today in --tz")
    ap.add_argument("--category", default="Company Holidays",
                    help="only match events whose CATEGORIES contains this (case-insensitive)")
    ap.add_argument("--any-category", action="store_true", help="match events of any category")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()
    if not args.ics:
        ap.error("--ics is required (or --self-test)")

    # Resolve the target date. Any failure fails open (not a holiday -> run).
    try:
        if args.date:
            day = datetime.strptime(args.date, "%Y-%m-%d").date()
        elif ZoneInfo is not None:
            day = datetime.now(ZoneInfo(args.tz)).date()
        else:
            day = datetime.now().date()
    except Exception as e:  # noqa: BLE001 - fail open on any clock/tz error
        print(f"is-holiday: could not resolve date ({e}); treating as non-holiday", file=sys.stderr)
        return 1

    try:
        text = open(args.ics, encoding="utf-8", errors="replace").read()
    except OSError as e:
        print(f"is-holiday: could not read {args.ics} ({e}); treating as non-holiday", file=sys.stderr)
        return 1

    category = None if args.any_category else args.category
    match = holiday_on(text, day, category)
    if match:
        print(f"is-holiday: {day} is a company holiday: {match['summary'] or '(unnamed)'}")
        return 0
    print(f"is-holiday: {day} is not a company holiday")
    return 1


def self_test() -> int:
    failures = []

    def check(name, cond):
        print(("ok: " if cond else "FAIL: ") + name, file=sys.stdout if cond else sys.stderr)
        if not cond:
            failures.append(name)

    ics = (
        "BEGIN:VCALENDAR\r\n"
        "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE:20260703\r\nDTEND;VALUE=DATE:20260704\r\n"
        "CATEGORIES:Company Holidays\r\nSUMMARY:Company Holiday - Independence Day\r\nEND:VEVENT\r\n"
        # a multi-day span (DTEND exclusive): covers 28th and 29th, not the 30th
        "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE:20261228\r\nDTEND;VALUE=DATE:20261230\r\n"
        "CATEGORIES:Company Holidays\r\nSUMMARY:Winter break\r\nEND:VEVENT\r\n"
        # a PTO event the same day as a workday — must be ignored by the category filter
        "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE:20260626\r\nDTEND;VALUE=DATE:20260627\r\n"
        "CATEGORIES:Time Off\r\nSUMMARY:Someone - Vacation\r\nEND:VEVENT\r\n"
        # a folded SUMMARY line + no DTEND (single all-day)
        "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE:20260907\r\n"
        "CATEGORIES:Company Holidays\r\nSUMMARY:Company Holiday - \r\n Labor Day\r\nEND:VEVENT\r\n"
        "END:VCALENDAR\r\n"
    )
    cat = "Company Holidays"

    check("single-day holiday matches", holiday_on(ics, date(2026, 7, 3), cat) is not None)
    check("day before holiday does not match", holiday_on(ics, date(2026, 7, 2), cat) is None)
    check("DTEND is exclusive (day after does not match)", holiday_on(ics, date(2026, 7, 4), cat) is None)
    check("multi-day span: first day matches", holiday_on(ics, date(2026, 12, 28), cat) is not None)
    check("multi-day span: middle day matches", holiday_on(ics, date(2026, 12, 29), cat) is not None)
    check("multi-day span: exclusive end excluded", holiday_on(ics, date(2026, 12, 30), cat) is None)
    check("category filter ignores non-holiday PTO", holiday_on(ics, date(2026, 6, 26), cat) is None)
    check("--any-category would catch the PTO", holiday_on(ics, date(2026, 6, 26), None) is not None)
    check("missing DTEND -> single all-day match", holiday_on(ics, date(2026, 9, 7), cat) is not None)
    check("missing DTEND -> next day excluded", holiday_on(ics, date(2026, 9, 8), cat) is None)
    check("folded SUMMARY is unfolded", (holiday_on(ics, date(2026, 9, 7), cat) or {}).get("summary") == "Company Holiday - Labor Day")
    check("matched holiday carries its summary", "Independence Day" in (holiday_on(ics, date(2026, 7, 3), cat) or {}).get("summary", ""))

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall is-holiday self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
