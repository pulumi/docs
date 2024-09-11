---
title: "Inspecting Infrastructure"
title_tag: "Inspecting Infrastructure"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn how to inspect your Pulumi resources in this tutorial.

# A similar description used for search results and social-media previews.
meta_desc: Learn how to inspect your Pulumi resources in this tutorial.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: inspect-infra-meta.png

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
    Pulumi configurations and state data include highly structured information about the resources they manage, such as dependency information, outputs, and more. The Pulumi CLI includes commands for inspecting this data. You can use these to integrate other tools with Pulumi's infrastructure data, or just to gain a deeper or more holistic understanding of your infrastructure.

    In this tutorial, we'll demonstrate the various ways you can use the Pulumi CLI to inspect your infrastructure.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to view your stack's status, outputs, and configurations
    - How to view the state file of your stack
    - How to view the dependency graph of your stack's resources
    - How to preview a dry-run of your stacks updates
    - How to view your stack's details in the Pulumi Cloud

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - A [Pulumi account](https://app.pulumi.com) and [access token](/docs/pulumi-cloud/access-management/access-tokens/)
    - The [Pulumi CLI](https://www.pulumi.com/docs/install/)
    - An [Amazon Web Services](https://aws.amazon.com/) account
    - The [AWS CLI](https://aws.amazon.com/cli/)
    - Your desired [language runtime installed](/docs/clouds/aws/get-started/begin/#install-language-runtime)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 10

# # An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
# collections:
#     - some-non-existent-collection
---

## [Optional] Create a new project

{{< notes type="info" >}}

The commands found in this tutorial can be run against any projects or stacks that you may have already created. Feel free to skip this step and use your own project/stack if that is the case.

{{< /notes >}}

To start, login to the [Pulumi CLI](/docs/cli/commands/pulumi_login/) and ensure it is [configured to use your AWS account](/docs/clouds/aws/get-started/begin/#configure-pulumi-to-access-your-aws-account). Next, [create a new project](/docs/clouds/aws/get-started/create-project/) and replace the default program code with the following:

{{< example-program path="aws-s3bucket-bucketpolicy" >}}

This code example creates the following resources:

- An S3 bucket
- An S3 bucket policy definition
- An S3 bucket policy attachment

It also includes two exports that will output the name and ARN of the S3 bucket.

Now run the `pulumi up` command to deploy your resources before moving onto the next steps.

## Inspect your infrastructure

In this section, you will run a number of commands in the Pulumi CLI that will enable you to view more details about the resources you have deployed.

### pulumi stack

The [pulumi stack](/docs/cli/commands/pulumi_stack/) command is used to provide a quick overview of the current stack's status and configuration. Running this command will list the management details, resources, and [output](/docs/concepts/inputs-outputs/#outputs) names and values of the current stack.

Run the `pulumi stack` command as shown below:

{{< video title="Running the pulumi stack command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-stack.mp4" autoplay="true" loop="true" >}}

### pulumi stack graph

The [pulumi stack graph <filename>](/docs/cli/commands/pulumi_stack_graph/) command is used to visualize the dependency graph of a Pulumi stack. This graphical representation can help users to understand the relationships and dependencies between resources in their infrastructure.

Run the `pulumi stack graph <filename>` command as shown below, making sure to replace `<filename>` with the name of the file that you want the graph to be exported to:

{{< video title="Running the pulumi stack graph command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-stack-graph.mp4" autoplay="true" loop="true" >}}

{{< notes type="info" >}}

The output of the file will be in Graphviz DOT format. You can use an online viewer such as [GraphvizOnline](https://dreampuf.github.io/GraphvizOnline) to view a visual representation of the graph.

{{< /notes >}}

### pulumi stack output

The [pulumi stack output](/docs/cli/commands/pulumi_stack_output/) command is used to list all output names and values that are exported from a stack. This command helps to facilitate automation workflows and integration with other tools and scripts by providing easy access to important output values.

Run the `pulumi stack output` command as shown below:

{{< video title="Running the pulumi stack output command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-stack-output.mp4" autoplay="true" loop="true" >}}

You can return the value of just a single output by adding the name of the desired output property to the command. To demonstrate, run the `pulumi stack output <outputname>` command, replacing `<outputname>` with one of the output names of your stack.

{{< video title="Running the pulumi stack output command for a single output" src="https://www.pulumi.com/uploads/aws-cli-pulumi-stack-output-single.mp4" autoplay="true" loop="true" >}}

### pulumi stack export

The [pulumi stack export](/docs/cli/commands/pulumi_stack_export/) command is used to export the current state of a stack in JSON format to standard out. This state definition contains all the information about the resources, their states, and the configuration of the stack. The exported state can be used for things like backup, migration, or debugging purposes.

Run the `pulumi stack export` command as shown below:

{{< video title="Running the pulumi stack export command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-stack-export.mp4" autoplay="true" loop="true" >}}

### pulumi preview

The [pulumi preview](/docs/cli/commands/pulumi_preview/) command is an important tool for understanding the changes that will be made to your infrastructure before actually applying them. It does a dry run of the update, showing a detailed preview of the resources that will be created, updated, or deleted without making any actual changes to your cloud resources.

Before running this command, you will need to make a change to your Pulumi program. Change the name of your S3 bucket resource and then save your file.

{{< video title="Making a small change to the program code" src="https://www.pulumi.com/uploads/aws-cli-pulumi-preview-change.mp4" autoplay="true" loop="true" >}}

Now run the `pulumi preview` command to display a preview of the updates that will be made:

{{< video title="Running the pulumi preview command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-preview.mp4" autoplay="true" loop="true" >}}

### pulumi console

The [pulumi console](/docs/cli/commands/pulumi_console/) command opens the current stack in the Pulumi Console, providing a graphical user interface to view and manage your Pulumi stack and resources. From there, you can view detailed information about the stack such as its resources, outputs, and configuration values.

{{< video title="Running the pulumi console command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-console.mp4" autoplay="true" loop="true" >}}

## Clean up

{{< cleanup >}}

## Next steps

In this tutorial, you used a variety of Pulumi CLI commands to view more details about your infrastructure. To learn more about creating and managing resources in Pulumi, take a look at the following resources:

- Learn more about the available CLI commands in the [Pulumi CLI documentation](/docs/cli/commands/).
- Learn more about stack outputs and references in the [Stack Outputs and References](/tutorials/stack-outputs-and-references/) tutorial.
