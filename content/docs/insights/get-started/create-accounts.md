---
title_tag: Create an Insights Account | Pulumi Insights
title: Create an Insights Account
h1: "Pulumi Insights: Create an Insights Account"
meta_desc: This page provides an overview on how to get started with Pulumi Insights Accounts.
menu:
  insights:
    parent: insights-get-started
    identifier: insights-get-started-accounts
    weight: 3
---

## Create an Insights account

Navigate to the **Pulumi Insights** section in the Pulumi Cloud console and click **Accounts**. You will be directed to the Accounts landing page where you'll be able to create and manage all your Insights accounts and view scan statuses.

Click **Create Account** and choose your cloud provider (AWS, Azure, Oracle Cloud, or Kubernetes)

![Creating a new account in the Pulumi Insights console](/docs/insights/assets/insights-create-new-account.png)

Click on the drop-down to select your newly created environment `insights-discovery/insights-discovery-env`, then provide a unique account name, such as `Insights-aws-account`.

Add any provider-specific configuration, such as the regions to scan for AWS.

Finally, choose whether to enable scheduled scans or run them manually.

{{% notes type="info" %}}
When scheduled scans are enabled, Pulumi automatically scans the account every 24 hours.
{{% /notes %}}

The ESC environment containing your credentials
For AWS: Select regions to scan

Your first scan will begin automatically after you click **Create**.

Next, you will learn how to see the progress of your first account scan and how to explore your infrastructure resources and use [Research search](/docs/pulumi-cloud/insights/search/).

{{< get-started-stepper >}}
