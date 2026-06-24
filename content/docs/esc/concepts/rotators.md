---
title: Rotators
title_tag: Rotators | Pulumi ESC
h1: Rotators
meta_desc: Pulumi ESC rotators periodically replace stored credentials with freshly issued ones, automatically on a schedule or manually on demand.
aliases:
  - /docs/esc/environments/rotation/
  - /docs/esc/environments/syntax/rotators/
  - /docs/reference/esc-syntax/rotators/
  - /docs/esc/reference/rotators/
menu:
  esc:
    name: Rotators
    identifier: esc-concepts-rotators
    parent: esc-concepts
    weight: 4
---

Rotators are first-party Pulumi ESC plugins that enable the automated, periodic updating of sensitive credentials. By defining a schedule, you can specify when and how often a secret should be rotated, ensuring that long-lived credentials do not remain static over time. This is useful for maintaining best practices in security by reducing the risk of credential exposure or misuse.

ESC rotated secrets use a two-secret strategy in which two secrets are active and valid at any point in time. This is especially useful when multiple instances of an application share a credential but not all instances pull in the latest credential at the same time, allowing you to rotate a secret without worrying about some instances being unavailable due to invalid credentials.

## How rotators work

A rotator is invoked under `values:` using `fn::rotate::<name>`. Rotators are stateful: a rotator stores the credentials it has issued in the environment definition and replaces them on demand (manually via `pulumi env rotate` or on a schedule). Consumers open the environment to read the current credentials; rotation only happens when explicitly triggered. Rotators that act on an external service use a [login provider](/docs/esc/providers/login/) to authenticate the rotation call itself, with the most secure option being OpenID Connect (OIDC). See [OIDC setup](/docs/esc/guides/configuring-oidc/) for per-provider trust configuration.

Some rotators require you to deploy a [rotation connector](/docs/esc/operations/rotation/) in order to rotate credentials inside private networks.

## Available rotators

For the complete list of built-in rotators — including which require a rotation connector — see the [rotator reference](/docs/esc/providers/rotators/). If no built-in rotator fits, a custom adapter lets you plug in your own service.

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

Once a rotation function is configured within the environment definition, you can manually rotate your secrets by running the `pulumi env rotate` command, or by clicking the `Rotate secrets` button in the Pulumi Cloud UI.

#### Via the CLI

```bash
pulumi env rotate rotators/pulumi-ci
Environment 'rotators/pulumi-ci' rotated.
New revision '19' was created.
```

#### Via the Pulumi Cloud UI

In the Pulumi Cloud console, open the environment and click the **Rotate secrets** button on its **Rotated secrets** tab.

### Schedule

You can create a schedule for automatic rotation of your secrets in the Pulumi Cloud UI by navigating to the `Rotated secrets` tab of your environment, and clicking the `Create rotation schedule` button.

The rotation schedule can be defined as a [cron expression](https://crontab.cronhub.io/).

### Rotation connectors

Many organizations keep their databases in private networks, making it impossible for external credential managers (like ESC) to rotate the credentials.

Pulumi ESC's solution to that problem are rotation connectors - open-source, easy-to-deploy pieces of infrastructure that will securely rotate your credentials and store them in your ESC Environment for easy use.

See the [rotators](/docs/esc/providers/rotators/) page for details on which rotators require you to deploy a rotation connector.

Once you determined that you need one, follow the links below to learn how to set up and use each rotation connector.

| Rotation Connector                                                             | Description                                                                                                                     |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [AWS Lambda](/docs/esc/operations/rotation/aws-lambda/)                       | The `AWS Lambda` rotation connector enables you to rotate credentials inside private AWS VPCs.                                  |

## Permissions

- To `rotate` an environment, a user must have `WRITE` permissions on the environment, and `OPEN` permissions on any imported environment.
- To `open` an environment, a user must have `OPEN` permissions on the environment (and does not need any permissions for the implicitly imported environment which provides the rotation credentials).
- To configure a rotation schedule for an environment, the user must have `WRITE` permissions on the environment.

## Best practices

For operational guidance on organizing rotated environments and handling failures, see [Best practices](/docs/esc/operations/rotation/best-practices/).
