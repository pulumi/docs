---
description: Review and approve/merge pull requests as a maintainer (full workflow with approve, request changes, merge, close actions)
---

# Pull Request Review Command

**Use this when:** You're reviewing someone's pull request as a maintainer and need to approve, request changes, merge, or close it.

Performs comprehensive review with style and accuracy checks, then provides an interactive workflow for approval actions. Automatically detects contributor type (internal/external/bot) and adapts communication tone (warm/welcoming for external, professional for internal, technical/professional for bots).

---

## Usage

`/pr-review <PR_NUMBER>`

Reviews any pull request and presents action choices for approval, changes, or closure.

**Required**: PR number

**Works with**: All PRs (internal, external, and bots)

**Special handling**: Automatically detects contributor type and adapts messaging (warm for external, professional for internal, technical for bots). Provides risk-based workflow for Dependabot PRs with testing checklists and label-driven recommendations.

---

## Process

**CRITICAL SUCCESS CRITERIA**: Complete all 10 steps in sequence. Every step is mandatory and serves a critical purpose in the review workflow. **DO NOT SKIP ANY STEP OR END THE WORKFLOW PREMATURELY!**

**Step Counter**: Display progress before each step as: **[Step X/10]** followed by the step heading. This helps users track progress through the workflow.

**References**: Always follow the detailed instructions in the referenced documents for each step. The references contain the complete implementation details required.

---

### Step 1: Verify PR and Detect Contributor Type

1. Run the contributor detection script:

   ```bash
   bash .claude/commands/pr-review/scripts/contributor-detection.sh {{arg}}
   ```

   The script outputs:

   - `AUTHOR` - GitHub username
   - `CONTRIBUTOR_TYPE` - bot/internal/external
   - `PR_METADATA` - JSON with number, title, url
   - `FILES_CHANGED` - List of changed file paths
   - `PR_DATA_JSON` - Complete PR data for caching

   After running the script, store the following for later steps:

    - PR data (in PR_DATA variable for use in later steps)
    - Contributor type (bot/internal/external)
    - File paths (displayed for Step 4 reference)

2. **Critical!** Display this output to the user immediately:

   ```markdown
   ## 👤 Contributor Detection

   [icon] Reviewing PR #{{arg}} from @username ([type] contributor)
   ```

   Icons:

   - 🤖 for bot account
   - 📝 for internal contributors
   - 🌍 for external contributors

Continue to Step 2.

### Step 2: Gather PR Diff

1. View the full PR context: `gh pr view {{arg}}`
2. Get the diff: `gh pr diff {{arg}}`
3. Note the PR title, description, files changed, additions/deletions, and labels

Continue to Step 3.

### Step 3: Present Test Deployment and Review Guidance

**CRITICAL**: This step must be completed and presented to the user IMMEDIATELY after Step 2 and BEFORE starting Step 4. Do not delay this output.

1. Run the test deployment guidance script:

   ```bash
   bash .claude/commands/pr-review/scripts/test-deployment-guidance.sh {{arg}}
   ```

   The script outputs JSON with:

   - `deploymentUrl` - The test deployment URL or null
   - `deploymentStatus` - "ready" or "pending"
   - `pages[]` - Array of changed pages with titles, URLs, and change statistics
   - `nonContentFiles[]` - Array of non-content file paths

2. Parse the JSON output and analyze the PR diff context to understand what changed.

3. **Critical!** Present deployment review with context-aware guidance to the user immediately:

   - Show deployment URL (or pending message if not ready)
   - For each page: display direct link + specific review items based on:
     - Type of content (docs/blog/tutorials)
     - What changed (headings → check structure, codeBlocks → test examples, images → verify loading, links → test navigation)
     - Change magnitude (small typo vs major rewrite)
   - Adapt tone and specificity to change type
   - Generate concrete, actionable guidance based on actual diff content

   This allows users to review the deployment while you perform the comprehensive analysis in Step 5.

