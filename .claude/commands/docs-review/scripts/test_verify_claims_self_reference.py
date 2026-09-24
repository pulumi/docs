"""Tests for the self-reference and same-site-only source-discipline gates.

A ledger audit of 117 PR reviews found 66 `contradicted` verdicts; 9 cited the
live published copy of the file under review and 9 more rested on other
pulumi.com pages alone. The live copy shows the pre-change text, so it
"contradicts" every value a PR changes. The shape is not pure noise, though: it
fired falsely on intentional refreshes (#21720, #21394, #21509) and correctly
on two bot rewrites that weakened a true fact (#21552, #21602). The gate
therefore re-verifies rather than downgrades: one more pass1 hop, told the live
page is not evidence either way; an independently sourced answer stands, and
only an unsettled re-check becomes `unverifiable`.

`testdata/self-reference-verdicts.json` holds the real verdict records from
those PRs, keyed by PR number.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

HERE = Path(__file__).parent
SPEC = importlib.util.spec_from_file_location("verify_claims", HERE / "verify-claims.py")
vc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(vc)

REPO_ROOT = HERE.resolve().parents[3]
LEDGER = json.loads((HERE / "testdata" / "self-reference-verdicts.json").read_text())


def ledger_claim(pr: str, i: int = 0, **extra) -> dict:
    v = LEDGER[pr][i]
    return {"__id": f"pr{pr}-{i}", "file": v["file"], "line_range": f"L{v['line']}",
            "text": v["claim"], "type": "version", **extra}


def verify_block(verdict, evidence, source, confidence="high", **extra):
    return [{"type": "tool_use", "id": "t1", "name": "verify_claim",
             "input": {"verdict": verdict, "confidence": confidence,
                       "evidence": evidence, "source": source, **extra}}]


def ledger_block(pr: str, i: int = 0):
    v = LEDGER[pr][i]
    return verify_block(v["verdict"], v["evidence"], v["source"])


@pytest.fixture
def api(monkeypatch):
    """Stub the single network seam. `script` maps a lane to the content blocks
    served on successive calls to it (last entry repeats); the lane is read off
    the request's tools, as in test_framing_drift.py."""
    state = {"script": {}, "order": [], "bodies": []}

    def fake(api_key, body):
        names = {t.get("name") for t in body.get("tools", [])}
        lane = "pass1" if "gh_query" in names else "pass3" if "web_search" in names else "pass2"
        seq = state["script"][lane]
        i = min(state["order"].count(lane), len(seq) - 1)
        state["order"].append(lane)
        state["bodies"].append(body)
        return {"content": seq[i],
                "usage": {"input_tokens": 100, "output_tokens": 10,
                          "cache_read_input_tokens": 7, "cache_creation_input_tokens": 3}}

    monkeypatch.setattr(vc, "_post_messages", fake)
    return state


def user_text(body) -> str:
    return body["messages"][0]["content"]


# ---- content path → site path ------------------------------------------------


@pytest.mark.parametrize("file_path, expected", [
    ("content/docs/iac/concepts/providers/any-terraform-provider.md",
     "/docs/iac/concepts/providers/any-terraform-provider/"),
    ("content/docs/iac/languages-sdks/javascript/_index.md", "/docs/iac/languages-sdks/javascript/"),
    ("content/blog/some-post/index.md", "/blog/some-post/"),
    ("./content/docs/Mixed-Case.md", "/docs/mixed-case/"),
    ("content/_index.md", "/"),
    ("data/pulumi_pricing.yaml", None),
    ("static/programs/aws-s3-typescript/index.ts", None),
    ("content/docs/iac/diagram.png", None),
    ("", None),
])
def test_content_path_to_site_path(file_path, expected):
    assert vc.content_path_to_site_path(file_path) == expected


# ---- the pure predicate ------------------------------------------------------

ATP = "content/docs/iac/concepts/providers/any-terraform-provider.md"
ATP_URL = "https://www.pulumi.com/docs/iac/concepts/providers/any-terraform-provider/"


def shape(source, file_path=ATP, text="The pin is 1.4.0.", **claim):
    return vc.source_discipline_shape({"file": file_path, "text": text, **claim}, source)


