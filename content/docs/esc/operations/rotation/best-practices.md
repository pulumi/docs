---
title: Best practices
title_tag: Pulumi ESC rotation best practices
h1: Best practices
meta_desc: Best practices for rotating secrets with Pulumi ESC — least privilege, separation of concerns, composing rotated environments, and handling partial failures.
menu:
  esc:
    identifier: esc-operations-rotation-best-practices
    parent: esc-operations-rotation
    weight: 1
---

Recommendations for rotating secrets safely and reliably with Pulumi ESC. For conceptual background on what rotators are and how the `fn::rotate::*` syntax works, see [Rotators](/docs/esc/concepts/rotators/).

## Least privilege

It is recommended to follow the principle of least privilege when defining the permissions for the user or role that will be used to rotate the secret. The user or role should have only the necessary permissions to perform the rotation action, and no more.

The minimum required permissions for each rotation function are documented in the [rotator reference](/docs/esc/providers/rotators/).

## Separation of concerns

It is recommended that the login credentials required to perform the rotation action are stored in a separate environment, and imported via an [implicit import](/docs/esc/concepts/imports/#implicit-imports). This ensures that the credentials are not exposed to users who are unable to open the managing environment.

## Composition

It is a best practice to define a separate environment for your rotated functions, and import them into the environments that require the rotated credentials. This allows you to manage the rotation logic in a single place, and allows for the rotated environment to be versioned separately from the rest of your configuration. Specifically, since a new revision is created on every rotation, you may want to always import the latest version of the rotated environment to ensure that the latest rotated credentials are always used.

Another reason to keep your rotated functions in a separate environment is that an environment containing a rotation function *cannot be rolled back*, since the rotated secrets have been deactivated. By keeping your rotation functions separate, you can ensure that the rest of your configuration can be rolled back to a previous revision if needed.

## Organization

There are a few options for how you might organize your rotated environments.

You may want to organize your rotated environment by rotation schedule. Since a single environment can only have one rotation schedule, you can group your rotated environments by the frequency at which they need to be rotated. For example, you may have a `daily` environment, a `weekly` environment, and a `monthly` environment, each with their own rotation schedule.

Alternatively, you may want to keep a separate environment for each rotated secret. This avoids the potential for partial failures, described in more detail below.

## Handling partial failures

If multiple rotation functions are defined in a single environment, it is possible that some fail while others succeed. In these cases, a partial failure will be reported.

To handle partial failures, failed keys can be individually retried using the `esc env rotate [envName] [path(s)-to-rotate]` command. This will allow you to retry the rotation of a specific key without affecting the rotation of other keys in the environment.

```bash
esc env rotate rotators/pulumi-ci credentials.bot.aws
Environment 'rotators/pulumi-ci' rotated.
New revision '23' was created.
```

{{% notes type="warning" %}}
**WARNING** Beware of double rotation in the case of partial failures. If a key is rotated twice, the first rotation will be invalidated and the second rotation will be active. This can lead to unexpected behavior if not handled correctly, for example if the rotated secret has not been updated at the consumer.
{{% /notes %}}
