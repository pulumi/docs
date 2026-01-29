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

Fetch all PR data and detect contributor type with minimal commands:

1. Get PR details, metadata, and detect contributor type in a single bash execution:

   ```bash
   # Fetch PR data once (excluding body to avoid control character parsing issues)
   PR_DATA=$(gh pr view {{arg}} --json number,title,author,url,files,additions,deletions,labels,headRefName)

   # Extract author
   AUTHOR=$(echo "$PR_DATA" | jq -r '.author.login')

   # Detect contributor type
   if [[ "$AUTHOR" == *"[bot]"* ]] || [[ "$AUTHOR" == "pulumi-bot" ]] || [[ "$AUTHOR" == app/* ]]; then
     CONTRIBUTOR_TYPE="bot"
   else
     if gh api orgs/pulumi/members/$AUTHOR --silent 2>/dev/null; then
       CONTRIBUTOR_TYPE="internal"
     else
       CONTRIBUTOR_TYPE="external"
     fi
   fi

   echo "Author: $AUTHOR"
   echo "Contributor type: $CONTRIBUTOR_TYPE"
   echo "$PR_DATA" | jq -r '{number, title, url}'

   # Display file paths for use in Step 4
   echo ""
   echo "Files changed:"
   echo "$PR_DATA" | jq -r '.files[].path'
   ```

2. Store the results: PR data (in PR_DATA variable), contributor type (bot/internal/external), file paths (displayed for Step 4 reference)

3. Display: "[icon] Reviewing PR #{{arg}} from @username ([type] contributor)" (🤖 for bot account, 📝 for internal/external)

### Step 2: Gather PR Diff

1. View the full PR context: `gh pr view {{arg}}`
2. Get the diff: `gh pr diff {{arg}}`
3. Note the PR title, description (from PR view), files changed, additions/deletions (from Step 1), and labels (if bot, from Step 1)

### Step 3: Present Test Deployment and Review Guidance

**CRITICAL**: This step must be completed and presented to the user IMMEDIATELY after Step 2 and BEFORE starting Step 4. Do not delay this output.

#### Part A: Fetch Test Deployment URL

1. Get most recent pulumi-bot comment: `gh api repos/pulumi/docs/issues/{{arg}}/comments --jq '.[] | select(.user.login == "pulumi-bot") | {created_at, body}' | tail -1`
2. Extract deployment URL: `http://www-testing-pulumi-docs-origin-pr-{PR}-{HASH}.s3-website.us-west-2.amazonaws.com`
3. **No comment/URL**: Display "⏳ Deployment not ready. Typically appears in minutes. Review code now, check deployment later."

#### Part B: Analyze Changes and Generate Targeted Review Guidance

**IMPORTANT**: Base guidance on **actual diff substance**, not generic rules.

1. **Analyze the diff from Step 2** to identify: Content (headings `+ ##`, code blocks `+ `````, images`+ ![`, links`+ [`), Config (frontmatter, YAML), Assets (tables, callouts), Structure (moved sections), Terminology (replacements)

2. **Generate specific guidance**:
   - ✅ "Verify new TypeScript example on Components page runs"
   - ✅ "Check reorganized sections flow logically"
   - ❌ Avoid generic: "Check formatting, links, code rendering"

3. **Construct direct URLs**: Remove `content/` prefix, remove `.md`/`_index.md` suffix, add trailing `/`, prepend base URL. Example: `content/docs/iac/concepts/components/_index.md` → `[base]/docs/iac/concepts/components/`. **CRITICAL**: Each page needs direct link, not just base URL.

#### Part C: Display the Review Guidance

1. **Group guidance by page/file** with 2-4 specific items per page based on what changed

**TIMING**: Display this output IMMEDIATELY after Step 2 completes, BEFORE starting the comprehensive AI review in Step 4. This allows users to review the deployment while the AI performs its analysis.

**Format** (adapt based on whether deployment URL is available):

**If deployment URL is available:**

```markdown
## 🔍 Test Deployment Review

**Deployment URL**: [base-url]

### Review the Following Changes

**[Page/File Name]** - [Direct link to this specific page]
- [ ] [Specific change-based item from diff analysis]
- [ ] [Specific change-based item from diff analysis]
- [ ] [Specific change-based item from diff analysis]

**[Another Page/File Name]** - [Direct link to this specific page]
- [ ] [Specific change-based item from diff analysis]
- [ ] [Specific change-based item from diff analysis]

[... continue for all pages with substantive changes ...]

---

*Please review these specific changes in the deployment before proceeding.*
```

**If deployment URL is NOT available:**

