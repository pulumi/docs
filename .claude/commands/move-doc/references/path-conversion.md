# Path Conversion Reference

How to convert Hugo content file paths to URL paths for alias calculation.

## Algorithm

Hugo converts file paths to URLs following these rules:

```python
def path_to_url(filepath):
    """
    Convert a Hugo content file path to its URL path.

    Args:
        filepath: Path to content file (e.g., "content/docs/foo/bar.md")

    Returns:
        URL path with trailing slash (e.g., "/docs/foo/bar/")
    """
    url = filepath.replace('content/', '', 1)  # Remove content/ prefix
    url = url.replace('.md', '')                # Remove .md extension
    url = url.replace('/_index', '')            # Handle index files
    if not url.endswith('/'):
        url += '/'                              # Add trailing slash
    return url
```

## Examples

### Regular Content Files

```
content/docs/get-started/intro.md
→ /docs/get-started/intro/

content/docs/concepts/resources.md
→ /docs/concepts/resources/

content/blog/2024-01-15-announcement.md
→ /blog/2024-01-15-announcement/
```

### Index Files (`_index.md`)

Index files represent the directory itself, not a subpage:

```
content/docs/_index.md
→ /docs/

content/docs/get-started/_index.md
→ /docs/get-started/

content/blog/_index.md
→ /blog/
```

**Critical**: The `/_index` portion is removed, not just `.md`

### Edge Cases

**Root content**: `content/_index.md` → `/`

**Nested paths**: `content/docs/clouds/aws/get-started/_index.md` → `/docs/clouds/aws/get-started/`

## Validation

1. **Manual check**: `make serve` and test old URL redirects to new URL
2. **Script verification**: Run `scripts/alias-verification/verify-aliases.py`
3. **Production check**: After deploy, verify redirect with `curl -I`
