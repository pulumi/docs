---
title: Octopus Deploy

menu:
    userguides:
        parent: cont_delivery
        weight: 1
---

[Octopus Deploy](https://octopus.com) is a deployment automation server, designed to make it easy to orchestrate releases and deploy applications, whether on-premises or in the cloud. Octopus is unlike a traditional CI system. In fact, Octopus is not a CI system. However, it can integrate with your existing build pipeline and integrate with several of your existing CI systems, like Jenkins, TeamCity, Azure DevOps etc.

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

To login non-interactively in to the CLI, you will need to set the env var `PULUMI_ACCESS_TOKEN` as a [project variable](https://octopus.com/docs/deployment-process/variables). To create a new access token, go the [Access Tokens](https://app.pulumi.com/account/tokens) page on the Pulumi Console.

## Octopus Setup

### Infrastructure

Infrastructure in Octopus is represented as deployment targets and workers (tentacles or SSH machines). Additionally, you can also have environments which is a logical grouping of deployment targets and workers that represents each of your environments.

In a typical scenario where Pulumi is creating your cloud infrastructure, you will only need to a worker that can run the Pulumi CLI commands against your code package.

### Project

A project represents the application being deployed. A project uses versioned packages (which you will read about in the following section) and uses variables during the deployment process.

### Packages

Packages can be your source code bundled-up in one of the [supported formats](https://octopus.com/docs/packaging-applications#supported-formats). They can also just be a handlful of scripts that you may want to use during your deployment process.

In order to create a package, Octopus offers several ways that you can integrate into your existing build (CI) system. [Learn more](https://octopus.com/docs/packaging-applications/create-packages) about the options available to you for packaging your apps.

For Pulumi apps, you can simply package the entire Pulumi app and extract the bundled package onto a worker where the Pulumi CLI can access them.

## Create and configure a project

A [deployment process](https://octopus.com/docs/deployment-process) is comprised of the following steps:

- Configure Project Variables
- Create the Process

### Configure Project Variables
You can configure your AWS Account and Azure Subscription credentials as project variables using the built-in `AWS Account` and `Azure Subscription` variable types. Before you can do that, though, you will need to add them to the **Accounts** section under **Infrastructure** in your Octopus instance.

For other cloud providers, you will need to add the account credentials directly as a project variable using the appropriate built-in variable type.

Variables can be scoped right down to the environment that can access them. For sensitive strings, be sure to set the right scopes so that the account credentials are not accidentally used by the wrong environments.

### Create the Process

A process consists of the steps to execute in a project. The following sections outline the steps for configuring your process in order to use Pulumi to deploy infrastructure (not be confused with Octopus Infrastructure).

#### Extract the code package

- Click on the **Add Step** button in your project's **Process** section.
- Click the **Referenced Packages** and choose the package that contains your Pulumi infrastructure app.
  - **Package feed**: Choose the appropriate source for your package.
  - **Package ID**: This is usually derived from your package, but enter a name of your choice. This ID will be used later.
  - **Package Name**: Enter any name.
  ![Add Package Reference](/images/docs/guides/continuous-delivery/octopus-deploy/package-reference.png)
- Select the **Run a Script**, fill out the following fields as follows:
  - **Script Source**: Inline source code
  - **Inline Source Code**: (click the **Bash** radio button)
  ```bash
    # Remove any previously extracted packages
    rm -rf /tmp/pulumi-app
    # Use the pre-defined variable to get the extracted path for the package.
    extractedPath=$(get_octopusvariable "Octopus.Action.Package[aws-typescript].ExtractedPath")
    # Copy the extracted package contents to another directory that can be accessed by other steps.
    cp -r "${extractedPath}/infrastructure/" /tmp/pulumi-app
    cd /tmp/pulumi-app
  ```

#### Run Pulumi

- Click on **Add Step** again and search for `Pulumi` from the **Community Library Steps**.
- Fill out the configuration as appropriate for your stack.
  - For example, in the following screenshot the stack configuration is overridden using a
file that is created in a separate **Run a script** step.
  - It is not required that you override stack configuration. It was done here purely for demonstrating
  the options you have with the Pulumi Step Template.
![Add Package Reference](/images/docs/guides/continuous-delivery/octopus-deploy/run-pulumi.png)

The next steps are to simply create a release from the latest package from the package feed and deploy it.
Click on **Releases** under the **Projects** tab and click on **Create Release**, and follow on-screen instructions.

## Additional Information

### Manual Intervention Steps
Since Octopus Deploy is a _deployment_ automation server it does not inherit the capabilities of a traditional VCS wherein you have Pull Request or Push builds. With Pulumi modifying your infrastructure, you may be interested in running `pulumi preview` first, then run `pulumi up` but only if the `preview` looks right to you. One way to do this is, to add a [Manual Intervention and Approval Step](https://octopus.com/docs/deployment-process/steps/manual-intervention-and-approvals). With this step, you can effectively pause the deployment of your infrastructure changes until someone has signed-off on it. This is desirable in a team-based environment where several members might be making changes.

### Variable Sets
We showed you at a high-level how you could use Project Variables to inject sensitive values in to your deployment process. Octopus Deploy also supports [Variable Sets](https://octopus.com/docs/deployment-process/variables/library-variable-sets) which are variables that are common across deployment environments. Variable Sets can be scoped just like regular Project-specific variables. [Learn more](https://octopus.com/docs/deployment-process/variables) about all of the ways you can make use of the rich configuration system in Octopus Deploy.
