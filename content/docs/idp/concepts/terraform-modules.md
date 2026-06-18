---
title_tag: Terraform Modules in the Pulumi Cloud Registry | Pulumi IDP
title: Terraform Modules
h1: "Terraform Modules in the Pulumi Cloud Registry"
meta_desc: Publish and consume Terraform modules in Pulumi Cloud using the HCP-compatible registry surface.
menu:
  idp:
    parent: idp-concepts
    identifier: idp-concepts-terraform-modules
    weight: 15
---

Pulumi Cloud hosts Terraform modules as a first-class registry resource alongside [components](/docs/iac/concepts/resources/components/) and [templates](/docs/idp/concepts/organization-templates/). Teams migrating from HCP Terraform can publish their existing modules to Pulumi Cloud using the same tooling they already use (the [go-tfe](https://github.com/hashicorp/go-tfe) library, the [hashicorp/tfe Terraform provider](https://registry.terraform.io/providers/hashicorp/tfe/latest/docs), or the [tfc-workflows-github](https://github.com/hashicorp/tfc-workflows-github) Action) by pointing those tools at `tf.pulumi.com` instead of `app.terraform.io`. Consumers reference the modules from `.tf` files with `tofu init` or from Pulumi programs with `pulumi package add terraform-module`.

## Before you begin

1. You need a [Pulumi Cloud](https://app.pulumi.com) account on the Enterprise or Business Critical plan. Publishing is gated to those tiers; reading, listing, and deleting modules is available on any plan, so you always keep access to modules you have already published.
1. You need the [Pulumi CLI](/docs/install/) installed if you plan to consume modules from a Pulumi program.
1. You need OpenTofu or Terraform installed if you plan to consume modules from a `.tf` file with `tofu init` / `terraform init`.

## Authenticate

`terraform login tf.pulumi.com` produces the bearer token used by every HashiCorp-protocol service Pulumi Cloud exposes (state backend, module registry). The credential lands in `~/.terraform.d/credentials.tfrc.json`.

Run it once per workstation:

```bash
terraform login tf.pulumi.com
```

Self-hosted Pulumi Cloud installations follow the same flow against their own host (`terraform login <your-pulumi-host>`).

## Publish a module

Pulumi Cloud's publish API is wire-compatible with HCP Terraform's private registry. Existing HCP migration tooling works unmodified, just pointed at the new host. The three most common paths:

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

### tfc-workflows-github GitHub Action

```yaml
- uses: hashicorp/tfc-workflows-github/actions/create-run@v1
  with:
    hostname: tf.pulumi.com
    token: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

### Module layout

At publish time Pulumi Cloud extracts the following from the standard [Terraform module structure](https://developer.hashicorp.com/terraform/language/modules/develop/structure):

- Root `variables.tf`, `outputs.tf`, `versions.tf` for the module's inputs, outputs, and required providers.
- `README.md` (optional) rendered on the module's detail page.
- `modules/<name>/` subdirectories for each submodule, parsed the same way as the root.
- `examples/<name>/` subdirectories for examples, captured as syntax-highlighted snippets.

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

`tofu init` discovers the `modules.v1` endpoint on Pulumi Cloud's `.well-known/terraform.json`, lists available versions, and downloads the tarball using the bearer token from `terraform login`.

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

The CLI injects a `TF_TOKEN_tf_pulumi_com` (or the equivalent host-derived token name for self-hosted installations) into the `pulumi-terraform-module` provider's environment, so `tofu init` resolves against Pulumi Cloud without further configuration. The persisted `Pulumi.yaml` entry uses the existing parameterized-provider shape; see [Use a Terraform Module in Pulumi](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) for examples.

## Delete a module or version

Two paths, both supported:

- From Pulumi Cloud's console, the module detail page exposes a per-version delete button.
- Programmatically with go-tfe (`client.RegistryModules.DeleteVersion`, `Delete`) or the GitHub Action, against the HCP-compatible `/api/v2/.../registry-modules/...` surface.

Hard delete is permanent. Stacks that were already deployed using the module continue to work locally, but `pulumi up` or `tofu init` from a fresh checkout fails because the module can no longer be fetched.
