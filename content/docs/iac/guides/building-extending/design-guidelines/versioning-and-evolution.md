---
title_tag: "Versioning and Evolution | Pulumi Design Guidelines"
meta_desc: Evolve a Pulumi component without breaking consumers — semantic versioning, breaking changes, defaults as contract, deprecation, and aliases.
title: Versioning and Evolution
h1: Versioning and Evolution
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Versioning and evolution
        parent: iac-guides-design-guidelines
        weight: 70
---

A component is never finished. You will add capabilities, fix bugs, and reshape its internals long after the first consumer adopts it — and every one of those changes lands in stacks you don't control. This chapter is about making a component evolve without forcing a flag day on everyone downstream: what a version number promises, which changes honor that promise and which break it, and the tools Pulumi gives you to refactor structure without churning live resources.

## The package is the unit of versioning

A component does not carry its own version. It ships inside a [package](/docs/iac/concepts/packages/), and the package's version is what consumers pin and upgrade. Bumping the package version versions every component in it at once, whether or not each one changed. That single fact drives how you group components: the version number is only meaningful if it tracks the evolution of the things it covers.

{{% guideline type="do" %}}
**DO** group components that evolve together into one package, so the version number actually describes what changed. Components that are used together and change together share a release cadence honestly.
{{% /guideline %}}

{{% guideline type="avoid" %}}
**AVOID** bundling unrelated components in one package. An unrelated component's breaking change drags everything else to a new major version, even the components that didn't change. Consumers then can't read the version to tell whether the component they depend on actually moved.
{{% /guideline %}}

The decision of what belongs in a package is the same cohesion judgment that governs [composition](/docs/iac/guides/building-extending/design-guidelines/composition/). [Repository strategy for Pulumi packages](/docs/iac/guides/building-extending/packages/repository-strategy/) covers the mechanics — one package per repository, and what "cohesive" looks like in practice.

## Use semantic versioning

Consumers pin a version and decide when to move. Semantic versioning is the contract that lets them decide safely: the shape of the version bump tells them whether an upgrade is routine or requires work. Semver applied to versioned, pinnable units in a registry is the model module ecosystems have converged on, and Pulumi packages follow it.

{{% guideline type="do" %}}
**DO** follow semantic versioning. Increment the major version for a breaking change, the minor version for a backward-compatible addition, and the patch version for a fix that changes no contract.
{{% /guideline %}}

A consumer who sees a minor or patch bump should be able to upgrade without reading a migration guide. A major bump is your signal that they cannot. Breaking that correspondence — slipping a breaking change into a minor release — is worse than the breaking change itself, because it defeats the one mechanism consumers have for protecting themselves.

## Know what's breaking

Whether a change breaks consumers comes down to two questions: does it change the component's surface — its inputs, outputs, and type — or does it change the resources a consumer already has in state? Either one is breaking.

Changes that break the surface:

1. Removing or renaming an input or output property.
1. Changing a property's type, including narrowing a union or tightening what values are accepted.
1. Making an optional input required, which breaks every consumer who omitted it.

Changes that break existing resources:

1. Changing a child resource's name suffix or its parent. Both alter the child's [URN](/docs/iac/concepts/resources/names/#urns), which Pulumi treats as a delete-and-replace of a live resource.
1. Changing a default in a way that alters the resources a consumer already deployed (see [Defaults are part of the contract](#defaults-are-part-of-the-contract)).

{{% guideline type="dont" %}}
**DON'T** rename or remove a public input, output, or type, change a property's type, or make an optional input required in anything but a major version. Each of these forces consumers to edit their programs before they can upgrade.
{{% /guideline %}}

By contrast, adding to the surface is safe. A new optional input with a sensible default leaves every existing program valid and every existing stack unchanged; a new output gives consumers something to reference without taking anything away.

{{% guideline type="do" %}}
**DO** prefer additive changes. A new optional input with a default and a new output are backward-compatible and ship in a minor version.
{{% /guideline %}}

Here is the additive case — a new `errorDocument` input that defaults to the existing behavior, so consumers who don't set it see no change:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
export interface StaticPageArgs {
    indexContent: pulumi.Input<string>;
    // Added in a minor release. Optional, with a default, so existing
    // programs compile unchanged and existing stacks see no diff.
    errorDocument?: pulumi.Input<string>;
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
class StaticPageArgs:
    index_content: pulumi.Input[str]
    # Added in a minor release. Optional, with a default, so existing
    # programs run unchanged and existing stacks see no diff.
    error_document: Optional[pulumi.Input[str]] = None
```

{{% /choosable %}}

{{% choosable language go %}}

```go
type StaticPageArgs struct {
    IndexContent pulumi.StringInput `pulumi:"indexContent"`
    // Added in a minor release. Optional, with a default, so existing
    // programs compile unchanged and existing stacks see no diff.
    ErrorDocument pulumi.StringPtrInput `pulumi:"errorDocument"`
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
public sealed class StaticPageArgs {
    public Input<string> IndexContent { get; set; } = null!;

    // Added in a minor release. Optional, with a default, so existing
    // programs compile unchanged and existing stacks see no diff.
    public Input<string>? ErrorDocument { get; set; }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
public final class StaticPageArgs {
    private Output<String> indexContent;

    // Added in a minor release. Optional, with a default, so existing
    // programs compile unchanged and existing stacks see no diff.
    private @Nullable Output<String> errorDocument;
}
```

{{% /choosable %}}

{{< /chooser >}}

## Defaults are part of the contract

A default is not a private implementation detail. It is the value thousands of consumers are implicitly relying on, and it is baked into the resources sitting in their stacks. Change it and the new value re-runs for everyone on upgrade.

{{% guideline type="dont" %}}
**DON'T** change a default value casually. A consumer who never set the input gets the new value on the next `pulumi up`, which can show up as an unexpected diff — or, if the property forces replacement, as a destroyed and recreated resource in production.
{{% /guideline %}}

The safe path is to make the new behavior reachable without changing what existing consumers get. Add a new optional input that defaults to the old behavior; consumers opt in when they're ready. Flip the default to the new behavior only in a major version, where consumers expect to do migration work.

{{% guideline type="consider" %}}
**CONSIDER** introducing new behavior behind a new optional input that defaults to the existing behavior, and changing the default only at a major version boundary. This turns a breaking change into an opt-in for everyone who wants it and a no-op for everyone who doesn't.
{{% /guideline %}}

## Deprecate before removing

When a public input, output, or whole component outlives its usefulness, retire it in two steps rather than one. Mark it deprecated and point to the replacement while keeping it working, then remove it only at the next major version. Consumers get a release where the old surface still functions and the warning tells them what to do.

{{% guideline type="do" %}}
**DO** deprecate a public input, output, or component before removing it: keep it working, mark it deprecated, and document the replacement. Remove it only in a major version.
{{% /guideline %}}

{{% guideline type="dont" %}}
**DON'T** delete a public surface without a deprecation period. A consumer's first encounter with the change should be a warning on a working program, not a compile error or a failed deployment.
{{% /guideline %}}

The [package schema](/docs/iac/guides/building-extending/packages/schema/) carries a `deprecationMessage` on resources, functions, and individual properties. Setting it surfaces the deprecation in the generated SDKs and docs for every language, so consumers see the warning and the suggested replacement in their own editor.

## Use aliases to refactor safely

Renaming a component or restructuring its children changes URNs, and Pulumi reads a changed URN as a different resource — delete the old, create the new. For a live database or a stateful volume, that is exactly the outcome you must avoid. [Aliases](/docs/iac/concepts/resources/options/aliases/) are the tool that lets the identity survive the refactor.

{{% guideline type="do" %}}
**DO** add an alias when you rename a component or move a child to a new name or parent, so Pulumi maps the old URN to the new one and updates the resource in place instead of replacing it.
{{% /guideline %}}

Aliases are inherited through the parent/child tree: aliasing a renamed component automatically re-maps its children, including the name prefix they derive from the component's name. Adding `aliases: [{ name: "${name}-storage" }]` to a child you renamed from `${name}-storage` to `${name}-bucket`, for instance, lets the existing bucket keep its identity through the rename.

{{% guideline type="consider" %}}
**CONSIDER** the alias temporary. Once every stack has rolled forward to the new identity, remove the alias from the component so the declaration stays clean.
{{% /guideline %}}

The structural mechanics of parent/child relationships and child naming live in [composition](/docs/iac/guides/building-extending/design-guidelines/composition/) and [naming](/docs/iac/guides/building-extending/design-guidelines/naming/). This chapter is about when to reach for an alias instead of accepting a replacement.

## Communicate changes

Consumers can't act on a change they don't know about. The version number tells them a breaking change exists; release notes tell them what it is and what to do.

{{% guideline type="do" %}}
**DO** ship release notes for every version and a migration note for every breaking change. State what changed, why, and the exact steps to upgrade — including any aliases consumers must add to their own programs.
{{% /guideline %}}

For [published packages](/docs/iac/guides/building-extending/packages/publishing-packages/), lean on the generated reference docs. Pulumi produces per-language documentation from the [package schema](/docs/iac/guides/building-extending/packages/schema/), so every consumer sees current inputs, outputs, and deprecation messages in their own language without you maintaining five copies by hand.

## Tighten the contract with policy

A component's contract often tightens over time — a value that used to be acceptable becomes one you want to forbid. Encoding every such rule as a required input or a narrower type is a breaking change, and a blunt one. Policy lets you enforce the constraint without changing the component's surface.

{{% guideline type="consider" %}}
**CONSIDER** validating inputs and usage with policy as the contract tightens, rather than making inputs required or narrowing types in a breaking way. Policy can enforce new constraints across consumers without forcing a major version on the component itself.
{{% /guideline %}}

See [Validating component inputs using policy functions](/docs/idp/guides/best-practices/patterns/validating-component-inputs-using-policy-functions/) for sharing one validation routine between a policy pack and the component constructor.

## See also

- [Repository strategy for Pulumi packages](/docs/iac/guides/building-extending/packages/repository-strategy/) — what belongs in a package, the unit of versioning
- [Resource option: aliases](/docs/iac/concepts/resources/options/aliases/) — preserving identity across renames and restructures
- [Composition and resource structure](/docs/iac/guides/building-extending/design-guidelines/composition/) — parent/child structure and child naming
- [Pulumi package schema](/docs/iac/guides/building-extending/packages/schema/) — deprecation messages and generated docs
