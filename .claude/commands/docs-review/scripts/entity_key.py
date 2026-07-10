#!/usr/bin/env python3
"""entity_key.py — deterministic entity keying for extracted claims.

Shared by `merge-claims.py` (stamps `entity_key` + `volatile` onto each merged
claim) and `scripts/content-review/reverify-claims.py` (groups the persisted
claims index by entity for nightly re-verification). One module so both sides
derive identical keys.

An entity key names the *subject* of a claim — the CLI flag, package, price,
or API surface it asserts something about — normalized so two pages asserting
facts about the same entity produce the same key. The claimed *value* (the
version number, the price figure) is deliberately excluded: the key must stay
stable when the value changes, or re-verification and contradiction detection
can't join across pages and time.

Key format: `<type>/<subject-slug>`, e.g.
    version/pulumi-gcp
    numerical/deployment-minutes-free-tier
    api-surface/aws-s3-bucket-versioning
    entity-spec/enterprise-plan-audit-logs

Only the four concrete, entity-shaped types are keyed — `version`,
`numerical`, `api-surface`, `entity-spec`. Everything else (behavior,
positioning, quote, ...) gets `entity_key: None`: those claims still persist
in the index but are invisible to entity-keyed consumers. A keyable claim
whose subject doesn't normalize to at least one significant token also gets
None — a missing key is always safe (the claim just isn't re-verified from
the index), a wrong key is not.

`volatile` marks the claim types worth cheap nightly re-verification straight
from the index — assertions whose truth drifts with the outside world even
when the page doesn't change: version pins, prices/rates/limits, and
pricing/limit-flavored entity specs.

No LLM involvement: derivation is pure text normalization, so keys are
reproducible from the claim record alone. Run the smoke checks with
`python3 entity_key.py --self-test`.
"""

from __future__ import annotations

import re
import sys

# Claim types that name a concrete entity we can key on. The soft/judgment
# types (behavior, feature, positioning, comparison, quote, attribution,
# temporal, cross-reference, url) are not keyed.
KEYED_TYPES = {"version", "numerical", "api-surface", "entity-spec"}

# Types whose truth drifts with the outside world; re-verified nightly from
# the index. `entity-spec` is volatile only in its pricing/limit flavor —
# "runners run in us-west-2" is stable, "feature Z is on the Enterprise plan"
# is not.
ALWAYS_VOLATILE_TYPES = {"version", "numerical"}
PRICING_LIMIT_RE = re.compile(
    r"\b(?:price|prices|pricing|priced|cost|costs|fee|fees|billed|billing|"
    r"per[- ](?:month|year|hour|minute|user|seat|resource|credit)|"
    r"tier|tiers|plan|plans|edition|editions|subscription|"
    r"limit|limits|limited|quota|quotas|cap|capped|maximum|minimum|"
    r"free|paid|enterprise|business[- ]critical)\b",
    re.IGNORECASE,
)

MAX_SUBJECT_TOKENS = 5

_STOPWORDS = {
    "the", "a", "an", "of", "to", "in", "on", "is", "are", "be", "and", "or",
    "for", "with", "that", "this", "it", "its", "by", "as", "at", "from",
    "was", "were", "has", "have", "had", "will", "can", "but", "not", "all",
    "any", "each", "per", "you", "your", "when", "which", "than", "then",
    "there", "their", "these", "those", "into", "onto", "also", "only",
    "more", "most", "least", "such", "may", "must", "should", "would",
    "does", "do", "did", "no", "new", "now", "up", "down", "requires",
    "required", "supports", "supported", "available", "takes", "take",
    "uses", "used", "using", "default", "defaults", "currently", "since",
    "version", "versions",  # "version" itself is the type, never the subject
}

# A version-like or purely numeric token is the claim's VALUE, not its
# subject — excluded so the key survives a value change. `v3.230`, `3.252.0`,
# `18+`, `40x`, `$75`, `99.9%`.
_VALUE_TOKEN_RE = re.compile(
    r"""^(?:
        v?\d+(?:\.\d+)*(?:-[\w.]+)?   # 3.252.0, v8.2, 1.21-rc1
        | \d+(?:\.\d+)?[x%+]?         # 40x, 99.9%, 18+
        | \$\d+(?:\.\d+)?[km]?        # $75, $1.5k
    )$""",
    re.IGNORECASE | re.VERBOSE,
)

_CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")
_WORD_RE = re.compile(r"[A-Za-z0-9$][\w.$+%-]*")


def _slug_token(raw: str) -> str:
    """Normalize one token into slug form: lowercase, inner punctuation → '-'."""
    t = raw.lower().strip(".,;:!?'\"()[]{}")
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t


def _subject_tokens(text: str) -> list[str]:
    """Ordered significant tokens of a claim's subject: stopwords, bare URLs,
    and value-shaped tokens (numbers, versions, prices) removed."""
    text = re.sub(r"https?://\S+", " ", text or "")
    out: list[str] = []
    seen: set[str] = set()
    for raw in _WORD_RE.findall(text):
        if _VALUE_TOKEN_RE.match(raw.strip(".,;:!?'\"()[]{}")):
            continue
        t = _slug_token(raw)
        if not t or len(t) < 2 or t.isdigit() or t in _STOPWORDS or t in seen:
            continue
        seen.add(t)
        out.append(t)
        if len(out) >= MAX_SUBJECT_TOKENS:
            break
    return out


