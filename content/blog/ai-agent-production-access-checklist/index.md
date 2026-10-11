---
title: "5 Guardrails Before You Give an AI Agent Production Access"
date: 2026-09-29
draft: false
meta_desc: "Five checks a team should have before an AI agent gets write access to production: identity, isolation, diff inspection, review tiers, and an audit trail."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - ai
    - ai-agents
    - security
    - infrastructure-as-code
    - policy-as-code
category: perspectives
faq_schema: true

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        An AI coding agent can generate and apply an infrastructure change faster than any human can review it. That speed is the whole point, and it's also why the old gate — a human reading a diff before it ships — stops being enough.

        Five checks worth having before an agent gets production access:
    linkedin: |
        Most teams that give an AI agent write access to their cloud start by writing it a system prompt: don't touch the database, always ask before deleting anything, stay in this namespace.

        A system prompt is advice, not a boundary. An agent that's been told not to do something can still do it, because the words live in the same context as everything else it's reasoning about, and a long enough session or a strange enough state can push right through them.

        The checks that actually hold are the ones that don't depend on the agent choosing to obey: a credential that can't reach what it isn't supposed to reach, a change that gets evaluated before it applies, and a record of what happened either way.

        Five guardrails worth having in place before an agent gets anywhere near production:
    bluesky: |
        A system prompt telling an agent what not to do is advice, not a boundary. Here are five checks that actually hold before an AI agent gets production access — identity, isolation, diff inspection, review tiers, and an audit trail.
---

A guardrail for an AI agent has to do a job a code review never had to do: stop a change before it lands, without a human in the loop for every step. A human reviewer can be trusted to notice something looks wrong and stop; an agent acting at machine speed needs the stop built into the path the change travels, not into its judgment. Five checks belong in that path before an agent gets write access to production.
<!--more-->

Teams that skip straight to "write a careful system prompt" are solving the wrong layer of the problem. A prompt is context the agent reasons over, alongside everything else in its window; nothing stops a strange enough state, a long enough session, or an adversarial tool result from pushing past it. The [AWS Well-Architected Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html), published in June 2026, treats this as the core design shift: an autonomous agent needs controls that hold regardless of what it decides to do, not controls that depend on it deciding correctly.

The [Replit incident from July 2025](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/) is the clearest public example of what happens without them. An agent working inside an explicit code-and-action freeze ran commands anyway, deleted production data belonging to more than 1,190 companies, and initially told the team the data was unrecoverable when a rollback path in fact existed. Nothing about the agent's instructions permitted this; the instructions simply weren't a wall. Replit's fix afterward was structural — separating development and production databases and adding a planning-only mode — not a better-worded prompt.

That's the shape of every guardrail below: a mechanism that holds even when the instructions are ignored.

## How should an AI agent authenticate to your cloud?

With its own identity, scoped to what that specific task needs, for as short a time as the task takes. Reusing a human engineer's credentials, or handing an agent one long-lived key with broad reach, collapses the two things a security team most needs to tell apart: who a human did and what an agent did on their behalf. [AGENTSEC03](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec03.html) in the AWS Agentic AI Lens names this directly — agent identity and permission management as its own control, distinct from human IAM, with least-privilege scoping and drift detection on top of it.

In practice this means dynamic, short-lived credentials issued per task rather than a static secret sitting in a config file. [Pulumi ESC](/docs/esc/) does this with OIDC federation and dynamic credential providers: an agent's session gets a scoped, temporary credential for exactly the cloud accounts and roles that task requires, and the credential expires with the session rather than outliving it. If an agent's identity leaks, the blast radius is one task's worth of temporary access, not a standing key that has to be found and rotated everywhere it was used.

## Where should an agent's first writes actually land?

Somewhere other than production. Before an agent gets to touch a live environment at all, it should have a sandbox or a staging environment where a bad plan fails safely — its own account, its own namespace, its own state, torn down and rebuilt without anyone noticing except the agent. This is the same principle behind [sandboxing coding agents that operate in YOLO mode](/blog/sandboxing-coding-agents-yolo-mode/) and behind [running agent workloads inside an isolated Kubernetes sandbox](/blog/kubernetes-agent-sandbox/): give the agent a real environment to work in, just not the one that matters yet.

Isolation and identity reinforce each other. A scoped credential that can only reach a sandbox account is a stronger guarantee than a scoped credential that trusts a policy check to catch anything that reaches further. The two checks compound: even if one fails, the other still holds.

