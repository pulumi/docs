---
title: "Best Terraform Alternatives in 2026"
date: 2026-07-18
updated: 2026-08-21
draft: false
meta_desc: "Terraform alternatives for 2026, updated for CDKTF's sunset and OpenTofu 1.12: Pulumi, AWS CDK, Crossplane, and Bicep compared on reach and governance."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - terraform
    - infrastructure-as-code
    - ai
    - platform-engineering
    - devops
category: general
faq_schema: true
social:
    twitter: |
        Updated for August 2026: CDK for Terraform is archived, OpenTofu is at 1.12, and Pulumi now runs your existing .tf files directly.

        We compared eight Terraform alternatives on multi-cloud reach, governance, and how well each works with an agent in the loop.
    linkedin: |
        Terraform remains a capable, widely used tool. But as AI coding agents become part of everyday infrastructure work, teams are re-evaluating what they need from their IaC platform.

        Agents reason best about code they were trained on: real, general-purpose languages with tests, functions, and packages, not a single proprietary DSL. That's prompting a fresh look at the Terraform-alternatives landscape.

        Since we first published this guide, HashiCorp archived CDK for Terraform, OpenTofu shipped its 1.12 release, and Pulumi shipped both native HCL support and a Terraform-compatible state backend, so authoring format and deployment engine no longer have to be the same decision.

        We lined up eight alternatives, from a community-governed HCL-compatible fork to Kubernetes-native frameworks to general-purpose-language platforms, against the same three questions: multi-cloud reach, governance, and agent-readiness.

        Which one wins depends on which of those three questions matters most to your team, and it isn't the same answer for everyone.
    bluesky: |
        Terraform alternatives in 2026 split into three camps: general-purpose-language platforms, HCL-compatible forks, and cloud-specific tools.

        Updated for August 2026: CDK for Terraform is now archived, and Pulumi can run your .tf files directly or sit under your existing Terraform CLI as a state backend.
---

The strongest Terraform alternatives in 2026 fall into three groups: general-purpose-language platforms like Pulumi and AWS CDK, HCL-compatible forks like OpenTofu, and cloud-specific tools like AWS CloudFormation, Azure Bicep, and Crossplane. Which one fits depends less on syntax preference than on how well it lets your team, and your AI coding agents, read, test, and change infrastructure safely.

What's changed since this list was last useful: HashiCorp archived CDK for Terraform in December 2025, OpenTofu shipped its 1.12 release in May 2026, and Pulumi now runs the same HCL files Terraform does, so authoring format and deployment engine are separate decisions.

<!--more-->

## Why teams are re-evaluating Terraform in 2026

Terraform has been the default infrastructure-as-code tool for most of the last decade, and for good reason: a mature provider ecosystem, a large community, and a state model that most platform teams have learned to live with. But three forces are pushing teams to look again at what else is available.

The first is licensing. HashiCorp moved Terraform from the open-source Mozilla Public License to the Business Source License in August 2023, a shift that triggered the community fork now known as OpenTofu. HashiCorp itself became a wholly owned subsidiary of IBM when that acquisition closed in February 2025. Neither event breaks anything for existing Terraform users, but both changed how governance and long-term product direction get decided, and that's enough for some platform teams to want a documented Plan B.

The second is the accumulated cost of working in a domain-specific language. HCL wasn't designed for the abstraction, composition, and testing patterns that platform engineering now expects: sharing logic across teams, writing meaningful unit tests, and building internal libraries that read like software rather than templated configuration. Terraform has closed some of this gap over time, adding a native test framework in version 1.6, but the ceiling on what a declarative DSL can express is still lower than what a general-purpose language offers.

The third, and the one reshaping the conversation fastest, is agentic AI. Coding agents like GitHub Copilot, Claude, and Pulumi's own Neo are now a standing part of how engineering teams write and review code, and infrastructure is not exempt. These agents were trained on enormous volumes of real Python, TypeScript, Go, and Java, plus their entire testing and tooling ecosystems, but on comparatively little well-formed HCL. When an agent can write and modify infrastructure in a language it already understands deeply, the feedback loop of propose, test, preview, and ship gets tighter. When it has to reason about a purpose-built DSL, that loop lengthens and the agent is more likely to produce configuration nobody would write by hand. That gap doesn't disqualify Terraform, but it does mean "which IaC tool works best with AI agents" is now a first-class question when teams evaluate alternatives, alongside the perennial ones about multi-cloud reach and governance.

