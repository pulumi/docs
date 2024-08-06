---
title_tag: "Managing the State of Pulumi Resources | Tutorials"
meta_desc: Learn how to manage resources in Pulumi state in this tutorial.
title: "Managing the State of Pulumi Resources"
h1: "Managing the State of Pulumi Resources"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  usingpulumi:
    identifier: managing-pulumi-state
    weight: 1
tags:
    - resources
    - state
    - infrastructure
    - fundamentals
    - tutorial
---

[INTRO]

## Prerequisites

This tutorial assumes that you are familiar with the basics of the Pulumi workflow. If you are new to Pulumi, complete the [Get Started series](/docs/get-started/) first.

Additionally, you will need the following tools to complete this tutorial:

- A [Pulumi account](https://app.pulumi.com)
  - [Optional] Create an [access token](/docs/pulumi-cloud/access-management/access-tokens/)
- The [Pulumi CLI](https://www.pulumi.com/docs/install/)
- An [Amazon Web Services](https://aws.amazon.com/) account
- The [AWS CLI](https://aws.amazon.com/cli/)
- Your desired [language runtime installed](/docs/clouds/aws/get-started/begin/#install-language-runtime)

Let's get started!

## [Optional] Create a New Project

{{< notes type="info" >}}

The commands found in this tutorial can be run against any projects or stacks that you may have already created. Feel free to skip this step and use your own project/stack if that is the case.

{{< /notes >}}

To start, login to the [Pulumi CLI](/docs/cli/commands/pulumi_login/) and ensure it is [configured to use your AWS account](/docs/clouds/aws/get-started/begin/#configure-pulumi-to-access-your-aws-account). Next, [create a new project](/docs/clouds/aws/get-started/create-project/) and replace the default program code with the following:

{{< example-program path="aws-ec2-sg-nginx-server-python" >}}

This code example creates the following resources:

- An EC2 instance configured with Nginx
- A Security Group configured for public access

It also includes one export that will output value of the server's IP address.

Now run the `pulumi up` command to deploy your resources before moving onto the next steps.

{{< notes type="warning" >}}

For the purposes of this tutorial, we will be creating our resources in AWS in the `us-east-1` region. If you are deploying resources in a region other than the `us-east-1` region, make sure to replace the AMI ID value with the ID that is [specific to your region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html). Otherwise you may run into an `InvalidAMIID.NotFound` error.

{{< /notes >}}

## Examine State with the CLI

Now that you have deployed your program code, a state file has been created that tracks the resources created by Pulumi. You can view the contents of the state file with the `pulumi stack export` command. By default, this will output the contents of the state file to the command line, but you can pipe the output to a file for easier viewing and modification. Run the `pulumi stack export > state.json` to export the contents of your Pulumi state to the `state.json` file:

[VIDEO]

### Explore the state resources

While it is not recommended to manually manage or edit your infrastructure via the state file, there may be scenarios in which this becomes necessary such as correcting inconsistencies in a stack's state due to failed deployments or if there were any manual changes made to cloud resources.

## Clean up

{{< cleanup >}}

## Next Steps

In this tutorial, you ...

To learn more about creating resources in Pulumi, take a look at the following resources:

- Learn more about stack outputs and references in the [Stack Outputs and References](/docs/using-pulumi/stack-outputs-and-references/) tutorial.
- Learn more about inputs and outputs in the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation.
- Learn more about [resource names](/docs/concepts/resources/names/), [options](/docs/concepts/options/), and [providers](/docs/concepts/resources/providers/) in the Pulumi documentation.
