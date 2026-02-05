# AEO (Answer Engine Optimization) Checklist

Use this checklist to evaluate content for AI discoverability. AI answer engines (ChatGPT, Claude, Perplexity, Google AI Overviews) prefer content that is structured, authoritative, and easy to extract.

## Core AEO Patterns

### 1. Quotable Definition (Opening Paragraph)

**Why it matters:** AI tools extract opening paragraphs to answer "what is" queries. A clear, direct definition increases citation likelihood.

**Check:**
- First 1-2 sentences provide a clear, standalone definition
- Definition can be quoted without requiring surrounding context
- Avoids jargon or assumes minimal prior knowledge
- Under 50 words for the core definition
- **No hedging, no fluff** - direct answer without qualifiers

**Good example:**
```
Configuration management is the process of maintaining systems, servers,
and software in a desired, consistent state. It ensures that changes are
tracked, controlled, and can be reversed if needed.
```

**Bad examples:**

Fluffy intro (no direct answer):
```
In this article, we'll explore how modern teams are approaching the
challenge of keeping their infrastructure consistent. Let's dive in!
```

Hedging language (avoids commitment):
```
Configuration management can mean different things depending on context.
It depends on your specific needs, but generally speaking, it might involve...
```

### 2. Semantic Chunking

**Why it matters:** AI systems extract self-contained meaning units. Each section should address one specific concept.

**Check:**
- Each H2 section covers a single, focused topic
- Paragraphs are 2-4 sentences (not walls of text)
- Sections can be understood in isolation
- Clear topic sentences at the start of sections

**Good structure:**
```markdown
## What is Configuration Management?
[Definition and explanation - one concept]

## Benefits of Configuration Management
[List of benefits - one concept]

## How Pulumi Handles Configuration Management
[Pulumi-specific approach - one concept]
```

**Bad structure:**
```markdown
## Introduction
[Mixes definition, history, benefits, and tools in one section]
```

### 3. FAQ Sections (Doubt-Removers)

**Why it matters:** Q&A format directly matches how users query AI tools. FAQs should target "doubt-removers" - the specific questions that block purchase decisions.

**Check:**
- Questions target high-stakes evaluation criteria (not general education)
- Answers are direct and complete (2-4 sentences)
- Structure matters more than schema markup for LLM extraction

**Priority FAQ topics (doubt-removers):**
- **Integrations**: "Does Pulumi work with X?" / "Can I use Pulumi with Kubernetes?"
- **Limits/constraints**: "What are the limits?" / "How many resources can I manage?"
- **Pricing/billing**: "How does pricing work?" / "Is there a free tier?"
- **Security/compliance**: "Is Pulumi SOC 2 compliant?" / "How are secrets stored?"
- **Migration**: "How do I migrate from Terraform?" / "Can I import existing resources?"

**Good format:**
```markdown
## Frequently Asked Questions

### What is the difference between configuration management and IaC?
Configuration management focuses on maintaining the state of existing
systems, while Infrastructure as Code (IaC) provisions and manages
the infrastructure itself. Pulumi bridges both by using real
programming languages for infrastructure that can also manage
configuration.

### How do I get started with configuration management in Pulumi?
Start by installing Pulumi and creating a new project with
`pulumi new`. Then define your configuration using TypeScript,
Python, Go, or another supported language.
```

### 4. Citable Claims with Specific Data

**Why it matters:** AI tools prefer citing sources with specific, verifiable data over vague claims.

**Check:**
- Factual claims include specific numbers, dates, or metrics
- Statistics are attributed to sources
- Comparisons use concrete data points
- Avoids vague superlatives ("very fast", "many users")

**Good examples:**
```
Pulumi supports over 290 cloud and SaaS providers.
Teams using Pulumi report 3-5x faster deployments.
Founded in 2017, Pulumi has 8+ years of infrastructure intelligence.
```

