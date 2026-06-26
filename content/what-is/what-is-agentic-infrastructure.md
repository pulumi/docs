---
title: What Is Agentic Infrastructure?
meta_desc: "Agentic infrastructure is cloud infrastructure that AI agents provision, govern, and operate through code. Learn what it is, how it works, and how to build it."
type: what-is
page_title: "What Is Agentic Infrastructure?"
authors: ["alex-leventer"]
---

**Agentic infrastructure is cloud infrastructure that AI agents provision, govern, and operate autonomously, writing code, running deployments, enforcing policy, and proposing changes through pull requests, with humans reviewing and approving rather than executing every step.**

This is one of the more significant shifts happening in how engineering teams work right now. The mental model most of us carry (an engineer at a terminal, running `pulumi up` or clicking through a cloud console) is giving way to something different: a goal stated in natural language, an agent that reasons over your actual infrastructure state, writes code, previews the impact, checks it against policy, and opens a PR for review.

## What does "agentic infrastructure" actually mean?

The word "agentic" refers to an AI system that takes sequences of actions to reach a goal, observing state, making decisions, and executing steps, rather than generating a single-prompt response.

Applied to infrastructure, it means an AI agent that can receive a goal in natural language, query your actual deployed state to understand the environment, write or modify infrastructure code, preview the impact against your cloud environment, validate the changes against your organization's policies, and open a pull request for human review with a summary of what will change and why. If CI/CD feedback comes back (a failed security scan, a policy violation), the agent reads it, pushes a fix, and iterates.

The human role shifts. Instead of authoring every resource definition and running every deployment, engineers define the goals, review the proposals, and set the policies that constrain what agents can do. The agent handles the execution.

This is meaningfully different from earlier waves of infrastructure automation (scripts, pipelines, runbooks), because those automate procedures that humans already defined. An agentic system can reason about novel situations, generate new code, interpret error messages, and propose solutions that weren't pre-scripted.

Joe Duffy, Pulumi's CEO, described it this way in [The Agentic Infrastructure Era](/blog/the-agentic-infrastructure-era/):

> "Agentic infrastructure is a super exciting one-way door for our industry."

Pulumi is tracking LLMs doing over 20% of infrastructure deployments today, up from nearly zero a year ago, with that share expected to grow past 50% by the end of 2026.

## Why do AI agents and infrastructure as code go together?

The connection between AI agents and infrastructure as code isn't obvious until you think about what agents are actually good at: code.

Frontier models score 86% on SWE-bench Verified today, up from 33% in August 2024. That jump has happened because code is highly "in-distribution": there are billions of lines of production-grade Python, TypeScript, and Go for models to learn from. The public corpus of general-purpose code is deep, diverse, and production-quality in a way that infrastructure DSLs aren't.

This asymmetry is what makes infrastructure the "last mile," the part of shipping software that has historically resisted automation. Andrej Karpathy captured the gap: "The reality of building web apps in 2025 is that it's a bit like assembling IKEA furniture." The code came together fast. Getting it actually running in production (services, API keys, environments, deployments) remained stubbornly human. That gap exists because clickops and bespoke DSLs are out-of-distribution for models trained overwhelmingly on general-purpose code. Put the last mile in code too, and the gap closes.

This is the core insight behind [infrastructure as code](/what-is/what-is-infrastructure-as-code/): by expressing cloud resources in real programming languages, you bring them into the domain agents already know. As Duffy put it:

> "It is a happy accident that the combination of this plus the verifiability of every change is the exact combination that empowers agents to do infrastructure. LLMs are natural coders. By mapping infrastructure space in code space, agents can do what they're great at — code — and the infrastructure as code engine is the link that maps those code edits back down into infrastructure space."

Three things follow from this:

**Agents get richer training signal.** Public Python and TypeScript include genuinely production-scale open source: real patterns at large scale, not tutorial snippets. A model that has learned from millions of Python programs brings that experience to bear when writing infrastructure code in Python. Infrastructure DSL corpora are much thinner, and skew toward documentation examples rather than production usage.

