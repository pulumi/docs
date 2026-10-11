---
user-invocable: false
description: Guide for writing social media copy that tees up the article without delivering it
---

# Social Copy Writing Guide

You are writing social media copy for Pulumi's corporate accounts. The copy will be attached to a blog post link. **Tee up the article. Don't deliver it.** The post sets up what the article reveals — the reveal stays in the article.

A useful frame: a social post is the back-cover blurb, not the last chapter. The blurb makes you want the book; it doesn't tell you who the killer is.

**Bad — gives away the killer:**
> We tested three AI coding frameworks on the same Pulumi project. Superpowers' TDD discipline drove the chardet 41x rewrite. GSD's phase-based orchestrators kept context fresh through long sessions. GSTACK's 23-role isolation was overkill for pure infra but unbeatable on product builds.
>
> We wrote up the comparison.

The reader has the verdict for all three. The article has nothing left to do.

**Good — keeps the mystery:**
> We tested three AI coding frameworks on the same Pulumi project. One caught a scope drift the other two missed. One produced a 41x speedup. One we probably won't reach for again.
>
> Here's how they compared.

Same outcomes are revealed. The mapping — which framework did which — is what the reader has to read the article to find out. That's the whodunit.

## The structure: setup, gap, pointer

Every post must have three parts:

1. **Setup** — a concrete, specific situation the reader recognizes or finds surprising
2. **Gap** — something withheld that the reader now wants to know (which one? how? why?)
3. **Pointer** — a line that acknowledges the answer exists without spelling it out

All three are required. The pointer is what connects the social post to the article — without it, the post is a standalone observation and the article ends up doing nothing.

### Setup: concrete vs abstract

Bad:
> There's a common challenge teams face when testing infrastructure policies. We found that the feedback loop was slower than it needed to be.
>
> We built a faster way. Here's what changed.

"There's a common challenge teams face" earns nothing. The reader has no reason to care.

Good:
> Fraser Waters kept hearing the same request: let me test a policy without running my whole Pulumi program. So he built a command that runs policy packs against existing stack state.
>
> Here's what it does and when it matters.

The reader can picture the frustration. A named person and a specific command make it real.

### Gap: what to withhold when you can

Not every post has a natural gap. Product announcements, tutorials, and how-to posts sometimes just need a clear setup and a pointer.

Good — no gap, just a concrete setup and pointer:
> Bun runs Pulumi programs 3x faster than Node on cold starts. It has been the most requested runtime since its 1.0 release.
>
> It is now fully supported. Here is what to know before switching.

No mystery, no withholding. The setup gets the reader's attention with a specific number, and the pointer signals there's more to read.

When the article does have a comparison, a surprise, or a non-obvious result, withholding the right detail is what gives the article something to do.

Things worth withholding when the article supports it:
- Which tool/approach produced which result
- The recommendation or verdict
- The surprising mechanism or explanation
- The "how" when you've teased the "what"

You can reveal dramatic outcomes (a performance gain, a bug caught, a tool that failed) as long as you don't reveal which thing maps to which outcome.

Bad — reveals approach and result:
> We benchmarked AI agents writing Terraform HCL and Pulumi TypeScript. HCL uses fewer tokens but Pulumi deployed clean on the first pass with zero repairs, making Opus + Pulumi 41% cheaper overall.
>
> Here is the full analysis.

The reader already knows which language won and why.

Good — reveals outcomes, withholds the mapping:
> We benchmarked AI agents generating Terraform HCL and Pulumi TypeScript across two models. One language uses fewer tokens. The other costs 41% less to actually deploy.
>
> Here is why those are not the same thing.

Both outcomes are revealed (fewer tokens, 41% cheaper) but the reader does not know which language is which. That is the gap.

### Pointer: natural endings

The pointer connects the post to the article. It should feel like the natural last line of a story that continues elsewhere, not a marketing CTA.

**Banned:**
- "Read our blog"
- "Check out our latest post"
- "Learn more"

**Pointer styles that work:**

"Here's" family (use often but not exclusively):
> Here's how it works.
> Here's what changed.
> Here's what that looks like.

"We [created]" form:
> We wrote up the full timeline.
> We documented the architecture.
> We wrote up what we did and what we'd change.

Closing statement (when the gap is strong enough to carry the post):
> We tested all three.
> The setup takes about 15 minutes.

Implicit gap (the pointer IS the gap):
> The answers were not what we expected.
> The fix was not a better prompt.
> The reason wasn't what we expected.

Vary the style across platforms. If X uses "Here's how," LinkedIn and Bluesky should use a different form.

## Voice

These posts go out from Pulumi's corporate accounts.

### When Pulumi is the actor — use "we"

Use "we" for team efforts, product launches, and posts where no single person is the story.

Good:
> We kept finding that the first thing Neo changed in a complex task was the thing we would have told it to skip. The fix was not a better prompt.
>
> We changed the workflow entirely. Here is what that looks like.

This is a team building a product feature. "We" is the natural voice.

### When an external company is the actor — name them

Bad:
> We moved from AWS CDK to Pulumi because CDK tied us to AWS and debugging CloudFormation was painful.
>
> Here's how the switch went.

