# Alias Injection Reference

How to inject Hugo aliases into frontmatter when moving files.

## Overview

When a file is moved, we must add an alias to preserve the old URL. Hugo aliases create redirect rules that send visitors from old URLs to new locations.

## Frontmatter Structure

Hugo frontmatter is YAML between `---` markers at the file start:

```yaml
---
title: Page Title
meta_desc: Description for SEO
menu:
  docs:
    parent: concepts
    weight: 10
aliases:
  - /old/path/one/
  - /old/path/two/
---

# Content starts here
```

## Alias Syntax

Aliases are YAML arrays with URLs as strings:

```yaml
aliases:
  - /old/url/path/
```

**Requirements**:

- Must start with `/`
- Must end with `/`
- Must be valid URL paths
- Can have multiple entries

## Injection Strategies

### Case 1: No Aliases Section Exists

**Before**:

```yaml
---
title: Page Title
meta_desc: Description
menu:
  docs:
    parent: concepts
---
```

**After**:

```yaml
---
title: Page Title
meta_desc: Description
menu:
  docs:
    parent: concepts
aliases:
  - /old/path/
---
```

**Strategy**: Insert `aliases:` section before the closing `---`

### Case 2: Aliases Section Exists (Array Format)

**Before**:

```yaml
---
title: Page Title
aliases:
  - /existing/path/
---
```

**After**:

```yaml
---
title: Page Title
aliases:
  - /existing/path/
  - /old/path/
---
```

**Strategy**: Append new entry to existing array

### Case 3: Aliases Section Exists (Inline Format)

**Before**:

```yaml
---
title: Page Title
aliases: [/existing/path/]
---
```

**After**:

```yaml
---
title: Page Title
aliases:
  - /existing/path/
  - /old/path/
---
```

**Strategy**: Convert to multi-line array format and append

## Using Edit Tool

Use the Edit tool with string replacement to inject aliases. Read the file first, then:

**If no aliases section exists**: Find the closing `---` of frontmatter and replace with `aliases:\n  - {old_url}\n---`

**If aliases section exists**: Find the last alias entry and append the new one, or replace the entire aliases section with an expanded version including the new alias.

## Edge Cases

**No Frontmatter**: Create frontmatter with alias (warn - this is unusual)

**Malformed Frontmatter**: Error - cannot safely inject, report for manual fix

**Duplicate Alias**: Check if URL already exists in aliases, skip injection, report success

## Validation

After injection verify:

1. File is valid YAML (extract frontmatter and parse)
2. Alias format is correct (starts/ends with `/`)
3. Hugo builds successfully (`make build`)
4. Redirect works (`make serve` and test old URL)
