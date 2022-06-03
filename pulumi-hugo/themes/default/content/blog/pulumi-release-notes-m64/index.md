---
title: "Nov. 17 releases: `dependOn` Helm charts, new Elastic Cloud provider, functions support outputs, set the CLI's default organization"
date: 2021-11-17T08:00:00-07:00
draft: false
allow_long_title: true
meta_desc: The latest Pulumi updates include a new provider for Elastic Cloud, easier ways to create more complex infrastructure, better support for organizations, & more
meta_image: meta.png
authors:
    - alex-mullans
tags:
    - features
---

It's been another exciting few weeks here at Pulumi! We've caught our breath from [Cloud Engineering Summit]({{<relref "/cloud-engineering-summit">}}) (don't forget to check out the talks if you haven't yet!) and we're back to adding new value and highly-requested fixes across the Pulumi Cloud Engineering Platform. Read on to learn about new providers, new enhancements to the core Pulumi experience, and more!

- Pulumi Registry, Pulumi Packages, & integrations
  - [`dependsOn` can now await a fully-deployed Helm `Chart` resource]({{<relref "/blog/pulumi-release-notes-m64#dependson-can-now-await-a-fully-deployed-helm-chart-resource">}})
  - [New provider: Elastic Cloud]({{<relref "/blog/pulumi-release-notes-m64#new-provider-elastic-cloud">}})
  - [AWS Native provider supports auto-naming]({{<relref "/blog/pulumi-release-notes-m64#aws-native-provider-supports-auto-naming">}})
  - [New resources in the AWS Native provider]({{<relref "/blog/pulumi-release-notes-m64#new-resources-in-the-aws-native-provider">}})
  - [New resources in the Azure Native provider]({{<relref "/blog/pulumi-release-notes-m64#new-resources-in-the-azure-native-provider">}})
- Pulumi CLI and core technologies
  - [Functions now support outputs]({{<relref "/blog/pulumi-release-notes-m64#functions-now-support-outputs">}})
  - [`--json` flag for `pulumi {update|destroy|preview|refresh}`]({{<relref "/blog/pulumi-release-notes-m64#--json-flag-for-pulumi-updatedestroypreviewrefresh">}})
  - [Python 3.6 support will be deprecated soon]({{<relref "/blog/pulumi-release-notes-m64#python-36-support-will-be-deprecated-soon">}})
- Pulumi Service & Pulumi.com
  - [Set the default organization for newly-created stacks]({{<relref "/blog/pulumi-release-notes-m64#new-resources-in-the-azure-native-provider">}})

<!--more-->

## Pulumi Registry, Pulumi Packages, & integrations

### `dependsOn` can now await a fully-deployed Helm `Chart` resource

Pulumi's [`dependsOn` option]({{<relref "/docs/intro/concepts/resources#dependson">}}) enables you to write programs that deploy resources in a specific order. Previously, using this option with a Helm `Chart` resource could be confusing because Pulumi would consider the resource ready once it had registered the chart, even if Helm was still deploying some of the resources defined by the chart. Now, you can depend on a new `ready` attribute that will ensure that none of the dependent resources are deployed until the chart is deployed. For example, the code sample below creates an NGINX Ingress Controller and then creates a Kubernetes `ConfigMap` that depends on the controller being fully deployed.

```typescript
import * as k8s from "@pulumi/kubernetes";

const nginxIngress = new k8s.helm.v3.Chart("nginx-ingress", {
    chart: "nginx-ingress",
    version: "1.24.4",
    namespace: "test-namespace",
    fetchOpts:{
        repo: "https://charts.helm.sh/stable",
    },
});

// Create a ConfigMap depending on the Chart. The ConfigMap will not be created until after all of the Chart
// resources are ready. Note the use of the `ready` attribute; depending on the Chart resource directly will not work.
new k8s.core.v1.ConfigMap("foo", {
    metadata: { namespace: namespaceName },
    data: {foo: "bar"}
}, {dependsOn: nginxIngress.ready})
```

{{% notes type="info" %}}
This change impacts the older Helm [`Chart`]({{<relref "/registry/packages/kubernetes/api-docs/helm/v3/chart">}}) resource. The new Helm [`Release`]({{<relref "/registry/packages/kubernetes/api-docs/helm/v3/release">}}) resource always waits for the Helm chart to be fully deployed.
{{% /notes %}}

