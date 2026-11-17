#!/usr/bin/env bash
#
# scrub-pr.sh: remove everything GitHub lets someone with write access remove for one pull request.
#
# Use it when a PR leaked something it shouldn't have (unreleased product details,
# credentials, customer data). It inventories the PR, prints the full plan, and does
# nothing until you type the PR number back. Then it:
#
#   1. Replaces the title and body with a neutral line and closes the PR.
#   2. Deletes every review comment and conversation comment.
#   3. Replaces the body of every submitted review (GitHub won't delete those).
#   4. Deletes every Actions run whose head commit belongs to the PR (logs and artifacts go with it).
#   5. Deletes the PR's deployments.
#   6. Deletes the head branch, if it lives in this repo.
#
# Runs are matched by commit SHA, never by branch name, so a reused branch name
# can't drag in another PR's runs.
#
# GitHub doesn't let anyone but GitHub Support delete the PR itself, its edit
# history, or refs/pull/<n>/*. The script writes a support request for those.
#
# Usage:
#   scripts/scrub-pr.sh <pr-number> [--repo owner/name] [--dry-run]
#
# Requires: gh signed in as someone with write access to the repo (classic token
# scope `repo`, SSO-authorized for the org), jq, and bash 4+.

set -uo pipefail

REPO="pulumi/docs"
DRY_RUN=0
PR=""
REPLACEMENT="Closed, created in error."

while [[ $# -gt 0 ]]; do
    case "$1" in
        --repo) REPO="$2"; shift 2 ;;
        --dry-run) DRY_RUN=1; shift ;;
        -h|--help) awk 'NR>1 && !/^#/ {exit} NR>1 {sub(/^# ?/, ""); print}' "$0"; exit 0 ;;
        *) if [[ -z "$PR" && "$1" =~ ^[0-9]+$ ]]; then PR="$1"; shift; else echo "Unknown argument: $1" >&2; exit 2; fi ;;
    esac
done

[[ -n "$PR" ]] || { echo "Usage: $0 <pr-number> [--repo owner/name] [--dry-run]" >&2; exit 2; }
command -v gh >/dev/null || { echo "gh is not installed." >&2; exit 1; }
command -v jq >/dev/null || { echo "jq is not installed." >&2; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "gh is not signed in. Run: gh auth login" >&2; exit 1; }

api() { gh api -H "Accept: application/vnd.github+json" "$@"; }

echo "Inventorying ${REPO}#${PR}..."

pr_json=$(api "repos/${REPO}/pulls/${PR}") || { echo "Couldn't read ${REPO}#${PR}." >&2; exit 1; }
title=$(jq -r .title <<<"$pr_json")
state=$(jq -r .state <<<"$pr_json")
merged=$(jq -r .merged <<<"$pr_json")
author=$(jq -r .user.login <<<"$pr_json")
head_ref=$(jq -r .head.ref <<<"$pr_json")
head_repo=$(jq -r '.head.repo.full_name // ""' <<<"$pr_json")
viewer=$(api user --jq .login)

mapfile -t shas < <(api --paginate "repos/${REPO}/pulls/${PR}/commits?per_page=100" --jq '.[].sha')
mapfile -t issue_comments < <(api --paginate "repos/${REPO}/issues/${PR}/comments?per_page=100" --jq '.[] | "\(.id)\t\(.user.login)"')
mapfile -t review_comments < <(api --paginate "repos/${REPO}/pulls/${PR}/comments?per_page=100" --jq '.[] | "\(.id)\t\(.user.login)"')
mapfile -t reviews < <(api --paginate "repos/${REPO}/pulls/${PR}/reviews?per_page=100" --jq '.[] | select((.body // "") != "") | "\(.id)\t\(.user.login)\t\(.state)"')

runs=()
for sha in "${shas[@]}"; do
    while IFS= read -r line; do [[ -n "$line" ]] && runs+=("$line"); done < <(
        api --paginate "repos/${REPO}/actions/runs?head_sha=${sha}&per_page=100" \
            --jq '.workflow_runs[] | "\(.id)\t\(.name)\t\(.status)\t\(.head_sha[0:7])"')
done
mapfile -t runs < <(printf '%s\n' "${runs[@]+"${runs[@]}"}" | awk -F'\t' 'NF && !seen[$1]++')

branch_exists=0
if [[ "$head_repo" == "$REPO" ]] && api "repos/${REPO}/git/ref/heads/${head_ref}" >/dev/null 2>&1; then
    branch_exists=1
fi

other_prs=""
if [[ "$head_repo" == "$REPO" ]]; then
    other_prs=$(api "repos/${REPO}/pulls?state=all&head=${REPO%%/*}:${head_ref}&per_page=100" --jq "[.[] | select(.number != ${PR}) | .number] | join(\", \")")
fi

# Workflows on pull_request events deploy from the merge ref, so look there as well as at the PR's own commits.
merge_sha=$(jq -r '.merge_commit_sha // ""' <<<"$pr_json")
deploy_queries=()
for sha in "${shas[@]}" ${merge_sha:+"$merge_sha"}; do deploy_queries+=("sha=${sha}"); done
deploy_queries+=("ref=refs/pull/${PR}/merge" "ref=refs/pull/${PR}/head")
[[ "$head_repo" == "$REPO" && -z "$other_prs" ]] && deploy_queries+=("ref=${head_ref}")
deployments=()
for q in "${deploy_queries[@]}"; do
    while IFS= read -r line; do [[ -n "$line" ]] && deployments+=("$line"); done < <(
        api "repos/${REPO}/deployments?${q}&per_page=100" --jq '.[] | "\(.id)\t\(.environment)"')
