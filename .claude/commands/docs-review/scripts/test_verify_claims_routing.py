"""Tests for verify-claims.py URL routing — the target-alignment rule.

A URL in the claim text takes absolute precedence over source_hint: a
mispaired hint (pointing at a neighboring link's page) must never route a
claim to pass2 against the wrong pre-fetched page. Regression fixtures are
drawn from the 2026-07 ledger re-adjudication's wrong-target false positives.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "verify_claims", Path(__file__).parent / "verify-claims.py")
vc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(vc)


CONFIGURE = "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html"
INSTALL = "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html"


def fetched(*urls):
    return {vc._normalize_url(u): {"url": u, "status": 200, "body": "x"} for u in urls}


def test_text_url_wins_over_conflicting_hint():
    # docs-iac-get-started-aws-configure c4: hint pointed at the adjacent
    # install link; the claim cites the configure page.
    claim = {"text": f"The AWS CLI can be configured using the instructions at {CONFIGURE}.",
             "source_hint": INSTALL}
    # Raw candidates may keep sentence-final punctuation; compare normalized.
    assert [vc._normalize_url(u) for u in vc._claim_urls(claim)] == [vc._normalize_url(CONFIGURE)]


def test_conflicting_hint_does_not_reach_pass2():
    # Only the WRONG page is pre-fetched: the claim must not route to pass2
    # against it — pass3 fetches the right page instead.
    claim = {"text": f"The AWS CLI can be configured using the instructions at {CONFIGURE}.",
             "source_hint": INSTALL, "type": "url"}
    assert vc.route_claim(claim, fetched(INSTALL)) == "pass3"
    assert vc.find_fetched_url(claim, fetched(INSTALL)) is None


def test_text_url_routes_pass2_when_prefetched():
    claim = {"text": f"Configure the AWS CLI: {CONFIGURE}", "source_hint": INSTALL}
    assert vc.route_claim(claim, fetched(CONFIGURE, INSTALL)) == "pass2"
    assert vc.find_fetched_url(claim, fetched(CONFIGURE, INSTALL))["url"] == CONFIGURE


def test_hint_used_when_text_has_no_url():
    claim = {"text": "Retries default to 3 attempts per the AWS Lambda docs.",
             "source_hint": INSTALL}
    assert vc._claim_urls(claim) == [INSTALL]
    assert vc.route_claim(claim, fetched(INSTALL)) == "pass2"


def test_no_urls_at_all():
    claim = {"text": "Encryption is enabled by default.", "source_hint": "AWS docs"}
    assert vc._claim_urls(claim) == []
    assert vc.find_fetched_url(claim, fetched(INSTALL)) is None
