"""pytest suite for routing.py — the lane-routing config loader/resolver.

Discovered by `make test-review-pipeline` via
`scripts/content-review/test_*.py` / `scripts/blog-review/test_*.py`-style
standalone collection is NOT how this one runs — it's plain pytest, picked
up the same way `.claude/commands/docs-review/scripts/` is: run directly
with `python3 -m pytest scripts/review-v3/`. See
`scripts/test-review-pipeline.sh`.
"""

from __future__ import annotations

import copy
from pathlib import Path

import pytest

import routing

HERE = Path(__file__).resolve().parent


@pytest.fixture
def base_config() -> dict:
    return copy.deepcopy(routing._CANNED_CONFIG)


@pytest.fixture
def config(base_config) -> routing.Config:
    cfg, errors, _warnings = routing.validate_raw(base_config)
    assert errors == []
    return cfg


# ---- validation failure modes, one per rule --------------------------------


def test_unknown_top_level_key_is_error(base_config):
    base_config["surprise"] = True
    _, errors, _ = routing.validate_raw(base_config)
    assert any("unknown key" in e and "top level" in e for e in errors)


def test_schema_not_one_is_error(base_config):
    base_config["schema"] = 2
    _, errors, _ = routing.validate_raw(base_config)
    assert any("schema must be 1" in e for e in errors)


def test_schema_missing_is_error(base_config):
    del base_config["schema"]
    _, errors, _ = routing.validate_raw(base_config)
    assert any("schema must be 1" in e for e in errors)


def test_matrix_role_absent_from_teams_is_error(base_config):
    base_config["matrix"]["docs"]["substantive"] = "no-such-team"
    _, errors, _ = routing.validate_raw(base_config)
    assert any(
        "matrix.docs.substantive names unknown role" in e for e in errors
    )


def test_matrix_role_none_is_not_an_error(base_config):
    base_config["matrix"]["docs"]["substantive"] = "none"
    _, errors, _ = routing.validate_raw(base_config)
    assert errors == []


def test_matrix_missing_subject_is_error(base_config):
    del base_config["matrix"]["website"]
    _, errors, _ = routing.validate_raw(base_config)
    assert any("missing required subject 'website'" in e for e in errors)


def test_matrix_unknown_subject_is_error(base_config):
    base_config["matrix"]["gadgets"] = {"mechanical": "none", "substantive": "none"}
    _, errors, _ = routing.validate_raw(base_config)
    assert any("unknown subject 'gadgets'" in e for e in errors)


def test_matrix_cell_unknown_key_is_error(base_config):
    base_config["matrix"]["docs"]["surprise"] = "none"
    _, errors, _ = routing.validate_raw(base_config)
    assert any("matrix.docs: unknown key 'surprise'" in e for e in errors)


def test_matrix_cell_bad_staging_evidence_value_is_error(base_config):
    base_config["matrix"]["infra"]["staging_evidence"] = "sometimes"
    _, errors, _ = routing.validate_raw(base_config)
    assert any("staging_evidence must be one of" in e for e in errors)


def test_missing_sla_entry_for_matrix_role_is_error(base_config):
    del base_config["sla"]["tools"]
    _, errors, _ = routing.validate_raw(base_config)
    assert any("sla is missing entry for role 'tools'" in e for e in errors)


def test_missing_sla_entry_for_claims_overlay_role_is_error(base_config):
    # marketing is used by both the matrix (blog/website) and the overlay;
    # dropping it must still be caught via the matrix-usage path.
    del base_config["sla"]["marketing"]
    _, errors, _ = routing.validate_raw(base_config)
    assert any("sla is missing entry for role 'marketing'" in e for e in errors)


def test_malformed_team_slug_is_error(base_config):
    base_config["teams"]["tools"] = "docs-tools"  # missing 'org/'
    _, errors, _ = routing.validate_raw(base_config)
    assert any("not a valid 'org/slug' team reference" in e for e in errors)


def test_non_positive_business_days_is_error(base_config):
    base_config["sla"]["tools"]["business_days"] = 0
    _, errors, _ = routing.validate_raw(base_config)
    assert any("business_days must be a positive integer" in e for e in errors)


def test_negative_business_days_is_error(base_config):
    base_config["sla"]["tools"]["business_days"] = -1
    _, errors, _ = routing.validate_raw(base_config)
    assert any("business_days must be a positive integer" in e for e in errors)


def test_warn_days_gte_close_days_is_error(base_config):
    base_config["author_staleness"] = {"warn_days": 21, "close_days": 21}
    _, errors, _ = routing.validate_raw(base_config)
    assert any("must be less than" in e for e in errors)


def test_warn_days_less_than_close_days_is_valid(base_config):
    _, errors, _ = routing.validate_raw(base_config)
    assert errors == []