@pytest.mark.parametrize("source", [
    ATP_URL,
    ATP_URL.rstrip("/"),
    ATP_URL.replace("https://www.", "http://"),
    ATP_URL.upper().replace("HTTPS://WWW.PULUMI.COM", "https://www.pulumi.com"),
    ATP_URL + "#specifying-a-version",
    ATP_URL + "?utm=x#y",
    f"live page: {ATP_URL}.",
    f"https://www.pulumi.com/docs/iac/get-started/ and {ATP_URL}",
    f"https://www.pulumi.com/docs/iac/get-started/; {ATP_URL}",
    f"https://www.pulumi.com/docs/iac/get-started/, {ATP_URL}",
    f"{ATP_URL} vs https://www.pulumi.com/docs/iac/get-started/",
    f"WebSearch ran query \"terraform-provider version\"; {ATP_URL}",
    f"repo:{ATP} and {ATP_URL}",     # the reviewed file itself is not a second source
])
def test_self_reference_sources(source):
    assert shape(source) == "self-reference"


@pytest.mark.parametrize("source", [
    "https://www.pulumi.com/docs/iac/get-started/",
    "https://pulumi.com/pricing/ and https://www.pulumi.com/docs/iac/concepts/stacks/",
    "https://www.pulumi.com/registry/packages/aws/installation-configuration/",   # editorial, not api-docs
])
def test_same_site_only_sources(source):
    assert shape(source) == "same-site-only"


@pytest.mark.parametrize("source", [
    # An independent source alongside a pulumi.com URL — including the page's own.
    f"{ATP_URL} and https://github.com/pulumi/pulumi-terraform-provider/releases/tag/v1.4.0",
    f"{ATP_URL}; gh release list -R pulumi/pulumi-terraform-provider",
    f"`gh api repos/pulumi/pulumi/contents/pkg/x.go` and {ATP_URL}",
    f"{ATP_URL} and github.com/pulumi/pulumi-terraform-provider",
    f"{ATP_URL} and repo:data/pulumi_pricing.yaml",
    f"{ATP_URL} and static/programs/any-tf-yaml/Pulumi.yaml",
    f"{ATP_URL} and https://registry.terraform.io/providers/hashicorp/random/latest",
    # The generated-reference carve-out carries product-source authority.
    "https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucket/",
    "https://www.pulumi.com/docs/iac/cli/commands/pulumi_up/",
    "https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/pulumi/",
    f"{ATP_URL} and https://www.pulumi.com/docs/iac/cli/commands/pulumi_package_add/",
    # Not this repo rendered.
    "https://app.pulumi.com/acme/settings",
    # Positive evidence only: nothing identifiable is not the same as circular.
    "WebSearch ran query \"terraform-provider 1.4.0\"; top results didn't address the claim",
    "(no source pointer returned)",
    "",
])
def test_independent_or_unrecognised_sources_are_not_shaped(source):
    assert shape(source) is None


def test_a_generated_reference_page_under_review_is_still_self_reference():
    cli = "content/docs/iac/cli/commands/pulumi_up.md"
    assert shape("https://www.pulumi.com/docs/iac/cli/commands/pulumi_up/", file_path=cli) == "self-reference"


def test_claim_about_the_cited_url_is_exempt():
    # The pass2 dead-link shape: the only possible source IS the pulumi.com URL.
    svg = "https://www.pulumi.com/images/docs/concepts/state.svg"
    assert shape(svg, text=f"The state diagram is published at {svg}.") is None
    assert shape(svg, text="The diagram lives at `/images/docs/concepts/state.svg`.") is None
    assert shape(svg, text="The pin is 1.4.0.", source_hint=svg) is None
    assert shape(svg, text="The pin is 1.4.0.") == "same-site-only"
    # A site-relative link is delimited: `/docs/` does not match inside a longer path.
    assert shape("https://www.pulumi.com/docs/",
                 text="See [stacks](/docs/iac/concepts/stacks/).") == "same-site-only"
    assert shape("https://www.pulumi.com/docs/iac/concepts/stacks/#create",
                 text="See [stacks](/docs/iac/concepts/stacks/).") is None


