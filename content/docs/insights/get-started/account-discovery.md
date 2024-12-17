---
title_tag: View and query infrastructure resources | Pulumi Insights
title: Using Insights Resources view
h1: "Pulumi Insights: Using Resources view"
meta_desc: This page provides an overview on how to get started with Pulumi Insights Accounts.
menu:
  insights:
    parent: insights-get-started
    identifier: insights-get-started-resources
    weight: 4
---

Now that you scan is underway you can view the **Accounts** page to see a list of all your created accounts along with the current status of the latest account scans.

## Understanding your infrastructure

As each of your Accounts start scanning, your resources will be displayed in the Insights Resources Explorer. The Resources Explorer and Resources Search enables you to ask questions and factor your resources into logical groupings that significantly improves the process for managing your infrastructure and getting answers to key questions needed for your projects. For example, you can ask the AI Resource Search to ‘Find all public IP addresses’ and any other question you might have about your infrastructure.

Let's start with how to filter resources using the Resources Explorer.

## Resources Explorer

{{< video title="Discovered Resources" src="" autoplay="true" loop="true" >}}

### Grouping resources

To group by a particular column, drag and drop the column header to the grouping control in the top left of the grid. You can group by multiple columns and can control the order of the grouping by reordering them in the grouping control. Grouping enables you to factor your resources in different ways to help you understand the scope and uncover issues within your infrastructure.

### Filtering resources

Adding filters to each column can be done by selecting the filter icon in the column header. A filter dialog will be displayed based on the type of data present in the column. Adding a column filter will add the specific filter to the Resource Search query enabling you to use the grid as a form of query builder.

### Sorting resources

To sort your resources by a particular column, click once on the column header to sort in ascending order and click a second time to sort in descending order. To add or remove columns from the grid, select the **Choose Columns** menu item from the column menu selector. This presents a pop-up to allow you to add, remove or rearrange the order of columns in the grid.

You can also resize the width of a column by clicking and dragging on the column boundary line on the right side of the column header. To automatically resize the column to the width of the widest cell contents, double-click on the boundary line.

Finally, you can copy the contents of a cell to the clipboard by right-clicking on the cell and selecting Copy. This is particularly useful for resource values you need to use in other contexts like the Name or URN.

Next, you will learn how to search for resources using keywords, the search syntax and with Pulumi co-pilot's natural language searching for intelligent insight discovery and analysis.

{{< get-started-stepper >}}
