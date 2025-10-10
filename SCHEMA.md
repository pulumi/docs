# Schema.org Structured Data Reference

This document explains how structured data (schema.org markup) works on the Pulumi website.

## What is Structured Data?

Structured data helps search engines understand your content better, leading to:
- Rich search results (FAQs, events, articles)
- Better SEO and search visibility
- Enhanced AI citations (ChatGPT, Perplexity, Google AI Overviews)
- Improved content discoverability

## Schema Types Available

The site automatically generates appropriate schema.org markup based on content type. You can also explicitly control which schema type to use.

### Available Schema Types

| Schema Type | Schema.org Type | Use For | Example |
|------------|----------------|---------|---------|
| `blog` | BlogPosting | Blog posts | `/blog/my-post/` |
| `article` | TechArticle | Documentation, educational content | `/docs/`, `/what-is/` |
| `faq` | FAQPage | FAQ pages with Q&A pairs | `/docs/iac/faq/` |
| `howto` | HowTo | Step-by-step tutorials | `/tutorials/` |
| `product` | SoftwareApplication | Product pages | `/product/` |
| `event` | Event | Webinars, conferences, meetups | `/events/` |
| `auto` | (various) | Intelligent auto-detection | Default behavior |
| `none` | (none) | No schema markup | Special cases |

## How Auto-Detection Works

By default (or when `schema_type: auto`), the system automatically determines the appropriate schema based on:

### 1. Page Type Detection

```
- type: blog → BlogPosting
- type: tutorials → HowTo
- type: webinars → Event
- type: docs → TechArticle
- type: what-is → FAQPage (if questions found) or TechArticle (if no questions)
```

### 2. URL Pattern Detection

```
- /faq in URL → FAQPage
- "faq" or "frequently asked" in title → FAQPage
```

### 3. Section Detection

```
- section: product → SoftwareApplication
- section: case-studies → TechArticle
```

### 4. Smart Fallbacks

If a page is detected as FAQ but has no Q&A content, it automatically falls back to Article schema to prevent invalid structured data.

## Explicit Schema Declaration

You can override auto-detection by specifying `schema_type` in your page frontmatter:

### Basic Usage

```yaml
---
title: "My Page Title"
schema_type: faq
---
```

### When to Use Explicit Declaration

**Use explicit declaration when:**
- Auto-detection chooses the wrong schema type
- You want to be specific about SEO markup
- Content structure doesn't match typical patterns
- You need to prevent schema generation (`schema_type: none`)

**Leave as auto when:**
- Your content follows typical patterns
- Page type clearly indicates schema type
- You want the system to make intelligent decisions

### Examples

#### Force FAQ Schema (even if not auto-detected)

```yaml
---
title: "Common Questions About Pulumi"
schema_type: faq
---

## What is Pulumi?
Pulumi is an infrastructure as code platform...

## How does Pulumi work?
Pulumi uses familiar programming languages...
```

#### Prevent Schema Generation

```yaml
---
title: "Internal Planning Doc"
schema_type: none
---
```

#### Override Detection

```yaml
---
title: "Understanding Kubernetes"
type: docs  # Would normally get TechArticle
schema_type: howto  # Override to HowTo if it's step-by-step
---
```

## Content Requirements by Schema Type

### FAQPage Schema

**Requirements:**
- Must have H2 or H3 headers ending with `?`
- Each question must be followed by answer content
- Questions are extracted automatically from markdown

**Valid Question Formats:**
```markdown
## How do I install Pulumi?
Answer content here...

## What languages does Pulumi support?
Answer content here...
```

