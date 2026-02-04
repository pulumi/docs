# SEO Fundamentals Checklist

Use this checklist to evaluate content for traditional search engine optimization. These are established best practices based on Google's official guidelines.

## On-Page SEO Elements

### 1. Title Tag

**Guidelines (per Google):**
- Under 60 characters (Google typically displays 50-60)
- Include primary keyword, preferably near the beginning
- Unique for each page
- Accurately describes the page content
- Compelling to encourage clicks

**Check:**
- [ ] Length under 60 characters
- [ ] Contains primary keyword
- [ ] Accurately reflects content
- [ ] Not duplicated elsewhere on site

**Good examples:**
```
Configuration Management with Pulumi | Tutorial
How to Use Pulumi ESC for Secrets Management
Infrastructure as Code: Getting Started Guide
```

**Bad examples:**
```
A Comprehensive Guide to Understanding and Implementing Modern Configuration Management Practices (too long)
Pulumi | Pulumi | Configuration (keyword stuffing)
Blog Post (not descriptive)
```

### 2. Meta Description

**Guidelines (per Google):**
- Under 155 characters (Google may truncate longer descriptions)
- Include primary keyword naturally
- Compelling call-to-action or value proposition
- Accurately summarizes page content
- Unique for each page

**Check:**
- [ ] Length under 155 characters
- [ ] Contains primary keyword
- [ ] Includes value proposition or CTA
- [ ] Accurately summarizes content

**Good examples:**
```
Learn how to manage infrastructure configuration with Pulumi using TypeScript, Python, or Go. Get started in minutes with our step-by-step guide.
```

**Bad examples:**
```
This is a blog post about configuration management. We will discuss various topics related to configuration management and how it works. (no value prop)
configuration management pulumi configuration management infrastructure (keyword stuffing)
```

### 3. H1 Heading

**Guidelines:**
- One H1 per page
- Matches or closely relates to title tag
- Addresses user's search intent
- Includes primary keyword naturally

**Check:**
- [ ] Single H1 on page
- [ ] Contains primary keyword
- [ ] Matches search intent
- [ ] Consistent with title tag

**Relationship to title:**
```yaml
title: "Configuration Management with Pulumi | Tutorial"  # In search results
h1: "Configuration Management with Pulumi"                 # On the page
```

### 4. H2 Headings (Subheadings)

**Guidelines:**
- Create logical content hierarchy
- Include keyword variations and related terms
- Use sentence case (per style guide)
- Help users scan and navigate content

**Check:**
- [ ] Logical hierarchy (H2 > H3 > H4)
- [ ] Include keyword variations
- [ ] Descriptive and scannable
- [ ] No skipped heading levels

**Good structure:**
```markdown
# Configuration Management with Pulumi        <- H1 (primary keyword)

## What is configuration management?          <- H2 (question variant)

## Benefits of configuration management       <- H2 (related term)

## How Pulumi handles configuration          <- H2 (branded variant)

### Using the Command provider               <- H3 (specific subtopic)

### Managing secrets with ESC                <- H3 (specific subtopic)
```

### 5. Internal Links

**Guidelines (per Google):**
- Use descriptive anchor text (not "click here")
- Link to relevant, related content
- Help users discover more content
- Distribute page authority throughout the site

**Check:**
- [ ] At least 2-3 internal links per page
- [ ] Descriptive anchor text
- [ ] Links to relevant content
- [ ] No broken links

**Good anchor text:**
```markdown
Learn more about [Pulumi ESC for secrets management]({{< relref "/docs/esc" >}}).
See our [getting started guide]({{< relref "/docs/get-started" >}}) for installation.
```

**Bad anchor text:**
```markdown
Learn more [here]({{< relref "/docs/esc" >}}).
[Click here]({{< relref "/docs/get-started" >}}) to get started.
```

### 6. Image Alt Text

**Guidelines:**
- Every image should have descriptive alt text
- Alt text should describe the image content, not just "image" or "screenshot"
- Include relevant keywords naturally where appropriate
- Keep alt text concise (under 125 characters)
- Decorative images can use empty alt (`alt=""`)

**Why it matters:**
- Accessibility: Screen readers use alt text for visually impaired users
- SEO: Search engines use alt text to understand image content
- Fallback: Displays when images fail to load

**Check:**
- [ ] All content images have descriptive alt text
- [ ] Alt text describes what the image shows
- [ ] Keywords included where natural
- [ ] Decorative images marked appropriately

**Good examples:**
```markdown
![Pulumi Cloud dashboard showing deployment history](dashboard-deployments.png)
![Architecture diagram of Pulumi ESC secrets flow](esc-architecture.png)
```

**Bad examples:**
```markdown
![image](dashboard.png)
![screenshot](screenshot1.png)
![](decorative-banner.png)  <!-- Missing alt text entirely -->
```

## SEO Scoring

| Element | Weight | Pass Criteria |
|---------|--------|---------------|
| Title Tag | High | Under 60 chars, includes keyword |
| Meta Description | High | Under 155 chars, includes keyword, has CTA |
| H1 Heading | High | Single H1, matches search intent |
| H2 Headings | Medium | Include keyword variations |
| Internal Links | Medium | 2+ links with descriptive anchors |
| Image Alt Text | Medium | Descriptive alt text on content images |

**Scoring:**
- 6/6: Excellent SEO fundamentals
- 5/6: Good, minor improvement needed
- 3-4/6: Fair, some gaps to address
- 1-2/6: Poor, significant issues

## Content-Specific Guidelines

### Blog Posts

Additional SEO considerations:
- **Date freshness**: Include year in title for timely topics
- **Author authority**: Author bio establishes expertise
- **Social sharing**: og:title, og:description, og:image
- **Related posts**: Link to other relevant blog content

### Documentation

Additional SEO considerations:
- **Navigation context**: Breadcrumbs and menu structure
- **Canonical URLs**: Avoid duplicate content issues
- **Version handling**: Noindex old versions if applicable
- **Code searchability**: Code examples are indexable text

### What-Is Pages

Additional SEO considerations:
- **Featured snippet optimization**: Definition in first paragraph
- **Related terms**: Link to related what-is pages
- **Comparison hooks**: Address "vs" queries
- **Getting started path**: Clear conversion path

## Hugo-Specific Implementation

### Frontmatter SEO Fields

```yaml
---
title: "Configuration Management with Pulumi"  # Title tag (required)
meta_desc: "Learn how to manage..."            # Meta description (required)
h1: "Configuration Management with Pulumi"     # H1 if different from title
---
```

### Internal Link Syntax

Always use Hugo's `relref` shortcode for internal links:

```markdown
[descriptive text]({{< relref "/docs/path/to/page" >}})
```

This ensures:
- Links work across environments
- Broken links caught at build time
- Proper URL generation

### Canonical URLs

Hugo handles canonical URLs automatically. Override if needed:

```yaml
---
canonical_url: "https://www.pulumi.com/docs/preferred-url/"
---
```
