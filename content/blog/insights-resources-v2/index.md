---
title: "Introducing the new Resources view"
date: 2024-10-02T14:35:35-07:00
draft: false
meta_desc: The updated Resources page provides a new user experience for creating
  custom views that help you gain an understanding and insights into your infrastructure.

meta_image: meta.png
authors:
  - craig-symonds
tags:
  - insights
  - resources
search:
  keywords:
    - resources
    - insights
    - infrastructure
    - resources view
    - resource explorer
    - pinned views
---

Pulumi Insights gives you the tools to stay informed about your cloud infrastructure. Our Resource explorer provides advanced search and filtering too [find what you need](/blog/resource-search). Today, we are excited to release an update that adds new ways to factor your resource data, and share those views with other users in your organization!

<!--more-->

### Factoring the Data

Being able find and group your resources using different fields and properties is the key to gaining the insights needed to understand the status of your infrastructure and determine any future projects needed. The new Resources view provides several updated tools for doing this factoring.

* **Groups** - Resources can be grouped into logical categories, including nested groups. Group resources by properties like stack, modified time, or category to explore your infrastructure from different angles. Relevant aggregations are included for each grouping to help you understand the information at a glance.
* **Filters** - Columns provide type-specific filters to narrow your search. Filters work in conjunction with the free-form search bar, giving you the control to build focused views for different aspects of your infrastructure.
* **Sorting** - Each column supports sorting, and multi-sort support allows multiple columns to be included in the ordering.

{{< video title="Grouping, Filtering, Sorting" src="grouping-sorting-filtering.mp4" autoplay="true" loop="true" >}}

### Customizing Columns

The updated Resources page enables you to customize the view of your resources by enabling you to control the columns of the table. With the table actions menu you can add and remove columns as well as auto size each of the columns in the table to fit the current content. Like previous versions of the Resources page, this menu also enables you to export the Resources as a CSV file for integration into external tools.

{{< video title="Column Selection" src="column-selection.mp4" autoplay="true" loop="true" >}}

### Pinning Favorite Views

Once you have configured the resources view to provide the insights needed, you can now save that view as a pinned view under the Resource tab in the left navigation panel. These pinned views enable the Resources page to act as a dashboard to the most important views and insights into your infrastructure. The views are also defined in the url for the page which means you can freely copy the url and send it to a collegue, or add the URL to a work tracking system to provide context in the task definition.

{{< video title="Favorites" src="favorites.mp4" autoplay="true" loop="true" >}}

Overall, the new Resources page provides the tools needed to enable you to gain additional insights and track and manage those insights to ensure your infrastructure is delivering on the goals you have set.
