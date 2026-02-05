---
user-invocable: false
description: Infrastructure deployment detection and workflow triggers
---

# Infrastructure Deployment

Check if the PR contains dependency or infrastructure changes by examining the files changed.

**CRITICAL OUTPUT**: Always use the message templates below to display deployment status to the user.

## Dependency Changes - Patterns

Any of these patterns indicate dependency changes:

- PR author contains `dependabot` or `renovate`
- Files changed include: `package.json`, `yarn.lock`, `package-lock.json`
- Files changed include: `go.mod`, `go.sum`
- Files changed include: `requirements.txt`, `Pipefile`, `Pipefile.lock`, `poetry.lock`
- Files changed include: `Gemfile`, `Gemfile.lock`

## Infrastructure Changes - Patterns

Any of these patterns indicate infrastructure changes:

- Files changed include anything in `infrastructure/` directory
- Files changed include: `.github/workflows/*.yml` or `.github/workflows/*.yaml`
- Files changed include: `netlify.toml`, `vercel.json`, or deployment configuration files

## Decision Logic

- ❌ **If NONE of the patterns above match** → Skip to next step
- ✅ **If ANY pattern matches** → **STOP HERE** and present the infrastructure deployment prompt

## Prompt User (When Patterns Match)

Use AskUserQuestion with:

**Question**: "This PR contains dependency/infrastructure changes. Deploy to pulumi-test.io for testing?"

**Options**: Yes, deploy now | No, skip

### If User Chooses "Yes"

1. Get PR branch name:

   ```bash
   gh pr view {{arg}} --json headRefName --jq '.headRefName'
   ```

2. Trigger workflow:

   ```bash
   gh workflow run testing-build-and-deploy.yml --ref <branch-name>
   ```

3. Wait 2-3s, fetch URL:

   ```bash
   gh run list --workflow=testing-build-and-deploy.yml --limit 1 --json databaseId,status,url,headBranch --jq '.[0]'
   ```

4. Display deployment monitoring instructions with this template and continue:

   ```markdown
   ## 🔧 Infrastructure Deployment Initiated

   Deployment started for PR #{{arg}} to pulumi-test.io

   📊 Monitor: [Workflow URL] | 🌐 Test site (~10 min): https://pulumi-test.io

   Instructions: Monitor workflow → Wait ~10 min → Visit pulumi-test.io → Check console (F12) → Test search → Verify no Lambda@Edge errors

   ⚠️ Next merge to master resets pulumi-test.io.

   PR Deployment [if available]: [URL]
   ```

### If User Chooses "No"

Display this message and continue:

```markdown
## 🔧 Infrastructure Testing Skipped

PR Deployment [if available]: [URL]
```
