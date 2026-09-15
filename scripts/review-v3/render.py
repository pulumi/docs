#!/usr/bin/env python3
"""Render queue.json as the /pr-review board, one PR's detail view, or a
terminal table — three views of the same rows.

    render.py --in .pr-review-queue.json --board .pr-review-board.html
    render.py --in .pr-review-queue.json --detail 21598 --out .pr-review-board.html
    render.py --in .pr-review-queue.json --terminal [--pr 21598]

The board groups rows owner → domain, pins collision clusters at the top,
carries filter chips (owner / domain / verdict / author / since), and lets
checkboxes and action buttons compose one `/pr-review --act …` command at
the bottom. The page never calls GitHub: everything it shows is inlined
from queue.json (a `<script type="application/json">` block, the
render-evidence-html.py pattern), and the only thing it produces is a
command for the person to run.

Every value that reaches the page goes through `esc()` exactly once,
server-side; the vanilla JS only toggles `hidden` and concatenates
`data-cmd` attributes it never parses. Theme-aware through CSS custom
properties under both `prefers-color-scheme` and `data-theme`, the token
set of the hand-built triage board this queue replaced.

Deterministic, no model calls.
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_HERE))
import sentinel  # noqa: E402

_compose = sentinel._compose
SHOTS_DIR = _REPO_ROOT / ".pr-review-shots"
VERDICT_ORDER = ("stamp", "judge", "route", "blocked")
VERDICT_CLASS = {"stamp": "go", "judge": "hold", "route": "route", "blocked": "stop"}
BUCKET_LABEL = {
    "outstanding": "🚨 Outstanding", "author-answer": "❓ Author answer", "reviewer-check": "⚠️ Reviewer check",
    "low": "⚠️ Low-confidence", "style": "✏️ Style", "pre-existing": "💡 Pre-existing", "preexisting": "💡 Pre-existing",
}
HIDDEN_REASON_PREFIXES = ("owner:", "label:")  # rendered elsewhere on the row


def esc(v) -> str:
    """html.escape every value that reaches the page, in exactly one place."""
    if v is None:
        return ""
    return html.escape(str(v), quote=True)


# ---- pieces --------------------------------------------------------------------


def pr_url(queue: dict, n: int) -> str:
    return f"https://github.com/{queue.get('repo') or 'pulumi/docs'}/pull/{n}"


def files_url(queue: dict, n: int) -> str:
    return pr_url(queue, n) + "/files"


def deep_link(queue: dict, pr: dict, item: dict) -> str | None:
    file = item.get("file")
    if not file:
        return None
    return files_url(queue, pr["number"]) + _compose.diff_anchor(file, item.get("anchor") or item.get("ref") or "")


def chips(reasons: list[str]) -> str:
    out = []
    for r in reasons:
        if r.startswith(HIDDEN_REASON_PREFIXES):
            continue
        code = r.split(":", 1)[0]
        out.append(f'<span class="chip r-{esc(code)}" title="{esc(r)}">{esc(r if len(r) <= 48 else r[:45] + "…")}</span>')
    return "".join(out)


def owner_label(pr: dict) -> str:
    if pr.get("is_mine", True):
        return "mine"
    for d in pr.get("domains") or []:
        o = (pr.get("owners") or {}).get(d) or {}
        if o.get("role"):
            return o["role"]
    return "unowned"


def verdict_chip(pr: dict) -> str:
    v = pr.get("verdict") or "judge"
    extra = ""
    if v == "route":
        act = next((a for a in pr.get("actions") or [] if a["id"] == "route"), None)
        if act:
            extra = " → " + act["cmd"].split(":", 1)[1]
    if pr.get("recommended") and pr["recommended"] != v:
        extra += f' <span class="v v-dim">model: {esc(pr["recommended"])}</span>'
    return f'<span class="v v-{esc(v)}">{esc(v)}{esc(extra) if not extra.startswith(" <") else extra}</span>'


def meta_line(pr: dict) -> str:
    checks = (pr.get("checks") or {}).get("state") or "?"
    ci = {"green": "CI ✓", "red": "CI ✗", "pending": "CI …"}.get(checks, f"CI {checks}")
    review = pr.get("review") or {}
    reviewed = (review.get("reviewed_sha") or "")[:7]
    head = (pr.get("head") or {}).get("sha", "")[:7]
    fresh = f"reviewed@{reviewed} = head" if reviewed and head.startswith(reviewed[: len(head)]) or (reviewed and reviewed.startswith(head)) else (f"reviewed@{reviewed} ≠ head {head}" if reviewed else f"head {head}")
    parts = [
        ", ".join(pr.get("domains") or []) or "?",
        f"+{pr.get('additions', 0)} −{pr.get('deletions', 0)} · {len(pr.get('files') or [])} file{'s' if len(pr.get('files') or []) != 1 else ''}",
        ci, f"mergeable: {esc(pr.get('mergeable_state'))}", fresh,
        f"risk:{pr.get('risk_tier')}",
        f"@{(pr.get('author') or {}).get('login', '')}",
    ]
    return "".join(f"<span>{esc(p)}</span>" for p in parts)


def diffq(j: dict) -> str:
    minus = j.get("quote_minus") or []
    plus = j.get("quote_plus") or []
    if isinstance(minus, str):
        minus = [minus]
    if isinstance(plus, str):
        plus = [plus]
    if not minus and not plus:
        return ""
    lines = [f'<span class="del">- {esc(l)}</span>' for l in minus] + [f'<span class="add">+ {esc(l)}</span>' for l in plus]
    return '<div class="diffq">' + "\n".join(lines) + "</div>"


def disposition_label(d: str | None) -> str:
    """`fixed` is not a call to make: the diff already did it. The other four
    are the approver's decision, so they read as a recommendation."""
    if d == "fixed":
        return "<b>already fixed in the diff</b>"
    return f"recommend <b>{esc(d or '?')}</b>"


