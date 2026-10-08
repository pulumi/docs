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


# --- version claims: the hint names a package, not an external authority ---
#
# claim-extraction.md tells the extractor to put "the package/product" in
# `source_hint` for a version claim; route_claim read any non-URL hint as "a
# named external source" and web-searched it. For a Pulumi package whose name
# has no pulumi-shaped token, the top web hit is pulumi.com's own page — PR
# #21720's pin bump came back `contradicted` against the page under review.

PR21720_TEXT = ("The example Pulumi YAML pins the `terraform-provider` package version to 1.4.0, "
                "described as 'Version of the terraform-provider package'.")


def test_version_claim_with_bare_package_hint_routes_pass1():
    claim = {"text": PR21720_TEXT, "type": "version", "source_hint": "terraform-provider"}
    assert vc.route_claim(claim, {}) == "pass1"
    for hint in ("command", "docker-build", "hashicorp/random", "Node.js"):
        assert vc.route_claim({"text": "The example pins it to 1.4.0.", "type": "version",
                               "source_hint": hint}, {}) == "pass1"


def test_version_claim_with_repo_hint_routes_pass1():
    claim = {"text": PR21720_TEXT, "type": "version", "source_hint": "pulumi/pulumi-terraform-provider"}
    assert vc.route_claim(claim, {}) == "pass1"


def test_version_claim_urls_still_route_by_url():
    text = "Requires Node.js 18+ per https://nodejs.org/en/about/previous-releases."
    claim = {"text": text, "type": "version", "source_hint": "Node.js"}
    assert vc.route_claim(claim, {}) == "pass3"
    assert vc.route_claim(claim, fetched("https://nodejs.org/en/about/previous-releases")) == "pass2"


def test_non_version_claim_with_named_external_source_still_routes_pass3():
    for ctype in ("attribution", "numerical", "behavior", "quote"):
        claim = {"text": "Retries default to 3 attempts.", "type": ctype, "source_hint": "AWS Lambda docs"}
        assert vc.route_claim(claim, {}) == "pass3"
    # Same text and hint as the #21720 claim, different type: the carve-out is
    # keyed on `version`, not on the hint.
    assert vc.route_claim({"text": PR21720_TEXT, "type": "behavior",
                           "source_hint": "terraform-provider"}, {}) == "pass3"
