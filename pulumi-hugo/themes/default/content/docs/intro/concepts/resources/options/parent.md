---
title: "Parent"
meta_desc: The parent resource option establishes an explicit parent/child relationship between resources.
menu:
  intro:
    identifier: parent
    parent: options
    weight: 8
---

The `parent` resource option specifies a parent for a resource. It is used to associate children with the parents that encapsulate or are responsible for them. Good examples of this are [component resources]({{< relref "../components" >}}). The default behavior is to parent each resource to the implicitly-created `pulumi:pulumi:Stack` component resource that is a root resource for all Pulumi stacks.

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

* [`provider`]({{< relref "provider" >}}):  The provider instance used to construct a resource is inherited from it's parent, unless explicitly overridden by the child resource. The parent itself may have inherited the global [default provider]({{< relref "../providers/#default-provider-configuration" >}}) if no resource in the parent chain specified a provider instance for the corresponding provider type.

* [`aliases`]({{< relref "aliases" >}}):  Aliases applied to a parent are applied to all child resources, so that changing the type of a parent resource correctly changes the qualified type of a child resource, and changing the name of a parent resource correctly changes the name prefix of child resources.

* [`protect`]({{< relref "protect" >}}):  A protected parent will protect all children.  This ensures that if a parent is marked as protected, none of it's children will be deleted ahead of the attempt to delete the parent failing.

* [`transformations`]({{< relref "transformations" >}}):  Transformations applied to a parent will run on the parent and on all child resources. This allows a transformation to be applied to a component to intercept and modify any resources created by it's children. As a special case, [Stack transformations]({{< relref "transformations#stack-transformations" >}}) will be applied to *all* resources (since all resources ultimately are parented directly or indirectly by the root stack resource).