def judgment_boxes(queue: dict, pr: dict) -> str:
    js = pr.get("judgments") or []
    if not js:
        return pending_judgment(queue, pr)
    out = []
    for j in js:
        link = j.get("deep_link")
        where = f'<a href="{esc(link)}">{esc(j.get("file") or "")} L{esc(j.get("line") or "?")} ↗</a>' if link else '<a href="' + esc(pr_url(queue, pr["number"])) + '">open the PR ↗</a>'
        out.append(
            '<div class="jbox">'
            f'<div class="q">{esc(j.get("finding_id") or "")} {esc(j.get("decision") or j.get("question") or "")}</div>'
            + diffq(j)
            + f'<div class="jmeta">{where} · {disposition_label(j.get("disposition"))}'
            + (f' — {esc(j["note"])}' if j.get("note") else "")
            + "</div></div>"
        )
    return "".join(out)


def pending_judgment(queue: dict, pr: dict) -> str:
    """Before the judge step runs: the open findings and what each row asks."""
    review = pr.get("review") or {}
    items = [i for i in review.get("items") or [] if not i.get("disposition") and i.get("bucket") not in ("style", "pre-existing", "preexisting")]
    if pr.get("triage_prose"):
        bullets = [l.strip("- ").strip() for l in pr["triage_prose"].splitlines() if l.startswith("- [")]
        items += [{"id": f"triage:{i + 1}", "summary": b, "bucket": "reviewer-check"} for i, b in enumerate(bullets)]
    if not items and pr.get("verdict") != "judge":
        return ""
    rows = []
    for i in items[:8]:
        link = deep_link(queue, pr, i)
        loc = f'<a href="{esc(link)}">{esc(i.get("file") or "")} {esc(i.get("anchor") or "")}</a>' if link else esc(i.get("anchor") or "")
        rows.append(f'<li><b>{esc(i.get("id"))}</b> <span class="v v-dim">{esc(BUCKET_LABEL.get(i.get("bucket"), i.get("bucket")))}</span> {esc(i.get("summary") or i.get("text") or "")} {loc}</li>')
    if len(items) > 8:
        rows.append(f"<li>… {len(items) - 8} more on the PR</li>")
    why = [r for r in pr.get("reasons") or [] if r.split(":")[0] in ("warnings", "outstanding", "self-accepted", "size", "blog", "directional", "duplicate", "collision", "desc", "brief", "scrutiny", "shape", "mergeable", "checks", "review", "merging-over")]
    return ('<div class="jbox pending"><div class="q">Needs a call' + (": " + esc(", ".join(why[:4])) if why else "") + "</div>"
            + ("<ul>" + "".join(rows) + "</ul>" if rows else "")
            + "</div>")


def action_bar(pr: dict, queue: dict) -> str:
    btns = []
    for a in pr.get("actions") or []:
        primary = " p" if a is (pr.get("actions") or [None])[0] else ""
        btns.append(f'<button class="btn{primary}" data-cmd="{esc(a["cmd"])}" data-pr="{pr["number"]}">{esc(a["label"])}</button>')
    btns.append(f'<a class="btn" href="{esc(pr_url(queue, pr["number"]))}">open PR</a>')
    return '<div class="acts">' + "".join(btns) + "</div>"


def row_html(queue: dict, pr: dict, *, expanded: bool = False) -> str:
    n = pr["number"]
    v = pr.get("verdict") or "judge"
    checked = " checked" if v == "stamp" else ""
    disabled = "" if any(a["id"] == "stamp" for a in pr.get("actions") or []) else " disabled"
    stamp_cmd = next((a["cmd"] for a in pr.get("actions") or [] if a["id"] == "stamp"), f"--stamp {n}")
    author = (pr.get("author") or {}).get("norm") or ""
    created = (pr.get("created_at") or "")[:10]
    body = [
        f'<div class="mrow {VERDICT_CLASS.get(v, "hold")}" data-pr="{n}" data-verdict="{esc(v)}" data-owner="{esc(owner_label(pr))}" '
        f'data-domains="{esc(" ".join(pr.get("domains") or []))}" data-author="{esc(author)}" data-created="{esc(created)}" '
        f'data-mine="{"1" if pr.get("is_mine", True) else "0"}">',
        f'<input type="checkbox" class="cb" data-cmd="{esc(stamp_cmd)}" data-pr="{n}"{checked}{disabled} aria-label="select #{n}">',
        f'<a class="pr" href="{esc(pr_url(queue, n))}">#{n}</a>',
        "<div>",
        f'<h4>{esc(pr.get("title"))} {verdict_chip(pr)}</h4>',
        f'<div class="meta">{meta_line(pr)}</div>',
        f'<div class="chips">{chips(pr.get("reasons") or [])}</div>',
        f'<p class="sum">{esc(pr.get("summary") or "")}</p>' if pr.get("summary") else "",
    ]
    if v in ("judge",) or pr.get("judgments") or expanded:
        body.append(judgment_boxes(queue, pr))
    if v == "blocked":
        body.append(f'<div class="jbox stop"><div class="q">Blocked: {esc(", ".join(pr.get("blockers") or []))}</div></div>')
    body.append(action_bar(pr, queue))
    if expanded:
        body.append(detail_sections(queue, pr))
    body.append("</div></div>")
    return "".join(body)


