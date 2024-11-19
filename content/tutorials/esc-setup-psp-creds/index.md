---
title: Setup Pulumi Service Provider using ESC
title_tag: Setup Pulumi Service Provider using ESC
layout: single
description: Create an ESC Environment to store your Pulumi Service Provider credentials and easily re-use them across your IaC stacks.
meta_desc: Create an ESC Environment to store your Pulumi Service Provider credentials and easily re-use them across your IaC stacks.
meta_image: meta.png
weight: 999
summary: |
    [Pulumi ESC](https://pulumi.com/esc) makes it easy to store and retrieve static and dynamic configuration settings, manage them securely and flexibly, and use them in your applications. In this tutorial, you will create an ESC environment to store credentials for the Pulumi Service Provider, then use this environment to create new Pulumi Cloud resources, including more ESC Environments.
youll_learn:
    - How to store and retrieve configuration values with Pulumi ESC
    - How to configure Pulumi Service Provider
    - How to use Pulumi Service Provider to create more ESC Environments
prereqs:
    - Basic understanding of Pulumi IaC
    - The [Pulumi CLI](/docs/iac/download-install/) installed
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - Familiarity with TypeScript and Node.js
estimated_time: 10
collections:
    - pulumi-esc
---

{{% notes %}}
This tutorial is all about using ESC with Pulumi Service Provider (PSP). However, using ESC is an encouragement rather than a requirement. If you *don't* want to use ESC, refer to [PSP setup docs](/registry/packages/pulumiservice/installation-configuration/) instead.
{{% /notes %}}

## Log into Pulumi Cloud

Before you begin, make sure you've [signed into Pulumi Cloud](https://app.pulumi.com/). Once you've done so, you can log in with Pulumi CLI and be prompted to :

```bash
$ pulumi login

Manage your Pulumi stacks by logging in.
Run `pulumi login --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser
```

## Obtain a personal access token

Next, you'll also need a Pulumi Cloud [personal access token](/docs/pulumi-cloud/access-management/access-tokens/#personal-access-tokens). Create a short-lived access token for this tutorial and copy it into your current shell to login into Pulumi Cloud. Be sure to keep track of this token as you will need it for the next step of the tutorial.

## Brief Explanation

Pulumi Service Provider (PSP) is a Pulumi provider for creating and configuring Pulumi Cloud resources using Pulumi IaC Programs. Just like an S3 bucket is created using an AWS provider, PSP allows creation of things like Environments, Environment Version Tags, Environment Webhooks, and much more. In order to authenticate with Pulumi Cloud, PSP uses the same personal access token (PAT) as Pulumi CLI. This is where ESC comes in!

Instead of providing the PAT as an environment variable, risking losing or leaking it, we will create an ESC Environment and store the PAT there. We will then import this environment into the configuration of a new stack, in which we will create Pulumi Cloud resources

## Create a new ESC environment

ESC [_Environments_](/docs/esc/environments/working-with-environments/) are a great way to store configuration settings and secrets. Environments can be created in the Pulumi Cloud console or with the CLI.

To get started, navigate to the Environments page using Pulumi Cloud console's navigation bar on the left. Then click `Create Environment` button, fill in `creds` for project name and `psp` for environment name and click `Create`. You will now see a blank new environment with some default commented-out explanations.

## Fill in the PAT

Select everything in the Environment definition pane and replace it with this:

```bash
values:
  pulumiConfig:
    "pulumiservice:accessToken":
      fn::secret: % FILL IN PAT HERE %
```

{{% notes %}}
If you are using *Pulumi Self-hosted*, you will also need to add a field `"pulumiservice:apiUrl"` next to the `accessToken` one. Fill it with your Pulumi Cloud backend URL. This is *not* needed for most users.
{{% /notes %}}

Once you fill in your previously created PAT, click `Save` on the top right. This will update your new environment's definition with the values you just added. Note that the plaintext PAT was converted into a secret value. It is now securely stored within Pulumi Cloud, removing the risk of losing or leaking the PAT, while your stacks are still able to decrypt and use it. Feel free to erase the plaintext PAT, we won't need it again!

## Create a new Pulumi Program

Now it's time to create a new Pulumi Program that will use the new Environment and PSP to create more Pulumi Cloud resources!

Create a new folder in your shell (for example `esc-psp-tutorial`) and navigate into it. Then, run `pulumi new`, and navigate the menu to create a new stack from a template called `typescript`. Fill in the project name as `esc-psp-tutorial`, and the stack name as `%ORG NAME%/dev`, filling in your actual organization name (for the rest of the tutorial, `tutorials` will be used), and `dev` as the name of the new stack.

Once Pulumi CLI finishes installing dependencies, you should see the following files in your tutorial folder:

```
Pulumi.yaml  index.ts  node_modules  package-lock.json  package.json  tsconfig.json
```

## Import the ESC Environment into the IaC stack

In your tutorial folder, create a new file `Pulumi.dev.yaml`. This file will contain configuration specific to your new `dev` stack. Fill the file in with this:

```
environment:
  - creds/psp
```

Here, `environment` field lets you specify an array of ESC Environments to import. In this case, we only want to import the Environment we created above, `creds/psp`, where `creds` is the ESC project name and `psp` is the Environment name.

## Write the Pulumi program

Open your new project in an IDE of your choice. Replace the code in `index.ts` with the code below:

```typescript
import * as service from "@pulumi/pulumiservice";
import * as pulumi from "@pulumi/pulumi";

let config = new pulumi.Config();

var environment = new service.Environment("environment-from-psp", {
  organization: "tutorials",
  project: "esc-psp-tutorial",
  name: "first-psp-environment",
  yaml: new pulumi.asset.StringAsset(
`values:
  esc-mastered: true
  psp-mastered: true`
  )
})
```

Remember to replace `tutorials` with your actual organization name.

Now, to be able to use PSP, run `npm install @pulumi/pulumiservice` to install the plugin. (Your command will differ if you're not using `npm` as Node's package manager.)

## Create a new Environment via IaC

You are now all set! Run `pulumi up`, and your Pulumi program will create a new environment called `first-psp-environment`. Navigate to the Environments page in Pulumi Cloud console to confirm it exists. You should be able to see the environment definition from your code - both `esc-mastered` and `psp-mastered` values are now `true`.

### Wrapping up

You have learned how to create ESC environments in the Pulumi Cloud console, import them into IaC stacks and even create Environments using the Pulumi Service Provider. The environment you created, `creds/psp` can now be easily re-used between your stacks, or used to compose more complex environments, using [Environment imports](https://www.pulumi.com/docs/esc/environments/imports/). Using what you know now, you can easily create other Environments under the `creds` project to store credentials for other providers. For example, `creds/aws` or `creds/azure`!
