#!/usr/bin/env python3
"""Surface the contradictions a report-only review found on a generated page.

The report-only lane (pulumi/docs#20996) runs the claim pipeline over pages a
generator owns — the 248-page CLI command reference today — and records the
result to the S3 claims index. Recording alone is not enough on the FIRST pass
over a page, and that first pass is where the findings are:

  * nothing re-reads the index later, so a contradicted claim recorded
    without a report would sit there forever without anyone being told;
  * on the fix lane the model reads the verdicts and acts on them. There is no
    model on this lane — nothing edits a file a generator overwrites — so if
    this script doesn't report the contradiction, nothing does.

So: read the same pre-model `.verified-claims.json` snapshot the claims index
is built from, keep the decided-wrong verdicts, and route each one through
`fix_route` and `references/upstream-claims.yaml`, so a finding arrives with a
prefilled issue against the repo that owns the text, and a finding a human has
already filed stays quiet.

Nothing here marks a page, opens a PR, or edits anything: the pages this runs
on have no fixable source in this repo.

`--artifacts-dir` also sums the pipeline's own reported token usage into
`cost{}`. That is not decoration — the issue asks for the model spend to be
sized before the lane is turned up, and a per-page number measured on real
pages beats an estimate. It is printed on every run and rides the artifact.

Usage:
    report-claims-findings.py --queue .content-review-queue.json \\
        --verified .review-snapshot/.verified-claims.json \\
        [--artifacts-dir .review-snapshot] [--repo-root .] \\
        [--tiers <strategic-tiers.yaml>] [--known-upstream <upstream-claims.yaml>] \\
        [--out .report-findings.json] [--slack-out .report-slack.txt] \\
        [--run-url <url>]

Writes `has_findings` / `has_new_findings` / `n_contradicted` to $GITHUB_OUTPUT
when set. Degrades gracefully: an absent or unreadable snapshot yields an empty
report and exit 0 — a page whose verify pre-step failed is retried by the
ledger's `incomplete` path, not reported as clean here.

Self-contained smoke checks: `python3 report-claims-findings.py --self-test`.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
DEFAULT_TIERS = (
    REPO_ROOT
    / ".claude/commands/review-existing-content/references/strategic-tiers.yaml"
)
DEFAULT_KNOWN_UPSTREAM = (
    REPO_ROOT
    / ".claude/commands/review-existing-content/references/upstream-claims.yaml"
)

SCHEMA_VERSION = 1
# The verdicts that mean "the source says otherwise".
CONTRADICTED_VERDICTS = {"contradicted", "mismatch", "framing-drift"}
# Names this lane in the prefilled issue body. Worth saying: this is the first
# time anyone has checked the page at all.
ISSUE_ORIGIN = "report-only content review (the first fact-check of this page)"

_SELECT = None


def log(msg: str) -> None:
    print(f"report-claims-findings: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::report-claims-findings: {msg}", file=sys.stderr)


# ---- upstream routing --------------------------------------------------------


def _policy_for(path: str, rules: list[dict]):
    """select-articles.policy_for, imported by path so the tier semantics have
    exactly one definition (same pattern check-retire-veto.py uses)."""
    global _SELECT
    if _SELECT is None:
        spec = importlib.util.spec_from_file_location(
            "select_articles", HERE / "select-articles.py")
        _SELECT = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_SELECT)
    return _SELECT.policy_for(path, rules)


def load_tier_rules(tiers_file: Path | None) -> list[dict]:
    """Tier rules, or [] when unreadable. Failing to [] means every page looks
    editable, which reports the finding as route=local (a visible tiers-file
    problem) rather than dropping it."""
    if tiers_file is None or not tiers_file.is_file():
        return []
    try:
        _policy_for("content/docs/x.md", [])  # force the import, surface errors here
        return _SELECT.load_tiers(tiers_file)
    except Exception as e:  # noqa: BLE001
        warn(f"could not load tiers from {tiers_file} ({e}); "
             f"generated trees will route by file existence alone")
        return []


def fix_route(assertions: list[dict], repo_root: Path | None,
              tier_rules: list[dict] | None = None) -> str:
    """Where a contradicted claim about these pages can actually be fixed.

    Returns "local", "generated", or "missing". Two distinct ways to have no
    page a PR here can edit, and the file check alone catches only the first:

    * "missing" — no markdown in the tree. A Hugo content adapter builds the
      page from `data/` at request time (the pre-built policy packs).
    * "generated" — the markdown exists but is machine-written and clobbered
      on the next generator run, so an edit to it is thrown away. The CLI
      command reference is 248 such files. `strategic-tiers.yaml` already
      states exactly this as `editable: false`, so that file is the authority
      rather than a second list to keep in sync. Note it is the EDITABLE flag,
      not the tier: since #20996 the CLI tree is tier 3 and `reviewable: true`
      (this lane records its claims), and those claims must still route
      upstream.

    A claim asserted on several pages is fixable if ANY of them is.

    `repo_root=None` (and no rules) means "assume local", for pure-logic
    callers and the self-tests.
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