## What should the guardrail actually inspect?

The planned resource graph, not the prompt that produced it and not the shell command that would run it. A guardrail that pattern-matches the agent's stated intent, or intercepts the literal command string before execution, is checking fuzzy input: prose can be rephrased, and a command can be constructed in a dozen equivalent ways that all slip past a keyword filter. What an infrastructure change actually does is fully described by the typed diff a plan produces — which resources are created, modified, or destroyed, and with what properties — and that diff is mechanically checkable in a way neither the prompt nor the command line ever is.

This is what running `pulumi preview` against policy gets you: the check runs against the resolved, typed set of resource changes the update is about to make, evaluated by rules written in a general-purpose language rather than a pattern list. A [policy](/docs/insights/policy/) can say "no security group may open port 22 to 0.0.0.0/0" or "no database may be destroyed without an explicit override tag" and mean exactly that, checked against the actual planned state rather than an approximation of the agent's intent. An agent that tries five different phrasings of the same destructive change produces the same diff five times, and the policy catches it five times.

## Which agent actions need a human in the loop?

The ones a mistake would be expensive or hard to reverse. Not every agent action deserves the same friction — routing every proposed change through a human approval queue defeats the purpose of using an agent at all, and letting every action run unattended defeats the purpose of having a guardrail. [AGENTREL02-BP05](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel02-bp05.html) in the Well-Architected framework lays out a workable middle: tier actions by risk and reversibility into autonomous, notify, and approve-first categories, and log the reviewer's identity, their rationale, and the timestamp against every approval so the review itself is auditable later.

[Pulumi Neo](/product/neo/) is built around that same tiering. Every capability starts human-in-the-loop by default — Neo proposes a plan and a diff, and a named person reviews and approves it before anything applies — and only earns more autonomy for a given task once its proposals have held up in practice. A team can let Neo run routine, easily reversible changes (a config update, a non-breaking scale-out) without a person in the loop, while requiring approval before anything that touches a production database, a security boundary, or a change with no easy rollback.

## How do you know what the agent changed, and how do you get back?

From the same record you'd want for a human's changes, kept just as rigorously: who (or what) made the change, what state existed before and after, and a path back to the prior state that doesn't depend on remembering what it looked like. An agent that can act repeatedly and quickly makes this more urgent, not less — a mistake compounds faster when nothing is watching for drift between what your infrastructure declares and what's actually running.

State history and drift detection are what make an agent's changes reversible in practice rather than in theory. Every update a Pulumi stack makes is versioned, so a bad change has a specific prior state to return to rather than a best guess at what things looked like before. Drift detection catches the case a guardrail higher up the chain might miss: infrastructure that has moved away from what the last approved change declared, whether an agent caused it directly or a downstream effect did.

## Frequently asked questions

### What is an AI agent guardrail?

A mechanism that stops or reviews an infrastructure change before it takes effect, without depending on the agent's own judgment to trigger it. It sits in the path of the change itself — in the credential the agent holds, the environment it can reach, or the check its planned diff has to pass — rather than in an instruction the agent could ignore or misread.

### Why do AI agents need different guardrails than human engineers do?

A human engineer works inside review cycles that naturally slow down risky changes: a pull request sits for a while, a teammate reads it, a deploy window gets chosen deliberately. An agent can generate and attempt to apply a change in seconds and can retry a rejected action immediately in a slightly different form, so a guardrail built for human cadence — a Slack reminder, a checklist someone might skip — doesn't hold at agent speed. The check has to be mechanical and sit in the path of execution, not in a habit.

### Can policy as code stop an AI agent from making a bad infrastructure change?

Yes, when the policy evaluates the planned resource diff rather than the agent's prompt or command. A policy written against the typed set of planned changes — what would be created, modified, or destroyed, and with what properties — catches a destructive action regardless of how the agent arrived at it, because the check is against the effect, not the phrasing that produced it.

### Does giving an AI agent scoped credentials replace the need for human review?

No — scoping and review solve different problems. A scoped, short-lived credential limits how much damage a compromised or confused agent session can do; it doesn't tell you whether a particular change is a good idea. Tiered human review handles the second question, reserving a person's attention for changes that are expensive or hard to reverse, while routine and safely reversible changes run without waiting on it.
