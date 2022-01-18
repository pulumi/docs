---
title: "Aliases"
meta_desc: The alises resource option an be used to refactor resources.
menu:
  intro:
    parent: options
    weight: 2
aliases:
  - /docs/intro/concepts/resources/#aliases
---

The `aliases` resource option provides a list of aliases for a resource or component resource. If you’re changing the name, type, or parent path of a resource or component resource, you can add the old name to the list of aliases for a resource to ensure that existing resources will be migrated to the new name instead of being deleted and replaced with the new named resource.

Aliases are frequently used when refactoring Pulumi programs.

For example, imagine we change a database resource’s name from `old-name-for-db` to `new-name-for-db`. By default, when we run `pulumi up`, we see that the old resource is deleted and the new one created. If we annotate that resource with the aliases option, however, the resource is updated in-place:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [{ name: "old-name-for-db" }] });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [{ name: "old-name-for-db" }] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('db',
    opts=ResourceOptions(aliases=[Alias(name='old-name-for-db')]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.Aliases(pulumi.Alias{Name: pulumi.String("old-name-for-db")}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("new-name-for-db", new DatabaseArgs(),
    new CustomResourceOptions { Aliases = { new Alias { Name = "old-name-for-db"} } });
```

{{% /choosable %}}

{{< /chooser >}}

The aliases option accepts a list of old identifiers. If a resource has been renamed multiple times, it can have many aliases. The list of aliases may contain old `Alias` objects and/or old resource URNs.

The above example used objects of type `Alias` with the old resource names. These values may specify any combination of the old name, type, parent, stack, and/or project values. Alternatively, you can just specify the URN directly:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [ "urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db" ] });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [ "urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db" ] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('db',
    opts=ResourceOptions(aliases=['urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db']))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.Aliases([]pulumi.Alias{pulumi.Alias{
        URN: pulumi.URN("urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db"),
    }})
)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("new-name-for-db", new DatabaseArgs(),
    new CustomResourceOptions { Aliases = { new Alias {
        Urn = "urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db" } } });
```

{{% /choosable %}}

{{< /chooser >}}

Aliases are implicitly inherited from a [parent]({{< relref "parent" >}}) so that if a parent is moved (new name, new type, etc.) all children will also be aliased appropriately. This includes both updating the parent type in the qualified type in the child's URN, as well as updating the child name prefix if the name starts with the parent name. If there are aliases for both the parent and the child, all combinations of parent and child aliases are computed, allowing any combination of these previous parent and child identities to be treated as the same as the new identity. This process is inherited through any number of levels of parent/child relationships.  