```markdown
## 🔍 Test Deployment Review

⏳ Test deployment is not ready yet (no pulumi-bot comment found)

The deployment typically appears within a few minutes after pushing commits.
You can proceed with the code review now and check the deployment later.

### When the deployment is ready, review:

**[Page/File Name]**
- [ ] [Specific change-based item from diff analysis]
- [ ] [Specific change-based item from diff analysis]

**[Another Page/File Name]**
- [ ] [Specific change-based item from diff analysis]
- [ ] [Specific change-based item from diff analysis]

[... continue for all pages with substantive changes ...]

---

*The deployment URL will be available at: http://www-testing-pulumi-docs-origin-pr-{{arg}}-[commit-hash].s3-website.us-west-2.amazonaws.com*
```

#### Part D: Handle Edge Cases

- **>10 files** - Prioritize `.md` under `content/`, show "... and N more"
- **Mechanical changes** - Typos/whitespace only → "Mechanical fixes. Suggest quick scan."
- **Infrastructure/non-visual** - `.yaml`/`.json`/scripts → Explain behavior verification
- **Blog posts** - Focus: readability, images, code (not cross-refs)
- **Mixed types** - Group by: docs/blog/examples/infrastructure

Continue to Step 4.

### Step 4: Offer Infrastructure Deployment

Check if the PR contains dependency or infrastructure changes by examining the files changed (displayed in Step 1):

**Dependency changes** - Any of these patterns:

- PR author contains `dependabot` or `renovate`
- Files changed include: `package.json`, `yarn.lock`, `package-lock.json`
- Files changed include: `go.mod`, `go.sum`
- Files changed include: `requirements.txt`, `Pipefile`, `Pipefile.lock`, `poetry.lock`
- Files changed include: `Gemfile`, `Gemfile.lock`

**Infrastructure changes** - Any of these patterns:

- Files changed include anything in `infrastructure/` directory
- Files changed include: `.github/workflows/*.yml` or `.github/workflows/*.yaml`
- Files changed include: `netlify.toml`, `vercel.json`, or deployment configuration files

**Decision Point**:

- ❌ **If NONE of the patterns above match** → Skip to Step 5
- ✅ **If ANY pattern matches** → **STOP HERE** and present the infrastructure deployment prompt below

**WHEN PATTERNS MATCH, USE AskUserQuestion WITH:**

**Question**: "This PR contains dependency/infrastructure changes. Deploy to pulumi-test.io for testing?"

**Options**: Yes, deploy now | No, skip

**If Yes**:

1. Get PR branch name: `gh pr view {{arg}} --json headRefName --jq '.headRefName'`
2. Trigger workflow: `gh workflow run testing-build-and-deploy.yml --ref <branch-name>`
3. Wait 2-3s, fetch URL: `gh run list --workflow=testing-build-and-deploy.yml --limit 1 --json databaseId,status,url,headBranch --jq '.[0]'`

Display:

```markdown
## 🔧 Infrastructure Deployment Initiated

Deployment started for PR #{{arg}} to pulumi-test.io

📊 Monitor: [Workflow URL] | 🌐 Test site (~10 min): https://pulumi-test.io

Instructions: Monitor workflow → Wait ~10 min → Visit pulumi-test.io → Check console (F12) → Test search/algolia → Verify no Lambda@Edge errors

⚠️ Next merge to master resets pulumi-test.io. This is temporary.

PR Deployment [if available]: [URL from Part A]
```

**If No**: Display `## 🔧 Infrastructure Testing Skipped\n\nPR Deployment [if available]: [URL from Part A]`

**After completing Step 4 (or confirming no infrastructure/dependency changes)**, continue to Step 5.

### Step 5: Perform Comprehensive Review

**PREREQUISITE**: Step 4 must be completed before starting this step. If you haven't checked Step 4 yet, go back and evaluate whether infrastructure deployment is needed.

1. Read the review criteria: Use the Read tool to read `.claude/commands/docs-review.md` and locate the **Review Criteria** section.

2. Review the PR changes using those criteria, which include:
   - Style guide enforcement (STYLE-GUIDE.md compliance)
   - Spelling/grammar
   - Link validation
   - Code examples
   - File standards (frontmatter, structure)
   - SEO considerations
   - Special cases (file moves, redirects, infrastructure changes)
   - Role-specific guidelines for documentation vs blog/marketing content

### Step 6: Present Review Findings

Present the review in the conversation:

