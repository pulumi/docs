#!/usr/bin/env python3
"""Phase 2 of /pr-review: the shared queue, its labels, and its published board.

    pr_queue.py labels  --in queue.json [--apply] [--changed-out FILE]
    pr_queue.py publish --in queue.json --board board.html [--out-dir DIR]
    pr_queue.py --self-test

`pr-queue.yml` runs collect.py (`--shared`) and analyze.py (`--owner any`)
on a schedule, exactly as the skill runs them on an approver's machine, and
then hands the analyzed queue.json to this script. Nothing here computes a
verdict or a collision: those are analyze.py's, and this file only maps
them onto two outputs that outlive the run.

**Labels** (`labels`). Every open PR in the queue carries exactly one verdict
label and, when a team owes it a decision, a route label per owning role:

  queue:stamp | queue:judge | queue:blocked       the shared verdict
  queue:route:<role>                             who decides (stamp/judge rows)
  queue:collides-with-#N                         wait for #N (Sentinel G6)

The shared board has no approver (`collect.py --shared`) and owns every
lane (`--owner any`), so analyze.py never computes `route` there: on a
board that belongs to everyone, nothing is someone else's lane. The route
label is therefore not a verdict but the question "whose decision is it":
on a stamp or judge row, each role in the row's `roles` (the routing
matrix plus the claims overlay, the same resolution the Sentinel's G3
reads). A blocked row carries none, because its next move is the author's
or a re-run's, not a team's.

`queue:collides-with-#N` is the one label the Sentinel reads. It goes on
the PR that should WAIT, never on both sides of a pair, because a label on
both would make each PR red until the other merged — a deadlock. Edges
come from analyze.py's facts:

  - an `overlap` pair (hunks touch on the base side; git's own conflict
    rule): the later PR in analyze.py's merge order waits on the earlier
    (fewest changed lines first, then PR number — `collision_clusters`);
  - a directional conflict (A adds links to an alias-only URL that B
    removes links to): A waits on B, since A is the one that will ship a
    link into whatever B is retiring.

Overlap edges follow one total order and so can never form a cycle. A
directional edge that would close one is dropped (deterministically, in
sorted order) and reported, so no set of labels can deadlock the queue. A
`same-file` pair is no label: it merges in either order.

The label writer touches `queue:*` labels and nothing else. It strips them
from an open PR that left the queue (converted to draft), leaves alone a
PR whose collect errored (its facts are unknown, so are its labels), and
leaves closed PRs as they are. It creates a label before applying it — a
missing label fails the whole `POST` — and deletes the repo's
`queue:collides-with-#N` definitions whose #N is no longer open, so the
label list does not grow one entry per PR forever. Without `--apply` it
prints the plan and writes nothing.

`--changed-out FILE` writes the PR numbers whose `queue:collides-with-*`
set changed, one per line: labels written with the workflow's
GITHUB_TOKEN fire no `labeled` event, so the workflow dispatches the
Sentinel for exactly those PRs instead.

**Publish** (`publish`). Writes `queue.json` and `board.html` locally
(`.pr-review-queue-publish/`, ALWAYS, so the workflow artifact never
depends on S3), then, when `PR_REVIEW_EVIDENCE_URI` is set, uploads them
to `<uri>/queue/queue.json`, `<uri>/queue/board.html` and an immutable
`<uri>/queue/runs/<date>/<ts>.json` — the record the issue asks for when it
says phase 1 is the measurement: what the queue said, hour by hour, to
compare against what approvers did. Same degradation contract as
record-evidence.py: URI unset ⇒ local files plus `::warning::`, never a
failure; an upload failure warns and continues.

Deterministic, no model calls (scripts/review-v3 contract). The judge step
stays out of CI: judge rows publish unjudged, and the skill judges on
demand.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import sentinel  # noqa: E402  (COLLIDES_LABEL_PREFIX: the one label the Sentinel reads)
from gh_client import GhClient, GhError  # noqa: E402

LABEL_PREFIX = "queue:"
ROUTE_PREFIX = "queue:route:"
COLLIDES_PREFIX = sentinel.COLLIDES_LABEL_PREFIX  # "queue:collides-with-#"
VERDICT_LABELS = {"stamp": "queue:stamp", "judge": "queue:judge", "blocked": "queue:blocked"}
# Verdicts whose next move is a team's decision, so they carry route labels.
ROUTED_VERDICTS = ("stamp", "judge")
DEFAULT_OUT_DIR = ".pr-review-queue-publish"
_COLLIDES_RE = re.compile(r"^" + re.escape(COLLIDES_PREFIX) + r"(\d+)$")

# name -> (color, description). Route and collides labels are families; the
# entry for each is keyed by its prefix.
LABEL_STYLE = {
    "queue:stamp": ("0e8a16", "Shared /pr-review queue: every stamp gate passes; approving asserts nothing beyond CI"),
    "queue:judge": ("fbca04", "Shared /pr-review queue: decidable from the board, needs a human's call"),
    "queue:blocked": ("b60205", "Shared /pr-review queue: can't merge yet (findings, conflict, red CI, stale review)"),
    ROUTE_PREFIX: ("c5def5", "Shared /pr-review queue: this team owes the decision"),
    COLLIDES_PREFIX: ("d93f0b", "Shared /pr-review queue: overlaps an open PR that merges first (Sentinel G6)"),
}


def log(msg: str) -> None:
    print(f"pr-queue: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::pr-queue: {msg}", file=sys.stderr)


def label_style(name: str) -> tuple[str, str]:
    if name in LABEL_STYLE:
        return LABEL_STYLE[name]
    for prefix in (ROUTE_PREFIX, COLLIDES_PREFIX):
        if name.startswith(prefix):
            color, desc = LABEL_STYLE[prefix]
            if prefix == COLLIDES_PREFIX:
                desc = f"Shared /pr-review queue: overlaps open #{name[len(prefix):]}, which merges first (Sentinel G6)"
            return color, desc
    return "ededed", "Shared /pr-review queue"


def collides_target(label: str) -> int | None:
    m = _COLLIDES_RE.match(label or "")
    return int(m.group(1)) if m else None


# ---- collisions → wait edges -----------------------------------------------


def _order_key(pr: dict | None, n: int) -> tuple[int, int]:
    """analyze.collision_clusters' merge order: fewest changed lines first,
    then PR number. Used per pair, not per cluster, because analyze.py
    narrows a cluster's `merge_order` to the approver's own rows."""
    return ((pr or {}).get("changed_lines") or 0, n)


def _reaches(edges: dict[int, set[int]], start: int, goal: int) -> bool:
    seen, stack = set(), [start]
    while stack:
        x = stack.pop()
        if x == goal:
            return True
        if x in seen:
            continue
        seen.add(x)
        stack.extend(edges.get(x, ()))
    return False


def wait_edges(queue: dict) -> tuple[dict[int, set[int]], list[dict]]:
    """waiter -> {PRs it waits on}, plus the directional edges dropped to
    keep the graph acyclic. Only PRs present in the queue take part."""
    by = {p["number"]: p for p in queue.get("prs") or []}
    edges: dict[int, set[int]] = {}
    for c in queue.get("clusters") or []:
        for pair in c.get("pairs") or []:
            if pair.get("kind") != "overlap":
                continue
            a, b = pair["a"], pair["b"]
            if a not in by or b not in by:
                continue
            first, later = sorted((a, b), key=lambda n: _order_key(by.get(n), n))
            edges.setdefault(later, set()).add(first)
    dropped = []
    seen_pairs = set()
    for d in sorted(queue.get("directional") or [], key=lambda d: (d["adds_links_pr"], d["removes_links_pr"], d["path"])):
        waiter, blocker = d["adds_links_pr"], d["removes_links_pr"]
        if waiter not in by or blocker not in by or (waiter, blocker) in seen_pairs:
            continue
        seen_pairs.add((waiter, blocker))
        if blocker in edges.get(waiter, set()):
            continue
        if _reaches(edges, blocker, waiter):
            dropped.append({"waiter": waiter, "blocker": blocker, "path": d["path"], "why": "would close a wait cycle"})
            continue
        edges.setdefault(waiter, set()).add(blocker)
    return edges, dropped


# ---- desired labels ----------------------------------------------------------


def desired_labels(queue: dict) -> dict[int, set[str]]:
    """The full `queue:*` label set each PR in the queue should wear."""
    edges, _ = wait_edges(queue)
    out: dict[int, set[str]] = {}
    for pr in queue.get("prs") or []:
        n = pr["number"]
        want: set[str] = set()
        verdict = pr.get("verdict")
        if verdict in VERDICT_LABELS:
            want.add(VERDICT_LABELS[verdict])
        if verdict in ROUTED_VERDICTS:
            want |= {f"{ROUTE_PREFIX}{r}" for r in pr.get("roles") or [] if r and r != "none"}
        want |= {f"{COLLIDES_PREFIX}{m}" for m in edges.get(n, ())}
        out[n] = want
    return out


def label_plan(queue: dict, open_prs: list[dict]) -> list[dict]:
    """One entry per open PR whose `queue:*` labels must change:
    {"pr", "add", "remove", "collides_changed"}. `open_prs` is the live
    listing (number + labels), read fresh, so the plan diffs against what
    the PR wears now rather than what it wore at collect time."""
    want = desired_labels(queue)
    errored = {e.get("pr") for e in queue.get("errors") or []}
    plan = []
    for pr in sorted(open_prs, key=lambda p: p["number"]):
        n = pr["number"]
        if n in errored:
            continue
        have = {l.get("name") if isinstance(l, dict) else l for l in pr.get("labels") or []}
        have = {l for l in have if l and l.startswith(LABEL_PREFIX)}
        target = want.get(n, set())  # not in the queue (draft) ⇒ no queue labels
        add, remove = sorted(target - have), sorted(have - target)
        if add or remove:
            changed = any(l.startswith(COLLIDES_PREFIX) for l in add + remove)
            plan.append({"pr": n, "add": add, "remove": remove, "collides_changed": changed})
    return plan


# ---- applying ----------------------------------------------------------------


def _label_path(repo: str, name: str) -> str:
    return f"repos/{repo}/labels/{urllib.parse.quote(name, safe='')}"


def ensure_labels(gh, names: set[str], existing: set[str], *, apply: bool) -> list[str]:
    created = []
    for name in sorted(names - existing):
        color, desc = label_style(name)
        if apply:
            gh.post(f"repos/{gh.repo}/labels", {"name": name, "color": color, "description": desc[:100]})
        created.append(name)
    return created


def apply_plan(gh, plan: list[dict], *, apply: bool) -> dict:
    """Create missing labels, then add/remove per PR. Failures on one PR are
    reported and the rest continue; labels are re-derived every run, so a
    missed write heals on the next one."""
    existing = {l.get("name") for l in gh.get(f"repos/{gh.repo}/labels", paginate=True) or []}
    needed = {l for step in plan for l in step["add"]}
    result = {"created": [], "applied": [], "failed": [], "pruned": []}
    try:
        result["created"] = ensure_labels(gh, needed, existing, apply=apply)
    except GhError as exc:
        warn(f"could not create labels: {exc}")
        result["failed"].append({"pr": None, "error": str(exc)})
        return result
    for step in plan:
        n = step["pr"]
        try:
            if apply and step["add"]:
                gh.post(f"repos/{gh.repo}/issues/{n}/labels", {"labels": step["add"]})
            for name in step["remove"]:
                if apply:
                    gh.delete(f"repos/{gh.repo}/issues/{n}/labels/{urllib.parse.quote(name, safe='')}")
            result["applied"].append(step)
        except GhError as exc:
            warn(f"#{n}: label write failed: {exc}")
            result["failed"].append({"pr": n, "error": str(exc)})
    open_numbers = {p for p in (step["pr"] for step in plan)} | set(gh_open_numbers(gh))
    for name in sorted(existing | set(result["created"])):
        target = collides_target(name)
        if target is not None and target not in open_numbers:
            try:
                if apply:
                    gh.delete(_label_path(gh.repo, name))
                result["pruned"].append(name)
            except GhError as exc:
                warn(f"could not delete stale label {name}: {exc}")
    return result


def gh_open_numbers(gh) -> list[int]:
    cached = getattr(gh, "_pr_queue_open", None)
    if cached is not None:
        return [p["number"] for p in cached]
    return [p["number"] for p in gh.list_open_prs() or []]


# ---- publishing --------------------------------------------------------------


def _s3_put(local: Path, uri: str, content_type: str) -> None:
    subprocess.run(["aws", "s3", "cp", str(local), uri, "--content-type", content_type],
                   check=True, capture_output=True, text=True)


def publish(queue_path: Path, board_path: Path | None, *, out_dir: Path, uri: str | None,
            now: datetime | None = None, uploader=_s3_put) -> dict:
    now = now or datetime.now(timezone.utc)
    out_dir.mkdir(parents=True, exist_ok=True)
    queue_text = queue_path.read_text()
    json.loads(queue_text)  # a corrupt queue must not land anywhere
    local = {"queue.json": out_dir / "queue.json"}
    local["queue.json"].write_text(queue_text)
    if board_path and board_path.exists():
        local["board.html"] = out_dir / "board.html"
        local["board.html"].write_text(board_path.read_text())
    result = {"local": {k: str(v) for k, v in local.items()}, "uploaded": [], "failed": []}
    if not uri:
        warn("PR_REVIEW_EVIDENCE_URI is unset; the queue is published as local files (the workflow artifact) only")
        return result
    base = uri.rstrip("/") + "/queue"
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    targets = [(local["queue.json"], f"{base}/queue.json", "application/json"),
               (local["queue.json"], f"{base}/runs/{now.strftime('%Y-%m-%d')}/{stamp}.json", "application/json")]
    if "board.html" in local:
        targets.append((local["board.html"], f"{base}/board.html", "text/html; charset=utf-8"))
    for path, dest, ctype in targets:
        try:
            uploader(path, dest, ctype)
            result["uploaded"].append(dest)
        except Exception as exc:  # noqa: BLE001 — best-effort, the artifact is the fallback
            warn(f"upload to {dest} failed: {exc}")
            result["failed"].append(dest)
    return result


# ---- CLI ---------------------------------------------------------------------


def _print_plan(plan: list[dict], dropped: list[dict], apply: bool) -> None:
    verb = "applying" if apply else "would apply (dry run; pass --apply to write)"
    log(f"{verb}: {len(plan)} PR(s) with label changes")
    for step in plan:
        bits = [f"+{l}" for l in step["add"]] + [f"-{l}" for l in step["remove"]]
        log(f"  #{step['pr']}: {' '.join(bits)}")
    for d in dropped:
        log(f"  directional #{d['waiter']} → #{d['blocker']} ({d['path']}) not labelled: {d['why']}")


def cmd_labels(args) -> int:
    queue = json.loads(Path(args.inp).read_text())
    gh = GhClient(args.repo or queue.get("repo") or "pulumi/docs", args.backend, snapshot_dir=args.snapshot_dir)
    open_prs = gh.list_open_prs() or []
    gh._pr_queue_open = open_prs
    plan = label_plan(queue, open_prs)
    _, dropped = wait_edges(queue)
    _print_plan(plan, dropped, args.apply)
    result = apply_plan(gh, plan, apply=args.apply)
    if result["pruned"]:
        log(f"{'deleted' if args.apply else 'would delete'} stale label(s): {', '.join(result['pruned'])}")
    if args.changed_out:
        changed = [str(s["pr"]) for s in result["applied"] if s["collides_changed"]] if args.apply else []
        Path(args.changed_out).write_text("".join(f"{n}\n" for n in changed))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps({"apply": args.apply, "plan": plan, "dropped": dropped, **result},
                                                     indent=1, sort_keys=True) + "\n")
    return 0


def cmd_publish(args) -> int:
    result = publish(Path(args.inp), Path(args.board) if args.board else None, out_dir=Path(args.out_dir),
                     uri=os.environ.get("PR_REVIEW_EVIDENCE_URI") or None)
    for dest in result["uploaded"]:
        log(f"uploaded {dest}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--self-test", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    lp = sub.add_parser("labels", help="stamp queue:* labels from an analyzed queue.json")
    lp.add_argument("--in", dest="inp", required=True)
    lp.add_argument("--repo")
    lp.add_argument("--apply", action="store_true", help="write; without it, print the plan only")
    lp.add_argument("--changed-out", help="write PR numbers whose collides-with labels changed")
    lp.add_argument("--summary-out", help="write the plan and its result as JSON")
    lp.add_argument("--backend", default="auto", choices=("auto", "gh", "rest", "snapshot"))
    lp.add_argument("--snapshot-dir")
    pp = sub.add_parser("publish", help="write queue.json + board.html locally and to the evidence bucket")
    pp.add_argument("--in", dest="inp", required=True)
    pp.add_argument("--board")
    pp.add_argument("--out-dir", default=DEFAULT_OUT_DIR)
    return ap


def main(argv: list[str] | None = None) -> int:
    ap = build_parser()
    args = ap.parse_args(argv)
    if args.self_test:
        import test_pr_queue  # noqa: PLC0415 — the pytest file doubles as the harness
        return test_pr_queue.run_standalone()
    if args.cmd == "labels":
        return cmd_labels(args)
    if args.cmd == "publish":
        return cmd_publish(args)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
