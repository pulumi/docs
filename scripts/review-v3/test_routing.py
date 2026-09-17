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


@pytest.mark.parametrize("change_type", ["mechanical", "substantive"])
def test_matrix_role_none_is_now_an_error(base_config, change_type):
    """Every governed PR must resolve to an approver team.

    `none` used to mean "no human gate", which was only ever true inside the
    Sentinel — GitHub's required-review rule doesn't read this config. So a
    `none` cell removed the reviewer request and told the author nobody was
    needed, while a human stamped it by hand anyway. The parser rejects it
    now so the assumption can't be reintroduced quietly.
    """
    base_config["matrix"]["docs"][change_type] = "none"
    _, errors, _ = routing.validate_raw(base_config)
    assert any(f"matrix.docs.{change_type} is 'none'" in e for e in errors)
    # The message has to name the alternatives, or the next person just
    # picks a team at random to get past it.
    assert any("mechanical" in e and "not_governed" in e for e in errors)


def test_matrix_missing_subject_is_error(base_config):
    del base_config["matrix"]["website"]
    _, errors, _ = routing.validate_raw(base_config)
    assert any("missing required subject 'website'" in e for e in errors)


def test_matrix_unknown_subject_is_error(base_config):
    base_config["matrix"]["gadgets"] = {"mechanical": "tools", "substantive": "tools"}
    _, errors, _ = routing.validate_raw(base_config)
    assert any("unknown subject 'gadgets'" in e for e in errors)


def test_matrix_cell_unknown_key_is_error(base_config):
    base_config["matrix"]["docs"]["surprise"] = "tools"
    _, errors, _ = routing.validate_raw(base_config)
    assert any("matrix.docs: unknown key 'surprise'" in e for e in errors)


def test_retired_matrix_staging_evidence_key_is_error(base_config):
    """`staging_evidence` moved out of the matrix and onto its own
    path-keyed section. A config that still carries the cell must fail
    closed — silently ignoring it would drop gate G4 for every path."""
    base_config["matrix"]["infra"]["staging_evidence"] = "required"
    _, errors, _ = routing.validate_raw(base_config)
    assert any("matrix.infra: unknown key 'staging_evidence'" in e for e in errors)


def test_staging_evidence_section_is_required(base_config):
    del base_config["staging_evidence"]
    _, errors, _ = routing.validate_raw(base_config)
    assert any("staging_evidence must be a mapping" in e for e in errors)


def test_staging_evidence_unknown_key_is_error(base_config):
    base_config["staging_evidence"]["surprise"] = True
    _, errors, _ = routing.validate_raw(base_config)
    assert any("staging_evidence: unknown key 'surprise'" in e for e in errors)


@pytest.mark.parametrize("paths", [[], "infrastructure/", None, {}])
def test_staging_evidence_paths_must_be_a_nonempty_list(base_config, paths):
    base_config["staging_evidence"]["paths"] = paths
    _, errors, _ = routing.validate_raw(base_config)
    assert any("staging_evidence.paths must be a non-empty list" in e for e in errors)


def test_staging_evidence_paths_rejects_blank_and_absolute(base_config):
    base_config["staging_evidence"]["paths"] = ["infrastructure/", "  ", "/Makefile"]
    _, errors, _ = routing.validate_raw(base_config)
    assert any("staging_evidence.paths[1] must be a non-empty string" in e for e in errors)
    assert any("staging_evidence.paths[2] must be repo-root-relative" in e for e in errors)


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
    assert routing.not_governed_reason(cfg, "pulumi-bot", {"domain:docs"}) is None
    # Every cell routes somewhere — no unrouted lanes in the live config.
    for subject, cell in cfg.matrix.items():
        for change_type in routing.CHANGE_TYPES:
            assert cell[change_type] in cfg.teams, (subject, change_type)
    # Every bot that opens PRs on this repo is on the denylist.
    assert {"pulumi-bot", "workprentice[bot]", "github-copilot[bot]",
            "eon-pulumi-agent[bot]", "dependabot[bot]"} <= set(cfg.bots)
    assert not hasattr(cfg, "auto_approve")


# ---- not_governed ---------------------------------------------------------