def _code_subject(text: str) -> str | None:
    """The first backticked identifier that isn't a value — the strongest
    subject signal for api-surface claims (`--diff`, `aws.s3.Bucket`)."""
    for m in _CODE_SPAN_RE.finditer(text or ""):
        span = m.group(1).strip()
        # A multi-word span is a phrase, not an identifier.
        if not span or " " in span:
            continue
        if _VALUE_TOKEN_RE.match(span):
            continue
        t = _slug_token(span)
        if t and t not in _STOPWORDS:
            return t
    return None


def derive(claim: dict) -> tuple[str | None, bool]:
    """(entity_key, volatile) for one claim record.

    Reads `type`, `text`, and `source_hint`. Never raises: any shape it can't
    key returns (None, volatile-by-type).
    """
    ctype = str(claim.get("type") or "")
    text = str(claim.get("text") or "")
    hint = str(claim.get("source_hint") or "")

    volatile = ctype in ALWAYS_VOLATILE_TYPES or (
        ctype == "entity-spec" and bool(PRICING_LIMIT_RE.search(text))
    )

    if ctype not in KEYED_TYPES:
        return None, volatile

    tokens: list[str] = []
    if ctype == "api-surface":
        code = _code_subject(text) or _code_subject(hint)
        if code:
            tokens = [code]
    if not tokens and ctype == "version":
        # The pinned package/product: prefer the extractor's source_hint
        # ("pulumi-gcp"), fall back to the text's subject tokens.
        tokens = _subject_tokens(hint)[:2] or _subject_tokens(text)[:2]
    if not tokens:
        tokens = _subject_tokens(text)
        if not tokens:
            tokens = _subject_tokens(hint)

    if not tokens:
        return None, volatile
    return f"{ctype}/{'-'.join(tokens)}", volatile


def stamp(claim: dict) -> dict:
    """Mutate `claim` in place with `entity_key` and `volatile`; returns it."""
    key, volatile = derive(claim)
    claim["entity_key"] = key
    claim["volatile"] = volatile
    return claim


# ---- self-test ---------------------------------------------------------------


def self_test() -> int:
    failures: list[str] = []

    def check(name: str, cond: bool) -> None:
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    # Version pin: keyed on the package, not the version number; volatile.
    k, v = derive({"type": "version",
                   "text": "`pulumi-gcp` v8.2.0 is the current provider release.",
                   "source_hint": "pulumi-gcp"})
    check("version keyed on package", k == "version/pulumi-gcp")
    check("version is volatile", v is True)

    # Same entity, different pinned value -> same key (value excluded).
    k2, _ = derive({"type": "version",
                    "text": "`pulumi-gcp` v9.0.1 is the current provider release.",
                    "source_hint": "pulumi-gcp"})
    check("version key stable across value change", k2 == k)

    # Version with no hint falls back to text subject.
    k, _ = derive({"type": "version", "text": "Requires Node.js 18+."})
    check("version falls back to text subject", k == "version/node-js")

    # Numerical: subject tokens only, figure stripped; volatile.
    k, v = derive({"type": "numerical",
                   "text": "The Free tier includes 3,000 deployment minutes."})
    check("numerical keyed on subject", k is not None and k.startswith("numerical/"))
    check("numerical key has no figure", k is not None and "3" not in k)
    check("numerical is volatile", v is True)
    k2, _ = derive({"type": "numerical",
                    "text": "The Free tier includes 5,000 deployment minutes."})
    check("numerical key stable across value change", k2 == k)

    # api-surface: keyed on the backticked identifier.
    k, v = derive({"type": "api-surface",
                   "text": "The `aws.s3.Bucket` constructor takes a `versioning` argument.",
                   "source_hint": "pulumi-aws"})
    check("api-surface keyed on identifier", k == "api-surface/aws-s3-bucket")
    check("api-surface is not volatile", v is False)

    # entity-spec, pricing-flavored -> volatile; stable flavor -> not.
    k, v = derive({"type": "entity-spec",
                   "text": "Audit logs are available on the Enterprise plan."})
    check("pricing entity-spec keyed", k is not None and k.startswith("entity-spec/"))
    check("pricing entity-spec is volatile", v is True)
    _, v = derive({"type": "entity-spec",
                   "text": "Pulumi-hosted deployment runners run in AWS us-west-2."})
    check("hosting entity-spec is not volatile", v is False)

    # Non-keyed types: no key, not volatile.
    k, v = derive({"type": "behavior",
                   "text": "`pulumi up` deploys all resources in the stack."})
    check("behavior not keyed", k is None)
    check("behavior not volatile", v is False)

    # Unkeyable subject -> None, never a junk key.
    k, _ = derive({"type": "numerical", "text": "40x"})
    check("value-only text yields no key", k is None)

    # Missing/garbage fields never raise.
    k, v = derive({})
    check("empty claim yields (None, False)", k is None and v is False)

    # stamp() mutates in place.
    c = {"type": "version", "text": "requires Go 1.21", "source_hint": "go"}
    stamp(c)
    check("stamp sets both fields", c["entity_key"] == "version/go" and c["volatile"] is True)

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall entity_key self-tests passed")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    print(__doc__.split("\n\n")[0], file=sys.stderr)
    sys.exit(2)
