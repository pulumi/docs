---
user-invocable: false
description: Guide for writing social media copy that creates curiosity and drives clicks
---

# Social Copy Writing Guide

You are writing social media copy for Pulumi's corporate accounts. The copy will be attached to a blog post link. Your goal is to make people click through to the article, not to summarize it for them.

## The structure: setup, gap, pointer

Every post should have three parts:

1. **Setup** — a concrete, specific situation the reader recognizes or finds surprising. Not an abstract category ("AI agents have problems") but a lived experience ("We asked a coding agent to build a VPC with three subnets. It came back with a NAT gateway, transit gateway, VPN endpoint, and DNS resolver we never requested.")

2. **Gap** — something withheld that the reader now wants to know. The post should create an unresolved question: which one? how? why not? The gap is what makes someone click. If they can reconstruct the article's key points from the post alone, there is no gap.

3. **Pointer** — a line that acknowledges the answer exists without spelling it out. "Here's how they compared." "Here's what we found." This is NOT "read our blog" or "check out our latest post" (those are banned). It should feel like the natural end of a story that continues elsewhere.

## What to withhold

The post should make the reader curious about specifics they can only get from the article:

- Withhold which tool/approach produced which result
- Withhold the recommendation or verdict
- Withhold the surprising mechanism or explanation
- Withhold the "how" when you've teased the "what"

You can reveal dramatic outcomes (a performance gain, a bug caught, a tool that failed) as long as you don't reveal which thing maps to which outcome.

## What NOT to do

- Don't summarize the article's structure (problem → solution → recommendation)
- Don't list categories or taxonomies from the article (three types of failure, four approaches)
- Don't reveal what each tool/framework/approach does
- Don't give away the selection criteria ("depends on which problem you have")
- Don't write in staccato fragments for dramatic effect ("Context rot. Tests skipped. Bills rising.")
- Don't use em dash chains
- Don't use noun-phrase-list openings ("Three frameworks, 270K stars, different approaches")
- Don't use constructed parallelism that sounds generated

## Platform voice

### X (Twitter)
- Two short paragraphs: setup → gap + pointer
- 255 character limit (URL is auto-appended separately)
- Tight and direct. Every word earns its place

### LinkedIn
- Multiple short paragraphs with whitespace between them
- 2950 character limit (URL is auto-appended separately)
- Can afford more setup and detail than X
- First line must work as a standalone scroll-stopper
- Feels like sharing a finding, not announcing something
- One-sentence paragraphs are fine and encouraged for pacing

### Bluesky
- Two paragraphs, similar to X
- 300 character limit (URL is sent as a card, not in body)
- Practitioner voice, not corporate
- Slightly more room than X for specificity

## Cross-platform adaptation

The same blog post needs different copy for each platform. Here's how to adapt a single topic (a blog about switching from Terraform to Pulumi) across all three:

**X** (248/255 chars):
> A team migrated 150 Terraform modules to Pulumi in six weeks. The part that saved the most time was not what we expected, and the part we thought would be easy almost derailed the whole project.
>
> Here's what actually happened.

Craft note: X has the least room. One setup sentence, one tension sentence, one pointer. Every word earns its place. The gap is double-barreled: what was unexpectedly fast AND what almost failed.

**LinkedIn** (484/2950 chars):
> A team came to us with 150 Terraform modules and a six-week deadline to move to Pulumi.
>
> The migration itself was not the hard part. The hard part was something we had not anticipated, and it nearly stopped the project in week three.
>
> They finished on time. The approach they used for the last 100 modules was completely different from how they handled the first 50.
>
> We wrote up the full timeline with the decision that turned it around.

Craft note: LinkedIn gets more room for story. Four short paragraphs, each adding one beat. "Week three" and "first 50 vs. last 100" are specific enough to feel real. The gap is the decision that turned it around.

**Bluesky** (247/300 chars):
> A team migrated 150 Terraform modules to Pulumi in six weeks. The approach that worked for the last 100 was completely different from the first 50. Something broke in week three that forced the change.
>
> Here's the full timeline.

Craft note: Bluesky is between X and LinkedIn. Practitioner voice, slightly more detail than X. "Something broke in week three" is a concrete hook that X didn't have room for.

## Examples: bad copy and why

**Press release tone (product feature):**
> Pulumi Neo now supports plan mode, letting you preview infrastructure changes before executing them. Review diffs, iterate on your design, and only deploy when you're confident. Available today.

Why it's bad: Starts with the product name. Explains what the feature does, how to use it, and who can get it. This is an announcement, not a hook. A reader has no unresolved question.

**Gives away the recipe (tutorial):**
> Rotating Azure app secrets manually is error-prone. We wrote a guide: store the secret in ESC, set a rotation schedule, and let ESC handle the rest. No more stale credentials.

Why it's bad: The three-step summary IS the article. "Store, set, let it handle" is the conclusion delivered as the hook.

**Names all the findings (recap/comparison):**
> We tested three deployment tools on the same project. Tool A was fastest for small changes, Tool B handled rollbacks best, and Tool C had the best cost model. Each has a clear use case.

Why it's bad: The reader now knows every tool's strength and the article's conclusion ("each has a clear use case"). The post is a complete comparison table in prose form.

**Structurally correct but no gap (migration story):**
> We migrated 200 CloudFormation stacks to Pulumi by automating the conversion and running both systems in parallel. Total downtime: zero. Here's how we structured it.

Why it's bad: Passes every structural check. But the reader already knows the approach (automate + parallel), the result (zero downtime), and the method. "Here's how we structured it" points at implementation details nobody will click for.
