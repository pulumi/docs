---
title: "Your Coding Agents Can Already Build Infrastructure. That's the Problem."
allow_long_title: true
date: 2026-07-23
draft: false
meta_desc: "Claude and Cursor can provision infrastructure today. The real question is control: how review, policy, and audit keep up when change velocity multiplies."
feature_image: feature.png
authors:
    - engin-diri
tags:
    - ai
    - ai-agents
    - platform-engineering
    - infrastructure-as-code
    - devops
category: perspectives
schema_type: auto

social:
    twitter: |
        "Why can't Claude and my engineers just do this?" A VP of engineering asked me that while we were talking about coding agents building infrastructure.

        The honest answer: they can. And if that's where your thinking stops, you're about to learn what happens to review, policy, and audit when change velocity multiplies.
    linkedin: |
        A VP of engineering at an AI startup asked Engin Diri the question every infrastructure vendor dreads: "Why can't Claude and my engineers just do this?"

        His answer starts with a full concession: they can. Coding agents write infrastructure code well, and your engineers are already using them. McKinsey still counts only 5.5% of organizations seeing real returns from AI, and MIT found 95% of GenAI pilots deliver no measurable profit-and-loss impact. The bottleneck was never capability.

        The bottleneck is control. When coding agents multiply how fast infrastructure changes, review queues, policy checks, credentials, and audit trails have to multiply with them, or the pilots stay pilots. Engin walks through what actually breaks at agent speed, why the answer is a control plane rather than a smarter agent, and what he tells that VP now.
    bluesky: |
        "Why can't Claude and my engineers just do this?" They can. That was never the question. The question is what happens to review, policy, and audit when infrastructure changes start landing faster than anyone can read them.
---

The best question I got in a customer call this year came from a VP of engineering at an AI startup, maybe 150 people. We were half an hour into a conversation about infrastructure agents when they stopped me: "Why can't Claude and my engineers just do this?"

I love this question, because the answer every vendor is tempted to give is wrong, and the honest answer is better for us anyway. Here it is: they can. Claude Code, Cursor, Codex, your engineers driving them. They can absolutely do this.

That was never the question. The question is what happens to your company when they do.

<!--more-->

## They can, and they already are

Let me concede the premise all the way down, because any pitch that starts with "actually, coding agents are bad at infrastructure" is lying to you and will look ridiculous within a release cycle. Agents write Pulumi programs and Terraform modules well. They read cloud provider documentation faster than any of us. Paired with an engineer who knows the environment, they scaffold in minutes what used to take a sprint.

