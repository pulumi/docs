---
title: "CDKTF is deprecated: What's next for your team?"
date: 2025-12-17
draft: false
meta_desc: "The deprecation of CDKTF has left many teams without a clear path forward. This post outlines the options and shows what it's like to move from CDKTF to Pulumi."
meta_image: meta.png
authors:
  - adam-gordon-bell
  - christian-nunciato
tags:
  - migration
  - terraform
  - cdktf
---

In July, 2020, CDK for Terraform (CDKTF) was introduced, and last week, on December 10, it was officially deprecated. Support for CDKTF has stopped, the [organization](https://github.com/cdktf) and [repository](https://github.com/hashicorp/terraform-cdk) have been archived, and HashiCorp/IBM will no longer be updating or maintaining it, leaving a lot of teams out there without a clear path forward.

For most teams, that means it's time to start looking for a replacement.

It's an unfortunate situation to suddenly find yourself in as a user of CDKTF, but you do have options, and Pulumi is one of them. In this post, we'll help you understand what those options are, how Pulumi fits into them, and what it'd look like to migrate your CDKTF projects to Pulumi.

## What are the options?

Teams migrating away from CDKTF generally have three options:

### Option 1: Fall back to HCL

HashiCorp's official recommendation is to export your projects to HashiCorp Configuration Language (HCL) and manage them with Terraform. CDKTF even has a command that makes this fairly simple:

```bash
cdktf synth --hcl
```

Of course, if you're using CDKTF, you probably chose it specifically to avoid HCL. So while possible, this probably isn't the choice most teams would make unless they had to.

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
    versioning: {
        enabled: true,
    },
    acl: 'private',
});
```

Notice how different these APIs are — and this is just one simple resource with only a few properties; imagine having to rewrite dozens or hundreds of them. Beyond that, there's also the problem of state: How would you go about translating the contents of a Terraform state file containing hundreds of resources into the equivalent CloudFormation YAML or JSON?

Despite their surface similarities, CDKTF and AWS CDK have little in common. Migration would essentially mean a ground-up rewrite that'd also leave you without the multi-cloud support you already have with CDKTF. For most teams, that makes this option a practical non-starter.

### Option 3: Migrate to Pulumi

This is where we should acknowledge our obvious bias — but we genuinely believe that for most users of CDKTF, Pulumi really is the simplest and most broadly compatible way forward.

Like CDKTF, Pulumi lets you build and manage your infrastructure with general-purpose languages like TypeScript, Python, Go, C#, and Java, and it supports organizing your code into higher-level abstractions called [_components_](/docs/iac/concepts/components/), which you can think of like CDKTF constructs. Both organize cloud resources into [_stacks_](/docs/iac/concepts/stacks/) (think `dev`, `prod`), and both track [deployment state](/docs/iac/concepts/state-and-backends/) similarly, with local, remote, and cloud-hosted options available.

Many of Pulumi's most popular [providers](/docs/iac/concepts/resources/providers/) (e.g., the AWS provider) are also built from open-source Terraform schemas, which means their resource models will be nearly identical to what you're used to with CDKTF. Here's what an S3 bucket looks like in Pulumi, for example:

```typescript
import * as aws from '@pulumi/aws';

const bucket = new aws.s3.Bucket('my-bucket', {
    bucket: 'my-example-bucket',
    versioning: {
        enabled: true,
    },
    acl: 'private',
});
```

You can also use [any Terraform provider](/docs/iac/get-started/terraform/terraform-providers/) with Pulumi, and you can even [reference Terraform modules directly](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#using-terraform-modules-directly) from within your Pulumi code.

Pulumi is also different from CDKTF in several ways. One is that rather than transpile your source code to a format like JSON as CDKTF does (and then deploying it separately later), Pulumi uses its own declarative deployment engine that resolves the resource graph at runtime and provisions cloud resources directly, which is much faster and more flexible. You can learn more about the deployment model in [How Pulumi Works](/docs/iac/concepts/how-pulumi-works/).

Given the API similarities, the support for all Terraform providers and modules, the ability to [coexist](/docs/iac/guides/migration/#coexistence) alongside Terraform-managed projects, and the built-in support for conversion (which we'll cover next), we think Pulumi is the best option for most teams looking to migrate.

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

Refactoring can get a bit more complicated when custom logic and higher-level abstractions are involved, as fidelity to the original CDKTF code is often lost in the translation to HCL. In these situations, having the help of an LLM to recapture that original logic or translate your CDKTF constructs into Pulumi components can be a big time-saver.

## An end-to-end example

The best way to get a feel for how this works, though, is to try it yourself.

The [**pulumi/cdktf-to-pulumi-example**](https://github.com/pulumi/cdktf-to-pulumi-example) repository on GitHub contains a CDKTF project with multiple stacks written in TypeScript, along with a guide that walks you through the process of migrating that project to Pulumi. The guide covers everything we've discussed here so far, including:

* Converting the CDKTF project into a new Pulumi project
* Importing its actively running resources into Pulumi stacks
* Modifying the generated code to align with imported state
* Performing an initial deployment with Pulumi to complete the migration process

The walkthrough takes only a few minutes to complete, and it's a great way to stand up an example of your own to get more familiar with Pulumi.

## What's next?

If you’re moving on from CDKTF, there are a few possible paths forward. For teams that want to keep using real languages and avoid a ground-up rewrite, Pulumi offers the clearest way forward.

To learn more about how Pulumi works, how it differs from CDKTF and from Terraform, how to handle additional conversion scenarios, and more, we recommend:

* Diving into [the Pulumi docs](/docs/iac/concepts/) to get familiar with core concepts and features of the platform
* Reading [Migrating from Terraform or CDKTF to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) for more detailed, Terraform-specific migration guidance
* Joining us in the [Pulumi Community Slack](https://slack.pulumi.com/) to ask questions and learn from others who've successfully made the leap from Terraform and CDKTF to Pulumi

And of course, [feel free to reach out](/contact/)! We'd love to help in any way we can.
