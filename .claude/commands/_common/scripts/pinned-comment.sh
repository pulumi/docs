#!/usr/bin/env bash
# pinned-comment.sh — manage a single logical Claude review on a PR as one
# or more GitHub comments tagged with `<!-- CLAUDE_REVIEW N/M -->` markers.
#
# Subcommands:
#   find          --pr <N>                           List pinned comment IDs in marker order.
#   fetch         --pr <N>                           Print the full body of every pinned comment, in order, separated by markers.
#   upsert        --pr <N> --body-file <path>        Split body, edit existing comments in place, append new, prune tail.
#   prune         --pr <N> --keep <count>            Delete tail-end pinned comments past <count>.
#   last-reviewed-sha --pr <N>                       Print the most recent SHA from the 1/M comment's review history.
#
# Common flags:
#   --repo <owner/repo>   Override repository (default: $GH_REPO, $GITHUB_REPOSITORY, or `gh repo view`).
#   --max-bytes <N>       Maximum body size per comment (default: 60000; GitHub hard cap is 65536).
#   --dry-run             Print intended API calls; do not mutate.
#
# Marker convention: every managed comment starts with a single line
#   <!-- CLAUDE_REVIEW N/M -->
# where N is 1-indexed and M is the total comment count in the sequence.
#
# Hard rule: the 1/M comment is sacrosanct. This script will NEVER delete it
# while a sequence is being managed in place. Tail-end deletes are fine.

set -euo pipefail

MARKER_RE='^<!-- CLAUDE_REVIEW ([0-9]+)/([0-9]+) -->'
DEFAULT_MAX_BYTES=60000

usage() {
    sed -n '2,18p' "$0" | sed 's/^# \{0,1\}//' >&2
    exit 2
}

die() {
    printf 'pinned-comment.sh: %s\n' "$1" >&2
    exit 1
}

require_cmd() {
    command -v "$1" >/dev/null 2>&1 || die "missing required command: $1"
}

resolve_repo() {
    if [[ -n "${REPO_FLAG:-}" ]]; then
        printf '%s' "$REPO_FLAG"
    elif [[ -n "${GH_REPO:-}" ]]; then
        printf '%s' "$GH_REPO"
    elif [[ -n "${GITHUB_REPOSITORY:-}" ]]; then
        printf '%s' "$GITHUB_REPOSITORY"
    else
        gh repo view --json nameWithOwner -q .nameWithOwner
    fi
}