**Only after displaying output from this step**, continue to Step 4.

### Step 4: Offer Infrastructure Deployment

Check if PR contains dependency or infrastructure changes. See `pr-review:references:infrastructure-deployment` for patterns and workflow.

**Only after displaying output from this step**, continue to Step 5.

### Step 5: Perform Comprehensive Review

Review all files against STYLE-GUIDE.md compliance: spelling, grammar, links, code examples, file moves with aliases, images, frontmatter, and cross-references. Apply role-specific guidelines per content type. See `_common:review-criteria` for full criteria.

**Large diffs (>100 lines)**: Summarize findings by category rather than line-by-line.

Continue to Step 6.

### Step 6: Summarize Review Findings

Present review results in terminal-friendly format:

```markdown
## 📋 Review Summary

**Overall Assessment**: [Clean/Minor issues/Issues found/Critical issues]

### Findings

**[Category]**: [Brief summary]
- Line X: [Issue description]
- Line Y: [Issue description]

### Recommendations

[Specific recommendations based on findings]
```

Continue to Step 7.

### Step 7: Present Action Menu

Present action menu based on contributor type (bot vs non-bot) and review findings.

See `pr-review:references:bot-action-menus` for complete menu structures and logic.

Continue to Step 8 with selected action.

### Step 8: Preview Planned Actions and Get Confirmation

**CRITICAL**: Always show what will happen before executing.

See `pr-review:references:action-preview-templates` for preview formats.

Display preview showing:

- Exact comment text that will be posted (using templates from `pr-review:references:message-templates`)
- Commands that will be executed
- For "Make changes and approve": Show file-by-file changes

**Confirmation options** (use AskUserQuestion):

1. **Yes, proceed** - Execute as previewed
2. **Edit comment** - Modify comment text
3. **Change action** - Return to Step 7
4. **Cancel** - Exit without changes

Handle each response appropriately:

- Edit comment → Show updated preview → Confirm again
- Change action → Return to action menu (Step 7)
- Cancel → Exit with "No action taken"

Continue to Step 9 with confirmed action.

### Step 9: Execute Confirmed Action

Execute using confirmed/edited content from Step 8.

**Commands by action**:

- **Approve**: `gh pr review {{arg}} --approve --body "{{COMMENT}}"`
- **Approve and merge**: `gh pr review {{arg}} --approve --body "{{COMMENT}}"` then `gh pr merge {{arg}} --auto --squash`
- **Request changes**: `gh pr review {{arg}} --request-changes --body "{{COMMENT}}"`
- **Close PR**: `gh pr comment {{arg}} --body "{{COMMENT}}"` then `gh pr close {{arg}}`
- **Do nothing yet**: Exit with message

**Make changes and approve**: See `pr-review:references:action-preview-templates` for complete workflow.

Continue to Step 10.

### Step 10: Report Execution Results

See `pr-review:references:execution-results` for result message templates.

Display appropriate success message with:

- Confirmation of action taken
- PR URL for easy access
- Additional context (bot info, risk tier, deployment warnings)
- Verification commands where helpful

**For Dependabot HIGH/MEDIUM**: Warn that next merge to master triggers pulumi-test.io deployment.

Workflow complete.

---

## Critical Workflow Rules

1. **Complete all 10 steps in sequence** - Never skip steps or end workflow prematurely
2. **Step 3 timing** - Present test deployment guidance BEFORE starting comprehensive review (Step 5)
3. **Step 4 prerequisite** - Must complete infrastructure deployment check before Step 5
4. **Always preview before execution** - Show exactly what will happen (Step 8) before executing (Step 9)
5. **Use confirmed content** - Execute only with user-approved text from Step 8
6. **Track progress** - Display **[Step X/10]** before each step heading
7. **Preserve branch safety** - For "Make changes and approve": save current branch, return to it even on errors

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
