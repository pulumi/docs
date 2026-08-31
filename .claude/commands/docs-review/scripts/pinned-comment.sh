#!/usr/bin/env bash
# pinned-comment.sh — manage a single logical Claude review on a PR as one
# or more GitHub comments tagged with `<!-- CLAUDE_REVIEW N/M -->` markers.
#
# Subcommands:
#   find             --pr <N> [--role author|brief]     List pinned comment IDs in marker order; with --role, that one comment's ID.
#   fetch            --pr <N>                           Print the full body of every pinned comment, in order, separated by markers.
#   upsert           --pr <N> --body-file <path> [--soft-floor]   Split body, edit existing comments in place, append new, prune tail. With --soft-floor: re-run validate-pinned.py --soft-floor first (emits the `soft-floor`-labeled CI annotation surfacing residual violations to the maintainer), then publish regardless — the documented second-failure fallback per ci.md §4.
#   upsert           --pr <N> --body-file <path> --role author|brief   v3 surface: upsert the single role-marked card verbatim (no split, no footer restamp, no spine floor). Oversized input is an error, never a pagination event.
#   prune            --pr <N> --keep <count>            Delete tail-end pinned comments past <count>.
#   clear            --pr <N>                           Delete ALL pinned comments (1/M, tail, and v3 role cards). Bypasses the 1/M-sacrosanct rule. For explicit regenerate-from-scratch flows only.
#   last-reviewed-sha --pr <N>                          Print the current reviewed SHA: the CLAUDE_REVIEW_HEAD marker when present (same precedence as review-label-reconcile.yml), else the last (sha) in the 1/M comment's review history.
#
# Common flags:
#   --repo <owner/repo>   Override repository (default: $GH_REPO, $GITHUB_REPOSITORY, or `gh repo view`).
#   --max-bytes <N>       Maximum body size per comment (default: 60000; GitHub hard cap is 65536).
#   --dry-run             Print intended API calls; do not mutate.
#
# Marker convention: every managed comment starts with a single line
#   <!-- CLAUDE_REVIEW N/M -->
# where N is 1-indexed and M is the total comment count in the sequence.
# v3 role cards additionally carry <!-- CLAUDE_REVIEW_AUTHOR --> or
# <!-- CLAUDE_REVIEW_BRIEF --> within their first three lines; the author card
# keeps a legacy `1/1` first line so every v2 consumer still finds it.
#
# Hard rule: the 1/M comment is sacrosanct. This script will NEVER delete it
# while a sequence is being managed in place. Tail-end deletes are fine.

set -euo pipefail

MARKER_RE='^<!-- CLAUDE_REVIEW ([0-9]+)/([0-9]+) -->'
DEFAULT_MAX_BYTES=60000

# The review footer (refresh instructions + the don't-hide-me warning) lives in
# one place, `docs-review/footer.md`, and this script is its authoritative
# writer: split_body strips any inbound copy and every page gets a freshly
# stamped one. Two reasons it can't just ride along in the composed body:
#   1. On a split review the composed footer lands on the LAST page only --
#      i.e. comment 3/3 -- while the comment everyone actually reads is 1/3.
#   2. The re-entrant path re-renders the whole body through the model, which
#      can silently drop it. Stamping here makes that unlosable.
# compose-review.py renders the same file so drafts stay complete documents;
# keep FOOTER_SENTINEL in sync with its copy of the constant.
FOOTER_SENTINEL='<!-- CLAUDE_REVIEW_FOOTER -->'
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
FOOTER_FILE="$SCRIPT_DIR/../footer.md"

# v3 role-card markers. A card is identified by its role marker appearing as
# an exact line within the FIRST THREE lines of the body — first-lines-only for
# the same reason list_pinned_comments reads only line 1: a GitHub quote-reply
# copies HTML comments verbatim but prefixes every line with `> `, so requiring
# an unprefixed match near the top keeps quoted copies from matching.
AUTHOR_MARKER='<!-- CLAUDE_REVIEW_AUTHOR -->'
BRIEF_MARKER='<!-- CLAUDE_REVIEW_BRIEF -->'
LEGACY_ALIAS_RE='^<!-- CLAUDE_REVIEW 1/1 -->[[:space:]]*$'
HEAD_MARKER_GREP='<!-- CLAUDE_REVIEW_HEAD [0-9a-f]{7,40} -->'