def file_issue_url(finding: dict, claim_text: str, repos: list[dict]) -> str | None:
    """A prefilled GitHub new-issue URL for an unfiled upstream finding.

    Returns None when no mapping owns the page — the finding still reports and
    still pages #docs-ops, it just arrives without a one-click filing.

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
        f"Found by the pulumi/docs {ISSUE_ORIGIN}. The page is generated, "
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


# ---- inputs ------------------------------------------------------------------


def load_article(queue_path: Path) -> dict:
    data = json.loads(queue_path.read_text())
    articles = data.get("articles") or []
    if not articles:
        raise SystemExit(f"report-claims-findings: no articles in {queue_path}")
    return articles[0]


def load_verdicts(verified_path: Path) -> tuple[list[dict], list[str], bool]:
    """(verdicts, errors, usable). `usable` is False when the artifact is
    absent or unparseable — the caller reports nothing rather than reporting a
    degraded run as a clean page."""
    if not verified_path.is_file():
        warn(f"{verified_path} is absent; nothing to report")
        return [], [], False
    try:
        doc = json.loads(verified_path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        warn(f"{verified_path} is unreadable ({e}); nothing to report")
        return [], [], False
    if not isinstance(doc, dict):
        warn(f"{verified_path} is not a JSON object; nothing to report")
        return [], [], False
    verdicts = [v for v in (doc.get("verdicts") or []) if isinstance(v, dict)]
    errors = [str(e) for e in (doc.get("errors") or [])]
    if not verdicts and errors:
        # The verify pre-step degraded. record-claims.py already declines to
        # overwrite the page's snapshot in this case; report nothing for the
        # same reason — "no contradictions" and "the check never ran" must not
        # look alike.
        warn(f"verify pre-step degraded ({len(errors)} error(s)); nothing to report")
        return [], errors, False
    return verdicts, errors, True


# ---- cost --------------------------------------------------------------------

# (artifact filename, meta keys to sum) — the pipeline stages that spend
# tokens. Extraction reports its usage under `meta`, verification under `meta`
# too, and merge-claims re-reports the extractors' totals under `llm_*` keys
# (skipped here so they aren't double-counted).
COST_ARTIFACTS = [
    (".candidate-claims-llm-1.json", "extract_atomic"),
    (".candidate-claims-llm-2.json", "extract_holistic"),
    (".verified-claims.json", "verify"),
]
TOKEN_KEYS = ("input_tokens", "output_tokens",
              "cache_read_input_tokens", "cache_creation_input_tokens")


def measure_cost(artifacts_dir: Path | None) -> dict:
    """Per-stage and total token usage as the pre-steps themselves reported it.

    Absent artifacts contribute zero rather than failing: this is
    instrumentation, and a missing number must never cost a run.
    """
    stages: dict[str, dict] = {}
    total = dict.fromkeys(TOKEN_KEYS, 0)
    if artifacts_dir is None:
        return {"stages": stages, "total": total}
    for filename, stage in COST_ARTIFACTS:
        f = artifacts_dir / filename
        if not f.is_file():
            continue
        try:
            meta = (json.loads(f.read_text()) or {}).get("meta") or {}
        except (OSError, json.JSONDecodeError, AttributeError):
            continue
        counts = {k: int(meta.get(k) or 0) for k in TOKEN_KEYS}
        stages[stage] = counts
        for k in TOKEN_KEYS:
            total[k] += counts[k]
    return {"stages": stages, "total": total}


# ---- findings ----------------------------------------------------------------


def build_findings(article: dict, verdicts: list[dict], repo_root: Path | None,
                   tier_rules: list[dict], known: dict[str, dict],
                   repos: list[dict]) -> list[dict]:
    """One entry per decided-wrong verdict, routed to where it can be fixed.

    `route` is `fix_route`'s answer for this page: "generated" or "missing" is
    the expected case here (that is what the lane runs on) and carries the
    upstream treatment, because no PR in this repo could fix it. A "local" route means the page turned out
    to be editable after all, which is a tiers-file bug rather than a finding
    to route upstream; it is reported as such rather than silently reshaped.
    """
    path = article["path"]
    route = fix_route([{"path": path}], repo_root, tier_rules)
    findings = []
    for v in verdicts:
        if v.get("verdict") not in CONTRADICTED_VERDICTS:
            continue
        entity_key = v.get("entity_key") or ""
        finding = {
            "entity_key": entity_key,
            "claim_id": v.get("claim_id"),
            "verdict": v.get("verdict"),
            "confidence": v.get("confidence"),
            "text": v.get("text") or "",
            "line_range": v.get("line_range"),
            "evidence": v.get("evidence") or "",
            "source": v.get("source") or "",
            "route": route,
            "pages": [{"path": path}],
            # An unkeyed claim can't be matched against the registry at all, so
            # it is always "new". Saying so beats pretending the lookup applied.
            "new": bool(not entity_key or entity_key not in known),
            "issue": (known.get(entity_key) or {}).get("issue") if entity_key else None,
        }
        if finding["new"]:
            finding["file_issue_url"] = file_issue_url(finding, finding["text"], repos)
        findings.append(finding)
    return sorted(findings, key=lambda f: (f["entity_key"], str(f["claim_id"])))


def slack_text(article: dict, findings: list[dict], run_url: str | None) -> str:
    """The #docs-ops line for a page that came back with NEW findings.

    Counts and one line per finding, with the prefilled filing link: a human
    reads it, judges it, and files it with one click and their own name on the
    issue.
    """
    new = [f for f in findings if f["new"]]
    url = article.get("url") or article["path"]
    lines = [
        f"Report-only content review: {len(new)} unfiled contradicted claim(s) on "
        f"`{article['path']}` — a generated page, so there is nothing to fix here "
        f"and the issue belongs upstream:"
    ]
    for f in new:
        label = f["entity_key"] or f.get("claim_id") or "(unkeyed claim)"
        lines.append(f"  • [{f['route']}] {label} ({f['verdict']})")
        lines.append(f"      {' '.join((f['evidence'] or '').split())[:240]}")
        if f.get("file_issue_url"):
            # Long URL on its own line — Slack renders it as the link text.
            lines.append(f"      <{f['file_issue_url']}|file it upstream>")
    tail = f"Page: {url}"
    if run_url:
        tail += f" · <{run_url}|Run log>"
    lines.append(tail)
    return "\n".join(lines)


# ---- outputs -----------------------------------------------------------------


def write_github_output(report: dict) -> None:
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if not gh_out:
        return
    counts = report["counts"]
    with open(gh_out, "a", encoding="utf-8") as fh:
        fh.write(f"n_contradicted={counts['contradicted']}\n")
        fh.write(f"has_findings={'true' if counts['contradicted'] else 'false'}\n")
        fh.write(f"has_new_findings={'true' if counts['new'] else 'false'}\n")


def run(args) -> int:
    article = load_article(Path(args.queue))
    verdicts, errors, usable = load_verdicts(Path(args.verified))
    tier_rules = load_tier_rules(Path(args.tiers) if args.tiers else None)
    known = load_known_upstream(
        Path(args.known_upstream) if args.known_upstream else None)
    repos = load_upstream_repos(
        Path(args.known_upstream) if args.known_upstream else None)

    findings = (
        build_findings(article, verdicts, Path(args.repo_root) if args.repo_root else None,
                       tier_rules, known, repos)
        if usable else []
    )
    report = {
        "schema_version": SCHEMA_VERSION,
        "path": article["path"],
        "slug": article.get("slug"),
        "url": article.get("url"),
        "checked_at": datetime.now(timezone.utc).date().isoformat(),
        "usable": usable,
        "counts": {
            "verdicts": len(verdicts),
            "contradicted": len(findings),
            "new": len([f for f in findings if f["new"]]),
            "known": len([f for f in findings if not f["new"]]),
            "errors": len(errors),
        },
        "cost": measure_cost(Path(args.artifacts_dir) if args.artifacts_dir else None),
        "findings": findings,
    }

    out_path = Path(args.out)
    out_path.write_text(json.dumps(report, indent=2) + "\n")
    c = report["counts"]
    total = report["cost"]["total"]
    log(f"{article['path']}: {c['verdicts']} verdict(s), {c['contradicted']} "
        f"contradicted ({c['new']} unfiled, {c['known']} already filed upstream) "
        f"-> {out_path}")
    log(f"model spend for this page: {total['input_tokens']} in / "
        f"{total['output_tokens']} out / {total['cache_read_input_tokens']} cache-read")
    for f in findings:
        state = "UNFILED" if f["new"] else f"filed: {f['issue']}"
        log(f"  [{f['route']}] {f['entity_key'] or f['claim_id']} "
            f"({f['verdict']}, {state}): {' '.join(f['evidence'].split())[:200]}")
        if f.get("file_issue_url"):
            log(f"    file it: {f['file_issue_url']}")

    if args.slack_out and c["new"]:
        Path(args.slack_out).write_text(
            slack_text(article, findings, args.run_url) + "\n")
    write_github_output(report)
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--queue", help="single-article queue JSON")
    p.add_argument("--verified", help="the pre-model .verified-claims.json snapshot")
    p.add_argument("--artifacts-dir", help="directory holding the pre-step artifacts (for cost)")
    p.add_argument("--repo-root", default=str(REPO_ROOT), help=argparse.SUPPRESS)
    p.add_argument("--tiers", default=str(DEFAULT_TIERS))
    p.add_argument("--known-upstream", default=str(DEFAULT_KNOWN_UPSTREAM))
    p.add_argument("--out", default=".report-findings.json")
    p.add_argument("--slack-out", help="write a #docs-ops message here when findings are new")
    p.add_argument("--run-url", help="workflow run URL, for the Slack line")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()
    if args.self_test:
        return self_test()
    if not args.queue or not args.verified:
        p.error("--queue and --verified are required")
    return run(args)


# ---- self-test ---------------------------------------------------------------


def self_test() -> int:
    import tempfile
    from urllib.parse import unquote_plus

    failures: list[str] = []

    def check(name: str, cond: bool) -> None:
        print(("ok: " if cond else "FAIL: ") + name,
              file=sys.stdout if cond else sys.stderr)
        if not cond:
            failures.append(name)

    article = {"path": "content/docs/iac/cli/commands/pulumi_up.md",
               "slug": "docs-iac-cli-commands-pulumi-up",
               "url": "/docs/iac/cli/commands/pulumi_up/"}
    rules = [{"prefix": "content/docs/iac/cli/commands/", "tier": 3,
              "editable": False, "reviewable": True}]
    repos = [{"prefix": "content/docs/iac/cli/commands/", "repo": "pulumi/pulumi"}]
    verdicts = [
        {"claim_id": "c1", "entity_key": "numerical/known-one", "verdict": "contradicted",
         "text": "The default is 90 days.", "evidence": "The source says 30.",
         "source": "https://example.com/x"},
        {"claim_id": "c2", "entity_key": "numerical/fresh-one", "verdict": "contradicted",
         "text": "Rotated every 90 days.", "evidence": "Unused, not rotated.",
         "source": "https://example.com/y"},
        {"claim_id": "c3", "entity_key": "version/ok", "verdict": "verified",
         "text": "v3", "evidence": "", "source": ""},
        {"claim_id": "c4", "entity_key": "", "verdict": "mismatch",
         "text": "Unkeyed but wrong.", "evidence": "no", "source": ""},
    ]
    known = {"numerical/known-one": {"issue": "https://github.com/pulumi/pulumi/issues/1"}}

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "content/docs/iac/cli/commands").mkdir(parents=True)
        (root / article["path"]).write_text("# gen\n")

        findings = build_findings(article, verdicts, root, rules, known, repos)
        check("only decided-wrong verdicts become findings", len(findings) == 3)
        check("a generated page routes upstream, never to a marker",
              all(f["route"] == "generated" for f in findings))
        by_key = {f["entity_key"]: f for f in findings}
        check("an already-filed finding is not new and carries its issue",
              by_key["numerical/known-one"]["new"] is False
              and by_key["numerical/known-one"]["issue"].endswith("/1"))
        check("an unfiled finding is new and carries a prefilled issue link",
              by_key["numerical/fresh-one"]["new"] is True
              and "github.com/pulumi/pulumi/issues/new"
              in by_key["numerical/fresh-one"]["file_issue_url"])
        check("an unkeyed claim can't be matched, so it reports as new",
              by_key[""]["new"] is True)

        # A page the tiers file says IS editable must not be reshaped into an
        # upstream finding: that is a tiers-file bug and the route says so.
        local = build_findings(article, verdicts, root, [], known, repos)
        check("an editable page reports route=local rather than pretending",
              all(f["route"] == "local" for f in local))

        # Degradation: verifier never ran -> report nothing, not "clean".
        (root / "degraded.json").write_text(json.dumps(
            {"verdicts": [], "errors": ["verify-claims.py failed to start"]}))
        _, errs, usable = load_verdicts(root / "degraded.json")
        check("a degraded verify artifact is not usable", usable is False and len(errs) == 1)
        _, _, usable_missing = load_verdicts(root / "nope.json")
        check("an absent artifact is not usable, and never raises", usable_missing is False)
        (root / "empty.json").write_text(json.dumps({"verdicts": [], "errors": []}))
        _, _, usable_empty = load_verdicts(root / "empty.json")
        check("a genuinely claim-free page IS usable", usable_empty is True)

        # Cost: summed from what the pre-steps reported, missing files are zero.
        (root / ".verified-claims.json").write_text(json.dumps(
            {"meta": {"input_tokens": 10, "output_tokens": 2,
                      "cache_read_input_tokens": 5, "cache_creation_input_tokens": 0}}))
        (root / ".candidate-claims-llm-1.json").write_text(json.dumps(
            {"meta": {"input_tokens": 7, "output_tokens": 3}}))
        cost = measure_cost(root)
        check("cost sums the stages that reported usage",
              cost["total"]["input_tokens"] == 17
              and cost["total"]["output_tokens"] == 5
              and set(cost["stages"]) == {"verify", "extract_atomic"})
        check("no artifacts dir -> zeros, never an error",
              measure_cost(None)["total"]["input_tokens"] == 0)

        text = slack_text(article, findings, "https://example.com/run")
        check("the Slack line counts only the unfiled findings",
              text.startswith("Report-only content review: 2 unfiled"))
        check("the Slack line carries the filing link and the run log",
              "file it upstream" in text and "issues/new" in text and "Run log" in text)
        check("the prefilled issue says which lane found it",
              "report-only+content+review" in by_key["numerical/fresh-one"]["file_issue_url"])

    # Routing: the file check alone can't tell a generated page from an
    # editable one, and a claim spanning both kinds routes to the fixable one.
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
        check("a tier-0 page with a real file still routes generated",
              fix_route(gen, root, rules) == "generated")
        check("one fixable asserting page wins", fix_route(gen + local, root, rules) == "local")
        check("generated beats missing when a claim spans both",
              fix_route(gen + absent, root, rules) == "generated")
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
            "    issue: https://github.com/pulumi/pulumi/issues/1\n")
        check("known-upstream parses to a key map",
              set(load_known_upstream(ku)) == {"numerical/known-one"})
        check("missing known-upstream file is empty, not fatal",
              load_known_upstream(root / "nope.yaml") == {})
        (root / "bad.yaml").write_text("known: [{{{\n")
        check("malformed known-upstream fails open (noisier, never blinder)",
              load_known_upstream(root / "bad.yaml") == {})

    # Prefilled filing links: mapped tree gets one, unmapped tree gets None
    # (still reported, still paged — just no one-click).
    pp_repos = [{"prefix": "content/docs/reference/pre-built-policy-packs/",
                 "repo": "pulumi/policy-packs-internal"}]
    finding = {"entity_key": "numerical/iam-user-unused-credentials-90",
               "evidence": "AWS Config's rule covers UNUSED credentials, not rotation.",
               "source": "https://docs.aws.amazon.com/config/latest/developerguide/x.html",
               "pages": [{"path": "content/docs/reference/pre-built-policy-packs/cis/aws.md"}]}
    url = file_issue_url(finding, "The policy ensures credentials are rotated within 90 days.",
                         pp_repos)
    check("mapped tree yields a filing link",
          url is not None and url.startswith("https://github.com/pulumi/policy-packs-internal/issues/new?"))
    check("link carries the claim, the finding, the source, and the page",
          all(t in unquote_plus(url) for t in
              ("rotated within 90 days", "UNUSED credentials", "docs.aws.amazon.com",
               "content/docs/reference/pre-built-policy-packs/cis/aws.md")))
    check("unmapped tree yields no link",
          file_issue_url({**finding, "pages": [{"path": "content/docs/iac/concepts/x.md"}]},
                         "t", pp_repos) is None)
    check("a finding with no pages yields no link",
          file_issue_url({**finding, "pages": []}, "t", pp_repos) is None)
    # A body that silently loses its tail is worse than a short one, so the
    # fields are clipped; guard the total against GitHub's query-string limit.
    huge = file_issue_url({**finding, "evidence": "E" * 20000, "source": "S" * 20000},
                          "C" * 20000, pp_repos)
    check(f"oversized finding still yields a usable URL ({len(huge)} chars)", len(huge) < 8000)

    # The shipped file itself: every entry needs a tracking issue, or it is a
    # mute button with nobody behind it.
    check("shipped repo map parses and covers the policy-pack tree",
          any(r["prefix"] == "content/docs/reference/pre-built-policy-packs/"
              for r in load_upstream_repos(DEFAULT_KNOWN_UPSTREAM)))
    if DEFAULT_KNOWN_UPSTREAM.is_file():
        entries = load_known_upstream(DEFAULT_KNOWN_UPSTREAM)
        check("every shipped entry cites an upstream issue",
              all(str(e.get("issue") or "").startswith("http") for e in entries.values()))
        check("every shipped entry says what is wrong",
              all(str(e.get("what") or "").strip() for e in entries.values()))

    print()
    if failures:
        print(f"{len(failures)} report-claims-findings self-test(s) FAILED", file=sys.stderr)
        return 1
    print("all report-claims-findings self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
