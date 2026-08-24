---
title: "Why AI Agents Write Better Infrastructure in Real Languages than HCL"
allow_long_title: true
date: 2026-08-09
draft: false
meta_desc: "Recent research shows AI agents write infrastructure fine on day one. Day two, changing it, is where HCL falls short and real languages pull ahead."
feature_image: feature.png
authors:
    - joe-duffy
tags:
    - ai
    - ai-agents
    - infrastructure-as-code
    - platform-engineering
    - terraform
    - hcl
category: perspectives
faq_schema: true

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Recent research on AI agents managing cloud infra: Terraform hits 100% success on day-one provisioning, then drops to 33% on updates.

        The gap shows up when infrastructure needs to change, not when it's first written:
    linkedin: |
        A recent academic study out of Michigan, Berkeley, and a16z ("Cloud Infrastructure Management in the Age of AI Agents," arXiv:2506.12270) put four kinds of AI agents through the same cloud tasks: an IaC agent writing Terraform, an SDK agent writing Python, a CLI agent, and a browser agent clicking through a console.

        The IaC agent tied for the best score on first-time provisioning. Then its success rate fell to 33% on updates and 40% on monitoring, with the authors pointing to hallucinated fields and deprecated methods.

        The distinction that matters is Day 1 (write it once, greenfield) versus Day 2 (change it, query it, keep it correct over time). Most real infrastructure work is Day 2. General-purpose languages give an agent leverage that a declarative config file can't: types, tests, refactoring tools, a compiler, and programmatic access to live state.

        We wrote up what the research says, where HCL still wins, and what it means for how you let an agent touch your infrastructure.
    bluesky: |
        Recent research: AI agents hit 100% success writing Terraform for the first time, then their success rate on changing it later falls to 33%.

        The gap is Day 2, not Day 1, and that's a language problem:
---

An AI agent can generate a working Terraform file about as reliably as it can generate a working Python script. The gap shows up afterward: when that file needs to change. A recent academic study found agent success rates on infrastructure updates fall to 33% for Terraform, versus 67% for agents working in a general-purpose language — and on monitoring tasks the gap widens, 40% for Terraform against roughly 80%. Day 1 is close to solved. Day 2, where most real infrastructure work happens, is where language choice decides everything.

Pulumi ships HCL natively today, and Pulumi Cloud now hosts Terraform and OpenTofu state directly. The argument here is for being precise about what each format is good at, and why the agentic era raises the stakes on that choice.

<!--more-->

## What does the research actually say about AI agents and infrastructure code?

