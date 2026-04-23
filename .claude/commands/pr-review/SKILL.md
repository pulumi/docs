---
name: pr-review
description: Review and approve/merge pull requests as a maintainer (full workflow with approve, request changes, merge, close actions)
---

# Pull Request Review Command

**Use this when:** You're reviewing someone's pull request as a maintainer and need to approve, request changes, merge, or close it.

Performs comprehensive review with style, code, and **factual claim verification**, then provides an interactive workflow for approval actions. Automatically detects contributor type and computes a **two-axis trust model** (etiquette + content scrutiny) plus an **AI-suspect flag** that forces heightened scrutiny on AI-generated PRs regardless of who wrote them.

---

## Usage

`/pr-review [<PR_NUMBER>] [--ai|--no-ai]`

Reviews any pull request and presents action choices for approval, changes, or closure.

**PR number**: Optional. If omitted, the workflow infers the PR from the current branch via `gh pr view --json number` — useful when you're already checked out on the branch under review. If no PR is open for the current branch, the workflow errors out and asks for an explicit number.

**Optional flags**:

- `--ai` — force AI-suspect ON for this run (heightened content scrutiny)
- `--no-ai` — force AI-suspect OFF for this run (clears any auto-detected signals)

**Works with**: All PRs (internal, external, and bots)

**Special handling**: Automatically detects contributor type and adapts messaging tone while keeping content scrutiny independent. Provides risk-based workflow for Dependabot PRs with testing checklists and label-driven recommendations.

---

## Process

**CRITICAL SUCCESS CRITERIA**: Complete all 10 steps in sequence. Every step is mandatory and serves a critical purpose in the review workflow. **DO NOT SKIP ANY STEP OR END THE WORKFLOW PREMATURELY!**

**Step Counter**: Display progress before each step as: **[Step X/10]** followed by the step heading. This helps users track progress through the workflow.

**References**: Always follow the detailed instructions in the referenced documents for each step. The references contain the complete implementation details required.

**Output discipline**: Steps 1, 2, 4, and 5 are **silent** — they produce no user-facing output. Step 3 is the only early interactive prompt and only fires for infra changes. Step 6 is the first comprehensive output, designed so the user reads one coherent package in one sitting rather than fragmenting attention across multiple status updates.

---

### Step 1: Detect contributor, trust axes, risk tier, and AI-suspect

**PR number resolution**: If `{{arg}}` is empty, infer the PR from the current branch first:

```bash
gh pr view --json number --jq '.number'
```

If this fails (no PR open for the current branch), abort the workflow with a clear error asking for an explicit PR number. Otherwise, use the inferred number as `PR_NUMBER` and substitute it for every `{{arg}}` reference in subsequent steps.

Run the contributor detection script with any manual override flag. The script itself also supports PR inference, but doing the inference at the workflow level lets downstream steps (that have hardcoded `{{arg}}` references) see the resolved number:

```bash
bash .claude/commands/pr-review/scripts/contributor-detection.sh $PR_NUMBER [--ai|--no-ai]
```

The script outputs:

- `AUTHOR` — GitHub username
- `CONTRIBUTOR_TYPE` — bot/internal/external
- `ETIQUETTE_TRUST` — low/standard/high (controls tone, welcome language, merge defaults)
- `CONTENT_SCRUTINY` — standard/heightened (controls review depth and fact-check aggressiveness)
- `AI_SUSPECT` — true/false
- `AI_SUSPECT_REASONS` — comma-separated list of triggers (allowlist, trailer:claude, prose-pattern:em-dash, manual)
- `RISK_TIER` — typo/minor/standard/major/infra
- `PR_METADATA` — JSON with number, title, url
- `FILES_CHANGED` — list of changed file paths
- `PR_DATA_JSON` — complete PR data for caching

Store all of these for later steps. **Do not display anything to the user yet** — Step 6 surfaces this information in the unified package header. The only exception is if the script fails: report the failure immediately.

