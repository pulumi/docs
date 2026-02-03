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

---

### Step 1: Verify PR and Detect Contributor Type

Fetch all PR data and detect contributor type (bot/internal/external).

See [contributor-detection.md](references/contributor-detection.md) for complete detection script and display formatting.

**Key actions**:
- Fetch PR data once using gh CLI
- Detect contributor type: bot (username contains "[bot]" or matches bot patterns), internal (Pulumi org member), or external (community contributor)
- Display: "[icon] Reviewing PR #{{arg}} from @username ([type] contributor)"
- Cache PR_DATA for reuse in later steps

Continue to Step 2.

### Step 2: Gather PR Diff

1. View the full PR context: `gh pr view {{arg}}`
2. Get the diff: `gh pr diff {{arg}}`
3. Note the PR title, description, files changed, additions/deletions, and labels

Continue to Step 3.

### Step 3: Present Test Deployment and Review Guidance

**CRITICAL**: This step must be completed and presented to the user IMMEDIATELY after Step 2 and BEFORE starting Step 4. Do not delay this output.

See [test-deployment-guidance.md](references/test-deployment-guidance.md) for complete implementation.

**Key actions**:

- Fetch test deployment URL from pulumi-bot comment
- Analyze diff to generate specific, targeted review guidance (not generic checklists)
- Construct direct URLs for each changed page
- Display review guidance immediately (allows user to review deployment while AI performs comprehensive review in Step 5)
- Handle edge cases (>10 files, mechanical changes, infrastructure files, blog posts, mixed types)

Continue to Step 4.

### Step 4: Offer Infrastructure Deployment

Check if PR contains dependency or infrastructure changes.

See [infrastructure-deployment.md](references/infrastructure-deployment.md) for patterns and workflow.

**Decision point**:

- If NO dependency/infrastructure patterns match → Skip to Step 5
- If ANY pattern matches → Prompt user to deploy to pulumi-test.io

**Patterns that trigger prompt**:

- Dependency files (package.json, go.mod, requirements.txt, etc.)
- Infrastructure directory or workflow files
- Author is dependabot or renovate

If user chooses "Yes": Trigger testing-build-and-deploy.yml workflow and display monitoring instructions.

Continue to Step 5.

### Step 5: Perform Comprehensive Review

**PREREQUISITE**: Step 4 must be completed before starting this step.

1. Read review criteria: Use Read tool to load `.claude/commands/_common/review-criteria.md`
2. Review all files in the diff against criteria
3. Check: STYLE-GUIDE.md compliance, spelling/grammar, links, code examples, file moves with aliases, infrastructure changes, images, frontmatter, cross-references, SEO
4. Apply role-specific guidelines (documentation vs blog/marketing)
5. For blog posts announcing features: Check if corresponding documentation exists

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

**If contributor type is bot**, use bot-specific menus. Otherwise, use standard action menu adapted to review findings.

See [bot-action-menus.md](references/bot-action-menus.md) for complete menu structures.

**Bot PRs**:

- **Dependabot**: Parse labels, determine risk tier, show appropriate 4-option menu with testing checklist
  - See [dependabot-labels.md](references/dependabot-labels.md) for label taxonomy and risk classification
- **Other bots**: Show 4-option menu with automation/merge label detection

**Non-bot PRs** (adaptive 3-scenario approach):

- **Scenario A: Issues found** → Request changes recommended (4 options)
- **Scenario B: Clean review** → Approve recommended (4 options)
- **Scenario C: Should close** → Close PR recommended (4 options)

Select appropriate menu based on review findings. Max 4 options per menu (AskUserQuestion limit).

Continue to Step 8 with selected action.

### Step 8: Preview Planned Actions and Get Confirmation

**CRITICAL**: Always show what will happen before executing.

See [action-preview-templates.md](references/action-preview-templates.md) for preview formats.

Display preview showing:

- Exact comment text that will be posted (using templates from [message-templates.md](references/message-templates.md))
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

**Make changes and approve** (8-step flow):

1. Save current branch
2. Check out PR: `gh pr checkout {{arg}}`
3. Make changes (Edit/Write tools)
4. Show diff: `git diff`
5. Ask: "Proceed with commit and approval?"
   - No → Ask for additional changes or cancel → Return to original branch
   - Yes → Continue
6. Commit with co-author: `git add . && git commit -m "Apply style and formatting fixes\n\nCo-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"`
7. Push: `git push`
8. Approve: `gh pr review {{arg}} --approve --body "{{COMMENT}}"`
9. Return to original branch

Continue to Step 10.

### Step 10: Report Execution Results

See [execution-results.md](references/execution-results.md) for result message templates.

Display appropriate success message with:

- Confirmation of action taken
- PR URL for easy access
- Additional context (bot info, risk tier, deployment warnings)
- Verification commands where helpful

**For Dependabot HIGH/MEDIUM**: Warn that next merge to master triggers pulumi-test.io deployment.

Workflow complete.

---

## Important Notes

### Message Templates

All review comments use templates from [message-templates.md](references/message-templates.md) based on contributor type:

- **External**: Warm, welcoming, with emojis
- **Internal**: Professional, efficient, brief
- **Bot**: Technical, factual, no emojis
- **Dependabot**: Risk-aware with testing details

### Dependabot Handling

Complete handling guidelines in [dependabot-labels.md](references/dependabot-labels.md):

- Risk classification from labels
- Testing checklists by tier
- Quarterly review workflow
- Message variations by risk

### Critical Workflow Rules

1. **Never skip steps** - All 10 steps are mandatory
2. **Step 3 timing** - Present test deployment guidance BEFORE starting comprehensive review (Step 5)
3. **Step 4 prerequisite** - Must complete before Step 5
4. **Always preview** - Show exactly what will happen before executing (Step 8)
5. **Use confirmed content** - Execute with user-approved text from Step 8 (Step 9)

### Error Handling

If any command fails:

- Display error message with context
- Provide recovery commands
- For "Make changes and approve": Return to original branch on error

### Branch Safety

For "Make changes and approve":

- Always save and restore original branch
- Show diff before committing
- Allow cancellation at any point
- Return to original branch even on errors
