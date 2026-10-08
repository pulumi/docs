"""Tests for review-admin.py (offline — no AWS, no network)."""

from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "review_admin", Path(__file__).parent / "review-admin.py")
ra = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ra)


@pytest.fixture
def cache(tmp_path: Path) -> Path:
    """A populated cache directory built from the module's own fixtures."""
    for rel, record in ra.FIXTURES.items():
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(record) + "\n")
    return tmp_path


def test_self_test_passes():
    assert ra.self_test() == 0


def test_load_docs_tolerates_legacy_records_without_schema_version(cache: Path):
    docs = ra.load_docs(cache)
    assert len(docs) == 1
    assert "schema_version" not in docs[0]
    assert docs[0]["slug"] == "docs-get-started"


def test_load_json_dir_skips_unreadable_files(cache: Path, capsys):
    (cache / "content-review" / "ledger" / "broken.json").write_text("{not json")
    docs = ra.load_docs(cache)
    assert len(docs) == 1
    assert "unreadable JSON skipped" in capsys.readouterr().err


def test_flatten_claims_denormalizes_article_fields(cache: Path):
    rows = ra.flatten_claims(ra.load_claims(cache))
    assert len(rows) == 2
    for row in rows:
        assert row["slug"] == "docs-example"
        assert row["commit"] == "abc123"
        assert row["article_reviewed_at"] == "2026-07-16"
        assert "claims" not in row
    assert rows[1]["verdict"] == "contradicted"


def test_flatten_blog_issues_uses_latest_run_per_slug(cache: Path):
    older = dict(ra.FIXTURES["content-review/blog-review/runs/2026-07-16/example-post.json"])
    older["issues"] = [{"category": "stale", "severity": "low"}] * 3
    old_dir = cache / "content-review" / "blog-review" / "runs" / "2026-07-01"
    old_dir.mkdir(parents=True)
    (old_dir / "example-post.json").write_text(json.dumps(older))

    issues = ra.flatten_blog_issues(ra.load_blog_runs(cache))
    assert len(issues) == 1
    assert issues[0]["issue_category"] == "dead-link"
    assert issues[0]["run_date"] == "2026-07-16"


def test_load_social_dedupes_across_state_files(cache: Path):
    duplicate = ra.FIXTURES["social/posted-social.json"]
    (cache / "social" / "posted.json").write_text(json.dumps(duplicate))
    rows = ra.load_social(cache)
    assert len(rows) == 2  # x + linkedin, not doubled
    assert all(r["source_file"] == "posted-social.json" for r in rows)
    assert all(r["failures"] == 1 for r in rows)


def test_build_summary_counts(cache: Path):
    s = ra.build_summary(cache)
    assert s["docs"]["by_status"]["clean"] == 1
    assert s["claims"]["by_verdict"] == {"verified": 1, "contradicted": 1}
    assert s["blog"]["by_severity"]["medium"] == 1
    assert s["social"]["by_platform"] == {"x": 1, "linkedin": 1}


def test_export_csv_and_jsonl_shapes(cache: Path, tmp_path: Path):
    out = tmp_path / "out"
    out.mkdir()
    rows = ra.flatten_claims(ra.load_claims(cache))
    ra.write_exports(rows, out, "claims", ra.CLAIM_COLUMNS, {"csv", "jsonl"})

    with (out / "claims.csv").open() as fh:
        parsed = list(csv.DictReader(fh))
    assert len(parsed) == 2
    assert parsed[0]["claim_id"] == "c1"
    assert parsed[0]["volatile"] == "False"

    jsonl = [json.loads(line) for line in (out / "claims.jsonl").read_text().splitlines()]
    assert jsonl[0]["volatile"] is False
    assert "_file" not in jsonl[0]


