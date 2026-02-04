---
description: Enhance content for better search engine and AI discoverability. Works during content creation (proactive) or on existing content (reactive).
---

# /seo-enhance Command

**Use this when:** You're creating new content (blog post, documentation) or want to optimize existing content for better visibility in traditional search (SEO) and AI answer engines (AEO/GEO).

## Usage

```
/seo-enhance [file-path]
```

**Examples:**
- `/seo-enhance` - Analyze the currently open file
- `/seo-enhance content/blog/2026/01/my-post/index.md` - Analyze a specific file
- `/seo-enhance content/docs/esc/get-started/_index.md` - Analyze documentation

## Instructions for Claude

### Step 1: Detect Target File

Determine the target file from (in order of priority):
1. Explicit file path argument
2. Currently open file in IDE context
3. Ask the user which file to analyze

If no file can be determined, use AskUserQuestion:
```
Which file would you like me to analyze for SEO/AEO improvements?
```

### Step 2: Analyze Current State

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

### Step 3: Check AEO Patterns

**Load reference:** Read `references/aeo-checklist.md`

Evaluate against AI discoverability patterns:

| Pattern | Check | Status |
|---------|-------|--------|
| **Quotable Definition** | Opening paragraph contains a clear, direct answer | Pass/Fail |
| **Semantic Chunking** | Each section covers one focused concept | Pass/Fail |
| **FAQ Sections** | Common questions addressed in Q&A format | Pass/Fail/N/A |
| **Citable Claims** | Factual statements include specific data | Pass/Fail |
| **Comparison Tables** | Structured tables for comparisons | Pass/Fail/N/A |
| **Question Coverage** | Content answers what/how/why/when | Pass/Fail |

### Step 4: Check SEO Fundamentals

**Load reference:** Read `references/seo-checklist.md`

Evaluate against SEO best practices:

| Element | Guideline | Current | Status |
|---------|-----------|---------|--------|
| **Title** | Under 60 chars, includes primary keyword | [actual] | Pass/Fail |
| **Meta description** | Under 155 chars, compelling, includes keyword | [actual] | Pass/Fail |
| **H1** | Matches search intent, unique | [actual] | Pass/Fail |
| **H2s** | Include keyword variations | [list] | Pass/Fail |
| **Internal links** | Descriptive anchor text, relevant targets | [count] | Pass/Fail |

### Step 5: Check Positioning Alignment

**Load reference:** Read `references/pulumi-positioning.md`

For content promoting Pulumi capabilities, verify:

| Alignment | Check | Status |
|-----------|-------|--------|
| **Differentiators** | Emphasizes relevant advantages (real languages, unified platform, etc.) | Pass/Fail/N/A |
| **Jobs-to-be-Done** | Connects to customer outcomes | Pass/Fail/N/A |
| **Terminology** | Uses Pulumi's language, not competitor's | Pass/Fail |

### Step 6: Generate Recommendations

Present findings in a structured format:

---

## SEO/AEO Analysis: `[filename]`

### Summary

| Category | Score | Priority Items |
|----------|-------|----------------|
| AEO Readiness | X/6 | [top issues] |
| SEO Fundamentals | X/5 | [top issues] |
| Positioning | X/3 | [top issues] |

### Priority Recommendations

#### High Priority (Quick Fixes)

**1. [Issue]: [Current state]**
- **Problem**: [Why this matters]
- **Recommendation**: [Specific change]
- **Example**:
  ```
  Current: [current value]
  Proposed: [new value]
  ```

#### Medium Priority (Content Improvements)

**2. [Issue]: [Current state]**
- **Problem**: [Why this matters]
- **Recommendation**: [Specific change]
- **Suggested content**: [Brief outline or example]

#### Low Priority (Nice to Have)

**3. [Issue]**
- **Recommendation**: [Suggestion]

---

### Step 7: Offer to Apply Changes

After presenting recommendations, ask the user:

```
Would you like me to apply these changes?
- [A] Apply all recommendations
- [B] Apply high priority only
- [C] Let me choose specific changes
- [D] No changes - just wanted the analysis
```

If user approves changes:

1. Edit the file using the Edit tool
2. Make changes in order of priority
3. After each major change, briefly note what was modified
4. Run `make lint` to verify no issues introduced
5. Summarize all changes made

## Content Type-Specific Guidance

### Blog Posts

Additional checks for blog content:
- **Recency signal**: Year in title or prominent placement
- **Author credibility**: Author has bio with relevant expertise
- **Social meta**: og:image, og:description present
- **Call to action**: Clear next step for readers

### Documentation

Additional checks for docs:
- **Task orientation**: Helps users accomplish specific goals
- **Code examples**: Working, copy-pasteable code
- **Prerequisites**: Clear about what users need to know/have
- **Next steps**: Links to related content

### What-Is Pages

Additional checks for explainer content:
- **Definition first**: Clear definition in first paragraph
- **Comparison context**: How it relates to alternatives
- **Use cases**: When and why to use this
- **Getting started**: Path to hands-on experience

## Example Output

```markdown
## SEO/AEO Analysis: `content/blog/2026/01/config-management/index.md`

### Summary

| Category | Score | Priority Items |
|----------|-------|----------------|
| AEO Readiness | 3/6 | Missing quotable definition, no FAQ section |
| SEO Fundamentals | 4/5 | Title slightly long (67 chars) |
| Positioning | 2/3 | Could emphasize real programming languages |

### Priority Recommendations

#### High Priority

**1. Title too long (67 chars)**
- **Problem**: May be truncated in search results
- **Recommendation**: Shorten to under 60 characters
- **Example**:
  ```
  Current: "How to Implement Configuration Management with Pulumi and TypeScript"
  Proposed: "Configuration Management with Pulumi and TypeScript"
  ```

**2. Missing quotable definition**
- **Problem**: AI tools can't extract a clear answer
- **Recommendation**: Add a direct definition in the first paragraph
- **Suggested opening**:
  ```
  Configuration management is the process of maintaining systems,
  servers, and software in a desired, consistent state. Pulumi
  enables configuration management using real programming languages
  like TypeScript, Python, and Go.
  ```

#### Medium Priority

**3. No FAQ section**
- **Recommendation**: Add FAQ addressing common questions
- **Suggested questions**:
  - What is configuration management?
  - How does Pulumi handle configuration management?
  - What's the difference between configuration management and IaC?
```

## Integration Notes

This skill is recommended as a follow-up to:
- `/new-blog-post` - After creating a new blog post
- `/glow-up` - After comprehensive content review
- Manual content creation - Before committing new documentation