See `pr-review:references:trust-and-scrutiny` for the full model.

Continue to Step 2.

### Step 2: Gather PR diff

1. View the full PR context: `gh pr view {{arg}}`
2. Get the diff: `gh pr diff {{arg}}`
3. Note the PR title, description, files changed, additions/deletions, and labels

**Silent step** — store data for later use. No output to the user.

Continue to Step 3.

### Step 3: Offer infrastructure deployment (only early interactive prompt)

Check if PR contains dependency or infrastructure changes (`RISK_TIER=infra` is the primary signal). See `pr-review:references:infrastructure-deployment` for patterns and workflow.

This is the **only step before Step 6 that produces user-facing output**, and only when infra changes are detected. If `RISK_TIER` is anything other than `infra`, this step is silent.

Continue to Step 4.

### Step 4: Comprehensive style and code review (silent)

#### 4a: Read full file contents

For every changed content file (`.md`, `.html`, or template files), read the **entire file** — not just the diff. This enables catching pre-existing issues that exist outside the changed lines.

When `RISK_TIER=major` or `CONTENT_SCRUTINY=heightened`, full-file reads are mandatory. For `RISK_TIER=typo` or `minor`, you may read only the diff context.

#### 4b: Style guide compliance

Review the full file content against STYLE-GUIDE.md. See `_common:review-criteria` for full criteria. Apply role-specific guidelines per content type.

For each issue found, classify as one of:

- **PR-introduced**: The issue is within lines added or modified by this PR's diff.
- **Pre-existing**: The issue exists in the file but was not introduced by this PR.

#### 4c: Code snippet verification

For every code example in changed files — both inline fenced code blocks and referenced `/static/programs/` files — verify correctness using the code examples criteria in `_common:review-criteria`. Read the full source of any referenced program files.

#### 4d: Program tests

If files under `static/programs/` are changed:

1. Check `scripts/programs/ignore.txt` — if the program is listed there, note it is ignored and skip testing.
2. For non-ignored programs, run:

   ```bash
   ONLY_TEST="program-name" ./scripts/programs/test.sh
   ```

3. Store pass/fail results for the Step 6 unified package.

#### 4e: PR description accuracy

Compare the PR description (from Step 2) against the actual diff. Inaccuracies — files mentioned that weren't changed, changes described that aren't in the diff, significant changes omitted, incorrect characterization of what the changes do — are **trivial-fix candidates**, not style/structure findings. Collect them for the Step 6 trivial-fix preview; do not include them in the style findings or let them influence the assessment.

For each inaccuracy, draft a corrected description that accurately reflects the diff. The corrected description will be applied via `gh pr edit --body` in Step 9 if not vetoed.

**Large diffs (>100 lines)**: Summarize findings by category rather than line-by-line.

**Silent step** — store all findings for Step 6. Do not display anything to the user yet.

Continue to Step 5.

### Step 5: Factual claim verification (silent)

This is the rigor enforcement step. See `_common:fact-check` for the complete procedure.

Summary:

1. **Gate** — run `should-fact-check.sh` with the contributor type, AI-suspect flag, and risk tier from Step 1. If SKIP, store the reason and continue to Step 6.
2. **Extract claims** — for each changed content file, extract structured factual claims (command behavior, version availability, API surface, cross-references, numerical claims). When `CONTENT_SCRUTINY=heightened`, extract from the **full file**, not just the diff.
3. **Dispatch parallel subagents** — batch up to 4 at a time, each verifying a small group of claims using the source order: local repo → `gh` CLI → live execution → WebFetch → Notion/Slack. Subagents return structured `{status, confidence, evidence, source, suggested_fix}` results.
4. **Collate into tiered triage** — build the structured object that Step 6 will render: `🚨 Needs your eyes` (contradicted + unverifiable), `⚠️ Low-confidence verified`, `✅ Verified` (collapsed).
5. **Populate author-question buffer** — every unverifiable claim becomes a line-anchored question for the comment body, used by Step 7/8 if Request changes is selected.