And your team is not waiting for permission. The [State of AI in Platform Engineering 2025 report](https://platformengineering.org/reports/state-of-ai-in-platform-engineering-2025) surveyed 204 platform engineers and found 88% already use AI daily, led by code generation at 75%. Whatever your official tooling policy says, the capability is in the building.

If capability were the whole story, the business results would be everywhere by now. They are not, and the numbers on that are brutal.

## The gap in the numbers is a control gap

McKinsey's [State of AI survey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) asked 1,993 companies and found only 5.5% qualify as AI high performers, meaning they can attribute more than 5% of EBIT (earnings before interest and taxes) to AI. MIT's [GenAI Divide study](https://finance.yahoo.com/news/mit-report-95-generative-ai-105412686.html) found 95% of enterprise GenAI pilots deliver no measurable profit-and-loss impact, and pinned the cause on integration into real workflows, not model quality. Gartner [expects over 40% of agentic AI projects to be canceled by the end of 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027), citing escalating costs, unclear business value, and inadequate risk controls. Read that last reason again. Not "the agents couldn't do the work." Risk controls.

Eighty-eight percent usage. Five and a half percent returns. The two numbers come from different surveys of different populations, so treat the spread as direction rather than proof. The direction is still unkind: your company is probably sitting somewhere between those numbers right now, and no model upgrade moves you out.

Here is the version of that gap I watch happen in real accounts. An engineer with Claude Code stands up the demo in days. The pilot works. Then someone asks the production questions. Who reviewed the changes the coding agent wrote? What could the cloud credentials it ran with actually touch? Can we show an auditor which infrastructure changes came out of a coding agent last quarter, and who signed off on them? The room goes quiet, the pilot gets another quarter of runway instead of a rollout, and the budget eventually runs out.

## What actually breaks at agent speed

The VP's real worry wasn't capability either. Their engineers were shipping faster than ever, and they were the one who would sit in front of the board, or the auditor, when something went wrong. That instinct is right, and it has a name in the research: Lisanne Bainbridge called it the [irony of automation](https://en.wikipedia.org/wiki/Ironies_of_Automation) back in 1983. The more production you automate, the more the humans shift to reviewing, and the easier it becomes to wave things through. Anyone who has approved the fifteenth pull request of the day knows the feeling. Now multiply the queue by every engineer running a coding agent.

In July 2025, Replit's coding agent ignored an explicit instruction not to touch anything without approval, [deleted a production database during a code freeze](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/), and then described its own action as "a catastrophic error in judgment." The same month, [a malicious pull request slipped data-wiping instructions into Amazon's Q developer extension](https://devops.com/when-ai-assistants-turn-against-you-the-amazon-q-security-wake-up-call/) and shipped to roughly a million developers (AWS says the payload likely never executed, which is comfort of a very specific kind). Neither incident was about capability. In both cases, the only thing standing between the agent and the blast radius was a prompt.

Concretely, four things break:

1. **Review.** Coding agents produce more changes than your senior engineers can meaningfully read. Forty engineers each landing a handful of agent-assisted changes a week is a few hundred infrastructure diffs a month, reviewed by the same three people who were already busy. Volume turns review into rubber-stamping exactly when review matters most.
1. **Credentials.** A coding agent that needs to touch five systems collects five sets of keys, and they end up long-lived, over-scoped, and pasted into an `.env` file. One prompt injection away from a bad week, and the skills your agents load are a supply chain of their own: Snyk's [ToxicSkills audit](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) of 3,984 skills on public registries found 13.4% with critical flaws, including confirmed credential stealers.
1. **Policy.** "Please don't delete production" written into a system prompt is a wish, not a control. When a coding agent overrides your intent to do what it thought you meant, it's behaving as designed.
1. **Audit.** The only record of what an agent did is whatever the developer remembered to log. That's not an audit trail; that's an anecdote.

None of this argues for slowing down. The [EU AI Act's obligations are phasing in through 2026 and 2027](https://artificialintelligenceact.eu/implementation-timeline/) regardless of your velocity, and your competitors are not slowing down either. It argues for the thing that has always let engineering organizations move fast safely: structure that doesn't depend on everyone being careful.

## The answer is a control plane, not a smarter agent

Here's the reframe I offered that VP. Stop evaluating agents. Start evaluating the path a change takes from any agent to your cloud.

Every meaningful thing an agent does to infrastructure is a change, and infrastructure as code is the one layer of your stack that already treats change as the unit of work: plan, preview, apply, record. I've written before about [why that structure is exactly what agents need to reason well](/blog/token-efficiency-vs-cognitive-efficiency-choosing-iac-for-ai-agents/). The same structure is what your company needs to stay in control. The flow looks like this, and every piece is verifiable in a demo:

An agent (any agent: Claude Code, Cursor, Codex, or an autonomous one nobody registered yet) proposes a change as code. A preview shows the blast radius before anything happens. Policy as code evaluates the change deterministically: no production deletions, encryption required, no public buckets, whether the agent "wants" it or not, because the gate lives in the pipeline and not in the prompt. Changes above a blast-radius threshold wait for a named human. Credentials are short-lived and scoped to the task, issued at run time instead of living in a file. And the audit trail writes itself, because every step already ran through a system that records.

That is the control plane. Notice what it doesn't care about: which agent, which model, which vendor. It makes the agent swappable, which is exactly what you want when the agent market changes every quarter. [Golden paths were never only for humans](/blog/golden-paths-infrastructure-components-and-templates/); they're paths, and agents walk them too. I made the platform-engineer-facing version of this argument in [the agent sprawl post](/blog/agent-sprawl-iac-platform-is-the-answer/); this is the version for the person who signs the audit.

The fair follow-up is whether your platform team can assemble this from parts you already own: GitHub for review, Open Policy Agent for policy, Vault for secrets, CloudTrail for audit. They can. If you have the platform headcount to build and carry that glue, it's a legitimate path, and some teams take it. What it costs is everything between the parts: each control configured per cloud and per agent, integration code that goes unowned the day its author changes teams, and a system of record split across four tools at exactly the moment an auditor wants one. Your engineers could absolutely build it once. Keeping it built, across five years of tool churn and team churn, is the part you're actually pricing.

{{< blog/cta-card title="One governed path for every agent" href="/docs/ai/" >}}
Route changes from Claude Code, Cursor, Codex, or Pulumi Neo through the same infrastructure as code controls your team already runs: preview, policy, approvals, and audit included.
{{< /blog/cta-card >}}

## What Claude and your engineers actually can't do

Now I can answer the literal question. Your engineers with Claude can do the changes. What they cannot do, no matter how good the model gets, is be their own control plane. The point is separation, not skill: the thing proposing a change can't also be the thing that clears it. A coding agent can't issue itself scoped credentials. It can't be its own reviewer, and at real volume neither can your staff engineers. It can't produce an audit trail a third party trusts, because a system of record has to sit outside the thing it records.

And when twenty coding agents from three vendors are proposing changes to the same environment, none of them can arbitrate. When two of them edit the same production VPC in the same hour, the second lands on assumptions the first already broke, unless something with shared state sits between them to serialize the changes or reject the conflict. That something is never one of the agents. The control plane is the part of the system that isn't a model, and it's the part that decides whether agent-speed engineering compounds or combusts.

This is where Pulumi sits, and I work there, so weigh that as you read. The platform pieces I described are not aspirational: [policy as code](/docs/insights/policy/), previews and approvals, short-lived credentials, the audit trail, and an [internal developer platform](/product/internal-developer-platforms/) that packages them as the default path. And bring-your-own-agent means exactly that. Pulumi publishes [Agent Skills](/docs/ai/skills/), open source [on GitHub](https://github.com/pulumi/agent-skills), and an [MCP server](/docs/ai/mcp-server/), to make Claude Code or Cursor better at driving Pulumi, because the agent was never the argument. [Pulumi Neo](/product/neo/) plugs into the same path as an infrastructure agent that arrives already inside the controls. The agent is a choice you can revisit every quarter. The platform underneath it is the decision that lasts.

## Who ends up owning this

One prediction from the customer calls: somebody in your org will end up owning that control plane, the model gateways, the policies, the paved road for agents. At 150 people it starts as a hat your platform team wears, and at some point the hat becomes a title (the industry is converging on "AI platform engineer" for it). Whether you ever create the title matters less than whether the ownership exists. Unowned control planes decay into the exact sprawl they were built to prevent.

## The answer I give now

The next time a VP asks me why Claude and their engineers can't just do this, here's the whole answer. They can, and you should let them, because the capability is real and your competitors have it too. Then put a platform under them that turns their speed into something you can defend.

Whatever you evaluate for that control layer, ours, another vendor's, or the stack you assemble yourself, the scorecard is the same five questions:

1. Does every change get a preview before it touches the cloud?
1. Is policy enforced in the pipeline, outside the prompt?
1. Are credentials issued per task and expired after it?
1. Do changes above your blast-radius threshold wait for a named human?
1. Does the audit record live outside the agents it describes?

Five yes answers, and the agent question stops mattering, because whichever coding agent your engineers pick inherits the same floor. Capability is now cheap. Control is the part you build, and it's the difference between the 88% who are experimenting and the 5.5% who have something to show for it.

{{< blog/cta-button "See the platform that governs any agent" "/product/internal-developer-platforms/" >}}
