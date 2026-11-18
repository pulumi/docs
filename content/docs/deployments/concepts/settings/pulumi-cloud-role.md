---
title_tag: "Run As | Pulumi Deployments"
meta_desc: Choose the service principal, team, or role a stack's deployments run as in Pulumi Cloud, and what that identity needs access to.
title: "Run as"
h1: "Run as"
menu:
  deployments:
    name: Run as
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-pulumi-cloud-role
    weight: 95
---

A stack's deployment settings decide who its deployments run as in Pulumi Cloud. That identity's permissions determine whether a deployment can read stack references from other stacks, open environments, and manage organization resources such as teams, members, or OIDC issuers.

On the stack's **Settings** → **Deploy** page, the **Permissions** section has a **Run as** setting with these choices:

| Run as | What it means | Editions |
|--------|---------------|----------|
| **Service principal** | Every run uses a [service principal](/docs/administration/concepts/rbac/service-principals/) your organization manages, with its own permissions, no matter who or what starts it. | Essentials, Pro, Enterprise |
| **Team** | Every run uses the team's service principal, so the team's permissions apply. | {{< pulumi-cloud-editions "teams" >}} |
| **Deployment role** | Automatic runs use a background runner limited to this role. Manual runs use the permissions of whoever starts them. | Essentials, Pro, Enterprise |

In the Free edition, deployments always run as the organization's single member, and there's nothing to choose.

{{% notes type="warning" %}}
Deployment roles are being removed. Prefer a service principal or a team, which give every run the same permissions and are the only choices in organizations on the restricted [permission mode](/docs/administration/concepts/rbac/permission-modes/).
{{% /notes %}}

## Running as a service principal or a team

Select **Service principal** and pick one from the list, or select **Create new service principal** to create one without leaving the page. Select **Team** to run as a team's service principal instead.

The identity you select needs:

- **Stack Write on this stack.** If it doesn't have it, the console offers to assign it when you save. That requires permission to change the stack's access; otherwise, ask a stack admin to assign it on the stack's **Access** settings.
- **Environment Open on the environment the stack's runs open**, if the stack is linked to one. The console offers to assign this too.
- **Whatever else the program reads**: Stack Read on stacks it references, and Environment Open on environments it imports. Grant these as [entity access](/docs/administration/concepts/rbac/entities/#entity-access) or through a role.

Once a service principal or a team is selected:

- Every run uses its permissions, whether a person starts it from the console, the REST API triggers it, or a git push, schedule, or review stack does. The deployment's page shows who it ran as, for example **Runs as service principal deploy-prod**.
- It gets admin on the stacks and environments it creates during a run.
- The deployment settings can't set a `PULUMI_ACCESS_TOKEN` environment variable, and individual deployments and schedules can't override the identity or the runner pool.
- Only stack admins can select another identity, remove it, delete the deployment settings, or change the stack's runner pool.
- The service principal can't be deleted while the stack's settings select it.

You can only select a service principal or a team whose permissions you hold yourself, so the setting can't be used to gain access you don't have.

[Review stacks](/docs/deployments/concepts/review-stacks/) copy their template stack's settings, including the service principal, which is assigned Stack Write on each review stack automatically.

## Deployment roles

In organizations on the permissive [permission mode](/docs/administration/concepts/rbac/permission-modes/), you can instead limit automatic runs with a role:

- In editions with [custom roles](/docs/administration/concepts/rbac/roles/#custom-roles), pick any built-in or custom role under **Deployment role**. Custom roles are marked with a **Custom** badge.
- In other editions, pick **Admin**, **Write**, or **Read** under **Deployment permissions**.
- **Organization default** saves no role. Automatic runs then use the organization's default role.

A deployment role only limits automatic runs, such as those started by a git push or a schedule. A deployment started from the console or the REST API runs with the permissions of whoever starts it.

For a full explanation of how a deployment's permissions are determined, see [Permissions](/docs/deployments/operations/permissions/).

## Using the REST API

In the [deployment settings API](/docs/reference/cloud-rest-api/deployments/), the identity is `operationContext.servicePrincipal`. Set it to `{"userId": "<service principal login>"}` or `{"teamName": "<team name>"}`, or to `null` to clear it. A deployment's `runsAs` field reports the identity it ran as.
