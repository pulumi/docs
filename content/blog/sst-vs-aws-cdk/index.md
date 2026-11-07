---
title: "SST vs. AWS CDK: Which Should You Use?"
date: 2026-10-09
updated: 2026-10-09
draft: false
meta_desc: "SST vs. AWS CDK compared: what each tool is, how SST relates to Pulumi, a side-by-side table, and when to choose each for your AWS project."
authors:
    - pulumi-content-team
tags:
    - aws
    - aws-cdk
    - serverless
    - sst
    - infrastructure-as-code
category: general
faq_schema: true
social:
    twitter: |
        SST vs. AWS CDK: which should you use? A side-by-side comparison of abstraction level, state, local dev loop, rollback, and where SST's engine sits on Pulumi.
    linkedin: |
        Choosing between SST and AWS CDK for an AWS project? This guide compares what each tool is, how SST v3+ relates to Pulumi, and when to pick each, with a table and FAQ.
    bluesky: |
        SST vs. AWS CDK: which should you use? Table, decision criteria, and FAQ.
---

SST is a full-stack application framework that deploys serverless-first apps to your own cloud account, while AWS CDK is an AWS-only infrastructure as code library that synthesizes CloudFormation templates. Choose SST for opinionated app delivery with live Lambda development. Choose AWS CDK when you need CloudFormation semantics, AWS-native support, and the broadest AWS service coverage.

<!--more-->

This guide compares the two tools as of October 2026 so you can pick one for a new project. It covers what each tool does, how SST's runtime relates to Pulumi, a side-by-side table, and decision criteria. For the story of why the SST team replaced CDK in their own engine, read [why SST switched from AWS CDK to Pulumi](/blog/aws-cdk-vs-pulumi-why-sst-switched/).

## SST overview

