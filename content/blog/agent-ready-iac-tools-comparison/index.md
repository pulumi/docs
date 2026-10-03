---
title: "How Agent-Ready Is Your IaC Tool? A Practical Comparison"
date: 2026-10-03
draft: false
meta_desc: "Score Pulumi, Terraform, OpenTofu, AWS CDK, and Crossplane on seven agent-readiness criteria: preview, structured output, tests, policy, guardrails, and MCP."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - ai-agents
    - infrastructure-as-code
    - ai
    - platform-engineering
category: general
faq_schema: true
itemlist_name: "Agent-Ready Infrastructure as Code Tools"
itemlist:
    - name: "Pulumi"
      url: "https://www.pulumi.com/"
    - name: "Terraform"
    - name: "OpenTofu"
    - name: "AWS CDK"
    - name: "Crossplane"

related_posts:
    - token-efficiency-vs-cognitive-efficiency-choosing-iac-for-ai-agents
    - better-cli-interactions-for-agents-and-humans
    - infrastructure-as-code-tools

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        An IaC tool is agent-ready when an agent can preview, test, and be stopped before it breaks something.

        We scored Pulumi, Terraform, OpenTofu, AWS CDK, and Crossplane on seven practical criteria, with credit where each tool is strong.
    linkedin: |
        When an AI agent runs your infrastructure as code, the tool matters as much as the model. Can the agent preview a change before applying it? Does the tool return structured output? Can policy block an unsafe change? Can you fence off destructive operations?

        We scored Pulumi, Terraform, OpenTofu, AWS CDK, and Crossplane on seven criteria, with a comparison table, fair credit for each tool's strengths, and guidance on which workflows fit which tool.
    bluesky: |
        Which IaC tools work well with AI agents? We scored Pulumi, Terraform, OpenTofu, AWS CDK, and Crossplane on seven criteria: preview, structured output, tests, policy, guardrails, and MCP support.
---

An IaC tool is agent-ready when an AI agent can propose a change, preview it, test it, and be stopped by policy before anything breaks, all without a human reading terminal output. Seven criteria separate the tools: preview, structured output, testing, policy hooks, fast feedback, delete guardrails, and a programmatic or MCP interface. This post scores Pulumi, Terraform, OpenTofu, AWS CDK, and Crossplane on each.

<!--more-->

Most "best IaC tools" lists compare syntax, ecosystem size, and cloud coverage. Those still matter, and our [broader infrastructure as code tools roundup](/blog/infrastructure-as-code-tools/) covers them. An agent adds a different set of requirements, because it works in a loop of write, preview, fix, and retry, and it cannot squint at a console and decide a plan looks fine. The criteria below come from what that loop needs.

For evidence on the writing side of the loop, see our [benchmark of token efficiency versus cognitive efficiency](/blog/token-efficiency-vs-cognitive-efficiency-choosing-iac-for-ai-agents/) for agents generating Terraform HCL and Pulumi TypeScript. This post covers everything around the generated code.

## How do the tools compare at a glance?

Every tool here can be driven by an agent today, so the table scores how much of the agent loop each one covers natively. "Strong" means the capability is built in and documented, "Partial" means it exists with a gap or an extra tool, and "Limited" means you would build it yourself.

| Criterion | Pulumi | Terraform / OpenTofu | AWS CDK | Crossplane |
|---|---|---|---|---|
| Preview before apply | Strong: `pulumi preview` | Strong: `terraform plan` | Strong: `cdk diff`, change sets | Limited: local render only |
| Structured output | Strong: `--json` | Strong: `show -json` | Partial: CloudFormation JSON APIs | Strong: Kubernetes API objects |
| Self-testing | Strong: standard test frameworks | Strong: `terraform test`, `tofu test` | Strong: assertions module | Partial: render and validate |
| Policy hooks | Strong: Pulumi Policies | Strong: Sentinel, OPA | Strong: cdk-nag, Guard, Hooks | Partial: admission policy |
| Fast feedback while writing | Strong: compiler and IDE | Partial: `validate` and `plan` | Strong: compiler and IDE | Partial: schema validation |
| Delete guardrails | Strong: `protect` | Strong: `prevent_destroy` | Strong: removal policies | Partial: management policies |
| Programmatic or MCP interface | Strong: Automation API, MCP server, [Neo](/product/neo/) | Strong: MCP server, HCP API | Partial: Toolkit Library, MCP servers | Partial: Kubernetes API |

The rest of this post explains each score and where the gaps are.

## Can the agent preview a change before applying it?

A preview lets an agent see exactly what will be created, updated, or deleted before it commits. This is the single most important safety property for agent-driven infrastructure, because the preview is where a wrong guess gets caught instead of deployed.

