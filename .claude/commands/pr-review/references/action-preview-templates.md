---
user-invocable: false
description: Preview formats and confirmation flows for PR actions
---

# Action Preview Templates

**CRITICAL**: Always show what will happen before executing any action.

## Preview format

Every preview shows the chosen action, the merge toggle, any auto-applied changes, and the comment body that will be posted. Order:

```
## Preview

Action: <action>
[x] Auto-merge after approval (squash)   ← toggle, default depends on rules below

[If "Make changes and approve"]
Trivial fixes (will be applied):
  <N> trivial fixes: <breakdown>  [show diff]

Contradicted-claim fixes (will be applied):
  <file:line> — "<replacement text>"
  ...

Comment body that will be posted:
  <full comment>

Commands that will run:
  <list of gh commands>
```

When `AI_SUSPECT=true`, the trivial-fixes section is replaced with:

```
Trivial-fix auto-apply disabled (AI-suspect — manual review required)
```

## Auto-merge toggle defaults

The toggle's initial state is determined by these rules. The user can flip it during preview without re-navigating menus.

### Toggle defaults ON

Only when **all** of:

- Contributor is a **bot** (dependabot, pulumi-bot, renovate, copilot, github-actions)
- CI is green
- No remaining contradictions or unverifiable claims
- `AI_SUSPECT=false`

### Toggle defaults OFF

For all human-authored PRs, regardless of seniority, contributor type, or CI status. Pulumi convention: authors merge their own PRs.

### AI-suspect override

When `AI_SUSPECT=true`, the toggle defaults OFF unconditionally — even for bot PRs.

## Standard Action Previews

| Action | Commands (with merge toggle ON) | Commands (with merge toggle OFF) |
|--------|----------------------------------|----------------------------------|
| **Approve** | `gh pr review {{arg}} --approve --body "{{COMMENT}}"`<br>`gh pr merge {{arg}} --auto --squash` | `gh pr review {{arg}} --approve --body "{{COMMENT}}"` |
| **Make changes and approve** | (See workflow below) followed by merge | (See workflow below), no merge |
| **Request changes** | `gh pr review {{arg}} --request-changes --body "{{COMMENT}}"` | (same — merge toggle hidden for this action) |
| **Close PR** | `gh pr comment {{arg}} --body "{{COMMENT}}"`<br>`gh pr close {{arg}}` | (same — merge toggle hidden for this action) |
| **Do nothing yet** | No changes will be made to PR #{{arg}}.<br>Run /pr-review {{arg}} again when ready. | (same) |

The merge toggle is shown only when the chosen action is `Approve` or `Make changes and approve`. For `Request changes`, `Close PR`, and `Do nothing yet`, it's hidden.

## Make Changes and Approve Preview

**Note**: Not available for bot PRs (excluded from bot menus).

**Flow**: Pull the candidate fixes from two sources, show the preview, confirm (with veto opportunity), then execute:

```
## Preview: Make Changes and Approve

Action: Make changes and approve
[ ] Auto-merge after approval (squash)   ← OFF by default for human PRs

Trivial fix candidates (4) — will be applied unless vetoed:
  [1] content/docs/foo.md:12   — heading case: "Deploy To AWS" → "Deploy to AWS"
  [2] content/docs/foo.md (EOF) — add EOF newline
  [3] content/docs/bar.md:42   — strip trailing whitespace
  [4] PR description            — inaccuracy: says "updates bar.md" but bar.md was not changed

Contradicted-claim fixes (will be applied):
  content/docs/cli/logout.md:42 — "removes credentials for the current backend"
  content/blog/foo.md:88        — "available since v3.230.0 (not v3.220.0)"

Comment body that will be posted:
  [Template from message-templates.md]

I will:
1. Save current branch
2. Check out PR: gh pr checkout {{arg}}
3. Apply surviving PR description fixes: gh pr edit {{arg}} --body "$CORRECTED_BODY"
4. Apply each non-vetoed trivial fix via Edit
5. Apply contradicted-claim suggested fixes via Edit
6. Show diff
7. Commit: "Apply review fixes\n\nCo-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
8. Push changes
9. Approve with comment above
10. [If toggle ON] gh pr merge {{arg}} --auto --squash
11. Return to original branch
```

### Trivial fix candidates

Apply trivial fixes one-by-one with language judgment (heading case especially — preserve proper nouns like Pulumi, TypeScript, Azure, Kubernetes). When a fix is genuinely ambiguous, skip and surface it rather than apply.

Categories the agent considers:

- Trailing whitespace removal
- Missing EOF newlines
- Sentence-case headings (only when unambiguous — preserve proper nouns)
- Missing aliases on moved files
- Missing language specifier on fenced code blocks (only when unambiguous from context)
- PR description inaccuracies (description text that misrepresents the diff — applied via `gh pr edit --body`, not file edit)

Each candidate is itemized in the preview with a numeric index so the user can veto specific fixes.

**Suppressed entirely when `AI_SUSPECT=true`** (see `pr-review:references:trust-and-scrutiny`) — the AI may have introduced subtly wrong "fixes" that look like typos but aren't.

See SKILL.md Step 9 for complete workflow details.

## Approve-as-is Preview (with finding suppression)