Sounds like Pulumi migrated away from CDK. It was SST.

Good:
> SST powers thousands of serverless apps and they just rebuilt their entire framework on Pulumi, replacing AWS CDK. The reason wasn't what we expected.
>
> Here's what drove the switch.

SST is named. "We" appears once as Pulumi observing.

Good — no "we" at all:
> SST started on AWS CDK. It worked until they needed to go beyond AWS. Rebuilding an entire developer framework on a new infrastructure engine is not a small decision.
>
> Here's the full story of why they switched and what broke along the way.

### When a single author writes about their own experience

If the blog post is written by one person about something they personally did — attended a conference, ran an experiment, built a feature, got paged — prefer naming them. A named person is more vivid than "we" and more credible than an anonymous corporate voice.

Bad — converts to generic "we":
> We spent four days at our KubeCon EU booth asking visitors what they're running in production with AI on Kubernetes.
>
> The answers were not what we expected.

Good — names the person who was there:
> Engin Diri spent four days at the Pulumi booth at KubeCon EU asking every visitor the same question: what are you running in production with AI on Kubernetes?
>
> The answers were not what anyone predicted. Here's his recap.

Good — author drove an initiative:
> Boris Schlosser asked: if a compromised GitHub Action runs in our CI, what can it steal? Across 70+ repos the answer was too much. He replaced every static secret with short-lived credentials.
>
> Here is how he built a zero-static-secrets pipeline.

Use "we" instead when the post is a team effort, a product launch, or the author is just the writer rather than the person who did the thing.

### Not every post starts with "we"

Overusing "we" makes every post sound the same. Vary the subject across the three platforms.

Stat-first — let a number do the setup:
> 66% of organizations run AI on Kubernetes. Only 7% deploy to production daily. That gap showed up in every conversation at KubeCon EU this year.
>
> Three trends emerged that nobody predicted. Here's what they were.

Product as subject — works when there's a concrete result, not just an announcement:
> Bun runs Pulumi programs 3x faster than Node on cold starts. It has been the most requested runtime since its 1.0 release.
>
> It's now fully supported. Here's what to know before switching.

Third-party as subject — for guest posts and community stories:
> Simen Olsen from Bjerk designed what he thought was a future-proof distributed system in 2018. Six months later it had become a constraint rather than an enabler.
>
> His post-mortem is worth reading. Here is what he would do differently.

Named author — when a single author writes about their own experience:
> Sean Yeh got paged on a Friday night because an Azure app secret expired. Two weeks later a different app broke for the same reason. He automated the rotation.
>
> The setup takes 15 minutes. Here's how it works.

All four have setup, gap, and pointer. None use "we." When writing for all three platforms on the same post, try using "we" on one and a different structure on the others.

## Making it specific

The difference between generic and specific copy is the difference between scrolling past and stopping to read.

Bad:
> We ran into some issues with how our coding agents handled longer projects. The problems were predictable but the solutions took different approaches.
>
> We tested a few options and wrote up what we found.

"Some issues," "the problems," "a few options" — no concrete detail.

Good:
> We asked a coding agent for a three-subnet VPC. It added a NAT gateway, transit gateway, VPN endpoint, and DNS resolver on its own.
>
> Three frameworks claim to fix this. One produced a 41x speedup. We tested all three.

Named resources, a specific number, a concrete count.

## Stick to what the post says

Specificity is powerful, but only when it is accurate. Every claim in the social copy must come from the blog post. Do not round up, infer, or embellish.

Common mistakes:
- Calling a solo creator "a team" because it sounds more impressive
- Inventing a number the post never mentions
- Generalizing a single example into a pattern ("teams keep hitting this" when the post describes one incident)
- Attributing a result to the wrong actor

If the post says one person built something, say one person. If the post does not give a number, do not invent one. The copy should be a window into the article, not a dramatization of it.

## Only Pulumi could write this

If you can swap "Pulumi" for a competitor and the post still works, rewrite it.

Bad:
> Platform engineering is changing how teams deliver software. We built a way to automate, secure, and manage everything you run in the cloud.
>
> We documented the architecture.

Good:
> Most internal developer platforms start with Kubernetes and Backstage and months of glue code. Pulumi IDP skips that — all four layers share one engine.
>
> Teams in our preview were live in a day. We documented the setup.

Names the competition, identifies a structural difference.

## Avoiding fluffy announcements

Some posts ARE announcements — product launches, feature releases, customer wins, conference presence. Those are valid post types and should announce directly. The thing to avoid is the *fluffy* announcement: vague claims, release-note phrasing, no specific person/place/number/outcome.

Most docs posts are **link-promo announcements** (the post links to a writeup of the news). Lead with the problem and withhold the mechanism — the writeup is where the reader gets the answer.

Bad:
> We built a new way to import existing cloud resources into Pulumi. Discover unmanaged resources, group them into stacks, and generate code in your language of choice. Available now for all Team and Enterprise customers.
>
> Here's what it looks like.

Explains what, how, and who. "Available now" is release-note language. The article has nothing left to do.

