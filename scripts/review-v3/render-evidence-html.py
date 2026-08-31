#!/usr/bin/env python3
"""Render a pr-review evidence object into a self-contained HTML page.

    render-evidence-html.py --evidence FILE --output FILE.html

The two pinned PR comments carry only summaries; this is the page a
reviewer actually reads the evidence on — linked from both, hosted as an
S3 static-site object (see README.md "The evidence object"). It has to work
from a plain `file://` open as well as from S3, so everything is inlined:
CSS, JS, and the evidence data itself (as a `<script type="application/json">`
block, same pattern as `scripts/review-admin/review-admin.py`'s
`render_html`/`HTML_TEMPLATE`). No external requests, no CDN script tags.

Design choice worth stating: the trail, findings, investigation log, and
history are rendered server-side (by this script, into plain HTML) rather
than client-side from the embedded JSON. A small amount of vanilla JS then
does progressive enhancement — verdict filtering and text search — by
toggling `hidden` on rows already in the DOM. Two reasons: (1) every value
that reaches the page goes through `html.escape` exactly once, in Python,
so there is a single place to audit for injection, rather than trusting
every client-side render call site to use `textContent` and never
`innerHTML`; and (2) it makes the anchors and the escaping both verifiable
by `--self-test` against the static output, with no browser involved. The
embedded JSON block is kept anyway (as `#evidence-data`) so the page still
satisfies "data inlined as JSON, zero external requests" for any future
client-side feature, and so a viewer can copy the raw evidence out.

Trail rows get a STABLE anchor: `id="claim-<n>"` where `n` is the row's
1-based position in `evidence["trail"]` as given — computed before the
verdict grouping that determines where the row is displayed, so a comment
that links `#claim-7` keeps pointing at the same claim even though the
page groups rows by verdict rather than array order.

Self-contained — run the smoke checks with
`render-evidence-html.py --self-test` (anchors present, all eight verdicts
rendered, and a claim containing `<script>` comes out escaped, never as a
live tag).
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path

# verdict -> (emoji, display label), in the display order sections render in.
VERDICT_VOCAB = [
    ("verified", "✅", "Verified"),
    ("matches", "🤝", "Matches"),
    ("not-a-claim", "➖", "Not a claim"),
    ("unverifiable", "🤷", "Unverifiable"),
    ("contradicted", "❌", "Contradicted"),
    ("mismatch", "⚔️", "Mismatch"),
    ("framing-drift", "🌀", "Framing drift"),
    ("flagged", "🚩", "Flagged"),
]
VERDICT_EMOJI = {v: e for v, e, _ in VERDICT_VOCAB}
VERDICT_LABEL = {v: label for v, _, label in VERDICT_VOCAB}
VERDICT_ORDER = {v: i for i, (v, _, _) in enumerate(VERDICT_VOCAB)}

BUCKET_LABEL = {
    "outstanding": "🚨 Outstanding",
    "author-answer": "❓ Author answer",
    "reviewer-check": "👀 Reviewer check",
    "preexisting": "💡 Preexisting",
}


def esc(v) -> str:
    """html.escape every value that reaches the page, in exactly one place."""
    if v is None:
        return ""
    return html.escape(str(v), quote=True)


def _file_lines(f: dict) -> str:
    file = f.get("file") or ""
    lines = f.get("lines") or []
    if not lines:
        return file
    if len(lines) == 1:
        return f"{file}:{lines[0]}"
    return f"{file}:{lines[0]}-{lines[1]}"


def render_header(evidence: dict) -> str:
    repo = evidence.get("repo") or ""
    pr = evidence.get("pr")
    sha = evidence.get("head_sha") or ""
    short_sha = sha[:10]
    pr_url = f"https://github.com/{repo}/pull/{pr}"
    return f"""
<header>
  <h1>Review evidence</h1>
  <div class="meta">
    <span>{esc(repo)}</span>
    <a href="{esc(pr_url)}">PR #{esc(pr)}</a>
    <span title="{esc(sha)}">{esc(short_sha)}</span>
    <span>generated {esc(evidence.get('generated_at'))}</span>
  </div>
  {f'<p class="summary">{esc(evidence.get("summary"))}</p>' if evidence.get('summary') else ''}
