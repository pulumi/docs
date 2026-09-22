---
title_tag: "Terraform & OpenTofu | Pulumi Integrations"
meta_desc: Use Pulumi with Terraform and OpenTofu. Store state and run plans in Pulumi Cloud, use Terraform providers and modules, reference state, or convert HCL.
title: Terraform & OpenTofu
linktitle: Terraform & OpenTofu
h1: Terraform & OpenTofu
menu:
  integrations:
    name: Terraform & OpenTofu
    identifier: integrations-terraform
    parent: integrations-home
    weight: 3
  iac:
    name: Terraform users
    identifier: terraform-get-started
    parent: iac-get-started
    weight: 50
aliases:
  - /docs/iac/get-started/terraform/
  - /docs/iac/get-started/terraform/begin/
  - /docs/iac/get-started/terraform/first-look/
  - /docs/iac/get-started/terraform/next-steps/
---

Pulumi works alongside your existing Terraform and OpenTofu investment. You don't have to migrate everything at once, or at all: Pulumi Cloud can manage your Terraform state and runs, Pulumi programs can use Terraform providers, modules, and state directly, and you can convert HCL to Pulumi when and where it makes sense.

This page links to every Pulumi capability for Terraform and OpenTofu users. If you're new to Pulumi, start by [installing Pulumi](/docs/install/) and following a [get-started guide](/docs/get-started/) for your cloud.

## Terraform and Pulumi side by side

Here's a Terraform configuration that looks up the latest Ubuntu AMI:

```hcl
data "aws_ami" "ubuntu" {
  region      = "us-west-2"
  most_recent = true
  owners      = ["099720109477"] # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}

output "latest_ubuntu_ami_id" {
  value = data.aws_ami.ubuntu.id
}
```

The same program in TypeScript:

```typescript
import * as aws from "@pulumi/aws";

const ubuntu = aws.ec2.getAmiOutput({
    region: "us-west-2",
    mostRecent: true,
    owners: ["099720109477"],
    filters: [{
        name: "name",
        values: ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"],
    }],
});

export const latestUbuntuAmiId = ubuntu.id;
```

Pulumi programs can be written in TypeScript, JavaScript, Python, Go, .NET, Java, or YAML. You can also keep writing HCL: with the [Pulumi HCL runtime](/docs/iac/languages-sdks/hcl/), the Terraform configuration above runs unchanged under the Pulumi engine. For a concept-by-concept mapping, see [Terraform terminology](/docs/iac/comparisons/terraform/#terminology).

## Pulumi Cloud for Terraform

Use Pulumi Cloud as the backend and control plane for Terraform and OpenTofu configurations you keep as they are.

- [Store Terraform state in Pulumi Cloud](/docs/integrations/terraform/state-backend/): use Pulumi Cloud as your state backend, with update history, state locking, RBAC, audit policies, and unified resource visibility.
- [Remote execution](/docs/integrations/terraform/remote-execution/): run Terraform and OpenTofu plans and applies on Pulumi Cloud, with credentials from Pulumi ESC and VCS-triggered runs.
- [Terraform module registry](/docs/integrations/terraform/module-registry/): publish and consume Terraform modules in Pulumi Cloud through an HCP-compatible registry, with each module also available as a Pulumi package.

## Use Terraform from Pulumi

Bring the Terraform ecosystem into Pulumi programs.

- [Any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/): use any Terraform or OpenTofu provider in a Pulumi program, including providers with no pre-built Pulumi package.
- [Terraform modules](/docs/integrations/terraform/modules/): use existing Terraform modules directly, with generated, typed SDKs.
- [Reference Terraform state](/docs/integrations/terraform/reference-state/): read outputs from Terraform state files so Pulumi and Terraform can manage infrastructure side by side.

## Convert and orchestrate

- [Convert Terraform HCL to Pulumi](/docs/integrations/terraform/convert-hcl/): convert configurations with a coding agent or with `pulumi convert`.
- [Orchestrate Terraform and Pulumi together](/docs/integrations/terraform/orchestrate/): coordinate deployments of both tools in CI/CD and manage the dependencies between them.

## Secrets and configuration

- [Pulumi ESC with Terraform](/docs/esc/guides/integrate-with/terraform/): supply credentials, secrets, and configuration to Terraform from Pulumi ESC environments.
- [`terraform-state` provider](/docs/esc/providers/iac/terraform-state/): read Terraform state outputs into Pulumi ESC environments.

## Migrate and compare

- [Migrate from Terraform](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/): plan a full or gradual migration, including importing existing resources.
- [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/): compare languages, state management, and workflows.
- [Pulumi vs. OpenTofu](/docs/iac/comparisons/opentofu/): compare Pulumi with OpenTofu.
