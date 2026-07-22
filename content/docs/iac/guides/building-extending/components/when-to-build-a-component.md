---
title_tag: "When to Build a Component"
meta_desc: "Understand when to encapsulate resources in a Pulumi component instead of a plain function, and what a component gives you that a function cannot."
title: When to Build a Component
h1: When to Build a Component
menu:
    iac:
        name: When to Build a Component
        parent: iac-guides-components
        weight: 5
---

A [component](/docs/iac/concepts/components/) groups related resources behind a single, well-defined interface. But a plain function can also create a group of resources and return them, which raises a fair question: why write a component at all?

The answer comes down to one difference. A component is a resource: it gets its own node in your [stack's](/docs/iac/concepts/stacks/) state, with a [URN](/docs/iac/concepts/resources/names/#urns) and a parent-child relationship to everything it creates. A function is code that runs. The resources it creates land in your stack as loose, unrelated children, and the grouping exists only in your head. Everything below follows from that.

## Resource options propagate to children

Set a [resource option](/docs/iac/concepts/resources/options/) on a component and it applies to every resource the component creates:

```typescript
const network = new AcmeVpc("prod", {
    cidrBlock: "10.0.0.0/16",
}, {
    protect: true,
});
```

Every subnet, route table, and gateway inside `AcmeVpc` is now protected. The same holds for [`providers`](/docs/iac/concepts/resources/options/providers/), [`transforms`](/docs/iac/concepts/resources/options/transforms/), [`retainOnDelete`](/docs/iac/concepts/resources/options/retainondelete/), and [`deletedWith`](/docs/iac/concepts/resources/options/deletedwith/). Not every option is inherited — see [Options inherited from a component to its children](/docs/iac/concepts/resources/options/#options-inherited-from-a-component-to-its-children) for the full list.

With a function, you have to thread each option through to each resource by hand. That works until someone adds a new resource to the function and forgets to pass the option along, a mistake that produces no error, only an unprotected resource.

## Other resources can depend on the whole group

Because a component is a resource, other resources can depend on it directly:

```typescript
const cluster = new AcmeCluster("prod", {
    nodeCount: 3,
});

const app = new k8s.apps.v1.Deployment("app", {
    /* ... */
}, {
    dependsOn: [cluster],
});
```

Pulumi expands the component into the resources it transitively reaches, including those inside nested components, so the deployment waits for every one of them. A function returns a bag of resources, so callers have to know which ones matter and list them individually, then update that list whenever the function's internals change.

## The component appears as one node

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

That grouping is real, not cosmetic. The component's URN means you can target it with [`pulumi up --target`](/docs/iac/cli/commands/pulumi_up/), and you can restructure its internals later without replacing resources by adding an [alias](/docs/iac/concepts/resources/options/aliases/). Resources created by a function have no shared parent to target or alias.

## Components match the declarative style of your program

Pulumi programs are declarative: you describe the infrastructure you want and Pulumi works out how to get there. `new VirtualMachine("web", { size: "large" })` matches the shape of every other resource declaration in the file. `createVirtualMachine("web", "large")` is an imperative call that looks like an exception to the pattern.

This is more than style. When every abstraction in your codebase is declared the same way, readers don't have to work out which helpers create infrastructure and which merely compute values.

## A component can graduate to a shared package

A component that starts as a class in a single program can later be published as a [native language package](/docs/iac/guides/building-extending/components/packaging-components/#native-language-packages), packaged as a [plugin package](/docs/iac/guides/building-extending/components/packaging-components/#source-based-plugin-packages) consumable from any Pulumi language, or listed in the [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/). Consumers keep calling it exactly the same way.

A function has no such path. Making it available to another language or another team means rewriting it as a component first.

## When a function is the right call

Components are for creating infrastructure. If your helper doesn't create resources, it should stay a function:

- **Computing values**: deriving a CIDR block, building a connection string, calculating a size from an environment name.
- **Naming and tagging**: assembling the standard tag map your organization stamps on every resource.
- **Assembling arguments**: building the argument object you then pass to a resource or component constructor.

A function is also reasonable for a small group of resources used exactly once, in one program, that you're confident will never need shared resource options, a dependency edge, or reuse elsewhere. Be aware that converting it to a component later means replacing resources unless you add aliases, so the cost of guessing wrong grows over time.

## Next steps

- [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/) — write your first component.
- [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) — decide how to distribute it once you have one.
