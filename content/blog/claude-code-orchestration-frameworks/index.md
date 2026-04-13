---
title: "Superpowers, GSD, and GSTACK: Picking the Right Framework for Your Coding Agent"
allow_long_title: true
date: 2026-04-13
draft: false
meta_desc: "Three frameworks for AI coding agents compared: Superpowers enforces TDD, GSD prevents context rot, and GSTACK adds role-based governance."
meta_image: meta.png
feature_image: feature.png
authors:
    - engin-diri
tags:
    - ai
    - claude-code
    - ai-agents
    - devops
    - cursor
    - ai-coding
social:
    twitter: |
        AI coding agents break down in predictable ways. Context rot. Tests quietly skipped. Scope that drifts until you're paying for infrastructure nobody asked for.

        Three community frameworks independently built answers — and they take completely different approaches. We tested all three on real infrastructure workflows to find out which failure mode each one actually fixes.
    linkedin: |
        There's a pattern every team building with AI coding agents eventually hits. First session: impressive. By the third session on a complex project, the agent has forgotten half your requirements, stopped writing tests, and started provisioning resources nobody asked for.

        The context window doesn't care how well you wrote your prompt. It fills up. Earlier instructions lose weight. Quality degrades — predictably, every time.

        Three community frameworks converged on fixes, and they take completely different approaches. We spent several weeks testing all three on real infrastructure workflows with Pulumi. Which one helps depends entirely on which failure mode keeps hitting you.
    bluesky: |
        AI coding agents have a window where everything works. After that, context rot, skipped tests, and scope drift are predictable — regardless of which agent you're using.

        Three community frameworks built different answers to this problem. We tested them on real Pulumi infrastructure workflows. Which one helps depends on what keeps going wrong.
---

