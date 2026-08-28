---
title: "Superpowers, GSD, and GSTACK: Picking the Right Framework for Your Coding Agent"
allow_long_title: true
date: 2026-04-13
updated: 2026-08-28
draft: false
faq_schema: true
meta_desc: "Superpowers, GSD, and GSTACK compared and updated: what each does, whether they work with Codex, and the alternatives worth knowing about."
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
    - codex
category: perspectives
social:
    twitter: |
        We gave three AI coding frameworks the same Pulumi project. One caught scope drift the others missed entirely. One we probably won't use again.

        Here's how they compared on real infrastructure work, updated for Codex support and a few alternatives.
    linkedin: |
        We gave three open-source AI coding frameworks the same real infrastructure project and ran them for a few weeks.

        One produced a 41x speedup on a library release along the way. One caught a category of bug the other two missed entirely. One we probably won't reach for again.

        Between them they have accumulated hundreds of thousands of GitHub stars, and completely different theories about what goes wrong when agents work on longer projects. Turns out they're not all solving the same problem.

        Update: we refreshed this with current Codex compatibility, a maintainer change at one of the three projects, and the newer frameworks worth knowing about.
    bluesky: |
        We ran three AI coding frameworks on the same Pulumi infrastructure project for a few weeks. One caught scope drift the other two missed. One we probably won't use again.

        Updated with Codex support and newer alternatives.
---