def detail_sections(queue: dict, pr: dict) -> str:
    n = pr["number"]
    review = pr.get("review") or {}
    parts = ['<div class="detail">']
    # findings
    items = review.get("items") or []
    if items:
        rows = []
        for i in items:
            link = deep_link(queue, pr, i)
            where = f'<a href="{esc(link)}">{esc(i.get("file") or "")} {esc(i.get("anchor") or "")}</a>' if link else esc(i.get("anchor") or "")
            disp = i.get("disposition") or ("open" if i.get("blocking") or i.get("bucket") in ("low", "reviewer-check") else "advisory")
            rows.append(f"<tr><td>{esc(i.get('id'))}</td><td>{esc(BUCKET_LABEL.get(i.get('bucket'), i.get('bucket')))}</td>"
                        f"<td>{where}</td><td>{esc(i.get('summary') or '')}</td><td>{esc(disp)}</td></tr>")
        parts.append(f'<h5>Findings ({len(items)}) · review {esc(review.get("status"))} · {esc(review.get("surface"))}</h5>'
                     "<table><tr><th>id</th><th>bucket</th><th>where</th><th>finding</th><th>state</th></tr>" + "".join(rows) + "</table>")
    elif pr.get("triage_prose"):
        parts.append("<h5>Triage prose check (no full review ran)</h5><pre>" + esc(pr["triage_prose"]) + "</pre>")
    else:
        parts.append(f'<h5>No review findings · review {esc(review.get("status"))}</h5>')
    if review.get("stances"):
        parts.append('<p class="note">The brief lists editorial stances (advisory unless --strict-stances).</p>')
    # cross-PR
    cross = [r for r in pr.get("reasons") or [] if r.split(":")[0] in ("collision", "directional", "duplicate")]
    if cross:
        parts.append("<h5>Cross-PR</h5><ul>" + "".join(f"<li>{esc(c)}</li>" for c in cross) + "</ul>")
    # preview
    prev = pr.get("preview") or {}
    if prev.get("pages"):
        li = []
        for pg in prev["pages"]:
            href = pg.get("preview_url") or pg.get("url")
            li.append(f'<li><a href="{esc(href)}">{esc(pg.get("title"))}</a> <code>{esc(pg.get("url"))}</code>' + shot_img(n, pg) + "</li>")
        parts.append(f'<h5>Preview · {esc(prev.get("status"))}</h5><ul class="pages">' + "".join(li) + "</ul>")
    # files
    parts.append("<h5>Files</h5><ul class=\"files\">" + "".join(
        f'<li><a href="{esc(files_url(queue, n) + _compose.diff_anchor(f["path"], ""))}"><code>{esc(f["path"])}</code></a> '
        f'<span class="v v-dim">{esc(f.get("status"))}</span> +{f.get("additions", 0)} −{f.get("deletions", 0)}</li>'
        for f in pr.get("files") or []) + "</ul>")
    # fix draft / description
    if pr.get("fix_draft"):
        fd = pr["fix_draft"]
        parts.append(f'<h5>Drafted fix ({esc(fd.get("kind"))})</h5><pre>{esc(fd.get("body") or fd.get("patch") or "")}</pre>')
    if pr.get("body"):
        parts.append("<details><summary>PR description</summary><pre>" + esc(pr["body"]) + "</pre></details>")
    parts.append("</div>")
    return "".join(parts)


def shot_img(n: int, page: dict, max_bytes: int = 1_500_000) -> str:
    slug = (page.get("url") or "").strip("/").replace("/", "_") or "index"
    f = SHOTS_DIR / str(n) / f"{slug}.png"
    if not f.is_file():
        return ""
    data = f.read_bytes()
    if len(data) > max_bytes:
        return f' <span class="v v-dim">screenshot at {esc(f)}</span>'
    return f'<br><img class="shot" alt="preview of {esc(page.get("url"))}" src="data:image/png;base64,{base64.b64encode(data).decode()}">'