Good:
> Most teams trying to adopt infrastructure as code hit the same wall: hundreds of existing cloud resources created by hand or with scripts nobody remembers. Getting them into IaC meant writing boilerplate one resource at a time.
>
> We built a way to skip that. Here is what it looks like.

Same feature. Leads with the problem, withholds the mechanism.

Occasionally a docs post is a **standalone announcement** layered with a writeup — "we'll be at KubeCon, here's our recap of last year" or "Pulumi just hit 100k stars, here's the retrospective." The body delivers the news directly; the link is for the deeper story. Concrete specifics carry these — booth number, person's name, number, date, place.

Bad:
> Excited to be at KubeCon next week. Come say hi. Here's our writeup from last year.

Generic. Could be any company at any conference. No specifics.

Good:
> We'll be at KubeCon Atlanta Nov 12 at booth 314. Engin Diri is on stage Wednesday talking about what teams are running in production with AI on Kubernetes — and what isn't working.
>
> Last year's recap is below if you want the prequel.

Same shape (we'll be at X), but specific: date, booth, named speaker, concrete topic. The reader has a reason to care, and the link is positioned as context, not bait.

## Avoiding LLM-speak

Generated text has recognizable patterns. If the copy reads like it was generated, rewrite it.

Bad:
> Infrastructure secrets. Expired credentials. Friday night pages. We built a single automation pipeline that handles all three.
>
> The setup takes about 15 minutes. We wrote up how it works.

Staccato noun phrases as dramatic beats. The structure is fine but the writing sounds generated.

Good:
> Last quarter an Azure app secret expired on a Friday night. The on-call engineer rotated it by hand. Two weeks later a second app broke because it shared the same secret.
>
> We automated the whole rotation process. Here is how it works.

Same topic, same specificity. Narrative with cause and consequence instead of dramatic fragments.

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
> We wrote up the full timeline.

Bluesky is between X and LinkedIn. Practitioner voice, slightly more detail than X.

## Drafting from a blank `social:` block

When the post has no existing copy, you have the most leverage and the most ways to go wrong. **Read the blog body in full before drafting** — the body is the only source of truth for specifics. Title, URL slug, `meta_desc`, and tags are not authoritative — they're shorthand and they sometimes drift from the body's actual claims.

Then find:

1. The most concrete specific in the article — a number, a named tool, a person, a moment ("week three", "Friday night page", "41x speedup", "200 modules"). This is your setup.
2. The article's main verdict, mechanism, or surprising mapping. This is what you withhold.
3. The natural reader question the article answers. The pointer is what tells the reader the answer is in the article.

Then build setup → gap → pointer in that order, on each platform. Don't draft three platforms in parallel — draft one (usually X, since it's the tightest), then adapt. Whichever platform you write first will sound the freshest; the other two should differ in subject (vary "we" vs. stat-first vs. named-author) and in pointer phrasing.

**After drafting, verify every specific against the body.** If you wrote a number, name, or attribution, it has to appear in the blog body — not the title, slug, or `meta_desc`. If a claim doesn't trace, drop it or replace it. Example: a URL `top-8-claude-skills-…` doesn't mean the body says eight; the body might list fourteen.

Common ways drafting from scratch goes wrong:

- **Defaulting to "We're excited to share…" or "Today we're announcing…"** — release-note phrasing. Find the problem the article solves and lead with that instead.
- **Recapping the article's structure** — "We cover three frameworks. We tested each one. Here's what we found." That's a table of contents, not a hook.
- **Generic openers because the article's subject is technical** — "Infrastructure as code is changing how teams ship software." Cut. Lead with a concrete moment from the post.
- **Three near-identical posts across platforms** — same opener, same pointer, just trimmed. Vary the subject (one with "we", one stat-first, one named-author) so each platform earns its space.

If after one read of the article you can't find a concrete specific to lead with, the article likely is generic — flag that to the author rather than drafting around it.

## Spotting and replacing LLM-fill copy

When the existing copy reads like it was generated by an LLM that didn't read the article, treat it as if the block were empty. Recognizable patterns:

- **Three staccato noun phrases as drama:** "Infrastructure secrets. Expired credentials. Friday night pages."
- **Em-dash chains as connective tissue:** "The problem isn't capability — it's consistency — and three teams built answers — each different."
- **Constructed parallelism that signals nothing:** "Built for builders. Designed for developers. Optimized for ops."
- **Generic openers that name the trend:** "In today's cloud landscape…", "As organizations adopt AI…", "Teams everywhere are realizing…"
- **Buzzword stacking:** "AI-powered, cloud-native, enterprise-ready infrastructure automation."
- **Overuse of "transform", "unlock", "empower", "leverage", "seamless", "robust"**
- **Closing CTA in marketing voice:** "Read on to discover how we're revolutionizing infrastructure as code."

The fix is the same for all of them: drop the LLM copy entirely and draft fresh from the article using the setup → gap → pointer shape. Preserving fragments of the LLM copy and patching around them tends to leave a hybrid that's worse than either.

Don't try to "improve" LLM-fill in place — recognize the pattern, throw it out, start from the article.