**Agents can use real software engineering primitives.** Loops, functions, classes, package imports, unit tests, type checking, IDE tooling: these apply to Pulumi programs the same way they apply to application code. An agent writing a Pulumi program can import a library, write a test, refactor a module, or inherit from a base class. It's not limited to what a configuration language can express.

**Every change is verifiable.** `pulumi preview` maps code changes to a concrete, auditable list of resource operations (what will be created, updated, or deleted) before anything in the cloud changes. An agent can verify its own output. That feedback loop (write, preview, validate, adjust) is what makes autonomous infrastructure tractable at scale. As Duffy notes: "Just as we wouldn't vibe code without git showing us the source changes, we shouldn't vibe infrastructure without a tool that shows what it will do before it does it, and what it has already done in the past." It's essentially `git diff` for your cloud.

Research bears this out. The CodeAct paper (Wang et al., ICML 2024) measured 17 models across a range of tasks and found that agents consistently perform better when they act by writing executable code rather than emitting JSON or config. Code gives agents a richer action space, tighter feedback loops, and a substrate they've been trained on at scale.

## What does an AI infrastructure agent actually do?

[Pulumi Neo](/product/neo/) is an AI infrastructure engineering agent built into Pulumi Cloud. A concrete workflow illustrates how agentic infrastructure actually operates.

**Example task:** *"Update all our Lambda functions from Node.js 16 to Node.js 20."*

1. **State the intent.** A user sends the goal in natural language, whether through Pulumi Cloud, the CLI, or the Slack integration. Neo creates a task to track the work.

1. **Investigate and plan.** In Plan Mode, Neo queries your actual Pulumi state graph. It identifies every Lambda function running Node 16, checks dependencies, and synthesizes a plan grounded in your real environment, not in hypothetical configurations. The plan is presented for human review before anything changes.

1. **Execute with configured controls.** Depending on your task mode (Review for step-by-step human approval, Balanced for approval before `pulumi up`, or Auto for trusted, fully automated workflows), Neo proceeds within the RBAC entitlements of the user who initiated the task. It cannot do anything the user themselves could not do.

1. **Run `pulumi preview`.** Neo validates the generated code, shows exactly which resources will be created, updated, or deleted, and runs your Pulumi Policies. No resources change until this step completes cleanly.

1. **Open a pull request.** Neo creates a PR with a problem description, a list of modified resources, and the preview summary. The PR flows through your existing GitHub, GitLab, or Bitbucket CI/CD pipeline.

1. **Handle CI/CD feedback.** If a pipeline check fails (a security scan, a policy violation, a test), Neo reads the output, pushes a corrective fix to the same PR, and iterates.

1. **Schedule automations.** Any task can become a recurring job. Neo opens a PR whenever a scheduled run detects infrastructure drift or produces changes, so environments stay current without manual polling.

What makes this different from a generic coding assistant is that Neo is [grounded AI](/blog/grounded-ai-why-neo-knows-your-infrastructure/): it reasons over your actual state graph and deployment history rather than generating code from internet patterns. See the [Neo documentation](/docs/ai/) for a full reference.

## What about infrastructure for AI agents?

The phrase "agentic infrastructure" is also used to describe a second thing: the compute, networking, and data infrastructure that AI agents themselves run on. GPU clusters, inference endpoints, vector databases, and RAG pipelines: the platform underneath AI workloads.

These two meanings are related but distinct:

| | Infrastructure *managed by* AI agents | Infrastructure *for* AI agents |
|---|---|---|
| **What it is** | AI takes on the operational workload of your cloud | The cloud platform your AI workloads run on |
| **Example** | Neo provisions and updates your AWS environment | A GPU cluster running a training job or inference service |
| **Who manages it** | The AI agent, with human review | Your platform team, often using IaC |

Most organizations will need to think about both. Teams building AI products need the platform layer (infrastructure *for* agents). Those same teams also benefit from AI agents operating that platform (infrastructure *managed by* agents). The two compound: agents that understand infrastructure can also manage the infrastructure their own workloads run on.

## How do you govern and secure agentic infrastructure?

