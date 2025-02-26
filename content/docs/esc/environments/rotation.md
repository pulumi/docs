---
title: Rotating secrets
title_tag: Rotating secrets | Pulumi ESC
h1: Rotating secrets
meta_desc: Pulumi ESC allows you to rotate secrets on a pre-defined schedule.
menu:
  esc:
    name: Rotating secrets
    identifier: esc-rotating-secrets
    parent: esc-environments
    weight: 4
---

Secret Rotation is a feature in Pulumi ESC that enables the automated periodic updating of sensitive credentials. By defining a schedule, you can specify when and how often a secret should be rotated, ensuring that any long-lived credentials do not remain static over time. This feature is useful for maintaining best practices in security by reducing the risk of credential exposure or misuse.

ESC Rotated secrets use a two-secret strategy in which two secrets are active and valid at any point in time. This is especially useful when multiple instances of an application share a credential but not all instances pull in the latest credential at the same time, allowing you to rotate a secret without worrying about some instances being unavailable due to invalid credentials.

## Usage

### Definition

Secret rotations are defined using a special function, `fn::rotate::`, which is evaluated by the Pulumi ESC runtime during a `rotation` action, which may be executed manually via the CLI or Pulumi Cloud UI, or automatically on a schedule.

```yaml
values:
  rotatedCredentials:
    fn::rotate::aws-iam:
      inputs:
        region: us-west-2
        login: ${environments.credentials.production.aws.login}
        userArn: arn:aws:iam::123456789012:user/username
      # If there are existing credentials, it's possible to specify them in the state - but this section is optional
      state:
        previous:
          accessKeyId: AKIA...
          secretAccessKey:
            fn::secret:
              ciphertext: ...
        current:
          accessKeyId: AKIA...
          secretAccessKey:
            fn::secret:
              ciphertext: ...
```

In the above example, note the `${environments.credentials.production.aws.login}` reference. This is an implicit import of the `credentials/production` environment's aws.login path.

This import is only resolved at `rotate` time, meaning that the value is not available during `open` time, making it possible for a user to access the rotated secret without needing access to the managing credentials.

### Rotation

Once a rotation function is configured within the environment definition, you can manually rotate your secrets by running the `esc env rotate` command, or by clicking the `Rotate secrets` button in the Pulumi Cloud UI.

#### Via the CLI

```bash
esc env rotate rotators/pulumi-ci
Environment 'rotators/pulumi-ci' rotated.
New revision '19' was created.
```

#### Via the Pulumi Cloud UI

![button.png](../button.png)

### Schedule

You can create a schedule for automatic rotation of your secrets in the Pulumi Cloud UI by navigating to the `Rotated secrets` tab of your environment, and clicking the `Create rotation schedule` button.

The rotation schedule can be defined as a [cron expression](https://crontab.cronhub.io/).

![schedule.png](../schedule.png)

## Permissions

- To `rotate` an environment, a user must have `WRITE` permissions on the environment, and `OPEN` permissions on any imported environment.
- To `open` an environment, a user must have `OPEN` permissions on the environment (and does not need any permissions for the implicitly imported environment which provides the rotation credentials).
- To configure a rotation schedule for an environment, the user must have `WRITE` permissions on the environment.

## Best practices

### Least privilege

It is recommended to follow the principle of least privilege when defining the permissions for the user or role that will be used to rotate the secret. The user or role should have only the necessary permissions to perform the rotation action, and no more.

The minimum required permissions for each rotation function are documented in the [Rotated Secret](/docs/esc/integrations/rotated-secrets) provider documentation.

### Separation of concerns

It is recommended that the login credentials required to perform the rotation action are stored in a separate environment, and imported via an [implicit import](/docs/esc/environments/imports#implicit-imports), as shown in the example above. This ensures that the credentials are not exposed to users who are unable to open the managing environment.

### Composition

It is a best practice to define a separate environment for your rotated functions, and import them into the environments that require the rotated credentials. This allows you to manage the rotation logic in a single place, and allows for the rotated environment to be versioned separately from the rest of your configuration. Specifically, since a new revision is created on every rotation, you may want to always import the latest version of the rotated environment to ensure that the latest rotated credentials are always used.

Another reason to keep your rotated functions in a separate environment is that an environment containing a rotation function *cannot be rolled back*, since the rotated secrets have been deactivated. By keeping your rotation functions separate, you can ensure that the rest of your configuration can be rolled back to a previous revision if needed.

### Organization

There are a few options for how you might organize your rotated environments.

You may want to organize your rotated environment by rotation schedule. Since a single environment can only have one rotation schedule, you can group your rotated environments by the frequency at which they need to be rotated. For example, you may have a `daily` environment, a `weekly` environment, and a `monthly` environment, each with their own rotation schedule.

Alternatively, you may want to keep a separate environment for each rotated secret. This avoids the potential for partial failures, described in more detail below.

### Handling partial failures

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