[Learn more about `dependsOn` and Helm charts in this GitHub issue](https://github.com/pulumi/pulumi-kubernetes/issues/861)

### New provider: Elastic Cloud

You can now provision Elastic Cloud resources like ElasticSearch using Pulumi! Visit the [`ElasticCloud (EC)` provider on Pulumi Registry]({{<relref "/registry/packages/ec">}}) to get started. The example below shows how you can create an Elastic Cloud deployment in just a few lines of code:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const ec = require("@pulumi/ec")

const REGION = "us-east-1";

const latestVersion = elasticCloud.getStack({
    region: REGION,
    versionRegex: "latest"
});

new elasticCloud.Deployment('my-deployment', {
    region: REGION,
    version: latestVersion.then((x: { version: string; }) => x.version),
    deploymentTemplateId: "aws-io-optimized-v2",
    elasticsearch: {}
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as elasticCloud from "@pulumi/ec";

const REGION = "us-east-1";

const latestVersion = elasticCloud.getStack({
    region: REGION,
    versionRegex: "latest"
});

new elasticCloud.Deployment('my-deployment', {
    region: REGION,
    version: latestVersion.then((x: { version: string; }) => x.version),
    deploymentTemplateId: "aws-io-optimized-v2",
    elasticsearch: {}
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_ec as ec

REGION = "us-east-1"

latest_version = ec.get_stack(
    region=REGION, version_regex="latest").version

deployment = ec.Deployment('my-deployment', region=REGION, version=latest_version,
                           deployment_template_id="aws-io-optimized-v2", elasticsearch={})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
  ec "github.com/pulumi/pulumi-ec/sdk/go/ec"
)

func main() {
  pulumi.Run(func(ctx *pulumi.Context) error {
        version, err := ec.GetStack(ctx, &GetStackArgs{
      Region:       pulumi.String("us-east-1"),
      VersionRegex: "latest",
        }
    if err != nil {
      return err
    }

    _, err := ec.NewDeployment(ctx, "my-deployment", &ec.DeploymentArgs{
            Region:               pulumi.String("us-east-1"),
      Version:              version.Version,
            DeploymentTemplateId: pulumi.String("aws-io-optimized-v2")
      ElasticSearch:        &ec.DeploymentElasticsearch{},
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
using System.Threading.Tasks;
using Pulumi;
using ElasticCloud = Pulumi.ElasticCloud;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var latest = Output.Create(ElasticCloud.GetStack.InvokeAsync(new ElasticCloud.GetStackArgs
            {
                Region = "us-east-1",
                VersionRegex = "latest",
            });

            var deployment = ElasticCloud.Deployment("my-deployment", new ElasticCloud.DeploymentArgs
            {
                Region = "us-east-1",
                Version = latest.Version,
                DeploymentTemplateId = "aws-io-optimized-v2",
                ElasticSearch = {},
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

### AWS Native provider supports auto-naming

Most Pulumi providers support [auto-naming for resources]({{<relref "/docs/intro/concepts/resources#autonaming">}}), which makes it easier to have multiple stacks of the same Pulumi program by avoiding naming conflicts, among other benefits. Now, our AWS Native provider joins the club with full auto-naming support.

[Learn more about AWS auto-naming in this GitHub issue](https://github.com/pulumi/pulumi-aws-native/issues/156)

### New resources in the AWS Native provider

We shipped new versions of the AWS Native provider (0.3.0 through 0.4.0) that added [38 new resources](https://github.com/pulumi/pulumi-aws-native/compare/v0.2.0...v0.4.0#diff-1ac835cc58d7899e9299c7570151c7b0d7732c78f1bd53fe25fd4189b72e168e) giving you access to resources like `AWS::EKS::Cluster`, `AWS::Lightsail::Database`, and several new resources in the `AWS::Redshift` namespace.

### New resources in the Azure Native provider

We shipped new versions of the Azure Native provider (1.43.0 through 1.45.0) that collectively added [4 new resources](https://github.com/pulumi/pulumi-azure-native/blob/master/CHANGELOG.md#1450-2021-11-05) giving you access to resources like Cognitive Services.

## Pulumi CLI and core technologies

In this milestone, we shipped Pulumi version [3.17.0](https://github.com/pulumi/pulumi/releases/tag/v3.17.0). The full list of changes in this version is available in the [changelog](https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md); read on to learn about some of the biggest changes.

### Functions now support outputs

When creating complex infrastructure, it's common to pass information about one resource to a function provided by another resource. Previously, doing this in Pulumi required you to use `apply` to get the information from the first resource and pass it into the function. Now, we've simplified the process so you can reference outputs directly from the function—no `apply` needed. To take advantage of these changes, make sure you've updated to the latest versions of Pulumi and the providers you're using.

[Learn more in the "Functions now accept outputs" blog post]({{<relref "/blog/functions-accept-outputs">}})

### `--json` flag for `pulumi {update|destroy|preview|refresh}`

When automating or troubleshooting Pulumi operations, it can be helpful to see all of the details emitted by the Pulumi engine rather than the standard progress bar. Now, you can! Just add `--json` to your `pulumi {update|destroy|preview|refresh}` command.

[Learn more about the new `--json` flag in this GitHub issue](https://github.com/pulumi/pulumi/issues/2390)

### Python 3.6 support will be deprecated soon

Python 3.6 will be end-of-lifed ("EOLed") on [December 23, 2021](https://www.python.org/downloads/#:~:text=2016-12-23-,2021-12-23,-PEP%20494). Around that time, Pulumi will drop support for Python 3.6. If you're using Python 3.6, consider upgrading to a newer version of Python. The Pulumi CLI will display a message when it runs a Pulumi program using Python 3.6.

[Learn more about Python 3.6 deprecation in this GitHub issue](https://github.com/pulumi/pulumi/issues/8131)

## Pulumi Service & Pulumi.com

### Set the default organization for newly-created stacks

If you're using Pulumi as part of a team or company, rather than as part of a personal project, you likely want to ensure that any infrastructure you deploy is registered in your company's Pulumi organization, rather than in your personal Pulumi account. Previously, you needed to either create each stack inside the organization (`pulumi new -s <org>/<stackname>`) or transfer stacks into the organization once created. Now, you can set the default organization for Pulumi to use when creating new stacks: `pulumi org set-default <org>`. Watch the asciinema recording below to get a feel for how it works:

<script id="asciicast-9TQjcB0QGFGzj6MMzdfYUkwDc" src="https://asciinema.org/a/9TQjcB0QGFGzj6MMzdfYUkwDc.js" async></script>

[Learn more about setting the default organization in this GitHub issue](https://github.com/pulumi/pulumi/issues/3989)
