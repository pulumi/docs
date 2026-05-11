---
title: "Seven Rules for Building an AI-Native Software Factory"
date: 2026-05-07
draft: false
meta_desc: "Ewan Dawson, CTO of Compostable AI, on building a software factory where AI agents write the code. Seven rules learned across nineteen client deployments."
meta_image: meta.png
feature_image: feature.png
youtube_id: oHNdlWlsR-w
authors:
    - ewan-dawson
    - adam-gordon-bell
author_roles:
    adam-gordon-bell: "as told to"
tags:
    - ai
    - ai-agents
    - infrastructure-as-code
    - pulumi-neo
    - pulumi-esc
social:
    twitter: |
        Five engineers. Nineteen clients. Custom code shipped within a day of signing.

        Ewan Dawson, CTO of Compostable AI, on the seven rules he built around the agents that write almost all of his company's code.
    linkedin: |
        Ewan Dawson runs a five-person software factory at Compostable AI. Most of the code it ships, he hasn't read.

        The agents do the writing. The team handles what the agents can't: defining the work, talking to the customers, deciding what gets built. The factory keeps producing whether the engineers are at their desks or not.

        In a recent Pulumi webinar, Ewan walked through the rules in brief. The blog post is the expanded version. For anyone trying to figure out how to set their team up for what's happening in software now.
    bluesky: |
        Five engineers. Nineteen clients. Custom code shipped within a day of signing.

        Ewan Dawson's seven rules for an AI-native software factory — where agents write nearly all the code.
---

