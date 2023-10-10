---
title: Environments (ESC)
title_tag: Environments, Secrets, and Configuration (ESC) | Pulumi Concepts
h1: Pulumi ESC (Environments, Secrets, and Configuration)
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  concepts:
    weight: 8
search:
  boost: true
  keywords:
    - environments
    - secrets
    - configuration
---

Do you have secrets and configuration that is copy/pasted around multiple environments, that is prone to drift and accidental disclosure? Have you ever made a change to a config or secret and were unsure what the impact would be? Is it hard for developers in your organization to get access to short-lived credentials to work in the environments they need to develop and deploy into? Do you struggle to audit access levels and who has accessed or changed your secrets and configuration?

Pulumi ESC (Environments, Secrets, and Configuration) enables teams to create collections of configuration and secrets called Environments. Teams can then access those environment collections using the `esc` CLI, `pulumi` CLI, Pulumi SDK, or Pulumi Cloud REST API for various application and infrastructure needs. These environments can be composed of other environments to allow teams increased flexibility and fine-grained access control. Teams can have as many environments as they need.

Environments have built-in support for dynamic secret and config providers allowing for security and infrastructure best practices such as short-term credentials via OIDC and dynamically pulling secret values as need for all major cloud providers.

## Static Configuration

Simple environments might have static configuration, either as simple key/value pairs.  They can also contain interpolated values.

```yaml
values:
  name: world
  salutation: hello
  greeting: ${salutation}, ${name}
```

They can also contain complex [structured configuration](/docs/pulumi-cloud/esc/environments/#structured-configuration).

## Dynamic Secret Providers

Environments supports referencing secret and configuration providers, which allow you to pull in secrets from OIDC connect providers for short lived credentials or from vaults/secret managers for all the major cloud providers.

The team can manage access permissions to allow only select teams to have access to "open" and environment and retrieve secrets.

For more detail, see [Adding OIDC and Secrets providers](/docs/pulumi-cloud/esc/environments/#adding-oidc-and-secrets-providers).

Please see the [providers list](/docs/pulumi-cloud/esc/providers/) for a full list of currently supported providers.

## Removing Duplication

Environments contain collections of secrets and configuration, but can also import one or more other environments.  Values can be overridden, interpolated from other values, and arbitrarily nested.  This allows for flexible composition and reuse, and avoids copy paste.

## Organizing Environments

Environments can map to your organizational team or security boundaries, rather than just named deployment targets.

Imagine a hypothetical dev organization comprised of a few teams:

* The billing service team, that manages secrets/config for the payment processor
* The communications team, that manages secrets/config for the mailing service and texting service.
* The central platform team, that owns most common config, including OIDC config and the keys/config for the feature flag system.

Teams can manage permissions to these Environments to minimize security exposure.

Here is one way those teams might organize their environments:

![A diagram showing how the different environments with team based organization](../img/team_environments.png)
