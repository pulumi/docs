---
title: Reserved Properties
title_tag: Reserved Properties
h1: Reserved Properties
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/esc/reference/reserved-properties/
menu:
  reference:
    parent: reference-esc-syntax
    identifier: esc-ref-reserved-properties
    weight: 7
---

The [`esc` CLI](/docs/install/esc/) and other ESC consumers (e.g. the [`pulumi` CLI](/docs/install/)) conventially assign specific semantics to certain top-level properties of evaluated ESC environments (i.e. properties defined under the [`values` section of the environment definition](/docs/reference/esc-syntax/top-level-keys/values)).

## ESC

- [`environmentVariables`](/docs/reference/esc-syntax/reserved-properties/environment-variables)
- [`files`](/docs/reference/esc-syntax/reserved-properties/files)

## Pulumi IaC

- [`pulumiConfig`](/docs/reference/esc-syntax/reserved-properties/pulumi-config)