def test_ledger_records_classify_as_audited():
    got = {f"{pr}/{i}": vc.source_discipline_shape(ledger_claim(pr, i), v["source"])
           for pr, recs in LEDGER.items() for i, v in enumerate(recs)}
    assert got == {
        "21720/0": "self-reference", "21720/1": "self-reference",
        "21552/0": "self-reference", "21602/0": "self-reference",
        "21394/0": "self-reference", "21394/1": "self-reference",
        "21509/0": "same-site-only",   # cites the page's pre-move URL — a different path
        "21509/1": "self-reference",   # two URLs joined by " and ", one of them its own
        "21509/2": "self-reference",
        "21509/3": None,               # a github.com issue alongside /pricing/ is independent
    }


def test_gate_verdict_scope():
    claim = {"file": ATP, "text": "The pin is 1.4.0."}
    other = "https://www.pulumi.com/docs/iac/get-started/"

    def gate(verdict, source, repo_root=REPO_ROOT, **rec):
        return vc._gate_for_verdict(claim, {"verdict": verdict, "source": source, **rec}, repo_root)

    assert gate("contradicted", ATP_URL) == "self-reference"
    assert gate("mismatch", ATP_URL) == "self-reference"
    assert gate("contradicted", other) == "same-site-only"
    # Rule 2 makes `mismatch` the correct verdict for two Pulumi pages disagreeing.
    assert gate("mismatch", other) is None
    for verdict in ("verified", "matches", "unverifiable", "not-a-claim", "framing-drift"):
        assert gate(verdict, ATP_URL) is None
    assert gate("contradicted", ATP_URL, source_discipline_gate="generated-from-data") is None
    assert gate("contradicted", ATP_URL, repo_root=None) is None
    assert vc._gate_for_verdict({"text": "t"}, {"verdict": "contradicted", "source": ATP_URL}, REPO_ROOT) is None


# ---- the re-check hop --------------------------------------------------------


def test_refresh_false_positive_is_cleared_by_release_tags(api):
    # PR #21720: a bot bumped the `terraform-provider` pin 0.10.0 → 1.4.0 (the
    # real latest release); pass3 found the live page and called it contradicted.
    api["script"] = {
        "pass3": [ledger_block("21720", 1)],
        "pass1": [verify_block("verified", "v1.4.0 is the latest release of pulumi-terraform-provider.",
                               "gh release list -R pulumi/pulumi-terraform-provider --limit 5")],
    }
    rec = vc.run_verifier("k", ledger_claim("21720", 1), "pass3", None, "m", REPO_ROOT, False)
    assert api["order"] == ["pass3", "pass1"]
    assert rec["verdict"] == "verified" and rec["route"] == "pass1"
    assert rec["evidence"].startswith("(re-verified after self-reference) ")
    assert "source_discipline_gate" not in rec

    first, second = (user_text(b) for b in api["bodies"])
    assert "SOURCE-DISCIPLINE RE-CHECK" not in first
    assert "SOURCE-DISCIPLINE RE-CHECK" in second
    assert ATP_URL in second and "PRE-CHANGE" in second
    assert "pulumi.com/docs/iac/concepts/providers/any-terraform-provider/" in second


def test_real_regression_survives_when_independently_confirmed(api):
    # PR #21552: a rewrite weakened `ES2022` to `ES2017`. The live page was
    # right — and the re-check proves it from a source that is not the page.
    api["script"] = {
        "pass3": [ledger_block("21552")],
        "pass1": [verify_block("contradicted",
                               "TS1378: top-level await requires target ES2022 or higher with module nodenext.",
                               "https://www.typescriptlang.org/tsconfig/#target")],
    }
    rec = vc.run_verifier("k", ledger_claim("21552"), "pass3", None, "m", REPO_ROOT, False)
    assert rec["verdict"] == "contradicted" and rec["confidence"] == "high"
    assert "source_discipline_gate" not in rec
    assert rec["source"] == "https://www.typescriptlang.org/tsconfig/#target"
    assert rec["evidence"].startswith("(re-verified after self-reference) ")


