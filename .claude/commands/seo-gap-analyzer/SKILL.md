---
description: Analyze content coverage gaps for specific topics and produce strategic plans to improve Pulumi's visibility in traditional search (SEO) and AI discovery (AEO/GEO).
---

# /seo-gap-analyzer Command

**Use this when:** You need to analyze content coverage gaps for a specific topic, keyword, or section of pulumi.com. Useful to identify visibility issues, competitors outranking Pulumi, or AI tools not mentioning Pulumi for relevant queries.

## Usage

```
/seo-gap-analyzer <topic-or-scope>
```

**Examples:**

- `/seo-gap-analyzer configuration management` - Analyze gap for a topic
- `/seo-gap-analyzer content/docs/esc/` - Analyze a documentation section
- `/seo-gap-analyzer https://pulumi.com/docs/iac/concepts/` - Analyze a specific page

## Instructions for Claude

This is a **hybrid skill**: research and plan first, then ask for approval before implementing changes.

### Phase 1: Intake and Context Gathering

Extract from the user's request:

- **Target**: Topic, keyword, URL, or content section to analyze
- **Scope**: Single page, section/topic, or cross-site competitive analysis
- **Goals**: What outcome is expected (rank higher, get AI citations, etc.)
- **Context**: Any Slack threads, competitor URLs, or product requirements provided

If critical context is missing, ask:

1. What specific search behavior should trigger Pulumi appearing?
2. What Pulumi capabilities solve the searcher's problem?
3. Are there specific competitors to benchmark against?

### Phase 2: Keyword Research

**Load reference:** Read `references/keyword-strategy.md` for the keyword classification framework.

For the target topic, identify keyword variants:

**Unbranded keywords (PRIMARY FOCUS):**

- Head term: `[topic]` (e.g., "configuration management")
- Long-tail: `[topic] + [modifier]` (e.g., "configuration management kubernetes")
- Intent variants: `[topic] tutorial`, `what is [topic]`, `[topic] tools`

**Branded keywords (SECONDARY):**

- `pulumi [topic]`
- `[topic] with pulumi`
- `pulumi vs [competitor] [topic]`

Prioritize unbranded keywords - they have higher volume and capture users earlier in the discovery journey.

**Identify "Money Prompts":**

Money prompts are high-value queries worth winning in AI tools. Identify them using these proxies:

- **Paid search winners**: Keywords competitors bid on (high commercial intent)
- **Sales call themes**: Questions prospects ask during evaluations
- **Support tickets**: Common questions from existing users
- **High-intent threads**: Reddit/HackerNews discussions about tool selection

Aim to identify 30-100 prompts worth winning for any major topic area. These become AEO targets.

### Phase 3: Current State Analysis

**For SEO (use WebSearch):**

Run searches for prioritized keywords:

1. `[topic]` - Pure unbranded head term
2. `[topic] infrastructure as code` - Category-qualified
3. `[topic] tutorial` / `[topic] guide` - Educational intent
4. `pulumi [topic]` - Branded

For each search, document:

- Pulumi's position (if ranking)
- Which URL ranks (note if `/registry/` - non-editable)
- Top 3 competitors and their content type
- SERP features present (featured snippet, PAA, video)

**For AEO (describe approach to user):**

Explain that AI tools (ChatGPT, Claude, Perplexity) should be tested with queries like:

- "What is [topic]?"
- "How do I use Pulumi for [topic]?"
- "Best tools for [topic] with infrastructure as code"

Document whether AI tools mention Pulumi and in what context.

**Reddit/Community Research:**

Mine Reddit and other developer communities for valuable insights:

- **Question phrasing**: How do users actually phrase their questions?
- **Edge cases**: What specific scenarios cause confusion?
- **Objections**: What concerns do people raise about Pulumi or alternatives?
- **Comparison criteria**: What factors do people use to evaluate tools?

Search relevant subreddits (r/devops, r/kubernetes, r/aws, r/terraform) for topic discussions. Turn findings into FAQ sections, comparison content, and use-case pages.

### Phase 4: Existing Content Audit

Use the Grep tool to search the repository for relevant content:

- Find pages mentioning the topic in content
- Check frontmatter for title and meta_desc fields containing the topic
- Identify which content sections (docs, blog, learn, what-is, product) cover the topic

**Categorize pages:**

- **EDITABLE**: `/content/docs/`, `/content/blog/`, `/content/learn/`, `/content/what-is/`, `/content/product/`
- **NON-EDITABLE** (different repo): Anything rendering to `/registry/*`

For each EDITABLE page, evaluate:

| Element | Check |
|---------|-------|
| Title | Includes primary keyword? Under 60 chars? |
| Meta description | Includes keyword? Under 155 chars? Compelling? |
| H1 | Matches search intent? |
| H2s | Include keyword variations? |
| Opening paragraph | Clear definition/answer? |
| Content depth | Comprehensive coverage? |
| Internal links | Well-connected to related content? |

