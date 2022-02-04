---
title: "From Kubernetes YAML or Helm Charts"
meta_desc: Migrate your existing Kubernetes YAML or Helm Charts and/or coexist with existing templates.
menu:
  userguides:
    parent: adopting
    weight: 5
---

<img src="/logos/tech/k8s.svg" align="right" class="h-16 px-8 pb-4">

Pulumi makes it easy to author your Kubernetes configuration in your choice of language, as well as reuse existing Kubernetes and Helm YAML configuration files. This enables you to write, rewrite, or reuse existing Kubernetes configuration, or even take a hybrid approach, while still standardizing on Pulumi for deployment orchestration. It's common, for example, to have Helm charts deployed in Pulumi alongside natively defined object configurations.

Pulumi also enables you to render the Kubernetes objects in your program into YAML which eases adoption in the opposite direction: you can use Pulumi to author your configuration, getting the benefits of general-purpose and familiar programming languages, while still being able to deploy the resulting YAML with existing toolchains like `kubectl` or your CI/CD vendor's Kubernetes support.

> To learn more about Pulumi's Kubernetes support, see [the Kubernetes Overview]({{< relref "/registry/packages/kubernetes" >}}) or jump straight in with [the Getting Started Guide]({{< relref "/docs/get-started/kubernetes" >}}).

## Deploying Kubernetes YAML

The Kubernetes package provides the `yaml` module which defines two resource types:

* `ConfigFile`: deploy a single Kubernetes YAML file
* `ConfigGroup`: deploy a collection of Kubernetes YAML files together

