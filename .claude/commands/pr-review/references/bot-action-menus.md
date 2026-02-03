---
user-invocable: false
description: Action menu options for bot and non-bot PRs
---

# Bot Action Menus

**Decision Point**: If contributor type is bot, use bot-specific action menu. Otherwise, use standard action menu.

## Dependabot PRs

Parse labels from PR data: `deps-risk-*`, `deps-security-patch`, `deps-lambda-edge-risk`, `deps-bulk-update`, `deps-merge-after-test`, `deps-quarterly-review`

### Display Header

Use AskUserQuestion with header:

```
🤖 Dependabot PR | Risk: [HIGH/MEDIUM/LOW/UNKNOWN]
[If security] 🔒 Security Update
[If lambda-edge] 🚨 Lambda@Edge Risk - Review deployment
[If bulk] 📦 Bulk Update (10+ deps)
```

### Options (Max 4 - Adjust Based on Risk Tier)

#### For HIGH Risk or Security Patches

1. **Approve and merge** (Recommended after testing) - Approve + merge (squash) when testing complete
2. **Approve** - Approve only, manual merge later
3. **Request changes** - Technical feedback needed
4. **Do nothing yet** - Need to test/investigate

#### For LOW/MEDIUM Risk with quarterly-review Label

1. **Approve** (Recommended) - Approve for quarterly batch
2. **Approve and merge** - Merge now if urgent
3. **Close with quarterly note** - Defer to next quarterly batch
4. **Do nothing yet** - Need to test/investigate

#### For Other Dependabot PRs (No Clear Risk Label)

1. **Approve and merge** - Ready for immediate merge
2. **Approve** - Approve for later merge
3. **Request changes** - Technical feedback needed
4. **Do nothing yet** - Need investigation

### Testing Checklist (Show by Risk)

Display appropriate checklist based on risk tier:

- **HIGH**: `make serve-all`, search, console errors, markdown, PR deployment (URL loads, Lambda@Edge errors via F12, search, navigation)
- **MEDIUM**: `make build`, warnings, [if build tools] PR deployment URL loads
- **LOW**: `make lint`

## Other Bot PRs

For non-Dependabot bots (pulumi-bot, renovate, etc.)

### Display Header

```
🤖 Bot: @username
[If automation/merge] ✓ automation/merge label
```

### Options (Max 4)

1. **Approve and merge** (Recommended if automation/merge label) - Ready for immediate merge
2. **Approve** - Changes acceptable, manual merge later
3. **Request changes** - Issues need addressing
4. **Do nothing yet** - Need investigation

### Important Notes

- If "Close PR" is needed, user can select "Do nothing yet" and close manually via web UI or by re-running with updated guidance
- "Make changes and approve" excluded for bots (editing breaks automation; bot PRs regenerated, not manually edited)

## Standard Action Menu (Non-Bot Contributors)

**IMPORTANT**: AskUserQuestion only supports max 4 options. Use adaptive menus based on review findings.

### Adaptive Menu Selection

Choose the appropriate menu based on review findings:

- **Scenario A**: Issues found (blockers or changes needed) → Request changes menu
- **Scenario B**: Clean review or minor suggestions → Approve menu
- **Scenario C**: PR should be closed (duplicate, obsolete, wrong direction) → Close menu

### Scenario A: Issues Found - Request Changes Recommended

Use when there are technical issues, style violations, or changes needed before merge.

**Options**:

1. **Request changes** (Recommended) - Author should address issues
2. **Make changes and approve** - Fix issues yourself + approve (preserves contributor credit)
3. **Approve** - Approve despite issues (non-blocking feedback)
4. **Do nothing yet** - Need more time/discussion

**Tone**: Warm/welcoming for external, professional for internal

### Scenario B: Clean Review - Approve Recommended

Use when PR is ready to merge or has only minor non-blocking suggestions.

**Options**:

1. **Approve** (Recommended) - Approve PR with feedback
2. **Approve and merge** - Approve + merge (squash) for immediate merge
3. **Make changes and approve** - Minor edits (typos, formatting) + approve
4. **Do nothing yet** - Need more time/discussion

**Tone**: Warm/welcoming for external, professional for internal

### Scenario C: Should Close - Close PR Recommended

Use when PR doesn't fit, is duplicate, obsolete, or going in wrong direction.

**Options**:

1. **Close PR** (Recommended) - Close with explanation
2. **Request changes** - Give author chance to address fundamental issues
3. **Approve** - Override concerns and approve anyway
4. **Do nothing yet** - Need discussion before closing

**Tone**: Respectful and explanatory, especially for external contributors

## Implementation Notes

- Always use AskUserQuestion tool with max 4 options
- Select appropriate menu based on context (review findings, contributor type, PR state)
- Display risk indicators and labels for Dependabot PRs
- Show testing checklists for dependency PRs
- Tone adjusts based on contributor type (external vs internal)
- "Make changes and approve" preserves contributor credit for minor fixes
- Bot PRs exclude "Make changes and approve" (breaks automation)
