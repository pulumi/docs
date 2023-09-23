---
title_tag: "deletedWith | Resource Options"
meta_desc: The deletedWith resource option allows you to skip running resource deletion if another resource is being deleted as well.
title: "deletedWith"
h1: "Resource option: deletedWith"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    identifier: deletedWith
    parent: options
    weight: 5
aliases:
- /docs/intro/concepts/resources/options/deletedwith/
---

The `deletedWith` resource option allows you to skip resource deletion if a another resource is being deleted as well.

Pulumi will normally call the providers delete action for every resource during a delete operation. Sometimes this is redundant if another resource is deleted, such as a parent container resource, and can cause your delete or destroy operations to take longer than needed.

For example, if you are deleting a Kubernetes cluster or Kubernetes namespace, you might want to speed up deletion by skipping delete on any Pulumi managed resources created in that Kubernetes cluster or namespace since they will be deleted implicitely.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let k8s = require("@pulumi/kubernetes");

let ns = new k8s.core.v1.Namespace("res1", {/*...*/})
let dep = new k8s.apps.v1.Deployment("res2", {/*...*/}, { deletedWith: ns });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

let ns = new k8s.core.v1.Namespace("res1", {/*...*/})
let dep = new k8s.apps.v1.Deployment("res2", {/*...*/}, { deletedWith: ns });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# IMPORTANT: Python appends an underscore (`import_`) to avoid conflicting with the keyword.

import pulumi_kubernetes as k8s

ns = k8s.core.v1.Namespace("res1". {})
dep = k8s.apps.v1.Deployment("res2", opts=ResourceOptions(deletedWith=ns))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
ns, err := v1.NewNamespace(ctx, "res1", nil)
if err != nil {
  return err
}

dep, err := v1.NewDeployment(ctx, "res2", &v1.DeploymentArgs{/*...*/}, pulumi.DeletedWith(ns))
if err != nil {
  return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var ns = new Namespace("res1");
var dep = new Deployment("res2", new DeploymentArgs(), 
    new CustomResourceOptions { DeletedWith = { ns } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var ns = new Namespace("res1");
var dep = new Deployment("res2", new DeploymentArgs(), 
   CustomResourceOptions.builder()
        .deletedWith(ns)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  ns:
    type: kubernetes:apps/v1:Deployment
    name: res1
  res2:
    type: kubernetes:apps/v1:Deployment
    name: res2
    options:
      deletedWtih: ${ns}
        
```

{{% /choosable %}}

{{< /chooser >}}