**When used**: The user picks **Approve** (or the adaptive menu's "Approve as-is" variant) while findings exist that weren't addressed. Pulumi convention is to let authors merge their own PRs, but not every finding needs to become a comment — sometimes the author knows what they're doing, and listing every nit is just being pedantic.

The preview itemizes every finding that *would* land in the approval comment, and the confirmation menu's slot 2 becomes **Suppress finding(s)** so the user can drop specific items before the comment is posted. Suppressed findings are silently dropped — the author never sees them.

```
## Preview: Approve

Action: Approve (as-is)
[ ] Auto-merge after approval (squash)   ← OFF by default for human PRs

Findings that will be mentioned in the approval comment (3):
  [1] content/docs/foo.md:12   — style: heading could lead with primary search term
  [2] content/docs/foo.md:45   — fact-check: unverifiable claim "supported in v3.230+"
  [3] content/blog/bar.md:88   — style: heavy em-dash usage

Comment body that will be posted:
  LGTM! A few minor things I noticed but didn't flag for changes:

  - `foo.md:12` — heading could lead with the primary search term
  - `foo.md:45` — couldn't independently verify "supported in v3.230+"
  - `bar.md:88` — heavy em-dash usage

  Approving as-is.
```

### Suppression rules

- **Only PR-introduced findings** are candidates. Pre-existing findings are never mentioned in an approval comment — they're the previous author's work and nagging about them is rude.
- **Contradicted claims with high confidence and no suggested fix** cannot be suppressed. If the review found something that's definitely wrong with no obvious fix, the author needs to hear about it. The menu shows these as `[locked]` and they stay in the comment regardless of suppression requests.
- **All other findings are suppressable**: style nits, low-confidence contradictions, unverifiable claims, SEO suggestions, formatting observations.

When every suppressable finding is dropped, the comment collapses to a clean "LGTM!" with no laundry list. If only locked findings remain, the comment shows just those.

### Rebuilding the comment after suppression

The comment body is **regenerated** from the surviving findings every time the user suppresses more. This is different from the merge-toggle flow (where the preview is not re-displayed) because the comment body itself is changing and the user needs to see what's actually going to be posted.

After each suppression pass:

1. Rebuild the comment body from the surviving findings using the relevant `pr-review:references:message-templates` template
2. Re-display **only the updated findings list + updated comment body** (not the full preview header or the action/toggle lines)
3. Re-ask the confirmation question

## Confirmation Question

Use AskUserQuestion with these options. The menu is **context-adaptive** — slot 2 changes based on what's pending.

**Question**: "Proceed with this action?"

**When trivial fixes are pending** (Make changes and approve with at least one trivial fix candidate):

1. **Yes, proceed** - Execute the action as previewed
2. **Veto trivial fix(es)** - Drop one or more trivial fixes from the candidate list
3. **Toggle merge** - Flip the auto-merge toggle (no re-preview)
4. **Cancel** - Exit without making any changes

**When approving as-is with suppressable findings** (Approve action and at least one PR-introduced finding exists in the comment body):

1. **Yes, proceed** - Execute the action as previewed
2. **Suppress finding(s)** - Drop one or more findings from the approval comment
3. **Toggle merge** - Flip the auto-merge toggle (no re-preview)
4. **Cancel** - Exit without making any changes

**When nothing is suppressable**:

1. **Yes, proceed** - Execute the action as previewed
2. **Edit comment** - Modify the comment text before executing
3. **Toggle merge** - Flip the auto-merge toggle (no re-preview)
4. **Cancel** - Exit without making any changes

Edit comment is always reachable through the AskUserQuestion `Other` field even when not in the explicit slot. The trivial-fix veto and finding-suppression slots are mutually exclusive (the former only appears for Make changes and approve; the latter only for Approve as-is).

## Response Handling

### Yes, proceed

- Continue to execution step
- Use exact content from preview, including current toggle state and the surviving trivial-fix candidate list

### Veto trivial fix(es)

1. Use AskUserQuestion with an open-ended `Other` prompt: "Which trivial fixes should we skip? (e.g. `1`, `1,3`, `all heading-case`, `all`)"
2. Parse the response:
   - Numeric indices (`1`, `1,3`, `2 4`) → drop those candidates by index
   - `all` → drop every trivial fix candidate
   - `all <category>` (`all heading-case`, `all trailing-ws`, `all eof`, `all alias`, `all lang-spec`, `all desc-inaccuracy`) → drop every candidate in that category
3. Re-display **only the updated trivial fix candidates section** (not the full preview), then re-ask the confirmation question. The user can veto more fixes, toggle merge, edit the comment, or proceed.

### Suppress finding(s)

1. Use AskUserQuestion with an open-ended `Other` prompt: "Which findings should we leave out of the approval comment? (e.g. `1`, `1,3`, `all style`, `all fact-check`, `all`)"
2. Parse the response:
   - Numeric indices (`1`, `1,3`, `2 4`) → drop those findings from the comment
   - `all` → drop every suppressable finding (locked findings stay; see "Suppression rules" above)
   - `all <category>` (`all style`, `all fact-check`, `all seo`, `all format`, ...) → drop every suppressable finding in that category
3. **Rebuild the comment body** from the surviving findings using the relevant `pr-review:references:message-templates` template. If no findings survive, collapse to a clean "LGTM!" template with no laundry list.
4. Re-display **only the updated findings list + updated comment body** (not the full preview header or the action/toggle lines), then re-ask the confirmation question.

Locked findings — high-confidence contradicted claims with no suggested fix — cannot be suppressed. If the user's suppression request would drop a locked finding, print: `Finding [N] is locked and cannot be suppressed: <reason>` and leave it in the comment. The rest of the request is still applied.

### Toggle merge

- Flip the `Auto-merge after approval` toggle (ON ↔ OFF)
- Print a single-line confirmation: `Auto-merge toggle is now ON` (or `OFF`)
- Re-ask the confirmation question — **do not** re-display the full preview. The user just saw it; they only need the new toggle state and the menu.

### Edit comment

1. Use AskUserQuestion to ask user for revised comment text (open-ended)
2. Print a single-line confirmation: `Comment updated`
3. Re-ask the confirmation question — do not re-display the full preview.

### Cancel

- Exit workflow immediately
- Display: "No action taken on PR #{{arg}}."
- Do not modify PR in any way

