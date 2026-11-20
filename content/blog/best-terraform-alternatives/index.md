---
title: "Best Terraform Alternatives in 2026"
date: 2026-07-18
updated: 2026-11-19
draft: false
meta_desc: "The best Terraform alternatives in 2026: Pulumi, OpenTofu, AWS CDK, Crossplane, Bicep, and Terragrunt compared on cloud reach and governance."
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
        Updated for November 2026: CDK for Terraform is archived, OpenTofu is at 1.13, and Pulumi runs your existing .tf files directly.

        We compared eight Terraform alternatives on multi-cloud reach, governance, and how well each works with an agent in the loop.
    linkedin: |
        Terraform remains a capable, widely used tool. But as AI coding agents become part of everyday infrastructure work, teams are re-evaluating what they need from their IaC platform.

        Agents reason best about code they were trained on: real, general-purpose languages with tests, functions, and packages, rather than a single proprietary DSL. That's prompting a fresh look at the Terraform-alternatives landscape.

        Since we first published this guide, HashiCorp archived CDK for Terraform, OpenTofu shipped 1.13, Crossplane graduated in the CNCF, and Pulumi shipped both native HCL support and a Terraform-compatible state backend, so authoring format and deployment engine no longer have to be the same decision.

        We lined up eight alternatives, from a community-governed HCL-compatible fork to Kubernetes-native frameworks to general-purpose-language platforms, against the same three questions: multi-cloud reach, governance, and agent-readiness.

        Which one wins depends on which of those three questions matters most to your team.
    bluesky: |
        Terraform alternatives in 2026 split into three camps: general-purpose-language platforms, HCL-compatible forks, and cloud-specific tools.

        Updated for November 2026: CDK for Terraform is archived, and Pulumi can run your .tf files directly or sit under your existing Terraform CLI as a state backend.
---

The strongest Terraform alternatives in 2026 fall into three groups: general-purpose-language platforms like Pulumi and AWS CDK, HCL-compatible forks like OpenTofu, and cloud-specific tools like AWS CloudFormation, Azure Bicep, and Crossplane. Which one fits depends less on syntax preference than on how well it lets your team, and your AI coding agents, read, test, and change infrastructure safely.

What's changed since this list was last useful: HashiCorp archived CDK for Terraform in December 2025 (a community fork, CDK Terrain, has since appeared), Crossplane graduated in the CNCF in October 2025, OpenTofu shipped 1.13 in September 2026, Terraform 1.17 made Terraform Policy generally available in October 2026, and Pulumi now runs the same HCL files Terraform does, so authoring format and deployment engine are separate decisions.

<!--more-->

## Why teams are re-evaluating Terraform in 2026

Terraform has been the default infrastructure-as-code tool for most of the last decade, and for good reason: a mature provider ecosystem, a large community, and a state model that most platform teams have learned to live with. But three forces are pushing teams to look again at what else is available.

The first is licensing. HashiCorp moved Terraform from the open-source Mozilla Public License to the Business Source License in August 2023, a shift that triggered the community fork now known as OpenTofu. HashiCorp itself became a wholly owned subsidiary of IBM when that acquisition closed in February 2025. Neither event breaks anything for existing Terraform users, but both changed how governance and long-term product direction get decided, and that's enough for some platform teams to want a documented Plan B. Packaging has moved too: HCP Terraform now sells free, Essentials, Standard, and Premium [plans](https://developer.hashicorp.com/terraform/cloud-docs/overview), and the free plan is limited by managed resources.

The second is the accumulated cost of working in a domain-specific language. HCL wasn't designed for the abstraction, composition, and testing patterns that platform engineering now expects: sharing logic across teams, writing meaningful unit tests, and building internal libraries that read like software rather than templated configuration. Terraform has closed some of this gap over time, adding a native test framework in version 1.6, but the ceiling on what a declarative DSL can express is still lower than what a general-purpose language offers.

