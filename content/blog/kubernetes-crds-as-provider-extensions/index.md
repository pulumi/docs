---
title: "Custom Resource Definitions as provider extensions"
# TODO: Update this date before publishing! Currently set to far future to prevent premature publication.
date: 2099-01-01
draft: false
meta_desc: "Extend the Pulumi Kubernetes provider with any CustomResourceDefinition using the new --extension flag: no crd2pulumi, no vendored SDK."
feature_image: feature.png
authors:
    - guinevere-saenger
tags:
    - kubernetes
    - releases
    - providers
category: product
schema_type: auto

social:
    twitter:
    linkedin:
    bluesky:
---

We're really excited to bring you the newest pulumi-kubernetes provider. As with any release, we've shipped standard dependency updates and bug fixes. This provider release includes the newest resources for Kubernetes v1.37.0, which was recently cut. So that in itself is very exciting!

<!--more-->

But the feature we're proudest of is that you can now extend the Kubernetes provider with any Kubernetes Custom Resource Definition (CRD) of your choice by passing its manifest file to Pulumi, using the new `--extension` flag. We believe making CRDs easy to use with Pulumi is becoming more important than ever. For example, since the retirement of the ingress-nginx controller earlier this year, the recommended path for cluster ingress is Gateway API, which is maintained and shipped as CRDs.

## Use

In your project root, run:

```bash
pulumi package add kubernetes --extension "name=gateway-networking crd-manifest=gateway-api-crds.yaml"
```

You will see the custom SDK generated in a new `sdks/` folder, as well as a new parameterization reference in `Pulumi.yaml`.

## One provider instance

Your new CRD schema exists as an extension to your existing provider and will be managed under the same provider instance, allowing you to use a single provider configuration and kubeconfig.

## No more vendoring a generated SDK

Additionally, your code no longer needs to ship SDK files as part of the project. The provider extension is referenced in your project file and its SDK, like all dependencies, can be regenerated via `pulumi install`.

## Full language support, including for YAML

Kubernetes CRDs can now be provisioned with Pulumi in all supported languages, not just the ones implemented in `crd2pulumi`.

## No more separate CLI

You will no longer need to use `crd2pulumi` as a separate CLI. `pulumi package add --extension` will see your CRD schema extended into your pulumi-kubernetes provider.

## Migration from crd2pulumi

If you've been using `crd2pulumi` in the past, pivoting to using the new provider extension is possible by referencing the new SDK package name in your Pulumi program. This change should result in a seamless no-op on `pulumi up`.

### Using crd2pulumi

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as crontabs from "./crontabs";