@pytest.mark.parametrize("recheck_block, outcome", [
    (verify_block("unverifiable", "No release notes address IAM defaults.", "gh search code --owner pulumi ecr", "low"),
     "could not settle it"),
    (verify_block("contradicted", "The live guide says enabled by default.",
                  "https://www.pulumi.com/docs/iac/guides/clouds/aws/ecr/"),
     "returned `contradicted` on non-independent evidence again"),
    (verify_block("contradicted", "Another guide says enabled by default.",
                  "https://www.pulumi.com/docs/iac/guides/clouds/aws/ecs/"),
     "returned `contradicted` on non-independent evidence again"),
])
def test_unsettled_recheck_downgrades_and_keeps_the_reasoning(api, recheck_block, outcome):
    api["script"] = {"pass3": [ledger_block("21602")], "pass1": [recheck_block]}
    rec = vc.run_verifier("k", ledger_claim("21602"), "pass3", None, "m", REPO_ROOT, False)
    original = LEDGER["21602"][0]
    assert rec["verdict"] == "unverifiable" and rec["confidence"] == "low"
    assert rec["source_discipline_gate"] == "self-reference"
    assert rec["route"] == "pass3" and rec["source"] == original["source"]
    assert rec["evidence"].startswith("[source-discipline gate: ")
    assert rec["evidence"].endswith(original["evidence"])       # verbatim, so the reviewer sees X vs Y
    assert outcome in rec["evidence"] and "author question" in rec["evidence"]
    assert api["order"] == ["pass3", "pass1"]                   # one re-check, never a second


def test_same_site_only_contradiction_shares_the_machinery(api):
    api["script"] = {
        "pass3": [ledger_block("21509", 0)],
        "pass1": [verify_block("unverifiable", "Token-type gating is not in a public repo.", "gh search code x", "low")],
    }
    rec = vc.run_verifier("k", ledger_claim("21509", 0), "pass3", None, "m", REPO_ROOT, False)
    assert rec["verdict"] == "unverifiable" and rec["source_discipline_gate"] == "same-site-only"
    assert "Same-site pages are never ground truth" in user_text(api["bodies"][1])
    assert LEDGER["21509"][0]["source"] in user_text(api["bodies"][1])


def test_recheck_turn_cap_and_errors_downgrade_rather_than_raise(api, monkeypatch):
    api["script"] = {"pass3": [ledger_block("21720")], "pass1": [[{"type": "text", "text": "hmm"}]]}
    rec = vc.run_verifier("k", ledger_claim("21720"), "pass3", None, "m", REPO_ROOT, False)
    assert rec["source_discipline_gate"] == "self-reference" and "ran out of turns" in rec["evidence"]
    assert "turn_cap_exhausted" not in rec
    assert api["order"].count("pass1") == vc.MAX_TURNS["pass1"] and api["order"].count("pass3") == 1

    first_hop = api["script"]["pass3"][0]

    def flaky(api_key, body):
        if any(t.get("name") == "gh_query" for t in body["tools"]):
            raise RuntimeError("HTTP 529: overloaded")
        return {"content": first_hop, "usage": {}}

    monkeypatch.setattr(vc, "_post_messages", flaky)
    rec = vc.run_verifier("k", ledger_claim("21720"), "pass3", None, "m", REPO_ROOT, False)
    assert rec["verdict"] == "unverifiable" and rec["source_discipline_gate"] == "self-reference"
    assert "HTTP 529" in rec["evidence"]


def test_usage_is_aggregated_across_hops(api):
    read_turn = [{"type": "tool_use", "id": "r1", "name": "read_file", "input": {"path": "nope.md"}}]
    api["script"] = {
        "pass3": [ledger_block("21720")],
        "pass1": [read_turn, verify_block("verified", "v1.4.0 exists.", "gh release view v1.4.0 -R pulumi/pulumi-terraform-provider")],
    }
    rec = vc.run_verifier("k", ledger_claim("21720"), "pass3", None, "m", REPO_ROOT, False)
    assert rec["model_usage"] == {"input_tokens": 300, "output_tokens": 30, "cache_read_input_tokens": 21,
                                  "cache_creation_input_tokens": 9, "turns": 3}
    # The downgrade path sums both hops too.
    api["order"].clear()
    api["script"]["pass1"] = [verify_block("unverifiable", "nothing", "gh search code x", "low")]
    rec = vc.run_verifier("k", ledger_claim("21720"), "pass3", None, "m", REPO_ROOT, False)
    assert rec["source_discipline_gate"] == "self-reference"
    assert rec["model_usage"]["input_tokens"] == 200 and rec["model_usage"]["turns"] == 2


