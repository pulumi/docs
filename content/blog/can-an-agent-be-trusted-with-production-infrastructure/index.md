---
title: "Can an Agent Be Trusted to Change Production Infrastructure? What Has to Be True First"
allow_long_title: true
date: 2026-10-15
draft: false
meta_desc: "An AI agent should change production only with a preview, a known blast radius, an approval threshold, an audit trail, and a tested rollback."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - ai-agents
    - ai
    - pulumi-neo
    - infrastructure-as-code
    - policy-as-code
category: perspectives
faq_schema: true
related_posts:
    - the-agentic-infrastructure-era
    - deployment-guardrails-with-policy-as-code
    - sandboxing-coding-agents-yolo-mode

social:
    twitter: |
        Can an AI agent be trusted to change production infrastructure? Not by default.

        Five things have to be true first: a preview of the exact change, a known blast radius, an approval threshold set in advance, an audit trail, and a tested way back.
    linkedin: |
        When a "Claude Code for Infrastructure" project hit the front page of Hacker News, the top reply called agent tooling a pyramid scheme: tools for building things, with nothing built. That skepticism deserves a straight answer.

        Our answer: an agent should not change production until five things are true. You can see the exact change beforehand, you know its blast radius, a human approves anything above a threshold you wrote down in advance, every change is recorded, and there is a tested way back.

        The post walks through each condition, a threshold table you can adapt, two worked examples (one autonomous, one not), and where the industry still falls short.
    bluesky: |
        Can an AI agent be trusted with production infrastructure? Not by default. Five conditions: a previewed change, a known blast radius, an approval threshold, an audit trail, and a tested rollback. A decision framework with worked examples.
---

An AI agent should not change production infrastructure by default. It earns that access when five things are true about the change: you can see the exact change before it happens, you know its blast radius, a human approves anything above a risk threshold you set in advance, the change is recorded, and there is a rollback path you have tested.

