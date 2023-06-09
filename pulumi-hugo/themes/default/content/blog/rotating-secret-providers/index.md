---
title: "Rotating Secret Providers"
date: 2020-08-05
meta_desc: "Pulumi adds ability to rotate stack secret providers"
meta_image: secrets_rotation.png
authors:
    - paul-stack

tags:
    - features
    - Security
---

Customers and users have asked for the ability
to change the secrets manager associated with their stacks. This would allow a user to rotate
their secrets providers when people leave their organization or even to be able to migrate
to another secret manager of their choice. The [v2.8.0 release](https://github.com/pulumi/pulumi/releases/tag/v2.8.0)
of Pulumi adds support for this specific feature.

Let's have a look at how to change a secrets provider for an existing stack:

```bash
pulumi stack change-secrets-provider "awskms://alias/ChangeSecretsProvider?region=us-west-2"
```

This command will change the secrets provider *for the currently selected stack*. It will
ensure that the the configuration values in `Pulumi.<stack>.yaml` are re-encrypted
with the new secrets provider and that the latest checkpoint (state file)
also has any secrets held within are migrated with the new secrets provider.

{{< asciicast id="gApPSWG2lNxC4sWxdKIPkuXLc" >}}

## Creating New Stacks based on existing stacks

When creating a new stack, we added the ability to create that new stack based on the configuration of
an existing stack. This means that when you need to create a new developer stack or a new stack for a
different environment, then you can create that stack as follows:

```bash
pulumi stack init test --copy-config-from dev
```

This flag creates a new `test` stack and initiates the default secrets provider for the stack. It will then
get the existing configuration from the dev stack and re-encrypt it to the test stack's default secret provider.
We can, of course, pass a secrets provider to this new stack:

```bash
pulumi stack init test --secrets-provider="awskms://alias/ChangeSecretsProvider?region=us-west-2" --copy-config-from dev
```

{{< asciicast id="QZDHSYjXYUPDBLvALbZM776CX" >}}

## Copying Config Between Stacks

When working on a Pulumi project that has multiple stacks, there are times that we create a configuration
in one of the stacks that need to be copied to the other stacks in the project. Rather than selecting each
stack individually, we can now programmatically copy the configuration between stacks. Let's take an example where
a new database password was added to the dev stack. We can copy that password to the production stack as follows:

```bash
pulumi config cp MyDatabasePassword --dest production
```

This ensures that the `MyDatabasePassword` configuration will be re-encrypted into the production stack. If
there's a situation where we want to copy all of the configuration between the `dev` and `production` stacks,
then we omit the key (`MyDatabasePassword`):

```bash
pulumi config cp --dest production
```

We can iterate over all of the stacks that we need to copy the configuration to and the new configuration
values will be encrypted as per the new stack.

{{< asciicast id="VCc6J56RzOv2r08lP9veTE6Rr" >}}

## Learn More

If you’d like to learn about Pulumi and manage your infrastructure through code,
[get started today](https://www.pulumi.com/docs/quickstart/). Pulumi is open source and free to use.

As always, you can check out our code on [GitHub](https://github.com/pulumi), follow us
on [Twitter](https://twitter.com/pulumicorp), subscribe to our [YouTube channel](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw),
or join our [Community Slack](https://slack.pulumi.com/) channel if you have any questions,
need support, or just want to say hello.