def test_claims_overlay_unknown_role_is_error(base_config):
    base_config["claims_overlay"]["add"] = "ghostwriters"
    _, errors, _ = routing.validate_raw(base_config)
    assert any("claims_overlay.add names unknown role" in e for e in errors)


def test_external_contributors_unknown_gate_is_error(base_config):
    base_config["external_contributors"]["skip_gates"] = ["made-up-gate"]
    _, errors, _ = routing.validate_raw(base_config)
    assert any("unknown gate" in e for e in errors)


def test_waive_missing_key_is_error(base_config):
    del base_config["waive"]["log_prefix"]
    _, errors, _ = routing.validate_raw(base_config)
    assert any("waive.log_prefix must be a non-empty string" in e for e in errors)


# ---- TODO escalate_to: valid but flagged -----------------------------------


def test_todo_escalate_to_is_warning_not_error(base_config):
    base_config["sla"]["tools"]["escalate_to"] = "TODO-tools-lead"
    cfg, errors, warnings = routing.validate_raw(base_config)
    assert errors == []
    assert cfg is not None
    assert any("TODO placeholder" in w for w in warnings)


def test_non_todo_escalate_to_produces_no_warning(base_config):
    base_config["sla"]["tools"]["escalate_to"] = "@real-human"
    base_config["sla"]["docs-guild"]["escalate_to"] = "@real-human-2"
    base_config["sla"]["marketing"]["escalate_to"] = "@real-human-3"
    _, errors, warnings = routing.validate_raw(base_config)
    assert errors == []
    assert warnings == []


# ---- load_config / real file on disk ---------------------------------------


def test_load_config_raises_on_invalid(tmp_path):
    bad = tmp_path / "bad.yml"
    bad.write_text("schema: 2\n")
    with pytest.raises(routing.RoutingConfigError):
        routing.load_config(bad)


def test_load_config_real_file_is_valid():
    cfg = routing.load_config(routing.DEFAULT_CONFIG_PATH)
    assert cfg.schema == 1
    assert "tools" in cfg.teams
    # Every escalation contact is a real handle now (2026-09-11); a TODO
    # creeping back in should be a visible test change, not a silent warning.
    assert cfg.warnings == []
    assert cfg.matrix["frontend"]["substantive"] == "marketing"
    assert cfg.matrix["other"]["substantive"] == "tools"
    assert routing.not_governed_reason(cfg, "dependabot[bot]", set())
    assert routing.not_governed_reason(cfg, "pulumi-bot", {"automation/merge"})
    assert routing.not_governed_reason(cfg, "pulumi-bot", {"surface:v3"}) is None
    assert routing.auto_approve_author(cfg, "pulumi-bot")
    assert not routing.auto_approve_author(cfg, "CamSoper")


# ---- not_governed / auto_approve ------------------------------------------


def test_not_governed_and_auto_approve_are_optional(base_config):
    del base_config["not_governed"]
    del base_config["auto_approve"]
    cfg, errors, _ = routing.validate_raw(base_config)
    assert errors == []
    assert cfg.not_governed == {} and cfg.auto_approve == {}
    assert routing.not_governed_reason(cfg, "dependabot[bot]", set()) is None
    assert routing.auto_approve_author(cfg, "pulumi-bot") is False


def test_not_governed_unknown_key_is_error(base_config):
    base_config["not_governed"]["labels"] = ["x"]
    _, errors, _ = routing.validate_raw(base_config)
    assert any("not_governed: unknown key 'labels'" in e for e in errors)


def test_not_governed_pair_missing_label_is_error(base_config):
    base_config["not_governed"]["author_label_pairs"] = [{"author": "pulumi-bot"}]
    _, errors, _ = routing.validate_raw(base_config)
    assert any("author_label_pairs[0].label" in e for e in errors)


def test_not_governed_authors_must_be_list(base_config):
    base_config["not_governed"]["authors"] = "dependabot[bot]"
    _, errors, _ = routing.validate_raw(base_config)
    assert any("not_governed.authors must be a list" in e for e in errors)


def test_auto_approve_authors_must_be_list_of_strings(base_config):
    base_config["auto_approve"]["authors"] = [""]
    _, errors, _ = routing.validate_raw(base_config)
    assert any("auto_approve.authors" in e for e in errors)


def test_not_governed_pair_needs_both_author_and_label(config):
    assert routing.not_governed_reason(config, "pulumi-bot", set()) is None
    assert routing.not_governed_reason(config, "someone", {"automation/merge"}) is None
    reason = routing.not_governed_reason(config, "pulumi-bot", {"automation/merge", "domain:docs"})
    assert reason and "automation/merge" in reason


# ---- frontend / other subjects -----------------------------------------------


def test_frontend_routes_to_marketing_without_staging_evidence(config):
    for path in ("layouts/partials/foo.html", "theme/src/scss/_x.scss",
                 "assets/fingerprinted/images/x.svg", "static/images/logo.png"):
        r = routing.resolve_lanes([path], mechanical=False, claims=False, config=config)
        assert r.roles == {"marketing"}, path
        assert r.staging_evidence_required is False, path
        assert r.subjects[path] == "frontend"