</header>
"""


def render_trail(trail: list[dict]) -> str:
    # Anchors are assigned from the raw array position, BEFORE the
    # verdict-grouped sort below — see module docstring.
    rows = [(i + 1, t) for i, t in enumerate(trail)]
    rows_sorted = sorted(
        rows, key=lambda pair: VERDICT_ORDER.get(pair[1].get("verdict"), 999)
    )

    chips = "".join(
        f'<button class="chip" data-verdict-filter="{v}">{e} {label}'
        f'<span class="chip-count" data-verdict-count="{v}"></span></button>'
        for v, e, label in VERDICT_VOCAB
    )

    row_html = []
    for n, t in rows_sorted:
        verdict = t.get("verdict") or ""
        emoji = VERDICT_EMOJI.get(verdict, "")
        label = VERDICT_LABEL.get(verdict, verdict)
        loc = t.get("file") or ""
        if t.get("line"):
            loc = f"{loc}:{t['line']}"
        extra = []
        if t.get("evidence"):
            extra.append(f'<div class="trail-evidence">{esc(t["evidence"])}</div>')
        if t.get("source"):
            extra.append(f'<div class="trail-source">source: {esc(t["source"])}</div>')
        if t.get("route"):
            extra.append(f'<span class="trail-route">{esc(t["route"])}</span>')
        row_html.append(f"""
    <div class="trail-row" id="claim-{n}" data-verdict="{esc(verdict)}">
      <a class="anchor" href="#claim-{n}">#{n}</a>
      <span class="verdict-badge" title="{esc(label)}">{emoji} {esc(label)}</span>
      <div class="trail-body">
        <div class="trail-loc">{esc(loc)}</div>
        <div class="trail-claim">{esc(t.get('claim'))}</div>
        {''.join(extra)}
      </div>
    </div>""")

    return f"""
<section id="trail">
  <h2>Verification trail</h2>
  <div class="controls">
    <input id="trail-search" type="search" placeholder="Search claims…" aria-label="Search claims">
    <div class="chips">{chips}</div>
  </div>
  <div id="trail-rows">{''.join(row_html) if row_html else '<p class="empty">No trail entries.</p>'}</div>
  <p id="trail-empty" class="empty" hidden>No claims match the current filter.</p>
</section>
"""


def render_findings(findings: list[dict]) -> str:
    if not findings:
        return '<section id="findings"><h2>Findings</h2><p class="empty">No findings.</p></section>'
    rows = []
    for f in findings:
        disp = f.get("disposition") or {}
        disp_text = disp.get("disposition") or "—"
        if disp.get("note"):
            disp_text += f" — {disp['note']}"
        rows.append(f"""
    <tr>
      <td>{esc(f.get('id'))}</td>
      <td>{esc(BUCKET_LABEL.get(f.get('bucket'), f.get('bucket')))}</td>
      <td>{esc(_file_lines(f))}</td>
      <td>{esc(f.get('status'))}</td>
      <td>{esc(disp_text)}</td>
    </tr>""")
    return f"""
<section id="findings">
  <h2>Findings</h2>
  <div class="tablewrap">
    <table>
      <thead><tr><th>ID</th><th>Bucket</th><th>File:lines</th><th>Status</th><th>Disposition</th></tr></thead>
      <tbody>{''.join(rows)}</tbody>
    </table>
  </div>
</section>
"""


def render_investigation_log(ilog: dict) -> str:
    if not ilog:
        return ""
    items = "".join(
        f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in ilog.items()
    )
    return f"""
<section id="investigation-log">
  <h2>Investigation log</h2>
  <dl class="ilog">{items}</dl>
</section>
"""


def render_editorial_balance(balance) -> str:
    if not balance:
        return ""
    return f"""
<section id="editorial-balance">
  <h2>Editorial balance</h2>
  <pre>{esc(json.dumps(balance, indent=2, sort_keys=True))}</pre>
</section>
"""


def render_triaged(triaged: list) -> str:
    if not triaged:
        return ""
    items = "".join(f"<li><pre>{esc(json.dumps(t, indent=2, sort_keys=True))}</pre></li>" for t in triaged)
    return f"""
<section id="triaged">
  <h2>Triaged</h2>
  <ul class="triaged-list">{items}</ul>
</section>
"""


def render_history(history: list[dict]) -> str:
    if not history:
        return ""
    items = "".join(
        f"""<li><span class="history-ts">{esc(h.get('ts'))}</span>
        <span class="history-sha">{esc((h.get('sha') or '')[:10])}</span>
        <p>{esc(h.get('summary'))}</p></li>"""
        for h in history
    )
    return f"""
<section id="history">
  <h2>History</h2>
  <ol class="history-timeline">{items}</ol>
