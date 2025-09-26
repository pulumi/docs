---
title_tag: "parent | Resource Options"
meta_desc: The parent resource option establishes an explicit parent/child relationship between resources.
title: "parent"
h1: "Resource option: parent"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: parent
    parent: options-concepts
    weight: 10
aliases:
- /docs/intro/concepts/resources/options/parent/
- /docs/concepts/options/parent/
---

The `parent` resource option specifies a parent for a resource, which has the following effects:

* The child inherits additional resource options from its parent.
* The Pulumi CLI shows the parent/child hierarchy in CLI output.

By default, resources are parented to the implicitly created `pulumi:pulumi:Stack` resource which is at the root of all Pulumi stacks. The most common use of explicitly setting the `parent` property is when authoring a [Component Resource](/docs/iac/concepts/components/). Resources that are part of a component should be explicitly parented to the component itself. This ensures that all resources within a component share desirable lifecycle behavior. You can also create multiple levels of nesting within a component to improve the visual display in the CLI.

## Setting a resource's parent

The following example shows a simple parent/child relationship between two resources:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const parent = new MyResource("parent", {/*...*/});
const child = new MyResource("child", {/*...*/}, { parent: parent });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
parent = MyResource("parent");
child = MyResource("child", opts=ResourceOptions(parent=parent));
```

{{% /choosable %}}
{{% choosable language go %}}

```go
parent, _ := NewMyResource(ctx, "parent", &MyResourceArgs{/*...*/})
child, _ := NewMyResource(ctx, "child", &MyResourceArgs{/*...*/}, pulumi.Parent(parent))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var parent = new MyResource("parent", new MyResourceArgs());
var child = new MyResource("child", new MyResourceArgs(),
    new CustomResourceOptions { Parent = parent });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var parent = new MyResource("parent");
var child = new MyResource("child",
    MyResourceArgs.Empty,
    CustomResourceOptions.builder()
        .parent(parent)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  parent:
    type: MyResource
  child:
    type: MyResource
    options:
      parent: ${parent}
```

{{% /choosable %}}

{{< /chooser >}}

## Parent relationships in the CLI

Specifying a resource's parent can help visually organize resources in the CLI. For example, the following `pulumi up` output shows an AWS Virtual Private Cloud (VPC) with two child subnets (and also shows the VPC's child relationship to the implicit `pulumi:pulumi:Stack` resource):

```bash
Previewing update (dev):

    Type                    Name                             Plan
    pulumi:pulumi:Stack     parent-demo-dev
+   ├─ aws:ec2:Vpc          default-vpc-866580ff             create
+   │  ├─ aws:ec2:Subnet    default-vpc-866580ff-public-1    create
+   │  └─ aws:ec2:Subnet    default-vpc-866580ff-public-0    create
```

## Inherited resource options

Child resources inherit the following values from their `parent`:

* [`provider`](/docs/iac/concepts/options/provider): Child resources inherit their parent's provider in order to ensure that child resources are created in the same cloud context (account, region, etc.) as their parent.

* [`aliases`](/docs/iac/concepts/options/aliases): Aliases are inherited so that changing the type of a parent resource correctly changes the qualified type of a child resource, and changing the name of a parent resource correctly changes the name prefix of child resources.

* [`protect`](/docs/iac/concepts/options/protect): Child resources inherit their parent's protection bit in order to ensure that deletions execute correctly. Children are deleted before their parent, so inheriting protection ensures that if a parent is marked as protected, none of its children will be deleted (because deleting the protected parent would fail).

* [`transforms`](/docs/iac/concepts/options/transforms):  Transforms applied to a parent will run on the parent and on all child resources. This allows a transform to be applied to a component to intercept and modify any resources created by its children. As a special case, [Stack transforms](/docs/iac/concepts/options/transforms#stack-transforms) will be applied to *all* resources (since all resources ultimately are parented directly or indirectly by the root stack resource).

* [`transformations`](/docs/iac/concepts/options/transformations):  Transformations applied to a parent will run on the parent and on all child resources. This allows a transformation to be applied to a component to intercept and modify any resources created by its children. As a special case, [Stack transformations](/docs/iac/concepts/options/transformations#stack-transformations) will be applied to *all* resources (since all resources ultimately are parented directly or indirectly by the root stack resource). Prefer `transforms` over `transformations` as the latter is deprecated.
