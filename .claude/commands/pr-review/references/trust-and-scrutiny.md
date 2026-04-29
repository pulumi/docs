---
user-invocable: false
description: Two-axis trust model, risk tiering, and AI-suspect detection for pr-review
---

# Trust, Scrutiny, and AI-Suspect Detection

This reference defines how `/pr-review` reasons about contributors and PR risk. Etiquette trust controls tone; content scrutiny controls review depth. They are independent — etiquette trust never relaxes content scrutiny.

## Two-axis trust model

`contributor-detection.sh` emits two independent fields.

### Etiquette trust

Controls tone, welcoming language, default merge behavior, and how the comment templates are phrased. Has nothing to do with how carefully the *content* is reviewed.

| Value | Triggered by |
|---|---|
| `low` | First-time external contributor; unknown bot account |
| `standard` | External contributor with prior merged PRs to `pulumi/docs` |
| `high` | Internal contributor (Pulumi org member); known good bot (dependabot, pulumi-bot, renovate, copilot) |

### Content scrutiny

Controls review depth, fact-check aggressiveness, and auto-apply policy.

| Value | Triggered by |
|---|---|
| `standard` | Default for everyone, regardless of etiquette trust |
| `heightened` | **AI-suspect flag is set** — overrides everything else |

There is deliberately no "relaxed" content-scrutiny tier. Every PR gets at least `standard` scrutiny. The only knob is whether to *increase* it.

## Risk tier

`contributor-detection.sh` also computes a risk tier from the diff shape. Risk tier scopes review depth — there is no point running full claim extraction on a 3-line typo PR.

| Tier | Heuristic | Effect |
|---|---|---|
| `typo` | ≤5 changed lines, only prose, no code blocks touched | Skip fact-check entirely; minimal review |
| `minor` | ≤30 changed lines, single file, no new files | Standard review, no full-file claim extraction |
| `standard` | Default | Full fact-check if gated in |
| `major` | New page, >300 lines, structural changes, file moves | Full fact-check; whole-file read recommended |
| `infra` | Touches `scripts/`, `.github/workflows/`, `Makefile`, `infrastructure/`, `package.json`, `webpack.config.js` | Triggers the infrastructure deployment prompt; uses existing infra review path |

When `CONTENT_SCRUTINY=heightened`, the `typo` and `minor` tiers no longer skip fact-check — AI hallucinations show up in tiny diffs too.

## AI-suspect detection

A PR is flagged AI-suspect when **any** of the following signals fire. The flag is a single boolean (`AI_SUSPECT=true|false`) plus a `REASONS` list for the gauge.

### Signal 1: Local allowlist (reason: `allowlist`)

`detect-ai-suspect.sh` reads a newline-delimited list of GitHub usernames from:

```
~/.claude/pr-review/ai-suspect-authors.txt
```

If the PR author appears in the file, the flag is set.

**This file is local-only and is never created, written, or committed by the skill.** Each user maintains their own (or doesn't). The other detection signals work without an allowlist.

**File format:** one GitHub username per line, optional `#` comments, blank lines ignored. Example:

```
# Personal AI-suspect allowlist for /pr-review
# Names here trigger heightened content scrutiny on every PR.
# Local-only — never commit this file.

some-user
```

### Signal 2: AI authoring trailer (reason: `trailer:<which>`)

`detect-ai-suspect.sh` searches the PR body and every commit message in the PR for known AI-authoring markers:

- `Co-Authored-By: Claude` (any model variant — Sonnet, Opus, Haiku)
- `Co-Authored-By: Claude Code`
- `Generated with Claude Code`
- `noreply@anthropic.com`
- `Co-Authored-By: Cursor`
- `Co-Authored-By: Copilot`
- `Co-Authored-By: GitHub Copilot`
- `🤖 Generated with`

Any match sets the flag with reason `trailer:claude`, `trailer:cursor`, `trailer:copilot`, etc.

### Signal 3: Prose pattern density (reason: `prose-pattern:<which>`)

For every added prose line in the diff (lines starting with `+` in `.md` files, excluding code blocks and frontmatter), compute three densities:

- **em-dash density** — count of `—` per added word. Threshold: > 0.015 (≈ 1 em-dash per 65 words).
- **contrastive density** — count of "not X — Y" / "not X, but Y" / "It's not X, it's Y" constructions per added paragraph. Threshold: > 1 per 3 paragraphs.
- **hedge density** — count of `generally|typically|tends to|can often|may sometimes|in many cases|it's worth noting|it's important to note` per added word. Threshold: > 0.012.

If any density exceeds threshold AND the PR has more than 10 added prose lines (to avoid false positives on tiny diffs), set the flag with the corresponding reason.

### Signal 4: Manual override (reason: `manual`)

The user can pass:

- `/pr-review 123 --ai` — force AI_SUSPECT=true with reason `manual`
- `/pr-review 123 --no-ai` — force AI_SUSPECT=false (clears any other signals for this run only)

Manual override always wins over the other three signals.

## Heightened-scrutiny behaviors

When `CONTENT_SCRUTINY=heightened` (i.e., `AI_SUSPECT=true`), the skill behaves differently in several places:

| Where | Behavior |
|---|---|
| fact-check gating | `should-fact-check.sh` always returns RUN, even for non-content paths and bot/dependabot PRs |
| fact-check claim extraction | Runs over the **full file**, not just diff context. AI hallucinates surrounding prose. |
| fact-check verification | Web/`gh`/schema verification runs by default on every claim, not just claims that would normally graduate to it |
| fact-check triage tiers | The bar for "Low-confidence verified" drops one level. Medium-confidence verified claims become *visible* instead of collapsed under `<details>`. |
| Step 6 confidence gauge | Prepends `🤖 AI-suspect (<reasons>)` and caps the gauge at MEDIUM. HIGH is impossible when AI-suspect is set. |
| Step 6 trivial-fix preview | Suppressed entirely; see `pr-review:references:action-preview-templates` §AI-suspect override. |
| Step 8 merge toggle | Defaults **OFF** regardless of contributor type. |
| Make-changes-and-approve trivial fixes | Agent skips all trivial-fix application during the make-changes workflow. The AI may have introduced subtly wrong "fixes" that look like typos but aren't (e.g., renaming a real method to a hallucinated one). |
