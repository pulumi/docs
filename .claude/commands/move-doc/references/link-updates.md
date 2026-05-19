---
user-invocable: false
---

# Link Updates Reference

How to find and update internal links when moving documentation files.

## Overview

When a file moves, internal links in other files need updating to reflect the new URL. This prevents broken links and maintains documentation integrity.

## Repository Guidelines

From `AGENTS.md` (lines 83-98):

**DO update links in**:

- `content/docs/` - Active documentation
- `content/product/` - Product pages

**DO NOT update links in**:

- `content/blog/` - Historical blog posts
- `content/tutorials/` - Historical tutorials

**Why**: Blog posts and tutorials represent a point in time. Aliases handle redirects automatically, preserving historical accuracy.

## Search Strategy

### Find References

Use `grep` to find files containing the old URL:

```bash
grep -rl "{old_url}" content/docs/ content/product/ --include="*.md"
```

**Options explained**:

- `-r`: Recursive search
- `-l`: List filenames only (not line content)
- `--include="*.md"`: Only search markdown files

**Example**:

```bash
grep -rl "/docs/concepts/resources/" content/docs/ content/product/ --include="*.md"
```

**Output**:

```
content/docs/get-started/intro.md
content/docs/guides/advanced.md
content/product/features.md
```

### Count References

```bash
grep -r "{old_url}" content/docs/ content/product/ --include="*.md" | wc -l
```

### Show Context

Preview changes with context lines:

```bash
grep -rn -C 2 "{old_url}" content/docs/ content/product/ --include="*.md"
```

**Options**:

- `-n`: Show line numbers
- `-C 2`: Show 2 lines context before and after

## Update Strategy

### Replace URLs

Use `find` with `sed` for in-place replacement:

```bash
find content/docs content/product -name "*.md" \
  -exec sed -i 's|{old_url}|{new_url}|g' {} +
```

**Important**:

- Use `|` as delimiter (not `/`) to avoid conflicts with URL slashes
- Use `+` at end for efficiency (processes multiple files per sed call)
- `-i` modifies files in-place

**Example**:

```bash
find content/docs content/product -name "*.md" \
  -exec sed -i 's|/docs/old/path/|/docs/new/path/|g' {} +
```

## Link Patterns

Patterns to update:
- Markdown links: `[text](/docs/old/path/)`
- Links with anchors: `[text](/docs/old/path/#section)`
- Hugo relref shortcodes: `{{< relref "/docs/old/path" >}}`
- HTML links: `<a href="/docs/old/path/">text</a>`

## Edge Cases

**Anchor Links**: Preserved automatically by sed pattern (e.g., `/docs/old/#section` → `/docs/new/#section`)

**Partial Matches**: Use `grep -F` for fixed string matching to avoid false positives (e.g., `/docs/aws/` vs `/docs/aws-native/`)

**Multiple URLs in Same File**: The `sed` command with `g` flag replaces all occurrences

## Verification

**Preview**: Use `grep -rn "{old_url}" content/docs/ content/product/ --include="*.md"` before applying

**Review**: After updates, use `git diff content/docs/ content/product/` to verify only intended URLs changed

**Rollback**: Use `git restore content/docs/ content/product/` if changes are incorrect

## External References (workflows and scripts)

Hugo aliases redirect URLs at request time — they do **not** rewrite filesystem paths or hard-coded URL strings in CI workflows or repository scripts. If automation reads or writes the moved file by its old path, the move silently breaks that automation at the next scheduled run.

### Search

Search both the old URL and the old filesystem path (without the leading `./`):

```bash
old_path_trimmed="${source_file#./}"
grep -rn "{old_url}\|${old_path_trimmed}" .github/workflows/ scripts/ 2>/dev/null
```

### Do not auto-update these matches

Workflow and script references appear inside shell strings, regex, JavaScript, YAML literals, JSON, etc., where blind `sed` substitution can corrupt surrounding syntax or the semantics of adjacent code. Surface matches as a manual-review warning instead and let the user update each one in context.

### Common breakage patterns

- **Hard-coded `sed -i` / `cat` / `cp` writes** to the moved file (e.g. `sed -i ./content/docs/old/path/file.md` in a workflow step)
- **URL lists in audit scripts** — Lighthouse runners, link-checkers, smoke-test scripts iterating over a hard-coded set of paths
- **Algolia ranking rules** keyed on the old canonical URL (`page.getObjectID({ href: "/docs/old/..." })`)
- **Redirect destinations** in `scripts/redirects/*.txt` pointing to the old URL — these create double-redirects rather than breaking, so they're easy to miss
- **CODEOWNERS** lines targeting the old path for auto-merge or review routing

### Real example

PR #19137 moved `content/docs/get-started/download-install/versions.md` to `content/docs/install/versions.md`. Hugo aliases kept all user URLs working, but `.github/workflows/pulumi-cli-docs.yml` had a `sed -i ./content/docs/get-started/download-install/versions.md` line that wasn't updated. The next scheduled CLI docs run failed with `sed: can't read ...: No such file or directory` — see [run 26097909723](https://github.com/pulumi/docs/actions/runs/26097909723/job/76740530471).

## Performance Considerations

**Small updates (< 20 files)**: Show preview with context, ask confirmation
**Large updates (>= 20 files)**: Show count only, ask confirmation

**Optimization**: Use `find ... -exec sed ... {} +` (not `\;`) to batch files for faster execution
