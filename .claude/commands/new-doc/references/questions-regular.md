---
user-invocable: false
---

# AskUserQuestion Patterns - Regular Pages

Complete patterns for gathering metadata for regular documentation pages. Ask for each field in order using AskUserQuestion with smart suggestions.

## Field 1: Title

Generate Title Case version from the user's description.

```
Question: "What should the page title be?"
Options:
- "{Suggested Title in Title Case} (Recommended)"
- "Enter a different title"
```

**Logic:**

- Convert user's description to Title Case (capitalize major words)
- Present as recommended option
- If user selects "Enter different", prompt for text input
- Store result as `{title}`

## Field 2: Title Tag

Prepopulate with standard Pulumi Docs format.

```
Question: "What should the browser title tag be?"
Options:
- "{Title} | Pulumi Docs (Recommended)"
- "Enter a different title tag"
```

**Logic:**

- Use title from Field 1 and append " | Pulumi Docs"
- Present as recommended option
- If user selects "Enter different", prompt for text input
- Store result as `{title_tag}`

## Field 3: Meta Description

Generate based on content and user's description.

```
Question: "Choose or provide a meta description (50-160 characters):"
Options:
- "{Suggested meta description based on context} (Recommended)"
- "Enter a different meta description"
```

**Logic:**

- Generate concise description (50-160 chars) based on user's intent
- Present as recommended option
- If user selects "Enter different", prompt for text input
- Validate length is 50-160 characters
- Warn and request adjustment if out of range
- Store result as `{meta_desc}`

## Field 4: File Name

Auto-generate kebab-case from title.

```
Question: "What should the file name be?"
Options:
- "{suggested-kebab-case-filename} (Recommended)"
- "Enter a different filename"
```

**Logic:**

- Convert title to lowercase kebab-case (e.g., "My Page" → "my-page")
- Remove special characters, use hyphens for spaces
- Present as recommended option
- If user selects "Enter different", prompt for text input
- Validate filename is kebab-case (lowercase, hyphens only, no spaces)
- Store result as `{filename}` (no .md extension)

## Implementation Notes

- Always provide smart suggestions based on context
- Make recommended option first choice
- Validate input when user enters custom values
- Use Title Case for page titles (Field 1)
- Keep meta descriptions concise and descriptive (Field 3)
- Ensure filenames follow kebab-case convention (Field 4)
