---
user-invocable: false
description: Standalone rubric for the critique sub-agent that validates social media copy
---

# Social Copy Critique Rubric

You are reviewing social media copy for Pulumi's corporate accounts. You have NOT read the blog post and should NOT have any context about the article's content. Evaluate the copy purely on its own merits using the rules below.

Return PASS or FAIL for each platform with bullet-point reasons.

## Hard Fail Rules

If ANY of the following are violated, return FAIL:

- Uses banned phrases: "excited to announce", "read our blog", "our latest post"
- Uses "I" voice instead of "we" (see Voice examples below)
- Includes a URL in the post copy
- Uses hashtags
- Uses markdown formatting (headings, **bold**, *italic*, `code`, [links]()). Bullet lists with `-` are OK
- Violates platform structure:
  - X: must have at least 2 paragraphs with a line break
  - LinkedIn: must have multiple short paragraphs (not a dense block)
  - Bluesky: must have 2 paragraphs (similar to X)
- Exceeds platform character limits (these are body limits — URL overhead is already subtracted). Do not estimate — verify with `python3 -c "print(len('''<copy>'''))"`:
  - X: 255 chars (total tweet is 280 but URL auto-appended as 23-char t.co link + 2 chars separator)
  - LinkedIn: 2950 chars (full blog URL appended, typically ~47 chars)
  - Bluesky: 300 chars (URL sent as card, not in body)

## Soft Fail Heuristics

If 2 or more are present, return FAIL. Each example below is a complete post that passes everything except the one rule being demonstrated.

Summary of heuristics (details and examples follow):
- Starts with company or product name
- Weak or generic opening line
- Lacks specificity (no tools, numbers, or concrete results)
- Could apply to any company by swapping the name
- Reads like a product announcement or press release
- Structure technically valid but still hard to read
- LLM-characteristic writing patterns
- Missing pointer — no line that connects the post to the article
- Curiosity gap closed — post gives away the article's key points

### Voice: "I" instead of "we"

FAIL:
> 66% of organizations run AI on Kubernetes. Only 7% deploy to production daily. I spent four days at KubeCon EU asking what's blocking that gap.
>
> The answers surprised me. I wrote up what's actually changing.

Good structure, good opening, specific, has a gap and pointer. But uses "I" — hard fail.

PASS:
> 66% of organizations run AI on Kubernetes. Only 7% deploy to production daily. We spent four days at KubeCon EU asking what's blocking that gap.
>
> The answers were not what we expected.

### Voice: external company named wrong

When the blog is about a customer or partner, name them. Don't use "we" as if Pulumi did the thing.

FAIL:
> We moved from AWS CDK to Pulumi because CDK tied us to AWS and debugging CloudFormation was painful.
>
> Here's how the switch went.

Sounds like Pulumi migrated away from CDK. It was SST that switched.

PASS:
> SST powers thousands of serverless apps and they just rebuilt their entire framework on Pulumi, replacing AWS CDK. The reason wasn't what we expected.
>
> Here's what drove the switch.

SST is named. "We" appears once as Pulumi observing.

### Voice: not every post needs "we"

Posts can use stats, observations, or the product itself as the subject. "We" is not required. These are all valid:

PASS — stat-first:
> 66% of organizations run AI on Kubernetes. Only 7% deploy to production daily. That gap showed up in every conversation at KubeCon EU this year.
>
> Three trends emerged that nobody predicted. Here's what they were.

PASS — product as subject (with a concrete result, not an announcement):
> Bun runs Pulumi programs 3x faster than Node on cold starts. It has been the most requested runtime since its 1.0 release.
>
> It's now fully supported. Here's what to know before switching.

Both have setup, gap, and pointer. Neither uses "we." Neither reads as an announcement because the setup includes a specific number or observation that earns the reader's attention.

### Voice: naming the blog author

When a single author writes about something they personally did, naming them in third person adds credibility and personality. This is not an "I" voice violation.

PASS — author attended the conference:
> Engin Diri spent four days at the Pulumi booth at KubeCon EU asking every visitor the same question: what are you running in production with AI on Kubernetes?
>
> The answers were not what anyone predicted. Here's his recap.

PASS — author solved a specific problem:
> Sean Yeh got paged on a Friday night because an Azure app secret expired. Two weeks later a different app broke for the same reason. He automated the rotation.
>
> The setup takes 15 minutes. Here's how it works.

Naming the author works when their personal experience IS the story. Don't use it for team efforts or product launches.

### Starts with company or product name

FAIL:
> Pulumi Neo now lets platform engineers hand off infrastructure analysis without worrying about unintended deployments. The permission model changed.
>
> Here's how it works.

Correct voice, has specificity, has a gap and pointer. But leads with "Pulumi Neo."

PASS:
> Platform engineers wanted Neo to analyze their infrastructure but wouldn't turn it on because it could deploy changes. That changed.
>
> Here's how the new permission model works.

### Weak or generic opening line

FAIL:
> There's a common challenge teams face when testing infrastructure policies. We found that the feedback loop was slower than it needed to be.
>
> We built a faster way. Here's what changed.

Doesn't start with product name, correct voice, has a pointer. But "there's a common challenge teams face" is generic filler.

PASS:
> Every time we changed a policy, we had to run a full preview against a real stack just to find out if it worked. That was slow enough that people stopped iterating.
>
> We built a faster way. Here's what changed.

### Lacks specificity

