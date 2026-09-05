---
title: "MCP for Infrastructure as Code: What It Means for Pulumi Users"
meta_desc: MCP connects AI agents to your cloud infrastructure. Learn what MCP for IaC means, how vendors are building it, and how Pulumi's MCP server works.
type: what-is
page_title: "MCP for Infrastructure as Code: What It Means for Pulumi Users"
schema_type: auto
authors: ["alex-leventer"]
---

MCP for infrastructure as code is the use of the Model Context Protocol, an open standard for connecting AI applications to external tools, to let AI agents read, generate, and act on cloud infrastructure defined in code. An MCP server exposes IaC operations, like previewing and deploying resources, through one consistent interface any MCP-compatible agent can call.

## What is the Model Context Protocol?

MCP is an open-source standard, originally created and open-sourced by Anthropic in November 2024, for connecting AI applications to external systems. As of December 2025, governance of the specification was donated to the [Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation), a directed fund under the Linux Foundation co-founded by Anthropic, Block, and OpenAI with support from Google, Microsoft, AWS, Cloudflare, and Bloomberg, so the protocol continues to evolve under neutral, vendor-independent stewardship rather than staying tied to any single company. The current specification, released July 28, 2026, is the fourth major revision since the original November 2024 launch (following 2025-03-26, 2025-06-18, and 2025-11-25), reflecting how quickly the ecosystem is still moving.

