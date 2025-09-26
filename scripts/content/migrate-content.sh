#!/bin/bash

set -o errexit -o pipefail

# Content migration script for bulk moves with history preservation
# Usage: ./migrate-content.sh --source "/docs/iac/guides" --dest "/docs/guides" --menu-parent "guides-home"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONTENT_DIR="content"

# Default values
SOURCE_PATH=""
DEST_PATH=""
MENU_PARENT=""
OLD_MENU_SECTION=""
NEW_MENU_SECTION=""
DRY_RUN=false
VERBOSE=false

show_help() {
    cat << EOF
Content Migration Tool

USAGE:
    $0 [OPTIONS]

OPTIONS:
    --source PATH           Source path to migrate from (e.g., "/docs/iac/guides")
    --dest PATH            Destination path to migrate to (e.g., "/docs/guides")
    --menu-parent ID       New menu parent identifier (e.g., "guides-home")
    --old-menu SECTION     Old menu section to replace (e.g., "iac")
    --new-menu SECTION     New menu section to use (e.g., "guides")
    --dry-run             Preview changes without executing
    --verbose             Show detailed output
    --help                Show this help message

EXAMPLES:
    # Move IaC guides to new guides section
    $0 --source "/docs/iac/guides" --dest "/docs/guides" \\
       --old-menu "iac" --new-menu "guides" --menu-parent "guides-home"

    # Preview changes first
    $0 --source "/docs/iac/concepts" --dest "/docs/concepts" \\
       --old-menu "iac" --new-menu "concepts" --menu-parent "concepts-home" --dry-run

EOF
}

log() {
    if [ "$VERBOSE" = true ]; then
        echo "📋 $1"
    fi
}

error() {
    echo "❌ Error: $1" >&2
    exit 1
}

success() {
    echo "✅ $1"
}

warning() {
    echo "⚠️  Warning: $1"
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --source)
            SOURCE_PATH="$2"
            shift 2
            ;;
        --dest)
            DEST_PATH="$2"
            shift 2
            ;;
        --menu-parent)
            MENU_PARENT="$2"
            shift 2
            ;;
        --old-menu)
            OLD_MENU_SECTION="$2"
            shift 2
            ;;
        --new-menu)
            NEW_MENU_SECTION="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=true
            shift
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
            error "Unknown option: $1. Use --help for usage information."
            ;;
    esac
done

# Validate required parameters
if [[ -z "$SOURCE_PATH" || -z "$DEST_PATH" ]]; then
    error "Both --source and --dest are required. Use --help for usage information."
fi

# Convert paths to filesystem paths
SOURCE_FS_PATH="${CONTENT_DIR}${SOURCE_PATH}"
DEST_FS_PATH="${CONTENT_DIR}${DEST_PATH}"

# Validation phase
validate_migration() {
    echo "🔍 Validating migration parameters..."

    # Check source exists
    if [[ ! -d "$SOURCE_FS_PATH" ]]; then
        error "Source path does not exist: $SOURCE_FS_PATH"
    fi

    # Check destination parent exists
    DEST_PARENT=$(dirname "$DEST_FS_PATH")
    if [[ ! -d "$DEST_PARENT" ]]; then
        error "Destination parent directory does not exist: $DEST_PARENT"
    fi

    # Check destination doesn't already exist
    if [[ -d "$DEST_FS_PATH" ]]; then
        error "Destination path already exists: $DEST_FS_PATH"
    fi

    # Count files to migrate
    local file_count
    file_count=$(find "$SOURCE_FS_PATH" -name "*.md" | wc -l)

    if [[ $file_count -eq 0 ]]; then
        warning "No .md files found in source directory"
    else
        log "Found $file_count markdown files to migrate"
    fi

    success "Validation passed"
}

# Git operations
move_files() {
    echo "📦 Moving files with git history preservation..."

    if [[ "$DRY_RUN" = true ]]; then
        echo "DRY RUN: Would execute: git mv \"$SOURCE_FS_PATH\" \"$DEST_FS_PATH\""
        return
    fi

    git mv "$SOURCE_FS_PATH" "$DEST_FS_PATH"
    success "Files moved successfully"
}

