---
title_tag: "Pre-run Commands | Pulumi Deployments"
meta_desc: Run arbitrary shell commands before a Pulumi Deployment starts, for environment setup or authentication
title: "Pre-run Commands"
h1: "Pre-run Commands"
menu:
  deployments:
    name: Pre-run Commands
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-pre-run-commands
    weight: 50
---

Pre-run commands allow you to execute arbitrary shell commands before the deployment process starts. This is useful for environment setup, authentication with private package repositories, or other preparatory work. Note that each line of your pre-run command runs in a separate shell.

For example, you might use pre-run commands to:

- Install additional dependencies
- Configure authentication for private repositories
- Generate configuration files
- Set up environment variables - see [PULUMI_ENV](/docs/deployments/concepts/settings/environment-variables/#pulumi_env) if you need to persist these to your Pulumi program.

{{% notes type="info" %}}
Pulumi ESC environments that you reference in your Pulumi stack's configuration are not available when pre-run commands are executed, but you can use _any_ environment with pre-run commands by prefixing each command with `pulumi env run`. For example:

```bash
pulumi env run aws-creds/prod -- aws s3 ls
```

This executes the `aws s3 ls` command with credentials from your `aws-creds/prod` ESC environment. See the [Pulumi CLI documentation](/docs/iac/cli/commands/pulumi_env/) for more details.
{{% /notes %}}
