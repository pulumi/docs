"""review_state.py's high-water helpers: the fallback that keeps finding ids
from restarting after a forced review errors with its card already cleared."""

from __future__ import annotations

import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import review_state  # noqa: E402


def test_marker_round_trips_and_the_largest_wins():
    bodies = "\n".join([
        "<!-- CLAUDE_PROGRESS -->\n🤖 Review errored. " + review_state.hw_marker(4),
        "<!-- CLAUDE_PROGRESS -->\n🤖 Review timed out. " + review_state.hw_marker(9),
        "unrelated comment",
    ])
    assert review_state.marker_high_water(bodies) == 9
    assert review_state.marker_high_water("") == 0
    assert review_state.hw_marker(0) == "", "nothing to carry → no marker"


def test_cli_reads_markers_from_stdin():
    r = subprocess.run([sys.executable, str(HERE / "review_state.py"), "high-water-marker"],
                       input="x " + review_state.hw_marker(7), capture_output=True, text=True, check=True)
    assert r.stdout.strip() == "7"
