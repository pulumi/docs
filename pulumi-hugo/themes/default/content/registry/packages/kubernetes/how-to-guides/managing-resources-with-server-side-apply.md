---
title: "Managing Resources with Server-Side Apply"
meta_desc: Learn how to manage Kubernetes resources with Server-Side Apply
layout: how-to-guide
---

[Server-Side Apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/) (SSA) is a resource management strategy that was introduced in Kubernetes `v1.18`. Clients using SSA can safely share the management of Kubernetes resources by making the API Server responsible for computing diffs and resolving conflicts.

The [v3.20.0 release](https://github.com/pulumi/pulumi-kubernetes/releases/tag/v3.20.0) of the Pulumi Kubernetes provider added support for managing resources using SSA. This feature is currently opt-in using the `enableServerSideApply` [Provider option]({{< relref "/registry/packages/kubernetes/api-docs/provider">}}), but will become the default in the next major release. Using SSA provides the following benefits:

1. Kubernetes resources may be safely managed by more than one controller.
2. It is now possible to "Upsert" resources; create the resource if it does not exist, or apply the configuration to an existing resource.
3. It is now possible to patch resources with the Patch resource types in the SDK. Each resource type in the SDK has a corresponding Patch resource.
4. The `last-applied-configuration` annotation is no longer used.

This guide will show you how to enable SSA support and use these features to manage Kubernetes resources.

## Enable Server-Side Apply

Use the `enableServerSideApply` [Provider option]({{< relref "/registry/packages/kubernetes/api-docs/provider">}}) option to enable Server-Side Apply for the Provider. This option can be set in the following ways:

1. Set the stack config explicitly with `pulumi config set kubernetes:enableServerSideApply true`
2. Set the stack config using an environment variable: `PULUMI_K8S_ENABLE_SERVER_SIDE_APPLY=true`
3. Set the `enableServerSideApply option` on a first-class Provider as shown in the following example

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

const provider = new kubernetes.Provider("k8s", {enableServerSideApply: true});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_kubernetes as kubernetes

provider = kubernetes.Provider("k8s", enable_server_side_apply=True)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        _, err := kubernetes.NewProvider(ctx, "k8s", &kubernetes.ProviderArgs{
            EnableServerSideApply: pulumi.BoolPtr(true),
        })
		if err != nil {
			return err
		}
		return nil
	})
}

```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Kubernetes;

await Deployment.RunAsync(() =>
{
    var provider = new Provider("k8s", new ProviderArgs
    {
        EnableServerSideApply = true,
    });
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.kubernetes;
import com.pulumi.kubernetes.ProviderArgs;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var provider = new Provider("provider", ProviderArgs.builder()
            .enableServerSideApply(true)
            .build());

    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
    provider:
        type: pulumi:providers:kubernetes
        properties:
            enableServerSideApply: true
```

{{% /choosable %}}

{{< /chooser >}}

## Upsert a Resource

With Server-Side Apply mode enabled, you can "upsert" a resource; that is, update a resource if it already exists, or create it if it does not yet exist. You can set the `pulumi.com/patchForce` annotation if you want to force an override for any conflicts with an existing version of the resource.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

