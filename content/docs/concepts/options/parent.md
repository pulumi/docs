---
title_tag: "parent | Resource Options"
meta_desc: The parent resource option establishes an explicit parent/child relationship between resources.
title: "parent"
h1: "Resource option: parent"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    identifier: parent
    parent: options
    weight: 9
aliases:
- /docs/intro/concepts/resources/options/parent/
---

The `parent` resource option specifies a parent for a resource. It is used to associate children with the parents that encapsulate or are responsible for them. Good examples of this are [component resources](/docs/concepts/resources/components/). The default behavior is to parent each resource to the implicitly-created `pulumi:pulumi:Stack` component resource that is a root resource for all Pulumi stacks.

{{% notes type="warning" %}}
Although the `parent` resource option can be used to parent a resource to any other resource, it is strongly recommended to parent resources only to [component resources](/docs/concepts/resources/components/) when they are actually children.  Parenting a resource to another [custom resource](/docs/concepts/resources/) can in some cases result in undefined behavior.
{{% /notes %}}

For example, this code creates two resources, a parent and child, the latter of which is a child to the former:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let parent = new MyResource("parent", {/*...*/});
let child = new MyResource("child", {/*...*/}, { parent: parent });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let parent = new MyResource("parent", {/*...*/});
let child = new MyResource("child", {/*...*/}, { parent: parent });
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

Using parents can clarify causality or why a given resource was created in the first place. For example, this pulumi up output shows an AWS Virtual Private Cloud (VPC) with two subnets attached to it, and also shows that the VPC directly belongs to the implicit `pulumi:pulumi:Stack` resource:

```bash
Previewing update (dev):

    Type                       Name                             Plan
    pulumi:pulumi:Stack        parent-demo-dev
+   ├─ awsx:x:ec2:Vpc          default-vpc-866580ff             create
+   │  ├─ awsx:x:ec2:Subnet    default-vpc-866580ff-public-1    create
+   │  └─ awsx:x:ec2:Subnet    default-vpc-866580ff-public-0    create
```

Child resources inherit default values for many other resource options from their `parent`, including:

* [`provider`](/docs/concepts/options/provider):  The provider instance used to construct a resource is inherited from its parent, unless explicitly overridden by the child resource. The parent itself may have inherited the global [default provider](../providers/#default-provider-configuration) if no resource in the parent chain specified a provider instance for the corresponding provider type.

* [`aliases`](/docs/concepts/options/aliases):  Aliases applied to a parent are applied to all child resources, so that changing the type of a parent resource correctly changes the qualified type of a child resource, and changing the name of a parent resource correctly changes the name prefix of child resources.

* [`protect`](/docs/concepts/options/protect):  A protected parent will protect all children.  This ensures that if a parent is marked as protected, none of it's children will be deleted ahead of the attempt to delete the parent failing.

* [`transformations`](/docs/concepts/options/transformations):  Transformations applied to a parent will run on the parent and on all child resources. This allows a transformation to be applied to a component to intercept and modify any resources created by its children. As a special case, [Stack transformations](/docs/concepts/options/transformations#stack-transformations) will be applied to *all* resources (since all resources ultimately are parented directly or indirectly by the root stack resource). Prefer `transforms` if possible. `transformations` will be deprecated in the future in favor of `transforms`.

* [`transforms`](/docs/concepts/options/transforms):  Transforms applied to a parent will run on the parent and on all child resources. This allows a transform to be applied to a component to intercept and modify any resources created by its children. As a special case, [Stack transforms](/docs/concepts/options/transforms#stack-transforms) will be applied to *all* resources (since all resources ultimately are parented directly or indirectly by the root stack resource).