def test_escalated_hop_is_gated_too(api):
    # pass1 → pass3 escalation lands on the live page; the re-check still runs,
    # and still exactly once.
    api["script"] = {
        "pass1": [verify_block("unverifiable", "not in source", "gh search code x", "low", route_escalation="pass3"),
                  verify_block("verified", "v1.4.0 is the latest release.", "gh release list -R pulumi/pulumi-terraform-provider")],
        "pass3": [ledger_block("21720")],
    }
    rec = vc.run_verifier("k", ledger_claim("21720"), "pass1", None, "m", REPO_ROOT, False)
    assert api["order"] == ["pass1", "pass3", "pass1"]
    assert rec["verdict"] == "verified"
    assert rec["evidence"].startswith("(escalated from pass1) (re-verified after self-reference) ")
    assert rec["model_usage"]["turns"] == 3


def test_independent_contradiction_is_never_rechecked(api):
    api["script"] = {"pass3": [verify_block(
        "contradicted", "Latest release is v1.4.0, not 2.0.0.",
        f"{ATP_URL} and https://github.com/pulumi/pulumi-terraform-provider/releases")]}
    rec = vc.run_verifier("k", ledger_claim("21720"), "pass3", None, "m", REPO_ROOT, False)
    assert rec["verdict"] == "contradicted" and api["order"] == ["pass3"]
    assert "source_discipline_gate" not in rec


def test_dead_link_claim_keeps_its_pass2_contradiction(api):
    svg = "https://www.pulumi.com/images/docs/concepts/state.svg"
    claim = {"__id": "c9", "file": ATP, "line_range": "L9", "type": "cross-reference",
             "text": f"The state diagram is published at {svg}."}
    api["script"] = {"pass2": [verify_block("contradicted", "cited URL returns HTTP 404", svg)]}
    rec = vc.run_verifier("k", claim, "pass2", {"url": svg, "status": 404, "content_text": ""},
                          "m", REPO_ROOT, False)
    assert rec["verdict"] == "contradicted" and api["order"] == ["pass2"]


def test_gate_is_inert_in_dry_run_and_without_a_repo_root_or_file(api):
    api["script"] = {"pass3": [ledger_block("21720")]}
    rec = vc.run_verifier("k", ledger_claim("21720"), "pass3", None, "m", REPO_ROOT, True)
    assert rec["source"] == "dry-run" and api["order"] == []

    rec = vc.run_verifier("k", ledger_claim("21720"), "pass3", None, "m", None, False)
    assert rec["verdict"] == "contradicted" and api["order"] == ["pass3"]

    api["order"].clear()
    no_file = {k: v for k, v in ledger_claim("21720").items() if k != "file"}
    rec = vc.run_verifier("k", no_file, "pass3", None, "m", REPO_ROOT, False)
    assert rec["verdict"] == "contradicted" and api["order"] == ["pass3"]


def test_generated_from_data_gate_takes_precedence(api):
    generated = "content/docs/reference/pre-built-policy-packs/cis-aws.md"
    claim = {"__id": "c1", "file": generated, "line_range": "L1", "type": "numerical", "text": "CIS 4.2"}
    api["script"] = {"pass3": [verify_block(
        "contradicted", "live page says otherwise",
        "https://www.pulumi.com/docs/reference/pre-built-policy-packs/cis-aws/")]}
    rec = vc.run_verifier("k", claim, "pass3", None, "m", REPO_ROOT, False)
    assert rec["source_discipline_gate"] == "generated-from-data" and api["order"] == ["pass3"]


# ---- own-file-only: a `contradicted` citing nothing but the reviewed file ----

OWN_FILE = "content/docs/iac/concepts/providers/any-terraform-provider.md"


def _own_claim():
    return {"file": OWN_FILE, "line_range": "L57", "type": "version",
            "text": "The example Pulumi YAML pins the `terraform-provider` package's `random` provider to version 1.4.0."}


def test_own_file_only_shape_matches_repo_and_bare_paths():
    for src in (f"repo:{OWN_FILE}", f"repo:{OWN_FILE} (line 289)", OWN_FILE):
        assert vc.source_discipline_shape(_own_claim(), src) == "own-file-only", src


def test_own_file_alongside_independent_source_is_not_gated():
    for src in (f"repo:{OWN_FILE}; gh release list -R pulumi/pulumi-terraform-provider",
                f"repo:{OWN_FILE}; pulumi/registry themes/default/data/registry/packages/honeycombio.yaml",
                f"repo:{OWN_FILE} and github.com/pulumi/pulumi-terraform-provider",
                "WebSearch ran query \"x\"; top results didn't address the claim"):
        assert vc.source_discipline_shape(_own_claim(), src) is None, src


