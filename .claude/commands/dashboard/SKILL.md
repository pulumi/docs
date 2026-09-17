---
description: Display repository status with issues, CI/CD health, and suggested tasks (PR triage lives in /pr-review)
---

# Repository Dashboard

**Use this when:** You want a quick overview of repository status, priority work items, and health metrics.

Displays assigned issues, suggested next tasks, CI/CD health, and deployment status. Open PRs are adjudicated on the `/pr-review` board; the dashboard shows only their count.

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
  "prs": [],                    // always empty — PR triage moved to /pr-review
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

If `rate_remaining` < 50, show warning: `⚠️  GitHub API rate limit low ({count} remaining) - dashboard requires 6+ API calls`

#### Priority Items Section

**PRs:** not listed here. Open PRs are adjudicated on the `/pr-review` board (stamp / judge / route / blocked, with collision clusters); the dashboard shows only the open-PR count from `stats.total_prs`, as one line: `📋 {total_prs} open PRs → /pr-review`.

**Issues:**

- Show assigned issues after PRs
- Format: `🐛 #{number}  {title} (issue, {age}d)`
- Limits: compact 5, detailed 10, full 20

#### Suggested Tasks Section

Generate actionable tasks based on data. Priority order:

1. **Open PRs** (if `stats.total_prs > 0`):
   - `📋 Adjudicate {total_prs} open PRs → /pr-review`

2. **Uncommitted changes** (if `uncommitted_changes > 0`):
   - `📝 Review and commit {count} uncommitted changes → git status`

3. **Assigned issues**:
   - `🐛 Work on issue #{number}: {short_title} → gh issue view {number}`
   - Limit to top 2

4. **Workflow failures** (if `status: "CRITICAL"` and recent failures):
   - `❌ Investigate workflow failure: {name} → gh run list --workflow "{name}"`

5. **Current branch work** (if not on master/main):
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

## Display Modes

### Compact (Default)

- **Purpose**: Quick status check
- **Items**: Top 5 issues, 3 tasks
- **Details**: Essential info only
- **Target**: Fits on one screen

### Detailed

- **Purpose**: Standard review workflow
- **Items**: Top 10 issues, 5 tasks
- **Details**: More context per item
- **Target**: 1-2 screens

### Full

- **Purpose**: Deep investigation
- **Items**: Top 20+ issues, 10 tasks
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