In June 2025, researchers from the University of Michigan, UC Berkeley, and Andreessen Horowitz (including Martin Casado) published ["Cloud Infrastructure Management in the Age of AI Agents"](https://arxiv.org/abs/2506.12270) (arXiv:2506.12270). The paper builds a benchmark of realistic cloud tasks — provisioning, making updates, and monitoring — and runs four kinds of agents against them: an SDK agent writing Python, a CLI agent running shell commands, an IaC agent writing Terraform, and a Web agent clicking through a cloud console.

Here's how they scored, as success rate and average steps to complete a task:

| Agent modality | Provisioning | Updates | Monitoring |
|---|---|---|---|
| SDK (Python) | 67% success, 4.5 steps | 67% success, 2.0 steps | 80% success, 1.25 steps |
| CLI (Shell) | 100% success, 1.6 steps | 67% success, 3.0 steps | 80% success, 1.0 steps |
| IaC (Terraform) | 100% success, 2.0 steps | 33% success, 5.0 steps | 40% success, 2.5 steps |
| Web (ClickOps) | 33% success, 46.0 steps | 67% success, 20.0 steps | 100% success, 2.75 steps |

Read that table honestly and the IaC agent isn't the worst performer overall, and it isn't uniformly bad. It ties the CLI agent for the best provisioning score, and needs barely more steps to get there. Where it falls apart is everything after the first apply: a 33% success rate on updates and 40% on monitoring, the two weakest scores in the whole table for those task types. The authors describe what went wrong in their own words: on the monitoring tasks, "the IaC agent was poorly suited for monitoring tasks, with only 40% success rate. We found that this agent encountered numerous bugs in the monitoring tasks, such as hallucination that generated non-IaC languages or invocation of deprecated methods." On updates, "the IaC agent only achieved 33% success rate; we hypothesize that its effectiveness would increase with longer context windows." Meanwhile, "the CLI and SDK agents performed similarly, achieving around 80% success rates within one step on average" on monitoring.

Note the shape of that result. Terraform is fine, even strong, for a one-shot "stand this up" task. It gets meaningfully worse the moment the job becomes "look at what's already there and change it correctly," which is most of what platform and DevOps teams actually spend their time doing.

## Why do LLMs struggle with HCL?

Not because they can't write it. Provisioning shows they can, at 100% in this study. They struggle with HCL specifically on the tasks that require reasoning about state that already exists: reading a live configuration, understanding what changed since it was written, and producing a correct diff.

HashiCorp Configuration Language is a declarative, static format. Its functions are pure and evaluated at plan time, so there is no way to call out and introspect what is actually deployed; there is no compiler to catch a bad reference or a type error before it reaches an API; and testing a change means standing it up against a real provider through Terraform's own harness rather than exercising the code directly the way an agent tests application code. When an agent needs to reason about a plan it didn't write from scratch, and iterate on it, a static config format gives it little to hold onto, which is consistent with the paper's own diagnosis: hallucinated fields, deprecated method calls, and errors that only a longer context window would paper over.

Agents can plainly write configuration files; the reliability problem shows up once that file needs to change. Day 2 infrastructure work is a change-management and reasoning problem, not a generation problem, and a declarative DSL doesn't give an agent the scaffolding that kind of problem needs.

## What makes real languages easier for agents to reason about?

General-purpose languages give an agent the same tools a human engineer relies on to change code safely, and none of them exist in a declarative config format:

- **Types.** A type error is immediate, mechanical feedback an agent can act on before ever calling a cloud API. A malformed HCL block or a hallucinated field often isn't caught until `apply` fails, or worse, doesn't fail and does the wrong thing.
- **Tests.** An agent can write and run a unit test against infrastructure code the same way it tests application code, and check its own change before proposing it. `terraform test` exists, but it checks a configuration by standing it up against a real provider, so the feedback loop is a cloud round-trip rather than something an agent can run on every iteration.
- **Functions and abstraction.** Loops, conditionals, and reusable functions let an agent express "do this for every environment" once, instead of hand-editing N near-duplicate blocks and risking drift between them.
- **Refactoring tooling.** Rename a variable, extract a component, or restructure a module, and an IDE or language server can make the change for you and verify that it compiles. Outside of dependency updates, it might be rare to want to refactor across multiple applications at once, but it [happens all the time with infrastructure](https://thenewstack.io/pulumi-infrastructure-agent-era/).
- **A real package ecosystem.** An agent can pull in a well-tested, versioned component from PyPI or npm instead of re-deriving a pattern from scratch in HCL, where module reuse is comparatively thin.
- **Programmatic access to live state.** Interfaces like Pulumi's [Automation API](/docs/iac/concepts/automation-api/) let an agent query and drive infrastructure the same way it would call any other library, which is exactly the capability the SDK and CLI agents used to hold their edge on updates and monitoring in the study above.

Customers who've moved from copy-pasted declarative blocks to a real language describe the same shift. Mike Corsaro, Senior Software Engineer at Atlassian, [put it plainly](/case-studies/atlassian/): "With the old tool, spinning up our databases meant we had 20 blocks of code and a lot of copy and pasting. With Pulumi, it's Python. It's five lines of code. If you want to add a new database, add one line, and you're good to go." Dinesh Ramamurthy, Engineering Manager at Mercedes-Benz R&D, [framed the same benefit](/case-studies/mercedes-benz/) as engineering practice: "What really stands out in Pulumi is the ability to apply program language constructs and best practices to your cloud infrastructure code." Both are describing exactly the leverage — abstraction, reuse, and standard engineering practice — that also happens to be what an agent needs to change infrastructure reliably.

## Where does HCL still make the most sense?

The paper's own numbers make the fair case: for pure greenfield provisioning, IaC tied for the best result, at 100% success. If the job really is "stand up this exact thing once," a declarative format does that job well, and there's no reason to fight it. That's also why Pulumi supports HCL as a first-class language today, not only Python, TypeScript, Go, C#, and Java. Teams with an existing Terraform or OpenTofu investment can [bring that state directly into Pulumi Cloud](/blog/bring-your-terraform-estate-into-the-agentic-era/), keep writing HCL where it already works, and get Pulumi Cloud's state backend, RBAC, and policy engine underneath it without a rewrite. See [HCL as a Pulumi language](/docs/iac/languages-sdks/hcl/) and [importing Terraform state into Pulumi Cloud](/docs/iac/get-started/terraform/terraform-state-backend/) for how that works in practice. Know what job you're asking an agent to do before you pick the format, since increasingly that job is Day 2, not Day 1.

## Who is responsible when an agent writes bad infrastructure?

Responsibility sits with the platform around the agent, not the agent or the format alone. Weave Intelligence's Luca Galante made this the second of his ["10 Platform Engineering Predictions for 2026"](https://platformengineering.org/blog/10-platform-engineering-predictions-for-2026): "As developers increasingly rely on AI to generate infrastructure code, Terraform configurations, and Kubernetes manifests, platforms must serve as the primary reviewer and auto-remediator." His reasoning is worth quoting directly, because it matches what the arXiv study found in practice: "Non-deterministic code generation introduces risks traditional validation can't catch. An LLM might invent a plausible-looking Kubernetes API field that passes linting but fails in production. It might generate Terraform that omits IAM restrictions, creating security vulnerabilities." Galante is clear this isn't an argument against AI-assisted infrastructure work: "This isn't about blocking AI usage. It's about making AI-assisted development safe at scale. Platforms that solve this become competitive advantages. Those that don't become liability generators."

That's the case for guardrails living at the platform layer rather than trusting any one agent's output: policy as code that reviews a proposed change before it ships regardless of what wrote it, human-in-the-loop approval on anything touching production, and an infrastructure agent like [Pulumi Neo](/product/neo/) that runs previews, checks policy, and opens a pull request for a human to approve, rather than applying changes unsupervised.

## How much infrastructure are agents actually writing today?

More every month, and mostly under approval, not unsupervised. Pulumi's [State of Agentic Infrastructure 2026](/state-of-agentic-infrastructure/) survey of 510 platform, DevOps, and product engineers found that 45% already say agents handle half or more of their infrastructure work, and that share is expected to rise to 52% within six months. GitHub Copilot (62%) and Claude Code (56%) lead the tools teams use to do it. Notably, 81% of respondents let agents change production infrastructure at all, but almost all is gated: 62% require approval, versus only 19% who allow it autonomously. That approval-gated pattern is exactly what you'd expect if teams have already internalized the Day 1 vs. Day 2 distinction, even without seeing this research: agents propose, humans confirm before it hits anything real. Separately, [more than 40% of Pulumi's own users now manage infrastructure using AI agents](/blog/bring-your-terraform-estate-into-the-agentic-era/), a different measure (share of users, not share of deployments) but pointed in the same direction.

## Frequently asked questions

### Does this mean Terraform is bad at writing infrastructure code?

No. In the arXiv study, the Terraform-writing agent tied for the best score on first-time provisioning, at 100% success in two steps on average. It's the tasks that come after the first `apply` — updates and monitoring — where its success rate dropped sharply, to 33% and 40% respectively.

### Why do agents do worse at changing infrastructure than writing it the first time?

Changing existing infrastructure requires reasoning about state that already exists, not only generating a correct file from a blank page. General-purpose languages give an agent tools built for exactly that: types that catch mistakes immediately, tests it can run against its own change, and programmatic access to query what's actually deployed. A declarative config format offers none of those, so an agent has less to check its work against.

### Does Pulumi support HCL?

Yes. HCL is a first-class Pulumi language alongside Python, TypeScript, Go, C#, and Java, and Pulumi Cloud can host Terraform and OpenTofu state directly, so teams with an existing HCL investment don't have to rewrite it to get Pulumi Cloud's state backend, policy engine, and governance.

### What should a team do differently because of this research?

Match the format to the job. Use HCL (in Pulumi or elsewhere) for genuinely one-shot, greenfield provisioning where its declarative simplicity is a strength. For anything that will be updated, refactored, or queried over its life, which is most production infrastructure, choose a general-purpose language so both your human engineers and any agents helping them have types, tests, and refactoring tools to work with. Either way, put policy-as-code review and human approval between any agent and production, since the research shows exactly where unsupervised agents are most likely to make mistakes.

Ready to see the difference in practice? [Get started with Pulumi](/docs/get-started/) in the language your team already uses, or read how [Pulumi Neo](/product/neo/) keeps a human in the loop as agents take on more of the day-to-day infrastructure work.
