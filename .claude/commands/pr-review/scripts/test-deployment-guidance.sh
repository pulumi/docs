#!/bin/bash
# Test Deployment Guidance Script
# Usage: ./test-deployment-guidance.sh <PR_NUMBER>
#
# Outputs:
# JSON object with deployment URL, status, and structured page data

set -e

if [ -z "$1" ]; then
  echo "Error: PR number required" >&2
  echo "Usage: $0 <PR_NUMBER>" >&2
  exit 1
fi

PR_NUMBER="$1"

# Fetch pulumi-bot comment and extract deployment URL
DEPLOYMENT_URL=$(gh api repos/pulumi/docs/issues/"$PR_NUMBER"/comments \
  --jq '.[] | select(.user.login == "pulumi-bot") | .body' 2>/dev/null | \
  grep -oP 'http://www-testing-pulumi-docs-origin-pr-\d+-[a-f0-9]+\.s3-website\.us-west-2\.amazonaws\.com' | \
  tail -1 || echo "")

# Fetch PR data including files
PR_DATA=$(gh pr view "$PR_NUMBER" --json files,additions,deletions)

# Get changed files
CHANGED_FILES=$(echo "$PR_DATA" | jq -r '.files[].path')

# Fetch full diff once for analysis
FULL_DIFF=$(gh pr diff "$PR_NUMBER" 2>/dev/null || echo "")

# Function to convert content path to URL path
convert_path_to_url() {
  local file_path="$1"
  local url_path="$file_path"

  # Remove content/ prefix
  url_path="${url_path#content/}"

  # Remove .md or _index.md suffix
  url_path="${url_path%.md}"
  url_path="${url_path%_index}"

  # Ensure trailing slash
  if [[ ! "$url_path" =~ /$ ]]; then
    url_path="${url_path}/"
  fi

  echo "/$url_path"
}

# Function to extract page title from file (fallback to filename)
get_page_title() {
  local file_path="$1"
  local title=""

  # Try to extract title from frontmatter
  if [ -f "$file_path" ]; then
    title=$(grep -m 1 '^title:' "$file_path" 2>/dev/null | sed 's/^title:[[:space:]]*["'"'"']\?//' | sed 's/["'"'"'][[:space:]]*$//' || echo "")
  fi

  # Fallback to filename
  if [ -z "$title" ]; then
    title=$(basename "$file_path" | sed 's/\.md$//' | sed 's/_index$//' | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')
  fi

  echo "$title"
}

# Function to analyze diff for specific file
analyze_diff_for_file() {
  local file_path="$1"
  local diff_output="$2"

  # Check for various types of changes (grep returns 1 when no matches, so use || true)
  local heading_changes=$(echo "$diff_output" | grep -c '^+[[:space:]]*##' || true)
  local code_changes=$(echo "$diff_output" | grep -c '^+[[:space:]]*```' || true)
  local image_changes=$(echo "$diff_output" | grep -c '^+.*!\[' || true)
  local link_changes=$(echo "$diff_output" | grep -c '^+.*\[.*\](' || true)

  # Count additions/deletions for this file
  local additions=$(echo "$diff_output" | grep -c '^+' || true)
  local deletions=$(echo "$diff_output" | grep -c '^-' || true)

  # Ensure variables are numeric (default to 0 if empty)
  heading_changes=${heading_changes:-0}
  code_changes=${code_changes:-0}
  image_changes=${image_changes:-0}
  link_changes=${link_changes:-0}
  additions=${additions:-0}
  deletions=${deletions:-0}

  # Output as space-separated values for easy parsing
  echo "$heading_changes $code_changes $image_changes $link_changes $additions $deletions"
}

# Start with base JSON object
json_output=$(jq -n \
  --arg prNumber "$PR_NUMBER" \
  '{
    deploymentUrl: null,
    deploymentStatus: "pending",
    prNumber: ($prNumber | tonumber),
    pages: [],
    nonContentFiles: []
  }')

# Add deployment URL if found
if [ -n "$DEPLOYMENT_URL" ]; then
  json_output=$(echo "$json_output" | jq \
    --arg url "$DEPLOYMENT_URL" \
    '.deploymentUrl = $url | .deploymentStatus = "ready"')
fi

# Process changed files
while IFS= read -r file; do
  if [[ "$file" == content/*.md ]]; then
    # Get page title
    page_title=$(get_page_title "$file")

    # Convert to URL
    url_path=$(convert_path_to_url "$file")

    # Extract diff for this specific file from the full diff
    diff_content=$(echo "$FULL_DIFF" | awk -v file="$file" '
      /^diff --git/ {
        in_file = ($0 ~ "a/"file" b/"file)
        next
      }
      in_file {
        if (/^diff --git/) exit
        print
      }
    ')

    # Analyze diff and get change counts
    read -r headings code images links adds dels <<< "$(analyze_diff_for_file "$file" "$diff_content")"

    # Build page object and add to array
    page_obj=$(jq -n \
      --arg file "$file" \
      --arg title "$page_title" \
      --arg url "$url_path" \
      --argjson headings "$headings" \
      --argjson code "$code" \
      --argjson images "$images" \
      --argjson links "$links" \
      --argjson adds "$adds" \
      --argjson dels "$dels" \
      '{
        file: $file,
        title: $title,
        url: $url,
        changes: {
          headings: $headings,
          codeBlocks: $code,
          images: $images,
          links: $links,
          additions: $adds,
          deletions: $dels
        }
      }')

    json_output=$(echo "$json_output" | jq --argjson page "$page_obj" \
      '.pages += [$page]')
  else
    # Add non-content files to array
    json_output=$(echo "$json_output" | jq --arg file "$file" \
      '.nonContentFiles += [$file]')
  fi
done <<< "$CHANGED_FILES"

# Output final JSON
echo "$json_output"
