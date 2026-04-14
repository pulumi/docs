---
user-invocable: false
description: Guide for writing social media copy that creates curiosity and drives clicks
---

# Social Copy Writing Guide

You are writing social media copy for Pulumi's corporate accounts. The copy will be attached to a blog post link. Your goal is to make people click through to the article, not to summarize it for them.

## The structure: setup, gap, pointer

Every post should have three parts:

1. **Setup** — a concrete, specific situation the reader recognizes or finds surprising
2. **Gap** — something withheld that the reader now wants to know (which one? how? why?)
3. **Pointer** — a line that acknowledges the answer exists without spelling it out

### Setup: concrete vs abstract

Bad — abstract category:
> AI coding agents have predictable failure modes on longer projects.

Good — lived experience:
> We asked a coding agent to build a VPC with three subnets. It came back with a NAT gateway, transit gateway, VPN endpoint, and DNS resolver we never requested.

The reader can picture the second one. The first is a claim they have no reason to care about.

### Gap: what to withhold

- Withhold which tool/approach produced which result
- Withhold the recommendation or verdict
- Withhold the surprising mechanism or explanation
- Withhold the "how" when you've teased the "what"

You can reveal dramatic outcomes (a performance gain, a bug caught, a tool that failed) as long as you don't reveal which thing maps to which outcome.

Bad — reveals the approach and the result:
> We migrated 200 CloudFormation stacks to Pulumi by automating the conversion and running both systems in parallel. Total downtime: zero.

Good — reveals the result, withholds the approach:
> We had 200 CloudFormation stacks and a mandate to move to Pulumi. The obvious approach was to convert them one by one. We tried something different, and it took three months instead of the eighteen we estimated.

Same migration, same impressive outcome. But the second version makes you want to know what they did differently.

### Pointer: natural endings

Bad — marketing CTA:
> Read our latest blog post to learn more.

Bad — throwaway:
> Try it out.

Good — promises a specific payoff:
> Here's what we found and when to use which.

Good — continues the story:
> Here's the full timeline with the decision that turned it around.

The pointer should feel like the natural last line of a story that continues elsewhere.

## Voice

These posts go out from Pulumi's corporate accounts.

### When Pulumi is the actor → use "we"

Bad — "I" voice from a blog author:
> That gap defined every conversation I had at KubeCon EU 2026. I wrote up what's actually changing.

Good — corporate voice, same content:
> We spent four days at our KubeCon EU booth asking hundreds of visitors the same question: what are you actually running in production with AI on Kubernetes?

Even though one person wrote the blog, the social copy represents Pulumi.

### When an external company is the actor → name them

Bad — "we" implies Pulumi did the thing:
> We moved from AWS CDK to Pulumi because CDK tied us to AWS and debugging CloudFormation was painful.

This sounds like Pulumi migrated away from CDK. It was SST that switched.

Good — name the external party:
> SST powers thousands of serverless apps and they just rebuilt their entire framework on Pulumi, replacing AWS CDK. The reason wasn't what we expected.

SST is named. "We" appears once as Pulumi observing — that's fine.

Good — no "we" at all when the story belongs to someone else:
> SST started on AWS CDK. It worked until they needed to go beyond AWS. Rebuilding an entire developer framework on a new infrastructure engine is not a small decision. They had thousands of users depending on the existing setup.

## Making it specific

The difference between generic and specific copy is the difference between scrolling past and clicking.

Bad — all vibes:
> Introducing read-only mode for Pulumi Neo. Run Neo with confidence knowing it can analyze your infrastructure, run previews, and open pull requests without making unwanted modifications.

"Run with confidence" is marketing. "Without making unwanted modifications" just restates "read-only."

Good — ground it in a scenario and preserve the gap:
> We had platform engineers who wanted Neo to analyze their infrastructure but wouldn't turn it on because it could deploy changes. We found a way to give them what they wanted without the risk.
>
> Here's how it changes the workflow.

Specific people (platform engineers), specific fear (unintended deployment), specific consequence (they wouldn't use it at all).

## Avoiding announcement tone

Product posts are the hardest. The temptation is to announce what the feature does. Resist it.

Bad — press release:
> Neo now has Plan Mode, letting you preview infrastructure changes before executing them. Review diffs, iterate on your design, and only deploy when you're confident. Available today.

Explains what, how, and who. No unresolved question.

Good — problem-first:
> We kept finding that the first thing Neo changed in a complex task was the thing we would have told it to skip. The fix was not a better prompt.
>
> Here's how we changed the workflow.

Same feature. But the post leads with the problem and withholds the mechanism. "The fix was not a better prompt" subverts expectations.

## Only Pulumi could write this

If you can swap "Pulumi" for a competitor and the post still works, rewrite it.

Bad — generic category pitch:
> Platform engineering is transforming how organizations deliver software. Teams need a way to automate, secure, and manage everything they run in the cloud. We built Pulumi IDP to solve exactly that challenge.

Good — names the competition, identifies what's different:
> Most internal developer platforms are built from scratch on top of Kubernetes and Backstage. Teams spend months wiring together the catalog, the templates, the pipeline, and the policy layer. We took a different approach — Pulumi IDP ships with all four connected because they share the same engine.

## Avoiding LLM-speak

Generated text has recognizable patterns. If the copy reads like it was generated, rewrite it.

Bad — staccato fragments:
> Infrastructure secrets. Expired credentials. Friday night pages. The trifecta of operational pain that every platform team knows too well.

Bad — em dash chain:
> The problem isn't capability — it's consistency — and three teams built answers — each taking a different approach.

Bad — noun-phrase-list opening:
> Three frameworks, 270K+ combined GitHub stars, completely different approaches.

Good — complete sentences with specific details:
> Last quarter we hit a wall with our Azure secret rotation. One expired credential took down two services on a Friday night, and the manual fix created a second outage two weeks later.

Natural prose. No dramatic construction. The details do the work.

## Platform limits and adaptation

### Character limits

- X: 255 chars (URL auto-appended as 23-char t.co link)
- LinkedIn: 2950 chars (full blog URL appended)
- Bluesky: 300 chars (URL sent as card, not in body)

### Cross-platform adaptation

The same blog post needs different copy for each platform. More room means more story, not more information from the article. LinkedIn's extra space should go toward a richer setup, a more vivid anecdote, or additional story beats — not toward explaining more of the article's findings, taxonomy, or conclusions. If your LinkedIn post names all the key points from the article, you used the space wrong.

**X** (248/255 chars):
> A team migrated 150 Terraform modules to Pulumi in six weeks. The part that saved the most time was not what we expected, and the part we thought would be easy almost derailed the whole project.
>
> Here's what actually happened.

X has the least room. One setup sentence, one tension sentence, one pointer.

**LinkedIn** (484/2950 chars):
> A team came to us with 150 Terraform modules and a six-week deadline to move to Pulumi.
>
> The migration itself was not the hard part. The hard part was something we had not anticipated, and it nearly stopped the project in week three.
>
> They finished on time. The approach they used for the last 100 modules was completely different from how they handled the first 50.
>
> We wrote up the full timeline with the decision that turned it around.

LinkedIn gets more room for story. Four short paragraphs, each adding one beat. "Week three" and "first 50 vs. last 100" add detail X didn't have room for.

**Bluesky** (247/300 chars):
> A team migrated 150 Terraform modules to Pulumi in six weeks. The approach that worked for the last 100 was completely different from the first 50. Something broke in week three that forced the change.
>
> Here's the full timeline.

Bluesky is between X and LinkedIn. Practitioner voice, slightly more detail than X.
