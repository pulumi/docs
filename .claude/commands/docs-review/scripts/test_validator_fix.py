#!/usr/bin/env python3
"""Unit tests for validator-fix.py.

Self-contained — run with `python3 test_validator_fix.py` (no pytest dep).
Imports the module directly and exercises `extract_splice_output()`, the
guard that decides whether a Messages API response can be trusted as a
full-body echo. Regression tests for pulumi/docs#20135, where a
`stop_reason == "max_tokens"` truncation passed the old emptiness-only
check and the amputated review body got published.
"""

from __future__ import annotations

import importlib.util
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE / "validator-fix.py"

_spec = importlib.util.spec_from_file_location("validator_fix", MODULE_PATH)
validator_fix = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(validator_fix)  # type: ignore[union-attr]

extract_splice_output = validator_fix.extract_splice_output

BODY = "### 🔍 Verification trail\n\n" + "\n".join(
    f"- L{n} in `file.md` \"claim text {n}\" → ✅ verified" for n in range(40)
)


def _payload(text: str, stop_reason: str = "end_turn") -> dict:
    return {
        "content": [{"type": "text", "text": text}],
        "stop_reason": stop_reason,
    }


def test_full_echo_passes() -> None:
    out = extract_splice_output(_payload(BODY), len(BODY))
    assert out == BODY, "verbatim full-length echo must be accepted"


def test_max_tokens_rejected_even_with_content() -> None:
    truncated = BODY[: len(BODY) // 2]
    out = extract_splice_output(_payload(truncated, stop_reason="max_tokens"), len(BODY))
    assert out is None, "max_tokens response must be discarded regardless of content"


def test_max_tokens_rejected_even_at_full_length() -> None:
    # Belt and suspenders: stop_reason wins even if the length looks fine.
    out = extract_splice_output(_payload(BODY, stop_reason="max_tokens"), len(BODY))
    assert out is None, "max_tokens response must be discarded even at full length"


def test_empty_content_rejected() -> None:
    out = extract_splice_output(_payload(""), len(BODY))
    assert out is None, "empty content must be discarded"


def test_missing_content_rejected() -> None:
    out = extract_splice_output({"stop_reason": "end_turn"}, len(BODY))
    assert out is None, "missing content block must be discarded"


def test_shrunken_echo_rejected() -> None:
    shrunk = BODY[: int(len(BODY) * 0.5)]
    out = extract_splice_output(_payload(shrunk), len(BODY))
    assert out is None, "echo far below the shrink floor must be discarded"


def test_lightly_edited_echo_passes() -> None:
    edited = BODY[: int(len(BODY) * 0.95)]
    out = extract_splice_output(_payload(edited), len(BODY))
    assert out == edited, "echo within the shrink floor must be accepted"


def test_code_fence_stripped_before_length_check() -> None:
    fenced = "```markdown\n" + BODY + "\n```"
    out = extract_splice_output(_payload(fenced), len(BODY))
    assert out == BODY, "fence wrapper must be stripped and the body accepted"


TESTS = [
    test_full_echo_passes,
    test_max_tokens_rejected_even_with_content,
    test_max_tokens_rejected_even_at_full_length,
    test_empty_content_rejected,
    test_missing_content_rejected,
    test_shrunken_echo_rejected,
    test_lightly_edited_echo_passes,
    test_code_fence_stripped_before_length_check,
]


def main() -> int:
    failures: list[tuple[str, str]] = []
    for t in TESTS:
        name = t.__name__
        try:
            t()
            print(f"  ok  {name}")
        except AssertionError as e:
            failures.append((name, str(e) or "assertion failed"))
            print(f"  FAIL {name}: {e}")
        except Exception:
            failures.append((name, traceback.format_exc()))
            print(f"  ERROR {name}:\n{traceback.format_exc()}")
    print()
    if failures:
        print(f"{len(failures)}/{len(TESTS)} tests failed")
        return 1
    print(f"{len(TESTS)}/{len(TESTS)} tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
