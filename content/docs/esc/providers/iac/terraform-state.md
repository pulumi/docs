---
title_tag: terraform-state Pulumi ESC Provider
meta_desc: The terraform-state provider enables you to read outputs from Terraform state files stored in S3 or Terraform Cloud.
title: terraform-state
h1: terraform-state
menu:
  esc:
    identifier: terraform-state
    parent: esc-providers-iac
    weight: 2
aliases:
  - /docs/esc/providers/secrets/terraform-state/
  - /docs/pulumi-cloud/esc/providers/terraform-state/
  - /docs/esc/providers/terraform-state/
  - /docs/esc/integrations/infrastructure/terraform/terraform-state/
  - /docs/esc/integrations/terraform-state/
  - /docs/esc/concepts/providers/secrets/terraform-state/
---

The `terraform-state` provider enables you to read outputs from Terraform state files stored in S3 or Terraform Cloud. By importing those outputs into your environment, you can seamlessly consume Terraform-managed infrastructure as inputs to your Pulumi programs — referencing values such as VPC IDs, subnet IDs, and cluster endpoints directly, without copying them by hand or rewriting your Terraform in Pulumi. This bridges the two tools, so you can adopt Pulumi incrementally alongside an existing Terraform footprint.

Imported outputs are available under the `outputs` key (for example, `${terraform.outputs.vpc_id}`) and can be mapped to either of the following:

- `pulumiConfig` — to consume them as [stack configuration](/docs/iac/concepts/config/) (that is, as inputs to your Pulumi program).
- `environmentVariables` — to expose them as environment variables for the Pulumi CLI, a downstream Terraform run, or any other tooling.

## Example

### S3 backend

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
  pulumiConfig:
    # Consume the Terraform outputs as Pulumi stack configuration (inputs to your program)
    vpcId: ${terraform.outputs.vpc_id}
    subnetIds: ${terraform.outputs.subnet_ids}
  environmentVariables:
    # Expose the outputs as TF_VAR_* environment variables to feed a downstream Terraform run
    TF_VAR_vpc_id: ${terraform.outputs.vpc_id}
```

### Terraform Cloud backend

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
    # Consume the Terraform outputs as Pulumi stack configuration (inputs to your program)
    vpcId: ${terraform.outputs.vpc_id}
    subnetIds: ${terraform.outputs.subnet_ids}
  environmentVariables:
    # Expose the outputs as TF_VAR_* environment variables to feed a downstream Terraform run
    TF_VAR_vpc_id: ${terraform.outputs.vpc_id}
```

## Schema reference

{{< esc-schema-updated >}}

### Inputs

{{< esc-schema type="provider" name="terraform-state" section="inputs" >}}

### Outputs

{{< esc-schema type="provider" name="terraform-state" section="outputs" >}}
