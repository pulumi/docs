#!/usr/bin/env python3
"""Render the weekly #docs-ops digest from digest.py's JSON.

Everything structured is rendered here, deterministically: the SLA sweep's
verdicts grouped by team, the abandoned-PR list, the Sentinel-green PRs
ready to merge, per-team review-queue links, review-loop outcomes, failing
workflows, and the lane switches. The
only model-written part is the order (and a short "why") of the top "Needs a
human" list, which rank.py produces from `candidates` below; with no ranking
(model unavailable, or no --ranking) the renderer falls back to a fixed
priority order, so the digest never depends on the model.

Each PR appears at most once: whatever the top list shows is removed from the
grouped sections under it.

Grouped sections are capped to keep the message short. Whatever a cap cuts
goes to a thread reply instead (`render_parts` returns both texts), and the
cut reads "+N more in thread", so no "+N" in the digest is a dead end.

Usage:
  render.py candidates <digest.json>                 -> candidates JSON (rank.py input)
  render.py render <digest.json> [--ranking r.json] [--thread-out t.txt]
                                                     -> Slack mrkdwn message
                                                        (+ thread reply text)
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime

REPO_URL = "https://github.com/pulumi/docs"
TOP_N = 5
TITLE_MAX = 40
INLINE_MAX = 4          # links per grouped line before "+N more"
KEEP_OR_KILL_DAYS = 14  # open this long with no review state -> keep-or-kill
TELEMETRY_GAP = 0.25    # share of closed PRs with no review data worth flagging
BROKEN_STREAK = 3       # a workflow whose last N runs all failed is broken, not flaky
TREND_SHIFT = 0.25      # week-over-week throughput change worth a line

# Fallback ranking when the model is unavailable. Lower is more urgent.
KIND_PRIORITY = {
    "merged-over-findings": 0,
    "broken-workflow": 1,
    "abandoned": 2,
    "overdue": 3,
    "keep-or-kill": 4,
    "untriaged-issue": 5,
}


# ---- formatting helpers -------------------------------------------------------


def esc(text: str) -> str:
    """Slack mrkdwn escaping for text inside or outside a link. `|` would end
    a link's URL part early, so it becomes a slash."""
    return (text or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("|", "/")


def short(title: str, limit: int = TITLE_MAX) -> str:
    """Trim to `limit` characters at a word boundary."""
    title = " ".join((title or "").split())
    if len(title) <= limit:
        return title
    cut = title[: limit - 1]
    if " " in cut[limit // 2:]:
        cut = cut[: cut.rindex(" ")]
    return cut.rstrip(" ,:;-") + "…"


def pr_url(n: int) -> str:
    return f"{REPO_URL}/pull/{n}"


def issue_url(n: int) -> str:
    return f"{REPO_URL}/issues/{n}"


def link(url: str, text: str) -> str:
    return f"<{url}|{esc(text)}>"


def num(url: str, n: int) -> str:
    return link(url, "#%d" % n)


def fmt_age(days) -> str:
    if days is None:
        return "?"
    days = int(days)
    return f"{days // 365}y" if days >= 730 else f"{days}d"


def signed(n) -> str:
    return f"+{n}" if n > 0 else ("±0" if n == 0 else f"−{-n}")


THREAD_TITLE_MAX = 60


class Spill:
    """Collects the full version of every list a cap shortened, for the
    thread reply. Each entry is (heading, lines)."""

    def __init__(self):
        self.sections: list[tuple[str, list[str]]] = []

    def add(self, heading: str, lines: list[str]) -> None:
        self.sections.append((heading, lines))


def inline(items: list[str], limit: int = INLINE_MAX, spill: Spill | None = None,
           heading: str = "", full: list[str] | None = None) -> str:
    """Join items with a cap. With a Spill, a cut sends `full` (one line per
    item, same order as `items`) to the thread and says so."""
    shown = items[:limit]
    extra = len(items) - len(shown)
    if extra <= 0:
        return " · ".join(shown)
    if spill is not None and full is not None:
        spill.add(heading, full)
        return " · ".join(shown) + f" · +{extra} more in thread"
    return " · ".join(shown) + f" · +{extra} more"


def pr_line(url: str, n: int, title: str, detail: str = "") -> str:
    """One thread-reply line: a titled link plus its key fact."""
    return f"• {link(url, '#%d ' % n + short(title, THREAD_TITLE_MAX))}" + (f" — {esc(detail)}" if detail else "")


def owner(policy: dict, role: str) -> str:
    who = (policy.get("escalate_to") or {}).get(role) or ""
    return "" if not who or who.startswith("TODO") else f" → {who}"


# ---- view model ---------------------------------------------------------------


def _worst_role(roles: list[dict]) -> dict:
    # Most overdue relative to its own SLA; a 1bd tools SLA blown by 3 days
    # outranks a 3bd docs-guild SLA blown by 1.
    return max(roles, key=lambda r: (r["waited"] - r["sla"], r["waited"]))


def build_view(d: dict) -> dict:
    """Group the digest into the sections the message renders, and build the
    candidate pool for the top list. Pure: digest dict in, view dict out."""
    prs = {p["number"]: p for p in d.get("prs") or []}
    humans = {n: p for n, p in prs.items() if not p.get("is_bot")}
    sla = d.get("sla") or {}
    verdicts = {v["pr"]: v for v in sla.get("verdicts") or []} if sla.get("available") else {}
    policy = sla.get("policy") or {}
    sweep = sla.get("enabled")  # "on" | "off" | "unknown"

    candidates: list[dict] = []

    def add(kind, ref, number, title, url, facts, **extra):
        candidates.append({"kind": kind, "ref": ref, "number": number, "title": title,
                           "url": url, "facts": facts, **extra})

    ro = d.get("review_outcomes") or {}
    for m in (ro.get("merged_with_outstanding") or []) if ro.get("available") else []:
        n = m["pr"]
        count = len(m.get("findings") or [])
        add("merged-over-findings", f"pr:{n}", n, m.get("title") or "", m.get("url") or pr_url(n),
            f"{count} blocking finding(s) unanswered at merge; file a follow-up",
            findings=count, sort_key=-count)

    for wf in (d.get("workflow_failures") or {}).get("failing") or []:
        if wf.get("streak", 0) >= BROKEN_STREAK:
            add("broken-workflow", f"workflow:{wf['workflow']}", None, wf["workflow"],
                wf.get("last_failure_url") or f"{REPO_URL}/actions",
                f"failed its last {wf['streak']} runs ({wf['failures']}/{wf['runs']} this week); fix or disable",
                sort_key=-wf["streak"])

    # Ready to merge is the merge gate's own verdict (digest.py reads each
    # PR's Sentinel check), not a rebuild of it here. Humans are listed;
    # bot PRs (Dependabot, pulumi-bot) are only counted, since they go out
    # in batches.
    ready = [p for p in prs.values() if not p.get("isDraft") and p.get("sentinel") == "ready"]
    ready_humans = sorted((p for p in ready if not p.get("is_bot")), key=lambda p: -(p.get("age_days") or 0))
    ready_numbers = {p["number"] for p in ready}
    # A Sentinel-green PR is listed once, as ready. The sweep can still call
    # it overdue: the gate accepts an approval from any review team, while
    # the sweep waits on the routed team. The gate decides mergeability.

    waiting_on_author = 0
    for n, v in sorted(verdicts.items()):
        pr = humans.get(n)
        if pr is None or n in ready_numbers:
            continue
        if v["kind"] == "reviewer" and v.get("overdue"):
            worst = _worst_role(v["overdue"])
            others = [r["role"] + owner(policy, r["role"]) for r in v["overdue"] if r is not worst]
            facts = (f"{worst['role']} review {worst['waited']}bd on a {worst['sla']}bd SLA"
                     f"{owner(policy, worst['role'])}")
            if others:
                facts += f"; also overdue: {', '.join(others)}"
            add("overdue", f"pr:{n}", n, pr["title"], pr_url(n), facts,
                role=worst["role"], waited=worst["waited"], sla=worst["sla"], red=pr.get("checks") == "red",
                sort_key=-(worst["waited"] - worst["sla"]))
        elif v["kind"] == "author":
            if v.get("abandoned"):
                findings = v.get("undecided_count")
                what = f"{findings} findings open" if findings else "changes requested"
                days = v.get("closes_in_days")
                if sweep == "on":
                    # No projection (a `close` the dry run would issue now, or
                    # one that failed last sweep) means it's due immediately.
                    fate = f"closes in {days}d" if days else "closes at the next sweep"
                elif sweep == "off":
                    fate = "close or rescue it by hand"
                else:
                    fate = "closes on its own only if the SLA sweep is on"
                add("abandoned", f"pr:{n}", n, pr["title"], pr_url(n),
                    f"author idle {round(v['idle_days'])}d, {what}; {fate}",
                    idle_days=v["idle_days"], closes_in_days=v.get("closes_in_days"),
                    sort_key=days or 0)
            else:
                waiting_on_author += 1

    # "No verdict" only means "no reviewer clock" when the sweep's verdicts
    # actually arrived. Without them every PR looks verdict-free, and one
    # that simply wasn't evaluated would read as "never reviewed".
    for n, pr in sorted(humans.items()) if sla.get("available") else []:
        if pr.get("isDraft") or n in verdicts or n in ready_numbers:
            continue
        labels = set(pr.get("labels") or [])
        if (pr.get("age_days") or 0) > KEEP_OR_KILL_DAYS and not (labels & {"review:no-blockers",
                                                                           "review:outstanding-issues"}):
            add("keep-or-kill", f"pr:{n}", n, pr["title"], pr_url(n),
                f"open {pr['age_days']}d, never reviewed: keep or close",
                age_days=pr["age_days"], sort_key=-(pr.get("age_days") or 0))

    issues = d.get("issues") or {}
    for i in issues.get("new_this_week") or []:
        if i.get("needs_triage"):
            add("untriaged-issue", f"issue:{i['number']}", i["number"], i["title"], issue_url(i["number"]),
                "new issue, not triaged", sort_key=-(i.get("age_days") or 0))

    listed = {c["number"] for c in candidates if c["ref"].startswith("pr:")} | ready_numbers
    sentinel_seen = any(p.get("sentinel") in ("ready", "blocked", "none") for p in prs.values())
    return {
        "candidates": candidates,
        "ready": {"available": sentinel_seen, "humans": ready_humans,
                  "bots": sum(1 for p in ready if p.get("is_bot"))},
        "queues": d.get("review_queues"),
        "other_open": {
            "drafts": sum(1 for p in humans.values() if p.get("isDraft")),
            "waiting_on_author": waiting_on_author,
            "bots": sum(1 for p in prs.values() if p.get("is_bot") and p["number"] not in ready_numbers),
            "in_progress": sum(1 for n, p in humans.items()
                               if not p.get("isDraft") and n not in listed
                               and verdicts.get(n, {}).get("kind") != "author"),
        },
        "policy": policy,
        "sla": sla,
    }


def fallback_ranking(candidates: list[dict], limit: int | None = TOP_N) -> list[dict]:
    ordered = sorted(candidates, key=lambda c: (KIND_PRIORITY[c["kind"]], c.get("sort_key", 0), c["ref"]))
    return [{"ref": c["ref"], "why": c["facts"]} for c in ordered[:limit]]


def resolve_ranking(candidates: list[dict], ranking: dict | None) -> tuple[list[dict], str]:
    """The top list to render: the model's order when it's valid, else the
    fallback. Unknown refs and duplicates are dropped; a model list that ends
    up empty is treated as no ranking at all."""
    by_ref = {c["ref"]: c for c in candidates}
    picked, seen = [], set()
    for item in (ranking or {}).get("order") or []:
        ref = item.get("ref") if isinstance(item, dict) else None
        if ref in by_ref and ref not in seen:
            why = " ".join(str(item.get("why") or "").split())[:110] or by_ref[ref]["facts"]
            picked.append({"ref": ref, "why": why})
            seen.add(ref)
        if len(picked) == TOP_N:
            break
    if picked:
        return picked, "model"
    return fallback_ranking(candidates), "fallback"


# ---- rendering ----------------------------------------------------------------


def _header(d: dict) -> list[str]:
    when = d.get("generated_at")
    try:
        date = datetime.fromisoformat(when).strftime("%b %-d") if when else ""
    except ValueError:
        date = ""
    open_prs = len(d.get("prs") or [])
    open_issues = (d.get("issues") or {}).get("all_open_count")
    tw = (d.get("throughput") or {}).get("this_week") or {}
    pw = (d.get("throughput") or {}).get("prev_week") or {}

    def delta(opened, *closed):
        vals = [tw.get(k) for k in (opened, *closed)]
        return None if any(v is None for v in vals) else vals[0] - sum(vals[1:])

    pr_d = delta("prs_opened", "prs_merged", "prs_closed")
    is_d = delta("issues_opened", "issues_closed")
    head = f"*{open_prs}* open PRs" + (f" ({signed(pr_d)})" if pr_d is not None else "")
    if open_issues is not None:
        head += f" · *{open_issues}* issues" + (f" ({signed(is_d)})" if is_d is not None else "")
    suffix = " vs last week" if pr_d is not None or is_d is not None else ""
    lines = [f":clipboard: *Docs weekly* · {date}".rstrip(" ·"), head + suffix]

    # Throughput only earns a line when it moved: a flat week is already
    # summed up by the deltas above.
    shifts = []
    for key, label in (("prs_merged", "merged"), ("prs_opened", "opened")):
        now, prev = tw.get(key), pw.get(key)
        if now is not None and prev and abs(now - prev) / prev >= TREND_SHIFT:
            shifts.append(f"{now} PRs {label} (prior week {prev})")
    if shifts:
        lines.append("Throughput shift: " + " · ".join(shifts))
    return lines


def _cand_label(c: dict) -> str:
    return short(c["title"]) if c["number"] is None else "#%d " % c["number"] + short(c["title"])


def _top(view: dict, top: list[dict], spill: Spill) -> list[str]:
    by_ref = {c["ref"]: c for c in view["candidates"]}
    if not top:
        return ["*Needs a human*", "Nothing this week."]
    total = len(view["candidates"])
    head = "*Needs a human*" + (f" (top {len(top)} of {total})" if total > len(top) else "")
    out = [head]
    for i, t in enumerate(top, 1):
        c = by_ref[t["ref"]]
        out.append(f"{i}. {link(c['url'], _cand_label(c))} — {esc(t['why'])}")
    if total > len(top):
        # The model ranks only the top five; the rest continue in the fixed
        # priority order, numbered on from there. Each also sits in its
        # grouped section below, so the thread is the one ranked view.
        shown = {t["ref"] for t in top}
        rest = [r for r in fallback_ranking(view["candidates"], limit=None) if r["ref"] not in shown]
        lines = [f"{i}. {link(by_ref[r['ref']]['url'], _cand_label(by_ref[r['ref']]))} — {esc(r['why'])}"
                 for i, r in enumerate(rest, len(top) + 1)]
        spill.add(f"*Needs a human*, {len(top) + 1}–{total} (fixed priority order)", lines)
        out.append(f"_+{len(rest)} more in thread_")
    return out


READY_MAX = 12  # ready PRs are few and each is a click; list nearly all of them


def _queues(view: dict, spill: Spill) -> list[str]:
    """Two lines of standing queues, each item a link: Sentinel-green PRs
    (the merge gate says every sign-off is in) and, per routed team, the
    no-blockers PRs with that team's review still requested."""
    out = []
    r = view["ready"]
    bots = f"+{r['bots']} bot PR{'s' if r['bots'] != 1 else ''}" if r["bots"] else ""
    if not r["available"]:
        out.append(":warning: *Ready to merge*: Sentinel verdicts unreadable this week")
    elif r["humans"]:
        items = [num(pr_url(p["number"]), p["number"]) for p in r["humans"]]
        full = [pr_line(pr_url(p["number"]), p["number"], p["title"]) for p in r["humans"]]
        out.append(f"*Ready to merge* ({len(r['humans'])}, Sentinel green): "
                   + inline(items, READY_MAX, spill, "*Ready to merge* (Sentinel green)", full)
                   + (f" · {bots}" if bots else ""))
    else:
        out.append("*Ready to merge*: none" + (f" ({bots})" if bots else ""))
    queues = view.get("queues") or []
    if queues:
        links = [link(q["url"], f"{q['role']} {q['count'] if q['count'] is not None else '?'}") for q in queues]
        out.append("*Awaiting review* (no blockers, team requested): " + " · ".join(links))
    return out


def _team_line(role: str, items: list[dict], policy: dict, spill: Spill) -> str:
    # Red-CI PRs first and labelled: they need a fix from the author, not an
    # approval, so they must not hide behind "+N more".
    items.sort(key=lambda c: (not c.get("red"), -c["waited"], c["number"]))
    same_wait = len({c["waited"] for c in items}) == 1
    head = f"• {role}{owner(policy, role)} (SLA {items[0]['sla']}bd): "
    if same_wait:
        head += f"{len(items)} PR{'s' if len(items) > 1 else ''} at {items[0]['waited']}bd: "

    def item(c):
        text = num(c["url"], c["number"])
        if not same_wait:
            text += f" {c['waited']}bd"
        return text + (" red CI" if c.get("red") else "")

    full = [pr_line(c["url"], c["number"], c["title"],
                    f"{c['waited']}bd" + (", red CI" if c.get("red") else "")) for c in items]
    heading = f"*Over review SLA*: {role}{owner(policy, role)} (SLA {items[0]['sla']}bd)"
    return head + inline([item(c) for c in items], INLINE_MAX, spill, heading, full)


def _sections(view: dict, shown: set[str], spill: Spill) -> list[str]:
    rest = [c for c in view["candidates"] if c["ref"] not in shown]
    by_kind: dict[str, list[dict]] = {}
    for c in rest:
        by_kind.setdefault(c["kind"], []).append(c)
    out: list[str] = []
    policy = view["policy"]

    sla = view["sla"]
    if not sla.get("available"):
        out += ["", ":warning: SLA verdicts unavailable this week (the sweep dry-run failed): "
                    "overdue and abandoned lists are missing."]
    else:
        overdue = by_kind.get("overdue") or []
        if overdue:
            out += ["", "*Over review SLA*"]
            teams: dict[str, list[dict]] = {}
            for c in overdue:
                teams.setdefault(c["role"], []).append(c)
            for role, items in sorted(teams.items(), key=lambda kv: -max(i["waited"] for i in kv[1])):
                out.append(_team_line(role, items, policy, spill))

        abandoned = by_kind.get("abandoned") or []
        if abandoned:
            out += ["", f"*Abandoned* (author idle >{policy.get('warn_days')}d)"]
            for c in sorted(abandoned, key=lambda c: (c.get("closes_in_days") or 0, c["number"])):
                out.append(f"• {link(c['url'], '#%d ' % c['number'] + short(c['title'], 32))} — {esc(c['facts'])}")

    kok = by_kind.get("keep-or-kill") or []
    if kok:
        full = [pr_line(c["url"], c["number"], c["title"], f"open {fmt_age(c['age_days'])}") for c in kok]
        out += ["", "*Keep or close?* (never reviewed): "
                + inline([f"{num(c['url'], c['number'])} {fmt_age(c['age_days'])}" for c in kok],
                         INLINE_MAX, spill, "*Keep or close?* (never reviewed)", full)]
    untriaged = by_kind.get("untriaged-issue") or []
    if untriaged:
        full = [pr_line(c["url"], c["number"], c["title"]) for c in untriaged]
        out += ["", "*Untriaged issues*: " + inline([num(c["url"], c["number"]) for c in untriaged],
                                                     INLINE_MAX, spill, "*Untriaged issues*", full)]
    return out


def _summary(d: dict, view: dict, shown: set[str], spill: Spill) -> list[str]:
    out = [""]

    ro = d.get("review_outcomes") or {}
    if not ro.get("available"):
        out.append(":warning: *Review loop*: outcome telemetry unavailable this week")
    elif not ro.get("prs_scraped"):
        out.append("*Review loop*: no reviewed PRs closed this week")
    else:
        h = (ro.get("outcomes") or {}).get("human") or {}
        ignored = h.get("ignored_outstanding", 0) + h.get("ignored_low_confidence", 0)
        gap = ro.get("prs_no_review_data") or 0
        with_data = max(ro["prs_scraped"] - gap, 0)
        line = (f"*Review loop* (findings on {with_data} closed PRs): {h.get('fixed', 0)} fixed"
                f" · {ignored} ignored at merge")
        if ro["prs_scraped"] and gap / ro["prs_scraped"] > TELEMETRY_GAP:
            line += f" · :warning: {gap} of {ro['prs_scraped']} had no review data"
        merged_over = [m for m in ro.get("merged_with_outstanding") or [] if f"pr:{m['pr']}" not in shown]
        if merged_over:
            full = [pr_line(m.get("url") or pr_url(m["pr"]), m["pr"], m.get("title") or "",
                            f"{len(m.get('findings') or [])} finding(s) unanswered at merge") for m in merged_over]
            line += " · also merged over findings: " + inline(
                [num(m.get("url") or pr_url(m["pr"]), m["pr"]) for m in merged_over],
                INLINE_MAX, spill, "*Merged over findings*", full)
        out.append(line)

    sla = view["sla"]
    ops = d.get("v3_ops") or {}
    if sla.get("enabled") == "on":
        if ops.get("available"):
            out.append(f"*SLA sweep, last 7d*: {ops.get('escalations_total', 0)} escalations · "
                       f"{ops.get('warns', 0)} warned · {ops.get('closes', 0)} closed · "
                       f"{ops.get('waives', 0)} waived")
        else:
            out.append(":warning: *SLA sweep* is on but its run records were unreadable this week")
    elif ops.get("available") and (ops.get("escalations_total") or ops.get("warns") or ops.get("closes")):
        out.append(f"*SLA sweep, last 7d* (manual runs): {ops.get('escalations_total', 0)} escalations · "
                   f"{ops.get('warns', 0)} warned · {ops.get('closes', 0)} closed")

    wf = d.get("workflow_failures") or {}
    failing = [f for f in wf.get("failing") or [] if f"workflow:{f['workflow']}" not in shown]
    broken = [f for f in failing if f.get("streak", 0) >= BROKEN_STREAK]
    flaky = [f for f in failing if f.get("streak", 0) < BROKEN_STREAK]
    if failing:
        parts = []
        if broken:
            full = [f"• {link(f['last_failure_url'] or REPO_URL, f['workflow'])} — failed its last "
                    f"{f['streak']} runs ({f['failures']}/{f['runs']} this week)" for f in broken]
            parts.append(inline([f"{link(f['last_failure_url'] or REPO_URL, f['workflow'])} {f['failures']}/{f['runs']}"
                                 for f in broken], 3, spill, "*Broken workflows*", full))
        if flaky:
            failed = sum(f["failures"] for f in flaky)
            text = f"{len(flaky)} flaky ({failed} of {wf.get('total_runs')} runs"
            noisiest = max(flaky, key=lambda f: f["failures"])
            if len(flaky) > 1 and noisiest["failures"] * 2 > failed:
                text += (f", {noisiest['failures']} in "
                         f"{link(noisiest['last_failure_url'] or REPO_URL, noisiest['workflow'])}")
            parts.append(text + ")")
        out.append("*Failed runs* (scheduled + master): " + " · ".join(parts))
    elif wf.get("total_runs"):
        out.append(f"*Failed runs*: none in {wf['total_runs']} scheduled + master runs")
    else:
        out.append(":warning: *Failed runs*: run history unavailable")

    if sla.get("available") and sla.get("ledger") is False:
        out.append(":warning: *Review ledger unreadable*: the sweep's per-PR state is missing, so "
                   "a PR it already warned may close sooner than shown")

    switches = d.get("switches") or []
    unknown = [s for s in switches if s["state"] == "unknown"]
    known = [s for s in switches if s["state"] != "unknown"]
    bits = []
    off = [s["label"] for s in known if s["state"] == "off"]
    report = [s["label"] for s in known if s["state"] == "report"]
    if off:
        bits.append("off: " + ", ".join(off))
    if report:
        bits.append("report-only: " + ", ".join(report))
    if unknown:
        bits.append("unknown: " + ", ".join(s["label"] for s in unknown))
    out.append("*Switches*: " + ("; ".join(bits) if bits else "all lanes on"))

    o = view["other_open"]
    # "Within SLA" is the sweep's verdict; without verdicts it's unknown.
    in_progress = "in progress within SLA" if view["sla"].get("available") else "other open"
    rest = [(o["in_progress"], in_progress), (o["waiting_on_author"], "waiting on author"),
            (o["drafts"], "drafts"), (o["bots"], "bot PRs")]
    rest = [f"{n} {what}" for n, what in rest if n]
    if rest:
        out.append("_Not listed: " + " · ".join(rest) + "_")
    return out


def render_parts(d: dict, ranking: dict | None = None) -> tuple[str, str]:
    """(message, thread). The thread holds the full version of every list
    the message shortened; it's "" when nothing was cut, and the poster
    then skips the reply."""
    view = build_view(d)
    top, source = resolve_ranking(view["candidates"], ranking)
    shown = {t["ref"] for t in top}
    spill = Spill()
    lines = (_header(d) + [""] + _top(view, top, spill) + [""] + _queues(view, spill)
             + _sections(view, shown, spill) + _summary(d, view, shown, spill))
    if source == "fallback" and ranking is not None and top:
        lines.append("_Top list in fixed priority order (model ranking unavailable)._")
    message = "\n".join(lines).strip() + "\n"
    if not spill.sections:
        return message, ""
    thread = ["Full lists for everything the digest above shortened:"]
    for heading, items in spill.sections:
        thread += ["", heading, *items]
    return message, "\n".join(thread) + "\n"


def render(d: dict, ranking: dict | None = None) -> str:
    return render_parts(d, ranking)[0]


def candidates_for_model(d: dict) -> list[dict]:
    """What rank.py sends the model: no URLs, no sort keys."""
    keep = ("ref", "kind", "title", "facts")
    return [{k: c[k] for k in keep} for c in build_view(d)["candidates"]]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("mode", choices=["candidates", "render"])
    ap.add_argument("digest")
    ap.add_argument("--ranking", help="rank.py output; omit for the fixed priority order")
    ap.add_argument("--thread-out", help="write the thread-reply text here (empty file when nothing was cut)")
    args = ap.parse_args()
    with open(args.digest, encoding="utf-8") as f:
        d = json.load(f)
    if args.mode == "candidates":
        json.dump(candidates_for_model(d), sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0
    ranking = None
    if args.ranking:
        try:
            with open(args.ranking, encoding="utf-8") as f:
                ranking = json.load(f)
        except (OSError, json.JSONDecodeError) as exc:
            sys.stderr.write(f"warning: unreadable ranking ({exc}); using the fallback order\n")
            ranking = {}
    message, thread = render_parts(d, ranking)
    sys.stdout.write(message)
    if args.thread_out:
        with open(args.thread_out, "w", encoding="utf-8") as f:
            f.write(thread)
    return 0


if __name__ == "__main__":
    sys.exit(main())
