---
title_tag: "Managing Configuration and Secrets | Tutorials"
meta_desc: Learn how to manage and interact with configuration values and secrets in this tutorial.
title: "Managing Configuration and Secrets"
h1: "Managing Configuration and Secrets"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  usingpulumi:
    identifier: manage-config-secrets
    weight: 1
tags:
    - configuration
    - secrets
    - fundamentals
    - tutorial
---

In Pulumi, an environment is a collection of values intended to capture the configuration values needed to work with a particular environment. These can be raw values like server names, environment types, region names and so on. They can also be sensitive values such as database passwords or service tokens.

## Prerequisites

This tutorial assumes that you are familiar with the basics of the Pulumi workflow. If you are new to Pulumi, complete the [Get Started series](/docs/get-started/) first.

Additionally, you will need the following tools to complete this tutorial:

- A [Pulumi account](https://app.pulumi.com)
  - [Optional] Create an [access token](/docs/pulumi-cloud/access-management/access-tokens/)
- The [Pulumi CLI](https://www.pulumi.com/docs/install/)

Let's get started!

## Create a new project

To start, login to the [Pulumi CLI](/docs/cli/commands/pulumi_login/) and ensure it is [configured to use your AWS account](/docs/clouds/aws/get-started/begin/#configure-pulumi-to-access-your-aws-account). Next, [create a new project](/docs/clouds/aws/get-started/create-project/) and replace the default program code with the following:

{{< example-program path="aws-config-secrets-simple" >}}

## Clean Up

{{< cleanup >}}

## Next Steps

In this tutorial, you made an EC2 instance configured as an Nginx webserver and made it publically available by referencing the Pulumi Registry to define the security group. You also reviewed resource properties and example usage.

To learn more about creating resources in Pulumi, take a look at the following resources:

- Learn more about stack outputs and references in the [Stack Outputs and References](/docs/using-pulumi/stack-outputs-and-references/) tutorial.
- Learn more about inputs and outputs in the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation.
- Learn more about [resource names](/docs/concepts/resources/names/), [options](/docs/concepts/options/), and [providers](/docs/concepts/resources/providers/) in the Pulumi documentation.
