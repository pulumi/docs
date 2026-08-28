---
title: "Best MCP Servers for Infrastructure and DevOps in 2026"
date: 2026-08-28
draft: false
meta_desc: "The best MCP servers for infrastructure and DevOps in 2026, evaluated by transport, auth, read-only mode, and maturity: IaC, cloud, K8s, CI/CD, ops."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - ai
    - infrastructure-as-code
    - devops
    - platform-engineering
    - kubernetes
category: general
faq_schema: true
howto_schema: true
itemlist_name: "MCP Servers for Infrastructure and DevOps"
itemlist:
    - name: "Pulumi MCP Server"
      url: "https://www.pulumi.com/docs/ai/mcp-server/"
    - name: "HashiCorp Terraform MCP Server"
      url: "https://developer.hashicorp.com/terraform/mcp-server"
    - name: "HashiCorp Vault MCP Server"
      url: "https://developer.hashicorp.com/vault/docs/ai/mcp-server/overview"
    - name: "AWS Knowledge MCP Server"
      url: "https://awslabs.github.io/mcp/"
    - name: "Azure MCP Server"
      url: "https://learn.microsoft.com/azure/developer/azure-mcp-server"
    - name: "containers/kubernetes-mcp-server"
      url: "https://github.com/containers/kubernetes-mcp-server"
    - name: "Flux Operator MCP Server"
      url: "https://fluxcd.control-plane.io/mcp/"
    - name: "GitHub MCP Server"
      url: "https://github.com/github/github-mcp-server"
    - name: "Docker MCP Gateway"
      url: "https://docs.docker.com/ai/mcp-catalog-and-toolkit/"
    - name: "Grafana MCP Server"
      url: "https://grafana.com/docs/grafana/latest/developer-resources/mcp/"
    - name: "Datadog MCP Server"
      url: "https://docs.datadoghq.com/mcp_server/"
    - name: "PagerDuty MCP Server"
      url: "https://github.com/pagerduty/pagerduty-mcp-server"

social:
    twitter: |
        Every cloud vendor and half of DevOps shipped an MCP server this year. We ranked 12 on what matters for infrastructure: what they can mutate, and what stands in front of it.

        IaC, Kubernetes, CI/CD, observability, secrets: one buyer's guide.
    linkedin: |
        MCP servers went from novelty to default in about a year. Every hyperscaler, most CI/CD and observability vendors, and the two biggest IaC ecosystems now ship one.

        The question that matters for a platform team is what the agent on the other end can actually do to production, and what stands between a bad suggestion and a bad outcome. We evaluated MCP servers across infrastructure as code, cloud control planes, Kubernetes and GitOps, CI/CD, observability, and secrets on that axis, not on tool counts.

        The result is a comparison table and a role-based starting point, not another retelling of what MCP is.
    bluesky: |
        We ranked 12 MCP servers for infrastructure and DevOps work on the axis that actually matters: what they can mutate, and what gate stands in front of it.

        One comparison table, not another "what is MCP" explainer.
---

The best MCP server for your infrastructure work depends on what you need an agent to touch: Pulumi's MCP server or HashiCorp's Terraform MCP server for IaC, the AWS Knowledge or Azure MCP servers for cloud control-plane lookups, `containers/kubernetes-mcp-server` for cluster operations, and Grafana, Datadog, or PagerDuty's servers for observability and on-call work. The harder question is which of those servers can change something in production and what gate stands between a bad suggestion and a bad outcome. That's the axis this guide ranks on.

<!--more-->

## At a glance

