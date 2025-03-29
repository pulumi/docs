---
title: Environments
title_tag: Pulumi ESC Environments
h1: Environments
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of
  configuration and secrets called environments and consume them in various ways.
menu:
  esc:
    parent: esc-home
    identifier: esc-environments
    weight: 4
search:
  keywords:
    - Environments
    - Configuration
    - YAML documents
    - OpenID Connect
---

Pulumi ESC (Environments, Secrets, and Configuration) lets you define collections of configuration settings and secrets called _environments_ and use them in any application or service. Environments are YAML documents composed of static key-value pairs, programmatic expressions, dynamically retrieved values from supported providers including all major clouds through OpenID Connect (OIDC), and other Pulumi ESC environments.

Environments are accessible with the standalone [`esc` CLI](/docs/install/esc/), the [`pulumi` CLI](/docs/install/), the [Pulumi SDK](/docs/esc/development/languages-sdks/), and the [Pulumi Cloud console](#in-the-pulumi-cloud-console) and [REST API](/docs/pulumi-cloud/cloud-rest-api/#environments), and you can have as many environments as you need. Pulumi ESC is a service of Pulumi Cloud and is currently in public preview.

Environments are YAML documents composed of static key-value pairs, programmatic expressions, dynamically retrieved values from supported providers including all major clouds through OpenID Connect (OIDC), and other Pulumi ESC environments.

The following example shows a Pulumi ESC environment which dynamically pulls values from AWS OIDC and AWS Secrets Manager, as well as setting environment-specific configuration and overriding inherited configuration.

```yaml
# imports allow you to compose other pre-existing environments
imports:
  # AWS creds via OIDC
  - aws-production
  # stripe API keys imported from vault
  - stripe-production
  # keys for signing docker images via AWS Secrets Manager
  - docker-signing-production
values:
  # environment-specific configuration
  desiredInstanceCount: 8
  # overriding imports
  aws:region: us-west-2
```

## Getting started with Pulumi ESC

Begin your journey with Pulumi ESC through a hands-on, self-paced [tutorial](/docs/esc/get-started/).
