---
title_tag: Using Research Search | Pulumi Insights
title: Using Insights Resource Search
h1: "Pulumi Insights: Using Resources Search"
meta_desc: This page provides an overview on how to get started with Pulumi Insights Accounts.
weight: 4
menu:
  insights:
    parent: insights-get-started
    identifier: insights-get-started-resource-search
    weight: 4
---

[Pulumi Resource Search](/docs/pulumi-cloud/insights/search/) offers multi-cloud search and analytics across every environment in your organization. You can issue queries that find all of your AWS VPCs, or all of your VPCs in AWS and Azure, or all resources with the “production” tag across all cloud environments. You also have access to statistics about cloud usage, including a breakdown by cloud provider, resource type, and department. Resource search enables you to find the needle within your cloud haystack and visualize cloud consumption trends.

Pulumi Resource Search is composed of:

- **Query syntax**: Infrastructure can be discovered interactively with a rich, structured query language, for example package:snowflake.
- **AI Assist**: A natural language query interface that generates the query syntax for you. You can use it to express queries where you might not know the exact syntax, type tokens, or package names.
- **Search advanced filtering**: Advanced filtering allows you to see aggregations over your data at a glance, such as top stacks, projects, providers, teams and types by resource count. Additionally, if you are searching for something specific they can help you understand the shape of your search results and further refine them.
- **Search API**: We understand that console searches aren’t the only way our customers want to utilize Resource Search. To meet this need, we’re also launching new Resource Search API endpoints, allowing you to integrate Resource Search into your internal systems and workflows. Use the API to add search functionality to your Internal Developer Platform or create automation around search results. To learn more about the API spec details view the [Pulumi Service REST API documentation](https://www.pulumi.com/docs/pulumi-cloud/cloud-rest-api/#resource-search).
- **Data Export**: Export resource data to ingest in your data warehouse.

{{< get-started-stepper >}}
