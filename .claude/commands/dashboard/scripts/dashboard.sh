#!/bin/bash
set -euo pipefail

# This script collects repository data and outputs structured JSON
# The SKILL.md file instructs Claude how to interpret and present this data

# ═══════════════════════════════════════════════════════════════════════════
# 1. Collect User Context
# ═══════════════════════════════════════════════════════════════════════════

GITHUB_USER=$(gh api user --jq '.login' 2>/dev/null || echo "unknown")
IS_PULUMI_MEMBER="false"
if gh api orgs/pulumi/members/$GITHUB_USER --silent 2>/dev/null; then
  IS_PULUMI_MEMBER="true"
fi

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")
UNCOMMITTED_CHANGES=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')

# Check GitHub API rate limit
RATE_REMAINING=$(gh api rate_limit --jq '.rate.remaining' 2>/dev/null || echo "0")

# ═══════════════════════════════════════════════════════════════════════════
# 2. Parallel Data Collection
# ═══════════════════════════════════════════════════════════════════════════

TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

(
  # PRs assigned to me
  gh pr list --assignee @me --json number,title,author,state,createdAt,labels,isDraft,updatedAt --limit 100 > "$TMPDIR/prs_assigned.json" 2>/dev/null &

  # PRs mentioning me
  gh pr list --search "mentions:@me" --json number,title,author,state,createdAt,labels,isDraft,updatedAt --limit 100 > "$TMPDIR/prs_mentions.json" 2>/dev/null &

  # All open PRs
  gh pr list --state open --json number,title,author,state,createdAt,labels,isDraft,updatedAt --limit 100 > "$TMPDIR/prs_all.json" 2>/dev/null &

  # Issues assigned to me
  gh issue list --assignee @me --json number,title,author,state,createdAt,labels --limit 100 > "$TMPDIR/issues_assigned.json" 2>/dev/null &

  # All open issues
  gh issue list --state open --json number,title,author,state,createdAt,labels --limit 100 > "$TMPDIR/issues_all.json" 2>/dev/null &

  # Recent workflow runs
  gh run list --limit 50 --json databaseId,status,conclusion,name,createdAt,headBranch,event > "$TMPDIR/workflows.json" 2>/dev/null &

  wait
) || {
  echo '{"error": "Some GitHub API calls failed"}' >&2
}

# ═══════════════════════════════════════════════════════════════════════════
# 3. Calculate Priority Scores for PRs
# ═══════════════════════════════════════════════════════════════════════════

is_team_member() {
  local author="$1"
  if [ "$IS_PULUMI_MEMBER" = "true" ]; then
    gh api orgs/pulumi/members/$author --silent 2>/dev/null
    return $?
  fi
  return 1
}

