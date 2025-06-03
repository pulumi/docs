# CLAUDE.md - Guide for Working in this Repository

## Repository Context

This is the **Pulumi documentation repository** - a Hugo-based static site that powers [pulumi.com](https://pulumi.com). The repository contains:

- **Hand-crafted documentation** for Pulumi's Infrastructure as Code, Pulumi ESC, Pulumi Insights and Pulumi IDP products
- **Blog posts and tutorials** for the Pulumi community
- **Multi-language code examples** tested for accuracy
- **Landing pages and marketing content** for pulumi.com

## Key Technologies

- **Hugo** (>= 0.126.0) - Static site generator
- **Node.js/Yarn** - Dependency management and build tools
- **TypeScript** - Language for scripts and components
- **Stencil** - Web components framework
- **Tailwind CSS** - Styling framework
- **Algolia** - Search indexing

## Critical File Locations

### **Documentation & Content**

- `content/` - All Markdown content (docs, blog, pages)
- `content/docs/` - Main documentation
- `content/blog/` - Blog posts (each in own directory with `_index.md`)
- `static/programs/` - Multi-language code examples for testing

### **Hugo Infrastructure**

- `layouts/shortcodes/` - Custom Hugo shortcodes
- `layouts/partials/` - Reusable template components
- `config/` - Hugo configuration files
- `data/` - Site data files (team info, etc.)

### **Assets & Styling**

- `theme/` - Source files for CSS/JS
- `assets/` - Built CSS/JS bundles (checked in)
- `static/` - Static assets (images, programs, etc.)

### **Documentation Guidelines**

- `STYLE-GUIDE.md` - **Essential writing and formatting standards (read this first!)**
- `BLOGGING.md` - Blog post creation process
- `CODE-EXAMPLES.md` - Code example standards and testing
- `CONTRIBUTING.md` - General contribution guidelines

---

# Documentation Standards

## **Language and Terminology**

- Use `pulumi` or "the Pulumi CLI" to refer to the CLI
- Use `Pulumi Cloud` to refer to the infrastructure management platform  
- **Avoid ableist language:** Use "wild" instead of "crazy", "select" instead of "click", "placeholder" instead of "dummy"
- **Never use "easy" or "simple"** - they make assumptions about reader expertise

## **Content Structure**

- **One `h1` per page** - every page must have exactly one
- **Heading hierarchy:** Only increment one level at a time (h2 → h3, never h2 → h4)
- **Sentence case headings** for docs and registry (first letter capitalized only)
- **Keep paragraphs short** - rarely use 4+ sentences
- **Lead with engaging content**, end with exactly one call-to-action
- **Use semantic line breaks** or keep paragraphs on single lines - **never reflow text**

## **Links and References**

- **Use descriptive link text** - avoid "here", "click here", "see here"
- **Internal links:** Use standard Markdown syntax `[text](/path)` (migrating away from `{{< relref >}}`)
- **External links:** Include full URLs with descriptive text
- **Add redirects** via Hugo aliases when changing URLs: `aliases: [/old-path/]`

---

# Custom Hugo Features

## **Language Choosers**

Multi-language content selection using custom web components:

```markdown
{{< chooser "language" "typescript,python,go" >}}

{{< choosable "language" "typescript" >}}
// TypeScript code here
{{< /choosable >}}

{{< choosable "language" "python" >}}
# Python code here
{{< /choosable >}}

{{< /chooser >}}
```

**Available chooser types:** `language`, `os`, `cloud`

## **Tested Code Examples**

All examples in `/static/programs/` are automatically tested:

```markdown
<!-- Shows complete programs with language chooser -->
{{< example-program path="aws-s3-bucket" >}}

<!-- Shows specific lines from a program -->
{{< example-program-snippet path="aws-s3-bucket" language="typescript" from="10" to="20" >}}

<!-- Limit displayed languages -->
{{< example-program path="aws-s3-bucket" languages="typescript,python" >}}
```

**Naming convention:** `<program-name>-<language>` (e.g., `aws-s3-bucket-typescript`)

## **Notes and Alerts**

Styled notification boxes:

```markdown
{{% notes type="info" %}}
General information that's important to highlight
{{% /notes %}}

{{% notes type="tip" %}}
Helpful suggestions and best practices
{{% /notes %}}

{{% notes type="warning" %}}
Critical information - serious consequences if ignored
{{% /notes %}}
```

## **Video Embeds**

YouTube video embedding:

```markdown
{{< youtube "video-id?rel=0" >}}
```

**Always use `?rel=0`** for Pulumi YouTube videos to limit suggested videos to the same channel.

## **Pulumi CLI Integration**

Auto-generated CLI documentation shortcodes:

- `{{< pulumi-new >}}` - Shows `pulumi new` command help
- `{{< pulumi-up >}}` - Shows `pulumi up` command help  
- `{{< pulumi-config >}}` - Shows config-related commands
- And many more for specific CLI functions

---

# Code and Examples

## **Code Blocks**

```typescript
// ✅ DO: Use language-specific code fences with proper syntax highlighting
const bucket = new aws.s3.BucketV2("my-bucket");

// ❌ DON'T: Use generic code blocks without language specification
```

## **Multi-Language Examples**

- Store in `/static/programs/` following naming: `<program-name>-<language>`
- Languages: `javascript`, `typescript`, `python`, `csharp`, `java`, `go`, `yaml`
- Use `{{< example-program path="program-name" >}}` shortcode
- Limit languages: `{{< example-program path="aws-s3" languages="typescript,python" >}}`

## **Code Snippets**

- Use `{{< example-program-snippet path="program-name" language="typescript" from="10" to="20" >}}`
- All examples must be complete, testable programs

---

# Frontmatter Standards

## **Required Fields**

---
title: "Page Title (60 char limit for SEO)"
meta_desc: "SEO description"
author: joe-duffy
---

## **Extended Frontmatter**

---
title: "Short Title for SEO"
allow_long_title: true  # Allows longer h1 display title
meta_image: meta.png  # Social sharing image (1200x628 PNG)
canonical_url: "https://canonical-source.com"  # For syndicated content
authors:
    - author-id
tags:
    - existing-tag-only  # Use existing tags, avoid creating new ones
aliases:
    - /old-url/
    - /another-old-url/
---


## **Blog-Specific Frontmatter**


---
date: 2024-01-15T10:00:00-07:00
meta_image: meta.png
authors:
    - author-id
tags:
    - pulumi-news  # Company news
    - aws  # Cloud providers (only major ones)
    - features  # Feature announcements
    - typescript  # Language-specific posts
---

---

# File Organization

## **Content Structure**
- `/content/` - All Markdown content
- `/content/blog/` - Blog posts with `_index.md` in subdirectories
- `/content/docs/` - Documentation content
- `/static/programs/` - Multi-language code examples
- `/static/images/` - Images and assets

## **Layout Structure**
- `/layouts/shortcodes/` - Custom Hugo shortcodes
- `/layouts/partials/` - Reusable template components
- `/theme/` - CSS/JS source files
- `/assets/` - Built CSS/JS assets (checked in)

## **Blog Posts**

```
content/blog/
├── my-post-slug/
│   ├── _index.md          # Main content
│   ├── meta.png           # Social sharing image
│   └── example-image.png  # Inline images
```

## **Code Examples**

```
static/programs/
├── aws-s3-bucket-typescript/
│   ├── index.ts
│   ├── package.json
│   └── Pulumi.yaml
├── aws-s3-bucket-python/
│   ├── __main__.py
│   ├── requirements.txt
│   └── Pulumi.yaml
```

---

# Images and Media

## **Blog Images**

- Place images in same directory as blog post
- Reference relatively: `![Alt text](image.png)`
- **Social images:** 1200×628 PNG, opaque background
- Use [Figma template](https://www.figma.com/file/TnD7nxjIxVvXq8w0W7awPG/Build-Your-Own-Meta-Image) for consistency

## **Animated GIFs**

- Max 1200px wide, 3MB size limit
- Optimize with Gifsicle: `gifsicle ./animation.gif --resize-width=1200 --optimize=3 --batch`

## **Team Images**

- Add to `/static/images/team/`
- Square JPG, 400x400 max, named with author ID

---

# Development Workflow

## **Local Development Commands**

**Important:** Do not change the package manager to pnpm in `package.json` - keep using Yarn for consistency.

```bash
make ensure          # Install all dependencies
make serve           # Start dev server (localhost:1313)
make serve-all       # Dev server + watch CSS/JS changes
make lint            # Check Markdown and formatting issues
make format          # Auto-format all files
make build           # Generate static site to ./public
make test            # Test all example programs (time-intensive)
```

## **Content Creation**

```bash
make new-blog-post              # Scaffold new blog post
make new-tutorial               # Create single-page tutorial
make new-tutorial-module        # Create multi-page tutorial
make new-example-program        # Generate multi-language example
```

## **Testing Code Examples**

Examples in `/static/programs/` are tested via:

1. **`pulumi preview`** - Default testing method
2. **Custom Makefile** - For non-standard testing needs

Test specific example: `ONLY_TEST="aws-s3-bucket-typescript" ./scripts/programs/test.sh`

## **Line Breaks and Formatting**

- **Semantic line breaks** preferred over hard wrapping
- **Never reflow paragraphs** - causes diff noise
- **One line per paragraph** or semantic breaks only
- **All new files must end with a newline** - required for consistency

---

# Hugo Template Development

## **Shortcode Creation**
Location: `layouts/shortcodes/my-shortcode.html`

```html
{{ $param := .Get 0 }}
{{ if not $param }}
    {{ errorf "%s Missing required parameter." .Path }}
{{ end }}

<div class="my-component">
    {{ .Inner | markdownify }}
</div>
```

## **Partial Templates**

Location: `layouts/partials/my-partial.html`

```html
{{ $context := . }}
<section class="my-section">
    {{ range .Params.items }}
        <div>{{ .title }}</div>
    {{ end }}
</section>
```

## **Common Hugo Patterns**

### **Conditional Content**

```html
{{ if .Params.show_section }}
    <section>Content here</section>
{{ end }}
```

### **Loops and Data**
```html
{{ range .Params.items }}
    <div>{{ .title }}</div>
{{ end }}
```

### **Partials and Includes**
```html
{{ partial "component-name.html" . }}
```

---

# Search and SEO

## **Algolia Search Indexing**

Content indexed includes:
- **Page titles** (`title` and `h1` frontmatter)
- **Meta descriptions** (`meta_desc` param)
- **H2 headings** in content
- **Keywords** (`search.keywords` param)
- **Authors and tags**

## **SEO Best Practices**

- **Strategic keyword placement** in titles, descriptions, and H2s
- **Canonical URLs** for syndicated content
- **Descriptive link text** (never "click here" or "read more")
- **Image alt text** for accessibility and SEO

---

# Common Issues and Solutions

## **Hugo Shortcode Nesting**
- Use `{{< >}}` for containers (no Markdown processing)
- Use `{{% %}}` for content that needs Markdown rendering
- **Never nest `{{% %}}`** shortcodes - causes double rendering

## **Image Optimization**

- **Blog images:** Place in post directory, reference relatively
- **Social images:** 1200x628 PNG, opaque background
- **GIFs:** Max 1200px wide, 3MB, optimize with Gifsicle

---

## Additional Resources

- **Full Style Guide:** [STYLE-GUIDE.md](STYLE-GUIDE.md)
- **Blogging Guide:** [BLOGGING.md](BLOGGING.md)  
- **Code Examples:** [CODE-EXAMPLES.md](CODE-EXAMPLES.md)
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md)

This repository powers one of the most comprehensive infrastructure-as-code documentation sites. Always prioritize **clarity, conciseness and accuracy** in content creation and maintenance.