### Phase 5: Gap Analysis

**Load reference:** Read `references/seo-aeo-sources.md` for authoritative best practices.

Categorize identified gaps:

| Gap Type | Description | Priority |
|----------|-------------|----------|
| **On-page optimization** | Pages with poor SEO elements | HIGH - Quick fix |
| **Content depth** | Pages that mention topic but lack depth | HIGH - Moderate effort |
| **Internal linking** | Pages exist but aren't connected | HIGH - Quick fix |
| **Keyword coverage** | No page targeting key unbranded terms | MEDIUM - New content |
| **AEO/GEO** | AI tools don't surface Pulumi | MEDIUM - Long-term |
| **Citation gaps** | Competitors cited but Pulumi is not | HIGH - Content opportunity |

**Citation Gap Mapping:**

For each target topic, document the current citation landscape:

1. **What gets cited?** - Which sources do AI tools currently reference for this topic?
2. **Why them?** - What makes those sources "path of least resistance" for AI?
3. **What's missing?** - What would Pulumi need to be the preferred citation?

Common citation gap patterns:
- Competitor has a dedicated page; Pulumi only mentions topic in passing
- Competitor content is more structured (tables, lists, clear definitions)
- Competitor content is more recent or comprehensive
- Pulumi content exists but isn't well-connected (poor internal linking)

### Phase 6: Strategic Plan

**Load reference:** Read `references/pulumi-positioning.md` for messaging alignment.

Produce a prioritized plan:

#### Executive Summary

- 2-3 sentence summary of gap and opportunity
- Primary unbranded keyword target
- Key existing page(s) to optimize

#### Priority 1: Existing Page Optimizations

For each page to optimize:

**Page: [URL]**
**File: `content/[path]/[file].md`**

| Element | Current | Proposed | Rationale |
|---------|---------|----------|-----------|
| Title | [current] | [new] | Include keyword per Google guidelines |
| Meta desc | [current] | [new] | Improve CTR |
| H1 | [current] | [new] | Match search intent |

**Content changes:**

- Add section: [H2 heading] - [description]
- Expand section: [existing H2] - [what to add]

**Internal links:**

- Link TO this page FROM: [pages with anchor text]
- Link FROM this page TO: [pages with anchor text]

#### Priority 2: Internal Linking Campaign

| Source Page | Anchor Text | Location |
|-------------|-------------|----------|
| `content/docs/[path].md` | [keyword-rich anchor] | [section] |

#### Priority 3: New Content (Only If Necessary)

Only recommend if existing pages cannot cover the keyword:

- **File path**: `content/[section]/[slug]/_index.md`
- **Target keyword**: [unbranded keyword]
- **Why new content**: [what gap this fills]
- **Content brief**: [H1, key H2s, main points]

#### Success Metrics

- Rank top 10 for "[unbranded keyword]" within 90 days
- Rank top 3 for "[branded keyword]" within 30 days
- AI tools cite Pulumi for "[topic]" queries

### Phase 7: Approval Gate

**CRITICAL**: Present the complete plan to the user and ask for approval before making any changes.

Use AskUserQuestion to confirm:

- Which recommendations to implement
- Any modifications to the plan
- Priority order for implementation

**Do NOT proceed to Phase 8 without explicit approval.**

### Phase 8: Implementation

After approval, implement changes:

1. Create a feature branch:

   ```bash
   git checkout -b seo/[topic]-optimization
   ```

2. Make approved changes:
   - Edit frontmatter (title, meta_desc)
   - Update markdown content
   - Add internal links using Hugo syntax:

     ```markdown
     [descriptive anchor text]({{< relref "/docs/path/to/page" >}})
     ```

3. Validate:

   ```bash
   make lint
   make serve  # Preview at http://localhost:1313
   ```

4. Commit with clear message:

   ```bash
   git add content/[files]
   git commit -m "SEO: Optimize [page] for '[keyword]'

   - Updated title to include '[keyword]'
   - Expanded [section] with [topic] coverage
   - Added internal links

   Target: Rank top 10 for '[keyword]'"
   ```

## Critical Constraints

1. **Never modify `/registry/*` pages** - They're in a separate repository (pulumi/registry)
2. **Optimize existing content first** - Existing pages have domain authority; new pages don't
3. **Focus on unbranded keywords** - Higher volume, earlier funnel, builds awareness
4. **Follow Google's guidelines** - See `references/seo-aeo-sources.md` for authoritative sources

## Example Triggers

- "We need better coverage for 'configuration management' - here's the Slack thread..."
- "Competitors are outranking us for '[term]', what can we do?"
- "AI tools don't mention Pulumi when asked about [capability]"
- "The Command provider should rank for 'configuration management' but it's in Registry"