const provider = new kubernetes.Provider("k8s", {enableServerSideApply: true});
const example = new kubernetes.core.v1.ConfigMap("example", {
    metadata: {
        annotations: {
            "pulumi.com/patchForce": "true",
        },
        name: "example",
    },
    data: {
        foo: "bar",
    },
}, {
    provider: provider,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_kubernetes as kubernetes

provider = kubernetes.Provider("k8s", enable_server_side_apply=True)
example = kubernetes.core.v1.ConfigMap("example",
                                       metadata=kubernetes.meta.v1.ObjectMetaArgs(
                                           annotations={
                                               "pulumi.com/patchForce": "true",
                                           },
                                           name="example",
                                       ),
                                       data={
                                           "foo": "bar",
                                       },
                                       opts=pulumi.ResourceOptions(provider=provider))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
    corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
    metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        provider, err := kubernetes.NewProvider(ctx, "provider", &kubernetes.ProviderArgs{
            EnableServerSideApply: pulumi.Bool(true),
        })
        if err != nil {
            return err
        }
        _, err = corev1.NewConfigMap(ctx, "example", &corev1.ConfigMapArgs{
            Metadata: &metav1.ObjectMetaArgs{
                Annotations: pulumi.StringMap{
                    "pulumi.com/patchForce": pulumi.String("true"),
                },
                Name: pulumi.String("example"),
            },
            Data: pulumi.StringMap{
                "foo": pulumi.String("bar"),
            },
        }, pulumi.Provider(provider))
        if err != nil {
            return err
        }
        return nil
    })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    var provider = new Kubernetes.Provider("provider", new()
    {
        EnableServerSideApply = true,
    });

    var example = new Kubernetes.Core.V1.ConfigMap("example", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Annotations =
            {
                { "pulumi.com/patchForce", "true" },
            },
            Name = "example",
        },
        Data =
        {
            { "foo", "bar" },
        },
    }, new CustomResourceOptions
    {
        Provider = provider,
    });
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.kubernetes;
import com.pulumi.kubernetes.ProviderArgs;
import com.pulumi.kubernetes.core_v1.ConfigMap;
import com.pulumi.kubernetes.core_v1.ConfigMapArgs;
import com.pulumi.kubernetes.meta_v1.inputs.ObjectMetaArgs;
import com.pulumi.resources.CustomResourceOptions;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var provider = new Provider("provider", ProviderArgs.builder()
            .enableServerSideApply(true)
            .build());

        var example = new ConfigMap("example", ConfigMapArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .annotations(Map.of("pulumi.com/patchForce", "true"))
                .name("example")
                .build())
            .data(Map.of("foo", "bar"))
            .build(), CustomResourceOptions.builder()
                .provider(provider)
                .build());

    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
    provider:
        type: pulumi:providers:kubernetes
        properties:
            enableServerSideApply: true
    example:
        type: kubernetes:core/v1:ConfigMap
        properties:
            metadata:
                annotations:
                    pulumi.com/patchForce: "true"
                name:
                    example
            data:
                foo: bar
        options:
            provider: ${provider}
