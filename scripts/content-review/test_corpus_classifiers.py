#!/usr/bin/env python3
"""Run the content-review classifiers against a REAL sample of the claims index.

Every other test in this tree feeds the classifiers strings someone invented.
That is how three separate changes shipped inert and nobody noticed for weeks:

  * entity_key.py's self-describing exclusion (#20851) matched 0 of 53 volatile
    entities for a month. Its unit tests passed the whole time — they asserted
    on hand-written sentences that happened to hit the pattern, while every
    real claim missed it.
  * the `vars.X != '0'` job gate, where an unset variable coerced to 0 and
    inverted the documented default, keeping whole lanes dark.
  * `upload-artifact` silently uploading nothing, because the report is a
    dotfile and hidden files are excluded by default.

All three passed their tests and did nothing. The shared shape is a component
that is *exercised* but never *measured against production data*, so this file
asserts on DISTRIBUTIONS over a checked-in sample of the live index rather than
on individual verdicts.

The assertions are deliberately loose bands, not exact numbers: the sample is
refreshed periodically and a brittle equality would just get bumped until it
stopped meaning anything. A band catches the failure mode that actually
happens — a classifier that collapses to all-yes or all-no.

REGENERATING THE SAMPLE (needs AWS creds for the ledger bucket):

    aws s3 sync s3://content-review-ledger-e8e6737/claims/ /tmp/claims/ --quiet
    python3 - /tmp/claims <<'EOF'
    import sys, json, pathlib
    src = pathlib.Path(sys.argv[1])
    out = pathlib.Path("scripts/content-review/testdata/claims-sample.json")
    snaps = [json.loads(f.read_text()) for f in sorted(src.glob("*.json"))]
    snaps.sort(key=lambda s: s["slug"])
    keep = [{"path": s["path"], "slug": s["slug"], "reviewed_at": s.get("reviewed_at"),
             "claims": [{k: c.get(k) for k in
                         ("type", "text", "verdict", "entity_key", "volatile", "source_hint")}
                        for c in (s.get("claims") or [])]}
            for i, s in enumerate(snaps) if i % 3 == 0]
    out.write_text(json.dumps({"note": "deterministic sample of the live claims index; "
                                       "regenerate with the header comment's command",
                               "sampled_at": "YYYY-MM-DD", "pages": keep}, indent=1) + "\\n")
    EOF

Run: python3 scripts/content-review/test_corpus_classifiers.py
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
SAMPLE = HERE / "testdata" / "claims-sample.json"

_passes = 0
_failures: list[str] = []


def check(ok: bool, label: str) -> None:
    global _passes
    if ok:
        _passes += 1
        print(f"  ok: {label}")
    else:
        _failures.append(label)
        print(f"  FAIL: {label}")


def band(value: float, lo: float, hi: float, label: str) -> None:
    check(lo <= value <= hi, f"{label} = {value:.1%} (expected {lo:.0%}-{hi:.0%})")


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    if not SAMPLE.is_file():
        print(f"missing sample: {SAMPLE}", file=sys.stderr)
        return 1
    sample = json.loads(SAMPLE.read_text())
    pages = sample["pages"]
    claims = [c for p in pages for c in p["claims"]]
    print(f"corpus sample: {len(pages)} pages, {len(claims)} claims "
          f"(sampled {sample.get('sampled_at')})\n")

    ek = load("entity_key", REPO / ".claude/commands/docs-review/scripts/entity_key.py")
    rv = load("reverify_claims", HERE / "reverify-claims.py")

    # --- volatility: the nightly lane's whole input ---------------------------
    print("volatility classifier")
    volatile = [c for c in claims if ek.is_volatile(c)]
    check(len(volatile) > 0, "some claims are volatile (a lane with no input is a dead lane)")
    band(len(volatile) / len(claims), 0.005, 0.20,
         "volatile share of all claims")

    # --- the self-describing exclusion: the one that shipped inert ------------
    print("\nself-describing exclusion (#20851)")
    numerical = [c for c in claims if c.get("type") == "numerical"]
    check(len(numerical) > 0, "the sample contains numerical claims to exclude from")
    excluded = [c for c in numerical
                if ek.SELF_DESCRIBING_RE.search(c.get("text") or "")
                and not ek.PRICING_LIMIT_RE.search(c.get("text") or "")]
    # THE regression test. This was 0 for a month while its unit tests passed.
    check(len(excluded) > 0,
          "the exclusion excludes SOMETHING real (0 here is the #20851 bug)")
    band(len(excluded) / len(numerical), 0.01, 0.60,
         "numerical claims excluded as self-describing")

    # The CLI's "plans to create N resources" must not read as a pricing plan.
    check(ek.PRICING_LIMIT_RE.search("`pulumi up` plans to create 2 resources") is None,
          "the verb 'plans to' is not a pricing veto")

    # --- entity keying --------------------------------------------------------
    print("\nentity keying")
    keyed = [c for c in claims if ek.derive(c)[0]]
    band(len(keyed) / len(claims), 0.10, 0.80, "claims that derive an entity key")
    keyable = [c for c in claims if c.get("type") in ek.KEYED_TYPES]
    unkeyed = [c for c in keyable if not ek.derive(c)[0]]
    band(len(unkeyed) / max(len(keyable), 1), 0.0, 0.35,
         "keyable claims that fail to produce a key")

    # A key must not embed the value it describes, or re-verification can never
    # join the same entity across a version bump.
    digits = [k for k in (ek.derive(c)[0] for c in claims)
              if k and k.startswith("version/") and any(ch.isdigit() for ch in k)]
    band(len(digits) / max(len([c for c in claims if c.get("type") == "version"]), 1),
         0.0, 0.50, "version keys containing a digit")

    # --- fix routing: which findings can be acted on here ---------------------
    print("\nfix routing (local / generated / missing)")
    rules = rv.load_tier_rules(
        REPO / ".claude/commands/review-existing-content/references/strategic-tiers.yaml")
    check(len(rules) > 0, "strategic-tiers.yaml loads")
    routes = {}
    for p in pages:
        routes[p["path"]] = rv.fix_route([{"path": p["path"]}], REPO, rules)
    counts = {r: sum(1 for v in routes.values() if v == r)
              for r in ("local", "generated", "missing")}
    print(f"  routes: {counts}")
    check(counts["local"] > 0, "some pages route local (else nothing is ever fixable)")
    # Not asserting generated>0: a sample may legitimately contain none, and a
    # false failure here would train people to ignore this file.
    band(counts["local"] / len(pages), 0.30, 1.0, "pages that route local")

    # --- claim types ----------------------------------------------------------
    print("\nclaim type distribution")
    types = {}
    for c in claims:
        types[c.get("type")] = types.get(c.get("type"), 0) + 1
    check(len(types) >= 5, f"the extractor produces varied claim types ({len(types)} seen)")
    top = max(types.values()) / len(claims)
    band(top, 0.0, 0.75, "share held by the single most common claim type")

    print(f"\n{_passes} passed, {len(_failures)} failed")
    if _failures:
        print("\nA band failure usually means a classifier changed behavior against real\n"
              "data — check the diff before widening the band.", file=sys.stderr)
    return 1 if _failures else 0


if __name__ == "__main__":
    sys.exit(main())
