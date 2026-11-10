#!/usr/bin/env python3
"""Ask the model to rank the weekly digest's "Needs a human" candidates.

The one judgment call in the digest: of this week's candidates (overdue
reviews, abandoned PRs, PRs merged over findings, keep-or-kill PRs, untriaged
issues), which five matter most, and why, in a few words. Everything else in
the message is rendered deterministically by render.py.

Never fatal. Any failure (no key, API error, thinking that eats the budget,
malformed output) writes `{}` and exits 0; render.py then uses its fixed
priority order and says so in the message. A bad week for the API must not
cost the team the digest.

Usage: rank.py <candidates.json> > ranking.json
Env:   ANTHROPIC_API_KEY
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

PROMPT = Path(__file__).resolve().parent / "rank-prompt.md"
API_URL = "https://api.anthropic.com/v1/messages"
# Sonnet 5.5: same price as Sonnet 5, and the request below (adaptive
# thinking, effort low, no sampling params, no prefill) is valid on it as-is.
MODEL = "claude-sonnet-5-5"
# Thinking tokens count against max_tokens. The output here is ~5 short
# lines, so the first budget is generous; one retry covers a run where
# adaptive thinking still exhausts it (seen on the old synthesis call).
BUDGETS = (8000, 16000)
TIMEOUT = 120


def call(prompt: str, budget: int, key: str) -> dict:
    body = json.dumps({
        "model": MODEL,
        "max_tokens": budget,
        "thinking": {"type": "adaptive"},
        "output_config": {"effort": "low"},
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")
    req = urllib.request.Request(API_URL, data=body, headers={
        "x-api-key": key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:  # noqa: S310 -- fixed https URL
        return json.loads(resp.read())


def parse_order(text: str) -> list[dict]:
    """The model's {"order": [...]} out of its text, tolerating code fences.
    Raises ValueError on anything that isn't that shape."""
    text = re.sub(r"^\s*```(?:json)?\s*|\s*```\s*$", "", text.strip())
    data = json.loads(text)
    order = data.get("order") if isinstance(data, dict) else None
    if not isinstance(order, list):
        raise ValueError("no `order` list in model output")
    return [{"ref": str(i.get("ref")), "why": str(i.get("why") or "")} for i in order if isinstance(i, dict)]


def rank(candidates: list[dict], key: str) -> dict:
    prompt = PROMPT.read_text() + "\n\n=== CANDIDATES (JSON) ===\n\n" + json.dumps(candidates, indent=1)
    for budget in BUDGETS:
        resp = call(prompt, budget, key)
        if resp.get("stop_reason") == "max_tokens":
            sys.stderr.write(f"::warning::ranking hit max_tokens at {budget}\n")
            continue
        text = "".join(b.get("text", "") for b in resp.get("content") or [] if b.get("type") == "text")
        return {"order": parse_order(text)}
    raise RuntimeError("ranking hit max_tokens on every budget")


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit("usage: rank.py <candidates.json>")
    candidates = json.loads(Path(sys.argv[1]).read_text())
    if not candidates:
        print(json.dumps({"order": []}))
        return 0
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        sys.stderr.write("::warning::ANTHROPIC_API_KEY unset; digest uses the fixed priority order\n")
        print("{}")
        return 0
    try:
        result = rank(candidates, key)
    except Exception as exc:  # noqa: BLE001 -- by contract nothing here may fail the job
        sys.stderr.write(f"::warning::ranking failed ({str(exc)[:300]}); digest uses the fixed priority order\n")
        print("{}")
        return 0
    print(json.dumps(result, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