SST is an open source (MIT licensed) framework for building full-stack applications on your own infrastructure. You define the whole app in a single `sst.config.ts` file using high-level components such as `sst.aws.Nextjs`, `sst.aws.Function`, `sst.aws.Bucket`, and `sst.aws.Postgres`. The [SST documentation](https://sst.dev/docs/) describes it as a way to define databases, buckets, queues, and frontends in code and deploy them with one command.

Key characteristics:

- **App-level abstractions.** Components bundle the underlying resources, such as a CDN, a Lambda function, and an S3 bucket for a Next.js site.
- **Live development.** `sst dev` starts a multiplexer that deploys infrastructure changes and runs Lambda functions live against your local code, so you can test without redeploying each edit.
- **Optional Console.** The SST Console adds logs, issues, and deploy automation for apps deployed to AWS, with a free tier.
- **Provider breadth.** SST supports 150+ Pulumi and Terraform providers, so an app can include Cloudflare, Stripe, or Vercel resources next to AWS ones.

## AWS CDK overview

The AWS Cloud Development Kit (CDK) is an open source (Apache-2.0) framework for defining AWS infrastructure in TypeScript, JavaScript, Python, Java, C#, or Go. CDK code synthesizes to CloudFormation templates, and CloudFormation performs the deployment. The [AWS CDK developer guide](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is the authoritative reference.

Key characteristics:

- **Construct levels.** L1 constructs map one to one to CloudFormation resources, L2 constructs add sensible defaults and helper methods, and L3 patterns combine several resources.
- **CloudFormation underneath.** State lives in CloudFormation stacks. Failed updates roll back automatically, and stacks show up in the AWS console and CloudTrail.
- **AWS first.** CDK is built and supported by AWS and tracks new AWS services closely. It targets AWS only.
- **Broad ecosystem.** Teams extend it with Construct Hub libraries, aspects, and community tools such as cdk-nag for compliance checks.

## How SST relates to Pulumi

SST v2 was built on AWS CDK. SST v3 (originally codenamed Ion) replaced that foundation with an engine built on Pulumi, and the current major line is v4. In SST's own words, its providers come from the Pulumi and Terraform ecosystems.

In practice this means:

1. SST embeds the Pulumi deployment engine and uses Pulumi providers, including providers bridged from Terraform.
2. Most SST users write `sst.config.ts` and SST components. They do not write Pulumi programs directly, and they do not need Pulumi knowledge to ship an app.
3. When a component does not expose a setting, SST lets you use `transform` options or add any Pulumi provider resource to the same config.
4. SST runs its own CLI and state handling. It is a separate product from Pulumi IaC and Pulumi Cloud, with its own configuration model.

SST's [state documentation](https://sst.dev/docs/state/) explains that the state file is generated locally and backed up to a bucket in the cloud account you choose as the app's `home` (`aws` or `cloudflare`), with an encryption passphrase stored in an SSM parameter.

## SST vs. AWS CDK comparison table

| Dimension | SST | AWS CDK |
| --- | --- | --- |
| What it is | Full-stack app framework | Infrastructure library for AWS |
| Abstraction level | App components (Next.js site, Function, Postgres) | L1, L2, and L3 constructs over CloudFormation |
| Languages | TypeScript config; function code in several runtimes | TypeScript, JavaScript, Python, Java, C#, Go |
| Clouds and providers | AWS and Cloudflare built in; 150+ Pulumi and Terraform providers | AWS only |
| Deployment engine | Embedded Pulumi engine with bridged Terraform providers | AWS CloudFormation |
| State location | Bucket in your account (`home` setting) | CloudFormation stacks managed by AWS |
| Local dev loop | `sst dev` with live Lambda | `cdk watch` and hotswap deployments; `sam local` for Lambda |
| Rollback behavior | No CloudFormation-style automatic rollback; fix forward by redeploying | CloudFormation rolls back failed stack updates |
| Governance and policy | Bring your own checks; no built-in policy engine | CloudFormation Guard and Hooks, Aspects, community cdk-nag |
| Maintainer and license | SST open source project, MIT | AWS, Apache-2.0 |
| Ecosystem and maturity | Younger, focused on web apps and serverless | Mature, large AWS-backed community |
| Best fit | Product teams shipping web apps fast | Teams standardized on AWS and CloudFormation |

## Choose SST if

Pick SST when most of these describe your project:

- You are building a web or serverless application, such as a Next.js, Remix, Astro, or API backed by Lambda.
- You want one config file and high-level components instead of assembling resources yourself.
- Fast feedback matters, and live Lambda development would save you deploy cycles.
- You want to mix in non-AWS services, such as Cloudflare or Stripe, in the same app definition.
- A small team owns both application code and infrastructure.

## Choose AWS CDK if

Pick AWS CDK when most of these describe your project:

- Your organization is committed to AWS and wants CloudFormation as the deployment system of record.
- You need automatic rollback, CloudFormation drift detection, or integration with AWS-native governance such as Service Catalog and CloudFormation Hooks.
- You build lower-level or non-serverless infrastructure like VPCs, EKS clusters, and data platforms, where broad service coverage matters.
- Your teams want to write infrastructure in Python, Java, C#, or Go.
- You want vendor-supported tooling with a long track record.

## If neither fits

Platform teams that manage many clouds, need policy as code, or want shared components across languages often look at a general-purpose infrastructure as code platform. [Pulumi](/docs/iac/) offers the same real-language approach as CDK across AWS, Azure, Google Cloud, Kubernetes, and 180+ providers. See the [Pulumi vs. AWS CDK comparison](/docs/iac/comparisons/aws-cdk/) and the [Pulumi vs. Serverless Framework comparison](/docs/iac/comparisons/serverless/) for detail.

## Frequently asked questions

### Is SST built on AWS CDK?

SST v2 was built on AWS CDK. SST v3 and later (v4 is current) no longer use CDK. They run on an engine built on Pulumi and use Pulumi and Terraform providers.

### Is SST built on Pulumi?

SST v3 and later embed the Pulumi deployment engine and use Pulumi providers, including providers bridged from Terraform. SST is a separate open source project with its own CLI, components, and state handling, so using it does not require a Pulumi account.

### Do I need to know Pulumi to use SST?

No. Most SST apps use only `sst.config.ts` and SST components. Pulumi knowledge helps when you drop below the component layer, for example to add a provider resource or use `transform` options.

### Can I migrate from SST v2 to v3 or later?

Yes, but plan it as a migration rather than an upgrade. The underlying engine changed from CDK and CloudFormation to Pulumi, so stacks and resource definitions need to be rewritten and existing resources reconciled. The v2 documentation remains available at v2.sst.dev, and the current SST docs cover the v3+ model.

### Can SST deploy to clouds other than AWS?

Yes. SST supports Cloudflare as a built-in home and component provider, and it can use 150+ Pulumi and Terraform providers. AWS has the deepest set of high-level components.

### Can I use CDK constructs in SST?

Not directly in v3 and later, because the engine no longer synthesizes CloudFormation. Use SST components or Pulumi and Terraform providers instead. SST v2 did support CDK constructs.

### Is SST free?

The SST framework is MIT licensed and free to use. You pay your cloud provider for the resources you deploy. The optional SST Console has a free tier.

### Which is better for Next.js on AWS?

SST is built for this case. A single `sst.aws.Nextjs` component provisions the site, CDN, and functions, and `sst dev` gives a fast loop. AWS CDK can host Next.js too, but you assemble the hosting resources yourself or adopt a community construct.

### Is AWS CDK multi-cloud?

No. AWS CDK targets AWS through CloudFormation. Pulumi, Terraform, and similar tools cover multi-cloud.

## Conclusion

SST and AWS CDK solve different problems. SST packages application-level components and a fast dev loop on top of a Pulumi-based engine, which suits product teams building web apps and serverless backends. AWS CDK gives AWS-focused teams CloudFormation guarantees, rollback, and the widest AWS coverage. Pick based on whether your center of gravity is the application or the AWS platform, and revisit the choice if your needs grow toward multi-cloud and governance.

To see how the SST team made its own switch, read the [case study on why SST moved from AWS CDK to Pulumi](/blog/aws-cdk-vs-pulumi-why-sst-switched/).
