---
title_tag: "Deployment Permissions | Pulumi Deployments"
meta_desc: Learn how to configure and manage permissions for Pulumi Deployments
title: "Deployment Permissions"
h1: "Deployment Permissions"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    parent: pulumi-cloud-deployments
    weight: 35
---

This page explains how permissions work in Pulumi Deployments and how to configure them for your deployment needs.

{{% notes type="info" %}}
This page contains information on the actions your Deployment is allowed to perform _within Pulumi Cloud_, like opening an ESC environment. To enable your Deployment to manage resources in your cloud, see [Supplying Cloud Credentials to Pulumi Deployments](../cloud-credentials/)
{{% /notes %}}

## Default Deployment Permissions

By default, the permissions that are granted to a deployment depend on how the deployment is being invoked:

- If the deployment is created via the **REST API** or by using the **Actions buttons** in the Pulumi Cloud console, it is granted the permissions of the user that has executed the action.
- If a deployment is created because of a **`git push`** or a **pull request**, it uses an ephemeral stack token that has admin permissions on only the stack itself, but nothing else.

## Permissions Impact

The permission model has the following practical implications:

- If your organization has default stack permissions set to `NONE`, then any deployment created by a `git push` or a pull request will not be able to access any [Stack References](https://www.pulumi.com/docs/concepts/stack/#stackreferences), and will fail if it tries to do so.

- If your organization has default environment permissions set to `NONE`, then any deployment created by a `git push` or a pull request will not be able to access any [ESC Environments](https://www.pulumi.com/docs/esc/environments/) that are listed in the stack's configuration file.

## Granting Additional Permissions

The recommended approach for granting additional permissions to deployments is through role assignment. To assign a role to a deployment, navigate to your stack's deployment settings in the Pulumi Console under `Settings > Deploy`. In the Role assignment section, use the dropdown menu to select from the available organization roles. Once a role is assigned, the deployment's stack token will inherit the permissions associated with that role, enabling access to stack references, environments, and organization resources as needed. Organization roles are managed through the [Roles section](../../access-management/rbac/roles/).

Alternatively, you can set the `PULUMI_ACCESS_TOKEN` environment variable to a token with the desired permissions in the stack's deployment settings.

This token can be an individual, team, or organization token, and it will grant the deployment the permissions that are associated with the token. If this environment variable is set, it will be used regardless of how the deployment was created (REST API, `git push`, etc.).

### Minimum Required Token Permissions

If using an individual or team token, the token must have at minimum:

- `WRITE` access to the stack that is being deployed
- `READ` access to any stacks from which Stack References are being used
- `OPEN` access to any ESC environment that is listed in the stack's configuration file, including any environments that are imported transitively

## Using ESC with Deployments

For enhanced security and simplified credential management, we recommend configuring your stack to use [Pulumi ESC](/docs/esc/) for cloud credentials and ensuring the Deployment has an appropriately scoped Pulumi token.

This approach offers several advantages:

- Dynamic, short-lived credentials instead of long-lived static credentials
- Fine-grained control over credential scope and permissions
- Centralized credential management
- Reduced risk of credential exposure
- Complete audit trail of credential usage

### Configuring ESC for Deployments

1. Create an ESC environment with the appropriate cloud provider credentials
2. Reference this environment in your Pulumi stack configuration
3. Create a Pulumi access token with the appropriate permissions (as described above)
4. Add this token as the `PULUMI_ACCESS_TOKEN` environment variable in your deployment settings

For more information on setting up ESC environments, see the [ESC documentation](/docs/esc/).

You can use ESC with pre-run commands in Deployments by prefixing each command with `pulumi env run`. For example:

```bash
pulumi env run my-aws-env -- aws s3 ls
```

This executes the `aws s3 ls` command with credentials from your `my-aws-env` ESC environment.
