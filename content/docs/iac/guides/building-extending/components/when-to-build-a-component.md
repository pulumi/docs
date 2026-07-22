---
title_tag: "When to Build a Component"
meta_desc: "Understand what a Pulumi component gives you that a plain function creating the same resources cannot, and when a function is the better choice."
title: When to Build a Component
h1: When to Build a Component
menu:
    iac:
        name: When to Build a Component
        parent: iac-guides-components
        weight: 5
---

A [component](/docs/iac/concepts/components/) groups related resources behind a single, well-defined interface. But a function can do that too: take some arguments, create five resources, return the useful outputs. Why write a component?

The call site isn't the answer. A constructor is a function, and `new Vpc("main", args)` and `createVpc("main", args)` cost about the same to write. The difference is that a component **registers the grouping with Pulumi**. The engine learns that these resources belong together and that this one owns them, and that registration buys you concrete things a function cannot offer.

## You keep the option to consume it from another language

A component authored in one language can be [packaged as a plugin package](/docs/iac/guides/building-extending/components/packaging-components/#source-based-plugin-packages) and consumed from any Pulumi language, including YAML, or published to the [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/) for other teams to discover. Consumers keep constructing it the same way they always did.

This matters most when you can't yet predict who needs the abstraction. A TypeScript component that turns out to be useful to a Python team is a packaging task. The same logic in a TypeScript function is a rewrite. Writing it as a component costs nothing extra up front and keeps the option open.

## Resource options apply consistently to everything inside

Set a [resource option](/docs/iac/concepts/resources/options/) on a component and it applies to every resource the component creates:

```typescript
const network = new AcmeVpc("prod", {
    cidrBlock: "10.0.0.0/16",
}, {
    protect: true,
});
```

Every subnet, route table, and gateway inside `AcmeVpc` is now protected. The same inheritance applies to [`providers`](/docs/iac/concepts/resources/options/providers/), [`transforms`](/docs/iac/concepts/resources/options/transforms/), [`retainOnDelete`](/docs/iac/concepts/resources/options/retainondelete/), and [`deletedWith`](/docs/iac/concepts/resources/options/deletedwith/). Not every option is inherited, so check [Options inherited from a component to its children](/docs/iac/concepts/resources/options/#options-inherited-from-a-component-to-its-children) for the full list.

A function has to thread each option through to each resource by hand. That works until someone adds a new resource and forgets to pass the option along, which produces no error, only an unprotected resource. With a component, the guarantee holds for resources that didn't exist when you wrote the option.

The same consistency applies to dependencies. Because a component is a resource, `dependsOn: [myComponent]` expands to the resources the component transitively reaches, including those inside nested components, so a consumer can wait on the whole group without knowing what's in it.

## Refactoring stays cheap as the component evolves

A [URN](/docs/iac/concepts/resources/names/#urns) encodes the chain of parent types above a resource, so a component's children are named relative to the component rather than sitting flat under the stack. Two instances of the same component don't collide, and the child names stay predictable as the program grows.

That parentage doesn't make a URN harder to change, but it does make the change cheap to absorb. [Aliases are inherited from a parent](/docs/iac/concepts/resources/options/aliases/), so renaming or re-typing a component carries its children along automatically, through any number of levels:

```typescript
const site = new StaticWebsite("site", args, {
    aliases: [{ type: "acme:index:StaticSite" }],
});
```

One alias on the component preserves the identity of every resource beneath it. Refactoring the equivalent function means writing an alias for each resource it created, and missing one replaces that resource. See [Refactoring with aliases](/docs/iac/operations/stack-management/refactoring-with-aliases/) for the common workflows.

## Operations treat it as one unit

A component appears as a single node in `pulumi preview` and `pulumi up`, with its children nested underneath:

```output
Updating (dev):
     Type                                Name          Status
 +   pulumi:pulumi:Stack                 website-dev   created
 +   └─ acme:index:StaticWebsite         site          created
 +      ├─ aws:s3:Bucket                 site-bucket   created
 +      ├─ aws:s3:BucketPolicy           site-policy   created
 +      └─ aws:cloudfront:Distribution   site-cdn      created
```

The grouping is operational, not cosmetic. The component's URN is addressable, so you can target the whole group with [`pulumi up --target`](/docs/iac/cli/commands/pulumi_up/). Resources created by a function have no shared parent to address.

## When a function is the right call

Components are for creating infrastructure. If your helper doesn't create resources, it should stay a function:

- **Computing values**: deriving a CIDR block, building a connection string, calculating a size from an environment name.
- **Naming and tagging**: assembling the standard tag map your organization stamps on every resource.
- **Assembling arguments**: building the argument object you then pass to a resource or component constructor.

A function is also reasonable for a small group of resources used exactly once, in one program, that will never need shared resource options, a dependency edge, or reuse elsewhere. Converting it to a component later means writing per-resource aliases to avoid replacement, so the cost of guessing wrong grows as the stack ages.

## Next steps

- [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/) — write your first component.
- [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) — decide how to distribute it once you have one.
