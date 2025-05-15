---
title: "Evaluate Compliance of Terraform Resources"
title_tag: "Evaluate Compliance of Terraform Resources using Pulumi Insights"
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
    In this tutorial, you will learn how to use Pulumi Insights to discover and evaluate cloud resources for compliance, regardless of how they were deployed. [Pulumi Insights](/docs/insights/) can scan resources provisioned by any IaC tool, or even resources that were deployed manually. This tutorial will focus on scanning and evaluating AWS resources that are deployed using Terraform in particular, but the same approach applies to other major cloud providers and deployment methods.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to scan your cloud environment for resources
    - How to evaluate resources for policy violations

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud Team, Enterprise, or Business Critical account](https://app.pulumi.com/signup)
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
- A Security Group configured for public access
- An S3 bucket

## Scan Terraform resources

Now that you have deployed your resources, you will run a Pulumi Insights scan to retrieve a list of the resources in your account. To do so, navigate to the **Accounts** page in the [Pulumi Console](https://app.pulumi.com/) and click on your Pulumi Insights account. For the purposes of this tutorial, we have created an account named `pulumi-tutorials-insights`.

{{< video title="Navigating to Pulumi Insights accounts page" src="/tutorials/eval-compliance-terraform/assets/insights-nav-to-accounts.mp4" autoplay="true" loop="true" >}}

Once there, click on the **Actions** dropdown and select the `Scan` radio button, then click **Scan**. You will see a status message that says "Scan started a few seconds ago" once the scan has started.

{{< video title="Initializing account scan" src="/tutorials/eval-compliance-terraform/assets/insights-start-account-scan.mp4" autoplay="true" loop="true" >}}

To check on the status of the scan, you will need to navigate to the individual sub-accounts of your Pulumi insights account and click the **Scans** tab.

{{< video title="View sub-account scans" src="/tutorials/eval-compliance-terraform/assets/insights-view-sub-acct-scan.mp4" autoplay="true" loop="true" >}}

Once the scan has completed, the outline color of the scan will change to green, and the status will change to say "Scan #X succeeded in X minutes".

![Insights scan success message""](/tutorials/eval-compliance-terraform/assets/insights-scan-success.png)

Now you can view a list of your account resources by navigating to the **Resources** page in the console.

!["List of account resources in Insights"](/tutorials/eval-compliance-terraform/assets/insights-resources-list.png)

> If you have multiple Insights accounts, you can filter by your account name using the **Project** column filter. You can learn more about querying and filtering your resources by reviewing the [Pulumi Insights: Using Resources Explorer](/docs/insights/get-started/using-resource-explorer/) documentation.

## Configure compliance policies

Before you can evaluate your Terraform resources for policy violations, you must first create and deploy a Pulumi Insights Policy Pack. In this section, you will create a policy that enforces specific compliance for one of your AWS resources, more specifically for Security Groups.

### Create and publish a policy pack

To start, open your terminal and run the following command:

```bash
pulumi policy new aws-python
```

This will initialize your project, creating the necessary files for policy creation. Next, open the `main.py` file, paste in the following configuration, and save the file.

```python
from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

def security_group_no_public_ingress_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "aws:ec2/securityGroup:SecurityGroup":
        ingress_rules = args.props.get("ingress", [])
        for rule in ingress_rules:
            cidr_blocks = rule.get("cidrBlocks", [])
            if "0.0.0.0/0" in cidr_blocks:
                report_violation(
                    "Ingress rule allows public access from 0.0.0.0/0, which is prohibited. "
                    "Please restrict the CIDR blocks to specific IP ranges."
                )

security_group_no_public_ingress = ResourceValidationPolicy(
    name="security-group-no-public-ingress",
    description="Prohibits security group ingress rules that allow public access.",
    validate=security_group_no_public_ingress_validator,
)

PolicyPack(
    name="aws-security",
    enforcement_level=EnforcementLevel.MANDATORY,
    policies=[
        security_group_no_public_ingress,
    ],
)
```

This template sets up an example resource policy that prevents Security Groups from allowing public access, and it names the Policy Pack `aws-security`. To publish this template to your Pulumi organization, run the following command:

```bash
pulumi policy publish
```

### Add policy pack to an Insights Account

With your policy pack published, you’ll need to create a Policy Group that associates your Insights account with a policy pack. In the Pulumi Cloud console, navigate to **Policies** under the **Pulumi Insights** section.

![Insights Policies - New Policy Pack](/docs/insights/assets/create-policy-group.png)

Next, click **Create policy group** and provide a descriptive name, such as "sg-security-policy-group" Then click **Add policy group**. Once your policy group has been created, click on the name of the policy group to open its configuration page, and then click **Add policy pack**.

!["Adding a policy pack"](/tutorials/eval-compliance-terraform/assets/insights-add-policy-pack.png)

Select your newly published policy pack from the dropdown and choose the version you want to enforce. Here you can configure the enforcement level at either a global level for all policies in your policy pack, or a granular level for each individual policy check. For the purposes of this tutorial, select the enforcement level of `advisory` under **All**, then click **Enable** to confirm your settings.

!["Configuring the policy pack"](/tutorials/eval-compliance-terraform/assets/insights-configure-policy-pack.png)

The last thing you need to do in this section is add your insights account to the policy group. On your Policy Group configuration page, click **Add accounts**, and type the name of the account you want to include for Insights policies (e.g. pulumi-tutorials-insights/us-west-2). Then click **Add account to policy group**.

!["Adding an account to the policy group"](/tutorials/eval-compliance-terraform/assets/insights-add-policy-group-acct.png)

> If you want to learn more about creating custom Policy Packs in Pulumi, you can refer to our [Creating a Custom Policy Pack](/tutorials/custom-policy-pack/) tutorial series.

## Evaluate Terraform resources

Now that your policy pack has been deployed and your account has been associated with it, you can evaluate your discovered AWS resources against the policy. To do so, navigate back to the **Accounts** section and select your account. Click the **Actions** dropdown button, select the **Scan** radio button, and then click **Scan**.

As the scan progresses, you can monitor policy compliance in real-time through the **Policy Violations** page in the Pulumi Cloud Console.

![Insights Policies - Policy Violations](/tutorials/eval-compliance-terraform/assets/insights-policy-violations.png)

You should see a violation entry for the publically accessible security group in the list. Each violation entry provides detailed information about:

- The specific resource that triggered the violation
- Which policy rule was violated
- Contextual information to help understand why the resource is non-compliant

## Clean up

If needed, you can tear down the example Terraform resources by running the `terraform destroy` command.

## Next steps

In this tutorial, you used Pulumi Insights to scan your AWS account for resources that were deployed using Terraform. You also created and deployed a policy pack and evaluated your resources against the defined policy.

To learn more about Pulumi services, take a look at the following resources:

- Learn more about the Pulumi Cloud in the [Pulumi Cloud](/docs/pulumi-cloud/) documentation.
- Learn more about how you can use Pulumi to centrally manage configuration and secrets in the [Pulumi ESC](/docs/esc/) documentation.
- Learn how you can deploy cloud resources uses modern programming languages in the [Pulumi IaC](/docs/iac/) documentation.
