#!/usr/bin/env bash
#
# Tests for scripts/scrub-pr.sh, run against a stub `gh` instead of GitHub.
#
# The stub serves a fixture PR from a JSON state file, applies the script's writes to
# that state (deletes, edits, cancels), and logs every call. The tests then assert on
# which writes happened. They pin the guarantees that matter for a destructive script:
# a dry run or a wrong confirmation writes nothing, runs from other PRs survive, the
# default branch is never deleted, and the sweeps catch what closing the PR sets off.
#
# Usage: scripts/scrub-pr.test.sh    (needs bash 4+ and jq)

set -uo pipefail

SCRIPT="$(cd "$(dirname "$0")" && pwd)/scrub-pr.sh"
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

mkdir -p "$WORK/bin"
cat > "$WORK/bin/gh" <<'STUB'
#!/usr/bin/env bash
# Minimal stand-in for `gh api` over a fixture state file ($STUB_STATE).
set -uo pipefail
if [[ "${1:-} ${2:-}" == "auth status" ]]; then exit 0; fi
[[ "${1:-}" == "api" ]] || { echo "stub gh: unsupported: $*" >&2; exit 1; }
shift

method=GET jq_expr="" endpoint="" fields=()
while (( $# )); do
    case "$1" in
        -H) shift 2 ;;
        -X) method=$2; shift 2 ;;
        --jq) jq_expr=$2; shift 2 ;;
        --paginate) shift ;;
        -f|-F) fields+=("$2"); shift 2 ;;
        *) endpoint=$1; shift ;;
    esac
done
echo "${method} ${endpoint}" >> "$STUB_CALLS"

path=${endpoint%%\?*}
query=""; [[ "$endpoint" == *\?* ]] && query=${endpoint#*\?}
param() {  # value of a query-string or -f/-F parameter
    local kv
    for kv in ${query//&/ } "${fields[@]+"${fields[@]}"}"; do
        [[ "${kv%%=*}" == "$1" ]] && { printf '%s' "${kv#*=}"; return; }
    done
}
field_json() {  # -f/-F fields as a JSON object
    local kv out='{}'
    for kv in "${fields[@]+"${fields[@]}"}"; do
        out=$(jq -c --arg k "${kv%%=*}" --arg v "${kv#*=}" '. + {($k): $v}' <<<"$out")
    done
    printf '%s' "$out"
}
update() { jq "$@" "$STUB_STATE" > "$STUB_STATE.tmp" && mv "$STUB_STATE.tmp" "$STUB_STATE"; }
q() { jq "$@" "$STUB_STATE"; }

repo=$(q -r .repo)
r="repos/${repo}"
pr=$(q -r .pr.number)

if [[ "$method" != "GET" ]]; then
    case "$method $path" in
        "PATCH $r/pulls/$pr")
            update --argjson f "$(field_json)" '.pr += $f | .issue_comments += .on_close.comments | .runs += .on_close.runs' ;;
        "DELETE $r/issues/comments/"*)  update --argjson id "${path##*/}" '.issue_comments |= map(select(.id != $id))' ;;
        "DELETE $r/pulls/comments/"*)   update --argjson id "${path##*/}" '.review_comments |= map(select(.id != $id))' ;;
        "PUT $r/pulls/$pr/reviews/"*)   update --argjson id "${path##*/}" --arg b "$(param body)" '.reviews |= map(if .id == $id then .body = $b else . end)' ;;
        "POST $r/actions/runs/"*/force-cancel)
            id=${path%/force-cancel}; id=${id##*/}
            update --argjson id "$id" '.runs |= map(if .id == $id then .status = "completed" else . end)' ;;
        "DELETE $r/actions/runs/"*)     update --argjson id "${path##*/}" '.runs |= map(select(.id != $id))' ;;
        "POST $r/deployments/"*/statuses) ;;
        "DELETE $r/deployments/"*)      update --argjson id "${path##*/}" '.deployments |= map(select(.id != $id))' ;;
        "DELETE $r/git/refs/heads/"*)   update --arg b "${path#"$r/git/refs/heads/"}" 'del(.branches[$b])' ;;
        *) echo "stub gh: unexpected write: $method $path" >&2; exit 1 ;;
    esac
    echo '{}'
    exit 0
fi

