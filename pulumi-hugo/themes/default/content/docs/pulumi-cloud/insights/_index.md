---
title_tag: "Pulumi Insights Overview"
meta_desc: Pulumi Insights provides advanced search, analytics, and AI for your infrastructure as code.
title: Insights
h1: Pulumi Insights
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    identifier: insights
    weight: 7
aliases:
- /docs/intro/insights/
---

Pulumi Insights provides advanced search, analytics, and AI for your infrastructure as code.

It provides:

- **Resource Search**: Explore all of your resources under management.
  Filter resources by stack, project, or a number of other dimensions.

- **Resource Search Aggregates**: See aggregates at a glance for your resources under management.
  Start with a birds-eye view of your infrastructure, and leverage search to dig deeper.

- **Cloud Import**: Bring your own cloud provider account and import all your existing resources into Pulumi to see how things break down. Zero code required.

- **Data Export**: Export your Pulumi resources into your business intelligence tool of choice to go even further.

- **Resource Search AI Assist**: (experimental) Use natural language processing to help craft search queries to explore your data.

## Resource Search

<iframe width="560" height="315" src="https://www.youtube.com/embed/pMEIX7LmXYo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Resource Search can be accessed directly from the Pulumi Cloud dashboard or from the side navigation by navigating to **Resources**.

By default, you will see a table with the resources you have access to, ordered by most recently updated.

A count is shown the upper-right corner with the total number of resources matched by this query -- in this case, we have 70 resources.

![Resource Search Table](search-table.png)

You can control how many resources are displayed per page and paginate through your resources by using controls on the bottom of the page:

![Resource Search Pagination](search-pagination.png)

{{% notes "info" %}}
If you need access to more resources, you can use the [Data Export](export) feature or access them programmatically via the [Pulumi Cloud Rest API](/docs/pulumi-cloud/cloud-rest-api#resource-search).
{{% /notes %}}

Use the search bar to refine the resources displayed on the page.

Selecting **project** will pre-populate a query with `project:` which we can then extend to `project:production` to return resources with "production" in their project name.

Selecting the **Filters** menu to augments or pre-populate queries with helpful date ranges.

![Resource Search Filters](search-filters.png)

The columns displayed on results can be modified to show or hide information by selecting the gear icon.

![Resource Search Columns](search-columns.png)

Selecting a column header will modify the query to sort by that column.

### Resource Search Aggregates

The **Advanced filtering** menu can be expanded to apply additional filters to your query and to view finer-grained resource counts.

![Resource Search Advanced Filters](search-advanced.png)

In this example, the query has been restricted to the "my-stack" stack.

The counts next to each value show that this stack has 18 subnets, and 366 AWS resources in total.

Selecting **Clear filters** will remove all previously selected filters.

## Data Export

{{% notes "info" %}}
This feature is only available to organizations using the Enterprise and Business Critical editions.
If you don't see it in your organization, [contact us](/contact?form=sales).
{{% /notes %}}

Organizations with Data Export enabled are able to export all resources matching a particular query in CSV format.

For a more detailed description of CSV schema, see the [export documentation](export).

## APIs

See the [Pulumi Cloud REST API](/docs/pulumi-cloud/cloud-rest-api#resource-search) for full details of the API endpoint to query and export resources.