**Bad examples:**
```
Pulumi supports many cloud providers.
Pulumi makes deployments much faster.
Pulumi has been around for a long time.
```

### 5. Comparison Tables

**Why it matters:** AI systems easily parse structured tables. Comparison content ranks highly for "vs" and "best" queries.

**Check:**
- Use markdown tables for feature comparisons
- Include clear column headers
- Keep cells concise (1-5 words ideal)
- Cover 3-5 key comparison points

**Good format:**
```markdown
| Feature | Pulumi | Terraform | CloudFormation |
|---------|--------|-----------|----------------|
| Languages | TypeScript, Python, Go, C#, Java | HCL only | YAML/JSON |
| Multi-cloud | Yes | Yes | AWS only |
| Testing | Native language testing | Limited | Limited |
| IDE Support | Full (IntelliSense, debugging) | Basic | Basic |
```

### 6. Question Coverage (What/How/Why/When)

**Why it matters:** Users query AI tools with different intents. Comprehensive content addresses multiple question types.

**Check:**
- **What**: Definition and explanation covered
- **How**: Implementation steps or tutorial included
- **Why**: Benefits and use cases explained
- **When**: Appropriate scenarios described

**Question mapping:**
```markdown
## What is [Topic]?          <- Answers "what is" queries
## Why Use [Topic]?          <- Answers "why should I" queries
## How to Implement [Topic]  <- Answers "how do I" queries
## When to Use [Topic]       <- Answers "when should I" queries
```

### 7. Listicle Format

**Why it matters:** Research shows listicles make up 32% of all AI citations (SEOMator analysis of 177 million citations). AI systems prefer extracting from single comprehensive sources with clear, numbered or bulleted lists.

**Check:**
- Content includes numbered or bulleted lists where appropriate
- List items are self-contained and extractable
- Lists summarize key points, steps, or options
- "Top X" or "X ways to" format for relevant content

**Good formats:**
```markdown
## 5 Benefits of Configuration Management

1. **Consistency**: Ensures all systems maintain the same state
2. **Auditability**: Track all changes with version control
3. **Reproducibility**: Recreate environments reliably
4. **Compliance**: Meet regulatory requirements automatically
5. **Efficiency**: Reduce manual configuration errors

## Key Features of Pulumi ESC

- **Hierarchical configuration**: Inherit and override settings
- **Dynamic secrets**: Pull from external providers at runtime
- **Environment composition**: Combine multiple config sources
- **Access control**: Fine-grained permissions per environment
```

**When to use:**
- "Best practices" content
- Feature comparisons
- Step-by-step guides
- Benefits/advantages summaries
- Tool or option roundups

### 8. E-E-A-T Signals (Experience, Expertise, Authoritativeness, Trustworthiness)

**Why it matters:** Google's quality guidelines emphasize E-E-A-T as a key factor in content evaluation. AI systems similarly prefer citing sources that demonstrate clear expertise and authority.

**Check:**
- **Experience**: Content shows real-world usage (code examples, screenshots, case studies)
- **Expertise**: Author credentials visible, technical depth appropriate to topic
- **Authoritativeness**: Citations to official docs, industry recognition, backlinks
- **Trustworthiness**: Accurate information, recent updates, transparent about limitations

**Good signals:**
```markdown
<!-- Experience -->
In our production deployment at [Company], we reduced deployment time by 40%...
Here's the actual Pulumi code we use to manage our Kubernetes clusters:

<!-- Expertise -->
Authors: jane-doe (Senior Platform Engineer, 8 years IaC experience)

<!-- Authoritativeness -->
Per Google's official documentation: "..."
As recommended in the CIS Kubernetes Benchmark...

<!-- Trustworthiness -->
Last updated: January 2026
Note: This approach works for Pulumi v3.x. For v2.x, see [migration guide].
```

**Content indicators:**
- Author bios with relevant credentials
- "Last updated" dates on technical content
- Links to official documentation and standards
- Real code examples from production use
- Acknowledgment of edge cases or limitations

