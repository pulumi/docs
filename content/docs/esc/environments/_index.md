---
title: Environments
title_tag: Pulumi ESC Environments
h1: Environments
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets called environments and consume them in various ways.
menu:
  pulumiesc:
    identifier: esc-environments
    weight: 3
---

Pulumi ESC (Environments, Secrets, and Configuration) lets you define collections of configuration settings and secrets called _environments_ and use them in any application or service. With Pulumi ESC, you can create environments, import configurations from a variety of sources, and manage secrets securely, ensuring your infrastructure is consistent and compliant.

Environments are YAML documents composed of static key-value pairs, programmatic expressions, dynamically retrieved values from supported providers including all major clouds through OpenID Connect (OIDC), and other Pulumi ESC environments.

Environments are accessible with the standalone [`esc` CLI](/docs/install/esc/), the [`pulumi` CLI](/docs/install/), the [Pulumi SDK](/docs/esc/languages-sdks/), and the [Pulumi Cloud console](/docs/esc/environments/working-with-environments#editing-an-environment-as-yaml-in-the-pulumi-cloud-console) and [REST API](/docs/pulumi-cloud/cloud-rest-api/#environments), and you can have as many environments as you need. Pulumi ESC is a service of Pulumi Cloud and is currently in public preview.

## Getting started with Pulumi ESC

Begin your journey with Pulumi ESC through a hands-on, self-paced [tutorial](/docs/esc/get-started/).
