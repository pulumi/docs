---
title_tag: "Refactoring with aliases | Pulumi Operations"
meta_desc: Rename, re-parent, change the type, or move resources across stacks without destroying and recreating them, using the Pulumi aliases resource option.
title: Refactoring with aliases
h1: Refactoring with aliases
menu:
    iac:
        name: Refactoring with aliases
        parent: iac-operations-stack-management
        weight: 50
---

Pulumi identifies every resource by its [URN](/docs/iac/concepts/resources/names/#urns), which encodes the resource's name, type, parent path, project, and stack. When you change any of those — by renaming a resource, moving it under a new parent, wrapping a group of resources in a [`ComponentResource`](/docs/iac/concepts/components/), or migrating to a different provider type — the URN changes. By default Pulumi will treat the old URN as a delete and the new URN as a create, even though the underlying cloud resource is the same.

The [`aliases`](/docs/iac/concepts/resources/options/aliases/) resource option tells Pulumi "this old URN refers to the same resource as the new one." With it, you can restructure a program without forcing replacement on real infrastructure.

{{% notes type="info" %}}
This page focuses on the operational workflow — when to reach for an alias and how to remove it once the migration is complete. For the full property reference and every combination of fields on the `Alias` type, see the [`aliases` option reference](/docs/iac/concepts/resources/options/aliases/).
{{% /notes %}}

## When you need an alias

| You're changing | Use an alias entry like | Section |
| - | - | - |
| The logical name passed to the resource constructor | `{ name: "old-name" }` | [Renaming a resource](#renaming-a-resource) |
| The `parent` resource option | `{ parent: oldParent }` | [Re-parenting a resource](#re-parenting-a-resource) |
| A group of resources, by wrapping them in a new component | `{ parent: <root-stack> }` on each child | [Wrapping resources in a component](#wrapping-resources-in-a-component) |
| The resource's type token | `{ type: "old:Type" }` | [Changing a resource's type](#changing-a-resources-type) |
| The stack or project the resource belongs to | `{ stack: "old-stack", project: "old-project" }` | [Moving across stacks or projects](#moving-across-stacks-or-projects) |

You never need an alias when changing a property *inside* the resource's args (size, region, tags, and so on). Property changes are reconciled normally; only changes that affect the URN need an alias.

Before any of these refactors, run `pulumi preview` on each stack to confirm the alias prevents replacement. The preview should show the resource as `same` (or as an in-place update), not `delete` + `create`.

## Renaming a resource

Pass the old name in an alias entry. The first `pulumi up` after the change updates the stack state to use the new URN; no cloud resource is touched.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const db = new Database("primary-db", { /* ... */ }, {
    aliases: [{ name: "old-db" }],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database("primary-db",
    opts=ResourceOptions(aliases=[Alias(name="old-db")]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "primary-db", &DatabaseArgs{ /* ... */ },
    pulumi.Aliases([]pulumi.Alias{
        {Name: pulumi.String("old-db")},
    }))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("primary-db", new DatabaseArgs(),
    new CustomResourceOptions { Aliases = { new Alias { Name = "old-db" } } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var db = new Database("primary-db",
    DatabaseArgs.Empty,
    CustomResourceOptions.builder()
        .aliases(Alias.builder().name("old-db").build())
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  primary-db:
    type: pkg:index:Database
    options:
      aliases:
        - name: old-db
```

{{% /choosable %}}

{{< /chooser >}}

## Re-parenting a resource

When a resource moves under a new explicit parent, reference the old parent in the alias. Pulumi will recognize the resource by its previous URN and update the parent path in state.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const key = new ServiceAccountKey("primary-key", {
    serviceAccountId: newParent.email,
}, {
    parent: newParent,
    aliases: [{ parent: oldParent }],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
key = ServiceAccountKey("primary-key",
    service_account_id=new_parent.email,
    opts=ResourceOptions(
        parent=new_parent,
        aliases=[Alias(parent=old_parent)],
    ))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
key, err := NewServiceAccountKey(ctx, "primary-key", &ServiceAccountKeyArgs{
    ServiceAccountId: newParent.Email,
}, pulumi.Parent(newParent), pulumi.Aliases([]pulumi.Alias{
    {Parent: oldParent},
}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var key = new ServiceAccountKey("primary-key", new ServiceAccountKeyArgs
{
    ServiceAccountId = newParent.Email,
}, new CustomResourceOptions
{
    Parent = newParent,
    Aliases = { new Alias { Parent = oldParent } },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var key = new ServiceAccountKey("primary-key",
    ServiceAccountKeyArgs.builder()
        .serviceAccountId(newParent.email())
        .build(),
    CustomResourceOptions.builder()
        .parent(newParent)
        .aliases(Alias.builder().parent(oldParent).build())
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  primary-key:
    type: gcp:serviceAccount:Key
    properties:
      serviceAccountId: ${newParent.email}
    options:
      parent: ${newParent}
      aliases:
        - parent: ${oldParent}
```

{{% /choosable %}}

{{< /chooser >}}

Aliases are inherited from a parent, so if the parent itself is also being renamed or re-parented, you don't need to repeat that information on each child. See the [reference page](/docs/iac/concepts/resources/options/aliases/) for the inheritance rules.

## Wrapping resources in a component

A common refactor is to take a handful of related resources that were declared at the stack root and group them inside a new [`ComponentResource`](/docs/iac/concepts/components/). Each child needs an alias indicating it previously lived at the stack root (no explicit parent). The sentinel differs per SDK: TypeScript and Python have a named root-stack value, while Go, .NET, and Java use a `NoParent` flag with equivalent semantics.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

export class AppData extends pulumi.ComponentResource {
    constructor(name: string, args: AppDataArgs, opts?: pulumi.ComponentResourceOptions) {
        super("myorg:app:AppData", name, {}, opts);

        const db = new Database(`${name}-db`, {
            engine: args.engine,
        }, {
            parent: this,
            aliases: [{ parent: pulumi.rootStackResource }],
        });

        const cache = new Cache(`${name}-cache`, {
            sizeMb: args.cacheSizeMb,
        }, {
            parent: this,
            aliases: [{ parent: pulumi.rootStackResource }],
        });

        this.registerOutputs({});
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi

class AppData(pulumi.ComponentResource):
    def __init__(self, name, args, opts=None):
        super().__init__("myorg:app:AppData", name, {}, opts)

        db = Database(f"{name}-db",
            engine=args.engine,
            opts=pulumi.ResourceOptions(
                parent=self,
                aliases=[pulumi.Alias(parent=pulumi.ROOT_STACK_RESOURCE)],
            ))

        cache = Cache(f"{name}-cache",
            size_mb=args.cache_size_mb,
            opts=pulumi.ResourceOptions(
                parent=self,
                aliases=[pulumi.Alias(parent=pulumi.ROOT_STACK_RESOURCE)],
            ))

        self.register_outputs({})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
type AppData struct {
    pulumi.ResourceState
}

func NewAppData(ctx *pulumi.Context, name string, args *AppDataArgs, opts ...pulumi.ResourceOption) (*AppData, error) {
    component := &AppData{}
    if err := ctx.RegisterComponentResource("myorg:app:AppData", name, component, opts...); err != nil {
        return nil, err
    }

    _, err := NewDatabase(ctx, name+"-db", &DatabaseArgs{
        Engine: args.Engine,
    }, pulumi.Parent(component), pulumi.Aliases([]pulumi.Alias{
        {NoParent: pulumi.Bool(true)},
    }))
    if err != nil {
        return nil, err
    }

    _, err = NewCache(ctx, name+"-cache", &CacheArgs{
        SizeMb: args.CacheSizeMb,
    }, pulumi.Parent(component), pulumi.Aliases([]pulumi.Alias{
        {NoParent: pulumi.Bool(true)},
    }))
    if err != nil {
        return nil, err
    }

    return component, nil
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
public class AppData : ComponentResource
{
    public AppData(string name, AppDataArgs args, ComponentResourceOptions? opts = null)
        : base("myorg:app:AppData", name, opts)
    {
        var db = new Database($"{name}-db", new DatabaseArgs
        {
            Engine = args.Engine,
        }, new CustomResourceOptions
        {
            Parent = this,
            Aliases = { new Alias { NoParent = true } },
        });

        var cache = new Cache($"{name}-cache", new CacheArgs
        {
            SizeMb = args.CacheSizeMb,
        }, new CustomResourceOptions
        {
            Parent = this,
            Aliases = { new Alias { NoParent = true } },
        });

        RegisterOutputs();
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
public class AppData extends ComponentResource {
    public AppData(String name, AppDataArgs args, ComponentResourceOptions opts) {
        super("myorg:app:AppData", name, opts);

        var db = new Database(name + "-db",
            DatabaseArgs.builder().engine(args.engine()).build(),
            CustomResourceOptions.builder()
                .parent(this)
                .aliases(Alias.noParent())
                .build());

        var cache = new Cache(name + "-cache",
            CacheArgs.builder().sizeMb(args.cacheSizeMb()).build(),
            CustomResourceOptions.builder()
                .parent(this)
                .aliases(Alias.noParent())
                .build());

        this.registerOutputs();
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

In your program, replace the standalone `Database` and `Cache` declarations with a single `new AppData(...)` (or the language-equivalent constructor). After the next `pulumi up`, the resources move under the new component in state with no churn in the cloud.

{{% notes type="info" %}}
YAML programs don't define component resources directly. To group resources in YAML, factor the group into a [component package](/docs/iac/concepts/packages/) or move the program to one of the languages above.
{{% /notes %}}

## Changing a resource's type

When a provider deprecates a resource type or you migrate to a different provider entirely, the resource's type token changes. Add the old type in an alias entry:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const db = new aws.rds.Instance("primary-db", { /* ... */ }, {
    aliases: [{ type: "aws:rds/database:Database" }],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = aws.rds.Instance("primary-db",
    opts=ResourceOptions(aliases=[Alias(type_="aws:rds/database:Database")]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := rds.NewInstance(ctx, "primary-db", &rds.InstanceArgs{ /* ... */ },
    pulumi.Aliases([]pulumi.Alias{
        {Type: pulumi.String("aws:rds/database:Database")},
    }))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Aws.Rds.Instance("primary-db", new Aws.Rds.InstanceArgs(),
    new CustomResourceOptions { Aliases = { new Alias { Type = "aws:rds/database:Database" } } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var db = new Instance("primary-db",
    InstanceArgs.Empty,
    CustomResourceOptions.builder()
        .aliases(Alias.builder().type("aws:rds/database:Database").build())
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  primary-db:
    type: aws:rds:Instance
    options:
      aliases:
        - type: aws:rds/database:Database
```

{{% /choosable %}}

{{< /chooser >}}

A type-change alias only convinces Pulumi that the URN refers to the same resource. The new resource's schema must still be compatible with the cloud resource that exists — for example, the provider must use the same underlying API and accept the same identifiers. If the schemas are incompatible, use [`pulumi import`](/docs/iac/guides/migration/import/) instead.

## Moving across stacks or projects

When a resource moves to a new stack name or project name, supply the old identity:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const db = new Database("primary-db", { /* ... */ }, {
    aliases: [{ stack: "old-stack", project: "old-project" }],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database("primary-db",
    opts=ResourceOptions(aliases=[Alias(stack="old-stack", project="old-project")]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "primary-db", &DatabaseArgs{ /* ... */ },
    pulumi.Aliases([]pulumi.Alias{
        {Stack: pulumi.String("old-stack"), Project: pulumi.String("old-project")},
    }))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("primary-db", new DatabaseArgs(),
    new CustomResourceOptions { Aliases = { new Alias { Stack = "old-stack", Project = "old-project" } } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var db = new Database("primary-db",
    DatabaseArgs.Empty,
    CustomResourceOptions.builder()
        .aliases(Alias.builder().stack("old-stack").project("old-project").build())
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  primary-db:
    type: pkg:index:Database
    options:
      aliases:
        - stack: old-stack
          project: old-project
```

{{% /choosable %}}

{{< /chooser >}}

This alias form covers two common scenarios:

**Renaming a stack or project.** `pulumi stack rename` changes the stack's name and updates URNs in its state automatically; renaming a project means editing `name:` in `Pulumi.yaml`. A `stack` or `project` alias entry is still useful here when your program embeds the old identifier into a resource name — most commonly via `getStack()` — because the *resource's* URN changes even though the state-level rename already happened. The alias bridges that secondary change.

**Moving resources between stacks.** Use [`pulumi state move`](/docs/iac/cli/commands/pulumi_state_move/) to physically transfer resources from a source stack to a destination stack. The command rewrites the moved resources' URNs to use the destination's stack and project, so the move itself doesn't require an alias. Add a `stack` and/or `project` alias on those resources in the destination's program when the destination's code declares them with a different identity than the source did, or when you migrated state through some other path (export/import, manual edits) and the URNs weren't rewritten for you.

## Combining multiple alias entries

An `aliases` list can hold more than one entry, and the meaning of "list of entries" differs from "one entry with multiple fields":

- `aliases: [{ name: "old-name" }, { parent: oldParent }]` — two alternative identities. Pulumi matches the resource if its previous URN had either the old name *or* the old parent. Use this when a resource changed name in one update and parent in another, and you don't know which version of state the user is upgrading from.
- `aliases: [{ name: "old-name", parent: oldParent }]` — a single alias requiring *both* fields to match. Use this when the resource simultaneously had the old name and the old parent in the previous program.

When in doubt, prefer the list-of-objects form: it's broader, and Pulumi will pick whichever entry matches. False positives on alias matches are not a risk in practice — URNs are unique, so at most one entry can match a given resource.

## Removing aliases after migration

An alias is only load-bearing while at least one stack's state still references the old URN. Once every stack of the project has run `pulumi up` (or any operation that writes state, such as `pulumi refresh`) against the program with the alias in place, the new URN is recorded in state and the alias does nothing.

At that point you can delete the alias from the program:

1. List every stack of the project: `pulumi stack ls`.
1. For each stack, run `pulumi preview`. The resource should appear as `same` with no `aliases` warning in the output.
1. Remove the `aliases` entry from the program.
1. Run `pulumi preview` once more on each stack to confirm no replacement is planned.

Leaving stale aliases in the program isn't harmful, but they accumulate as code noise and obscure the intent of future refactors. Treat alias removal as a follow-up commit a few weeks after the original refactor lands, once you're confident every stack has rolled forward.

## See also

- [`aliases` resource option reference](/docs/iac/concepts/resources/options/aliases/) — full property surface and inheritance rules.
- [`parent` resource option](/docs/iac/concepts/resources/options/parent/) — the option whose value an alias most often references.
- [Resource names and URNs](/docs/iac/concepts/resources/names/#urns) — why URNs change when names, parents, types, stacks, or projects change.
- [Importing existing resources](/docs/iac/guides/migration/import/) — the alternative when aliases aren't enough (incompatible schemas, cross-stack moves).
- [Refactoring Pulumi code with `aliases`](/blog/cumundi-guest-post/) — a real-world walkthrough by Ringo De Smet of Cumundi that inspired this guide.
