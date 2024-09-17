---
title: "Introducing Pulumi Insights 2.0"
date: 2024-09-16T16:29:14-07:00
draft: false
meta_desc: Insights 2.0 brings a significantly updated set of automation and visualization tools to help you quickly gain visibility and control of your infrastructure. 
meta_image: meta.png
authors:
    - luke-hoban
tags:
    - insights
---

Since the launch of Pulumi Cloud Insights, we have seen significant growth in usage. Customers have used each of the tools to gain valuable insights into their IaC infrastructure through both the flexibility of [Resource Search](https://www.pulumi.com/blog/resource-search/) and the power of [Pulumi CrossGuard](https://www.pulumi.com/crossguard/). With Insights 2.0 we are significantly expanding the set of automation and visualization tools to quickly gain visibility, insight and control and improve the Security, Compliance and Efficiency of your infrastructure.

<!--more-->

Insights 2.0 builds on the previous generation of tools to provide a range of new capabilities:

* Expands Pulumi Providers to enable scanning and import of your entire infrastructure state into the Pulumi Data Graph  
* Adds Explorers, Structure Graphs and Dashboards for visualizing, understanding and managing your entire infrastructure  
* Extends CrossGuard PaC to discover and auto remediate insights into Security, Compliance and Efficiency  
* Integrates Pulumi IaC for enterprise class remediation and management  
* Brings CoPilot AI to your entire infrastructure for intelligent insight discovery and analysis

![Component Summary](component-summary.png)

## Resources 2.0

The updated Resources page provides a customizable experience for grouping, sorting, filtering and visualizing your resources to help you manage the scope and find insights about your infrastructure.

**Sorting:** Clicking on the column header enables you to sort the selected column in ascending order. Clicking again switches it to descending order and clicking a third time removes the sorting. Multiple column sorts can be done with the sort precedence being based on the order the columns we last clicked on.  

**Filtering:** Adding filters to each column can be done by selecting the first icon in the column header. A filter dialog will be displayed based on the type of data present in the column. If the data is made up of unique values, like the Name field, then a standard search text box is presented. If it is a date, then the date range selection dialog is presented. Otherwise you are presented with the list of unique values in the column where you can select multiple to filter with. Adding a column filter will add the specific filter to the Resource Search query enabling you to use the grid as a form of query builder.

![Filtering](filtering.png)

**Grouping:** To group by a particular column, drag and drop the column header to the grouping control in the top left of the grid. You can group by multiple columns and can control the order of the grouping by reordering them in the grouping control. Grouping enables you to factor your resources in different ways to help you understand the scope of your infrastructure and find insights for future investments.

![Grouping](grouping.mov)

**Column Selection:** To add or remove columns from the grid, select the ‘Choose Columns’ menu item from the column menu selector. This presents a pop up to allow you to add, remove or rearrange the order of columns in the grid.

![Choose Columns](choose-columns.png)

**Column Resize:** You can resize the width of a column by clicking and dragging on the column boundary line on the right side of the column header. To automatically resize the column to the width of the widest cell contents, double click on the boundary line.

**Copy Contents:** You can couple the contents of a cell to the clipboard by right clicking on the cell and selecting Copy. This is particularly useful for resource values you need to use in other contexts like the Name or URN.

## Policy Violations

The Policy Violations page provides a comprehensive view of all policy violations across your organization, helping you maintain visibility and control over your infrastructure. See the [Policy Violations](https://www.pulumi.com/blog/centralized-policy-violations/) blog post for more information.

## Resource Structure Graph

The new resource structure graph provides a visual representation of the relationships for a selected resource. This provides the additional context needed to understand the structure around the resource and what actions might need to be taken.

Within this view you can navigate the relationships by clicking on the related resources. When a resource clicked, the Resource Detail view will navigate to the selected resource to give you the details needed to understand that context.

Policy violations are indicated on the Resource Structure graph to quickly highlight when an insight has been detected and what related nodes are affected.

![Resources Graph](graph.png)

## User Customizable Dashboard

***Coming Soon***

Pulumi Cloud will provide a rich, user customizable dashboard that enables you to define rolled up views of any aspect of your infrastructure. This provides a powerful overview of your infrastructure and lets you easily track progress of any project.

The dashboard supports defining multiple pages so you can create separate dashboards for each application, each department, or any configuration that maps to your configuration.

Each dashboard page enables you to add, remove, rearrange and create new cards. Each new card can be customized to show the aggregate results of a resource field or property including related policy violation fields. The card can be configured to use a variety of different chart and graph visualizations that best suit the associated data.

![Dashboard](dashboard.png)

## Infrastructure Account Scanning

***Coming Soon***

We are excited to introduce Infrastructure Account Scanning (IAS). IAS fundamentally transforms Pulumi Cloud into a rich Asset Management and Insights platform that brings all of the Pulumi Insights capabilities to your entire infrastructure. With IAS, Pulumi can scan your entire infrastructure, even resources that are not IaC managed, and keep them up to date with any changes. This enables you to leverage all of the Insights 2.0 tools like, the Resource Explorer with Resource Structure Graphs, Pulumi CrossGruard with Auto Remediation and the Policy Violations Explorer, and the User Customizable Dashboard to manage your entire infrastructure.

IAS leverages the rich ecosystem of Pulumi Platform Providers to discover and read your resources independently of whether they have been moved to IaC.

With IAS Account management you can quickly configure how Pulumi Cloud is enabled to discover new or changed resources keeping your customized Resources, Policy Violations and Dashboard views up to date with your physical infrastructure.

![Account Scanning](account-scan.png)

## Auto Remediation

***Coming Soon***

Insights 2.0 provides you the tools needed to understand your infrastructure and find the insights needed to enable you to define the strategic projects that move your infrastructure forward. However, in addition to these tools for finding the insights, Pulumi Cloud also gives you the context and tools needed to remediate the issues.

When a policy violation occurs for a given resource and that policy is an ([Auto Remediation](https://www.pulumi.com/blog/remediation-policies/)) policy, a ‘Remediate’ button will be displayed in the Resource Details page. When selected, the Remediate button will run the remediation and show a diff of the infrastructure changes that will be applied in order to remediate targeted insight. If approved, Pulumi Cloud will apply the changes defined by the diff to your infrastructure using the associated Pulumi Providers.

Any change made through the Remediation flow will be tracked and auditable using the Pulumi Audit tools to give you confidence and tracking of the changes made to your infrastructure. In addition, this Remediation flow will provide a warning if the Resource is IaC managed as this change would cause drift with the underlying IaC code. For IaC managed resources it is recommended that you use the new Goto Definition feature to jump to the IaC code for the resource to apply the necessary remediation in the code.

![Remediation](remediation.png)

## Goto Definition

***Coming Soon***

For any resource that is Pulumi IaC managed, the Resource Details page will contain a link to the file and line of code in your source code provider that defines the given resource.

![Goto Definition Link](goto-definition-link.png)

Selecting this link will take you to the file and line making it easy for you to quickly see and edit the IaC code for the given resource.

![Goto Definition Code](goto-definition-code.png)

## Resource Query Import

Being able to browse your entire infrastructure and find the insights needed to move your platform forward enables you to understand and build strategic plans around your infrastructure. However, leveraging Pulumi IaC for managing your resources gives you the best in class tools for creating, updating and refactoring your resources to ensure your infrastructure is delivering on your strategic goals. With Insights 2.0, you can levarage the Insights 2.0 tools to create queries that define a block or resources you would like to import into IaC significantly simplifying the process.

The Pulumi cli import command will now support passing a Resource Query as a parameter. The results of this query will be used to get the resource IDs and types needed to be able to import the resources into your IaC program. The result of the command is the source code needed to construct each of the resources defined by the query.

```shell
pulumi import \-q ‘.volumeType:Standard’
...
import * as pulumi from "@pulumi/pulumi";
import * as aws_native from "@pulumi/aws-native";

const EC2Volumevol0a789ea1874bfac61 = new aws_native.ec2.Volume("EC2Volumevol0a789ea1874bfac61", {
    autoEnableIo: true,
    availabilityZone: "us-west-2b",
    encrypted: false,
    multiAttachEnabled: false,
    size: 8,
    snapshotId: "snap-0d017523dfd31e801",
    tags: [],
    volumeType: "standard",
}, {
    protect: true,
});
...

```

## Conclusion

Insights 2.0 provides you the set of tools needed to understand the chaos of modern enterprise clouds and to bring that chaos under control. The ability to scan your entire infrastructure enables you to leverage the rich visualization, remediation, and IaC migrations tools for all aspects of your infrastructure and gives you the insights needed to enable you to deliver on your strategic objectives.  
