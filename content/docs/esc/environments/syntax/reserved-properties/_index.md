---
title: Reserved Properties
title_tag: Reserved Properties
h1: Reserved Properties
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/reserved-properties/
  - /docs/esc/reference/reserved-properties/
menu:
  esc:
    parent: reference-esc-syntax
    identifier: esc-syntax-reserved-properties
    weight: 7
---

The [`esc` CLI](/docs/install/esc/) and other ESC consumers (e.g. the [`pulumi` CLI](/docs/install/)) conventially assign specific semantics to certain top-level properties of evaluated ESC environments (i.e. properties defined under the [`values` section of the environment definition](/docs/esc/environments/syntax/top-level-keys/values)).

## ESC

- [`environmentVariables`](/docs/esc/environments/syntax/reserved-properties/environment-variables)
- [`files`](/docs/esc/environments/syntax/reserved-properties/files)

## Pulumi IaC

- [`pulumiConfig`](/docs/esc/environments/syntax/reserved-properties/pulumi-config)
