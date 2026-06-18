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

Pulumi Cloud hosts Terraform modules as a first-class registry resource alongside [packages](/docs/iac/concepts/packages/) and [templates](/docs/idp/concepts/organization-templates/). Teams migrating from HCP Terraform can publish their existing modules to Pulumi Cloud using the same tooling they already use (the [go-tfe](https://github.com/hashicorp/go-tfe) library or the [hashicorp/tfe Terraform provider](https://registry.terraform.io/providers/hashicorp/tfe/latest/docs)) by pointing those tools at `tf.pulumi.com` instead of `app.terraform.io`. Consumers reference the modules from `.tf` files with `tofu init` or from Pulumi programs with `pulumi package add terraform-module`.

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

## Consume from a Pulumi program

```bash
pulumi package add terraform-module tf.pulumi.com/<namespace>/<name>/<system> <version> <local-name>
```

`terraform-module` is a parameterized provider. Its parameters are the module address (`tf.pulumi.com/<namespace>/<name>/<system>`), the module version, and the local package name you import in your program.

After `pulumi login`, `pulumi package add terraform-module` resolves the module using your Pulumi credentials, so no manual token or registry login is needed. The persisted `Pulumi.yaml` entry uses the existing parameterized-provider shape; see [Use a Terraform Module in Pulumi](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) for examples.

## Delete a module or version

Two paths, both supported:

- From Pulumi Cloud's console, the module detail page exposes a per-version delete button.
- Programmatically with go-tfe (`client.RegistryModules.DeleteVersion`, `Delete`), against the HCP-compatible `/api/v2/.../registry-modules/...` surface.

Hard delete is permanent. Stacks that were already deployed using the module continue to work locally, but `pulumi up` or `tofu init` from a fresh checkout fails because the module can no longer be fetched.
