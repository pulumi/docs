---
title: "Publish a Terraform module, get a Pulumi package automatically"
date: 2026-08-04
category: product
draft: false
meta_desc: "Publish private Terraform modules to the Pulumi Cloud registry and get a typed Pulumi package for every version, with generated SDKs and API docs."
meta_image: meta.png
feature_image: feature.png
authors:
  - fausto-nunez-alberro
tags:
  - terraform
  - features
  - migration
  - infrastructure-as-code
canonical_url: https://www.pulumi.com/docs/idp/concepts/terraform-modules/
social:
  twitter: |
    Publish a Terraform module to the Pulumi Cloud registry and every version becomes a typed Pulumi package: generated SDKs for TypeScript, Python, Go, C#, Java and YAML, API docs, and usage tracking across your stacks.
  linkedin: |
    The Pulumi Cloud registry now hosts Terraform modules, and converts every version you publish into a Pulumi package.

    The registry is wire-compatible with HCP Terraform's private module registry, so the tools you already use to publish keep working. You just point them at tf.pulumi.com instead of app.terraform.io.

    What you get back is a first-class package. Its variables become typed inputs and its outputs become typed outputs, with a generated SDK for TypeScript, Python, Go, C#, Java or YAML. Pulumi Cloud gives it an API reference, tracks which stacks depend on it, and shows which of them have fallen behind the latest version.
---

The Pulumi Cloud registry now hosts Terraform modules, and turns every version you publish into a Pulumi package. The module you already maintain becomes a typed component with a generated SDK in your language, an API reference, and usage tracking across the stacks that depend on it. None of it requires rewriting the module.

<!--more-->

If you already [keep Terraform state in Pulumi Cloud](/docs/iac/get-started/terraform/terraform-state-backend/), this puts your modules in the same place, behind the same login.

## A registry that speaks the HashiCorp protocol

The registry is wire-compatible with HCP Terraform's private module registry. The publish and consume APIs accept the same requests, so the tooling you already use keeps working. The only change is the host: point your tools at `tf.pulumi.com` instead of `app.terraform.io`.

Authentication uses a Pulumi access token. It is the bearer token for everything Pulumi Cloud exposes over the HashiCorp protocol, including the state backend and the module registry. When you publish, you hand it to go-tfe (or the tfe provider) exactly where an HCP token goes today. When you consume from a Pulumi program, `pulumi login` is enough and the CLI passes it through. For plain OpenTofu or Terraform, set it as the host token:

```bash
export TF_TOKEN_tf_pulumi_com=$PULUMI_ACCESS_TOKEN
```

## Publishing a module

Publishing is available on the Enterprise and Business Critical plans. The common HCP publish paths all work once you retarget them:

- The [go-tfe](https://github.com/hashicorp/go-tfe) library, by setting `Address` to `https://tf.pulumi.com`.
- The [hashicorp/tfe](https://registry.terraform.io/providers/hashicorp/tfe/latest/docs) Terraform provider, by setting `hostname = "tf.pulumi.com"`.

For example, with go-tfe:

```go
client, _ := tfe.NewClient(&tfe.Config{
    Address: "https://tf.pulumi.com",
    Token:   os.Getenv("PULUMI_ACCESS_TOKEN"),
})
```

At publish time the registry reads the [standard Terraform module layout](https://developer.hashicorp.com/terraform/language/modules/develop/structure). Root `.tf` files describe the module's inputs and outputs, `modules/<name>/` subdirectories become submodules, and `examples/<name>/` subdirectories are captured as examples. Submodules and examples are discovered automatically, so there is nothing extra to declare.

## Every version becomes a Pulumi package

Publishing does two things. The version becomes available over the Terraform module protocol, as it would on HCP Terraform. The version is also converted into a Pulumi package, automatically, with nothing extra to configure.

The package takes its name from the module: `<name>-<system>`, in the same namespace. The system is the last segment of the module's address, the one HCP Terraform calls the provider, naming what the module provisions. A module published as `acme-corp/vpc/aws` becomes a package called `vpc-aws`, and a Pulumi program installs it by that name:

```bash
pulumi package add vpc-aws 1.2.3
```

Installing a converted package needs [Pulumi CLI](/docs/install/) 3.248.0 or newer.

The module becomes a [multi-language component](https://github.com/pulumi/pulumi-hcl/blob/master/docs/mlc.md). Its `variable` blocks become typed inputs and its `output` blocks become typed outputs, and Pulumi generates an SDK for whichever language the project uses: TypeScript, Python, Go, C#, Java, or YAML. Editors complete the inputs, and a misspelled one fails at compile time rather than partway through a plan. The resources the module creates appear individually in previews and in the resource graph.

Pulumi Cloud treats it as it would any other package. The package page carries an API reference generated from the module's variables and outputs, and records which stacks depend on it and which of those are behind the latest version, so you know who to tell before publishing a breaking change. That count follows the package, so it covers the stacks consuming the module through Pulumi, not the ones consuming it over the Terraform protocol.

Conversion runs per version, so a module can have some versions with packages and some without. The package's page shows which versions have converted.

## Your Terraform consumers keep working

Nothing about the module changes for the people already consuming it. A `.tf` file references it as it would any private module, and `tofu init` (or `terraform init`) resolves it against Pulumi Cloud using the token from `TF_TOKEN_tf_pulumi_com`:

```hcl
module "vpc" {
  source  = "tf.pulumi.com/<namespace>/<name>/<system>"
  version = "1.2.3"
}
```

Submodules use the usual `//modules/<name>` syntax.

If a version you need has no package, you can convert the module locally instead, with `pulumi package add hcl module tf.pulumi.com/<namespace>/<name>/<system>`. That generates an SDK for your project without publishing anything, so it comes without the package page, API reference, and usage tracking. For a full walkthrough, see [Use a Terraform Module in Pulumi](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/).

## Get started

See [Terraform Modules in the Pulumi Cloud Registry](/docs/idp/concepts/terraform-modules/) for the full publish and consume reference, including how to migrate an existing registry, the naming rules to check first, and self-hosted hosts. If you are new to running Terraform modules through Pulumi, the [Use a Terraform Module in Pulumi](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) guide is the place to start.
