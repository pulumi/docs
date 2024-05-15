---
title_tag: Integrate with Terraform | Pulumi ESC
title: Terraform
h1: "Pulumi ESC: Integrate with Terraform"
meta_desc: This page provides an overview on how to use Pulumi ESC with Terraform.
weight: 2
menu:
  pulumiesc:
    parent: esc-other-integrations
    identifier: esc-other-integrations-terraform
---

## Overview

Pulumi ESC integrates with [Terraform](https://www.terraform.io) and [OpenTofu](https://opentofu.org) to help developers provision Terraform-managed infrastructure using centrally-managed, composable configuration and temporary credentials.

## Prerequisites

To complete the steps in this tutorial, you will need to install the following prerequisites:

- the [Pulumi ESC CLI](/docs/esc-cli/)
- the [Terraform CLI](https://developer.hashicorp.com/terraform/install)

{{% notes type="info" %}}
Although this guide is written for the Terraform CLI, OpenTofu users can also follow along by replacing the usage of the `terraform` commands with the equivalent `tofu` commands. In most cases, this is as simple as replacing `terraform` with `tofu`.
{{% /notes %}}

## Create and initialize a Terraform workspace

Create a directory to hold your infrastructure code, then copy and paste the following into a file named `main.tf`:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

variable "instance_type" {
  type = string
}

variable "region" {
  type = string
}

provider "aws" {
  region = var.region
}

data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm*"]
  }
}

resource "aws_instance" "app_server" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = var.instance_type

  tags = {
    Name = "ESCExampleAppServer"
  }
}
```

This sample code will create an EC2 instance running Amazon Linux 2. The instance's region and instance type are supplied by the user via [input variables](https://developer.hashicorp.com/terraform/language/values/variables).

Once you have created your `main.tf` file, run `terraform init` to install the necessary Terraform providers:

```bash
$ terraform init
```

## Create an ESC environment with Terraform variables

ESC integrates with Terraform by exporting environment variables from an opened environment. These environment variables typically come in two flavors: those used by Terraform providers and those used to provide values for Terraform input variables. The former are specific to each Terraform provider, while the latter are of the form [`TF_VAR_<variable name>`](https://developer.hashicorp.com/terraform/language/values/variables#environment-variables).

For this guide, we'll create an environment that supplies both temporary credentials for the Terraform AWS provider as well as values for our confguration's `region` and `instance_type` input variables:

```yaml
values:
  # Fetch temporary AWS credentials via OIDC
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: <your-oidc-iam-role-arn>
          sessionName: pulumi-environments-session
  environmentVariables:
    # Export AWS Credentials
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}

    # Export Terraform variables
    TF_VAR_region: us-west-2
    TF_VAR_instance_type: t3.small
```

## Run Terraform

Once you've created the example environment, you can now use the Terraform CLI with `esc run` to invoke Terraform with credentials and configuration:

```bash
$ esc run <your-env-name> -i -- terraform apply
```

This will open your ESC environment, export its environment variables, and then invoke `terraform apply` with those environment variables. The `-i` instructs `esc` to run in interactive mode, which is necessary for programs like the Terraform CLI that expect user input.

## Run Terraform with `-var-file`

While simple Terraform input variables work well with environment variables, it can be difficult to set variables with complex types (e.g. arrays, objects). If your Terraform input variables have complex types, you can use `-var-file` to supply their values.

```yaml
values:
  # Fetch temporary AWS credentials via OIDC
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: <your-oidc-iam-role-arn>
          sessionName: pulumi-environments-session
  files:
    TFVARS:
      fn::toJSON:
        region: us-west-2
        instance_type: t3.small
  environmentVariables:
    # Export AWS Credentials
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
```

With this environment, the `esc` CLI will write the value of the `TFVARS` property to a temporary file, then export the path to that temporary file in the `TFVARS` environment variable. You can then pass the path to this file to the Terraform CLI. This is slightly more involved because the Terraform CLI requires that the contents of the vars file is either valid HCL or JSON, and JSON files must have a `.json` extension:

```bash
$ esc run <your-env-name> -i -- sh -c 'mv $TFVARS $TFVARS.json && terraform apply -var-file=$TFVARS.json'
```