| If you need to... | Start with |
| --- | --- |
| Provision or preview cloud infrastructure as code | [Pulumi MCP Server](#pulumi-mcp-server) or [HashiCorp Terraform MCP Server](#hashicorp-terraform-mcp-server) |
| Query cloud provider docs and account state | [AWS Knowledge MCP Server](#aws-knowledge-mcp-server), [Azure MCP Server](#azure-mcp-server) |
| Operate a Kubernetes cluster or GitOps pipeline | [containers/kubernetes-mcp-server](#containerskubernetes-mcp-server), [Flux Operator MCP Server](#flux-operator-mcp-server) |
| Automate GitHub or container workflows | [GitHub MCP Server](#github-mcp-server), [Docker MCP Gateway](#docker-mcp-gateway) |
| Query dashboards, traces, or incidents | [Grafana MCP Server](#grafana-mcp-server), [Datadog MCP Server](#datadog-mcp-server), [PagerDuty MCP Server](#pagerduty-mcp-server) |
| Manage secrets and access policy | [HashiCorp Vault MCP Server](#hashicorp-vault-mcp-server) |

## What is an MCP server?

The Model Context Protocol (MCP) is an open standard for connecting AI applications to external tools and data. An MCP server exposes one system's operations, a cloud API, a registry, a dashboard, through a consistent interface any MCP-compatible agent can call, rather than each agent vendor writing a custom integration for every tool. For the full picture of how MCP applies to infrastructure as code specifically, including Pulumi's own server, see [MCP for Infrastructure as Code: What It Means for Pulumi Users](/what-is/mcp-for-infrastructure-as-code/).

MCP is no longer a single vendor's protocol. Anthropic created it in November 2024 and, in December 2025, [donated its governance](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) to the Agentic AI Foundation, a directed fund under the Linux Foundation co-founded by Anthropic, Block, and OpenAI, with Google, Microsoft, AWS, Cloudflare, and Bloomberg as supporting members. At the time of that donation, Anthropic counted more than 10,000 active public MCP servers across the ecosystem. Separately, we queried the [official MCP Registry](https://registry.modelcontextprotocol.io) on 2026-08-28 and found 139 actively listed servers whose name or description matched a curated set of infrastructure and DevOps keywords (Kubernetes, Terraform, AWS, Azure, GitOps, observability, and similar terms), deduplicated to the latest version of each. That's a keyword-biased lower bound, not an official category count, since the registry (itself still in public preview) doesn't yet publish categories, but it gives a sense of how crowded this specific corner of the ecosystem already is.

## Evaluating an MCP server for infrastructure work

Most MCP server comparisons stop at "does it exist" and "how many tools does it expose." For infrastructure and DevOps work, where a tool call can change something running in production, a handful of other criteria matter more.

| Criterion | Why it matters |
| --- | --- |
| **Read vs. write boundary** | Can the server only look things up, or can it change infrastructure? If it can write, is there a plan-only or dry-run mode you can enforce? |
| **Transport** | Stdio (local process) or Streamable HTTP (network-reachable)? Stdio confines the server to one machine; HTTP needs its own auth and network controls. |
| **Auth model** | Static long-lived tokens, OAuth 2.1 with scoped resource tokens, or delegated/agent-scoped identity? This determines what an agent can do if its session is compromised. |
| **Hosted vs. self-run** | A vendor-hosted endpoint removes operational burden but puts your infrastructure's context in a third party's request path. Self-run gives you control over egress and logging. |
| **Maturity** | GA, beta, or community-maintained? A beta label (HashiCorp's Vault MCP server, for instance) is the vendor telling you not to point it at production yet. |
| **Maintainer** | Vendor-official, CNCF/foundation-governed, or unaffiliated community project? This affects how much you can expect from security patching and long-term support. |

The read/write boundary is the one to lead with. A server that only answers questions carries a fundamentally different risk profile than one that can run `terraform apply` or delete a Kubernetes namespace, even if both show up on the same "MCP servers for infrastructure" list.

## Which MCP servers cover infrastructure as code?

### Pulumi MCP Server

**Maintainer:** Pulumi. **Transport:** stdio (local `@pulumi/mcp-server`) or Streamable HTTP (hosted at `mcp.ai.pulumi.com`). **Auth:** access token env var locally, OAuth on the hosted endpoint. **Read-only mode:** the registry and Pulumi Cloud tools are read-only by nature; the CLI tools (`pulumi-cli-up`, `pulumi-cli-refresh`) can write, gated by Pulumi's own preview step. **Maturity:** shipping product feature, both forms actively maintained.

Pulumi ships two forms so you can choose the operating model: a local server for CLI-driven workflows (preview, up, refresh, stack outputs) and a hosted server for organization-wide tools like policy-violation queries and Neo task delegation, no CLI install required. The full tool list, client setup for Cursor, Claude Code, Claude Desktop, Windsurf, and Kiro, and the local-versus-hosted tradeoffs are covered in the [Pulumi MCP server documentation](/docs/ai/mcp-server/); we won't re-list every tool here.

**Best for:** teams already on Pulumi who want an agent to query stacks, resources, and policy state, and optionally hand deployment work to Neo with a preview gate in front of it.

### HashiCorp Terraform MCP Server

**Maintainer:** HashiCorp. **Transport:** stdio (default) or Streamable HTTP. **Auth:** token passthrough supported for centralized HTTP deployments; no built-in OAuth documented at the time of writing. **Read-only mode:** yes, the server is documentation- and registry-lookup focused by default; a plan-only mode is available for teams that want proposals without execution access. **Maturity:** GA, per HashiCorp's own announcement.

The Terraform MCP server gives any MCP-compatible agent real-time access to Terraform Registry documentation, modules, and provider schemas, so generated HCL reflects the current registry state instead of a model's training-data snapshot.

**Best for:** Terraform and OpenTofu shops that want agent-generated HCL to stay current with registry changes without giving the agent standing apply access.

## Which MCP servers cover cloud provider control planes?

### AWS Knowledge MCP Server

**Maintainer:** AWS. **Transport:** Streamable HTTP. **Auth:** none required; it's a documentation retrieval tool, not an account-scoped one. **Read-only mode:** the entire server is read-only by design. **Maturity:** GA, announced October 1, 2025 following a July 2025 preview.

This server answers questions against AWS documentation, the What's New feed, Well-Architected guidance, and regional service availability. It requires no AWS credentials because it never touches your account, which makes it a low-risk default for teams that want agent-accurate AWS answers without opening any account access. AWS's separate `aws-api-mcp-server`, which can run arbitrary AWS CLI-equivalent calls against your account, is explicitly flagged on AWS's own docs as being superseded by newer, narrower servers; check the current AWS Labs MCP catalog before standing up a broad-access server when a narrower one (this one, or the EKS/ECS/IaC-specific servers) will do.

**Best for:** any team wanting agent answers grounded in current AWS documentation, with zero account-access risk.

### Azure MCP Server

**Maintainer:** Microsoft. **Transport:** local install via package manager or IDE extension, or remote deployment via Microsoft Foundry / Copilot Studio. **Auth:** Azure identity and RBAC. **Read-only mode:** depends on the service and the RBAC role granted; the server spans dozens of Azure services (Key Vault, Cosmos DB, Monitor, RBAC itself) with both read and write operations available per service. **Maturity:** actively maintained, consolidated into Microsoft's unified `microsoft/mcp` repository.

Because the Azure MCP server's capability surface tracks whatever RBAC role you grant it, the practical read/write boundary is a configuration decision, not a fixed property of the server. Scope the service principal narrowly per the criteria above rather than relying on the server itself to hold the line.

**Best for:** teams standardizing on Azure who want one server surface across many Azure services instead of one per product.

## Which MCP servers cover Kubernetes and GitOps?

### containers/kubernetes-mcp-server

**Maintainer:** the `containers` GitHub organization (Red Hat-affiliated). **Transport:** stdio and Streamable HTTP. **Auth:** whatever kubeconfig or ServiceAccount token the server is launched with. **Read-only mode:** available, and explicitly recommended in the project's own setup guide via a dedicated read-only ServiceAccount; the default mode is read/write. **Maturity:** actively released (versioned PyPI and container image releases).

This server exposes generic Kubernetes and OpenShift resource operations plus Helm chart install and list actions. Because its default posture is read/write against whatever cluster credentials you give it, the project's own documented hardening step, a read-only ServiceAccount, is the first thing to configure before pointing an agent at anything beyond a sandbox cluster.

**Best for:** teams wanting broad, generic cluster query and operation access from any MCP client, with the discipline to scope its ServiceAccount down first.

### Flux Operator MCP Server

**Maintainer:** ControlPlane, via the Flux Operator product (built on the CNCF Flux project). **Transport:** stdio. **Auth:** cluster credentials the operator runs with. **Read-only mode:** not the default; the server is built to let an agent inspect and act on GitOps reconciliation state. **Maturity:** shipping since mid-2025, actively developed into 2026.

Where `containers/kubernetes-mcp-server` is generic, the Flux Operator MCP server is purpose-built for GitOps: it understands Flux's reconciliation model (sources, kustomizations, Helm releases) rather than treating the cluster as an undifferentiated set of resources.

**Best for:** teams already running Flux Operator who want an agent that reasons about reconciliation state, not just raw manifests.

## Which MCP servers cover CI/CD and source control?

### GitHub MCP Server

**Maintainer:** GitHub. **Transport:** local stdio server (the more mature option) or a remote hosted server, in public preview since June 2025. **Auth:** GitHub OAuth or a personal access token, depending on mode. **Read-only mode:** available as a launch flag; default is read/write. **Maturity:** local server well-established; remote server newer and still in preview.

Dozens of tools cover repositories, issues, pull requests, Actions runs, and code search, with both read and write operations, including the ability to open PRs and merge them. That write capability is exactly why the read-only flag is worth enabling for any agent that only needs repository context rather than the ability to act on it.

**Best for:** any team wanting an agent to read or act on GitHub repository state, from PR review context to opening pull requests itself.

### Docker MCP Gateway

**Maintainer:** Docker. **Transport:** runs as a Docker Desktop / CLI plugin that proxies and aggregates other MCP servers behind one endpoint. **Auth:** per-server secrets isolation, managed by the gateway rather than by each individual server. **Read-only mode:** depends on which servers are catalogued behind it. **Maturity:** shipping Docker product feature.

Rather than an infrastructure-specific MCP server, this is distribution and aggregation infrastructure for running third-party MCP servers as containers, with the gateway handling secrets isolation and routing. Worth knowing about because it changes how you'd operationally run several of the other servers on this list, rather than adding a new capability of its own.

**Best for:** teams running several MCP servers who want one gateway managing secrets and routing instead of configuring each server's auth separately.

## Which MCP servers cover observability and incident response?

### Grafana MCP Server

**Maintainer:** Grafana Labs. **Transport:** local process, versioned releases. **Auth:** Grafana API key or service account token. **Read-only mode:** the server is primarily a query interface against dashboards, datasources, and alerts. **Maturity:** actively released.

Lets an agent query dashboards, datasources, and alert rules directly rather than working from a description of what a dashboard shows.

**Best for:** teams wanting an agent to reason over live Grafana dashboards and alerting state during investigation.

### Datadog MCP Server

**Maintainer:** Datadog. **Transport:** both a local/CLI mode and a hosted remote server. **Auth:** Datadog API and application keys. **Read-only mode:** query-focused by design (metrics, logs, monitors); Datadog documents it as agent-ready observability access. **Maturity:** shipping product feature with an official docs page.

**Best for:** teams standardized on Datadog who want an agent answering "what does the data say" without hand-copying dashboard screenshots into a prompt.

### PagerDuty MCP Server

**Maintainer:** PagerDuty (official). **Transport:** local server. **Auth:** PagerDuty API token. **Read-only mode:** incident and on-call query tools are the primary surface; check the current tool list before granting write scopes like acknowledging or resolving incidents. **Maturity:** actively maintained, officially branded.

**Best for:** on-call and incident-response workflows where an agent needs current incident and schedule state, not a training-data guess at your PagerDuty setup.

## Which MCP servers cover secrets and security?

### HashiCorp Vault MCP Server

**Maintainer:** HashiCorp. **Transport:** stdio and Streamable HTTP. **Auth:** Vault's own auth methods (tokens, mounts); no separate OAuth layer. **Read-only mode:** no, by default. The server's documented tool set includes creating and deleting KV secrets engines and mounts, which are mutating operations. **Maturity:** explicitly labeled beta by HashiCorp; the docs note beta functionality is "stable but possibly incomplete" and discourage production use.

This server pairs with HashiCorp's broader "agentic identity" push in Vault Enterprise: trusted identities for agents, delegated authorization, and fine-grained access through an Agent Registry. The beta label is HashiCorp being direct about where the line currently sits: treat it as a design-and-test tool for now, not a production secrets-management interface for autonomous agents.

**Best for:** Vault shops evaluating agent-scoped secrets access ahead of a production rollout, with the beta caveat firmly in mind.

## Full comparison table

| Server | Maintainer | Transport | Hosted or self-run | Read-only mode | Can mutate infra | Maturity |
| --- | --- | --- | --- | --- | --- | --- |
| Pulumi MCP Server | Pulumi | stdio + Streamable HTTP | Both | Registry/Cloud tools yes; CLI tools no | Yes (gated by preview) | Shipping |
| HashiCorp Terraform MCP Server | HashiCorp | stdio + Streamable HTTP | Self-run | Yes (default) | Yes (plan-only mode available) | GA |
| HashiCorp Vault MCP Server | HashiCorp | stdio + Streamable HTTP | Self-run | No | Yes | Beta |
| AWS Knowledge MCP Server | AWS | Streamable HTTP | Hosted | Yes (always) | No | GA |
| Azure MCP Server | Microsoft | Local or remote | Both | Depends on RBAC | Yes | Actively maintained |
| containers/kubernetes-mcp-server | containers org | stdio + Streamable HTTP | Self-run | Available, opt-in | Yes (default) | Actively released |
| Flux Operator MCP Server | ControlPlane / Flux | stdio | Self-run | No | Yes | Actively developed |
| GitHub MCP Server | GitHub | stdio or remote | Both | Available, opt-in | Yes (default) | Local: mature; remote: preview |
| Docker MCP Gateway | Docker | Local plugin | Self-run | Depends on catalog | Depends on catalog | Shipping |
| Grafana MCP Server | Grafana Labs | Local | Self-run | Yes (query-focused) | No | Actively released |
| Datadog MCP Server | Datadog | Local or hosted | Both | Yes (query-focused) | No | Shipping |
| PagerDuty MCP Server | PagerDuty | Local | Self-run | Mostly (check scopes) | Depends on scopes | Actively maintained |

## How to run an MCP server safely against production infrastructure

1. **Scope credentials narrowly.** Give the server the smallest token, role, or ServiceAccount that does the job, not the identity you use for everyday admin work.
2. **Prefer read-only where the task allows it.** Several servers on this list, `containers/kubernetes-mcp-server` and GitHub's server among them, ship a read-only mode as a launch flag. Default to it and only widen scope when a specific task needs it.
3. **Put a gateway or proxy in front of anything network-reachable.** Docker's MCP Gateway pattern, or a comparable internal proxy, centralizes secrets handling and gives you one place to enforce header-based routing and rate limits instead of trusting every client's local configuration.
4. **Require a preview or plan step before any mutating call executes.** Terraform's plan-only mode and Pulumi's preview-before-up discipline exist for exactly this reason: a human should see what will change before an agent, or anyone else, executes it.
5. **Pin server versions instead of always pulling latest.** Several servers are distributed via `npx`- or `uvx`-style runners that fetch the newest version at call time; pin a version so a supply-chain compromise upstream doesn't reach your agent automatically.
6. **Control egress from wherever the server runs.** An MCP server with broad account access and unrestricted outbound network access is a bigger blast radius than the same server on a locked-down network path.
7. **Log every tool call.** Treat MCP tool invocations the way you'd treat any privileged API call: with an audit trail you can review after the fact, not just in the moment.

MCP's threat model, including tool poisoning, prompt injection, and the specific CVEs researchers have documented against MCP infrastructure, is covered in more depth in [MCP for Infrastructure as Code: What It Means for Pulumi Users](/what-is/mcp-for-infrastructure-as-code/#is-mcp-secure-enough-for-production-infrastructure). The steps above are the operational controls that follow from that threat model, not a restatement of it.

## Which MCP server to start with

**If you're an IaC team:** start with the server for your existing tool, Pulumi's or HashiCorp's Terraform server, before adding a second one. Both give an agent current registry and stack context without requiring you to change how you provision anything.

**If you're a Kubernetes platform team:** start with `containers/kubernetes-mcp-server` in its read-only ServiceAccount mode. Add the Flux Operator server only if you're already running Flux Operator and want GitOps-aware queries specifically.

**If you're on-call or SRE:** Grafana's and PagerDuty's servers cover the two things you actually query mid-incident, dashboards and on-call state, without needing write access to either system.

**If you're evaluating this from a security standpoint:** start with the read-only, hosted options (AWS Knowledge MCP Server, Grafana, Datadog in query mode) to build confidence in the pattern before granting any server write access to production.

## Frequently asked questions

### Are MCP servers safe to point at production infrastructure?

It depends entirely on which server, which mode, and what credentials you give it. A read-only server like the AWS Knowledge MCP Server carries little risk because it can't change anything. A server that can mutate infrastructure, like `containers/kubernetes-mcp-server` in its default mode or the Terraform MCP server without plan-only enabled, needs the same scoped-credential and approval-gate discipline you'd apply to any automated system with write access.

### Do I need a separate MCP server for every tool in my stack?

Usually yes, at least one per major system (your IaC tool, your cluster, your observability stack), though a gateway like Docker's MCP Gateway can front several of them behind one endpoint for secrets and routing purposes. There's no single MCP server that spans infrastructure as code, Kubernetes, and observability today.

### What's the difference between a hosted and a self-run MCP server?

A hosted server, like the AWS Knowledge MCP Server or Pulumi's remote server at `mcp.ai.pulumi.com`, runs on the vendor's infrastructure and you connect over Streamable HTTP with no local install. A self-run server runs as a local process (stdio) or a service you deploy yourself, giving you more control over network egress and logging at the cost of running it.

### Is a beta-labeled MCP server, like HashiCorp's Vault server, safe to use at all?

Safe to evaluate and test against non-production data, not safe to point at production secrets. HashiCorp's own documentation is explicit that beta functionality is "stable but possibly incomplete" and discourages production use. Treat a beta label as the vendor's own answer to the maturity question in the evaluation criteria above.

### How is this different from comparing AI agents for infrastructure?

An MCP server and an AI agent are different layers. The server is an access and data interface; it does no reasoning of its own. An agent is the thing that decides what to do and calls the server's tools to do it. This guide evaluates the servers themselves, transport, auth, read/write boundary, maturity; evaluating the agents that plan and apply changes through them, Pulumi Neo and others, is a separate comparison.

### Does Pulumi's MCP server work with servers from other vendors?

Yes. Any MCP-compatible host, Cursor, Claude Code, Claude Desktop, and others, can connect to Pulumi's server alongside other MCP servers in the same session; MCP standardizes the connection rather than tying an agent to one vendor's server. See the [Pulumi MCP server documentation](/docs/ai/mcp-server/) for supported clients.

## Learn more

- [MCP for Infrastructure as Code: What It Means for Pulumi Users](/what-is/mcp-for-infrastructure-as-code/)
- [Pulumi MCP Server documentation](/docs/ai/mcp-server/)
- [Announcing Pulumi Remote MCP Server](/blog/remote-mcp-server/)
- [AI-Assisted IaC with Pulumi's MCP Server](/blog/mcp-server-ai-assistants/)
- [Neo External MCP Server Integrations](/docs/ai/neo/integrations/mcp/)
- [Pulumi Neo](/product/neo/)
- [Best AI Infrastructure Tools in 2026](/blog/ai-infrastructure-tools/)
