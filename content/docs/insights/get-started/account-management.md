---
title_tag: Manage Accounts and Scans | Pulumi Insights
title: Manage Accounts and Scans
h1: "Pulumi Insights: Manage Accounts and Scans"
meta_desc: This page provides an overview on how to manage Pulumi Insights Accounts.
weight: 4
menu:
  insights:
    parent: insights-get-started
    identifier: insights-get-started-manage-accounts
    weight: 4
search:
  keywords:
    - accounts
    - scans
    - insights
    - manage accounts
    - child accounts
---

Now that you have created a new account you can click on the **Accounts** page to see a list of all your created accounts, the last update and number of resources discovered.

## View Accounts

![Insights Account Discovery](/docs/insights/assets/insights-account-discovery.png)

Here you will notice that Insights automatically created child accounts based on the underlying platform model for each group you decide to enable. Child accounts enable you to control the discovery behavior for each group separately.

For example, AWS enables you to divide you infrastructure into regions and Insights will create separate child accounts for each region you specify. In this case you will see:

- Parent account: `insights-aws-account`
- Child account (region): `insights-aws-account/us-central-1`
- Child account (region): `insights-aws-account/us-west-1`

It's important to note that if you **Scan** or **Delete** the `insights-aws-account` account, Pulumi applies this action to all child accounts.

For a detailed explanation and more examples of how child accounts and hierarchies work see the [Insights accounts documentation](/docs/insights/accounts/#account-hierarchies)

## Manage Accounts

You can manage each by selecting your desired account, where you can see the provider summary, status and history of all scans.  This is where you can select the action to manually **Scan** or **Delete Account**.

Let's kick off the scan for the new account you created.

![Insights Account Discovery](/docs/insights/assets/insights-account-discovery.png)

After you select the `insights-aws-account` account, choose the **Scan** action and click **Scan**

## View Account discovery progress

Pulumi Insights will kick off a scan across each child account / region in parallel and as reasources are discovered you will begin to see a status of the number of resources known to Pulumi.

![Insights Account Discovery Scan](/docs/insights/assets/insights-account-discovery-scan.png)

As each account scan completes, you will see a checkmark and status update per account. The scan duration will depend on the number of resources for each account, however as soon as they are discovered you can begin to explore insights and do not have to wait for the entire discovery to finish.

![Insights Account Discovery Scan](/docs/insights/assets/insights-account-discovery-complete.png)

Let's introduce the Pulumi Resource Explorer for your newly discovered resources and learn how to draw insights about your cloud infrastructure.

{{< get-started-stepper >}}
