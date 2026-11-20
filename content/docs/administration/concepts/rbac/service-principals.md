---
title_tag: "Pulumi Cloud: Service principals"
meta_desc: Learn how service principals give automation in Pulumi Cloud its own identity, with its own roles and entity access.
title: "Service principals"
h1: "Service principals"
menu:
  administration:
    name: Service principals
    parent: administration-concepts-rbac
    weight: 7
    identifier: administration-concepts-rbac-service-principals
---

A service principal is a non-human identity for automation. Each one holds its own roles and entity access, and whatever runs as it acts with exactly that access. Use a service principal when work shouldn't run as a person or as the whole organization: most often, a stack's [deployments](/docs/deployments/concepts/settings/pulumi-cloud-role/).

Service principals are available in the Essentials, Pro, and Enterprise editions. Assigning custom roles to a service principal requires Pro or Enterprise.

{{% notes type="info" %}}
A service principal is a Pulumi Cloud identity, unrelated to a Microsoft Entra ID service principal.
{{% /notes %}}

## Kinds of service principals

The **Service Principals** tab lists every service principal in your organization with its type:

| Type | Created by | Managed by |
|------|------------|------------|
| User-defined | A member of your organization | You: name, roles, and entity access. |
| Delivery pipeline | Pulumi Cloud, for each [Pulumi Delivery](/docs/delivery/concepts/identity/) pipeline that names no identity of its own | Delivery. It gets access to the pipeline's stacks when you register the pipeline, you can grant it more, and it's deleted with the pipeline stack. |
| Pulumi Agent | Pulumi Cloud, for each [custom agent](/docs/ai/agents/) | The agent's settings. Deleting the agent removes its service principal and its access. |

Every team also has a service principal that its [team access tokens](/docs/administration/concepts/access-tokens/#how-team-tokens-are-identified) authenticate as. It follows the team's access and isn't listed on this tab.

The rest of this page covers user-defined service principals.

## How a service principal gets access

A service principal gets access the same two ways a member does:

- **Organization-wide roles**, which apply to every stack, environment, and cloud account. In editions with [custom roles](/docs/administration/concepts/rbac/roles/#custom-roles) ({{< pulumi-cloud-editions "custom-roles" >}}), a service principal can hold any number of custom roles plus the built-in `Admin`, `Maintainer`, `Builder`, and `Reader` roles. In other editions, it has one organization-wide permission: None, Read, Write, or Admin.
- **Entity access**, a [permission set granted on a single stack, environment, or cloud account](/docs/administration/concepts/rbac/entities/#entity-access).

Unlike a member, a service principal never follows the organization's [default role](/docs/administration/concepts/rbac/default-roles/). Without a role, it has only its entity access, which makes it a good fit for least-privilege automation: start with None and grant only the stacks and environments the work needs.

A service principal also gets admin on the stacks and environments it creates, like any other [creator](/docs/administration/concepts/rbac/#creator-grants).

## Creating a service principal

To create a service principal, you need the `service_principal:create` scope, which the `Admin`, `Maintainer`, and `Builder` roles include. You can only give a service principal roles that you could grant yourself, so a Builder can create a service principal with `Reader` or `Builder` but not with `Maintainer` or `Admin`.

1. Navigate to **Settings** > **Access management** and select the **Service Principals** tab.
1. Select **Create service principal**.
1. Enter a name. Names can contain letters, digits, spaces, hyphens, underscores, and periods, are at most 64 characters long, and must be unique in the organization.
1. Choose the **Organization-wide role** (or **Organization-wide permissions**) the service principal starts with, or **None** to give it access only through entity access.
1. Select **Create service principal**.

You can also create one where you need it: in a stack's deployment settings, the service principal picker has a **Create new service principal** link.

## Changing what a service principal can access

Open the service principal from the **Service Principals** tab and select its **Access** tab.

- **Entity Access** lists the stacks, environments, and cloud accounts the service principal has a permission set on. Select **Add rule** to grant another one.
- **Organization-wide roles** lists the roles it holds. Select **Add role** to assign one or more roles. In editions without custom roles, this is an **Organization-wide permissions** dropdown instead.

You can also grant access from the other direction: open a stack, environment, or cloud account's [access settings](/docs/administration/concepts/rbac/entities/#entity-access), select **Add Principal**, and choose **Service Principal**.

Changing a service principal's roles or entity access requires the `org_member:update` scope.

## Running deployments as a service principal

A stack's deployments can run as a service principal, so every run has the same permissions no matter who or what starts it. See [Run as](/docs/deployments/concepts/settings/pulumi-cloud-role/) for how to select one and what it needs. In organizations on the [restricted permission mode](/docs/administration/concepts/rbac/permission-modes/), every stack's deployments run as a service principal or a team.

## Running Delivery pipelines as a service principal

A [Pulumi Delivery](/docs/delivery/) pipeline runs as a service principal too. By default, Delivery generates one for each pipeline; to control the pipeline's access yourself, name a service principal you created in the pipeline program. See [Pipeline identity](/docs/delivery/concepts/identity/).

## Renaming and deleting a service principal

Open the service principal and use the **Actions** menu:

- **Rename service principal** changes its name. Its access is unchanged. Requires `org_member:update`.
- **Delete service principal** removes its roles and entity access. Updates and deployments it started are kept. Requires `org_member:delete`.

You can't delete a service principal while a stack's deployment settings select it. Choose another identity for those stacks first.

## Service principals and editions

- Moving to an edition without custom roles resets each service principal to the closest of Read, Write, or Admin. Review them afterwards, because the closest match can be broader than the roles it replaces.
- Moving to the Free edition deletes the organization's user-defined service principals.

## Audit logs

Service principals don't appear in the organization's member list and are listed on the **Service Principals** tab instead. In [audit logs](/docs/administration/concepts/audit-logs/), a service principal appears by name as the actor of what it does, with a login of the form `service-principal:<id>` that stays the same when you rename it. Creating, renaming, and deleting a service principal, and assigning or removing its roles, are all recorded.

## Learn more

- [Run as](/docs/deployments/concepts/settings/pulumi-cloud-role/): Choose the service principal or team a stack's deployments run as.
- [Permission modes](/docs/administration/concepts/rbac/permission-modes/): Decide whether work that runs on behalf of your organization gets only the access it was explicitly given.
- [Entities and organization-level access](/docs/administration/concepts/rbac/entities): Grant a service principal a permission set on a single stack, environment, or cloud account.
