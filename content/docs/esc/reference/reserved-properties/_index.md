---
title: Reserved Properties
title_tag: Reserved Properties
h1: Reserved Properties
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-reference
    identifier: esc-ref-reserved-properties
    weight: 7
---

The [`esc` CLI](/docs/install/esc/) and other ESC consumers (e.g. the [`pulumi` CLI](/docs/install/)) conventially assign specific semantics to certain top-level properties of evaluated ESC environments (i.e. properties defined under the [`values` section of the environment definition](/docs/esc/reference/top-level-keys/values)).

## ESC

- [`environmentVariables`](/docs/esc/reference/reserved-properties/environment-variables)
- [`files`](/docs/esc/reference/reserved-properties/files)

## Pulumi IaC

- [`pulumiConfig`](/docs/esc/reference/reserved-properties/pulumi-config)
