---
title: "New: Helm Chart resource for Java, YAML SDKs"
date: 2024-04-12T00:00:00-07:00
meta_image: meta.png
meta_desc: >-
  Pulumi Kubernetes v4.13 offers a new resource for applying Helm charts consistently across Pulumi SDKs, and broadens support to the Java and YAML SDKs.

authors:
    - eron-wright

tags:
    - kubernetes
    - yaml
    - java
    - helm
---

When you need to install a third-party application into your Kubernetes cluster, you're likely to find a
Helm chart for that in [Artifact Hub](https://artifacthub.io/) or other registry. Pulumi provides two
ways to apply a Helm chart, as outlined in [Choosing the Right Helm Resource For Your Use Case](/registry/packages/kubernetes/how-to-guides/choosing-the-right-helm-resource-for-your-use-case/).  The Chart resource offers deeper integration with Pulumi
and better drift remediation.

Today we're happy to announce a new "v4" version of the Chart resource, available now in v4.13 of the Pulumi Kubernetes provider.
The new Chart v4 resource is provided side-by-side with the existing Chart v3 resource.

## What's New
Let's look at what's new with Chart v4.

### New SDK Support - Java SDK & YAML SDK

The "v4" Chart resource is a multi-language Pulumi Component (MLC) that works consistently across all Pulumi SDKs.
We expect that having a unified implementation, as is now possible with MLC technology, will lead to fewer issues
and broader support.

Here, for example, is a simple deployment of [cert-manager](https://cert-manager.io/), a well-known Kubernetes add-on:

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language yaml %}}

```yaml
  certman:
    type: kubernetes:helm.sh/v4:Chart
    properties:
      namespace: cert-manager
      chart: oci://registry-1.docker.io/bitnamicharts/cert-manager
      version: "1.3.1"
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

const certman = new kubernetes.helm.v4.Chart("certman", {
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

certman = kubernetes.helm.v4.Chart("certman",
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
		_, err := helmv4.NewChart(ctx, "certman", &helmv4.ChartArgs{
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
    var certman = new Kubernetes.Helm.V4.Chart("certman", new()
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
        var certman = new Chart("certman", ChartArgs.builder()
            .namespace("cert-manager")
            .chart("oci://registry-1.docker.io/bitnamicharts/cert-manager")
            .version("1.3.1")
            .build());

    }
}
```

{{% /choosable %}}

{{% /chooser %}}

### OCI Registry Support

