---
title_tag: "Resource Methods"
meta_desc: Learn about resource methods - functions attached to resource types that return computed values from resources you are managing with Pulumi.
title: Resource methods
h1: Resource methods
menu:
    iac:
        name: Resource methods
        parent: iac-concepts-functions
        weight: 3
---

Provider SDKs may also include _methods_ attached to a resource type. These methods return computed values from resources you are managing with Pulumi. For example, in the [EKS](/registry/packages/eks/api-docs/) SDK, the `Cluster` resource has a [.GetKubeconfig](/registry/packages/eks/api-docs/cluster/#method_GetKubeconfig) method:

<div><pulumi-examples>
<div><pulumi-chooser type="language" options="typescript,python,go,csharp,java,yaml,hcl"></pulumi-chooser></div>
<div>
<pulumi-choosable type="language" values="typescript">

```typescript
getKubeconfig(args?: Cluster.GetKubeconfigArgs): Output<Cluster.GetKubeconfigResult>
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="csharp">

```csharp
public Output<string> GetKubeconfig(ClusterGetKubeconfigArgs? args = null)
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="go">

```go
func (r *Cluster) GetKubeconfig(ctx *Context, args *ClusterGetKubeconfigArgs) (pulumi.StringOutput, error)
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="python">

```python
def get_kubeconfig(self,
                   profile_name: Optional[pulumi.Input[str]] = None,
                   role_arn: Optional[pulumi.Input[str]] = None) -> Output[str]:
    ...
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="java">

No example available for Java

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="yaml">

No example available for YAML

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="hcl">

Pulumi HCL has no method syntax. A `call` block invokes the method instead, labeled with the resource's logical name and the method name in snake_case, and its results are read as `call.<resource>.<method>.<attribute>`. The `required_providers` entry is required: without `source = "pulumi/eks"`, an unqualified `eks` resolves against the OpenTofu registry rather than the native Pulumi EKS package that defines this method.

```hcl
terraform {
  required_providers {
    eks = {
      source = "pulumi/eks"
    }
  }
}

resource "eks_cluster" "cluster" {
  # ...
}

call "cluster" "get_kubeconfig" {
  profile_name = "my-profile"
}

output "kubeconfig" {
  value     = call.cluster.get_kubeconfig.result
  sensitive = true
}
```

</pulumi-choosable>
</div>

</pulumi-examples></div>

Unlike provider functions, methods always appear in the _output form_: they take `Input` arguments, and return an `Output` (because they cannot execute until after the resource has been created). Resource methods do not accept invoke options.
