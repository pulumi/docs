---
title_tag: Create an Insights Account | Pulumi Insights
title: Create an Insights Account
h1: "Pulumi Insights: Create an Insights Account"
meta_desc: This page provides an overview on how to get started with Pulumi Insights Accounts.
weight: 3
menu:
  insights:
    name: Create Accounts
    parent: insights-discovery-get-started
    identifier: insights-get-started-accounts
    weight: 3
aliases:
  - /docs/insights/get-started/create-accounts/
---

With the prerequisites in place, let’s connect your first cloud account and kick off a discovery scan. In this example you will see the steps for AWS; Azure and Google Cloud follow the same flow with their own browser-based sign-in. For Oracle Cloud and Kubernetes, choose **Connect using existing ESC credentials** on the Authentication step instead, using the ESC environment you configured earlier.

{{< notes type="info" >}}
Currently while in public preview, Pulumi Insights Account discovery supports AWS, Azure, Oracle Cloud, Kubernetes, and Google Cloud.
{{< /notes >}}

## Create an Insights account

1. Navigate to **Insights** > **Accounts** in the Pulumi Cloud console. You will be directed to the Accounts landing page where you'll be able to create and manage all your Insights accounts and view scan statuses.

1. Select **Connect cloud accounts** and choose your cloud provider. For this example, choose **AWS**.

1. On the **Authentication** step, keep the recommended **Connect using IAM Identity Center (SSO)** option. Enter your organization's **SSO start URL** and **Region**, then select **Next** and approve the authorization request that AWS opens in a new window. The wizard then lists the AWS accounts you can access. If your organization doesn't use IAM Identity Center, choose **Connect using static credentials**, or **Connect using existing ESC credentials** with [an environment you configure yourself](/docs/insights/discovery/accounts/#configure-esc-credentials).

1. On the **Accounts** step, the wizard pre-selects every discovered account that isn't already connected. For this tutorial, select **Edit selected accounts** and narrow the selection to a single account. Keep the default **Build & Manage** access level, or switch to the read-only **Discovery & Policy** level if your security review requires it.

1. On the **Discovery** step, review the defaults: scheduled scans and policy evaluation are both enabled, with a default policy pack pre-selected. For AWS, also review the partition the account belongs to and the regions you want scanned; global services are always scanned. For this tutorial, keep the default selections.

{{< notes type="info" >}}
Scheduled scans run every 24 hours by default; you can switch to a 12-hour schedule instead.
{{< /notes >}}

To finish, select **Next**. The wizard creates the IAM role and an ESC environment for the account, connects it, and shows a summary with next steps. The Insights account is named after your cloud account: for example, an AWS account named `production` becomes the Insights account `production`. The rest of this guide uses `production` as the example name; substitute the name of the account you connected.

For the full reference on the wizard, including the other authentication options and what gets created in your cloud accounts, see [Connect cloud accounts](/docs/insights/discovery/connect-cloud-accounts/).

Next, you will learn how to manage your accounts, and manually launch a scan.

{{< get-started-stepper >}}
