---
user-invocable: false
description: Action menu options for bot and non-bot PRs
---

# Action Menus

**Decision Point**: Select the appropriate section based on contributor type and review findings.

**Key principle**: The Step 7 menu chooses *what action to take*. Whether the action is followed by an auto-merge is a **toggle on the Step 8 preview screen**, not a separate menu choice. See `pr-review:references:action-preview-templates` for the merge-toggle logic and defaults.

## Dependabot PRs

Parse labels from PR data: `deps-risk-*`, `deps-security-patch`, `deps-lambda-edge-risk`, `deps-bulk-update`, `deps-merge-after-test`, `deps-quarterly-review`

### Display Header

Use AskUserQuestion with header:

```text
🤖 Dependabot PR | Risk: [HIGH/MEDIUM/LOW/UNKNOWN]
[If security] 🔒 Security Update
[If lambda-edge] 🚨 Lambda@Edge Risk - Review deployment
[If bulk] 📦 Bulk Update (10+ deps)
```

### Options (Max 4 - Adjust Based on Risk Tier)

#### For HIGH Risk or Security Patches

1. **Approve** (Recommended after testing) — merge toggle defaults ON when CI green and tests passed
2. **Request changes** - Technical feedback needed
3. **Close PR** - Reject the dep update
4. **Do nothing yet** - Need to test/investigate

#### For LOW/MEDIUM Risk with quarterly-review Label

1. **Approve** (Recommended) — merge toggle starts OFF for quarterly batch (deferred)
2. **Close with quarterly note** - Defer to next quarterly batch
3. **Request changes** - Technical feedback needed
4. **Do nothing yet** - Need to test/investigate

#### For Other Dependabot PRs (No Clear Risk Label)

1. **Approve** (Recommended) — merge toggle defaults ON for clean low-risk dep updates
2. **Request changes** - Technical feedback needed
3. **Close PR** - Reject
4. **Do nothing yet** - Need investigation

### Testing Checklist (Show by Risk)

Display appropriate checklist based on risk tier:

- **HIGH**: `make serve-all`, search, console errors, markdown, PR deployment (URL loads, Lambda@Edge errors via F12, search, navigation)
- **MEDIUM**: `make build`, warnings, [if build tools] PR deployment URL loads
- **LOW**: `make lint`

## Other Bot PRs

For non-Dependabot bots (pulumi-bot, renovate, etc.)

### Display Header

```text
🤖 Bot: @username
[If automation/merge] ✓ automation/merge label
```

### Options (Max 4)

1. **Approve** (Recommended) — merge toggle defaults ON for bots
2. **Request changes** - Issues need addressing
3. **Close PR** - Reject
4. **Do nothing yet** - Need investigation

### Important Notes

- "Make changes and approve" excluded for bots (editing breaks automation; bot PRs regenerated, not manually edited)

## Standard Action Menu (Non-Bot Contributors)

**IMPORTANT**: AskUserQuestion only supports max 4 options. Use adaptive menus based on review findings.

### Adaptive Menu Selection

Choose the appropriate menu based on review findings:

- **Scenario A**: Issues found, contradictions have suggested fixes → Make changes menu
- **Scenario B**: Issues found, contradictions need author input → Request changes menu
- **Scenario C**: Clean review → Approve menu
- **Scenario D**: Should close → Close menu

### Scenario A: Issues with Suggested Fixes — Make Changes Recommended

Use this when Step 5 surfaced contradictions and **every** contradiction has a high-confidence `suggested_fix`. Applying the fixes yourself is faster than round-tripping with the author.

**Options**:
1. **Make changes and approve** (Recommended) — apply trivial fixes + suggested fixes, then approve
2. **Request changes** - Send feedback to author instead
3. **Approve as-is** - Approve despite issues (non-blocking)
4. **Do nothing yet** - Need more time/discussion

### Scenario B: Issues Without Reliable Fixes — Request Changes Recommended

Use this when contradictions are unverifiable, lack suggested fixes, or are stylistic-judgment calls. The author-question buffer auto-populates the comment body with line-anchored questions per claim.

**Options**:
1. **Request changes** (Recommended) — author-question buffer pre-fills the comment
2. **Make changes and approve** - Fix issues yourself + approve
3. **Approve as-is** - Approve despite issues (non-blocking feedback)
4. **Do nothing yet** - Need more time/discussion

### Scenario C: Clean Review — Approve Recommended

**Options**:
1. **Approve** (Recommended) — merge toggle defaults OFF (Pulumi convention: authors merge their own PRs)
2. **Make changes and approve** - Minor edits (typos, formatting) + approve
3. **Request changes** - Hold for author input
4. **Do nothing yet** - Need more time/discussion

### Scenario D: Should Close — Close PR Recommended

**Options**:
1. **Close PR** (Recommended) - Close with explanation
2. **Request changes** - Give author chance to address issues
3. **Approve** - Override concerns and approve anyway
4. **Do nothing yet** - Need discussion before closing

## Merge Toggle Defaults (Step 8)

Whether the action is followed by an auto-merge is decided by the **`Auto-merge after approval` toggle** on the Step 8 preview screen, not by which Step 7 option is picked. This eliminates manual "approve and merge" typing without breaking the Pulumi convention that authors merge their own PRs.

### Default ON

Toggle defaults ON only when **all** of:

- Contributor is a **bot** (dependabot, pulumi-bot, renovate, copilot, github-actions)
- CI is green
- No remaining contradictions or unverifiable claims
- `AI_SUSPECT=false`

### Default OFF

Toggle defaults OFF for **all human-authored PRs**, regardless of seniority, contributor type, or CI status. **Reason:** Pulumi has a strong culture of authors merging their own PRs. As a reviewer, the default action is approve-and-let-the-author-merge; auto-merging on someone's behalf is the exception, not the norm.

The toggle exists so the user can flip it on for the rare case where they actually want to merge on the author's behalf — typically:

- External first-timer who doesn't have merge rights
- Stale PR the author has abandoned
- Time-sensitive fix where the author is out

### AI-Suspect Override

When `AI_SUSPECT=true`, the toggle defaults OFF unconditionally — even for bot PRs. This forces a conscious keystroke before merging anything that may contain AI-generated content.

## Implementation Notes

- Always use AskUserQuestion tool with max 4 options
- Select the adaptive menu based on review findings (A/B/C/D for non-bot)
- Display risk indicators and labels for Dependabot PRs
- Show testing checklists for dependency PRs
- Tone adjusts based on `etiquette_trust` (low → warm/welcoming; standard → friendly; high → professional/terse)
- "Make changes and approve" preserves contributor credit for minor fixes
- Bot PRs exclude "Make changes and approve" (breaks automation)
- The merge-toggle is decided in Step 8, not Step 7 — never add an "Approve and merge" option to a Step 7 menu