def clusters_html(queue: dict) -> str:
    cl = queue.get("clusters") or []
    dr = queue.get("directional") or []
    du = queue.get("duplicates") or []
    if not (cl or dr or du):
        return ""
    cards = []
    for c in cl:
        by_path: dict[str, set] = {}
        for p in c["pairs"]:
            for path in p["paths"]:
                by_path.setdefault(path, set()).update((p["a"], p["b"]))
        top = sorted(by_path.items(), key=lambda kv: -len(kv[1]))[:6]
        paths = "".join(f'<li><code>{esc(path)}</code> — {" ".join(f"#{x}" for x in sorted(prs))}</li>' for path, prs in top)
        more = f"<li>… {len(by_path) - 6} more paths</li>" if len(by_path) > 6 else ""
        order = " → ".join(f'<a href="{esc(pr_url(queue, x))}">#{x}</a>' for x in c["merge_order"])
        kind_cls = "no" if c["kind"] == "overlap" else "mid"
        cards.append(
            f'<div class="card {kind_cls}"><h4>{esc(c["id"])} · {len(c["prs"])} PRs · {esc(c["kind"])}</h4>'
            f"<p>Merge order: {order}</p>"
            f"<ul>{paths}{more}</ul></div>"
        )
    by_path: dict[str, tuple[set, set]] = {}
    for d in dr:
        adds, rems = by_path.setdefault(d["path"], (set(), set()))
        adds.add(d["adds_links_pr"])
        rems.add(d["removes_links_pr"])
    for path, (adds, rems) in sorted(by_path.items(), key=lambda kv: -len(kv[1][0]) - len(kv[1][1])):
        link = lambda x: f'<a href="{esc(pr_url(queue, x))}">#{x}</a>'  # noqa: E731
        cards.append(f'<div class="card no"><h4>Directional · <code>{esc(path)}</code></h4>'
                     f'<p>Alias-only URL. Adding links: {", ".join(link(x) for x in sorted(adds))}. Removing links: {", ".join(link(x) for x in sorted(rems))}. '
                     "Merge the removers first, then repoint the adders.</p></div>")
    for d in du:
        cards.append(f'<div class="card mid"><h4>Duplicate? #{d["newer"]} vs #{d["older"]}</h4>'
                     f'<p>Titles {int(d["title_ratio"] * 100)}% alike, opened {esc(d["minutes_apart"])} min apart, sharing {esc(", ".join(d["shared_files"][:3]))}.</p></div>')
    head, rest = cards[:6], cards[6:]
    more = f'<details><summary>{len(rest)} more</summary><div class="two">{"".join(rest)}</div></details>' if rest else ""
    return '<section class="clusters"><h2>Collisions first</h2><div class="two">' + "".join(head) + "</div>" + more + "</section>"


def filter_bar(queue: dict) -> str:
    prs = queue.get("prs") or []
    owners = sorted({owner_label(p) for p in prs})
    domains = sorted({d for p in prs for d in p.get("domains") or []})
    authors = sorted({(p.get("author") or {}).get("norm") or "" for p in prs})
    counts = queue.get("counts") or {}

    def chip(kind, val, label=None, on=True):
        return f'<button class="fchip{" on" if on else ""}" data-filter="{esc(kind)}" data-value="{esc(val)}">{esc(label or val)}</button>'

    parts = ['<div class="mock-bar">']
    parts += [chip("owner", o, f"owner: {o}") for o in owners]
    parts.append('<span class="sep"></span>')
    parts += [chip("domain", d) for d in domains]
    parts.append('<span class="sep"></span>')
    parts += [chip("verdict", v, f"{v} {counts.get(v, 0)}") for v in VERDICT_ORDER]
    parts.append('<span class="sep"></span>')
    parts += [chip("author", a, f"author: {a}") for a in authors]
    parts.append('<span class="sep"></span>')
    parts += [chip("since", s, f"since: {s}", on=False) for s in ("1d", "7d", "30d")]
    parts.append("</div>")
    return "".join(parts)


def group_rows(prs: list[dict]) -> list[tuple[str, str, list[dict]]]:
    groups: dict[tuple[str, str], list[dict]] = {}
    for p in prs:
        key = (owner_label(p), ", ".join(p.get("domains") or []) or "other")
        groups.setdefault(key, []).append(p)
    order = lambda k: (0 if k[0] == "mine" else 1, k[0], k[1])  # noqa: E731
    return [(o, d, sorted(rows, key=lambda p: (VERDICT_ORDER.index(p.get("verdict") or "judge"), -p["number"])))
            for (o, d), rows in sorted(groups.items(), key=lambda kv: order(kv[0]))]


# ---- pages --------------------------------------------------------------------

PAYLOAD_DROP = {"patch", "author_body", "brief_body", "body", "triage_prose", "one_click_suggestions"}


def slim(obj):
    """The inlined copy of the queue minus the bulk (patches, comment
    bodies): what a viewer might copy out, not a second render source."""
    if isinstance(obj, dict):
        return {k: slim(v) for k, v in obj.items() if k not in PAYLOAD_DROP}
    if isinstance(obj, list):
        return [slim(x) for x in obj]
    return obj