```

{{% /choosable %}}

{{< /chooser >}}

## Patch a Resource

With Server-Side Apply mode enabled, you can patch an existing resource to make changes to it. Every resource type in the SDK includes a corresponding Patch resource for this purpose. Patch resources have a few important differences from typical SDK resources:

1. The resource name (`.metadata.name`) is required, and auto-naming is not supported. The patch operation applies to an existing resource, so this field is used to specify which resource to patch. Remember to specify the namespace as well if required.
2. All other fields are optional, even if they would be required for a normal resource. The patch specification must be unambiguous, but it is not necessary to specify the complete resource.
3. More than one Patch resource may modify the same underlying Kubernetes resource. Each Patch resource is assigned a unique `FieldManager` name by default, or you can manually specify one using the `pulumi.com/patchFieldManager` annotation.
4. Server-Side Apply mode must be enabled to use Patch resources.
5. Deleting a Patch resource will undo the patched changes to the Kubernetes resource, but the resource will not be deleted. Any fields that become unmanaged during this process will reset to their default values, so the resulting resource may have changes from its original state before patching. See the [upstream docs](https://kubernetes.io/docs/reference/using-api/server-side-apply/#transferring-ownership) for more information about this behavior.

You can set the `pulumi.com/patchForce` annotation if you want to force an override for any conflicts with an existing version of the resource.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

const provider = new kubernetes.Provider("provider", {enableServerSideApply: true});
const patch1 = new kubernetes.core.v1.ConfigMapPatch("patch1", {
    metadata: {
        annotations: {
            "pulumi.com/patchForce": "true",
        },
        name: "example",
    },
    data: {
        foo: "bar",
    },
}, {
    provider: provider,
});
const patch2 = new kubernetes.core.v1.ConfigMapPatch("patch2", {
    metadata: {
        annotations: {
            "pulumi.com/patchForce": "true",
        },
        name: "example",
    },
    data: {
        oof: "rab",
    },
}, {
    provider: provider,
    dependsOn: [patch1],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_kubernetes as kubernetes

provider = kubernetes.Provider("k8s", enable_server_side_apply=True)
patch1 = kubernetes.core.v1.ConfigMapPatch("patch1",
                                           metadata=kubernetes.meta.v1.ObjectMetaPatchArgs(
                                               annotations={
                                                   "pulumi.com/patchForce": "true",
                                               },
                                               name="example",
                                           ),
                                           data={
                                               "foo": "bar",
                                           },
                                           opts=pulumi.ResourceOptions(provider=provider))
patch2 = kubernetes.core.v1.ConfigMapPatch("patch2",
                                           metadata=kubernetes.meta.v1.ObjectMetaPatchArgs(
                                               annotations={
                                                   "pulumi.com/patchForce": "true",
                                               },
                                               name="example",
                                           ),
                                           data={
                                               "oof": "rab",
                                           },
                                           opts=pulumi.ResourceOptions(provider=provider,
                                                                       depends_on=[patch1]))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
    corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
    metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        provider, err := kubernetes.NewProvider(ctx, "provider", &kubernetes.ProviderArgs{
            EnableServerSideApply: pulumi.Bool(true),
        })
        if err != nil {
            return err
        }
        patch1, err := corev1.NewConfigMapPatch(ctx, "patch1", &corev1.ConfigMapPatchArgs{
            Metadata: &metav1.ObjectMetaPatchArgs{
                Annotations: pulumi.StringMap{
                    "pulumi.com/patchForce": pulumi.String("true"),
                },
                Name: pulumi.String("example"),
            },
            Data: pulumi.StringMap{
                "foo": pulumi.String("bar"),
            },
        }, pulumi.Provider(provider))
        if err != nil {
            return err
        }
        _, err = corev1.NewConfigMapPatch(ctx, "patch2", &corev1.ConfigMapPatchArgs{
            Metadata: &metav1.ObjectMetaPatchArgs{
                Annotations: pulumi.StringMap{
                    "pulumi.com/patchForce": pulumi.String("true"),
                },
                Name: pulumi.String("example"),
            },
            Data: pulumi.StringMap{
                "oof": pulumi.String("rab"),
            },
        }, pulumi.Provider(provider), pulumi.DependsOn([]pulumi.Resource{
            patch1,
        }))
        if err != nil {
            return err
        }
        return nil
    })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    var provider = new Kubernetes.Provider("provider", new()
    {
        EnableServerSideApply = true,
    });

    var patch1 = new Kubernetes.Core.V1.ConfigMapPatch("patch1", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaPatchArgs
        {
            Annotations =
            {
                { "pulumi.com/patchForce", "true" },
            },
            Name = "example",
        },
        Data =
        {
            { "foo", "bar" },
        },
    }, new CustomResourceOptions
    {
        Provider = provider,
    });

    var patch2 = new Kubernetes.Core.V1.ConfigMapPatch("patch2", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaPatchArgs
        {
            Annotations =
            {
                { "pulumi.com/patchForce", "true" },
            },
            Name = "example",
        },
        Data =
        {
            { "oof", "rab" },
        },
    }, new CustomResourceOptions
    {
        Provider = provider,
        DependsOn = new[]
        {
            patch1,
        },
    });
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.kubernetes;
import com.pulumi.kubernetes.ProviderArgs;
import com.pulumi.kubernetes.core_v1.ConfigMapPatch;
import com.pulumi.kubernetes.core_v1.ConfigMapPatchArgs;
import com.pulumi.kubernetes.meta_v1.inputs.ObjectMetaPatchArgs;
import com.pulumi.resources.CustomResourceOptions;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var provider = new Provider("provider", ProviderArgs.builder()
            .enableServerSideApply(true)
            .build());

        var patch1 = new ConfigMapPatch("patch1", ConfigMapPatchArgs.builder()
            .metadata(ObjectMetaPatchArgs.builder()
                .annotations(Map.of("pulumi.com/patchForce", "true"))
                .name("example")
                .build())
            .data(Map.of("foo", "bar"))
            .build(), CustomResourceOptions.builder()
                .provider(provider)
                .build());

        var patch2 = new ConfigMapPatch("patch2", ConfigMapPatchArgs.builder()
            .metadata(ObjectMetaPatchArgs.builder()
                .annotations(Map.of("pulumi.com/patchForce", "true"))
                .name("example")
                .build())
            .data(Map.of("oof", "rab"))
            .build(), CustomResourceOptions.builder()
                .provider(provider)
                .dependsOn(patch1)
                .build());

    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
    provider:
        type: pulumi:providers:kubernetes
        properties:
            enableServerSideApply: true
    patch1:
        type: kubernetes:core/v1:ConfigMapPatch
        properties:
            metadata:
                annotations:
                    pulumi.com/patchForce: "true"
                name:
                    example
            data:
                foo: bar
        options:
            provider: ${provider}
    patch2:
        type: kubernetes:core/v1:ConfigMapPatch
        properties:
            metadata:
                annotations:
                    pulumi.com/patchForce: "true"
                name:
                    example
            data:
                oof: rab
        options:
            dependsOn:
                - ${patch1}
            provider: ${provider}
```

