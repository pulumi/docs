---
title: "SST Runs on the Pulumi Engine: What It Means to Build on Pulumi"
date: 2026-09-16
draft: false
meta_desc: "SST v3 replaced AWS CDK with an embedded Pulumi engine and bridged Terraform providers. What that says about Pulumi as infrastructure other tools build on."
authors:
    - pulumi-content-team
tags:
    - serverless
    - infrastructure-as-code
    - aws
    - typescript
category: general
faq_schema: true
related_posts:
    - aws-cdk-vs-pulumi-why-sst-switched

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        SST v3 dropped AWS CDK for an engine most of its users never see: an embedded Pulumi engine, talking to Terraform-bridged providers, with no Pulumi account required.

        What that says about Pulumi as plumbing:
    linkedin: |
        When SST rebuilt its deployment engine for v3, it didn't write a new one. `sst deploy` now runs on an embedded Pulumi engine that calls Terraform-bridged providers to make the actual cloud API calls — no CDK, no CloudFormation, no Pulumi account or Pulumi Cloud dependency required.

        SST isn't alone in this. Nitric and Defang also run application deployments through the Pulumi engine rather than building their own diff, state, and provider layer from scratch.

        We wrote up what "built on the Pulumi engine" actually means mechanically, why a framework would rather embed an engine than write one, and where SST stands today (still shipping, team's public attention has broadened to include an AI coding agent called opencode).
    bluesky: |
        SST v3 replaced AWS CDK with an embedded Pulumi engine talking to Terraform-bridged providers — no Pulumi account needed.

        What that says about Pulumi as infrastructure other tools build on:
---

SST v3 (the framework's Ion-based rewrite) replaced AWS CDK and CloudFormation with an embedded Pulumi engine that calls Terraform-bridged providers to make the underlying cloud API calls. Running `sst deploy` needs no separate Pulumi install and no Pulumi account — the engine ships inside the SST CLI, with state kept in an S3 bucket in your own AWS account.

<!--more-->

That's what the SST team has said about their own architecture, repeatedly, since the rewrite shipped. This post covers what "built on the Pulumi engine" means mechanically, why a framework would choose to embed an engine instead of writing one, who else has made the same choice, and where SST stands as of this writing.

## What SST is

[SST](https://sst.dev/) is an open source TypeScript framework, from the team formerly known as Serverless Stack, for building and deploying full-stack applications to AWS and more than 150 other providers. You define your app's infrastructure and code together in a single `sst.config.ts` file, using SST's own components (functions, queues, buckets, static sites, and so on), and `sst deploy` handles the provisioning end to end.

Through 2023, SST's provisioning layer was built directly on AWS CDK and CloudFormation. In late 2023 the team began a rewrite, code-named Ion, that replaced that entire deployment layer. Ion shipped as SST v3 in mid-2024 and has been the only supported architecture since.

## What "built on the Pulumi engine" actually means

Here's how the SST team has described the mechanics, in their own words:

> "Ion is a code name for a new engine for deploying SST applications. The constructs (or components) are defined using Terraform providers and deployed using Pulumi; as opposed to CDK and CloudFormation (CFN)." — [SST, "Moving away from CDK"](https://sst.dev/blog/moving-away-from-cdk)

> "When you run `sst deploy`, those resources make a call to an embedded Pulumi engine that makes a call to their bridged Terraform provider, and this makes the AWS SDK calls to create your resources." — [SST, "Moving away from CDK"](https://sst.dev/blog/moving-away-from-cdk)

> "SST uses Pulumi behind the scenes for the providers and the deployment engine. And Terraform's providers are bridged through Pulumi." — [SST docs, "What is SST"](https://sst.dev/docs/)

That's confirmed outside SST's own writing, too. Independent developers who've compared SST, Terraform, and Pulumi directly describe the same architecture:

> "SST uses the Pulumi engine under the hood to manage and provision resources, and lets users write Pulumi code in addition to using SST's constructs, enabling resources with no associated SST constructs to still be defined and deployed." — [Gautier Blandin, "Terraform, Pulumi, SST: a tradeoff analysis"](https://www.gautierblandin.com/articles/terraform-pulumi-sst-tradeoff-analysis)

> "You may notice right away the imports from Pulumi. It means the whole deployment process will be built on Pulumi now." — [Kiryl Anoshka, "SST ditches AWS CDK. Time to move on to Ion"](https://dev.to/fively/sst-ditches-aws-cdk-time-to-move-on-to-ion-19pi)

The published `package.json` for SST's platform package backs this up directly: it depends on `@pulumi/pulumi`, plus first-party Pulumi providers for AWS, Cloudflare, Docker builds, and more, alongside a Pulumiverse Vercel provider.[^sst-package-json]

The chain, in practice:

| Step | Who's responsible |
| --- | --- |
| `sst deploy` reads your `sst.config.ts` and resolves SST's own components | SST |
| Components compile into Pulumi resource declarations | SST |
| The Pulumi engine diffs desired vs. actual state, builds a dependency graph, and orders operations | Pulumi engine |
| Terraform-bridged providers translate each resource into cloud API calls | [Pulumi's Terraform bridge](https://github.com/pulumi/pulumi-terraform-bridge) |
| State is written to an S3 bucket in your AWS account | SST (self-hosted, not Pulumi Cloud) |

SST owns the developer-facing layer: the CLI, the component model, the local dev loop. Pulumi's engine owns the provisioning mechanics underneath it: dependency resolution, preview and diff, state tracking, and the plumbing to hundreds of provider APIs.

## Why a framework would embed an engine instead of writing one

Writing a correct provisioning engine is a bigger project than it looks like from the outside. Diffing desired state against actual cloud state, ordering operations by dependency, retrying safely, and keeping consistent state across a deploy are all easy to get wrong and expensive to get right. Providers are the same problem multiplied by every service you want to support: AWS alone exposes hundreds of resource types, each with its own create, update, and delete semantics.

[Pulumi's Terraform bridge](https://github.com/pulumi/pulumi-terraform-bridge) is Apache-2.0 licensed and built specifically to let projects like SST reuse that provider surface — Terraform's ecosystem of providers, adapted for the Pulumi engine — instead of writing and maintaining their own. Pulumi's engine itself embeds the same way: it doesn't require a Pulumi account, a network call to Pulumi Cloud, or any Pulumi-hosted service to run. That's also how Pulumi's own [Automation API](/docs/iac/concepts/automation-api/) works for teams embedding Pulumi programs inside their own tools, and it's the same [provider bridge](/blog/any-terraform-provider/) that lets any Pulumi user consume [Terraform providers directly](/docs/iac/get-started/terraform/terraform-providers/).

For a framework like SST, that means getting a production-grade provisioning engine and hundreds of cloud providers without building either from scratch, while keeping full control of the parts developers actually interact with: the component model, the CLI, and the local dev experience.

## Who else builds on the engine

SST isn't the only project to make this choice.

- **[Nitric](https://nitric.io/)**, a cloud-agnostic application framework, states in its own docs that "all of the direct deployment providers use Pulumi under the hood for their deployments," with official Nitric providers built directly on Pulumi's AWS, GCP, and Azure providers.
- **[Defang](https://github.com/DefangLabs/pulumi-defang)**, which deploys Docker Compose applications to the cloud, describes its Pulumi provider as taking "a Compose file, translates it to a Pulumi program, and runs `pulumi up`" to provision the result.

Both, like SST, expose a narrower, more opinionated interface to their users while relying on the Pulumi engine and its provider bridge underneath.

## What this does not mean

A few things worth being precise about, since it's easy to overstate this kind of connection:

- **SST users are not Pulumi Cloud customers.** SST's state lives in your own S3 bucket, not in Pulumi's hosted service, and SST doesn't require a Pulumi account to work.
- **SST keeps its own abstractions and its own API.** Most SST users never write a line of Pulumi code; they work entirely in SST's component model.
- **You can drop down to raw Pulumi resources inside an SST app if you need to.** Because SST's constructs compile to Pulumi resources, resources that don't have a dedicated SST construct yet can still be defined directly in Pulumi and deployed as part of the same app.

## Where SST stands in 2026

SST continues to ship: the latest release, v4.17.1, went out in July 2026, and the `sst` package on npm is pulling roughly 796,000 downloads a week as of this writing.[^npm-downloads] The team's public attention has also broadened. SST's own team page credits the same team behind [opencode](https://opencode.ai/), an open source AI coding agent that has grown quickly since launch and now carries a larger following on GitHub than SST itself.[^opencode-stars]

That's a legitimate expansion of what the team works on, not a sign that SST is being abandoned — the releases and download numbers say otherwise. It's simply worth noting plainly: SST's day-to-day spotlight now shares space with a second product, and the framework's dependency on the Pulumi engine hasn't changed as a result.

## What this means if you're choosing infrastructure tooling

If you already run SST, you're already running Pulumi's engine, whether or not you've written a line of Pulumi code yourself. That's a reasonable place to stop — SST's abstractions are enough for a lot of teams and a lot of applications.

It's also worth knowing what's available if your needs grow past a single app: [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) for cross-team visibility into infrastructure state, [policy as code](/docs/iac/concepts/policy/) for guardrails your platform team can enforce centrally, and [components](/docs/iac/concepts/components/) for sharing infrastructure patterns across a whole organization rather than just within one SST app. None of that requires leaving the engine you're already using — it's the same one.

## Frequently asked questions

### Is SST built on Pulumi?

Yes. Since SST v3 (the Ion rewrite, shipped mid-2024), `sst deploy` runs through an embedded Pulumi engine that calls Terraform-bridged providers to make the underlying cloud API calls, replacing SST's earlier architecture on AWS CDK and CloudFormation.

### Does using SST require a Pulumi account?

No. Pulumi's engine is embedded directly in the SST CLI, and SST keeps its own state in an S3 bucket in your AWS account rather than in Pulumi Cloud. You don't need to install Pulumi separately or create a Pulumi account to deploy an SST app.

### Does SST use Terraform directly?

Not directly. SST's components are defined using Terraform providers, but those providers are bridged through the Pulumi engine rather than run through Terraform itself. SST doesn't invoke the Terraform CLI or write Terraform state.

### Can I use raw Pulumi resources inside an SST app?

Yes. Because SST's components compile into Pulumi resource declarations, you can define resources directly with Pulumi for anything that doesn't yet have a dedicated SST construct, and deploy them as part of the same app.

### Is SST still maintained?

Yes. SST shipped v4.17.1 in July 2026 and the `sst` package continues to see roughly 796,000 weekly downloads on npm. The team's public attention has broadened to include opencode, an open source AI coding agent, but that hasn't changed SST's release cadence or its dependency on the Pulumi engine.

### Should I use SST or Pulumi directly?

That depends on what you're building. SST is a strong fit if you want an opinionated, full-stack application framework with infrastructure and code defined together. Reaching for Pulumi directly makes more sense once you need capabilities SST doesn't expose on its own — cross-team visibility, policy enforcement, or infrastructure shared across more than one application — since that's the same engine SST already runs on.

## Where to go next

- [AWS CDK vs Pulumi: Why SST Chose Pulumi](/blog/aws-cdk-vs-pulumi-why-sst-switched/) — the fuller story of SST's move off CDK, told from SST's side
- [How Pulumi IaC Works](/docs/iac/guides/basics/how-pulumi-works/) — the engine mechanics referenced throughout this post
- [Introducing: Support For Using Any Terraform Provider with Pulumi](/blog/any-terraform-provider/) — the bridge SST and others build on
- [Automation API](/docs/iac/concepts/automation-api/) — how other tools embed Pulumi the same way SST does

[^sst-package-json]: [`platform/package.json`](https://github.com/anomalyco/sst/blob/dev/platform/package.json) in the `anomalyco/sst` repository (formerly `sst/sst`), verified September 2026: `@pulumi/pulumi`, `@pulumi/aws`, `@pulumi/cloudflare`, `@pulumi/command`, `@pulumi/docker-build`, `@pulumi/random`, `@pulumi/tls`, and `@pulumiverse/vercel` are listed as direct dependencies.
[^npm-downloads]: [npm download stats for `sst`](https://api.npmjs.org/downloads/point/last-week/sst), 796,291 downloads for the week of September 5-11, 2026.
[^opencode-stars]: [`anomalyco/opencode`](https://github.com/anomalyco/opencode) on GitHub, star count observed September 2026.