case "$path" in
    user)                       body='{"login":"tester"}' ;;
    "$r")                       body=$(q '{default_branch}') ;;
    "$r/pulls/$pr")             body=$(q .pr) ;;
    "$r/pulls/$pr/commits")     body=$(q '.commits | map({sha: .})') ;;
    "$r/issues/$pr/events")     body=$(q .events) ;;
    "$r/pulls")                 body=$(q --arg h "$(param head)" '[.other_prs[] | select("\(.owner):\(.ref)" == $h)]') ;;
    "$r/issues/$pr/comments")   body=$(q .issue_comments) ;;
    "$r/pulls/$pr/comments")    body=$(q .review_comments) ;;
    "$r/pulls/$pr/reviews")     body=$(q .reviews) ;;
    "$r/actions/runs/"*)        body=$(q --argjson id "${path##*/}" '.runs[] | select(.id == $id)') ;;
    "$r/actions/runs")
        body=$(q --arg sha "$(param head_sha)" --arg ev "$(param event)" --arg since "$(param created)" '
            {workflow_runs: [.runs[]
                | select($sha == "" or .head_sha == $sha)
                | select($ev == "" or .event == $ev)
                | select($since == "" or .created_at >= ($since | ltrimstr(">=")))]}') ;;
    "$r/deployments")
        body=$(q --arg sha "$(param sha)" --arg ref "$(param ref)" '
            [.deployments[] | select(($sha != "" and .sha == $sha) or ($ref != "" and .ref == $ref))]') ;;
    "$r/git/ref/heads/"*)
        b=${path#"$r/git/ref/heads/"}
        [[ "$(q --arg b "$b" '.branches | has($b)')" == "true" ]] || { echo '{"message":"Not Found"}'; exit 1; }
        body='{}' ;;
    "$r/branches/"*)            body=$(q --arg b "${path#"$r/branches/"}" '{protected: (.branches[$b].protected // false)}') ;;
    *) echo "stub gh: unexpected read: $path" >&2; exit 1 ;;
esac

if [[ -n "$jq_expr" ]]; then jq -r "$jq_expr" <<<"$body"; else printf '%s\n' "$body"; fi
STUB
chmod +x "$WORK/bin/gh"

# A PR opened at 10:00 from branch "leak" with two commits, renamed once. The runs cover
# every way the script matches (or must not match) a run.
fixture() {
    cat <<'JSON'
{
  "repo": "acme/site",
  "default_branch": "master",
  "pr": {
    "number": 42, "title": "Leaky title", "state": "open", "merged": false,
    "user": {"login": "someone"}, "created_at": "2026-01-01T10:00:00Z",
    "merge_commit_sha": "m3rge", "body": "secret stuff",
    "head": {"ref": "leak", "repo": {"full_name": "acme/site"}}
  },
  "commits": ["c0mmit1", "c0mmit2"],
  "events": [{"event": "renamed", "rename": {"from": "Original leaky title", "to": "Leaky title"}}],
  "other_prs": [{"number": 42, "owner": "acme", "ref": "leak"}],
  "issue_comments": [{"id": 101, "user": {"login": "bot"}}],
  "review_comments": [{"id": 201, "user": {"login": "reviewer"}}],
  "reviews": [
    {"id": 301, "user": {"login": "reviewer"}, "state": "COMMENTED", "body": "quotes the secret"},
    {"id": 302, "user": {"login": "reviewer"}, "state": "APPROVED", "body": ""}
  ],
  "runs": [
    {"id": 1, "name": "build", "status": "completed", "event": "pull_request", "head_sha": "c0mmit1",
     "display_title": "Leaky title", "created_at": "2026-01-01T10:01:00Z", "pull_requests": []},
    {"id": 2, "name": "preview", "status": "in_progress", "event": "pull_request", "head_sha": "c0mmit2",
     "display_title": "Leaky title", "created_at": "2026-01-01T10:05:00Z", "pull_requests": []},
    {"id": 3, "name": "claude", "status": "completed", "event": "issue_comment", "head_sha": "mastertip",
     "display_title": "Original leaky title", "created_at": "2026-01-01T10:02:00Z", "pull_requests": []},
    {"id": 4, "name": "claude", "status": "completed", "event": "issue_comment", "head_sha": "mastertip",
     "display_title": "Some other PR", "created_at": "2026-01-01T10:03:00Z", "pull_requests": []},
    {"id": 5, "name": "claude", "status": "completed", "event": "issue_comment", "head_sha": "mastertip",
     "display_title": "Leaky title", "created_at": "2025-12-31T09:00:00Z", "pull_requests": []},
    {"id": 6, "name": "review", "status": "completed", "event": "pull_request_review", "head_sha": "mastertip",
     "display_title": "Unrelated", "created_at": "2026-01-01T10:04:00Z", "pull_requests": [{"number": 42}]}
  ],
  "deployments": [
    {"id": 901, "environment": "testing", "sha": "c0mmit1", "ref": "leak"},
    {"id": 902, "environment": "production", "sha": "other", "ref": "leak"},
    {"id": 903, "environment": "production", "sha": "unrelated", "ref": "master"}
  ],
  "branches": {"leak": {"protected": false}, "master": {"protected": true}},
  "on_close": {
    "comments": [{"id": 102, "user": {"login": "bot"}}],
    "runs": [{"id": 7, "name": "pr-closed", "status": "completed", "event": "pull_request", "head_sha": "c0mmit2",
              "display_title": "Closed, created in error", "created_at": "2099-01-01T00:00:00Z", "pull_requests": []}]
  }
}
JSON
}

failures=0
case_name=""
OUT="" STATUS=0

