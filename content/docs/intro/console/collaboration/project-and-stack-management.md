---
title: Project and Stack Management
meta_desc: An overivew of Project and Stack Management within the Pulumi Cloud Service.
---

> While you can create projects within the individual organization created for your account, instructions in this document apply to members of an organization with sufficient [stack permissions]({{< relref "stack-permissions" >}}).

The Pulumi Console automatically manages deployment state and gives you a comprehensive view of your projects and stacks. In your browser, navigate to [app.pulumi.com](https://app.pulumi.com). Once signed in, you can:

* Create new projects and get detailed instructions for deploying your stack via the [Pulumi CLI]({{< relref "/docs/reference/cli" >}})
* View your organization stacks
* View stack outputs and configurations
* Review your stack activity, resources, and settings

## Creating a New Project

If you have been added to a Pulumi organization with no existing projects, the Console displays the **New Project** button upon signing in. Click **New Project** and follow the prompts.

<img class="lg:max-w-xl pb-4" src="/images/docs/reference/service/new-project.png" alt="Create a new Pulumi project">

Click **Create Project** to get started with your project. The confirmation page gives you installation, setup, and stack deployment instructions.

To create a new project via the CLI, see [pulumi new]({{< relref "/docs/reference/cli/pulumi_new" >}}).

{{< get-started-note >}}

## Managing your Stacks

Every Pulumi program is deployed to a [stack]({{< relref "/docs/intro/concepts/stack" >}}). If you have followed the instructions after creating your project, you can view your newly-created stack in the Pulumi Console unless you have [explicitly opted out]({{< relref "/docs/intro/concepts/state" >}}). The Pulumi Console provides safe locking so that your resource state can never get corrupted by a concurrent update.

### Viewing your organization stacks

Once signed in, select your organization from the drop-down list on the upper left corner of the screen. The **Stacks** tab is displayed by default.

<img class="lg:max-w-xl" src="/images/docs/reference/service/organization-stacks.png" alt="Stack Outputs and Configuration">

The **Stacks** tab displays a card-based view of your stacks with relevant details including the project name and description, language, stack name, last update information, and resource count. This example shows an organization backed by GitHub and sorts the stacks by their GitHub repositories. By default, stacks are grouped by [project]({{< relref "/docs/intro/concepts/project" >}}) but you may group them by [tag]({{< relref "/docs/intro/concepts/stack#stack-tags" >}}). Click on the stack name to drill into a specific stack.

### Viewing a specific stack

If you have been added to a Pulumi organization with existing projects and stacks, the Console displays a list of _Stacks_ and a _Recent Activity_ stream when you sign in. The lists are collapsible and are sorted according to the most recent updates. Click on a specific stack update or activity for a more detailed view.

#### Stack View

Clicking on a specific stack update takes you to the Stack tab. This tab displays your stack's outputs, configuration values, and tags and renders a web-based view of the resulting output when you run `pulumi config` and `pulumi stack output` from the command line.

<img class="lg:max-w-xl" src="/images/docs/reference/service/stack-outputs-and-configuration.png" alt="Stack Outputs and Configuration">

You can see other details such as who applied the update and when, as well as counts of added, updated, and unchanged resources. If your stack is integrated with your workflow, such as [GitHub Actions]({{< relref "/docs/guides/continuous-delivery/github-actions" >}}), you should also see useful links to data like your Git commit hash, mapped branch, and pull request ID.

##### Stack tags

Custom [stack tags]({{< relref "/docs/intro/concepts/stack#stack-tags" >}}) can be managed within the Stack tab. Click the **NEW** button to create a new tag, the pencil to edit an existing tag, or the trash can to permanently delete a tag.

<img class="lg:max-w-xl" src="/images/docs/reference/service/stack-tags.png" alt="Stack Tags">

#### Detailed Activity View

By default, the Activity tab gives you a card-based list of stack updates sorted by date.

Clicking on "Details" from the Stack update tab, or clicking on a specific activity from the login screen gives you a detailed view of that specific update. The Activity tab provides insights into the operations that were performed on your stack resources during an update. This tab can include three tabs, depending on your setup:

* **Changes**. This lets you toggle between different log views:
<img class="lg:max-w-xl m-6" src="/images/docs/reference/service/resource-changes.png" alt="Stack Resource Graph">
    * _Summary Log_ which lists a summary of changes, counts of affected resources, and update duration
    * _Diff Log_ which displays a diff of the changes (created, updated, or deleted resources), your stack outputs, and the same counts and update duration shown in the Summary Log view.
    * _Diagnostic Log_ which displays warning messages or a description of the operations performed during the update (if any).

* **Timeline**. This gives you a detailed timeline of changes to individual cloud resources. It also includes useful resource links and counts of affected resources.

<img class="lg:max-w-xl m-6" src="/images/docs/reference/service/timeline.png" alt="Stack Resource Graph">

* **Configuration**. This displays the same configuration details that you can find in the Stack view for your update.

#### Resources View

You can click on a resource link from **Activity > Timeline** to drill into a specific resource's properties and dependencies, if any. The Resources tab lets you toggle between a list and a graph view.

##### List View

The Resource list view includes a useful search and filtering feature. You may filter by resource type which is broken down into three categories: Data, Compute, and Operations. Some resources include links to their associated pages in the cloud provider's console. For example, a Route 53 record set in the AWS Console.

<img class="lg:max-w-xl" src="/images/docs/reference/service/stack-resource-list.png" alt="Stack Resource Visualization">

To view the properties and dependencies of a specific stack resource, click on the individual resource. At the bottom of the Properties list is a "Details" link that renders the same list in JSON format.

##### Graph View

The Resource graph view does not include a search and filtering feature, but you may still click on individual resources to view its list of properties and dependencies.

<img class="lg:max-w-xl" src="/images/docs/reference/service/stack-resource-visualization.png" alt="Stack Resource Visualization">

### Deleting a stack

When drilling into a specific stack, organization members with [sufficient permissions]({{< relref "/docs/intro/console/collaboration/organization-roles#stack-deletion" >}}) have the additional option of being able to delete the stack. Note that this removes the stack entirely from the Pulumi Service, along with all of its update history.

## Next Steps

* [Continuous Delivery]({{< relref "/docs/guides/continuous-delivery" >}})