**Invalid (won't be detected):**
```markdown
## Installation Steps
This is not a question...

### Getting Started
Not a question either...
```

**Google Guidelines:**
- One answer per question
- Written by site (not user-submitted)
- Actually visible on the page
- Not for advertising purposes

[Learn more about FAQPage](https://developers.google.com/search/docs/appearance/structured-data/faqpage)

### Event Schema

**Auto-populated from frontmatter:**
- `main.title` → event name
- `main.sortable_date` → start date
- `main.duration` → duration
- `main.location` → location (physical or virtual)
- `main.presenters` → speakers/performers

**Example:**
```yaml
---
type: webinars
main:
    title: "Pulumi Workshop"
    sortable_date: 2025-03-15T10:00:00-07:00
    duration: "2 hours"
    location: "Seattle, WA"
    presenters:
        - name: "Jane Smith"
          role: "Developer Advocate"
---
```

[Learn more about Event schema](https://schema.org/Event)

### Article/TechArticle Schema

**Best for:**
- Documentation pages
- Educational content
- Technical guides
- Case studies

**Auto-populated from:**
- `title` → headline
- `meta_desc` → description
- `PublishDate` → datePublished
- `Lastmod` → dateModified

[Learn more about Article schema](https://developers.google.com/search/docs/appearance/structured-data/article)

### BlogPosting Schema

**Automatically applied to:**
- Pages with `type: blog` and `isPage: true`

**Includes:**
- Article metadata (title, dates, description)
- Author information
- Word count
- Images

[Learn more about BlogPosting](https://schema.org/BlogPosting)

### HowTo Schema

**Best for:**
- Step-by-step tutorials
- Procedural guides
- How-to content

**Auto-extracts:**
- Steps from markdown headers and content
- Duration if specified
- Prerequisites

[Learn more about HowTo schema](https://schema.org/HowTo)

## Testing Your Schema

### Google Rich Results Test

1. Build your page locally or deploy to staging
2. Visit [Rich Results Test](https://search.google.com/test/rich-results)
3. Enter your page URL
4. Check for errors or warnings

### Google Search Console

1. After deploying to production
2. Go to [Google Search Console](https://search.google.com/search-console)
3. Check "Enhancements" section for structured data issues
4. Monitor for "Missing field" or other errors

### Local Inspection

1. Run `make serve`
2. Visit your page at http://localhost:1313/your-page/
3. View page source
4. Look for `<script type="application/ld+json">`
5. Verify the JSON structure is valid and complete

## Common Issues and Solutions

### "Missing field 'mainEntity'" Error

**Problem:** FAQPage schema without questions

**Solution:** Either:
1. Add Q&A content (H2/H3 ending with `?`)
2. Set `schema_type: article` to use Article schema instead
3. The system now auto-falls back to Article if no questions found

### Multiple Schema Types Needed

**Problem:** Page could be both Article and FAQ

**Solution:** Choose the primary purpose:
- If primarily Q&A → use `faq`
- If primarily educational → use `article`
- Google prefers one primary schema type per page

### Schema Not Appearing

**Causes:**
1. Page type doesn't match any auto-detection rules
2. `schema_type: none` is set
3. Content doesn't meet requirements (e.g., FAQ with no questions)

**Solution:**
1. Check page frontmatter for `type` field
2. Add explicit `schema_type` if needed
3. Ensure content meets schema requirements

## For Developers

### Adding a New Schema Type

1. Create `layouts/partials/schema/collectors/[name]-entity.html`
2. Follow pattern from existing collectors (see `blog-entity.html`)
3. Add to `main-entity.html` explicit and auto-detection logic
4. Update this documentation
5. Add to archetype templates

### Schema Architecture

```
layouts/partials/schema/
├── collectors/
│   ├── main-entity.html          # Routes to appropriate schema
│   ├── article-entity.html        # TechArticle schema
│   ├── blog-entity.html           # BlogPosting schema
│   ├── faq-entity.html            # FAQPage schema
│   ├── howto-entity.html          # HowTo schema
│   ├── product-entity.html        # SoftwareApplication schema
│   ├── event-entity.html          # Event schema
│   ├── video-entity.html          # VideoObject (supplementary)
│   └── breadcrumb-entity.html     # BreadcrumbList (supplementary)
└── graph-builder.html             # Assembles @graph structure
```

### Schema is Generated as @graph

All schemas are assembled into a single JSON-LD `@graph` structure:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "BreadcrumbList", ...},
    {"@type": "BlogPosting", ...},
    {"@type": "Organization", ...},
    {"@type": "WebPage", ...}
  ]
}
```

## Additional Resources

- [Schema.org Documentation](https://schema.org/)
- [Google Search Central - Structured Data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Google Search Console](https://search.google.com/search-console)
- [SEO.md](./SEO.md) - SEO best practices including structured data
- [BLOGGING.md](./BLOGGING.md) - Blog post guidelines