# run_case <name> <jq to tweak the fixture> <stdin> <script args...>
run_case() {
    case_name=$1; local tweak=$2 input=$3; shift 3
    export STUB_STATE="$WORK/state.json" STUB_CALLS="$WORK/calls.log"
    fixture | jq "$tweak" > "$STUB_STATE"
    : > "$STUB_CALLS"
    OUT=$(cd "$WORK" && printf '%s' "$input" | PATH="$WORK/bin:$PATH" SCRUB_SWEEP_DELAY=0 bash "$SCRIPT" "$@" --repo acme/site 2>&1)
    STATUS=$?
}
fail() { echo "FAIL [$case_name] $*"; failures=$((failures + 1)); }
writes() { grep -v '^GET ' "$STUB_CALLS"; }
expect_status() { (( STATUS == $1 )) || fail "exit $STATUS, want $1"$'\n'"$OUT"; }
expect_out() { grep -qF -- "$1" <<<"$OUT" || fail "output lacks: $1"; }
expect_write() { writes | grep -qxF -- "$1" || fail "missing write: $1"; }
expect_no_write() { ! writes | grep -qF -- "$1" || fail "unexpected write: $(writes | grep -F -- "$1" | head -1)"; }
expect_no_writes() { [[ -z "$(writes)" ]] || fail "wrote in a no-write case: $(writes | head -3 | tr '\n' ';')"; }
state() { jq -r "$1" "$STUB_STATE"; }

# --- a dry run reads only, and its plan counts the right things ---
run_case "dry run" '.' '' 42 --dry-run
expect_status 0
expect_no_writes
expect_out "Dry run: nothing changed."
expect_out "1. Cancel 1 in-progress workflow run(s)"
expect_out "Delete 1 review comment(s) and 1 conversation comment(s)"
expect_out "Replace the body of 1 review(s)"
expect_out "5. Delete 4 workflow run(s)"
expect_out "6. Delete 2 deployment(s)"
expect_out "7. Delete branch leak"
expect_out "Original leaky title"

# --- anything but the PR number aborts before the first write ---
run_case "wrong confirmation" '.' $'43\n' 42
expect_status 1
expect_no_writes
expect_out "Aborted. Nothing changed."

# --- the full scrub ---
run_case "full scrub" '.' $'42\n' 42
expect_status 0
expect_out "Done. 0 step(s) failed."
expect_write "POST repos/acme/site/actions/runs/2/force-cancel"
expect_write "PATCH repos/acme/site/pulls/42"
[[ "$(state '.pr.title + "|" + .pr.state + "|" + .pr.body')" == "Closed, created in error|closed|Closed, created in error." ]] \
    || fail "PR not neutralized: $(state '.pr | [.title, .state, .body] | join("|")')"
expect_write "DELETE repos/acme/site/issues/comments/101"
expect_write "DELETE repos/acme/site/pulls/comments/201"
expect_write "PUT repos/acme/site/pulls/42/reviews/301"
expect_no_write "reviews/302"
for id in 1 2 3 6; do expect_write "DELETE repos/acme/site/actions/runs/${id}"; done
expect_no_write "actions/runs/4"   # another PR's title
expect_no_write "actions/runs/5"   # same title, but from before the PR opened
expect_write "DELETE repos/acme/site/deployments/901"
expect_write "DELETE repos/acme/site/deployments/902"
expect_no_write "deployments/903"
expect_write "DELETE repos/acme/site/git/refs/heads/leak"
# Closing the PR posted a comment and started a run; the sweeps must catch both.
expect_write "DELETE repos/acme/site/issues/comments/102"
expect_write "DELETE repos/acme/site/actions/runs/7"
[[ "$(state '[.runs[].id] | sort | join(",")')" == "4,5" ]] || fail "runs left: $(state '[.runs[].id] | join(",")')"
[[ -f "$WORK/scrub-pr-42-github-support.md" ]] || fail "no support request written"

# --- the default branch is never deleted, even with --force-branch ---
run_case "default branch" '.pr.head.ref = "master" | .other_prs = []' $'42\n' 42 --force-branch
expect_status 0
expect_out "Keep branch master: it's the default branch"
expect_no_write "git/refs/heads"

# --- a branch another PR uses is kept unless forced ---
shared='.other_prs += [{"number": 41, "owner": "acme", "ref": "leak"}]'
run_case "shared branch" "$shared" $'42\n' 42
expect_out "Keep branch leak: other PRs use it (41)"
expect_no_write "git/refs/heads"
expect_no_write "deployments/902"   # matched only by branch name, which 41 shares
run_case "shared branch, forced" "$shared" $'42\n' 42 --force-branch
expect_write "DELETE repos/acme/site/git/refs/heads/leak"

# --- a protected branch is kept unless forced ---
run_case "protected branch" '.branches.leak.protected = true' '' 42 --dry-run
expect_out "Keep branch leak: it's protected (--force-branch deletes it)"

# --- a fork's branch isn't ours to delete ---
run_case "fork" '.pr.head.repo.full_name = "fork/site"' '' 42 --dry-run
expect_out "Head branch: nothing to delete"

if (( failures )); then
    echo "${failures} check(s) failed."
    exit 1
fi
echo "All scrub-pr.sh tests passed."
