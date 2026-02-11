---
user-invocable: false
---

# Quality Checks Reference

Quick reference for quality check procedures in the `/shipit` skill.

## Check Detection Matrix

| Content Changed | Mandatory Checks | Optional Suggestions |
|-------------------|------------------|---------------------|
| Markdown files - meta content (README.md, AGENTS.md, Claude commands, etc.) | Correctness check | - |
| Markdown files - docs/blogs/website content | `make lint` | `make build`, `/docs-review` |
| Hugo templates and shortcodes | `make build` | `/docs-review` |
| Layout and style files (static/css/, static/js/) | `make build` | `/docs-review` |
| Inline code snippets | Test inline code compilation | `/docs-review` |
| Program examples (`static/programs/`) | Test changed programs | - |
| Other changes | Use your best judgment | - |

Any check above may be skipped at your discretion, e.g. if it was run recently or is unnecessary in context.

## Detecting Already-Run Checks

Scan last 10 conversation messages for:

**make lint patterns**: `"make lint"`, `"markdownlint"`, `"yamllint"`, `"lint passed"`

**make build patterns**: `"make build"`, `"hugo"`, `"Building sites"`, `"build passed"`

**/docs-review patterns**: `"/docs-review"`, `"[docs-review]"`

**Display if detected**: `[Step 2/8] Detected previous checks: lint ✓, build ✓ (skipping)`

## Inline Code Snippet Testing

### Extraction

1. Find changed markdown: `git status --short | grep '\.md$'`
2. Extract fenced blocks: ` ```(\w+)\n([\s\S]*?)``` `
3. Test supported languages only: TypeScript, JavaScript, Python, Go, YAML, Bash

### Testing Commands

| Language | Command |
|----------|---------|
| TypeScript | `tsc --noEmit --target es2020 --moduleResolution node --skipLibCheck /tmp/snippet.ts` |
| JavaScript | `node --check /tmp/snippet.js` |
| Python | `python3 -m py_compile /tmp/snippet.py` |
| Go | `go build -o /tmp/test /tmp/snippet.go` (wrap with `package main` if needed) |
| YAML | `python3 -c "import yaml; yaml.safe_load(open('/tmp/snippet.yaml'))"` |
| Bash | `bash -n /tmp/snippet.sh` |

### Partial Example Detection

Skip testing if code contains: `...`, `// ...`, `# ...`, `// TODO`, `<your-value>`, `{...}`, or is < 3 lines

### Results

- **Pass** ✓: Compiles successfully
- **Failed** ⚠️: Syntax errors (warning only, not blocker)
- **Skipped**: Partial/incomplete example

**Display**:

```
Code snippet testing (3 files):
- file1.md: 5 tested (4 passed ✓, 1 skipped)
- file2.md: 3 tested (2 passed ✓, 1 failed ⚠️)
Total: 8 passed ✓, 1 failed ⚠️, 1 skipped
```

## Program Example Testing

### Detection

```bash
git diff --name-only master | grep "^static/programs/" | cut -d'/' -f3 | sort | uniq
```

### Testing

For each program:

```bash
ONLY_TEST="program-name" ./scripts/programs/test.sh
```

### Results

- **Pass** ✓: Exit code 0, all checks passed
- **Failed** ✗: Exit code != 0 (mandatory blocker)

**Display**:

```
Program example testing (2 programs):
- aws-typescript-s3-folder: ✓ passed
- azure-python-vm: ✗ failed
⚠️ MANDATORY: Program tests must pass
```

### Error Handling

If failed:

1. Display full error output
2. Offer: Fix and re-run | Continue anyway (warning) | Cancel
3. If continuing: Add warning to PR description

## Summary Format

```
═══════════════════════════════════════════════════
Quality Checks Summary
═══════════════════════════════════════════════════
Mandatory Checks:
  ✓ make lint passed
  ✓ make build passed (skipped - detected in history)
  ⚠️ 1 code snippet failed (non-blocking warning)
  ✓ 2 program examples passed

Optional Suggestions:
  💡 Consider running /docs-review for content quality
═══════════════════════════════════════════════════
```

## Key Principles

- **Inline snippets**: Lenient (warnings only, many are partial)
- **Program examples**: Strict (must pass, they're complete working code)
- **Previous checks**: Skip if already run in this session
- **User control**: Allow overrides with acknowledgment