The third, and the one reshaping the conversation fastest, is agentic AI. Coding agents like GitHub Copilot, Claude, and Pulumi's own Neo are now a standing part of how engineering teams write and review code, and infrastructure is not exempt. Public code in Python, TypeScript, Go, and Java, along with their testing and tooling ecosystems, far outweighs well-formed HCL. When an agent works in a language it already understands deeply, the propose, test, preview, and ship loop gets tighter; with a purpose-built DSL the loop lengthens and the output is less reliable. That doesn't disqualify Terraform, but it does mean "which IaC tool works best with AI agents" is now a first-class question when teams evaluate alternatives, alongside the perennial ones about multi-cloud reach and governance.

Terraform is not going away: it is actively developed (version 1.17 shipped in October 2026) and has a very large provider catalog. 2026 is still a reasonable moment to look honestly at what else exists and pick the tool that fits where your infrastructure and your engineering workflow are headed. For a broader look at how AI agents are changing infrastructure work generally, see [building for agentic infrastructure](/releases/agentic-infrastructure-era/). For a head-to-head look at Pulumi and Terraform specifically, see our [Pulumi vs. Terraform comparison](/docs/iac/comparisons/terraform/).

## Do you have to leave HCL behind?

No, and that's a meaningful change since this guide was last written. Authoring format and deployment engine used to be a single choice: pick Terraform, and HCL and the Terraform CLI came as a bundle. Two things Pulumi shipped as generally available in August 2026 split that bundle apart. Staying on HCL without adopting Pulumi is also a real option, and the [OpenTofu section](#opentofu) below covers that path.

The first is [Pulumi HCL](/docs/iac/languages-sdks/hcl/), which runs the same `.tf` files you'd write for Terraform or OpenTofu, unmodified, on Pulumi's engine. A project is a `Pulumi.yaml` with `runtime: hcl` and one or more `.tf` files, needs Pulumi CLI 3.256.0 or later, and resolves providers against the OpenTofu registry by default. The emulation has gaps: `backend`, `provider_meta`, `required_version`, and `experiments` blocks are accepted but ignored with a warning, a `cloud` block is an error, existing Terraform state files aren't read directly (bring resources over with `pulumi import --from hcl`), and provisioner `connection` blocks support SSH only.

The second is [Pulumi Cloud as a Terraform and OpenTofu state backend](/docs/integrations/terraform/state-backend/), which goes the other direction: keep the Terraform or OpenTofu CLI exactly as it is, and point its `backend "remote"` or `cloud` block at `tf.pulumi.com` for encrypted state storage, locking, update history, and resource search across Terraform-managed resources. It has limits: drift detection isn't available for Terraform-managed stacks (it requires a Pulumi program), migrating from HCP Terraform state is a manual export and push rather than an automatic switch, and update diffs are derived from state rather than a live `terraform plan`, so they're best-effort.

| If you want to keep... | Change this... |
|---|---|
| Your `.tf` files and HCL syntax | Nothing — run them on Pulumi's engine with `runtime: hcl` |
| Your Terraform or OpenTofu CLI and workflow | Only the backend, pointed at Pulumi Cloud |
| Neither, and want a general-purpose language | Everything — see the [Pulumi vs. Terraform comparison](/docs/iac/comparisons/terraform/) |

For the mechanics of each path, see [terraform-to-pulumi-cloud-hands-on](/blog/terraform-to-pulumi-cloud-hands-on/), [how Pulumi's engine models Terraform's data model](/blog/terraforms-data-model-on-pulumis-engine/), and [how Pulumi HCL is tested for OpenTofu compatibility](/blog/compatibility-testing-pulumi-hcl/).

## Pulumi

Pulumi is an infrastructure-as-code platform that lets you define cloud infrastructure in general-purpose languages, including Python, TypeScript, JavaScript, Go, .NET, and Java, plus YAML and HCL for teams that prefer a declarative format. Pulumi programs run directly against a deployment engine with hundreds of providers, covering AWS, Azure, Google Cloud, Kubernetes, and a long tail of SaaS and on-prem targets.

Teams with a large, working Terraform estate don't have to rewrite anything to adopt it: the [HCL and state backend paths above](#do-you-have-to-leave-hcl-behind) give you Pulumi Cloud's state management, access controls, and policy enforcement first, and you can migrate configuration into a general-purpose language on your own timeline.

