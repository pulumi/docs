---
title: "Host Terraform modules in the Pulumi Cloud registry"
date: 2026-06-18
draft: false
meta_desc: "Publish private Terraform modules to the Pulumi Cloud registry and consume them from OpenTofu, Terraform, or Pulumi with your existing tooling."
meta_image: meta.png
feature_image: feature.png
authors:
  - idp-team
tags:
  - terraform
  - features
  - migration
  - infrastructure-as-code
canonical_url: https://www.pulumi.com/docs/idp/concepts/terraform-modules/
social:
  twitter: |
    The Pulumi Cloud registry now hosts Terraform modules. Publish with the HCP tooling you already use, and consume from OpenTofu, Terraform, or Pulumi. Just point at tf.pulumi.com.
  linkedin: |
    The Pulumi Cloud registry now hosts Terraform modules.

    The registry is wire-compatible with HCP Terraform's private module registry, so the tools you already use to publish keep working. You just point them at tf.pulumi.com instead of app.terraform.io.

    Consumers can reference modules from a .tf file with tofu init, or from a Pulumi program with pulumi package add. Reading and listing modules works on any plan.
---

The Pulumi Cloud registry now hosts Terraform modules. You can publish your private modules to your organization and consume them from OpenTofu, Terraform, or a Pulumi program, all under the `tf.pulumi.com` host.

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

## Consuming from OpenTofu or Terraform

Reference the module the same way you would any private module, with the Pulumi Cloud host in the source:

```hcl
module "vpc" {
  source  = "tf.pulumi.com/<namespace>/<name>/<system>"
  version = "1.2.3"
}
```

`tofu init` (or `terraform init`) resolves the module against Pulumi Cloud using the token from `TF_TOKEN_tf_pulumi_com`. Submodules use the usual `//modules/<name>` syntax.

## Consuming from a Pulumi program

You can also bring the module into a Pulumi program in any supported language:

```bash
pulumi package add terraform-module tf.pulumi.com/<namespace>/<name>/<system> <version> <local-name>
```

`terraform-module` is a parameterized provider, and its parameters are the module address, the version, and a local name for the generated package. After `pulumi login` the CLI resolves the module with your Pulumi credentials, so there is no separate login step. From there the module behaves like any other Pulumi package. For a full walkthrough, see [Use a Terraform Module in Pulumi](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/).

## Get started

See [Terraform Modules in the Pulumi Cloud Registry](/docs/idp/concepts/terraform-modules/) for the full publish and consume reference, including how to migrate an existing registry, the naming rules to check first, module deletion, and self-hosted hosts. If you are new to running Terraform modules through Pulumi, the [Use a Terraform Module in Pulumi](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) guide is the place to start.
