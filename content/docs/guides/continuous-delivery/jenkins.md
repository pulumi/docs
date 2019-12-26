---
title: Jenkins Pipeline
meta_desc: This document will help you setup a Jenkins Pipeline to deploy a sample app to Azure using Pulumi.
menu:
    userguides:
        parent: cont_delivery
        weight: 1

aliases: ["/docs/console/continuous-delivery/jenkins/"]
---

This document will help you setup a [Jenkins Pipeline](https://jenkins.io/doc/book/pipeline/) to deploy a sample app to Azure using Pulumi.
The source code will be hosted on GitHub just for the purpose of showing the GitHub integration between Jenkins and GitHub. Your source repository could be on any other VCS supported by Jenkins.

Pulumi doesn't require any particular arrangement of stacks or workflow to work in a
continuous integration / continuous deployment system. So the steps described here can be
altered to fit into any existing type of deployment setup.

## Prerequisites

- A working installation of a recent version of Jenkins.
- An account on the [Pulumi Console](https://app.pulumi.com).
- The latest version of Pulumi. Installation instructions are [here]({{< relref "/docs/get-started/install" >}}).
- Setup a new project and [stack]({{< relref "/docs/intro/concepts/stack" >}}) using one of our [Get Started]({{< relref "/docs/get-started" >}}) guides or simply by running [`pulumi new`]({{< relref "/docs/reference/cli/pulumi_new.md" >}})
and choosing one of the many templates that are available.
- A bare repo and set the remote URL to be your GitHub project.

## Sample Project

An example project is located [here](https://github.com/pulumi/examples/tree/master/azure-ts-appservice-springboot). You may download the project and upload it to your own repo to avoid having to clone the entire Pulumi Examples repo into your Jenkins workspace.

## Stack and Branch Mappings

The scripts below act on a hypothetical stack: `homer/acme/product-catalog-service-stack`.
You can create a new stack by running [`pulumi stack init`]({{< relref "/docs/reference/cli/pulumi_stack_init.md" >}}) if you have already created a project.
The source code for the stack is in a repository in GitHub and uses TypeScript as the language.

**Note**: The names used above are purely for demonstration purposes only.
You may choose a naming convention that best suits your organization.

Alternatively, you can also run `pulumi new [template]` to create a template project.
Learn more [here]({{< relref "/docs/reference/cli/pulumi_new.md" >}}).

## PULUMI_ACCESS_TOKEN

To login non-interactively in to the CLI, you will need to set the env var `PULUMI_ACCESS_TOKEN` as a build parameter when setting up the Jenkins build. To create a new access token, go the [Access Tokens](https://app.pulumi.com/account/tokens) page on the Pulumi Console.

## Creating a New Jenkins Build

### Classic UI

The classic UI lets you create manual (UI) builds, as well as a Declarative pipeline-based build. There are several options available to cater to your specific setup, but for the purposes of this walkthrough, we will assume a single branch, declarative pipeline.

### Jenkins Blue Ocean

Blue Ocean is an overhaul of the classic Jenkins UI. It features a new and intuitive pipeline configuration UI that helps you setup a CI pipeline in a matter of just minutes. [Learn more](https://jenkins.io/projects/blueocean/) about the Jenkins Blue Ocean project.

**Note** Regardless of the type of interface you choose to work with, the `Jenkinsfile` (more on that later) can be used interchangeably with both. The underlying pipeline configuration system is the same.

### Plugins

Ensure you have the following plugins installed:

- Git
- NodeJS

You can find available plugins by navigating to the Jenkins administration page and then selecting the **Manage Plugins** option on the Manage Jenkins page.

### Project Parameters (Environment Variables)

In order to deploy to one of the cloud providers, you will need to ensure that the authentication environment variables are set, so that the Pulumi CLI can use them to deploy your infrastructure resources. The set of environment variables to configure vary for each cloud. For Azure, depending on your setup, you may have to set at most 4 environment variables. In this example, we will assume you are using a [Service Principal]({{< relref "/docs/intro/cloud-providers/azure/setup#creating-a-service-principal" >}}).

The screenshot below shows you how you can parameterize your `Jenkinsfile` using environment variables.

![Jenkins Project Parameters](/images/docs/reference/jenkins/project-params.png)

#### Configuring the Node JS plugin

In order to use the Node JS plugin, you must first ensure you add at least one installation to it. Navigate to the **Global Tool Configuration** menu option on the Manage Jenkins page.

**Note** The name you enter in the configuration section will later be referenced in the `Jenkinsfile`, so be sure to save that name somewhere so you can easily copy/paste it into your pipeline configuration.

![Jenkins Global Tool Configuration](/images/docs/reference/jenkins/global-tool-config.png)

### Jenkinsfile

```groovy
pipeline {
    agent any

    stages {
        stage ("Checkout code") {
            steps {
                git url: "git@github.com:your-github-account/you-repo.git",
                    // Set your credentials id value here.
                    // See https://jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials
                    credentialsId: "yourCredentialsId",
                    // You could define a new stage that specifically runs for, say, feature/* branches
                    // and run only "pulumi preview" for those.
                    branch: "master"
            }
        }

        stage ("Install dependencies") {
            steps {
                sh "curl -fsSL https://get.pulumi.com | sh"
                sh "$HOME/.pulumi/bin/pulumi version"
            }
        }

        stage ("Pulumi up") {
            steps {
                // The value "node 8.9.4" is the configuration name in our Global Tool Configuration setup for node.
                // You should use the name that you used when you added the installation on that page.
                nodejs(nodeJSInstallationName: "node 8.9.4") {
                    withEnv(["PATH+PULUMI=$HOME/.pulumi/bin"]) {
                        sh "cd infrastructure && npm install"
                        sh "pulumi stack select ${PULUMI_STACK} --cwd infrastructure/"
                        sh "pulumi up --yes --cwd infrastructure/"
                    }
                }
            }
        }
    }
}
```

## Additional Information

### Single-quotes vs. double-quotes in Jenkinsfile

While the pipeline script editor may not complain about the use of single-quotes, we have noticed that using single-quotes can cause certain commands to silently fail. It is better to use double-quotes always to wrap arguments in your `Jenkinsfile`.

### The Manage Jenkins page

You can get to the administration in one of two ways depending on which UI (Classic vs. Blue Ocean) you are using. In the Classic UI, there is a **Manage Jenkins** link on the left nav menu, and in Blue Ocean you should see an **Administration** link on the top nav. You will only see these options if you are an admin in your Jenkins installation.

### Using the withCredentials binding plugin

Jenkins allows you to manage credentials in a global credentials store. Learn more [here](https://jenkins.io/doc/pipeline/steps/credentials-binding/). By using the `withCredentials` plugin, you could store your AWS, Azure or GCP credentials in the credentials store, and inject it into the pipeline easily. For example, in order to use the Azure CLI credentials, you will need the Azure CLI plugin additionally. Once added, you can add a new Service Principal credential and map its properties to the appropriate env variables needed by the Pulumi CLI.

```groovy
...
withCredentials([azureServicePrincipal(credentialsId: "your-credentials-id", clientIdVariable: "ARM_CLIENT_ID", clientSecretVariable: "ARM_CLIENT_SECRET", subscriptionIdVariable: "ARM_SUBSCRIPTION_ID", tenantIdVariable: "ARM_TENANT_ID")]) {
    ...
    sh "pulumi preview"
}
...
```
