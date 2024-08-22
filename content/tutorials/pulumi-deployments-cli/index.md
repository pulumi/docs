---
title_tag: Create a new project and configure Pulumi Deployments with the CLI
title: "Create a new project and configure Pulumi Deployments with the CLI"
layout: single
description: |
    Create and deploy infrastructure manually using Pulumi CLI, GitHub CLI, and Pulumi Deployments.
meta_desc: In this step-by-step tutorial, learn how to create and manage cloud infrastructure using Pulumi Deployments, the Pulumi CLI, and the GitHub CLI.
meta_image: meta.png
weight: 72
summary: |
    In this tutorial, you will learn how to configure Pulumi Deployments in the CLI...

youll_learn:
  - How to create a new Pulumi project using the Pulumi CLI
  - How to upload the project to GitHub using the GitHub CLI
  - How to configure Pulumi Deployments for manual projects
prereqs:
    - Completion of the AWS [Getting Started](/docs/clouds/aws/get-started/) guide or familiarity with the basics of the Pulumi workflow
    - A [Pulumi Cloud account](https://app.pulumi.com/signup)
    - An [Amazon Web Services](https://aws.amazon.com/) account, access key ID, and secret access key
    - A [GitHub account](https://github.com/) with admin rights to a Git repository or organization
    - The [GitHub CLI](https://cli.github.com/)
estimated_time: 10
allow_long_title: true
---
<!-- TODO: meta image -->
<!-- TODO: better summary -->

You can create a new Pulumi project, commit its code, and configure Pulumi Deployments using the Pulumi and GitHub CLIs.
<!-- TODO: link to first tutorial -->
### Create a project

Let’s begin by using the Pulumi CLI to create a S3 bucket on AWS using a [Pulumi Template](/templates/).

Initialize a new Pulumi project and pick your programming language of choice:

{{< chooser language "typescript,python,go,csharp,yaml" / >}}

{{% choosable language typescript %}}

```bash
$ mkdir learn-deployments-cli && cd learn-deployments-cli
$ pulumi new aws-typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ mkdir learn-deployments-cli && cd learn-deployments-cli
$ pulumi new aws-python
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
$ mkdir learn-deployments-cli && cd learn-deployments-cli
$ pulumi new aws-go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ mkdir learn-deployments-cli && cd learn-deployments-cli
$ pulumi new aws-csharp
```

{{% /choosable %}}
{{% choosable language yaml %}}

```bash
$ mkdir learn-deployments-cli && cd learn-deployments-cli
$ pulumi new aws-yaml
```

{{% /choosable %}}

Follow the prompts to set up your project and accept the default values or specify new values, such as `aws-region`.

Run `pulumi preview` to see the details for what resources will be created.

```bash
pulumi pre
```

```bash
Previewing update (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/tutorials/learn-deployments-cli/dev/previews/f6102d35-3c98-4f0a-9cd1-4d6e79b3b345

     Type                 Name                       Plan
 +   pulumi:pulumi:Stack  learn-deployments-cli-dev  create
 +   └─ aws:s3:Bucket     my-bucket                  create

Outputs:
    bucket_name: output<string>

Resources:
    + 2 to create
```

### Initialize git and create a new GitHub repository
Next, you will initialize a local git repository using the following commands:

```bash
$ git init
$ git branch -M main
$ git add .
$ git commit -m "first Pulumi Deployments tutorial commit"
```

Create a new private repo with the GitHub CLI to and push your local code:

```bash
$ gh repo create <github_owner>/learn-deployments-cli --private --source=. --push
```
Replace `<github_owner>` with your own GitHub owner.

### Configure deployment Settings

Now that you have your code in GitHub, you will configure your project in the Pulumi Cloud to use Pulumi Deployments.

1. Open a browser and login to the Pulumi Cloud at [https://app.pulumi.com/](https://app.pulumi.com/).
2. Select **Stacks** in the left navigation, and click on your stack.
3. Click on the **Settings** tab, click on **Deploy** on the left navigation.
4. Configure the `Source control settings` by selecting GitHub, your `GitHub organization/repository`, and the `Branch`.
5. Add your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` **Environment variables** required by this Pulumi program.

{{% notes type="info" %}}
Secret environment variables, such as `AWS_SECRET_ACCESS_KEY`, are encrypted end-to-end with Pulumi and can be set on each stack. However, by creating an [environment](/docs/pulumi-cloud/esc) with Pulumi ESC, you can centralize secrets and set up OIDC for secure authentication. This allows you to manage and share sensitive configuration data across multiple stacks efficiently.
{{% /notes %}}

A full description of all Deployment settings is available on the [deployment settings](/docs/pulumi-cloud/deployments/reference/#deployment-settings) docs page.

Finally, click **Save deployment configuration**.

## Run a Deployment from the CLI

Now that Deployments is configured you can run a deployment. From the CLI run a `Pulumi update` to initiate the deployment process.

```bash
pulumi up
```

You will see the progress of your deployment in the terminal and after completion, the summary of the resources you created.

## Cleanup

Before moving on, you can destroy the resources that are part of your stack to avoid incurring any charges.

1. Run `pulumi destroy` to delete all resources for this stack. You'll be prompted to confirm you want to perform this destroy.
2. To remove the stack completely, run `1`pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Service.

## Next Steps

In this tutorial, you set up a Pulumi project using the Pulumi CLI, uploaded it to GitHub using the GitHub CLI, and configured Pulumi Deployments. For more information on managing deployments with Pulumi Cloud, explore the following resources:

- **Deployment Triggers**: Learn about the various methods to trigger a deployment, such as using the REST API, the Pulumi Console, or GitHub push-to-deploy. Visit the [Pulumi documentation](https://www.pulumi.com/docs/pulumi-cloud/deployments/reference/#deployment-triggers).

- **Deployment Permissions**: Understand how to manage deployment permissions to control access and ensure security. See the [Pulumi documentation](https://www.pulumi.com/docs/pulumi-cloud/deployments/reference/#deployment-permissions).