**Silent step** — store all results for Step 6.

Continue to Step 6.

### Step 6: Present unified review package

This is the **first big user-facing output of the run**. It merges what used to be the early deployment-guidance step and the late summary step into a single coherent block, plus the new fact-check tiers.

Render in this order, top to bottom:

1. **Confidence gauge** — single line:

   ```
   Confidence: HIGH · 14 claims verified · 0 contradicted · contributor: @user (internal, trusted) · risk: minor · CI: green
   ```

   Or, when AI-suspect:

   ```
   Confidence: MEDIUM · 🤖 AI-suspect (allowlist + trailer:claude) · scrutiny: heightened · 14 claims · 2 contradicted · 1 unverifiable · CI: green
   ```

   Computation:

   | Gauge | When |
   |---|---|
   | `HIGH` | No contradicted claims, no PR-introduced critical issues, CI green, scrutiny `standard` |
   | `MEDIUM` | Any unverifiable claims, OR scrutiny `heightened` (always caps at MEDIUM), OR CI yellow |
   | `LOW` | Any high-confidence contradicted claim, OR CI red, OR critical issues found |

2. **Header** — PR title, contributor with etiquette icon (🤖 / 📝 / 🌍), risk tier badge, deployment URL (or "pending"). Run `test-deployment-guidance.sh` here to fetch the deployment URL and per-page links:

   ```bash
   bash .claude/commands/pr-review/scripts/test-deployment-guidance.sh {{arg}}
   ```

3. **Per-page review links** — direct links + change-aware specific review items from `test-deployment-guidance.sh` output (headings → check structure, codeBlocks → test examples, images → verify loading, links → test navigation).

4. **Style + structure findings** — PR-introduced vs pre-existing, from Step 4. Use this format:

   ```markdown
   ### Issues introduced by this PR
   **[Category]**: [brief summary]
   - file:line: [issue description]

   ### Pre-existing issues
   These were not introduced by this PR but are improvement opportunities.
   - file:line: [issue description]
   ```

5. **Code verification results** — program test pass/fail, snippet checks from Step 4d:

   ```
   - program-name: ✅ pass / ❌ fail / ⏭️ ignored / 🔍 syntax-only
   - Inline snippet (file:line): ✅ valid / ⚠️ issue
   ```

6. **🔬 Fact-check triage** — tiered view from the fact-check phase (Needs your eyes → Low-confidence verified → collapsed Verified). Skipped if the gate returned skip — show the gate reason instead (one line).

7. **Trivial fixes preview** (only if any candidates) — itemized so the user can see exactly what will change before Step 8 confirmation:

   ```
   Trivial fix candidates (4):
     [1] content/docs/foo.md:12   — heading case: "Deploy To AWS" → "Deploy to AWS"
     [2] content/docs/foo.md (EOF) — add EOF newline
     [3] content/docs/bar.md:42   — strip trailing whitespace
     [4] PR description            — inaccuracy: says "updates bar.md" but bar.md was not changed
   ```

   Each candidate gets a numeric index so the user can veto specific fixes in Step 8. Categories the agent considers: trailing whitespace removal, missing EOF newlines, heading case (only when unambiguous — proper nouns like Pulumi/TypeScript/Azure are preserved), missing aliases on moved files, missing language specifier on fenced code blocks, PR description inaccuracies (description text that misrepresents the diff — corrected via `gh pr edit --body`).

   Suppressed entirely when AI-suspect, replaced with:

   ```
   Trivial-fix auto-apply disabled (AI-suspect — manual review required)
   ```

8. **Overall assessment** — single line: Clean / Minor issues / Issues found / Critical issues. Computed from PR-introduced findings and fact-check results per the assessment rules in `_common:fact-check`. Pre-existing issues alone do not gate approval.

9. **Recommendations** — short, specific, action-oriented.

**ADHD principle**: This whole package lands in **one** message so the user reads it in one sitting. The confidence gauge alone is often sufficient — if it's HIGH, scroll directly to the action menu.

