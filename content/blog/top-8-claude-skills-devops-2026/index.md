---
title: "The Claude Skills I Actually Use for DevOps"
date: 2026-02-09
draft: false
meta_desc: "Skills teach AI agents how to work like experienced practitioners. In this post, we share several skills that can improve how you build cloud infrastructure."
meta_image: meta.png
authors:
    - engin-diri
tags:
    - ai
    - devops
    - platform-engineering
    - claude-code
    - ai-agents
---

When Claude Code first released [skills](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/skills), I ignored them. They looked like fancy prompts, another feature to add to the pile of things I would get around to learning eventually. Then I watched a few engineers demonstrate what skills actually do, and something clicked. By default, language models do not write good code. They write plausible code based on what they have read. Plausible code turns into bugs, horrible UX, and infrastructure that breaks at 3am.

<!--more-->

Skills fill that gap. They package engineering expertise into something Claude can use. The workflows and judgment matter more than the raw information. Without skills, every conversation starts from zero. You explain the same conventions and correct the same mistakes. Every morning, back to zero.

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

Slash commands were another option, but you had to remember to invoke them. Anthropic apparently agreed, because in January 2026 they [merged slash commands into skills](https://medium.com/@asher-at-plato/why-did-anthropic-merge-slash-commands-into-skills-4bf6464c96ca). One unified system instead of two.

Skills avoid this through progressive disclosure. Claude reads just the description at startup, maybe a hundred tokens. The full procedures only load when Claude decides they are relevant. Unlike those massive system prompts that used to eat through your context window, skills stay out of the way until they are needed. For DevOps engineers running long infrastructure sessions with dozens of resources, this matters. You keep your context budget for the actual work instead of burning it on instructions. Skills can also fork context, spinning up isolated subagents that do work without polluting your main conversation. Think of it like handing a colleague a written brief. They go work on it, hand back a summary, and never sit in on your conversation.

I still use MCPs for connecting Claude to external systems. The [Pulumi MCP server](/blog/mcp-server-ai-assistants/) lets Claude query the registry and validate code. But MCPs give Claude access to things. Skills teach Claude how to think about things. Different jobs. They get more useful when you combine them. One engineer built a financial reporting skill that connects to his Mercury bank account via MCP, pulls every transaction for a given month, classifies the expenses into categories, and generates a styled HTML report with totals and breakdowns. A skill that knows your deployment process connecting to MCPs that talk to your actual infrastructure is the same idea, just pointed at ops instead of accounting.

> [!NOTE]
> Skills are portable. They follow an [open standard](https://agentskills.io), so a skill you write for Claude Code works in Cursor, GitHub Copilot, or anywhere else that supports agent skills. You can even copy the skill content into ChatGPT as a starting prompt. No vendor lock-in.

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

Pulumi maintains its own skills repository at [pulumi/agent-skills](https://github.com/pulumi/agent-skills), which they [announced recently](/blog/pulumi-agent-skills/). The repo includes skills for ComponentResource patterns, Automation API, and migration from Terraform, CDK, CloudFormation, and ARM. The two I use daily are `pulumi-esc` and `pulumi-best-practices`.

The `pulumi-esc` skill teaches Claude how to work with [Pulumi ESC (Environments, Secrets, and Configuration)](/product/esc/). It knows the difference between `pulumi env get`, `pulumi env open`, and `pulumi env run`. It sets up OIDC for dynamic credentials, integrates with external secret stores like AWS Secrets Manager and Vault, and structures layered environment composition so your dev, staging, and production configs inherit from a shared base.

The `pulumi-best-practices` skill catches the mistakes that burn you in production. It stops Claude from creating resources inside `apply()` callbacks, enforces proper parent relationships in ComponentResources, encrypts secrets from day one, and makes sure `pulumi preview` runs before any deployment. These are the patterns that took me years to internalize, and now Claude follows them by default.

| Skill | What it teaches Claude |
|-------|------------------------|
| `pulumi-esc` | Environment, secrets, and configuration management with OIDC, dynamic credentials, and secret store integration |
| `pulumi-best-practices` | Resource dependencies, ComponentResource patterns, secret encryption, and safe refactoring |

```bash
npx skills add https://github.com/pulumi/agent-skills --skill pulumi-esc
npx skills add https://github.com/pulumi/agent-skills --skill pulumi-best-practices
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

The [obra/superpowers](https://github.com/obra/superpowers) repository contains a skill that changed how I debug with Claude. The `systematic-debugging` skill implements a four phase framework: root cause investigation, pattern analysis, hypothesis testing, and implementation.

Without this skill, Claude tends to suggest solutions immediately. Something is broken, here are five things that might fix it. This feels helpful but often wastes time because none of the suggestions address the actual problem.

With the systematic debugging skill, Claude approaches problems differently. It asks clarifying questions. It wants to see logs. It builds a model of what is happening before suggesting changes. When it proposes a fix, it explains why that fix addresses the root cause. Sometimes skills find problems you did not know about. One engineer pointed a skills-equipped Claude at a set of SEO pages and discovered they had been decaying for months with nobody watching. The infrastructure parallel is obvious: configuration drift, unused resources, permissions that expanded over time. A debugging skill that investigates before prescribing will find these things.

| Skill | What it teaches Claude |
|-------|------------------------|
| `systematic-debugging` | Root cause investigation, pattern analysis, hypothesis testing, and verified implementation |

```bash
npx skills add https://github.com/obra/superpowers --skill systematic-debugging
```

## Catching security issues before they ship

Two skills cover different sides of security review. The [wshobson/agents](https://github.com/wshobson/agents) `k8s-security-policies` skill handles Kubernetes-specific hardening: NetworkPolicies, Pod Security Standards, RBAC, OPA Gatekeeper constraints, and service mesh mTLS configuration. The [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) `security-review` skill covers application-level concerns like secrets management, SQL injection, XSS prevention, and input validation.

I asked Claude to check a Pulumi program that created an S3 bucket. Without the security skills, Claude confirmed the code was correct and moved on. With the skills loaded, it flagged that the bucket had no server-side encryption configured, the bucket policy allowed `s3:*` from an overly broad principal, and there was no access logging enabled. On the Kubernetes side, the `k8s-security-policies` skill catches things like missing default-deny NetworkPolicies and containers running as root. These skills are not a replacement for deterministic tools like tfsec, checkov, or trivy. Those catch known issues every time. Skills are probabilistic and work best as an extra layer during development, not as your only security gate.

| Skill | What it teaches Claude |
|-------|------------------------|
| `k8s-security-policies` | Network policies, pod security standards, RBAC, and admission control for defense-in-depth |
| `security-review` | Secrets management, input validation, SQL injection, XSS/CSRF prevention, and dependency auditing |

```bash
npx skills add https://github.com/wshobson/agents --skill k8s-security-policies
npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill security-review
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

## Vetting the skills you install

Before you install everything in sight, a warning. Skills run with the same permissions as your AI agent. A malicious skill can exfiltrate credentials, download backdoors, or disable safety mechanisms, and it will look like your agent doing it.

Snyk researchers published [ToxicSkills](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) in February 2026 after scanning 3,984 skills from public registries. 13.4% had critical-level vulnerabilities, and they found 76 confirmed malicious payloads. The attack techniques included base64-encoded commands that steal AWS credentials, skills that direct you to download password-protected executables from attacker infrastructure, and jailbreak attempts that try to disable safety mechanisms. 91% of malicious skills combine code-level malware with prompt injection, so they attack on two fronts simultaneously.

Treat skills like you treat any third-party dependency:

1. Read the source before installing. Skills are markdown and YAML files. If you cannot read the full skill in a few minutes, that is a red flag.
1. Check the repository. Look at stars, contributors, and commit history. A single-commit repository from an unknown account deserves scrutiny.
1. Run `uvx mcp-scan@latest --skills` to scan installed skills for known malicious patterns, prompt injection, and credential exposure.
1. Be cautious with skills that fetch external content at runtime. The Snyk research found 17.7% of skills on ClawHub pull from third-party URLs, which means the skill's behavior can change after you install it.
1. Stick to known repositories. Every skill recommended in this post comes from a repository with visible maintainers and community activity.

Eight malicious skills were still publicly available on ClawHub when Snyk published their findings. The skills ecosystem is young, and the vetting infrastructure is still catching up.

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
npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill security-review
```

Then try these two prompts to see how many skills activate at once:

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

## Get started

Every skill in this post includes its install command. Pick the section that matches your biggest pain point, run the `npx skills add` command, and try it on your next task. Skills work in Claude Code, Cursor, GitHub Copilot, and anything else that supports the [Agent Skills standard](https://agentskills.io).

The [Pulumi Agent Skills announcement](/blog/pulumi-agent-skills/) has more details, and the [GitHub repository](https://github.com/pulumi/agent-skills) has the source. If you want something that goes further, with organizational context and deployment governance, look at [Pulumi Neo](/product/neo/). Neo is [grounded in your actual infrastructure](/blog/grounded-ai-why-neo-knows-your-infrastructure/), not internet patterns. The [10 things you can do with Neo](/blog/10-things-you-can-do-with-neo/) post shows what that looks like in practice.

Give it one project. That is all it took for me.

{{< blog/cta-button "Try Pulumi for Free" "/docs/get-started/" >}}
