---
user-invocable: false
---

# Commit Message Guidelines

Quick reference for generating meaningful commit messages that follow repository conventions.

## Format

```
{prefix}: {brief description}

{optional longer description}

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

## General Principles

1. Use imperative mood: "Add feature" not "Added feature"
2. Keep first line under 72 characters
3. Be specific but concise
4. Always include co-author line at end

## Prefix Guidelines

| Prefix | When to Use | Example |
|--------|-------------|---------|
| `feat:` | New feature or capability | `feat: Add MCP server integration` |
| `fix:` | Bug fix | `fix: Correct pricing table alignment` |
| `docs:` | Documentation only changes | `docs: Update installation instructions` |
| `refactor:` | Code refactoring (no behavior change) | `refactor: Simplify auth logic` |
| `test:` | Adding or updating tests | `test: Add unit tests for parser` |
| `chore:` | Maintenance, dependencies, build | `chore: Update dependencies` |

**No prefix**: For documentation in this repo, prefixes are often optional:

- `Add blog post about ESC features`
- `Update AWS provider documentation`
- `Remove outdated Neo limitation`

## Context-Based Patterns

**Documentation** (`content/docs/`, `content/blog/`):

- `Add {feature} documentation`
- `Update {topic} documentation`
- `Fix typos in {section}`
- Example: `Add images and co-author to Platybot blog post (#17479)`

**Features**:

- `Add {feature}`
- `Implement {feature} for {purpose}`
- Example: `Add MCP server integration for AI features`

**Bug Fixes**:

- `Fix {issue}`
- `fix: Correct {problem}`
- Example: `Fix pricing table alignment on mobile`

**Refactoring**:

- `Refactor {component} for {reason}`
- `Simplify {code/logic}`
- Example: `Refactor authentication logic for clarity`

## When to Add Body

Add longer description when:

- Change affects multiple areas
- Context is important for reviewers
- Breaking changes introduced
- Non-obvious reasons for change

Example:

```
Add comprehensive MCP server documentation

Documents the new Model Context Protocol integration including
server setup, API reference, and examples.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

## Issue References

- `(#1234)` - PR number
- `Fixes #1234` - Closes issue
- `Closes #1234` - Closes issue

## Generation Strategy

Generate 3 options:

**Option 1**: Conventional commit with prefix (if applicable) + body if helpful
**Option 2**: Repository style (plain imperative, matches recent commits)
**Option 3**: Alternative phrasing (different emphasis, same meaning)

Consider:

- File types changed (docs/code/tests)
- Conversation context (what was the goal?)
- Recent commit patterns (`git log --oneline -5`)
- Scope (single file vs. feature-wide)

## Anti-Patterns

Avoid:

- ❌ Past tense: "Added feature" (use imperative: "Add feature")
- ❌ Vague: "Updated files", "Fixed stuff", "Changes"
- ❌ Too long: First line > 72 chars
- ❌ Incomplete: "WIP", "TODO", "test"

## Co-Author Line

**Always include at the end:**

```
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```