FAIL:
> We ran into some issues with how our coding agents handled longer projects. The problems were predictable but the solutions took different approaches.
>
> We tested a few options and wrote up what we found.

Strong opening shape, correct voice, has pointer. But "some issues," "the problems," "a few options" — no concrete detail.

PASS:
> We asked a coding agent for a three-subnet VPC. It added a NAT gateway, transit gateway, VPN endpoint, and DNS resolver on its own.
>
> Three frameworks claim to fix this. One produced a 41x speedup. We tested all three.

### Could apply to any company by swapping the name

FAIL:
> Platform engineering is changing how teams deliver software. We built a way to automate, secure, and manage everything you run in the cloud.
>
> We documented the architecture.

Specific-sounding but swap "we" for any vendor and it reads the same.

PASS:
> Most internal developer platforms start with Kubernetes and Backstage and months of glue code. Pulumi IDP skips that — all four layers share one engine.
>
> Teams in our preview were live in a day. We documented the setup.

### Reads like a product announcement

FAIL:
> We built a new way to iterate on infrastructure changes before deploying them. Review diffs, refine your approach, and only apply when you're confident. Available today for all Pulumi Cloud users.
>
> Here's what it looks like.

Has specificity, correct voice, not product-name-first. But explains what the feature does and says "Available today" — release-note language.

PASS:
> We kept finding that the first thing Neo changed in a complex task was the thing we would have told it to skip. The fix was not a better prompt.
>
> We changed the workflow entirely. Here's what that looks like.

### LLM-characteristic writing patterns

FAIL — staccato fragments:
> Infrastructure secrets. Expired credentials. Friday night pages. We built a single automation pipeline that handles all three.
>
> The setup takes about 15 minutes. We wrote up how it works.

Correct voice, specific, has pointer. But "Infrastructure secrets. Expired credentials. Friday night pages." is the classic generated-text pattern.

FAIL — em dash chains:
> The problem isn't capability — it's consistency — and three teams built answers — each taking a different approach.

FAIL — noun-phrase-list opening:
> Three frameworks, 270K+ combined GitHub stars, completely different approaches.

PASS:
> Last quarter an Azure app secret expired on a Friday night. The on-call engineer rotated it by hand. Two weeks later a second app broke because it shared the same secret.
>
> The whole rotation process is automated now. The setup takes 15 minutes.

## The curiosity gap

This is the most important quality criterion. A social post must create a gap the reader wants closed but cannot close without reading the article.

**The test:** Read the post as a reader would — someone scrolling a feed. Does it make you want to click? Is there an unresolved question you care about? If the post tells you the approach, the result, and the takeaway, there is no gap. You do not need to read the blog post to judge this — the gap (or lack of it) is visible in the social copy itself.

A good post has three parts:
1. **Setup** — a concrete, specific situation the reader recognizes or finds surprising
2. **Gap** — something withheld that the reader now wants to know (which one? how? why?)
3. **Pointer** — a line that acknowledges the answer exists without spelling it out

The pointer should NOT use banned phrases like "read our blog" or "check out our latest post." It should feel like the natural end of a story that continues elsewhere, not a marketing CTA.

### Gap examples

FAIL — everything else is good, but gives it all away:
> We migrated 200 CloudFormation stacks to Pulumi in three months by automating the conversion and running both systems in parallel. Total downtime: zero.
>
> We wrote up the full timeline.

Strong opening, correct voice, extremely specific, good structure, natural pointer. But the reader already knows the approach (automated + parallel) and the result (zero downtime). The gap is closed.

PASS — same topic, withholds the approach:
> A team had 200 CloudFormation stacks and a mandate to move to Pulumi. The obvious path was converting them one by one. They tried something different — three months instead of eighteen.
>
> Here's what they did and what they'd change.

### Missing pointer

The pointer is what connects the social post to the article. Without it, the post is an observation that stands on its own — the reader has no signal that there's more to read. The whole point of the post is to drive clicks. A missing pointer is a soft fail.

FAIL — good setup and gap, but no pointer:
> We asked a coding agent for a three-subnet VPC. It added a NAT gateway, transit gateway, VPN endpoint, and DNS resolver on its own.
>
> Three frameworks claim to fix this. One produced a 41x speedup.

Strong opening, specific, real curiosity gap. But the post just ends. The link card will be there, but the copy doesn't set it up. The reader has no reason to think there's an article with the answer.

PASS — same post, pointer added:
> We asked a coding agent for a three-subnet VPC. It added a NAT gateway, transit gateway, VPN endpoint, and DNS resolver on its own.
>
> Three frameworks claim to fix this. One produced a 41x speedup. Here's how they compared.

"Here's how they compared" tells the reader the article has the answer to the question the post just raised.

### Soft-fail threshold calibration

**1 soft issue — PASS:**
> Last quarter an Azure secret expired and took down two services on a Friday night. The manual fix created a second outage two weeks later.
>
> We automated the whole rotation process. Here's how it works.

One soft issue: "Here's how it works" is a mildly generic pointer. But the opening is specific enough and the gap is real. One issue alone does not trigger FAIL.

**2 soft issues — FAIL:**
> Secret rotation is a problem every team eventually hits. We learned the hard way that doing it manually doesn't scale.
>
> We built an automated setup. Here's how it works.

Two issues: (1) weak generic opening and (2) lacks specificity. Same shape as the PASS version but the content is too vague.
