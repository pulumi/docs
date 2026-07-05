---
title_tag: "Composition and Resource Structure | Pulumi Design Guidelines"
meta_desc: How to structure a Pulumi component's child resources — parent/child relationships, propagating resource options, and composing components.
title: Composition and Resource Structure
h1: Composition and Resource Structure
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Composition and resource structure
        parent: iac-guides-design-guidelines
        weight: 40
---

A component is more than the inputs and outputs on its surface. Internally it is a tree of child resources, and the shape of that tree is part of the experience you ship. It shows up in `pulumi up` previews, in state, and in the resource graph a consumer reads when something goes wrong. This chapter is about getting that internal structure right: how children attach to the component, which resource options flow down to them, and how to compose components without making the tree incoherent.

## Parent every child

A [component](/docs/iac/concepts/components/) becomes the parent of the resources it creates by passing the [`parent`](/docs/iac/concepts/resources/options/parent/) option to each one. The parent/child relationship is what makes the children nest under the component in state, group beneath it in previews, and inherit the options described below. A child created without `parent` is loose: it lands at the top of the stack's resource tree as if the consumer had written it themselves, defeating the encapsulation the component exists to provide.

{{% guideline type="do" %}}
**DO** set `parent` to the component on every child resource the component creates.
{{% /guideline %}}

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
export class StaticPage extends pulumi.ComponentResource {
    constructor(name: string, args: StaticPageArgs, opts?: pulumi.ComponentResourceOptions) {
        super("sample-components:index:StaticPage", name, args, opts);

        // Each child names itself off `name` and parents to `this`.
        const bucket = new aws.s3.Bucket(`${name}-bucket`, {}, { parent: this });

        const website = new aws.s3.BucketWebsiteConfiguration(`${name}-website`, {
            bucket: bucket.bucket,
            indexDocument: { suffix: "index.html" },
        }, { parent: this });

        this.registerOutputs({});
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
class StaticPage(pulumi.ComponentResource):
    def __init__(self, name, args, opts=None):
        super().__init__("sample-components:index:StaticPage", name, {}, opts)

        # Each child names itself off `name` and parents to `self`.
        bucket = s3.Bucket(f"{name}-bucket", opts=ResourceOptions(parent=self))

        website = s3.BucketWebsiteConfiguration(f"{name}-website",
            bucket=bucket.bucket,
            index_document={"suffix": "index.html"},
            opts=ResourceOptions(parent=self))

        self.register_outputs({})
```

{{% /choosable %}}

{{% choosable language go %}}

```go
func NewStaticPage(ctx *pulumi.Context, name string, args *StaticPageArgs, opts ...pulumi.ResourceOption) (*StaticPage, error) {
    comp := &StaticPage{}
    if err := ctx.RegisterComponentResource("sample-components:index:StaticPage", name, comp, opts...); err != nil {
        return nil, err
    }

    // Each child names itself off `name` and parents to `comp`.
    bucket, err := s3.NewBucket(ctx, fmt.Sprintf("%s-bucket", name), &s3.BucketArgs{},
        pulumi.Parent(comp))
    if err != nil {
        return nil, err
    }

    _, err = s3.NewBucketWebsiteConfiguration(ctx, fmt.Sprintf("%s-website", name), &s3.BucketWebsiteConfigurationArgs{
        Bucket:        bucket.Bucket,
        IndexDocument: s3.BucketWebsiteConfigurationIndexDocumentArgs{Suffix: pulumi.String("index.html")},
    }, pulumi.Parent(comp))
    if err != nil {
        return nil, err
    }

    return comp, ctx.RegisterResourceOutputs(comp, pulumi.Map{})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
class StaticPage : ComponentResource {
    public StaticPage(string name, StaticPageArgs args, ComponentResourceOptions? opts = null)
        : base("sample-components:index:StaticPage", name, args, opts)
    {
        // Each child names itself off `name` and parents to `this`.
        var bucket = new Bucket($"{name}-bucket", new() { }, new() { Parent = this });

        var website = new BucketWebsiteConfiguration($"{name}-website", new() {
            Bucket = bucket.BucketName,
            IndexDocument = new BucketWebsiteConfigurationIndexDocumentArgs { Suffix = "index.html" },
        }, new() { Parent = this });

        this.RegisterOutputs(new Dictionary<string, object?>());
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
class StaticPage extends ComponentResource {
    public StaticPage(String name, StaticPageArgs args, ComponentResourceOptions opts) {
        super("sample-components:index:StaticPage", name, null, opts);

        // Each child names itself off `name` and parents to `this`.
        var bucket = new Bucket(String.format("%s-bucket", name), null,
            CustomResourceOptions.builder().parent(this).build());

        var website = new BucketWebsiteConfiguration(String.format("%s-website", name),
            BucketWebsiteConfigurationArgs.builder()
                .bucket(bucket.bucket())
                .indexDocument(BucketWebsiteConfigurationIndexDocumentArgs.builder()
                    .suffix("index.html")
                    .build())
                .build(),
            CustomResourceOptions.builder().parent(this).build());

        this.registerOutputs(Map.of());
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

For the full mechanics of creating children, see [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/#creating-child-resources).

## Register outputs at the end

The last thing a component's constructor should do is call `registerOutputs` with the values it exposes. Beyond recording the outputs in state, this call marks the component as fully constructed — the engine treats it as the signal that no more children are coming. Calling it once, at the end, keeps that contract clear.

{{% guideline type="do" %}}
**DO** call `registerOutputs` once, as the final statement of the constructor, passing the component's outputs.
{{% /guideline %}}

{{% guideline type="avoid" %}}
**AVOID** creating child resources after `registerOutputs`. Children registered past that point race against the completion signal and can be missed in the component's reported state.
{{% /guideline %}}

Deciding *which* values belong in your outputs — and how to type them — is the subject of [Designing inputs and outputs](/docs/iac/guides/building-extending/design-guidelines/inputs-and-outputs/). For the registration mechanics, see [Registering component outputs](/docs/iac/guides/building-extending/components/build-a-component/#registering-component-outputs).

## Propagate resource options to children

Because children declare the component as their `parent`, several [resource options](/docs/iac/concepts/resources/options/) the consumer sets on the component instance flow down to every child automatically — you don't re-apply them yourself. The engine carries the value down the parent/child chain at registration time. The [inherited-options reference](/docs/iac/concepts/resources/options/#options-inherited-from-a-component-to-its-children) lists exactly which options propagate; the ones component authors most need to keep in mind are below.

The most important is the provider. When a consumer points your component at a specific [`provider`](/docs/iac/concepts/resources/options/provider/) or [`providers`](/docs/iac/concepts/resources/options/providers/) — a particular AWS region, a named Kubernetes cluster, an account with specific credentials — that choice is inherited by the component's child custom resources. This is what lets one consumer deploy your `Vpc` into `us-east-1` and another into `eu-west-1` from the same component, without you threading a region input through by hand.

{{% guideline type="do" %}}
**DO** let children inherit the consumer's `provider`/`providers` by parenting them to the component, rather than constructing providers inside the component from your own inputs. The consumer owns where their infrastructure lands.
{{% /guideline %}}

[`protect`](/docs/iac/concepts/resources/options/protect/) and [`retainOnDelete`](/docs/iac/concepts/resources/options/retainOnDelete/) are also inherited. A consumer who protects your `Database` component protects every child under it as a unit, which is almost always what they intend — the whole abstraction is the thing they don't want deleted.

{{% guideline type="consider" %}}
**CONSIDER** the consequences of inherited `protect` and `retainOnDelete` when you decide what to make a child of the component. Anything parented to the component participates in the consumer's protection as a single unit.
{{% /guideline %}}

[`dependsOn`](/docs/iac/concepts/resources/options/dependson/) works the other way around. It isn't pushed down to children, but because the children sit under the component, a consumer who lists your component in another resource's `dependsOn` is depending on the entire subtree — the dependent resource waits for every child to finish. That is the right default, and it means a component composes cleanly into a consumer's ordering without exposing its internals.

For options Pulumi does *not* inherit — `ignoreChanges`, `customTimeouts`, and others a child may need — set them directly on the child as you create it, or use [`transforms`](/docs/iac/concepts/resources/options/transforms/) on the component to inject the option into matching child registrations. See [Passing resource options to components](/docs/iac/guides/building-extending/components/build-a-component/#passing-resource-options-to-components) for how options reach the constructor in the first place.

## Compose components from components

A child of a component can itself be a component. A `Microservice` may create a `Vpc`, a `Database`, and a `LoadBalancer` as its children, each a component with children of its own. Set `parent` on the nested components exactly as you would on a leaf resource, and the whole tree stays coherent: the consumer sees `Microservice` at the top, the three sub-components beneath it, and their cloud resources below those.

This is composition at work, and the reasoning is familiar: a flat tree of small, single-purpose components is easier to reason about and reuse than one deep monolith. The parent/child relationship is what makes that composition show up directly in the Pulumi resource graph rather than living only in your code.

{{% guideline type="do" %}}
**DO** compose larger components out of smaller ones, parenting each nested component so the resource tree mirrors the conceptual hierarchy.
{{% /guideline %}}

{{% guideline type="consider" %}}
**CONSIDER** keeping each composed component independently useful. A `Vpc` that only works inside your `Microservice` is a missed opportunity; one that stands on its own can be reused, tested, and reasoned about in isolation. This is the composition guidance from [Choosing the right abstraction](/docs/iac/guides/building-extending/design-guidelines/abstraction/), applied to the resource tree.
{{% /guideline %}}

For a worked treatment of this pattern in a platform context, see [Components using other components](/docs/idp/guides/best-practices/patterns/components-using-other-components/).

## Keep the resource tree meaningful

The tree a consumer sees in `pulumi up` and in state is documentation they read whether or not you intended it as such. A well-shaped tree makes the component's structure legible at a glance; a poorly shaped one buries the structure in noise.

{{% guideline type="avoid" %}}
**AVOID** a flat pile of dozens of children directly under the component when a couple of intermediate components would group them into recognizable units. If your `Cluster` creates thirty resources, grouping the networking and the node pools into sub-components turns a wall of resources into a structure a reader can scan.
{{% /guideline %}}

{{% guideline type="avoid" %}}
**AVOID** nesting for its own sake. A sub-component that wraps a single resource, or a layer that exists only to add a level to the tree, adds depth without adding meaning. Introduce an intermediate component when it names something the consumer would recognize — not to satisfy a symmetry instinct.
{{% /guideline %}}

The test is the consumer's mental model. The tree should mirror how someone reasons about the system, so that the structure they see in state matches the structure they already hold in their head.

## Restructure safely

A resource's identity is its [URN](/docs/iac/concepts/resources/names/), and the URN is built from the resource's name and its parent chain. Renaming a child or reparenting it — including the reparenting that happens when you factor children into a new sub-component — changes the URN, and Pulumi treats a changed URN as a different resource: it deletes the old one and creates a new one. Inside an unreleased component that's harmless. In a released component, it means an internal refactor can replace live infrastructure in every consumer's stack.

{{% guideline type="dont" %}}
**DON'T** rename or reparent the children of a released component without [`aliases`](/docs/iac/concepts/resources/options/aliases/). The alias tells Pulumi the new URN is the same resource as the old one, preserving its identity across the refactor.
{{% /guideline %}}

This is the resource-tree facet of a larger topic; the full rules for evolving a component without breaking consumers live in [Versioning and evolution](/docs/iac/guides/building-extending/design-guidelines/versioning-and-evolution/).

## See also

- [Component resources](/docs/iac/concepts/components/) — the underlying concept
- [Resource options inherited by children](/docs/iac/concepts/resources/options/#options-inherited-from-a-component-to-its-children) — exactly which options propagate
- [Designing inputs and outputs](/docs/iac/guides/building-extending/design-guidelines/inputs-and-outputs/) — what to expose and how to type it
- [Versioning and evolution](/docs/iac/guides/building-extending/design-guidelines/versioning-and-evolution/) — restructuring released components safely