1. Start with a summary of what was reviewed (files, scope)
2. List findings by category (critical issues, style improvements, suggestions)
3. Include specific line numbers for each issue
4. Use suggestion code blocks for recommended changes
5. Highlight positive aspects of the contribution
6. Keep feedback constructive and encouraging
7. Display a change summary for context:

   **Changes:** [X] file(s) changed (+[additions]/-[deletions] lines)

   Extract counts from the PR data fetched in Step 1:
   - Files count: Length of `files` array
   - Additions: `additions` field
   - Deletions: `deletions` field

   Use singular "file" when count is 1, plural "files" otherwise.

   **Example outputs**:
   - "**Changes:** 1 file changed (+3/-1 lines)" - Small, focused change
   - "**Changes:** 15 files changed (+543/-234 lines)" - Substantial change

   This summary helps users understand scope when choosing an action in Step 7.

**After presenting the review findings above, immediately continue to Step 7.** Do not stop here - the workflow is incomplete without presenting action choices.

---

### Step 7: Present Action Choices

**If contributor type is bot**, use bot-specific action menu. Otherwise, use standard action menu.

#### Bot-Specific Action Menu

**Dependabot PRs**: Parse labels (`deps-risk-*`, `deps-security-patch`, `deps-lambda-edge-risk`, `deps-bulk-update`, `deps-merge-after-test`, `deps-quarterly-review`)

Use AskUserQuestion with header:

```output
🤖 Dependabot PR | Risk: [HIGH/MEDIUM/LOW/UNKNOWN]
[If security] 🔒 Security Update
[If lambda-edge] 🚨 Lambda@Edge Risk - Review deployment
[If bulk] 📦 Bulk Update (10+ deps)
```

**Options** (max 4 - adjust based on risk tier):

**For HIGH risk or security patches:**

1. **Approve and merge** (Recommended after testing) - Approve + merge (squash) when testing complete
2. **Approve** - Approve only, manual merge later
3. **Request changes** - Technical feedback needed
4. **Do nothing yet** - Need to test/investigate

**For LOW/MEDIUM risk with quarterly-review label:**

1. **Approve** (Recommended) - Approve for quarterly batch
2. **Approve and merge** - Merge now if urgent
3. **Close with quarterly note** - Defer to next quarterly batch
4. **Do nothing yet** - Need to test/investigate

**For other Dependabot PRs (no clear risk label):**

1. **Approve and merge** - Ready for immediate merge
2. **Approve** - Approve for later merge
3. **Request changes** - Technical feedback needed
4. **Do nothing yet** - Need investigation

**Testing Checklist** (show by risk):

- **HIGH**: `make serve-all`, search, console errors, markdown, PR deployment (URL loads, Lambda@Edge errors via F12, search, navigation)
- **MEDIUM**: `make build`, warnings, [if build tools] PR deployment URL loads
- **LOW**: `make lint`

**Other Bot PRs**: Use AskUserQuestion with header (max 4 options):

```output
🤖 Bot: @username
[If automation/merge] ✓ automation/merge label
```

**Options**:

1. **Approve and merge** (Recommended if automation/merge label) - Ready for immediate merge
2. **Approve** - Changes acceptable, manual merge later
3. **Request changes** - Issues need addressing
4. **Do nothing yet** - Need investigation

**Note**: If "Close PR" is needed, user can select "Do nothing yet" and close manually via web UI or by re-running with updated guidance.

**Note**: "Make changes and approve" excluded for bots (editing breaks automation; bot PRs regenerated, not manually edited).

#### Standard Action Menu (Non-Bot)

Use AskUserQuestion with 6 options (tone: warm/welcoming for external, professional for internal):

| Option | Action | When to Use |
|--------|--------|-------------|
| 1. **Approve** (Recommended) | Approve PR with feedback | PR ready to merge |
| 2. **Approve and merge** | Approve + merge (squash) | Ready for immediate merge |
| 3. **Make changes and approve** | Minor edits + approve | Small fixes (typos, formatting) preserving contributor credit |
| 4. **Request changes** | Review feedback with request-changes flag | Author should address issues |
| 5. **Close PR** | Close with explanation | Doesn't fit or no longer needed |
| 6. **Do nothing yet** | Exit without action | Need more time/discussion |

### Step 8: Preview Planned Actions and Get Confirmation

**CRITICAL**: Always show what will happen before executing. Preview format:

