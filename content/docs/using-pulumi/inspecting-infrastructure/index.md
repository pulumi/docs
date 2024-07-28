---
title_tag: "Inspecting Infrastructure | Tutorials"
meta_desc: Learn how to inspect your Pulumi resources in this tutorial.
title: "Inspecting Infrastructure"
h1: "Inspecting Infrastructure"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  usingpulumi:
    identifier: inspecting-infrastructure
    weight: 1
tags:
    - resources
    - infrastructure
    - fundamentals
    - tutorial
---

Pulumi configurations and state data include highly structured information about the resources they manage, such as dependency information, [outputs](/docs/concepts/inputs-outputs/#outputs), and more.

The Pulumi CLI includes some commands for inspecting this data. You can use these to integrate other tools with Pulumi's infrastructure data, or just to gain a deeper or more holistic understanding of your infrastructure.

In this tutorial, we'll demonstrate the various ways you can use the Pulumi CLI to inspect your infrastructure.

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

## Create a New Project

To start, login to the [Pulumi CLI](/docs/cli/commands/pulumi_login/) and ensure it is [configured to use your AWS account](/docs/clouds/aws/get-started/begin/#configure-pulumi-to-access-your-aws-account). Next, [create a new project](/docs/clouds/aws/get-started/create-project/) and replace the default program code with the following:

{{< example-program path="aws-s3bucket-bucketpolicy" >}}

Then run the `pulumi up` command to deploy your resources.

## Inspect your Infrastructure

In this section, you will run a number of commands in the Pulumi CLI that will enable you to view more details about the resources you have deployed.

### pulumi stack

The [pulumi stack](/docs/cli/commands/pulumi_stack/) command to provide a quick overview of the current stack's status and configuration. Running this command will list the management details, resources, and output names and values of the current stack.

Run the `pulumi stack` command as shown below:

{{< video title="Running the pulumi stack command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-stack.mp4" autoplay="true" loop="true" >}}

### pulumi stack graph

The [pulumi stack graph <filename>](/docs/cli/commands/pulumi_stack_graph/) command is used to visualize the dependency graph of a Pulumi stack. This graphical representation can help users to understand the relationships and dependencies between resources in their infrastructure.

Run the `pulumi stack graph <filename>` command as shown below, making sure to replace `<filename>` with the name of the file that you want the graph to be exported to:

{{< video title="Running the pulumi stack graph command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-stack-graph.mp4" autoplay="true" loop="true" >}}

### pulumi stack output

The [pulumi stack output](/docs/cli/commands/pulumi_stack_output/) command is used to list all output names and values that are exported from a stack. This command helps to facilitate automation workflows and integration with other tools and scripts by providing easy access to important output values.

Run the `pulumi stack output` command as shown below:

{{< video title="Running the pulumi stack output command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-stack-output.mp4" autoplay="true" loop="true" >}}

If a specific property-name is supplied, just that property’s value is shown. To demonstrate, run the `pulumi stack output <outputname>` command, replacing `<outputname>` with one of the output names of your stack.

{{< video title="Running the pulumi stack output command for a single output" src="https://www.pulumi.com/uploads/aws-cli-pulumi-stack-output-single.mp4" autoplay="true" loop="true" >}}

### pulumi stack export

The [pulumi stack export](/docs/cli/commands/pulumi_stack_export/) command is used to export the current state of a stack to standard out. This state definition contains all the information about the resources, their states, and the configuration of the stack. The exported state can be used for things like backup, migration, or debugging purposes.

Run the `pulumi stack export` command as shown below:

{{< video title="Running the pulumi stack export command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-stack-export.mp4" autoplay="true" loop="true" >}}

### pulumi preview

The [pulumi preview](/docs/cli/commands/pulumi_preview/) command is an important tool for understanding the changes that will be made to your infrastructure before actually applying them. It simulates the update, showing a detailed preview of the resources that will be created, updated, or deleted without making any actual changes to your cloud resources.

Before running this command, you will need to make a change to your Pulumi program. Change the name of your S3 bucket resource and then save your file.

{{< video title="Making a small change to the program code" src="https://www.pulumi.com/uploads/aws-cli-pulumi-preview-change.mp4" autoplay="true" loop="true" >}}

Now run the `pulumi preview` command to display a preview of the updates that will be made:

{{< video title="Running the pulumi preview command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-preview.mp4" autoplay="true" loop="true" >}}

### pulumi console

The [pulumi console](/docs/cli/commands/pulumi_console/) command opens the current stack in the Pulumi Console, providing a graphica user interface to view and manage your Pulumi stack and resources. From there, you can view detailed information about the stack such as its resources, outputs, and configuration values.

{{< video title="Running the pulumi console command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-console.mp4" autoplay="true" loop="true" >}}

## Clean Up

{{< cleanup >}}

## Next Steps

In this tutorial, you used a variety of Pulumi CLI commands to view more details about your infrastructure.

To learn more about creating and managing resources in Pulumi, take a look at the following resources:

- Learn more about the available CLI commands in the [Pulumi CLI documentation](/docs/cli/commands/).
- Learn more about stack outputs and references in the [Stack Outputs and References](/docs/using-pulumi/stack-outputs-and-references/) tutorial.

