---
title_tag: "CDK vs. Terraform vs. Pulumi"
faq_schema: true
authors: ["pulumi-content-team"]
meta_desc: "Compare AWS CDK, Terraform, and Pulumi on architecture, language support, multi-cloud reach, state management, and testing, and see where each one fits."
title: CDK vs. Terraform
h1: CDK vs. Terraform vs. Pulumi
menu:
    iac:
        name: CDK vs. Terraform
        parent: iac-comparisons
        weight: 26
        identifier: iac-comparisons-cdk-vs-terraform
---

AWS CDK, Terraform, and Pulumi all provision cloud infrastructure as code, but they differ in the language you write, how that code reaches the cloud, and how far each one reaches beyond a single provider. CDK compiles to CloudFormation and is AWS-only; Terraform uses its own HCL language across many clouds; Pulumi runs general-purpose languages (TypeScript, Python, Go, C#, Java) or HCL across any cloud, provisioning directly through its own engine with no template-synthesis step.

## How do CDK, Terraform, and Pulumi differ architecturally?

The three tools diverge structurally in how code becomes a deployed resource. AWS CDK code passes through [JSII](https://docs.aws.amazon.com/cdk/v2/guide/languages.html) and [`cdk synth`](https://docs.aws.amazon.com/cdk/v2/guide/deploy.html) into a CloudFormation template before anything is validated against real infrastructure; an agent's errors surface against synthesized logical IDs one translation step removed from the code it wrote. Terraform's `terraform plan` computes a resource-level diff without an intervening synthesis step, but HCL is a domain-specific language with limited abstraction, and tests live in a separate harness ([`terraform test`](https://developer.hashicorp.com/terraform/language/tests)) using dedicated `.tftest.hcl` files rather than alongside the resource code. Pulumi programs are written in the same general-purpose language (TypeScript, Python, Go, C#, Java, or HCL) the agent already uses elsewhere in the codebase, so a type checker, linter, and unit tests can catch errors before any cloud call, and `pulumi preview` returns a direct resource-level diff with no template-synthesis step.

## CDK vs. Terraform vs. Pulumi: feature comparison

| Feature | Pulumi | Terraform | AWS CDK |
| --- | --- | --- | --- |
| Languages | TypeScript, Python, Go, C#, Java, YAML, and HCL | HCL (a domain-specific language) | TypeScript, Python, Java, C#, Go (via JSII) |
| Language type | General-purpose, plus a first-class HCL runtime | Domain-specific | General-purpose, compiled to a DSL output |
| Cloud coverage | Any cloud or SaaS via [200+ providers](/registry/) | Any cloud via Terraform/OpenTofu providers | AWS only |
| Deploys through | Pulumi's own deployment engine | Terraform CLI applies directly | AWS CloudFormation (CDK synthesizes to CFN templates) |
| Preview/diff | `pulumi preview`, resource-level, no synthesis step | `terraform plan`, resource-level | `cdk diff`, compares to synthesized CloudFormation template |
| State management | Pulumi Cloud (default), self-managed backends, or use Pulumi as a [Terraform/OpenTofu state backend](/docs/iac/get-started/terraform/terraform-state-backend/) | HCP Terraform, S3/other remote backends, or local state | CloudFormation stack state (AWS-managed) |
| Testing | Native unit/property tests in-language, run before any cloud call | Separate harness (`terraform test`, Terratest) | Native unit tests in-language (CDK assertions library), against synthesized template |
| Reusable abstractions | Components, packages published to language package managers | Modules | Constructs, published as libraries via JSII |
| Policy as code | Built-in ([Pulumi Policies](/docs/insights/policy/)) | Sentinel/OPA (HCP Terraform or separate tooling) | CloudFormation Guard, cdk-nag (separate tooling) |
| Secrets management | Built-in ([Pulumi ESC](/docs/esc/)) | Vault or external integration | AWS Secrets Manager / SSM (external, AWS-only) |
| Agent feedback loop | Shortest: same-language type checks, tests, and preview, no translation step | Fast plan/apply, but a separate DSL and test harness | Longest: JSII binding layer, synthesis to CloudFormation, stack-level rollback |
| License | Apache 2.0 (open source) | Business Source License (BUSL), IBM-owned since Feb. 2025 | Apache 2.0 (open source) |
| Current version (measured 2026-08-07) | CLI v3.256.0 | v1.15.8 (OpenTofu v1.12.5) | v2.263.0 |

## How do CDK, Terraform, and Pulumi differ on multi-cloud reach?

AWS CDK is scoped to AWS: it synthesizes to CloudFormation, and CloudFormation only understands AWS (and a small set of third-party resource types registered with it). No supported path exists to provision Azure, Google Cloud, or Kubernetes resources from a CDK app without stepping outside CDK entirely.

Terraform and Pulumi both provision any cloud through a provider ecosystem. The [Terraform Registry lists 7,000+ providers](https://registry.terraform.io/) (measured 2026-08-07), and OpenTofu — the Linux Foundation-stewarded fork created after Terraform's 2023 license change — reports [3,900+ providers and 23,600+ modules](https://search.opentofu.org/) (measured 2026-08-07). Pulumi supports [200+ providers](/registry/), many derived from the same open-source Terraform provider schemas, plus native providers for AWS, Azure, and Kubernetes with no bridging layer.

## How does each tool manage state?

CDK relies entirely on CloudFormation's own stack state; there is no separate state file to manage, but there is also no state backend choice to make; you get CloudFormation's model or nothing.

Terraform and OpenTofu track state in a file, typically stored remotely (HCP Terraform, an S3 bucket, or another supported backend). Pulumi defaults to Pulumi Cloud as a managed state backend, but as of 2026 can also run as [the state backend for existing Terraform or OpenTofu configurations](/docs/iac/get-started/terraform/terraform-state-backend/) via a standard `backend "remote"` block, with no change to how `.tf` files are authored.

## How do you test infrastructure in each tool?

CDK ships a unit testing library (`aws-cdk-lib/assertions`) that asserts against the synthesized CloudFormation template, in the same language as the app. Terraform testing lives in a separate harness rather than alongside the resource code: `terraform test` runs dedicated `.tftest.hcl` files, and third-party options like Terratest are written in Go regardless of what deployed the infrastructure. Pulumi programs are ordinary code, so they use the same unit and property-testing frameworks (Jest, pytest, Go's testing package, and so on) already used for application code in that language, and those tests can run before any cloud call is made.

## How do the ecosystems and communities compare?

Terraform has the largest and oldest provider ecosystem by raw count (7,000+ providers in the Terraform Registry, measured 2026-08-07), reflecting nearly a decade as the default IaC tool. OpenTofu, forked from Terraform in 2023 after HashiCorp's license change to BUSL, inherited that same provider compatibility and has grown its own module registry (23,600+ modules, per [search.opentofu.org](https://search.opentofu.org/), measured 2026-08-07) under Linux Foundation governance. AWS CDK's ecosystem is the Construct Hub, which indexes reusable constructs for CDK (and for CDK8s and CDKTF); the AWS-only constraint comes from CloudFormation, the deployment target, rather than from the construct ecosystem itself. Pulumi's registry spans 200+ pre-built providers, mixing native providers (built directly against cloud provider APIs, including Kubernetes and Azure Native) with providers bridged from Terraform's schemas — and [any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) can be adapted into a Pulumi provider on demand, so the registry count isn't the ceiling on what's reachable from Pulumi.

## How well does each tool work with AI coding agents?

Beyond architecture and ecosystem, one more axis worth measuring separately is how each tool holds up when an AI coding agent, rather than a person, is writing the code.

Recent research on LLM-generated infrastructure as code finds that raw syntax is mostly a solved problem: a 2025 study of LLM-generated CloudFormation, Terraform, and AWS CDK found [more than 95% syntactic validity across all three formats](https://arxiv.org/abs/2509.05303), with the real gap in "semantic alignment and handling complex infrastructure patterns." Across all three formats, the differentiator is the verification loop available to the agent rather than the syntax it produces.

A separate 2026 study, [IaC-Eval v2](https://arxiv.org/abs/2607.20478), measured how much a tight feedback loop matters in practice: a 7B model's pass rate on Terraform/AWS tasks rose from a **14.0% pass@1** baseline to **45.7%** with active retrieval, and to **62.9%** (7B model) and **84.4%** (GPT-4o) once agents could iteratively refine against verifier feedback. The tighter and more direct that feedback loop, the better an agent performs.

Pulumi's own benchmark of Claude Opus 4.6 and GPT-5.2-Codex against equivalent Terraform and Pulumi generation tasks found that with Opus, the [total cost of an agent completing a generation-plus-refactor pipeline was 41% lower with Pulumi than Terraform ($0.146 vs. $0.249)](/blog/token-efficiency-vs-cognitive-efficiency-choosing-iac-for-ai-agents/), and that "the difference comes entirely from repair cycles: Pulumi needed zero repairs across both scenarios, while Terraform refactoring triggered self-repair on every run." Fewer translation steps and more verifiers close to the code an agent wrote means fewer repair cycles, which is where the real cost and reliability gap shows up.

## How does each tool's agent feedback loop actually work?

* **AWS CDK**: code (TypeScript, Python, Java, C#, or Go via JSII) → `cdk synth` produces a CloudFormation template → `cdk deploy` hands the template to the CloudFormation service. An agent's edits are validated by `cdk diff` and CloudFormation's own drift detection, but failures surface against the synthesized template and roll back at the stack level, one step removed from the source the agent edited.
* **Terraform**: HCL → `terraform plan` computes a resource-level diff → `terraform apply`. The plan step is fast and high-fidelity, but HCL has no native type system or general-purpose control flow, so an agent working across modules is reasoning in a DSL distinct from the rest of the codebase, and correctness checks beyond syntax require a separate test harness.
* **Pulumi**: code in a general-purpose language → compiler/type-checker and unit tests run locally, before any cloud call → `pulumi preview` gives a resource-level diff in the same run. Every verifier available to that language's toolchain (IDE, linter, type checker, test framework) applies directly to the infrastructure code, with no synthesis or transpilation step between what the agent wrote and what gets deployed.

## When should you choose each one?

* **Choose AWS CDK** if your infrastructure is AWS-only for the foreseeable future, your team already standardizes on CloudFormation for governance or compliance reasons, and you want native integration with AWS-specific tooling like SAM or CDK Pipelines.
* **Choose Terraform (or OpenTofu)** if you have deep existing HCL investment, a team fluent in Terraform's module ecosystem, and no near-term need for general-purpose language features like loops, testing frameworks, or shared libraries across infrastructure and application code.
* **Choose Pulumi** if you want multi-cloud coverage in a general-purpose language your team (and your AI agents) already write, want infrastructure tests to run in the same framework as application tests, or want to keep existing `.tf` files and Terraform workflows while gaining a faster agent feedback loop and Pulumi Cloud's collaboration features.

None of these is a universally correct choice; teams with heavy CloudFormation tooling or Terraform module investment have real switching costs that this comparison doesn't erase.

## Frequently asked questions

### Can AWS CDK do multi-cloud?

No. AWS CDK synthesizes to AWS CloudFormation templates, and CloudFormation only provisions AWS resources (plus a limited set of third-party resource types registered with it). Teams that need genuine multi-cloud coverage from a single tool typically choose Terraform, OpenTofu, or Pulumi instead.

### Is Pulumi a Terraform replacement or a CDK replacement?

Both, depending on what you're replacing. Pulumi replaces CDK for teams that want the same general-purpose-language model without being locked to AWS and CloudFormation. Pulumi also replaces Terraform for teams that want the same multi-cloud provider coverage with real languages and tests instead of HCL — and, if you're not ready to leave HCL, Pulumi can run as [a drop-in state backend for existing Terraform or OpenTofu configurations](/docs/iac/get-started/terraform/terraform-state-backend/) with no rewrite required.

### What happened to CDK for Terraform (CDKTF)?

CDK for Terraform, a separate HashiCorp project that let you write Terraform configurations in TypeScript, Python, Java, C#, or Go, [was deprecated on December 10, 2025](https://developer.hashicorp.com/terraform/cdktf), and its GitHub repository has been archived. See [Pulumi vs. CDKTF](/docs/iac/comparisons/cdktf/) for migration paths.

### Can I use my existing AWS CDK constructs with Pulumi?

Not directly; CDK constructs are JSII-based and synthesize to CloudFormation, while Pulumi programs run through Pulumi's own deployment engine. Migrating means re-expressing constructs as Pulumi components, though the underlying AWS resource shapes are usually similar since both ultimately model the same AWS APIs. See the [AWS CDK migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-cdk/) for the recommended path.

### Can I keep writing HCL and still use Pulumi?

Yes. Pulumi supports HCL as a first-class language (`runtime: hcl` in `Pulumi.yaml`), running ordinary `.tf` files as a superset of Terraform's HCL, and separately can serve as the state backend for Terraform or OpenTofu configurations you don't want to touch at all. See [HCL on Pulumi](/docs/iac/languages-sdks/hcl/) for details.

### Which of the three deploys fastest?

It depends on the resources and account topology more than the tool itself; all three ultimately wait on the same underlying cloud provider APIs. Where the tools differ is iteration speed during development: Pulumi's `pulumi preview` and Terraform's `terraform plan` both give a fast resource-level diff without a synthesis step, while CDK's `cdk diff` compares against a freshly synthesized CloudFormation template, adding a step to each iteration.

### Do I have to migrate everything at once?

No. All three tools support incremental adoption. Pulumi can [import existing resources](/docs/iac/guides/migration/import/) managed by CDK, CloudFormation, or Terraform without recreating them, and its Terraform state backend support lets you adopt Pulumi Cloud for existing Terraform-managed infrastructure before rewriting any configuration.

## Next steps

* [Pulumi vs. AWS CDK](/docs/iac/comparisons/aws-cdk/) — a deeper look at Pulumi as a direct CDK alternative
* [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/) — the full feature-by-feature comparison with Terraform
* [Pulumi vs. CDKTF](/docs/iac/comparisons/cdktf/) — migration guidance now that CDKTF is deprecated
* [Pulumi vs. AWS CloudFormation](/docs/iac/comparisons/cloudformation/) — comparing the underlying deployment target CDK synthesizes to
* [HCL on Pulumi](/docs/iac/languages-sdks/hcl/) — run existing Terraform HCL files directly on Pulumi
* [Using Pulumi Cloud as a Terraform/OpenTofu state backend](/docs/iac/get-started/terraform/terraform-state-backend/)
* [Migrating from AWS CDK to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-cdk/)
* [Token efficiency vs. cognitive efficiency: choosing IaC for AI agents](/blog/token-efficiency-vs-cognitive-efficiency-choosing-iac-for-ai-agents/) — Pulumi's own benchmark data on agent generation cost and repair cycles
* [Pulumi Neo](/docs/ai/neo/) — an infrastructure engineering agent that works across these workflows
