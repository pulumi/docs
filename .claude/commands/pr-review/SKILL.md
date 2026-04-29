---
name: pr-review
description: Adjudicate a pull request as a maintainer. Reads the CI-posted pinned review as the source of truth, refreshes it if stale, and provides an interactive workflow to approve / request changes / make changes / close — with optional auto-merge.
---

# Pull Request Review Command

This is the maintainer adjudication layer on top of the CI review pipeline (`claude-code-review.yml` posts a pinned `<!-- CLAUDE_REVIEW N/M -->` comment with all findings; this skill reads that as the source of truth). The goal is **fast adjudication**, not parallel review — duplicate review work was the original anti-pattern.

## Usage

`/pr-review [<PR_NUMBER>] [--ai|--no-ai]`

- **PR number**: Optional. If omitted, the workflow infers from the current branch via `gh pr view --json number`. Errors out if no PR is open for the branch.
- `--ai` / `--no-ai`: force AI-suspect ON or OFF for this run.

Works with all PRs (internal, external, bots).

---

## Process

Complete all 10 steps in sequence. Display **[Step X/10]** before each step heading.

Steps 1, 2, 3, 5 are **silent** — no user-facing output. Step 4 is interactive only when the PR has infra changes. Step 6 is the first comprehensive output.

---

### Step 1: Detect contributor, trust axes, risk tier, and AI-suspect

If `{{arg}}` is empty, infer the PR from the current branch:

```bash
gh pr view --json number --jq '.number'
```

If that fails, abort with a clear error asking for an explicit PR number. Otherwise use the inferred number as `PR_NUMBER` for every `{{arg}}` reference below.

Run contributor detection:

```bash
bash .claude/commands/pr-review/scripts/contributor-detection.sh $PR_NUMBER [--ai|--no-ai]
```

The script outputs:

- `AUTHOR` — GitHub username
- `CONTRIBUTOR_TYPE` — bot/internal/external
- `ETIQUETTE_TRUST` — low/standard/high (controls tone, welcome language, merge defaults)
- `CONTENT_SCRUTINY` — standard/heightened
- `AI_SUSPECT` — true/false
- `AI_SUSPECT_REASONS` — comma-separated triggers
- `RISK_TIER` — typo/minor/standard/major/infra
- `PR_METADATA` — JSON with number, title, url
- `FILES_CHANGED` — list of changed file paths
- `LABELS` — comma-separated current labels (drives Step 2's pinned-review state machine)
- `PR_DATA_JSON` — complete PR data

Store all of these. **No user output yet.** Step 6 surfaces them in the unified package.

See `pr-review:references:trust-and-scrutiny`.

### Step 2: Fetch the pinned CI review and classify state

Fetch the diff and the pinned review:

```bash
gh pr diff "$PR_NUMBER"

bash .claude/commands/docs-review/scripts/pinned-comment.sh fetch --pr "$PR_NUMBER"
```

Determine the pinned-review state from labels and fetch output:

| State | Detection | What Step 3 does |
|---|---|---|
| `CURRENT` | `review:claude-ran` set, `review:claude-stale` absent, fetch returns body | Nothing — proceed to Step 4 |
| `STALE` | `review:claude-stale` set | Refresh in place by invoking `docs-review:references:update` locally (Sonnet pass + `pinned-comment.sh upsert`) |
| `WORKING` | `review:claude-working` set | CI is producing the review right now; abort with a message asking the user to retry in a few minutes |
| `ABSENT` | Fetch returns no `<!-- CLAUDE_REVIEW -->` markers | Fall back: run a local review (see Step 3 §Absent path) |

Store the parsed pinned-comment findings (🚨 Outstanding, ⚠️ Low-confidence, 💡 Pre-existing, ✅ Resolved, 📜 Review history) for Step 6.

### Step 3: Resolve pinned-review state

Branch on the state from Step 2.

#### CURRENT

Continue to Step 4.

#### STALE

Refresh the pinned comment in place by invoking `docs-review:references:update` locally with `PR_NUMBER` set. The update procedure runs the Sonnet refresh (re-reading the diff since the last reviewed SHA, classifying as Case 1/2/3, and writing the refreshed body via `pinned-comment.sh upsert`). When it completes, re-fetch the pinned comment and re-parse findings for Step 6.

This is a real GitHub-state write. The contributor-facing pinned comment will reflect the refresh regardless of whether the user proceeds to approve.

#### WORKING

A CI review is in flight. Abort:

```text
⏳ CI is currently running a review on PR #{{arg}} (label: review:claude-working).

Re-run /pr-review {{arg}} when the run completes (typically 1–5 minutes).
```

#### ABSENT

No pinned comment exists. This typically means: the PR is a draft (CI doesn't review drafts), CI failed, or the `review:trivial` short-circuit fired. Ask the user how to proceed via AskUserQuestion:

1. **Run a local review now** — perform a full local style + code review (apply `docs-review:references:shared-criteria` plus the appropriate domain criteria per file) and a fact-check pass via `docs-review:references:fact-check`. Slow but thorough.
2. **Adjudicate without findings** — proceed to Step 6 with no findings; rely on your own diff read and the contributor's PR description.
3. **Cancel** — exit; consider transitioning the PR to ready-for-review to trigger CI, or mention `@claude` to invoke a fresh review.

Only the local-review path produces findings; otherwise Step 6 renders an empty findings block.

### Step 4: Offer infrastructure deployment (only fires for infra changes)

If `RISK_TIER=infra` (PR contains dependency or infrastructure changes), follow `pr-review:references:infrastructure-deployment` to optionally trigger a pulumi-test.io deployment. This is the only step before Step 6 that produces user-facing output. For other risk tiers, skip silently.

### Step 5: PR description accuracy check (silent)

CI doesn't check this; pr-review does. Compare the PR description against the actual diff. Inaccuracies — files mentioned that weren't changed, changes described that aren't in the diff, significant changes omitted, incorrect characterization — are **trivial-fix candidates** that can be applied via `gh pr edit --body` in Step 9 if the user picks Make-changes-and-approve and doesn't veto them.

For each inaccuracy, draft a corrected description that accurately reflects the diff. Store for Step 6 + Step 9.

### Step 6: Present unified review package

This is the **first big user-facing output**. Render in this order, top to bottom:

1. **Confidence gauge** — single line:

   ```text
   Confidence: HIGH · 0 outstanding · 2 low-confidence · contributor: @user (internal) · risk: minor · CI: green · pinned: current
   ```

   Or, when AI-suspect:

   ```text
   Confidence: MEDIUM · 🤖 AI-suspect (allowlist + trailer:claude) · scrutiny: heightened · 2 outstanding · 1 low-confidence · CI: green · pinned: refreshed
   ```

   Computation:

   | Gauge | When |
   |---|---|
   | `HIGH` | No 🚨 Outstanding findings, CI green, scrutiny `standard`, pinned current/refreshed |
   | `MEDIUM` | Any ⚠️ Low-confidence findings, OR scrutiny `heightened` (always caps at MEDIUM), OR CI yellow, OR pinned absent |
   | `LOW` | Any 🚨 Outstanding finding, OR CI red |

2. **Header** — PR title, contributor with etiquette icon (🤖 / 📝 / 🌍), risk tier badge, pinned-review state, deployment URL (or "pending"). Run `test-deployment-guidance.sh` here to fetch the deployment URL and per-page links:

   ```bash
   bash .claude/commands/pr-review/scripts/test-deployment-guidance.sh {{arg}}
   ```

3. **Per-page review links** — direct links + change-aware specific review items from `test-deployment-guidance.sh` output.

4. **Pinned review findings** — render the parsed 🚨 Outstanding, ⚠️ Low-confidence, 💡 Pre-existing, and ✅ Resolved findings from Step 2 verbatim (they're already in the format from `docs-review:references:output-format`). If a refresh ran in Step 3, note "*Pinned comment refreshed at HH:MM*" above the findings block. If absent and the user picked local review in Step 3, render those findings here in the same format.

5. **PR description inaccuracies** (only if Step 5 found any) — itemized so the user can see exactly what would change before Step 8 confirmation:

   ```text
   PR description corrections (2):
     [1] Says "updates content/blog/foo.md" but foo.md was not changed
     [2] Omits significant change: content/docs/bar.md was renamed
   ```

   Each item gets a numeric index for veto in Step 8.

6. **Trivial-fix candidates** (only if any) — applied via Make-changes-and-approve. Categories: trailing whitespace, missing EOF newlines, sentence-case headings (proper nouns preserved), missing aliases on moved files, missing language specifier on fenced code blocks. Suppressed entirely when AI-suspect, replaced with:

   ```text
   Trivial-fix auto-apply disabled (AI-suspect — manual review required)
   ```

7. **Overall assessment** — single line: Clean / Minor issues / Issues found / Critical issues. Computed from the pinned 🚨 Outstanding count and any code-correctness findings. Pre-existing alone does not gate approval.

8. **Recommendations** — short, action-oriented. Map directly to a Step 7 menu (e.g., "→ Approve" or "→ Make changes and approve").

Render the whole package in one message.

### Step 7: Present action menu

Use AskUserQuestion (max 4 options). Selection is adaptive based on findings:

- **Bot PR** → bot menu
- **🚨 Outstanding findings with high-confidence suggested fixes** → Scenario A: "Make changes and approve" recommended
- **🚨 Outstanding findings without reliable fixes** → Scenario B: "Request changes" recommended (the pinned author-question buffer pre-fills the comment)
- **No 🚨 Outstanding** → Scenario C: "Approve" recommended
- **Should close** → Scenario D: "Close PR" recommended

The Step 7 menu chooses *what* to do. Auto-merge is decided in Step 8 via the merge toggle, never as a Step 7 option.

See `pr-review:references:action-menus`.

### Step 8: Preview action and confirm (with merge toggle)

See `pr-review:references:action-preview-templates`.

The preview shows:

- Chosen action
- Auto-merge toggle with computed default (per the toggle defaults in `pr-review:references:action-preview-templates`)
- For Make-changes-and-approve: file-by-file changes (PR description corrections + trivial fixes + suggested fixes from CI's pinned findings)
- The exact comment text that will be posted (using `pr-review:references:message-templates`)
- The full list of `gh` commands that will run

The posted comment must obey the voice/length rules in `pr-review:references:message-templates`: never disclose scrutiny level, AI-suspect status, the pinned-comment refresh, or fact-check narration. Step 6's local package is for the maintainer's eyes; the public maintainer comment is its own thing.

The confirmation menu adapts to the pending action:

| Pending | Slot 2 |
|---|---|
| Make-changes-and-approve | **Veto trivial fix(es) / PR description correction(s)** |
| Approve with suppressable findings | **Suppress finding(s)** |
| Approve with disputable findings | **Dispute finding(s)** *(only when 🚨 Outstanding findings exist; opt-in)* |
| Otherwise | **Edit comment** |

Slots 1, 3, 4 are always: **Yes, proceed** / **Toggle merge** / **Cancel**.

#### Dispute path (opt-in)

When the user picks "Dispute finding(s)", AskUserQuestion prompts for the finding number(s) and the dispute reasoning. pr-review composes a mention body in this shape:

```text
[Maintainer dispute from @{{user}}]

Finding {{N}} (in {{file:line}}, {{summary}}): {{reasoning}}

Adjudicate per Case 2 dispute rules.
```

The body is fed to `docs-review:references:update` locally with `MENTION_BODY` populated. Update.md Case 2 takes over: classifies the dispute (domain-knowledge / verifiable / reframing), concedes or holds with citation, and re-renders the pinned comment via `pinned-comment.sh upsert`. Re-fetch the pinned comment afterwards so the Step 6 view reflects the resolution before the action proceeds.

Maintainer write-access is sufficient evidence for domain-knowledge disputes (per `docs-review:references:update` Case 2).

### Step 9: Execute confirmed action

Execute using the confirmed/edited content from Step 8, including the merge toggle state.

| Action | Commands (toggle ON) | Commands (toggle OFF) |
|---|---|---|
| **Approve** | `gh pr review {{arg}} --approve --body "{{COMMENT}}"` then `gh pr merge {{arg}} --auto --squash` | `gh pr review {{arg}} --approve --body "{{COMMENT}}"` |
| **Make changes and approve** | Make-changes workflow (below) followed by merge | Make-changes workflow, no merge |
| **Request changes** | `gh pr review {{arg}} --request-changes --body "{{COMMENT}}"` | (toggle hidden) |
| **Close PR** | `gh pr comment {{arg}} --body "{{COMMENT}}"` then `gh pr close {{arg}}` | (toggle hidden) |
| **Do nothing yet** | Exit with message | (same) |

#### Make-changes-and-approve workflow

1. Save current branch
2. `gh pr checkout {{arg}}`
3. Apply surviving PR description corrections via `gh pr edit {{arg}} --body "$CORRECTED_BODY"`
4. Apply non-vetoed trivial fixes via Edit (agent-applied with language judgment to preserve proper nouns; suppressed entirely when `AI_SUSPECT=true`)
5. Apply CI-flagged 🚨 contradicted-claim suggested fixes via Edit
6. Show diff to user
7. Commit with author trailer:

   ```text
   <commit message>


   Co-Authored-By: <agent name> <agent email>
   ```

8. Push
9. Approve with comment
10. If toggle ON: `gh pr merge {{arg}} --auto --squash`
11. **Always** return to original branch (even on error)

### Step 10: Report execution results

See `pr-review:references:execution-results`.

Workflow complete.

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

For Make-changes-and-approve failures: always return to original branch before reporting error.
