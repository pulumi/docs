---
title: Resource explorer
meta_desc: Learn how to visually explore your cloud infrastructure with Pulumi Resource Explorer using filters, grouping, and AI Assist.
title_tag: Pulumi Resource Explorer | Pulumi Insights
menu:
  insights:
    parent: insights-resources
    identifier: insights-resource-explorer
    weight: 1
---

Pulumi Resource Explorer gives you a real-time view of your infrastructure across every stack, project, and cloud provider. It’s the fastest way to explore your resources visually—no query syntax required. All scanned resources are displayed on the **Resources** page in Pulumi Cloud.  

Use Resource Explorer to:

* Filter and group resources by tag, type, project, stack, or provider
* Quickly answer common infrastructure questions
* Collaborate with your team during audits, cost reviews, and troubleshooting
* Jump directly into a stack or resource for further investigation

### Viewing resources in the grid

* **Grid structure**:  
  * **Project column**: Displays the ultimate parent account name.  
  * **Stack/Account column**: Displays the full child account path. For example:  
    * **Project**: `my-aws-account`  
    * **Stack/Account**: `us-east-1/my-cluster`

![Resources page](/docs/insights/assets/insights-resource-explorer.png)

* **Resource navigation**: Click on a resource's name to view its resource details. This page includes:  
  * **Resource history**: Pulumi tracks and displays all versions of a resource, with changes based on property updates.  
  * **Properties**: View detailed properties for each resource version.  
  * **References**: See edges (relationships) to other resources in the same account.

![Resource details page](/docs/insights/assets/insights-resources.png)