By defining these resources in code, you can deploy off-the-shelf Kubernetes YAML files without needing to change them. Pulumi understands the full topology of resource objects inside of those YAML files. The examples below show how to do both &mdash; first a single YAML file and then a group of them &mdash; using the standard [Kubernetes Guestbook Application](https://github.com/kubernetes/examples/tree/master/guestbook).

### Deploying a Single Kubernetes YAML File

The `ConfigFile` resource type accepts a `file` parameter that indicates the path or URL to read the YAML configuration from. By default, names are used as-is, however you can specify a `namePrefix` to rewrite the names. One or more `transformations` callbacks can be supplied to arbitrarily rewrite resource configurations on-the-fly before deploying them.

To deploy the Kubernetes Guestbook Application using a single YAML file, first download the "all-in-one" configuration:

```bash
$ curl -L --remote-name \
    https://raw.githubusercontent.com/kubernetes/examples/master/guestbook/all-in-one/guestbook-all-in-one.yaml
```

This Pulumi program uses `ConfigFile` to read that YAML file, provision the resources inside of it, and export the resulting IP addresses:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let k8s = require("@pulumi/kubernetes");

// Create resources from standard Kubernetes guestbook YAML example.
let guestbook = new k8s.yaml.ConfigFile("guestbook", {
    file: "guestbook-all-in-one.yaml",
});

// Export the private cluster IP address of the frontend.
let frontend = guestbook.getResource("v1/Service", "frontend");
module.exports = {
    privateIp = frontend.spec.clusterIP,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create resources from standard Kubernetes guestbook YAML example.
const guestbook = new k8s.yaml.ConfigFile("guestbook", {
    file: "guestbook-all-in-one.yaml",
});

// Export the private cluster IP address of the frontend.
const frontend = guestbook.getResource("v1/Service", "frontend");
export const privateIp = frontend.spec.clusterIP;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_kubernetes as k8s

# Create resources from standard Kubernetes guestbook YAML example.
guestbook = k8s.yaml.ConfigFile('guestbook', 'guestbook-all-in-one.yaml')

# Export the private cluster IP address of the frontend.
frontend = guestbook.get_resource('v1/Service', 'frontend')
pulumi.export('private_ip', frontend.spec['cluster_ip'])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
    "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/yaml"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        guestbook, err := yaml.NewConfigFile(ctx, "guestbook", &yaml.ConfigFileArgs{
            File: "guestbook-all-in-one.yaml",
        })
        if err != nil {
            return err
        }

        // Export the private cluster IP address of the frontend.
        frontend := guestbook.GetResource("v1/Service", "frontend", "").(*corev1.Service)
        ctx.Export("privateIP", frontend.Spec.ClusterIP())

        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;

using Pulumi;
using Pulumi.Kubernetes.Yaml;
using Pulumi.Kubernetes.Core.V1;

class Program
{
    static Task<int> Main()
    {
        return Pulumi.Deployment.RunAsync(() =>
        {
            // Create resources from standard Kubernetes guestbook YAML example.
            var guestbook = new ConfigFile("guestbook", new ConfigFileArgs
            {
                File = "guestbook-all-in-one.yaml",
            });

            // Export the private cluster IP address of the frontend.
            var frontend = guestbook.GetResource<Service>("frontend");
            return new Dictionary<string, object?>
            {
                { "privateIp", frontend.Apply(fe => fe.Spec.Apply(spec => spec.ClusterIP)) },
            };
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

As we can see here, the `getResource` function lets us retrieve an internal resource by type and name, so that we can interact with its properties. These will be strongly typed based on the resource type. Be careful using this, of course, as it makes your code subject to the internal implementation details of the YAML configuration &mdash; however, it's often necessary to find the information you need, like the auto-assigned IP addresses.

Running `pulumi up` will deploy the resources and then export the resulting frontend service's auto-assigned cluster IP address:

```bash
Updating (dev):
     Type                              Name          Status
 +   pulumi:pulumi:Stack               k8s-yaml-dev  created
 +   └─ kubernetes:yaml:ConfigFile     guestbook     created
 +      ├─ kubernetes:core:Service     redis-master  created
 +      ├─ kubernetes:core:Service     frontend      created
 +      ├─ kubernetes:apps:Deployment  frontend      created
 +      ├─ kubernetes:core:Service     redis-slave   created
 +      ├─ kubernetes:apps:Deployment  redis-master  created
 +      └─ kubernetes:apps:Deployment  redis-slave   created

Outputs:
    privateIp: "10.52.254.168"

Resources:
    + 8 created
```

### Deploying Multiple Kubernetes YAML Files

The `ConfigGroup` resource type is similar to `ConfigFile`. Instead of a single file, it accepts a `files` parameter that contains a list of file paths, file globs, and/or URLs from which to read the YAML configuration from. By default, names are used as-is, however you can specify a `namePrefix` to rewrite the names. One or more `transformations` callbacks can be supplied to arbitrarily rewrite resource configurations on-the-fly before deploying them.

To deploy the Kubernetes Guestbook Application using a colllection of YAML files, first create a `yaml` directory and download them into it:

```bash
$ mkdir yaml
$ pushd yaml
$ curl -L --remote-name \
    "https://raw.githubusercontent.com/kubernetes/examples/master/guestbook/{frontend-deployment,frontend-service,redis-master-deployment,redis-master-service,redis-slave-deployment,redis-slave-service}.yaml"
$ popd
```

This Pulumi program uses `ConfigGroup` to read these YAML files, provision the resources inside of them, and export the resulting IP addresses:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let k8s = require("@pulumi/kubernetes");
let path = require("path");

// Create resources from standard Kubernetes guestbook YAML example.
let guestbook = new k8s.yaml.ConfigGroup("guestbook", {
    files: [ path.join("yaml", "*.yaml") ],
});

// Export the private cluster IP address of the frontend.
let frontend = guestbook.getResource("v1/Service", "frontend");
module.exports = {
    privateIp = frontend.spec.clusterIP,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";
import * as path from "path";

// Create resources from standard Kubernetes guestbook YAML example.
const guestbook = new k8s.yaml.ConfigGroup("guestbook", {
    files: [ path.join("yaml", "*.yaml") ],
});

// Export the private cluster IP address of the frontend.
const frontend = guestbook.getResource("v1/Service", "frontend");
export const privateIp = frontend.spec.clusterIP;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi_kubernetes.yaml import ConfigGroup
from pulumi import export

# Create resources from standard Kubernetes guestbook YAML example.
guestbook = ConfigGroup(
  "guestbook",
  files=["yaml/*.yaml"])

# Export the private cluster IP address of the frontend.
frontend = guestbook.get_resource("v1/Service", "frontend")
export(
  name="privateIp",
  value=frontend.spec.cluster_ip)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "path/filepath"

    corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
    "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/yaml"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        guestbook, err := yaml.NewConfigGroup(ctx, "guestbook", &yaml.ConfigGroupArgs{
            Files: []string{filepath.Join("yaml", "*.yaml")},
        })
        if err != nil {
            return err
        }

        // Export the private cluster IP address of the frontend.
        frontend := guestbook.GetResource("v1/Service", "frontend", "").(*corev1.Service)
        ctx.Export("privateIP", frontend.Spec.ClusterIP())

        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.IO;
using System.Threading.Tasks;

using Pulumi;
using Pulumi.Kubernetes.Yaml;
using Pulumi.Kubernetes.Core.V1;

class Program
{
    static Task<int> Main()
    {
        return Pulumi.Deployment.RunAsync(() =>
        {
            // Create resources from standard Kubernetes guestbook YAML example.
            var guestbook = new ConfigGroup("guestbook", new ConfigGroupArgs
            {
                Files = { Path.Combine("yaml", "*.yaml") },
            });

            // Export the private cluster IP address of the frontend.
            var frontend = guestbook.GetResource<Service>("frontend");
            return new Dictionary<string, object?>
            {
                { "privateIp", frontend.Apply(fe => fe.Spec.Apply(spec => spec.ClusterIP)) },
            };
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Running `pulumi up` will deploy all of the resources in all of the YAML files and then export the resulting frontend service's auto-assigned cluster IP address:

```bash
Updating (dev):
     Type                                 Name                               Status
 +   pulumi:pulumi:Stack                  k8s-yaml-group-dev                 created
 +   └─ kubernetes:yaml:ConfigGroup       guestbook                          created
 +      ├─ kubernetes:yaml:ConfigFile     yaml/redis-slave-service.yaml      created
 +      │  └─ kubernetes:core:Service     redis-slave                        created
 +      ├─ kubernetes:yaml:ConfigFile     yaml/redis-master-service.yaml     created
 +      │  └─ kubernetes:core:Service     redis-master                       created
 +      ├─ kubernetes:yaml:ConfigFile     yaml/redis-master-deployment.yaml  created
 +      │  └─ kubernetes:apps:Deployment  redis-master                       created
 +      ├─ kubernetes:yaml:ConfigFile     yaml/frontend-deployment.yaml      created
 +      │  └─ kubernetes:apps:Deployment  frontend                           created
 +      ├─ kubernetes:yaml:ConfigFile     yaml/frontend-service.yaml         created
 +      │  └─ kubernetes:core:Service     frontend                           created
 +      └─ kubernetes:yaml:ConfigFile     yaml/redis-slave-deployment.yaml   created
 +         └─ kubernetes:apps:Deployment  redis-slave                        created

Outputs:
    privateIp: "10.51.254.33"

Resources:
    + 14 created
```

## Deploying Helm Charts

<img src="/logos/tech/helm.svg" align="right" class="h-32 px-8 pb-4">

Pulumi supports two distinct means of using Helm Charts:

1. [Emulating Helm Charts to render resource templates](#emulating-helm-charts-with-chart-resources)
2. [Natively installing Helm Charts as Releases](#natively-installing-helm-charts-as-releases)

We discuss and provide examples for each approach in this section.

### Emulating Helm Charts With Chart Resources

With the [Helm V3]({{< relref "/registry/packages/kubernetes/api-docs/helm/v3/release" >}}) chart resources, Pulumi renders the templates and applies them directly, much like with `ConfigFile` and `ConfigGroup` shown earlier, which means all provisioning happens client-side using your Kubernetes authentication setup without needing a server-side component.

The `Chart` resource type provides a number of options to control where to fetch the chart's contents from. This includes:

* `chart`: The required chart name (for instance, `"wordpress"`).
* `repo`: (Optional) The helm repository to pull the chart from (e.g., `"stable"`).
* `path`: (Optional) A path to a chart stored locally on your filesystem.
* `version`: (Optional) The semantic chart version to pull (by default `"latest"`).
* `values`: (Optional) A dictionary of named key/value values for Charts with parameters.
* `fetchOpts`: (Optional) A bag of options to control the fetch behavior.

In addition to those core options, you can specify `transformations` (similar to what is shown [configurations below](#configuration-transformations)), `namePrefix` to control naming, or `namespace` to place all resources inside of a specific Kubernetes namespace. Please refer to the [API reference]({{< relref "/registry/packages/kubernetes/api-docs/helm/v3/release" >}}) documentation for more details.

#### Provisioning a Helm Chart

To illustrate provisioning a Helm Chart using Pulumi, we will deploy the `wordpress` chart from `https://charts.bitnami.com/bitnami`. This will stand up a fully functional WordPress instance that uses MariaDB:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let k8s = require("@pulumi/kubernetes");

// Deploy v9.6.0 version of the wordpress chart.
let wordpress = new k8s.helm.v3.Chart("wpdev", {
    fetchOpts: {
        repo: "https://charts.bitnami.com/bitnami"
    },
    chart: "wordpress",
    version: "9.6.0",
});

// Export the public IP for WordPress.
let frontend = wordpress.getResource("v1/Service", "wpdev-wordpress");
module.exports = {
    frontendIp: frontend.status.loadBalancer.ingress[0].ip,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

// Deploy v9.6.0 version of the wordpress chart.
// Deploy the latest version of the stable/wordpress chart.
const wordpress = new k8s.helm.v3.Chart("wpdev", {
    fetchOpts: {
        repo: "https://charts.bitnami.com/bitnami"
    },
    chart: "wordpress",
    version: "9.6.0",
});

// Export the public IP for WordPress.
const frontend = wordpress.getResource("v1/Service", "wpdev-wordpress");
export const frontendIp = frontend.status.loadBalancer.ingress[0].ip;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts

# Deploy v9.6.0 version of the wordpress chart.
wordpress = Chart('wpdev', ChartOpts(
    fetch_opts={'repo': 'https://charts.bitnami.com/bitnami'},
    chart='wordpress',
    version='9.6.0',
))

# Export the public IP for WordPress.
frontend = wordpress.get_resource('v1/Service', 'wpdev-wordpress')
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
        // Deploy v9.6.0 version of the wordpress chart.
        wordpress, err := helmv3.NewChart(ctx, "wpdev", helmv3.ChartArgs{
            Chart:   pulumi.String("wordpress"),
            Version: pulumi.String("9.6.0"),
            FetchArgs: helmv3.FetchArgs{
                Repo: pulumi.String(`https://charts.bitnami.com/bitnami`),
            },
        })
        if err != nil {
            return err
        }

        // Export the public IP for WordPress.
        frontendIP := wordpress.GetResource("v1/Service", "wpdev-wordpress", "").Apply(func(r interface{}) (interface{}, error) {
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

            // Deploy v9.6.0 version of the wordpress chart.
            var wordpress = new Chart("wpdev", new ChartArgs
            {
                Chart = "wordpress",
                Version = "9.6.0",
                FetchOptions = new ChartFetchArgs
                {
                    Repo = "https://charts.bitnami.com/bitnami"
                }
            });

            // Export the public IP for WordPress.
            var frontend = wordpress.GetResource<Service>("wpdev-wordpress");
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

Similar to `ConfigFile` and `ConfigGroup` resource types shown above, all provisioned resources are available via the `getResource` function.

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

### Natively installing Helm Charts as Releases

The [Helm Release]({{< relref "/registry/packages/kubernetes/api-docs/helm/v3/release">}})) resource (GA as of [v3.15.0](https://github.com/pulumi/pulumi-kubernetes/releases/tag/v3.15.0) of the Pulumi Kubernetes Provider) is another option for installing Charts. In this case, the Pulumi Kubernetes provider uses an embedded version of the Helm SDK to provide full-fidelity support for managing [`Helm Releases`](https://helm.sh/docs/glossary/#release).

The `Release` resource type's inputs closely mirror the options supported by the Helm CLI and deviate slightly from the API supported by the `Chart` resources. Some key options are highlighted here:

* `chart`: The required chart name (for instance, `"wordpress"`). For a local helm chart, a path can be specified instead.
* `repositoryOpts`: (Optional) Options to configure URL and authentication/authorization information for the hosting Helm repository, if any.
* `version`: (Optional) The semantic chart version to pull (by default `"latest"`).
* `values`: (Optional) A dictionary of named key/value values for Charts with parameters.
* `skipAwait`: (Optional) Whether or not to skip waiting on the availability of all resources installed by the chart. By default, this is set to `false` (i.e. awaits all resources) which allows us to chain dependent resources and execution to the `Release` resource.
* `timeout`: (Optional) When `skipAwait` is `false`, the amount of time to wait on resources being available. If the timeout expires, the release is marked as `failed`.

For more details on all the supported inputs, please refer to the [API reference documentation]({{< relref "/registry/packages/kubernetes/api-docs/helm/v3/release/#inputs" >}}).

Unlike `Chart` resource types, `Release` doesn't include references to the underlying Kubernetes resources created during the installation. As a result, only the `Release` resource is stored in Pulumi state by default. The `Release` resource type includes the [`ReleaseStatus`]({{< relref "/registry/packages/kubernetes/api-docs/helm/v3/release/#releasestatus" >}}) as an output type. The following example shows how to retrieve resources managed by a Release.

#### Installing a Helm Release

To illustrate provisioning a Helm Chart using the `Release` resource, we will deploy the same `wordpress` chart as we did earlier:

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
    version: "9.6.0",
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
        version="9.6.0",
    ),
)

srv = Service.get("wpdev-wordpress", Output.concat(wordpress.status.namespace, "/", wordpress.status.name, "-wordpress"))
# Export the ingress IP for Wordpress frontend.
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
			Version: pulumi.String("9.6.0"),
			Chart:   pulumi.String("wordpress"),
			RepositoryOpts: &helm.RepositoryOptsArgs{
				Repo: pulumi.String("https://charts.bitnami.com/bitnami"),
			},
		})

        // Export the ingress IP for Wordpress frontend.
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
            Version = "9.6.0",
        });

        // Get the status field from the wordpress service, and then grab a reference to the spec.
        var status = wordpress.Status;
        var service = Service.Get("wpdev-wordpress", Output.All(status).Apply(
            s => $"{s[0].Namespace}/{s[0].Name}-wordpress"));
        // Export the ingress IP for Wordpress frontend.
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

In addition to deploying Kubernetes YAML via the methods above, you can also convert Kubernetes YAML to Pulumi program code using `kube2pulumi`. `kube2pulumi` will take your YAML manifest and
convert it into the language of your choice. You can get started using `kube2pulumi` either by [installing the binary](https://github.com/pulumi/kube2pulumi#building-and-installation) or via the [web interface]({{< relref "/kube2pulumi" >}}).

## Rendering Kubernetes YAML

While Pulumi has excellent support for deploying and updating Kubernetes resources on a cluster, Pulumi also offers the ability to render YAML to make it easier to integrate into existing workflows. This gives you the ability to author Kubernetes configuration using general-purpose programming languages, consume libraries, and easily mix in infrastructure configuration (e.g., managed database endpoints, object storage, etc.), all in the same program.

To render YAML during a `pulumi up` rather than have Pulumi perform the deployment against your cluster as it does by default, set the `renderYamlToDirectory` property on [an explicit Kubernetes provider]({{< relref "/docs/intro/concepts/resources#explicit-provider-configuration" >}}) object.

This example provisions a simple load-balanced NGINX service using a general purpose language but renders the output to YAML:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let k8s = require("@pulumi/kubernetes");

// Instantiate a Kubernetes Provider and specify the render directory.
let renderProvider = new k8s.Provider("k8s-yaml-renderer", {
    renderYamlToDirectory: "yaml",
});

// Create an NGINX Deployment and load-balanced Service that use it.
let labels = { "app": "nginx" };
let dep = new k8s.apps.v1.Deployment("nginx-dep", {
    spec: {
        selector: { matchLabels: labels },
        replicas: 1,
        template: {
            metadata: { labels: labels },
            spec: { containers: [{ name: "nginx", image: "nginx" }] },
        },
    },
}, { provider: renderProvider });
let svc = new k8s.core.v1.Service("nginx-svc", {
    spec: {
        type: "LoadBalancer",
        selector: labels,
        ports: [{ port: 80 }],
    },
}, { provider: renderProvider });
```

{{% /choosable %}}
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
render_provider = Provider('k8s-yaml-rendered',
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
    }, __opts__=ResourceOptions(provider=render_provider)
)
svc = Service('nginx-svc',
    spec={
        'type': 'LoadBalancer',
        'selector': labels,
        'ports': [{'port': 80}],
    }, __opts__=ResourceOptions(provider=render_provider)
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

{{< /chooser >}}

Next, just run `pulumi up`:

```bash
$ pulumi up
Updating (dev):
     Type                            Name               Status
 +   pulumi:pulumi:Stack             k8s-render-dev     created
 +   ├─ pulumi:providers:kubernetes  k8s-yaml-renderer  created
 +   ├─ kubernetes:core:Service      nginx-svc          created
 +   └─ kubernetes:apps:Deployment   nginx-dep          created

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

These are typically YAML configuration files so you can now do whatever you'd like with them, such as applying them with `kubectl apply -f ...`. Note that CustomResourceDefinition resources need to be applied first, so they are rendered in a separate subdirectory. (This example doesn’t include any CRDs, so the directory is empty). You could deploy the rendered manifests with kubectl like this:

```bash
$ kubectl apply -f "yaml/0-crd"
$ kubectl apply -f "yaml/1-manifest"
```

There are two important caveats to note about YAML rendering support:

* The YAML-rendered resources are not created on a Kubernetes cluster, so information that is computed server-side will not be available in your program. For example, a Service will not have IP assignments, so attempting to export these values will not work as usual (i.e., the value will be undefined).
* Any Secret values will appear in plaintext in the rendered manifests. This includes any values marked as secret in Pulumi. A warning will be printed for any secret values being rendered to YAML, but it is your responsibility to protect the rendered files.

## Configuration Transformations

Let's see how to assign our service a public IP address, starting with [the single `ConfigFile` example above](#deploying-a-single-kubernetes-yaml-file), using transformations.

The Kubernetes Guestbook by default does not assign a load balancer for the frontend service. To fix this, we could edit the YAML file, of course, but let's see `transformations` in action. By supplying the `transformations` callback that rewrites the object configuration on the fly, we can cause a load balancer to get created:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
...
let guestbook = new k8s.yaml.ConfigFile("guestbook", {
    file: "guestbook-all-in-one.yaml",
    transformations: [(obj: any) => {
        if (obj.kind === "Service" && obj.metadata.name === "frontend") {
            obj.spec.type = "LoadBalancer";
        }
    }],
});
...
module.exports = {
    privateIp = frontend.spec.clusterIP,
    publicIp = frontend.status.loadBalancer.ingress[0].ip,
};
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
...
const guestbook = new k8s.yaml.ConfigFile("guestbook", {
    file: "guestbook-all-in-one.yaml",
    transformations: [(obj: any) => {
        if (obj.kind === "Service" && obj.metadata.name === "frontend") {
            obj.spec.type = "LoadBalancer";
        }
    }],
});
...
export const publicIp = frontend.status.loadBalancer.ingress[0].ip;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
...
def make_frontend_public(obj):
    if obj['kind'] == "Service" and obj['metadata']['name'] == "frontend":
        obj['spec']['type'] = "LoadBalancer"
guestbook = k8s.yaml.ConfigFile('guestbook', 'guestbook-all-in-one.yaml',
    transformations=[make_frontend_public])
...
pulumi.export('public_ip', frontend.status['load_balancer']['ingress'][0]['ip'])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
...
guestbook, err := yaml.NewConfigFile(ctx, "guestbook", &yaml.ConfigFileArgs{
    File: "guestbook-all-in-one.yaml",
    Transformations: []yaml.Transformation{func(state map[string]interface{}, opts ...pulumi.ResourceOption) {
        if kind, ok := state["kind"]; ok && kind == "Service" && state["metadata"].(map[string]interface{})["name"] == "frontend" {
            state["spec"].(map[string]interface{})["type"] = "LoadBalancer"
        }
    }},
})
if err != nil {
    return err
}

// Export the private cluster IP address of the frontend.
frontend := guestbook.GetResource("v1/Service", "frontend", "").(*corev1.Service)
ctx.Export("privateIP", frontend.Spec.ClusterIP())
ctx.Export("publicIP", frontend.Status.LoadBalancer().Ingress().Index(pulumi.Int(0)).Ip())
...
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
...
Func<ImmutableDictionary<string, object>,
    CustomResourceOptions, ImmutableDictionary<string, object>>[] transformations =
{
    (obj, opts) => {
        if ((string)obj["kind"] == "Service" &&
                (string)((ImmutableDictionary<string, object>)obj["metadata"])["name"] == "frontend")
        {
            var spec = ((ImmutableDictionary<string, object>)obj["spec"]);
            obj = obj.SetItem("spec", spec.SetItem("type", "LoadBalancer"));
        }
        return obj;
    },
};
var guestbook = new ConfigFile("guestbook", new ConfigFileArgs
{
    File = "guestbook-all-in-one.yaml",
    Transformations = transformations,
});
...
return new Dictionary<string, object?>
{
    { "privateIp", frontend.Apply(fe => fe.Spec.Apply(spec => spec.ClusterIP)) },
    { "publicIp", frontend.Apply(fe => fe.Status.Apply(status => status.LoadBalancer.Ingress[0].Ip)) },
};
...
```

{{% /choosable %}}

{{< /chooser >}}

After running `pulumi up`, we will see the `frontend` service replaced and that a `publicIp` is now assigned:

```bash
$ pulumi up
Updating (dev):
     Type                           Name          Status       Info
     pulumi:pulumi:Stack            k8s-yaml-dev
     └─ kubernetes:yaml:ConfigFile  guestbook
 +-     └─ kubernetes:core:Service  frontend      replaced     [diff: ~spec]

Outputs:
  ~ privateIp: "10.52.254.168" => "10.51.244.125"
  + publicIp : "37.182.242.140"

Resources:
    +-1 replaced
    7 unchanged
```

Afterwards, we can `curl` the `publicIp` and see our Guestbook up and running:

```bash
$ curl http://$(pulumi stack output publicIp)
<html ng-app="redis">
  <head>
    <title>Guestbook</title>
  ...
</html>
```

Although this example shows the YAML `ConfigFile` resource, the same behavior is available with YAML `ConfigGroup` and Helm `Chart` resource types.

## Provisioning Mixed Configurations

It is possible to provision a combination of native Kubernetes objects, YAML files, Helm Charts, and other cloud resources all together, with dependences between them. For an example of doing so, see [this blog post]({{< relref "/blog/using-helm-and-pulumi-to-define-cloud-native-infrastructure-as-code" >}}) which demonstrates provisioning an Azure Kubernetes cluster, MongoDB-flavored CosmosDB instance, a Kubernetes secret to store the connection information, and a Helm Chart that consumes this secret and connects to the CosmosDB database.