The governance question comes up immediately, and it deserves a direct answer. Giving an AI agent write access to a production environment is only sensible if the controls are in place first.

Duffy frames it plainly:

> "The smartest agent in the world still needs guardrails, audit trails, and policy enforcement to be trusted with production systems at scale, and that layer gets more valuable as agents get more capable, not less."

The layers Pulumi provides:

**Policy as code.** [Pulumi Policies](/docs/iac/crossguard/) lets teams define organizational rules as code (no unencrypted storage, required tags, allowed instance types) that run on every `pulumi preview`. Non-compliant changes are blocked before they reach the cloud. Because Pulumi Policies run on the preview output, they apply whether a human or an agent proposed the change.

**RBAC and entitlements.** Neo operates within the Pulumi Cloud RBAC entitlements of the user who initiated the task. It cannot escalate privilege. If a developer cannot delete a production database, Neo cannot either, regardless of what the task requests.

**Configurable human-in-the-loop.** Review mode, the default, requires human approval at every step. Balanced mode gates specifically on `pulumi up`, and Auto mode runs completely unattended for workflows where the team has already established confidence. Teams can set a different mode per environment.

**Audit trails.** Every agent action (every preview, every deployment, every PR) is logged with timestamps, the initiating user, and the full resource diff. This is the same audit trail that applies to human-initiated changes.

**Secrets via Pulumi ESC.** Agents reference secrets through [Pulumi ESC](/docs/esc/) without ever handling raw values. Credentials are rotated, scoped, and auditable.

The practical result is that agentic changes go through the same review pipeline as human changes, pull requests, CI/CD checks, and policy validation, with an additional layer of structured logging that human-driven console operations often lack.

## Who is already using agentic infrastructure?

Usage at scale is already happening. A few examples:

**Wiz** manages over 1 million cloud resources, handling hundreds of thousands of infrastructure updates daily with Pulumi. At that volume, manual execution of every infrastructure change is impractical. Automation, increasingly agentic, is how the team keeps pace with growth.

**BMW** manages 20,000+ cloud resources with Python-based IaC. The combination of real programming languages and policy-as-code governance is what makes that scale tractable for a platform team.

**Werner Enterprises** reduced infrastructure provisioning time from 3 days to 4 hours after adopting Pulumi Neo for provisioning workflows.

**Mysten Labs** described their goal as "minimizing the time it takes an engineer to go from an idea to an experiment in production." That reduction in execution overhead is what agentic tooling makes possible.

The pattern across these teams is consistent: engineering headcount has not shrunk, but the mix of work has changed. Architecture, policy design, and reviewing agent proposals have replaced the mechanical execution that once dominated the workday.

## How do you get started with agentic infrastructure?

The entry point is [Pulumi Neo](/product/neo/), which is built into Pulumi Cloud.

**Step 1: Start with Pulumi IaC.** Neo works with Pulumi programs. If your team is already using Pulumi, Neo can start operating your existing stacks immediately. If you are migrating from another tool, Pulumi provides [conversion documentation](/docs/iac/comparisons/terraform/) for common starting points.

**Step 2: Activate Neo.** Navigate to the [Neo documentation](/docs/ai/) for activation steps. You can start with a single project or stack before expanding.

**Step 3: Start in Review mode.** Neo's default task mode requires human approval at every step. This is the right starting point: you learn how Neo reasons, build trust in its outputs, and establish your policy baseline before giving it more autonomy.

**Step 4: Define your policies.** Encode your team's standards in [Pulumi Policies](/docs/iac/crossguard/) before expanding Neo's autonomy. Policies run on every preview and block non-compliant changes automatically.

**Step 5: Connect your CI/CD pipeline.** Neo opens pull requests that flow through your existing GitHub, GitLab, or Bitbucket workflows. No changes to your pipeline are required.

**Step 6: Expand to more environments.** Once the pattern is working on lower-risk environments, extend it. The governance controls (policies, RBAC, and audit logs) scale with the scope.

## Frequently asked questions

### What is agentic infrastructure?

