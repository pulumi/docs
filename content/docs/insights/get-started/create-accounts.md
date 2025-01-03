---
title_tag: Create an Insights Account | Pulumi Insights
title: Create an Insights Account
h1: "Pulumi Insights: Create an Insights Account"
meta_desc: This page provides an overview on how to get started with Pulumi Insights Accounts.
weight: 3
menu:
  insights:
    parent: insights-get-started
    identifier: insights-get-started-accounts
    weight: 3
---

Now that you have set up your ESC and your cloud account, let’s create your first Pulumi Insights account and kick off a discovery scan. In this example you will see the steps for AWS and you can follow along with any cloud provider.

{{< notes type="info" >}}  
Currently while in public preview, Pulumi Insights Account discovery supports AWS, Azure, Oracle Cloud, and Kubernetes.  
{{< /notes >}}

## Create an Insights account

Navigate to the **Pulumi Insights** section in the Pulumi Cloud console and click **Accounts**. You will be directed to the Accounts landing page where you'll be able to create and manage all your Insights accounts and view scan statuses.

Click **Create Account** and choose your cloud provider (AWS, Azure, Oracle Cloud, or Kubernetes)

{{< video title="Column Selection" src="https://pulumi.com/uploads/insights-create-account.mp4" autoplay="true" loop="false" >}}

Click on the drop-down to select your newly created environment `insights-discovery/insights-discovery-env`, then provide a unique account name, such as `Insights-aws-account`.

Add any provider-specific configuration, such as the regions to scan for AWS.

Finally, you can select whether to enable scheduled scans or run them manually, let's keep the default selection.

{{< notes type="info" >}}
When scheduled scans are enabled, Pulumi automatically scans the account every 24 hours.
{{< /notes >}}

To finish creating this new account click **Create** and you will see a success notification and arrive on the details page of the account.

Next, you will learn how to manage your accounts, and manually launch a scan.

{{< get-started-stepper >}}