def test_not_governed_is_optional(base_config):
    del base_config["not_governed"]
    cfg, errors, _ = routing.validate_raw(base_config)
    assert errors == []
    assert cfg.not_governed == {}
    assert routing.not_governed_reason(cfg, "dependabot[bot]", set()) is None


def test_retired_auto_approve_section_is_error(base_config):
    """`auto_approve` let a bot author pass G3 with no approval at all.

    Nothing consumed the flag it set, and GitHub's required review doesn't
    read this file, so it only made G3 report a pass the merge box
    disagreed with. Deleted — and a config still carrying it fails closed
    rather than having the key silently ignored.
    """
    base_config["auto_approve"] = {"authors": ["pulumi-bot"]}
    _, errors, _ = routing.validate_raw(base_config)
    assert any("unknown key 'auto_approve'" in e for e in errors)


def test_auto_approve_helper_is_gone():
    assert not hasattr(routing, "auto_approve_author")


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
    # subject:infra, but an arbitrary workflow is not on staging_evidence.paths.
    assert r2.staging_evidence_required is False


def test_content_data_files_route_with_their_content(config):
    r = routing.resolve_lanes(
        ["content/docs/foo.md", "data/docs_menu_sections.yml"],
        mechanical=False, claims=False, config=config,
    )
    assert r.roles == {"docs-guild"}
    assert r.subjects["data/docs_menu_sections.yml"] == "docs"


# ---- resolve_lanes cases ----------------------------------------------------


def test_pure_docs_mechanical_still_routes_to_the_lane_team(config):
    """`mechanical` skips the model review, not the approver.

    It used to resolve to no roles, which meant no reviewer was requested
    and G3 reported "no human approval required" — on a repo whose own
    rules require an approving review regardless.
    """
    r = routing.resolve_lanes(["content/docs/foo.md"], mechanical=True, claims=False, config=config)
    assert r.roles == {"docs-guild"}
    assert r.staging_evidence_required is False


def test_no_governed_path_resolves_to_zero_roles(config):
    """The invariant behind "every PR is routed": for every subject and
    both change types, some team is always on the hook."""
    for path in ("content/docs/a.md", "content/blog/b/index.md",
                 "content/pricing.md", "static/programs/p/index.ts",
                 "scripts/x.sh", "layouts/y.html", "unplaceable.xyz"):
        for mechanical in (True, False):
            r = routing.resolve_lanes([path], mechanical=mechanical,
                                      claims=False, config=config)
            assert r.roles, (path, mechanical)


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


def test_any_infra_file_requires_tools(config):
    r = routing.resolve_lanes(["scripts/build.py"], mechanical=False, claims=False, config=config)
    assert r.roles == {"tools"}
    # subject:infra decides the approver. It does not decide staging.
    assert r.staging_evidence_required is False


def test_one_staging_path_mixed_with_docs_still_requires_staging_evidence(config):
    r = routing.resolve_lanes(
        ["scripts/run-pulumi.sh", "content/docs/foo.md"],
        mechanical=False,
        claims=False,
        config=config,
    )
    assert r.roles == {"tools", "docs-guild"}
    assert r.staging_evidence_required is True
    assert any("staging evidence required: scripts/run-pulumi.sh" in x for x in r.reasons)


def test_infra_mechanical_still_requires_tools(config):
    # Unlike docs/blog/website/programs/other, infra requires tools even
    # for a mechanical change — the matrix says so explicitly.
    r = routing.resolve_lanes([".github/workflows/ci.yml"], mechanical=True, claims=False, config=config)
    assert r.roles == {"tools"}


def test_staging_evidence_is_independent_of_change_type(config):
    """G4 asks "could this alter the deploy", which a one-character diff
    answers the same way a rewrite does. Mechanical must not buy a pass."""
    for mechanical in (True, False):
        r = routing.resolve_lanes(
            ["infrastructure/index.ts"], mechanical=mechanical, claims=False, config=config
        )
        assert r.staging_evidence_required is True, mechanical


