---
title: "Updated Resources View"
date: 2024-10-02T14:35:35-07:00
draft: false
meta_desc: The updated Resources page provides a new user experience for creating custom views that help you gain an understanding and insights into your infrastructure.

meta_image: meta.png
authors:
    - craig-symonds
tags:
    - insights
    - resources
---

Today we are excited to release an updated version of the Pulumi Insights Resources page that provides a new user experience for grouping, filtering and sorting, and enables you to create custom views to help you gain additional understanding and insights of your infrastructure.

<!--more-->

* **Grouping** provides a rich model for factoring your resources into logical groupings to help you gain insights over your infrastructure and plan actions in incremental groupings. To create a group, drag the column header to the grouping control. Note that you can create hierarchical groups by adding multiple columns and even rearrange the order of the groups.
* **Filtering** allows you to quickly find specific resources or groups of resources based on different attributes of the resource. Filtering can be done by selecting the filter icon in the column header for the column you want to filter by. This will present a drop down that enables you to select, or enter, the values to filter by. Adding column filters updates the Resource Search field to reflect the filters selected, in this way, the column filtering can be used to help create Resource Queries that can be reused in other contexts.
* **Sorting** is done in the standard way by clicking on the column header.

{{< video title="Grouping, Filtering, Sorting" src="grouping-sorting-filtering.mp4" autoplay="true" loop="true" >}}

The updated Resources page enables you to customize the view of your resources by enabling you to control the columns of the table. With the table actions menu you can add and remove columns as well as auto size each of the columns in the table to fit the current content. Like previous versions of the Resources page, this menu also enables you to export the Resources as a CSV file for integration into external tools.

{{< video title="Column Selection" src="column-selection.mp4" autoplay="true" loop="true" >}}

Once you have configured the resources view to provide the insights needed, you can now save that view as a pinned view under the Resource tab in the left navigation panel. These pinned views enable the Resources page to act as a dashboard to the most important views and insights into your infrastructure. The views are also defined in the url for the page which means you can freely copy the url and send it to collegue for them to have a look at, or add the URL to a work tracking system to provide context in the task definition.

{{< video title="Favorites" src="favorites.mp4" autoplay="true" loop="true" >}}

Overall, the new Resources page provides the tools needed to enable you to gain additional insights and track and manage those insights to ensure your infrastructure is delivering on the goals you have set.
