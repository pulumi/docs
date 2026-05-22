---
title_tag: "aliases | Resource Options"
meta_desc: The aliases resource option is commonly used when refactoring Pulumi programs.
title: "aliases"
h1: "Resource option: aliases"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: aliases
    parent: options-concepts
    weight: 20
aliases:
  - /docs/iac/concepts/options/aliases/
  - /docs/intro/concepts/resources/#aliases
  - /docs/intro/concepts/resources/options/aliases/
  - /docs/concepts/options/aliases/
---

The `aliases` resource option provides a list of aliases for a resource or component resource. If you’re changing the name, type, or parent path of a resource or component resource, you can add the old name to the list of aliases for a resource to ensure that existing resources will be migrated to the new name instead of being deleted and replaced with the new named resource.

{{< resource-option-scope "aliases" >}}

Aliases are frequently used when refactoring Pulumi programs.

For example, imagine we change a database resource’s name from `old-name-for-db` to `new-name-for-db`. By default, when we run `pulumi up`, we see that the old resource is deleted and the new one created. If we annotate that resource with the aliases option, however, the resource is updated in-place. Pulumi identifies resources by their [URN](/docs/iac/concepts/resources/names/#urns), which encodes the resource name, so the alias tells Pulumi to treat the old URN as equivalent to the new one:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [{ name: "old-name-for-db" }] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('new-name-for-db',
    opts=ResourceOptions(aliases=[Alias(name='old-name-for-db')]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "new-name-for-db", &DatabaseArgs{ /*...*/ },
    pulumi.Aliases([]pulumi.Alias{
        {Name: pulumi.String("old-name-for-db")},
    }))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("new-name-for-db", new DatabaseArgs(),
    new CustomResourceOptions { Aliases = { new Alias { Name = "old-name-for-db"} } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var db = new Database("new-name-for-db",
    DatabaseArgs.Empty,
    CustomResourceOptions.builder()
        .aliases(Alias.builder()
            .name("old-name-for-db")
            .build())
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  db:
    type: new:Database
    options:
      aliases:
        - name: old-name-for-db
```

{{% /choosable %}}

{{< /chooser >}}

The aliases option accepts a list of old identifiers. If a resource has been renamed multiple times, it can have many aliases. The list of aliases may contain old `Alias` objects and/or old resource URNs.

The above example used objects of type `Alias` with the old resource names. These values may specify any combination of the old name, type, parent, stack, and/or project values. Alternatively, you can just specify the URN directly:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [ "urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db" ] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('new-name-for-db',
    opts=ResourceOptions(aliases=['urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db']))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "new-name-for-db", &DatabaseArgs{ /*...*/ },
    pulumi.Aliases([]pulumi.Alias{
        {URN: pulumi.URN("urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db")},
    }))
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
{{% choosable language java %}}

```java
var db = new Database("new-name-for-db", DatabaseArgs.Empty,
    CustomResourceOptions.builder()
        .aliases(Alias.withUrn("urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db"))
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  db:
    type: new:Database
    options:
      aliases:
        - urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db
```

{{% /choosable %}}

{{< /chooser >}}

## Aliasing by parent

If a resource was moved to a different parent component resource, use the `parent` field to reference the old parent resource so that Pulumi can map the old URN to the new one:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let db = new Database("db", {/*...*/},
    { aliases: [{ parent: oldParentResource }] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('db',
    opts=ResourceOptions(aliases=[Alias(parent=old_parent_resource)]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.Aliases([]pulumi.Alias{
        {Parent: oldParentResource},
    }))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("db", new DatabaseArgs(),
    new CustomResourceOptions { Aliases = { new Alias { Parent = oldParentResource } } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var db = new Database("db",
    DatabaseArgs.Empty,
    CustomResourceOptions.builder()
        .aliases(Alias.builder()
            .parent(oldParentResource)
            .build())
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  old-parent:
    type: SomeComponent
  db:
    type: aws:rds/instance:Instance
    options:
      aliases:
        - parent: ${old-parent}
```

{{% /choosable %}}

{{< /chooser >}}

## Aliasing by stack and project

If a resource was moved from another stack or project, use the `stack` and/or `project` fields to refer to the old identity:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let db = new Database("db", {/*...*/},
    { aliases: [{ stack: "old-stack", project: "old-project" }] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('db',
    opts=ResourceOptions(aliases=[Alias(stack='old-stack', project='old-project')]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.Aliases([]pulumi.Alias{
        {Stack: pulumi.String("old-stack"), Project: pulumi.String("old-project")},
    }))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("db", new DatabaseArgs(),
    new CustomResourceOptions { Aliases = { new Alias { Stack = "old-stack", Project = "old-project" } } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var db = new Database("db",
    DatabaseArgs.Empty,
    CustomResourceOptions.builder()
        .aliases(Alias.builder()
            .stack("old-stack")
            .project("old-project")
            .build())
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  db:
    type: aws:rds/instance:Instance
    options:
      aliases:
        - stack: old-stack
          project: old-project
```

{{% /choosable %}}

{{< /chooser >}}

## Aliasing by type

If a resource's type was changed (for example, when migrating to a different provider resource type), use the `type` field to specify the old type:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let db = new Database("db", {/*...*/},
    { aliases: [{ type: "aws:rds/instance:Instance" }] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('db',
    opts=ResourceOptions(aliases=[Alias(type_='aws:rds/instance:Instance')]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.Aliases([]pulumi.Alias{
        {Type: pulumi.String("aws:rds/instance:Instance")},
    }))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("db", new DatabaseArgs(),
    new CustomResourceOptions { Aliases = { new Alias { Type = "aws:rds/instance:Instance" } } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var db = new Database("db",
    DatabaseArgs.Empty,
    CustomResourceOptions.builder()
        .aliases(Alias.builder()
            .type("aws:rds/instance:Instance")
            .build())
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  db:
    type: aws:rds/instance:Instance
    options:
      aliases:
        - type: aws:rds/database:Database
```

{{% /choosable %}}

{{< /chooser >}}

Aliases are implicitly inherited from a [parent](/docs/iac/concepts/resources/options/parent/) so that if a parent is moved (new name, new type, etc.) all children will also be aliased appropriately. This includes both updating the parent type in the qualified type in the child's URN, as well as updating the child name prefix if the name starts with the parent name. If there are aliases for both the parent and the child, all combinations of parent and child aliases are computed, allowing any combination of these previous parent and child identities to be treated as the same as the new identity. This process is inherited through any number of levels of parent/child relationships.

Once a resource has been migrated on all stacks, the alias can be removed from the resource declaration.