Continue to Step 7.

### Step 7: Present action menu

**Use AskUserQuestion** (max 4 options) to present the appropriate action menu. Selection is adaptive:

- **Bot PR** → bot menu (see `pr-review:references:action-menus`)
- **Issues with high-confidence suggested fixes** → Scenario A: "Make changes and approve" recommended
- **Issues without reliable fixes** → Scenario B: "Request changes" recommended (author-question buffer auto-fills the comment)
- **Clean review** → Scenario C: "Approve" recommended
- **Should close** → Scenario D: "Close PR" recommended

**Important**: The Step 7 menu chooses *what* to do. Whether the action is followed by an auto-merge is decided in Step 8 via the merge toggle. Never add an "Approve and merge" option to a Step 7 menu.

See `pr-review:references:action-menus` for complete menu structures and recommendation logic.

Continue to Step 8 with selected action.

### Step 8: Preview action and confirm (with merge toggle)

**CRITICAL**: Always show what will happen before executing.

See `pr-review:references:action-preview-templates` for preview formats.

Display the preview showing:

- The chosen action
- The **`Auto-merge after approval` toggle** with its computed default state (see toggle defaults below)
- For "Make changes and approve": file-by-file changes (trivial fixes summary + suggested-fix list)
- The exact comment text that will be posted (using templates from `pr-review:references:message-templates`). The posted comment must obey the voice/length rules at the top of that file: Step 6's rich local package is for the reviewer's eyes, **not** a draft for the public comment. Never disclose scrutiny level, AI-suspect status, or fact-check narration in the posted text, and never tack on a self-merge footer -- the auto-merge toggle handles that silently.
- The full list of `gh` commands that will run

**Auto-merge toggle defaults**:

| Default | When |
|---|---|
| ON | Bot PR (dependabot/pulumi-bot/renovate/copilot) AND CI green AND no contradictions AND `AI_SUSPECT=false` |
| OFF | All human-authored PRs (Pulumi convention: authors merge their own PRs) |
| OFF | Any PR with `AI_SUSPECT=true`, regardless of contributor type |

**Confirmation options** (use AskUserQuestion). The menu is context-adaptive — slot 2 changes depending on what's in the pending action:

When trivial fixes are pending (Make changes and approve):

1. **Yes, proceed** — Execute as previewed
2. **Veto trivial fix(es)** — Drop one or more trivial fixes from the candidate list
3. **Toggle merge** — Flip the auto-merge toggle
4. **Cancel** — Exit without changes

When approving as-is with suppressable findings (Approve action with at least one PR-introduced finding in the comment body):

1. **Yes, proceed** — Execute as previewed
2. **Suppress finding(s)** — Drop one or more findings from the approval comment so the author isn't pestered about every nit
3. **Toggle merge** — Flip the auto-merge toggle
4. **Cancel** — Exit without changes

When nothing is suppressable:

1. **Yes, proceed** — Execute as previewed
2. **Edit comment** — Modify comment text
3. **Toggle merge** — Flip the auto-merge toggle
4. **Cancel** — Exit without changes

Edit comment is always reachable via the AskUserQuestion `Other` field even when not in the explicit slot.

Handle each response per `pr-review:references:action-preview-templates`. The trivial-fix list, the suppressed-findings list, the toggle, and the comment can all be edited as many times as the user wants without re-running the workflow. Locked findings (high-confidence contradictions without a suggested fix) cannot be suppressed.

Continue to Step 9 with confirmed action and toggle state.

### Step 9: Execute confirmed action

Execute using the confirmed/edited content from Step 8, including the merge toggle state.

**Commands by action** (with merge toggle ON):