### 9. Down-Funnel Specificity

**Why it matters:** AEO skews heavily toward "down-funnel, specific, messy" questions - integrations, workflows, edge cases, comparisons. These are the queries where LLMs need authoritative answers most, and where generic content fails.

**Check:**
- Content addresses specific use cases, not just general concepts
- Covers integrations with other tools/platforms
- Documents edge cases and workarounds
- Addresses real evaluation criteria buyers have

**High-value content types:**
- Integration guides ("Pulumi + Kubernetes + ArgoCD")
- Workflow documentation ("CI/CD with Pulumi and GitHub Actions")
- Edge case coverage ("Handling state drift", "Managing large stacks")
- Comparison content ("Pulumi vs Terraform for multi-cloud")
- Migration guides ("Moving from CloudFormation to Pulumi")

**Bad example (too generic):**
```
Pulumi is an infrastructure as code platform. It helps you manage cloud resources.
```

**Good example (specific, actionable):**
```
To deploy a Kubernetes application with Pulumi and ArgoCD, first create a
Pulumi program that defines your Kubernetes resources, then configure ArgoCD
to watch your Git repository for changes. Here's a working example...
```

### 10. Agent-Friendly Content

**Why it matters:** AI agents increasingly complete tasks, not just answer questions. Content should include clear, executable steps that an agent could follow or recommend.

**Check:**
- Clear CTAs with specific next steps
- Numbered steps for executable actions
- Well-defined tasks with concrete outcomes
- Commands and code that can be copied/executed

**Good format:**
```markdown
## Get started in 3 steps

1. **Install the Pulumi CLI**
   ```bash
   curl -fsSL https://get.pulumi.com | sh
   ```

2. **Create a new project**
   ```bash
   pulumi new typescript
   ```

3. **Deploy your infrastructure**
   ```bash
   pulumi up
   ```
```

**Why this works for agents:**
- Each step has a concrete action
- Commands are copy-pasteable
- Success criteria is clear (infrastructure deployed)
- No ambiguity about what to do next

## AEO Scoring

| Pattern | Weight | Pass Criteria |
|---------|--------|---------------|
| Quotable Definition | High | Clear definition in first 2 sentences, no hedging |
| Semantic Chunking | High | Single concept per section |
| FAQ Sections | Medium | Targets doubt-removers (integrations, limits, security, migration) |
| Citable Claims | Medium | 3+ specific data points |
| Comparison Tables | Medium | At least 1 table (where appropriate) |
| Question Coverage | Medium | Addresses 3+ question types |
| Listicle Format | Medium | Uses lists for key points (where appropriate) |
| E-E-A-T Signals | High | Shows experience, expertise, authority, trust |
| Down-Funnel Specificity | High | Covers integrations, edge cases, specific workflows |
| Agent-Friendly Content | Medium | Clear CTAs, numbered steps, executable actions |

**Scoring:**
- 10/10: Excellent AEO readiness
- 8-9/10: Good, minor improvements needed
- 5-7/10: Moderate, some gaps to address
- 0-4/10: Poor, major restructuring needed

## Content Type Applicability

| Pattern | Blog | Docs | What-Is | Tutorial |
|---------|------|------|---------|----------|
| Quotable Definition | Required | Required | Required | Optional |
| Semantic Chunking | Required | Required | Required | Required |
| FAQ Sections | Recommended | Optional | Recommended | Optional |
| Citable Claims | Recommended | Recommended | Required | Optional |
| Comparison Tables | Optional | Optional | Recommended | Optional |
| Question Coverage | Recommended | Optional | Required | Optional |
| Listicle Format | Recommended | Recommended | Recommended | Required |
| E-E-A-T Signals | Required | Recommended | Required | Recommended |
| Down-Funnel Specificity | Recommended | Required | Recommended | Required |
| Agent-Friendly Content | Recommended | Required | Recommended | Required |