def test_staging_evidence_reason_is_recorded_either_way(config):
    hit = routing.resolve_lanes(["Makefile"], mechanical=False, claims=False, config=config)
    assert any("staging evidence required: Makefile" in x for x in hit.reasons)
    miss = routing.resolve_lanes(
        ["content/docs/foo.md"], mechanical=False, claims=False, config=config
    )
    assert any("no changed path requires staging evidence" in x for x in miss.reasons)


# ---- the path matcher ------------------------------------------------------


@pytest.mark.parametrize("pattern,path,want", [
    # A trailing slash is the whole subtree, however deep.
    ("infrastructure/", "infrastructure/index.ts", True),
    ("infrastructure/", "infrastructure/a/b/c.ts", True),
    # ...but not the bare directory name, and not a sibling with a prefix.
    ("infrastructure/", "infrastructure", False),
    ("infrastructure/", "infrastructure-old/index.ts", False),
    # An exact path is exact.
    ("Makefile", "Makefile", True),
    ("Makefile", "Makefile.local", False),
    ("Makefile", "theme/Makefile", False),
    # `*` stays inside one segment — the property fnmatch does NOT have, and
    # the reason this matcher is hand-rolled.
    ("scripts/*.sh", "scripts/ci-push.sh", True),
    ("scripts/*.sh", "scripts/redirects/thing.sh", False),
    ("webpack.*.js", "webpack.config.js", True),
    ("webpack.*.js", "webpack.config.prod.js", True),
    ("webpack.*.js", "theme/webpack.config.js", False),
])
def test_pattern_matcher_segment_semantics(pattern, path, want):
    assert bool(routing._pattern_to_regex(pattern).match(path)) is want


def test_patterns_are_compiled_once_per_config(config):
    first = routing.staging_evidence_patterns(config)
    assert routing.staging_evidence_patterns(config) is first


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


def test_link_only_any_team_policy():
    cfg = routing.validate_raw({**copy.deepcopy(routing._CANNED_CONFIG), "link_only": {"approval": "any-team"}})[0]
    lane = routing.validate_raw({**copy.deepcopy(routing._CANNED_CONFIG), "link_only": {"approval": "lane"}})[0]
    paths = ["content/blog/p/index.md"]
    # a link-only sweep: the lane's role stays on the record, but any team
    # in teams: satisfies it
    res = routing.resolve_lanes(paths, False, False, cfg, link_only=True)
    assert res.roles == {"marketing"} and res.any_team is True
    assert any("any team" in r for r in res.reasons)
    # not link-only, or the lane policy: the ordinary rule
    assert routing.resolve_lanes(paths, False, False, cfg, link_only=False).any_team is False
    assert routing.resolve_lanes(paths, False, False, lane, link_only=True).any_team is False
    # A mechanical link-only sweep is still routed (mechanical no longer
    # means "nobody"), so any-team applies to it the same way.
    mech = routing.resolve_lanes(paths, True, False, cfg, link_only=True)
    assert mech.roles == {"marketing"} and mech.any_team is True
    # and the key is validated
    bad = routing.validate_raw({**copy.deepcopy(routing._CANNED_CONFIG), "link_only": {"approval": "whoever"}})
    assert bad[0] is None and any("link_only.approval" in e for e in bad[1])


def test_resolution_to_json_shape(config):
    r = routing.resolve_lanes(["content/docs/foo.md"], mechanical=False, claims=False, config=config)
    payload = r.to_json()
    assert set(payload) == {"roles", "staging_evidence_required", "subjects", "reasons", "any_team"}
    assert payload["roles"] == ["docs-guild"]


# ---- classify_path passthrough sanity --------------------------------------


def test_classify_path_is_the_real_triage_function():
    # routing.classify_path must be triage-classify.py's actual function,
    # not a reimplementation that can drift from it.
    assert routing.classify_path("content/docs/foo.md") == "domain:docs"
    assert routing.classify_path("content/blog/bar/index.md") == "domain:blog"
    assert routing.classify_path("scripts/build.py") == "domain:infra"
    assert routing.classify_path("some/unknown/path.txt") is None


def _real_lanes(paths):
    cfg = routing.load_config(str(routing.DEFAULT_CONFIG_PATH))
    return routing.resolve_lanes(paths, False, [], cfg)


