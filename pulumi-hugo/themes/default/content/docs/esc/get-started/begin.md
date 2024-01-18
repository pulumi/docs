---
title_tag: Before You Begin | Pulumi ESC
title: Before you begin
h1: "Pulumi ESC: Before you begin"
meta_desc: This page provides an overview on how to get started with Pulumi ESC.
weight: 2
menu:
  pulumiesc:
    parent: esc-get-started
    identifier: esc-get-started-begin
---

Before you get started using Pulumi ESC, let's run through a few quick steps to ensure your environment is set up correctly.

### Create a Pulumi account

Pulumi ESC is a service of Pulumi Cloud, meaning you will need to create a Pulumi account to be able to use it. To do so, navigate to the [Pulumi Cloud console](https://app.pulumi.com) and create a new account. Once created, you can [optionally create an access token](/docs/pulumi-cloud/access-management/access-tokens/). Doing so will provide you an alternative way to sign into the Pulumi Cloud via the CLI. The token can also be used to automate your usage of the Pulumi Cloud using the REST API.

### Install the Pulumi ESC CLI

{{< notes type="info" >}}
Pulumi ESC can be used with or without Pulumi IaC. This means that if you already have the [Pulumi IaC CLI](/docs/cli/) installed, you do not need to install the Pulumi ESC CLI, and you may substitute `pulumi env` anywhere you see the `esc env` command in the rest of this tutorial.
{{< /notes >}}

Use the below option to install the Pulumi ESC CLI based on your operating system.

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

```bash
$ brew update && brew install pulumi/tap/esc
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
$ curl -fsSL https://get.pulumi.com/esc/install.sh | sh
```

{{% /choosable %}}

{{% choosable os windows %}}

<div class="mb-6 border-solid border-b-2 border-gray-200">
<div class="w-full">
<h3 class="no-anchor pt-4"><i class="fas fa-download pr-2"></i>Windows Binary Download</h3>
<p>
<a class="btn btn-secondary mx-2" href="https://get.pulumi.com/esc/releases/esc-v{{< latest-version-esc >}}-windows-x64.zip">amd64</a>
</p>
</div>
</div>

{{% /choosable %}}

{{% /chooser %}}

You can explore more installation options by visiting the [ESC installation docs](/docs/install/esc/).

### Login to the ESC CLI

Run the following command to log into the CLI:

```bash
esc login
```

You will be prompted to log in to the Pulumi Cloud using either the browser or by optionally providing an access token.

```bash
$ esc login
Manage your Pulumi ESC environments by logging in.
Run `esc --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser                   :
Logged in to https://api.pulumi.com/ as your-pulumi-org (https://app.pulumi.com/your-pulumi-org)
```

### [Optional] Configure OpenID Connect (OIDC)

Pulumi supports [OpenID Connect (OIDC) integration](/docs/pulumi-cloud/oidc/) across various services including Pulumi ESC. OIDC enables secure interactions between Pulumi and cloud providers by leveraging signed, short-lived tokens issued by the Pulumi Cloud. Use one of the following guides below to configure OIDC between Pulumi ESC and your chosen cloud provider:

- [OIDC Configuration for AWS](/docs/pulumi-cloud/oidc/aws/)
- [OIDC Configuration for Azure](/docs/pulumi-cloud/oidc/azure/)
- [OIDC Configuration for Google Cloud](/docs/pulumi-cloud/oidc/gcp/)

This is an optional step that is not required to get started with Pulumi ESC. There are some steps in this series that will require OIDC configuration to complete, but that will be indicated on the relevant pages.

In the next section, you will start your journey with Pulumi ESC by creating a new environment.

{{< get-started-stepper >}}
