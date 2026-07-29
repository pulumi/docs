---
title_tag: Before You Begin | Pulumi Insights
title: Before You Begin
h1: "Pulumi Insights: Before You Begin"
meta_desc: This page provides an overview on how to get started with Pulumi Insights Accounts.
weight: 2
menu:
  insights:
    name: Before You Begin
    parent: insights-discovery-get-started
    identifier: insights-get-started-begin
    weight: 2
aliases:
  - /docs/insights/get-started/begin/
---

## Before you begin

Before connecting your first cloud account, confirm the following prerequisites are in place.

- Ensure you’re an admin of your Pulumi organization, or have permission to connect cloud accounts and create [Pulumi ESC (Environments, Secrets, and Configuration)](/docs/esc/) environments.
- You're using Pulumi's **Team**, **Enterprise**, or **Business Critical** edition.
- You have administrative access to the cloud account or organization you want to connect: the ability to authorize applications and create IAM resources in AWS, grant admin consent in Microsoft Entra ID, or grant organization-level roles in Google Cloud.

If you're new to Pulumi you can click here to [start a free trial](https://app.pulumi.com/signup?create-organization).

## How authentication works

You don't need to create credentials or ESC environments ahead of time. The **Connect cloud accounts** wizard authenticates to AWS, Azure, and Google Cloud with a browser-based sign-in using OpenID Connect (OIDC), then creates the trust roles and ESC environments each account needs. With these recommended flows, no long-lived cloud secrets are stored in Pulumi Cloud.

{{% notes type="info" %}}
Discovery uses Pulumi ESC to securely manage the credentials required to scan your infrastructure. The wizard generates these environments for you, following the same best practices as the manual OIDC guides for [AWS](/docs/esc/guides/configuring-oidc/aws/), [Azure](/docs/esc/guides/configuring-oidc/azure/), and [Google Cloud](/docs/esc/guides/configuring-oidc/gcp/).
{{% /notes %}}

Oracle Cloud and Kubernetes accounts connect through an ESC environment that you configure yourself. If you're connecting one of those providers, set up the environment first by following [Create and manage Insights accounts](/docs/insights/discovery/accounts/#configure-esc-credentials).

Next, you'll connect a cloud account and kick off your first discovery scan.

{{< get-started-stepper >}}
