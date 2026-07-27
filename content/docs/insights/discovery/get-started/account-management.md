---
title_tag: Manage Accounts and Scans | Discovery & Governance
title: Manage Accounts and Scans
h1: Manage Accounts and Scans
meta_desc: This page provides an overview on how to manage cloud accounts in Pulumi.
weight: 4
menu:
  insights:
    name: Manage Accounts and Scans
    parent: insights-discovery-get-started
    identifier: insights-get-started-manage-accounts
    weight: 4
aliases:
  - /docs/insights/get-started/account-management/
pulumi_cloud_feature: insights-discovery
---

Now that you have connected a new account you can select the **Accounts** page to see a list of all your accounts, the last update and number of resources discovered.

## View accounts

Here you will notice that Discovery automatically created child accounts based on the underlying platform model for each group you decide to enable. Child accounts enable you to control the discovery behavior for each group separately.

For example, AWS enables you to divide your infrastructure into regions and Discovery will create separate child accounts for each region you specify. With the default region selection, you will see:

- Parent account: `production`
- Child account (region): `production/us-east-1`
- Child account (region): `production/us-east-2`
- Child account (region): `production/us-west-2`
- Child account (region): `production/eu-west-1`

It's important to note that if you **Scan** or **Delete** the `production` account, Pulumi applies this action to all child accounts.

For a detailed explanation and more examples of how child accounts and hierarchies work see the [cloud accounts documentation](/docs/insights/discovery/accounts/#account-hierarchies)

## Manage accounts

You can manage each by selecting your desired account, where you can see the provider summary, status and history of all scans. This is where you can select the action to manually **Scan** or **Delete Account**.

The wizard already started an initial scan when you connected the account. Here, let's launch one manually so you know how to re-scan on demand.

After you select the `production` account, select the **Actions** drop-down, choose the **Scan** action, and select the **Scan** button.

## View account discovery progress

Discovery will kick off a scan across each child account / region in parallel and as resources are discovered you will begin to see a status of the number of resources known to Pulumi.

As each account scan completes, you will see a checkmark and status update per account. The scan duration will depend on the number of resources for each account, however as soon as they are discovered you can begin to explore insights and do not have to wait for the entire discovery to finish.

Let's introduce the Pulumi Resource Explorer for your newly discovered resources and learn how to draw insights about your cloud infrastructure.

{{< get-started-stepper >}}
