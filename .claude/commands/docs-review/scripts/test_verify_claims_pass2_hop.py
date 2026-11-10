"""A cited page that doesn't address a claim hops to pass1 when the PR cites
its implementing change.

pulumi/docs#22397: the only claim cited the Cloudflare post on the eMudhra
compromise, so it routed to pass2. The page described the compromise, not
what Pulumi's self-hosted release does, and the bare "the page didn't say"
became a blocking author question. The PR body linked the change that ships
it (a private repo), but nothing ever looked there, so the private-source
carve-out in compose-review.py had nothing to match.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).parent
SPEC = importlib.util.spec_from_file_location("verify_claims_hop", HERE / "verify-claims.py")
vc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(vc)

URL = "https://blog.cloudflare.com/emudhra-certificate-compromise/"
CLAIM = {"__id": "c1", "__route": "pass2", "file": "content/docs/x.md", "line_range": "L27",
         "text": "The API service no longer trusts eight eMudhra intermediates.", "urls": [URL]}
FETCHED = {URL: {"url": URL, "status": 200, "body": "8 eMudhra certificates are compromised"}}


def _rec(route, verdict, evidence, **extra):
    return {"claim_id": "c1", "route": route, "verdict": verdict, "evidence": evidence,
            "source": "x", "model_usage": {"input_tokens": 1, "output_tokens": 1,
                                           "cache_read_input_tokens": 0,
                                           "cache_creation_input_tokens": 0, "turns": 1},
            **extra}


def _run(monkeypatch, pass2_rec, impl_refs):
    calls = []

    def fake(api_key, claim, route, evidence_pack, *a, **kw):
        calls.append(route)
        if route == "pass2":
            return dict(pass2_rec)
        return _rec("pass1", "unverifiable", "pulumi/pulumi-service#51235 is not readable with this token")

    monkeypatch.setattr(vc, "run_verifier", fake)
    monkeypatch.setattr(vc, "find_fetched_url", lambda claim, fetched: fetched[URL])
    rec, err = vc.process_claim("k", dict(CLAIM), FETCHED, "m", HERE, False, impl_refs=impl_refs)
    return rec, err, calls


def test_an_unaddressed_cited_page_hops_to_the_implementing_change(monkeypatch):
    rec, err, calls = _run(monkeypatch, _rec("pass2", "unverifiable", "the page doesn't say"),
                           ["pulumi/pulumi-service#51235"])
    assert err is None and calls == ["pass2", "pass1"]
    assert rec["route"] == "pass1", "route counts read the verdict's own route"
    assert "pulumi-service#51235" in rec["evidence"]
    assert rec["evidence"].startswith("(the cited page didn't address it")
    assert rec["model_usage"]["turns"] == 2 and rec["model_usage"]["input_tokens"] == 2


def test_no_hop_without_an_implementing_change_or_when_the_page_settled_it(monkeypatch):
    _, _, calls = _run(monkeypatch, _rec("pass2", "unverifiable", "the page doesn't say"), [])
    assert calls == ["pass2"]
    for verdict in ("verified", "contradicted"):
        rec, _, calls = _run(monkeypatch, _rec("pass2", verdict, "page says so"),
                             ["pulumi/pulumi-service#51235"])
        assert calls == ["pass2"] and rec["verdict"] == verdict
    _, _, calls = _run(monkeypatch, _rec("pass2", "unverifiable", "cap", turn_cap_exhausted=True),
                       ["pulumi/pulumi-service#51235"])
    assert calls == ["pass2"], "a budget failure isn't evidence the page was silent"
