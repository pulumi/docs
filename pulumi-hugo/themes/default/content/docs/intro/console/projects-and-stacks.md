---
title: Projects and Stacks
meta_desc: An overivew of Project and Stack Management within the Pulumi Cloud Service.
menu:
  intro:
    parent: console
    weight: 4
aliases:
- /docs/intro/console/project-and-stack-management/
- /docs/reference/service/roles-and-access-controls/
- /docs/console/collaboration/stack-permissions/
- /docs/intro/console/stack-permissions/
---

Projects group stacks together and are folders containing a Pulumi.yaml file.
Stacks are isolated, independently configurable instances of a Pulumi program.
Projects can have as many stacks as you need.

## Creating a Project

To create a project:

1. Navigate to **Projects**.
1. Select **Create project**.
1. Select a cloud and a language and use the **Next** button.
1. Optionally, change your project name and project description.
1. Select **Create project**.
1. Follow the provided CLI command instructions.

## Stack Permissions

The Pulumi Console provides fine-grained access controls for stacks. Stack permissions are
based on the member's role within the organization, and on their team membership.
Additionally, any member who creates a stack is granted admin permissions on that stack.

Organization admins can control the stack default permissions at the organization level from the organization's **Settings**.
There are four types of stack permissions: `None`, `Read`, `Write`, and `Admin`.
[Team permissions]({{< relref "/docs/intro/console/teams#team-permissions" >}}) will expand these default permissions.

Stack permissions allow users to perform the following actions:

| Action | None | Read | Write | Admin |
|--------|------|------|-------|-------|
| View update history | | ✅ | ✅ | ✅ |
| Decrypt secret configuration | | ✅ | ✅ | ✅ |
| Read stack resources | | ✅ | ✅ | ✅ |
| Preview stack changes | | ✅ | ✅ | ✅ |
| Update stack | | | ✅ | ✅ |
| Destroy stack (`pulumi destroy`) | |   | ✅ | ✅ |
| Export stack checkpoint | | ✅ | ✅ | ✅ |
| Import stack checkpoint |  | | ✅ | ✅ |
| Delete stack (`pulumi stack rm`) | | | | ✅ |
| Transfer to another organization | | | | ✅ |

## Viewing Stacks

![Organization projects and stacks](/images/docs/reference/service/organization-stacks.png)

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

Custom stack tags can help you group and filter your stacks.

To create a custom tag:

1. Navigate to **Projects** and then a specific stack.
1. Select **New tag**.

To modify or delete a custom tag:

1. Navigate to **Projects** and then a specific stack.
1. To modify a custom tag, use the pencil icon.
1. To delete a custom tag, use the trash can icon.

#### Stack Activity

To view stack activity:

1. Navigate to **Projects** and then a specific stack.
1. Navigate to **Activity**.
1. Review insights and operations that were performed on your stack resources during the update.
1. Navigate to **Changes**, **Timeline**, or **Configuration** for more details.

The **Changes** section of activity lets you toggle between different log views:

* _Summary Log_ which lists a summary of changes, counts of affected resources, and update duration
* _Diff Log_ which displays a diff of the changes (created, updated, or deleted resources), your stack outputs, and the same counts and update duration shown in the Summary Log view.
* _Diagnostic Log_ which displays warning messages or a description of the operations performed during the update (if any).

![Stack resource graph](/images/docs/reference/service/resource-changes.png)

The **Timeline** section provides a detailed timeline of changes to individual cloud resources. It also includes useful resource links and counts of affected resources.

![Stack resource graph timeline](/images/docs/reference/service/timeline.png)

The **Configuration** section displays the same configuration details that you can find in the Stack view for your update.

#### Stack Resources

To view a stack's resources:

1. Navigate to **Projects** and then a specific stack.
1. Navigate to **Resources**.
1. Select **List View** or **Graph View** to toggle between a list view and a graph view.
1. Selecting an individual resource from the list or graph view will provide more details.

The list view displays a list of all of the stack's resources including their type, name,
status, and link to the associated cloud provider.

![Stack resource list](/images/docs/reference/service/stack-resource-list.png)

The graph view displays a graphical representation of the stack's resources and their
dependencies. Select an individual resource to view its list of properties and dependencies.

![Stack resource visualization](/images/docs/reference/service/stack-resource-visualization.png)

## Transferring Stacks

Stack admins can transfer their stacks between personal accounts and organizations or between organizations.

If transferring to an organization, the **Allow organization members to create stacks and transfer stacks to this organization**
setting must be turned on from the **Access Management** page in the organization's settings.

To transfer a stack:

1. Navigate to the stack, and then the stack's **Settings**.
1. Select **Transfer stack**.
1. Provide the personal account or organization name and select **Transfer**.

## Deleting a Stack

Deleting a stack removes the stack entirely from the Pulumi Service, along with all of its update history.

To delete a stack:

1. Navigate to **Projects** and then a specific stack.
1. Navigate to the stack's **Settings**.
1. Follow the instructions in the _Danger Zone_.

## Related Blogs

* [Building New Pulumi Projects and Stacks From Templates]({{< ref "/blog/building-new-pulumi-projects-and-stacks-from-templates" >}})
