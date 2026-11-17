#!/usr/bin/env bash
#
# scrub-pr.sh: remove everything GitHub lets someone with write access remove for one pull request.
#
# Use it when a PR leaked something it shouldn't have (unreleased product details,
# credentials, customer data). It inventories the PR, prints the full plan, and does
# nothing until you type the PR number back. Then it:
#
#   1. Cancels the PR's in-progress Actions runs, so nothing posts new content mid-scrub.
#   2. Replaces the title and body with a neutral line and closes the PR.
#   3. Deletes every review comment and conversation comment.
#   4. Replaces the body of every submitted review (GitHub won't delete those).
#   5. Deletes the PR's Actions runs (logs and artifacts go with them).
#   6. Deletes the PR's deployments.
#   7. Deletes the head branch, if it lives in this repo and nothing else needs it.
#   8. Sweeps again a few times for comments, runs, and deployments that closing
#      and editing the PR set off, waits for those runs to finish, and deletes them.
#
# A run belongs to the PR when its head commit is one of the PR's commits, or when
# it was triggered by a comment or review event after the PR opened and its title
# is one of the PR's titles (comment-triggered runs record the default branch's
# commit, not the PR's). Branch names are never used to match runs.
#
# The head branch is kept when it's the default branch, is protected, or another
# PR uses it, unless you pass --force-branch.
#
# GitHub doesn't let anyone but GitHub Support delete the PR itself, its edit
# history, or refs/pull/<n>/*. The script writes a support request for those.
#
# Usage:
#   scripts/scrub-pr.sh <pr-number> [--repo owner/name] [--dry-run] [--force-branch]
#
# Requires: gh signed in as someone with write access to the repo (classic token
# scope `repo`, SSO-authorized for the org), jq, and bash 4.4+.
#
# Exits 1 if any step failed or a run was still in progress at the end.
#
# Tests: scripts/scrub-pr.test.sh runs this script against a stub gh.

set -uo pipefail

if (( BASH_VERSINFO[0] < 4 || (BASH_VERSINFO[0] == 4 && BASH_VERSINFO[1] < 4) )); then
    echo "Needs bash 4.4 or later (this is ${BASH_VERSION})." >&2
    exit 1
fi

REPO="pulumi/docs"
DRY_RUN=0
FORCE_BRANCH=0
PR=""
REPLACEMENT="Closed, created in error."
SWEEP_PASSES=3
SWEEP_DELAY=${SCRUB_SWEEP_DELAY:-20}
RUN_WAIT_SECONDS=300
COMMENT_EVENTS=(issue_comment pull_request_review pull_request_review_comment)

while [[ $# -gt 0 ]]; do
    case "$1" in
        --repo) REPO="$2"; shift 2 ;;
        --dry-run) DRY_RUN=1; shift ;;
        --force-branch) FORCE_BRANCH=1; shift ;;
        -h|--help) awk 'NR>1 && !/^#/ {exit} NR>1 {sub(/^# ?/, ""); print}' "$0"; exit 0 ;;
        *) if [[ -z "$PR" && "$1" =~ ^[0-9]+$ ]]; then PR="$1"; shift; else echo "Unknown argument: $1" >&2; exit 2; fi ;;
    esac
done

[[ -n "$PR" ]] || { echo "Usage: $0 <pr-number> [--repo owner/name] [--dry-run] [--force-branch]" >&2; exit 2; }
command -v gh >/dev/null || { echo "gh is not installed." >&2; exit 1; }
command -v jq >/dev/null || { echo "jq is not installed." >&2; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "gh is not signed in. Run: gh auth login" >&2; exit 1; }

api() { gh api -H "Accept: application/vnd.github+json" "$@"; }
dedupe() { awk -F'\t' 'NF && !seen[$1]++'; }
# Branch names can contain &, #, and %, which gh api sends unencoded.
ref_path() { jq -rn --arg r "$1" '$r | split("/") | map(@uri) | join("/")'; }

echo "Inventorying ${REPO}#${PR}..."

