#!/usr/bin/env python3
"""Turn one CI job's Claude calls into durable usage rows.

The review pipelines already measure almost every token they spend: each
pre-step writes its totals into its JSON `meta`, `.verified-claims.json` puts a
`model_usage` block on every verdict, and claude-code-action's execution log
ends with a `result` event carrying per-model usage and `total_cost_usd`. None
of it outlives the runner (or the 30/90-day artifact), so cost per PR, per step
and per claim was only answerable by hand. This script reads whatever of that
exists at the end of a job and writes one NDJSON file of rows the data team
loads from the content-review ledger bucket (`usage/` prefix).

    record-usage.py --job claude-review --pr 123 --head-sha abc... \
        --source meta:extract-atomic:.candidate-claims-llm-1.json \
        --source claims:verify:.verified-claims.json \
        --source exec:compose:$RUNNER_TEMP/claude-execution-output.json \
        --outcome compose=success --effort compose=low

Source kinds (`--source KIND:STEP:PATH`, repeatable; a missing or unreadable
file is skipped with a note, never an error):

  meta    A pre-step artifact with top-level `model` and token totals in
          `meta` (extract-claims-llm.py, readthrough.py). One step row.
  claims  `.verified-claims.json`. One step row (the `meta` totals) plus one
          claim row per verdict, from that verdict's `model_usage`.
  exec    claude-code-action's execution log (stream-JSON, NDJSON or array).
          One step row per model in the `result` event's `modelUsage`, so a
          run whose subagents ran on another model prices correctly. With no
          `result` event (timeout, crash) the assistant messages are summed
          per model instead, deduplicated by message id. That is a lower
          bound: streamed messages report partial output counts.
  usage   A Messages API response, or any JSON with `model` and `usage`
          (the triage Haiku call). One step row.

Grains (`grain` field): `step` rows carry a step's tokens; `claim` rows carry
one verified claim's tokens, so summing both double-counts the verify step.
Dashboards sum `step` rows for spend and use `claim` rows to split the verify
step by claim, route and verdict.

Rows carry raw token counts, never prices. The one dollar figure is
`reported_cost_usd` on `exec` rows, which is what claude-code-action reports.
Prices live in an effective-dated seed the warehouse applies at query time.

Output: `<out-dir>/<YYYY-MM-DD>/<run_id>-<attempt>-<job>.ndjson`, one immutable
file per job. No rows ⇒ no file. The workflow uploads the directory as a
`docs-agent-usage-*` artifact and record-usage.yml copies it to S3. This script
never touches the network and never fails the run: any error is a `::warning::`
and exit 0.

Self-contained smoke checks: `record-usage.py --self-test`.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import traceback
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = 1
TOKEN_KEYS = (
    "input_tokens",
    "output_tokens",
    "cache_read_input_tokens",
    "cache_creation_input_tokens",
)
# claude-code-action's `modelUsage` spells the same four counters in camelCase.
CAMEL_KEYS = {
    "inputTokens": "input_tokens",
    "outputTokens": "output_tokens",
    "cacheReadInputTokens": "cache_read_input_tokens",
    "cacheCreationInputTokens": "cache_creation_input_tokens",
}
SOURCE_KINDS = ("meta", "claims", "exec", "usage")
DEFAULT_OUT_DIR = ".docs-agent-usage"


def log(msg: str) -> None:
    print(f"record-usage: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::record-usage: {msg}")


def _int(v) -> int:
    try:
        return int(v or 0)
    except (TypeError, ValueError):
        return 0


def _tokens(usage: dict | None) -> dict:
    usage = usage or {}
    return {k: _int(usage.get(k)) for k in TOKEN_KEYS}


def _iso(epoch) -> str | None:
    try:
        return datetime.fromtimestamp(int(epoch), tz=timezone.utc).isoformat(timespec="seconds")
    except (TypeError, ValueError, OverflowError, OSError):
        return None


def map_outcome(step_outcome: str | None, degraded: bool = False) -> str:
    """Fold a GitHub step outcome (plus what the artifact itself says) into
    the row's `outcome`. Unknown words pass through: the data team flags
    them rather than the recorder guessing."""
    o = (step_outcome or "").strip().lower()
    if o in ("", "success"):
        return "degraded" if degraded else "success"
    if o == "failure":
        return "failed"
    return o


def workflow_file(ref: str | None) -> str | None:
    """`owner/repo/.github/workflows/x.yml@refs/heads/master` → `x.yml`."""
    if not ref:
        return None
    return ref.split("@", 1)[0].rsplit("/", 1)[-1] or None


class Context:
    def __init__(self, args):
        self.repo = args.repo or os.environ.get("GITHUB_REPOSITORY")
        self.workflow = args.workflow or workflow_file(os.environ.get("GITHUB_WORKFLOW_REF"))
        self.job = args.job or os.environ.get("GITHUB_JOB")
        self.run_id = _int(args.run_id or os.environ.get("GITHUB_RUN_ID")) or None
        self.run_attempt = _int(args.run_attempt or os.environ.get("GITHUB_RUN_ATTEMPT") or 1)
        self.pr = _int(args.pr) or None
        self.head_sha = args.head_sha or None
        self.page_path = args.page_path or None
        self.job_started_at = _iso(args.job_started_at) if args.job_started_at else None
        self.outcomes = _kv(args.outcome)
        self.efforts = _kv(args.effort)
        self.started = _kv(args.started_at)
        self.models = _kv(args.model)

    def base(self, grain: str, step: str) -> dict:
        return {
            "schema_version": SCHEMA_VERSION,
            "grain": grain,
            "repo": self.repo,
            "workflow": self.workflow,
            "job": self.job,
            "step": step,
            "run_id": self.run_id,
            "run_attempt": self.run_attempt,
            "pr": self.pr,
            "head_sha": self.head_sha,
            "page_path": self.page_path,
        }

    def step_row(self, step: str, model: str | None, tokens: dict, *, turns=None,
                 reported_cost_usd=None, duration_ms=None, degraded=False,
                 outcome: str | None = None) -> dict:
        row = self.base("step", step)
        started = _iso(self.started.get(step)) or self.job_started_at
        row.update({
            "model": model or self.models.get(step),
            "effort": self.efforts.get(step),
            **tokens,
            "turns": turns,
            "reported_cost_usd": reported_cost_usd,
            "started_at": started,
            "duration_ms": duration_ms,
            "outcome": outcome or map_outcome(self.outcomes.get(step), degraded),
        })
        return row


def _kv(items: list[str] | None) -> dict:
    out = {}
    for item in items or []:
        if "=" in item:
            k, v = item.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


# ---- source readers -------------------------------------------------------


def rows_from_meta(ctx: Context, step: str, data: dict) -> list[dict]:
    if data.get("ran") is False:
        # readthrough.py's explicit "lane skipped" marker: no call was made.
        return []
    tokens = _tokens(data.get("meta"))
    return [ctx.step_row(step, data.get("model"), tokens, degraded=bool(data.get("errors")))]


def rows_from_claims(ctx: Context, step: str, data: dict) -> list[dict]:
    verdicts = [v for v in (data.get("verdicts") or []) if isinstance(v, dict)]
    meta_tokens = _tokens(data.get("meta"))
    # The meta totals are the sum of the verdicts' usage; recompute when a
    # hand-built stub left them at zero so the step row never undercounts.
    summed = {k: sum(_int((v.get("model_usage") or {}).get(k)) for v in verdicts) for k in TOKEN_KEYS}
    tokens = summed if sum(summed.values()) > sum(meta_tokens.values()) else meta_tokens
    turns = sum(_int((v.get("model_usage") or {}).get("turns")) for v in verdicts)
    step_model = data.get("model")
    rows = [ctx.step_row(step, step_model, tokens, turns=turns, degraded=bool(data.get("errors")))]
    for v in verdicts:
        mu = v.get("model_usage") or {}
        row = ctx.base("claim", step)
        row.update({
            "claim_id": v.get("claim_id"),
            "entity_key": v.get("entity_key"),
            "claim_type": v.get("type"),
            "file": v.get("file"),
            "line_range": v.get("line_range"),
            "route": v.get("route"),
            "verdict": v.get("verdict"),
            "confidence": v.get("confidence"),
            "turn_cap_exhausted": bool(v.get("turn_cap_exhausted")),
            "source_discipline_gate": v.get("source_discipline_gate"),
            "model": v.get("model") or step_model,
            **_tokens(mu),
            "turns": _int(mu.get("turns")),
        })
        rows.append(row)
    return rows


def _read_stream(path: Path) -> list[dict]:
    """claude-code-action's log is NDJSON on older versions and a single JSON
    array on newer ones (same tolerance as per-tool-spend.py)."""
    text = path.read_text(encoding="utf-8")
    stripped = text.lstrip()
    if stripped.startswith("["):
        try:
            data = json.loads(stripped)
            return [e for e in data if isinstance(e, dict)]
        except json.JSONDecodeError:
            pass
    events = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            events.append(obj)
    return events


def rows_from_exec(ctx: Context, step: str, events: list[dict]) -> list[dict]:
    configured = ctx.models.get(step)
    init_model = next((e.get("model") for e in events
                       if e.get("type") == "system" and e.get("subtype") == "init" and e.get("model")), None)
    primary = configured or init_model
    result = next((e for e in reversed(events) if e.get("type") == "result"), None)

    if result is not None:
        failed = bool(result.get("is_error")) or (result.get("subtype") not in (None, "success"))
        outcome = None
        if failed and map_outcome(ctx.outcomes.get(step)) == "success":
            outcome = "failed"
        per_model = result.get("modelUsage") or {}
        if per_model:
            rows = []
            # The configured model first, so turns and duration land on it.
            names = sorted(per_model, key=lambda m: (not _same_model(m, primary), m))
            for i, name in enumerate(names):
                mu = per_model[name] or {}
                tokens = {snake: _int(mu.get(camel)) for camel, snake in CAMEL_KEYS.items()}
                cost = mu.get("costUSD")
                rows.append(ctx.step_row(
                    step, name, tokens,
                    turns=_int(result.get("num_turns")) if i == 0 else None,
                    reported_cost_usd=float(cost) if cost is not None else None,
                    duration_ms=_int(result.get("duration_ms")) if i == 0 else None,
                    outcome=outcome,
                ))
            return rows
        cost = result.get("total_cost_usd")
        return [ctx.step_row(
            step, primary, _tokens(result.get("usage")),
            turns=_int(result.get("num_turns")),
            reported_cost_usd=float(cost) if cost is not None else None,
            duration_ms=_int(result.get("duration_ms")),
            outcome=outcome,
        )]

    # No result event: the step was killed mid-run. Every assistant message
    # still carries its own usage; a message split across several events
    # repeats the same usage, so keep one per message id.
    by_id: dict[str, tuple[str | None, dict]] = {}
    for i, e in enumerate(events):
        if e.get("type") != "assistant":
            continue
        msg = e.get("message") or {}
        usage = msg.get("usage")
        if not usage:
            continue
        by_id[msg.get("id") or f"anon-{i}"] = (msg.get("model") or primary, _tokens(usage))
    if not by_id:
        return []
    per_model: dict[str | None, dict] = {}
    for model, tokens in by_id.values():
        agg = per_model.setdefault(model, {k: 0 for k in TOKEN_KEYS})
        for k in TOKEN_KEYS:
            agg[k] += tokens[k]
    outcome = map_outcome(ctx.outcomes.get(step))
    if outcome == "success":
        # A clean exit always writes a result event; its absence means the
        # run did not end cleanly, whatever the step reported.
        outcome = "failed"
    return [ctx.step_row(step, model, tokens, outcome=outcome)
            for model, tokens in sorted(per_model.items(), key=lambda kv: (not _same_model(kv[0], primary), kv[0] or ""))]


def _same_model(a: str | None, b: str | None) -> bool:
    if not a or not b:
        return False
    strip = lambda m: m.split("[", 1)[0]
    return strip(a) == strip(b)


def rows_from_usage(ctx: Context, step: str, data: dict) -> list[dict]:
    usage = data.get("usage")
    if not isinstance(usage, dict):
        return []
    degraded = bool(data.get("error")) or data.get("type") == "error"
    return [ctx.step_row(step, data.get("model"), _tokens(usage), degraded=degraded)]


def collect(ctx: Context, sources: list[str]) -> list[dict]:
    rows: list[dict] = []
    for spec in sources:
        parts = spec.split(":", 2)
        if len(parts) != 3 or parts[0] not in SOURCE_KINDS or not parts[1] or not parts[2]:
            warn(f"ignoring malformed --source {spec!r} (want KIND:STEP:PATH, KIND in {SOURCE_KINDS})")
            continue
        kind, step, raw_path = parts
        path = Path(raw_path)
        if not path.is_file() or path.stat().st_size == 0:
            log(f"{step}: {path} absent; no rows")
            continue
        try:
            if kind == "exec":
                new = rows_from_exec(ctx, step, _read_stream(path))
            else:
                data = _load_json(path)
                if not isinstance(data, dict):
                    raise ValueError("top level is not an object")
                new = {"meta": rows_from_meta, "claims": rows_from_claims,
                       "usage": rows_from_usage}[kind](ctx, step, data)
        except (OSError, ValueError) as e:
            warn(f"{step}: could not read {path}: {e}")
            continue
        log(f"{step}: {len(new)} row(s) from {path}")
        rows.extend(new)
    return rows


def write_rows(rows: list[dict], ctx: Context, out_dir: Path, today: str | None = None) -> Path | None:
    if not rows:
        return None
    today = today or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    name = f"{ctx.run_id or 'local'}-{ctx.run_attempt}-{ctx.job or 'job'}.ndjson"
    path = out_dir / today / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n")
    return path


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--source", action="append", default=[], metavar="KIND:STEP:PATH")
    p.add_argument("--outcome", action="append", default=[], metavar="STEP=OUTCOME",
                   help="GitHub step outcome (success/failure/cancelled/skipped) or timeout")
    p.add_argument("--effort", action="append", default=[], metavar="STEP=EFFORT")
    p.add_argument("--model", action="append", default=[], metavar="STEP=MODEL",
                   help="configured model, for sources that don't name one")
    p.add_argument("--started-at", action="append", default=[], metavar="STEP=EPOCH")
    p.add_argument("--job-started-at", help="epoch seconds; started_at for steps without their own")
    p.add_argument("--job", help="default: $GITHUB_JOB")
    p.add_argument("--workflow", help="default: basename of $GITHUB_WORKFLOW_REF")
    p.add_argument("--repo", help="default: $GITHUB_REPOSITORY")
    p.add_argument("--run-id", help="default: $GITHUB_RUN_ID")
    p.add_argument("--run-attempt", help="default: $GITHUB_RUN_ATTEMPT")
    p.add_argument("--pr")
    p.add_argument("--head-sha")
    p.add_argument("--page-path")
    p.add_argument("--out-dir", default=DEFAULT_OUT_DIR)
    p.add_argument("--self-test", action="store_true")
    return p


def run(args) -> int:
    ctx = Context(args)
    rows = collect(ctx, args.source)
    path = write_rows(rows, ctx, Path(args.out_dir))
    if path is None:
        log("no usage rows; nothing written")
    else:
        n_step = sum(1 for r in rows if r["grain"] == "step")
        log(f"wrote {n_step} step row(s) and {len(rows) - n_step} claim row(s) → {path}")
    return 0


def main() -> int:
    args = build_parser().parse_args()
    if args.self_test:
        return self_test()
    try:
        return run(args)
    except Exception:  # noqa: BLE001 — telemetry must never fail the run
        warn("unexpected error; no usage rows written\n" + traceback.format_exc())
        return 0


# ---- self-test ------------------------------------------------------------


def self_test() -> int:
    failures = 0

    def check(name: str, cond: bool) -> None:
        nonlocal failures
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")
        if not cond:
            failures += 1

    def ctx_for(**kw) -> Context:
        argv = ["--job", "claude-review", "--workflow", "claude-code-review.yml",
                "--repo", "pulumi/docs", "--run-id", "42", "--run-attempt", "2",
                "--pr", "123", "--head-sha", "a" * 40]
        for k, vs in kw.items():
            for v in (vs if isinstance(vs, list) else [vs]):
                argv += [f"--{k.replace('_', '-')}", v]
        return Context(build_parser().parse_args(argv))

    usage = {"input_tokens": 100, "output_tokens": 20,
             "cache_read_input_tokens": 300, "cache_creation_input_tokens": 40}

    # meta source
    ctx = ctx_for(outcome="extract-atomic=success")
    rows = rows_from_meta(ctx, "extract-atomic", {"model": "claude-sonnet-5-5", "meta": usage, "errors": []})
    check("meta: one step row", len(rows) == 1 and rows[0]["grain"] == "step")
    check("meta: tokens copied", rows[0]["input_tokens"] == 100 and rows[0]["cache_read_input_tokens"] == 300)
    check("meta: join keys", rows[0]["run_id"] == 42 and rows[0]["run_attempt"] == 2 and rows[0]["pr"] == 123)
    check("meta: errors → degraded",
          rows_from_meta(ctx, "extract-atomic", {"model": "m", "meta": usage, "errors": ["x"]})[0]["outcome"] == "degraded")
    check("meta: ran=false → no row", rows_from_meta(ctx, "readthrough", {"ran": False, "meta": usage}) == [])
    check("outcome: failure → failed",
          rows_from_meta(ctx_for(outcome="readthrough=failure"), "readthrough", {"meta": usage})[0]["outcome"] == "failed")

    # claims source
    verified = {
        "model": "claude-opus-5-5",
        "verdicts": [
            {"claim_id": "c1", "type": "version", "entity_key": "version/pulumi-aws", "route": "pass1",
             "verdict": "verified", "confidence": "high", "file": "content/docs/x.md", "line_range": "L4",
             "model_usage": {**usage, "turns": 3}},
            {"claim_id": "c2", "type": "prose", "route": "pass0", "verdict": "not-a-claim",
             "model_usage": {k: 0 for k in TOKEN_KEYS} | {"turns": 0}},
            {"claim_id": "c3", "type": "numerical", "route": "pass3", "verdict": "unverifiable",
             "turn_cap_exhausted": True, "model_usage": {**usage, "turns": 8}},
        ],
        "errors": [],
        "meta": {k: 2 * v for k, v in usage.items()},
    }
    rows = rows_from_claims(ctx_for(effort="verify=medium"), "verify", verified)
    steps = [r for r in rows if r["grain"] == "step"]
    claims = [r for r in rows if r["grain"] == "claim"]
    check("claims: one step row + one row per verdict", len(steps) == 1 and len(claims) == 3)
    check("claims: step row sums turns", steps[0]["turns"] == 11 and steps[0]["effort"] == "medium")
    check("claims: step tokens = meta", steps[0]["input_tokens"] == 200)
    check("claims: claim row fields", claims[0]["claim_id"] == "c1" and claims[0]["entity_key"] == "version/pulumi-aws"
          and claims[0]["claim_type"] == "version" and claims[0]["route"] == "pass1" and claims[0]["turns"] == 3)
    check("claims: turn_cap_exhausted carried", claims[2]["turn_cap_exhausted"] is True and claims[0]["turn_cap_exhausted"] is False)
    check("claims: claim row model falls back to artifact model", claims[1]["model"] == "claude-opus-5-5")
    stub = dict(verified, meta={k: 0 for k in TOKEN_KEYS})
    check("claims: zero meta recomputed from verdicts",
          rows_from_claims(ctx, "verify", stub)[0]["output_tokens"] == 40)

    # exec source: result event with modelUsage
    events = [
        {"type": "system", "subtype": "init", "model": "claude-opus-5-5"},
        {"type": "assistant", "message": {"id": "m1", "model": "claude-opus-5-5", "usage": usage}},
        {"type": "result", "subtype": "success", "is_error": False, "num_turns": 17, "duration_ms": 300000,
         "total_cost_usd": 1.75, "usage": usage,
         "modelUsage": {
             "claude-haiku-5-5": {"inputTokens": 5, "outputTokens": 6, "cacheReadInputTokens": 7,
                                   "cacheCreationInputTokens": 8, "costUSD": 0.01},
             "claude-opus-5-5": {"inputTokens": 1000, "outputTokens": 200, "cacheReadInputTokens": 3000,
                                  "cacheCreationInputTokens": 400, "costUSD": 1.74},
         }},
    ]
    rows = rows_from_exec(ctx_for(outcome="compose=success"), "compose", events)
    check("exec: one row per model", [r["model"] for r in rows] == ["claude-opus-5-5", "claude-haiku-5-5"])
    check("exec: turns and duration on the primary model only",
          rows[0]["turns"] == 17 and rows[0]["duration_ms"] == 300000 and rows[1]["turns"] is None)
    check("exec: per-model reported cost", rows[0]["reported_cost_usd"] == 1.74 and rows[1]["reported_cost_usd"] == 0.01)
    check("exec: camelCase tokens mapped", rows[0]["cache_read_input_tokens"] == 3000 and rows[1]["input_tokens"] == 5)
    err_events = [dict(events[-1], is_error=True, subtype="error_max_turns")]
    check("exec: error result on a 'successful' step → failed",
          rows_from_exec(ctx_for(outcome="compose=success"), "compose", err_events)[0]["outcome"] == "failed")
    no_mu = [{"type": "result", "subtype": "success", "num_turns": 2, "total_cost_usd": 0.5, "usage": usage}]
    r = rows_from_exec(ctx_for(model="compose=claude-opus-5-5"), "compose", no_mu)
    check("exec: no modelUsage → one row from usage + configured model",
          len(r) == 1 and r[0]["model"] == "claude-opus-5-5" and r[0]["reported_cost_usd"] == 0.5)

    # exec source: killed mid-run (no result event)
    partial = [
        {"type": "system", "subtype": "init", "model": "claude-opus-5-5"},
        {"type": "assistant", "message": {"id": "m1", "model": "claude-opus-5-5", "usage": usage}},
        {"type": "assistant", "message": {"id": "m1", "model": "claude-opus-5-5", "usage": usage}},
        {"type": "assistant", "message": {"id": "m2", "model": "claude-opus-5-5", "usage": usage}},
        {"type": "assistant", "message": {"id": "s1", "model": "claude-sonnet-5-5", "usage": usage}},
    ]
    rows = rows_from_exec(ctx_for(outcome="compose=timeout"), "compose", partial)
    check("exec partial: summed per model, deduped by message id",
          [(r["model"], r["input_tokens"]) for r in rows] == [("claude-opus-5-5", 200), ("claude-sonnet-5-5", 100)])
    check("exec partial: outcome carried", all(r["outcome"] == "timeout" for r in rows))
    check("exec partial: a 'success' with no result is failed",
          rows_from_exec(ctx_for(outcome="compose=success"), "compose", partial)[0]["outcome"] == "failed")
    check("exec: empty log → no rows", rows_from_exec(ctx, "compose", []) == [])

    # usage source (triage Haiku response)
    resp = {"id": "msg_1", "type": "message", "model": "claude-haiku-5-5", "usage": usage}
    rows = rows_from_usage(ctx_for(effort="triage-prose=low"), "triage-prose", resp)
    check("usage: one row", len(rows) == 1 and rows[0]["model"] == "claude-haiku-5-5" and rows[0]["effort"] == "low")
    check("usage: API error has no usage → no row",
          rows_from_usage(ctx, "triage-prose", {"type": "error", "error": {"type": "overloaded_error"}}) == [])

    # end to end through files
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        (tdp / "llm1.json").write_text(json.dumps({"model": "claude-sonnet-5-5", "meta": usage}))
        (tdp / "verified.json").write_text(json.dumps(verified))
        (tdp / "exec.json").write_text(json.dumps(events))  # array form
        (tdp / "garbage.json").write_text("{not json")
        args = build_parser().parse_args([
            "--job", "claude-review", "--repo", "pulumi/docs", "--run-id", "7", "--run-attempt", "1",
            "--pr", "5", "--out-dir", str(tdp / "out"), "--job-started-at", "1760000000",
            "--source", f"meta:extract-atomic:{tdp / 'llm1.json'}",
            "--source", f"claims:verify:{tdp / 'verified.json'}",
            "--source", f"exec:compose:{tdp / 'exec.json'}",
            "--source", f"meta:readthrough:{tdp / 'missing.json'}",
            "--source", f"meta:broken:{tdp / 'garbage.json'}",
            "--source", "nonsense",
        ])
        ctx = Context(args)
        rows = collect(ctx, args.source)
        path = write_rows(rows, ctx, Path(args.out_dir), today="2026-10-13")
        lines = path.read_text().splitlines() if path else []
        check("e2e: file path is <date>/<run>-<attempt>-<job>.ndjson",
              path is not None and path.relative_to(tdp / "out").as_posix() == "2026-10-13/7-1-claude-review.ndjson")
        check("e2e: 1 + 4 + 2 rows, bad sources skipped", len(lines) == 7)
        parsed = [json.loads(line) for line in lines]
        check("e2e: every row has the schema version and join keys",
              all(r["schema_version"] == 1 and r["run_id"] == 7 and r["pr"] == 5 for r in parsed))
        check("e2e: started_at from job start", parsed[0]["started_at"] == "2025-10-09T08:53:20+00:00")
        empty = Context(build_parser().parse_args(["--job-started-at", "1760000000", "--started-at", "compose="]))
        check("e2e: an empty step start falls back to the job start",
              empty.step_row("compose", "m", {})["started_at"] == "2025-10-09T08:53:20+00:00")
        check("e2e: no rows → no file", write_rows([], ctx, tdp / "out2") is None)
        check("e2e: run() never raises on a bad source dir",
              run(build_parser().parse_args(["--out-dir", str(tdp / "out3"), "--source", "meta:x:/nonexistent"])) == 0)

    check("workflow_file parses GITHUB_WORKFLOW_REF",
          workflow_file("pulumi/docs/.github/workflows/claude-triage.yml@refs/pull/1/merge") == "claude-triage.yml")

    print(f"record-usage self-test: {'FAILED' if failures else 'passed'} ({failures} failure(s))")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