</section>
"""


STYLE = """
:root {
  --bg:#fff; --fg:#1a1a2e; --muted:#5a5a72; --border:#d8d8e4; --surface:#f4f4fa;
  --accent:#805ac3; --bad:#c0392b; --good:#1e7e46; --warn:#a66900;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg:#16161f; --fg:#e8e8f0; --muted:#a3a3b8; --border:#3a3a4c; --surface:#20202c;
    --accent:#b49aea; --bad:#e57368; --good:#5dbb85; --warn:#d9a04a;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--fg);
  font: 15px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
main { max-width: 880px; margin: 0 auto; padding: 0 16px 60px; }
header { padding: 20px 16px; border-bottom: 1px solid var(--border); }
header h1 { font-size: 20px; margin: 0 0 8px; }
header .meta { display: flex; gap: 14px; flex-wrap: wrap; color: var(--muted); font-size: 13px; }
header .meta a { color: var(--accent); }
header .summary { margin: 10px 0 0; color: var(--fg); }
section { margin-top: 32px; }
h2 { font-size: 16px; margin: 0 0 12px; }
.empty { color: var(--muted); font-style: italic; }
.controls { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; margin-bottom: 14px; }
#trail-search {
  padding: 7px 10px; border: 1px solid var(--border); border-radius: 6px;
  background: var(--bg); color: var(--fg); min-width: 220px; flex: 1 1 auto;
}
.chips { display: flex; gap: 6px; flex-wrap: wrap; }
.chip {
  border: 1px solid var(--border); background: var(--surface); color: var(--fg);
  border-radius: 12px; padding: 4px 10px; font-size: 12px; cursor: pointer;
}
.chip.on { border-color: var(--accent); color: var(--accent); font-weight: 600; }
.chip-count { color: var(--muted); margin-left: 4px; }
.trail-row {
  display: flex; gap: 10px; align-items: flex-start; padding: 10px 0;
  border-bottom: 1px solid var(--border); scroll-margin-top: 12px;
}
.trail-row:target { background: var(--surface); }
.trail-row .anchor { color: var(--muted); text-decoration: none; font-size: 12px; padding-top: 2px; }
.verdict-badge { white-space: nowrap; font-size: 13px; }
.trail-body { flex: 1; min-width: 0; }
.trail-loc { font-family: ui-monospace, monospace; font-size: 12px; color: var(--muted); word-break: break-all; }
.trail-claim { margin-top: 2px; }
.trail-evidence { margin-top: 4px; font-size: 13px; color: var(--muted); }
.trail-source { margin-top: 2px; font-size: 12px; color: var(--muted); }
.trail-route { font-size: 11px; color: var(--muted); }
.tablewrap { overflow-x: auto; border: 1px solid var(--border); border-radius: 8px; }
table { border-collapse: collapse; width: 100%; min-width: 480px; }
th, td { text-align: left; padding: 7px 10px; border-bottom: 1px solid var(--border); vertical-align: top; }
th { background: var(--surface); position: sticky; top: 0; }
.ilog { display: grid; grid-template-columns: max-content 1fr; gap: 6px 16px; }
.ilog dt { color: var(--muted); font-size: 13px; }
.ilog dd { margin: 0; }
pre {
  background: var(--surface); border: 1px solid var(--border); border-radius: 8px;
  padding: 10px; overflow-x: auto; font-size: 12px;
}
.triaged-list { list-style: none; margin: 0; padding: 0; }
.triaged-list li { margin-bottom: 10px; }
.history-timeline { list-style: none; margin: 0; padding: 0; border-left: 2px solid var(--border); }
.history-timeline li { padding: 0 0 14px 16px; position: relative; }
.history-timeline li::before {
  content: ""; position: absolute; left: -5px; top: 4px; width: 8px; height: 8px;
  border-radius: 50%; background: var(--accent);
}
.history-ts { font-size: 12px; color: var(--muted); }
.history-sha { font-family: ui-monospace, monospace; font-size: 12px; color: var(--muted); margin-left: 8px; }
.history-timeline p { margin: 2px 0 0; }
"""

SCRIPT = """
(function () {
  var search = document.getElementById('trail-search');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip'));
  var rows = Array.prototype.slice.call(document.querySelectorAll('.trail-row'));
  var empty = document.getElementById('trail-empty');
  var activeVerdicts = new Set();

  chips.forEach(function (chip) {
    var v = chip.getAttribute('data-verdict-filter');
    var count = rows.filter(function (r) { return r.getAttribute('data-verdict') === v; }).length;
    var countEl = chip.querySelector('.chip-count');
    if (countEl) countEl.textContent = '(' + count + ')';
    chip.addEventListener('click', function () {
      if (activeVerdicts.has(v)) { activeVerdicts.delete(v); chip.classList.remove('on'); }
      else { activeVerdicts.add(v); chip.classList.add('on'); }
      apply();
    });
  });

  function apply() {
    var q = (search.value || '').toLowerCase();
    var visible = 0;
    rows.forEach(function (row) {
      var verdictOk = activeVerdicts.size === 0 || activeVerdicts.has(row.getAttribute('data-verdict'));
      var textOk = !q || row.textContent.toLowerCase().indexOf(q) !== -1;
      var show = verdictOk && textOk;
      row.hidden = !show;
      if (show) visible++;
    });
    empty.hidden = visible !== 0;
  }

  if (search) search.addEventListener('input', apply);
})();
"""


def render_evidence_html(evidence: dict) -> str:
    payload = json.dumps(evidence, indent=2).replace("</", "<\\/")
    body = "\n".join([
        render_header(evidence),
        '<main>',
        render_trail(evidence.get("trail") or []),
        render_findings(evidence.get("findings") or []),
        render_investigation_log(evidence.get("investigation_log") or {}),
        render_editorial_balance(evidence.get("editorial_balance")),
        render_triaged(evidence.get("triaged") or []),
        render_history(evidence.get("history") or []),
        '</main>',
    ])
    repo = esc(evidence.get("repo") or "")
    pr = esc(evidence.get("pr"))
    title = f"Review evidence — {repo} #{pr}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{STYLE}</style>
</head>
<body>
{body}
<script type="application/json" id="evidence-data">{payload}</script>
<script>{SCRIPT}</script>
</body>
</html>
"""