Writing infrastructure in a real language means you get the tooling that comes with it for free: IDE autocomplete and type checking, unit and integration test frameworks, package managers for sharing reusable components, and the same code review and CI/CD conventions your application teams already use. There is no compile-to-template step, unlike CDK-style tools that transpile into another system's format before anything deploys, so an AI agent iterating on infrastructure gets a tighter feedback loop. [Pulumi Neo](/product/agents/), the platform's infrastructure agent, builds on this directly: it can propose Terraform-to-Pulumi migrations, run policy-checked previews, respond to failures, and open pull requests inside a team's existing review workflow.

For platform teams, Pulumi adds built-in guardrails: [policy as code](/topics/secrets-and-security/what-is-policy-as-code/) for enforcing organizational rules before a deployment ships, [Pulumi ESC](/docs/esc/) for secrets and configuration (composable environments, short-lived OIDC credentials for AWS, Azure, and Google Cloud, integrations with stores like HashiCorp Vault and 1Password, and `pulumi env run` to inject values into any command, including `terraform` and `tofu`), human-in-the-loop approval gates, and reusable components that teams can publish and consume like any other internal library, in whatever language they use. The tradeoff is ecosystem maturity in the opposite direction from Terraform: Pulumi's provider catalog, while broad, has a shorter history than Terraform's for a handful of niche or long-tail providers, and some teams will need to weigh that against the language and workflow benefits.

At scale, Pulumi customers report concrete outcomes. BMW's Software Factory manages more than 20,000 cloud resources with Python-based infrastructure code. Wiz manages more than a million cloud resources through Pulumi's Automation API and Kubernetes operator, pushing hundreds of thousands of daily infrastructure updates across hundreds of data centers. Supabase scaled from a single region to 16 regions and roughly 80,000 resources. Atlassian's Bitbucket team reported a 50% reduction in infrastructure maintenance time after adopting Pulumi.

## OpenTofu

[OpenTofu](/topics/infrastructure-as-code/opentofu-vs-terraform/) is an open-source fork of Terraform, governed by the Linux Foundation rather than a single vendor. It emerged directly from HashiCorp's August 2023 license change: a group of Terraform users and vendors forked the last MPL-licensed Terraform release and committed to keeping the fork under a permissive open-source license going forward.

The pitch is continuity: OpenTofu stays a close drop-in replacement for Terraform, with the same HCL syntax, the same providers (most work unmodified), and largely the same workflow. OpenTofu's own FAQ notes the compatibility boundary directly: it works with state files created by Terraform up through the 1.5.x line, the last release before HashiCorp's license change.