None of this is an argument that Terraform is going away. It remains a capable, widely adopted tool with a genuinely large provider catalog. It's an argument that 2026 is a reasonable moment to look at what else exists, honestly, and pick the tool that fits where your infrastructure and your engineering workflow are actually headed. For a broader look at how AI agents are changing infrastructure work generally, see [building for agentic infrastructure](/releases/agentic-infrastructure-era/). For a head-to-head look at Pulumi and Terraform specifically, see our [Pulumi vs. Terraform comparison](/docs/iac/comparisons/terraform/).

## Do you have to leave HCL behind?

No, and that's a meaningful change since this guide was last written. Authoring format and deployment engine used to be a single choice: pick Terraform, and HCL and the Terraform CLI came as a bundle. Two things Pulumi shipped as generally available in August 2026 split that bundle apart.

The first is [Pulumi HCL](/docs/iac/languages-sdks/hcl/), which runs the same `.tf` files you'd write for Terraform or OpenTofu, unmodified, on Pulumi's engine. A project is a `Pulumi.yaml` with `runtime: hcl` and one or more `.tf` files, needs Pulumi CLI 3.256.0 or later, and resolves providers against the OpenTofu registry by default. It isn't a perfect emulation: `backend`, `provider_meta`, `required_version`, and `experiments` blocks are accepted but ignored with a warning, a `cloud` block is an error, existing Terraform state files aren't read directly (bring resources over with `pulumi import --from hcl`), and provisioner `connection` blocks support SSH only.

The second is [Pulumi Cloud as a Terraform and OpenTofu state backend](/docs/iac/get-started/terraform/terraform-state-backend/), which goes the other direction: keep the Terraform or OpenTofu CLI exactly as it is, and point its `backend "remote"` block at `tf.pulumi.com` for encrypted state storage, locking, update history, and Insights visibility. This also has real limits worth stating plainly: drift detection isn't available for Terraform-managed stacks (it requires a Pulumi program), migrating from HCP Terraform state is a manual export and push rather than an automatic switch, and update diffs are derived from state rather than a live `terraform plan`, so they're best-effort.

| If you want to keep... | Change this... |
|---|---|
| Your `.tf` files and HCL syntax | Nothing — run them on Pulumi's engine with `runtime: hcl` |
| Your Terraform or OpenTofu CLI and workflow | Only the backend, pointed at Pulumi Cloud |
| Neither, and want a general-purpose language | Everything — see the [Pulumi vs. Terraform comparison](/docs/iac/comparisons/terraform/) |

For the mechanics of each path, see [terraform-to-pulumi-cloud-hands-on](/blog/terraform-to-pulumi-cloud-hands-on/), [how Pulumi's engine models Terraform's data model](/blog/terraforms-data-model-on-pulumis-engine/), and [how Pulumi HCL is tested for OpenTofu compatibility](/blog/compatibility-testing-pulumi-hcl/).

## Pulumi

Pulumi is an infrastructure-as-code platform that lets you define cloud infrastructure in general-purpose languages, including Python, TypeScript, JavaScript, Go, .NET, and Java, plus YAML and HCL for teams that prefer a declarative format. Rather than compiling down to another tool's templates, Pulumi programs run directly against a deployment engine that supports more than 180 providers in total, covering AWS, Azure, Google Cloud, Kubernetes, and a long tail of SaaS and on-prem targets.

Pulumi also supports HCL as a first-class language, and Pulumi Cloud can serve as a drop-in [state backend for existing Terraform code](/docs/iac/get-started/terraform/terraform-state-backend/). That means teams with a large, working Terraform estate aren't required to rewrite anything to get Pulumi Cloud's state management, access controls, and policy enforcement — they can point existing HCL at Pulumi with minimal changes, then migrate configuration into a general-purpose language on their own timeline rather than all at once.

