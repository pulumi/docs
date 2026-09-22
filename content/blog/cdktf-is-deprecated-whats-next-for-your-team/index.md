---
title: "CDKTF is deprecated: What's next for your team?"
date: 2025-12-18T10:00:00-08:00
updated: 2026-09-22
draft: false
meta_desc: "CDKTF was archived December 10, 2025. Your options in 2026: HCL on Terraform or OpenTofu, AWS CDK, the CDK Terrain fork, or migrating to Pulumi."
authors:
  - adam-gordon-bell
  - christian-nunciato
tags:
  - migration
  - terraform
  - cdktf
category: best-practices
faq_schema: true
---

CDK for Terraform (CDKTF) was deprecated and archived on December 10, 2025, and HashiCorp has stopped maintaining it. Teams that built on it now have four paths forward: export to HCL and run it on Terraform or OpenTofu, migrate to AWS CDK, move to the community fork CDK Terrain, or migrate to Pulumi.

That's a decision a lot of teams are having to make. This post walks through all four options, including their tradeoffs, and shows what it looks like to migrate a CDKTF project to Pulumi in practice.

## What are the alternatives to CDKTF in 2026?

Here's how the four options compare at a glance:

| Option | What you keep | What you give up | Best for |
|---|---|---|---|
| Export to HCL, run on Terraform or OpenTofu | Terraform's module and provider ecosystem, current state format | A general-purpose programming language | Teams willing to write HCL directly |
| Migrate to AWS CDK | A programming language | Multi-cloud support; requires a ground-up rewrite | AWS-only teams already comfortable with CDK |
| Move to CDK Terrain | Your existing constructs, TypeScript or Python code, multi-cloud support | A vendor-backed, well-resourced upstream | Teams that want the lowest-diff move off CDKTF |
| Migrate to Pulumi | A programming language, multi-cloud support, built-in convert and import tooling | The synth-then-apply step CDKTF required | Teams that want to keep writing real code, with an actively developed platform behind it |

### Option 1: Export to HCL and run it on Terraform or OpenTofu

HashiCorp's official recommendation is to export your projects to HashiCorp Configuration Language (HCL) and manage them with Terraform going forward. CDKTF has a command that makes this fairly simple:

```bash
cdktf synth --hcl
```