pr_json=$(api "repos/${REPO}/pulls/${PR}") || { echo "Couldn't read ${REPO}#${PR}." >&2; exit 1; }
title=$(jq -r .title <<<"$pr_json")
state=$(jq -r .state <<<"$pr_json")
merged=$(jq -r .merged <<<"$pr_json")
author=$(jq -r .user.login <<<"$pr_json")
head_ref=$(jq -r .head.ref <<<"$pr_json")
head_repo=$(jq -r '.head.repo.full_name // ""' <<<"$pr_json")
created_at=$(jq -r .created_at <<<"$pr_json")
# A merged PR's merge commit is on the default branch, so its deployments aren't the PR's.
merge_sha=""
[[ "$merged" == "true" ]] || merge_sha=$(jq -r '.merge_commit_sha // ""' <<<"$pr_json")
viewer=$(api user --jq .login)
default_branch=$(api "repos/${REPO}" --jq .default_branch)

mapfile -t shas < <(api --paginate "repos/${REPO}/pulls/${PR}/commits?per_page=100" --jq '.[].sha')

# Every title the PR has had, so comment-triggered runs from before a rename still match.
titles_json=$(
    { jq -c '[.title]' <<<"$pr_json"
      api --paginate "repos/${REPO}/issues/${PR}/events?per_page=100" \
          --jq '[.[] | select(.event == "renamed") | .rename.from, .rename.to]'
    } | jq -sc --arg r "${REPLACEMENT%.}" 'add | unique | map(select(. != $r))'
)
shas_json=$(printf '%s\n' "${shas[@]}" | jq -Rsc 'split("\n") | map(select(length > 0))')

other_prs=""
if [[ "$head_repo" == "$REPO" ]]; then
    other_prs=$(api -X GET "repos/${REPO}/pulls" -f state=all -f head="${REPO%%/*}:${head_ref}" -F per_page=100 \
        --jq "[.[] | select(.number != ${PR}) | .number] | join(\", \")")
fi

branch_exists=0
branch_protected=0
branch_keep_reason=""
if [[ "$head_repo" == "$REPO" ]]; then
    [[ "$(api "repos/${REPO}/branches/$(ref_path "$head_ref")" --jq .protected 2>/dev/null)" == "true" ]] && branch_protected=1
    if api "repos/${REPO}/git/ref/heads/$(ref_path "$head_ref")" >/dev/null 2>&1; then
        branch_exists=1
        if [[ "$head_ref" == "$default_branch" ]]; then
            branch_keep_reason="it's the default branch"
        elif (( branch_protected )); then
            branch_keep_reason="it's protected"
        elif [[ -n "$other_prs" ]]; then
            branch_keep_reason="other PRs use it (${other_prs})"
        fi
        [[ "$head_ref" == "$default_branch" ]] || { (( FORCE_BRANCH )) && branch_keep_reason=""; }
    fi
fi

inventory_comments() {
    mapfile -t issue_comments < <(api --paginate "repos/${REPO}/issues/${PR}/comments?per_page=100" --jq '.[] | "\(.id)\t\(.user.login)"')
    mapfile -t review_comments < <(api --paginate "repos/${REPO}/pulls/${PR}/comments?per_page=100" --jq '.[] | "\(.id)\t\(.user.login)"')
    mapfile -t reviews < <(api --paginate "repos/${REPO}/pulls/${PR}/reviews?per_page=100" \
        --jq ".[] | select((.body // \"\") != \"\" and .body != \"${REPLACEMENT}\") | \"\(.id)\t\(.user.login)\t\(.state)\"")
}

