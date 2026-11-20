---
title_tag: "Deployment Permissions | Pulumi Deployments"
meta_desc: Learn how to configure and manage permissions for Pulumi Deployments
title: "Deployment Permissions"
h1: "Deployment Permissions"
aliases:
- /docs/deployments/deployments/permissions/
- /docs/pulumi-cloud/deployments/permissions/
- /docs/deployments/guides/gated-deployments/
menu:
  deployments:
    name: Permissions
    parent: deployments-operations
    identifier: deployments-operations-permissions
    weight: 10
---

This page explains how permissions work in Pulumi Deployments and how to configure them for your deployment needs.

{{% notes type="info" %}}
This page mostly covers the actions your Deployment is allowed to perform _within Pulumi Cloud_, like opening an ESC environment. For the GitHub credential that deployments from a GitHub-connected source receive, see [Version control credentials](#version-control-credentials). To enable your Deployment to manage resources in your cloud, see [Supplying Cloud Credentials to Pulumi Deployments](/docs/deployments/guides/cloud-credentials/)
{{% /notes %}}

## How a deployment's permissions are determined

Who a deployment runs as depends on the stack's [**Run as**](/docs/deployments/concepts/settings/pulumi-cloud-role/) setting and on your organization's [permission mode](/docs/administration/concepts/rbac/permission-modes/):

- **A service principal or a team is selected.** Every deployment runs as that [service principal](/docs/administration/concepts/rbac/service-principals/), or as the team's service principal, with exactly its permissions. It doesn't matter who or what starts the deployment.
- **Nothing is selected, in a permissive organization.** The permissions depend on how the deployment starts:
    - If the deployment is created via the **REST API** or by using the **Actions buttons** in the Pulumi Cloud console, it is granted the permissions of the user that has executed the action.
    - If a deployment is created because of a **`git push`**, a **pull request**, or a **schedule**, it runs as the organization's background runner, limited to the stack's deployment role if one is set, and otherwise to the organization's default role.
- **Nothing is selected, in a restricted organization.** The deployment is refused. Every stack must select a service principal or a team.
- **In the Free edition**, deployments always run as the organization's single member.

The deployment's page shows the result, for example **Runs as service principal deploy-prod** or **Runs as the person who triggered it**.

## Version control credentials

The Pulumi Cloud identity a deployment runs as is not the only credential it receives. When a deployment's source is connected through the [Pulumi GitHub app](/docs/integrations/version-control/github-app/), Pulumi also injects a `GITHUB_TOKEN` environment variable. This token is a GitHub App installation token with the installation's full scope, not a token limited to the source repository. It can reach every repository you granted the app and holds every permission the app holds, including write access to repository contents and workflows. Treat it as a broadly privileged credential. For the list of permissions and details on the token's lifetime, see [GitHub token in deployments](/docs/integrations/version-control/github-app/#github-token-in-deployments).

To give a deployment a narrower GitHub credential, set your own `GITHUB_TOKEN` in the stack's [environment variables](/docs/deployments/concepts/settings/environment-variables/), for example a fine-grained personal access token limited to the repositories the deployment needs. A value you set always overrides the one Pulumi provides. If you configure the source with your own personal access token, Pulumi uses that token as `GITHUB_TOKEN` instead.

## Granting additional permissions

The recommended way to control what a deployment can access is to run it as a [service principal](/docs/administration/concepts/rbac/service-principals/):

1. Create a service principal, with no organization-wide role if the deployment only needs a few stacks and environments.
1. Give it Stack Write on the stack, Stack Read on any stacks whose stack references the program reads, and Environment Open on any environments the stack uses, including environments imported transitively. Grant these on each stack's and environment's [access settings](/docs/administration/concepts/rbac/entities/#entity-access), or through a role.
1. On the stack's **Settings** → **Deploy** page, select it under [**Run as**](/docs/deployments/concepts/settings/pulumi-cloud-role/), then select **Save**.

To manage organization resources such as teams, members, or OIDC issuers from a deployment, give the service principal a role that includes those permissions.

In permissive organizations, two older options remain:

- **A deployment role.** Choose a role under **Run as** to limit automatic runs to that role's permissions. Deployment roles are being deprecated, so prefer a service principal or a team.
- **A `PULUMI_ACCESS_TOKEN` environment variable** in the stack's deployment settings, set to an individual, team, or organization token. The deployment gets the permissions associated with the token, regardless of how it was created (REST API, `git push`, etc.). This can't be combined with a service principal or a team, and isn't available in restricted organizations.

### Minimum required token permissions

If using an individual or team token, the token must have at minimum:

- `WRITE` access to the stack that is being deployed
- `READ` access to any stacks from which Stack References are being used
- `OPEN` access to any ESC environment that is listed in the stack's configuration file, including any environments that are imported transitively

## Using ESC with Deployments

For enhanced security and simplified credential management, we recommend configuring your stack to use [Pulumi ESC](/docs/esc/) for cloud credentials and ensuring the Deployment runs as an appropriately scoped service principal.

This approach offers several advantages:

- Dynamic, short-lived credentials instead of long-lived static credentials
- Fine-grained control over credential scope and permissions
- Centralized credential management
- Reduced risk of credential exposure
- Complete audit trail of credential usage

### Configuring ESC for Deployments

1. Create an ESC environment with the appropriate cloud provider credentials
1. Reference this environment in your Pulumi stack configuration
1. Give the [service principal](/docs/administration/concepts/rbac/service-principals/) the stack's deployments run as Environment Open on the environment, as described in [Granting additional permissions](#granting-additional-permissions)

For more information on setting up ESC environments, see the [ESC documentation](/docs/esc/).

You can use ESC with pre-run commands in Deployments by prefixing each command with `pulumi env run`. For example:

```bash
pulumi env run my-aws-env -- aws s3 ls
```

This executes the `aws s3 ls` command with credentials from your `my-aws-env` ESC environment.
