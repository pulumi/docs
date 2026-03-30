#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

# Pages to audit.
page_names=("Homepage" "Install Pulumi" "AWS Get Started")
page_paths=("/" "/docs/get-started/download-install/" "/docs/iac/get-started/aws/")

# Read preview URL from the metadata file created by sync-and-test-bucket.sh.
metadata_file="$(origin_bucket_metadata_filepath)"
if [[ ! -f "$metadata_file" ]]; then
    echo "No metadata file found at $metadata_file. Skipping Lighthouse."
    exit 0
fi

base_url="$(jq -r '.url' "$metadata_file")"
commit_sha="$(jq -r '.commit' "$metadata_file" | cut -c1-8)"

if [[ -z "$base_url" || "$base_url" == "null" ]]; then
    echo "No preview URL found in metadata. Skipping Lighthouse."
    exit 0
fi

echo "Running Lighthouse audits against ${base_url}..."

# Install Lighthouse CLI.
npm install -g lighthouse --silent 2>/dev/null

chrome_flags="--headless --no-sandbox"
tmp_dir="$(mktemp -d)"

score_indicator() {
    local score=$1
    if [[ $score -ge 90 ]]; then
        echo ":green_circle:"
    elif [[ $score -ge 50 ]]; then
        echo ":yellow_circle:"
    else
        echo ":red_circle:"
    fi
}

format_time_s() {
    awk "BEGIN { printf \"%.1fs\", $1 / 1000 }"
}

format_tbt() {
    awk "BEGIN { printf \"%.0fms\", $1 }"
}

format_cls() {
    awk "BEGIN { printf \"%.3f\", $1 }"
}

# Run Lighthouse for each page/device combination.
for i in "${!page_paths[@]}"; do
    for device in mobile desktop; do
        url="${base_url}${page_paths[$i]}"
        output_file="${tmp_dir}/${i}-${device}.json"

        echo "Auditing ${page_names[$i]} (${device}): ${url}"

        preset_flag=""
        if [[ "$device" == "desktop" ]]; then
            preset_flag="--preset=desktop"
        fi

        lighthouse "$url" \
            $preset_flag \
            --chrome-flags="$chrome_flags" \
            --output json \
            --output-path "$output_file" \
            --only-categories=performance \
            --quiet \
            || true
    done
done

# Build the markdown comment.
comment_body=""
add_line() { comment_body+="$1"$'\n'; }

add_line "## Lighthouse Performance Report"
add_line ""
add_line "Commit: \`${commit_sha}\`"
add_line ""
add_line "| Page | Device | Score | FCP | LCP | TBT | CLS | SI |"
add_line "|------|--------|-------|-----|-----|-----|-----|----|"

for i in "${!page_paths[@]}"; do
    for device in mobile desktop; do
        json_file="${tmp_dir}/${i}-${device}.json"
        page_name="${page_names[$i]}"
        device_label="$(echo "$device" | sed 's/^./\U&/')"

        if [[ ! -f "$json_file" ]]; then
            add_line "| ${page_name} | ${device_label} | Error | - | - | - | - | - |"
            continue
        fi

        score_raw=$(jq -r '.categories.performance.score // empty' "$json_file" 2>/dev/null)
        if [[ -z "$score_raw" ]]; then
            add_line "| ${page_name} | ${device_label} | Error | - | - | - | - | - |"
            continue
        fi

        score=$(awk "BEGIN { printf \"%.0f\", $score_raw * 100 }")
        indicator=$(score_indicator "$score")

        fcp=$(jq -r '.audits["first-contentful-paint"].numericValue // 0' "$json_file")
        lcp=$(jq -r '.audits["largest-contentful-paint"].numericValue // 0' "$json_file")
        tbt=$(jq -r '.audits["total-blocking-time"].numericValue // 0' "$json_file")
        cls=$(jq -r '.audits["cumulative-layout-shift"].numericValue // 0' "$json_file")
        si=$(jq -r '.audits["speed-index"].numericValue // 0' "$json_file")

        add_line "| ${page_name} | ${device_label} | ${indicator} ${score} | $(format_time_s "$fcp") | $(format_time_s "$lcp") | $(format_tbt "$tbt") | $(format_cls "$cls") | $(format_time_s "$si") |"
    done
done

# Post the comment to the PR.
if [[ -n "$GITHUB_EVENT_PATH" ]]; then
    pr_comment_api_url="$(jq -r '.pull_request._links.comments.href' "$GITHUB_EVENT_PATH" 2>/dev/null)"

    if [[ -n "$pr_comment_api_url" && "$pr_comment_api_url" != "null" ]]; then
        echo "Posting Lighthouse results to PR..."
        json_payload=$(jq -n --arg body "$comment_body" '{"body": $body}')

        curl -s \
            -X POST \
            -H "Authorization: token ${PULUMI_BOT_TOKEN}" \
            -H "Content-Type: application/json" \
            -d "$json_payload" \
            "$pr_comment_api_url" > /dev/null

        echo "Lighthouse comment posted."
    else
        echo "No PR comment URL found. Printing results to stdout:"
        echo "$comment_body"
    fi
else
    echo "Not running in GitHub Actions. Printing results to stdout:"
    echo "$comment_body"
fi

# Cleanup.
rm -rf "$tmp_dir"

echo "Lighthouse audits complete."
