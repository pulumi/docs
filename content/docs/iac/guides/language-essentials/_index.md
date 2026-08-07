---
title_tag: "Language Essentials | Pulumi Guides"
meta_desc: Learn the small set of general-purpose programming constructs you need to write effective Pulumi IaC programs, mapped from YAML and HCL.
title: Language Essentials
h1: Language Essentials for Pulumi Programs
menu:
    iac:
        name: Language Essentials
        parent: iac-using-pulumi
        weight: 15
        identifier: iac-guides-language-essentials
---

This series is for engineers who are fluent in YAML, HCL, and cloud APIs, but who
haven't written much code in a general-purpose language. It translates the ideas
you already use every day, such as variables, conditionals, and modules, into the
handful of constructs that show up in a typical Pulumi program.

A Pulumi program's job is narrower than an application's. It declares the desired
state of your infrastructure. Pulumi runs it once per operation, evaluates the
resources it registers, and computes the diff against the last known state.
You're not building a long-running service; you're describing a graph of
resources, the same job you do today in a `.tf` file or a `Pulumi.yaml` file,
with a language that gives you more expressive tools when you need them.

Here's how the ideas map from configuration languages to a general-purpose one:

| What you write today | What it becomes in a general-purpose language |
| --- | --- |
| A `variables:` entry in Pulumi YAML, or a `locals` block in HCL | A variable |
| `${...}` interpolation | String interpolation, or an output helper |
| `count` or `for_each` | A loop |
| `count = var.enabled ? 1 : 0` | An `if` statement |
| A module | A function, or a class that groups resources into a component |
| The registry a module comes from | A package from npm, PyPI, Go modules, NuGet, or Maven |

## Pulumi YAML and HCL remain fully supported

Nothing here implies you should stop writing Pulumi YAML or Terraform HCL. Both
are complete, supported ways to define infrastructure, and for many teams and
many stacks, they're the right choice. The honest limit is this: neither
expresses a conditional or a loop natively. Pulumi YAML covers configuration,
resources, providers, outputs, and a set of built-in functions (see the
[YAML language reference](/docs/iac/languages-sdks/yaml/yaml-language-reference/)),
but the moment you need to create a resource only in production, or create one
resource per item in a list, you need a general-purpose language, or a
[component](/docs/iac/guides/building-extending/components/when-to-build-a-component/)
that someone already wrote in one. That's the point where this series pays for
itself.

If you're using [Pulumi Neo](/) while you're learning, it can draft and explain
program code for you, which is a reasonable way to see a construct in context
before you write it yourself.

## How to read this series

Each guide covers one construct: how you've already expressed the same idea in
YAML or HCL, the minimal syntax in each Pulumi language, a realistic
infrastructure example, and the Pulumi-specific details worth knowing before you
use it. Work through them in order, or jump to the one you need:

1. [Variables and values](/docs/iac/guides/language-essentials/variables/)
1. [Conditionals](/docs/iac/guides/language-essentials/conditionals/)
1. [Loops and iteration](/docs/iac/guides/language-essentials/loops/)
1. [Functions](/docs/iac/guides/language-essentials/functions/)
1. [Classes and components](/docs/iac/guides/language-essentials/classes/)
1. [Packages and dependencies](/docs/iac/guides/language-essentials/packages-and-dependencies/)

## Next steps

Start with [variables and values](/docs/iac/guides/language-essentials/variables/),
or see [Get started](/docs/iac/get-started/aws/) if you haven't installed Pulumi or
written your first program yet.

## Learn more

- [Languages & SDKs](/docs/iac/languages-sdks/) for per-language toolchain and
  runtime reference.
- [Inputs and outputs](/docs/iac/concepts/inputs-outputs/) for the async
  programming model that resource properties use.
