---
title_tag: "Migrating from Kubernetes YAML or Helm Charts"
meta_desc: Migrate your existing Kubernetes YAML or Helm Charts and/or coexist with existing templates.
title: Kubernetes YAML & Helm Charts
h1: Migrating from Kubernetes YAML or Helm Charts to Pulumi
menu:
    iac:
        name: Kubernetes YAML or Helm Charts
        parent: iac-guides-migration-from
        weight: 5
aliases:
- /docs/guides/adopting/from_kubernetes/
- /docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-kubernetes/
- /docs/iac/adopting-pulumi/migrating-to-pulumi/from-kubernetes/
---

<img src="/logos/tech/k8s.svg" align="right" class="h-16 px-8 pb-4">

Pulumi lets you author your Kubernetes configuration in your choice of language, as well as reuse existing Kubernetes and Helm YAML configuration files. This enables you to write, rewrite, or reuse existing Kubernetes configuration, or even take a hybrid approach, while still standardizing on Pulumi for deployment orchestration. It's common, for example, to have Helm charts deployed in Pulumi alongside natively defined object configurations.

Pulumi also enables you to render the Kubernetes objects in your program into YAML which eases adoption in the opposite direction: you can use Pulumi to author your configuration, getting the benefits of general-purpose and familiar programming languages, while still being able to deploy the resulting YAML with existing toolchains like `kubectl` or your CI/CD vendor's Kubernetes support.

> To learn more about Pulumi's Kubernetes support, see [the Kubernetes Overview](/registry/packages/kubernetes/) or jump straight in with [the Getting Started Guide](/docs/iac/get-started/kubernetes/).

## Deploying Kubernetes YAML

The Kubernetes package provides the `yaml` module which defines two resource types:

* `ConfigFile`: deploy a single Kubernetes YAML file
* `ConfigGroup`: deploy a collection of Kubernetes YAML files together