*Ewan Dawson is CTO of [Compostable AI](https://compostable.ai/), where five engineers run an AI-native software factory: nineteen clients, custom AWS deployments, most of them shipped within a day of contract signing. This article is adapted from his recent Pulumi webinar, and covers rules in more depth than we had time for on stage.*

<!--more-->

For the past twenty years, I've viewed software development as a craft. The best engineers drew on decades of experience and took the time to make sure every function, method, and module was right.

But two years into the agentic AI revolution, I realised software is going to look more like a factory than a craft. The economics have changed. We can no longer afford to treat code as bespoke. To scale, we have to adopt an industrial mindset and figure out how to use these tools to deliver more value with less human labour.

I joined Compostable AI soon after it was founded 2.5 years ago, and I built the engineering org AI-native from day one. The technology has come a long way since then, and so has my understanding of what AI-native actually means in practice. Here are seven rules I keep coming back to.

## 1. Transform, don't enhance

<img src="rule-1-chrysalis.png" alt="" class="float-right w-32 ml-4 mb-2 mt-1 rounded-lg sm:w-40 sm:ml-6 lg:w-44">

Going AI-native is not an incremental enhancement to your existing process. If you treat AI as a way to hand your developers smarter tools, you leave most of the value on the table. The leverage comes from rethinking how you develop software from the ground up, and rebuilding the culture and processes around that.

I know that's a tall order for a large, mature engineering org. My advice: start small. Pick one team or one business area and run it as a fully AI-native function. Take the learnings and roll them out from there. And do the political work early, especially with your Governance, Risk, and Compliance function. Bring GRC along on the journey. Otherwise AI becomes a compliance fight instead of a structural advantage.

{{< notes type="tip" size="large" >}}
**Don't bolt AI onto your existing workflow. Redesign the workflow around what agents can do.**

Most of the leverage in this technology comes from rebuilding around it. The tool change is the small part.
{{< /notes >}}

## 2. Remove the problem, don't solve it

<img src="rule-2-knot.png" alt="" class="float-left w-32 mr-4 mb-2 mt-1 rounded-lg sm:w-40 sm:mr-6 lg:w-44">

Going AI-native flips which problems are hard and which are easy. The right move often isn't to engineer a solution. It's to reframe the problem so it goes away.

A concrete example. To serve multiple clients while leaning hard on AI in our development process, we had to manage blast radius and security risk. Our instinct was to build a secure multi-tenant sandbox. But securing a shared environment with autonomous agents loose in it is genuinely hard. So we removed the problem: every client gets two dedicated AWS accounts instead, one for production and one "digital twin" staging account. Agents iterate on staging until the work is verified; only then does it ship to production. Nineteen accounts now, one per client.

Managing nineteen AWS accounts with five engineers used to be an administrative nightmare. In an AI-native world where code is cheap, infrastructure-as-code tools like AWS Control Tower and Pulumi make it the easier path.

{{< notes type="tip" size="large" >}}
**Remove the problem before you try to solve it.**

Easier to manage a fleet of accounts than to secure a shared environment. Cheaper to reframe the problem than to engineer your way through it.
{{< /notes >}}

## 3. Pick tools your agents can drive

<img src="rule-3-wrench.png" alt="" class="float-right w-32 ml-4 mb-2 mt-1 rounded-lg sm:w-40 sm:ml-6 lg:w-44">

Removing problems is the process side. The other side is tooling. If you want an automated factory, your tech stack has to be amenable to agentic AI. I find this overlaps heavily with tools that have great developer experience. Robust API plus clean CLI, agents can drive it. Heavy click-ops around a web UI, agents stop there.

We didn't get there first try. Our first IaC tool worked fine when we had a couple of clients. As we added more, accounts drifted, deployments slowed, retries got complicated. We needed something built for the scale we were heading toward.

I went looking, and [Pulumi](/) fit. It lets us express infrastructure as type-safe code (TypeScript, in our case, rather than HCL), which agents are good at writing. Pairing that with specialized AI agents like [Pulumi Neo](/product/neo/) — pre-loaded with domain-specific Pulumi skills — means we can develop and deploy infrastructure following best practices. One of my colleagues put it: "The scary thing about Neo is it just seems to know everything about what we do." Combining Pulumi IaC with [Pulumi ESC](/docs/pulumi-cloud/esc/) as our configuration plane is faster than stitching tools together. And TypeScript lets us build higher-level abstractions, which makes managing our estate of AWS accounts tractable.

{{< pullquote >}}
"I don't actually care if it's HCL or TypeScript, as long as my software development agents can write it. And they do a better job with TypeScript than HCL."
{{< /pullquote >}}

{{< notes type="tip" size="large" >}}
**Tools have to share your AI-native mindset. If they don't integrate deeply, the human becomes the glue.**

If part of your stack still requires a human to click through a web UI to provision an account, your agents stop there.
{{< /notes >}}

## 4. Don't let one agent do everything

<img src="rule-4-constellation.png" alt="" class="float-left w-32 mr-4 mb-2 mt-1 rounded-lg sm:w-40 sm:mr-6 lg:w-44">

When I first started with agents, I reached for a god prompt: one massive system prompt meant to guide a single agent through the whole software lifecycle. It didn't work. Agents struggle when you give them multiple goals. The writer is lenient on its own work — it won't catch what it just shipped. You don't want it reviewing the code, checking for security flaws, or hunting bugs.

We get much higher quality when we run a constellation of specialized agents, each focused on one specific part of the production line. Pulumi Neo handles infrastructure. Alongside it sit agents specialized in:

* Code implementation
* Code review and testing
* Security auditing
* Internal standards compliance
* Documentation updates

Passing tasks down that assembly line is how we get high-quality code with minimal human supervision.

{{< notes type="tip" size="large" >}}
**Don't let any agent mark its own homework. Specialize by job.**

Writers are lenient on themselves. Specialists each look for one thing — review, security, docs — and they catch what the writer missed.
{{< /notes >}}

## 5. Measure human hours per unit of value

<img src="rule-5-hourglass.png" alt="" class="float-right w-32 ml-4 mb-2 mt-1 rounded-lg sm:w-40 sm:ml-6 lg:w-44">

Once we had agents writing and agents reviewing, throughput went up — but the bottleneck moved past the PR. Engineering hours were still the most expensive thing in the building, so my core metric is human hours per unit of value produced. Minimize that.

In practice that means hunting for every step that still goes through a person, especially the mid-pipeline steps between ideation and production. If we can automate the human touchpoints along that line, we run a factory that produces 24/7.

Pushing automation this hard turns out to enforce good engineering practices. A chaotic, undocumented process is impossible to automate. Good software engineering is still good software engineering, whether you use AI or not. Adding agents to a weak process won't magically fix it.

{{< notes type="tip" size="large" >}}
**Measure human hours per unit of value. Treat every one as a bottleneck to remove.**

Mid-pipeline is where the bottlenecks hide. Automate the human touchpoints between ideation and production, and the underlying process gets cleaner along the way.
{{< /notes >}}

## 6. Design for convergence, not one-shot correctness

<img src="rule-6-spiral.png" alt="" class="float-left w-32 mr-4 mb-2 mt-1 rounded-lg sm:w-40 sm:mr-6 lg:w-44">

Even with the human touchpoints removed, the agents don't ship right the first try. Once you embrace the factory pipeline, you stop needing them to. The goal is to design a system that converges on the correct solution through automated iteration.

The loop we run looks like this:

1. **Refinement:** agents iterate on the Product Requirements Document until the problem is clear.
2. **Planning:** agents draft multiple technical approaches, and evaluation agents pick the best one.
3. **Implementation:** coding agents write the software.
4. **Review:** specialized checking agents look for bugs, API misuse, and security flaws.

If the checkers find a problem, they hand it back to the implementation agent. The loop repeats until all the automated tests pass and all the agents agree on a clean pull request. Once it converges, we merge and deploy to staging with high confidence.

Two things have to be true for that to work. You need a way to evaluate whether the output is good enough — without that you don't know when to stop. And the loop has to actually converge: each pass has to get closer. A checker that fails every PR for a different reason isn't helping; it just keeps the work going in circles. The feedback has to be specific enough that "fix this" narrows the search rather than widening it.

Once it converges, the question moves on. How cheap can we make it? Lower the time to PR, reduce token count, drop the overall cost. The optimization never really ends.

{{< notes type="tip" size="large" >}}
**Don't aim for one-shot correctness. Design for convergence.**

It doesn't matter how many tries it takes, as long as the loop closes without a human in it. Get convergence first. The optimization comes after.
{{< /notes >}}

## 7. Run the factory in the cloud, not on a laptop

<img src="rule-7-cloud.png" alt="" class="float-right w-32 ml-4 mb-2 mt-1 rounded-lg sm:w-40 sm:ml-6 lg:w-44">

Even a converged factory has to live somewhere. Try running a fully automated factory on individual developers' laptops, and it falls apart. Laptops are highly trusted environments. Running capable, autonomous agents there weakens your security posture. And a factory needs to be running 24/7, responding to events that happen elsewhere — PR comments, Slack conversations, errors in test environments.

Running in the cloud also eliminates the headache of configuration drift across a dozen developer machines. Same prompts running against different model versions; env vars half-set on half the laptops. The thing you're trying to optimize lives in different states across the team. Cloud isn't just where the factory runs; it's the only place a team can iterate on it together. Keep everything in one place — AWS, Pulumi Cloud, GitHub. The specific stack matters less than the principle.

And the part that matters most: the factory keeps running, testing, and deploying long after we've closed our laptops and gone to sleep.

{{< notes type="tip" size="large" >}}
**Build the factory somewhere you can work on it — not just somewhere it can run.**

A factory scattered across laptops can't be improved as a system. Cloud keeps it in one shape, 24/7, and lets the team iterate together.
{{< /notes >}}

## Closing thought

I've shipped more code in the last two years than I did in the fifteen before that. Most of it in languages I couldn't write by hand. And that's after a stretch in leadership where I wrote almost none.

If you're where I was two years ago: don't ask how AI fits into what you already do. Find the biggest thing a human still does by hand and take that human out of the loop. Then do it again.

The factory is built one rule at a time. Mine isn't finished. That's the point.

---

*Watch the [original Pulumi webinar](https://www.youtube.com/watch?v=oHNdlWlsR-w). Learn more about [Compostable AI](https://compostable.ai/) and [Pulumi Neo](/product/neo/).*