def test_own_file_only_gates_contradicted_but_not_mismatch():
    root = Path(".")
    rec = {"verdict": "contradicted", "source": f"repo:{OWN_FILE}"}
    assert vc._gate_for_verdict(_own_claim(), rec, root) == "own-file-only"
    # A page that disagrees with itself is a legitimate internal-consistency finding.
    rec = {"verdict": "mismatch", "source": f"repo:{OWN_FILE}"}
    assert vc._gate_for_verdict(_own_claim(), rec, root) is None


def test_own_file_recheck_note_names_the_three_outcomes():
    msg = vc.build_user_message(_own_claim(), "pass1", None,
                                recheck={"gate": "own-file-only", "urls": [], "own_path": None})
    assert "not-a-claim" in msg and "mismatch" in msg and "file under review" in msg


# ---- own-file-only `verified`: re-check (#21733) -----------------------------
#
# 27% of `verified` verdicts in the claims index (13% in PR reviews) cited only
# the page under review. A hand audit of 50 found two-thirds were checkable
# product claims nobody checked, so each one gets the same re-check hop.

OWN_SOURCE = f"repo:{OWN_FILE} (L57)"
RELEASES = "gh release list -R pulumi/pulumi-terraform-provider"


def _typed_claim(ctype: str) -> dict:
    return {**_own_claim(), "__id": "c1", "type": ctype}


@pytest.mark.parametrize("source", [
    # Real audit sources that name product source without a `gh` command or URL.
    "pulumi/pulumi:pkg/cmd/esc/cli/env_provider_gcp_login.go; "
    "pulumi/docs:content/docs/iac/concepts/providers/any-terraform-provider.md",
    f"repo:{OWN_FILE} (lines 77-96); pulumi/esc README",
    f"{OWN_FILE}; pulumi/pulumi-dotnet sdk/Pulumi/Stack.cs",
    f"repo:{OWN_FILE}; pulumi/pulumi changelog/v3.133.0.md",
])
def test_product_source_without_a_gh_marker_is_independent(source):
    assert vc.source_discipline_shape(_own_claim(), source) is None


@pytest.mark.parametrize("source", [
    f"repo:{OWN_FILE}#L99",
    f"repo:{OWN_FILE}#L10-L20",
    f"repo:{OWN_FILE}:346",
    f"pulumi/docs:{OWN_FILE}",
    f"repo:{OWN_FILE} (L141-144); general knowledge of Pulumi engine diff semantics",
])
def test_own_file_with_line_anchors_or_general_knowledge_is_own_file_only(source):
    assert vc.source_discipline_shape(_own_claim(), source) == "own-file-only"


def test_import_path_echoed_from_the_claim_is_not_a_product_citation():
    # Go import paths are the claim's own content, not a repository consulted.
    src = f"repo:{OWN_FILE} (imports github.com/pulumi/pulumi-aws/sdk/v4)"
    assert vc.source_discipline_shape(_own_claim(), src) is None  # bare github.com still fails open
    assert vc._cites_product_repo("content/docs/migrating-to-pulumi/from-kubernetes.md") is False


def test_verified_gate_scope():
    def gate(source, confidence="high", ctype="behavior"):
        return vc._gate_for_verdict(_typed_claim(ctype),
                                    {"verdict": "verified", "confidence": confidence,
                                     "source": source}, REPO_ROOT)

    for ctype in ("behavior", "feature", "api-surface", "url", "version", "numerical"):
        assert gate(OWN_SOURCE, ctype=ctype) == "own-file-only", ctype
    assert gate(OWN_SOURCE, confidence="medium") == "own-file-only"
    # Low confidence already surfaces as a ⚠️ "verified weakly" stub.
    assert gate(OWN_SOURCE, confidence="low") is None
    assert gate(f"{OWN_SOURCE}; {RELEASES}") is None
    assert gate("repo:content/docs/iac/concepts/providers/_index.md") is None
    assert gate("the page under review") is None