As HashiCorp puts it in [the project's FAQ](https://github.com/hashicorp/terraform-cdk): "If you are not using AWS CDK, we highly recommend migrating to standard Terraform and HCL for long-term support and ecosystem alignment."

You don't have to stay on Terraform itself to take this path. [OpenTofu](/docs/iac/comparisons/opentofu/), the open-source fork now stewarded by the Linux Foundation, is broadly compatible with Terraform's HCL, providers, and modules, and it's continued to ship on its own schedule — the latest stable release, 1.12.6, landed in August 2026 with capabilities like state encryption, early variable evaluation, and OCI registry support that arrived on OpenTofu before Terraform. Either way, you're still writing HCL.

Some teams managing many Terraform or OpenTofu configurations also reach for [Terragrunt](https://terragrunt.gruntwork.io/) to keep them DRY. Terragrunt hit its 1.0 milestone in early 2026 with an explicit backwards-compatibility guarantee and stabilized support for defining multiple environments as "Stacks" from a single configuration. It's a genuinely useful orchestration layer, but it sits on top of the `terraform` or `tofu` CLI rather than replacing it, so it changes how your HCL is organized, not what language you write it in.

Of course, if you're using CDKTF, you probably chose it specifically to avoid HCL in the first place. Terraform, OpenTofu, and Terragrunt on top of either one, are all still HCL under the hood, so this path is worth considering mainly for teams willing to make that tradeoff.

### Option 2: Migrate to AWS CDK

If your team is all-in on AWS, another option would be to migrate to AWS CDK. It's widely used, officially supported, the programming model is similar to CDKTF's, and both CDK and CDKTF transpile to an intermediate format (CloudFormation YAML and Terraform JSON, respectively) that gets passed on to their underlying tools for deployment.

But while their programming and deployment models are conceptually similar, their resource models and APIs are entirely different. Here's the code for an S3 bucket written in AWS CDK, for example:

```typescript
import * as s3 from 'aws-cdk-lib/aws-s3';

const bucket = new s3.Bucket(this, 'my-bucket', {
    bucketName: 'my-example-bucket',
    versioned: true,
    publicReadAccess: false,
});
```

And here's the code for a similarly configured bucket in CDKTF:

```typescript
import { S3Bucket } from '@cdktf/provider-aws/lib/s3-bucket';

const bucket = new S3Bucket(this, 'my-bucket', {
    bucket: 'my-example-bucket',
    tags: {
        Environment: 'dev',
    },
});
```

Notice how different these APIs are — and this is just one simple resource with only a few properties; imagine having to rewrite dozens or hundreds of them. Beyond that, there's also the problem of state: How would you go about translating the contents of a Terraform state file containing hundreds of resources into the equivalent CloudFormation YAML or JSON?

Despite their surface similarities, CDKTF and AWS CDK have little in common. Migration would essentially mean a ground-up rewrite that'd also leave you without the multi-cloud support you already have with CDKTF. For most teams, that makes this option a practical non-starter.

### Option 3: Move to the community fork, CDK Terrain

A newer option didn't exist when CDKTF was first deprecated: [CDK Terrain](https://cdktn.io/) (CDKTN), a community-led fork of CDKTF maintained under the [Open Construct Foundation](https://github.com/open-constructs). It lets you keep writing infrastructure in TypeScript or Python, keep your existing constructs largely intact, and run the result against either Terraform or OpenTofu. It's picked up enough traction to land on the ThoughtWorks Technology Radar, and it's the lowest-diff path off CDKTF of any option here, since much of your existing code carries over directly.

The tradeoff is what you're giving up along with HashiCorp: CDK Terrain is run by its community rather than a vendor with dedicated engineering resources, so its long-term pace and support are still being established. It also inherits CDKTF's underlying execution model — your code still synthesizes to HCL or JSON before anything gets applied, rather than deploying directly the way CDKTF's own docs described as one of its slower points. If you want to keep exactly the authoring experience CDKTF gave you and are comfortable betting on a young, community-run project, it's worth a serious look.

### Option 4: Migrate to Pulumi

This is where we should acknowledge our obvious bias — but we genuinely believe that for most users of CDKTF, Pulumi really is the simplest and most broadly compatible alternative.

Like CDKTF, Pulumi lets you build and manage your infrastructure with general-purpose languages like TypeScript, JavaScript, Python, Go, .NET, and Java, plus YAML and HCL, and it supports organizing your code into higher-level abstractions called [_components_](/docs/iac/concepts/components/), which you can think of like CDKTF constructs. Both organize cloud resources into [_stacks_](/docs/iac/concepts/stacks/) (think `dev`, `prod`), and both track [deployment state](/docs/iac/concepts/state-and-backends/) similarly, with local, remote, and cloud-hosted options available.

Many of Pulumi's most popular [providers](/docs/iac/concepts/providers/) (e.g., the AWS provider) are also built from open-source Terraform schemas, which means their resource models will be nearly identical to what you're used to with CDKTF. Here's what the same S3 bucket looks like in Pulumi, for example:

```typescript
import * as aws from '@pulumi/aws';

const bucket = new aws.s3.Bucket('my-bucket', {
    bucket: 'my-example-bucket',
    tags: {
        Environment: 'dev',
    },
});
```

You can also use [any Terraform provider](/docs/iac/get-started/terraform/terraform-providers/) with Pulumi, and you can even [reference Terraform modules directly](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#using-terraform-modules-directly) from within your Pulumi code.

Pulumi is also different from CDKTF in several ways. One is that rather than transpile your source code to a format like JSON as CDKTF does (and then deploying it separately later), Pulumi uses its own declarative deployment engine that resolves the resource graph at runtime and provisions cloud resources directly, which is much faster and more flexible. You can learn more about the deployment model in [How Pulumi Works](/docs/iac/guides/basics/how-pulumi-works/).

If you want a smaller first step, [Pulumi HCL](/docs/iac/languages-sdks/hcl/) can run the `.tf` files that `cdktf synth --hcl` produces directly, on Pulumi's engine, without a rewrite. It's a bridge rather than a destination: a way to land your exported HCL on Pulumi's state management and deployment engine now, and move any of it into TypeScript, Python, or another supported language later, on your own schedule.

Given the API similarities, the support for all Terraform providers and modules, the ability to [coexist](/docs/iac/guides/migration/#coexistence) alongside Terraform-managed projects, and the built-in support for conversion (which we'll cover next), we think Pulumi is the best alternative for most teams looking to migrate.

{{< blog/cta-card title="Migrate from CDKTF to Pulumi" href="/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/" >}}
Keep writing infrastructure in TypeScript, JavaScript, Python, Go, .NET, or Java, plus YAML and HCL, and use Pulumi's built-in convert and import commands to bring your CDKTF projects and state across.
{{< /blog/cta-card >}}

## What migrating to Pulumi looks like

Migrating a CDKTF project to Pulumi generally happens in three steps:

1. **Conversion**, which translates your CDKTF code into a new Pulumi program
2. **Import**, which reads the contents of your CDKTF state into a new Pulumi stack
3. **Refactoring**, which brings the code in the new program into alignment with the stack's currently deployed resources

### Conversion and import

Migration starts with exporting your CDKTF project to HCL with `cdktf synth`. From there, Pulumi's built-in [`convert`](/docs/iac/cli/commands/pulumi_convert/) and [`import`](/docs/iac/cli/commands/pulumi_import/) commands handle creating the new program and importing your state:

```bash
# Export your project to HCL.
cdktf synth --hcl

# Convert the HCL into a new Pulumi project.
pulumi convert --from terraform --language typescript

# Create a new Pulumi stack.
pulumi stack init dev

# Import your CDKTF stack's resources into your new Pulumi stack.
pulumi import --from terraform ./terraform.dev.tfstate
```

The converter automatically translates Terraform input variables, data sources, resources, and outputs into their Pulumi equivalents. You can read more about how this works in [Converting Terraform HCL to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi).

### Refactoring

Once you've imported your state, you'll often have to make some adjustments to the code to bring it in line with the new Pulumi stack. For instance, `pulumi import` marks new resources [protected](/docs/iac/concepts/resources/options/protect/) by default, to prevent them from being accidentally deleted — but since the code produced by `pulumi convert` doesn't include the `protect` resource option, you'll need to add it yourself. Fortunately the import step also emits code that you can copy into your program to make this process a little easier.

Refactoring can get a bit more complicated when custom logic and higher-level abstractions are involved, as fidelity to the original CDKTF code is often lost in the translation to HCL. In these situations, having the help of an LLM to recapture that original logic or translate your CDKTF constructs into Pulumi components can be a big time-saver, and Pulumi's own AI agent, [Neo](/product/neo/), can carry out much of this refactoring work directly inside your existing workflow.

## An end-to-end example

The best way to get a feel for how this works, though, is to try it yourself.

The [pulumi/cdktf-to-pulumi-example](https://github.com/pulumi/cdktf-to-pulumi-example) repository on GitHub contains a CDKTF project with multiple stacks written in TypeScript, along with a guide that walks you through the process of migrating that project to Pulumi. The guide covers everything we've discussed here so far, including:

* Converting the CDKTF project into a new Pulumi project
* Importing its actively running resources into Pulumi stacks
* Modifying the generated code to align with imported state
* Performing an initial deployment with Pulumi to complete the migration process

The walkthrough takes only a few minutes to complete, and it's a great way to stand up an example of your own to get more familiar with Pulumi.

{{< github-card repo="pulumi/cdktf-to-pulumi-example" >}}

## Frequently asked questions

### When was CDKTF deprecated?

CDKTF was deprecated and its repository archived on December 10, 2025, a little over five years after HashiCorp first introduced it in 2020. HashiCorp and IBM have stopped maintaining the project, no further releases are planned, and the GitHub organization behind it has been archived alongside the code.

### Can I keep using CDKTF now that it's archived?

Yes, in the short term. Existing CDKTF projects will keep working, since Terraform itself hasn't changed. But you won't get bug fixes, security patches, or compatibility updates for new provider or Terraform versions, so most teams should plan a move within the next year or two.

### Is there a maintained fork of CDKTF?

Yes. [CDK Terrain](https://cdktn.io/) (CDKTN) is a community-led fork of CDKTF, maintained under the Open Construct Foundation, that lets you keep writing infrastructure in TypeScript or Python and run it against Terraform or OpenTofu. It's the closest option to staying exactly where you are, though it's run by the community rather than a commercial vendor.

### Do OpenTofu or Terragrunt replace CDKTF?

Not directly. OpenTofu is a fork of Terraform, and Terragrunt is an orchestration layer on top of Terraform or OpenTofu; both are still built around HCL rather than a general-purpose programming language. If the reason you chose CDKTF was to write real code instead of HCL, neither one gets you back to that model on its own.

### Can I use Python instead of TypeScript after leaving CDKTF?

Yes, with either CDK Terrain or Pulumi. CDK Terrain supports TypeScript and Python, and Pulumi supports both of those plus JavaScript, Go, .NET, and Java, so a move to either one doesn't require standardizing your whole team on a single language.

### Do I have to rewrite my infrastructure to migrate off CDKTF?

Not with Pulumi. Pulumi's `convert` and `import` commands translate your exported CDKTF code and state directly into a new Pulumi program and stack, so most teams start from a working baseline and refactor from there rather than rewriting from scratch.

## What's next?

If you're moving on from CDKTF and looking for an alternative, there are a few possible paths forward. For teams that want to keep using real languages and avoid a ground-up rewrite, Pulumi offers the clearest way forward.

To learn more about how Pulumi works, how it differs from CDKTF and from Terraform, how to handle additional conversion scenarios, and more, we recommend:

* Diving into [the Pulumi docs](/docs/iac/concepts/) to get familiar with core concepts and features of the platform
* Reading [Migrating from Terraform or CDKTF to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) for more detailed, Terraform-specific migration guidance
* Comparing [Pulumi and CDKTF](/docs/iac/comparisons/cdktf/) side by side for a feature-by-feature look at the two platforms
* Comparing [Pulumi and Terraform](/docs/iac/comparisons/terraform/) if you want a deeper look at how the two platforms differ beyond CDKTF specifically
* Reading [Pulumi vs. the best Terraform alternatives](/blog/best-terraform-alternatives/) for a wider look at how Pulumi, OpenTofu, and other tools compare across the broader Terraform ecosystem
* Joining us in the [Pulumi Community Slack](https://slack.pulumi.com/) to ask questions and learn from others who've successfully made the leap from Terraform and CDKTF to Pulumi
* Checking out [Pulumi for All Your IaC — Including Terraform and HCL](/blog/all-iac-including-terraform-and-hcl/) to learn more about Pulumi's native support for Terraform and HCL

And of course, [feel free to reach out](/contact/)! We'd love to help in any way we can.