def test_other_routes_to_tools_and_dedupes_with_infra(config):
    r = routing.resolve_lanes([".claude/commands/x/SKILL.md"], mechanical=False, claims=False, config=config)
    assert r.roles == {"tools"}
    assert r.staging_evidence_required is False
    r2 = routing.resolve_lanes(
        [".github/workflows/ci.yml", ".claude/commands/x/SKILL.md", "data/versions.json"],
        mechanical=False, claims=False, config=config,
    )
    assert r2.roles == {"tools"}
    assert r2.staging_evidence_required is True


def test_content_data_files_route_with_their_content(config):
    r = routing.resolve_lanes(
        ["content/docs/foo.md", "data/docs_menu_sections.yml"],
        mechanical=False, claims=False, config=config,
    )
    assert r.roles == {"docs-guild"}
    assert r.subjects["data/docs_menu_sections.yml"] == "docs"


# ---- resolve_lanes cases ----------------------------------------------------


def test_pure_docs_mechanical_no_roles(config):
    r = routing.resolve_lanes(["content/docs/foo.md"], mechanical=True, claims=False, config=config)
    assert r.roles == set()
    assert r.staging_evidence_required is False


def test_docs_substantive_docs_guild(config):
    r = routing.resolve_lanes(["content/docs/foo.md"], mechanical=False, claims=False, config=config)
    assert r.roles == {"docs-guild"}


def test_mixed_docs_blog_substantive_both_roles(config):
    r = routing.resolve_lanes(
        ["content/docs/foo.md", "content/blog/bar/index.md"],
        mechanical=False,
        claims=False,
        config=config,
    )
    assert r.roles == {"docs-guild", "marketing"}
    assert r.subjects == {
        "content/docs/foo.md": "docs",
        "content/blog/bar/index.md": "blog",
    }


def test_any_infra_file_requires_tools_and_staging_evidence(config):
    r = routing.resolve_lanes(["scripts/build.py"], mechanical=False, claims=False, config=config)
    assert r.roles == {"tools"}
    assert r.staging_evidence_required is True


def test_infra_mixed_with_docs_still_requires_staging_evidence(config):
    r = routing.resolve_lanes(
        ["scripts/build.py", "content/docs/foo.md"],
        mechanical=False,
        claims=False,
        config=config,
    )
    assert r.roles == {"tools", "docs-guild"}
    assert r.staging_evidence_required is True


def test_infra_mechanical_still_requires_tools(config):
    # Unlike docs/blog/website/programs/other, infra requires tools even
    # for a mechanical change — the matrix says so explicitly.
    r = routing.resolve_lanes([".github/workflows/ci.yml"], mechanical=True, claims=False, config=config)
    assert r.roles == {"tools"}
    assert r.staging_evidence_required is True


def test_claims_overlay_stacks_and_forces_substantive(config):
    r = routing.resolve_lanes(["content/docs/foo.md"], mechanical=True, claims=True, config=config)
    assert r.roles == {"docs-guild", "marketing"}
    assert any("forces substantive" in reason for reason in r.reasons)


def test_claims_overlay_on_already_substantive_change(config):
    r = routing.resolve_lanes(
        ["content/blog/bar/index.md"], mechanical=False, claims=True, config=config
    )
    # marketing is both the blog-substantive role and the overlay role;
    # the set collapses to one entry either way.
    assert r.roles == {"marketing"}


def test_unclassifiable_path_is_subject_other(config):
    r = routing.resolve_lanes(["random-file-at-root.txt"], mechanical=False, claims=False, config=config)
    assert r.subjects["random-file-at-root.txt"] == "other"
    # Repo plumbing is the tools team's, and never needs a staging run.
    assert r.roles == {"tools"}
    assert r.staging_evidence_required is False


def test_no_changed_paths_resolves_to_no_roles(config):
    r = routing.resolve_lanes([], mechanical=False, claims=False, config=config)
    assert r.roles == set()
    assert r.subjects == {}


def test_resolution_to_json_shape(config):
    r = routing.resolve_lanes(["content/docs/foo.md"], mechanical=False, claims=False, config=config)
    payload = r.to_json()
    assert set(payload) == {"roles", "staging_evidence_required", "subjects", "reasons"}
    assert payload["roles"] == ["docs-guild"]


# ---- classify_path passthrough sanity --------------------------------------


def test_classify_path_is_the_real_triage_function():
    # routing.classify_path must be triage-classify.py's actual function,
    # not a reimplementation that can drift from it.
    assert routing.classify_path("content/docs/foo.md") == "domain:docs"
    assert routing.classify_path("content/blog/bar/index.md") == "domain:blog"
    assert routing.classify_path("scripts/build.py") == "domain:infra"
    assert routing.classify_path("some/unknown/path.txt") is None