| Action | Preview | Commands |
|--------|---------|----------|
| **Approve** | Comment: [Template from Message Templates] | `gh pr review {{arg}} --approve --body "{{COMMENT}}"` |
| **Approve and merge** | Comment: [Template from Message Templates] | `gh pr review {{arg}} --approve --body "{{COMMENT}}"`<br>`gh pr merge {{arg}} --auto --squash` |
| **Request changes** | Comment: [Template from Message Templates]<br>Include issues with line numbers + suggestion blocks | `gh pr review {{arg}} --request-changes --body "{{COMMENT}}"` |
| **Close PR** | Comment: [Template from Message Templates]<br>Include clear closing explanation | `gh pr comment {{arg}} --body "{{COMMENT}}"`<br>`gh pr close {{arg}}` |
| **Do nothing yet** | No changes will be made to PR #{{arg}}.<br>Run /pr-review {{arg}} again when ready. | - |

**Make changes and approve** (not available for bots):

1. Ask user: "What changes should I make to the PR?"
2. Display preview:

   ```
   ## Preview: Changes and Approval

   I will:
   1. Save current branch
   2. Check out PR: gh pr checkout {{arg}}
   3. Make changes:
      - File: [path] - [description]
      - File: [path] - [description]
   4. Show diff before committing
   5. Commit: "Apply style and formatting fixes"
   6. Push changes
   7. Approve with comment: [Template from Message Templates]
   8. Return to original branch
   ```

**Confirmation** (use AskUserQuestion):

**Options**: Yes, proceed | Edit comment | Change action | Cancel

**Responses**:

- **Yes, proceed** → Continue to Step 8
- **Edit comment** → Ask for revised text → Show updated preview → Confirm again
- **Change action** → Return to Step 6
- **Cancel** → Exit with "No action taken on PR #{{arg}}."

#### Message Templates

Select template based on contributor type (Step 1). Bot templates: professional/technical, no emojis.

| Action | External | Internal | Bot |
|--------|----------|----------|-----|
| **Approve** | "Thank you! [≤1 sentence praise if warranted]. Welcome! 🎉" | "LGTM! [feedback/suggestions]" | **Dependabot**: "Security patch approved [testing notes]" (security), "High-risk update reviewed. Checklist: [items]" (high), "Update reviewed for quarterly batch" (med/low)<br>**Other**: "Automated changes approved." |
| **Approve and merge** | "Thank you! [≤1 sentence praise]. Auto-merge enabled. 🎉" | "LGTM! Auto-merge enabled." | **Dependabot**: "Security patch approved. Auto-merge enabled." (security), "High-risk update tested. Auto-merge enabled." (high), "Update approved. Auto-merge enabled." (med/low)<br>**Other**: "Automated changes approved. Auto-merge enabled." |
| **Make changes and approve** | "Applied minor style/formatting fixes. Thank you! 🙏" | "Applied style/formatting fixes. LGTM!" | N/A (excluded for bots) |
| **Request changes** | Opening: "Thank you!"<br>Acknowledge positives (≤1 sentence)<br>Issues with line numbers<br>Suggestion blocks<br>Close: "Mention @claude if you need help" | Professional opening<br>Issues with line numbers<br>Suggestion blocks<br>Clear action items | Technical issue description<br>Line numbers<br>What needs changing<br>No suggestion blocks<br>Close: "This automated PR may need closing and regeneration after fixing source configuration." |
| **Close PR** | "Thank you for contributing!"<br>Clear, kind closing reason<br>Acknowledge valuable aspects<br>Suggest alternatives<br>"We appreciate your interest in Pulumi!" | Clear closing reason | **Dependabot quarterly**: "Closing to batch with other low/medium-risk updates in quarterly review. See [Dependency Management](https://github.com/pulumi/docs/blob/master/BUILD-AND-DEPLOY.md#dependency-management)."<br>**Dependabot other**: "Closing this update. [Technical reason: conflicts, superseded, etc.]"<br>**Other bots**: "Closing. [Technical reason]" |

### Step 9: Execute Confirmed Action

**Use confirmed/edited content from Step 7**. All actions use templates from Message Templates section based on contributor type.

**Commands** (see Step 7 for detailed flow):

- **Approve**: `gh pr review {{arg}} --approve --body "{{COMMENT}}"`
- **Approve and merge**: `gh pr review {{arg}} --approve --body "{{COMMENT}}"` then `gh pr merge {{arg}} --auto --squash` (Note: `--auto` enables auto-merge; PR merges when checks pass)
- **Request changes**: `gh pr review {{arg}} --request-changes --body "{{COMMENT}}"`
- **Close PR**: `gh pr comment {{arg}} --body "{{COMMENT}}"` then `gh pr close {{arg}}`
- **Do nothing yet**: Exit with "No action taken. Run this command again when ready."

**Make changes and approve** (detailed steps):

