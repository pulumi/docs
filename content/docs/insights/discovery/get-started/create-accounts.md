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

Now that you have set up your ESC and your cloud account, let’s create your first Pulumi Insights account and kick off a discovery scan. In this example you will see the steps for AWS and you can follow along with any provider covered in the previous step. For Google Cloud, use the wizard's recommended browser-based sign-in, described in [Connect cloud accounts](/docs/insights/discovery/connect-cloud-accounts/), instead of the ESC-credentials option shown here.

{{< notes type="info" >}}
Currently while in public preview, Pulumi Insights Account discovery supports AWS, Azure, Oracle Cloud, Kubernetes, and Google Cloud.
{{< /notes >}}

## Create an Insights account

1. Navigate to **Insights** > **Accounts** in the Pulumi Cloud console. You will be directed to the Accounts landing page where you'll be able to create and manage all your Insights accounts and view scan statuses.

1. Select **Connect cloud accounts** and choose your cloud provider (AWS, Azure, Oracle Cloud, Kubernetes, or Google Cloud).

1. On the **Authentication** step, choose **Connect using existing ESC credentials** (rather than the browser-based sign-in recommended for AWS, Azure, and Google Cloud), select your newly created environment `insights-discovery/insights-discovery-env`, and select **Next**. Pulumi validates the credentials stored in the environment.

1. On the **Discovery** step, review the defaults: scheduled scans and policy evaluation are both enabled, with a default policy pack pre-selected. For AWS, also review the partition the account belongs to and the regions you want scanned; global services are always scanned. For this tutorial, keep the default selections.

{{< notes type="info" >}}
Scheduled scans run every 24 hours by default; you can switch to a 12-hour schedule instead.
{{< /notes >}}

To finish creating this new account, select **Next**. The wizard connects the account, names it after your ESC environment (for example, `insights-discovery-env`), and shows a summary with next steps.

Next, you will learn how to manage your accounts, and manually launch a scan.

{{< get-started-stepper >}}