# ---- self-test ---------------------------------------------------------


def _fixture_evidence() -> dict:
    trail = []
    for i, (v, _, _) in enumerate(VERDICT_VOCAB):
        trail.append({
            "file": f"content/docs/file-{i}.md",
            "line": i + 1,
            "claim": f"Claim body for verdict {v} <script>alert(1)</script>",
            "verdict": v,
            "evidence": "some evidence",
        })
    return {
        "schema_version": 1,
        "repo": "pulumi/docs",
        "pr": 21300,
        "head_sha": "a" * 40,
        "run_id": "run-1",
        "generated_at": "2026-08-31T17:00:00Z",
        "high_water": 1,
        "findings": [
            {"id": "F1", "bucket": "outstanding", "file": "x.md", "lines": [1, 2],
             "text": "t", "origin": "o", "status": "open"},
        ],
        "trail": trail,
        "investigation_log": {"scan": "ok"},
        "editorial_balance": {"note": "balanced"},
        "triaged": [{"id": "T1"}],
        "history": [{"ts": "2026-08-31T17:00:00Z", "summary": "compose", "sha": "a" * 7}],
        "summary": "Fixture summary",
    }


def self_test() -> int:
    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    evidence = _fixture_evidence()
    out = render_evidence_html(evidence)

    check("doctype present", out.strip().startswith("<!doctype html>"))
    check("no external script or stylesheet tags",
          "<script src=" not in out and "<link" not in out
          and "cdnjs" not in out and "jsdelivr" not in out)

    for i in range(1, len(VERDICT_VOCAB) + 1):
        check(f"anchor claim-{i} present", f'id="claim-{i}"' in out)

    for v, e, label in VERDICT_VOCAB:
        check(f"verdict {v!r} emoji rendered", e in out)
        check(f"verdict {v!r} label rendered", esc(label) in out)

    check("raw <script>alert(1)</script> from claim text never appears literally",
          "<script>alert(1)</script>" not in out)
    check("claim text is present, escaped",
          "&lt;script&gt;alert(1)&lt;/script&gt;" in out)

    check("PR link present", "https://github.com/pulumi/docs/pull/21300" in out)
    check("head sha (short) present", out.count("aaaaaaaaaa") >= 1)

    check("findings table renders the finding id", ">F1<" in out)
    check("investigation log renders its key", "scan" in out)
    check("editorial balance rendered", "balanced" in out)
    check("triaged rendered", '"id": "T1"' in out)
    check("history rendered", "compose" in out)

    # Anchor stability: re-render with a shuffled fixture whose trail array
    # order is unchanged (grouping is a display concern only) should assign
    # identical anchors.
    out2 = render_evidence_html(_fixture_evidence())
    ids1 = [line for line in out.splitlines() if 'class="trail-row" id="claim-' in line]
    ids2 = [line for line in out2.splitlines() if 'class="trail-row" id="claim-' in line]
    check("anchors are stable across identical re-renders", ids1 == ids2)

    empty_trail = {**evidence, "trail": []}
    out3 = render_evidence_html(empty_trail)
    check("empty trail renders without error", "No trail entries." in out3)

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall render-evidence-html self-tests passed")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Render a pr-review evidence object to HTML.")
    p.add_argument("--evidence", help="evidence JSON file")
    p.add_argument("--output", help="output .html file")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()

    if args.self_test:
        return self_test()
    if not args.evidence or not args.output:
        p.error("--evidence and --output are required")

    try:
        evidence = json.loads(Path(args.evidence).read_text())
    except (OSError, json.JSONDecodeError) as e:
        print(f"render-evidence-html: unreadable evidence file: {e}", file=sys.stderr)
        return 1

    html_out = render_evidence_html(evidence)
    Path(args.output).write_text(html_out)
    print(f"render-evidence-html: wrote {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
