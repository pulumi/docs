"""The no-claims External claim verification bullet carries the metadata skeleton.

Regression for pulumi/docs#20596 (part 2). The composer used to stub a diff with
no fact-check claims as `not run (no claims in this diff)`. That validates, but
it has no specialists/routed segments. When the reviewer then found claims
in-review and rewrote the bullet into the `X of Y claims verified` form, the
dispatch- and routed-metadata rules fired on a line that had nothing to
preserve (seen on fork fixture #222, mirroring #18799), and validator-fix
couldn't reconstruct the counts.

The composer now emits the canonical form with zero counts, so an in-review
addition increments segments that already exist.
"""

from __future__ import annotations

import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


cr = _load("compose_review", "compose-review.py")
vp = _load("validate_pinned", "validate-pinned.py")

EXTERNAL_RULES = (
    vp.check_external_claim_state_format,
    vp.check_external_claim_dispatch_metadata,
    vp.check_external_claim_routed_metadata,
    vp.check_external_claim_pass2_outcome,
)


def _log(verdicts):
    return cr.render_investigation_log(
        cross_sibling=[], verdicts=verdicts,
        route_counts=cr.compute_route_counts(verdicts, None),
        frontmatter=[], has_temporal_trigger=False, diff_files=[],
        has_fenced_code_in_content=False, editorial_balance=None, is_blog=False,
        diff_unavailable=False)


def _external_line(log: str) -> str:
    return next(l for l in log.splitlines() if l.lstrip().startswith("- **External claim verification"))


def _violations(line: str) -> list[str]:
    ctx = vp.Context(body=line, body_lines=[line], pr=None, repo=None,
                     diff_files=[], diff_files_added=set(), diff_text="",
                     repo_root=pathlib.Path("."), is_blog=False)
    return [v.rule_id for rule in EXTERNAL_RULES for v in rule(ctx)]


def _simulate_in_review_additions(line: str, n: int) -> str:
    """What the reviewer does: bump X/Y and the inline route count by n."""
    line = re.sub(r"(\d+) of (\d+) claims verified",
                  lambda m: f"{int(m.group(1)) + n} of {int(m.group(2)) + n} claims verified", line)
    return re.sub(r"routed: (\d+) inline", lambda m: f"routed: {int(m.group(1)) + n} inline", line)


def test_no_claims_renders_zero_skeleton_not_stub():
    line = _external_line(_log([]))
    assert "not run" not in line
    assert line == (
        "- **External claim verification:** 0 of 0 claims verified (0 unverifiable, 0 contradicted) · "
        "4 specialists (numerical, cross-reference, capability, framing); 0 cross-specialist corroborations · "
        "routed: 0 inline, 0 Pass 1, 0 Pass 2, 0 Pass 3."
    )


def test_zero_skeleton_validates():
    assert _violations(_external_line(_log([]))) == []


def test_detector_only_verdicts_still_render_zero_skeleton():
    # Preflight detector findings aren't fact-check claims; they must not leak
    # into the zero skeleton's counts.
    detectors = [{"verdict": "flagged", "route": "preflight"}]
    line = _external_line(_log(detectors))
    assert "0 of 0 claims verified" in line
    assert "routed: 0 inline, 0 Pass 1, 0 Pass 2, 0 Pass 3." in line


def test_in_review_additions_keep_metadata_rules_green():
    # The #222 shape: composer had no claims, reviewer found 3 in-review and
    # resolved them inline. With the skeleton, incrementing is all it takes.
    line = _simulate_in_review_additions(_external_line(_log([])), 3)
    assert "3 of 3 claims verified" in line and "routed: 3 inline" in line
    assert _violations(line) == []


def test_old_stub_shape_is_what_broke():
    # Pins the failure mode the skeleton prevents: the stub rewritten into the
    # counted form with no segments trips both metadata rules.
    rewritten = "- **External claim verification:** 3 of 3 claims verified (0 unverifiable, 0 contradicted)."
    assert set(_violations(rewritten)) == {
        "external-claim-dispatch-metadata", "external-claim-routed-metadata"}


def test_claims_path_unchanged():
    verdicts = [{"verdict": "verified", "route": "pass1"},
                {"verdict": "contradicted", "route": "pass1"}]
    line = _external_line(_log(verdicts))
    assert "1 of 2 claims verified (0 unverifiable, 1 contradicted)" in line
    assert "routed: 0 inline, 2 Pass 1, 0 Pass 2, 0 Pass 3." in line
