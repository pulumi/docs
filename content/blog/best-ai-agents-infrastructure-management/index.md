---
title: "Best AI Agents for Infrastructure, DevOps, and SRE in 2026"
date: 2026-11-10
draft: false
meta_desc: "AI agents for DevOps, infrastructure, and SRE sorted into ChatOps, incident, change, and code agents, with a fair look at Pulumi Neo and its peers."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - ai
    - infrastructure-as-code
    - platform-engineering
    - devops
    - kubernetes
category: general
faq_schema: true
howto_schema: true
itemlist_name: "AI Agents for Infrastructure, DevOps, and SRE"
itemlist:
    - name: "Pulumi Neo"
      url: "https://www.pulumi.com/product/neo/"
    - name: "env zero Agent CLI"
      url: "https://www.envzero.com/"
    - name: "Spacelift Intelligence"
      url: "https://spacelift.io/"
    - name: "Upbound and Crossplane control planes"
      url: "https://upbound.io/"
    - name: "Azure SRE Agent"
    - name: "AWS DevOps Agent"
    - name: "Datadog Bits Investigation"
    - name: "HolmesGPT"
    - name: "Botkube"
    - name: "Traversal"
    - name: "Cleric"
    - name: "Gemini Cloud Assist"
    - name: "HashiCorp Terraform and Vault MCP servers"

