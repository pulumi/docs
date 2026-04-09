---
user-invocable: false
description: Two-axis trust model, risk tiering, and AI-suspect detection for pr-review
---

# Trust, Scrutiny, and AI-Suspect Detection

This reference defines how `/pr-review` reasons about contributors and PR risk. The model is intentionally split into orthogonal axes so that "this contributor is trusted" never relaxes the scrutiny of content that may have been AI-generated.

## Two-axis trust model

`contributor-detection.sh` emits two independent fields. **Conflating them was the original bug** — high etiquette trust used to relax content scrutiny, which is exactly wrong for AI-authored PRs from senior contributors.

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
| `typo` | ≤5 changed lines, only prose, no code blocks touched | Skip Step 5 entirely; minimal review |
| `minor` | ≤30 changed lines, single file, no new files | Standard review, no full-file claim extraction |
| `standard` | Default | Full Step 5 if gated in |
| `major` | New page, >300 lines, structural changes, file moves | Full Step 5; recommend reading whole file in Step 4 |
| `infra` | Touches `scripts/`, `.github/workflows/`, `Makefile`, `infrastructure/`, `package.json`, `webpack.config.js` | Triggers Step 3 deployment prompt; uses existing infra review path |

When `CONTENT_SCRUTINY=heightened`, the `typo` and `minor` tiers no longer skip Step 5 — AI hallucinations show up in tiny diffs too.

## AI-suspect detection

A PR is flagged AI-suspect when **any** of the following signals fire. The flag is a single boolean (`AI_SUSPECT=true|false`) plus a `REASONS` list for the gauge.

### Signal 1: Local allowlist (reason: `allowlist`)

`detect-ai-suspect.sh` reads a newline-delimited list of GitHub usernames from:

```
~/.claude/pr-review/ai-suspect-authors.txt
```

If the PR author appears in the file, the flag is set.

**This file is local-only and is never created, written, or committed by the skill.** It contains specific colleagues' names with the implicit message "this person ships AI-drafted PRs," which is a private judgment call. Tracking it in git would be a political landmine. Each user maintains their own file (or doesn't). The other detection signals work without an allowlist, so the skill behaves correctly on machines that don't have one.

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

These thresholds are starting points and should be tuned over time based on false-positive feedback from `/pr-review` runs.

### Signal 4: Manual override (reason: `manual`)

The user can pass:

- `/pr-review 123 --ai` — force AI_SUSPECT=true with reason `manual`
- `/pr-review 123 --no-ai` — force AI_SUSPECT=false (clears any other signals for this run only)

Manual override always wins over the other three signals.

## Heightened-scrutiny behaviors

When `CONTENT_SCRUTINY=heightened` (i.e., `AI_SUSPECT=true`), the skill behaves differently in several places:

| Where | Behavior |
|---|---|
| Step 5 gating | `should-fact-check.sh` always returns RUN, even for non-content paths and bot/dependabot PRs |
| Step 5 claim extraction | Runs over the **full file**, not just diff context. AI hallucinates surrounding prose. |
| Step 5 verification | Web/`gh`/schema verification runs by default on every claim, not just claims that would normally graduate to it |
| Step 5 triage tiers | The bar for "Low-confidence verified" drops one level. Medium-confidence verified claims become *visible* instead of collapsed under `<details>`. |
| Step 6 confidence gauge | Prepends `🤖 AI-suspect (<reasons>)` and caps the gauge at MEDIUM. HIGH is impossible when AI-suspect is set. |
| Step 6 trivial-fix preview | Suppressed entirely, replaced with: `Trivial-fix auto-apply disabled (AI-suspect — manual review required)` |
| Step 8 merge toggle | Defaults **OFF** regardless of contributor type. |
| Auto-trivials script | Refuses to run; exits with `SKIP: AI_SUSPECT=true`. |

## Why heightened scrutiny doesn't depend on contributor type

The original conflation: "internal contributor → trusted → relax review." This is exactly wrong for AI-drafted PRs, because:

1. The most prolific AI-PR authors on the team are often the most senior people — they have the leverage to ship a lot, and they use AI to amplify it.
2. AI hallucinations in docs don't get caught by "trust the author" reasoning — they get caught by *actually verifying the claims*.
3. A trusted author who ships AI slop without checking it is, for review purposes, indistinguishable from an untrusted author. The signal that matters is "did a human verify this?" not "is the GitHub username on the org roster?"

So the rule is: **etiquette trust never relaxes content scrutiny.** Etiquette trust controls how warm the comment is. Content scrutiny controls how carefully the words are checked. They are independent.
