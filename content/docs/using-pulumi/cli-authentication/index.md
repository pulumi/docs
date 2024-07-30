---
title_tag: "CLI Authentication | Tutorials"
meta_desc: Learn how to authenticate to the Pulumi CLI in this tutorial.
title: "CLI Authentication"
h1: "CLI Authentication"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  usingpulumi:
    identifier: cli-authentication
    weight: 1
tags:
    - authentication
    - cli
    - fundamentals
    - tutorial
---

The [pulumi login](/docs/cli/commands/pulumi_login/) command is used to login to the Pulumi Cloud from the [Pulumi CLI](/docs/cli/). Logging in to the Pulumi Cloud enables you to manage your state, resources, and secrets in a secure way. In this tutorial, we'll demonstrate how to authenticate to the Pulumi Cloud using the Pulumi CLI.

## Prerequisites

You will need the following tools to complete this tutorial:

- A [Pulumi account](https://app.pulumi.com)
- Create a [personal access token](/docs/pulumi-cloud/access-management/access-tokens/#personal-access-tokens)
  - Make sure to securely store your token after creation as it will no longer be visible in the console
- The [Pulumi CLI](https://www.pulumi.com/docs/install/)

Let's get started!

## Logging into the CLI

When you run the `pulumi login` command, you will be presented with a prompt that will offer you two methods of authenticating: either via access token or via the browser.

```bash
$ pulumi login
Manage your Pulumi stacks by logging in.
Run `pulumi login --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser                   :
```

{{< notes type="info" >}}

By default, logging into the Pulumi CLI will log you into the managed Pulumi Cloud backend, but it is also possible to use this command to login to a self-hosted Pulumi Cloud backend. This is out of the scope of this tutorial, but you can learn more by visiting the [Managing state & backend options documentation](/docs/concepts/state/#logging-into-and-out-of-state-backends).

{{< /notes >}}

In the next steps, you will learn how to login using both options, and you will also learn how to logout of the Pulumi CLI when you are done.

### Authenticate using a token

Run the `pulumi login` command to initiate the authentication process. When prompted, copy and paste your token into the command line and press enter.

{{< video title="Running the pulumi stack command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-login-token.mp4" autoplay="true" loop="true" >}}

In the CLI, you will receive a message to indicate that you've successfully logged in.

### Authenticate using the browser

Run the `pulumi login` command to initiate the authentication process. When prompted, press enter to be directed to the browser. From there, login with the appropriate credentials:

{{< video title="Running the pulumi stack command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-login-browser.mp4" autoplay="true" loop="true" >}}

In both the browser and the CLI, you will receive a message to indicate that you've successfully logged in.

{{< video title="Running the pulumi stack command" src="https://www.pulumi.com/uploads/aws-cli-pulumi-login-browser-success.mp4" autoplay="true" loop="true" >}}

## Logging out of the CLI

When you want to logout of the Pulumi CLI, run the [pulumi logout](/docs/cli/commands/pulumi_logout/) command. You will receive the following output that indicates you were logged out successfully:

```bash
$ pulumi logout
Logged out of https://api.pulumi.com
```

## Next Steps

In this tutorial, you learned how to authenticate to the Pulumi CLI using the browser and using a Pulumi access token. To learn more about using the CLI to create and manage resources in Pulumi, take a look at the following resources:

- Learn more about the available CLI commands in the [Pulumi CLI documentation](/docs/cli/commands/).
- Learn more about configuring Pulumi providers to work with Pulumi in the following resources:
  - [AWS Configuration](/docs/clouds/aws/get-started/begin/#configure-pulumi-to-access-your-aws-account)
  - [Azure Configuration](/docs/clouds/azure/get-started/begin/#configure-pulumi-to-access-your-microsoft-azure-account)
  - [Google Cloud Configuration](/docs/clouds/gcp/get-started/begin/#configure-pulumi-to-access-your-google-cloud-account)
  - [Kubernetes Configuration](/docs/clouds/kubernetes/get-started/begin/#configure-kubernetes)
- Learn more about the different Pulumi Cloud hosting options in the [Managed Pulumi Cloud vs Self-Hosted Pulumi Cloud documentation](/docs/pulumi-cloud/self-hosted/)
