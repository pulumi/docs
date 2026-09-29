"""extract-claims-llm.py: a claim list that outgrows MAX_TOKENS is retried as
two halves of the numbered body instead of failing the whole file.

The September 2026 content-review runs over the Pulumi YAML reference (770
lines) truncated on both passes, so the page was verified on the regex floor
alone and the glow-up's edits to it went unchecked until the PR review.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("extract_claims_llm", HERE / "extract-claims-llm.py")
ecl = importlib.util.module_from_spec(_spec)
sys.modules["extract_claims_llm"] = ecl
_spec.loader.exec_module(ecl)


def _prompt(n_lines: int) -> str:
    body = []
    for i in range(1, n_lines + 1):
        body.append(f"{i}\t## Section {i}" if i % 10 == 1 else f"{i}\tLine {i} says a thing.")
    return "File: `content/docs/x.md`\n```\n" + "\n".join(body) + "\n```\nTrailer.\n"


def test_split_keeps_preamble_line_numbers_and_trailer():
    halves = ecl.split_user_text(_prompt(40))
    assert halves and len(halves) == 2
    for h in halves:
        assert h.startswith("File: `content/docs/x.md`")
        assert h.rstrip().endswith("Trailer.")
    assert "1\t## Section 1" in halves[0] and "1\t## Section 1" not in halves[1]
    # The cut lands on an H2, so the second half opens with a heading.
    second_body = halves[1].split("```\n", 1)[1]
    assert second_body.split("\t", 1)[1].startswith("## Section")


def test_split_finds_h2_in_standard_scope_hunks():
    body = [f"{i}\t+ ## Heading {i}" if i == 13 else f"{i}\t  line {i}" for i in range(1, 41)]
    halves = ecl.split_user_text("preamble\n```\n" + "\n".join(body) + "\n```\n")
    assert halves[1].split("```\n", 1)[1].startswith("13\t+ ## Heading 13")


def test_split_refuses_tiny_or_unfenced_bodies():
    assert ecl.split_user_text("no fence here") is None
    assert ecl.split_user_text("```\n1\ta\n```") is None


def test_truncation_retries_as_halves(monkeypatch, tmp_path):
    calls = []

    def fake_call(api_key, system_body, mode_header, text, model):
        n = text.count("\n") - 3
        calls.append(n)
        if n > 25:
            raise ecl.TruncatedError("truncated", {"input_tokens": 100, "output_tokens": 8192})
        first = next(ln for ln in text.split("\n") if "\t" in ln).split("\t")[0]
        return ([{"line_range": f"L{first}", "text": f"claim from L{first}", "type": "behavior"}],
                {"input_tokens": 10, "output_tokens": 5})

    monkeypatch.setattr(ecl, "call_anthropic", fake_call)
    monkeypatch.setattr(ecl, "build_user_message", lambda *a, **k: (_prompt(40), None))
    monkeypatch.setattr(ecl, "rename_similarity", lambda *a, **k: None)
    res = ecl.process_file("k", tmp_path, "", "content/docs/x.md", "standard", "atomic",
                           "m", "sys", False)
    assert res["error"] is None, res["error"]
    assert len(res["claims"]) == 2
    assert res["usage"]["output_tokens"] == 8192 + 10  # the truncated attempt is still billed
    assert len(calls) == 3 and calls[0] > 25 >= max(calls[1:])


def test_truncation_gives_up_after_split_depth(monkeypatch, tmp_path):
    def always_truncated(*a, **k):
        raise ecl.TruncatedError("truncated", {"output_tokens": 1})

    monkeypatch.setattr(ecl, "call_anthropic", always_truncated)
    monkeypatch.setattr(ecl, "build_user_message", lambda *a, **k: (_prompt(40), None))
    monkeypatch.setattr(ecl, "rename_similarity", lambda *a, **k: None)
    res = ecl.process_file("k", tmp_path, "", "content/docs/x.md", "standard", "atomic",
                           "m", "sys", False)
    # 1 + 2 + 4 calls, and the four leaves each report the truncation.
    assert res["usage"]["output_tokens"] == 7
    assert res["error"].count("TruncatedError") == 4
