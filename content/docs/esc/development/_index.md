---
title: Development
title_tag: Develop infrastructure solutions with Pulumi ESC
h1: Develop with Pulumi ESC
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of
  configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-home
    identifier: esc-development
    weight: 8
search:
  keywords:
    - development
    - esc
    - hierarchical
    - compose
    - consume
    - secrets
    - collections
---

The [Pulumi ESC SDK](/docs/esc/development/languages-sdks/) provides a programmatic interface to manage environments, secrets, and configuration directly within your applications. Using the SDK, you can create, update, and delete environments, apply version tags. It also simplifies the secure handling of secrets and configurations, allowing you to retrieve sensitive data like cloud credentials, connection strings, and feature flags at runtime without long-term storage.

[Pulumi Service Provider](/docs/esc/development/psp/) provides the ability to create ESC resources like environments, environment permissions, and environment version tags using a Pulumi program. Combined with other Pulumi Service resources like Stacks, this makes setting up a development platform a breeze!

[Pulumi Automation API](/docs/esc/development/automation-api/) allows interaction with Pulumi ESC environments in your deployment workflow. This enables you to seamlessly manage stack configuration and secrets, allowing more complex automation logic.