# list_pinned_comments <repo> <pr>
# Emits TSV: comment_id<TAB>position<TAB>total<TAB>created_at
# Sorted by position ascending.
list_pinned_comments() {
    local repo="$1" pr="$2"
    # jq does the parsing: extract the leading line of each body, capture
    # the N/M marker, and emit only matching comments. Avoids relying on
    # gawk-specific match() captures.
    # Note: no regex flags on `capture`. Not every jq build ships with
    # extended-mode (`x`) support, and the GitHub Actions runner's jq
    # errors with "unsupported regular expression flag: x" -- caught
    # during fork-based re-entrant testing. The pattern has no
    # extended-mode features to preserve, so the flag is unneeded.
    gh api --paginate "repos/$repo/issues/$pr/comments" --jq '
        .[]
        | . as $c
        | (.body | split("\n") | .[0]) as $line1
        | ($line1 | capture("^<!-- CLAUDE_REVIEW (?<n>[0-9]+)/(?<m>[0-9]+) -->")? // empty)
        | [$c.id, .n, .m, $c.created_at] | @tsv
    ' | sort -t$'\t' -k2,2n
}

# fetch_pinned_bodies <repo> <pr>
# Emits the full bodies, one after another, separated by a delimiter line.
fetch_pinned_bodies() {
    local repo="$1" pr="$2"
    local ids
    ids=$(list_pinned_comments "$repo" "$pr" | cut -f1)
    if [[ -z "$ids" ]]; then
        return 0
    fi
    local first=1
    while IFS= read -r id; do
        [[ -z "$id" ]] && continue
        if (( first )); then
            first=0
        else
            printf '\n----- PINNED-COMMENT-DELIMITER -----\n'
        fi
        gh api "repos/$repo/issues/comments/$id" --jq '.body'
    done <<< "$ids"
}

# split_body <body_file> <max_bytes>
# Writes split pages to a temp dir; prints the temp dir path on stdout.
# Each page is a file named page-001, page-002, ...
split_body() {
    local body_file="$1" max_bytes="$2"
    local tmpdir
    tmpdir=$(mktemp -d)

    # We split at line boundaries only. Algorithm:
    # - Walk the input lines, accumulating into the current page.
    # - When adding the next line would exceed max_bytes, finalize the page
    #   and start a new one with that line.
    # - Prefer splitting at `### ` heading boundaries when within the last
    #   25% of the budget, but never required (size always wins).
    awk -v max="$max_bytes" -v outdir="$tmpdir" '
        function flush() {
            if (length(buf) == 0) return
            page++
            fname = sprintf("%s/page-%03d", outdir, page)
            printf "%s", buf > fname
            close(fname)
            buf = ""
            cur = 0
        }
        BEGIN { page = 0; buf = ""; cur = 0; soft = int(max * 0.75) }
        {
            line = $0 "\n"
            llen = length(line)
            if (cur + llen > max && cur > 0) {
                flush()
            } else if (cur > soft && llen > 0 && substr($0, 1, 4) == "### ") {
                # Soft-split at section boundaries when over 75% of budget.
                flush()
            }
            buf = buf line
            cur += llen
        }
        END { flush() }
    ' "$body_file"

    printf '%s' "$tmpdir"
}

# render_with_markers <pages_dir> <total>
# Reads page-NNN files, prepends the CLAUDE_REVIEW N/M marker, writes back.
render_with_markers() {
    local pages_dir="$1" total="$2"
    local i=0
    for page in "$pages_dir"/page-*; do
        i=$((i + 1))
        local marker="<!-- CLAUDE_REVIEW $i/$total -->"
        local tmp
        tmp=$(mktemp)
        printf '%s\n' "$marker" >"$tmp"
        cat "$page" >>"$tmp"
        mv "$tmp" "$page"
    done
}

# patch_comment <repo> <comment_id> <body_file>
patch_comment() {
    local repo="$1" id="$2" body_file="$3"
    if (( DRY_RUN )); then
        printf '[dry-run] PATCH repos/%s/issues/comments/%s (%d bytes)\n' \
            "$repo" "$id" "$(wc -c <"$body_file")" >&2
        return 0
    fi
    gh api -X PATCH "repos/$repo/issues/comments/$id" \
        --field "body=@$body_file" >/dev/null
}

# create_comment <repo> <pr> <body_file>
create_comment() {
    local repo="$1" pr="$2" body_file="$3"
    if (( DRY_RUN )); then
        printf '[dry-run] POST repos/%s/issues/%s/comments (%d bytes)\n' \
            "$repo" "$pr" "$(wc -c <"$body_file")" >&2
        return 0
    fi
    gh api -X POST "repos/$repo/issues/$pr/comments" \
        --field "body=@$body_file" >/dev/null
}

# delete_comment <repo> <comment_id>
delete_comment() {
    local repo="$1" id="$2"
    if (( DRY_RUN )); then
        printf '[dry-run] DELETE repos/%s/issues/comments/%s\n' "$repo" "$id" >&2
        return 0
    fi
    gh api -X DELETE "repos/$repo/issues/comments/$id" >/dev/null
}

cmd_find() {
    local repo pr
    repo=$(resolve_repo)
    pr="${PR:?--pr required}"
    list_pinned_comments "$repo" "$pr" | cut -f1
}

cmd_fetch() {
    local repo pr
    repo=$(resolve_repo)
    pr="${PR:?--pr required}"
    fetch_pinned_bodies "$repo" "$pr"
}

cmd_upsert() {
    local repo pr body_file
    repo=$(resolve_repo)
    pr="${PR:?--pr required}"
    body_file="${BODY_FILE:?--body-file required}"
    [[ -r "$body_file" ]] || die "body file not readable: $body_file"

    local pages_dir
    pages_dir=$(split_body "$body_file" "$MAX_BYTES")
    local pages
    pages=( "$pages_dir"/page-* )
    local total=${#pages[@]}
    (( total > 0 )) || die "split produced no pages (empty input?)"
    render_with_markers "$pages_dir" "$total"

    # Re-glob after marker prepend.
    pages=( "$pages_dir"/page-* )

    local existing_tsv
    existing_tsv=$(list_pinned_comments "$repo" "$pr" || true)
    local existing_ids=()
    if [[ -n "$existing_tsv" ]]; then
        while IFS=$'\t' read -r id _pos _tot _created; do
            existing_ids+=("$id")
        done <<< "$existing_tsv"
    fi

    local existing_count=${#existing_ids[@]}
    local i
    for (( i = 0; i < total; i++ )); do
        local page="${pages[$i]}"
        if (( i < existing_count )); then
            patch_comment "$repo" "${existing_ids[$i]}" "$page"
        else
            create_comment "$repo" "$pr" "$page"
        fi
    done

    # Prune surplus tail comments. Skip index 0 always (1/M is sacrosanct).
    if (( existing_count > total )); then
        for (( i = total; i < existing_count; i++ )); do
            if (( i == 0 )); then
                printf 'pinned-comment.sh: refusing to delete 1/M (sacrosanct)\n' >&2
                continue
            fi
            delete_comment "$repo" "${existing_ids[$i]}"
        done
    fi

    rm -rf "$pages_dir"
}

cmd_prune() {
    local repo pr keep
    repo=$(resolve_repo)
    pr="${PR:?--pr required}"
    keep="${KEEP:?--keep required}"

    local existing_tsv
    existing_tsv=$(list_pinned_comments "$repo" "$pr" || true)
    [[ -z "$existing_tsv" ]] && return 0

    local i=0
    while IFS=$'\t' read -r id _pos _tot _created; do
        if (( i >= keep )); then
            if (( i == 0 )); then
                printf 'pinned-comment.sh: refusing to delete 1/M (sacrosanct)\n' >&2
            else
                delete_comment "$repo" "$id"
            fi
        fi
        i=$((i + 1))
    done <<< "$existing_tsv"
}

cmd_last_reviewed_sha() {
    local repo pr first_id
    repo=$(resolve_repo)
    pr="${PR:?--pr required}"
    first_id=$(list_pinned_comments "$repo" "$pr" | head -1 | cut -f1)
    [[ -z "$first_id" ]] && return 0
    # Read the body and pull out the last (sha) parenthetical inside the
    # `### 📜 Review history` section. Awk segments by section; grep + sed
    # extract the SHA portably without gawk-specific match() captures.
    gh api "repos/$repo/issues/comments/$first_id" --jq '.body' \
        | awk '
            /^### .*Review history/ { in_hist = 1; next }
            in_hist && /^### / { in_hist = 0 }
            in_hist { print }
        ' \
        | grep -oE '\([0-9a-f]{7,40}\)' \
        | tail -1 \
        | tr -d '()'
}

# Argument parsing.
[[ $# -ge 1 ]] || usage
SUBCOMMAND="$1"; shift

PR=""
BODY_FILE=""
KEEP=""
REPO_FLAG=""
MAX_BYTES=$DEFAULT_MAX_BYTES
DRY_RUN=0

while [[ $# -gt 0 ]]; do
    case "$1" in
        --pr)         PR="$2"; shift 2 ;;
        --body-file)  BODY_FILE="$2"; shift 2 ;;
        --keep)       KEEP="$2"; shift 2 ;;
        --repo)       REPO_FLAG="$2"; shift 2 ;;
        --max-bytes)  MAX_BYTES="$2"; shift 2 ;;
        --dry-run)    DRY_RUN=1; shift ;;
        -h|--help)    usage ;;
        *)            die "unknown flag: $1" ;;
    esac
done

require_cmd gh
require_cmd jq
require_cmd awk

case "$SUBCOMMAND" in
    find)              cmd_find ;;
    fetch)             cmd_fetch ;;
    upsert)            cmd_upsert ;;
    prune)             cmd_prune ;;
    last-reviewed-sha) cmd_last_reviewed_sha ;;
    *)                 usage ;;
esac
