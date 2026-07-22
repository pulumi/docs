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

A [component](/docs/iac/concepts/components/) groups related resources behind a single, well-defined interface. But in every language Pulumi supports for authoring, which is TypeScript, Python, Go, .NET, and Java, you can also create a group of resources by writing a plain function. So why write a component instead of just a function?

Both take about the same effort. In TypeScript, Python, .NET, and Java, a component is a class that subclasses a base `ComponentResource` type and creates its resources in the constructor. Go has no inheritance, so a component there is a struct that embeds `pulumi.ResourceState`, paired with a `NewX` constructor function that does the same work. In each case the base call, whether `super`, `base`, or `ctx.RegisterComponentResource`, **registers the grouping with Pulumi**. The engine records that these resources belong together and that the component owns them. A function creates the same resources without registering anything, so Pulumi holds no record of the grouping. The sections below cover what that record makes possible.

## A component can be packaged for other languages later

A component authored in one language can be [packaged as a plugin package](/docs/iac/guides/building-extending/components/packaging-components/#source-based-plugin-packages) and consumed from any Pulumi language, including YAML, or published to the [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/) for other teams to discover. Consumers construct it the same way regardless of its authoring language.

If a TypeScript component later turns out to be useful to a team writing Python, packaging becomes a build-and-publish task and the component source does not change. The same logic in a TypeScript function has to be rewritten in Python, or converted to a component first. Authoring it as a component leaves that path open without requiring you to decide up front.

## Resource options are inherited by child resources

Set a [resource option](/docs/iac/concepts/resources/options/) on a component and it applies to every resource the component creates:

```typescript
const network = new AcmeVpc("prod", {
    cidrBlock: "10.0.0.0/16",
}, {
    protect: true,
});
```

Every subnet, route table, and gateway inside `AcmeVpc` is now protected. The same inheritance applies to [`providers`](/docs/iac/concepts/resources/options/providers/), [`transforms`](/docs/iac/concepts/resources/options/transforms/), [`retainOnDelete`](/docs/iac/concepts/resources/options/retainondelete/), and [`deletedWith`](/docs/iac/concepts/resources/options/deletedwith/). Not every option is inherited, so check [Options inherited from a component to its children](/docs/iac/concepts/resources/options/#options-inherited-from-a-component-to-its-children) for the full list.

With a function, each option has to be passed to each resource explicitly. If someone later adds a resource and does not pass the option along, Pulumi reports no error and the resource is created without it. Inheritance from a component also covers resources added after the option was set.

Dependencies behave the same way. Because a component is a resource, `dependsOn: [myComponent]` expands to the resources the component transitively reaches, including those inside nested components, so a consumer can wait on the whole group without knowing its contents.

## Aliases are inherited when a component is refactored

A [URN](/docs/iac/concepts/resources/names/#urns) encodes the chain of parent types above a resource, so a component's children are named relative to the component rather than sitting directly under the stack. This keeps names from colliding when a program creates more than one instance of the same component.

Because the URN depends on that chain, renaming or re-typing a component changes the URNs of its children, and a changed URN means the resource is deleted and recreated rather than updated in place. [Aliases are inherited from a parent](/docs/iac/concepts/resources/options/aliases/), so a single alias on the component covers its children, through any number of levels:

```typescript
const site = new StaticWebsite("site", args, {
    aliases: [{ type: "acme:index:StaticSite" }],
});
```

Refactoring the equivalent function requires an alias on each resource it created, and any resource missed is deleted and recreated. See [Refactoring with aliases](/docs/iac/operations/stack-management/refactoring-with-aliases/) for the common workflows.

## The CLI treats the component as one resource

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

Because the component has its own URN, commands that accept a URN can refer to it directly, and the wildcard forms that [`pulumi up --target`](/docs/iac/cli/commands/pulumi_up/) accepts can select its children by URN prefix. Resources created by a function share no parent, so each one has to be named individually.

## When a function is the better choice

Components are for creating infrastructure. If your helper does not create resources, it should stay a function:

- **Computing values**: deriving a CIDR block, building a connection string, calculating a size from an environment name.
- **Naming and tagging**: assembling the standard tag map your organization stamps on every resource.
- **Assembling arguments**: building the argument object you then pass to a resource or component constructor.

A function is also reasonable for a small group of resources used exactly once, in one program, that will never need shared resource options, a dependency edge, or reuse elsewhere. Converting it to a component later requires a per-resource alias to avoid deleting and recreating each resource, so the cost of that conversion grows as the stack does.

## Next steps

- [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/) — write your first component.
- [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) — decide how to distribute it once you have one.