Three community frameworks have emerged that fix the specific ways AI coding agents break down on real projects. [Superpowers](https://github.com/obra/superpowers) enforces test-driven development. [GSD](https://github.com/open-gsd/gsd-core) prevents context rot. [GSTACK](https://github.com/garrytan/gstack) adds role-based governance. All three started as Claude Code plugins and now reach across Codex, Cursor, Windsurf, Gemini CLI, OpenCode, and half a dozen other agents.

Pulumi uses general-purpose programming languages to define infrastructure. TypeScript, JavaScript, Python, Go, .NET, Java. Every framework that makes AI agents write better TypeScript also makes your `pulumi up` better. After spending a few weeks with each one, and revisiting them again as the space moved, I have opinions about when to use which.

<!--more-->

## What is Claude Code orchestration?

Claude Code orchestration is the practice of wrapping an AI coding agent in a repeatable process instead of letting it freelance: decomposing work into phases, enforcing tests or reviews at each gate, handing state between context windows, and dispatching subagents for isolated tasks. Superpowers, GSD, and GSTACK are the three most widely adopted frameworks that do this, each betting on a different failure mode as the one worth fixing first.

## How do orchestration frameworks differ from single-agent workflows?

A single-agent workflow trusts one continuous conversation to hold the whole project in its head; an orchestration framework assumes that trust breaks down and builds structure around the breakage. AI coding agents are impressive for the first 30 minutes. Then things go sideways. The patterns are predictable enough that three separate teams independently built frameworks to fix them.

**Context rot.** Every LLM has a context window. As that window fills up, earlier instructions fade. You start a session asking for an [S3 bucket](/docs/iac/clouds/aws/guides/) with AES-256 encryption, proper ACLs, and access logging. Two hours and 200K tokens later, the agent creates a new bucket with none of those requirements. The context window got crowded and your original instructions lost weight.

**No test discipline.** Agents write code that looks plausible. Plausible code compiles. Plausible code even runs, for a while. But plausible code without tests is a liability. The agent adds a feature and quietly breaks two others because nothing verified the existing behavior was preserved.

**Scope drift.** You ask for a [VPC with three subnets](/docs/iac/guides/clouds/aws/vpc/). The agent decides you also need a NAT gateway, a transit gateway, a VPN endpoint, and a custom DNS resolver. Helpful in theory. In practice, you now have infrastructure you never requested and barely understand. You will also pay for it monthly.

These problems are not specific to Claude Code or any particular agent. They happen with Cursor, Codex, Windsurf, and every other LLM-powered coding tool. The context window does not care which brand name is on the wrapper.

## Superpowers: what does it do and who is it for?

Superpowers enforces a strict rule: no production code gets written without a failing test first. [Superpowers](https://github.com/obra/superpowers) was created by [Jesse Vincent](https://www.linkedin.com/in/jessevincent/) and has grown to roughly 279K GitHub stars.

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

The results are worth citing carefully. [chardet 7.0's own performance docs](https://chardet.readthedocs.io/en/7.0.0/performance.html) show it running 41x faster than chardet 6.0.0 (494 files/sec versus 12). Maintainer Dan Blanchard [wrote about rewriting chardet from scratch](https://dan-blanchard.github.io/blog/chardet-rewrite-controversy/) with Claude, delegating implementation work to subagents — but his post never names Superpowers, and it's mostly about whether the result counts as a derivative work. Take the 41x figure as verified; take "built with Superpowers specifically" as unconfirmed.

Superpowers now reaches well beyond Claude Code: Antigravity, Codex App, Codex CLI, Cursor, Devin CLI, Factory Droid, Gemini CLI, GitHub Copilot CLI, Grok Build CLI, Kimi Code, OpenCode, Pi, and Hermes Agent are all in its current install list.

## GSD: how does it prevent context rot?

GSD prevents context rot by keeping the orchestrator out of the work: your main session spawns a fresh-context subagent for each research, planning, execution, and verification task, then collects results instead of accumulating them. [GSD](https://github.com/open-gsd/gsd-core) (Get Shit Done) was created by Lex Christopherson, known online as TÂCHES.

The key architectural decision: the orchestrator never touches source files. Because it only spawns agents, collects their results, and updates shared state on disk, its own context window grows slowly and predictably, while each spawned agent starts with a clean window scoped to exactly one task. Phase state lands in `.planning/` as durable files, so the next step reads artifacts rather than conversation history.

Think about why this matters. When the orchestrator also writes the code, your 200K token context window is a shared resource. Instructions from hour one compete with code from hour three. GSD sidesteps this entirely, because the orchestrator's job is dispatch and bookkeeping, not implementation. GSD also includes quality gates that detect schema drift and scope reduction. If the agent starts cutting corners or wandering from the plan, the gates catch it.

**What changed since this post first ran:** the original repository, `gsd-build/get-shit-done`, was [archived by its owner on June 26, 2026](https://github.com/gsd-build/get-shit-done) with 64.6K stars frozen in place. Development continues in the Open GSD organization as [GSD Core](https://github.com/open-gsd/gsd-core), currently at roughly 8.8K stars and installed via `npx @opengsd/gsd-core@latest`.

The tradeoff: GSD has more ceremony than the other two frameworks. For a quick script or a single-file change, the phase-based workflow is overkill. GSD earns its keep on projects that span multiple files, multiple sessions, or multiple days.

The core commands map to a phase-based workflow:

| Command | What it does |
|---------|--------------|
| `/gsd-new-project` | Full initialization: questions, research, requirements, roadmap |
| `/gsd-onboard` | Onboard an existing codebase instead of starting greenfield |
| `/gsd-discuss-phase` | Capture implementation decisions before planning starts |
| `/gsd-plan-phase` | Research, plan, and verify for a single phase |
| `/gsd-execute-phase` | Execute all plans in parallel waves, verify when complete |
| `/gsd-verify-work` | Manual user acceptance testing |
| `/gsd-ship` | Create PR from verified phase work with auto-generated body |

GSD Core's installer supports Claude Code, OpenCode, Antigravity CLI, Kimi CLI, Kilo, Codex, Copilot, Cursor, and Windsurf, and prompts you for which one at install time.

## GSTACK: what does role-based governance buy you?

GSTACK buys you a division of labor: instead of one agent trying to hold product, engineering, QA, and security judgment simultaneously, it splits the work across 23 specialist roles, each with its own scope and constraints. [GSTACK](https://github.com/garrytan/gstack) was created by [Garry Tan](https://www.linkedin.com/in/garrytan/) (President and CEO of Y Combinator) and has grown to roughly 130K stars.

The framework enforces five layers of constraint. Role focus keeps each specialist in their lane. Data flow controls what information passes between roles. Quality control gates ensure standards at handoff points. The "boil the lake" principle means each role finishes what it can do perfectly and skips what it cannot, rather than producing mediocre work across everything. And the simplicity layer pushes back against unnecessary complexity.

The role isolation is what makes GSTACK distinctive. The engineer role does not see the product roadmap. The QA role does not see the implementation details. Each role only receives the context it needs to do its job. This is not just about efficiency. It prevents the kind of scope creep where an agent that knows everything tries to do everything.

"Boil the lake" is my favorite principle across all three frameworks. It is the opposite of how most agents work. Agents default to attempting everything and producing something mediocre. GSTACK says: do fewer things, but do them right.

The tradeoff: 23 specialist roles feels heavy for pure infrastructure work. If you are writing Pulumi programs and deploying cloud resources with [component resources](/docs/iac/concepts/components/), you probably do not need a product manager role or a designer role. GSTACK shines when you are building a product, not just provisioning infrastructure.

Each slash command activates a different specialist:

| Command | Role | What it does |
|---------|------|---------------|
| `/office-hours` | YC partner | Six forcing questions that reframe your product before you write code |
| `/plan-ceo-review` | CEO | Four modes: expand scope, selective expand, hold, reduce |
| `/plan-eng-review` | Engineering manager | Lock architecture, map data flow, list edge cases |
| `/review` | Staff engineer | Find bugs that pass CI but break in production, auto-fix the obvious ones |
| `/qa` | QA lead | Real Playwright browser testing, not simulated |
| `/ship` | Release engineer | One-command deploy with coverage audit |
| `/cso` | Security officer | OWASP and STRIDE security audits |

GSTACK's Codex support is the most deliberate of the three: setup reads the `model` field from your `~/.codex/config.toml` and generates a matching behavioral profile automatically, so the role constraints adapt to the specific Codex model you are running. It also supports Claude Code, OpenCode, Cursor, Factory Droid, Slate, Kiro, and Hermes.

## Superpowers, GSD, or GSTACK: which one should you use?

None of these is universally best. Knowing your failure mode is the real decision.

| | Superpowers | GSD | GSTACK |
|---|---|---|---|
| What it locks down | The dev process itself | The execution environment | Who decides what |
| Orchestration | Single orchestrator | Per-phase orchestrators | 23 specialist roles |
| Context management | One window | State-to-disk, fresh per phase | Role-scoped handoffs |
| Where it shines | TDD, subagent delegation, disciplined plan execution | Marathon sessions, parallel workstreams, crash recovery | Product strategy, multi-perspective review, real browser QA |
| Where it struggles | Anything beyond the build phase | Overkill for small tasks, no role separation | The actual writing-code part |
| Best for | Solo devs who need test discipline | Complex projects that span days or weeks | Founder-engineers shipping a product |
| GitHub stars (current) | ~279K | ~8.8K on the new repo (plus 64.6K on the archived original) | ~130K |
| Agent support | 13+ agents | 9+ agents via installer | 8+ agents |

For infrastructure work, GSD's context management matters most. Long Pulumi sessions that provision dozens of resources across multiple stacks are exactly the scenario where context rot bites hardest. GSD's phase-based approach keeps each orchestrator fresh.

Superpowers' TDD workflow maps well to application code where unit tests are straightforward. Infrastructure testing is different. You cannot unit test whether an [IAM policy](/docs/iac/guides/clouds/aws/iam/) actually grants the right permissions. You can test the shape of the policy with [Pulumi's testing frameworks](/docs/iac/guides/testing/), but the real validation happens at [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/) and [`pulumi up`](/docs/iac/cli/commands/pulumi_up/). Superpowers still helps here (discipline is discipline), but the TDD cycle is less natural for infra than for app code.

GSTACK shines when the project has product dimensions. If you are building a SaaS platform where the infrastructure serves a product vision, GSTACK's multi-role governance keeps the product thinking connected to the engineering work. For pure infra provisioning, the extra roles add overhead without much benefit.

| What keeps going wrong | Try this | The reason |
|------------------------|----------|------------|
| Code works today, breaks tomorrow | Superpowers | Forces every change through a failing test first |
| Quality drops after the first hour | GSD | Fresh context per phase, nothing carries over |
| You ship features nobody asked for | GSTACK | Product review before engineering starts |
| All of the above | GSTACK for direction, bolt on Superpowers TDD | No single framework covers everything yet |

{{< blog/cta-card title="Point your coding agent at Pulumi" href="/docs/ai/" >}}
Whichever framework and agent you run, Pulumi defines infrastructure in TypeScript, Python, and Go, so your agent generates cloud resources it already knows how to write.
{{< /blog/cta-card >}}

## Do Superpowers, GSD, and GSTACK work with Codex?

Yes, all three now support OpenAI's Codex, though the depth of that support varies. Superpowers ships two separate Codex integrations distributed through the official OpenAI plugin marketplace; GSTACK goes furthest by detecting your specific Codex model and generating a matching behavioral profile; GSD's installer offers Codex as one of several supported runtimes without Codex-specific tuning.

| Framework | Codex support | How it works |
|---|---|---|
| Superpowers | Native, dual-mode | Separate "Codex App" and "Codex CLI" integrations, both installed through the [official Codex plugin marketplace](https://github.com/openai/plugins) |
| GSD (GSD Core) | Native, generic | The `npx @opengsd/gsd-core@latest` installer lists Codex as a supported runtime alongside Claude Code, Cursor, and others |
| GSTACK | Native, model-aware | `./setup --host codex` installs to `~/.codex/skills/gstack-*/` and reads your Codex model from `config.toml` to tune role behavior automatically |

Codex support has deepened noticeably since this post first ran. All three frameworks now treat it as a first-class target rather than one more name in an install matrix.

## What are the alternatives to Superpowers, GSD, and GSTACK?

The most talked-about alternative right now is [Everything Claude Code](https://github.com/affaan-m/ecc) (ECC), built by Affaan Mustafa. Where Superpowers, GSD, and GSTACK each impose one opinionated methodology, ECC takes the opposite approach: a large pre-built bundle of subagents, skills, hooks, and commands — dozens of the first, hundreds of the second — plus a security layer called AgentShield. It works best with Claude Code today, has a supported Codex sync path, and offers capability-limited adapters for Cursor and OpenCode, so check its support-status matrix before assuming feature parity across agents. It has grown large enough that community threads now debate "ECC vs. Superpowers" the same way they debate the three frameworks above. Choose ECC if you want breadth and are willing to pick your own process; choose one of the three above if you want the process itself enforced.

Also worth knowing: [`wshobson/agents`](https://github.com/wshobson/agents) positions itself as a plugin marketplace rather than a single framework, aggregating dozens of agents, skills, and commands that install natively through Claude Code's plugin system. It is less a competitor to Superpowers, GSD, or GSTACK than a different shelf in the same store.

You can also roll your own. Claude Code's native subagents, hooks, and skills now cover a meaningful slice of what these frameworks automate, including asynchronous subagent execution that used to require a third-party context-management layer. If your needs are narrow, a CLAUDE.md file plus a couple of custom skills may get you 80% of the value without adopting a whole framework.

For infrastructure specifically, there is also the managed-agent route rather than the framework route — see the note on [Pulumi Neo](/product/neo/) at the end of this post.

## How do these frameworks work with Pulumi?

These frameworks solve the "how" of agent orchestration. [Skills](/blog/top-8-claude-skills-devops-2026/) (like the ones from [Pulumi Agent Skills](https://github.com/pulumi/agent-skills)) solve the "what," teaching agents the right patterns for specific technologies. Frameworks and skills complement each other. A skill tells the agent to use [OIDC](/docs/esc/guides/configuring-oidc/aws/) instead of hardcoded credentials. A framework makes sure the agent still remembers that instruction 200K tokens later. This works because Pulumi infrastructure is real code: an agent operating under Superpowers' TDD gates or GSD's phase boundaries can test, refactor, and version infrastructure the same way it does application code, which a declarative config format does not give it room to do.

GSD's state-to-disk approach pairs naturally with [Pulumi stack outputs](/docs/iac/concepts/inputs-outputs/). Each phase can read the previous phase's stack outputs from the state files, so a networking phase can provision a VPC and the compute phase can reference the subnet IDs without any context window gymnastics.

Superpowers' TDD cycle maps to infrastructure validation. Write a failing test (the expected shape of your infrastructure). Run [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/) (red, the resources do not exist yet). Run [`pulumi up`](/docs/iac/cli/commands/pulumi_up/) (green, the infrastructure matches the test). This is not a perfect analogy since infrastructure tests are broader than unit tests, but the discipline of "verify before moving on" translates directly.

You do not have to pick one framework and commit forever. Try GSD for a long multi-stack project. Try Superpowers for a focused library. See which failure mode bites you most and let that guide your choice.

## How do you install and get started?

{{< github-card repo="obra/superpowers" >}}

{{< github-card repo="open-gsd/gsd-core" >}}

{{< github-card repo="garrytan/gstack" >}}

All three frameworks support multiple agents. For Claude Code, the current install commands are:

```bash
# Superpowers
/plugin install superpowers@claude-plugins-official

# GSD Core (installer asks which agent and whether to install globally or locally)
npx @opengsd/gsd-core@latest

# GSTACK
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup
```

If you have an old GSD install pointed at `get-shit-done-cc`, switch to `@opengsd/gsd-core`; the original repository is archived and will not receive further updates. Check each repository's README for Codex, Cursor, Windsurf, and other agent-specific instructions.

If you want a managed experience that handles orchestration for you, [Pulumi Neo](/product/neo/) is [grounded in your actual infrastructure](/blog/grounded-ai-why-neo-knows-your-infrastructure/), not internet patterns. It understands your stacks, your dependencies, and your deployment history. The [10 things you can do with Neo](/blog/10-things-you-can-do-with-neo/) post shows what that looks like in practice.

Pick one and give it a project. You will know within an hour whether it fixes your particular failure mode.

{{< blog/cta-button "Try Pulumi for Free" "/docs/get-started/" >}}
