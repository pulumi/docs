#!/usr/bin/env python3
"""The approver's local config for /pr-review: `~/.pr-review.yml`.

    me: [docs, infra, frontend, other]   # routing lanes that are "mine"
    stamp_max_lines: 40                  # a diff at or above this is never a stamp
    stale_date_days: 3                   # blog `date:` older than this is stale
    link_fixes: mine                     # mine | route — a link-only diff is yours whatever its lane

Routing itself (subject → owning team) comes from `.github/review-routing.yml`
via routing.py; this file only says which of those lanes the person running
the queue approves for, so the queue can tell "mine" from "route". It is
local and never committed. When the file is missing every lane counts as
mine, with a warning, so the board still renders on first run.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import routing  # noqa: E402

DEFAULT_PATH = Path.home() / ".pr-review.yml"
DEFAULT_STAMP_MAX_LINES = 40
DEFAULT_STALE_DATE_DAYS = 3
DEFAULT_LINK_FIXES = "mine"
LINK_FIXES_VALUES = frozenset({"mine", "route"})


@dataclass
class UserConfig:
    me: list[str]
    stamp_max_lines: int = DEFAULT_STAMP_MAX_LINES
    stale_date_days: int = DEFAULT_STALE_DATE_DAYS
    link_fixes: str = DEFAULT_LINK_FIXES  # "mine": a link-only diff bypasses the lane check; "route": it doesn't
    source: str = "defaults"
    warnings: list[str] = field(default_factory=list)

    def to_json(self) -> dict:
        return {
            "me": list(self.me),
            "stamp_max_lines": self.stamp_max_lines,
            "stale_date_days": self.stale_date_days,
            "link_fixes": self.link_fixes,
            "source": self.source,
            "warnings": list(self.warnings),
        }


def lanes_from_teams(memberships: dict, config) -> list[str]:
    """The lanes a person owns by virtue of the teams they are actually on:
    every team they belong to maps back to its routing role, and every matrix
    cell naming that role contributes its subject. This is what `me` means
    when no config file pins it — the org chart already knows the answer, so
    a first run doesn't have to claim every lane."""
    roles = {r for r, team in config.teams.items() if memberships.get(team) is True}
    if not roles:
        return []
    lanes = {d for d, cell in config.matrix.items()
             if roles & {cell.get("mechanical"), cell.get("substantive")}}
    return sorted(lanes)


def parse_config(raw: object, source: str = "<raw>") -> UserConfig:
    """Validate a loaded YAML value into a UserConfig. Raises ValueError on a
    shape the queue can't honour (unknown lane, non-integer threshold)."""
    if raw is None:
        raw = {}
    if not isinstance(raw, dict):
        raise ValueError(f"{source}: top level must be a mapping")
    unknown = set(raw) - {"me", "stamp_max_lines", "stale_date_days", "link_fixes"}
    if unknown:
        raise ValueError(f"{source}: unknown key(s) {sorted(unknown)}")
    me = raw.get("me")
    warnings: list[str] = []
    if me is None:
        me = sorted(routing.SUBJECTS)
        warnings.append(f"{source}: no `me:` — treating every lane as mine")
    if isinstance(me, str):
        me = [me]
    if not isinstance(me, list) or not all(isinstance(m, str) for m in me):
        raise ValueError(f"{source}: `me` must be a list of lane names")
    bad = [m for m in me if m not in routing.SUBJECTS]
    if bad:
        raise ValueError(f"{source}: unknown lane(s) {bad}; valid: {sorted(routing.SUBJECTS)}")

    def _int(key: str, default: int) -> int:
        v = raw.get(key, default)
        if isinstance(v, bool) or not isinstance(v, int) or v < 0:
            raise ValueError(f"{source}: `{key}` must be a non-negative integer")
        return v

    link_fixes = raw.get("link_fixes", DEFAULT_LINK_FIXES)
    if link_fixes not in LINK_FIXES_VALUES:
        raise ValueError(f"{source}: `link_fixes` must be one of {sorted(LINK_FIXES_VALUES)}")

    return UserConfig(
        me=list(dict.fromkeys(me)),
        stamp_max_lines=_int("stamp_max_lines", DEFAULT_STAMP_MAX_LINES),
        stale_date_days=_int("stale_date_days", DEFAULT_STALE_DATE_DAYS),
        link_fixes=link_fixes,
        source=source,
        warnings=warnings,
    )


def load_user_config(path: str | Path | None = None) -> UserConfig:
    p = Path(path) if path else DEFAULT_PATH
    if not p.exists():
        cfg = parse_config({}, source="defaults")
        cfg.warnings = [f"{p} not found — falling back to your GitHub team memberships (every lane, if those can't be read); create it to pin your lanes"]
        return cfg
    try:
        raw = yaml.safe_load(p.read_text())
    except yaml.YAMLError as exc:
        raise ValueError(f"{p} is not valid YAML: {exc}") from exc
    return parse_config(raw, source=str(p))


def self_test() -> int:
    cfg = parse_config({"me": ["docs", "infra"], "stamp_max_lines": 10})
    assert cfg.me == ["docs", "infra"] and cfg.stamp_max_lines == 10 and cfg.stale_date_days == 3 and cfg.link_fixes == "mine"
    assert parse_config({"link_fixes": "route"}).link_fixes == "route"
    cfg = parse_config(None)
    assert set(cfg.me) == set(routing.SUBJECTS) and cfg.warnings
    for bad in ({"me": ["nope"]}, {"stamp_max_lines": "x"}, {"extra": 1}, ["a"], {"link_fixes": "always"}):
        try:
            parse_config(bad)
            raise AssertionError(f"accepted {bad!r}")
        except ValueError:
            pass
    missing = load_user_config("/nonexistent/.pr-review.yml")
    assert missing.warnings and set(missing.me) == set(routing.SUBJECTS)
    print("all pr_review_config self-tests passed")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--config", help=f"path (default {DEFAULT_PATH})")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    import json  # noqa: PLC0415
    print(json.dumps(load_user_config(args.config).to_json(), indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
