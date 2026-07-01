---
title_tag: "Pulumi Design Guidelines | Building & Extending"
meta_desc: Prescriptive guidelines for designing reusable Pulumi components — abstraction, naming, inputs and outputs, multi-language ergonomics, and evolution.
title: Pulumi Design Guidelines
h1: Pulumi Design Guidelines
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Design Guidelines
        parent: iac-guides-building-extending
        weight: 2
        identifier: iac-guides-design-guidelines
---

These guidelines describe how to design Pulumi [components](/docs/iac/concepts/components/) and [packages](/docs/iac/concepts/packages/) that other people will be glad to use. They are about judgment, not mechanics: how to choose the right level of abstraction, how to name things, what to accept as input and expose as output, and how to evolve a component without breaking the programs that depend on it.

A good component encapsulates hard-won expertise, so that everyone who consumes it inherits sound decisions for free: the author does the thinking once, and every consumer benefits. The guidance here is drawn from Pulumi's own component libraries — [AWSX](/registry/packages/awsx/), [Pulumi EKS](/registry/packages/eks/), and others — and from a generation of infrastructure tooling that grappled with the same problems.

## Who should read this

This guide is for anyone authoring abstractions that other people consume:

- **Platform teams** building the components and packages that application teams self-serve.
- **Package authors** publishing to the [Pulumi Registry](/registry) or a [private registry](/docs/idp/).
- **Anyone** factoring repeated infrastructure in their own programs into a reusable component.

It assumes you already know the mechanics of building a component. If you don't, start with [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/), then come back here to make it good. For distribution choices, see [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/).

## Why design matters

A component is an abstraction, and the value of an abstraction is measured by what it lets the consumer stop thinking about. A well-designed `Vpc` component lets a developer provision a sound, secure network without knowing how subnets, route tables, NAT gateways, and flow logs fit together. That is the entire point: the component author understands those details so the consumer doesn't have to.

Design decisions are also expensive to reverse. Once a component is published and adopted, its names, inputs, and outputs become a contract. Consumers write programs against that contract, and every stack they deploy depends on it. Renaming an input or changing a default is no longer a local edit — it is a breaking change that ripples out to every program and every stack. The cost of a careless decision is paid by everyone downstream, repeatedly, for as long as the component lives.

The consumer experience is the product. A component that does the right thing but is confusing to call, awkward to configure, or surprising in its output will be worked around rather than adopted. These guidelines exist to help you get the contract right the first time.

## How to read the guidelines

Each recommendation is tagged with one of four terms — a convention borrowed from the [.NET Framework Design Guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/) — that convey how strongly it applies.

{{% guideline type="do" %}}
**DO** guidelines should almost always be followed. Deviating requires a genuinely unusual reason.
{{% /guideline %}}

{{% guideline type="consider" %}}
**CONSIDER** guidelines should generally be followed, but the right call depends on context. Understand the guideline before deciding it doesn't apply to you.
{{% /guideline %}}

{{% guideline type="avoid" %}}
**AVOID** guidelines point to things that are usually a bad idea, though not always wrong.
{{% /guideline %}}

{{% guideline type="dont" %}}
**DON'T** guidelines should almost never be violated.
{{% /guideline %}}

Guidelines are recommendations, not rules a compiler enforces. The goal is a consistent, high-quality experience across the whole ecosystem of Pulumi components, so that consumers can move between components and find that they behave the way they expect.

## The guidelines

1. **[Choosing the right abstraction](/docs/iac/guides/building-extending/design-guidelines/abstraction/)** — finding the "Goldilocks" altitude: high enough to add value, low enough to stay flexible, and knowing when not to build a component at all.
1. **[Naming](/docs/iac/guides/building-extending/design-guidelines/naming/)** — type tokens, packages, properties, and child resources, with an eye toward a great experience in every language.
1. **[Designing inputs and outputs](/docs/iac/guides/building-extending/design-guidelines/inputs-and-outputs/)** — argument shape, required versus optional, sensible and secure defaults, secrets, validation, and what to expose.
1. **[Composition and resource structure](/docs/iac/guides/building-extending/design-guidelines/composition/)** — parent/child relationships, propagating resource options, and building components out of other components.
1. **[Single- versus multi-cloud abstractions](/docs/iac/guides/building-extending/design-guidelines/single-vs-multi-cloud/)** — when a cloud-agnostic abstraction earns its keep and when it becomes a leaky lowest common denominator.
1. **[Designing for multiple languages](/docs/iac/guides/building-extending/design-guidelines/designing-for-languages/)** — the type-system constraints of multi-language components and how to design for them from day one.
1. **[Versioning and evolution](/docs/iac/guides/building-extending/design-guidelines/versioning-and-evolution/)** — semantic versioning, breaking versus non-breaking changes, deprecation, and migrating consumers safely.

## See also

- [Component resources](/docs/iac/concepts/components/) — the underlying concept
- [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/) — the mechanics
- [Abstraction and encapsulation](/docs/tutorials/abstraction-encapsulation/) — a hands-on tutorial
- [Four factors of a platform](/docs/idp/guides/best-practices/four-factors/) — where components fit in platform engineering
