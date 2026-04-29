---
user-invocable: false
description: Triage prose-check prompt. Loaded only when triage-classify.py classifies a PR as trivial or frontmatter-only. Classification itself is deterministic and lives in triage-classify.py.
---

# PR Triage — Prose Check

You are doing a focused spelling/grammar pass on a small pull request that the triage shell has already classified as **trivial** (≤5 lines of prose-only body changes) or **frontmatter-only** (every change is inside a Hugo frontmatter block). Either way, the full review will be skipped — this is the only sanity-check pass before merge.

This is a fast, narrow pass (Sonnet, ~512 token output cap). Output exactly one JSON object on a single line, no prose, no code fences:

```json
{"prose_concerns":["path/to/file.md:LINE — issue (suggested fix)", ...]}
```

If you find no issues, output `{"prose_concerns":[]}`.

## What to flag

- Misspelled common English words (e.g., "recieve" → "receive").
- Subject-verb disagreement.
- Missing articles in unambiguous cases.
- Punctuation that changes meaning (e.g., missing comma in a non-restrictive clause).
- Wrong-word substitutions: "their" vs "there", "its" vs "it's", "affect" vs "effect", "loose" vs "lose".

## What NOT to flag

- Technical terms: Pulumi, ESC, IAM, kubectl, etc.
- Proper nouns and product names.
- CLI commands or flags (e.g., `--no-fail-on-create`).
- Code identifiers, variable names, file paths.
- Intentional style choices (sentence fragments for emphasis, em-dash density).
- Regional spelling variants (US vs UK English) — neither is "wrong."
- Oxford-comma preference (the repo doesn't enforce one way).

## Frontmatter-only PRs: scope

When the PR is frontmatter-only, only inspect prose-bearing fields:

- `title`, `linktitle`
- `meta_desc`, `description`
- `social_image_text`, `og_description`
- `excerpt`, `summary`

Skip data fields entirely — they're not prose:

- `aliases`, `slug`, `url`
- `tags`, `categories`, `keywords`
- `draft`, `date`, `weight`, `expiryDate`
- `author`, `authors` (proper-noun-only)
- `cluster_*`, `block_*`, layout/template directives

## Output format

Each finding is one element in `prose_concerns`, formatted as:

```text
path/to/file.md:LINE — issue (suggested fix)
```

Be specific so the author can act without re-reading the diff. One concern per array element. Cap output at the most important ~5 findings — this is a sanity check, not a copy edit.

---

## Notes for maintainers

The classification logic — domain (path-precedence), triviality, frontmatter-only detection, fact-check signal, agent-authored signal — is deterministic and lives in `.claude/commands/_common/scripts/triage-classify.py`. That script is the source of truth; this prompt is loaded only when the classifier flags `prose_check_needed: true`.

Most PRs never reach this prompt because most PRs are not trivial or frontmatter-only. The full review handles them and runs its own prose-quality checks per `_common/review-*.md`.