You can use container registries with OCI support such as [Docker Hub](https://hub.docker.com/) to store and share 
Helm chart packages. The "v4" Chart resource now has full support for OCI, bringing it to parity with
the Release resource.

To use an authenticated OCI registry, you must first login using `helm registry login` or `docker login`.

The "v4" Chart also supports the use of [Helm chart repositories](https://helm.sh/docs/topics/chart_repository/),
and adopts the same `repositoryOpts` API as was introduced in the Release resource.

### Lock File Support

Helm has support for lock files (Chart.lock) to control a chart's dependencies. When deploying a chart from a local directory,
Pulumi automatically rebuilds the chart's dependencies if a lock file is present. See
[Helm Dependency Build](https://helm.sh/docs/helm/helm_dependency_build/) for details.

### Better Handling of Chart Values

Chart "v4" offers new ways to work with Chart values. It is now possible to use multiple values files and to use
[Pulumi Assets](/docs/concepts/assets-archives/#assets). Of course you can also use output values from other
resources as chart values.

It is also possible to set a chart value to the contents of a text file, similarly to using Helm's `--set-file` argument.
To do that, simply use a Pulumi Asset as a value within the `values` map.

### Better Connectivity

You may now use chart functions that require a connection to the cluster, e.g. to:
- Check the Kubernetes server version with [`.Capabilities.KubeVersion`](https://helm.sh/docs/chart_template_guide/builtin_objects/)
- Check if an API version or kind is available with [`.Capabilities.APIVersions.Has`](https://helm.sh/docs/chart_template_guide/function_list/#capabilitiesapiversionshas)
- Use the [`lookup` function](https://helm.sh/docs/chart_template_guide/function_list/#lookup)
in your templates to get existing objects in your live cluster.

Note that the lookup function is executed in both the preview and the non-preview mode, and keep in mind that
the expected object may not exist during a preview.

### Resource Ordering

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

### New-Style Pulumi Transformations

Pulumi has a new way to transform component resources and their children, the `transforms`  options. The older
`transformations` option doesn't work with multi-language components like Chart "v4". See
[Resource Option: transforms](content/docs/concepts/options/transforms.md) for more details.

Note: you cannot change an object's namespace or name using a Pulumi transformation, and you cannot add or discard
an object.

Here's an example of using the `transforms` option to add the `pulumi.com/patchForce` annotation
to a chart's resources.

```ts
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

### Not Supported: Kubernetes Transformations

The "v4" resource does not support the `transformations` argument of Chart "v3", which facilitates a
Kubernetes-centric transformation and/or discarding of objects from the rendered manifest. 

One alternative is to use use Pulumi transformations to transform the object and resource options.
Another is to use post-rendering, which we'll cover next.

### Post-Rendering Support

New to "v4" is support for a post-rendering command, with optional arguments, to be applied to the rendered manifest.
See [Advanced Helm Techniques: Post Rendering](https://helm.sh/docs/topics/advanced/#post-rendering) for details.

### "Keep" Policy

The Chart "v4" resource now understands Helm resource policies, specifically "keep" which instructs Pulumi
not to delete a given object when the resource is destroyed. Simply apply the `helm.sh/resource-policy: keep` annotation
to the object. See [Tell Helm Not To Uninstall a Resource](https://helm.sh/docs/howto/charts_tips_and_tricks/#tell-helm-not-to-uninstall-a-resource)
for details.

## Example: Argo CD

Here's a real-world example of installing ArgoCD into a Kubernetes cluster, and of using ArgoCD's `Application`
resource to deploy the 'guestbook' example.

```ts
import * as k8s from "@pulumi/kubernetes";
import * as random from "@pulumi/random";

const ns = new k8s.core.v1.Namespace("argo-cd", {
    metadata: {
        name: "argocd",
    },
});

// create a Secret containing the redis password, as is done with `argocd admin redis-initial-password`
const password = new random.RandomPassword("argo-cd-redis-password", {
    length: 16,
});
const redisSecret = new k8s.core.v1.Secret("argo-cd-redis-secret", {
    metadata: {
        name: "argocd-redis",
        namespace: ns.metadata.name,
    },
    type: "Opaque",
    stringData: {
        auth: password.result,
    },
}, {dependsOn: [ns], retainOnDelete: true});

// install the ArgoCD server
const argoChart = new k8s.helm.v4.Chart("argo-cd", {
    chart: "argo-cd",
    version: "6.11.1",
    namespace: ns.metadata.name,
    repositoryOpts: {
        repo: "https://argoproj.github.io/argo-helm",
    },
}, {dependsOn: [redisSecret]});

// deploy the guestbook using the Application resource
const guestbook = new k8s.apiextensions.CustomResource("guestbook", {
    apiVersion: "argoproj.io/v1alpha1",
    kind: "Application",
    metadata: {
        name: "guestbook",
        namespace: ns.metadata.name,
    },
    spec: {
        project: "default",
        source: {
            repoURL: "https://github.com/argoproj/argocd-example-apps.git",
            targetRevision: "HEAD",
            path: "guestbook",
        },
        "destination": {
            server: "https://kubernetes.default.svc",
            namespace: "default",
        }
    }
}, {dependsOn: [argoChart]});

export const redisPassword = password.result;
```

The program creates the `argocd` namespace, installs the ArgoCD server, and then creates an `Application`.
Observe how the program installs and uses a Custom Resource Definition (CRD) successfully, and uses `dependsOn`
to ensure that the CRD is installed first.

The `argo-cd` chart normally makes use of a Helm hook to initialize a password for the redis server. 
Since the Chart v4 resource doesn't support Helm hooks, this program creates the password directly.

## Conclusion

Pulumi loves empowering developers to use the best tools for the job, and we recommend using Helm charts to install
third-party Kubernetes applications. Pulumi complements Helm by handling the cloud resources that are often required,
such as an IAM Role or cloud storage bucket. Such combinations make for great reusable componentry.

This is part of a broad initiative to use Multi-Language Component (MLC) technology to offer a consistent experience
across the Pulumi SDKs. See [pulumi-kubernetes#1971](https://github.com/pulumi/pulumi-kubernetes/issues/1971) for details.

Check out the following links to learn more about Pulumi Kubernetes today!

* [Getting Started](/docs/clouds/kubernetes/get-started/)
* [Documentation](/docs/clouds/kubernetes/)
* [Open Source](https://github.com/pulumi/pulumi-kubernetes)
* [Community Slack](https://slack.pulumi.com/)
