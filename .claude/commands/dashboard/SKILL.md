---
description: Display repository status with PRs, issues, CI/CD health, and suggested tasks
---

# Repository Dashboard

**Use this when:** You want a quick overview of repository status, priority work items, and health metrics.

Displays priority PRs/issues, suggested next tasks, CI/CD health, and deployment status with intelligent prioritization based on user context.

---

## Usage

`/dashboard [mode]`

**Modes:**

- (none): `compact` (default) - Top 5-8 most important items
- `detailed`: Top 10-15 items with more context
- `full`: Everything with complete details

---

## Implementation

### Step 1: Collect Data

Run the data collection script:

```bash
bash .claude/commands/dashboard/scripts/dashboard.sh
```

This outputs structured JSON with all repository data.

### Step 2: Parse and Present

Parse the JSON output and present it according to the mode requested. The JSON structure is:

```json
{
  "user": {
    "github_user": "string",
    "is_pulumi_member": boolean,
    "current_branch": "string",
    "uncommitted_changes": number,
    "rate_remaining": number
  },
  "prs": [
    {
      "number": number,
      "title": "string",
      "author": {"login": "string"},
      "isDraft": boolean,
      "createdAt": "timestamp",
      "labels": [{"name": "string"}],
      "priority": number,        // Calculated priority score
      "age_days": number,        // Days since creation
      "type": "security|high-risk|medium-risk|normal",
      "is_assigned": boolean,    // Assigned to current user
      "is_mentioned": boolean    // User mentioned in PR
    }
  ],
  "issues": [
    {
      "number": number,
      "title": "string",
      "age_days": number,
      "labels": [{"name": "string"}]
    }
  ],
  "workflows": {
    "status": "HEALTHY|WARNING|CRITICAL|UNKNOWN",
    "total_runs": number,
    "success_runs": number,
    "failure_runs": number,
    "success_rate": number,
    "recent": [
      {
        "name": "string",
        "status": "string",
        "conclusion": "string",
        "createdAt": "timestamp"
      }
    ]
  },
  "deployment": {
    "commit": "string",
    "timestamp": number  // Unix timestamp in seconds
  },
  "stats": {
    "total_prs": number,
    "assigned_prs": number,
    "total_issues": number,
    "assigned_issues": number
  }
}
```

### Step 3: Format Dashboard

Create a terminal-friendly dashboard with these sections:

#### Header Section

```
════════════════════════════════════════════════════════════════════════════════
📊 PULUMI DOCS DASHBOARD
════════════════════════════════════════════════════════════════════════════════

👤 User: @{github_user} ({internal|external}) | Branch: {branch} | Uncommitted: {count}
```

If `rate_remaining` < 10, show warning: `⚠️  GitHub API rate limit low ({count} remaining)`

#### Priority Items Section

**PRs:**

- Sort by `priority` (descending), then by `age_days` (descending)
- Show emojis based on type:
  - 🔒 = `type: "security"`
  - ⚠️  = `type: "high-risk"`
  - 📝 = normal (or draft if `isDraft: true`)
  - 🤖 = bot author (contains `[bot]` in username)
- Format: `{emoji} #{number}  {title} ({type if special}, {age}d)`
- Truncate titles to 60 characters

**Item limits by mode:**

- **compact**: Top 5 PRs
- **detailed**: Top 10 PRs
- **full**: Top 20 PRs (or all if less)

**Issues:**

- Show assigned issues after PRs
- Format: `🐛 #{number}  {title} (issue, {age}d)`
- Same limits as PRs (5/10/20)

#### Suggested Tasks Section

Generate actionable tasks based on data. Priority order:

1. **Security patches** (`type: "security"`):
   - `🔒 Review and merge security patch PR #{number} → /pr-review {number}`

2. **Uncommitted changes** (if `uncommitted_changes > 0`):
   - `📝 Review and commit {count} uncommitted changes → git status`

3. **Assigned PRs** (`is_assigned: true`):
   - `🔍 Review assigned PR #{number}: {short_title} → /pr-review {number}`
   - Limit to top 3 by priority

4. **High-risk PRs** (`type: "high-risk"`):
   - `⚠️  Review high-risk dependency PR #{number} → /pr-review {number}`
   - Limit to top 2

5. **Assigned issues**:
   - `🐛 Work on issue #{number}: {short_title} → gh issue view {number}`
   - Limit to top 2

6. **Workflow failures** (if `status: "CRITICAL"` and recent failures):
   - `❌ Investigate workflow failure: {name} → gh run list --workflow "{name}"`

7. **Current branch work** (if not on master/main):
   - `🔧 Continue work on branch {current_branch}`

**Task limits by mode:**

- **compact**: Top 3 tasks
- **detailed**: Top 5 tasks
- **full**: Top 10 tasks

Number tasks sequentially: `1.`, `2.`, etc.

#### Health Section

```
────────────────────────────────────────────────────────────────────────────────
🏥 HEALTH: {emoji} {status} (24h: {total_runs} runs, {success_rate}% success)
────────────────────────────────────────────────────────────────────────────────
```

Status emojis:

- ✅ = HEALTHY
- ⚠️  = WARNING
- ❌ = CRITICAL
- ❓ = UNKNOWN

**Recent workflows** (top 3):

- Calculate time ago from `createdAt` timestamp
- Format: `Recent: {emoji} {name} ({time}, {conclusion})`
- Join multiple with ` | `
- Emojis: ✅ success, ❌ failure, ⏳ in_progress, ⏸️  other

**Deployment info:**

- Calculate time ago from `deployment.timestamp`
- Format time as `Xm ago`, `Xh ago`, or `Xd ago`
- Line: `Deploy: {commit} ({time_ago}) | PRs: {total} open ({assigned} assigned) | Issues: {total} ({assigned} assigned)`

#### Footer

```
════════════════════════════════════════════════════════════════════════════════
Tip: Use '/dashboard detailed' or '/dashboard full' for more information
```

Adjust tip based on current mode.

---

## Priority Scoring Algorithm

PRs are scored with these weights (already calculated in JSON):

- **+100**: Assigned to me
- **+80**: Mentions me
- **+70**: Security patch (`deps-security-patch` label)
- **+60**: High-risk (`deps-risk-high` label)
- **+40**: Ready for review (not draft)
- **+30**: Team member (internal users only)
- **+50**: Age > 14 days
- **+25**: Age > 7 days
- **+20**: Medium-risk (`deps-risk-medium` label)
- **-20**: Draft

---

## Display Modes

### Compact (Default)

- **Purpose**: Quick status check
- **Items**: Top 5 PRs/issues, 3 tasks
- **Details**: Essential info only
- **Target**: Fits on one screen

### Detailed

- **Purpose**: Standard review workflow
- **Items**: Top 10 PRs/issues, 5 tasks
- **Details**: More context per item
- **Target**: 1-2 screens

### Full

- **Purpose**: Deep investigation
- **Items**: Top 20+ PRs/issues, 10 tasks
- **Details**: Complete visibility
- **Target**: Comprehensive view

---

## Error Handling

If the JSON indicates errors or missing data:

- Show what data is available
- Indicate which sections are unavailable
- Suggest checking GitHub API access or network connection
- Always show local git context (branch, uncommitted changes)

---

## Performance

Target execution time: **3-5 seconds** (script runs all API calls in parallel)
