---
title_tag: "How Pulumi ESC Works"
meta_desc: An overview of how Pulumi ESC works and discussion of core concepts.
title: How Pulumi ESC works
h1: How Pulumi ESC works
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    parent: esc-concepts
    identifier: how-pulumi-esc-works
    weight: 1
---

Pulumi ESC enables teams to aggregate secrets and configuration from many sources into a composable collection called an [environment](/docs/esc/concepts/). Teams can then consume those configuration and secrets from a variety of different infrastructure and application services.  Pulumi ESC works hand-in-hand with Pulumi IaC to simplify configuration management, and has a standalone CLI and API for other use cases apart from Pulumi IaC.

Pulumi ESC is offered as a fully managed cloud service in [Pulumi Cloud](/docs/pulumi-cloud/) (and Pulumi Cloud Self-hosted in the near future). The [pulumi/esc project](https://github.com/pulumi/esc) is open source, and contains the evaluation engine for environments, the esc CLI, and in the future, the extensible plugins for source and target integrations.

![Pulumi ESC ecosystem](/docs/esc/assets/pulumi_esc.png)

The following details corresponds to the numbered sections in the above diagram:

1. Pulumi ESC enables you to define environments, which contain collections of secrets and configuration. Each environment can be composed from multiple environments.

2. Pulumi ESC supports a variety of configuration and secrets sources, and it has an extensible plugin model that allows third-party sources.

3. Pulumi ESC has a rich API that allows for easy integration. Every value in an environment can be accessed from any target execution environment.

4. Every environment can be locked down with RBAC, versioned, and audited.

## Dynamic Secrets Providers

Support for dynamic configuration providers allow Pulumi ESC to [integrate with secrets stored in any other provider](/docs/esc/integrations/dynamic-secrets/).  Organizations often use AWS OIDC, AWS Secrets Manager, Vault, Azure OIDC, Azure KeyVault, GCP OIDC, and GCP Secrets Manager plus many more sources of truth for their secrets and configuration.  Pulumi ESC supports them all, providing a single interface to your configuration and secrets, no matter where their source of truth is.  Pulumi ESC works with these tools to provide improved management of secrets and configuration.

Teams can setup OIDC in their cloud providers to allow Environments to retrieve dynamic short-lived credentials. They can also pull secrets from other secrets managers and vaults.

These credentials can be used with [Pulumi IaC](/docs/pulumi-cloud/esc/environments/#using-with-pulumi-iac) with `pulumi up` as well as used to [run external CLIs](/docs/pulumi-cloud/esc/environments/#running-third-party-commands-using-pulumi-esc-secrets-and-config) like `aws`, `kubectl`, and more.

## Composable

Platform and service teams can centralize and control common configuration and secrets by creating environments that other teams can import. They can trace what other environments or stacks are using their configuration and assess the blast radius of any changes.

## Configuration as Code

Environments are defined as YAML documents which can describe how to project and compose secrets and configuration, integrate dynamic configuration providers, and compute new configuration from other values (constructing a URL from a DNS name, or concatenating multiple configuration values into a derived value).  The incredible flexibility of a code-based approach over traditional point-and-click interfaces allows Pulumi ESC to offer rich expressiveness for managing complex configuration.

## Authentication and RBAC

Pulumi ESC brokers access to secrets and configuration that live in other systems, and so authentication and granular RBAC are critical to ensure robust access controls across your organization. Pulumi ESC leverages the same Pulumi Cloud identity, RBAC, Teams, SAML/SCIM and scoped access tokens that are used for Pulumi IaC today, extending these all to managing access to environments as well as [Stacks](/docs/concepts/stack/).

Teams can create and control access to their environments. They can control who can update and preview environments, as well as who can open environments and retrieve their secrets. Audit logs let teams know who has changed or accessed configuration.

## Auditable

Environments must be “opened” to compute and see the set of value they provide, and this action is recorded in audit logs, including a full record of how each value was sourced from within the hierarchy of environments that contributed to it.

## Consume from Anywhere

The `esc` CLI and the Pulumi ESC Rest API enables environments to be accessed from any application, infrastructure provider, or automation system.  At launch, first-class integrations are available with Pulumi IaC, local environment and .env files, GitHub Actions, and more.
