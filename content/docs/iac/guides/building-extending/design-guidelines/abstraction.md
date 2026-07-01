---
title_tag: "Choosing the Right Abstraction | Pulumi Design Guidelines"
meta_desc: How to choose the right level of abstraction for a Pulumi component — high enough to add value, low enough to stay flexible — and when not to build one.
title: Choosing the Right Abstraction
h1: Choosing the Right Abstraction
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Choosing the right abstraction
        parent: iac-guides-design-guidelines
        weight: 10
---

The hardest decision in component design is how much to abstract. Set the level too low and the component is overhead that adds nothing; set it too high and it becomes a monolith nobody can adapt to their needs. Get it just right — the "Goldilocks" altitude — and the component captures something the consumer already thinks of as a single thing, makes the decisions an expert would make on their behalf, and leaves the rest in their hands.

It helps to picture a spectrum. At the bottom sits a raw resource — a single `aws.ec2.Vpc`, fully configurable and entirely your problem to wire up. At the top sits a finished, opinionated solution that makes nearly every decision for you. A good component lands in between, usually higher than its author first expects. The layers are worth naming: raw resources, curated defaults, and opinionated patterns. The same gradient runs through Pulumi components, from a bare provider resource to an [AWSX](/registry/packages/awsx/) abstraction to a full application platform built from many components.

## Add value, don't relabel

A component earns its place by encapsulating decisions: the wiring between resources, sensible defaults, security posture, and the invariants that keep a configuration correct. A consumer who uses the component inherits all of that for free.

{{% guideline type="do" %}}
**DO** build a component when it encapsulates a composition or a set of decisions that a consumer would otherwise have to get right themselves.
{{% /guideline %}}

A [`StaticPage` component](/docs/iac/guides/building-extending/components/build-a-component/) is a good example. Behind one input, it wires up a bucket, a website configuration, an index object, a public-access block, and a bucket policy — and it gets the policy and access settings right so the consumer doesn't expose their account by accident.

{{% guideline type="dont" %}}
**DON'T** wrap a single resource one-to-one with no added defaults, wiring, validation, or policy. A component that only forwards its arguments to one underlying resource is indirection without value — the consumer would be better off using the resource directly.
{{% /guideline %}}

A legitimate exception exists: a component that wraps a single resource but applies an opinionated, secure-by-default configuration — a hardened bucket, a database with backups and encryption switched on — is adding value, even though it manages one resource.

{{% guideline type="avoid" %}}
**AVOID** abstractions whose inputs are merely the union of the underlying resources' inputs. If a consumer has to understand every low-level setting to use your component, the abstraction isn't doing its job.
{{% /guideline %}}

## Model one concept

A component should represent one coherent concept that a consumer can name and reason about: a `Vpc`, a `StaticWebsite`, a `KubernetesCluster`. The name is a good test of whether the altitude is right.

{{% guideline type="consider" %}}
**CONSIDER** the name test: if you cannot give a component a clear, single-noun name, it is probably doing too much. `Vpc` is a concept; `NetworkingAndDatabaseAndMonitoring` is three.
{{% /guideline %}}

{{% guideline type="avoid" %}}
**AVOID** "god components" that bundle unrelated concerns behind dozens of flags. They are hard to learn, hard to evolve, and force a consumer to accept everything in order to get anything.
{{% /guideline %}}