Three community frameworks have emerged that fix the specific ways AI coding agents break down on real projects. [Superpowers](https://github.com/obra/superpowers) enforces test-driven development. [GSD](https://github.com/gsd-build/get-shit-done) prevents context rot. [GSTACK](https://github.com/garrytan/gstack) adds role-based governance. All three started with Claude Code but now work across Cursor, Codex, Windsurf, Gemini CLI, and more.

Pulumi uses general-purpose programming languages to define infrastructure. TypeScript, Python, Go, C#, Java. Every framework that makes AI agents write better TypeScript also makes your `pulumi up` better. After spending a few weeks with each one, I have opinions about when to use which.

<!--more-->

## The problem all three frameworks solve

AI coding agents are impressive for the first 30 minutes. Then things go sideways. The patterns are predictable enough that three separate teams independently built frameworks to fix them.

**Context rot.** Every LLM has a context window. As that window fills up, earlier instructions fade. You start a session asking for an [S3 bucket](/docs/iac/clouds/aws/guides/) with AES-256 encryption, proper ACLs, and access logging. Two hours and 200K tokens later, the agent creates a new bucket with none of those requirements. The context window got crowded and your original instructions lost weight.

**No test discipline.** Agents write code that looks plausible. Plausible code compiles. Plausible code even runs, for a while. But plausible code without tests is a liability. The agent adds a feature and quietly breaks two others because nothing verified the existing behavior was preserved.

**Scope drift.** You ask for a [VPC with three subnets](/docs/iac/clouds/aws/guides/vpc/). The agent decides you also need a NAT gateway, a transit gateway, a VPN endpoint, and a custom DNS resolver. Helpful in theory. In practice, you now have infrastructure you never requested and barely understand. You will also pay for it monthly.

These problems are not specific to Claude Code or any particular agent. They happen with Cursor, Codex, Windsurf, and every other LLM-powered coding tool. The context window does not care which brand name is on the wrapper.

## Superpowers: the test-driven discipline enforcer

[Superpowers](https://github.com/obra/superpowers) was created by [Jesse Vincent](https://www.linkedin.com/in/jessevincent/) and has accumulated over 149K GitHub stars. The core idea is simple: no production code gets written without a failing test first.

The framework enforces a 7-phase workflow. Brainstorm the approach. Write a spec. Create a plan. Write failing tests (TDD). Spin up subagents to implement. Review. Finalize. Every phase has gates. You cannot skip ahead. The iron law is that production code only exists to make a failing test pass.

This sounds rigid. It is. That is the point.

Superpowers includes a Visual Companion for design decisions, which helps when you are making architectural choices that need visual reasoning. The main orchestrator manages the entire workflow from a single context window, delegating implementation work to subagents that run in isolation.

The tradeoff is that the mega-orchestrator pattern means the orchestrator itself can hit context limits on very long sessions. One big brain coordinating everything works well until the big brain fills up. For most projects, this is not an issue. For marathon sessions with dozens of files, keep it in mind.

The workflow breaks down into skills that trigger automatically:

| Skill | Phase | What it does |
|-------|-------|--------------|
| `brainstorming` | Design | Refines rough ideas through Socratic questions, saves design doc |
| `writing-plans` | Planning | Breaks work into 2-5 minute tasks with exact file paths and code |
| `test-driven-development` | Implementation | RED-GREEN-REFACTOR: failing test first, minimal code, commit |
| `subagent-driven-development` | Implementation | Dispatches fresh subagent per task with two-stage review |
| `requesting-code-review` | Review | Reviews against plan, blocks progress on critical issues |
| `finishing-a-development-branch` | Finalize | Verifies tests pass, presents merge/PR/keep/discard options |

The results speak for themselves. Jesse used Superpowers to ship [chardet](https://github.com/chardet/chardet) v7.0.0 with a 41x performance improvement. Not a 41% improvement. 41 times faster. That is what happens when every code change has to pass a test: the agent optimizes aggressively because it has a safety net.

Superpowers works with Claude Code, Cursor, Codex, OpenCode, GitHub Copilot CLI, and Gemini CLI.

## GSD: preventing context rot before it ruins your project

[GSD](https://github.com/gsd-build/get-shit-done) (Get Shit Done) was created by [Lex Christopherson](https://www.linkedin.com/in/lexchristopherson/) and has over 51K stars. Where Superpowers focuses on test discipline, GSD attacks the context window problem directly.

The key architectural decision: GSD does not use a single mega-orchestrator. Instead, it assigns a separate orchestrator to each phase of work. Each orchestrator stays under 50% of its context capacity. When a phase completes, the orchestrator writes its state to disk as Markdown files, then a fresh orchestrator picks up where the last one left off.

Think about why this matters. With a single orchestrator, your 200K token context window is a shared resource. Instructions from hour one compete with code from hour three. GSD sidesteps this entirely. Every phase starts with a full context budget because the previous phase's orchestrator handed off cleanly and shut down.

The state files use XML-formatted instructions because (it turns out) LLMs parse structured XML more reliably than freeform Markdown. GSD also includes quality gates that detect schema drift and scope reduction. If the agent starts cutting corners or wandering from the plan, the gates catch it.

GSD evolved from v1 (pure Markdown configuration) to v2 (TypeScript SDK), which tells you something about the level of engineering behind it. The v2 SDK gives you programmatic control over orchestration, not just static instruction files.

The tradeoff: GSD has more ceremony than the other two frameworks. For a quick script or a single-file change, the phase-based workflow is overkill. GSD earns its keep on projects that span multiple files, multiple sessions, or multiple days.

The core commands map to a phase-based workflow:

| Command | What it does |
|---------|--------------|
| `/gsd-new-project` | Full initialization: questions, research, requirements, roadmap |
| `/gsd-discuss-phase` | Capture implementation decisions before planning starts |
| `/gsd-plan-phase` | Research, plan, and verify for a single phase |
| `/gsd-execute-phase` | Execute all plans in parallel waves, verify when complete |
| `/gsd-verify-work` | Manual user acceptance testing |
| `/gsd-ship` | Create PR from verified phase work with auto-generated body |
| `/gsd-fast` | Inline trivial tasks, skips planning entirely |

GSD supports the widest range of agents: 14 and counting. Claude Code, Cursor, Windsurf, Codex, Copilot, Gemini CLI, Cline, Augment, Trae, Qwen Code, and more.

## GSTACK: when you need a whole team, not just an engineer

[GSTACK](https://github.com/garrytan/gstack) was created by [Garry Tan](https://www.linkedin.com/in/garrytan/) (CEO of Y Combinator) and has over 71K stars. It takes a fundamentally different approach from the other two frameworks.

Instead of disciplining a single agent, GSTACK models a 23-person team. CEO, product manager, QA lead, engineer, designer, security reviewer. Each role has its own responsibilities, its own constraints, and its own slice of the problem.

The framework enforces five layers of constraint. Role focus keeps each specialist in their lane. Data flow controls what information passes between roles. Quality control gates ensure standards at handoff points. The "boil the lake" principle means each role finishes what it can do perfectly and skips what it cannot, rather than producing mediocre work across everything. And the simplicity layer pushes back against unnecessary complexity.

The role isolation is what makes GSTACK distinctive. The engineer role does not see the product roadmap. The QA role does not see the implementation details. Each role only receives the context it needs to do its job. This is not just about efficiency. It prevents the kind of scope creep where an agent that knows everything tries to do everything.

"Boil the lake" is my favorite principle across all three frameworks. It is the opposite of how most agents work. Agents default to attempting everything and producing something mediocre. GSTACK says: do fewer things, but do them right.

The tradeoff: 23 specialist roles feels heavy for pure infrastructure work. If you are writing Pulumi programs and deploying cloud resources with [component resources](/docs/iac/concepts/components/), you probably do not need a product manager role or a designer role. GSTACK shines when you are building a product, not just provisioning infrastructure.

Each slash command activates a different specialist:

| Command | Role | What it does |
|---------|------|--------------|
| `/office-hours` | YC partner | Six forcing questions that reframe your product before you write code |
| `/plan-ceo-review` | CEO | Four modes: expand scope, selective expand, hold, reduce |
| `/plan-eng-review` | Engineering manager | Lock architecture, map data flow, list edge cases |
| `/review` | Staff engineer | Find bugs that pass CI but break in production, auto-fix the obvious ones |
| `/qa` | QA lead | Real Playwright browser testing, not simulated |
| `/ship` | Release engineer | One-command deploy with coverage audit |
| `/cso` | Security officer | OWASP and STRIDE security audits |

GSTACK works with Claude Code, Codex CLI, OpenCode, Cursor, Factory Droid, Slate, and Kiro.

## Where each framework fits

| | Superpowers | GSD | GSTACK |
|---|---|---|---|
| What it locks down | The dev process itself | The execution environment | Who decides what |
| Orchestration | Single orchestrator | Per-phase orchestrators | 23 specialist roles |
| Context management | One window | State-to-disk, fresh per phase | Role-scoped handoffs |
| Where it shines | TDD, subagent delegation, disciplined plan execution | Marathon sessions, parallel workstreams, crash recovery | Product strategy, multi-perspective review, real browser QA |
| Where it struggles | Anything beyond the build phase | Overkill for small tasks, no role separation | The actual writing-code part |
| Best for | Solo devs who need test discipline | Complex projects that span days or weeks | Founder-engineers shipping a product |
| GitHub stars | 149K | 51K | 71K |
| Agent support | 6 agents | 14+ agents | 7 agents |

For infrastructure work, GSD's context management matters most. Long Pulumi sessions that provision dozens of resources across multiple stacks are exactly the scenario where context rot bites hardest. GSD's phase-based approach keeps each orchestrator fresh.

Superpowers' TDD workflow maps well to application code where unit tests are straightforward. Infrastructure testing is different. You cannot unit test whether an [IAM policy](/docs/iac/clouds/aws/guides/iam/) actually grants the right permissions. You can test the shape of the policy with [Pulumi's testing frameworks](/docs/iac/guides/testing/), but the real validation happens at [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/) and [`pulumi up`](/docs/iac/cli/commands/pulumi_up/). Superpowers still helps here (discipline is discipline), but the TDD cycle is less natural for infra than for app code.

GSTACK shines when the project has product dimensions. If you are building a SaaS platform where the infrastructure serves a product vision, GSTACK's multi-role governance keeps the product thinking connected to the engineering work. For pure infra provisioning, the extra roles add overhead without much benefit.

My honest take: none of these is universally best. Knowing your failure mode is the real decision.

| What keeps going wrong | Try this | The reason |
|------------------------|----------|------------|
| Code works today, breaks tomorrow | Superpowers | Forces every change through a failing test first |
| Quality drops after the first hour | GSD | Fresh context per phase, nothing carries over |
| You ship features nobody asked for | GSTACK | Product review before engineering starts |
| All of the above | GSTACK for direction, bolt on Superpowers TDD | No single framework covers everything yet |

## Combining frameworks with Pulumi workflows

These frameworks solve the "how" of agent orchestration. [Skills](/blog/top-8-claude-skills-devops-2026/) (like the ones from [Pulumi Agent Skills](https://github.com/pulumi/agent-skills)) solve the "what," teaching agents the right patterns for specific technologies. Frameworks and skills complement each other. A skill tells the agent to use [OIDC](/docs/esc/guides/configuring-oidc/aws/) instead of hardcoded credentials. A framework makes sure the agent still remembers that instruction 200K tokens later.

GSD's state-to-disk approach pairs naturally with [Pulumi stack outputs](/docs/iac/concepts/inputs-outputs/). Each phase can read the previous phase's stack outputs from the state files, so a networking phase can provision a VPC and the compute phase can reference the subnet IDs without any context window gymnastics.

Superpowers' TDD cycle maps to infrastructure validation. Write a failing test (the expected shape of your infrastructure). Run [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/) (red, the resources do not exist yet). Run [`pulumi up`](/docs/iac/cli/commands/pulumi_up/) (green, the infrastructure matches the test). This is not a perfect analogy since infrastructure tests are broader than unit tests, but the discipline of "verify before moving on" translates directly.

You do not have to pick one framework and commit forever. Try GSD for a long multi-stack project. Try Superpowers for a focused library. See which failure mode bites you most and let that guide your choice.

## Getting started

{{< github-card repo="obra/superpowers" >}}

{{< github-card repo="gsd-build/get-shit-done" >}}

{{< github-card repo="garrytan/gstack" >}}

All three frameworks support multiple agents. For Claude Code, the install commands are straightforward:

```bash
# Superpowers
/plugin install superpowers@claude-plugins-official

# GSD (the installer asks which agents and whether to install globally or locally)
npx get-shit-done-cc@latest

# GSTACK
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup
```

Check each repository's README for Cursor, Codex, Windsurf, and other agents.

If you want a managed experience that handles orchestration for you, [Pulumi Neo](/product/neo/) is [grounded in your actual infrastructure](/blog/grounded-ai-why-neo-knows-your-infrastructure/), not internet patterns. It understands your stacks, your dependencies, and your deployment history. The [10 things you can do with Neo](/blog/10-things-you-can-do-with-neo/) post shows what that looks like in practice.

Pick one and give it a project. You will know within an hour whether it fixes your particular failure mode.

{{< blog/cta-button "Try Pulumi for Free" "/docs/get-started/" >}}
