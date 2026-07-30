---
title_tag: Terraform modules in the Pulumi Cloud registry | Pulumi IDP
title: Terraform modules
h1: "Terraform modules in the Pulumi Cloud registry"
meta_desc: Publish and consume Terraform modules in Pulumi Cloud using the HCP-compatible registry surface.
menu:
  idp:
    parent: idp-concepts
    identifier: idp-concepts-terraform-modules
    weight: 15
---

Pulumi Cloud hosts Terraform modules as a first-class registry resource alongside [packages](/docs/iac/concepts/packages/) and [templates](/docs/idp/concepts/organization-templates/). Teams migrating from HCP Terraform can publish their existing modules to Pulumi Cloud using the same tooling they already use (the [go-tfe](https://github.com/hashicorp/go-tfe) library or the [hashicorp/tfe Terraform provider](https://registry.terraform.io/providers/hashicorp/tfe/latest/docs)) by pointing those tools at `tf.pulumi.com` instead of `app.terraform.io`. Every module version you publish is also converted into a Pulumi package. The module's variables become typed inputs and its outputs become typed outputs, with a generated SDK in TypeScript, Python, Go, C#, Java, or YAML, an API reference on the package's page, and a record of which stacks depend on it. Existing `.tf` consumers are unaffected and keep resolving the module over the Terraform protocol.

## Before you begin

1. You need a [Pulumi Cloud](https://app.pulumi.com) account on the Enterprise or Business Critical plan. Publishing is gated to those tiers; reading, listing, and deleting modules is available on any plan, so you always keep access to modules you have already published.
1. You need the [Pulumi CLI](/docs/install/) installed if you plan to consume modules from a Pulumi program.
1. You need OpenTofu or Terraform installed if you plan to consume modules from a `.tf` file with `tofu init` / `terraform init`.

## Authenticate

Every surface authenticates with a [Pulumi access token](/docs/pulumi-cloud/access-management/access-tokens/). It is the bearer token for everything Pulumi Cloud exposes over the HashiCorp protocol: the publish API, the state backend, and the module registry.

- Publishing: the go-tfe client and the tfe provider take your Pulumi access token wherever they expect a TFE token today. See [Publish a module](#publish-a-module).
- Consuming from a Pulumi program: run `pulumi login`. `pulumi package add terraform-module` passes the token through to the provider, so there is no separate registry login.
- Consuming from plain OpenTofu or Terraform: set the host token. OpenTofu and Terraform derive the variable name from the host by replacing dots with underscores (and dashes with double underscores), so `tf.pulumi.com` becomes `TF_TOKEN_tf_pulumi_com`:

  ```bash
  export TF_TOKEN_tf_pulumi_com=$PULUMI_ACCESS_TOKEN
  ```

  You can also store the token in the Terraform CLI credentials file (`~/.terraform.d/credentials.tfrc.json`). Self-hosted installations use the same scheme with their own host.

## Publish a module

Pulumi Cloud's publish API is wire-compatible with HCP Terraform's private registry. Existing HCP migration tooling works unmodified, pointed at the new host. The two most common paths:

### go-tfe

```go
client, _ := tfe.NewClient(&tfe.Config{
    Address: "https://tf.pulumi.com",
    Token:   os.Getenv("PULUMI_ACCESS_TOKEN"),
})
```

The `RegistryModules` surface (`client.RegistryModules.Create`, `CreateVersion`, `UploadTarGzip`, etc.) accepts the same payloads it accepts against `app.terraform.io`.

### `hashicorp/tfe` Terraform provider

```hcl
provider "tfe" {
  hostname = "tf.pulumi.com"
  token    = var.pulumi_access_token
}

resource "tfe_registry_module" "vpc" {
  organization = "acme"
  ...
}
```

### Module layout

At publish time Pulumi Cloud reads the standard [Terraform module structure](https://developer.hashicorp.com/terraform/language/modules/develop/structure):

- Root `.tf` files (any filenames) define the module's inputs, outputs, and required providers.
- `modules/<name>/` subdirectories are parsed the same way as the root and can be consumed as submodules.
- `examples/<name>/` subdirectories and the `README.md` are captured at publish.

## Migrating from HCP Terraform

If you publish from CI today, the move is mostly a host change. Point your existing pipelines at `tf.pulumi.com`, supply a Pulumi access token, and your publish steps run unchanged. Reading, listing, and deleting modules work on any plan, so you keep access to modules you have already published regardless of your plan.

### Module names

Pulumi Cloud uses the same `<namespace>/<name>/<system>` address form as HCP Terraform, where the namespace is your Pulumi organization. One rule is stricter: the module name must be lowercase letters, digits, and hyphens (`[a-z0-9-]`), so underscores are rejected at publish. A module that HCP hosts under a name like `control_tower_account_factory` has to be renamed to `control-tower-account-factory` before you publish it. Uppercase in the name is lowercased automatically.

## What happens when you publish

Publishing a module version also converts it into a Pulumi package, with no extra step on your part. The package is named after the module: `<name>-<system>`, published under the same namespace and registry source, so a module published as `acme-corp/vpc/aws` produces a package called `vpc-aws`.

Conversion runs per version, so a module can have some versions with packages and some without. The package's page in Pulumi Cloud shows which versions have converted and gives you the command to install one. A version that has not converted, either because it is still running or because the module uses Terraform features Pulumi cannot express yet, can be [consumed directly](#using-a-module-that-has-not-converted) in the meantime.

## Consume from a Pulumi program

Once a version has converted, install it by package name:

```bash
pulumi package add <name>-<system> [<version>]
```

The module is a [multi-language component](https://github.com/pulumi-labs/pulumi-hcl/blob/main/docs/mlc.md): its `variable` blocks become typed inputs, its `output` blocks become typed outputs, and Pulumi generates an SDK in the language your project uses. The version you pass is persisted in `Pulumi.yaml`, so `pulumi install` regenerates the same pinned version.

The resources the module creates appear individually in previews and in the resource graph rather than as one opaque unit. In Pulumi Cloud the package gets the same treatment as any other: an [API reference](/docs/idp/concepts/private-registry/#api-documentation) generated from the module's variables and outputs, and [usage tracking](/docs/idp/concepts/private-registry/#usage-tracking) recording which stacks depend on it and which of those are behind the latest version.

Usage tracking only counts consumption through the converted package. A stack or workspace that consumes the module over the Terraform protocol does not report a dependency, so it does not appear in the usage columns or on the package's "Used by" tab.

{{% notes type="info" %}}
Installing a converted package requires Pulumi CLI 3.248.0 or newer. Older versions fail with a plugin handshake error.
{{% /notes %}}

### Using a module that has not converted

While a version is converting, and for modules that cannot convert, consume the module directly:

```bash
pulumi package add hcl module tf.pulumi.com/<namespace>/<name>/<system> [<version>]
```

`hcl` is a parameterized provider. The `module` keyword selects module mode, followed by the module address and an optional version. Omit the version to resolve the latest published version; pass one to pin it.

This performs the same conversion locally, at the moment you run it, rather than using the package the registry produced. A module the registry could not convert fails here for the same reason.

After `pulumi login`, both commands resolve using your Pulumi credentials, so no manual token or registry login is needed. See [Use a Terraform Module in Pulumi](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) for examples.

## Consume from OpenTofu or Terraform

Reference the module in a `.tf` file:

```hcl
module "vpc" {
  source  = "tf.pulumi.com/<namespace>/<name>/<system>"
  version = "1.2.3"
}
```

`tofu init` discovers the `modules.v1` endpoint on Pulumi Cloud's `.well-known/terraform.json`, lists available versions, and downloads the tarball using the token from `TF_TOKEN_tf_pulumi_com`.

Submodules are referenced with the standard `//modules/<name>` source syntax:

```hcl
module "private_subnet" {
  source  = "tf.pulumi.com/<namespace>/<name>/<system>//modules/<submodule>"
  version = "1.2.3"
}
```

## Delete a module or version

Delete a module or a single version with go-tfe (`client.RegistryModules.DeleteVersion`, `Delete`), against the HCP-compatible `/api/v2/.../registry-modules/...` surface.

Hard delete is permanent. Stacks that were already deployed using the module continue to work locally, but `pulumi up` or `tofu init` from a fresh checkout fails because the module can no longer be fetched.

