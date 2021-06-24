---
title: Project and Stack Management
meta_desc: An overivew of Project and Stack Management within the Pulumi Cloud Service.
menu:
  intro:
    parent: console
    weight: 4
---

{{% notes "info" %}}
While you can create projects within an individual account, instructions in this document apply to members of an organization with sufficient [stack permissions]({{< relref "/docs/intro/console/stack-permissions" >}}).
{{% /notes %}}

The Pulumi Console automatically manages deployment state and gives you a comprehensive view of your projects and stacks. In your browser, navigate to [app.pulumi.com](https://app.pulumi.com). Once signed in, you can:

* Create new projects and get detailed instructions for deploying your stack via the [Pulumi CLI]({{< relref "/docs/reference/cli" >}})
* View your organization stacks
* View stack outputs and configurations
* Review your stack activity, resources, and settings

## Creating a Project

To create a project:

1. Navigate to **Projects**.
1. Select **Create project**.
1. Select a cloud and a language and use the **Next** button.
1. Optionally, change your project name and project description.
1. Select **Create project**.
1. Follow the provided CLI command instructions.

## Managing your Stacks

Every Pulumi program is deployed to a [stack]({{< relref "/docs/intro/concepts/stack" >}}). If you have followed the instructions after creating your project, you can view your newly-created stack in the Pulumi Console unless you have [explicitly opted out]({{< relref "/docs/intro/concepts/state" >}}). The Pulumi Console provides safe locking so that your resource state can never get corrupted by a concurrent update.

### Viewing your organization stacks

![Stack outputs and configuration](/images/docs/reference/service/organization-stacks.png)

To view an organization's stacks:

1. Navigate to **Projects**.
1. Optionally, adjust the grouping by selecting the **Group By** and **Sort By** controls.
1. To view a stacks details select the name of the stack.
1. To view a specific stack update, navigate to **Activity** and select it from the list.

### Stack Detailed View

To view a stack's details:

1. Navigate to **Projects** and then a specific stack.
1. Navigate to **Activity**.
1. Review the stack's outputs, configuration values, and tags.

![Stack outputs and configuration](/images/docs/reference/service/stack-outputs-and-configuration.png)

You can see other details such as who applied the update and when, as well as counts of added, updated, and unchanged resources. If your stack is integrated with a CI/CD pipeline, such as [GitHub Actions]({{< relref "/docs/guides/continuous-delivery/github-actions" >}}), you also see useful links to data like your Git commit hash, mapped branch, and pull request ID.

#### Custom Stack Tags

![Stack tags](/images/docs/reference/service/stack-tags.png)

To create a custom tag:

1. Navigate to **Projects** and then a specific stack.
1. Select **New tag**.

To modify or delete a custom tag:

1. Navigate to **Projects** and then a specific stack.
1. To modify a custom tag, use the pencil icon.
1. To delete a custom tag, use the trash can icon.

#### Activity

To view stack activity:

1. Navigate to **Projects** and then a specific stack.
1. Navigate to **Activity**.
1. Review insights and operations that were performed on your stack resources during the update.
1. Navigate to **Changes**, **Timeline**, or **Configuration** for more details.

##### Changes

This lets you toggle between different log views:

* _Summary Log_ which lists a summary of changes, counts of affected resources, and update duration
* _Diff Log_ which displays a diff of the changes (created, updated, or deleted resources), your stack outputs, and the same counts and update duration shown in the Summary Log view.
* _Diagnostic Log_ which displays warning messages or a description of the operations performed during the update (if any).

![Stack resource graph](/images/docs/reference/service/resource-changes.png)

##### Timeline

This gives you a detailed timeline of changes to individual cloud resources. It also includes useful resource links and counts of affected resources.

![Stack resource graph timeline](/images/docs/reference/service/timeline.png)

##### Configuration

This displays the same configuration details that you can find in the Stack view for your update.

#### Resources View

To view a stack's resources:

1. Navigate to **Projects** and then a specific stack.
1. Navigate to **Resources**.
1. Select **List View** or **Graph View** to toggle between a list view and a graph view.

##### List View

The Resource list view includes a useful search and filtering feature. You may filter by resource type which is broken down into three categories: Data, Compute, and Operations. Some resources include links to their associated pages in the cloud provider's console.

![Stack resource list](/images/docs/reference/service/stack-resource-list.png)

To view the properties and dependencies of a specific stack resource, select an individual resource. At the bottom of the Properties list is a "Details" link that renders the same list in JSON format.

##### Graph View

Select an individual resources to view its list of properties and dependencies.

![Stack resource visualization](/images/docs/reference/service/stack-resource-visualization.png)

### Deleting a stack

Deleting a stack removes the stack entirely from the Pulumi Service, along with all of its update history.

To delete a stack:

1. Navigate to **Projects** and then a specific stack.
1. Navigate to the stack's **Settings**.
1. Follow the instructions in the _Danger Zone_.

## Related Blogs

* [Building New Pulumi Projects and Stacks From Templates]({{< ref "/blog/building-new-pulumi-projects-and-stacks-from-templates" >}})