1. Save branch: `git rev-parse --abbrev-ref HEAD`
2. Check out: `gh pr checkout {{arg}}`
3. Make changes from Step 7 (Edit/Write tools)
4. Show diff: `git diff`
5. Ask: "Proceed with commit and approval? (Yes/No)"
   - No → Ask: "Additional changes or cancel?" → Repeat from step 3 or return to original branch
   - Yes → Continue
6. Commit: `git add . && git commit -m "Apply style and formatting fixes\n\nCo-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"`
7. Push: `git push`
8. Approve: `gh pr review {{arg}} --approve --body "{{COMMENT}}"`
9. Return: `git checkout <original-branch>`

### Step 10: Report Execution Results

| Action | Result Message | Additional Info |
|--------|---------------|-----------------|
| **Approve** | ✅ PR #{{arg}} approved successfully!<br><br>Approval comment posted. | PR URL |
| **Approve and merge** | ✅ PR #{{arg}} approved with auto-merge enabled!<br><br>PR will merge using squash when checks pass. Verify with: `gh pr view {{arg}} --json state,mergedAt,autoMergeRequest` | PR URL<br>Bot context (if bot): @username, Risk tier, Labels<br>If Dependabot HIGH/MEDIUM: "⚠️ Next merge to master triggers pulumi-test.io deployment" |
| **Make changes and approve** | ✅ Changes applied and PR #{{arg}} approved!<br><br>Changes committed: [SHA]<br>Files: [list] | PR URL/commits |
| **Request changes** | ✅ Changes requested on PR #{{arg}}<br><br>Review posted with request-changes flag. | PR URL |
| **Close PR** | ✅ PR #{{arg}} closed<br><br>Closing comment posted. | PR URL |
| **Do nothing yet** | No action taken on PR #{{arg}}.<br><br>Run /pr-review {{arg}} again when ready. | - |
| **Error** | ❌ Error executing action<br><br>Command: [failed command]<br>Error: [message]<br><br>No changes made to PR #{{arg}}. | Recovery:<br>• Run /pr-review {{arg}} again<br>• Check: `gh auth status`<br>• Verify: `gh pr view {{arg}} --json state,url`<br>• Use GitHub web UI<br><br>If checked out PR branch: `git checkout <original-branch>` before displaying error |

---

## Important Notes

- **Preview accuracy**: Previews show the planned action with exact comment text. The actual execution in Step 9 uses the confirmed (or edited) content from Step 8.
- **Preview-to-execution consistency**: What users see in the preview is exactly what gets posted to GitHub. Always use the confirmed comment text from Step 8 when executing in Step 9.
- **Edit flexibility**: The "Edit comment" option allows users to refine tone, add context, or adjust wording before posting. After editing, show the updated preview and confirm again.
- **Communication tone**: Use warm, welcoming language with external contributors. Keep praise brief and specific (1 sentence max).
- **Encouragement**: Make contributors feel welcomed to the Pulumi community
- **Credit**: Use "make changes" option judiciously - only for minor fixes that don't reduce contributor's credit for the work
- **Branch safety**: Always track current branch and return to it after PR checkout, especially if errors occur
- **Error handling**: See error recovery template in Step 10
- **Token efficiency**: Generate preview text once in Step 8 and reuse it in Step 9. For large diffs (>100 lines), show summary with option to expand full diff.
- **Large diffs**: When showing diffs in "Make changes and approve", if the diff exceeds 100 lines, show a summary (files changed, lines added/removed) and ask if user wants to see the full diff
- **Contributor type caching**: Store the contributor type (internal/external/bot) result from Step 1 and reuse it throughout Steps 7-10. Don't re-query the GitHub API if the user changes actions during preview.
- **Bot contributor handling**: Bot PRs receive technical, professional messaging without emojis. Dependabot PRs get risk-based workflow with testing checklists. Other bots get generic professional workflow.
- **Label-based recommendations**: For Dependabot PRs, action recommendations are based on auto-applied risk tier and action labels from label-dependabot.yml workflow. Always check labels before choosing an action.
- **Bot PR editing**: "Make changes and approve" option is excluded for bot PRs. Bot PRs should be closed and regenerated rather than manually edited to avoid breaking automation.
- **AskUserQuestion limit**: The tool accepts a maximum of 4 options. Bot-specific menus are adapted by risk tier to stay within this limit.
- **GitHub workflow refs**: When triggering workflows for PRs, always fetch the branch name first with `gh pr view --json headRefName` and use that as the ref. Do not use `refs/pull/{PR}/head` format as it is not accepted by the workflow dispatch API.
- **GitHub CLI fields**: When checking PR status, use `state`, `mergedAt`, and `autoMergeRequest` fields. Do not use `merged` field (does not exist).
