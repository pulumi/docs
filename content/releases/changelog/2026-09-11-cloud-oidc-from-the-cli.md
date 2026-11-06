---
title: "Set up cloud OIDC from the Pulumi CLI"
date: 2026-09-11
meta_desc: The new pulumi env setup command configures OIDC trust for AWS, Azure, and Google Cloud and creates the ESC environments that use it.
authors:
    - christian-nunciato
---

You can now configure keyless cloud authentication without leaving your terminal. The new [`pulumi env setup`](/docs/iac/cli/commands/pulumi_env_setup/) command sets up OIDC trust for AWS, Azure, or Google Cloud and creates the [Pulumi ESC](/docs/esc/) environments that use it, so your stacks and deployments can pull short-lived cloud credentials instead of storing long-lived secrets.

```bash
pulumi env setup aws
```

The command prompts for anything you don't pass as flags, such as which policy to attach and which accounts or projects to cover, then prints everything it created when it's done.

To learn more, read the [announcement post](/blog/esc-oidc-setup-cli/) or the [`pulumi env setup` documentation](/docs/iac/cli/commands/pulumi_env_setup/).
