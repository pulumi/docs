#!/usr/bin/env python3
"""Render the weekly #docs-ops digest from digest.py's JSON.

Everything structured is rendered here, deterministically: the SLA sweep's
verdicts grouped by team, the abandoned-PR list, the one-line blog/marketing
backlog, review-loop outcomes, failing workflows, and the lane switches. The
only model-written part is the order (and a short "why") of the top "Needs a
human" list, which rank.py produces from `candidates` below; with no ranking
(model unavailable, or no --ranking) the renderer falls back to a fixed
priority order, so the digest never depends on the model.

Each PR appears at most once: whatever the top list shows is removed from the
grouped sections under it.

Usage:
  render.py candidates <digest.json>                 -> candidates JSON (rank.py input)
  render.py render <digest.json> [--ranking r.json]  -> Slack mrkdwn message
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime

REPO_URL = "https://github.com/pulumi/docs"
# Blog and marketing PRs are the bulk of the open queue and have their own
# owners, so they collapse to one summary line instead of per-PR entries. A
# PR the SLA sweep has verdicts for is classified by its overdue roles (a
# blog post also overdue for docs-guild review stays visible under
# docs-guild); anything else by its domain label.
BLOG_LABELS = {"domain:blog", "domain:website"}
BLOG_ROLES = {"blog", "marketing"}
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
    "merge-now": 4,
    "keep-or-kill": 5,
    "untriaged-issue": 6,
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


def inline(items: list[str], limit: int = INLINE_MAX) -> str:
    shown = items[:limit]
    extra = len(items) - len(shown)
    return " · ".join(shown) + (f" · +{extra} more" if extra > 0 else "")


def owner(policy: dict, role: str) -> str:
    who = (policy.get("escalate_to") or {}).get(role) or ""
    return "" if not who or who.startswith("TODO") else f" → {who}"


# ---- view model ---------------------------------------------------------------


def _labelled_blog(pr: dict) -> bool:
    return bool(BLOG_LABELS & set(pr.get("labels") or []))


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
    sweep_on = sla.get("enabled") == "on"

    def in_blog_lane(n: int) -> bool:
        v = verdicts.get(n)
        if v and v["kind"] == "reviewer" and v.get("overdue"):
            return all(r["role"] in BLOG_ROLES for r in v["overdue"])
        if v and v["kind"] == "reviewer" and v.get("roles"):
            return all(r["role"] in BLOG_ROLES for r in v["roles"])
        return _labelled_blog(humans[n])

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

    blog_overdue = []
    waiting_on_author = 0
    for n, v in sorted(verdicts.items()):
        pr = humans.get(n)
        if pr is None:
            continue
        if v["kind"] == "reviewer" and v.get("overdue"):
            if in_blog_lane(n):
                blog_overdue.append((n, _worst_role(v["overdue"])))
                continue
            listed_roles = [r for r in v["overdue"] if r["role"] not in BLOG_ROLES]
            worst = _worst_role(listed_roles)
            others = [r["role"] + owner(policy, r["role"]) for r in v["overdue"] if r is not worst]
            facts = (f"{worst['role']} review {worst['waited']}bd on a {worst['sla']}bd SLA"
                     f"{owner(policy, worst['role'])}")
            if others:
                facts += f"; also overdue: {', '.join(others)}"
            add("overdue", f"pr:{n}", n, pr["title"], pr_url(n), facts,
                role=worst["role"], waited=worst["waited"], sla=worst["sla"], red=pr.get("checks") == "red",
                sort_key=-(worst["waited"] - worst["sla"]))
        elif v["kind"] == "author":
            # Abandoned PRs are listed even when they're blog posts: a close
            # is consequential and lands on the author, not the review queue.
            if v.get("abandoned"):
                findings = v.get("undecided_count")
                what = f"{findings} findings open" if findings else "changes requested"
                fate = (f"closes in {v.get('closes_in_days')}d" if sweep_on
                        else "the sweep is off, so close or rescue it by hand")
                add("abandoned", f"pr:{n}", n, pr["title"], pr_url(n),
                    f"author idle {round(v['idle_days'])}d, {what}; {fate}",
                    idle_days=v["idle_days"], closes_in_days=v.get("closes_in_days"),
                    sort_key=v.get("closes_in_days") or 0)
            elif not in_blog_lane(n):
                waiting_on_author += 1

    for n, pr in sorted(humans.items()):
        if pr.get("isDraft") or n in verdicts or in_blog_lane(n):
            continue
        labels = set(pr.get("labels") or [])
        if "review:no-blockers" in labels and pr.get("checks") == "green" and "do-not-merge" not in labels:
            add("merge-now", f"pr:{n}", n, pr["title"], pr_url(n),
                "green, no blockers, no required reviewer: merge it",
                sort_key=-(pr.get("age_days") or 0))
        elif (pr.get("age_days") or 0) > KEEP_OR_KILL_DAYS and not (labels & {"review:no-blockers",
                                                                             "review:outstanding-issues"}):
            add("keep-or-kill", f"pr:{n}", n, pr["title"], pr_url(n),
                f"open {pr['age_days']}d, never reviewed: keep or close",
                age_days=pr["age_days"], sort_key=-(pr.get("age_days") or 0))

    issues = d.get("issues") or {}
    for i in issues.get("new_this_week") or []:
        if i.get("needs_triage"):
            add("untriaged-issue", f"issue:{i['number']}", i["number"], i["title"], issue_url(i["number"]),
                "new issue, not triaged", sort_key=-(i.get("age_days") or 0))

    listed = {c["number"] for c in candidates if c["ref"].startswith("pr:")}
    blog_open = [n for n, p in humans.items() if not p.get("isDraft") and in_blog_lane(n)]
    blog_oldest = max(blog_overdue, key=lambda t: t[1]["waited"], default=None)
    return {
        "candidates": candidates,
        "blog": {"open": len(blog_open), "overdue": len(blog_overdue),
                 "oldest": ({"number": blog_oldest[0], "waited": blog_oldest[1]["waited"]}
                            if blog_oldest else None),
                 "oldest_age": max((humans[n].get("age_days") or 0 for n in blog_open), default=None)},
        "other_open": {
            "drafts": sum(1 for n, p in humans.items() if p.get("isDraft") and not in_blog_lane(n)),
            "waiting_on_author": waiting_on_author,
            "bots": sum(1 for p in prs.values() if p.get("is_bot")),
            "in_progress": sum(1 for n, p in humans.items()
                               if not p.get("isDraft") and not in_blog_lane(n) and n not in listed
                               and verdicts.get(n, {}).get("kind") != "author"),
        },
        "policy": policy,
        "sla": sla,
    }


def fallback_ranking(candidates: list[dict]) -> list[dict]:
    ordered = sorted(candidates, key=lambda c: (KIND_PRIORITY[c["kind"]], c.get("sort_key", 0), c["ref"]))
    return [{"ref": c["ref"], "why": c["facts"]} for c in ordered[:TOP_N]]


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
    lines = [f":clipboard: *Docs weekly* · {date}".rstrip(" ·"), head + " vs last week"]

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


def _top(view: dict, top: list[dict]) -> list[str]:
    by_ref = {c["ref"]: c for c in view["candidates"]}
    if not top:
        return ["*Needs a human*", "Nothing this week."]
    out = ["*Needs a human*"]
    for i, t in enumerate(top, 1):
        c = by_ref[t["ref"]]
        label = short(c["title"]) if c["number"] is None else "#%d " % c["number"] + short(c["title"])
        out.append(f"{i}. {link(c['url'], label)} — {esc(t['why'])}")
    return out


def _team_line(role: str, items: list[dict], policy: dict) -> str:
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

    return head + inline([item(c) for c in items])


def _sections(view: dict, shown: set[str]) -> list[str]:
    rest = [c for c in view["candidates"] if c["ref"] not in shown]
    by_kind: dict[str, list[dict]] = {}
    for c in rest:
        by_kind.setdefault(c["kind"], []).append(c)
    out: list[str] = []
    policy = view["policy"]

    sla = view["sla"]
    if not sla.get("available"):
        out += ["", ":warning: SLA verdicts unavailable this week (the sweep dry-run failed); "
                    "overdue and abandoned lists are missing."]
    else:
        overdue = by_kind.get("overdue") or []
        if overdue:
            note = "" if sla.get("enabled") == "on" else " (the sweep is off: nobody was pinged)"
            out += ["", f"*Over review SLA*{note}"]
            teams: dict[str, list[dict]] = {}
            for c in overdue:
                teams.setdefault(c["role"], []).append(c)
            for role, items in sorted(teams.items(), key=lambda kv: -max(i["waited"] for i in kv[1])):
                out.append(_team_line(role, items, policy))

        abandoned = by_kind.get("abandoned") or []
        if abandoned:
            out += ["", f"*Abandoned* (author idle >{policy.get('warn_days')}d)"]
            for c in sorted(abandoned, key=lambda c: (c.get("closes_in_days") or 0, c["number"])):
                out.append(f"• {link(c['url'], '#%d ' % c['number'] + short(c['title'], 32))} — {esc(c['facts'])}")

    merge_now = by_kind.get("merge-now") or []
    if merge_now:
        out += ["", "*Ready to merge* (no reviewer required): "
                + inline([num(c["url"], c["number"]) for c in merge_now])]
    kok = by_kind.get("keep-or-kill") or []
    if kok:
        out += ["", "*Keep or close?* (never reviewed): "
                + inline([f"{num(c['url'], c['number'])} {fmt_age(c['age_days'])}" for c in kok])]
    untriaged = by_kind.get("untriaged-issue") or []
    if untriaged:
        out += ["", "*Untriaged issues*: " + inline([num(c["url"], c["number"]) for c in untriaged])]
    return out


def _summary(d: dict, view: dict, shown: set[str]) -> list[str]:
    out = [""]
    b = view["blog"]
    blog = f"*Blog/marketing*{owner(view['policy'], 'blog')}: {b['open']} open"
    if view["sla"].get("available"):
        blog += f" · {b['overdue']} over SLA"
        if b["oldest"]:
            o = b["oldest"]
            blog += f" · longest wait {num(pr_url(o['number']), o['number'])} {o['waited']}bd"
    elif b["oldest_age"] is not None:
        blog += f" · oldest {fmt_age(b['oldest_age'])}"
    out.append(blog)

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
            line += " · also merged over findings: " + inline(
                [num(m.get("url") or pr_url(m["pr"]), m["pr"]) for m in merged_over])
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
            parts.append(inline([f"{link(f['last_failure_url'] or REPO_URL, f['workflow'])} {f['failures']}/{f['runs']}"
                                 for f in broken], 3))
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
    rest = [(o["in_progress"], "in progress within SLA"), (o["waiting_on_author"], "waiting on author"),
            (o["drafts"], "drafts"), (o["bots"], "bot PRs")]
    rest = [f"{n} {what}" for n, what in rest if n]
    if rest:
        out.append("_Not listed: " + " · ".join(rest) + "_")
    return out


def render(d: dict, ranking: dict | None = None) -> str:
    view = build_view(d)
    top, source = resolve_ranking(view["candidates"], ranking)
    shown = {t["ref"] for t in top}
    lines = _header(d) + [""] + _top(view, top) + _sections(view, shown) + _summary(d, view, shown)
    if source == "fallback" and ranking is not None:
        lines.append("_Top list in fixed priority order (model ranking unavailable)._")
    return "\n".join(lines).strip() + "\n"


def candidates_for_model(d: dict) -> list[dict]:
    """What rank.py sends the model: no URLs, no sort keys."""
    keep = ("ref", "kind", "title", "facts")
    return [{k: c[k] for k in keep} for c in build_view(d)["candidates"]]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("mode", choices=["candidates", "render"])
    ap.add_argument("digest")
    ap.add_argument("--ranking", help="rank.py output; omit for the fixed priority order")
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
    sys.stdout.write(render(d, ranking))
    return 0


if __name__ == "__main__":
    sys.exit(main())