def render_board(queue: dict, *, artifact: bool = False) -> str:
    prs = queue.get("prs") or []
    counts = queue.get("counts") or {}
    cfg = queue.get("config") or {}
    sections = []
    for owner, domain, rows in group_rows(prs):
        sections.append(f'<section class="grp"><div class="sec-head"><h2>{esc(owner)}</h2><span class="dlabel">{esc(domain)}</span><span class="count">{len(rows)}</span></div>'
                        + "".join(row_html(queue, p) for p in rows) + "</section>")
    tally = "".join(f'<div class="t-{VERDICT_CLASS[v]}"><b>{counts.get(v, 0)}</b><span>{v}</span></div>' for v in VERDICT_ORDER)
    payload = json.dumps(slim(queue), sort_keys=True).replace("</", "<\\/")
    return (FRAGMENT if artifact else PAGE).format(
        title="PR review queue",
        style=STYLE,
        eyebrow=esc(f"{queue.get('repo')} · queue · {queue.get('analyzed_at') or queue.get('generated_at')} · owner: {cfg.get('owner', 'me')} · me: {', '.join(cfg.get('me') or [])}"),
        h1="PR review queue",
        dek=esc(f"{len(prs)} open PRs sorted into stamp / judge / route / blocked. Stamp rows are pre-checked; every button below only adds to the command at the bottom — the page never talks to GitHub."),
        tally=f'<div class="tally">{tally}</div>',
        filters=filter_bar(queue),
        clusters=clusters_html(queue),
        body="".join(sections) or '<p class="empty">Nothing to adjudicate.</p>',
        cmd=cmd_footer(),
        payload=payload,
        script=SCRIPT,
    )


def render_detail(queue: dict, n: int, *, artifact: bool = False) -> str:
    pr = next((p for p in queue.get("prs") or [] if p["number"] == n), None)
    if pr is None:
        raise SystemExit(f"#{n} is not in the queue (drafts and filtered rows are not collected)")
    payload = json.dumps(slim({**queue, "prs": [pr]}), sort_keys=True).replace("</", "<\\/")
    return (FRAGMENT if artifact else PAGE).format(
        title=f"#{n} · {esc(pr.get('title'))}",
        style=STYLE,
        eyebrow=esc(f"{queue.get('repo')} · #{n} · {queue.get('analyzed_at') or queue.get('generated_at')}"),
        h1=esc(pr.get("title")),
        dek=verdict_chip(pr) + " " + esc(pr.get("summary") or ""),
        tally="",
        filters="",
        clusters="",
        body=row_html(queue, pr, expanded=True),
        cmd=cmd_footer(),
        payload=payload,
        script=SCRIPT,
    )


def cmd_footer() -> str:
    return ('<div class="cmdwrap"><div class="cmd" id="cmd">$ /pr-review --act</div>'
            '<button class="btn" id="copy">copy</button><button class="btn" id="clear">clear</button></div>')


def render_terminal(queue: dict, n: int | None = None, width: int = 110) -> str:
    prs = queue.get("prs") or []
    if n is not None:
        prs = [p for p in prs if p["number"] == n]
    counts = queue.get("counts") or {}
    lines = [f"PR review queue · {queue.get('repo')} · {len(prs)} rows · " + " · ".join(f"{counts.get(v, 0)} {v}" for v in VERDICT_ORDER), ""]
    hdr = f"{'#':>6}  {'verdict':<8} {'owner':<11} {'domain':<14} {'size':>9} {'CI':<4} reasons"
    lines += [hdr, "-" * len(hdr)]
    for owner, domain, rows in group_rows(prs):
        for p in rows:
            reasons = [r for r in p.get("reasons") or [] if not r.startswith(HIDDEN_REASON_PREFIXES)]
            ci = {"green": "✓", "red": "✗", "pending": "…"}.get((p.get("checks") or {}).get("state"), "?")
            size = f"+{p.get('additions', 0)}/−{p.get('deletions', 0)}"
            line = f"{p['number']:>6}  {p.get('verdict'):<8} {owner[:11]:<11} {domain[:14]:<14} {size:>9} {ci:<4} " + " ".join(reasons)
            lines.append(line[:width] + ("…" if len(line) > width else ""))
    cl = queue.get("clusters") or []
    if cl:
        lines += ["", "collisions:"]
        for c in cl:
            lines.append(f"  {c['id']} {c['kind']}: merge " + " → ".join(f"#{x}" for x in c["merge_order"]))
    for d in queue.get("directional") or []:
        lines.append(f"  directional {d['path']}: #{d['adds_links_pr']} adds links, #{d['removes_links_pr']} removes them")
    judge = [p for p in prs if p.get("verdict") == "judge"]
    if judge:
        lines += ["", "judge rows (AskUserQuestion each in --terminal mode):"]
        for p in judge:
            lines.append(f"  #{p['number']} {p.get('title')}")
            for j in p.get("judgments") or []:
                lines.append(f"      {j.get('finding_id') or ''} {j.get('decision') or ''} → {j.get('disposition') or '?'} {j.get('deep_link') or ''}")
            for a in p.get("actions") or []:
                lines.append(f"      [{a['label']}]  {a['cmd']}")
    stamps = [a["cmd"].split()[1] for p in prs for a in p.get("actions") or [] if a["id"] == "stamp" and p.get("verdict") == "stamp"]
    if stamps:
        lines += ["", f"$ /pr-review --act --stamp {','.join(stamps)}"]
    return "\n".join(lines) + "\n"


# ---- template ---------------------------------------------------------------------

