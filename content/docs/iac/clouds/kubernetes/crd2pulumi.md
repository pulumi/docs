---
title_tag: "Generate typed CustomResources with crd2pulumi"
meta_desc: crd2pulumi generates typed Pulumi SDK classes from Kubernetes CustomResourceDefinition (CRD) YAML schemas, enabling IDE autocompletion and type checking.
title: crd2pulumi
h1: crd2pulumi
meta_image: /images/docs/meta-images/docs-clouds-kubernetes-meta-image.png
menu:
  iac:
    name: crd2pulumi
    parent: kubernetes-clouds
    identifier: kubernetes-clouds-crd2pulumi
    weight: 20
---

`crd2pulumi` is a CLI tool that generates typed Pulumi SDK classes from Kubernetes [CustomResourceDefinition (CRD)](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) YAML schemas. While Pulumi lets you manage Kubernetes [`CustomResources`](/registry/packages/kubernetes/api-docs/apiextensions/customresource/) directly, those resources are untyped by default because every CRD schema is different. `crd2pulumi` solves this by reading a CRD's OpenAPI schema and generating strongly typed classes for your language of choice, enabling IDE autocompletion and compile-time type checking.

This is particularly useful for complex CRDs with large schemas, such as [cert-manager](https://cert-manager.io/) or [Istio](https://istio.io/), where manually constructing resource arguments is error-prone.

## Installation

Install `crd2pulumi` via Homebrew:

```bash
brew install pulumi/tap/crd2pulumi
```

Alternatively, download a binary from the [GitHub releases page](https://github.com/pulumi/crd2pulumi/releases).

## Usage

The following example uses the [CronTab CRD](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) from the Kubernetes documentation. Generate typed SDK classes with `crd2pulumi`, then use them alongside [`ConfigFile`](/registry/packages/kubernetes/api-docs/yaml/v2/configfile/) to register the CRD and instantiate a typed resource.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

Generate TypeScript types:

```bash
crd2pulumi --nodejsPath ./crontabs resourcedefinition.yaml
```

Import the generated types into your Pulumi program:

```typescript
import * as crontabs from "./crontabs";
import * as k8s from "@pulumi/kubernetes";

const cronTabDefinition = new k8s.yaml.v2.ConfigFile("my-crontab-definition", {
    file: "resourcedefinition.yaml",
});

const myCronTab = new crontabs.stable.v1.CronTab("my-new-cron-object", {
    metadata: {
        name: "my-new-cron-object",
    },
    spec: {
        cronSpec: "* * * * */5",
        image: "my-awesome-cron-image",
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

Generate Python types:

```bash
crd2pulumi --pythonPath ./crontabs resourcedefinition.yaml
```

Import the generated types into your Pulumi program:

```python
from pulumi_kubernetes.yaml.v2 import ConfigFile
import crontabs.pulumi_crds as crontabs

crontab_definition = ConfigFile("my-crontab-definition", file="resourcedefinition.yaml")

crontab_instance = crontabs.stable.v1.CronTab(
    "my-new-cron-object",
    metadata={"name": "my-new-cron-object"},
    spec=crontabs.stable.v1.CronTabSpecArgs(
        cron_spec="* * * * */5",
        image="my-awesome-cron-image",
    ),
)
```

{{% /choosable %}}

{{% choosable language go %}}

Generate Go types:

```bash
crd2pulumi --goPath ./crontabs resourcedefinition.yaml
```

Import the generated types into your Pulumi program. In this example the Go module is named `crds-go-final`, so the import path is `crds-go-final/crontabs/stable/v1` — replace this with your own module name:

```go
package main

import (
    crontabs_v1 "crds-go-final/crontabs/stable/v1"

    yamlv2 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/yaml/v2"
    meta_v1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        _, err := yamlv2.NewConfigFile(ctx, "my-crontab-definition",
            &yamlv2.ConfigFileArgs{
                File: pulumi.String("resourcedefinition.yaml"),
            },
        )
        if err != nil {
            return err
        }

        _, err = crontabs_v1.NewCronTab(ctx, "my-new-cron-object", &crontabs_v1.CronTabArgs{
            Metadata: &meta_v1.ObjectMetaArgs{
                Name: pulumi.String("my-new-cron-object"),
            },
            Spec: crontabs_v1.CronTabSpecArgs{
                CronSpec: pulumi.String("* * * * */5"),
                Image:    pulumi.String("my-awesome-cron-image"),
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

Generate .NET types:

```bash
crd2pulumi --dotnetPath ./crontabs resourcedefinition.yaml
```

Import the generated types into your Pulumi program:

```csharp
using Pulumi;
using Pulumi.Kubernetes.Yaml.V2;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;

class MyStack : Stack
{
    public MyStack()
    {
        var cronTabDefinition = new ConfigFile("my-crontab-definition",
            new ConfigFileArgs
            {
                File = "resourcedefinition.yaml",
            }
        );

        var cronTabInstance = new Pulumi.Crds.Stable.V1.CronTab("my-new-cron-object",
            new Pulumi.Kubernetes.Types.Inputs.Stable.V1.CronTabArgs
            {
                Metadata = new ObjectMetaArgs
                {
                    Name = "my-new-cron-object",
                },
                Spec = new Pulumi.Kubernetes.Types.Inputs.Stable.V1.CronTabSpecArgs
                {
                    CronSpec = "* * * * */5",
                    Image = "my-awesome-cron-image",
                },
            }
        );
    }
}
```

If you see a `Duplicate 'global::System.Runtime.Versioning.TargetFrameworkAttribute' attribute` error when running `pulumi up`, delete the `crontabs/bin` and `crontabs/obj` folders and try again.

{{% /choosable %}}

{{% choosable language java %}}

Generate Java types:

```bash
crd2pulumi --javaPath ./crontabs resourcedefinition.yaml
```

Import the generated types into your Pulumi program:

```java
package com.example;

import com.pulumi.Pulumi;
import com.pulumi.kubernetes.yaml.v2.ConfigFile;
import com.pulumi.kubernetes.yaml.v2.ConfigFileArgs;

public class MyStack {

    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var cronTabDefinition = new ConfigFile("my-crontab-definition",
                ConfigFileArgs.builder()
                    .file("resourcedefinition.yaml")
                    .build());

            var cronTabInstance = new com.pulumi.crds.stable.v1.CronTab("my-new-cron-object",
                com.pulumi.crds.stable.v1.CronTabArgs.builder()
                    .metadata(com.pulumi.kubernetes.meta.v1.inputs.ObjectMetaArgs.builder()
                        .name("my-new-cron-object")
                        .build())
                    .spec(com.pulumi.kubernetes.stable.v1.inputs.CronTabSpecArgs.builder()
                        .cronSpec("* * * * */5")
                        .image("my-awesome-cron-image")
                        .build())
                    .build());
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}
