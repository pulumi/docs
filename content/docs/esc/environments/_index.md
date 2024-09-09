---
title: Environments
title_tag: Pulumi ESC Environments
h1: Environments | Pulumi ESC
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets called environments and consume them in various ways.
menu:
  pulumiesc:
    identifier: esc-environments
    weight: 3
---

Pulumi ESC (Environments, Secrets, and Configuration) lets you define collections of configuration settings and secrets called _environments_ and use them in any application or service. With Pulumi ESC, you can create environments, import configurations from a variety of sources, and manage secrets securely, ensuring your infrastructure is consistent and compliant.

Environments are YAML documents composed of static key-value pairs, programmatic expressions, dynamically retrieved values from supported providers including all major clouds through OpenID Connect (OIDC), and other Pulumi ESC environments.

Environments are accessible with the standalone [`esc` CLI](/docs/install/esc/), the [`pulumi` CLI](/docs/install/), the [Pulumi SDK](/docs/esc/languages-sdks/), and the [Pulumi Cloud console](/docs/esc/environments/working-with-environments#editing-an-environment-as-yaml-in-the-pulumi-cloud-console) and [REST API](/docs/pulumi-cloud/cloud-rest-api/#environments), and you can have as many environments as you need. Pulumi ESC is a service of Pulumi Cloud and is currently in public preview.

## Key features

Explore the following sections to learn more about the key features and benefits of Pulumi ESC:

- [Working with environments](/docs/esc/environments/working-with-environments)
- [Importing other environments](/docs/esc/environments/imports)
- [Versioning](/docs/esc/environments/versioning)
- [Dynamic environment variables](/docs/esc/environments/dynamic-environment-variables)
- [Access control](/docs/esc/environments/access-control)

## Getting started with Pulumi ESC

Begin your journey with Pulumi ESC through a hands-on, self-paced [tutorial](/docs/esc/get-started/).