- **Pulumi:** `pulumi preview` shows the planned changes, `--diff` shows property-level differences, and `--expect-no-changes` exits with an error if the program would change anything. That last flag is useful for an agent verifying a refactor.
- **Terraform and OpenTofu:** `terraform plan -out=tfplan` saves a plan that `apply` later executes, so the thing the agent reviewed is the thing that runs.
- **AWS CDK:** `cdk diff` compares your app with the deployed stack. With `--method=change-set` it creates a CloudFormation change set, and `--fail` returns a non-zero exit code when differences exist.
- **Crossplane:** there is no native plan against live state. `crossplane composition render` shows the resources a composition would produce, locally, which helps but does not diff against the cluster.

Crossplane's model is continuous reconciliation, so resources converge on their own once applied. That suits long-running control planes, and it means previewing happens earlier, in the pipeline that validates manifests.

## Does the tool return structured, machine-readable output?

An agent reads output as text, and text full of progress bars and color codes wastes tokens and invites misreads. Structured output lets the agent branch on fields instead of parsing prose.

- **Pulumi:** `pulumi preview --json` and `pulumi up --json` emit machine-readable results, and the [Automation API](/docs/iac/concepts/automation-api/) returns typed results from code. Our post on [better CLI interactions for agents and humans](/blog/better-cli-interactions-for-agents-and-humans/) covers the CLI design choices behind this.
- **Terraform and OpenTofu:** `terraform show -json tfplan` converts a saved plan to JSON. The documentation warns that the output can contain sensitive values in plain text, so an agent pipeline should handle it accordingly.
- **AWS CDK:** `cdk diff` prints for humans, but CloudFormation change sets can be read as JSON through `aws cloudformation describe-change-set`.
- **Crossplane:** every resource is a Kubernetes object, so `kubectl get -o json` and status conditions give agents structured state with no extra tooling.

## Can the agent test its own changes?

An agent that can run tests can check its own work and iterate without a human. The question is whether tests run in the framework the agent already knows and whether they run without touching the cloud.

- **Pulumi:** programs are ordinary code, so [unit tests](/docs/iac/guides/testing/unit/) run in Jest, pytest, `go test`, and the other native frameworks, with `pulumi.runtime.setMocks` replacing provider calls. Integration tests deploy real stacks.
- **Terraform and OpenTofu:** `terraform test` and `tofu test` run `*.tftest.hcl` files, with plan-only and apply modes.
- **AWS CDK:** the assertions module checks synthesized CloudFormation templates with `Template.fromStack` and `hasResourceProperties`, and supports snapshot tests.
- **Crossplane:** `crossplane composition render` runs a composition function pipeline locally, and `crossplane resource validate` checks resources against XRD, CRD, and provider schemas.

## Are there policy hooks that block unsafe changes before deploy?

Policy turns "the agent was told not to" into "the agent cannot". It is the control that scales when many agents and many people change infrastructure at once.

- **Pulumi:** [Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/) evaluates resources during `pulumi preview` and `pulumi up`. Enforcement levels are `advisory`, `mandatory`, and `remediate`, and a `mandatory` violation blocks the deployment.
- **Terraform and OpenTofu:** HCP Terraform supports Sentinel and OPA policy enforcement and run tasks at pre-plan, post-plan, pre-apply, and post-apply stages. With OpenTofu or self-managed Terraform, you can run OPA or Conftest against the plan JSON in CI.
- **AWS CDK:** cdk-nag adds rule packs to synthesis, CloudFormation Guard validates templates, and CloudFormation Hooks check resources during provisioning.
- **Crossplane:** Kubernetes admission control applies, through ValidatingAdmissionPolicy, Kyverno, or OPA Gatekeeper, so you assemble the policy layer from cluster tooling.

## Does the agent get fast, unambiguous feedback while it writes?

Agents fix mistakes quickly when errors are specific and arrive early. A compiler error naming a wrong property and its type is easier for a model to act on than a failure discovered at apply time.

Pulumi and CDK use general-purpose languages, so type checkers, linters, and language servers catch many mistakes before any preview runs. HCL is a smaller and simpler language that models handle well, and `terraform validate` plus `terraform plan` give quick feedback too. The [benchmark linked above](/blog/token-efficiency-vs-cognitive-efficiency-choosing-iac-for-ai-agents/) found HCL used fewer tokens while typed Pulumi TypeScript needed fewer repair attempts, so each approach wins on a different axis.

Crossplane manifests are YAML validated against schemas, which catches structural errors but not logic errors. Composition functions written in Go or Python get the same compiler feedback as any code in those languages.

## Can destructive operations be fenced off?

Guardrails limit the blast radius when an agent gets something wrong despite previews and policy. The goal is for deleting a database to require a deliberate human step.