# Rows: id, workflow name, status, why it matched, run title.
inventory_runs() {
    local sha ev
    runs=()
    for sha in "${shas[@]}"; do
        while IFS= read -r line; do [[ -n "$line" ]] && runs+=("$line"); done < <(
            api --paginate "repos/${REPO}/actions/runs?head_sha=${sha}&per_page=100" \
                --jq '.workflow_runs[] | "\(.id)\t\(.name)\t\(.status)\tcommit \(.head_sha[0:7])\t\(.display_title // "")"')
    done
    # After the scrub renames the PR, its new title is shared with every other scrubbed
    # PR, so only trust it for runs created after this scrub started.
    local since titles
    for ev in "${COMMENT_EVENTS[@]}"; do
        for since in "$created_at" ${scrub_started:+"$scrub_started"}; do
            titles=$titles_json
            [[ "$since" == "${scrub_started:-}" ]] && titles=$(jq -cn --arg r "${REPLACEMENT%.}" '[$r]')
            while IFS= read -r line; do [[ -n "$line" ]] && runs+=("$line"); done < <(
                api -X GET --paginate "repos/${REPO}/actions/runs" -f event="$ev" -f created=">=${since}" -F per_page=100 \
                    --jq '.workflow_runs[]' |
                jq -r --argjson titles "$titles" --argjson shas "$shas_json" --argjson pr "$PR" '
                select((.display_title as $t | $titles | index($t))
                       or (.head_sha as $s | $shas | index($s))
                       or any(.pull_requests[]?; .number == $pr))
                | "\(.id)\t\(.name)\t\(.status)\t\(.event)\t\(.display_title // "")"')
        done
    done
    mapfile -t runs < <(printf '%s\n' "${runs[@]+"${runs[@]}"}" | dedupe)
}

inventory_deployments() {
    local q queries=()
    for q in "${shas[@]}" ${merge_sha:+"$merge_sha"}; do queries+=("sha=${q}"); done
    queries+=("ref=refs/pull/${PR}/merge" "ref=refs/pull/${PR}/head")
    # Deployments made from a pull_request event can be recorded against the branch name.
    # Skip that lookup for the default branch and for protected or shared branches, whose
    # deployments aren't only this PR's.
    if [[ "$head_repo" == "$REPO" && -z "$other_prs" && "$head_ref" != "$default_branch" ]] && (( ! branch_protected )); then
        queries+=("ref=${head_ref}")
    fi
    deployments=()
    for q in "${queries[@]}"; do
        while IFS= read -r line; do [[ -n "$line" ]] && deployments+=("${line}"$'\t'"${q}"); done < <(
            api -X GET "repos/${REPO}/deployments" -f "$q" -F per_page=100 --jq '.[] | "\(.id)\t\(.environment)"')
    done
    mapfile -t deployments < <(printf '%s\n' "${deployments[@]+"${deployments[@]}"}" | dedupe)
}

scrub_started=""
inventory_comments
inventory_runs
inventory_deployments

if (( branch_exists )) && [[ -z "$branch_keep_reason" ]]; then
    branch_plan="Delete branch ${head_ref}"
elif (( branch_exists )); then
    branch_plan="Keep branch ${head_ref}: ${branch_keep_reason}"
    [[ "$head_ref" == "$default_branch" ]] || branch_plan+=" (--force-branch deletes it)"
else
    branch_plan="Head branch: nothing to delete (already gone or in a fork)"
fi

in_progress=$(printf '%s\n' "${runs[@]+"${runs[@]}"}" | awk -F'\t' 'NF && $3!="completed"' | wc -l | tr -d ' ')

cat <<EOF

================================================================
 Plan for ${REPO}#${PR}
================================================================
 Title:        ${title}
 Author:       ${author}
 State:        ${state}$( [[ "$merged" == "true" ]] && echo " (MERGED)" )
 Head branch:  ${head_ref} (${head_repo:-deleted fork})
 Commits:      ${#shas[@]}
 Running as:   ${viewer}
----------------------------------------------------------------
 1. Cancel ${in_progress} in-progress workflow run(s)
 2. Set title to "${REPLACEMENT%.}", body to "${REPLACEMENT}", and close the PR
 3. Delete ${#review_comments[@]} review comment(s) and ${#issue_comments[@]} conversation comment(s)
 4. Replace the body of ${#reviews[@]} review(s) with "${REPLACEMENT}"
 5. Delete ${#runs[@]} workflow run(s)
 6. Delete ${#deployments[@]} deployment(s)
 7. ${branch_plan}
 8. Sweep ${SWEEP_PASSES} more times, ${SWEEP_DELAY}s apart, and delete any new comments,
    runs, and deployments for this PR (new runs are allowed to finish first)
----------------------------------------------------------------
EOF

if (( ${#issue_comments[@]} + ${#review_comments[@]} )); then
    echo " Comments by author:"
    printf '%s\n' "${issue_comments[@]}" "${review_comments[@]}" | awk -F'\t' 'NF {c[$2]++} END {for (a in c) printf "   %-30s %d\n", a, c[a]}'
fi
if (( ${#runs[@]} )); then
    echo " Workflow runs (id, workflow, status, matched by, run title):"
    echo " Check the titles: a run from another PR with the same title would match too."
    printf '%s\n' "${runs[@]}" | awk -F'\t' '{printf "   %s  %-38s %-12s %-20s %s\n", $1, $2, $3, $4, $5}'
fi
if (( ${#deployments[@]} )); then
    echo " Deployments (id, environment, matched by):"
    printf '%s\n' "${deployments[@]}" | awk -F'\t' '{printf "   %s  %-12s %s\n", $1, $2, $3}'
fi
echo " Titles used to match comment-triggered runs:"
jq -r '.[] | "   " + .' <<<"$titles_json"
if [[ "$merged" == "true" ]]; then
    echo
    echo " WARNING: this PR was merged. Its commits are in the base branch history, and"
    echo " this script can't remove them. You need a history rewrite plus GitHub Support."
fi
echo "================================================================"

if (( DRY_RUN )); then
    echo "Dry run: nothing changed."
    exit 0
fi

echo
read -r -p "Type the PR number (${PR}) to run this plan, or anything else to abort: " answer
[[ "$answer" == "$PR" ]] || { echo "Aborted. Nothing changed."; exit 1; }

failures=()
step() {
    local label="$1"; shift
    if "$@" >/dev/null 2>&1; then echo "  ok    ${label}"; else echo "  FAIL  ${label}"; failures+=("$label"); fi
}

run_status() { api "repos/${REPO}/actions/runs/$1" --jq .status 2>/dev/null; }

wait_for_runs() {
    local deadline=$(( SECONDS + $1 )) id pending
    shift
    while :; do
        pending=0
        for id in "$@"; do [[ "$(run_status "$id")" == "completed" ]] || pending=1; done
        (( pending == 0 || SECONDS >= deadline )) && return "$pending"
        sleep 5
    done
}

cancel_runs() {
    local row id ids=()
    for row in "${runs[@]}"; do
        IFS=$'\t' read -r id _ status _ <<<"$row"
        [[ "$status" == "completed" ]] && continue
        api -X POST "repos/${REPO}/actions/runs/${id}/force-cancel" >/dev/null 2>&1 && echo "  ok    cancel run ${id}"
        ids+=("$id")
    done
    (( ${#ids[@]} )) && wait_for_runs 60 "${ids[@]}"
    return 0
}

delete_comments() {
    local row
    for row in "${review_comments[@]}"; do step "review comment ${row%%$'\t'*}" api -X DELETE "repos/${REPO}/pulls/comments/${row%%$'\t'*}"; done
    for row in "${issue_comments[@]}"; do step "comment ${row%%$'\t'*}" api -X DELETE "repos/${REPO}/issues/comments/${row%%$'\t'*}"; done
    for row in "${reviews[@]}"; do step "review ${row%%$'\t'*}" api -X PUT "repos/${REPO}/pulls/${PR}/reviews/${row%%$'\t'*}" -f body="${REPLACEMENT}"; done
}

delete_runs() {
    local row id name
    for row in "${runs[@]}"; do
        IFS=$'\t' read -r id name _ _ <<<"$row"
        step "run ${id} (${name})" api -X DELETE "repos/${REPO}/actions/runs/${id}"
    done
}

delete_deployments() {
    local row id
    for row in "${deployments[@]}"; do
        id=${row%%$'\t'*}
        api -X POST "repos/${REPO}/deployments/${id}/statuses" -f state=inactive >/dev/null 2>&1
        step "deployment ${id}" api -X DELETE "repos/${REPO}/deployments/${id}"
    done
}

scrub_started=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo
echo "1. Cancel in-progress runs"
cancel_runs

echo "2. Title, body, state"
step "edit and close PR" api -X PATCH "repos/${REPO}/pulls/${PR}" \
    -f title="${REPLACEMENT%.}" -f body="${REPLACEMENT}" -f state=closed

echo "3-4. Comments and reviews"
delete_comments

echo "5. Workflow runs"
delete_runs

echo "6. Deployments"
delete_deployments

echo "7. Head branch"
if (( branch_exists )) && [[ -z "$branch_keep_reason" ]]; then
    step "branch ${head_ref}" api -X DELETE "repos/${REPO}/git/refs/heads/$(ref_path "$head_ref")"
else
    echo "  skip  ${branch_plan}"
fi

# Closing and editing the PR starts workflows of its own (the docs repo's pr-closed
# cleanup deletes the preview buckets), so let those finish before deleting them.
unfinished=()
for pass in $(seq 1 "$SWEEP_PASSES"); do
    unfinished=()
    echo "8. Sweep ${pass}/${SWEEP_PASSES} (waiting ${SWEEP_DELAY}s)"
    sleep "$SWEEP_DELAY"
    inventory_comments
    inventory_runs
    inventory_deployments
    if (( ${#issue_comments[@]} + ${#review_comments[@]} + ${#reviews[@]} + ${#runs[@]} + ${#deployments[@]} == 0 )); then
        echo "  ok    nothing new"
        continue
    fi
    mapfile -t running < <(printf '%s\n' "${runs[@]+"${runs[@]}"}" | awk -F'\t' 'NF && $3!="completed" {print $1}')
    if (( ${#running[@]} )); then
        echo "  wait  ${#running[@]} run(s) still in progress (up to ${RUN_WAIT_SECONDS}s)"
        wait_for_runs "$RUN_WAIT_SECONDS" "${running[@]}" || true
        inventory_runs
        mapfile -t unfinished < <(printf '%s\n' "${runs[@]+"${runs[@]}"}" | awk -F'\t' 'NF && $3!="completed"')
        mapfile -t runs < <(printf '%s\n' "${runs[@]+"${runs[@]}"}" | awk -F'\t' 'NF && $3=="completed"')
    fi
    delete_comments
    delete_runs
    delete_deployments
done

request_file="scrub-pr-${PR}-github-support.md"
{
    echo "Subject: Request to delete PR ${REPO}#${PR} and purge its refs, commits, and edit history"
    echo
    echo "Hi,"
    echo
    echo "A pull request in ${REPO} was opened by mistake and exposes information that must not be public. We need it removed entirely."
    echo
    echo "- Pull request: https://github.com/${REPO}/pull/${PR}"
    echo "- Head branch: ${head_ref}"
    echo "- Refs still present: refs/pull/${PR}/head, refs/pull/${PR}/merge"
    echo "- Commits only reachable through those refs:"
    for sha in "${shas[@]}"; do echo "  - ${sha}"; done
    echo
    echo "We have closed the PR, replaced its title and description, and deleted its comments, workflow runs, and deployments."
    echo
    echo "Please:"
    echo
    echo "1. Delete pull request #${PR}."
    echo "2. Remove refs/pull/${PR}/head and refs/pull/${PR}/merge, and garbage-collect the commits above so they can't be fetched by SHA or viewed through commit, compare, or blob URLs."
    echo "3. Purge the edit history of the PR title, description, comments, and reviews."
    echo "4. Clear any cached views of the PR, its files, and its diff."
    echo
    echo "Thanks,"
    echo "${viewer}"
} > "$request_file"

cat <<EOF

================================================================
 Done. ${#failures[@]} step(s) failed.
EOF
for f in "${failures[@]+"${failures[@]}"}"; do echo "   - ${f}"; done
if (( ${#unfinished[@]} )); then
    echo
    echo " Runs still in progress at the end, not deleted. Delete them once they finish:"
    printf '%s\n' "${unfinished[@]}" | awk -F'\t' '{printf "   https://github.com/'"${REPO}"'/actions/runs/%s  (%s)\n", $1, $2}'
fi
cat <<EOF

 Still there, and only GitHub Support can remove it:
   - The PR itself and the edit history of its title, body, comments, and reviews
   - refs/pull/${PR}/head and /merge, and the ${#shas[@]} commit(s) they point to
   - Commit statuses and check runs on those commits

 Request text written to ./${request_file}
 File it at https://support.github.com/contact (signed in as an org owner).

 Check by hand:
   - Runs triggered by comments on this PR from workflows that set their own
     run-name, so their title doesn't match the PR's. Look through
     https://github.com/${REPO}/actions?query=event%3Aissue_comment
   - Preview builds (the docs repo's pr-closed workflow deletes the PR's S3
     preview buckets), Slack notifications, and issues or PRs linking here.
================================================================
EOF

(( ${#failures[@]} + ${#unfinished[@]} == 0 ))
