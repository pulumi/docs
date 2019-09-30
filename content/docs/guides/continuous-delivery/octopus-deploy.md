---
title: Octopus Deploy

menu:
    userguides:
        parent: cont_delivery
        weight: 1
---

[Octopus](https://octopus.com) is a deployment automation server, designed to make it easy to orchestrate releases and deploy applications, whether on-premises or in the cloud. Octopus is unlike a traditional CI system. In fact, Octopus is not a CI system. However, it can integrate with your existing build pipeline and integrate with several of your existing CI systems, like Jenkins, TeamCity, Azure DevOps etc.

## Prerequisites

- A working installation of Octopus or a hosted instance from https://octopus.com.
- An account on the [Pulumi Console](https://app.pulumi.com).
- The latest version of Pulumi. Installation instructions are [here]({{< relref "/docs/get-started/install" >}}).
- Setup a new project and [stack]({{< relref "/docs/intro/concepts/stack" >}}) using one of our [Get Started]({{< relref "/docs/get-started" >}}) guides or simply by running [`pulumi new`]({{< relref "/docs/reference/cli/pulumi_new.md" >}})
and choosing one of the many templates that are available.
- A bare repo and set the remote URL to be your GitHub project.

## Sample Project

For the sake of this walkthrough, we will try to deploy the simple AWS example located [here](https://github.com/pulumi/examples/tree/master/aws-ts-hello-fargate). The example deploys a containerized Python Flask app on [AWS Fargate](https://aws.amazon.com/fargate/). This example also shows a pattern that is common with Pulumi -- keeping your infrastructure app (Pulumi) with your actual application code, but certainly not necessary. Regardless of how you decide to structure your project, you will need to provide the package to Octopus somehow.

Alternatively, you can also run `pulumi new [template]` to create a template project.
Learn more [here]({{< ref "/docs/reference/cli/pulumi_new.md" >}}).

## Stack and Branch Mappings

The scripts below act on a hypothetical stack: `homer/acme-org/python-app`.
You can create a new stack by running [`pulumi stack init`]({{< relref "/docs/reference/cli/pulumi_stack_init.md" >}}) if you have already created a project.

**Note**: The names used above are purely for demonstration purposes only.
You may choose a naming convention that best suits your organization.

## PULUMI_ACCESS_TOKEN

To login non-interactively in to the CLI, you will need to set the env var `PULUMI_ACCESS_TOKEN` as a build parameter when setting up the Jenkins build. To create a new access token, go the [Access Tokens](https://app.pulumi.com/account/tokens) page on the Pulumi Console.