The [official MCP documentation](https://modelcontextprotocol.io/introduction) describes it this way:

> "MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems... Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems."

Before MCP, connecting *N* AI applications to *M* external tools required roughly *N × M* custom integrations, one per pairing. MCP collapses that to *N + M*: any MCP-compatible AI application can talk to any MCP server without bespoke glue code.

MCP defines three roles:

- **Hosts** are the AI applications end users interact with, such as Claude, ChatGPT, Cursor, or an IDE's chat panel.
- **Clients** live inside a host and maintain a 1:1 connection to a single server.
- **Servers** expose specific capabilities, tools to call, resources to read, and prompts to reuse, over that connection.

Since OpenAI adopted MCP for its Agents SDK and ChatGPT desktop app on March 26, 2025, and Google announced native MCP support in the Gemini SDK on May 20, 2025, the protocol has become the closest thing the industry has to a common language for agent-to-tool communication, spanning the major model vendors rather than staying with any one of them.

## Why does MCP matter for infrastructure as code?

Infrastructure as code was already a natural fit for AI agents because, by definition, it's code: something a language model can read, generate, and reason about the way it reasons about any other program. What MCP adds is a standard way for an agent to act on that code safely, calling the same preview, deploy, and inspection operations a human engineer would run, instead of an agent guessing at shell commands or hallucinating an API that does not exist.

That distinction matters more for infrastructure than for most domains an agent touches. A mistaken edit to a text document can be undone in seconds. A mistaken `apply` against a production VPC, database, or IAM policy cannot. MCP does not eliminate that risk, but it gives infrastructure tools a structured surface, typed tool calls with defined inputs and outputs, on which to build guardrails: previews before changes, scoped credentials, and policy checks that run in the same loop as the agent's own reasoning.

## Who is building MCP servers for infrastructure?

MCP for infrastructure is a genuinely multi-vendor category, and it's moving fast. No single company owns this space yet, which is exactly why an accurate, current picture matters.

| Vendor | What they shipped | Status as of mid-2026 |
| --- | --- | --- |
| **Pulumi** | `@pulumi/mcp-server` (local, npm) and a hosted server at `mcp.ai.pulumi.com` | General availability; local and remote transports |
| **AWS** | Amazon Bedrock AgentCore open-source MCP server | Launched October 2, 2025; AgentCore Gateway has since added support for newer spec revisions |
| **Microsoft** | Azure MCP Server, an MCP tool inside Azure AI Foundry Agent Service, and Anthropic's official C# SDK (co-created with Microsoft) | Rolling out across Azure and Windows; positioned as first-party tooling for Azure resources |
| **Red Hat** | MCP servers for OpenShift and Ansible Automation Platform | Available for cluster operations and playbook-driven automation |
| **Community / CNCF ecosystem** | Independent `k8s-mcp-server` projects exposing `kubectl`-equivalent operations | Multiple community implementations, varying in scope and maintenance |

A few patterns hold across most of them. Well-designed servers distinguish read operations (list resources, inspect state, run a plan or preview) from write operations (apply, deploy, delete), and the ones built around a plan-and-apply workflow treat the preview-before-apply step as a first-class safety mechanism rather than an afterthought. Where vendors differ is breadth: cloud-provider servers (AWS, Azure) are naturally scoped to their own resources, Kubernetes-focused servers are scoped to cluster operations, and Pulumi's server is the one built specifically around the IaC development loop itself, spanning any of Pulumi's 180+ providers rather than one cloud.

The category is young enough that survey data captures both the appetite and the friction. Zuplo's "State of MCP" research counted over 17,000 publicly listed MCP servers, and a [companion survey of technical professionals](https://zuplo.com/blog/mcp-survey) conducted November-December 2025 found 72% of adopters expect their use of MCP to increase over the next 12 months, while 50% named security and access control as their top challenge. Separately, [Stacklok's "State of Model Context Protocol in Software 2026" report](https://stacklok.com/wp-content/uploads/2026/01/State-of-MCP-in-Software-2026_FINAL.pdf), published January 2026, found 41% of surveyed software organizations already report limited or broad production use of MCP servers. Adoption and unease are rising together, which is the normal shape of a fast-moving, pre-standardized security posture.

## How does Pulumi's MCP server work?

Pulumi ships MCP support in two forms, a local server and a hosted one, so teams can pick the tradeoff between control and setup effort that fits their environment.

| | Local server | Hosted server |
| --- | --- | --- |
| Package | `@pulumi/mcp-server` (npm), also available as the `mcp/pulumi` Docker image | `https://mcp.ai.pulumi.com/mcp` |
| Transport | stdio | Streamable HTTP |
| Auth | `PULUMI_ACCESS_TOKEN` environment variable | OAuth via browser popup |
| Requires Pulumi CLI installed | Yes | No |
| Typical fit | Local development, CI runners you already control | Editors and agents you don't want to provision a CLI on |

The local server's tool names are prefixed to keep them unambiguous inside a host that may be connected to multiple servers at once: `pulumi-registry-list-resources`, `pulumi-registry-list-functions`, `pulumi-registry-get-resource`, `pulumi-registry-get-function`, `pulumi-registry-get-type`, `pulumi-cli-preview`, `pulumi-cli-up`, `pulumi-cli-stack-output`, `pulumi-cli-refresh`, `pulumi-resource-search`, and `neo-task-launcher`, plus a `deploy-to-aws` prompt for a common starting workflow. The hosted server exposes an unprefixed set with the same intent, including `get-stacks` and `resource-search`. Full parameter-level documentation lives on the [Pulumi MCP server docs page](/docs/ai/mcp-server/).

## What can AI agents do with it?

Connected through either transport, an agent can:

- **Inspect your registry and cloud state.** Search Pulumi's registry of resources and providers, look up a resource's exact schema, and read current stack outputs, all without you switching out of your editor to check documentation or the CLI.
- **Generate infrastructure in your language.** Because Pulumi programs are ordinary TypeScript, Python, Go, C#, Java, or YAML, an agent generates infrastructure the same way it generates application code: reading existing patterns in your repository, following your conventions, and producing a diff you review like any other pull request.
- **Run a preview before anything changes.** `pulumi-cli-preview` runs the same dry-run Pulumi engineers use manually, showing exactly which resources would be created, updated, or deleted, so the agent's proposal is inspectable before `pulumi-cli-up` executes it.
- **Delegate multi-step work to Neo.** For tasks that span multiple files or require iterating on a plan, `neo-task-launcher` hands the job to [Neo](/product/neo/), Pulumi's infrastructure engineering agent, which can migrate Terraform to Pulumi, enforce policy, and manage multi-cloud deployments inside your existing workflows.

```typescript
// Example: what an MCP-connected agent might generate after being asked
// to "add an S3 bucket for build artifacts with versioning enabled"
import * as aws from "@pulumi/aws";

const artifactBucket = new aws.s3.BucketV2("build-artifacts", {
    tags: { Purpose: "ci-build-artifacts" },
});

new aws.s3.BucketVersioningV2("build-artifacts-versioning", {
    bucket: artifactBucket.id,
    versioningConfiguration: { status: "Enabled" },
});
```

```python
# The same request, generated in Python
import pulumi_aws as aws

artifact_bucket = aws.s3.BucketV2(
    "build-artifacts",
    tags={"Purpose": "ci-build-artifacts"},
)

aws.s3.BucketVersioningV2(
    "build-artifacts-versioning",
    bucket=artifact_bucket.id,
    versioning_configuration={"status": "Enabled"},
)
```

## How do you connect Pulumi to your AI agent?

The hosted server is the fastest path for most agents and editors:

1. In your MCP host's configuration, add a remote server pointing to `https://mcp.ai.pulumi.com/mcp` using Streamable HTTP transport.
2. Approve access through the OAuth popup when your host first connects. You'll paste a [Pulumi access token](https://app.pulumi.com/account/tokens) and pick the organization the agent should operate against — but no Pulumi CLI installation is required on that machine.
3. Confirm the connection by asking your agent to list your Pulumi stacks; a successful response confirms the tools are registered.

### Running the server locally instead

If you need the connection to run inside an environment you already control, such as a CI runner or an air-gapped workstation, install `@pulumi/mcp-server` (or run the `mcp/pulumi` Docker image), set `PULUMI_ACCESS_TOKEN`, and point your host's server configuration at the local stdio process instead of the hosted URL. The two servers overlap on registry lookups and Neo delegation, but they aren't identical: the CLI-driven tools (`pulumi-cli-preview`, `pulumi-cli-up`, `pulumi-cli-refresh`) are local-only, while organization-wide tools like `get-policy-violations` and `get-users` are hosted-only.

## Is MCP secure enough for production infrastructure?

This is the most common question teams ask before connecting any agent to real cloud resources, and it deserves a direct, non-promotional answer: MCP is still a young protocol, and its security model is still maturing.

Independent researchers have already documented real attack classes. Invariant Labs disclosed Tool Poisoning Attacks, where malicious instructions are hidden inside a tool's description rather than its output, tricking an agent into taking unintended actions, and released MCP-Scan to detect them. Simon Willison and researchers at Snyk Labs have separately analyzed prompt injection as an MCP-specific vector, since a server's responses become part of an agent's context the same way any other tool output does. Two CVEs are publicly tracked: CVE-2025-54136, nicknamed "MCPoison," is remote code execution through silent modification of an already-approved MCP server configuration file, a config-trust issue rather than a tool-description poisoning one, and CVE-2025-49596 affects MCP-Inspector. MCPSecBench, an academic benchmark, catalogs 17 distinct attack types across 4 attack surfaces. In May 2026, the NSA published "Model Context Protocol (MCP): Security Design Considerations," warning that current mitigations offer only partial protection given the protocol's early security maturity, a caution worth taking at face value rather than downplaying.

None of that is unique to Pulumi, and none of it should be read as an argument against connecting infrastructure to MCP; it's an argument for connecting it carefully. Pulumi's approach leans on controls that exist independent of MCP itself: every write operation goes through a preview step an engineer can inspect before approving, access tokens are scoped rather than broad, the hosted server authenticates through OAuth rather than shared secrets, and [policy as code](/docs/insights/policy/) can block a non-compliant change regardless of whether a human or an agent proposed it. Pulumi does not claim to solve MCP's protocol-level security questions; the discipline is treating an MCP-connected agent the same way you would treat a new, junior engineer with real access, that is, with previews, scoped permissions, and policy guardrails in the loop, not unchecked write access to production.

## How does Neo relate to MCP?

[Neo](/product/neo/) is Pulumi's infrastructure engineering agent, and MCP is one of the ways it connects to the rest of your toolchain, alongside its own direct integrations. Where the MCP server exposes granular tools, preview, deploy, search, that any MCP-compatible host can call one at a time, Neo is built specifically to plan and execute multi-step infrastructure work: migrating a Terraform codebase to Pulumi, proposing a fix when a deployment fails, or carrying out a policy change across many stacks, then opening a pull request for review. The `neo-task-launcher` tool in Pulumi's MCP server is the bridge, letting any MCP host hand a task to Neo rather than trying to orchestrate every step itself. For a deeper look at how MCP fits alongside Pulumi's other agent integrations, see [External MCP Servers](/docs/ai/neo/integrations/mcp/) and [CLI for AI Agents](/docs/ai/cli-for-agents/).

## Frequently asked questions

### What is MCP for infrastructure as code?

MCP for infrastructure as code is the application of the Model Context Protocol, an open standard for connecting AI applications to external tools, to infrastructure operations. An MCP server exposes actions like previewing, deploying, and inspecting cloud resources so any MCP-compatible AI agent can call them through one consistent interface instead of a bespoke integration.

### Does Pulumi have an MCP server?

Yes. Pulumi ships both a local server, `@pulumi/mcp-server`, distributed via npm or as the `mcp/pulumi` Docker image, and a hosted server at `https://mcp.ai.pulumi.com/mcp` that authenticates through OAuth and requires no local CLI installation.

### Which vendors are shipping MCP servers for infrastructure?

Pulumi, AWS (Bedrock AgentCore), Microsoft (Azure MCP Server and Azure AI Foundry Agent Service), Red Hat (OpenShift and Ansible Automation Platform), and multiple community-maintained Kubernetes MCP servers all currently ship infrastructure-focused MCP servers, with adoption growing across the ecosystem.

### Which AI tools work with the Pulumi MCP server?

Any MCP-compatible host works, since the protocol standardizes the connection rather than tying it to one vendor. That includes Claude, Cursor, and other IDEs and agent frameworks that implement the MCP client specification.

### Do I need the Pulumi CLI installed to use MCP?

Only for the local server, which shells out to the CLI on your machine. The hosted server at `mcp.ai.pulumi.com` needs no local installation; you connect over Streamable HTTP and authenticate through an OAuth flow, entering a Pulumi access token and choosing an organization the first time you connect.

### Is MCP tied to one AI vendor?

No. MCP was created by Anthropic but was donated to the Agentic AI Foundation in December 2025, a Linux Foundation fund co-founded by Anthropic, Block, and OpenAI with support from Google, Microsoft, AWS, Cloudflare, and Bloomberg. OpenAI adopted MCP in its Agents SDK and ChatGPT desktop app in March 2025, and Google added native MCP support to the Gemini SDK in May 2025.

### What should I do to run MCP safely in production?

MCP's security model is still maturing; researchers have documented real risks including tool poisoning and prompt injection, and the NSA has published guidance noting current mitigations are only partial. Treat an MCP-connected agent the way you would a new engineer with real access: require previews before changes, scope credentials narrowly, and enforce policy as code regardless of who or what proposed the change.

### Which Pulumi MCP tool hands work off to Neo?

Neo is Pulumi's infrastructure engineering agent. MCP is one of the ways it connects to your toolchain; the `neo-task-launcher` tool lets any MCP host hand multi-step work, like a Terraform migration or a policy rollout, to Neo rather than orchestrating each step itself.

### Can an MCP-connected agent deploy real infrastructure?

Yes, through the local server's `pulumi-cli-up` tool. The hosted server doesn't expose a deploy tool of its own, so agents connected through it hand deployment work to Neo's `neo-task-launcher` instead. Either way, every deployment can and should go through a preview step first so a human reviews the plan before it executes, the same discipline used in any CI/CD pipeline.

## Learn more

- [Best MCP Servers for Infrastructure and DevOps in 2026](/blog/best-mcp-servers-infrastructure-devops/)
- [Pulumi MCP Server documentation](/docs/ai/mcp-server/)
- [AI-Assisted IaC with Pulumi's MCP Server](/blog/mcp-server-ai-assistants/)
- [Announcing Pulumi Remote MCP Server](/blog/remote-mcp-server/)
- [External MCP Servers for Neo](/docs/ai/neo/integrations/mcp/)
- [CLI for AI Agents](/docs/ai/cli-for-agents/)
- [What is Agentic Infrastructure?](/what-is/what-is-agentic-infrastructure/)
- [What is an Internal Developer Platform?](/what-is/what-is-an-internal-developer-platform/)
