---
title: "Secret Rotation with Pulumi ESC"
date: 2024-12-10T15:43:02-08:00
draft: false
meta_desc: "Extending ESC to perform automated secret rotation."
meta_image: meta.png
authors:
  - claire-gaestel
tags:
  - esc
  - secrets
search:
  keywords:
    - esc
    - credential
    - rotation
    - secret
    - extending
    - perform
    - automated
---

{{% notes "info" %}}
Pulumi ESC now natively supports secrets rotation that makes secrets lifecycle management much easier. Check out the [launch blogpost](/blog/esc-rotated-secrets-launch/) and [docs](/docs/esc/environments/rotation).
{{% /notes %}}

Managing secrets in modern cloud applications can be challenging, particularly when it comes to rotation policies. While dynamic secrets (like AWS IAM temporary credentials) handle this automatically, many systems still rely on static secrets that require periodic rotation.

Static secrets, like database passwords or API keys, [should be rotated regularly to maintain security](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#272-rotation), and services depending on these secrets need time to transition to new credentials to avoid downtime. This makes rotating credentials error-prone, and often forgotten.

In this post, we'll explore an approach for automating static secret rotation using [Pulumi ESC](https://www.pulumi.com/docs/esc/) combined with [Pulumi IaC](https://www.pulumi.com/docs/iac/).

<!--more-->

## A pattern for extending ESC

We can take advantage of ESC’s integration with [Pulumi Deployments](https://www.pulumi.com/docs/pulumi-cloud/deployments/) to create an ergonomic way of managing rotation schedules ourselves.

We’ll start by defining a custom declarative configuration format for managing a rotation schedule:

```yaml
# we'll create our own "extended" fn config for ESC
xfn::pulumi-scheduled-update:
  # stack reference to a pulumi program that manages a rotated secret
  stack: "example-rotator-stack-reference/dev"
  # schedule that will drive an automatic scheduled deployment
  scheduleCron: "0 0 * * 0"
  # trigger a manual unscheduled rotation whenever this value changes
  trigger: "break-glass"
```

Using webhooks, we’ll monitor when the environment is updated, then search for these configuration blocks, and use them to drive scheduled deployments of a stack that rotates credentials. Using ESC’s composition primitives, we can combine this rotation schedule config with a `fn::open::pulumi-stacks` provider to read the current secret value from the rotator stack to provide to our application.

Here is how the solution fits together:
![Architecture](architecture.svg)
Let's break down each component and see how they work together to solve our rotation challenges.

### The Rotator: Managing Credential Lifecycles

At the heart of our solution is a [generic `Rotator` component](https://github.com/pulumi/esc-examples/blob/f8a0c47da556aebb74d3ac2d6491f897271bfa27/rotate/example/rotator/rotator.ts) that manages credential pairs. It's designed to handle any type of static secret while ensuring zero-downtime rotations. The way it does this is by maintaining two versions of each secret: “current” and “previous”.  Each time the stack is deployed, “current” is replaced with a newly provisioned credential, the old value is demoted to “previous”, and the old previous credential is decommissioned. Crucially, the demoted secret _remains valid_, which allows consuming services enough time to switch over to the new secret.

```typescript
const creds = new Rotator("rotating-creds", {
    // rotate credentials on every deployment.
    trigger: Date().toString(),
    // create a set of equivalent credentials that will be rotated between.
    // a particular credential should be replaced whenever `trigger` is updated.
    construct: (name, trigger) => {
        // in this example we're just creating passwords,
        // but these could be mysql users or anything else.
        return new random.RandomPassword(name, {
            length: 10,
            keepers: {trigger}
        })
    },
})

// export when the last rotation happened
export const lastUpdate = creds.lastUpdate.apply(date => date.toISOString());
// export the currently active credential, which will be imported by the downstream ESC environment.
export const current = creds.current.result;
```

### The Scheduler: Orchestrating Rotations

The [scheduler component](https://github.com/pulumi/esc-examples/blob/f8a0c47da556aebb74d3ac2d6491f897271bfa27/rotate/example/scheduler/index.ts) acts as an orchestrator, watching an ESC environment for updates and managing deployment schedules of the rotator stacks. Whenever a change to the environment is saved, a webhook invokes the scheduler, which parses the environment definition to find `xfn::pulumi-scheduled-update` configuration blocks. Based on these schedule configurations, it creates [scheduled deployments](https://www.pulumi.com/docs/pulumi-cloud/deployments/schedules/) for the referenced rotator stacks automatically.

### Bringing It Together: Environment Configuration

Once wired together, the magic happens in the ESC environment configuration, where we compose a rotation schedule with dynamic credential retrieval, creating a rotated credential that is automatically kept up to date:

```yaml
values:
  db-credentials:
    stack: database-credential-rotator/dev
    schedule:
      xfn::pulumi-scheduled-update:
        stack: ${db-credentials.stack}
        scheduleCron: "0 0 * * 0"  # weekly rotation
        trigger: "break-glass"     # manual trigger
    secrets:
      fn::open::pulumi-stacks:
        stacks:
          credentials:
            stack: ${db-credentials.stack}

  api-keys:
    stack: api-key-rotator/dev
    schedule:
      xfn::pulumi-scheduled-update:
        stack: ${api-keys.stack}
        scheduleCron: "0 0 1 * *"  # monthly rotation
    secrets:
      fn::open::pulumi-stacks:
        stacks:
          keys:
            stack: ${api-keys.stack}

  environmentVariables:
    DB_CONNECTION_STRING: ${db-credentials.secrets.credentials.current}
    API_KEY: ${api-keys.secrets.keys.current}
```

This configuration demonstrates how our custom extension is able to seamlessly integrate with ESC to manage multiple rotating secrets with different schedules declaratively, co-located with dynamic retrieval of the latest credentials from the rotator stack outputs. Applications consuming this environment will automatically receive the latest credentials without any additional configuration.

## Trying it out

Open the example environment and take note of the current secrets:

```
❯ pulumi env open esc-rotation-demo/test db-credentials.secrets
{
  "credentials": {
    "current": "OBA=wxS:VT",
    "lastUpdate": "2024-11-26T17:49:03.000Z",
    "previous": "MUgPXkJ+kE"
  }
}
```

Now lets force a rotation by changing the manual trigger:

```
❯ pulumi env set esc-rotation-demo/test \
    db-credentials.schedule.xfn::pulumi-scheduled-update.trigger \
    break-glass2
```

After a few minutes we can see that the secret has rotated successfully! We can also observe that the previous secret remains valid, giving currently deployed consumers time to update to the new credentials.

```
$ pulumi env open esc-rotation-demo/test db-credentials.secrets
{
  "credentials": {
    "current": "X2WSmF3+29",
    "lastUpdate": "2024-11-26T17:57:05.000Z",
    "previous": "OBA=wxS:VT"      <---- old "current" has been demoted
  }
}
```

## Conclusion

Secret rotation doesn't have to be a manual, error-prone process. By leveraging Pulumi ESC and this component architecture, we can automate and streamline the rotation of static secrets while maintaining system stability and security. The solution is flexible enough to handle various types of secrets while being simple to configure and maintain. This approach offers several advantages:

- Automated: Set-and-forget secret rotation
- Zero-downtime: Smooth transitions between credentials
- Flexible: Works with any type of static secret
- Declarative: Configuration through ESC environments
- Auditable: Clear tracking of rotation history
- Scalable: Easy to manage across multiple environments

[The complete example is available for your perusal here.](https://github.com/pulumi/esc-examples/tree/main/rotate/example)

This pattern of extending ESC through configuration-driven components is a powerful technique that can be applied to other use cases. We’re excited to see what else you come up with 🙂