STYLE = r"""
:root{--ground:#f7f5fa;--surface:#fff;--surface-2:#f1eef6;--ink:#191622;--ink-2:#4a4358;--ink-3:#736b82;--line:#e3deec;--line-2:#cfc7dd;--accent:#6b3fa0;--accent-soft:#efe8f8;--go:#1c6b45;--go-soft:#e2f2ea;--hold:#94530c;--hold-soft:#fbeedb;--stop:#a32219;--stop-soft:#fbe6e4;--route:#1f5c8a;--route-soft:#e3eef8;--shadow:0 1px 2px rgba(25,22,34,.05),0 8px 24px -16px rgba(25,22,34,.3)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ground:#131119;--surface:#1b1824;--surface-2:#231f2f;--ink:#f0ecf6;--ink-2:#bdb5cc;--ink-3:#8e86a0;--line:#2e2839;--line-2:#443c54;--accent:#c4a2ee;--accent-soft:#2a2138;--go:#7fd6a9;--go-soft:#16281f;--hold:#f0bd76;--hold-soft:#2e2316;--stop:#f5a099;--stop-soft:#301816;--route:#8fc1ee;--route-soft:#172433;--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -16px rgba(0,0,0,.8)}}
:root[data-theme="dark"]{--ground:#131119;--surface:#1b1824;--surface-2:#231f2f;--ink:#f0ecf6;--ink-2:#bdb5cc;--ink-3:#8e86a0;--line:#2e2839;--line-2:#443c54;--accent:#c4a2ee;--accent-soft:#2a2138;--go:#7fd6a9;--go-soft:#16281f;--hold:#f0bd76;--hold-soft:#2e2316;--stop:#f5a099;--stop-soft:#301816;--route:#8fc1ee;--route-soft:#172433;--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -16px rgba(0,0,0,.8)}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:"IBM Plex Sans",ui-sans-serif,system-ui,sans-serif;font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:1120px;margin:0 auto;padding:32px 16px 120px}
h1,h2,h3,h4,h5{font-family:Archivo,"IBM Plex Sans",sans-serif;margin:0;text-wrap:balance}
code,.mono,pre,.cmd,.chip,.v,.pr,.btn,.fchip{font-family:"IBM Plex Mono",ui-monospace,monospace}
code{font-size:.92em;background:var(--surface-2);padding:1px 5px;border-radius:2px}
pre{background:var(--surface-2);border:1px solid var(--line);border-radius:3px;padding:12px 14px;font-size:12.5px;line-height:1.5;overflow-x:auto;white-space:pre-wrap;margin:8px 0}
a{color:var(--accent)}
.mast{border-bottom:2px solid var(--ink);padding-bottom:18px;margin-bottom:22px}
.eyebrow{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);margin-bottom:8px}
h1{font-size:clamp(26px,4.6vw,40px);font-weight:800;letter-spacing:-.022em;line-height:1.05}
.dek{color:var(--ink-2);max-width:72ch;margin:10px 0 0;font-size:15.5px}
.tally{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 6px}
.tally div{flex:1 1 120px;background:var(--surface);border:1px solid var(--line);border-radius:3px;padding:10px 14px;box-shadow:var(--shadow)}
.tally b{display:block;font-family:Archivo,sans-serif;font-size:28px;font-weight:700;line-height:1.1}
.tally span{font-size:12px;color:var(--ink-3)}
.t-go b{color:var(--go)}.t-hold b{color:var(--hold)}.t-stop b{color:var(--stop)}.t-route b{color:var(--route)}
.mock-bar{display:flex;gap:6px;flex-wrap:wrap;align-items:center;padding:12px 0;border-bottom:1px solid var(--line);margin-bottom:8px;position:sticky;top:env(safe-area-inset-top,0px);background:var(--ground);z-index:2}
.sep{width:1px;height:18px;background:var(--line-2);margin:0 4px}
.fchip{font-size:11.5px;border:1px solid var(--line-2);border-radius:99px;padding:2px 10px;color:var(--ink-2);background:var(--surface-2);cursor:pointer}
.fchip.on{background:var(--accent-soft);color:var(--accent);border-color:var(--accent)}
.grp{margin-top:26px}
.sec-head{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin-bottom:4px}
h2{font-size:21px;font-weight:700;letter-spacing:-.015em}
.dlabel{font-family:"IBM Plex Mono",monospace;font-size:12.5px;font-weight:600;background:var(--accent-soft);color:var(--accent);padding:2px 9px;border-radius:3px}
.count{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--ink-3);border:1px solid var(--line-2);border-radius:99px;padding:1px 9px}
.mrow{display:grid;grid-template-columns:22px 74px 1fr;gap:12px;padding:12px 0 12px 10px;border-bottom:1px solid var(--line);border-left:3px solid transparent}
.mrow.go{border-left-color:var(--go)}.mrow.hold{border-left-color:var(--hold)}.mrow.stop{border-left-color:var(--stop)}.mrow.route{border-left-color:var(--route)}
.mrow[hidden]{display:none}
.mrow>div{min-width:0}
.jmeta,.sum,.card p,.jbox li,.detail td{overflow-wrap:anywhere}
.cb{width:16px;height:16px;margin-top:4px;accent-color:var(--go)}
.pr{font-size:12px;font-weight:600;background:var(--surface-2);border:1px solid var(--line-2);border-radius:3px;padding:2px 7px;color:var(--ink);text-decoration:none;white-space:nowrap;align-self:start;justify-self:start}
.mrow h4{font-size:14.5px;font-weight:600;margin:0 0 3px;line-height:1.35}
.meta{font-size:12.5px;color:var(--ink-3);margin-bottom:4px}.meta span{margin-right:10px}
.chips{display:flex;flex-wrap:wrap;gap:4px;margin:2px 0 6px}
.chip{font-size:10.5px;border:1px solid var(--line-2);border-radius:2px;padding:1px 6px;color:var(--ink-2);background:var(--surface-2);white-space:nowrap}
.chip.r-collision,.chip.r-directional,.chip.r-duplicate,.chip.r-self-accepted,.chip.r-checks,.chip.r-mergeable{border-color:var(--stop);color:var(--stop)}
.chip.r-warnings,.chip.r-outstanding,.chip.r-scrutiny,.chip.r-blog,.chip.r-size,.chip.r-shape,.chip.r-review{border-color:var(--hold);color:var(--hold)}
.chip.r-route{border-color:var(--route);color:var(--route)}
.sum{font-size:13.5px;color:var(--ink-2);margin:0 0 4px}
.v{font-size:10.5px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;padding:2px 7px;border-radius:2px;white-space:nowrap;display:inline-block;vertical-align:middle}
.v-stamp{background:var(--go-soft);color:var(--go)}.v-judge{background:var(--hold-soft);color:var(--hold)}.v-route{background:var(--route-soft);color:var(--route)}.v-blocked{background:var(--stop-soft);color:var(--stop)}.v-dim{background:var(--surface-2);color:var(--ink-3);text-transform:none;letter-spacing:0}
.jbox{margin-top:8px;background:var(--hold-soft);border-radius:3px;padding:9px 11px;font-size:13px}
.jbox.stop{background:var(--stop-soft)}.jbox.pending{background:var(--surface-2)}
.jbox .q{font-weight:600;color:var(--ink);margin-bottom:5px}
.jbox ul{margin:0;padding-left:18px}.jbox li{margin:2px 0}
.jmeta{margin-top:5px;color:var(--ink-2)}
.diffq{font-family:"IBM Plex Mono",monospace;font-size:12px;background:var(--surface);border:1px solid var(--line);border-radius:3px;padding:6px 9px;margin:6px 0;overflow-x:auto;white-space:pre}
.diffq .del{color:var(--stop)}.diffq .add{color:var(--go)}
.acts{margin-top:8px;display:flex;gap:6px;flex-wrap:wrap}
.btn{font-size:11.5px;font-weight:600;border:1px solid var(--line-2);border-radius:3px;padding:3px 9px;background:var(--surface);color:var(--ink-2);cursor:pointer;text-decoration:none}
.btn.p{background:var(--accent);color:#fff;border-color:var(--accent)}.btn.sel{outline:2px solid var(--go)}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px;margin:12px 0}
.card{background:var(--surface);border:1px solid var(--line);border-radius:3px;padding:12px 14px}
.card h4{margin:0 0 6px;font-size:14px}.card p{font-size:13.5px;color:var(--ink-2);margin:0 0 6px}.card ul{margin:0;padding-left:18px;font-size:13px;color:var(--ink-2)}
.card.no{border-left:3px solid var(--stop)}.card.mid{border-left:3px solid var(--hold)}
.clusters{margin-top:18px}
.detail{margin-top:14px;border-top:1px dashed var(--line-2);padding-top:10px}
.detail h5{font-size:13px;margin:14px 0 6px;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-3)}
table{width:100%;border-collapse:collapse;font-size:13px}
th{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);text-align:left;padding:6px 8px;border-bottom:1px solid var(--line-2)}
td{padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink-2)}
.pages li,.files li{margin:3px 0;font-size:13.5px}
.shot{max-width:100%;border:1px solid var(--line-2);border-radius:3px;margin-top:6px}
.note{font-size:13px;color:var(--ink-3)}
.cmdwrap{position:fixed;left:0;right:0;bottom:0;background:var(--ground);border-top:1px solid var(--line-2);padding:10px 16px calc(10px + env(safe-area-inset-bottom,0px));display:flex;gap:8px;align-items:center;z-index:3}
.wrap{padding-inline:16px}
.cmd{flex:1;background:var(--ink);color:var(--ground);border-radius:3px;padding:8px 12px;font-size:12.5px;overflow-x:auto;white-space:nowrap}
.empty{color:var(--ink-3)}
@media (max-width:600px){.mrow{grid-template-columns:22px 1fr}.mrow .pr{grid-column:2}.mrow>div:last-child{grid-column:1/-1}}
"""

