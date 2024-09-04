---
title: "CLI Authentication"
title_tag: "CLI Authentication"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn how to authenticare to the Pulumi CLI in this tutorial.

# A similar description used for search results and social-media previews.
meta_desc: Learn how to authenticare to the Pulumi CLI in this tutorial.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: cli-auth-meta.png

# An optional video for the tutorial. When present, it appears at the top of the page, replacing
# the meta image. YouTube and HTML5 video sources are supported.
# video:
#     url: /blog/drift-detection/drift.mp4
#     youtube: Q8tw6YTD3ac

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
    The [`pulumi login`](/docs/cli/commands/pulumi_login/) command is used to login to the Pulumi Cloud from the [Pulumi CLI](/docs/cli/). Logging in to the Pulumi Cloud enables you to manage your state, resources, and secrets in a secure way. In this tutorial, we'll demonstrate how to authenticate to the Pulumi Cloud using the Pulumi CLI.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to authenticate using a personal access token
    - How to authenticate using the browser

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 5

# An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
# collections:
#     - some-non-existent-collection
---

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

{{< video title="Running the pulumi login command with access token" src="/tutorials/cli-authentication/aws-cli-pulumi-login-token.mp4" autoplay="true" loop="true" >}}

In the CLI, you will receive a message to indicate that you've successfully logged in.

### Authenticate using the browser

Run the `pulumi login` command to initiate the authentication process. When prompted, press enter to be directed to the browser. From there, login with the appropriate credentials:

{{< video title="Running the pulumi login command with browser" src="/tutorials/cli-authentication/aws-cli-pulumi-login-browser.mp4" autoplay="true" loop="true" >}}

In both the browser and the CLI, you will receive a message to indicate that you've successfully logged in.

{{< video title="Showing browser authentication completed" src="/tutorials/cli-authentication/aws-cli-pulumi-login-browser-success.mp4" autoplay="true" loop="true" >}}

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