Writing infrastructure in a real language means you get the tooling that comes with it for free: IDE autocomplete and type checking, unit and integration test frameworks, package managers for sharing reusable components, and the same code review and CI/CD conventions your application teams already use. It also means Pulumi programs run directly through Pulumi's own deployment engine against any cloud or SaaS platform, with no separate compile-to-template step in between, unlike CDK-style tools that transpile into another system's format before anything deploys. For an AI agent iterating on infrastructure, fewer steps between "write code" and "see the result" means a tighter feedback loop. [Pulumi Neo](/product/neo/), the platform's infrastructure agent, builds on this directly: it can propose Terraform-to-Pulumi migrations, run policy-checked previews, respond to failures, and open pull requests inside a team's existing review workflow.

For platform teams, Pulumi adds built-in guardrails that Terraform typically requires bolting on through third-party tooling: [policy as code](/what-is/what-is-policy-as-code/) for enforcing organizational rules before a deployment ships, a secrets and configuration management layer (ESC), human-in-the-loop approval gates, and reusable components that teams can publish and consume like any other internal library, in whatever language they use. The tradeoff is ecosystem maturity in the opposite direction from Terraform: Pulumi's provider catalog, while broad, has a shorter history than Terraform's for a handful of niche or long-tail providers, and some teams will need to weigh that against the language and workflow benefits.

At scale, Pulumi customers report concrete outcomes. BMW's Software Factory manages more than 20,000 cloud resources with Python-based infrastructure code for over 11,000 developers. Wiz manages more than a million cloud resources through Pulumi's Automation API and Kubernetes operator, pushing hundreds of thousands of daily infrastructure updates across hundreds of data centers. Supabase scaled from a single region to 16 regions and roughly 80,000 resources. Atlassian's Bitbucket team reported a 50% reduction in infrastructure maintenance time after adopting Pulumi.

## OpenTofu

[OpenTofu](/docs/iac/comparisons/terraform/opentofu/) is an open-source fork of Terraform, governed by the Linux Foundation rather than a single vendor. It emerged directly from HashiCorp's August 2023 license change: a group of Terraform users and vendors forked the last MPL-licensed Terraform release and committed to keeping the fork under a permissive open-source license going forward.

The practical pitch is continuity: OpenTofu aims to stay a close drop-in replacement for Terraform, using the same HCL syntax, the same provider ecosystem (most Terraform providers work unmodified), and largely the same workflow, so teams can migrate with minimal rewriting. OpenTofu's own FAQ notes the compatibility boundary directly: it works with state files created by Terraform up through the 1.5.x line, the last release before HashiCorp's license change.

