---
name: pr-review
description: Adjudicate a pull request as a maintainer. Reads the CI-posted pinned review as the source of truth, refreshes it if stale, and provides an interactive workflow to approve / request changes / make changes / close — with optional auto-merge.
---

# Pull Request Review Command

This is the maintainer adjudication layer on top of the CI review pipeline (`claude-code-review.yml` posts a pinned `<!-- CLAUDE_REVIEW N/M -->` comment with all findings; this skill reads it as the source of truth).

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
| `CURRENT` | `review:outstanding-issues` or `review:no-blockers` set; `review:stale` / `review:in-progress` / `review:error` absent; fetch returns body | Nothing — proceed to Step 4 |
| `STALE` | `review:stale` set | Refresh in place by invoking `docs-review:references:update` locally (re-runs claim verification against new commits, then writes via `pinned-comment.sh upsert`) |
| `IN_PROGRESS` | `review:in-progress` set | Wait briefly for the workflow to finish; re-check labels. If it stays >15 min, treat as `ERROR`. |
| `ERROR` | `review:error` set (or `review:in-progress` stuck) | Investigate the Actions logs before proceeding |
| `ABSENT` | Fetch returns no `<!-- CLAUDE_REVIEW -->` markers | Fall back: run a local review (see Step 3 §Absent path) |

Store the parsed pinned-comment findings (🚨 Outstanding, ⚠️ Low-confidence, 💡 Pre-existing, ✅ Resolved, 📜 Review history) for Step 6.

### Step 3: Resolve pinned-review state

Branch on the state from Step 2.

#### CURRENT

Continue to Step 4.

#### STALE

Refresh the pinned comment in place by invoking `docs-review:references:update` locally with `PR_NUMBER` set. The update procedure re-reads the diff since the last reviewed SHA, classifies as Case 1/2/3, and writes the refreshed body via `pinned-comment.sh upsert`. When it completes, re-fetch the pinned comment and re-parse findings for Step 6.

#### ABSENT

No pinned comment exists. This typically means: the PR is a draft (CI doesn't review drafts), CI failed, or the `review:trivial` short-circuit fired. Ask the user how to proceed via AskUserQuestion:

1. **Run a local review now** — perform a full local style + code review (apply `/docs-review`). Use the findings as the pinned-review findings for Step 6.
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

6. **Trivial-fix candidates** (only if any) — applied via Make-changes-and-approve per `pr-review:references:action-preview-templates`. Suppressed when AI-suspect; see action-preview-templates §AI-suspect override.

7. **Overall assessment** — single line: Clean / Minor issues / Issues found / Critical issues. Computed from the pinned 🚨 Outstanding count and any code-correctness findings. Pre-existing alone does not gate approval.

8. **Recommendations** — short, action-oriented. Map directly to a Step 7 menu (e.g., "→ Approve" or "→ Make changes and approve").

Render the whole package in one message.

### Step 7: Present action menu

Use AskUserQuestion. Adaptive-scenario selection (which menu fires for which finding shape) and per-scenario options live in `pr-review:references:action-menus`. The Step 7 menu chooses *what* to do; auto-merge is decided in Step 8 via the merge toggle, never as a Step 7 option.

### Step 8: Preview action and confirm (with merge toggle)

See `pr-review:references:action-preview-templates`.

The preview shows:

- Chosen action
- Auto-merge toggle with computed default (per the toggle defaults in `pr-review:references:action-preview-templates`)
- For Make-changes-and-approve: file-by-file changes (PR description corrections + trivial fixes + suggested fixes from CI's pinned findings)
- The exact comment text that will be posted (using `pr-review:references:message-templates`)
- The full list of `gh` commands that will run

The posted comment must obey the voice/length rules in `pr-review:references:message-templates`. Step 6's local package is for the maintainer's eyes; the public maintainer comment is its own thing.

Confirmation-menu adaptation (slot 2 changes per pending action; dispute-path opt-in is described below) lives in `pr-review:references:action-preview-templates` §Confirmation Question.

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

Execute per the commands and workflow in `pr-review:references:action-preview-templates`, using the merge-toggle state confirmed in Step 8. For Make-changes-and-approve failures: always return to original branch before reporting error.

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
