---
title: "Claude Skills for DevOps: What I Use and How I Vet Them"
date: 2026-02-09
updated: 2026-11-11
draft: false
meta_desc: "The Claude skills for DevOps I use for Pulumi, Kubernetes, monitoring, and incident response, plus how to scan third-party skills for malicious code first."
feature_image: feature.png
authors:
    - engin-diri
tags:
    - ai
    - devops
    - platform-engineering
    - claude-code
    - ai-agents
category: best-practices
faq_schema: true
---

When Claude Code first released [skills](https://code.claude.com/docs/en/skills), I ignored them. They looked like fancy prompts, another feature to add to the pile of things I would get around to learning eventually. Then I watched a few engineers demonstrate what skills actually do, and something clicked. By default, language models do not write good code. They write plausible code based on what they have read. Plausible code turns into bugs, horrible UX, and infrastructure that breaks at 3am.

<!--more-->

Skills fill that gap. They package engineering expertise into something Claude can use. The workflows and judgment matter more than the raw information. Without skills, every conversation starts from zero. You explain the same conventions and correct the same mistakes. Every morning, back to zero.

The best Claude skills for DevOps are the ones that encode a specific workflow: Pulumi best practices and ESC, monitoring, Kubernetes configuration, systematic debugging, security review, and incident runbooks. Install them from repositories with visible maintainers, and scan every third-party skill before it touches a project, because a skill runs with your agent's permissions.

Think about what separates a junior engineer from a senior one. Both can write code that compiles. Both can deploy infrastructure that runs. The difference is that the senior engineer knows the patterns that prevent problems before they happen. They know when to use component resources instead of plain resources. They know that creating infrastructure inside an `apply()` callback (Pulumi's way of transforming outputs that are not known until deployment) breaks preview. They know that hardcoded credentials will eventually end up in a git log somewhere embarrassing.

This knowledge takes years to accumulate through painful experience. Skills let you transfer that knowledge to Claude in minutes. And here is the thing that makes them practical: if you find yourself doing the same type of task with different content each time, that is a skill waiting to be built. You encode the process once, then feed it new inputs forever.

## The mechanic, the tools, and the manual

I heard an analogy recently that made skills click for me. Imagine Claude as a mechanic. A capable mechanic who knows engines, can diagnose problems, and fix most cars that come through the shop.

[MCP servers](https://modelcontextprotocol.io/) are like giving that mechanic a set of tools. Wrenches, diagnostic equipment, lift systems. Without tools, the mechanic cannot do much. With tools, the mechanic can work on whatever comes through the door.

But what happens when someone brings in a Formula 1 race car? Or a 1967 Ford Mustang that has been modified beyond recognition? The mechanic knows engines in general, but these specific vehicles require specific knowledge. The F1 car has procedures that must be followed in exact order. The vintage Mustang has quirks that only someone who has worked on that model would know.

Skills are the user manuals and standard operating procedures for these specific vehicles. They tell the mechanic what needs to happen and when. They encode the expertise of someone who has done this work a thousand times.

Or think about it from a carpenter's perspective. Skills are the process to make the table: the measurements, the design, the exact steps. MCPs are the tools: the saw, the hammer, the drill. You need both. The process alone is theoretical, and tools without a process just sit in the garage.

For DevOps engineers working with Pulumi, this matters because infrastructure as code has its own quirks and patterns. Generic AI assistance produces code that looks reasonable but breaks conventions the community learned the hard way. Skills teach Claude those conventions.

## Why skills instead of MCPs

Before skills clicked for me, I tried solving the expertise problem with MCPs. I kept adding servers until I noticed Claude getting slower and making worse decisions. Turns out the GitHub MCP alone [eats 46,000 tokens across 91 tools](https://smcleod.net/2025/08/stop-polluting-context-let-users-disable-individual-mcp-tools/) before you type anything. Cursor eventually [capped MCPs at 40 tools](https://demiliani.com/2025/09/04/model-context-protocol-and-the-too-many-tools-problem/) because [too many options made everything worse](https://jentic.com/blog/the-mcp-tool-trap).

Slash commands were another option, but you had to remember to invoke them. Anthropic apparently agreed: Claude Code has since [merged custom commands into skills](https://code.claude.com/docs/en/skills), so a skill with a name is also a slash command. One unified system instead of two.

Skills avoid this through progressive disclosure. Claude reads just the description at startup, maybe a hundred tokens. The full procedures only load when Claude decides they are relevant. Unlike those massive system prompts that used to eat through your context window, skills stay out of the way until they are needed. For DevOps engineers running long infrastructure sessions with dozens of resources, this matters. You keep your context budget for the actual work instead of burning it on instructions. Skills can also fork context, spinning up isolated subagents that do work without polluting your main conversation. Think of it like handing a colleague a written brief. They go work on it, hand back a summary, and never sit in on your conversation.

I still use MCPs for connecting Claude to external systems. The [Pulumi MCP server](/blog/mcp-server-ai-assistants/) lets Claude query the registry and validate code. But MCPs give Claude access to things. Skills teach Claude how to think about things. Different jobs. They get more useful when you combine them. One engineer built a financial reporting skill that connects to his Mercury bank account via MCP, pulls every transaction for a given month, classifies the expenses into categories, and generates a styled HTML report with totals and breakdowns. A skill that knows your deployment process connecting to MCPs that talk to your actual infrastructure is the same idea, just pointed at ops instead of accounting. If you want that combination ready-made for infrastructure, [Pulumi Neo](/product/neo/) is an agent that already works from your stacks, deployment history, and policies.

> [!NOTE]
> Skills are portable. They follow an [open standard](https://agentskills.io), so a skill you write for Claude Code also works in Cursor, GitHub Copilot, VS Code, OpenAI Codex, Gemini CLI, and other agents that support it. You can even copy the skill content into ChatGPT as a starting prompt. No vendor lock-in.

## Teaching Claude to write Pulumi like an expert

The first time you ask Claude to help with a Pulumi project, the process is painful. You have to explain the patterns you want. You correct mistakes. You explain why creating resources inside `apply()` breaks things. By the third or fourth project, you start copying your corrections from previous conversations.

I built the [dirien/claude-skills](https://github.com/dirien/claude-skills) `pulumi-typescript` skill after going through this painful process too many times. It knows the patterns that prevent common mistakes: [Pulumi ESC (Environments, Secrets, and Configuration)](/blog/pulumi-esc-ga/) integration, [OIDC (OpenID Connect) instead of hardcoded access keys](/blog/oidc-trust-relationships/), ComponentResource abstractions (reusable groups of related resources), and proper output structuring so dependent stacks can consume them cleanly.

| Skill | What it teaches Claude |
|-------|------------------------|
| `pulumi-typescript` | Pulumi with TypeScript, ESC secrets management, component patterns, and multi-cloud deployment |

```bash
npx skills add https://github.com/dirien/claude-skills --skill pulumi-typescript
```

Skills install as markdown files in your project's `.claude/skills/` directory, so they travel with your repo and are easy to review.

The next time you ask Claude to create infrastructure, it applies these patterns automatically. You do not have to remember to invoke the skill or correct the same mistakes repeatedly.

## The official Pulumi skills

Pulumi maintains its own skills repository at [pulumi/agent-skills](https://github.com/pulumi/agent-skills), which they [announced earlier this year](/blog/pulumi-agent-skills/). It has grown into 17 skills organized as plugins: authoring skills such as `pulumi-best-practices`, `pulumi-esc`, `pulumi-component`, `pulumi-automation-api`, and `pulumi-debug-failed-operation`; migration skills for Terraform, CDK, CloudFormation, and ARM; a handoff skill for delegating long-running work to an agent; and maintenance skills for provider authors. The two I use daily are still `pulumi-esc` and `pulumi-best-practices`.

The `pulumi-esc` skill teaches Claude how to work with [Pulumi ESC (Environments, Secrets, and Configuration)](/product/secrets-management/). It knows the difference between `pulumi env get`, `pulumi env open`, and `pulumi env run`. It sets up OIDC for dynamic credentials, integrates with external secret stores like AWS Secrets Manager and Vault, and structures layered environment composition so your dev, staging, and production configs inherit from a shared base.

The `pulumi-best-practices` skill catches the mistakes that burn you in production. It stops Claude from creating resources inside `apply()` callbacks, enforces proper parent relationships in ComponentResources, encrypts secrets from day one, and makes sure `pulumi preview` runs before any deployment. These are the patterns that took me years to internalize, and now Claude follows them by default.

| Skill | What it teaches Claude |
|-------|------------------------|
| `pulumi-esc` | Environment, secrets, and configuration management with OIDC, dynamic credentials, and secret store integration |
| `pulumi-best-practices` | Resource dependencies, ComponentResource patterns, secret encryption, and safe refactoring |

```bash
npx skills add https://github.com/pulumi/agent-skills --skill pulumi-esc
npx skills add https://github.com/pulumi/agent-skills --skill pulumi-best-practices
```

If you use Claude Code, the repository also documents a plugin install that pulls in the whole authoring and migration set at once:

```text
/plugin marketplace add pulumi/agent-skills
/plugin install pulumi
```

## Making Claude a monitoring expert by default

You deploy something, it works, and six months later something breaks and you realize you never added monitoring. We have all been there. The monitoring skills from the community teach Claude to add observability from the start.

The [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills) repository contains a `monitoring-expert` skill that knows Prometheus, Grafana, and DataDog.

| Skill | What it teaches Claude |
|-------|------------------------|
| `monitoring-expert` | Structured logging, metrics, distributed tracing, alerting, and performance testing for production systems |

```bash
npx skills add https://github.com/jeffallan/claude-skills --skill monitoring-expert
```

In my testing, deploying a static website with these skills installed looks different from vanilla Claude. Instead of just creating the S3 bucket and CloudFront distribution, Claude asked about error rate thresholds before writing any code. It suggested CloudWatch alarms and created an SNS topic for alerts. The results are not always this clean. Sometimes the monitoring suggestions are generic or miss your specific SLO requirements. But the baseline shifted from "no monitoring at all" to "monitoring that needs tuning," and that is a better starting point.

## Kubernetes configuration that actually passes security review

Kubernetes has hundreds of configuration options. Most deployments use a handful of them. The problem is that the important options like security contexts, resource limits, and pod disruption budgets are easy to forget when you are focused on getting something to run.

The [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills) `kubernetes-specialist` skill focuses on configurations that production deployments actually need. Without it, ask Claude for a deployment and you get something that runs: the right image, the right ports, maybe a service. With the skill, the same request comes back with `runAsNonRoot: true` in the security context, resource requests and limits that reflect actual usage patterns, liveness and readiness probes with sensible intervals, and a pod disruption budget. These are the things that make the difference between "it works in staging" and "it survives a node failure in production." The skill also understands when RollingUpdate makes sense versus Recreate, which is the kind of judgment call that usually requires context a generic model does not have.

The [wshobson/agents](https://github.com/wshobson/agents) repository fills in the gaps around Kubernetes with CI/CD, cost management, and deployment workflows:

| Skill | What it teaches Claude |
|-------|------------------------|
| `kubernetes-specialist` | Production cluster management, security hardening, and cloud-native architectures |
| `cost-optimization` | Cloud cost reduction across AWS, Azure, and GCP with right-sizing and reserved instances |
| `github-actions-templates` | CI/CD workflows, Docker builds, Kubernetes deployments, security scanning, and matrix builds |
| `gitops-workflow` | ArgoCD and Flux CD for automated Kubernetes deployments |

```bash
npx skills add https://github.com/jeffallan/claude-skills --skill kubernetes-specialist
npx skills add https://github.com/wshobson/agents --skill gitops-workflow
npx skills add https://github.com/wshobson/agents --skill github-actions-templates
npx skills add https://github.com/wshobson/agents --skill cost-optimization
```

## Debugging like a senior engineer

The [obra/superpowers](https://github.com/obra/superpowers) repository contains a skill that changed how I debug with Claude. The `systematic-debugging` skill implements a four-phase framework: root cause investigation, pattern analysis, hypothesis testing, and implementation.

Without this skill, Claude tends to suggest solutions immediately. Something is broken, here are five things that might fix it. This feels helpful but often wastes time because none of the suggestions address the actual problem.

With the systematic debugging skill, Claude approaches problems differently. It asks clarifying questions. It wants to see logs. It builds a model of what is happening before suggesting changes. When it proposes a fix, it explains why that fix addresses the root cause. Sometimes skills find problems you did not know about. One engineer pointed a skills-equipped Claude at a set of SEO pages and discovered they had been decaying for months with nobody watching. The infrastructure parallel is obvious: configuration drift, unused resources, permissions that expanded over time. A debugging skill that investigates before prescribing will find these things.

| Skill | What it teaches Claude |
|-------|------------------------|
| `systematic-debugging` | Root cause investigation, pattern analysis, hypothesis testing, and verified implementation |

```bash
npx skills add https://github.com/obra/superpowers --skill systematic-debugging
```

## Catching security issues before they ship

Two pieces cover different sides of security review. The [wshobson/agents](https://github.com/wshobson/agents) `k8s-security-policies` skill handles Kubernetes-specific hardening: NetworkPolicies, Pod Security Standards, RBAC, OPA Gatekeeper constraints, and service mesh mTLS configuration. For application-level concerns like secrets management, injection, and input validation, Claude Code ships a built-in [`/security-review` command](https://code.claude.com/docs/en/commands) that checks your current diff for security vulnerabilities. I originally installed a community `security-review` skill from a large aggregator repository. Claude Code's own command does the same job without a third-party install, which matters given what the vetting section below covers.

I asked Claude to check a Pulumi program that created an S3 bucket. Without the security skills, Claude confirmed the code was correct and moved on. With the skills loaded, it flagged that the bucket had no server-side encryption configured, the bucket policy allowed `s3:*` from an overly broad principal, and there was no access logging enabled. On the Kubernetes side, the `k8s-security-policies` skill catches things like missing default-deny NetworkPolicies and containers running as root. These skills are not a replacement for deterministic tools like tfsec, checkov, or trivy. Those catch known issues every time. Skills are probabilistic and work best as an extra layer during development, not as your only security gate.

| Skill | What it teaches Claude |
|-------|------------------------|
| `k8s-security-policies` | Network policies, pod security standards, RBAC, and admission control for defense-in-depth |
| `/security-review` (built in) | Checks the current diff for security vulnerabilities such as exposed secrets, injection, and unsafe input handling |

```bash
npx skills add https://github.com/wshobson/agents --skill k8s-security-policies
```

## Incident response before you need it

At 3am when something breaks, you want runbooks. The `incident-runbook-templates` skill from [wshobson/agents](https://github.com/wshobson/agents) helps Claude create these before you need them. It includes a four-level severity model (SEV1 through SEV4) with response time expectations, escalation decision trees, and communication templates for status updates.

When you ask Claude to document your deployment process, it produces runbooks with diagnostic steps, rollback protocols, and verification checks. It knows kubectl commands for Kubernetes recovery and SQL procedures for PostgreSQL troubleshooting. The output needs editing. Generated runbooks tend to be thorough on the happy path but thin on the failure modes that matter most at 3am. I treat them as a first draft that gets me to 60% in minutes instead of hours, then fill in the gaps from experience.

| Skill | What it teaches Claude |
|-------|------------------------|
| `incident-runbook-templates` | Detection, triage, mitigation, resolution, and communication procedures for production incidents |

```bash
npx skills add https://github.com/wshobson/agents --skill incident-runbook-templates
```

## General-purpose DevOps and SRE skills

The skills above target specific problems. The [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills) repository also includes two broader skills that cover the day-to-day work that does not fit neatly into one category.

The `devops-engineer` skill gives Claude a senior DevOps engineer persona covering CI/CD pipelines, container management, deployment strategies like blue-green and canary, and infrastructure as code across AWS, GCP, and Azure. It enforces constraints I care about: no deploying to production without approval, no secrets in code, no unversioned container images.

The `sre-engineer` skill focuses on reliability: SLO/SLI definitions, error budget calculations, golden signal dashboards, and toil reduction through automation. It produces Prometheus/Grafana configs, remediation runbooks, and reliability assessments. If you run production systems and want Claude to think about error budgets instead of just uptime, this is the skill.

| Skill | What it teaches Claude |
|-------|------------------------|
| `devops-engineer` | CI/CD pipelines, container management, deployment strategies, and infrastructure as code across clouds |
| `sre-engineer` | SLI/SLO management, error budgets, monitoring, automation, and incident response |

```bash
npx skills add https://github.com/jeffallan/claude-skills --skill devops-engineer
npx skills add https://github.com/jeffallan/claude-skills --skill sre-engineer
```

## How do you vet a third-party Claude skill before installing it?

Read every file in the skill, check who maintains the repository, commit the skill into your own repo so changes show up in review, and run a skill scanner before first use. A skill runs with your agent's permissions, so a malicious one can read credentials, run commands, and change what the agent does while looking like normal agent behavior.

Anthropic's own guidance says to [use skills only from trusted sources](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), because a malicious skill can direct Claude to call tools or run code in ways that do not match the skill's stated purpose. The same page warns that skills fetching external URLs are a particular risk, since even a trustworthy skill can be compromised if its external dependencies change over time.

The numbers back that up. Snyk researchers published [ToxicSkills](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) in February 2026 after scanning 3,984 skills from public registries. 13.4% had critical-level issues and 76 were confirmed malicious. The techniques included base64-encoded commands that steal AWS credentials, instructions to download password-protected executables from attacker infrastructure, and jailbreak text that tries to disable safety mechanisms. 91% of the malicious skills combined code-level malware with prompt injection. Separately, Koi Security reported [341 malicious skills on ClawHub](https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting) in the ClawHavoc campaign, and Palo Alto Networks' Unit 42 [found malicious skills persisting](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/) after the registry added its own scanning. A registry scan is a filter. It does not replace your own review.

Start with the source. A skill is markdown plus whatever scripts, templates, and reference files sit beside it, and the `SKILL.md` text is itself an instruction channel, so prompt injection can hide in plain prose as easily as in a script. If you cannot read the whole skill in a few minutes, treat that as a red flag. Look at the repository too: contributor history, how long it has existed, and whether the maintainer is someone you can identify. Be most careful with skills that pull content from third-party URLs at runtime. Snyk found 17.7% of the skills it scanned did this, which means the behavior you reviewed can change after you install it.

Next, make changes visible. Install skills into your project's `.claude/skills/` directory and commit them, so an update to a skill arrives as a diff in a pull request instead of a silent upgrade. Pin to a commit or tag where the install method allows it, and review the diff when you bump.

Then scan. Snyk's open source Agent Scan, previously published as `mcp-scan`, checks skills for prompt injection, malware payloads, and sensitive data handling:

```bash
# Scan every skill Claude Code has installed for your user
uvx snyk-agent-scan@latest ~/.claude/skills

# Scan one skill before you install it
uvx snyk-agent-scan@latest ~/path/to/my/SKILL.md
```

Check the [Agent Scan README](https://github.com/snyk/agent-scan) before the first run, since it documents which parts of a scan contact external services and recommends running scans of untrusted content in a sandbox. Cisco's [skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) combines static rules, behavioral dataflow analysis, and optional LLM-based review, and supports a pre-commit hook and CI exit codes, so a pull request that adds or changes a `SKILL.md` can fail before it merges. NVIDIA's [SkillSpector](https://github.com/NVIDIA/SkillSpector) is another option, and the OWASP Agentic Skills Top 10 has a [scanner integration guide](https://owasp.org/www-project-agentic-skills-top-10/skill-scanner-integration) with pre-commit examples. Scanners miss things, so use them to raise the cost of an attack and not as proof that a skill is safe.

Finally, limit what a bad skill could do. Claude Code lets you restrict tools per skill with `allowed-tools` in the skill frontmatter, set `disable-model-invocation` on skills that should only run when you call them, deny risky commands through permission rules, and block tool calls with `PreToolUse` hooks. Simon Willison's [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) is a useful test: an agent that combines access to private data, exposure to untrusted content, and a way to communicate externally can be made to leak. Keep at least one of the three out of the session. Credentials are the part you control most directly. [Short-lived OIDC credentials from Pulumi ESC](/blog/oidc-trust-relationships/) mean there is no long-lived cloud key sitting in your environment for a compromised skill to find.

{{< blog/cta-card title="Build infrastructure with agent skills" href="/docs/ai/skills/" >}}
Pulumi's Agent Skills teach Claude Code, Cursor, or any coding agent the infrastructure patterns covered here. Install them, then build and deploy your stacks with fewer corrections.
{{< /blog/cta-card >}}

## Putting it together

Stacking skills is where this pays off. Install the Pulumi skills and Claude writes better infrastructure code. Add monitoring and security on top and you start catching problems that used to slip through to production.

A note on stacking: I have not hit conflicts running all of these simultaneously, but more skills means more descriptions for Claude to evaluate at startup. If you notice Claude getting slower or making odd choices, pare back to the skills you actually use for that project. Start with the Pulumi and monitoring skills, add others as you need them.

Here is how to set up a new project with all of them:

```bash
mkdir -p pulumi-skills-demo && cd pulumi-skills-demo
pulumi new aws-typescript --name skills-demo --yes

npx skills add https://github.com/dirien/claude-skills --skill pulumi-typescript
npx skills add https://github.com/pulumi/agent-skills --skill pulumi-esc
npx skills add https://github.com/pulumi/agent-skills --skill pulumi-best-practices
npx skills add https://github.com/obra/superpowers --skill systematic-debugging
npx skills add https://github.com/jeffallan/claude-skills --skill monitoring-expert
npx skills add https://github.com/jeffallan/claude-skills --skill kubernetes-specialist
npx skills add https://github.com/wshobson/agents --skill gitops-workflow
npx skills add https://github.com/wshobson/agents --skill github-actions-templates
npx skills add https://github.com/wshobson/agents --skill cost-optimization
npx skills add https://github.com/wshobson/agents --skill incident-runbook-templates
npx skills add https://github.com/jeffallan/claude-skills --skill devops-engineer
npx skills add https://github.com/jeffallan/claude-skills --skill sre-engineer
npx skills add https://github.com/wshobson/agents --skill k8s-security-policies
```

The `/security-review` command ships with Claude Code, so it needs no install line. Then try these two prompts to see how many skills activate at once:

```bash
# Static website — triggers Pulumi TypeScript, monitoring, and security skills
Create a Pulumi TypeScript program for a static website on AWS with S3, CloudFront, OIDC credentials via Pulumi ESC, CloudWatch monitoring, and /security-review the infrastructure before deploying
```

```bash
# EKS cluster — stacks Kubernetes, GitOps, incident response, cost, and SRE skills
Create a Pulumi TypeScript program for an EKS cluster with /kubernetes-specialist security hardening, /gitops-workflow for ArgoCD deployment, /incident-runbook-templates for the cluster, /cost-optimization recommendations, and /sre-engineer SLO definitions for the services
```

The first prompt triggers the Pulumi TypeScript, monitoring, and security review skills in a single conversation. The second stacks Kubernetes, GitOps, incident response, cost, and SRE skills on one cluster build. You get infrastructure code, operational runbooks, and security policies from a single request.

## What changes

Fair warning: not every skill works perfectly on the first try. Some need iteration. Some produce output that you have to review and tweak before it matches your standards. Skills do not replace your judgment.

That said, after a few weeks with these skills installed, I stopped correcting the same mistakes. The code Claude writes now looks like code I would write, not code I would have to fix. That is the whole point. Skills just stop you from repeating the same corrections across every conversation.

## Frequently asked questions

### What are Claude skills?

Claude skills are folders containing a SKILL.md file with a name, a description, and instructions, plus optional scripts and reference files. Claude reads only the description at startup and loads the full instructions when a task matches, so skills add expertise without filling the context window. They follow the open Agent Skills standard.

### Are Claude skills safe to install?

Skills from maintainers you can identify and that you have read are a reasonable risk, but public registries have hosted malicious skills. A skill runs with your agent's permissions and can carry prompt injection in its text or malware in its scripts. Read the full skill, commit it to your repository, scan it, and limit its tool access before use.

### How do I scan a SKILL.md file for malicious instructions?

Run a skill scanner such as Snyk Agent Scan with uvx snyk-agent-scan@latest followed by the path to the skill, or Cisco's skill-scanner with skill-scanner scan followed by the path. Both can run in CI or a pre-commit hook so a changed skill fails the build. Treat results as a filter and still read the skill yourself.

### Do Claude skills work outside Claude Code?

Yes. Skills follow the open Agent Skills standard, so the same SKILL.md folder works in Cursor, GitHub Copilot, VS Code, OpenAI Codex, Gemini CLI, and other agents that support the standard. Install paths and some frontmatter options differ by tool, so check each tool's documentation after copying a skill across.

## Get started

Every skill in this post includes its install command. Pick the section that matches your biggest pain point, run the `npx skills add` command, and try it on your next task. Skills work in Claude Code, Cursor, GitHub Copilot, and anything else that supports the [Agent Skills standard](https://agentskills.io). Scan anything you did not write before you install it.

The [Pulumi Agent Skills announcement](/blog/pulumi-agent-skills/) has more details, and the [GitHub repository](https://github.com/pulumi/agent-skills) has the source. If you want something that goes further, with organizational context and deployment governance, look at [Pulumi Neo](/product/neo/). Neo is [grounded in your actual infrastructure](/blog/grounded-ai-why-neo-knows-your-infrastructure/), not internet patterns. The [10 things you can do with Neo](/blog/10-things-you-can-do-with-neo/) post shows what that looks like in practice.

Give it one project. That is all it took for me.

{{< blog/cta-button "Try Pulumi for Free" "/up/" >}}
