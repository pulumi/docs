---
title: Concepts
title_tag: Pulumi ESC Concepts
h1: Pulumi ESC Concepts
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of
  configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-home
    identifier: esc-concepts
    weight: 3
aliases:
  - /docs/concepts/environments/
search:
  keywords:
    - concepts
    - compose
    - hierarchical
    - consume
    - collections
    - esc
    - various
---

Pulumi ESC (Environments, Secrets, and Configuration) simplifies how organizations manage secrets and configurations across multiple environments. It enables teams to compose collections of configuration and secrets called *environments*, which can be consumed by various infrastructure and application services. ESC helps ensure security, consistency, and efficiency in handling secrets and configuration.

Pulumi ESC is offered both as a fully managed cloud service in [Pulumi Cloud](/docs/pulumi-cloud/) and self-hosted for scenarios that require isolated environments. ESC has native integration with several products and other Pulumi products, including Pulumi Infrastructure as Code (IaC). The [pulumi/esc project](https://github.com/pulumi/esc) is open source, and contains the evaluation engine for environments, the `esc` CLI.

{{< figure src="/docs/esc/assets/pulumi_esc.png" caption="Figure: The Pulumi ESC ecosystem.">}}

The diagram above shows four key concepts:

1. ***Environments***: ESC environments are collections of secrets and configuration. Environments are composable from multiple environments and draw from both static and dynamic sources and can be shared to many targets.

2. ***Sources***: ESC can *input* configuration and secrets from a variety of sources, and it has an extensible plugin model for integrating third-party sources. ESC's built-in support for dynamic secret providers, allows for best-practices like generating short-term credentials via OIDC, and dynamically pulling secret values at the time of use, for all major cloud providers.

3. ***Targets***: ESC *outputs* configuration and secrets to a variety of popular targets. Pulumi ESC has a rich API that allows for easy integration, and provides standard output mechanisms like environment variables and key files.

4. ***Management***: ESC environments are centrally managed in Pulumi Cloud, and can be permissioned with RBAC, versioned, tagged, and audited. ESC secrets are encrypted in flight and at rest.

## The ESC Approach

Pulumi ESC takes a distinct approach to managing secrets and configuration that is different from other secret managers. ESC emphasizes flexibility and an open-ecosystem approach to integrations and is specifically designed for managing secrets and configurations across complex multi-cloud environments. Whether used in conjunction with [Pulumi IaC](/docs/iac/) or as a standalone tool, ESC helps streamline operations, reduce duplication, and enhance security for teams across a wide range of use cases.

### Centralized management, composability, and reusability

Pulumi ESC aggregates secrets and configuration from different sources into *environments*. These environments can be composed from other environments, allowing for flexible organization and reuse without duplication.

Pulumi ESC provides fine-grained **Role-Based Access Control (RBAC)**, ensuring that only authorized users and teams can access specific environments and retrieve secrets. Audit logs track who accessed or changed the configurations, enhancing security and accountability.

{{< figure src="team_environments.png" caption="Figure: Composable ESC environments facilitate team-based organization.">}}

Pulumi ESC environments can be structured to reflect an organization’s team structure, security boundaries, or deployment targets. The above diagram shows an example of how a customer might organize and compose different security environments.

Imagine a hypothetical development organization comprised of a few teams:

* The *billing service* team, that manages secrets/config for the payment processor
* The *communications* team, that manages secrets/config for the mailing service and texting service.
* The *central platform* team, that owns most common config, including OIDC config and the keys/config for the feature flag system.

Permissions to these environments can be defined separately to minimize security exposure. They can be reused indepedently or composed into more complex application scenarios.

### Dynamic vs static configurations

Pulumi ESC supports both **static** configurations (e.g. simple key-value pairs) and **dynamic** configurations (values retrieved from third-party providers) in the same environment. This allows teams to mix-and-match the type of configuration they need.

Pulumi ESC also supports **dynamic secret providers**, such as AWS OIDC, Azure KeyVault, GCP Secrets Manager, and more. This allows teams to pull short-lived credentials or other secrets dynamically from external sources.

More detail on dynamic secret providers is available in [Adding OIDC and secrets providers](/docs/esc/environments/working-with-environments/#using-secrets-providers-and-oidc). The [providers list](/docs/esc/integrations/) details the currently supported integrations.

### Configuration-as-Code, automation, and integration everywhere

Like our other products, Pulumi ESC uses an "as-code" approach to configuration and secrets. ESC environments can be composed, managed, and accessed using code written in TypeScript, JavaScript, Go, Python, or YAML. The `esc` CLI and our full-featured API allows for scripted use in automated environments like CI/CD. This reduces copy/paste style duplication of credentials and allows for management from a single source of truth. ESC is already deeply integrated into Pulumi IaC and Pulumi Cloud, and provides a number of third-party product integrations both as secrets providers and consumers.

## Learn More

* [How Pulumi ESC Works](/docs/esc/concepts/how-esc-works)
* The [ESC providers](/docs/esc/integrations/) list
* [Environments Overview](/docs/esc/environments/)