Since forking, OpenTofu's maintainers have also shipped features HashiCorp hasn't, including state encryption, provider-defined functions, `for_each` on provider blocks, OCI registry support for providers and modules, and, in the [1.12 release from May 2026](https://opentofu.org/blog/opentofu-1-12-0/), dynamic `prevent_destroy` values. The [1.13 release from September 2026](https://opentofu.org/blog/opentofu-1-13-0/) added Windows ARM64 builds and planning hint functions that reduce unknown values. The project runs under the Linux Foundation and was accepted into the CNCF Sandbox in April 2025; its [registry](https://search.opentofu.org/) lists 3,900+ providers and 23,600+ modules. It remains MPL-2.0 licensed.

The tradeoff is that OpenTofu inherits HCL's ceiling along with its familiarity. It solves the licensing and governance concern cleanly, but it doesn't address the testing, composability, or general-purpose-language advantages that come with moving to a platform like Pulumi or AWS CDK, and AI coding agents face the same reasoning gap with OpenTofu's HCL that they do with Terraform's.

## AWS CloudFormation

CloudFormation is AWS's native infrastructure-as-code service, using YAML or JSON templates that AWS itself parses, validates, and rolls back on failure. Because it's built and operated by AWS, it gets first access to new AWS service features, and its state is managed entirely by AWS rather than a separate backend your team has to configure and secure.

The obvious limit is scope: CloudFormation is built for AWS resources, and its third-party registry extensions cover only a small set of other services, so any team running infrastructure across more than one cloud, or alongside Kubernetes and SaaS resources, will need a second tool for most of what sits outside AWS. Raw YAML or JSON authoring has the same testing and abstraction limits as HCL, without Terraform's community modules. Many AWS-focused teams write CloudFormation through AWS CDK instead.

## AWS CDK

AWS CDK (Cloud Development Kit) lets you define AWS infrastructure using general-purpose languages including TypeScript, JavaScript, Python, Java, C#, and Go. Under the hood, CDK code compiles down to standard CloudFormation templates, which AWS then deploys the same way it deploys any other CloudFormation stack.

CDK gives AWS-only teams most of the general-purpose-language benefits that Pulumi offers: real loops, functions, tests, and packages, plus the IDE support that comes with a mainstream language. The compile step is the notable difference from a platform like Pulumi, which runs your program directly against cloud provider APIs: CDK synthesizes a CloudFormation template first, then hands that off, which adds a layer between what your code says and what gets deployed, and can slow the feedback loop an AI coding agent depends on when it's proposing and testing changes iteratively. CDK is also AWS-only, so it doesn't help teams who need one consistent authoring model across multiple clouds. AWS CDK is actively developed and unaffected by HashiCorp's decision to sunset its own, differently named, CDK for Terraform — see the next section.

## CDK for Terraform (CDKTF) is archived, not an alternative

CDK for Terraform used to appear on lists like this one as a way to write Terraform infrastructure in TypeScript, Python, Java, C#, or Go instead of HCL. That's no longer a live option. HashiCorp [archived the project on December 10, 2025](https://github.com/hashicorp/terraform-cdk), stating in its own sunset notice that CDKTF "did not find product-market fit at scale" and that it would "focus its investments on Terraform core and its broader ecosystem" instead. The GitHub repository is now read-only, and per HashiCorp's FAQ, "no further updates, fixes, or improvements (including compatibility updates) will be made."

CDKTF is MPL-licensed, so existing code keeps running, and a community-led fork, [CDK Terrain (CDKTN)](https://cdktn.io), now offers TypeScript and Python support on Terraform or OpenTofu. HashiCorp itself has no maintainer on the original, no security patching, and no provider compatibility work going forward, so evaluate the fork's governance and release record before depending on it. Teams currently on CDKTF have two realistic paths: move to native HCL with OpenTofu or Terraform, or move to a maintained general-purpose-language platform. Pulumi supports both directions — HCL directly, or Python, TypeScript, Go, C#, and Java for a full migration — and Pulumi's own [teardown of the sunset and what to do next](/blog/cdktf-is-deprecated-whats-next-for-your-team/) covers the migration paths in more depth than fits here.

The names are similar, but AWS CDK and CDK for Terraform are separate projects. HashiCorp built CDKTF with the AWS CDK team on the same construct model, generating Terraform configuration. AWS CDK targets CloudFormation, is maintained by AWS, and keeps shipping releases (2.277 in November 2026). Only CDKTF is archived.

## Crossplane

Crossplane is a Kubernetes-native framework for infrastructure as code, letting platform teams define and provision cloud resources as Kubernetes custom resources, managed by controllers running inside a cluster. Rather than running a separate CLI-driven apply cycle, Crossplane treats the cluster's control plane as the single source of truth for both application and infrastructure state.

This model is a natural fit for teams already standardized on Kubernetes as their platform layer: infrastructure gets the same GitOps, RBAC, and reconciliation patterns as application workloads, and platform teams can build self-service abstractions (Crossplane calls these Compositions) that let application developers request infrastructure without learning Crossplane's own resource model directly. Crossplane graduated in the CNCF on October 28, 2025, and the current 2.x line is Apache 2.0 licensed. Many of its cloud providers are generated from Terraform providers with the upjet tool, so Crossplane still leans on the Terraform provider ecosystem, and some of Upbound's official provider releases (backports, FIPS builds, and older versions) require a subscription. The tradeoff is that Crossplane assumes a Kubernetes-centric operating model; teams without an existing cluster-based platform will be adopting Kubernetes as a prerequisite, and Crossplane has fewer named public enterprise case studies than Terraform or Pulumi.

## Azure Bicep

Bicep is Microsoft's domain-specific language for deploying Azure resources, designed as a cleaner authoring layer over Azure Resource Manager templates. Bicep code transpiles to ARM JSON, but with syntax that's considerably easier to read and write than hand-authored ARM. It's open source under the MIT license, and Microsoft's own documentation recommends it over raw ARM JSON for new Azure-only infrastructure work.

Like CloudFormation, Bicep's scope is a single cloud, in this case Azure exclusively, so it isn't a candidate for teams managing infrastructure across providers. It's also a DSL rather than a general-purpose language, which means the same testing and reuse ceiling as HCL, though for teams fully committed to Azure and nothing else, it remains a well-supported, low-friction choice.

## Ansible

Ansible is an agentless configuration management and automation tool that uses YAML playbooks to describe the desired state of servers, software, and application deployments. Red Hat, which acquired Ansible in 2015 and was itself acquired by IBM in 2019, maintains it today as part of Red Hat Ansible Automation Platform.

Ansible is often grouped with Terraform in "IaC tool" comparisons, but the two solve different problems and are frequently used together rather than as substitutes: Terraform or Pulumi provisions the resource, and Ansible then configures the operating system, installs software, and manages ongoing configuration state on top of it. Ansible ships cloud provisioning modules, but its design center is procedural configuration management. Teams evaluating Terraform alternatives for provisioning will usually pick another tool here and layer Ansible in afterward for day-two configuration.

## Terragrunt

Terragrunt is a thin orchestration wrapper maintained by Gruntwork that sits on top of Terraform or OpenTofu, rather than replacing either one. Its job is keeping multi-environment, multi-module HCL configurations DRY, and coordinating the order in which modules apply across a larger infrastructure codebase.

Terragrunt reached [1.0 in March 2026](https://www.gruntwork.io/blog/terragrunt-1-0-released), with 1.2 in October 2026 and the latest patch, 1.2.2, out in November 2026. The headline of 1.0 was a formal [backwards-compatibility guarantee](https://docs.terragrunt.com/process/1-0-guarantees/) covering CLI flags, HCL config, and command output for the entire 1.x line, rather than any new functionality, aimed at teams who'd been burned by breaking changes in earlier releases. Terragrunt Stacks, which let a single configuration generate multiple units, reached general availability earlier, in version 0.78. One detail worth knowing if you're choosing between forks: Terragrunt now shells out to `tofu` by default rather than `terraform`, reflecting where the community around it has settled; that's overridable via the `terraform_binary` option. It's still MIT licensed.

Terragrunt adds no new language, provider model, or state backend, so it won't resolve frustration with HCL itself. See [what Terragrunt is and isn't](/topics/infrastructure-as-code/what-is-terragrunt/) before assuming it solves a language problem.

## Comparison table

| Tool | Language | Cloud coverage | AI-agent readiness | Governance & policy | Best for |
|---|---|---|---|---|---|
| Pulumi | Python, TypeScript, JavaScript, Go, .NET, Java, YAML, HCL | hundreds of providers, any cloud | High — real languages agents are trained on; Neo agent built in | Policy as code, ESC environments (secrets, OIDC credentials), human-in-the-loop approvals | Teams standardizing on AI-native, multi-cloud engineering workflows |
| OpenTofu | HCL | Same provider ecosystem as Terraform | Same as Terraform — DSL limits agent reasoning | Linux Foundation / CNCF Sandbox; features like state encryption and dynamic `prevent_destroy` | Terraform users prioritizing open governance with minimal migration |
| AWS CloudFormation | YAML/JSON | AWS only | Low — templated config, no native testing | AWS-managed state and rollback | Teams fully committed to AWS wanting a fully managed native service |
| AWS CDK | TypeScript, Python, Java, C#, Go | AWS only (compiles to CloudFormation) | Medium — real languages, but a compile step slows feedback | Inherits CloudFormation governance | AWS-only teams wanting general-purpose languages |
| CDK for Terraform (CDKTF) | TypeScript, Python, Java, C#, Go | Archived Dec. 2025 — not a viable choice | N/A — no further updates of any kind | HashiCorp, unmaintained | Nothing new; existing users should plan a move |
| Crossplane | Kubernetes YAML/CRDs | Any cloud, via Kubernetes control plane | Medium — benefits from Kubernetes-native agent tooling | CNCF Graduated; RBAC and GitOps via Kubernetes | Platform teams already standardized on Kubernetes |
| Azure Bicep | Bicep DSL (compiles to ARM) | Azure only | Low — DSL, no general-purpose tooling | Inherits Azure Resource Manager governance | Azure-only teams wanting a cleaner ARM authoring layer |
| Ansible | YAML playbooks | Any cloud, config-management focused | Low for provisioning; not its design center | Role-based playbooks, limited policy tooling | Day-two configuration management alongside an IaC tool |
| Terragrunt | HCL (wraps Terraform/OpenTofu) | Same as underlying Terraform/OpenTofu | Same as underlying Terraform/OpenTofu | Same as underlying Terraform/OpenTofu | Keeping large Terraform/OpenTofu codebases DRY, not a language alternative |

### Where each project stands in November 2026

| Project | Latest release | License | Governed by | Status |
|---|---|---|---|---|
| Terraform | 1.17.x (Oct. 2026) | Business Source License | HashiCorp, an IBM Company | Actively developed |
| OpenTofu | 1.13 (Sep. 2026) | MPL-2.0 | Linux Foundation; CNCF Sandbox | Actively developed |
| Terragrunt | 1.2.x (Nov. 2026) | MIT | Gruntwork | Actively developed |
| CDK for Terraform (CDKTF) | Archived at sunset | MPL-2.0 | None — unmaintained | Archived Dec. 10, 2025; community fork CDK Terrain |
| Crossplane | 2.4.x (Oct. 2026) | Apache 2.0 | CNCF | Graduated Oct. 2025 |
| Pulumi | Rolling releases; CLI 3.277.x | Apache 2.0 (SDKs/CLI) | Pulumi Corporation | Actively developed |

## How to choose

If your team is standardizing on a single cloud and wants the deepest, most tightly integrated tooling for it, the native option, CloudFormation for AWS or Bicep for Azure, is a reasonable default, especially for smaller platform teams that don't need cross-cloud abstraction. If you're on AWS specifically and want general-purpose languages without leaving the CloudFormation ecosystem, AWS CDK is the more capable choice, with the caveat that its compile-then-deploy step adds a layer between code and infrastructure.

If your team is already running Kubernetes as its platform layer and wants infrastructure provisioning to follow the same GitOps and RBAC model as application workloads, Crossplane is worth a serious look, understanding that it comes with Kubernetes as a hard dependency.

If you're deep in Terraform today, comfortable with HCL, and your primary concern is licensing and governance rather than language or workflow, OpenTofu is the lowest-friction path: same syntax, same providers, community governance instead of vendor governance.

If your team is investing in AI coding agents as part of its engineering workflow, wants multi-cloud reach without maintaining separate tools per provider, and values real testing, packaging, and code review practices for infrastructure the same way it does for application code, Pulumi is built specifically for that combination. It's also the most direct path for teams on the now-archived CDKTF who need an actively maintained general-purpose-language platform, and, for teams on Terraform who aren't ready to leave HCL, it's the only option here that lets you keep writing `.tf` files while gaining that platform underneath them.

## Frequently asked questions

### Is Terraform being replaced?

No. Terraform is actively developed: version 1.17 shipped in October 2026 and made Terraform Policy generally available, and HashiCorp is now part of IBM. What is changing is that teams add or choose alternatives for specific reasons: open governance (OpenTofu), general-purpose languages and AI coding agents (Pulumi), or a single cloud (CloudFormation, Bicep). Pulumi can also run existing `.tf` files, so trying an alternative does not require a rewrite.

### Is Terraform still free to use?

Yes, for most teams. Terraform's core CLI and the vast majority of its providers remain free under the Business Source License that HashiCorp adopted in August 2023. The license restricts a narrow set of commercial use cases, mainly building a competing managed offering on top of Terraform, which doesn't affect ordinary infrastructure teams using it internally. HCP Terraform, HashiCorp's hosted service, is separate and sold as free, Essentials, Standard, and Premium plans.

### What is the best open-source Terraform alternative?

OpenTofu is the closest open-source alternative if you want to keep using HCL and the Terraform provider ecosystem, since it's a direct fork governed by the Linux Foundation. If open-source licensing matters but you're open to a different language, Pulumi's SDKs and CLI are open source (Apache 2.0), and Crossplane is a CNCF project for teams standardized on Kubernetes.

### Which IaC tool works best with AI coding agents?

Tools built on general-purpose languages give AI coding agents the strongest foundation, since those agents have far more training exposure to real Python, TypeScript, Go, C#, and Java than to any infrastructure-specific DSL. Pulumi and AWS CDK both fit this category; AWS CDK's compile step to CloudFormation adds a layer of indirection that Pulumi, which runs directly against provider APIs, doesn't have.

### Can I migrate from Terraform without rewriting everything?

It depends on which alternative you choose. Moving to OpenTofu requires essentially no rewriting, since it's HCL-compatible by design. Moving to Pulumi can be just as light-touch, since Pulumi Cloud works as a Terraform state backend and Pulumi speaks HCL natively. Moving into a general-purpose language, or to AWS CDK, means translating configuration into program code, though import and conversion tooling and AI coding agents can automate much of that.

### Is Pulumi a drop-in Terraform replacement?

It can be, if you want it to be. Pulumi Cloud now works as a [Terraform state backend](/docs/integrations/terraform/state-backend/), so a team can point its existing Terraform or OpenTofu CLI at Pulumi Cloud and keep every `.tf` file exactly as written — no rewrite required. Pulumi also [supports HCL as a first-class language](/docs/iac/languages-sdks/hcl/) alongside Python, TypeScript, JavaScript, Go, .NET, Java, and YAML, so HCL modules can be authored and consumed natively inside Pulumi IaC.

Moving off HCL entirely means translating configuration into code, and Pulumi provides tooling to import existing Terraform-managed infrastructure and convert Terraform configuration into a starting program, which teams typically use as a first draft rather than a finished migration.

### Does OpenTofu support everything Terraform does?

OpenTofu tracks Terraform's last open-source release closely and remains compatible with most existing Terraform configurations and providers. Since forking, its Linux Foundation-governed maintainers have also shipped features Terraform hadn't offered, such as state encryption, while newer HashiCorp-only Terraform features naturally won't appear in OpenTofu unless the community implements equivalents independently.

### Is CDK for Terraform (CDKTF) still supported?

No. HashiCorp archived CDKTF on December 10, 2025 and says in its own FAQ that "no further updates, fixes, or improvements (including compatibility updates) will be made." Existing CDKTF code keeps running since the license is MPL, but there's no maintainer behind it. Teams still on CDKTF should move to native HCL on Terraform or OpenTofu, or to a maintained general-purpose-language platform like Pulumi. This is a different project from AWS CDK, which is unaffected and actively developed.

### Is Terragrunt a Terraform alternative?

Not really. Terragrunt is an orchestration wrapper that sits on top of Terraform or OpenTofu to keep large, multi-environment HCL codebases DRY; it doesn't run infrastructure on its own, introduce a new provider model, or change what language you write in. See the [Terragrunt section](#terragrunt) above for its 1.0 release and current defaults. Teams pick Terragrunt to operate Terraform or OpenTofu at scale; it complements both.

For a broader roundup covering the full infrastructure-as-code category rather than Terraform alternatives specifically, see our guide to [the best IaC tools](/blog/infrastructure-as-code-tools/).

## Conclusion

Terraform remains a capable, widely used tool, and for teams with no appetite to change, OpenTofu offers a nearly friction-free path to the same workflow under different governance. The question worth asking for 2026 is whether your infrastructure tooling can keep pace with how your engineering organization actually builds software now, with AI coding agents as active participants rather than autocomplete. That question favors platforms built on real, general-purpose languages, tested and reviewed the same way application code is, over any tool, new or established, still built around a purpose-specific configuration syntax. Evaluate against your own cloud footprint, existing platform investment, and how central AI-assisted development is to your team, and the right alternative, or the right reason to stay put, becomes clear quickly.
