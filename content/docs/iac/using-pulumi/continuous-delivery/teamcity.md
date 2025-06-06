---
title_tag: "Using JetBrains TeamCity | CI/CD"
meta_desc: "This page provides an overview of how to use Pulumi with JetBrains TeamCity."
title: JetBrains TeamCity
h1: Pulumi CI/CD & JetBrains TeamCity
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: TeamCity
        parent: iac-using-pulumi-cicd
        weight: 15
aliases:
- /docs/guides/continuous-delivery/teamcity/
- /docs/using-pulumi/continuous-delivery/teamcity/
- /docs/iac/packages-and-automation/continuous-delivery/teamcity/
---

This page details how to use [JetBrains TeamCity](https://www.jetbrains.com/teamcity/) to deploy a sample infrastructure, using Pulumi. In the example below, we will deploy to AWS, but any cloud can be used.

## Prerequisites

- A working installation of TeamCity
- An account in the [Pulumi Cloud](https://app.pulumi.com).
- [Latest version of Pulumi](/docs/install/).
- Setup a new project and [stack](/docs/concepts/stack/) using one of our
[Get Started](/docs/get-started/) guides or by running [`pulumi new`](/docs/cli/commands/pulumi_new)
and choosing one of the many templates that are available.

## Sample Project

[Example Repository](https://github.com/pulumi/examples/tree/master/aws-ts-hello-fargate).
You may download the project and upload it to your own repo to avoid having to clone the entire Pulumi Examples repo onto
your TeamCity server.

## Configuring the TeamCity Project

For the purposes of this guide, we are going to build a TeamCity project via the UI. An alternative way to do this, would
be to use the [Kotlin DSL](https://www.jetbrains.com/help/teamcity/kotlin-dsl.html).

When creating a new project via the UI, we will see the project creation wizard. We are going to create a project
`From a repository URL` from the [Pulumi Examples](https://github.com/pulumi/examples) repository. This specific
repository is open source so we do not need to enter a `Username` and `Password`. We can then instruct TeamCity to
proceed to the next step.

TeamCity will tell us if it can successfully connect to the repository. If it can, then it will ask us to name this project
and to create a [build configuration](https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html) name. We are going to
name the project `Examples` and we will create a build configuration called `Tutorial`. We can then `Proceed` to the next step.
We can click the link that says `configure build steps manually` and then can start creating our project.

A TeamCity configuration is made of [build steps](https://www.jetbrains.com/help/teamcity/configuring-build-steps.html).
We can break down the steps required for us to deploy this application into a number of build steps.

### Install NodeJS and NPM Build Step

The first thing we need to do is to ensure that [NodeJS](https://nodejs.org/en/) and [NPM](https://www.npmjs.com/) are
installed on our build agents. We would chose `Command Line` as the [build runner](https://www.jetbrains.com/help/teamcity/build-runner.html)
type and TeamCity will present us with the build runner wizard

We are going to create a Build Step with the following parameters:

`Runner type`: Command Line<br />
`Step name`: Install NodeJS & NPM<br />
`Execute step`: If all previous steps finished successfully<br />
`Working directory`: aws-ts-eks-hello-world<br />
`Run`: Custom script<br />
`Custom Script`:

```bash
yum -y install nodejs
npm version
```

We can `Save` the step. Let's add the next build step by clicking on `Add Build Step`.

### Installing Pulumi Build Step

We are going to create a Build Step with the following parameters:

`Runner type`: Command Line<br />
`Step name`: Install Pulumi<br />
`Execute step`: If all previous steps finished successfully<br />
`Working directory`: aws-ts-eks-hello-world<br />
`Run`: Custom script<br />
`Custom Script`:

```bash
curl -sSL https://get.pulumi.com | sh
```

Again, we can `Save` the step and add the next build step by clicking on `Add Build Step`.

### Restoring NPM Dependencies Build Step

We are going to create a Build Step with the following parameters:

`Runner type`: Command Line<br />
`Step name`: Restore Dependencies<br />
`Execute step`: If all previous steps finished successfully<br />
`Working directory`: aws-ts-eks-hello-world<br />
`Run`: Custom script<br />
`Custom Script`:

```bash
curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.13.7/2019-06-11/bin/linux/amd64/aws-iam-authenticator
chmod +x ./aws-iam-authenticator
mkdir -p $HOME/bin && cp ./aws-iam-authenticator $HOME/bin/aws-iam-authenticator
npm install
```

Again, we can `Save` the step and add the next build step by clicking on `Add Build Step`.

### Pulumi Stack Creation Build Step

We are going to create a Build Step with the following parameters:

`Runner type`: Command Line<br />
`Step name`: Stack Creation<br />
`Execute step`: If all previous steps finished successfully<br />
`Working directory`: aws-ts-eks-hello-world<br />
`Run`: Custom script<br />
`Custom Script`:

```bash
pulumi stack init %STACK_NAME%
pulumi config set aws:region %AWS_REGION%
```

Again, we can `Save` the step and add the last build step by clicking on `Add Build Step`.

### Pulumi Up Build Step

`Runner type`: Command Line<br />
`Step name`: Pulumi Up<br />
`Execute step`: If all previous steps finished successfully<br />
`Working directory`: aws-ts-eks-hello-world<br />
`Run`: Custom script<br />
`Custom Script`:

```bash
pulumi up --yes
```

### Configuring Build Parameters

We need to create a few build parameters before we can actually run the build. The
[TeamCity Documentation](https://www.jetbrains.com/help/teamcity/configuring-build-parameters.html) describes how to
create these parameters. The parameters we will create are as follows:

`AWS_REGION`: us-east-2<br />
`STACK_NAME`: development-example

`env.AWS_ACCESS_KEY_ID`: <redacted><br />
`env.AWS_SECRET_ACCESS_KEY`: <redacted><br />
`env.PULUMI_ACCESS_TOKEN`: <redacted><br />
`env.PATH`: `%env.PATH%:%env.HOME%/.pulumi/bin:%env.HOME%/bin`

### Running the build

Now that all the steps are created and the configuration has been added to TeamCity, we can run the build by clicking on the
`Run` button. After a few minutes, we should have a successful build. On inspection of the build log, we can see that the
infrastructure has been successfully deployed:

```bash
[17:05:48][Step 5/5]                     exec: {
[17:05:48][Step 5/5]                         apiVersion: "client.authentication.k8s.io/v1alpha1"
[17:05:48][Step 5/5]                         args      : [
[17:05:48][Step 5/5]                             [0]: "token"
[17:05:48][Step 5/5]                             [1]: "-i"
[17:05:48][Step 5/5]                             [2]: "helloworld-eksCluster-c5bd220"
[17:05:48][Step 5/5]                         ]
[17:05:48][Step 5/5]                         command   : "aws-iam-authenticator"
[17:05:48][Step 5/5]                     }
[17:05:48][Step 5/5]                 }
[17:05:48][Step 5/5]             }
[17:05:48][Step 5/5]         ]
[17:05:48][Step 5/5]     }
[17:05:48][Step 5/5]     namespaceName  : "helloworld-eyay6eno"
[17:05:48][Step 5/5]     serviceHostname: "a2b21d9e5f4ee11e99d67026bafffdcc-603547860.us-east-2.elb.amazonaws.com"
[17:05:48][Step 5/5]     serviceName    : "helloworld-d4oadgeg"
[17:05:48][Step 5/5]
[17:05:48][Step 5/5] Resources:
[17:05:48][Step 5/5]     + 40 created
[17:05:48][Step 5/5]
[17:05:48][Step 5/5] Duration: 13m0s
[17:05:48][Step 5/5]
[17:05:48][Step 5/5] Permalink: https://app.pulumi.com/stack72/aws-ts-eks-hello-world/development-example/updates/1
[17:05:48][Step 5/5] Process exited with code 0
```