SCRIPT = r"""
(function(){
  var sel = {};   // key -> cmd (checkbox: 'cb:'+pr, button: 'btn:'+cmd)
  var cmdEl = document.getElementById('cmd');
  function compose(){
    var parts = [];
    Object.keys(sel).sort().forEach(function(k){ if (sel[k]) parts.push(sel[k]); });
    var stamps = [], others = [];
    parts.forEach(function(p){ var m = p.match(/^--stamp (\d+)$/); if (m) stamps.push(m[1]); else others.push(p); });
    var out = '$ /pr-review --act';
    if (stamps.length) out += ' --stamp ' + stamps.join(',');
    if (others.length) out += ' ' + others.join(' ');
    cmdEl.textContent = out;
  }
  document.querySelectorAll('input.cb').forEach(function(cb){
    if (cb.checked) sel['cb:' + cb.dataset.pr] = cb.dataset.cmd;
    cb.addEventListener('change', function(){ sel['cb:' + cb.dataset.pr] = cb.checked ? cb.dataset.cmd : ''; compose(); });
  });
  document.querySelectorAll('button.btn[data-cmd]').forEach(function(b){
    b.addEventListener('click', function(){
      var k = 'btn:' + b.dataset.pr + ':' + b.dataset.cmd;
      if (sel[k]) { delete sel[k]; b.classList.remove('sel'); } else { sel[k] = b.dataset.cmd; b.classList.add('sel'); }
      compose();
    });
  });
  document.getElementById('clear').addEventListener('click', function(){
    sel = {}; document.querySelectorAll('input.cb').forEach(function(cb){ cb.checked = false; });
    document.querySelectorAll('button.btn.sel').forEach(function(b){ b.classList.remove('sel'); }); compose();
  });
  document.getElementById('copy').addEventListener('click', function(){
    var t = cmdEl.textContent.replace(/^\$ /, '');
    if (navigator.clipboard) navigator.clipboard.writeText(t);
  });
  var filters = { owner: {}, domain: {}, verdict: {}, author: {}, since: {} };
  document.querySelectorAll('.fchip').forEach(function(f){
    filters[f.dataset.filter][f.dataset.value] = f.classList.contains('on');
    f.addEventListener('click', function(){ f.classList.toggle('on'); filters[f.dataset.filter][f.dataset.value] = f.classList.contains('on'); apply(); });
  });
  function anyOn(kind){ return Object.keys(filters[kind]).some(function(k){ return filters[kind][k]; }); }
  function sinceCut(){
    var days = null; Object.keys(filters.since).forEach(function(k){ if (filters.since[k]) { var d = parseInt(k, 10); if (days === null || d > days) days = d; } });
    if (days === null) return null; var t = new Date(); t.setDate(t.getDate() - days); return t.toISOString().slice(0, 10);
  }
  function apply(){
    var cut = sinceCut();
    document.querySelectorAll('.mrow').forEach(function(r){
      var ok = true;
      if (anyOn('owner') && !filters.owner[r.dataset.owner]) ok = false;
      if (anyOn('domain')) { var ds = r.dataset.domains.split(' '); if (!ds.some(function(d){ return filters.domain[d]; })) ok = false; }
      if (anyOn('verdict') && !filters.verdict[r.dataset.verdict]) ok = false;
      if (anyOn('author') && !filters.author[r.dataset.author]) ok = false;
      if (cut && r.dataset.created < cut) ok = false;
      r.hidden = !ok;
    });
    document.querySelectorAll('.grp').forEach(function(g){ g.hidden = !g.querySelector('.mrow:not([hidden])'); });
  }
  compose();
})();
"""

