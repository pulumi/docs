---
title: "New: Helm Chart v4 resource with new features and languages"
date: 2024-06-13T00:00:00-07:00
meta_desc: >-
  Pulumi Kubernetes v4.13 offers a new resource for applying Helm charts consistently
  across Pulumi SDKs, with new features and SDK support.
meta_image: chartv4.png
authors:
  - eron-wright

tags:
  - kubernetes
  - yaml
  - java
  - helm
search:
  keywords:
    - v4
    - helm
    - chart
    - new
    - features
    - resource
    - kubernetes
---

Today we're happy to announce a new "v4" version of the Chart resource, available now in v4.13 of the Pulumi Kubernetes provider.
The new [kubernetes.helm.sh/v4.Chart](/registry/packages/kubernetes/api-docs/helm/v4/chart/) resource is provided
side-by-side with the existing [kubernetes.helm.sh/v3.Chart](/registry/packages/kubernetes/api-docs/helm/v3/chart/) resource.
We expect to deprecate v3 in the future.

When you need to install a third-party application into your Kubernetes cluster, you're likely to find a
Helm chart for that in [Artifact Hub](https://artifacthub.io/) or other registry. Pulumi provides two
ways to apply a Helm chart, as outlined in [Choosing the Right Helm Resource For Your Use Case](/registry/packages/kubernetes/how-to-guides/choosing-the-right-helm-resource-for-your-use-case/).  The Chart resource offers deeper integration with Pulumi
and better drift remediation. v4 brings a host of new features, including enhanced SDK support across all Pulumi SDKs, full OCI registry support, improved handling of chart values, better connectivity for cluster interactions, and improved resource ordering.
Let's dig in.

## What's new

Let's look at what's new with Chart v4.

### New language support - Java SDK & YAML SDK

The Chart v4 resource is a [Pulumi Component](/docs/iac/packages-and-automation/pulumi-packages/debugging-provider-packages/#types-of-pulumi-packages) that works
consistently across all Pulumi SDKs. Earlier versions were implemented separately for each SDK, leading to various
inconsistencies and limited SDK support.

Here, for example, is a simple deployment of [cert-manager](https://cert-manager.io/), a well-known Kubernetes add-on:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

const certman = new kubernetes.helm.v4.Chart("cert-manager", {
    namespace: "cert-manager",
    chart: "oci://registry-1.docker.io/bitnamicharts/cert-manager",
    version: "1.3.1",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_kubernetes as kubernetes

certman = kubernetes.helm.v4.Chart("cert-manager",
    namespace="cert-manager",
    chart="oci://registry-1.docker.io/bitnamicharts/cert-manager",
    version="1.3.1")
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	helmv4 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v4"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := helmv4.NewChart(ctx, "cert-manager", &helmv4.ChartArgs{
			Namespace: pulumi.String("cert-manager"),
			Chart:     pulumi.String("oci://registry-1.docker.io/bitnamicharts/cert-manager"),
			Version:   pulumi.String("1.3.1"),
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
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    var certman = new Kubernetes.Helm.V4.Chart("cert-manager", new()
    {
        Namespace = "cert-manager",
        Chart = "oci://registry-1.docker.io/bitnamicharts/cert-manager",
        Version = "1.3.1",
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
import com.pulumi.kubernetes.helm.sh_v4.Chart;
import com.pulumi.kubernetes.helm.sh_v4.ChartArgs;
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
        var certman = new Chart("cert-manager", ChartArgs.builder()
            .namespace("cert-manager")
            .chart("oci://registry-1.docker.io/bitnamicharts/cert-manager")
            .version("1.3.1")
            .build());

    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  cert-manager:
    type: kubernetes:helm.sh/v4:Chart
    properties:
      namespace: cert-manager
      chart: oci://registry-1.docker.io/bitnamicharts/cert-manager
      version: "1.3.1"
```

{{% /choosable %}}

{{< /chooser >}}

### OCI registry support

You can use container registries with OCI support such as [Docker Hub](https://hub.docker.com/) to store and share
Helm chart packages. The Chart v4 resource now has full support for OCI, bringing it to parity with
the Release resource.

To use an authenticated OCI registry, you must first login using `helm registry login` or `docker login`.

Chart v4 also supports the use of [Helm chart repositories](https://helm.sh/docs/topics/chart_repository/),
and adopts the same `repositoryOpts` API as was introduced in the Release resource.

### Lock file support

Helm has support for lock files (Chart.lock) to control a chart's dependencies. When deploying a chart from a local directory,
Pulumi automatically rebuilds the chart's dependencies if a lock file is present. See
[Helm Dependency Build](https://helm.sh/docs/helm/helm_dependency_build/) for details.

### Better handling of chart values

Chart v4 offers new ways to work with Chart values. It is now possible to use multiple values files and to use
[Pulumi Assets](/docs/concepts/assets-archives/#assets). Of course you can also use output values from other
resources as chart values.

It is also possible to set a chart value to the contents of a text file, similarly to using Helm's `--set-file` argument.
To do that, simply use a Pulumi Asset as a value within the `values` map. This is useful for injecting large
values into a chart, such as additional templates as supported by the `extraDeploy` parameter of some Bitnami charts.

Here's an example of using a combination of values from different sources.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

const certManager = new kubernetes.helm.v4.Chart("cert-manager", {
    namespace: "cert-manager",
    chart: "oci://registry-1.docker.io/bitnamicharts/cert-manager",
    version: "1.3.1",
    valueYamlFiles: [new pulumi.asset.FileAsset("values.yaml")],
    values: {
        commonLabels: {
            "pulumi.com/stackName": pulumi.getStack(),
        },
        extraDeploy: [new pulumi.asset.FileAsset("manifest.yaml")],
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_kubernetes as kubernetes

cert_manager = kubernetes.helm.v4.Chart("cert-manager",
    namespace="cert-manager",
    chart="oci://registry-1.docker.io/bitnamicharts/cert-manager",
    version="1.3.1",
    value_yaml_files=[pulumi.FileAsset("values.yaml")],
    values={
        "commonLabels": {
            "pulumi.com/stackName": pulumi.get_stack(),
        },
        "extraDeploy": [pulumi.FileAsset("manifest.yaml")],
    })
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	helmv4 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v4"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := helmv4.NewChart(ctx, "cert-manager", &helmv4.ChartArgs{
			Namespace: pulumi.String("cert-manager"),
			Chart:     pulumi.String("oci://registry-1.docker.io/bitnamicharts/cert-manager"),
			Version:   pulumi.String("1.3.1"),
			ValueYamlFiles: pulumi.AssetOrArchiveArray{
				pulumi.NewFileAsset("values.yaml"),
			},
			Values: pulumi.Map{
				"commonLabels": pulumi.Any(map[string]interface{}{
					"pulumi.com/stackName": ctx.Stack(),
				}),
				"extraDeploy": pulumi.Array{
					pulumi.NewFileAsset("manifest.yaml"),
				},
			},
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
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    var certManager = new Kubernetes.Helm.V4.Chart("cert-manager", new()
    {
        Namespace = "cert-manager",
        Chart = "oci://registry-1.docker.io/bitnamicharts/cert-manager",
        Version = "1.3.1",
        ValueYamlFiles = new[]
        {
            new FileAsset("values.yaml"),
        },
        Values =
        {
            { "commonLabels", new Dictionary<string, object?>
            {
                ["pulumi.com/stackName"] = Deployment.Instance.StackName,
            } },
            { "extraDeploy", new[]
            {
                new FileAsset("manifest.yaml"),
            } },
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
import com.pulumi.deployment.Deployment;
import com.pulumi.kubernetes.helm.v4.Chart;
import com.pulumi.kubernetes.helm.v4.ChartArgs;
import com.pulumi.asset.FileAsset;
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
        var certManager = new Chart("cert-manager", ChartArgs.builder()
            .namespace("cert-manager")
            .chart("oci://registry-1.docker.io/bitnamicharts/cert-manager")
            .version("1.3.1")
            .valueYamlFiles(new FileAsset("values.yaml"))
            .values(Map.ofEntries(
                Map.entry("commonLabels", Map.of("pulumi.com/stackName", Deployment.getInstance().getStackName())),
                Map.entry("extraDeploy", List.of(new FileAsset("manifest.yaml")))
            ))
            .build());

    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  cert-manager:
    type: kubernetes:helm.sh/v4:Chart
    properties:
      namespace: cert-manager
      chart: oci://registry-1.docker.io/bitnamicharts/cert-manager
      version: "1.3.1"
      valueYamlFiles:
      - fn::fileAsset: values.yaml
      values:
        commonLabels:
          pulumi.com/stackName: ${pulumi.stack}
        extraDeploy:
        - fn::fileAsset: manifest.yaml
```

{{% /choosable %}}

{{< /chooser >}}

### Better connectivity

You may now use charts that use chart functions requiring a connection to the cluster, e.g. to:

- Check the Kubernetes server version with [`.Capabilities.KubeVersion`](https://helm.sh/docs/chart_template_guide/builtin_objects/)
- Check if an API version or kind is available with [`.Capabilities.APIVersions.Has`](https://helm.sh/docs/chart_template_guide/function_list/#capabilitiesapiversionshas)
- Use the [`lookup` function](https://helm.sh/docs/chart_template_guide/function_list/#lookup)
in your templates to get existing objects in your live cluster.

Note that the lookup function is executed in both the preview and the non-preview mode, and keep in mind that
the expected object may not exist during a preview.

### Improved resource ordering

It's now easy to wait for a chart's resources to be installed before installing other resources,
simply by using the `dependsOn` option. In earlier versions, we relied on a `ready` output property.

The Chart resource automatically detects dependencies between resources in the manifest(s).
For example, it knows to install namespaces and Custom Resource Definitions (CRDs) first.

Use the `config.kubernetes.io/depends-on` annotation to declare an explicit resource dependency.
The annotation accepts a list of resource references, delimited by commas.

It consists of the group, kind, name, and optionally the namespace, delimited by forward slashes.

| Resource Scope   | Format                                         |
| :--------------- | :--------------------------------------------- |
| namespace-scoped | `<group>/namespaces/<namespace>/<kind>/<name>` |
| cluster-scoped   | `<group>/<kind>/<name>`                        |

For resources in the “core” group, the empty string is used instead (for example: `/namespaces/test/Pod/pod-a`).

### New-style Pulumi transformations

Pulumi has a new way to transform component resources and their children, the `transforms`  options. The older
`transformations` option doesn't work with multi-language components like Chart v4. See
[Resource Option: transforms](/docs/concepts/options/transforms/) for more details.

Note: you cannot change an object's namespace or name using a Pulumi transformation, and you cannot add or discard
an object.

Here's an example of using the `transforms` option to add the `pulumi.com/patchForce` annotation
to a chart's resources.

{{< chooser language "typescript,python,go" >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const applyPatchForceAnnotation = async (args: pulumi.ResourceTransformArgs) => {
    switch(args.type) {
        case "kubernetes:helm.sh/v4:Chart":
            break;
        default:
            args.props.metadata.annotations = {
                "pulumi.com/patchForce": "true",
                ...args.props.metadata.annotations
            }
    }
    return {
        props: args.props,
        opts: args.opts,
    };
};

const ingressController = new kubernetes.helm.v4.Chart("ingresscontroller", {
    chart: "nginx-ingress",
    namespace: ingressNs.metadata.name,
    repositoryOpts: {
        repo: "https://helm.nginx.com/stable",
    },
    version: "0.14.1",
}, {transforms: [applyPatchForceAnnotation]});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
def apply_patchforce_annotation(args: ResourceTransformArgs):
    if not args.type_ == "kubernetes:helm.sh/v4:Chart":
        if not 'metadata' in args.props:
            args.props['metadata'] = {}
        if not 'annotations' in args.props['metadata']:
            args.props['metadata']['annotations'] = {}
        args.props['metadata']['annotations']['pulumi.com/patchForce'] = 'true'

    return ResourceTransformResult(
        props=args.props,
        opts=args.opts)

ingresscontroller = kubernetes.helm.v4.Chart(
    "ingresscontroller",
    chart="nginx-ingress",
    namespace=ingress_ns.metadata.name,
    repository_opts=kubernetes.helm.v3.RepositoryOptsArgs(
        repo="https://helm.nginx.com/stable",
    ),
    version="0.14.1",
    opts=pulumi.ResourceOptions(transforms=[apply_patchforce_annotation])
)
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
applyPatchForceAnnotation := func(ctx context.Context, rta *pulumi.ResourceTransformArgs) *pulumi.ResourceTransformResult {
	transform := func(applier interface{}) {
		o := rta.Props.ToMapOutputWithContext(ctx).ApplyT(applier)
		r, err := internals.UnsafeAwaitOutput(ctx, o)
		if err != nil {
			panic(err)
		}
		rta.Props = r.Value.(pulumi.Map)
	}

	switch rta.Type {
	case "kubernetes:helm.sh/v4:Chart":
		// Do nothing for Helm charts
	default:
		transform(func(obj map[string]any) pulumi.Map {
			// note: obj is an ordinary Unstructured object at this point.
			unstructured.SetNestedField(obj, "true", "metadata", "annotations", "pulumi.com/patchForce")
			return pulumi.ToMap(obj)
		})
	}
	return &pulumi.ResourceTransformResult{
		Props: rta.Props,
		Opts:  rta.Opts,
	}
}

// Use Helm to install the Nginx ingress controller
_, err = helmv4.NewChart(ctx, "ingresscontroller", &helmv4.ChartArgs{
	Chart:     pulumi.String("nginx-ingress"),
	Namespace: ingressNs.Metadata.Name(),
	RepositoryOpts: &helmv4.RepositoryOptsArgs{
		Repo: pulumi.String("https://helm.nginx.com/stable"),
	},
	Version: pulumi.String("0.14.1"),
}, pulumi.Transforms([]pulumi.ResourceTransform{applyPatchForceAnnotation}))
if err != nil {
	return err
}
```

{{% /choosable %}}

{{< /chooser >}}

### Post-rendering support

New to v4 is support for a post-rendering command, with optional arguments, to be applied to the rendered manifest.
See [Advanced Helm Techniques: Post Rendering](https://helm.sh/docs/topics/advanced/#post-rendering) for details.

### "Keep" policy

The Chart v4 resource now understands Helm resource policies, specifically "keep" which instructs Pulumi
not to delete a given object when the resource is destroyed. Simply apply the `helm.sh/resource-policy: keep` annotation
to the object. See [Tell Helm Not To Uninstall a Resource](https://helm.sh/docs/howto/charts_tips_and_tricks/#tell-helm-not-to-uninstall-a-resource)
for details.

### Release name

Charts typically generate object names based on the Helm release name. By default, Chart v4 uses its own resource name
as the release name. To customize the release name, set the `name` property on the `Chart`.

Some charts also accept a `fullnameOverride` value to control object naming, use that if possible.

## Limitations

### Not supported: Kubernetes transformations

Chart v4 does not support the `transformations` argument as seen in Chart v3, that facilitates a
Kubernetes-centric transformation and/or discarding of objects from the rendered manifest.

One alternative is to use use Pulumi transformations to transform the object and resource options.
Another is to use post-rendering, which we'll cover next.

### Not supported: Helm hooks

Some charts use hooks to perform pre- and post-installation tasks, and we recommend using the `Release` resource
to install such charts. Another option is to emulate the hook by performing the task directly, using other Pulumi resources
such as [kubernetes.batch/v1.Job](/registry/packages/kubernetes/api-docs/batch/v1/job/) and
[kubernetes.core/v1.Secret](/registry/packages/kubernetes/api-docs/core/v1/secret/).

Note that Chart v3 does not support hooks either but, for historical reasons, does emit the hooks as ordinary
child resources.

### Evolving: Resource outputs

The child resources created by the chart are presented to your program via the `resources` output, as an array
of Pulumi Resource objects. In some SDKs, you can cast the resource into the appropriate resource type,
e.g. `corev1.ConfigMap`. Not all SDKs support this (yet); see [pulumi/pulumi#15788](https://github.com/pulumi/pulumi/issues/15788).

## Example: Argo CD

Here's a real-world example of installing [Argo CD](https://argoproj.github.io/cd/) into a Kubernetes cluster,
and of using Argo CD's `Application` custom resource to deploy the 'guestbook' example.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";
import * as random from "@pulumi/random";

const ns = new kubernetes.core.v1.Namespace("ns", {metadata: {
    name: "argocd",
}});
const redisPasswordResource = new random.RandomPassword("redis-password", {length: 16});
const redisSecret = new kubernetes.core.v1.Secret("redis-secret", {
    metadata: {
        name: "argocd-redis",
        namespace: ns.metadata.apply(metadata => metadata.name),
    },
    type: "Opaque",
    stringData: {
        auth: redisPasswordResource.result,
    },
});
const argocd = new kubernetes.helm.v4.Chart("argocd", {
    chart: "argo-cd",
    version: "6.11.1",
    namespace: ns.metadata.apply(metadata => metadata.name),
    repositoryOpts: {
        repo: "https://argoproj.github.io/argo-helm",
    },
    values: {
        fullnameOverride: "",
    },
});
const guestbook = new kubernetes.yaml.v2.ConfigGroup("guestbook", {objs: [{
    apiVersion: "argoproj.io/v1alpha1",
    kind: "Application",
    metadata: {
        name: "guestbook",
        namespace: ns.metadata.apply(metadata => metadata.name),
    },
    spec: {
        project: "default",
        source: {
            repoURL: "https://github.com/argoproj/argocd-example-apps.git",
            targetRevision: "HEAD",
            path: "guestbook",
        },
        destination: {
            server: "https://kubernetes.default.svc",
            namespace: "default",
        },
    },
}]}, {
    dependsOn: [argocd],
});
export const redisPassword = redisPasswordResource.result;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_kubernetes as kubernetes
import pulumi_random as random

ns = kubernetes.core.v1.Namespace("ns", metadata=kubernetes.meta.v1.ObjectMetaArgs(
    name="argocd",
))
redis_password_resource = random.RandomPassword("redis-password", length=16)
redis_secret = kubernetes.core.v1.Secret("redis-secret",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        name="argocd-redis",
        namespace=ns.metadata.name,
    ),
    type="Opaque",
    string_data={
        "auth": redis_password_resource.result,
    })
argocd = kubernetes.helm.v4.Chart("argocd",
    chart="argo-cd",
    version="6.11.1",
    namespace=ns.metadata.name,
    repository_opts=kubernetes.helm.v4.RepositoryOptsArgs(
        repo="https://argoproj.github.io/argo-helm",
    ),
    values={
        "fullnameOverride": "",
    })
guestbook = kubernetes.yaml.v2.ConfigGroup("guestbook", objs=[{
    "apiVersion": "argoproj.io/v1alpha1",
    "kind": "Application",
    "metadata": {
        "name": "guestbook",
        "namespace": ns.metadata.name,
    },
    "spec": {
        "project": "default",
        "source": {
            "repoURL": "https://github.com/argoproj/argocd-example-apps.git",
            "targetRevision": "HEAD",
            "path": "guestbook",
        },
        "destination": {
            "server": "https://kubernetes.default.svc",
            "namespace": "default",
        },
    },
}],
opts=pulumi.ResourceOptions(depends_on=[argocd]))
pulumi.export("redisPassword", redis_password_resource.result)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	helmv4 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v4"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	yamlv2 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/yaml/v2"
	"github.com/pulumi/pulumi-random/sdk/v4/go/random"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		ns, err := corev1.NewNamespace(ctx, "ns", &corev1.NamespaceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("argocd"),
			},
		})
		if err != nil {
			return err
		}
		redisPasswordResource, err := random.NewRandomPassword(ctx, "redis-password", &random.RandomPasswordArgs{
			Length: pulumi.Int(16),
		})
		if err != nil {
			return err
		}
		_, err = corev1.NewSecret(ctx, "redis-secret", &corev1.SecretArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("argocd-redis"),
				Namespace: ns.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
					return metadata.Name, nil
				}).(pulumi.StringPtrOutput),
			},
			Type: pulumi.String("Opaque"),
			StringData: pulumi.StringMap{
				"auth": redisPasswordResource.Result,
			},
		})
		if err != nil {
			return err
		}
		argocd, err := helmv4.NewChart(ctx, "argocd", &helmv4.ChartArgs{
			Chart:   pulumi.String("argo-cd"),
			Version: pulumi.String("6.11.1"),
			Namespace: ns.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
				return metadata.Name, nil
			}).(pulumi.StringPtrOutput),
			RepositoryOpts: &helmv4.RepositoryOptsArgs{
				Repo: pulumi.String("https://argoproj.github.io/argo-helm"),
			},
			Values: pulumi.Map{
				"fullnameOverride": pulumi.Any(""),
			},
		})
		if err != nil {
			return err
		}
		_, err = yamlv2.NewConfigGroup(ctx, "guestbook", &yamlv2.ConfigGroupArgs{
			Objs: pulumi.Array{
				pulumi.Any(map[string]interface{}{
					"apiVersion": "argoproj.io/v1alpha1",
					"kind":       "Application",
					"metadata": map[string]interface{}{
						"name": "guestbook",
						"namespace": ns.Metadata.ApplyT(func(metadata metav1.ObjectMeta) (*string, error) {
							return metadata.Name, nil
						}).(pulumi.StringPtrOutput),
					},
					"spec": map[string]interface{}{
						"project": "default",
						"source": map[string]interface{}{
							"repoURL":        "https://github.com/argoproj/argocd-example-apps.git",
							"targetRevision": "HEAD",
							"path":           "guestbook",
						},
						"destination": map[string]interface{}{
							"server":    "https://kubernetes.default.svc",
							"namespace": "default",
						},
					},
				}),
			},
		}, pulumi.DependsOn([]pulumi.Resource{
			argocd,
		}))
		if err != nil {
			return err
		}
		ctx.Export("redisPassword", redisPasswordResource.Result)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Kubernetes = Pulumi.Kubernetes;
using Random = Pulumi.Random;

return await Deployment.RunAsync(() =>
{
    var ns = new Kubernetes.Core.V1.Namespace("ns", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Name = "argocd",
        },
    });

    var redisPasswordResource = new Random.RandomPassword("redis-password", new()
    {
        Length = 16,
    });

    var redisSecret = new Kubernetes.Core.V1.Secret("redis-secret", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Name = "argocd-redis",
            Namespace = ns.Metadata.Apply(metadata => metadata.Name),
        },
        Type = "Opaque",
        StringData =
        {
            { "auth", redisPasswordResource.Result },
        },
    });

    var argocd = new Kubernetes.Helm.V4.Chart("argocd", new()
    {
        Chart = "argo-cd",
        Version = "6.11.1",
        Namespace = ns.Metadata.Apply(metadata => metadata.Name),
        RepositoryOpts = new Kubernetes.Types.Inputs.Helm.V4.RepositoryOptsArgs
        {
            Repo = "https://argoproj.github.io/argo-helm",
        },
        Values =
        {
            { "fullnameOverride", "" },
        },
    });

    var guestbook = new Kubernetes.Yaml.V2.ConfigGroup("guestbook", new()
    {
        Objs = new[]
        {
            new Dictionary<string, object?>
            {
                ["apiVersion"] = "argoproj.io/v1alpha1",
                ["kind"] = "Application",
                ["metadata"] = new Dictionary<string, object?>
                {
                    ["name"] = "guestbook",
                    ["namespace"] = ns.Metadata.Apply(metadata => metadata.Name),
                },
                ["spec"] = new Dictionary<string, object?>
                {
                    ["project"] = "default",
                    ["source"] = new Dictionary<string, object?>
                    {
                        ["repoURL"] = "https://github.com/argoproj/argocd-example-apps.git",
                        ["targetRevision"] = "HEAD",
                        ["path"] = "guestbook",
                    },
                    ["destination"] = new Dictionary<string, object?>
                    {
                        ["server"] = "https://kubernetes.default.svc",
                        ["namespace"] = "default",
                    },
                },
            },
        },
    }, new ComponentResourceOptions
    {
        DependsOn =
        {
            argocd,
        },
    });

    return new Dictionary<string, object?>
    {
        ["redisPassword"] = redisPasswordResource.Result,
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.kubernetes.core.v1.Namespace;
import com.pulumi.kubernetes.core.v1.NamespaceArgs;
import com.pulumi.kubernetes.meta.v1.inputs.ObjectMetaArgs;
import com.pulumi.random.RandomPassword;
import com.pulumi.random.RandomPasswordArgs;
import com.pulumi.kubernetes.core.v1.Secret;
import com.pulumi.kubernetes.core.v1.SecretArgs;
import com.pulumi.kubernetes.helm.v4.Chart;
import com.pulumi.kubernetes.helm.v4.ChartArgs;
import com.pulumi.kubernetes.helm.v4.inputs.RepositoryOptsArgs;
import com.pulumi.kubernetes.yaml.v2.ConfigGroup;
import com.pulumi.kubernetes.yaml.v2.ConfigGroupArgs;
import com.pulumi.resources.ComponentResourceOptions;
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
        var ns = new Namespace("ns", NamespaceArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .name("argocd")
                .build())
            .build());

        var redisPasswordResource = new RandomPassword("redisPasswordResource", RandomPasswordArgs.builder()
            .length(16)
            .build());

        var redisSecret = new Secret("redisSecret", SecretArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .name("argocd-redis")
                .namespace(ns.metadata().applyValue(metadata -> metadata.name().get()))
                .build())
            .type("Opaque")
            .stringData(redisPasswordResource.result().applyValue(password -> Map.of("auth", password)))
            .build());

        var argocd = new Chart("argocd", ChartArgs.builder()
            .chart("argo-cd")
            .version("6.11.1")
            .namespace(ns.metadata().applyValue(metadata -> metadata.name().get()))
            .repositoryOpts(RepositoryOptsArgs.builder()
                .repo("https://argoproj.github.io/argo-helm")
                .build())
            .values(Map.of("fullnameOverride", ""))
            .build());

        var guestbook = new ConfigGroup("guestbook", ConfigGroupArgs.builder()
            .objs(Map.ofEntries(
                Map.entry("apiVersion", "argoproj.io/v1alpha1"),
                Map.entry("kind", "Application"),
                Map.entry("metadata", Map.ofEntries(
                    Map.entry("name", "guestbook"),
                    Map.entry("namespace", ns.metadata().applyValue(metadata -> metadata.name().get()))
                )),
                Map.entry("spec", Map.ofEntries(
                    Map.entry("project", "default"),
                    Map.entry("source", Map.ofEntries(
                        Map.entry("repoURL", "https://github.com/argoproj/argocd-example-apps.git"),
                        Map.entry("targetRevision", "HEAD"),
                        Map.entry("path", "guestbook")
                    )),
                    Map.entry("destination", Map.ofEntries(
                        Map.entry("server", "https://kubernetes.default.svc"),
                        Map.entry("namespace", "default")
                    ))
                ))
            ))
            .build(), ComponentResourceOptions.builder()
                .dependsOn(argocd)
                .build());

        ctx.export("redisPassword", redisPasswordResource.result());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  ns:
    type: kubernetes:core/v1:Namespace
    properties:
      metadata:
        name: argocd

  redis-password:
    type: random:RandomPassword
    properties:
      length: 16

  redis-secret:
    type: kubernetes:core/v1:Secret
    properties:
      metadata:
        name: argocd-redis
        namespace: ${ns.metadata.name}
      type: Opaque
      stringData:
        auth: ${redis-password.result}
    options:
      retainOnDelete: true

  argocd:
    type: kubernetes:helm.sh/v4:Chart
    properties:
      chart: argo-cd
      version: "6.11.1"
      namespace: ${ns.metadata.name}
      repositoryOpts:
        repo: https://argoproj.github.io/argo-helm
      values:
        fullnameOverride: ""

  guestbook:
    type: kubernetes:yaml/v2:ConfigGroup
    properties:
      objs:
      - apiVersion: argoproj.io/v1alpha1
        kind: Application
        metadata:
          name: guestbook
          namespace: ${ns.metadata.name}
        spec:
          project: default
          source:
            repoURL: https://github.com/argoproj/argocd-example-apps.git
            targetRevision: HEAD
            path: guestbook
          destination:
            server: https://kubernetes.default.svc
            namespace: default
    options:
      dependsOn:
      - ${argocd}

outputs:
  redisPassword: ${redis-password.result}
```

{{% /choosable %}}

{{< /chooser >}}

The program creates the `argocd` namespace, installs the ArgoCD server, and then creates an ArgoCD `Application` resource.
Observe how the program installs and uses a Custom Resource Definition (CRD) successfully, and uses `dependsOn`
to ensure that the CRD is installed before using it.

The `argo-cd` chart normally makes use of a Helm hook to initialize a password for the redis server.
Since the Chart v4 resource doesn't support Helm hooks, this program creates the password directly.

## Conclusion

Pulumi loves empowering developers to use the best tools for the job, and we recommend using Helm charts to install
third-party Kubernetes applications. Pulumi complements Helm by handling the cloud resources that are often required,
such as an IAM Role or cloud storage bucket. Such combinations make for great reusable componentry.

Check out the following links to learn more about Pulumi Kubernetes today!

- [Getting Started](/docs/iac/get-started/kubernetes/)
- [Documentation](/docs/clouds/kubernetes/)
- [Open Source](https://github.com/pulumi/pulumi-kubernetes)
- [Community Slack](https://slack.pulumi.com/)
