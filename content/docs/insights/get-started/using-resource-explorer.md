---
title_tag: Using Research Explorer | Pulumi Insights
title: Using Insights Resource Explorer
h1: "Pulumi Insights: Using Resources Explorer"
meta_desc: This page provides an overview on how to get started with Pulumi Insights Accounts.
weight: 5
menu:
  insights:
    parent: insights-get-started
    identifier: insights-get-started-resource-explorer
    weight: 5
---

[Pulumi Resource Explorer](/docs/insights/) offers multi-cloud search and analytics across every environment in your organization. You can issue queries that find all of your AWS VPCs, or all of your VPCs in AWS and Azure, or all resources with the “production” tag across all cloud environments. You also have access to statistics about cloud usage, including a breakdown by cloud provider, resource type, and department. Resource search enables you to find the needle within your cloud haystack and visualize cloud consumption trends.

![Insights Account Discovery Scan](/docs/insights/assets/insights-resource-explorer.png)

Pulumi Resource Explorer is composed of:

- **Query syntax**: Infrastructure can be discovered interactively with a rich, structured query language, for example package:snowflake.
- **AI Assist**: A natural language query interface that generates the query syntax for you. You can use it to express queries where you might not know the exact syntax, type tokens, or package names.
- **Search advanced filtering**: Advanced filtering allows you to see aggregations over your data at a glance, such as top stacks, projects, providers, teams and types by resource count. Additionally, if you are searching for something specific they can help you understand the shape of your search results and further refine them.
- **Search API**: Allows you to integrate Resource Search into your internal systems and workflows. Use the API to add search functionality to your Internal Developer Platform or create automation around search results. To learn more about the API spec details view the [Pulumi Service REST API documentation](https://www.pulumi.com/docs/pulumi-cloud/cloud-rest-api/#resource-search).
- **Data Export**: Export resource data to ingest in your data warehouse.

## Example use cases

The Resources Explorer and Resources Search enables you to ask questions that significantly improves the process for managing your infrastructure and getting answers to key questions needed for your projects.

Let's look at some common use cases and questions you might have about your infrastructure using [keywords, query syntax](/docs/insights/search/) as well as Pulumi AI assist, where you can type what you’re looking for Pulumi will suggest the search syntax.

### Search with keywords or query syntax

- See all resources that have been modified in the last 30 days

`modified:<now-30d`

![Insights Account Discovery Scan](/docs/insights/assets/resource-explorer-filter-30days.png)

You can also filter your search using the most common keywords, such as **Type**, **Project**, **Stack** and more.

To see all resources with a certain tag in your cloud provider, you can use the following syntax, which is important if you are looking for all resources owned by a certain cost enter.

`type:aws:s3/bucket:Bucket tags.costcenter:1234`

### AI Assist examples

To quickly find the right keywords and search syntax, you can ask natural language questions and let Pulumi AI assist suggest the correct search syntax.

**"show me all virtual machines"**

`type:"aws:ec2/instance:Instance" OR type:"azure:compute/virtualMachine:VirtualMachine"`

![Insights Explorer Ai assist vm](/docs/insights/assets/resource-explorer-pulumi-ai-assist-vm.png)

Let's say you are working with your security team as part of an audit, you could quickly find (or confirm compliance) on risks such as public facing S3 buckets.

**"show me all s3 public buckets"**

`type:"aws:s3/bucket:Bucket" .acl:public-read'

![Insights Explorer Ai assist public s3](/docs/insights/assets/insights-explorer-pulumi-ai-assist-public-s3.png)

With Pulumi Copilot and Resource Search, you are able to gain insights and ask questions about your infrastructure that would otherwise be challenging to answer, saving time and providing the critical information needed

{{% notes "info" %}}
Insights Account Discovery is free while in public preview, with per-resource pricing for Team, Enterprise and Business Critical tiers coming in Q1 2025.
{{% /notes %}}

{{< get-started-stepper >}}
