#!/bin/bash

set -o errexit -o pipefail

# Content discovery script to help identify migration candidates
# Usage: ./discover-migration-candidates.sh [--path PATH] [--verbose]

CONTENT_DIR="content"
SEARCH_PATH="${CONTENT_DIR}/docs"
VERBOSE=false

show_help() {
    cat << EOF
Content Migration Discovery Tool

Analyzes documentation structure to identify potential migration candidates
and their dependencies.

USAGE:
    $0 [OPTIONS]

OPTIONS:
    --path PATH     Directory to analyze (default: content/docs)
    --verbose       Show detailed analysis
    --help          Show this help message

EXAMPLES:
    # Analyze all docs
    $0

    # Analyze specific directory
    $0 --path content/docs/iac

    # Detailed analysis
    $0 --verbose

EOF
}

log() {
    if [ "$VERBOSE" = true ]; then
        echo "📋 $1"
    fi
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --path)
            SEARCH_PATH="$2"
            shift 2
            ;;
        --verbose)
            VERBOSE=true
            shift
            ;;
        --help)
            show_help
            exit 0
            ;;
        *)
            echo "❌ Unknown option: $1. Use --help for usage information." >&2
            exit 1
            ;;
    esac
done

analyze_structure() {
    echo "🔍 Content Structure Analysis"
    echo "=====================================ß"
    echo "Search path: $SEARCH_PATH"
    echo

    # Directory overview
    echo "📁 Directory Structure:"
    find "$SEARCH_PATH" -type d -maxdepth 2 | sort | while read -r dir; do
        local file_count
        file_count=$(find "$dir" -maxdepth 1 -name "*.md" | wc -l)
        echo "   ${dir#$CONTENT_DIR} ($file_count files)"
    done
    echo

    # Menu section analysis
    echo "📋 Menu Sections Found:"
    find "$SEARCH_PATH" -name "*.md" -exec grep -l "menu:" {} \; | \
    xargs grep -h "^\s*[a-zA-Z-]*:" | \
    grep -v "name:" | grep -v "parent:" | grep -v "identifier:" | grep -v "weight:" | \
    sort | uniq -c | sort -nr
    echo

    # Files with old menu patterns
    echo "🔧 Files needing menu updates:"
    local iac_count
    iac_count=$(find "$SEARCH_PATH" -name "*.md" -exec grep -l "iac:" {} \; | wc -l)
    if [[ $iac_count -gt 0 ]]; then
        echo "   $iac_count files still use 'iac:' menu section"
    fi

    local clouds_count
    clouds_count=$(find "$SEARCH_PATH" -name "*.md" -exec grep -l "clouds:" {} \; | wc -l)
    if [[ $clouds_count -gt 0 ]]; then
        echo "   $clouds_count files still use 'clouds:' menu section"
    fi

    if [[ $iac_count -eq 0 && $clouds_count -eq 0 ]]; then
        echo "   ✅ No outdated menu patterns found"
    fi
    echo

    # Cross-references analysis
    echo "🔗 Internal Link Analysis:"
    local link_count
    link_count=$(find "$SEARCH_PATH" -name "*.md" -exec grep -o '\[.*\](\s*/[^)]*\s*)' {} \; | wc -l)
    echo "   Found $link_count internal links"

    # Most common link patterns
    echo "   Common link patterns:"
    find "$SEARCH_PATH" -name "*.md" -exec grep -ho '(\s*/docs/[^)]*\s*)' {} \; | \
    sed 's|(/docs/\([^/]*\)/.*|\1|' | sort | uniq -c | sort -nr | head -5 | \
    while read -r count pattern; do
        echo "      $count links to /docs/$pattern/*"
    done
    echo
}

show_migration_suggestions() {
    echo "💡 Migration Suggestions:"
    echo "=========================="

    # Large directories that might benefit from reorganization
    echo "📦 Large directories (potential candidates):"
    find "$SEARCH_PATH" -type d | while read -r dir; do
        local file_count
        file_count=$(find "$dir" -maxdepth 1 -name "*.md" | wc -l)
        if [[ $file_count -gt 10 ]]; then
            echo "   ${dir#$CONTENT_DIR} ($file_count files) - Consider splitting"
        fi
    done
    echo

    # Suggest consolidation opportunities
    echo "🔄 Potential consolidations:"
    find "$SEARCH_PATH" -type d -name "*guide*" -o -name "*tutorial*" -o -name "*how-to*" | \
    while read -r dir; do
        local file_count
        file_count=$(find "$dir" -name "*.md" | wc -l)
        echo "   ${dir#$CONTENT_DIR} ($file_count files) - Workflow-oriented content"
    done
    echo
}

main() {
    echo "🚀 Pulumi Content Discovery Tool"
    echo

    if [[ ! -d "$SEARCH_PATH" ]]; then
        echo "❌ Error: Search path does not exist: $SEARCH_PATH" >&2
        exit 1
    fi

    analyze_structure
    show_migration_suggestions

    echo "📝 Next steps:"
    echo "   1. Review the analysis above"
    echo "   2. Choose directories to migrate"
    echo "   3. Use migrate-content.sh to execute moves"
    echo "   4. Example: ./migrate-content.sh --source \"/docs/iac/guides\" --dest \"/docs/guides\" --old-menu \"iac\" --new-menu \"guides\""
}

main "$@"