- **Approve**: `gh pr review {{arg}} --approve --body "{{COMMENT}}"` then `gh pr merge {{arg}} --auto --squash`
- **Make changes and approve**: full make-changes workflow (see below) followed by merge
- **Request changes**: `gh pr review {{arg}} --request-changes --body "{{COMMENT}}"`
- **Close PR**: `gh pr comment {{arg}} --body "{{COMMENT}}"` then `gh pr close {{arg}}`
- **Do nothing yet**: Exit with message

With merge toggle OFF, omit the `gh pr merge` step from Approve and Make changes and approve.

**Make changes and approve workflow**:

1. Save current branch name
2. `gh pr checkout {{arg}}`
3. Apply surviving PR description fixes via `gh pr edit {{arg}} --body "$CORRECTED_BODY"` (this doesn't touch the branch, so it goes before file edits)
4. Apply trivial fixes that **survived the user's veto in Step 8**, using Edit. The agent applies these directly rather than via a script because several categories (notably heading case) require language understanding to avoid corrupting proper nouns like Pulumi, TypeScript, Azure, Kubernetes, etc. — a regex can't tell "Working With Pulumi" (preserve "Pulumi") from "Deploy To AWS" (lowercase "to"). When in doubt, skip the fix and surface it to the user. Suppressed entirely when `AI_SUSPECT=true`.
5. Apply contradicted-claim suggested fixes via Edit
6. Show diff to user
7. Commit with author trailer:

   ```
   <commit message>


   Co-Authored-By: <agent name> <agent email>
   ```

8. Push
9. Approve with comment
10. If toggle ON: `gh pr merge {{arg}} --auto --squash`
11. **Always** return to original branch (even on error)

Continue to Step 10.

### Step 10: Report execution results

See `pr-review:references:execution-results` for result message templates.

Display the appropriate success message with:

- Confirmation of action taken (and whether merge was queued)
- PR URL for easy access
- Additional context (bot info, risk tier, deployment warnings)
- Verification commands where helpful

**For Dependabot HIGH/MEDIUM with merge queued**: Warn that next merge to master triggers pulumi-test.io deployment.

Workflow complete.

---

## Critical Workflow Rules

1. **Complete all 10 steps in sequence** — Never skip steps or end workflow prematurely
2. **Silent run-up to Step 6** — Steps 1, 2, 4, and 5 produce no user-facing output. Step 3 is the only early interactive prompt, and only fires for infra changes. Step 6 is the first comprehensive output.
3. **Step 5 docs gating** — Never run fact-check on bot/dependabot PRs unless AI-suspect is set; the gate script is authoritative.
4. **AI-suspect overrides trust** — `CONTENT_SCRUTINY=heightened` overrides any etiquette-trust-based relaxation. Internal-contributor status never relaxes content scrutiny when AI-suspect is set.
5. **Subagent budget** — Max 4 parallel fact-check subagents at once; if >20 claims extracted, batch by file rather than per-claim.
6. **MCP availability** — Notion/Slack steps are best-effort; absence of those tools must not fail the workflow, only annotate the evidence as "internal sources unavailable".
7. **Local allowlist is private** — `~/.claude/pr-review/ai-suspect-authors.txt` is read-only as far as the skill is concerned. Never created, written, or printed in full to any output. Only the *fact* that AI-suspect was triggered and the reason (`allowlist`) appears in the gauge.
8. **Always preview before execution** — Show exactly what will happen (Step 8) before executing (Step 9), including the merge toggle state.
9. **Use confirmed content** — Execute only with user-approved text from Step 8.
10. **Track progress** — Display **[Step X/10]** before each step heading.
11. **Preserve branch safety** — For "Make changes and approve": save current branch, return to it even on errors.
12. **Never add an "Approve and merge" menu option** — Merge is always a toggle in Step 8, never a Step 7 choice.

---

## Error Recovery

If any command fails during execution:

```text
❌ Failed to [action] PR #{{arg}}

Error: [error message]

Recovery options:
- /pr-review {{arg}} (re-run full workflow)
- Or use gh CLI directly: [relevant commands based on failure]
```

For "Make changes and approve" failures: Always return to original branch before reporting error.
