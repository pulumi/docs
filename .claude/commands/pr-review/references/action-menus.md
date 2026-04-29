---
user-invocable: false
description: Action menu options for bot and non-bot PRs
---

# Action Menus

Select the appropriate section based on contributor type and review findings. Auto-merge is a toggle on the Step 8 preview, not a Step 7 menu choice.

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

Tone adjusts based on `etiquette_trust` (low → warm/welcoming; standard → friendly; high → professional/terse). For merge-toggle defaults, see `pr-review:references:action-preview-templates`.
