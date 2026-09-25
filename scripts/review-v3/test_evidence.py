#!/usr/bin/env python3
"""pytest suite for the review-v3 evidence layer.

Covers `validate-evidence.py`, `record-evidence.py`, and
`render-evidence-html.py` together, since they share one contract (the
evidence object) and the interesting bugs are at the seams between them
(a merge that silently drops a disposition, a render that doesn't escape
what validation let through). Each of those three scripts also carries its
own `--self-test` smoke checks (run by `make test-review-pipeline`); this
file adds the truth-table and both-directions coverage that's easier to
express with pytest fixtures/parametrize than as a hand-rolled `check()`
loop.

The three scripts have hyphenated filenames (house style — see
`scripts/blog-review/record-findings.py` importing `validate-findings.py`
the same way), so they're loaded by file path rather than `import`.
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

HERE = Path(__file__).resolve().parent


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


validate_evidence_mod = _load("validate-evidence")
record_evidence_mod = _load("record-evidence")
render_html_mod = _load("render-evidence-html")

validate_evidence = validate_evidence_mod.validate_evidence
merge_dispositions = record_evidence_mod.merge_dispositions
merge_latest = record_evidence_mod.merge_latest
render_evidence_html = render_html_mod.render_evidence_html


# ---- fixtures ---------------------------------------------------------


@pytest.fixture
def valid_evidence() -> dict:
    return validate_evidence_mod._valid_fixture()


def _finding(**overrides) -> dict:
    base = {
        "id": "F1", "bucket": "outstanding", "file": "content/docs/x.md",
        "text": "t", "origin": "o", "status": "open",
    }
    base.update(overrides)
    return base


def _disposition(**overrides) -> dict:
    base = {"disposition": "accepted", "actor": "a", "note": "n",
            "updated_at": "2026-08-31T10:00:00Z"}
    base.update(overrides)
    return base


# ---- TASK 1: schema validation truth table -----------------------------


class TestValidateEvidence:
    def test_valid_fixture_passes(self, valid_evidence):
        assert validate_evidence(valid_evidence) == []

    @pytest.mark.parametrize("mutation,expected_substring", [
        (lambda e: e.pop("history"), "history is required"),
        (lambda e: e.update(bogus=1), "unexpected property"),
        (lambda e: e.update(schema_version=2), "schema_version"),
        (lambda e: e.update(repo="no-slash"), "evidence.repo"),
        (lambda e: e.update(head_sha="short"), "head_sha"),
        (lambda e: e.update(pr=0), "evidence.pr"),
        (lambda e: e.update(pr=-1), "evidence.pr"),
        (lambda e: e.update(high_water=-1), "high_water"),
        (lambda e: e.update(run_id=""), "run_id"),
        (lambda e: e.update(generated_at="2026-08-31"), "generated_at"),
        (lambda e: e.update(findings="nope"), "findings must be a list"),
        (lambda e: e.update(trail="nope"), "trail must be a list"),
        (lambda e: e.update(investigation_log=[]), "investigation_log must be an object"),
        (lambda e: e.update(history=[]), "history must be non-empty"),
        (lambda e: e.update(editorial_balance="nope"), "editorial_balance"),
        (lambda e: e.update(triaged="nope"), "triaged"),
        (lambda e: e.update(style_suggestions_count=-1), "style_suggestions_count"),
        (lambda e: e.update(confidence={"a": 1}), "confidence"),
        (lambda e: e.update(summary=5), "summary"),
    ])
    def test_top_level_violations(self, valid_evidence, mutation, expected_substring):
        mutation(valid_evidence)
        errors = validate_evidence(valid_evidence)
        assert any(expected_substring in e for e in errors), errors

    def test_top_level_not_a_dict(self):
        assert validate_evidence(["not", "a", "dict"]) != []
        assert validate_evidence(None) != []

    @pytest.mark.parametrize("finding,expected_substring", [
        (_finding(id="not-an-id"), "must match"),
        (_finding(bucket="vibes"), "bucket"),
        (_finding(text="  "), ".text"),
        (_finding(file=""), ".file"),
        (_finding(status="closed"), "status"),
        (_finding(origin=""), "origin"),
        (_finding(lines=[0]), "lines"),
        (_finding(lines=[1, 2, 3]), "lines"),
        (_finding(extra_key=1), "unexpected property"),
    ])
    def test_finding_violations(self, valid_evidence, finding, expected_substring):
        valid_evidence["findings"] = [finding]
        valid_evidence["high_water"] = 1
        errors = validate_evidence(valid_evidence)
        assert any(expected_substring in e for e in errors), errors

    def test_duplicate_finding_ids_rejected(self, valid_evidence):
        valid_evidence["findings"] = [_finding(id="F1"), _finding(id="F1")]
        errors = validate_evidence(valid_evidence)
        assert any("duplicated" in e for e in errors)

    def test_high_water_must_cover_max_index(self, valid_evidence):
        valid_evidence["findings"] = [_finding(id="F9")]
        valid_evidence["high_water"] = 3
        errors = validate_evidence(valid_evidence)
        assert any("high_water" in e for e in errors)

    @pytest.mark.parametrize("disposition_value", ["deferred", "accepted", "not-applicable"])
    def test_note_required_dispositions(self, valid_evidence, disposition_value):
        valid_evidence["findings"] = [
            _finding(disposition=_disposition(disposition=disposition_value, note=""))
        ]
        errors = validate_evidence(valid_evidence)
        assert any(".note is required" in e for e in errors), errors

    @pytest.mark.parametrize("disposition_value", ["fixed", "refuted"])
    def test_self_evidencing_dispositions_do_not_require_a_note(self, valid_evidence, disposition_value):
        valid_evidence["findings"] = [
            _finding(disposition=_disposition(disposition=disposition_value, note=""))
        ]
        errors = validate_evidence(valid_evidence)
        assert not any(".note is required" in e for e in errors), errors

    def test_unknown_disposition_value_rejected(self, valid_evidence):
        valid_evidence["findings"] = [_finding(disposition=_disposition(disposition="wontfix"))]
        errors = validate_evidence(valid_evidence)
        assert any("disposition" in e for e in errors)

    def test_disposition_bad_sha_rejected(self, valid_evidence):
        valid_evidence["findings"] = [_finding(disposition=_disposition(sha="zz"))]
        errors = validate_evidence(valid_evidence)
        assert any(".sha" in e for e in errors)

    @pytest.mark.parametrize("verdict", ["verified", "matches", "not-a-claim", "unverifiable",
                                          "contradicted", "mismatch", "framing-drift", "flagged"])
    def test_every_closed_verdict_accepted(self, valid_evidence, verdict):
        valid_evidence["trail"] = [{"file": "x.md", "claim": "c", "verdict": verdict}]
        assert validate_evidence(valid_evidence) == []

    def test_unknown_verdict_rejected(self, valid_evidence):
        valid_evidence["trail"] = [{"file": "x.md", "claim": "c", "verdict": "probably-true"}]
        errors = validate_evidence(valid_evidence)
        assert any("verdict" in e for e in errors)

    def test_history_entry_missing_sha(self, valid_evidence):
        valid_evidence["history"] = [{"ts": "2026-08-31T17:00:00Z", "summary": "x"}]
        errors = validate_evidence(valid_evidence)
        assert any(".sha is required" in e for e in errors)

    def test_history_entry_bad_sha_format(self, valid_evidence):
        valid_evidence["history"] = [{"ts": "2026-08-31T17:00:00Z", "summary": "x", "sha": "zz"}]
        errors = validate_evidence(valid_evidence)
        assert any("sha-stamped" in e for e in errors)


# ---- TASK 2: merge preserves the newer disposition, both directions -----


class TestMergeDispositions:
    def test_prior_wins_when_prior_is_newer(self):
        older = _disposition(disposition="accepted", updated_at="2026-08-31T10:00:00Z")
        newer = _disposition(disposition="refuted", note="", updated_at="2026-08-31T12:00:00Z")
        new_findings = [_finding(disposition=older)]
        prior_findings = [_finding(disposition=newer)]
        merged = merge_dispositions(new_findings, prior_findings)
        assert merged[0]["disposition"] == newer

    def test_new_wins_when_new_is_newer(self):
        older = _disposition(disposition="accepted", updated_at="2026-08-31T10:00:00Z")
        newer = _disposition(disposition="refuted", note="", updated_at="2026-08-31T12:00:00Z")
        new_findings = [_finding(disposition=newer)]
        prior_findings = [_finding(disposition=older)]
        merged = merge_dispositions(new_findings, prior_findings)
        assert merged[0]["disposition"] == newer

    def test_prior_disposition_survives_when_new_has_none(self):
        prior_disp = _disposition()
        new_findings = [_finding()]  # no disposition key
        prior_findings = [_finding(disposition=prior_disp)]
        merged = merge_dispositions(new_findings, prior_findings)
        assert merged[0]["disposition"] == prior_disp

    def test_new_disposition_kept_when_prior_has_none(self):
        new_disp = _disposition()
        new_findings = [_finding(disposition=new_disp)]
        prior_findings = [_finding()]  # no disposition key
        merged = merge_dispositions(new_findings, prior_findings)
        assert merged[0]["disposition"] == new_disp

    def test_finding_dropped_when_new_render_omits_it(self):
        prior_findings = [_finding(id="F1", disposition=_disposition())]
        merged = merge_dispositions([], prior_findings)
        assert merged == []

    def test_finding_added_by_new_render_has_no_disposition_to_merge(self):
        new_findings = [_finding(id="F2")]
        prior_findings = [_finding(id="F1", disposition=_disposition())]
        merged = merge_dispositions(new_findings, prior_findings)
        assert merged[0]["id"] == "F2"
        assert merged[0].get("disposition") is None

    def test_merge_latest_no_prior_returns_new_unchanged(self, valid_evidence):
        assert merge_latest(valid_evidence, None) == valid_evidence

    def test_merge_latest_high_water_never_decreases(self, valid_evidence):
        valid_evidence["high_water"] = 3
        result = merge_latest(valid_evidence, {"findings": [], "high_water": 99})
        assert result["high_water"] == 99


# ---- TASK 2: degradation path writes local without URI ------------------


class TestRecordEvidenceDegradation:
    def test_writes_local_files_without_uri(self, tmp_path, monkeypatch):
        monkeypatch.delenv("PR_REVIEW_EVIDENCE_URI", raising=False)
        evidence = validate_evidence_mod._valid_fixture()
        evidence_path = tmp_path / "evidence.json"
        evidence_path.write_text(json.dumps(evidence))
        out_dir = tmp_path / "out"

        calls = []
        monkeypatch.setattr(record_evidence_mod, "upload", lambda record, key: calls.append(key) or True)

        args = SimpleNamespace(evidence=str(evidence_path), pr=evidence["pr"],
                                head_sha=evidence["head_sha"], out_dir=str(out_dir))
        rc = record_evidence_mod.run(args)

        assert rc == 0
        assert calls == []
        sha_file = out_dir / f"{evidence['pr']}-{evidence['head_sha']}.json"
        latest_file = out_dir / f"{evidence['pr']}-latest.json"
        assert sha_file.is_file()
        assert latest_file.is_file()
        assert json.loads(sha_file.read_text()) == evidence
        assert json.loads(latest_file.read_text()) == evidence

    def test_warns_when_uri_unset(self, tmp_path, monkeypatch, capsys):
        monkeypatch.delenv("PR_REVIEW_EVIDENCE_URI", raising=False)
        evidence = validate_evidence_mod._valid_fixture()
        evidence_path = tmp_path / "evidence.json"
        evidence_path.write_text(json.dumps(evidence))
        args = SimpleNamespace(evidence=str(evidence_path), pr=evidence["pr"],
                                head_sha=evidence["head_sha"], out_dir=str(tmp_path / "out"))
        record_evidence_mod.run(args)
        assert "::warning::" in capsys.readouterr().err

    def test_invalid_evidence_exits_1_and_writes_nothing(self, tmp_path):
        bad_path = tmp_path / "bad.json"
        bad_path.write_text(json.dumps({"not": "valid"}))
        out_dir = tmp_path / "out"
        args = SimpleNamespace(evidence=str(bad_path), pr=1, head_sha="a" * 40, out_dir=str(out_dir))
        rc = record_evidence_mod.run(args)
        assert rc == 1
        assert not out_dir.exists()

    def test_pr_head_sha_mismatch_is_fatal(self, tmp_path):
        evidence = validate_evidence_mod._valid_fixture()
        evidence_path = tmp_path / "evidence.json"
        evidence_path.write_text(json.dumps(evidence))
        args = SimpleNamespace(evidence=str(evidence_path), pr=evidence["pr"] + 1,
                                head_sha=evidence["head_sha"], out_dir=str(tmp_path / "out"))
        assert record_evidence_mod.run(args) == 1

    def test_upload_invoked_with_merged_content_when_uri_set(self, tmp_path, monkeypatch):
        evidence = validate_evidence_mod._valid_fixture()
        evidence["findings"] = [_finding(disposition=_disposition(
            disposition="accepted", updated_at="2026-08-31T10:00:00Z"))]
        evidence["high_water"] = 1
        prior = {"findings": [_finding(disposition=_disposition(
            disposition="refuted", note="", updated_at="2026-08-31T12:00:00Z"))],
            "high_water": 5}

        monkeypatch.setenv("PR_REVIEW_EVIDENCE_URI", "s3://bucket/pr-review")
        monkeypatch.setattr(record_evidence_mod, "load_prior", lambda pr, uri: prior)
        uploaded = {}
        monkeypatch.setattr(record_evidence_mod, "upload",
                             lambda record, key: uploaded.__setitem__(key, record) or True)

        evidence_path = tmp_path / "evidence.json"
        evidence_path.write_text(json.dumps(evidence))
        args = SimpleNamespace(evidence=str(evidence_path), pr=evidence["pr"],
                                head_sha=evidence["head_sha"], out_dir=str(tmp_path / "out"))
        rc = record_evidence_mod.run(args)

        assert rc == 0
        assert len(uploaded) == 2
        latest_key = record_evidence_mod.s3_key("s3://bucket/pr-review", str(evidence["pr"]), "latest.json")
        assert uploaded[latest_key]["findings"][0]["disposition"]["disposition"] == "refuted"
        assert uploaded[latest_key]["high_water"] == 5


# ---- TASK 3: HTML escaping + anchor stability ----------------------------


class TestRenderEvidenceHtml:
    def test_script_tag_in_claim_text_is_escaped(self, valid_evidence):
        valid_evidence["trail"] = [{
            "file": "x.md", "claim": "<script>alert(1)</script>", "verdict": "contradicted",
        }]
        out = render_evidence_html(valid_evidence)
        assert "<script>alert(1)</script>" not in out
        assert "&lt;script&gt;alert(1)&lt;/script&gt;" in out

    def test_finding_text_is_escaped(self, valid_evidence):
        # findings text isn't in the fixture's table columns by default
        # (only id/bucket/file:lines/status/disposition are), so this checks
        # the disposition note column, which does surface finding-adjacent
        # free text into the rendered table.
        valid_evidence["findings"] = [
            _finding(disposition=_disposition(note='"><img src=x onerror=alert(1)>'))
        ]
        out = render_evidence_html(valid_evidence)
        body = out.split('<script type="application/json"', 1)[0]
        assert "<img src=x onerror=alert(1)>" not in body

    def test_history_summary_is_escaped(self, valid_evidence):
        valid_evidence["history"] = [
            {"ts": "2026-08-31T17:00:00Z", "summary": "<b>bold</b>", "sha": "a" * 7}
        ]
        out = render_evidence_html(valid_evidence)
        assert "<b>bold</b>" not in out
        assert "&lt;b&gt;bold&lt;/b&gt;" in out

    def test_all_eight_verdicts_render_with_their_emoji(self, valid_evidence):
        trail = [{"file": "x.md", "claim": f"claim {v}", "verdict": v}
                 for v, _, _ in render_html_mod.VERDICT_VOCAB]
        valid_evidence["trail"] = trail
        out = render_evidence_html(valid_evidence)
        for verdict, emoji, label in render_html_mod.VERDICT_VOCAB:
            assert emoji in out
            assert render_html_mod.esc(label) in out

    def test_anchors_are_1_indexed_by_array_position(self, valid_evidence):
        valid_evidence["trail"] = [
            {"file": "a.md", "claim": "first", "verdict": "verified"},
            {"file": "b.md", "claim": "second", "verdict": "flagged"},
            {"file": "c.md", "claim": "third", "verdict": "matches"},
        ]
        out = render_evidence_html(valid_evidence)
        assert 'id="claim-1"' in out
        assert 'id="claim-2"' in out
        assert 'id="claim-3"' in out

    def test_anchors_survive_verdict_grouping(self, valid_evidence):
        # First trail item has the LAST-displayed verdict ("flagged"); its
        # anchor must still be claim-1, not wherever it lands visually.
        valid_evidence["trail"] = [
            {"file": "a.md", "claim": "first, but flagged", "verdict": "flagged"},
            {"file": "b.md", "claim": "second, but verified", "verdict": "verified"},
        ]
        out = render_evidence_html(valid_evidence)
        idx_claim1 = out.index('id="claim-1"')
        idx_flagged_text = out.index("first, but flagged")
        idx_verified_text = out.index("second, but verified")
        # claim-1 anchors the flagged row wherever it's displayed.
        assert idx_claim1 < idx_flagged_text < idx_verified_text or \
            "first, but flagged" in out[idx_claim1:idx_claim1 + 400]

    def test_render_is_deterministic_for_identical_input(self, valid_evidence):
        out1 = render_evidence_html(json.loads(json.dumps(valid_evidence)))
        out2 = render_evidence_html(json.loads(json.dumps(valid_evidence)))
        assert out1 == out2

    def test_pr_link_and_repo_and_sha_in_header(self, valid_evidence):
        out = render_evidence_html(valid_evidence)
        assert f"https://github.com/{valid_evidence['repo']}/pull/{valid_evidence['pr']}" in out
        assert valid_evidence["head_sha"][:10] in out

    def test_no_external_requests(self, valid_evidence):
        out = render_evidence_html(valid_evidence)
        assert "<script src=" not in out
        assert "<link" not in out

    def test_dark_mode_media_query_present(self, valid_evidence):
        out = render_evidence_html(valid_evidence)
        assert "prefers-color-scheme: dark" in out

    def test_empty_trail_does_not_crash(self, valid_evidence):
        valid_evidence["trail"] = []
        out = render_evidence_html(valid_evidence)
        assert "No trail entries." in out


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
