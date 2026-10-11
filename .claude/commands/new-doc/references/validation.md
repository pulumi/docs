---
user-invocable: false
---

# Validation and Error Handling

Complete checklist for validating files before creation, handling errors gracefully, and displaying success output.

## Pre-Creation Validation Checklist

Before creating the file, verify:

- [ ] File doesn't exist at target path
- [ ] Parent identifier exists (or intentionally omitted for top-level pages)
- [ ] Menu identifier is unique within the section
- [ ] Weight is reasonable (0 < weight < 1000)
- [ ] All required frontmatter fields are populated
- [ ] YAML syntax is valid (proper indentation, quotes where needed)
- [ ] Filename is kebab-case (regular pages only)
- [ ] Meta description is 50-160 characters
- [ ] All links are valid (start with `/docs/` or are external URLs)

## Error Handling

Handle errors gracefully with these strategies:

- **File exists**: Suggest alternative filename or ask user to confirm overwrite
- **Invalid filename**: Auto-suggest kebab-case correction and apply it
- **Missing parent**: Warn about navigation issues, offer to create parent `_index.md` first
- **Weight out of range**: Suggest reasonable value based on sibling pages
- **Duplicate identifier**: Auto-append `-2`, `-3`, etc. until unique
- **Empty sections** (index pages only): Require at least one section before proceeding
- **Invalid meta_desc length**: Warn user and request adjustment to 50-160 character range
- **Path navigation at root**: Handle "go up" command gracefully with informative message

## Success Output Format

After successful file creation, display this output:

```text
✅ Created at /docs/{path}/{filename}.md
✅ Identifier: {identifier} (unique)
✅ Parent: {parent} (validated)
✅ Weight: {weight}
✅ Meta desc: {length} chars

Preview: http://localhost:1313/docs/{path}/
Next: Write content, run /docs-review, run make lint
```

Replace all `{variables}` with actual values from the created file.
