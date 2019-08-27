---
title: Project and Stack Management
_on_this_page: true
---

The Pulumi Console allows you to manage your projects and stacks. In your browser, navigate to [app.pulumi.com](https://app.pulumi.com). Once signed in, you can:

* Create new projects and get detailed instructions for deploying your stack via the [Pulumi CLI]({{< relref "/docs/reference/cli" >}})
* View stack outputs and configurations
* Review your stack activity, resources, and settings



## Creating a New Project

If you haven't been added to any Pulumi organizations with existing projects, the Console displays the **New Project** button upon signing in. Click **New Project** and follow the prompts.

<img class="lg:max-w-xl pb-4" src="/images/docs/reference/service/new-project.png" alt="Create a new Pulumi project">

To create a new project via the CLI, see [pulumi new]({{< relref "/docs/reference/cli/pulumi_new" >}}).

{{< get-started-note >}}

## Managing your Stacks

If you have been added to a Pulumi organization with existing projects and stacks, the Console displays a list of _Stacks_ and a _Recent Activity_ stream upon signing in. The lists are collapsible and are sorted according to the most recent updates. Click on a specific stack or activity for a more detailed view.

### Viewing your Stack Outputs and Configurations

Clicking on a stack update takes you to the Stack tab which displays your stack's outputs and configuration.

<img class="shadow-2xl lg:max-w-xl" src="/images/docs/reference/service/stack-outputs-and-configuration.png" alt="Stack Outputs and Configuration">

<img class="shadow-2xl lg:max-w-xl" src="/images/docs/reference/service/resource-graph.png" alt="Stack Resource Graph">
<img class="shadow-2xl lg:max-w-xl" src="/images/docs/reference/service/detailed-resource-view.png" alt="Detailed Stack Resource View">
<img class="shadow-2xl lg:max-w-xl" src="/images/docs/reference/service/detailed-configuration.png" alt="Detailed Stack Configuration View">
<img class="shadow-2xl lg:max-w-xl" src="/images/docs/reference/service/timeline.png" alt="Timeline">
<img class="shadow-2xl lg:max-w-xl" src="/images/docs/reference/service/change-summary.png" alt="Change Summary">


The Pulumi Service backend provides safe locking so that your resource state can never get corrupted by a concurrent update.

Navigate to previous stack updates, and see who applied what change and when. Or see the point-in-time history if an individual cloud resource.

<img class="shadow-2xl lg:max-w-xl" src="/images/docs/reference/service/stack-resource-visualization.png" alt="Stack Resource Visualization">