def test_export_preserves_unknown_fields(cache: Path, tmp_path: Path):
    docs = ra.load_docs(cache)
    docs[0]["brand_new_field"] = {"nested": True}
    out = tmp_path / "out"
    out.mkdir()
    ra.write_exports(docs, out, "docs-ledger", ra.DOCS_COLUMNS, {"csv", "jsonl"})
    with (out / "docs-ledger.csv").open() as fh:
        parsed = list(csv.DictReader(fh))
    assert parsed[0]["brand_new_field"] == '{"nested": true}'


def test_html_embeds_data_and_escapes_script_close(cache: Path):
    html = ra.render_html(cache)
    assert html.count("<script") == 2  # data block + app JS
    assert "</script> honest" not in html
    assert "docs-get-started" in html
    assert "console-access" in html


def test_record_matches_slug_path_and_url():
    record = {"slug": "docs-example", "path": "content/docs/example.md"}
    assert ra.record_matches(record, "docs-example")
    assert ra.record_matches(record, "content/docs/example.md")
    assert ra.record_matches(record, "example")
    assert not ra.record_matches(record, "unrelated")
    assert ra.record_matches({"url": "/blog/example-post/"}, "/blog/example-post/")


def test_pr_review_rows_joins_evidence_state_and_last_action(cache: Path):
    rows = ra.pr_review_rows(cache)
    assert len(rows) == 1
    row = rows[0]
    assert row["pr"] == 21300
    assert row["head_sha"] == "a" * 9
    assert row["blocking"] == 1     # F1: outstanding, no disposition
    assert row["dispositions"] == 1  # F2: has a disposition
    assert row["warns"] == 1
    assert row["escalations"] == 0
    assert row["closes"] == 0
    assert row["last_sweep_action"] == "warn"


def test_pr_review_rows_empty_when_prefix_absent(tmp_path: Path):
    assert ra.pr_review_rows(tmp_path) == []


def test_load_pr_review_state_tags_pr_from_filename(cache: Path):
    states = ra.load_pr_review_state(cache)
    assert len(states) == 1
    assert states[0]["pr"] == 21300
    assert len(states[0]["warns"]) == 1


def test_load_pr_review_runs_tags_run_date(cache: Path):
    runs = ra.load_pr_review_runs(cache)
    assert len(runs) == 1
    assert runs[0]["_run_date"] == "2026-08-31"
    assert runs[0]["actions"][0]["pr"] == 21300


def test_record_matches_by_pr_number():
    assert ra.record_matches({"pr": 21300}, "21300")
    assert not ra.record_matches({"pr": 21300}, "99999")


def test_build_summary_includes_pr_review(cache: Path):
    s = ra.build_summary(cache)
    assert s["pr_review"]["prs"] == 1
    assert s["pr_review"]["blocking_total"] == 1
    assert s["pr_review"]["warns_total"] == 1
    assert s["pr_review"]["escalations_total"] == 0


def test_list_pr_review(cache: Path, capsys):
    class Args:
        cache_dir = str(cache)
        domain = "pr-review"
        status = None
        verdict = None
        since = None
        limit = None

    assert ra.cmd_list(Args()) == 0
    out = capsys.readouterr().out
    assert "(1 rows)" in out
    assert "21300" in out and "warn" in out


def test_export_includes_pr_review(cache: Path, tmp_path: Path):
    out = tmp_path / "out"
    out.mkdir()
    ra.write_exports(ra.pr_review_rows(cache), out, "pr-review", ra.PR_REVIEW_COLUMNS, {"csv"})
    with (out / "pr-review.csv").open() as fh:
        parsed = list(csv.DictReader(fh))
    assert len(parsed) == 1
    assert parsed[0]["pr"] == "21300"


def test_list_filters(cache: Path, capsys):
    class Args:
        cache_dir = str(cache)
        domain = "claims"
        status = None
        verdict = "contradicted"
        since = None
        limit = None

    assert ra.cmd_list(Args()) == 0
    out = capsys.readouterr().out
    assert "(1 rows)" in out
    assert "contradicted" in out
    assert "verified" not in out