A well-sized component asks for high-level inputs that match its altitude. A `Vpc` should take a CIDR block and a number of availability zones — not require the consumer to hand it fully formed subnet and route-table arguments.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
// High-level inputs that match the abstraction. The consumer says what they
// want; the component decides how to lay out subnets, route tables, and gateways.
const vpc = new Vpc("app", {
    cidrBlock: "10.0.0.0/16",
    numberOfAvailabilityZones: 3,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# High-level inputs that match the abstraction. The consumer says what they
# want; the component decides how to lay out subnets, route tables, and gateways.
vpc = Vpc("app", {
    "cidr_block": "10.0.0.0/16",
    "number_of_availability_zones": 3,
})
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// High-level inputs that match the abstraction. The consumer says what they
// want; the component decides how to lay out subnets, route tables, and gateways.
vpc, err := NewVpc(ctx, "app", &VpcArgs{
    CidrBlock:                 pulumi.String("10.0.0.0/16"),
    NumberOfAvailabilityZones: pulumi.Int(3),
})
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// High-level inputs that match the abstraction. The consumer says what they
// want; the component decides how to lay out subnets, route tables, and gateways.
var vpc = new Vpc("app", new VpcArgs {
    CidrBlock = "10.0.0.0/16",
    NumberOfAvailabilityZones = 3,
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// High-level inputs that match the abstraction. The consumer says what they
// want; the component decides how to lay out subnets, route tables, and gateways.
var vpc = new Vpc("app", VpcArgs.builder()
    .cidrBlock("10.0.0.0/16")
    .numberOfAvailabilityZones(3)
    .build());
```

{{% /choosable %}}

{{< /chooser >}}

Pulumi's own `awsx.ec2.Vpc` is built this way: you give it a CIDR block and a number of availability zones, and it lays out public and private subnets across those zones, choosing a NAT gateway strategy whose default balances cost against availability. The consumer states intent; the component supplies the expertise.

## Prefer composition to monoliths

When an abstraction grows large, factor it into smaller components and compose them, rather than adding modes and flags to one big component. A `Microservice` can compose a `Vpc`, a `Database`, and a `LoadBalancer`, each independently useful and independently testable.

{{% guideline type="do" %}}
**DO** factor large abstractions into smaller components that can be used on their own and combined. Composition keeps each piece focused and lets consumers adopt only what they need.
{{% /guideline %}}

{{% guideline type="consider" %}}
**CONSIDER** whether a flag you are about to add is really a second concept trying to escape. Two flags that are only ever set together, or never together, are often a sign that two components are hiding inside one.
{{% /guideline %}}

For more on building components out of components, see [Composition and resource structure](/docs/iac/guides/building-extending/design-guidelines/composition/).

## Don't strand the consumer

No abstraction anticipates every need. When a consumer hits something the component doesn't expose, they should be able to reach past it rather than abandon it.

Pulumi's [EKS](/registry/packages/eks/) component is a good model. Alongside the `kubeconfig` most consumers want, `eks.Cluster` exposes the underlying `eksCluster` resource, a ready-to-use Kubernetes `provider`, and its `core` building blocks, so a consumer who needs something the high-level API doesn't cover can drop down without leaving the component behind. These deliberate openings are escape hatches, and every abstraction that survives contact with real users grows them.

{{% guideline type="consider" %}}
**CONSIDER** exposing the underlying resources, or their key properties, as outputs so consumers can reference and extend them.
{{% /guideline %}}

{{% guideline type="consider" %}}
**CONSIDER** accepting optional pass-through configuration for the settings consumers most commonly need to customize, with good defaults when they're omitted.
{{% /guideline %}}

{{% guideline type="dont" %}}
**DON'T** make a component an all-or-nothing black box. A small escape hatch costs far less than forcing a consumer to rip out the component the first time it doesn't fit.
{{% /guideline %}}

This guidance sits in tension with the previous sections: every escape hatch you add lowers the altitude of the abstraction. Expose too much and the component becomes the same lowest-level soup it was meant to hide. Aim for an abstraction that handles the common case in full and offers a deliberate, documented path for the uncommon one.

## Anticipate future needs

The escape hatch handles needs you didn't foresee. Many needs, though, are foreseeable from the resource types a component creates, and designing for them up front is far cheaper than bolting them on after consumers have built workarounds.

Tags are the textbook case. If a component creates taggable cloud resources, someone will want to tag them for cost allocation, ownership, or compliance. And they will want *every* resource tagged, not only the ones the component happened to expose. A component that threads a `tags` input through to all of its children answers that need before it is asked; one that doesn't forces each consumer to reach around the component for something every one of them will eventually want.

{{% guideline type="do" %}}
**DO** accept the pervasive, cross-cutting inputs your resources invite, starting with `tags`, and propagate them to every child the component manages.
{{% /guideline %}}

{{% guideline type="consider" %}}
**CONSIDER** what each resource type predictably invites: taggable resources invite tags, named resources invite a naming prefix, encryptable resources invite a key. These needs are visible the day you choose the resources, long before anyone files an issue.
{{% /guideline %}}

Pulumi's own libraries learned this the hard way. Tag propagation across the resources a component creates was one of the most persistent requests against AWSX, asked for repeatedly and across many of its components over the years, and consumers who couldn't wait resorted to applying a stack [transformation](/docs/iac/concepts/resources/options/transforms/) that walked the tree and tagged everything by hand.

That workaround is also a warning. A transformation is a legitimate escape hatch: a consumer can apply one to a component to adjust resources its API doesn't surface. But when consumers *routinely* need a transformation to use your component — to tag its resources, set a common property, or correct a default — the recurring transformation is telling you that a predictable need belongs in the API as a first-class input.

{{% guideline type="dont" %}}
**DON'T** make routine customization depend on transformations. When the same transform shows up across many consumers, promote what it does into a real input and propagate it yourself.
{{% /guideline %}}

Anticipation has a limit, and it is the same one the rest of this chapter draws. Designing in inputs nobody asks for is the over-configurability trap from [Model one concept](#model-one-concept). Anticipate the needs that are both predictable and pervasive, the ones every consumer will hit, and leave the genuinely rare ones to the escape hatch.

## When not to build a component

Not every repetition deserves a component. Abstracting too early is as costly as abstracting too much.

{{% guideline type="avoid" %}}
**AVOID** distilling a component from a single example. An abstraction drawn from one use case tends to bake in that example's accidents and break the moment a second consumer arrives. Wait until you have seen the pattern two or three times.
{{% /guideline %}}

{{% guideline type="consider" %}}
**CONSIDER** whether a plain function, a [project template](/docs/iac/guides/building-extending/creating-templates/), or inline code is a better fit. Components shine for reusable, multi-instance, and especially multi-language abstractions; a one-off composition used in a single program may not need one.
{{% /guideline %}}

## See also

- [Composition and resource structure](/docs/iac/guides/building-extending/design-guidelines/composition/)
- [Designing inputs and outputs](/docs/iac/guides/building-extending/design-guidelines/inputs-and-outputs/)
- [Organizing Pulumi projects and stacks](/docs/iac/guides/basics/organizing-projects-stacks/)
- [Abstraction and encapsulation](/docs/tutorials/abstraction-encapsulation/)
