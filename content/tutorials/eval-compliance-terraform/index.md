---
title: "Evaluate Compliance of Terraform Resources"
title_tag: "Evaluate Compliance of Terraform Resources"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn how to use Pulumi Insights to evaluate compliance of resources that are deployed with Terraform.

# A similar description used for search results and social-media previews.
meta_desc: Learn how to use Pulumi Insights to evaluate compliance of resources that are deployed with Terraform.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: meta.png

# An optional video for the tutorial. When present, it appears at the top of the page, replacing
# the meta image. YouTube and HTML5 video sources are supported.
# video:
#     url: /blog/drift-detection/drift.mp4
#     youtube: Q8tw6YTD3ac

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
    In this tutorial, you will learn how to use Pulumi Insights to evaluate compliance of cloud resources, specifically resources that have been deployed using Terraform. The examples in this tutorial will demonstrate how to scan and evaluate resources in the AWS cloud, but the steps are equally applicable to the other major cloud providers.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to scan your cloud environment for resources
    - How to evaluate resources for policy violations

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud Team, Enterprise, or Business Critical account](https://app.pulumi.com/signup)
    - A Pulumi Cloud [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - An [ESC environment and AWS credentials created and configured](/docs/insights/get-started/begin/)
    - A [Pulumi Insights account](/docs/insights/get-started/create-accounts/)
    - An [Amazon Web Services](https://aws.amazon.com/) account
    - The [AWS CLI](https://aws.amazon.com/cli/) configured for use with your AWS account
    - The [Terraform CLI](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 15

# # An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
# collections:
#     - some-non-existent-collection
---

## Deploy Terraform resources

This step is optional if you already have Terraform resources deployed in your AWS account. Otherwise, you can start by creating a new project folder and Terraform file:

```bash
$ mkdir pulumi-insights-terraform-resources && cd pulumi-insights-terraform-resources
$ touch main.tf
```

Open the `main.tf` file, paste in the following configuration, and save the file.

```terraform
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}

resource "aws_security_group" "http_access" {
  name        = "http_access"
  description = "SG module Achintha Bandaranaike"

  ingress {
    from_port   = "22"
    to_port     = "22"
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_s3_bucket" "tf-tutorial-test-s3-bucket" {
  bucket = "tf-tutorial-test-s3-bucket"
}
```

Then run the `terraform apply` command to have the following resources deployed into your account:

- An EC2 instance
- A Security Group
- An S3 bucket

## Scan Terraform resources

TBD

## Deploy compliance policies

TBD

## Evaluate Terraform resources

TBD