export const myCronTab = new crontabs.stable.v1.CronTab("my-new-cron-object", {
    metadata: { name: "my-new-cron-object" },
    spec: { cronSpec: "* * * * */5", image: "my-awesome-cron-image", replicas: 3 },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_kubernetes as k8s
import pulumi_crds as crontabs

my_cron_tab = crontabs.stable.v1.CronTab(
    "my-new-cron-object",
    metadata=k8s.meta.v1.ObjectMetaArgs(name="my-new-cron-object"),
    spec=crontabs.stable.v1.CronTabSpecArgs(
        cron_spec="* * * * */5",
        image="my-awesome-cron-image",
        replicas=3,
    ),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
import (
	crontabsv1 "myproject/crontabs/stable/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

pulumi.Run(func(ctx *pulumi.Context) error {
	_, err := crontabsv1.NewCronTab(ctx, "my-new-cron-object", &crontabsv1.CronTabArgs{
		Metadata: &metav1.ObjectMetaArgs{
			Name: pulumi.String("my-new-cron-object"),
		},
		Spec: &crontabsv1.CronTabSpecArgs{
			CronSpec: pulumi.String("* * * * */5"),
			Image:    pulumi.String("my-awesome-cron-image"),
			Replicas: pulumi.Int(3),
		},
	})
	return err
})
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Crds.Stable.V1;
using Pulumi.Crds.Types.Inputs.Stable.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;

var myCronTab = new CronTab("my-new-cron-object", new CronTabArgs
{
    Metadata = new ObjectMetaArgs { Name = "my-new-cron-object" },
    Spec = new CronTabSpecArgs
    {
        CronSpec = "* * * * */5",
        Image = "my-awesome-cron-image",
        Replicas = 3,
    },
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.crds.stable.example.com_v1.CronTab;
import com.pulumi.crds.stable.example.com_v1.CronTabArgs;
import com.pulumi.crds.stable.example.com_v1.inputs.CronTabSpecArgs;
import com.pulumi.kubernetes.meta.v1.inputs.ObjectMetaArgs;

var myCronTab = new CronTab("my-new-cron-object", CronTabArgs.builder()
    .metadata(ObjectMetaArgs.builder()
        .name("my-new-cron-object")
        .build())
    .spec(CronTabSpecArgs.builder()
        .cronSpec("* * * * */5")
        .image("my-awesome-cron-image")
        .replicas(3)
        .build())
    .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

`crd2pulumi` does not support YAML.

{{% /choosable %}}

{{< /chooser >}}

### Pivoting to extension

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as crontabs from "@pulumi/crontabs";

export const myCronTab = new crontabs.stable.v1.CronTab("my-new-cron-object", {
    metadata: { name: "my-new-cron-object" },
    spec: { cronSpec: "* * * * */5", image: "my-awesome-cron-image", replicas: 3 },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_kubernetes as k8s
import pulumi_crontabs as crontabs

my_cron_tab = crontabs.stable.v1.CronTab(
    "my-new-cron-object",
    metadata=k8s.meta.v1.ObjectMetaArgs(name="my-new-cron-object"),
    spec=crontabs.stable.v1.CronTabSpecArgs(
        cron_spec="* * * * */5",
        image="my-awesome-cron-image",
        replicas=3,
    ),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
import (
	crontabsv1 "crontabs/kubernetes/stable/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

pulumi.Run(func(ctx *pulumi.Context) error {
	_, err := crontabsv1.NewCronTab(ctx, "my-new-cron-object", &crontabsv1.CronTabArgs{
		Metadata: &metav1.ObjectMetaArgs{
			Name: pulumi.String("my-new-cron-object"),
		},
		Spec: &crontabsv1.CronTabSpecArgs{
			CronSpec: pulumi.String("* * * * */5"),
			Image:    pulumi.String("my-awesome-cron-image"),
			Replicas: pulumi.Int(3),
		},
	})
	return err
})
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Crontabs.Stable.V1;
using Pulumi.Crontabs.Types.Inputs.Stable.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;

var myCronTab = new CronTab("my-new-cron-object", new CronTabArgs
{
    Metadata = new ObjectMetaArgs { Name = "my-new-cron-object" },
    Spec = new CronTabSpecArgs
    {
        CronSpec = "* * * * */5",
        Image = "my-awesome-cron-image",
        Replicas = 3,
    },
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.crontabs.stable.v1.CronTab;
import com.pulumi.crontabs.stable.v1.CronTabArgs;
import com.pulumi.crontabs.stable.v1.inputs.CronTabSpecArgs;
import com.pulumi.kubernetes.meta.v1.inputs.ObjectMetaArgs;

var myCronTab = new CronTab("my-new-cron-object", CronTabArgs.builder()
    .metadata(ObjectMetaArgs.builder()
        .name("my-new-cron-object")
        .build())
    .spec(CronTabSpecArgs.builder()
        .cronSpec("* * * * */5")
        .image("my-awesome-cron-image")
        .replicas(3)
        .build())
    .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  my-new-cron-object:
    type: crontabs:stable.example.com/v1:CronTab
    properties:
      metadata:
        name: my-new-cron-object
      spec:
        cronSpec: "* * * * */5"
        image: my-awesome-cron-image
        replicas: 3
```

{{% /choosable %}}

{{< /chooser >}}

Read more in [Typed CustomResources with Provider Extensions](/registry/packages/kubernetes/how-to-guides/typed-customresources-with-provider-extensions/).

Available from Pulumi v3.255.0 and the Pulumi Kubernetes provider v4.34.0.
