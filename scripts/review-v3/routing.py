#!/usr/bin/env python3
"""Lane-routing config loader and resolver for the v3 PR review workflow.

Reads `.github/review-routing.yml` (schema documented in that file's header
comment) and answers two questions the Sentinel merge gate, triage routing,
and the SLA sweep all need: is this config well-formed (`load_config`), and
given a PR's changed paths and change type, which roles must approve and is
staging evidence required (`resolve_lanes`).

`load_config` fails closed: any structural problem — an unknown key at any
level, a matrix cell naming a role outside `teams:`, a missing subject, a
role the matrix can hand out with no `sla:` entry, a malformed team slug, a
non-positive `business_days`, `warn_days >= close_days` — raises
`RoutingConfigError` carrying every error found, not just the first. A
`TODO-`-prefixed `sla.<role>.escalate_to` is the one deliberate exception:
those names are pending an org decision, so the parser records a warning and
keeps validating rather than treating the placeholder as invalid.

Importable (`load_config`, `resolve_lanes`) and runnable:

    routing.py validate [--config PATH]
    routing.py resolve --config PATH --mechanical {true,false} --claims {true,false} path [path ...]
    routing.py --self-test
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
DEFAULT_CONFIG_PATH = REPO_ROOT / ".github" / "review-routing.yml"

# classify_path is shared with triage — imported by path (hyphenated
# filename, main() guarded), the select-glowup.py / record-review.py
# pattern — so routing and triage labeling can never disagree about what a
# changed file is.
_TRIAGE_CLASSIFY_PATH = (
    REPO_ROOT / ".claude" / "commands" / "docs-review" / "scripts" / "triage-classify.py"
)
_spec = importlib.util.spec_from_file_location("triage_classify", _TRIAGE_CLASSIFY_PATH)
_triage_classify = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_triage_classify)
classify_path = _triage_classify.classify_path

# The closed set of subjects the matrix must cover. Matches the domains
# classify_path() can emit (docs, blog, website, programs, infra) plus
# `other`, the fallback for a path classify_path() can't place — NOTE:
# classify_path() itself returns None for an unmatched path (the
# "domain:other" fallback string lives one layer up, in triage-classify.py's
# PR-level classify_pr(), not in classify_path()); resolve_lanes() below
# does that None -> "other" mapping itself.
SUBJECTS = frozenset({"docs", "blog", "website", "programs", "infra", "other"})

CHANGE_TYPES = ("mechanical", "substantive")
MATRIX_CELL_KEYS = frozenset({"mechanical", "substantive", "staging_evidence"})
STAGING_EVIDENCE_VALUES = frozenset({"required"})

TOP_LEVEL_KEYS = frozenset({
    "schema", "teams", "bots", "matrix", "claims_overlay",
    "external_contributors", "sla", "author_staleness", "waive",
})
CLAIMS_OVERLAY_KEYS = frozenset({"add"})
EXTERNAL_CONTRIBUTORS_KEYS = frozenset({"skip_gates"})
SLA_ENTRY_KEYS = frozenset({"business_days", "escalate_to"})
AUTHOR_STALENESS_KEYS = frozenset({"warn_days", "close_days"})
WAIVE_KEYS = frozenset({"label", "log_prefix"})

# Closed vocabulary for external_contributors.skip_gates. Add a gate id here
# when the Sentinel grows a new gate that a fork PR can legitimately skip.
KNOWN_GATES = frozenset({"review-ran", "findings-answered"})

TEAM_SLUG_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


class RoutingConfigError(Exception):
    """Raised by load_config when the routing config fails validation.

    Carries every error found (not just the first), because a config author
    fixing one typo at a time against single-error feedback is the failure
    mode this exists to avoid.
    """

    def __init__(self, errors: list[str]):
        super().__init__("; ".join(errors))
        self.errors = errors


@dataclass
class Config:
    schema: int
    teams: dict[str, str]
    bots: list[str]
    matrix: dict[str, dict[str, str]]
    claims_overlay: dict
    external_contributors: dict
    sla: dict[str, dict]
    author_staleness: dict
    waive: dict
    warnings: list[str] = field(default_factory=list)


@dataclass
class Resolution:
    roles: set[str]
    staging_evidence_required: bool
    subjects: dict[str, str]  # changed path -> subject
    reasons: list[str]

    def to_json(self) -> dict:
        return {
            "roles": sorted(self.roles),
            "staging_evidence_required": self.staging_evidence_required,
            "subjects": self.subjects,
            "reasons": self.reasons,
        }


def _is_nonempty_str(v) -> bool:
    return isinstance(v, str) and bool(v.strip())


def _check_unknown_keys(d: dict, allowed: frozenset, where: str, errors: list[str]) -> None:
    for key in d:
        if key not in allowed:
            errors.append(f"{where}: unknown key {key!r}")


def validate_raw(raw: dict) -> tuple[Config | None, list[str], list[str]]:
    """Validate a parsed routing config. Returns (config_or_None, errors, warnings).

    config is None whenever errors is non-empty — a config with any error is
    never handed back for use, per the fail-closed contract.
    """
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(raw, dict):
        return None, ["routing config must be a YAML mapping at the top level"], []

    _check_unknown_keys(raw, TOP_LEVEL_KEYS, "top level", errors)

    schema = raw.get("schema")
    if schema != 1:
        errors.append(f"schema must be 1, got {schema!r}")

    # ---- teams --------------------------------------------------------
    teams = raw.get("teams")
    if not isinstance(teams, dict) or not teams:
        errors.append("teams must be a non-empty mapping of role -> 'org/slug'")
        teams = {}
    else:
        for role, slug in teams.items():
            if not _is_nonempty_str(slug) or not TEAM_SLUG_RE.match(slug):
                errors.append(
                    f"teams.{role} is not a valid 'org/slug' team reference: {slug!r}"
                )

    # ---- bots -----------------------------------------------------------
    bots = raw.get("bots", [])
    if not isinstance(bots, list) or not all(_is_nonempty_str(b) for b in bots):
        errors.append("bots must be a list of non-empty strings")
        bots = []

    # ---- matrix -----------------------------------------------------------
    matrix = raw.get("matrix")
    matrix_roles_used: set[str] = set()
    if not isinstance(matrix, dict):
        errors.append("matrix must be a mapping of subject -> cell")
        matrix = {}
    else:
        missing_subjects = SUBJECTS - matrix.keys()
        for subject in sorted(missing_subjects):
            errors.append(f"matrix is missing required subject {subject!r}")
        extra_subjects = matrix.keys() - SUBJECTS
        for subject in sorted(extra_subjects):
            errors.append(f"matrix names unknown subject {subject!r}")

        for subject, cell in matrix.items():
            if subject not in SUBJECTS:
                continue
            if not isinstance(cell, dict):
                errors.append(f"matrix.{subject} must be a mapping")
                continue
            _check_unknown_keys(cell, MATRIX_CELL_KEYS, f"matrix.{subject}", errors)
            for change_type in CHANGE_TYPES:
                if change_type not in cell:
                    errors.append(f"matrix.{subject} is missing {change_type!r}")
                    continue
                role = cell[change_type]
                if role == "none":
                    continue
                if not _is_nonempty_str(role) or role not in teams:
                    errors.append(
                        f"matrix.{subject}.{change_type} names unknown role "
                        f"{role!r} (not in teams)"
                    )
                    continue
                matrix_roles_used.add(role)
            if "staging_evidence" in cell and cell["staging_evidence"] not in STAGING_EVIDENCE_VALUES:
                errors.append(
                    f"matrix.{subject}.staging_evidence must be one of "
                    f"{sorted(STAGING_EVIDENCE_VALUES)}, got {cell['staging_evidence']!r}"
                )

    # ---- claims_overlay -----------------------------------------------
    claims_overlay = raw.get("claims_overlay")
    if not isinstance(claims_overlay, dict):
        errors.append("claims_overlay must be a mapping with an 'add' key")
        claims_overlay = {}
    else:
        _check_unknown_keys(claims_overlay, CLAIMS_OVERLAY_KEYS, "claims_overlay", errors)
        add_role = claims_overlay.get("add")
        if not _is_nonempty_str(add_role) or add_role not in teams:
            errors.append(
                f"claims_overlay.add names unknown role {add_role!r} (not in teams)"
            )
        else:
            matrix_roles_used.add(add_role)

    # ---- external_contributors ------------------------------------------
    external_contributors = raw.get("external_contributors")
    if not isinstance(external_contributors, dict):
        errors.append("external_contributors must be a mapping with a 'skip_gates' key")
        external_contributors = {}
    else:
        _check_unknown_keys(
            external_contributors, EXTERNAL_CONTRIBUTORS_KEYS, "external_contributors", errors
        )
        skip_gates = external_contributors.get("skip_gates")
        if not isinstance(skip_gates, list):
            errors.append("external_contributors.skip_gates must be a list")
        else:
            for gate in skip_gates:
                if gate not in KNOWN_GATES:
                    errors.append(
                        f"external_contributors.skip_gates names unknown gate {gate!r} "
                        f"(known gates: {sorted(KNOWN_GATES)})"
                    )

    # ---- sla ----------------------------------------------------------
    sla = raw.get("sla")
    if not isinstance(sla, dict):
        errors.append("sla must be a mapping of role -> {business_days, escalate_to}")
        sla = {}
    else:
        for role, entry in sla.items():
            if not isinstance(entry, dict):
                errors.append(f"sla.{role} must be a mapping")
                continue
            _check_unknown_keys(entry, SLA_ENTRY_KEYS, f"sla.{role}", errors)
            business_days = entry.get("business_days")
            if not isinstance(business_days, int) or isinstance(business_days, bool) or business_days <= 0:
                errors.append(
                    f"sla.{role}.business_days must be a positive integer, got {business_days!r}"
                )
            escalate_to = entry.get("escalate_to")
            if not _is_nonempty_str(escalate_to):
                errors.append(f"sla.{role}.escalate_to must be a non-empty string")
            elif escalate_to.startswith("TODO"):
                warnings.append(
                    f"sla.{role}.escalate_to is a TODO placeholder: {escalate_to!r}"
                )
        for role in sorted(matrix_roles_used):
            if role not in sla:
                errors.append(f"sla is missing entry for role {role!r} (used in matrix)")

    # ---- author_staleness -----------------------------------------------
    author_staleness = raw.get("author_staleness")
    if not isinstance(author_staleness, dict):
        errors.append("author_staleness must be a mapping with 'warn_days' and 'close_days'")
        author_staleness = {}
    else:
        _check_unknown_keys(author_staleness, AUTHOR_STALENESS_KEYS, "author_staleness", errors)
        warn_days = author_staleness.get("warn_days")
        close_days = author_staleness.get("close_days")
        for key, value in (("warn_days", warn_days), ("close_days", close_days)):
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                errors.append(f"author_staleness.{key} must be a positive integer, got {value!r}")
        if (
            isinstance(warn_days, int) and not isinstance(warn_days, bool)
            and isinstance(close_days, int) and not isinstance(close_days, bool)
            and warn_days >= close_days
        ):
            errors.append(
                f"author_staleness.warn_days ({warn_days}) must be less than "
                f"close_days ({close_days})"
            )

    # ---- waive ----------------------------------------------------------
    waive = raw.get("waive")
    if not isinstance(waive, dict):
        errors.append("waive must be a mapping with 'label' and 'log_prefix'")
        waive = {}
    else:
        _check_unknown_keys(waive, WAIVE_KEYS, "waive", errors)
        for key in WAIVE_KEYS:
            if not _is_nonempty_str(waive.get(key)):
                errors.append(f"waive.{key} must be a non-empty string")

    if errors:
        return None, errors, warnings

    config = Config(
        schema=schema,
        teams=teams,
        bots=bots,
        matrix=matrix,
        claims_overlay=claims_overlay,
        external_contributors=external_contributors,
        sla=sla,
        author_staleness=author_staleness,
        waive=waive,
        warnings=warnings,
    )
    return config, errors, warnings


def load_config(path: Path | str) -> Config:
    """Load and validate the routing config at `path`.

    Raises RoutingConfigError (carrying every error found) on any invalid
    config. A TODO-prefixed sla.*.escalate_to does not raise — it lands in
    the returned Config's `warnings` list instead.
    """
    path = Path(path)
    try:
        raw = yaml.safe_load(path.read_text())
    except OSError as e:
        raise RoutingConfigError([f"cannot read {path}: {e}"]) from e
    except yaml.YAMLError as e:
        raise RoutingConfigError([f"{path} is not valid YAML: {e}"]) from e

    config, errors, _warnings = validate_raw(raw)
    if errors:
        raise RoutingConfigError(errors)
    return config


def resolve_lanes(
    changed_paths: list[str], mechanical: bool, claims: bool, config: Config
) -> Resolution:
    """Resolve the required roles and staging-evidence requirement for a PR.

    Subject is decided per file via classify_path() (shared with triage); an
    unclassifiable path (classify_path returns None) is subject "other".
    Mixed subjects union their roles. claims=True stacks
    config.claims_overlay's role on top of whatever the matrix resolved, and
    forces the change type to substantive regardless of `mechanical` — a
    claims-flagged change is never treated as mechanical.
    """
    reasons: list[str] = []
    subjects: dict[str, str] = {}

    for path in changed_paths:
        label = classify_path(path)
        subject = label.split(":", 1)[1] if label else "other"
        subjects[path] = subject
        reasons.append(f"{path} -> subject:{subject}")

    effective_mechanical = mechanical
    if claims and mechanical:
        effective_mechanical = False
        reasons.append("claims signal forces substantive (mechanical input overridden)")
    change_type = "mechanical" if effective_mechanical else "substantive"
    reasons.append(f"change type: {change_type}")

    roles: set[str] = set()
    staging_evidence_required = False

    for subject in sorted(set(subjects.values())):
        cell = config.matrix[subject]
        role = cell[change_type]
        if role != "none":
            roles.add(role)
            reasons.append(f"subject:{subject}/{change_type} -> role:{role}")
        else:
            reasons.append(f"subject:{subject}/{change_type} -> none")
        if cell.get("staging_evidence") == "required":
            staging_evidence_required = True
            reasons.append(f"subject:{subject} requires staging evidence")

    if claims:
        overlay_role = config.claims_overlay["add"]
        roles.add(overlay_role)
        reasons.append(f"claims overlay adds role:{overlay_role}")

    return Resolution(
        roles=roles,
        staging_evidence_required=staging_evidence_required,
        subjects=subjects,
        reasons=reasons,
    )


# ---- self-test --------------------------------------------------------

_CANNED_CONFIG = {
    "schema": 1,
    "teams": {
        "docs-guild": "pulumi/docs-guild",
        "marketing": "pulumi/docs-marketing-review",
        "tools": "pulumi/docs-tools",
    },
    "bots": ["pulumi-bot"],
    "matrix": {
        "docs": {"mechanical": "none", "substantive": "docs-guild"},
        "blog": {"mechanical": "none", "substantive": "marketing"},
        "website": {"mechanical": "none", "substantive": "marketing"},
        "programs": {"mechanical": "none", "substantive": "docs-guild"},
        "infra": {"mechanical": "tools", "substantive": "tools", "staging_evidence": "required"},
        "other": {"mechanical": "none", "substantive": "docs-guild"},
    },
    "claims_overlay": {"add": "marketing"},
    "external_contributors": {"skip_gates": ["review-ran", "findings-answered"]},
    "sla": {
        "tools": {"business_days": 1, "escalate_to": "TODO-tools-lead"},
        "docs-guild": {"business_days": 3, "escalate_to": "TODO-owning-manager"},
        "marketing": {"business_days": 3, "escalate_to": "TODO-named-fallback"},
    },
    "author_staleness": {"warn_days": 14, "close_days": 21},
    "waive": {"label": "review:waived", "log_prefix": "pr-review/waives/"},
}


def self_test() -> int:
    import copy

    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    config, errors, warnings = validate_raw(copy.deepcopy(_CANNED_CONFIG))
    check("canned config is valid", errors == [])
    check("canned config flags TODO escalate_to as warnings", len(warnings) == 3)

    # ---- real config on disk ------------------------------------------
    try:
        real = load_config(DEFAULT_CONFIG_PATH)
        check("real .github/review-routing.yml loads", True)
        check("real config carries TODO warnings", len(real.warnings) > 0)
    except RoutingConfigError as e:
        check(f"real .github/review-routing.yml loads ({e.errors})", False)

    # ---- resolve_lanes cases -------------------------------------------
    r = resolve_lanes(["content/docs/foo.md"], mechanical=True, claims=False, config=config)
    check("pure docs mechanical -> no roles", r.roles == set())

    r = resolve_lanes(["content/docs/foo.md"], mechanical=False, claims=False, config=config)
    check("pure docs substantive -> docs-guild", r.roles == {"docs-guild"})

    r = resolve_lanes(
        ["content/docs/foo.md", "content/blog/bar/index.md"],
        mechanical=False, claims=False, config=config,
    )
    check("mixed docs+blog substantive -> both roles", r.roles == {"docs-guild", "marketing"})

    r = resolve_lanes(
        ["content/docs/foo.md", "scripts/build.py"],
        mechanical=False, claims=False, config=config,
    )
    check("mixed docs+infra -> tools + docs-guild", r.roles == {"docs-guild", "tools"})
    check("infra file -> staging evidence required", r.staging_evidence_required is True)

    r = resolve_lanes(["content/docs/foo.md"], mechanical=True, claims=True, config=config)
    check("claims overlay adds marketing", "marketing" in r.roles)
    check("claims overlay forces substantive", r.roles == {"docs-guild", "marketing"})

    r = resolve_lanes(["some/unknown/path.txt"], mechanical=False, claims=False, config=config)
    check("unclassifiable path routed as subject:other", r.subjects["some/unknown/path.txt"] == "other")

    # ---- validation failure modes ---------------------------------------
    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["nope"] = True
    _, errs, _ = validate_raw(bad)
    check("unknown top-level key rejected", any("unknown key" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["schema"] = 2
    _, errs, _ = validate_raw(bad)
    check("schema != 1 rejected", any("schema must be 1" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["matrix"]["docs"]["substantive"] = "ghostwriters"
    _, errs, _ = validate_raw(bad)
    check("matrix role absent from teams rejected", any("unknown role" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    del bad["matrix"]["infra"]
    _, errs, _ = validate_raw(bad)
    check("missing subject rejected", any("missing required subject 'infra'" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    del bad["sla"]["tools"]
    _, errs, _ = validate_raw(bad)
    check("missing sla entry for matrix role rejected", any("sla is missing entry" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["teams"]["tools"] = "not-a-slug"
    _, errs, _ = validate_raw(bad)
    check("malformed team slug rejected", any("not a valid 'org/slug'" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["sla"]["tools"]["business_days"] = 0
    _, errs, _ = validate_raw(bad)
    check("non-positive business_days rejected", any("business_days must be a positive" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["author_staleness"] = {"warn_days": 21, "close_days": 14}
    _, errs, _ = validate_raw(bad)
    check("warn_days >= close_days rejected", any("must be less than" in e for e in errs))

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall routing self-tests passed")
    return 0


# ---- CLI ----------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Lane-routing config loader and resolver.")
    parser.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    sub = parser.add_subparsers(dest="command")

    p_validate = sub.add_parser("validate", help="validate a routing config")
    p_validate.add_argument("--config", default=str(DEFAULT_CONFIG_PATH))

    p_resolve = sub.add_parser("resolve", help="resolve required roles for changed paths")
    p_resolve.add_argument("--config", required=True)
    p_resolve.add_argument("--mechanical", choices=("true", "false"), required=True)
    p_resolve.add_argument("--claims", choices=("true", "false"), required=True)
    p_resolve.add_argument("paths", nargs="*")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    if args.command == "validate":
        try:
            config = load_config(args.config)
        except RoutingConfigError as e:
            for msg in e.errors:
                print(f"routing: {msg}", file=sys.stderr)
            return 1
        for msg in config.warnings:
            print(f"routing: warning: {msg}", file=sys.stderr)
        print(f"routing: {args.config} is valid")
        return 0

    if args.command == "resolve":
        try:
            config = load_config(args.config)
        except RoutingConfigError as e:
            for msg in e.errors:
                print(f"routing: {msg}", file=sys.stderr)
            return 1
        resolution = resolve_lanes(
            args.paths,
            mechanical=args.mechanical == "true",
            claims=args.claims == "true",
            config=config,
        )
        json.dump(resolution.to_json(), sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0

    parser.error("pass a command (validate, resolve) or --self-test")
    return 2


if __name__ == "__main__":
    sys.exit(main())