A "Claude Code for Infrastructure" thread on [Hacker News](https://news.ycombinator.com/item?id=46889703) drew 276 points and about 176 comments in February 2026. The skepticism in it is reasonable, and this post answers it with a checklist you can apply to any agent, from any vendor, against any cloud.

## The "pyramid scheme" comment deserves a straight answer

The [top comment](https://news.ycombinator.com/item?id=46890881) in that thread did not attack the project. It said: "All these tools to build something, but nothing to build. I feel like I am part of a Pyramid Scheme where every product is about building something else, but nothing reaches the end user." The commenter added that they had nothing against the tool itself.

A lot of agent tooling does fit that description. Tools exist to build tools, and demos end at the terminal. Infrastructure is where that stops being true, because infrastructure is the part that end users actually touch. A bad change to a database or a load balancer reaches them within minutes. Production is the test of whether an agent is useful or just busy.

Other commenters pressed harder. One [wrote](https://news.ycombinator.com/item?id=46894184) that "we have IaC, reviews, and promotion for a reason" and that infrastructure decisions look too high risk for agents today. The project's author [conceded the point](https://news.ycombinator.com/item?id=46892035): "I don't want LLMs on prod at all." The tool works against cloned sandboxes instead of production. Another [argued](https://news.ycombinator.com/item?id=46895020) that CI/CD with a manual approval step would work better, since infrastructure is code like anything else, and a third [questioned](https://news.ycombinator.com/item?id=46893044) whether a production clone is realistic at all.

Both camps are describing the same gap. Few people doubt that an agent can write a change. The open question is what has to be true before it is allowed to apply one.

## What has to be true before an agent changes production?

Five conditions, each with a test you can fail. If you cannot pass the test for a given change, a human applies it.

### Can you see the exact change before it happens?

Yes, if the agent works through a tool that produces a preview of every resource it will create, update, replace, or delete before anything runs. With Pulumi, `pulumi preview` does this, and policy packs evaluate that same preview. The test: can a reviewer read the preview and say what will differ in production afterward, without asking the agent?

Be honest about the limits. A preview shows the change, not its consequences. It cannot tell you that a replaced instance will take ninety seconds to warm a cache, or that a downstream service hard-codes an address. Values the cloud assigns at creation time show as unknown until the update runs. [Update plans](/docs/iac/concepts/update-plans/) go further by saving a preview and constraining `pulumi up` to those operations, but the feature is experimental, and the documentation notes it is a weaker guarantee about what the program itself will do.

### Do you know the blast radius?

Blast radius is the set of things that can break if this change goes wrong. It is a property you can estimate before the change runs, and most teams never write it down.

Pulumi's own guidance on organizing infrastructure puts the starting point plainly: "A stack is the unit of deployment, so it's also the unit of failure. The larger a stack, the more resources a single bad update can damage." See [organizing projects and stacks](/docs/iac/guides/basics/organizing-projects-stacks/) for the tradeoffs.

Within a stack, a useful estimate comes from five questions:

1. How many resources does the preview touch?
2. How many of those are replaced or deleted, rather than updated in place?
3. Do any hold state, such as databases, volumes, queues, or buckets with data?
4. What depends on them, including other stacks that reference these outputs?
5. Does the change sit on a traffic path, an identity boundary, or an encryption boundary?

Resource count alone misleads. A change touching 40 resources can be safer than a change touching one, as the examples below show.

### Is there a threshold above which a human must approve?

There should be, and it should be written down before the agent runs, not negotiated while a diff is open. The point of a threshold is that it removes judgment-in-the-moment, which is the thing that erodes under deadline pressure.

The mechanism has three parts that work together: a preview that shows the change, [mandatory policies](/docs/iac/crossguard/) that stop an update when it violates a rule, and an approval step for anything above the threshold. [Pulumi Neo](/product/neo/) is built this way. Its task modes decide where approval happens: in Review mode (the default) Neo asks before it previews, applies, or opens a pull request; in Balanced mode it asks only before it applies; in Auto mode it does not ask. The [Neo tasks documentation](/docs/ai/neo/tasks/) covers each mode. Neo also acts with the permissions of the person who invoked it, and [read-only mode](/docs/ai/neo/permissions/) removes its ability to write at all.

The modes are a dial. The table in the next section is how you decide where to set it.

### Will you be able to reconstruct what happened?

After an incident you need to answer five questions: who asked for the change, which agent made it, what instructions it was working from, what the preview said, and who approved. Pulumi Cloud [audit logs](/docs/administration/concepts/audit-logs/) record who did what and when, and `pulumi stack history` records each update to a stack. Together they give you the actions.

They do not give you the reasoning. Why the agent chose one approach over another is usually visible only in its conversation transcript, so keep the task description and approval comments with the change. The test: pick a change from last month and see whether a person who was not there can explain it from the record alone.

### Is there a real way back?

Rollback for infrastructure as code means redeploying the previous version of the program: revert the commit, preview, and apply. That works well for configuration. It does not restore data. If a change deleted a database, reverting the code creates a new empty database.

So the rollback test has two halves. First, have you actually run the redeploy path for this kind of change in a non-production stack? Second, for anything stateful, do you have a backup you have restored from? Resource options such as [`protect`](/docs/iac/concepts/resources/options/protect/) and [`retainOnDelete`](/docs/iac/concepts/resources/options/retainondelete/) block or soften the worst deletions, which is why stateful resources should carry them whether or not an agent is involved.

## A risk threshold you can write down

Adapt this table to your environment. The first column is a signal you can read straight from the preview or the resource type.

| Signal | Agent may apply on its own | Human approves first |
|---|---|---|
| Deletes or replaces in the preview | None | One or more |
| Stateful resources (databases, volumes, queues) | None touched | Any touched |
| IAM, network, or encryption boundaries | Untouched | Touched |
| Reversibility | Redeploying the old version fully restores it | Needs a restore from backup |
| Policy result | Clean | Any advisory violation, or any mandatory failure (which blocks the update outright) |

The rule is conjunctive. The agent applies on its own only if every row is in the left column. One entry on the right sends the change to a person.

## Two changes, two verdicts

**Change A: add cost-allocation tags to about 40 resources.** The preview shows 40 in-place updates, zero replaces, zero deletes. Tags do not alter traffic, identity, or data. Redeploying the old tags restores the prior state exactly. Every row is in the left column, so an agent can apply this autonomously in production, with a notification to the owning team and the usual audit record.

**Change B: enable storage encryption on an existing managed database.** On Amazon RDS this forces replacement, so the preview shows one resource, marked `replace`. That is one line in the diff and the largest blast radius on the page: a replacement destroys the old database and creates a new one. Rollback is a backup restore, not a redeploy. Four rows land on the right: replaces, stateful data, the encryption boundary, and reversibility. The agent's job here is to prepare the pull request, attach the preview, and propose a snapshot-and-cutover plan. A human approves and runs it.

**A gray case: tighten a security group's ingress rule.** One resource, one in-place update, no data. By count it looks like Change A. But it sits on a traffic path, and a rule that is too tight cuts off a service that nobody mentioned to the agent. The network row sends it to approval. The reviewer's job is the question the preview cannot answer: what else talks to this?

The lesson across all three: classify by what the change can break, never by how many resources it touches.

## Where the industry is not there yet

Pulumi has built much of this machinery, and some of it is still immature everywhere.

- **Blast radius is mostly estimated by hand.** The five questions above are a manual exercise. No tool, ours included, computes a trustworthy blast radius for an arbitrary change, especially across stacks and into running systems.
- **Previews show change, not consequence.** Runtime behavior, cold caches, and implicit dependencies sit outside the preview.
- **Data rollback is unsolved by infrastructure tooling.** Code can be reverted. Deleted data needs backups, and backup discipline varies enormously by team.
- **Audit trails capture actions, not reasoning.** You can see that an agent changed a rule. You often cannot see why.
- **Approval fatigue is real.** If an agent asks for sign-off fifty times a day, people stop reading. A threshold that is too low trains reviewers to rubber-stamp, which defeats it.
- **Agent capability is uneven.** IBM's [ITBench](https://arxiv.org/abs/2502.05352) study from early 2025 found that agents built on state-of-the-art models resolved 13.8% of SRE scenarios and 25.2% of CISO scenarios, and none of the FinOps scenarios. Models have improved since, but the study is a reminder to measure an agent on your own tasks before widening its access.
- **Agents inherit broad permissions.** An agent that acts as a user can do whatever that user can do. Scoping credentials down is work you have to do deliberately.

For the enforcement side, see [sandboxing coding agents](/blog/sandboxing-coding-agents-yolo-mode/) and [deployment guardrails with policy as code](/blog/deployment-guardrails-with-policy-as-code/).

## How trust gets earned

Trust in a person grows through a record. The same approach works for an agent, in stages:

1. **Read-only.** The agent inspects stacks, explains drift, and answers questions. Nothing changes.
2. **Propose.** The agent opens pull requests with a preview attached. A human reviews and merges.
3. **Apply below the threshold.** The agent applies changes that sit entirely in the left column of the table, such as tags, scaling within limits, and dev-environment changes, with notification.
4. **Move the threshold on evidence.** After a quarter of audit records show the agent's autonomous changes were clean, widen what counts as "below the line." If they were not clean, narrow it.

Back to the skeptic's question of whether any of this reaches the end user. It does only if the changes agents make are safe enough to keep making. An agent that writes infrastructure code nobody dares to apply produces nothing. An agent that applies anything produces an outage. The threshold, the preview, and the record are what make the middle path possible. For the broader context, see [what agentic infrastructure is](/what-is/what-is-agentic-infrastructure/) and [the agentic infrastructure era](/blog/the-agentic-infrastructure-era/).

## Frequently asked questions

### Should an AI agent ever change production without human approval?

Yes, for changes that pass every row of your threshold table: no deletes or replaces, no stateful resources, no identity or network boundaries, a clean policy result, and a redeploy that fully restores the old state. Tag updates and bounded scaling changes are typical. Everything else goes to a person.

### What is blast radius in infrastructure?

Blast radius is the set of systems and data that can be affected if a change goes wrong. It depends on how many resources are replaced or deleted, whether any hold state, what depends on them, and whether the change sits on a traffic, identity, or encryption boundary. Resource count alone is a poor proxy.

### Can you roll back an infrastructure change an AI agent made?

Configuration changes, yes: revert the program and redeploy. Data, no. Reverting code that deleted a database creates an empty one, so stateful resources need tested backups and protection options such as `protect` and `retainOnDelete`. Test the redeploy path in a non-production stack before relying on it.
