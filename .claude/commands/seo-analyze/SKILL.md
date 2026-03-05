---
description: Analyze content for search engine and AI discoverability. Use when writing new blog posts, documentation, or what-is pages, or when reviewing existing content for SEO and AEO (evaluates titles, meta descriptions, headings, and AEO patterns).
---

# /seo-analyze Command

**Use this when:** You're creating new content (blog post, documentation) or want to review existing content for visibility in traditional search (SEO) and AI answer engines (AEO/GEO).

## Usage

```
/seo-analyze <file-path>
```

**Examples:**
- `/seo-analyze content/blog/2026/01/my-post/index.md` - Analyze a blog post
- `/seo-analyze content/docs/esc/get-started/_index.md` - Analyze documentation
- `/seo-analyze content/what-is/infrastructure-as-code.md` - Analyze a what-is page

## Instructions for Claude

### Step 1: Detect target file

Determine the target file from (in order of priority):
1. Explicit file path argument
1. Currently open file in IDE context
1. Ask the user which file to analyze

If no file can be determined, use AskUserQuestion:
```
Which file would you like me to analyze?
```

### Step 2: Analyze current state

Read the target file and extract:

**Frontmatter:**
- `title` - Current title tag
- `meta_desc` - Current meta description
- `h1` - First H1 if different from title
- `date` - Publication date (for blog posts)
- `authors` - Author information (for blog posts)

**Content structure:**
- H1 and H2 headings
- Opening paragraph (first ~150 words)
- Presence of lists, tables, FAQ sections
- Internal links (count and anchor text quality)
- Word count and content depth

### Step 3: Evaluate AEO patterns

**Load reference:** Read `references/aeo-checklist.md`

Scan content against AI discoverability patterns. For each pattern, note what you observe -- not a binary verdict. Good content may not exhibit every pattern, and that's fine.

| Pattern | What to Look For |
|---------|------------------|
| **Quotable Definition** | Opening paragraph contains a clear, direct answer |
| **Semantic Chunking** | Each section covers one focused concept |
| **Citable Claims** | Factual statements include specific data |
| **Comparison Tables** | Structured tables for comparisons |
| **Question Coverage** | Content answers what/how/why/when |
| **Listicle Format** | Uses numbered/bulleted lists for key points |
| **E-E-A-T Signals** | Shows experience, expertise, authority, trust |
| **Down-Funnel Specificity** | Addresses specific use cases, integrations, edge cases |
| **Agent-Friendly Content** | Clear CTAs, numbered steps, executable actions |

### Step 4: Present analysis and recommendations

Present findings in a structured format:

---

## AEO Analysis: `[filename]`

### Summary

| Category | Score | Key Observations |
|----------|-------|------------------|
| AEO Readiness | X/10 | [observations] |

### Observations

For each AEO pattern, describe what you found. Focus on the patterns most relevant to this content type (see the Content Type Applicability table in `references/aeo-checklist.md`).

### Recommendations

Present educational suggestions the writer can consider. Focus on why each suggestion matters for search and AI discoverability, not just what to change.

**1. [Observation]**
- **Why it matters**: [How this affects search/AI visibility]
- **Suggestion**: [What the writer could consider]

**2. [Observation]**
- **Why it matters**: [How this affects search/AI visibility]
- **Suggestion**: [What the writer could consider]

**Note:** These are suggestions to consider, not mandatory changes. Good content may not check every box -- the goal is awareness of these patterns, not rigid compliance.

---

## Content type-specific guidance

### Blog posts

Additional considerations for blog content:
- **Recency signal**: Year in title or prominent placement
- **Author credibility**: Author has bio with relevant expertise
- **Social meta**: og:image, og:description present and not placeholders (verify `meta.png` is a real image)
- **Call to action**: Clear next step for readers

### Documentation

Additional considerations for docs:
- **Task orientation**: Helps users accomplish specific goals
- **Code examples**: If the content includes code, verify it appears functional and copy-pasteable
- **Prerequisites**: Clear about what users need to know/have
- **Next steps**: Links to related content

### What-is pages

Additional considerations for explainer content:
- **Definition first**: Clear definition in first paragraph
- **Comparison context**: How it relates to alternatives
- **Use cases**: When and why to use this
- **Getting started**: Path to hands-on experience

## Example output

```markdown
## AEO Analysis: `content/blog/2026/01/config-management/index.md`

### Summary

| Category | Score | Key Observations |
|----------|-------|------------------|
| AEO Readiness | 6/10 | Strong structure, missing quotable definition and E-E-A-T signals |

### Observations

- **Quotable Definition**: The opening paragraph introduces the topic but doesn't provide a standalone definition an AI tool could extract.
- **Semantic Chunking**: Good -- each H2 covers a distinct concept.
- **FAQ Sections**: Not present. Could be valuable given the topic has common evaluation questions.
- **Citable Claims**: Two specific data points found. Could benefit from more.
- **E-E-A-T Signals**: No author credentials or real-world usage examples visible.
- **Down-Funnel Specificity**: Covers general concepts well but doesn't address integration scenarios.

### Recommendations

**1. Opening paragraph lacks a quotable definition**
- **Why it matters**: AI answer engines extract opening paragraphs to answer "what is" queries. Without a clear, standalone definition, the content is less likely to be cited.
- **Suggestion**: Consider leading with a one-sentence definition of configuration management that could stand on its own if quoted.

**2. No FAQ section for common evaluation questions**
- **Why it matters**: Q&A format directly matches how users query AI tools. For a topic like configuration management, readers often have specific "does it work with X?" questions.
- **Suggestion**: Consider adding a FAQ section that addresses integration questions, migration concerns, or comparison criteria relevant to the topic.

**3. Limited E-E-A-T signals**
- **Why it matters**: Both Google and AI systems prefer citing sources that demonstrate real-world expertise. Author credentials and production experience increase citation likelihood.
- **Suggestion**: Consider adding author context or referencing real deployment scenarios where relevant.
```

## Integration notes

This skill is recommended as a follow-up to:
- `/new-blog-post` - After creating a new blog post
- `/glow-up` - After comprehensive content review
- Manual content creation - Before committing new documentation