# The page comes in two wrappings from one body: a standalone document
# (what render.py writes to disk and screenshot.mjs opens), and the
# fragment form the Artifact tool publishes — it supplies the document
# skeleton itself and wants only the title, styles and content.
FRAGMENT = """<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>{style}</style>
<div class="wrap">
<header class="mast"><div class="eyebrow">{eyebrow}</div><h1>{h1}</h1><p class="dek">{dek}</p></header>
{tally}
{filters}
{clusters}
{body}
</div>
{cmd}
<script type="application/json" id="queue">{payload}</script>
<script>{script}</script>
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
""" + FRAGMENT.replace("<style>{style}</style>\n", "<style>{style}</style>\n</head>\n<body>\n") + """</body>
</html>
"""


# ---- CLI --------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--in", dest="inp", default=str(_REPO_ROOT / ".pr-review-queue.json"))
    ap.add_argument("--board", metavar="OUT.html", help="write the board page")
    ap.add_argument("--detail", type=int, metavar="N", help="write one PR's detail page (with --out)")
    ap.add_argument("--out", help="output path for --detail")
    ap.add_argument("--terminal", action="store_true", help="print the table to stdout")
    ap.add_argument("--artifact", action="store_true", help="emit the fragment form the Artifact tool wraps (no html/head/body)")
    ap.add_argument("--pr", type=int, help="with --terminal: one row")
    ap.add_argument("--self-test", action="store_true")
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.self_test:
        import test_render  # noqa: PLC0415 — the pytest file doubles as the harness
        return test_render.run_standalone()
    queue = json.loads(Path(args.inp).read_text())
    did = False
    if args.board:
        Path(args.board).write_text(render_board(queue, artifact=args.artifact))
        print(f"board → {args.board}", file=sys.stderr)
        did = True
    if args.detail is not None:
        out = args.out or str(_REPO_ROOT / ".pr-review-board.html")
        Path(out).write_text(render_detail(queue, args.detail, artifact=args.artifact))
        print(f"detail #{args.detail} → {out}", file=sys.stderr)
        did = True
    if args.terminal or not did:
        sys.stdout.write(render_terminal(queue, args.pr))
    return 0


if __name__ == "__main__":
    sys.exit(main())