usage() {
    sed -n '2,24p' "$0" | sed 's/^# \{0,1\}//' >&2
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

# load_footer
# Print the canonical footer text (no trailing newline handling; callers add).
# Missing/unreadable file is non-fatal: publish an un-footered review rather
# than block the pipeline on a missing doc fragment.
load_footer() {
    if [[ -r "$FOOTER_FILE" ]]; then
        cat "$FOOTER_FILE"
    else
        printf 'pinned-comment.sh: WARNING: footer file not readable (%s); publishing without a footer\n' \
            "$FOOTER_FILE" >&2
    fi
}

# list_pinned_comments <repo> <pr>
# Emits TSV: comment_id<TAB>position<TAB>total<TAB>created_at<TAB>node_id
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
        | [$c.id, .n, .m, $c.created_at, $c.node_id] | @tsv
    ' | sort -t$'\t' -k2,2n
}

# role_marker <role>
role_marker() {
    case "$1" in
        author) printf '%s' "$AUTHOR_MARKER" ;;
        brief)  printf '%s' "$BRIEF_MARKER" ;;
        *)      die "unknown role: $1 (expected author or brief)" ;;
    esac
}

# list_role_comments <repo> <pr> <marker>
# Emits TSV: comment_id<TAB>created_at<TAB>node_id, oldest first. Matches the
# marker as an exact line among the body's first three lines (see the marker
# constants above for why not the whole body).
list_role_comments() {
    local repo="$1" pr="$2" marker="$3"
    gh api --paginate "repos/$repo/issues/$pr/comments" --jq "
        .[]
        | . as \$c
        | (.body | split(\"\n\"))[:3] as \$head
        | select(\$head | index(\"${marker}\"))
        | [\$c.id, \$c.created_at, \$c.node_id] | @tsv
    " | sort -t$'\t' -k2,2
}

# find_role_comment <repo> <pr> <role>
# Prints the single role comment's TSV row (oldest wins), warning when a bug
# has left more than one — the oldest is the one every prior PATCH targeted.
find_role_comment() {
    local repo="$1" pr="$2" role="$3"
    local marker rows count
    marker=$(role_marker "$role")
    rows=$(list_role_comments "$repo" "$pr" "$marker" || true)
    [[ -z "$rows" ]] && return 0
    count=$(printf '%s\n' "$rows" | wc -l)
    if (( count > 1 )); then
        printf 'pinned-comment.sh: WARNING: %d %s cards found; using the oldest\n' \
            "$count" "$role" >&2
    fi
    printf '%s\n' "$rows" | head -1
}

# unminimize_if_hidden <node_id>
# GitHub lets anyone with write access hide a comment (Hide -> Resolved), which
# collapses it in the UI. The REST list endpoint still returns it, body intact,
# so upsert would happily PATCH a comment nobody can see: the refresh job runs
# green, posts its progress comment, and the updated review is invisible. That
# is exactly what happened on pulumi/docs#20533 -- an `#update-review` reported
# success at 14:12 and the PR showed nothing until a `#new-review` six hours
# later. Unhide before patching so the update lands somewhere visible.
#
# Non-fatal on failure: unminimizeComment can be refused by the token's scopes,
# and a visible-but-stale review still beats no review at all. We warn loudly
# instead, so the operator sees why the refresh looked like a no-op.
unminimize_if_hidden() {
    local node_id="$1"
    [[ -z "$node_id" || "$node_id" == "null" ]] && return 0

    local minimized
    minimized=$(gh api graphql -f query='
        query($id: ID!) {
          node(id: $id) { ... on IssueComment { isMinimized } }
        }' -f id="$node_id" --jq '.data.node.isMinimized' 2>/dev/null || true)

    [[ "$minimized" != "true" ]] && return 0

    if (( DRY_RUN )); then
        printf '[dry-run] unminimizeComment %s\n' "$node_id" >&2
        return 0
    fi

    if gh api graphql -f query='
        mutation($id: ID!) {
          unminimizeComment(input: {subjectId: $id}) { clientMutationId }
        }' -f id="$node_id" >/dev/null 2>&1; then
        printf 'pinned-comment.sh: unhid minimized pinned comment %s before patching\n' "$node_id" >&2
    else
        printf 'pinned-comment.sh: WARNING: pinned comment %s is hidden and could not be unhidden; this update will not be visible on the PR\n' \
            "$node_id" >&2
    fi
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
    # - Strip any inbound <!-- CLAUDE_REVIEW N/M --> marker lines first. This
    #   script is the sole writer of markers; re-entrant callers sometimes
    #   echo the previous pinned body (marker included) into the upsert
    #   input, and without this filter render_with_markers would prepend a
    #   second marker on top of the stale one.
    # - Strip the footer the same way, for the same reason: everything from
    #   the CLAUDE_REVIEW_FOOTER sentinel to EOF is dropped and re-stamped per
    #   page by append_footer. The footer is by contract the LAST block of the
    #   body (output-format.md), so sentinel-to-EOF is the whole of it.
    # - Walk the remaining lines, accumulating into the current page.
    # - When adding the next line would exceed max_bytes, finalize the page
    #   and start a new one with that line.
    # - Prefer splitting at `### ` heading boundaries when within the last
    #   25% of the budget, but never required (size always wins).
    # - Track open `<details>` blocks. If a flush happens inside one, close
    #   the block at the end of the page and re-open a continuation
    #   `<details>` at the start of the next so the spilled list stays
    #   visually collapsed (otherwise the trailing items render as a naked
    #   bulleted list under the next H3 heading).
    awk -v max="$max_bytes" -v outdir="$tmpdir" -v sentinel="$FOOTER_SENTINEL" '
        function flush() {
            if (length(buf) == 0) return
            # If a <details> is open mid-flush, close it on this page; the
            # next page will re-open a continuation block.
            if (in_details > 0) {
                buf = buf "\n</details>\n"
            }
            page++
            fname = sprintf("%s/page-%03d", outdir, page)
            printf "%s", buf > fname
            close(fname)
            buf = ""
            cur = 0
            # Re-open the continuation block on the next page so spilled
            # bullets stay collapsed and self-labeled.
            if (in_details > 0) {
                cont = "<details>\n<summary><em>continued from previous comment</em></summary>\n\n"
                buf = cont
                cur = length(cont)
            }
        }
        BEGIN { page = 0; buf = ""; cur = 0; in_details = 0; soft = int(max * 0.75); footer = 0 }
        index($0, sentinel) == 1 { footer = 1 }
        footer { next }
        /^<!-- CLAUDE_REVIEW [0-9]+\/[0-9]+ -->[[:space:]]*$/ { next }
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
            # Update <details> depth AFTER buffering, so flush() above sees
            # the depth as of the PREVIOUS line. Required so the line that
            # opens a block ends up on the new page (not the old), and the
            # line that closes a block does not double-close.
            if (substr($0, 1, 9) == "<details>") {
                in_details++
            } else if (substr($0, 1, 10) == "</details>") {
                if (in_details > 0) in_details--
            }
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

# append_footer <pages_dir> <footer_file>
# Append the canonical footer to every page, so the refresh instructions and
# the don't-hide-me warning ride on the comment the reader is actually looking
# at -- not just on the tail comment of a split review.
append_footer() {
    local pages_dir="$1" footer_file="$2"
    [[ -s "$footer_file" ]] || return 0
    local page
    for page in "$pages_dir"/page-*; do
        printf '\n' >>"$page"
        cat "$footer_file" >>"$page"
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
    if [[ -n "$ROLE" ]]; then
        find_role_comment "$repo" "$pr" "$ROLE" | cut -f1
        return 0
    fi
    list_pinned_comments "$repo" "$pr" | cut -f1
}

# cmd_upsert_role — the v3 surface. One card per role, published VERBATIM:
# the composer renders complete cards (markers, role footer, REVIEW_STATE), so
# this path verifies rather than stamps. No split (evidence lives on the
# evidence page, so an oversized card is a composer bug, not a pagination
# event), no footer.md restamp (the role footers are footer-author.md /
# footer-reviewer.md, already in the body), and no splice-spine floor (the
# spine is machine-owned in the evidence object — there is nothing in the
# comment left to protect).
cmd_upsert_role() {
    local repo pr body_file
    repo=$(resolve_repo)
    pr="${PR:?--pr required}"
    body_file="${BODY_FILE:?--body-file required}"
    [[ -r "$body_file" ]] || die "body file not readable: $body_file"
    (( SOFT_FLOOR )) && die "--soft-floor applies to the v2 split path, not --role upserts"

    local marker
    marker=$(role_marker "$ROLE")

    # Malformed-input gates, loud on purpose: a card missing its own markers
    # or footer would publish fine and then be unfindable (or unreadable) for
    # every downstream consumer — fail here, where the composer bug is
    # attributable, not weeks later in reconcile.
    if ! head -3 "$body_file" | grep -Fxq "$marker"; then
        die "$ROLE card is missing its $marker line in the first three lines"
    fi
    if [[ "$ROLE" == "author" ]]; then
        head -1 "$body_file" | grep -Eq "$LEGACY_ALIAS_RE" \
            || die "author card must open with the legacy <!-- CLAUDE_REVIEW 1/1 --> alias line (v2 consumers find it there)"
    else
        grep -Eq '^<!-- CLAUDE_REVIEW [0-9]+/[0-9]+ -->' "$body_file" \
            && die "brief card must not carry a CLAUDE_REVIEW N/M marker (the v2 sequence would claim it)"
    fi
    grep -Fq "$FOOTER_SENTINEL" "$body_file" \
        || die "$ROLE card is missing its footer (no $FOOTER_SENTINEL sentinel) — cards arrive with role footers pre-rendered"

    local bytes
    bytes=$(wc -c <"$body_file")
    (( bytes <= MAX_BYTES )) \
        || die "$ROLE card is $bytes bytes, over the $MAX_BYTES budget — v3 cards never split; move bulk to the evidence page"

    local row id node_id
    row=$(find_role_comment "$repo" "$pr" "$ROLE")
    if [[ -n "$row" ]]; then
        id=$(printf '%s' "$row" | cut -f1)
        node_id=$(printf '%s' "$row" | cut -f3)
        unminimize_if_hidden "$node_id"
        patch_comment "$repo" "$id" "$body_file"
    else
        create_comment "$repo" "$pr" "$body_file"
    fi
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

    # Soft-floor fallback (the model's one validator retry already failed, per
    # ci.md §4): re-run validate-pinned.py with --soft-floor so the CI
    # annotation is labeled `soft-floor` (not `retry-1`) — surfacing the
    # residual violations to the maintainer — then publish regardless of the
    # validator's exit. (The env-var spelling `VALIDATE_SOFT_FLOOR=1 bash …`
    # is kept working for callers that still use it, but it doesn't match the
    # Bash allow-list pattern; the `--soft-floor` flag is the supported form.)
    if (( SOFT_FLOOR )) || [[ -n "${VALIDATE_SOFT_FLOOR:-}" ]]; then
        local script_dir validator
        script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
        validator="$script_dir/validate-pinned.py"
        if [[ -f "$validator" ]]; then
            python3 "$validator" check \
                --body-file "$body_file" \
                --pr "$pr" \
                --repo "$repo" \
                --soft-floor || true
        fi
    fi

    # Evidence-spine floor. This is the only point in the system that holds the
    # old body and the new one at the same moment: everything above fetches
    # comment IDs, not bodies, so nothing else can notice that a re-render
    # dropped the 🔍 Verification trail. Measured on 2026-08-10, the update
    # lane dropped it in 1 of 6 chained refreshes and published green.
    #
    # UNCONDITIONAL, deliberately. The model composes its own `pinned-comment.sh
    # upsert` command and the Bash allow-list is a prefix match, so a
    # `--spine-floor` flag could simply be omitted — the same reason the ✏️
    # marks are workflow-written rather than model-written. The escape hatch is
    # the env var, which does NOT match the allow-list pattern (that requires
    # the command to begin `bash .claude/…`), so it is reachable by a human or
    # a workflow step and not by the model.
    #
    # Never fatal: splice-spine.py exits 0 on any internal failure and leaves
    # the body as rendered. A repair pass must not be the reason a review fails
    # to publish. Operates on a COPY so a caller's file is never mutated.
    # Scoped by CAPABILITY, not by lane name. The floor is only sound where the
    # caller could not have re-derived the trail: claude-update.yml does a fresh
    # shallow checkout and runs only Vale, so a shrunken trail there is always a
    # loss. The composer lane (claude-code-review.yml, which reaches this
    # function through its validate / splice / re-validate / upsert step
    # chain) recomposes from
    # `.verified-claims.json` against the CURRENT diff — if the author force-
    # pushed a smaller change and re-requested review, a shorter trail is
    # CORRECT there, and restoring the old one would inject records for lines
    # that no longer exist. So: claims artifacts present => the caller owns the
    # trail, stand down. Absent => the prior comment is the only copy, hold.
    if [[ "${SPLICE_SPINE:-1}" != "0" ]] \
       && [[ ! -f .verified-claims.json && ! -f .candidate-claims.json ]]; then
        local script_dir splicer
        script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
        splicer="$script_dir/splice-spine.py"
        if [[ -f "$splicer" ]]; then
            local prior_file spliced_file
            prior_file=$(mktemp)
            spliced_file=$(mktemp)
            fetch_pinned_bodies "$repo" "$pr" >"$prior_file" 2>/dev/null || true
            cp "$body_file" "$spliced_file"
            python3 "$splicer" \
                --prior "$prior_file" \
                --body "$spliced_file" \
                --in-place \
                --report "${SPLICE_SPINE_REPORT:-/tmp/splice-spine.json}" || true
            body_file="$spliced_file"
            rm -f "$prior_file"
        fi
    fi

    # Reserve the footer's bytes out of the per-page budget up front: it is
    # appended to every page after the split, and a page sized to exactly
    # MAX_BYTES plus a footer would sail past GitHub's 65536 hard cap.
    local footer_file
    footer_file=$(mktemp)
    load_footer >"$footer_file"
    local footer_bytes=0
    [[ -s "$footer_file" ]] && footer_bytes=$(( $(wc -c <"$footer_file") + 1 ))
    local split_budget=$(( MAX_BYTES - footer_bytes ))
    (( split_budget > 0 )) || die "footer ($footer_bytes bytes) exceeds --max-bytes ($MAX_BYTES)"

    local pages_dir
    pages_dir=$(split_body "$body_file" "$split_budget")
    local pages
    pages=( "$pages_dir"/page-* )
    local total=${#pages[@]}
    (( total > 0 )) || die "split produced no pages (empty input?)"
    render_with_markers "$pages_dir" "$total"
    append_footer "$pages_dir" "$footer_file"
    rm -f "$footer_file"

    # Re-glob after marker prepend.
    pages=( "$pages_dir"/page-* )

    local existing_tsv
    existing_tsv=$(list_pinned_comments "$repo" "$pr" || true)
    local existing_ids=()
    local existing_nodes=()
    if [[ -n "$existing_tsv" ]]; then
        while IFS=$'\t' read -r id _pos _tot _created node_id; do
            existing_ids+=("$id")
            existing_nodes+=("$node_id")
        done <<< "$existing_tsv"
    fi

    local existing_count=${#existing_ids[@]}
    local i
    for (( i = 0; i < total; i++ )); do
        local page="${pages[$i]}"
        if (( i < existing_count )); then
            unminimize_if_hidden "${existing_nodes[$i]}"
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

cmd_clear() {
    local repo pr
    repo=$(resolve_repo)
    pr="${PR:?--pr required}"
    # Union of the v2 sequence and both v3 role cards, deduped: the author
    # card carries the legacy 1/1 alias, so it appears in BOTH lists and must
    # be deleted exactly once. `#new-review` depends on clear leaving nothing.
    local ids
    ids=$(
        {
            list_pinned_comments "$repo" "$pr" | cut -f1 || true
            list_role_comments "$repo" "$pr" "$AUTHOR_MARKER" | cut -f1 || true
            list_role_comments "$repo" "$pr" "$BRIEF_MARKER" | cut -f1 || true
        } | sort -u
    )
    [[ -z "$ids" ]] && return 0
    while IFS= read -r id; do
        [[ -z "$id" ]] && continue
        delete_comment "$repo" "$id"
    done <<< "$ids"
}

cmd_last_reviewed_sha() {
    local repo pr first_id body head_sha
    repo=$(resolve_repo)
    pr="${PR:?--pr required}"
    # The v3 author card keeps the legacy 1/1 alias as its first line, so the
    # first comment of the v2 sequence IS the author card when one exists —
    # one lookup serves both surfaces.
    first_id=$(list_pinned_comments "$repo" "$pr" | head -1 | cut -f1)
    [[ -z "$first_id" ]] && return 0
    body=$(gh api "repos/$repo/issues/comments/$first_id" --jq '.body')

    # Prefer the CLAUDE_REVIEW_HEAD marker — the sole machine head carrier on
    # the v3 author card, and stamped by the composer on v2 headers too. Same
    # precedence (marker first, history parenthetical as fallback) that
    # review-label-reconcile.yml uses, so the two can never disagree about
    # which SHA a review covers.
    head_sha=$(printf '%s\n' "$body" \
        | grep -oE "$HEAD_MARKER_GREP" | tail -1 \
        | grep -oE '[0-9a-f]{7,40}' || true)
    if [[ -n "$head_sha" ]]; then
        printf '%s\n' "$head_sha"
        return 0
    fi

    # Fallback: the last (sha) parenthetical inside `### 📜 Review history`.
    # Awk segments by section; grep + tr extract the SHA portably without
    # gawk-specific match() captures.
    printf '%s\n' "$body" \
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
SOFT_FLOOR=0
ROLE=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --pr)         PR="$2"; shift 2 ;;
        --body-file)  BODY_FILE="$2"; shift 2 ;;
        --keep)       KEEP="$2"; shift 2 ;;
        --repo)       REPO_FLAG="$2"; shift 2 ;;
        --max-bytes)  MAX_BYTES="$2"; shift 2 ;;
        --dry-run)    DRY_RUN=1; shift ;;
        --soft-floor) SOFT_FLOOR=1; shift ;;
        --role)       ROLE="$2"; shift 2 ;;
        -h|--help)    usage ;;
        *)            die "unknown flag: $1" ;;
    esac
done

if [[ -n "$ROLE" ]]; then
    case "$ROLE" in author|brief) ;; *) die "unknown role: $ROLE (expected author or brief)" ;; esac
    case "$SUBCOMMAND" in
        find|upsert) ;;
        *) die "--role applies to find and upsert only (clear already sweeps role cards; prune and fetch are v2-sequence operations)" ;;
    esac
fi

require_cmd gh
require_cmd jq
require_cmd awk

case "$SUBCOMMAND" in
    find)              cmd_find ;;
    fetch)             cmd_fetch ;;
    upsert)            if [[ -n "$ROLE" ]]; then cmd_upsert_role; else cmd_upsert; fi ;;
    prune)             cmd_prune ;;
    clear)             cmd_clear ;;
    last-reviewed-sha) cmd_last_reviewed_sha ;;
    *)                 usage ;;
esac
