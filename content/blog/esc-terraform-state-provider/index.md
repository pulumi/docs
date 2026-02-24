---
title: "Introducing the Terraform State Provider for Pulumi ESC"
date: 2026-02-13T00:00:00Z
draft: false
meta_desc: "The terraform-state provider for Pulumi ESC lets you read outputs from Terraform state files directly into your ESC environments."
meta_image: meta.png
authors: ["claire-gaestel"]
tags: ["esc", "terraform"]
---

Many organizations have years of infrastructure built and managed with Terraform.
Outputs such as VPC IDs, subnet lists, database endpoints, and cluster names are the connective tissue between infrastructure layers.
Getting those values into other tools and workflows often means manual copy-paste, wrapper scripts, or brittle glue code.

The [`terraform-state` provider](/docs/esc/integrations/infrastructure/terraform/terraform-state/) for Pulumi ESC helps bridge that gap.
It reads outputs directly from your Terraform state files and makes them available as first-class values in your ESC environments — no scripts, no duplication, no drift.
Any output marked as `sensitive` in your Terraform state is automatically treated as a secret in ESC.
If you've used [`pulumi-stacks`](/docs/esc/integrations/infrastructure/pulumi-iac/pulumi-stacks/) to read outputs from Pulumi stacks, this is the same idea for Terraform.

## How it works

The `terraform-state` provider uses `fn::open::terraform-state` to read from a Terraform state file and surface its outputs as ESC values.
Here's an example that reads from an S3 backend, using the `aws-login` provider for credentials, and exports a `KUBECONFIG` for an EKS cluster managed by Terraform:

```yaml
values:
  terraform:
    fn::open::terraform-state:
      backend:
        s3:
          login:
            fn::open::aws-login:
              oidc:
                roleArn: arn:aws:iam::123456789012:role/esc-oidc
                sessionName: pulumi-environments-session
          bucket: my-terraform-state-bucket
          key: path/to/terraform.tfstate
          region: us-west-2
  files:
    KUBECONFIG: ${terraform.outputs.kubeconfig}
```

Once the environment is opened, `terraform.outputs` contains every output from the Terraform state.
In this example we take the `kubeconfig` output from a Terraform-managed EKS cluster and project it as a file,
so any tool that reads `KUBECONFIG` - `kubectl`, `helm`, Pulumi - just works.
You can also reference outputs in `pulumiConfig` to pass values like VPC IDs and subnet lists directly into Pulumi stacks.[^1]

### Terraform Cloud support

If your state lives in Terraform Cloud (or any compatible remote backend), the provider supports that too:

```yaml
values:
  terraform:
    fn::open::terraform-state:
      backend:
        remote:
          organization: my-terraform-org
          workspace: my-workspace
          token:
            fn::secret: tfc-token-value
  pulumiConfig:
    vpcId: ${terraform.outputs.vpc_id}
    subnetIds: ${terraform.outputs.subnet_ids}
```

You can point it at any Terraform Cloud-compatible backend by setting the optional `hostname` property.

## Get started

Check out the full [`terraform-state` provider documentation](/docs/esc/integrations/infrastructure/terraform/terraform-state/) for the complete reference.

[^1]: You can also consume Terraform outputs directly in a Pulumi program with the [Pulumi Terraform provider](/registry/packages/terraform/).
