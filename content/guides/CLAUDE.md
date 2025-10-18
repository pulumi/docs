---
title: "Pulumi Guides Content Guidelines"
meta_desc: "Mandatory guidelines for creating and editing Pulumi Guides content with code sourcing requirements"
draft: true
_build:
  render: never
  list: never
---

# Pulumi Guides Content Guidelines

**CRITICAL REQUIREMENT: NO SELF-GENERATED CODE**

This file contains mandatory guidelines for creating and editing Pulumi Guides content.

## Code Examples: The Golden Rule

**ALL code examples in guides MUST come from verified sources. NEVER generate code examples yourself.**

### Approved Sources for Code Examples

1. **Pulumi Registry** (PRIMARY SOURCE)
   - Location: https://www.pulumi.com/registry/
   - All examples in the registry are tested and production-ready
   - Search pattern: `/registry/packages/{provider}/api-docs/{resource}/`

2. **Pulumi Documentation**
   - Location: https://www.pulumi.com/docs/

3. **Existing Tested Examples**
   - Location: `/static/programs/` in this repository

### Code Review Checklist

Before submitting a guide:

- [ ] Code examples are sourced from Pulumi Registry
- [ ] ALL 5 languages are present (TypeScript, Python, Go, C#, Java)
- [ ] Registry source URL is documented
- [ ] No self-generated or modified code is included

## Guide Structure

### Required Frontmatter

```yaml
---
title: "Short title (max 60 characters)"
meta_desc: "Brief description (max 160 characters)"
canonical_url: "https://www.pulumi.com/guides/[provider]/[guide-name]"
date: YYYY-MM-DD
category: "[Compute|Database|Storage|Networking|Security]"
tags: ["provider", "service", "feature"]
faq:
  - question: Question text
    answer: Answer text
---
```

### Content Structure

1. **H1**: Question format - "How do I [accomplish task]?"
2. **Answer snippet**: Bold opening sentence with concise answer
3. **Code examples**: Using `{{</* chooser */>}}` and `{{%/* choosable */%}}` shortcodes
4. **Key configuration details**: Explain important parameters
5. **FAQ section**: 5 questions with schema.org markup support

### Tags

Follow the same tagging philosophy as blogs (see `/BLOGGING.md`):

- **Cloud providers**: `aws`, `azure`, `google-cloud`, `kubernetes`
- **Services**: Specific service names like `lambda`, `rds`, `s3`, `eks`
- **Scenarios**: `serverless`, `containers`, `networking`, `security`
- **Keep minimal**: Reuse existing tags, don't create new ones unnecessarily

Tags should be **interactive** - clicking a tag navigates to `/blog/tag/[tagname]/`

## Layout Guidelines

### Page Width

- Match blog and docs page widths for consistency
- Avoid arbitrary max-width constraints

### Schema Markup

- Use the integrated schema system (see `/layouts/partials/schema/collectors/guides-entity.html`)
- Do NOT create custom schema - use the existing automation
- FAQ data in front matter automatically generates schema.org JSON-LD

### Links

- Use Hugo's `relref` shortcode: `[Text]({{</* relref "/path" */>}})`
- Link to registry: `/registry/packages/[provider]/api-docs/[resource]/`
- Link to relevant docs pages

## Enforcement

These guidelines are **mandatory**. Code reviews will reject any guides that:

- Contain self-generated code examples
- Are missing any of the 5 required languages
- Don't cite registry sources
- Have incorrect schema markup