def test_finalize_never_relabels_a_verified():
    rec = vc._finalize_verdict(_typed_claim("behavior"), "pass1",
                               {"verdict": "verified", "confidence": "high",
                                "evidence": "e", "source": OWN_SOURCE},
                               vc._zero_usage(), 1, REPO_ROOT)
    assert rec["verdict"] == "verified" and "source_discipline_gate" not in rec


def test_behavior_claim_is_rechecked_and_an_independent_answer_stands(api):
    api["script"] = {"pass1": [
        verify_block("verified", "The doc itself states replacements are created first.", OWN_SOURCE),
        verify_block("verified", "deleteBeforeReplace defaults to false",
                     "gh api repos/pulumi/pulumi/contents/sdk/go/common/resource/resource_goal.go"),
    ]}
    rec = vc.run_verifier("k", _typed_claim("behavior"), "pass1", None, "m", REPO_ROOT, False)
    assert rec["verdict"] == "verified" and "source_discipline_gate" not in rec
    assert rec["evidence"].startswith("(re-verified after own-file-only)")
    assert api["order"] == ["pass1", "pass1"]
    note = user_text(api["bodies"][1])
    assert "returned `verified` citing only the file under review" in note
    assert "not-a-claim" in note and "DIFFERENT" in note
    assert "latest release" not in note  # the currency ask is version-only


def test_stale_example_pin_asks_about_currency_and_keeps_what_it_found(api):
    # get-functions.md pins pulumi-aws/sdk/v4 in its Go example; latest is v7.
    api["script"] = {"pass1": [
        verify_block("verified", "the doc's own Go example imports sdk/v4", OWN_SOURCE),
        verify_block("unverifiable", "pinned v4, latest is v7.4.0", "gh release list -R pulumi/pulumi-aws"),
    ]}
    rec = vc.run_verifier("k", _typed_claim("version"), "pass1", None, "m", REPO_ROOT, False)
    assert rec["verdict"] == "unverifiable" and rec["source_discipline_gate"] == "own-file-only"
    assert "pinned v4, latest is v7.4.0" in rec["evidence"]
    assert "what is the source for this value?" in rec["evidence"]
    assert "latest release" in user_text(api["bodies"][1])


def test_own_file_verified_recheck_may_settle_on_not_a_claim(api):
    api["script"] = {"pass1": [
        verify_block("verified", "the page's example uses 3 replicas", OWN_SOURCE),
        verify_block("not-a-claim", "the replica count is the example's own choice", OWN_SOURCE),
    ]}
    rec = vc.run_verifier("k", _typed_claim("numerical"), "pass1", None, "m", REPO_ROOT, False)
    assert rec["verdict"] == "not-a-claim" and "source_discipline_gate" not in rec


def test_own_file_verified_twice_is_downgraded_to_an_author_question(api):
    api["script"] = {"pass1": [
        verify_block("verified", "the doc itself states 1.4.0", OWN_SOURCE),
        verify_block("verified", "the doc still says 1.4.0", OWN_SOURCE),
    ]}
    rec = vc.run_verifier("k", _typed_claim("feature"), "pass1", None, "m", REPO_ROOT, False)
    assert rec["verdict"] == "unverifiable" and rec["confidence"] == "low"
    assert rec["source_discipline_gate"] == "own-file-only"
    assert "`verified` is downgraded" in rec["evidence"]
    assert rec["evidence"].endswith("the doc itself states 1.4.0")
    assert rec["model_usage"]["turns"] == 2


def test_low_confidence_own_file_verified_is_not_rechecked(api):
    api["script"] = {"pass1": [verify_block("verified", "the doc says so", OWN_SOURCE, confidence="low")]}
    rec = vc.run_verifier("k", _typed_claim("behavior"), "pass1", None, "m", REPO_ROOT, False)
    assert rec["verdict"] == "verified" and api["order"] == ["pass1"]


def test_contradicted_own_file_note_is_unchanged_by_the_verified_branch(api):
    api["script"] = {"pass1": [
        verify_block("contradicted", "page says 3.7.1", OWN_SOURCE),
        verify_block("unverifiable", "no source", "none"),
    ]}
    rec = vc.run_verifier("k", _typed_claim("version"), "pass1", None, "m", REPO_ROOT, False)
    assert rec["verdict"] == "unverifiable"
    assert "does the page say what this claim says it does?" in rec["evidence"]
    body = user_text(api["bodies"][1])
    assert "returned `contradicted` citing only" in body and "latest release" not in body
