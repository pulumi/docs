---
title_tag: Cloud credentials for Pulumi Delivery
meta_desc: Give each stage of a Pulumi Delivery pipeline its own cloud credentials using Pulumi ESC environments with OIDC, or member environment variables.
title: Cloud credentials
h1: Cloud credentials for each stage
menu:
  delivery:
    name: Cloud credentials
    parent: delivery-guides
    weight: 10
aliases: []
---

Each `Stacks` update needs credentials for the cloud it deploys to, and you'll usually want different credentials for `dev` and `prod`. Delivery doesn't use a stack's [deployment settings](/docs/deployments/concepts/settings/) and doesn't do an OIDC exchange of its own, so the credentials come from the target stack or from the member.

## Use an ESC environment on the target stack

The recommended approach is to give each target stack an [ESC environment](/docs/esc/) that issues short-lived credentials through OIDC, such as one built on [`fn::open::aws-login`](/docs/esc/providers/login/aws-login/). Import the environment in the target stack's config file, for example `infra/Pulumi.dev.yaml`:

```yaml
environment:
  - aws-login/dev-sandbox
```

Because each stage updates different stacks, each stage gets its own credentials: `Pulumi.dev.yaml` imports the sandbox environment and `Pulumi.prod.yaml` imports the production one.

A `Stacks` update runs as the pipeline's [service principal](/docs/delivery/operations/permissions/#the-identity-a-pipeline-runs-as), which must be allowed to open the environment. If it isn't, the update fails with "you do not have permission to open environment".

<!-- TODO(launch): Confirm with DLV-434 that the service principal created at registration gets access to the target stacks' ESC environments, or only to the stacks. If only the stacks, say how to grant environment access. -->

## Pass credentials in `environment`

You can also pass credentials directly in a member's `environment`. A secret value stays secret:

```typescript
import * as pulumi from "@pulumi/pulumi";

const cfg = new pulumi.Config();

new delivery.Stacks("prod", {
    stage: prod,
    stacks: {
        app: {
            stack: "shop-infra/prod",
            source: repo,
            directory: "infra",
            environment: {
                AWS_ACCESS_KEY_ID: cfg.require("awsAccessKeyId"),
                AWS_SECRET_ACCESS_KEY: cfg.requireSecret("awsSecretAccessKey"),
            },
        },
    },
});
```

This keeps long-lived keys in the pipeline stack's config, so prefer the ESC approach where you can.

Don't put credentials in a `Stacks` entry's `config`. Values there are plain strings, and registration rejects a secret.

## Next steps

- Learn which [service principal a pipeline runs as](/docs/delivery/operations/permissions/#the-identity-a-pipeline-runs-as).
- Set up [OIDC for Pulumi ESC](/docs/esc/guides/configuring-oidc/).

<!-- TODO(launch): Consider a full AWS end-to-end example. -->