def test_the_review_pipelines_need_no_staging_run():
    """A staging deploy demonstrates that the site still builds. Nothing in
    `scripts/review-v3/` and its sibling pipelines is read by the build, so
    the deploy demonstrated nothing about them.

    They are `subject:other` (which buys them a free `mechanical` cell) and
    they are absent from `staging_evidence.paths` (which is what actually
    keeps them off gate G4 now)."""
    for d in ("review-v3", "review-admin", "content-review", "blog-review"):
        r = _real_lanes([f"scripts/{d}/thing.py"])
        assert set(r.subjects.values()) == {"other"}, (d, r.subjects)
        assert r.staging_evidence_required is False, d
        assert "tools" in r.roles, (d, r.roles)


def test_real_config_staging_gate_covers_the_deploy_and_nothing_else():
    """The live `staging_evidence.paths` list, asserted against the paths it
    is meant to catch and the ones it is meant to let through.

    The let-through half is the point of the section. `scripts/redirects/`
    is the case that forced it (PR #21698): `domain:infra`, so it used to
    demand a ~9-minute deploy of a shared, lock-contended stack to prove
    that a two-line redirect data file parsed."""
    requires = (
        # The Pulumi program and the build entry points.
        "infrastructure/index.ts",
        "infrastructure/Pulumi.www-testing.yaml",
        "Makefile",
        "package.json",
        # The scripts `make ci_push` executes, and the subtrees they run.
        "scripts/ci-push.sh",
        "scripts/build-site.sh",
        "scripts/run-pulumi.sh",
        "scripts/sync-and-test-bucket.sh",
        "scripts/make-s3-redirects.js",
        "scripts/await-in-progress.js",
        "scripts/search/main.js",
        "scripts/meta-images/render.mjs",
        "scripts/content/generate-docs-content.js",
        "scripts/versioned-docs/inject-live-sdk-selectors.sh",
        # The two workflows that run it.
        ".github/workflows/build-and-deploy.yml",
        ".github/workflows/testing-build-and-deploy.yml",
    )
    for path in requires:
        assert _real_lanes([path]).staging_evidence_required is True, path

    exempt = (
        # Data the deploy reads but cannot be broken by. The #21698 case.
        "scripts/redirects/general-broken-links-redirects.txt",
        # Tooling that never runs during a deploy.
        "scripts/review-v3/sentinel.py",
        "scripts/lint/lint-markdown.js",
        "scripts/link-checker/check.js",
        "scripts/social/post.js",
        "scripts/serve.sh",
        "scripts/fetch-github-stars.js",
        # Workflows that are not the deploy.
        ".github/workflows/blog-review-index.yml",
        ".github/workflows/review-sentinel.yml",
        ".github/workflows/check-links.yml",
        # Content, templates, styles.
        "content/blog/foo/index.md",
        "layouts/partials/foo.html",
        "theme/src/scss/main.scss",
    )
    for path in exempt:
        assert _real_lanes([path]).staging_evidence_required is False, path


def test_staging_gate_is_per_path_not_per_pr():
    """One deploy-touching path in the diff arms the gate for the whole PR,
    and the approver is unchanged either way — this section narrows what
    must be demonstrated, not who signs off."""
    mixed = _real_lanes(["scripts/review-v3/act.py", "scripts/run-pulumi.sh"])
    assert mixed.staging_evidence_required is True

    assert (set(_real_lanes(["scripts/review-v3/act.py"]).roles)
            == set(_real_lanes(["Makefile"]).roles)
            == {"tools"})


def test_pr_21698_needs_no_staging_run():
    """The regression this section exists for, verbatim: two blog posts and
    one redirect data file went red on G4 for a staging deploy that raced
    another run for the shared stack and 409'd."""
    r = _real_lanes([
        "content/blog/azure-v6-release/index.md",
        "content/blog/why-azure-resource-manager-templates-suck-for-deployments/index.md",
        "scripts/redirects/general-broken-links-redirects.txt",
    ])
    assert r.staging_evidence_required is False
    # Still reviewed by both lanes; only the deploy requirement is gone.
    assert r.roles == {"blog", "tools"}