Agentic infrastructure is cloud infrastructure that AI agents provision, govern, and operate. Instead of engineers typing every command, an AI agent receives a natural-language goal, reasons over the actual infrastructure state, writes infrastructure code, previews the impact, enforces policy, and opens a pull request for human review. The human role shifts from executor to approver and architect.

### How is agentic infrastructure different from DevOps automation?

Traditional DevOps automation executes predefined procedures: scripts, pipelines, runbooks. Agentic infrastructure uses AI agents that can reason about novel situations, generate new code, interpret error messages, and propose fixes, without a human pre-writing each procedure. Generative automation, not scripted automation.

### What programming languages do AI infrastructure agents use?

[Pulumi Neo](/product/neo/) writes and modifies infrastructure in Python, TypeScript, Go, C#, Java, and YAML. Using general-purpose languages means AI agents draw on richer training data and can apply full software engineering patterns (loops, functions, tests, package imports) to infrastructure code.

### Is agentic infrastructure safe for production environments?

Yes, when the governance layer is in place first. Pulumi Neo runs `pulumi preview` before every deployment, enforces Pulumi Policies on every change, operates within the initiating user's RBAC entitlements, logs every action with full audit trails, and defaults to requiring human approval at each step. The governance controls become more valuable, not less, as agents take on more work.

### What is Pulumi Neo?

[Pulumi Neo](/product/neo/) is an AI infrastructure engineering agent built into Pulumi Cloud. It accepts natural-language tasks, reasons over your actual infrastructure state graph, writes and modifies infrastructure code, runs previews, enforces policies, and opens pull requests across Amazon Web Services (AWS), Azure, Google Cloud, and hundreds of other providers, with configurable human-in-the-loop controls.

### What is the difference between infrastructure for AI agents and infrastructure managed by AI agents?

Infrastructure *for* AI agents is the compute, networking, and data platform that AI workloads run on: GPU clusters, vector databases, and inference endpoints. Infrastructure *managed by* AI agents means AI is operating your cloud environment, handling provisioning and updates. Both are real needs, and the same IaC platform and governance model applies to both.

### Which cloud providers does agentic infrastructure work with?

Pulumi Neo supports Amazon Web Services (AWS), Microsoft Azure, Google Cloud, Kubernetes, and hundreds of other providers, matching the full scope of the Pulumi IaC platform.

### What if my team uses a different IaC tool today?

Pulumi provides [migration documentation](/docs/iac/comparisons/terraform/) for teams moving from HashiCorp Terraform and other tools. Once infrastructure is expressed in a Pulumi program, Neo can begin operating it.

### Does agentic infrastructure replace infrastructure engineers?

No. It changes what infrastructure engineers spend time on: less mechanical execution, more architecture, policy design, and reviewing agent proposals. The teams doing this at scale today have not reduced their infrastructure teams; they have changed how those teams operate.

### How does Neo know what is actually deployed?

Neo queries your Pulumi state graph, resource relationships, and deployment history. It does not generate code from generic internet patterns; it reasons from your actual environment. This is what [grounded AI](/blog/grounded-ai-why-neo-knows-your-infrastructure/) means in practice: the agent's plans are based on your real infrastructure, not hypothetical configurations.

## Learn more

Joe Duffy's CascadiaJS 2026 keynote, "The Last Mile Is Code," covers the in-distribution argument and the CodeAct research in depth, with a live demo of Neo deploying a full application to AWS.

{{< youtube "SOMEfFNPsew?rel=0" >}}

[The Agentic Infrastructure Era](/blog/the-agentic-infrastructure-era/) is Duffy's companion essay on where infrastructure is headed. [Grounded AI: Why Neo Knows Your Infrastructure](/blog/grounded-ai-why-neo-knows-your-infrastructure/) explains the context lake approach that makes Neo reliable for production. The [Pulumi Neo product page](/product/neo/) covers capabilities and sign-up, and [10 things you can do with Neo](/blog/10-things-you-can-do-with-neo/) walks through concrete examples. For governance specifics, the [Pulumi Policies](/docs/iac/crossguard/) docs and the full [Neo documentation](/docs/ai/) are the authoritative references.