By defining these resources in code, you can deploy off-the-shelf Kubernetes YAML files without needing to change them. Pulumi understands the full topology of resource objects inside those YAML files. The examples below show how to do both &mdash; first a single YAML file and then a group of them &mdash; using the standard [Kubernetes Guestbook Application](https://github.com/kubernetes/examples/tree/master/web/guestbook).

### Deploying a single Kubernetes YAML file

The `ConfigFile` resource type accepts a `file` parameter that indicates the path or URL to read the YAML configuration from. By default, the auto-generated resource names are prefixed with the name of the `ConfigFile`, however you can specify a `resourcePrefix` to use a different prefix. One or more `transforms` callbacks can be supplied via `ResourceOptions` to arbitrarily rewrite resource configurations on-the-fly before deploying them.

To deploy the Kubernetes Guestbook Application using a single YAML file, first download the "all-in-one" configuration:

```bash
$ curl -L --remote-name \
    https://raw.githubusercontent.com/kubernetes/examples/master/web/guestbook/all-in-one/guestbook-all-in-one.yaml
```

The guestbook's `redis-master` Deployment uses the `registry.k8s.io/redis:e2e` image, which has a Docker schema 1 manifest that containerd 2.1 and later can no longer pull. Switch it to the official `redis` image, as the comment in the file suggests:

```bash
$ sed -i.bak 's|registry.k8s.io/redis:e2e|redis|' guestbook-all-in-one.yaml
```

This Pulumi program uses `ConfigFile` to read that YAML file and provision the resources inside it:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

const guestbook = new k8s.yaml.v2.ConfigFile("guestbook", {
    file: "guestbook-all-in-one.yaml",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi_kubernetes.yaml.v2 import ConfigFile

guestbook = ConfigFile("guestbook", file="guestbook-all-in-one.yaml")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    yamlv2 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/yaml/v2"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        _, err := yamlv2.NewConfigFile(ctx, "guestbook", &yamlv2.ConfigFileArgs{
            File: pulumi.String("guestbook-all-in-one.yaml"),
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
using System.Threading.Tasks;

using Pulumi.Kubernetes.Yaml.V2;
using Pulumi.Kubernetes.Types.Inputs.Yaml.V2;

class Program
{
    static Task<int> Main()
    {
        return Pulumi.Deployment.RunAsync(() =>
        {
            var guestbook = new ConfigFile("guestbook", new ConfigFileArgs
            {
                File = "guestbook-all-in-one.yaml",
            });
        });
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.kubernetes.yaml.v2.ConfigFile;
import com.pulumi.kubernetes.yaml.v2.ConfigFileArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var guestbook = new ConfigFile("guestbook",
            ConfigFileArgs.builder()
                .file("guestbook-all-in-one.yaml")
                .build());
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  guestbook:
    type: kubernetes:yaml/v2:ConfigFile
    properties:
      file: guestbook-all-in-one.yaml
```

{{% /choosable %}}

{{% choosable language hcl %}}

```hcl
terraform {
  required_providers {
    kubernetes = {
      source  = "pulumi/kubernetes"
      version = "4.23.0"
    }
  }
}

resource "kubernetes_yaml_v2_config_file" "guestbook" {
  file = "guestbook-all-in-one.yaml"
}
```

{{% /choosable %}}

{{< /chooser >}}

Running `pulumi up` deploys the resources:

```bash
Updating (dev):

     Type                                 Name                             Status
 +   pulumi:pulumi:Stack                  pulumi-k8s-test-dev              created
 +   └─ kubernetes:yaml/v2:ConfigFile     guestbook                        created
 +      ├─ kubernetes:apps/v1:Deployment  guestbook:default/redis-replica  created
 +      ├─ kubernetes:apps/v1:Deployment  guestbook:default/frontend       created
 +      ├─ kubernetes:core/v1:Service     guestbook:default/redis-replica  created
 +      ├─ kubernetes:core/v1:Service     guestbook:default/redis-master   created
 +      ├─ kubernetes:core/v1:Service     guestbook:default/frontend       created
 +      └─ kubernetes:apps/v1:Deployment  guestbook:default/redis-master   created

Resources:
    + 8 created
```

`ConfigFile` exposes the objects it creates through its `resources` output, but it doesn't provide a way to look up a single object by kind and name. To find a value that Kubernetes assigns at deploy time, like the frontend service's cluster IP address, query the cluster with `kubectl`:

```bash
$ kubectl get service frontend
NAME       TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
frontend   NodePort   10.107.35.136   <none>        80:31533/TCP   10s
```

### Deploying multiple Kubernetes YAML files

The `ConfigGroup` resource type works like `ConfigFile`. Instead of a single file, it accepts a `files` parameter that contains a list of file paths, file globs, and/or URLs from which to read the YAML configuration from. By default, the auto-generated resource names are prefixed with the name of the `ConfigGroup`, however you can specify a `resourcePrefix` to use a different prefix. One or more `transforms` callbacks can be supplied via `ResourceOptions` to arbitrarily rewrite resource configurations on-the-fly before deploying them.

To deploy the Kubernetes Guestbook Application using a collection of YAML files, first create a `yaml` directory and download them into it:

```bash
$ mkdir yaml
$ pushd yaml
$ curl -L --remote-name \
    "https://raw.githubusercontent.com/kubernetes/examples/master/web/guestbook/{frontend-deployment,frontend-service,redis-master-deployment,redis-master-service,redis-replica-deployment,redis-replica-service}.yaml"
$ popd
```

As with the single file, switch the `redis-master` Deployment to the official `redis` image:

```bash
$ sed -i.bak 's|registry.k8s.io/redis:e2e|redis|' yaml/redis-master-deployment.yaml
```

This Pulumi program uses `ConfigGroup` to read these YAML files and provision the resources inside of them:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";
import * as path from "path";

const guestbook = new k8s.yaml.v2.ConfigGroup("guestbook", {
    files: [ path.join("yaml", "*.yaml") ],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi_kubernetes.yaml.v2 import ConfigGroup

guestbook = ConfigGroup("guestbook", files=["yaml/*.yaml"])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "path/filepath"

    yamlv2 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/yaml/v2"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        _, err := yamlv2.NewConfigGroup(ctx, "guestbook", &yamlv2.ConfigGroupArgs{
            Files: pulumi.StringArray{pulumi.String(filepath.Join("yaml", "*.yaml"))},
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
using System.IO;
using System.Threading.Tasks;

using Pulumi.Kubernetes.Yaml.V2;
using Pulumi.Kubernetes.Types.Inputs.Yaml.V2;

class Program
{
    static Task<int> Main()
    {
        return Pulumi.Deployment.RunAsync(() =>
        {
            var guestbook = new ConfigGroup("guestbook", new ConfigGroupArgs
            {
                Files = { Path.Combine("yaml", "*.yaml") },
            });
        });
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.kubernetes.yaml.v2.ConfigGroup;
import com.pulumi.kubernetes.yaml.v2.ConfigGroupArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var guestbook = new ConfigGroup("guestbook",
            ConfigGroupArgs.builder()
                .files("yaml/*.yaml")
                .build());
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  guestbook:
    type: kubernetes:yaml/v2:ConfigGroup
    properties:
      files:
      - "yaml/*.yaml"
```

{{% /choosable %}}

{{% choosable language hcl %}}

```hcl
terraform {
  required_providers {
    kubernetes = {
      source  = "pulumi/kubernetes"
      version = "4.23.0"
    }
  }
}

resource "kubernetes_yaml_v2_config_group" "guestbook" {
  files = ["yaml/*.yaml"]
}
```

{{% /choosable %}}

{{< /chooser >}}

Running `pulumi up` deploys the resources in every YAML file:

```bash
Updating (dev):

     Type                                 Name                             Status
 +   pulumi:pulumi:Stack                  pulumi-k8s-test-dev              created
 +   └─ kubernetes:yaml/v2:ConfigGroup    guestbook                        created
 +      ├─ kubernetes:core/v1:Service     guestbook:default/redis-replica  created
 +      ├─ kubernetes:apps/v1:Deployment  guestbook:default/redis-master   created
 +      ├─ kubernetes:apps/v1:Deployment  guestbook:default/redis-replica  created
 +      ├─ kubernetes:apps/v1:Deployment  guestbook:default/frontend       created
 +      ├─ kubernetes:core/v1:Service     guestbook:default/frontend       created
 +      └─ kubernetes:core/v1:Service     guestbook:default/redis-master   created

Resources:
    + 8 created
```

## Deploying Helm charts

<img src="/logos/tech/helm.svg" align="right" class="h-32 px-8 pb-4">

Pulumi supports two distinct means of using Helm charts:

1. [Emulating Helm charts to render resource templates](#emulating-helm-charts-with-chart-resources)
1. [Natively installing Helm charts as Releases](#natively-installing-helm-charts-as-releases)

We discuss and provide examples for each approach in this section.

### Emulating Helm charts with Chart resources

With the [Helm V3](/registry/packages/kubernetes/api-docs/helm/v3/chart/) chart resources, Pulumi renders the templates and applies them directly, much like with `ConfigFile` and `ConfigGroup` shown earlier, which means all provisioning happens client-side using your Kubernetes authentication setup without needing a server-side component.

The `Chart` resource type provides options to control where to fetch the chart's contents from. This includes:

* `chart`: The required chart name (for instance, `"wordpress"`).
* `repo`: (Optional) The helm repository to pull the chart from (e.g., `"stable"`).
* `path`: (Optional) A path to a chart stored locally on your filesystem.
* `version`: (Optional) The semantic chart version to pull (by default `"latest"`).
* `values`: (Optional) A dictionary of named key/value values for Charts with parameters.
* `fetchOpts`: (Optional) A bag of options to control the fetch behavior.

Beyond those core options, you can specify `transformations` (like the [configurations below](#configuration-transformations)), `resourcePrefix` to control naming, or `namespace` to place all resources inside a specific Kubernetes namespace. Please refer to the [API reference](/registry/packages/kubernetes/api-docs/helm/v3/chart/) documentation for more details.

#### Provisioning a Helm chart

To provision a Helm chart with Pulumi, deploy the `wordpress` chart from `https://charts.bitnami.com/bitnami`. This stands up a fully functional WordPress instance that uses MariaDB:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

// Deploy the latest version of the bitnami/wordpress chart.
const wordpress = new k8s.helm.v3.Chart("wpdev", {
    fetchOpts: {
        repo: "https://charts.bitnami.com/bitnami"
    },
    chart: "wordpress",
});

// Export the public IP for WordPress.
const frontend = wordpress.getResource("v1/Service", "default/wpdev-wordpress");
export const frontendIp = frontend.status.loadBalancer.ingress[0].ip;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts

# Deploy the latest version of the bitnami/wordpress chart.
wordpress = Chart('wpdev', ChartOpts(
    fetch_opts={'repo': 'https://charts.bitnami.com/bitnami'},
    chart='wordpress',
))

# Export the public IP for WordPress.
frontend = wordpress.get_resource('v1/Service', 'default/wpdev-wordpress')
pulumi.export('frontend_ip', frontend.status.load_balancer.ingress[0].ip)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
    helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/helm/v3"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Deploy the latest version of the bitnami/wordpress chart.
        wordpress, err := helmv3.NewChart(ctx, "wpdev", helmv3.ChartArgs{
            Chart:   pulumi.String("wordpress"),
            FetchArgs: helmv3.FetchArgs{
                Repo: pulumi.String(`https://charts.bitnami.com/bitnami`),
            },
        })
        if err != nil {
            return err
        }

        // Export the public IP for WordPress.
        frontendIP := wordpress.GetResource("v1/Service", "default/wpdev-wordpress", "").Apply(func(r interface{}) (interface{}, error) {
            svc := r.(*corev1.Service)
            return svc.Status.LoadBalancer().Ingress().Index(pulumi.Int(0)).Ip(), nil
        })
        ctx.Export("frontendIp", frontendIP)

        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;

using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Helm;
using Pulumi.Kubernetes.Helm.V3;

class Program
{
    static Task<int> Main()
    {
        return Pulumi.Deployment.RunAsync(() =>
        {

            // Deploy the latest version of the bitnami/wordpress chart.
            var wordpress = new Chart("wpdev", new ChartArgs
            {
                Chart = "wordpress",
                FetchOptions = new ChartFetchArgs
                {
                    Repo = "https://charts.bitnami.com/bitnami"
                }
            });

            // Export the public IP for WordPress.
            var frontend = wordpress.GetResource<Service>("default/wpdev-wordpress");
            return new Dictionary<string, object?>
            {
                { "frontendIp", frontend.Apply(fe => fe.Status.Apply(status => status.LoadBalancer.Ingress[0].Ip)) },
            };
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Unlike the `ConfigFile` and `ConfigGroup` resource types shown above, the Helm V3 `Chart` makes all provisioned resources available via the `getResource` function.

After running `pulumi up`, we will see the resulting resources created, and the load balanced IP address will be printed:

```
Updating (dev):
     Type                                         Name                      Status
 +   pulumi:pulumi:Stack                          k8s-helm-dev              created
 +   └─ kubernetes:helm.sh/v3:Chart               wpdev                     created
 +      ├─ kubernetes:core:Secret                 wpdev-wordpress           created
 +      ├─ kubernetes:core:Secret                 wpdev-mariadb             created
 +      ├─ kubernetes:core:ConfigMap              wpdev-mariadb-tests       created
 +      ├─ kubernetes:core:ConfigMap              wpdev-mariadb             created
 +      ├─ kubernetes:core:PersistentVolumeClaim  wpdev-wordpress           created
 +      ├─ kubernetes:core:Service                wpdev-wordpress           created
 +      ├─ kubernetes:core:Service                wpdev-mariadb             created
 +      ├─ kubernetes:core:Pod                    wpdev-credentials-test    created
 +      ├─ kubernetes:core:Pod                    wpdev-mariadb-test-zbeq0  created
 +      ├─ kubernetes:apps:Deployment             wpdev-wordpress           created
 +      └─ kubernetes:apps:StatefulSet            wpdev-mariadb             created

Outputs:
    frontendIp: "34.71.25.45"

Resources:
    + 13 created
```

We can easily curl our new WordPress website:

```bash
$ curl http://$(pulumi stack output frontendIp)
<!DOCTYPE html>
<html lang="en-US" class="no-js no-svg">
<head>
<title>User's Blog! -- Just another WordPress site</title>
...
```

### Natively installing Helm charts as Releases

The [Helm Release](/registry/packages/kubernetes/api-docs/helm/v3/release/) resource (GA as of [v3.15.0](https://github.com/pulumi/pulumi-kubernetes/releases/tag/v3.15.0) of the Pulumi Kubernetes Provider) is another option for installing Charts. In this case, the Pulumi Kubernetes provider uses an embedded version of the Helm SDK to provide full-fidelity support for managing [`Helm Releases`](https://helm.sh/docs/glossary/#release).

The `Release` resource type's inputs closely mirror the options supported by the Helm CLI and deviate slightly from the API supported by the `Chart` resources. Some key options are highlighted here:

* `chart`: The required chart name (for instance, `"wordpress"`). For a local helm chart, a path can be specified instead.
* `repositoryOpts`: (Optional) Options to configure URL and authentication/authorization information for the hosting Helm repository, if any.
* `version`: (Optional) The semantic chart version to pull (by default `"latest"`).
* `values`: (Optional) A dictionary of named key/value pairs for Charts with parameters.
* `skipAwait`: (Optional) Whether to skip waiting on the availability of all resources installed by the chart. By default, this is set to `false` (i.e. awaits all resources) which allows us to chain dependent resources and execution to the `Release` resource.
* `timeout`: (Optional) When `skipAwait` is `false`, the amount of time to wait on resources being available. If the timeout expires, the release is marked as `failed`.

For more details on all the supported inputs, please refer to the [API reference documentation](/registry/packages/kubernetes/api-docs/helm/v3/release/#inputs).

Unlike `Chart` resource types, `Release` doesn't include references to the underlying Kubernetes resources created during the installation. As a result, only the `Release` resource is stored in Pulumi state by default. The `Release` resource type includes the [`ReleaseStatus`](/registry/packages/kubernetes/api-docs/helm/v3/release/#releasestatus) as an output type. The following example shows how to retrieve resources managed by a Release.

#### Installing a Helm Release

To illustrate provisioning a Helm chart using the `Release` resource, we will deploy the same `wordpress` chart as we did earlier:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

// Deploy the bitnami/wordpress chart.
const wordpress = new k8s.helm.v3.Release("wpdev", {
    chart: "wordpress",
    repositoryOpts: {
        repo: "https://charts.bitnami.com/bitnami",
    },
});

// Get the status field from the wordpress service, and then grab a reference to the spec.
const svc = k8s.core.v1.Service.get("wpdev-wordpress", pulumi.interpolate`${wordpress.status.namespace}/${wordpress.status.name}-wordpress`);
// Export the ingress IP for the wordpress frontend.
export const frontendIp = svc.status.loadBalancer.ingress[0].ip;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi import Output
from pulumi_kubernetes.core.v1 import Service
from pulumi_kubernetes.helm.v3 import Release, ReleaseArgs, RepositoryOptsArgs

# Deploy the bitnami/wordpress chart.
wordpress = Release(
    "wpdev",
    ReleaseArgs(
        chart="wordpress",
        repository_opts=RepositoryOptsArgs(
            repo="https://charts.bitnami.com/bitnami",
        ),
    ),
)

srv = Service.get("wpdev-wordpress", Output.concat(wordpress.status.namespace, "/", wordpress.status.name, "-wordpress"))
# Export the ingress IP for WordPress frontend.
pulumi.export("frontendIP", srv.status.load_balancer.ingress[0].ip)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"fmt"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/helm/v3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Deploy the bitnami/wordpress chart.
		wordpress, err := helm.NewRelease(ctx, "wpdev", &helm.ReleaseArgs{
			Chart:   pulumi.String("wordpress"),
			RepositoryOpts: &helm.RepositoryOptsArgs{
				Repo: pulumi.String("https://charts.bitnami.com/bitnami"),
			},
		})

        // Export the ingress IP for WordPress frontend.
		frontendIp := pulumi.All(wordpress.Status.Namespace(), wordpress.Status.Name()).ApplyT(func(r interface{})(interface{}, error){
			arr := r.([]interface{})
			namespace := arr[0].(*string)
			name := arr[1].(*string)
			svc, err := corev1.GetService(ctx, "svc", pulumi.ID(fmt.Sprintf("%s/%s-wordpress", *namespace, *name)), nil)
			if err != nil {
				return "", nil
			}
			return svc.Status.LoadBalancer().Ingress().Index(pulumi.Int(0)).Ip(), nil

		})
		ctx.Export("frontendIp", frontendIp)

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
using Pulumi.Kubernetes.Core.V1;
using System.Collections.Generic;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Helm.V3;

class MyStack : Stack
{
    public MyStack()
    {
        // Deploy the bitnami/wordpress chart.
        var wordpress = new Release("wpdev", new ReleaseArgs
        {
            Chart = "wordpress",
            RepositoryOpts = new RepositoryOptsArgs
            {
                Repo = "https://charts.bitnami.com/bitnami"
            },
        });

        // Get the status field from the wordpress service, and then grab a reference to the spec.
        var status = wordpress.Status;
        var service = Service.Get("wpdev-wordpress", Output.All(status).Apply(
            s => $"{s[0].Namespace}/{s[0].Name}-wordpress"));
        // Export the ingress IP for WordPress frontend.
        this.FrontendIP = service.Status.Apply(status => status.LoadBalancer.Ingress[0].Ip);
    }

    [Output]
    public Output<string> FrontendIP { get; set; }
}
```

{{% /choosable %}}

{{< /chooser >}}
After running `pulumi up`, we will see the resulting resources created, and the load balanced IP address will be printed:

```
Updating (dev)

     Type                              Name                                      Status
 +   pulumi:pulumi:Stack               <project/stack>                           created
 +   ├─ kubernetes:helm.sh/v3:Release  wpdev                                     created
     └─ kubernetes:core/v1:Service     wpdev-wordpress

Outputs:
    frontendIp        : "34.71.25.45"

Resources:
    + 2 created

Duration: 1m28s
```

We can now use the Helm CLI to confirm that a release has been created:

```
helm list -a
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
wpdev-xxxxxxxx  default         1               2022-02-01 01:06:08.513501 -0800 PST    deployed        wordpress-....
```

The Helm Release resource also supports importing existing Helm releases by using the `pulumi import` command.

## Converting Kubernetes YAML

In addition to deploying Kubernetes YAML via the methods above, you can also convert Kubernetes YAML to Pulumi program code using `pulumi convert --from kubernetes --language <language> --out <output_dir>`. The converter will take your YAML manifest and
convert it into your preferred language within the designated output directory. For more information about this plugin, please visit the [official repository](https://github.com/pulumi/pulumi-converter-kubernetes).

## Rendering Kubernetes YAML

While Pulumi has excellent support for deploying and updating Kubernetes resources on a cluster, Pulumi also offers the ability to render YAML to make it easier to integrate into existing workflows. This gives you the ability to author Kubernetes configuration using general-purpose programming languages, consume libraries, and easily mix in infrastructure configuration (e.g., managed database endpoints, object storage, etc.), all in the same program.

To render YAML during a `pulumi up` rather than have Pulumi perform the deployment against your cluster as it does by default, set the `renderYamlToDirectory` property on [an explicit Kubernetes provider](/docs/iac/concepts/providers/#default-and-explicit-providers) object.

This example provisions a simple load-balanced NGINX service using a general purpose language but renders the output to YAML:

{{< chooser language "typescript,python,go,csharp,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

// Instantiate a Kubernetes Provider and specify the render directory.
const renderProvider = new k8s.Provider("k8s-yaml-renderer", {
    renderYamlToDirectory: "yaml",
});

// Create an NGINX Deployment and load-balanced Service that use it.
const labels = { "app": "nginx" };
const dep = new k8s.apps.v1.Deployment("nginx-dep", {
    spec: {
        selector: { matchLabels: labels },
        replicas: 1,
        template: {
            metadata: { labels: labels },
            spec: { containers: [{ name: "nginx", image: "nginx" }] },
        },
    },
}, { provider: renderProvider });
const svc = new k8s.core.v1.Service("nginx-svc", {
    spec: {
        type: "LoadBalancer",
        selector: labels,
        ports: [{ port: 80 }],
    },
}, { provider: renderProvider });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi import ResourceOptions
from pulumi_kubernetes import Provider
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service

# Instantiate a Kubernetes Provider and specify the render directory.
render_provider = Provider('k8s-yaml-renderer',
    render_yaml_to_directory='yaml')

# Create an NGINX Deployment and load-balanced Service that use it.
labels = { 'app': 'nginx' }
dep = Deployment('nginx-dep',
    spec={
        'selector': { 'matchLabels': labels },
        'replicas': 1,
        'template': {
            'metadata': { 'labels': labels },
            'spec': { 'containers': [{ 'name': 'nginx', 'image': 'nginx' }] },
        },
    }, opts=ResourceOptions(provider=render_provider)
)
svc = Service('nginx-svc',
    spec={
        'type': 'LoadBalancer',
        'selector': labels,
        'ports': [{'port': 80}],
    }, opts=ResourceOptions(provider=render_provider)
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
    appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1"
    corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
    metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        renderProvider, err := kubernetes.NewProvider(ctx, "k8s-yaml-renderer", &kubernetes.ProviderArgs{
            RenderYamlToDirectory: pulumi.String("yaml"),
        })
        if err != nil {
            return err
        }

        labels := pulumi.StringMap{"app": pulumi.String("nginx")}

        _, err = appsv1.NewDeployment(ctx, "nginx-dep", &appsv1.DeploymentArgs{
            Spec: &appsv1.DeploymentSpecArgs{
                Selector: &metav1.LabelSelectorArgs{MatchLabels: labels},
                Replicas: pulumi.Int(1),
                Template: corev1.PodTemplateSpecArgs{
                    Metadata: metav1.ObjectMetaArgs{Labels: labels},
                    Spec: &corev1.PodSpecArgs{
                        Containers: &corev1.ContainerArray{
                            &corev1.ContainerArgs{
                                Name:  pulumi.String("nginx"),
                                Image: pulumi.String("nginx"),
                            },
                        },
                    },
                },
            },
        }, pulumi.Provider(renderProvider))
        if err != nil {
            return err
        }
        _, err = corev1.NewService(ctx, "nginx-svc", &corev1.ServiceArgs{
            Spec: &corev1.ServiceSpecArgs{
                Type:     pulumi.String("LoadBalancer"),
                Selector: labels,
                Ports:    corev1.ServicePortArray{corev1.ServicePortArgs{Port: pulumi.Int(80)}},
            },
        }, pulumi.Provider(renderProvider))
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
using System.Collections.Immutable;
using System.Threading.Tasks;

using Pulumi.Kubernetes;
using Pulumi.Kubernetes.Apps.V1;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;

class Program
{
    static Task<int> Main()
    {
        return Pulumi.Deployment.RunAsync(() =>
        {
            // Instantiate a Kubernetes Provider and specify the render directory.
            var renderProvider = new Provider("k8s-yaml-renderer", new ProviderArgs
            {
                RenderYamlToDirectory = "yaml",
            });

            // Create an NGINX Deployment and load-balanced Service that use it.
            var labels = new Dictionary<string, string> { { "app", "nginx" } }.ToImmutableDictionary();
            var dep = new Deployment("nginx-dep",
                new DeploymentArgs
                {
                    Spec = new DeploymentSpecArgs
                    {
                        Selector = new LabelSelectorArgs { MatchLabels = labels },
                        Replicas = 1,
                        Template = new PodTemplateSpecArgs
                        {
                            Metadata = new ObjectMetaArgs { Labels = labels },
                            Spec = new PodSpecArgs
                            {
                                Containers =
                                {
                                    new ContainerArgs
                                    {
                                        Name = "nginx",
                                        Image = "nginx",
                                    },
                                },
                            },
                        },
                    },
                },
                new Pulumi.CustomResourceOptions { Provider = renderProvider }
            );
            var svc = new Service("nginx-svc",
                new ServiceArgs
                {
                    Spec = new ServiceSpecArgs
                    {
                        Type = "LoadBalancer",
                        Selector = labels,
                        Ports =
                        {
                            new ServicePortArgs { Port = 80 },
                        },
                    },
                },
                new Pulumi.CustomResourceOptions { Provider = renderProvider }
            );
        });
    }
}
```

{{% /choosable %}}

{{% choosable language hcl %}}

```hcl
terraform {
  required_providers {
    kubernetes = {
      source  = "pulumi/kubernetes"
      version = "4.23.0"
    }
  }
}

# Instantiate a Kubernetes provider and specify the render directory.
provider "kubernetes" {
  alias                    = "k8s-yaml-renderer"
  render_yaml_to_directory = "yaml"
}

locals {
  labels = { app = "nginx" }
}

# Create an NGINX Deployment and load-balanced Service that use it.
resource "kubernetes_apps_v1_deployment" "nginx-dep" {
  provider = kubernetes.k8s-yaml-renderer

  spec = {
    selector = { match_labels = local.labels }
    replicas = 1
    template = {
      metadata = { labels = local.labels }
      spec = {
        containers = [{
          name  = "nginx"
          image = "nginx"
        }]
      }
    }
  }
}

resource "kubernetes_core_v1_service" "nginx-svc" {
  provider = kubernetes.k8s-yaml-renderer

  metadata = { labels = local.labels }

  spec = {
    type     = "LoadBalancer"
    ports    = [{ port = 80, target_port = 80, protocol = "TCP" }]
    selector = local.labels
  }
}
```

Property names are snake_case in HCL and are translated to the provider's camelCase, so `match_labels` and `target_port` reach the API as `matchLabels` and `targetPort`.

{{% /choosable %}}

{{< /chooser >}}

Next, just run `pulumi up`:

```bash
$ pulumi up
Updating (dev):
     Type                              Name               Status
 +   pulumi:pulumi:Stack               k8s-render-dev     created
 +   ├─ pulumi:providers:kubernetes    k8s-yaml-renderer  created
 +   ├─ kubernetes:core/v1:Service     nginx-svc          created
 +   └─ kubernetes:apps/v1:Deployment  nginx-dep          created

Resources:
    + 4 created

Duration: 2s
```

Instead of deploying these resources, the target YAML directory, `yaml/`, will have been created and populated with the resulting YAML files:

```bash
$ tree yaml
yaml
├── 0-crd
└── 1-manifest
    ├── deployment-nginx-dep-xj8peqh3.yaml
    └── service-nginx-svc-nsnetbz3.yaml

2 directories, 2 files
```

These are typically YAML configuration files, so you can now do whatever you'd like with them, such as applying them with `kubectl apply -f ...`. Note that CustomResourceDefinition resources need to be applied first, so they are rendered in a separate subdirectory. (This example doesn’t include any CRDs, so the directory is empty). You could deploy the rendered manifests with kubectl like this:

```bash
$ kubectl apply -f "yaml/0-crd"
$ kubectl apply -f "yaml/1-manifest"
```

There are two important caveats to note about YAML rendering support:

* The YAML-rendered resources are not created on a Kubernetes cluster, so information that is computed server-side will not be available in your program. For example, a Service will not have IP assignments, so attempting to export these values will not work as usual (i.e., the value will be undefined).
* Any Secret values will appear in plaintext in the rendered manifests. This includes any values marked as secret in Pulumi. A warning will be printed for any secret values being rendered to YAML, but it is your responsibility to protect the rendered files.

## Configuration transformations

Let's see how to assign our service a public IP address, starting with [the single `ConfigFile` example above](#deploying-a-single-kubernetes-yaml-file), using transforms.

The Kubernetes Guestbook by default does not assign a load balancer for the frontend service. To fix this, we could edit the YAML file, but let's see `transforms` in action instead. By supplying a `transforms` callback in the resource options, we can rewrite the object configuration on the fly and cause a load balancer to get created:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

const guestbook = new k8s.yaml.v2.ConfigFile("guestbook", {
    file: "guestbook-all-in-one.yaml",
}, {
    transforms: [
        async (args) => {
            if (args.type === "kubernetes:core/v1:Service" &&
                    (args.props as any)?.metadata?.name === "frontend") {
                const props = args.props as any;
                props.spec = { ...props.spec, type: "LoadBalancer" };
                return { props, opts: args.opts };
            }
            return undefined;
        },
    ],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi_kubernetes.yaml.v2 import ConfigFile

def make_frontend_public(args):
    if (args.type_ == "kubernetes:core/v1:Service" and
            args.props.get("metadata", {}).get("name") == "frontend"):
        props = dict(args.props)
        spec = dict(props.get("spec", {}))
        spec["type"] = "LoadBalancer"
        props["spec"] = spec
        return pulumi.ResourceTransformResult(props=props, opts=args.opts)

guestbook = ConfigFile("guestbook",
    file="guestbook-all-in-one.yaml",
    opts=pulumi.ResourceOptions(transforms=[make_frontend_public]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "context"

    yamlv2 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/yaml/v2"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        _, err := yamlv2.NewConfigFile(ctx, "guestbook", &yamlv2.ConfigFileArgs{
            File: pulumi.String("guestbook-all-in-one.yaml"),
        }, pulumi.Transforms([]pulumi.ResourceTransform{
            func(_ context.Context, args *pulumi.ResourceTransformArgs) *pulumi.ResourceTransformResult {
                if args.Type == "kubernetes:core/v1:Service" {
                    meta, _ := args.Props["metadata"].(pulumi.Map)
                    spec, ok := args.Props["spec"].(pulumi.Map)
                    if ok && meta["name"] == pulumi.String("frontend") {
                        spec["type"] = pulumi.String("LoadBalancer")
                        return &pulumi.ResourceTransformResult{
                            Props: args.Props,
                            Opts:  args.Opts,
                        }
                    }
                }
                return nil
            },
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
using System.Collections.Immutable;
using System.Threading.Tasks;

using Pulumi;
using Pulumi.Kubernetes.Yaml.V2;
using Pulumi.Kubernetes.Types.Inputs.Yaml.V2;

class Program
{
    static Task<int> Main()
    {
        return Pulumi.Deployment.RunAsync(() =>
        {
            var guestbook = new ConfigFile("guestbook", new ConfigFileArgs
            {
                File = "guestbook-all-in-one.yaml",
            }, new ComponentResourceOptions
            {
                ResourceTransforms =
                {
                    (args, _) =>
                    {
                        if (args.Type == "kubernetes:core/v1:Service"
                            && args.Args.GetValueOrDefault("metadata") is ImmutableDictionary<string, object?> meta
                            && meta.GetValueOrDefault("name") is "frontend"
                            && args.Args.GetValueOrDefault("spec") is ImmutableDictionary<string, object?> spec)
                        {
                            var props = args.Args.SetItem("spec", spec.SetItem("type", "LoadBalancer"));
                            return Task.FromResult<ResourceTransformResult?>(new ResourceTransformResult(props, args.Options));
                        }
                        return Task.FromResult<ResourceTransformResult?>(null);
                    },
                },
            });
        });
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}
{{% notes type="info" %}}
Transforms are not yet supported for the `ConfigFile` resource in Java.
{{% /notes %}}
{{% /choosable %}}
{{% choosable language yaml %}}
{{% notes type="info" %}}
Transforms are not yet supported for the `ConfigFile` resource in Pulumi YAML.
{{% /notes %}}
{{% /choosable %}}

{{< /chooser >}}

After running `pulumi up`, we will see the `frontend` service updated to a load balancer:

```bash
$ pulumi up
Updating (dev):
     Type                              Name                        Status   Info
     pulumi:pulumi:Stack               pulumi-k8s-test-dev
     └─ kubernetes:yaml/v2:ConfigFile  guestbook
 ~      └─ kubernetes:core/v1:Service  guestbook:default/frontend  updated  [diff: ~spec]

Resources:
    ~ 1 updated
    7 unchanged
```

Once the load balancer is ready, `kubectl` shows its external IP address:

```bash
$ kubectl get service frontend
NAME       TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
frontend   LoadBalancer   10.107.35.136   127.0.0.1     80:31533/TCP   24s
```

On minikube, `minikube tunnel` assigns `127.0.0.1` as the external IP address. Some providers, like AWS, report a hostname instead of an IP address; on those clusters, replace `ip` with `hostname` in the `jsonpath` expression below.

Afterwards, we can `curl` that address and see the Guestbook page:

```bash
$ curl http://$(kubectl get service frontend -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
<html ng-app="redis">
  <head>
    <title>Guestbook</title>
  ...
</html>
```

Although this example shows the YAML `ConfigFile` resource, the same transform behavior is available with YAML `ConfigGroup` and Helm `Chart` resource types.

## Provisioning mixed configurations

You can provision a combination of native Kubernetes objects, YAML files, Helm charts, and other cloud resources all together, with dependencies between them. For an example of doing so, see [this blog post](/blog/using-helm-and-pulumi-to-define-cloud-native-infrastructure-as-code/) which demonstrates provisioning an Azure Kubernetes cluster, MongoDB-flavored CosmosDB instance, a Kubernetes secret to store the connection information, and a Helm chart that consumes this secret and connects to the CosmosDB database.