# Update frontmatter in all migrated files
update_frontmatter() {
    echo "⚙️  Updating frontmatter in migrated files..."

    local files_updated=0

    while IFS= read -r -d '' file; do
        log "Processing: $file"

        if [[ "$DRY_RUN" = true ]]; then
            # In dry run, convert source path to what destination path would be
            local dest_file="${file/$SOURCE_FS_PATH/$DEST_FS_PATH}"
            echo "DRY RUN: Would update frontmatter in: $dest_file"
            ((files_updated++))
            continue
        fi

        local temp_file
        temp_file=$(mktemp)
        local in_frontmatter=false
        local frontmatter_ended=false
        local aliases_added=false
        local menu_updated=false

        while IFS= read -r line; do
            # Track frontmatter boundaries
            if [[ "$line" == "---" ]]; then
                if [[ "$in_frontmatter" = false ]]; then
                    in_frontmatter=true
                elif [[ "$frontmatter_ended" = false ]]; then
                    frontmatter_ended=true

                    # Add aliases section before closing frontmatter if not already added
                    if [[ "$aliases_added" = false ]]; then
                        # Calculate old path from file path
                        local relative_file_path="${file#$DEST_FS_PATH}"
                        local old_file_path="${SOURCE_PATH}${relative_file_path}"

                        echo "aliases:" >> "$temp_file"
                        echo "    - $old_file_path" >> "$temp_file"
                        aliases_added=true
                    fi
                fi
                echo "$line" >> "$temp_file"
                continue
            fi

            # Process frontmatter lines
            if [[ "$in_frontmatter" = true && "$frontmatter_ended" = false ]]; then
                # Update menu section if specified
                if [[ -n "$OLD_MENU_SECTION" && -n "$NEW_MENU_SECTION" && "$line" =~ ^[[:space:]]*"$OLD_MENU_SECTION": ]]; then
                    echo "$line" | sed "s/^\\([[:space:]]*\\)$OLD_MENU_SECTION:/\\1$NEW_MENU_SECTION:/" >> "$temp_file"
                    menu_updated=true
                # Update menu parent if specified and this is a menu section
                elif [[ -n "$MENU_PARENT" && "$line" =~ ^[[:space:]]*parent: ]]; then
                    echo "        parent: $MENU_PARENT" >> "$temp_file"
                # Handle existing aliases section
                elif [[ "$line" =~ ^aliases: ]]; then
                    echo "$line" >> "$temp_file"
                    # Add our alias to existing aliases
                    local relative_file_path="${file#$DEST_FS_PATH}"
                    local old_file_path="${SOURCE_PATH}${relative_file_path}"
                    echo "    - $old_file_path" >> "$temp_file"
                    aliases_added=true
                else
                    echo "$line" >> "$temp_file"
                fi
            else
                # Outside frontmatter - copy as-is
                echo "$line" >> "$temp_file"
            fi
        done < "$file"

        # Replace original file
        mv "$temp_file" "$file"
        ((files_updated++))
        log "Updated: $file"

    done < <(if [[ "$DRY_RUN" = true ]]; then
        find "$SOURCE_FS_PATH" -name "*.md" -print0
    else
        find "$DEST_FS_PATH" -name "*.md" -print0
    fi)

    success "Updated frontmatter in $files_updated files"
}

# Main execution
main() {
    echo "🚀 Pulumi Content Migration Tool"
    echo "Source: $SOURCE_PATH → Destination: $DEST_PATH"

    if [[ "$DRY_RUN" = true ]]; then
        echo "🔍 DRY RUN MODE - No changes will be made"
    fi

    validate_migration
    move_files
    update_frontmatter

    echo
    if [[ "$DRY_RUN" = true ]]; then
        echo "🔍 Dry run completed. Use without --dry-run to execute changes."
    else
        success "Migration completed successfully!"
        echo "📝 Next steps:"
        echo "   1. Review the changes: git status"
        echo "   2. Test the site builds: make build"
        echo "   3. Commit the changes: git add . && git commit -m 'migrate: move $SOURCE_PATH to $DEST_PATH'"
    fi
}

main "$@"