# Social media copy - auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        "AI agents for DevOps" now covers at least five different jobs: ChatOps, incident response, IaC-native change, code generation, and access layers.

        We sorted the field and built a 6-criterion rubric for evaluating any of them.
    linkedin: |
        Every DevOps and platform vendor now ships an "AI agent." Few of them do the same job.

        Some live in chat and answer questions about your clusters (Botkube). Some investigate incidents after something breaks (AWS DevOps Agent, Datadog Bits Investigation, HolmesGPT, Azure SRE Agent). Some plan and apply infrastructure changes as reviewable code (Pulumi Neo, env zero's Agent CLI, Spacelift Intelligence). Some write code but never see your live state, and some are MCP access layers that let any agent reach your infrastructure safely.

        The questions that decide a pilot are the same for all of them: what does the agent operate on, does it preview before it acts, does policy run in the pipeline or just the prompt, and whose identity is it using?

        We sorted the current field into categories, built a 6-criterion rubric, and gave every vendor a fair, sourced treatment, including where each one is a better fit than Pulumi.
    bluesky: |
        "AI agents for DevOps" covers five different jobs now: ChatOps, incident response, IaC-native change, code generation, and access layers.

        We sorted the field and built a rubric for evaluating any of them.
---

An AI agent for DevOps and infrastructure is software that uses an LLM to read your live cloud, Kubernetes, or observability state, propose or take action, and work inside guardrails a human defines. In 2026 the category splits into five jobs: ChatOps agents that answer questions and run commands from chat, autonomous remediation agents (often called AI SRE agents) that investigate incidents, IaC-native agents that plan and apply infrastructure changes as reviewable code, code-generation agents that write the files, and access layers (MCP servers) that let any agent reach your systems. Knowing which job you are hiring for is what makes a comparison useful, and most roundups skip it.

<!--more-->

## At a glance

| Tool | Category | Operates on | Best for |
|------|----------|-------------|----------|
| [Pulumi Neo](#pulumi-neo) | Change agent | General-purpose code (Python, TypeScript, Go, C#, Java, YAML) | Teams already on Pulumi who want changes to land as reviewable pull requests |
| [env zero Agent CLI](#env-zero-agent-cli) | Change agent | Terraform, OpenTofu, and other engines via one control plane | Governing multiple IaC engines under one policy and approval layer |
| [Spacelift Intelligence](#spacelift-intelligence) | Change agent | Terraform and OpenTofu providers, called directly or via generated code | Teams deep in Spacelift's existing run pipeline and Rego policies |
| [Upbound and Crossplane control planes](#upbound-and-crossplane-control-planes) | Change agent | Crossplane compositions on the Kubernetes API | Organizations standardized on Crossplane for fleet-scale control planes |
| [Azure SRE Agent](#azure-sre-agent) | Incident agent | Azure resource telemetry and logs | Azure-native teams that want automated root-cause analysis |
| [Traversal and Cleric](#traversal-and-cleric) | Incident agent | Alerts, logs, and traces across a heterogeneous stack | Cloud-agnostic on-call teams drowning in alert volume |
| [Gemini Cloud Assist](#gemini-cloud-assist) | Hyperscaler assistant | Google Cloud resources and Terraform configs | Google Cloud shops wanting an assistant inside `gcloud` and the console |
| [HashiCorp Terraform and Vault MCP servers](#hashicorp-terraform-and-vault-mcp-servers) | Access layer | Terraform Registry data and Vault secrets, exposed to any MCP client | Teams standardizing agent access to infrastructure context and secrets |

## What is an AI agent for infrastructure?

The defining trait is a loop: the agent reads real state (not just a prompt), proposes or takes an action, and that action is checked against policy and human judgment before or immediately after it lands. That loop is what separates an infrastructure agent from two adjacent categories it gets confused with constantly.

A **general-purpose coding assistant** (GitHub Copilot, Cursor, Claude Code) can write infrastructure code, but it has no built-in connection to your live cloud state, your policy engine, or your approval workflow. Without that connection it generates text, and it happens to be good at YAML and HCL.

An **MCP server** (Model Context Protocol server) works as a data and action interface: a standardized way for any agent to query a system's context (a Terraform Registry, a Vault instance, a cloud provider) and, in some implementations, take bounded actions. MCP servers are what make agents useful against real infrastructure, but the server itself does no reasoning. HashiCorp's Terraform and Vault MCP servers and the Pulumi MCP server are access layers other agents plug into, covered below.

## A rubric for evaluating an AI infrastructure agent

Six questions cut through vendor marketing faster than any feature list.

| Criterion | What to ask |
|-----------|-------------|
| 1. What it operates on | Does it write general-purpose code you can test and version, a provider-specific DSL, direct provider API calls, or Kubernetes custom resources? |
| 2. Preview before action | Does it show you a diff or plan before anything changes, the way `pulumi preview` or `terraform plan` does? |
| 3. Where policy runs | Does policy-as-code enforce in the pipeline regardless of what the agent intends, or does it rely on the agent's prompt to behave? |
| 4. Identity and approval | Does the agent inherit the requesting user's own permissions, or does it hold separate, standing credentials? Who approves, and at what step? |
| 5. Where the work lands | Does the change land as code you own and can diff, review, and roll back, or as state that lives only inside the tool? |
| 6. Reach | How many clouds, IaC engines, and languages does it actually cover today, not on a roadmap? |

Criterion 3 is worth dwelling on, because it is where most "AI governance" claims fall apart. As Pulumi has argued in its own writing on [agent sprawl](/blog/agent-sprawl-iac-platform-is-the-answer/), "an agent running through Pulumi hits those gates whether it 'wants' to or not, because the gates live in the pipeline and not in the prompt." A policy that depends on the agent choosing to respect it works as a suggestion.

## What kinds of AI agents exist for DevOps, infrastructure, and SRE?

There are five kinds, and each answers a different question. The hyperscaler assistants from Google Cloud and Microsoft usually fit inside the first two rows, embedded in a console or CLI.

| Kind | Job | Trigger | Preview before action | Where the work lands | Examples |
|------|-----|---------|-----------------------|----------------------|----------|
| ChatOps agents | Answer questions and run bounded commands from Slack or Teams | A person's message or an alert in chat | Varies by tool | A chat thread | Botkube, Gemini Cloud Assist |
| Autonomous remediation (AI SRE) agents | Investigate incidents, find root cause, suggest or take mitigation | An alert or an outage | Mostly diagnostic | Incident findings and tickets | AWS DevOps Agent, Datadog Bits Investigation, HolmesGPT, Azure SRE Agent, Traversal, Cleric |
| IaC-native agents | Plan and apply infrastructure changes | A request, a schedule, or detected drift | Yes, a plan or preview | Code and a pull request | Pulumi Neo, env zero Agent CLI, Spacelift Intelligence, Upbound |
| Code-generation agents | Write and edit infrastructure code | A developer's prompt | Only what you wire up yourself | Files in your editor or repo | Claude Code, GitHub Copilot, Cursor |
| Access layers | Expose infrastructure context and actions to any agent | A tool call from an external agent | Plan-only modes in some servers | Whatever the calling agent proposes | HashiCorp Terraform and Vault MCP servers, Pulumi MCP server |

## Which AI agent fits DevOps, SRE, and platform engineering teams?

Match the agent to the role's daily job:

- **DevOps engineers** who own pipelines and environments get the most from IaC-native agents and code-generation agents, because the output is code they already review.
- **SRE teams** carrying a pager get the most from autonomous remediation agents, which shorten the path from alert to root cause.
- **Platform engineering teams** building an internal developer platform usually want an agent layer over their golden paths: policy gates, scoped identities, and reusable components that every agent, from any vendor, has to pass through. That favors IaC-native agents and access layers, since both plug into the controls a platform team already runs.

## What makes an AI agent IaC-native?

### Pulumi Neo

[Pulumi Neo](https://www.pulumi.com/docs/ai/neo/) is Pulumi's own infrastructure agent, powered by Anthropic's Claude models accessed via Amazon Bedrock. It reads your live stack state to answer questions, and when it proposes a change, [it hands that back as a pull request](https://www.pulumi.com/blog/pulumi-neo/) describing the problem, the resources affected, and a preview summary, rather than applying anything silently. Every proposal runs through `pulumi preview` first, surfacing policy violations and diffs before a human approves.

Neo operates within the requesting user's own RBAC entitlements: "Neo never has more access than you do, only less," in Pulumi's words, which rules out the privilege-escalation risk that worries security teams about agentic tooling generally. It also [migrates existing Terraform, CDK, CloudFormation, and ARM resources](https://www.pulumi.com/blog/neo-migration/) into Pulumi incrementally, and runs scheduled work like provider-freshness checks and encryption or backup audits.

An IaC-native agent works through your infrastructure as code, so every change arrives as a diff you can review, test, and roll back. Neo is Pulumi's version of that idea, and you can see the full capability set on the [Pulumi Neo product page](/product/neo/).

Neo is included by default across Pulumi Cloud editions and metered by usage. Two capabilities are edition-gated: Slack integration requires the Team edition or higher, and scheduled tasks require the Enterprise edition or higher (see [Pulumi's pricing page](https://www.pulumi.com/pricing/) for current token rates and edition details). Neo's [code review feature](https://www.pulumi.com/blog/neo-code-reviews/) is free during its public preview.

**Best for:** teams already writing infrastructure in Python, TypeScript, Go, C#, or Java who want proposed changes to land as ordinary, reviewable pull requests rather than disappear into a separate tool's state.

**Where it isn't the best fit:** if your team has no Pulumi footprint and isn't planning one, evaluate it alongside the multi-engine options below rather than assuming it is the default choice.

### env zero Agent CLI

[env zero](https://www.envzero.com/) (formerly env0) shipped its [Agent CLI](https://www.envzero.com/blog/announcing-the-env-zero-agentic-experience-point-your-coding-agent-at-your-infrastructure) on August 18, 2026, as part of what it calls its Agentic Experience. It is a single-binary CLI that any coding agent, including Claude Code, Cursor, Codex, and Copilot, can point at real environment, deployment, and drift state and query in plain English, then act on through the same roles and approvals a human user would use. Output is structured JSON on stdout with stable exit codes, which is what makes it usable as a tool call from another agent rather than a human-facing chat interface.

The genuine strength here is breadth of governance: env zero has long supported multiple IaC engines (Terraform, OpenTofu, and others) under one control plane with a mature cost and policy substrate, which predates its AI push. Approval gates still pause changes for a human, and every action is recorded against the identity that ran it.

**Best for:** organizations running more than one IaC engine that want one governance and approval layer over all of them, rather than migrating everything to a single tool first.

**Where it isn't the best fit:** if you're single-engine and single-cloud, a narrower tool may be simpler to operate day to day.

### Spacelift Intelligence

Spacelift's agentic capability shipped in two stages. [Intent](https://spacelift.io/blog/announcing-spacelift-intent) launched in October 2025 and takes natural-language infrastructure requests, then calls the underlying cloud provider APIs directly through Terraform and OpenTofu providers, without generating HCL as an intermediate step. Resources created through Intent can still be exported to standard Terraform or OpenTofu code afterward. In March 2026, Spacelift launched [Spacelift Intelligence](https://spacelift.io/blog/introducing-spacelift-intelligence), with Intent continuing on as one of its components alongside a new in-UI Infra Assistant that answers questions, summarizes failed runs, and manages resources conversationally in what Spacelift calls Build mode.

Because Intelligence is delivered over MCP inside Spacelift's own infrastructure, it inherits whatever policies, state, and workers your existing Spacelift setup already has, meaning your Rego-based policy checks and approval flows still apply to anything the assistant proposes. Pricing is metered: the free plan includes a $10 AI token budget per 30-day period, paid plans get unlimited usage, and Intent's own natural-language requests draw on your own AI client rather than this budget (see [Spacelift's Intelligence docs](https://docs.spacelift.io/concepts/intelligence)).

**Best for:** teams already running GitOps-native Terraform or OpenTofu pipelines through Spacelift who want a conversational layer on top of a governance model they already trust.

**Where it isn't the best fit:** shops outside the Terraform and OpenTofu ecosystem, or without an existing Spacelift deployment, won't get the inherited-policy benefit that makes this compelling.

### Upbound and Crossplane control planes

Upbound, the company behind the open-source [Crossplane](https://www.crossplane.io/) project, brings AI into its control-plane model rather than into a chat interface. Its [Intelligent Control Planes guide](https://docs.upbound.io/guides/intelligent-control-planes) describes LLM-enabled composition functions, leveraging Claude, that provide AI-powered status transformers and contextual error analysis inside a Crossplane composition, with automated remediation suggestions when something fails. These functions run alongside [Upbound Platform v3](https://upbound.io/blog/announcing-upbound-v3-one-view-api-and-governance-model-for-every-control-plane-you-run), Upbound's single view, API, and governance model for every control plane an organization runs. As of this writing, Upbound's own documentation describes hosted SaaS availability for these capabilities as forthcoming, so confirm current availability directly with Upbound before planning around it.

The strength worth taking seriously here is that Upbound builds on [Crossplane](https://www.crossplane.io/), which pioneered Kubernetes-native, declarative, multi-control-plane governance at fleet scale years before AI entered the picture, and now runs in production at organizations including Apple, Nike, and JPMorgan Chase. That is a different and in some ways more mature governance model than a conversational agent bolted onto an existing tool.

**Best for:** organizations already standardized on Crossplane and Kubernetes as their control-plane substrate.

**Where it isn't the best fit:** teams without Kubernetes expertise will find the underlying model, Crossplane custom resources on the Kubernetes API, a steep prerequisite regardless of the AI layer on top.

## What do autonomous remediation (AI SRE) agents do?

Change agents plan and apply infrastructure. A separate, growing category responds after something has already broken: it reads alerts, logs, traces, and recent changes, forms hypotheses, and reports a likely root cause with suggested mitigation steps. Most of these agents are diagnostic first, so evaluate how much action they are allowed to take.

### AWS DevOps Agent

[AWS DevOps Agent](https://aws.amazon.com/devops-agent/) is Amazon's frontier agent for operations. AWS describes it as autonomously triaging incidents around the clock, providing root cause analysis and mitigation steps, and routing findings through Slack, ServiceNow, and PagerDuty. It also connects to Dynatrace, Datadog, New Relic, Splunk, GitHub, and GitLab, and AWS positions it across AWS, multicloud, and on-prem environments. AWS has since added release-management capabilities that assess code changes before production, which AWS lists as a preview.

**Best for:** AWS-centered teams that want incident triage tied to the observability and ticketing tools they already run.

### Datadog Bits Investigation

Datadog's [Bits Investigation](https://docs.datadoghq.com/bits_ai/bits_ai_sre/) (launched as Bits AI SRE and since renamed) is described in Datadog's documentation as an autonomous agent that forms hypotheses, gathers telemetry, and uses data-based reasoning to help on-call engineers pinpoint root causes.

**Best for:** teams already running Datadog for observability that want the investigation to start where the telemetry already lives.

### HolmesGPT

[HolmesGPT](https://github.com/HolmesGPT/holmesgpt) is an open source SRE agent that is a CNCF Sandbox project under the Apache 2.0 license. Its README states that it has read-only access by design and respects RBAC permissions, which makes it a low-risk first experiment for Kubernetes troubleshooting.

**Best for:** platform teams that want an open source, read-only investigator they can inspect and self-host.



### Azure SRE Agent

[Azure SRE Agent](https://azure.microsoft.com/en-us/products/sre-agent) reached [general availability in March 2026](https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-general-availability-for-the-azure-sre-agent/4500682) after a preview period with Microsoft's own teams and early customers. It performs automated root-cause analysis and assists with incident response against Azure resources, reading telemetry and logs to narrow down what changed and why, rather than proposing infrastructure changes proactively the way a change agent does.

**Best for:** Azure-native teams that want automated triage without adopting a separate, multi-cloud incident tool.

### Traversal and Cleric

[Traversal](https://www.traversal.com/) is an AI-SRE platform that triages alerts and works to identify root cause across a heterogeneous stack at scale. [Cleric](https://cleric.ai/) takes a similar job but emphasizes building a persistent knowledge graph from an organization's tribal operational knowledge over time, so its investigations improve the longer it runs. Both are venture-funded startups rather than incumbents, so evaluate them with the diligence you'd apply to any early-stage vendor holding production access.

**Best for:** cloud-agnostic, on-call-heavy teams evaluating a dedicated incident-response layer independent of any single cloud provider.

## What are ChatOps agents for AWS and Kubernetes?

ChatOps agents live where the team already talks. They answer questions about a cluster or account in plain language, surface alerts with context, and in some products run bounded commands from the chat thread. The work stays in the conversation unless something else turns it into code.

### Botkube

[Botkube](https://botkube.io/) delivers Kubernetes alerts to chat platforms and adds an AI assistant that, per its site, uses your tools and documentation to find root causes, explain issues in natural language, and generate commands for complex problems. It is aimed at letting developers troubleshoot without CLI access or a ticket to the DevOps team.

**Best for:** Kubernetes teams that want incident context and first-pass troubleshooting inside Slack or Teams.

### Hyperscaler assistants

Cloud providers embed similar assistants in their own consoles and CLIs, which makes them the lowest-friction option for single-cloud shops.

### Gemini Cloud Assist

Google unveiled a more proactive [Gemini Cloud Assist](https://cloud.google.com/blog/products/application-development/gemini-cloud-assist-at-next26) at Cloud Next '26, positioned as AI-assisted cloud operations working across `gcloud`, the console, and Terraform configurations. As announced, this is a forward-looking product direction rather than a broadly available, generally released capability, so verify current rollout status against Google's own release notes before depending on specific functionality.

**Best for:** Google Cloud-committed teams who want an assistant integrated into tools they already use daily.

## Access layers that let any agent touch infrastructure

Not every entry in this category is itself an agent. Some are the plumbing that makes any agent, including a generic coding assistant, safe to point at real infrastructure.

### HashiCorp Terraform and Vault MCP servers

HashiCorp's approach in 2026 has been to build governed access for other agents rather than ship its own autonomous change agent. The [Terraform MCP server](https://developer.hashicorp.com/terraform/mcp-server) gives any MCP-compatible agent real-time access to Terraform Registry documentation, modules, and Sentinel policies, so generated HCL reflects current provider schemas instead of a model's training-data snapshot; it can also create and, with approval, apply a plan, and supports a plan-only mode for teams that want proposals without execution access.

Alongside it, HashiCorp added [native AI agent support in Vault](https://www.hashicorp.com/en/blog/announcing-native-ai-agent-support-in-hashicorp-vault) in May 2026, framed as agentic identity and access management: trusted identities for agents, delegated authorization, and fine-grained access through an Agent Registry, available on Vault Enterprise. A companion [Vault MCP server](https://developer.hashicorp.com/vault/docs/ai/mcp-server/overview) exposes secrets and policy context the same way. This is a credible, enterprise-security-first answer to a question most agentic-infrastructure vendors haven't addressed yet: whose credentials is the agent actually using, and who is accountable for its actions in an audit?

**Best for:** organizations that already run Terraform and Vault and want to extend agent access to both without giving any agent standing, unscoped credentials.

**Where it isn't the best fit:** if you're looking for an agent that plans and applies changes on its own initiative, the server supplies infrastructure for other agents to build on and leaves the change-making to them.

### General-purpose coding agents

Claude Code, Cursor, GitHub Copilot, and similar tools can write and edit infrastructure code competently, and when paired with an MCP server like the ones above, they gain live context and bounded actions against real infrastructure. On their own, without that pairing, they have no visibility into your actual cloud state and no built-in policy enforcement, which is the gap every tool in this article is built to close.

## Full comparison table

| Tool | Operates on | Preview before action | Policy in pipeline | Identity model | Where work lands |
|------|-------------|------------------------|---------------------|-----------------|-------------------|
| Pulumi Neo | General-purpose code | Yes, `pulumi preview` | Yes, Policy as Code | Inherits requesting user's RBAC | Pull request you review and merge |
| env zero Agent CLI | Terraform, OpenTofu, and other engines | Through existing plan/apply flow | Yes, existing policy engine | Existing roles and approvals | Managed environment state |
| Spacelift Intelligence | Terraform, OpenTofu | Yes, existing run pipeline | Yes, Rego-based policies | Existing Spacelift approvals | Spacelift-managed state, exportable to code |
| Upbound / Crossplane | Crossplane compositions | Composition-level, tool-dependent | Kubernetes RBAC and policy tooling | Kubernetes service accounts | Crossplane-managed control plane |
| Azure SRE Agent | Azure telemetry and logs | N/A (diagnostic, not change) | N/A | Azure RBAC | Incident findings, not infrastructure changes |
| Traversal / Cleric | Alerts, logs, traces | N/A (diagnostic, not change) | N/A | Vendor-managed integration | Incident findings, not infrastructure changes |
| Gemini Cloud Assist | GCP resources, Terraform | Preview-stage feature | Unspecified as announced | Google Cloud IAM | Console and CLI guidance |
| AWS DevOps Agent | Alerts, telemetry, code changes across AWS and other clouds | Diagnostic, with mitigation steps suggested | Not described by AWS | AWS integrations and roles | Findings and mitigation steps routed to Slack, ServiceNow, PagerDuty |
| Datadog Bits Investigation | Datadog telemetry | Diagnostic | N/A | Datadog access controls | Investigation findings |
| HolmesGPT | Kubernetes and observability data | Read-only by design | N/A | Respects RBAC | Root-cause answers in chat or CLI |
| Botkube | Kubernetes clusters and chat | Suggests commands for review | Depends on configuration | Chat and cluster permissions | A chat thread |
| Terraform / Vault MCP servers | Terraform Registry data, Vault secrets | Plan-only mode available | Existing Sentinel/OPA and Vault policy | Delegated, agent-scoped identities | Whatever the calling agent proposes |

## How to evaluate an infrastructure agent in two weeks

1. **Name the job first.** Decide whether you need a ChatOps agent, an incident (AI SRE) agent, an IaC-native change agent, a code-generation agent, or an access layer before looking at any vendor. Most disappointing pilots start from "we need an AI agent" instead of a specific job.
2. **Pick one real, low-stakes workflow.** A drift check, a routine provider upgrade, or a single Terraform module refresh works better than a broad, undefined mandate.
3. **Confirm the identity model in writing.** Ask the vendor directly whether the agent inherits a user's own permissions or holds separate standing credentials, and get the answer from documentation, not a sales call.
4. **Run it against a non-production environment first.** Watch what it proposes, not just whether it succeeds. A tool that proposes reasonable changes it can't yet execute safely is more trustworthy than one that executes anything without a preview step.
5. **Check where the output lands.** If the change becomes a pull request or file diff you can review and revert with your existing tools, you keep full ownership. If it only lives inside the vendor's own state, understand that trade-off before committing production workloads.
6. **Scale only after a second workflow succeeds.** One clean pilot can be luck. A second, different workflow succeeding under the same guardrails is a pattern.

## When another tool is the better choice

- **You're all-in on Crossplane and Kubernetes as your control-plane substrate.** Upbound's tooling is purpose-built for that model in a way a general-purpose agent isn't.
- **Incident response, not change management, is your actual pain point.** Azure SRE Agent, Traversal, or Cleric address a different problem than any change agent in this list.
- **You run several IaC engines and don't plan to consolidate them.** env zero's multi-engine governance layer solves a real problem a single-engine tool can't.
- **Agent identity and secrets are the hard problem you're trying to solve, not code generation.** HashiCorp's Vault agentic IAM work is aimed squarely at that question.
- **You're already deep in Spacelift's run pipeline and Rego policies.** Spacelift Intelligence extends what you have rather than asking you to adopt something new.

## What the data says about agent adoption

Adoption is accelerating faster than trust is catching up, which is exactly why the guardrails questions above matter more than the feature list.

- Gartner projects that [up to 40% of enterprise applications will feature task-specific AI agents by 2026](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025), up from less than 5% in 2025.
- Gartner separately expects spending on [AI governance platforms to reach $492 million in 2026 and surpass $1 billion by 2030](https://www.gartner.com/en/newsroom/press-releases/2026-02-17-gartner-global-ai-regulations-fuel-billion-dollar-market-for-ai-governance-platforms), as regulation pushes organizations to formalize how they oversee AI systems, agents included.
- In Stack Overflow's [2025 Developer Survey](https://survey.stackoverflow.co/2025/ai), more developers actively distrust the accuracy of AI tools (46%) than trust it (33%), which is the trust gap every guardrail in this article exists to close.
- CNCF's [2025 Annual Cloud Native Survey](https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/) found 66% of organizations hosting generative AI models use Kubernetes to manage some or all of their inference workloads, which is a large share of the infrastructure these agents will increasingly touch.

Read together, these numbers describe a category moving faster than most organizations' governance has caught up to, which is exactly the gap a preview step, a policy gate, and a scoped identity are built to close.

## Frequently asked questions

### What are AI agents for DevOps?

AI agents for DevOps are LLM-driven tools that read live infrastructure, pipeline, or observability state and then answer questions, investigate incidents, or propose changes inside guardrails a team defines. They fall into five groups: ChatOps agents, autonomous remediation agents, IaC-native change agents, code-generation agents, and MCP access layers.

### What is an SRE AI agent?

An SRE AI agent investigates production incidents by reading alerts, logs, traces, and recent changes, then reports a likely root cause and suggested mitigation. Examples include AWS DevOps Agent, Datadog Bits Investigation, HolmesGPT, Azure SRE Agent, Traversal, and Cleric. Most are diagnostic first, so check how much action each one may take.

### What is a platform engineering AI agent?

A platform engineering AI agent works through the controls a platform team already owns: templates, policy as code, scoped identities, and reusable components. It can create or change infrastructure on a developer's behalf while every action passes the same gates as a human's. IaC-native agents such as Pulumi Neo follow this model.

### Is an AI agent for infrastructure the same thing as an AI coding assistant?

No. A coding assistant like Copilot or Cursor generates code, including infrastructure code, but has no built-in connection to your live cloud state, policy engine, or approval workflow. An infrastructure agent reads real state and acts inside guardrails, often via the same coding assistant paired with an MCP server for context and bounded actions.

### What is the difference between a change agent and an incident agent?

A change agent plans and applies infrastructure changes, such as Pulumi Neo, env zero's Agent CLI, or Spacelift Intelligence. An incident agent diagnoses and helps resolve problems after something has already broken, such as Azure SRE Agent, Traversal, or Cleric. Most organizations eventually need both, but they solve different problems and are evaluated differently.

### Can an infrastructure agent make changes without human approval?

It depends entirely on the tool's configuration, not just its capability. Every change agent in this article supports a preview-and-approve workflow; whether an organization enables fully autonomous execution for narrow, low-risk changes is a policy decision each team makes deliberately, not a default any vendor should ship silently.

### Does an infrastructure agent need its own credentials?

Not necessarily, and this is one of the most important evaluation questions. Some agents, including Pulumi Neo, are designed to inherit the requesting user's own permissions rather than hold separate standing credentials, which removes an entire class of privilege-escalation risk. Others hold their own service identity. Confirm which model a tool uses before granting it production access.

### What is MCP, and why does it matter for infrastructure agents?

The Model Context Protocol is a standard way for AI agents to query external systems for context and, in some implementations, take bounded actions. HashiCorp's Terraform and Vault MCP servers and Pulumi's MCP server are examples: they don't reason on their own, but they give any MCP-compatible agent real, current access to registry data, secrets, and infrastructure state instead of relying on a model's training data.

## Learn more

- [What is agentic infrastructure?](/what-is/what-is-agentic-infrastructure/)
- [Agent sprawl? Your IaC platform is the answer](/blog/agent-sprawl-iac-platform-is-the-answer/)
- [Best AI Infrastructure Tools in 2026](/blog/ai-infrastructure-tools/) (the compute and MLOps side of the AI-infrastructure landscape)
- [Pulumi Neo documentation](/docs/ai/neo/)
- [Pulumi MCP server documentation](/docs/ai/mcp-server/)
- [Best Terraform Alternatives](/blog/best-terraform-alternatives/)
- [Best Kubernetes Infrastructure as Code Tools in 2026](/blog/best-kubernetes-iac-tools-2026/)