done
mapfile -t deployments < <(printf '%s\n' "${deployments[@]+"${deployments[@]}"}" | awk -F'\t' 'NF && !seen[$1]++')

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
 1. Set title to "${REPLACEMENT%.}", body to "${REPLACEMENT}", and close the PR
 2. Delete ${#review_comments[@]} review comment(s)
 3. Delete ${#issue_comments[@]} conversation comment(s)
 4. Replace the body of ${#reviews[@]} review(s) with "${REPLACEMENT}"
 5. Delete ${#runs[@]} workflow run(s)
 6. Delete ${#deployments[@]} deployment(s)
 7. $( if (( branch_exists )); then echo "Delete branch ${head_ref}"; else echo "Head branch: nothing to delete (already gone or in a fork)"; fi )
----------------------------------------------------------------
EOF

if (( ${#issue_comments[@]} + ${#review_comments[@]} )); then
    echo " Comments by author:"
    printf '%s\n' "${issue_comments[@]}" "${review_comments[@]}" | awk -F'\t' 'NF {c[$2]++} END {for (a in c) printf "   %-30s %d\n", a, c[a]}'
fi
if (( ${#runs[@]} )); then
    echo " Workflow runs:"
    printf '%s\n' "${runs[@]}" | awk -F'\t' '{printf "   %s  %-40s %s @ %s\n", $1, $2, $3, $4}'
fi
if (( ${#deployments[@]} )); then
    echo " Deployments:"
    printf '%s\n' "${deployments[@]}" | awk -F'\t' '{printf "   %s  %s\n", $1, $2}'
fi
if [[ "$merged" == "true" ]]; then
    echo
    echo " WARNING: this PR was merged. Its commits are in the base branch history, and"
    echo " this script can't remove them. You need a history rewrite plus GitHub Support."
fi
if [[ -n "$other_prs" ]]; then
    echo
    echo " WARNING: other PRs use the same head branch (${other_prs})."
    echo " Deleting the branch affects them. Runs are matched by SHA, so theirs are left alone."
fi
if printf '%s\n' "${runs[@]+"${runs[@]}"}" | awk -F'\t' '$3!="completed"' | grep -q .; then
    echo
    echo " Note: some runs are still in progress. They'll be cancelled before they're deleted."
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

echo
echo "1. Title, body, state"
step "edit and close PR" api -X PATCH "repos/${REPO}/pulls/${PR}" \
    -f title="${REPLACEMENT%.}" -f body="${REPLACEMENT}" -f state=closed

echo "2. Review comments"
for row in "${review_comments[@]}"; do
    id=${row%%$'\t'*}
    step "review comment ${id}" api -X DELETE "repos/${REPO}/pulls/comments/${id}"
done

echo "3. Conversation comments"
for row in "${issue_comments[@]}"; do
    id=${row%%$'\t'*}
    step "comment ${id}" api -X DELETE "repos/${REPO}/issues/comments/${id}"
done

echo "4. Review bodies"
for row in "${reviews[@]}"; do
    id=${row%%$'\t'*}
    step "review ${id}" api -X PUT "repos/${REPO}/pulls/${PR}/reviews/${id}" -f body="${REPLACEMENT}"
done

echo "5. Workflow runs"
for row in "${runs[@]}"; do
    IFS=$'\t' read -r id name status _ <<<"$row"
    if [[ "$status" != "completed" ]]; then
        api -X POST "repos/${REPO}/actions/runs/${id}/force-cancel" >/dev/null 2>&1
        for _ in 1 2 3 4 5 6; do
            [[ "$(api "repos/${REPO}/actions/runs/${id}" --jq .status 2>/dev/null)" == "completed" ]] && break
            sleep 5
        done
    fi
    step "run ${id} (${name})" api -X DELETE "repos/${REPO}/actions/runs/${id}"
done

echo "6. Deployments"
for row in "${deployments[@]}"; do
    id=${row%%$'\t'*}
    api -X POST "repos/${REPO}/deployments/${id}/statuses" -f state=inactive >/dev/null 2>&1
    step "deployment ${id}" api -X DELETE "repos/${REPO}/deployments/${id}"
done

echo "7. Head branch"
if (( branch_exists )); then
    step "branch ${head_ref}" api -X DELETE "repos/${REPO}/git/refs/heads/${head_ref}"
else
    echo "  skip  nothing to delete"
fi

request_file="scrub-pr-${PR}-github-support.md"
{
    echo "Subject: Request to delete PR ${REPO}#${PR} and purge its refs, commits, and edit history"
    echo
    echo "Hi,"
    echo
    echo "A pull request in ${REPO} was opened by mistake and exposes information that must not be public. We need it removed entirely."
    echo
    echo "- Pull request: https://github.com/${REPO}/pull/${PR}"
    echo "- Head branch: ${head_ref} (deleted)"
    echo "- Refs still present: refs/pull/${PR}/head, refs/pull/${PR}/merge"
    echo "- Commits only reachable through those refs:"
    for sha in "${shas[@]}"; do echo "  - ${sha}"; done
    echo
    echo "We have closed the PR, replaced its title and description, deleted its comments, workflow runs, and deployments, and deleted the head branch."
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
cat <<EOF

 Still there, and only GitHub Support can remove it:
   - The PR itself and the edit history of its title, body, comments, and reviews
   - refs/pull/${PR}/head and /merge, and the ${#shas[@]} commit(s) they point to
   - Commit statuses and check runs on those commits

 Request text written to ./${request_file}
 File it at https://support.github.com/contact (signed in as an org owner).

 Outside GitHub, check: preview builds (the docs repo's pr-closed workflow deletes
 the PR's S3 preview buckets), Slack notifications, and any issues or PRs that
 link to this one.
================================================================
EOF
