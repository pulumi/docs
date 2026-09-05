---
title: What Is Terragrunt?
meta_desc: "Terragrunt wraps Terraform and OpenTofu to add DRY configuration, remote state management, and multi-module orchestration. Learn how it works."
type: what-is
page_title: "What Is Terragrunt?"
authors: ["pulumi-content-team"]
---

**Terragrunt is an open-source, thin wrapper for Terraform and OpenTofu that adds DRY configuration, automated remote state management, and multi-module orchestration on top of the underlying tool.** Originally created by [Gruntwork](https://gruntwork.io/), it exists to solve the repetition and scaling problems teams hit when they manage large infrastructure estates with plain Terraform or OpenTofu across many environments and modules.

Terragrunt does not replace Terraform or OpenTofu; it calls them. You keep writing modules in HCL, and Terragrunt orchestrates how those modules are configured, wired together, and applied, so you write less boilerplate and run fewer manual commands as your infrastructure grows.

In this article, we'll cover the key questions about Terragrunt:

* What is Terragrunt?
* Why does Terragrunt exist?
* How does Terragrunt work?
* What are Terragrunt's key features?
* How does Terragrunt relate to OpenTofu and Terraform?
* What are the alternatives to Terragrunt?
* How does Pulumi compare to Terragrunt?
* Frequently asked questions about Terragrunt

## What is Terragrunt?

Terragrunt is a command-line tool that wraps Terraform and OpenTofu to make large, multi-environment infrastructure codebases easier to keep DRY (don't repeat yourself) and easier to orchestrate. You invoke `terragrunt` in place of `terraform` or `tofu`, and it reads a small `terragrunt.hcl` configuration file that tells it how to generate backend configuration, pass inputs to a module, resolve dependencies between modules, and run commands across many modules at once.

The core problem Terragrunt targets is the repetition that appears when you manage the same infrastructure across development, staging, and production, or across many services that each need their own Terraform state. In plain Terraform, each of those directories tends to repeat the same backend block, the same provider configuration, and the same module-calling boilerplate. Terragrunt lets you define that configuration once and reference it everywhere, so a change happens in one place instead of a dozen.

Terragrunt is open source under the MIT license and is maintained by Gruntwork alongside a large community of contributors. It is a companion tool for the Terraform/OpenTofu ecosystem specifically: everything it does is expressed in HCL and delegated to Terraform or OpenTofu underneath.

## Why does Terragrunt exist?

Terraform is excellent at describing a single unit of infrastructure, but it does not include strong opinions about how to organize many units at scale. As a Terraform codebase grows, teams run into a predictable set of frustrations, and Terragrunt was built to address each of them.

**Repetition of backend and provider configuration.** Terraform requires a backend block in every root module, and it cannot use variables in that block. That forces teams to copy the same remote-state configuration into every environment and every component, changing only a key or a path. Terragrunt generates that configuration dynamically, so the backend is defined once.

**No native cross-module orchestration.** Plain Terraform applies one root module at a time. If your network module must exist before your database module, and your database before your application, you run each `terraform apply` in the correct order by hand or with custom scripts. Terragrunt models dependencies between modules and can apply an entire graph in the right order with a single command.

**Duplicated inputs across environments.** Development, staging, and production usually share most of their configuration and differ in a few values. Terragrunt lets you factor the common inputs into shared files and override only what changes per environment.

Gruntwork created Terragrunt out of its own consulting work building production infrastructure for clients, where these patterns recurred constantly. The tool encodes the conventions Gruntwork found useful for keeping a growing Terraform codebase maintainable.

## How does Terragrunt work?

Terragrunt sits between you and Terraform or OpenTofu. When you run a Terragrunt command, it reads configuration, generates the files Terraform expects, and then shells out to the underlying binary.

**You run `terragrunt` instead of `terraform`.** Commands mirror the tool underneath: `terragrunt plan`, `terragrunt apply`, `terragrunt destroy`. Terragrunt forwards these to Terraform or OpenTofu after doing its own preparation.

**Configuration lives in `terragrunt.hcl` files.** Each unit of infrastructure has a `terragrunt.hcl` that points at a Terraform module (local or remote), supplies its inputs, and can pull in shared configuration from parent files higher in the directory tree using the `include` and `read_terragrunt_config` functions.

**Backend and provider configuration is generated.** Rather than committing a static backend block, you declare a `remote_state` block once (often in a root `terragrunt.hcl`), and Terragrunt writes the correct backend configuration for each module at runtime, typically deriving a unique state key from the module's path.

**Dependencies are resolved into a graph.** A `dependency` block lets one module consume the outputs of another. Terragrunt reads these relationships, builds a dependency graph, and can run a command across all modules in the correct order.

**`run --all` orchestrates many modules.** Commands like `terragrunt run --all apply` walk the graph and apply every module, respecting dependencies, so you can stand up or tear down a whole environment in one invocation instead of visiting each directory.

Because Terragrunt delegates the actual planning and applying to Terraform or OpenTofu, your modules, your state, and your provider ecosystem are unchanged. Terragrunt only changes how that work is configured and sequenced.

## What are Terragrunt's key features?

Terragrunt's feature set clusters around keeping configuration DRY and orchestrating work across modules.

**DRY remote state.** A single `remote_state` block defines your backend once and applies it to every module, with per-module state keys generated automatically. This removes the most common source of copy-paste in Terraform codebases.

**DRY inputs and configuration inheritance.** Shared inputs, provider settings, and locals can be defined in parent `terragrunt.hcl` files and inherited by child modules through `include`, so environment-specific files contain only what actually differs.

**Dependencies between modules.** The `dependency` block lets a module read another module's outputs, and Terragrunt uses those relationships to order execution. This is how a database module can consume a VPC ID without you wiring it manually.

**Multi-module orchestration.** `run --all` (previously `run-all`) executes plan, apply, or destroy across an entire tree of modules in dependency order, turning what would be many manual runs into one command.

**Units and Stacks.** Newer Terragrunt introduces first-class terminology and configuration for composition: a *unit* is a Terragrunt wrapper around a single deployable Terraform module, and a *stack* (defined in a `terragrunt.stack.hcl` file) is a reusable collection of units that can be nested and composed, pushing Terragrunt from a DRY helper toward a pattern-level way to package infrastructure.

**Hooks and code generation.** Before/after hooks let you run commands around Terraform operations, and `generate` blocks let Terragrunt write provider or version files into each module at runtime.

The table below summarizes the gaps in plain Terraform that each feature addresses.

| Terragrunt feature | Problem in plain Terraform/OpenTofu | What Terragrunt does |
|---|---|---|
| DRY remote state | Backend block repeated in every root module, can't use variables | Generates backend config from one `remote_state` block |
| Configuration inheritance | Inputs and provider config duplicated per environment | Shares config via `include` from parent files |
| Dependencies | No native ordering between root modules | Models a dependency graph and passes outputs |
| `run --all` | Each module applied manually, one at a time | Applies many modules in dependency order |
| Units and Stacks | No first-class way to package and reuse module compositions | Reusable, nestable stacks of units |

## How does Terragrunt relate to OpenTofu and Terraform?

Terragrunt has always been a wrapper, and for most of its history the thing it wrapped was Terraform. When [OpenTofu](/docs/iac/comparisons/opentofu/) forked from Terraform, Gruntwork added first-class OpenTofu support to Terragrunt, and current releases default to invoking OpenTofu (`tofu`) while still supporting Terraform. You choose which binary Terragrunt calls, and every Terragrunt feature (DRY state, inheritance, dependencies, `run --all`) works the same regardless of which one runs underneath.

This is the important 2025-2026 context: the capabilities Terragrunt provides (remote-state management, DRY configuration, dependency ordering) are specific to the Terraform and OpenTofu world. They exist because HCL-based tools organize infrastructure as directories of root modules, each with its own state and backend. Terragrunt is the layer that makes that model scale. If you work in that ecosystem and want to reduce boilerplate without changing tools, Terragrunt is the most established answer. Gruntwork has also signaled a maturing product, shipping a Terragrunt 1.0 release in 2026 with an explicit backward-compatibility commitment.

## What are the alternatives to Terragrunt?

Terragrunt is not the only way to manage Terraform or OpenTofu at scale, and it is not the only way to do infrastructure as code. Alternatives fall into a few categories.

**Native Terraform/OpenTofu patterns.** Some teams avoid a wrapper entirely and lean on workspaces, partial backend configuration passed via `-backend-config`, and shared modules. This keeps the toolchain minimal but leaves the orchestration and DRY problems Terragrunt solves largely to you.

**TACO platforms (Terraform Automation and Collaboration).** Managed and self-hosted platforms such as HCP Terraform, Spacelift, env0, and Scalr run Terraform or OpenTofu for you, adding state management, run pipelines, policy, and drift detection. These overlap with parts of Terragrunt (state, orchestration) but operate as a control plane rather than a local wrapper, and several teams run Terragrunt inside them.

**OpenTofu on its own.** For teams whose main motivation is licensing, OpenTofu is a drop-in, open-source alternative to Terraform and can be used with or without Terragrunt.

**Different IaC tools.** Tools like [Pulumi](/docs/iac/), AWS CDK, and Crossplane take a different modeling approach altogether. Pulumi in particular replaces the HCL-plus-wrapper stack with general-purpose programming languages, which changes how DRY configuration and orchestration are expressed (more on this below).

The right alternative depends on what is driving the search. If the pain is Terraform boilerplate, Terragrunt or a TACO platform helps. If the pain is the HCL model itself, or the need for a separate tool just to stay DRY, a language-based IaC tool is worth evaluating.

## How does Pulumi compare to Terragrunt?

[Pulumi](/docs/iac/) and Terragrunt address some of the same pains from opposite directions. Terragrunt adds a DRY and orchestration layer *on top of* an HCL tool. Pulumi is a complete [infrastructure as code](/what-is/what-is-infrastructure-as-code/) platform in which the same needs are met by the programming language and the platform itself, so there is no separate wrapper to adopt.

**DRY comes from the language, not a wrapper.** In Pulumi, you write infrastructure in TypeScript, Python, Go, C#, Java, or YAML. Loops, functions, classes, and package imports are native to those languages, so factoring out shared configuration, iterating over environments, and building reusable abstractions ([components](/docs/iac/concepts/components/)) is just ordinary programming. The repetition Terragrunt exists to remove is handled by the same mechanisms you already use to keep application code DRY.

**State is a managed service, not a tool you configure.** Pulumi manages [state](/what-is/what-is-terraform-state/) for you through the managed Pulumi Cloud backend, or a self-hosted backend if you prefer (S3, Azure Blob, Google Cloud Storage, or local files). There is no per-module backend block to generate and keep DRY, because backend configuration is not something each project has to declare.

**Orchestration across stacks is built in.** Pulumi models environments as [stacks](/docs/iac/concepts/stacks/) and lets one stack consume another's outputs via [stack references](/docs/iac/concepts/stacks/#stackreferences), so ordering and cross-project wiring don't need an external dependency graph. [Pulumi Deployments](/docs/deployments/) adds managed runs, [drift detection](/what-is/what-is-infrastructure-drift/), and [GitOps](/what-is/what-is-gitops/) workflows.

| Dimension | Terragrunt | Pulumi |
|---|---|---|
| What it is | Wrapper over Terraform/OpenTofu | Full IaC platform |
| Authoring language | HCL + `terragrunt.hcl` | TypeScript, Python, Go, C#, Java, YAML |
| DRY mechanism | Config inheritance and generation | Native language features (loops, functions, classes) |
| State | Backend you configure per module | Managed service or self-hosted backend |
| Cross-module wiring | `dependency` blocks and `run --all` | Stack references and stacks |
| Extra tool required for DRY/orchestration | Yes (Terragrunt itself) | No |

None of this makes Terragrunt a poor choice. For teams committed to Terraform or OpenTofu and happy with HCL, Terragrunt is a well-established, pragmatic way to scale a codebase. Pulumi is worth considering when you'd rather get DRY configuration, abstraction, and orchestration from a programming language and a managed platform than from HCL plus a wrapper. If you already have Terraform or Terragrunt code, Pulumi can [convert and adopt it](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/), and the two ecosystems interoperate.

## Frequently asked questions about Terragrunt

### What is Terragrunt in simple terms?

Terragrunt is a small command-line tool that wraps Terraform or OpenTofu. You run `terragrunt` instead of `terraform`, and it removes repetitive configuration (like backend blocks and shared inputs) and lets you apply many related modules in the right order with one command. It doesn't replace Terraform; it makes a large Terraform codebase less repetitive and easier to orchestrate.

### What is the difference between Terragrunt and Terraform?

Terraform (and OpenTofu) is the engine that actually plans and provisions infrastructure from HCL modules. Terragrunt is a wrapper that sits on top and adds capabilities Terraform lacks at scale: DRY remote-state configuration, inheritance of shared inputs across environments, dependencies between modules, and multi-module orchestration. Terragrunt always calls Terraform or OpenTofu underneath to do the real work.

### What is the difference between Terragrunt and OpenTofu?

OpenTofu is an open-source fork of Terraform and functions as the provisioning engine. Terragrunt is a wrapper you can run on top of OpenTofu (or Terraform). Current Terragrunt releases default to invoking OpenTofu, but they are different kinds of tools: OpenTofu provisions infrastructure, and Terragrunt orchestrates and de-duplicates how you call it.

### What are the alternatives to Terragrunt?

Alternatives include using native Terraform patterns (workspaces, partial backend config, shared modules) without a wrapper; TACO platforms like HCP Terraform, Spacelift, env0, and Scalr that provide state and run orchestration as a service; and different IaC tools such as Pulumi, AWS CDK, and Crossplane that model infrastructure differently. The best fit depends on whether your pain is Terraform boilerplate specifically or the HCL model more broadly.

### Is Terragrunt still needed?

It depends on your stack and goals. Native Terraform and OpenTofu have improved, and TACO platforms now handle some of what Terragrunt provides, so a few teams no longer reach for it. But for organizations that manage many modules and environments in HCL and want to keep that configuration DRY without adopting a platform, Terragrunt remains one of the most widely used solutions, and Gruntwork continues to develop it, including a 1.0 release with a backward-compatibility commitment.

### What is the difference between Terragrunt and Pulumi?

Terragrunt is a wrapper that adds DRY configuration and orchestration on top of HCL-based Terraform or OpenTofu. Pulumi is a full infrastructure as code platform where you write infrastructure in general-purpose languages, so DRY configuration, abstraction, and looping come from the language itself and state is handled by a managed or self-hosted backend, with no separate wrapper to adopt. Terragrunt suits teams staying in the Terraform/OpenTofu ecosystem; Pulumi suits teams who prefer real programming languages and a managed platform.

### Does Terragrunt manage Terraform state?

Yes, indirectly. Terragrunt doesn't store state itself, but it generates the backend configuration for each module from a single `remote_state` block, typically deriving a unique state key per module. This keeps remote-state setup DRY across a large codebase while the state itself still lives in your chosen backend, such as an S3 bucket or Azure storage account.

### What are Terragrunt units and stacks?

A *unit* is a Terragrunt wrapper around a single deployable Terraform module, defined by a `terragrunt.hcl` file. A *stack* is a reusable collection of units, defined in a `terragrunt.stack.hcl` file, that can be composed and nested, for example reusing a web-app stack and adding a monitoring stack. Units and stacks give Terragrunt a first-class way to package and reuse infrastructure patterns, not just remove repetition.

## Learn more

Terragrunt is a solid choice for teams scaling Terraform or OpenTofu who want to stay in HCL. If you'd rather get DRY configuration, reusable abstractions, and orchestration from a general-purpose programming language, with state handled by a managed or self-hosted backend and no separate wrapper to maintain, Pulumi is worth a look. [Explore Pulumi infrastructure as code](/docs/iac/) or see how Pulumi [compares to Terraform](/docs/iac/comparisons/terraform/).

Related reading:

* [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
* [Pulumi vs. OpenTofu](/docs/iac/comparisons/opentofu/)
* [Convert Terraform to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/)
* [What is infrastructure as code?](/what-is/what-is-infrastructure-as-code/)
* [What is Terraform state?](/what-is/what-is-terraform-state/)
* [What is a Terraform module?](/what-is/what-is-a-terraform-module/)
* [What is infrastructure drift?](/what-is/what-is-infrastructure-drift/)
* [What is GitOps?](/what-is/what-is-gitops/)
* [What is platform engineering?](/what-is/what-is-platform-engineering/)
