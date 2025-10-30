---
title_tag: terraform-state Pulumi ESC Provider
meta_desc: The terraform-state provider enables you to read outputs from Terraform state files stored in S3 or Terraform Cloud.
title: terraform-state
h1: terraform-state
menu:
  esc:
    identifier: terraform-state
    parent: esc-terraform-integrations
    weight: 1
aliases:
  - /docs/pulumi-cloud/esc/providers/terraform-state/
  - /docs/esc/providers/terraform-state/
---

The `terraform-state` provider enables you to read outputs from Terraform state files stored in S3 or Terraform Cloud.

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
    vpcId: ${terraform.outputs.vpc_id}
    subnetIds: ${terraform.outputs.subnet_ids}
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
    vpcId: ${terraform.outputs.vpc_id}
    subnetIds: ${terraform.outputs.subnet_ids}
```

## Inputs

| Property  | Type                | Description                                                   |
|-----------|---------------------|---------------------------------------------------------------|
| `backend` | [Backend](#backend) | Configuration for the Terraform state backend (S3 or remote). |

### Backend

The `backend` property must contain exactly one of the following:

#### S3

| Property | Type                                                                     | Description                                      |
|----------|--------------------------------------------------------------------------|--------------------------------------------------|
| `login`  | [aws-login](/docs/esc/integrations/dynamic-login-credentials/aws-login/) | The credentials to use to access the state file. |
| `bucket` | string                                                                   | The S3 bucket name containing the state file.    |
| `key`    | string                                                                   | The S3 object key for the state file.            |
| `region` | string                                                                   | The AWS region where the bucket is located.      |

#### Remote

| Property       | Type   | Description                                                                             |
|----------------|--------|-----------------------------------------------------------------------------------------|
| `hostname`     | string | [Optional] - The remote backend hostname to connect to. Defaults to `app.terraform.io`. |
| `organization` | string | The name of the organization containing the targeted workspace.                         |
| `workspace`    | string | The name of the remote workspace.                                                       |
| `token`        | string | The token used to authenticate with the remote backend.                                 |

## Outputs

| Property  | Type   | Description                                    |
|-----------|--------|------------------------------------------------|
| `outputs` | object | A map of all outputs from the Terraform state. |

The provider preserves the sensitive flag for any outputs marked as sensitive in the Terraform state.

