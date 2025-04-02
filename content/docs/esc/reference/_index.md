---
title: Environment Reference
title_tag: Environment Reference
h1: ESC Environment Reference
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-home
    identifier: esc-reference
    weight: 5
aliases:
  - /docs/esc/syntax-reference
---

This is a reference for the various properties and constructs defined by ESC.

## Reference summary

The ESC Environment reference is divided into the following sections:

- __Top-level properties__: These are the different top-level document properties defined by the ESC language. Each property has its own well-defined semantics. For more information, see the [top-level property reference](/docs/esc/reference/top-level-properties).
- __Value references__: Value references are an additional syntactical construct ESC layers on top of YAML to enable users to reference and interpolate values. For more information, see the [value references syntax reference](/docs/esc/reference/value-references).
- __Built-in functions__: These are the different built-in functions defined by the ESC language. These functions allow you to perform common tasks such as encoding and decoding values and manipulating strings. For more information, see the [built-in functions reference](/docs/esc/reference/builtin-functions).
- __Built-in values__: These are the different predefined values available to symbols and interpolations. For more information, see the [built-in values reference](/docs/esc/reference/builtin-values).
- __Providers__: These are the different providers that allow dynamic access to credentials, configuration, and secrets stored outside of ESC. Each provider has its own set of inputs that affect its behavior. For more information, see the [providers reference](/docs/esc/reference/providers).
- __Rotators__: These are the different rotators that allow ESC to rotate credentials, configuration, and secrets stored outside of ESC. Each rotator has its own set of inputs that affect its behavior. For more information, see the [rotators reference](/docs/esc/reference/rotators).
- __Well-known properties__: These are the different environment properties that are interpreted by the [`esc` CLI](/docs/install/esc/) and other ESC consumers (e.g. the [`pulumi` CLI](/docs/install/)). The semantics of these properties are defined by conventions amongst consumers of ESC environments. For more information, see the [well-known property reference](/docs/esc/reference/well-known-properties).
- __Sample environment definition__: This is a sample environment definition that demonstrates many of the constructs described in the other reference sections. For more information, see the [sample environment definition reference](/docs/esc/reference/sample-environment-definition).

Each ESC environment is a YAML document that defines the structure and values produced when the environment is evaluated (also referred to as _opened_). For more information see the [high-level Environments documentation](/docs/esc/environments).
