#!/usr/bin/env python3
"""Surface the contradictions a report-only review found on a generated page.

The report-only lane (pulumi/docs#20996) runs the claim pipeline over pages a
generator owns — the 248-page CLI command reference today — and records the
result to the S3 claims index. Recording alone is not enough on the FIRST pass
over a page, and that first pass is where the findings are:

  * the nightly `reverify-claims.py` only re-checks *volatile* entities, so a
    contradicted claim that isn't a version pin, price, or limit would sit in
    the index forever without anyone being told;
  * on the fix lane the model reads the verdicts and acts on them. There is no
    model on this lane — nothing edits a file a generator overwrites — so if
    this script doesn't report the contradiction, nothing does.

So: read the same pre-model `.verified-claims.json` snapshot the claims index
is built from, keep the decided-wrong verdicts, and route each one exactly the
way the nightly lane routes its own — through `reverify-claims.py`'s
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
# Same vocabulary the nightly lane treats as "the source says otherwise".
CONTRADICTED_VERDICTS = {"contradicted", "mismatch", "framing-drift"}
# Names this lane in the prefilled issue body. Worth saying: unlike a nightly
# re-check of a claim already in the index, this is the first time anyone has
# checked the page at all.
ISSUE_ORIGIN = "report-only content review (the first fact-check of this page)"

_REVERIFY = None


def log(msg: str) -> None:
    print(f"report-claims-findings: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::report-claims-findings: {msg}", file=sys.stderr)


def reverify():
    """reverify-claims.py imported by path, so the routing rules, the known-
    upstream registry, and the prefilled-issue link have exactly one
    definition. Its main() is guarded, so importing has no side effects."""
    global _REVERIFY
    if _REVERIFY is None:
        spec = importlib.util.spec_from_file_location(
            "reverify_claims", HERE / "reverify-claims.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _REVERIFY = mod
    return _REVERIFY


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
    """One entry per decided-wrong verdict, routed the way the nightly lane
    routes its own findings.

    `route` is `fix_route`'s answer for this page: "generated" or "missing" is
    the expected case here (that is what the lane runs on) and carries the
    upstream treatment — never filed as a stale-claims marker, because no PR in
    this repo could ever retire one. A "local" route means the page turned out
    to be editable after all, which is a tiers-file bug rather than a finding
    to route upstream; it is reported as such rather than silently reshaped.
    """
    rv = reverify()
    path = article["path"]
    route = rv.fix_route([{"path": path}], repo_root, tier_rules)
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
            finding["file_issue_url"] = rv.file_issue_url(
                finding, finding["text"], repos, origin=ISSUE_ORIGIN)
        findings.append(finding)
    return sorted(findings, key=lambda f: (f["entity_key"], str(f["claim_id"])))


def slack_text(article: dict, findings: list[dict], run_url: str | None) -> str:
    """The #docs-ops line for a page that came back with NEW findings.

    Counts and one line per finding, with the prefilled filing link — the same
    contract the nightly lane's upstream line has: a human reads it, judges it,
    and files it with one click and their own name on the issue.
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
            # Long URL on its own line, same shape as the nightly lane's
            # upstream Slack block — Slack renders it as the link text.
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
    rv = reverify()
    tier_rules = rv.load_tier_rules(Path(args.tiers) if args.tiers else None)
    known = rv.load_known_upstream(
        Path(args.known_upstream) if args.known_upstream else None)
    repos = rv.load_upstream_repos(
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

    print()
    if failures:
        print(f"{len(failures)} report-claims-findings self-test(s) FAILED", file=sys.stderr)
        return 1
    print("all report-claims-findings self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