{{% /choosable %}}

{{< /chooser >}}

### Delete an existing field using Patch

With Server-Side Apply mode enabled, you can also remove a field from an existing resource. This example demonstrates removing `.labels.foo` from an existing Namespace.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

const uuid = "ee0d1b94-e749-4de4-ae8a-e4319a7f3ef2"; // Arbitrary UUID
const provider = new kubernetes.Provider("provider", {enableServerSideApply: true});
const patch1 = new kubernetes.core.v1.NamespacePatch("patch1", {metadata: {
        name: "foo",
        annotations: {
            "pulumi.com/patchForce": "true",
            "pulumi.com/patchFieldManager": uuid,
        },
        labels: {
            foo: "",
        },
    }}, {
    provider: provider,
});
const patch2 = new kubernetes.core.v1.NamespacePatch("patch2", {metadata: {
        name: "foo",
        annotations: {
            "pulumi.com/patchForce": "true",
            "pulumi.com/patchFieldManager": uuid,
        },
        labels: {
            foo: undefined,
        },
    }}, {
    provider: provider,
    dependsOn: [patch1],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_kubernetes as kubernetes

uuid = "ee0d1b94-e749-4de4-ae8a-e4319a7f3ef2" # Arbitrary UUID
provider = pulumi.providers.Kubernetes("provider", enable_server_side_apply=True)
patch1 = kubernetes.core.v1.NamespacePatch("patch1", metadata=kubernetes.meta.v1.ObjectMetaPatchArgs(
    name="foo",
    annotations={
        "pulumi.com/patchForce": "true",
        "pulumi.com/patchFieldManager": uuid,
    },
    labels={
        "foo": "",
    },
), opts=pulumi.ResourceOptions(provider=provider))
patch2 = kubernetes.core.v1.NamespacePatch("patch2", metadata=kubernetes.meta.v1.ObjectMetaPatchArgs(
    name="foo",
    annotations={
        "pulumi.com/patchForce": "true",
        "pulumi.com/patchFieldManager": uuid,
    },
    labels={
        "foo": None,
    },
), opts=pulumi.ResourceOptions(provider=provider, depends_on=[patch1]))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
    corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
    metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        uuid := "ee0d1b94-e749-4de4-ae8a-e4319a7f3ef2" // Arbitrary UUID
        provider, err := kubernetes.NewProvider(ctx, "provider", &kubernetes.ProviderArgs{
            EnableServerSideApply: pulumi.Bool(true),
        })
        if err != nil {
            return err
        }
        patch1, err := corev1.NewNamespacePatch(ctx, "patch1", &corev1.NamespacePatchArgs{
            Metadata: &metav1.ObjectMetaPatchArgs{
                Name: pulumi.String("foo"),
                Annotations: pulumi.StringMap{
                    "pulumi.com/patchForce":        pulumi.String("true"),
                    "pulumi.com/patchFieldManager": pulumi.String(uuid),
                },
                Labels: pulumi.StringMap{
                    "foo": pulumi.String(""),
                },
            },
        }, pulumi.Provider(provider))
        if err != nil {
            return err
        }
        _, err = corev1.NewNamespacePatch(ctx, "patch2", &corev1.NamespacePatchArgs{
            Metadata: &metav1.ObjectMetaPatchArgs{
                Name: pulumi.String("foo"),
                Annotations: pulumi.StringMap{
                    "pulumi.com/patchForce":        pulumi.String("true"),
                    "pulumi.com/patchFieldManager": pulumi.String(uuid),
                },
                Labels: pulumi.StringMap{
                    "foo": nil,
                },
            },
        }, pulumi.Provider(provider), pulumi.DependsOn([]pulumi.Resource{
            patch1,
        }))
        if err != nil {
            return err
        }
        return nil
    })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    var uuid = "ee0d1b94-e749-4de4-ae8a-e4319a7f3ef2"; // Arbitrary UUID

    var provider = new Kubernetes.Provider("provider", new()
    {
        EnableServerSideApply = true,
    });

    var patch1 = new Kubernetes.Core.V1.NamespacePatch("patch1", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaPatchArgs
        {
            Name = "foo",
            Annotations =
            {
                { "pulumi.com/patchForce", "true" },
                { "pulumi.com/patchFieldManager", uuid },
            },
            Labels =
            {
                { "foo", "" },
            },
        },
    }, new CustomResourceOptions
    {
        Provider = provider,
    });

    var patch2 = new Kubernetes.Core.V1.NamespacePatch("patch2", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaPatchArgs
        {
            Name = "foo",
            Annotations =
            {
                { "pulumi.com/patchForce", "true" },
                { "pulumi.com/patchFieldManager", uuid },
            },
            Labels =
            {
                { "foo", null },
            },
        },
    }, new CustomResourceOptions
    {
        Provider = provider,
        DependsOn = new[]
        {
            patch1,
        },
    });
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.kubernetes;
import com.pulumi.kubernetes.ProviderArgs;
import com.pulumi.kubernetes.core_v1.NamespacePatch;
import com.pulumi.kubernetes.core_v1.NamespacePatchArgs;
import com.pulumi.kubernetes.meta_v1.inputs.ObjectMetaPatchArgs;
import com.pulumi.resources.CustomResourceOptions;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        final var uuid = "ee0d1b94-e749-4de4-ae8a-e4319a7f3ef2"; // Arbitrary UUID

        var provider = new Provider("provider", ProviderArgs.builder()
            .enableServerSideApply(true)
            .build());

        var patch1 = new NamespacePatch("patch1", NamespacePatchArgs.builder()
            .metadata(ObjectMetaPatchArgs.builder()
                .name("foo")
                .annotations(Map.ofEntries(
                    Map.entry("pulumi.com/patchForce", "true"),
                    Map.entry("pulumi.com/patchFieldManager", uuid)
                ))
                .labels(Map.of("foo", ""))
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(provider)
                .build());

        var patch2 = new NamespacePatch("patch2", NamespacePatchArgs.builder()
            .metadata(ObjectMetaPatchArgs.builder()
                .name("foo")
                .annotations(Map.ofEntries(
                    Map.entry("pulumi.com/patchForce", "true"),
                    Map.entry("pulumi.com/patchFieldManager", uuid)
                ))
                .labels(Map.of("foo", null))
                .build())
            .build(), CustomResourceOptions.builder()
                .provider(provider)
                .dependsOn(patch1)
                .build());

    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
variables:
    uuid: ee0d1b94-e749-4de4-ae8a-e4319a7f3ef2 # Arbitrary UUID
resources:
    provider:
        type: pulumi:providers:kubernetes
        properties:
            enableServerSideApply: true
    patch1:
        type: kubernetes:core/v1:NamespacePatch
        properties:
            metadata:
                name: foo
                annotations:
                    pulumi.com/patchForce: "true"
                    pulumi.com/patchFieldManager: ${uuid}
                labels:
                    foo: ""
        options:
            provider: ${provider}
    patch2:
        type: kubernetes:core/v1:NamespacePatch
        properties:
            metadata:
                name: foo
                annotations:
                    pulumi.com/patchForce: "true"
                    pulumi.com/patchFieldManager: ${uuid}
                labels:
                    foo: null
        options:
            provider: ${provider}
            dependsOn:
                - ${patch1}
```

{{% /choosable %}}

{{< /chooser >}}