- **Pulumi:** the [`protect` resource option](/docs/iac/concepts/resources/options/protect/) makes deletion fail until it is removed, and `retainOnDelete` leaves the cloud resource in place when it leaves the Pulumi stack.
- **Terraform and OpenTofu:** `lifecycle { prevent_destroy = true }` makes any plan that would destroy the resource fail.
- **AWS CDK:** `RemovalPolicy.RETAIN`, CloudFormation `DeletionPolicy`, and stack termination protection serve the same purpose.
- **Crossplane:** `managementPolicies` can restrict a managed resource to actions such as `Observe`, so Crossplane watches a resource without updating or deleting it.

These options live in code or manifests, so a reviewer sees changes to them in the same diff as everything else. Pair them with scoped cloud credentials, because provider-side protections are the last line of defense.

## Is there a programmatic or MCP interface for agents?

Agents increasingly connect through the Model Context Protocol (MCP) or an SDK instead of a shell. An interface designed for agents can expose safe operations and withhold dangerous ones.

- **Pulumi:** the [Automation API](/docs/iac/concepts/automation-api/) drives deployments from code, and the [Pulumi MCP server](/docs/ai/mcp-server/) exposes tools for searching resources, reading policy findings, and launching Neo tasks. [Neo](/product/neo/) is Pulumi's infrastructure agent, and the Pulumi [agent skills](/docs/ai/skills/) work with clients including Claude Code, Codex, Cursor, and GitHub Copilot.
- **Terraform and OpenTofu:** HashiCorp's `terraform-mcp-server` covers registry lookups and HCP Terraform workspaces and runs. Tools that change workspaces or act on runs stay disabled until you set `ENABLE_TF_OPERATIONS=true`, a sensible default.
- **AWS CDK:** the CDK Toolkit Library offers programmatic access, and the AWS IaC MCP server in the `awslabs/mcp` repository provides CloudFormation template validation, CDK documentation search, and deployment troubleshooting.
- **Crossplane:** the Kubernetes API is the interface, so any agent that can use `kubectl` or a Kubernetes client can work with it, governed by Kubernetes RBAC.

## Which tool fits which agent workflow?

No single tool wins every row, so match the tool to the workflow you want agents to own.

- **Agents writing and refactoring application-adjacent infrastructure:** Pulumi and AWS CDK give agents typed code, real tests, and compiler feedback in a language they already know.
- **Agents extending an existing Terraform or OpenTofu estate:** stay with HCL. The ecosystem is large, `plan` output is well understood, and `terraform test` plus the MCP server cover the loop.
- **AWS-only teams with CloudFormation governance:** CDK change sets, Guard, and Hooks fit existing controls.
- **Kubernetes-centric platform teams:** Crossplane lets agents request infrastructure through the Kubernetes API with RBAC and admission policy already in place.
- **Multi-cloud, multi-team platforms with agents in the loop:** Pulumi's preview, policy, and Automation API combination in one tool reduces the number of pieces to assemble. Our [head-to-head comparisons](/docs/iac/comparisons/) cover migration and feature differences in more depth.

For the platform view of this shift, see [what is agentic infrastructure](/what-is/what-is-agentic-infrastructure/).

## Frequently asked questions

### What makes an IaC tool agent-ready?

An agent-ready IaC tool lets an agent preview changes, read structured output, run tests, pass policy checks, and operate within delete guardrails. It also offers a programmatic or MCP interface so the agent does not depend on scraping terminal text. A tool can be strong on some of these and still need supporting pieces for the rest.

### Can AI agents safely run terraform apply?

Agents can run `terraform apply` safely when they apply a reviewed, saved plan, policy checks run before apply, and credentials are scoped to the target environment. Many teams keep apply behind a human approval step or a pipeline. Applying a saved plan file ensures the agent executes the same change the reviewer saw.

### Is Pulumi or Terraform better for AI agents?

It depends on the workflow. Terraform has a large HCL ecosystem and a simple language models handle well. Pulumi offers typed languages, native test frameworks, and an Automation API, which helps agents verify their own work. In our [token efficiency benchmark](/blog/token-efficiency-vs-cognitive-efficiency-choosing-iac-for-ai-agents/), HCL used fewer tokens and Pulumi TypeScript needed fewer repairs.

### Do AI agents need an MCP server to manage infrastructure?

No. Agents manage infrastructure through CLIs every day, and a well-designed CLI with JSON output works. An MCP server adds value by exposing a curated set of operations, which lets you limit what the agent can call and standardize how it connects across tools.

### How do I stop an AI agent from deleting production infrastructure?

Combine several layers. Mark critical resources with `protect`, `prevent_destroy`, or a retain policy, require passing policy checks before deployment, scope the agent's cloud credentials to least privilege, and keep production applies behind human approval. No single control is enough, so layer them.
