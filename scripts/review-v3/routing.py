#!/usr/bin/env python3
"""Lane-routing config loader and resolver for the v3 PR review workflow.

Reads `.github/review-routing.yml` (schema documented in that file's header
comment) and answers two questions the Sentinel merge gate, triage routing,
and the SLA sweep all need: is this config well-formed (`load_config`), and
given a PR's changed paths and change type, which roles must approve and is
staging evidence required (`resolve_lanes`).

`load_config` fails closed: any structural problem — an unknown key at any
level, a matrix cell naming a role outside `teams:` or the retired literal
`none`, a missing subject, a role the matrix can hand out with no `sla:`
entry, a malformed team slug, a non-positive `business_days`,
`warn_days >= close_days` — raises
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
# classify_path() can emit (docs, blog, website, programs, infra, frontend)
# plus `other`, the fallback for a path classify_path() can't place — NOTE:
# classify_path() itself returns None for an unmatched path (the
# "domain:other" fallback string lives one layer up, in triage-classify.py's
# PR-level classify_pr(), not in classify_path()); resolve_lanes() below
# does that None -> "other" mapping itself.
SUBJECTS = frozenset({"docs", "blog", "website", "programs", "infra", "frontend", "other"})

CHANGE_TYPES = ("mechanical", "substantive")
# `staging_evidence` was a matrix cell key until it moved to its own
# path-keyed top-level section; it is NOT accepted here any more, so a config
# that still carries it fails closed and loud rather than silently dropping
# the gate. See STAGING EVIDENCE in the yaml header.
MATRIX_CELL_KEYS = frozenset({"mechanical", "substantive"})

TOP_LEVEL_KEYS = frozenset({
    "schema", "teams", "bots", "matrix", "overrides", "staging_evidence",
    "claims_overlay", "approval", "external_contributors", "sla",
    "author_staleness", "waive", "not_governed", "link_only",
})
STAGING_EVIDENCE_KEYS = frozenset({"paths"})
OVERRIDE_KEYS = frozenset({"paths", "role", "why"})
CLAIMS_OVERLAY_KEYS = frozenset({"add"})
EXTERNAL_CONTRIBUTORS_KEYS = frozenset({"skip_gates"})
SLA_ENTRY_KEYS = frozenset({"business_days", "escalate_to"})
AUTHOR_STALENESS_KEYS = frozenset({"warn_days", "close_days"})
WAIVE_KEYS = frozenset({"label", "log_prefix"})
NOT_GOVERNED_KEYS = frozenset({"authors", "author_label_pairs"})
AUTHOR_LABEL_PAIR_KEYS = frozenset({"author", "label"})
APPROVAL_KEYS = frozenset({"scope", "admins_satisfy"})
# Who can satisfy the approver gate (G3) on an ordinary PR. `lane` is the
# per-subject rule the matrix resolves; `any-team` says a member of any team
# in `teams:` satisfies it, whatever the matrix routed. The matrix still
# decides who gets REQUESTED — scope only decides who can clear the gate.
APPROVAL_SCOPE = frozenset({"lane", "any-team"})

LINK_ONLY_KEYS = frozenset({"approval"})
# Who may approve a diff whose every changed line differs only in a link.
# `lane` is the ordinary rule: the subject's own team. `any-team` says any
# team in `teams:` satisfies it, because checking a retargeted link needs a
# careful human, not a particular lane's human.
LINK_ONLY_APPROVAL = frozenset({"lane", "any-team"})

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
    overrides: list
    staging_evidence: dict
    claims_overlay: dict
    external_contributors: dict
    sla: dict[str, dict]
    author_staleness: dict
    waive: dict
    # Optional in the file (absent == empty): the automated processes the
    # Sentinel does not govern at all. See the yaml header for the semantics.
    not_governed: dict = field(default_factory=dict)
    link_only: dict = field(default_factory=dict)
    approval: dict = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)


@dataclass
class Resolution:
    roles: set[str]
    staging_evidence_required: bool
    subjects: dict[str, str]  # changed path -> subject
    # changed path -> role, for paths an `overrides` entry claimed. Their
    # subject is still in `subjects`; only the approver changed.
    overridden: dict[str, str]
    reasons: list[str]
    # True when any team in `teams:` satisfies the approver gate instead of
    # the lane's own team — either repo-wide (`approval.scope: any-team`) or
    # for this diff alone (`link_only.approval: any-team`).
    any_team: bool = False

    def to_json(self) -> dict:
        return {
            "roles": sorted(self.roles),
            "staging_evidence_required": self.staging_evidence_required,
            "subjects": self.subjects,
            "overridden": self.overridden,
            "reasons": self.reasons,
            "any_team": self.any_team,
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
                    # Every governed PR must resolve to an approver team. A
                    # `none` cell used to mean "no human gate", which was only
                    # ever true inside the Sentinel — GitHub's required-review
                    # rule does not read this file. See MATRIX in the yaml.
                    errors.append(
                        f"matrix.{subject}.{change_type} is 'none', which is no longer "
                        "accepted: every governed PR must name an approver team. Use "
                        "`mechanical` to skip the model review, or `not_governed` for "
                        "an automated process that already self-approves and self-merges."
                    )
                    continue
                if not _is_nonempty_str(role) or role not in teams:
                    errors.append(
                        f"matrix.{subject}.{change_type} names unknown role "
                        f"{role!r} (not in teams)"
                    )
                    continue
                matrix_roles_used.add(role)

    # ---- overrides (optional, ordered) --------------------------------
    # Path -> role, consulted before the matrix. See OVERRIDES in the yaml.
    overrides = raw.get("overrides", [])
    if overrides is None:
        overrides = []
    if not isinstance(overrides, list):
        errors.append("overrides must be a list of {paths, role, why} entries")
        overrides = []
    else:
        for i, entry in enumerate(overrides):
            if not isinstance(entry, dict):
                errors.append(f"overrides[{i}] must be a mapping with paths, role, why")
                continue
            _check_unknown_keys(entry, OVERRIDE_KEYS, f"overrides[{i}]", errors)
            role = entry.get("role")
            if not _is_nonempty_str(role) or role not in teams:
                errors.append(
                    f"overrides[{i}].role names unknown role {role!r} (not in teams)"
                )
            paths = entry.get("paths")
            if not isinstance(paths, list) or not paths:
                errors.append(f"overrides[{i}].paths must be a non-empty list of patterns")
            else:
                for j, pattern in enumerate(paths):
                    if not _is_nonempty_str(pattern):
                        errors.append(
                            f"overrides[{i}].paths[{j}] must be a non-empty string, "
                            f"got {pattern!r}"
                        )
                    elif pattern.startswith("/"):
                        errors.append(
                            f"overrides[{i}].paths[{j}] must be repo-root-relative "
                            f"with no leading slash, got {pattern!r}"
                        )
            # `why` is required on purpose: an override is a deliberate
            # exception to the matrix, and one that cannot say why it exists
            # is one nobody can safely delete later.
            if not _is_nonempty_str(entry.get("why")):
                errors.append(
                    f"overrides[{i}].why is required — say why this path does not "
                    "follow its subject's owner"
                )

    # ---- staging_evidence ---------------------------------------------
    # Required, not optional: an absent section would read as "nothing needs
    # a staging run", which is the one wrong answer a merge gate must never
    # give silently.
    staging_evidence = raw.get("staging_evidence")
    if not isinstance(staging_evidence, dict):
        errors.append("staging_evidence must be a mapping with a 'paths' key")
        staging_evidence = {"paths": []}
    else:
        _check_unknown_keys(staging_evidence, STAGING_EVIDENCE_KEYS, "staging_evidence", errors)
        paths = staging_evidence.get("paths")
        if not isinstance(paths, list) or not paths:
            errors.append("staging_evidence.paths must be a non-empty list of path patterns")
            staging_evidence = {"paths": []}
        else:
            for i, pattern in enumerate(paths):
                if not _is_nonempty_str(pattern):
                    errors.append(
                        f"staging_evidence.paths[{i}] must be a non-empty string, "
                        f"got {pattern!r}"
                    )
                elif pattern.startswith("/"):
                    errors.append(
                        f"staging_evidence.paths[{i}] must be repo-root-relative "
                        f"with no leading slash, got {pattern!r}"
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

    # ---- not_governed (optional) ------------------------------------------
    not_governed = raw.get("not_governed", {})
    if not_governed is None:
        not_governed = {}
    if not isinstance(not_governed, dict):
        errors.append("not_governed must be a mapping with optional 'authors' and 'author_label_pairs'")
        not_governed = {}
    else:
        _check_unknown_keys(not_governed, NOT_GOVERNED_KEYS, "not_governed", errors)
        ng_authors = not_governed.get("authors", [])
        if not isinstance(ng_authors, list) or not all(_is_nonempty_str(a) for a in ng_authors):
            errors.append("not_governed.authors must be a list of non-empty strings")
        pairs = not_governed.get("author_label_pairs", [])
        if not isinstance(pairs, list):
            errors.append("not_governed.author_label_pairs must be a list of {author, label} mappings")
        else:
            for i, pair in enumerate(pairs):
                if not isinstance(pair, dict):
                    errors.append(f"not_governed.author_label_pairs[{i}] must be a mapping")
                    continue
                _check_unknown_keys(pair, AUTHOR_LABEL_PAIR_KEYS, f"not_governed.author_label_pairs[{i}]", errors)
                for key in AUTHOR_LABEL_PAIR_KEYS:
                    if not _is_nonempty_str(pair.get(key)):
                        errors.append(f"not_governed.author_label_pairs[{i}].{key} must be a non-empty string")

    # ---- link_only (optional) ---------------------------------------------
    link_only = raw.get("link_only", {})
    if link_only is None:
        link_only = {}
    if not isinstance(link_only, dict):
        errors.append("link_only must be a mapping with an 'approval' key")
        link_only = {}
    else:
        _check_unknown_keys(link_only, LINK_ONLY_KEYS, "link_only", errors)
        approval = link_only.get("approval", "lane")
        if approval not in LINK_ONLY_APPROVAL:
            errors.append("link_only.approval must be one of: " + ", ".join(sorted(LINK_ONLY_APPROVAL)))

    # ---- approval (optional) ----------------------------------------------
    # Absent means `{scope: lane, admins_satisfy: false}` — the strictest
    # reading, so a config that predates this section keeps the old gate.
    approval_cfg = raw.get("approval", {})
    if approval_cfg is None:
        approval_cfg = {}
    if not isinstance(approval_cfg, dict):
        errors.append("approval must be a mapping with optional 'scope' and 'admins_satisfy'")
        approval_cfg = {}
    else:
        _check_unknown_keys(approval_cfg, APPROVAL_KEYS, "approval", errors)
        if approval_cfg.get("scope", "lane") not in APPROVAL_SCOPE:
            errors.append("approval.scope must be one of: " + ", ".join(sorted(APPROVAL_SCOPE)))
        if not isinstance(approval_cfg.get("admins_satisfy", False), bool):
            errors.append("approval.admins_satisfy must be true or false")

    if errors:
        return None, errors, warnings

    config = Config(
        schema=schema,
        teams=teams,
        bots=bots,
        matrix=matrix,
        overrides=overrides,
        staging_evidence=staging_evidence,
        claims_overlay=claims_overlay,
        external_contributors=external_contributors,
        sla=sla,
        author_staleness=author_staleness,
        waive=waive,
        not_governed=not_governed,
        link_only=link_only,
        approval=approval_cfg,
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


def _pattern_to_regex(pattern: str) -> re.Pattern:
    """Compile one path pattern (`overrides[].paths`, `staging_evidence.paths`).

    Deliberately not `fnmatch`: fnmatch's `*` crosses `/`, so `scripts/*`
    would match `scripts/redirects/general-broken-links-redirects.txt` — the
    exact path `staging_evidence` exists to exclude. Here:

      - `**/` is zero or more directories, so `content/docs/**/get-started/`
        matches `content/docs/get-started/x.md` AND
        `content/docs/iac/get-started/x.md`;
      - `*` matches within ONE segment and never crosses `/`;
      - a trailing `/` means that whole subtree;
      - anything else is an exact path.
    """
    suffix = r".+" if pattern.endswith("/") else r"\Z"
    body = ""
    # Split on `**/` first so the segment-local `*` rule below never sees it.
    for i, chunk in enumerate(pattern.split("**/")):
        if i:
            body += r"(?:[^/]*/)*"
        body += "".join(r"[^/]*" if part == "*" else re.escape(part)
                        for part in re.split(r"(\*)", chunk))
    return re.compile(body + suffix)


_STAGING_REGEX_CACHE: dict[tuple[str, ...], list[re.Pattern]] = {}


def staging_evidence_patterns(config: Config) -> list[re.Pattern]:
    """Compiled `staging_evidence.paths`, memoized per pattern tuple."""
    key = tuple(config.staging_evidence.get("paths") or ())
    if key not in _STAGING_REGEX_CACHE:
        _STAGING_REGEX_CACHE[key] = [_pattern_to_regex(pat) for pat in key]
    return _STAGING_REGEX_CACHE[key]


_OVERRIDE_REGEX_CACHE: dict[int, list[tuple[list[re.Pattern], str, str]]] = {}


def _override_rules(config: Config) -> list[tuple[list[re.Pattern], str, str]]:
    """Compiled `overrides`, in file order, memoized per Config object."""
    key = id(config)
    if key not in _OVERRIDE_REGEX_CACHE:
        _OVERRIDE_REGEX_CACHE[key] = [
            ([_pattern_to_regex(pat) for pat in entry.get("paths") or ()],
             entry.get("role") or "",
             entry.get("why") or "")
            for entry in (config.overrides or [])
        ]
    return _OVERRIDE_REGEX_CACHE[key]


def override_role(config: Config, path: str) -> tuple[str, str] | None:
    """The (role, why) an `overrides` entry assigns to `path`, or None.

    First match wins, in file order. This is consulted BEFORE the matrix and
    answers only "who owns this file" — the path's subject, and therefore the
    review criteria that apply to it, are untouched. See OVERRIDES in
    `.github/review-routing.yml` for why those are separate questions.
    """
    for regexes, role, why in _override_rules(config):
        if any(rx.match(path) for rx in regexes):
            return role, why
    return None


def requires_staging_evidence(config: Config, path: str) -> bool:
    """Does changing `path` require a demonstrated staging deploy (gate G4)?

    Keyed on the path alone, independent of which role reviews it — see
    STAGING EVIDENCE in `.github/review-routing.yml` for why those two
    questions are separate.
    """
    return any(rx.match(path) for rx in staging_evidence_patterns(config))


def resolve_lanes(
    changed_paths: list[str], mechanical: bool, claims: bool, config: Config, link_only: bool = False
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

    # Staging evidence is decided per changed path against
    # `staging_evidence.paths`, NOT by the subject's matrix row: the approver
    # and the blast radius are different questions. See STAGING EVIDENCE in
    # the yaml header.
    staging_paths = [p for p in changed_paths if requires_staging_evidence(config, p)]
    staging_evidence_required = bool(staging_paths)
    if staging_paths:
        reasons.append(
            "staging evidence required: " + ", ".join(sorted(staging_paths))
        )
    else:
        reasons.append("no changed path requires staging evidence")

    # Ownership overrides run first, per path. A path an override claims is
    # settled — it does not also contribute its subject to the matrix pass
    # below — but its SUBJECT is untouched, so the domain label and the
    # review criteria that follow from it are exactly what classify_path
    # said. See OVERRIDES in the yaml header.
    overridden: dict[str, str] = {}
    for path in changed_paths:
        hit = override_role(config, path)
        if hit is not None:
            role, _why = hit
            overridden[path] = role
            roles.add(role)
            reasons.append(
                f"override: {path} (subject:{subjects[path]}) -> role:{role}"
            )

    for subject in sorted({s for p, s in subjects.items() if p not in overridden}):
        cell = config.matrix[subject]
        role = cell[change_type]
        roles.add(role)
        reasons.append(f"subject:{subject}/{change_type} -> role:{role}")

    if claims:
        overlay_role = config.claims_overlay["add"]
        roles.add(overlay_role)
        reasons.append(f"claims overlay adds role:{overlay_role}")

    # Two rules can widen who satisfies the approver gate; the roles stay on
    # the record either way, because they are also what triage requests.
    #
    #   - `approval.scope: any-team` is repo-wide: the matrix names the
    #     reviewer best placed to look, not the only one allowed to.
    #   - `link_only.approval: any-team` is per-diff, for a sweep that
    #     changes nothing but link targets — careful work, but not lane
    #     knowledge. It still applies when the repo-wide scope is `lane`.
    scope = (config.approval or {}).get("scope", "lane")
    link_only_any_team = link_only and (config.link_only or {}).get("approval") == "any-team"
    any_team = bool(roles) and (scope == "any-team" or bool(link_only_any_team))
    if any_team:
        why = "approval.scope: any-team" if scope == "any-team" else "link-only diff"
        reasons.append(f"{why}: any team in teams: satisfies the approver gate")

    return Resolution(
        roles=roles,
        staging_evidence_required=staging_evidence_required,
        subjects=subjects,
        overridden=overridden,
        reasons=reasons,
        any_team=any_team,
    )


def admins_satisfy(config: Config) -> bool:
    """Does a repository administrator's approval satisfy the approver gate?

    Off unless `approval.admins_satisfy: true` — an admin can already merge
    past a red check, so this only lets the gate say so out loud instead of
    reporting a block the repo does not actually impose on them.
    """
    return bool((config.approval or {}).get("admins_satisfy"))


def not_governed_reason(config: Config, author: str, labels: set[str] | frozenset[str]) -> str | None:
    """Why the Sentinel does not govern this PR, or None if it does.

    `not_governed.authors` matches on the PR author alone (Dependabot);
    `author_label_pairs` needs both the author and the label (pulumi-bot's
    generated-docs regens carry `automation/merge`; its content-review PRs
    don't, and those ARE governed).
    """
    ng = config.not_governed or {}
    if author in (ng.get("authors") or []):
        return f"author `{author}` is listed in not_governed.authors"
    for pair in ng.get("author_label_pairs") or []:
        if pair.get("author") == author and pair.get("label") in labels:
            return f"author `{author}` with label `{pair['label']}` is listed in not_governed.author_label_pairs"
    return None


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
        "docs": {"mechanical": "docs-guild", "substantive": "docs-guild"},
        "blog": {"mechanical": "marketing", "substantive": "marketing"},
        "website": {"mechanical": "marketing", "substantive": "marketing"},
        "programs": {"mechanical": "docs-guild", "substantive": "docs-guild"},
        "infra": {"mechanical": "tools", "substantive": "tools"},
        "frontend": {"mechanical": "marketing", "substantive": "marketing"},
        "other": {"mechanical": "tools", "substantive": "tools"},
    },
    "staging_evidence": {"paths": ["infrastructure/", "Makefile", "scripts/run-pulumi.sh"]},
    "claims_overlay": {"add": "marketing"},
    "external_contributors": {"skip_gates": ["review-ran", "findings-answered"]},
    "sla": {
        "tools": {"business_days": 1, "escalate_to": "TODO-tools-lead"},
        "docs-guild": {"business_days": 3, "escalate_to": "TODO-owning-manager"},
        "marketing": {"business_days": 3, "escalate_to": "TODO-named-fallback"},
    },
    "author_staleness": {"warn_days": 14, "close_days": 21},
    "waive": {"label": "review:waived", "log_prefix": "pr-review/waives/"},
    "not_governed": {
        "authors": ["dependabot[bot]"],
        "author_label_pairs": [{"author": "pulumi-bot", "label": "automation/merge"}],
    },
    "link_only": {"approval": "any-team"},
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
        check("real config names every escalation contact (no TODO warnings)", real.warnings == [])
        check("real config governs pulumi-bot content-review PRs",
              not_governed_reason(real, "pulumi-bot", {"domain:docs"}) is None)
        check("real config does not govern automation/merge regens",
              not_governed_reason(real, "pulumi-bot", {"automation/merge"}) is not None)
        check("real config does not govern Dependabot",
              not_governed_reason(real, "dependabot[bot]", set()) is not None)
        check("real config routes every subject to a team (no 'none' cells)",
              all(cell[ct] != "none" for cell in real.matrix.values() for ct in CHANGE_TYPES))
        check("real config lists every PR-opening bot",
              {"pulumi-bot", "workprentice[bot]"} <= set(real.bots))
    except RoutingConfigError as e:
        check(f"real .github/review-routing.yml loads ({e.errors})", False)

    # ---- resolve_lanes cases -------------------------------------------
    r = resolve_lanes(["content/docs/foo.md"], mechanical=True, claims=False, config=config)
    check("pure docs mechanical still routes to docs-guild", r.roles == {"docs-guild"})

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
    check("subject:infra alone does NOT imply staging evidence",
          r.staging_evidence_required is False)

    r = resolve_lanes(
        ["content/docs/foo.md", "scripts/run-pulumi.sh"],
        mechanical=False, claims=False, config=config,
    )
    check("a listed deploy script -> staging evidence required",
          r.staging_evidence_required is True)
    r = resolve_lanes(["infrastructure/index.ts"], mechanical=False, claims=False, config=config)
    check("a subtree pattern matches below itself", r.staging_evidence_required is True)

    r = resolve_lanes(["content/docs/foo.md"], mechanical=True, claims=True, config=config)
    check("claims overlay adds marketing", "marketing" in r.roles)
    check("claims overlay forces substantive", r.roles == {"docs-guild", "marketing"})

    r = resolve_lanes(["some/unknown/path.txt"], mechanical=False, claims=False, config=config)
    check("unclassifiable path routed as subject:other", r.subjects["some/unknown/path.txt"] == "other")
    check("subject:other substantive -> tools, no staging evidence",
          r.roles == {"tools"} and r.staging_evidence_required is False)
    r_mech = resolve_lanes(["some/unknown/path.txt"], mechanical=True, claims=False, config=config)
    check("subject:other mechanical -> tools too (mechanical never means nobody)",
          r_mech.roles == {"tools"})

    r = resolve_lanes(["layouts/partials/foo.html"], mechanical=False, claims=False, config=config)
    check("template -> subject:frontend -> marketing", r.roles == {"marketing"})
    check("frontend never requires staging evidence", r.staging_evidence_required is False)

    r = resolve_lanes([".github/workflows/ci.yml", ".claude/commands/x/SKILL.md"],
                      mechanical=False, claims=False, config=config)
    check("infra + other dedupes to tools alone", r.roles == {"tools"})

    # ---- staging evidence keys on path, not subject --------------------
    # The matcher's whole contract in three cases: `*` must not cross `/`,
    # a trailing `/` must reach the whole subtree, and an unlisted path in a
    # listed directory must stay off the gate.
    check("`scripts/*` style pattern does not cross a path segment",
          not requires_staging_evidence(config, "scripts/redirects/general.txt"))
    check("exact-path pattern matches exactly",
          requires_staging_evidence(config, "scripts/run-pulumi.sh")
          and not requires_staging_evidence(config, "scripts/run-pulumi.sh.bak"))
    check("subtree pattern does not match the bare directory name",
          not requires_staging_evidence(config, "infrastructure"))

    real_paths = {
        # PR #21698: domain:infra, but a redirect line cannot change the deploy.
        "scripts/redirects/general-broken-links-redirects.txt": False,
        "scripts/review-v3/sentinel.py": False,
        "scripts/lint/lint-markdown.js": False,
        ".github/workflows/blog-review-index.yml": False,
        "content/blog/foo/index.md": False,
        "infrastructure/index.ts": True,
        "Makefile": True,
        "scripts/ci-push.sh": True,
        "scripts/search/main.js": True,
        ".github/workflows/testing-build-and-deploy.yml": True,
    }
    try:
        for path, want in real_paths.items():
            check(f"real config: staging {'required' if want else 'not required'} for {path}",
                  requires_staging_evidence(real, path) is want)
    except NameError:  # real config failed to load; already reported above
        pass

    bad = copy.deepcopy(_CANNED_CONFIG)
    del bad["staging_evidence"]
    _, errs, _ = validate_raw(bad)
    check("staging_evidence is required, not optional",
          any("staging_evidence must be a mapping" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["staging_evidence"] = {"paths": []}
    _, errs, _ = validate_raw(bad)
    check("staging_evidence.paths must be non-empty",
          any("staging_evidence.paths must be a non-empty list" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["staging_evidence"] = {"paths": ["/infrastructure/"]}
    _, errs, _ = validate_raw(bad)
    check("staging_evidence.paths rejects a leading slash",
          any("repo-root-relative" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["matrix"]["infra"]["staging_evidence"] = "required"
    _, errs, _ = validate_raw(bad)
    check("the retired matrix cell key now fails closed",
          any("unknown key 'staging_evidence'" in e for e in errs))

    check("not_governed: dependabot by author",
          not_governed_reason(config, "dependabot[bot]", set()) is not None)
    check("not_governed: pulumi-bot needs the label",
          not_governed_reason(config, "pulumi-bot", set()) is None
          and not_governed_reason(config, "pulumi-bot", {"automation/merge"}) is not None)
    check("every subject/change-type pair resolves to at least one role",
          all(resolve_lanes([path], mechanical=m, claims=False, config=config).roles
              for m in (True, False)
              for path in ("content/docs/a.md", "content/blog/b/index.md",
                           "content/nav/c.md", "static/programs/d/index.ts",
                           "scripts/e.sh", "layouts/f.html", "zzz-unknown.txt")))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["not_governed"] = {"authors": "dependabot[bot]"}
    _, errs, _ = validate_raw(bad)
    check("not_governed.authors must be a list", any("not_governed.authors" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["surprise_section"] = {"authors": ["pulumi-bot"]}
    _, errs, _ = validate_raw(bad)
    check("a retired/unknown top-level section is rejected",
          any("unknown key 'surprise_section'" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["auto_approve"] = {"authors": ["pulumi-bot"]}
    _, errs, _ = validate_raw(bad)
    check("the retired auto_approve section now fails closed",
          any("unknown key 'auto_approve'" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["matrix"]["docs"]["mechanical"] = "none"
    _, errs, _ = validate_raw(bad)
    check("a 'none' matrix cell is rejected",
          any("matrix.docs.mechanical is 'none'" in e for e in errs))

    ok_cfg = copy.deepcopy(_CANNED_CONFIG)
    del ok_cfg["not_governed"]
    cfg2, errs, _ = validate_raw(ok_cfg)
    check("not_governed is optional", errs == [] and cfg2.not_governed == {})

    # ---- approval scope -------------------------------------------------
    check("approval is optional and defaults to the lane rule",
          config.approval == {} and admins_satisfy(config) is False
          and resolve_lanes(["content/docs/foo.md"], mechanical=False, claims=False,
                            config=config).any_team is False)
    any_team_cfg, errs, _ = validate_raw({
        **copy.deepcopy(_CANNED_CONFIG),
        "approval": {"scope": "any-team", "admins_satisfy": True},
    })
    check("approval.scope: any-team validates", errs == [])
    r = resolve_lanes(["content/docs/foo.md"], mechanical=False, claims=False, config=any_team_cfg)
    check("approval.scope: any-team widens the gate but keeps the routed role",
          r.any_team is True and r.roles == {"docs-guild"})
    check("approval.admins_satisfy is readable", admins_satisfy(any_team_cfg) is True)
    check("a zero-role PR is not 'any team'",
          resolve_lanes([], mechanical=False, claims=False, config=any_team_cfg).any_team is False)

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["approval"] = {"scope": "whoever"}
    _, errs, _ = validate_raw(bad)
    check("approval.scope is validated", any("approval.scope" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["approval"] = {"admins_satisfy": "yes"}
    _, errs, _ = validate_raw(bad)
    check("approval.admins_satisfy must be a bool", any("admins_satisfy" in e for e in errs))

    bad = copy.deepcopy(_CANNED_CONFIG)
    bad["approval"] = {"scope": "any-team", "admin": True}
    _, errs, _ = validate_raw(bad)
    check("an unknown approval key fails closed", any("unknown key 'admin'" in e for e in errs))

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