Since forking, OpenTofu's maintainers have also shipped features HashiCorp hasn't, including state encryption, provider-defined functions, `for_each` on provider blocks, OCI registry support for providers and modules, and, in the [1.12 release from May 2026](https://opentofu.org/blog/opentofu-1-12-0/), dynamic `prevent_destroy` values. The project runs under the Linux Foundation and was accepted into the CNCF Sandbox in April 2025; its registry now lists more than 3,900 providers and 23,600 modules. It remains MPL-2.0 licensed.

The tradeoff is that OpenTofu inherits HCL's ceiling along with its familiarity. It solves the licensing and governance concern cleanly, but it doesn't address the testing, composability, or general-purpose-language advantages that come with moving to a platform like Pulumi or AWS CDK, and AI coding agents face the same reasoning gap with OpenTofu's HCL that they do with Terraform's.

## AWS CloudFormation

CloudFormation is AWS's native infrastructure-as-code service, using YAML or JSON templates that AWS itself parses, validates, and rolls back on failure. Because it's built and operated by AWS, it gets first access to new AWS service features, and its state is managed entirely by AWS rather than a separate backend your team has to configure and secure.

The obvious limit is scope: CloudFormation only provisions AWS resources, so any team running infrastructure across more than one cloud, or alongside Kubernetes and SaaS resources, will need a second tool for everything outside AWS. Authoring in raw YAML or JSON also means the same testing and abstraction limitations that HCL-based tools face, without even Terraform's ecosystem of community modules to offset it. Many AWS-focused teams increasingly write CloudFormation stacks through AWS CDK rather than by hand.

## AWS CDK

AWS CDK (Cloud Development Kit) lets you define AWS infrastructure using general-purpose languages including TypeScript, JavaScript, Python, Java, C#, and Go. Under the hood, CDK code compiles down to standard CloudFormation templates, which AWS then deploys the same way it deploys any other CloudFormation stack.

CDK gives AWS-only teams most of the general-purpose-language benefits that Pulumi offers: real loops, functions, tests, and packages, plus the IDE support that comes with a mainstream language. The compile step is the notable difference from a platform like Pulumi, which runs your program directly against cloud provider APIs: CDK synthesizes a CloudFormation template first, then hands that off, which adds a layer between what your code says and what gets deployed, and can slow the feedback loop an AI coding agent depends on when it's proposing and testing changes iteratively. CDK is also AWS-only, so it doesn't help teams who need one consistent authoring model across multiple clouds. AWS CDK is actively developed and unaffected by HashiCorp's decision to sunset its own, differently named, CDK for Terraform — see the next section.

## CDK for Terraform (CDKTF) is archived, not an alternative

CDK for Terraform used to appear on lists like this one as a way to write Terraform infrastructure in TypeScript, Python, Java, C#, or Go instead of HCL. That's no longer a live option. HashiCorp [archived the project on December 10, 2025](https://github.com/hashicorp/terraform-cdk), stating in its own sunset notice that CDKTF "did not find product-market fit at scale" and that it would "focus its investments on Terraform core and its broader ecosystem" instead. The GitHub repository is now read-only, and per HashiCorp's FAQ, "no further updates, fixes, or improvements (including compatibility updates) will be made."

CDKTF is MPL-licensed, so existing code keeps running and community forks are technically possible, but there's no maintainer, no security patching, and no provider compatibility work going forward. Teams currently on CDKTF have two realistic paths: move to native HCL with OpenTofu or Terraform, or move to a maintained general-purpose-language platform. Pulumi supports both directions — HCL directly, or Python, TypeScript, Go, C#, and Java for a full migration — and Pulumi's own [teardown of the sunset and what to do next](/blog/cdktf-is-deprecated-whats-next-for-your-team/) covers the migration paths in more depth than fits here.

One disambiguation worth stating plainly, since the two names are easy to confuse: AWS CDK and CDK for Terraform are different, unrelated projects that happened to share the "CDK" name and a general shape. AWS CDK targets CloudFormation, is maintained by AWS, and continues to ship regular releases. Only CDKTF, HashiCorp's Terraform-targeting CDK, is the one that's archived.

## Crossplane

Crossplane is a Kubernetes-native framework for infrastructure as code, letting platform teams define and provision cloud resources as Kubernetes custom resources, managed by controllers running inside a cluster. Rather than running a separate CLI-driven apply cycle, Crossplane treats the cluster's control plane as the single source of truth for both application and infrastructure state.

This model is a natural fit for teams already standardized on Kubernetes as their platform layer: infrastructure gets the same GitOps, RBAC, and reconciliation patterns as application workloads, and platform teams can build self-service abstractions (Crossplane calls these Compositions) that let application developers request infrastructure without learning Crossplane's own resource model directly. The tradeoff is that Crossplane assumes a Kubernetes-centric operating model; teams without an existing cluster-based platform will be adopting Kubernetes as a prerequisite, not just an infrastructure tool, and Crossplane's ecosystem of documented, named enterprise deployments is thinner than Terraform's or Pulumi's, making it harder to evaluate at-scale track record from public case studies alone.

## Azure Bicep

Bicep is Microsoft's domain-specific language for deploying Azure resources, designed as a cleaner authoring layer over Azure Resource Manager templates. Bicep code transpiles to ARM JSON, but with syntax that's considerably easier to read and write than hand-authored ARM. It's open source under the MIT license, and Microsoft's own documentation recommends it over raw ARM JSON for new Azure-only infrastructure work.

Like CloudFormation, Bicep's scope is a single cloud, in this case Azure exclusively, so it isn't a candidate for teams managing infrastructure across providers. It's also a DSL rather than a general-purpose language, which means the same testing and reuse ceiling as HCL, though for teams fully committed to Azure and nothing else, it remains a well-supported, low-friction choice.

## Ansible

Ansible is an agentless configuration management and automation tool that uses YAML playbooks to describe the desired state of servers, software, and application deployments. Red Hat, which acquired Ansible in 2015 and was itself acquired by IBM in 2019, maintains it today as part of Red Hat Ansible Automation Platform.

Ansible is often grouped with Terraform in "IaC tool" comparisons, but the two solve different problems and are frequently used together rather than as substitutes: Terraform or Pulumi provisions the resource, and Ansible then configures the operating system, installs software, and manages ongoing configuration state on top of it. Ansible does ship cloud provisioning modules and can create resources directly, but its design center is procedural configuration management, not declarative resource provisioning at the scale Terraform-class tools target. Teams evaluating Terraform alternatives for cloud provisioning specifically will usually want a tool from this list's other categories, with Ansible layered in afterward for day-two configuration.

## Terragrunt

Terragrunt is a thin orchestration wrapper maintained by Gruntwork that sits on top of Terraform or OpenTofu, rather than replacing either one. Its job is keeping multi-environment, multi-module HCL configurations DRY, and coordinating the order in which modules apply across a larger infrastructure codebase.

Terragrunt reached [1.0 in March 2026](https://www.gruntwork.io/blog/terragrunt-1-0-released), with the latest patch, 1.1.3, out in August 2026. The headline of 1.0 wasn't a new feature; it was a formal [backwards-compatibility guarantee](https://terragrunt.gruntwork.io/docs/process/1-0-guarantees) covering CLI flags, HCL config, and command output for the entire 1.x line, aimed at teams who'd been burned by breaking changes in earlier releases. Terragrunt Stacks, which let a single configuration generate multiple units, reached general availability earlier, in version 0.78. One detail worth knowing if you're choosing between forks: Terragrunt now shells out to `tofu` by default rather than `terraform`, reflecting where the community around it has settled; that's overridable via the `terraform_binary` option. It's still MIT licensed.

It's worth being precise about what Terragrunt is not: it doesn't introduce a new language, provider model, or state backend, and it doesn't address HCL's testing or abstraction limitations on its own. Teams considering Terragrunt aren't choosing a Terraform alternative; they're choosing a companion tool that makes Terraform or OpenTofu easier to operate at scale. If the underlying frustration is with HCL itself rather than with configuration sprawl, Terragrunt won't resolve it, and it's worth reading [what Terragrunt is and isn't](/what-is/what-is-terragrunt/) before assuming it solves a language problem.

## Comparison table

| Tool | Language | Cloud coverage | AI-agent readiness | Governance & policy | Best for |
|---|---|---|---|---|---|
| Pulumi | Python, TypeScript, JavaScript, Go, .NET, Java, YAML, HCL | 180+ providers, any cloud | High — real languages agents are trained on; Neo agent built in | Policy as code, ESC secrets, human-in-the-loop approvals | Teams standardizing on AI-native, multi-cloud engineering workflows |
| OpenTofu | HCL | Same provider ecosystem as Terraform | Same as Terraform — DSL limits agent reasoning | Linux Foundation / CNCF Sandbox; features like state encryption and dynamic `prevent_destroy` | Terraform users prioritizing open governance with minimal migration |
| AWS CloudFormation | YAML/JSON | AWS only | Low — templated config, no native testing | AWS-managed state and rollback | Teams fully committed to AWS wanting a fully managed native service |
| AWS CDK | TypeScript, Python, Java, C#, Go | AWS only (compiles to CloudFormation) | Medium — real languages, but a compile step slows feedback | Inherits CloudFormation governance | AWS-only teams wanting general-purpose languages |
| CDK for Terraform (CDKTF) | TypeScript, Python, Java, C#, Go | Archived Dec. 2025 — not a viable choice | N/A — no further updates of any kind | HashiCorp, unmaintained | Nothing new; existing users should plan a move |
| Crossplane | Kubernetes YAML/CRDs | Any cloud, via Kubernetes control plane | Medium — benefits from Kubernetes-native agent tooling | RBAC and GitOps via Kubernetes | Platform teams already standardized on Kubernetes |
| Azure Bicep | Bicep DSL (compiles to ARM) | Azure only | Low — DSL, no general-purpose tooling | Inherits Azure Resource Manager governance | Azure-only teams wanting a cleaner ARM authoring layer |
| Ansible | YAML playbooks | Any cloud, config-management focused | Low for provisioning; not its design center | Role-based playbooks, limited policy tooling | Day-two configuration management alongside an IaC tool |
| Terragrunt | HCL (wraps Terraform/OpenTofu) | Same as underlying Terraform/OpenTofu | Same as underlying Terraform/OpenTofu | Same as underlying Terraform/OpenTofu | Keeping large Terraform/OpenTofu codebases DRY, not a language alternative |

### Where each project stands in August 2026

| Project | Latest release | License | Governed by | Status |
|---|---|---|---|---|
| Terraform | 1.15.x | Business Source License | HashiCorp, an IBM Company | Actively developed |
| OpenTofu | 1.12 (May 2026) | MPL-2.0 | Linux Foundation; CNCF Sandbox | Actively developed |
| Terragrunt | 1.1.3 (Aug. 2026) | MIT | Gruntwork | Actively developed |
| CDK for Terraform (CDKTF) | Archived at sunset | MPL-2.0 | None — unmaintained | Archived Dec. 10, 2025 |
| Pulumi | Rolling releases; CLI 3.259.x | Apache 2.0 (SDKs/CLI) | Pulumi Corporation | Actively developed |

## How to choose

If your team is standardizing on a single cloud and wants the deepest, most tightly integrated tooling for it, the native option, CloudFormation for AWS or Bicep for Azure, is a reasonable default, especially for smaller platform teams that don't need cross-cloud abstraction. If you're on AWS specifically and want general-purpose languages without leaving the CloudFormation ecosystem, AWS CDK is the more capable choice, with the caveat that its compile-then-deploy step adds a layer between code and infrastructure.

If your team is already running Kubernetes as its platform layer and wants infrastructure provisioning to follow the same GitOps and RBAC model as application workloads, Crossplane is worth a serious look, understanding that it comes with Kubernetes as a hard dependency.

If you're deep in Terraform today, comfortable with HCL, and your primary concern is licensing and governance rather than language or workflow, OpenTofu is the lowest-friction path: same syntax, same providers, community governance instead of vendor governance.

If your team is investing in AI coding agents as part of its engineering workflow, wants multi-cloud reach without maintaining separate tools per provider, and values real testing, packaging, and code review practices for infrastructure the same way it does for application code, Pulumi is built specifically for that combination. It's also the most direct path for teams on the now-archived CDKTF who need an actively maintained general-purpose-language platform, and, for teams on Terraform who aren't ready to leave HCL, it's the only option here that lets you keep writing `.tf` files while gaining that platform underneath them.

## Frequently asked questions

### Is Terraform still free to use?

Yes, for most teams. Terraform's core CLI and the vast majority of its providers remain free under the Business Source License that HashiCorp adopted in August 2023. The license restricts a narrow set of commercial use cases, mainly building a competing managed offering on top of Terraform, which doesn't affect ordinary infrastructure teams using it internally.

### What is the best open-source Terraform alternative?

OpenTofu is the closest open-source alternative if you want to keep using HCL and the Terraform provider ecosystem, since it's a direct fork governed by the Linux Foundation. If open-source licensing matters but you're open to a different language, Pulumi's SDKs and CLI are open source (Apache 2.0), and Crossplane is a CNCF project for teams standardized on Kubernetes.

### Which IaC tool works best with AI coding agents?

Tools built on general-purpose languages give AI coding agents the strongest foundation, since those agents have far more training exposure to real Python, TypeScript, Go, C#, and Java than to any infrastructure-specific DSL. Pulumi and AWS CDK both fit this category; AWS CDK's compile step to CloudFormation adds a layer of indirection that Pulumi, which runs directly against provider APIs, doesn't have.

### Can I migrate from Terraform without rewriting everything?

It depends on which alternative you choose. Moving to OpenTofu requires essentially no rewriting, since it's HCL-compatible by design. Moving to Pulumi can be just as light-touch, since Pulumi Cloud works as a Terraform state backend and Pulumi IaC speaks HCL natively; teams that do want to move into a general-purpose language, or that are adopting AWS CDK or a similar platform, will need to translate configuration into program code, though tools like Pulumi's import and conversion tooling, and increasingly AI coding agents themselves, can automate a meaningful share of that translation rather than requiring a manual line-by-line rewrite.

### Is Pulumi a drop-in Terraform replacement?

It can be, if you want it to be. Pulumi Cloud now works as a [Terraform state backend](/docs/iac/get-started/terraform/terraform-state-backend/), so a team can point its existing Terraform or OpenTofu CLI at Pulumi Cloud and keep every `.tf` file exactly as written — no rewrite required. Pulumi also [supports HCL as a first-class language](/docs/iac/languages-sdks/hcl/) alongside Python, TypeScript, JavaScript, Go, .NET, Java, and YAML, so HCL modules can be authored and consumed natively inside Pulumi IaC.

For teams that do want to move off HCL entirely, that's also an option: Pulumi's general-purpose languages let infrastructure code get loops, functions, tests, and packages that HCL doesn't offer. Moving to that model means translating configuration into code rather than reusing files unchanged, though the underlying model carries over — state, providers, and resources map conceptually in similar ways — and Pulumi provides tooling to import existing Terraform-managed infrastructure and convert Terraform configuration into a starting Pulumi program, which teams typically use as a first draft rather than a finished migration.

### Does OpenTofu support everything Terraform does?

OpenTofu tracks Terraform's last open-source release closely and remains compatible with most existing Terraform configurations and providers. Since forking, its Linux Foundation-governed maintainers have also shipped features Terraform hadn't offered, such as state encryption, while newer HashiCorp-only Terraform features naturally won't appear in OpenTofu unless the community implements equivalents independently.

### Is CDK for Terraform (CDKTF) still supported?

No. HashiCorp archived CDKTF on December 10, 2025 and says in its own FAQ that "no further updates, fixes, or improvements (including compatibility updates) will be made." Existing CDKTF code keeps running since the license is MPL, but there's no maintainer behind it. Teams still on CDKTF should move to native HCL on Terraform or OpenTofu, or to a maintained general-purpose-language platform like Pulumi. This is a different project from AWS CDK, which is unaffected and actively developed.

### Is Terragrunt a Terraform alternative?

Not really. Terragrunt is an orchestration wrapper that sits on top of Terraform or OpenTofu to keep large, multi-environment HCL codebases DRY; it doesn't run infrastructure on its own, introduce a new provider model, or change what language you write in. Terragrunt reached 1.0 in March 2026 with a formal backwards-compatibility guarantee for its 1.x line, and now defaults to running OpenTofu's `tofu` binary rather than Terraform's. Teams pick Terragrunt to make Terraform or OpenTofu easier to operate at scale, not as a replacement for either.

For a broader roundup covering the full infrastructure-as-code category rather than Terraform alternatives specifically, see our guide to [the best IaC tools](/what-is/top-iac-tools/).

## Conclusion

Terraform remains a capable, widely used tool, and for teams with no appetite to change, OpenTofu offers a nearly friction-free path to the same workflow under different governance. The question worth asking for 2026 is whether your infrastructure tooling can keep pace with how your engineering organization actually builds software now, with AI coding agents as active participants rather than autocomplete. That question favors platforms built on real, general-purpose languages, tested and reviewed the same way application code is, over any tool, new or established, still built around a purpose-specific configuration syntax. Evaluate honestly against your own cloud footprint, existing platform investment, and how central AI-assisted development already is to your team, and the right alternative, or the right reason to stay put, becomes clear quickly.