calculate_priority() {
  local pr_json="$1"
  local priority=0

  local number=$(echo "$pr_json" | jq -r '.number')
  local author=$(echo "$pr_json" | jq -r '.author.login')
  local is_draft=$(echo "$pr_json" | jq -r '.isDraft')
  local created_at=$(echo "$pr_json" | jq -r '.createdAt')
  local labels=$(echo "$pr_json" | jq -r '.labels[].name' | tr '\n' '|')

  # Check if assigned to me
  if cat "$TMPDIR/prs_assigned.json" 2>/dev/null | jq -e ".[] | select(.number == $number)" >/dev/null 2>&1; then
    priority=$((priority + 100))
  fi

  # Check if mentions me
  if cat "$TMPDIR/prs_mentions.json" 2>/dev/null | jq -e ".[] | select(.number == $number)" >/dev/null 2>&1; then
    priority=$((priority + 80))
  fi

  # Security patches
  if echo "$labels" | grep -q "deps-security-patch"; then
    priority=$((priority + 70))
  fi

  # High-risk Dependabot
  if echo "$labels" | grep -q "deps-risk-high"; then
    priority=$((priority + 60))
  fi

  # Ready for review (not draft)
  if [ "$is_draft" = "false" ]; then
    priority=$((priority + 40))
  fi

  # Team member bonus (internal users only)
  if is_team_member "$author"; then
    priority=$((priority + 30))
  fi

  # Age calculation (days old)
  if [ "$created_at" != "null" ]; then
    created_timestamp=$(date -d "$created_at" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$created_at" +%s 2>/dev/null || echo "0")
    current_timestamp=$(date +%s)
    age_days=$(( (current_timestamp - created_timestamp) / 86400 ))

    if [ $age_days -gt 14 ]; then
      priority=$((priority + 50))
    elif [ $age_days -gt 7 ]; then
      priority=$((priority + 25))
    fi
  fi

  # Medium-risk Dependabot
  if echo "$labels" | grep -q "deps-risk-medium"; then
    priority=$((priority + 20))
  fi

  # Draft penalty
  if [ "$is_draft" = "true" ]; then
    priority=$((priority - 20))
  fi

  echo "$priority"
}

# Build enriched PR list with priorities
PRS_WITH_PRIORITY="$TMPDIR/prs_enriched.json"
echo "[" > "$PRS_WITH_PRIORITY"
first=true

if [ -f "$TMPDIR/prs_all.json" ]; then
  cat "$TMPDIR/prs_all.json" | jq -c '.[]' | while read -r pr; do
    number=$(echo "$pr" | jq -r '.number')
    created_at=$(echo "$pr" | jq -r '.createdAt')
    labels=$(echo "$pr" | jq -r '.labels[].name' | tr '\n' '|')

    priority=$(calculate_priority "$pr")

    # Calculate age
    age_days=0
    if [ "$created_at" != "null" ]; then
      created_timestamp=$(date -d "$created_at" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$created_at" +%s 2>/dev/null || echo "0")
      current_timestamp=$(date +%s)
      age_days=$(( (current_timestamp - created_timestamp) / 86400 ))
    fi

    # Determine type
    type="normal"
    if echo "$labels" | grep -q "deps-security-patch"; then
      type="security"
    elif echo "$labels" | grep -q "deps-risk-high"; then
      type="high-risk"
    elif echo "$labels" | grep -q "deps-risk-medium"; then
      type="medium-risk"
    fi

    # Check if assigned or mentions me
    is_assigned="false"
    is_mentioned="false"
    if cat "$TMPDIR/prs_assigned.json" 2>/dev/null | jq -e ".[] | select(.number == $number)" >/dev/null 2>&1; then
      is_assigned="true"
    fi
    if cat "$TMPDIR/prs_mentions.json" 2>/dev/null | jq -e ".[] | select(.number == $number)" >/dev/null 2>&1; then
      is_mentioned="true"
    fi

    # Add priority and metadata to PR object
    enriched=$(echo "$pr" | jq --arg prio "$priority" --arg age "$age_days" --arg type "$type" --arg assigned "$is_assigned" --arg mentioned "$is_mentioned" \
      '. + {priority: ($prio | tonumber), age_days: ($age | tonumber), type: $type, is_assigned: ($assigned == "true"), is_mentioned: ($mentioned == "true")}')

    if [ "$first" = true ]; then
      echo "$enriched" >> "$PRS_WITH_PRIORITY"
      first=false
    else
      echo ",$enriched" >> "$PRS_WITH_PRIORITY"
    fi
  done
fi

echo "]" >> "$PRS_WITH_PRIORITY"

# ═══════════════════════════════════════════════════════════════════════════
# 4. Enrich Issues with Age
# ═══════════════════════════════════════════════════════════════════════════

ISSUES_ENRICHED="$TMPDIR/issues_enriched.json"
echo "[" > "$ISSUES_ENRICHED"
first=true

if [ -f "$TMPDIR/issues_assigned.json" ]; then
  cat "$TMPDIR/issues_assigned.json" | jq -c '.[]' | while read -r issue; do
    created_at=$(echo "$issue" | jq -r '.createdAt')

    age_days=0
    if [ "$created_at" != "null" ]; then
      created_timestamp=$(date -d "$created_at" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$created_at" +%s 2>/dev/null || echo "0")
      current_timestamp=$(date +%s)
      age_days=$(( (current_timestamp - created_timestamp) / 86400 ))
    fi

    enriched=$(echo "$issue" | jq --arg age "$age_days" '. + {age_days: ($age | tonumber)}')

    if [ "$first" = true ]; then
      echo "$enriched" >> "$ISSUES_ENRICHED"
      first=false
    else
      echo ",$enriched" >> "$ISSUES_ENRICHED"
    fi
  done
fi

echo "]" >> "$ISSUES_ENRICHED"

# ═══════════════════════════════════════════════════════════════════════════
# 5. Workflow Health Analysis
# ═══════════════════════════════════════════════════════════════════════════

WORKFLOW_STATUS="UNKNOWN"
TOTAL_RUNS=0
SUCCESS_RUNS=0
FAILURE_RUNS=0
SUCCESS_RATE=0

if [ -f "$TMPDIR/workflows.json" ]; then
  CUTOFF_TIMESTAMP=$(date -d "24 hours ago" +%s 2>/dev/null || date -v-24H +%s 2>/dev/null || echo "0")

  cat "$TMPDIR/workflows.json" | jq -c '.[]' | while read -r run; do
    created_at=$(echo "$run" | jq -r '.createdAt')
    conclusion=$(echo "$run" | jq -r '.conclusion')
    status=$(echo "$run" | jq -r '.status')

    if [ "$created_at" != "null" ]; then
      run_timestamp=$(date -d "$created_at" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$created_at" +%s 2>/dev/null || echo "0")

      if [ "$run_timestamp" -gt "$CUTOFF_TIMESTAMP" ]; then
        echo "$conclusion|$status" >> "$TMPDIR/workflow_stats.txt"
      fi
    fi
  done

  if [ -f "$TMPDIR/workflow_stats.txt" ] && [ -s "$TMPDIR/workflow_stats.txt" ]; then
    # Use awk for reliable line counting
    TOTAL_RUNS=$(awk 'END {print NR}' "$TMPDIR/workflow_stats.txt")
    SUCCESS_RUNS=$(grep -cE "^(success|skipped)\|" "$TMPDIR/workflow_stats.txt" 2>/dev/null || echo "0")
    FAILURE_RUNS=$(grep -c "^failure|" "$TMPDIR/workflow_stats.txt" 2>/dev/null || echo "0")

    # Sanitize to ensure numeric values
    TOTAL_RUNS=$(printf "%d" "$TOTAL_RUNS" 2>/dev/null || echo "0")
    SUCCESS_RUNS=$(printf "%d" "$SUCCESS_RUNS" 2>/dev/null || echo "0")
    FAILURE_RUNS=$(printf "%d" "$FAILURE_RUNS" 2>/dev/null || echo "0")

    if [ "$TOTAL_RUNS" -gt 0 ]; then
      SUCCESS_RATE=$(( SUCCESS_RUNS * 100 / TOTAL_RUNS ))

      if [ "$FAILURE_RUNS" -eq 0 ] && [ "$SUCCESS_RATE" -ge 95 ]; then
        WORKFLOW_STATUS="HEALTHY"
      elif [ "$FAILURE_RUNS" -le 2 ] && [ "$SUCCESS_RATE" -ge 85 ]; then
        WORKFLOW_STATUS="WARNING"
      else
        WORKFLOW_STATUS="CRITICAL"
      fi
    fi
  fi
fi

# Enrich recent workflows with time ago
RECENT_WORKFLOWS="$TMPDIR/recent_workflows_enriched.json"
if [ -f "$TMPDIR/workflows.json" ]; then
  cat "$TMPDIR/workflows.json" | jq '[.[] | select(.createdAt != null)] | .[0:3]' > "$RECENT_WORKFLOWS"
else
  echo "[]" > "$RECENT_WORKFLOWS"
fi

# ═══════════════════════════════════════════════════════════════════════════
# 6. Deployment Information
# ═══════════════════════════════════════════════════════════════════════════

DEPLOYMENT_COMMIT="unknown"
DEPLOYMENT_TIMESTAMP=0

if DEPLOYMENT_INFO=$(curl -s --max-time 5 https://www.pulumi.com/metadata.json 2>/dev/null); then
  DEPLOYMENT_COMMIT=$(echo "$DEPLOYMENT_INFO" | jq -r '.commit // "unknown"' | cut -c1-7)
  DEPLOYMENT_TIME=$(echo "$DEPLOYMENT_INFO" | jq -r '.timestamp // "0"')
  if [ "$DEPLOYMENT_TIME" != "0" ] && [ "$DEPLOYMENT_TIME" != "null" ]; then
    DEPLOYMENT_TIMESTAMP=$(( DEPLOYMENT_TIME / 1000 ))
  fi
fi

# ═══════════════════════════════════════════════════════════════════════════
# 7. Output Structured JSON
# ═══════════════════════════════════════════════════════════════════════════

TOTAL_PRS=$(cat "$TMPDIR/prs_all.json" 2>/dev/null | jq 'length' || echo "0")
ASSIGNED_PRS=$(cat "$TMPDIR/prs_assigned.json" 2>/dev/null | jq 'length' || echo "0")
TOTAL_ISSUES=$(cat "$TMPDIR/issues_all.json" 2>/dev/null | jq 'length' || echo "0")
ASSIGNED_ISSUES=$(cat "$TMPDIR/issues_assigned.json" 2>/dev/null | jq 'length' || echo "0")

# Build final JSON output
jq -n \
  --arg github_user "$GITHUB_USER" \
  --argjson is_pulumi_member "$IS_PULUMI_MEMBER" \
  --arg current_branch "$CURRENT_BRANCH" \
  --argjson uncommitted_changes "$UNCOMMITTED_CHANGES" \
  --argjson rate_remaining "$RATE_REMAINING" \
  --argjson prs "$(cat "$PRS_WITH_PRIORITY" 2>/dev/null || echo '[]')" \
  --argjson issues "$(cat "$ISSUES_ENRICHED" 2>/dev/null || echo '[]')" \
  --arg workflow_status "$WORKFLOW_STATUS" \
  --argjson total_runs "$TOTAL_RUNS" \
  --argjson success_runs "$SUCCESS_RUNS" \
  --argjson failure_runs "$FAILURE_RUNS" \
  --argjson success_rate "$SUCCESS_RATE" \
  --argjson recent_workflows "$(cat "$RECENT_WORKFLOWS" 2>/dev/null || echo '[]')" \
  --arg deployment_commit "$DEPLOYMENT_COMMIT" \
  --argjson deployment_timestamp "$DEPLOYMENT_TIMESTAMP" \
  --argjson total_prs "$TOTAL_PRS" \
  --argjson assigned_prs "$ASSIGNED_PRS" \
  --argjson total_issues "$TOTAL_ISSUES" \
  --argjson assigned_issues "$ASSIGNED_ISSUES" \
  '{
    user: {
      github_user: $github_user,
      is_pulumi_member: $is_pulumi_member,
      current_branch: $current_branch,
      uncommitted_changes: $uncommitted_changes,
      rate_remaining: $rate_remaining
    },
    prs: $prs,
    issues: $issues,
    workflows: {
      status: $workflow_status,
      total_runs: $total_runs,
      success_runs: $success_runs,
      failure_runs: $failure_runs,
      success_rate: $success_rate,
      recent: $recent_workflows
    },
    deployment: {
      commit: $deployment_commit,
      timestamp: $deployment_timestamp
    },
    stats: {
      total_prs: $total_prs,
      assigned_prs: $assigned_prs,
      total_issues: $total_issues,
      assigned_issues: $assigned_issues
    }
  }'
