---
title: Environment Definition Syntax
title_tag: Environment Definition Syntax
h1: Environment Definition Syntax
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-environments
    identifier: esc-syntax
    weight: 2
aliases:
  - /docs/reference/esc-syntax/
  - /docs/esc/syntax-reference
  - /docs/esc/reference/
  - /docs/esc/environments/structure/
---

This is a reference for the syntactical constructs defined by ESC.

## Reference summary

The syntax reference is divided into the following sections:

- __Top-level keys__: These are the different top-level document keys defined by the ESC language. Each key has its own well-defined semantics. For more information, see the [top-level key reference](/docs/esc/environments/syntax/top-level-keys).
- __Interpolations and references__: Interpolations and references are additional syntactical constructs ESC layers on top of YAML to enable users to reuse property values. For more information, see the [interpolation and references syntax reference](/docs/esc/environments/syntax/interpolations-and-references).
- __Built-in functions__: These are the different built-in functions defined by the ESC language. These functions allow you to perform common tasks such as encoding and decoding values and manipulating strings. For more information, see the [built-in functions reference](/docs/esc/environments/syntax/builtin-functions).
- __Built-in properties__: These are the different predefined properties available to [interpolations and references](/docs/esc/environments/syntax/interpolations-and-references). For more information, see the [built-in properties reference](/docs/esc/environments/syntax/builtin-properties).
- __Providers__: These are the different providers that allow dynamic access to credentials, configuration, and secrets stored outside of ESC. Each provider has its own set of inputs that affect its behavior. For more information, see the [providers reference](/docs/esc/environments/syntax/providers).
- __Rotators__: These are the different rotators that allow ESC to rotate credentials, configuration, and secrets stored outside of ESC. Each rotator has its own set of inputs that affect its behavior. For more information, see the [rotators reference](/docs/esc/environments/syntax/rotators).
- __Reserved properties__: These are the different environment properties that are interpreted by the [`esc` CLI](/docs/install/esc/) and other ESC consumers (e.g. the [`pulumi` CLI](/docs/install/)). The semantics of these properties are defined by conventions amongst consumers of ESC environments. For more information, see the [reserved property reference](/docs/esc/environments/syntax/reserved-properties).
- __Sample environment definition__: This is a sample environment definition that demonstrates many of the constructs described in the other reference sections. For more information, see the [sample environment definition reference](/docs/esc/environments/syntax/sample-environment-definition).

Each ESC environment is a YAML document that defines the structure and values produced when the environment is evaluated (also referred to as _opened_). For more information see the [high-level Environments documentation](/docs/esc/environments).
