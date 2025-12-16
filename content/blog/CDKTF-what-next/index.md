---
title: "If you're using CDKTF, what to do next"
date: 2025-12-17
draft: false
meta_desc: "CDKTF is deprecated. Here are your options: stay on CDKTF, move to Terraform/OpenTofu, or migrate to Pulumi and keep writing infrastructure in real languages."
meta_image: meta.png
authors:
  - adam-gordon-bell
tags:
  - migration
  - terraform
---
If you're using CDK for Terraform (CDKTF), you probably liked the best part of "infrastructure as code": the code. TypeScript, Python, Go, C#, Java.

Unfortunately, CDKTF is now deprecated and the repo archived. That puts teams in a familiar spot: it works today, but what about next year?

## A short history: from Terrastack to CDKTF

Before CDKTF existed, Terrastack explored the same idea: keep Terraform as the engine, but write infrastructure in real languages and synthesize Terraform config.

In July 2020, AWS announced CDK for Terraform as a collaboration with HashiCorp. They thanked Sebastian Korfmann (Terrastack's maintainer) for helping build it and made him a maintainer.

CDKTF hit general availability in August 2022 (v0.12). And as of December 10, 2025, it's deprecated.

## Your options

You have three paths:

1. **Stay on CDKTF**:  it still works, but you're on your own for fixes. HashiCorp says "at your own risk."
1. **Go back to HCL**: run `cdktf synth --hcl` to generate Terraform config, then use Terraform or OpenTofu.
1. **Migrate to Pulumi**: keep writing infrastructure in real languages.

This is a Pulumi blog, so I'm biased toward option 3. But it's also the option that preserves what you probably liked about CDKTF: real programming languages, not a DSL.

## Migrating to Pulumi

At a high level, the workflow is: synthesize to Terraform (HCL), convert to Pulumi code, import existing resources.

```bash
# 1) Export CDKTF to HCL
cdktf synth --hcl

# 2) In a new folder, copy in the HCL + the TF state you’ll import from
mkdir my-project && cd my-project
cp ../terraform.dev.tfstate .
cp ../cdktf.out/stacks/dev/cdk.tf .

# 3) Convert HCL to Pulumi program (TypeScript shown)
pulumi convert --from terraform --language typescript

# 4) Create a stack and import the deployed resources from state
pulumi stack init dev
pulumi import --from terraform --out ./imported.ts ./terraform.dev.tfstate
```

After import, you’ll usually make a small pass to align the converted `index.ts` with the imported reality then `pulumi up` to confirm everything is unchanged. See the full walkthrough: [CDKTF to Pulumi migration example](https://github.com/pulumi/cdktf-to-pulumi-example).

**Use Neo for AI-assisted migration**: [Pulumi Neo](/blog/pulumi-neo/) is an LLM agent that's very capable of doing migrations to Pulumi. Pulumi customers often use it to speed up migrations. See [10 things you can do with Neo](/blog/10-things-you-can-do-with-neo/) for examples.

**Use Terraform modules directly in Pulumi**: If modules are most of your infra, rewriting them takes time. Pulumi can [use Terraform modules directly](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/), even [without conversion](/blog/announcing-direct-tf-modules/):

```bash
pulumi package add terraform-module terraform-aws-modules/vpc/aws 5.19.0 vpc
```

## Closing

CDKTF solved a real problem. The deprecation is frustrating. But you have options, and you can pick the one that matches why you adopted CDKTF in the first place.
