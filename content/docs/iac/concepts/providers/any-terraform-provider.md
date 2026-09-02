---
title_tag: Using Any Terraform Provider
meta_desc: Learn how to use any Terraform or OpenTofu provider in a Pulumi program, including providers that have no pre-built Pulumi package.
title: Any Terraform Provider
h1: Using any Terraform provider
menu:
    iac:
        name: Any Terraform Provider
        parent: iac-concepts-providers
        weight: 5
---

Pulumi can use any [Terraform](https://registry.terraform.io) or [OpenTofu](https://search.opentofu.org) provider directly in your Pulumi programs. Between them, those ecosystems cover thousands of providers spanning clouds, SaaS platforms, on-premises systems, and internal tooling, and the Any Terraform Provider feature makes them available to Pulumi.

Reach for it when:

- **No Pulumi provider exists for the service you need, but a Terraform or OpenTofu provider does.** This is the most common case, and it covers the long tail of SaaS and infrastructure vendors.
- **Your organization maintains its own Terraform provider.** You can point Pulumi at a provider binary on disk, so internal providers work the same way published ones do.
- **You need a provider version that the Pulumi Registry doesn't publish**, such as an older release you're pinned to or a newer one that isn't available in the Pulumi Registry yet.

## Language support

The Any Terraform Provider feature works with every Pulumi language, and `pulumi package add` is how you add a provider in each one. What differs is whether you also get a generated SDK.

In TypeScript, Python, Go, .NET, and Java, `pulumi package add` generates a typed SDK for the provider in your project, so you get autocompletion, type checking, and inline documentation in your editor, the same as with a provider published to the [Pulumi Registry](/registry/).

In YAML there's no SDK to generate. `pulumi package add` records the package in your `Pulumi.yaml`, and you reference its resources by their schema token, which takes the form `<package-name>:<module>:<Resource>`.

{{% notes type="info" %}}
[Pulumi HCL](/docs/iac/languages-sdks/hcl/) doesn't need `pulumi package add` at all. Terraform and OpenTofu providers resolve from the OpenTofu registry and are bridged automatically, the same way they are in OpenTofu. Declare a provider in a `required_providers` block if you want to pin its source and version, then run `pulumi install`.
{{% /notes %}}

## Adding a Terraform provider

Use the [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) command:

```bash
pulumi package add terraform-provider [<registry>/]<author>/<name> [version]
```

Pulumi resolves providers from the [OpenTofu registry](https://search.opentofu.org) by default. That registry is API-compatible with the Terraform registry and hosts the same providers, so a provider published to either one is available. You can also give a fully qualified reference to any server that implements the Terraform registry API.

### Basic example

To add the HashiCorp `random` provider:

```bash
pulumi package add terraform-provider hashicorp/random
```

Along with making the provider available to your program, this adds an entry to your `Pulumi.yaml`:

```yaml
packages:
  random:
    source: terraform-provider
    version: 0.10.0
    parameters:
      - hashicorp/random
```

### Specifying a version

If you don't specify a version, Pulumi uses the latest one available from the registry. Pin the version instead, so that everyone on your team and every CI run gets the same provider:

```bash
pulumi package add terraform-provider hashicorp/random 3.7.1
```

The pinned version is recorded in `Pulumi.yaml` alongside the provider name:

```yaml
packages:
  random:
    source: terraform-provider
    version: 0.10.0  # Version of the terraform-provider package
    parameters:
      - hashicorp/random
      - 3.7.1  # Version of the hashicorp/random Terraform provider
```

Two versions appear here because two things are versioned independently: `version` is the version of Pulumi's `terraform-provider` package, and the second parameter is the version of the Terraform provider it wraps. Pin both for fully reproducible builds.

### Using a provider binary on disk

For a custom or internal provider that isn't published to a registry, pass the path to its binary:

```bash
pulumi package add terraform-provider /path/to/my/terraform-provider-binary
```

## Walkthrough

The following walkthrough uses the Honeycomb Terraform provider with Pulumi. [Honeycomb](https://www.honeycomb.io/) is an observability platform whose provider is available to Pulumi through this feature.

### Step 1: Create a new Pulumi project

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```bash
pulumi new typescript
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
pulumi new python
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
pulumi new go
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
pulumi new csharp
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
pulumi new java
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
pulumi new yaml
```

{{% /choosable %}}

### Step 2: Add the Terraform provider

```bash
pulumi package add terraform-provider honeycombio/honeycombio
```

This downloads the provider and records it in your `Pulumi.yaml`. In every language except YAML, it also generates and links a typed SDK in your project.

### Step 3: Use the provider in your code

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as honeycombio from "@pulumi/honeycombio";

const marker = new honeycombio.Marker("deployment-marker", {
    message: "Deployed via Pulumi",
    dataset: "my-dataset"
});

export const markerId = marker.id;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_honeycombio as honeycombio

marker = honeycombio.Marker(
    "deployment-marker",
    message="Deployed via Pulumi",
    dataset="my-dataset"
)

pulumi.export("marker_id", marker.id)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-terraform-provider/sdks/go/honeycombio"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        marker, err := honeycombio.NewMarker(ctx, "deployment-marker", &honeycombio.MarkerArgs{
            Message: pulumi.String("Deployed via Pulumi"),
            Dataset: pulumi.String("my-dataset"),
        })
        if err != nil {
            return err
        }

        ctx.Export("markerId", marker.ID())
        return nil
    })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Honeycombio;

return await Deployment.RunAsync(() =>
{
    var marker = new Marker("deployment-marker", new MarkerArgs
    {
        Message = "Deployed via Pulumi",
        Dataset = "my-dataset"
    });

    return new Dictionary<string, object?>
    {
        ["markerId"] = marker.Id
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.honeycombio.Marker;
import com.pulumi.honeycombio.MarkerArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var marker = new Marker("deployment-marker", MarkerArgs.builder()
            .message("Deployed via Pulumi")
            .dataset("my-dataset")
            .build());

        ctx.export("markerId", marker.id());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: honeycomb-example
runtime: yaml
description: Using the Honeycomb Terraform provider with Pulumi
resources:
  marker:
    type: honeycombio:Marker
    properties:
      message: Deployed via Pulumi
      dataset: my-dataset
outputs:
  markerId: ${marker.id}
packages:
  honeycombio:
    source: terraform-provider
    version: 0.10.0
    parameters:
      - honeycombio/honeycombio
```

{{% /choosable %}}

### Step 4: Deploy your infrastructure

```bash
pulumi up
```

## Configuring the provider

Terraform providers name their configuration fields in snake_case, such as `oauth_client_id`. Pulumi uses camelCase for those names instead, so the same field becomes `oauthClientId`.

Provider configuration keys always use the camelCase form, no matter which language your program is written in:

```bash
pulumi config set tailscale:oauthClientId <value>
```

The same is true everywhere provider configuration is set, including [`pulumi config set`](/docs/iac/cli/commands/pulumi_config_set/), [Pulumi ESC](/docs/esc/), and the Automation API's `setConfig`.

{{% notes type="warning" %}}
A snake_case configuration key such as `tailscale:oauth_client_id` isn't recognized, and is silently ignored. Always use the camelCase form.
{{% /notes %}}

Resource inputs and outputs are a separate matter. They're written the way your language writes names, exactly as they are for any other Pulumi provider: `clientId` in TypeScript, Go, .NET, and Java, and `client_id` in Python. See [Inputs & outputs](/docs/iac/concepts/inputs-outputs/) for more.

To look up a name, read the provider's own documentation in the [OpenTofu](https://search.opentofu.org) or [Terraform](https://registry.terraform.io) registry. Its fields are listed in snake_case, and the Pulumi configuration key is the camelCase form of the same name.

## Working with your team

Commit your `Pulumi.yaml` to source control. It records the provider and its version, which is all a teammate or a CI job needs to reproduce your setup.

When someone clones the repository, they run [`pulumi install`](/docs/iac/cli/commands/pulumi_install/):

```bash
pulumi install
```

This installs whatever is missing: the Terraform provider binary, and the generated SDK if the SDK directory isn't checked in. Provider binaries are cached in a shared location outside your project directory, so each one is downloaded only once per machine.

Whether to check the generated SDK directory into source control is a tradeoff. See [Local SDKs](/docs/iac/guides/building-extending/packages/local-sdks/) for that decision, along with guidance on upgrading a provider and on team workflow.

## Providers in the Pulumi Registry

Many of the more popular providers Pulumi makes available this way are also listed in the [Pulumi Registry](/registry/), so you can search for them, read their documentation, and get installation instructions in the same place you'd look for any other Pulumi provider. When you search the Registry, these providers carry a badge identifying them as Any Terraform Provider packages. The [Honeycomb provider](/registry/packages/honeycombio/) is one example.

If the provider you need isn't in the Pulumi Registry, search the [OpenTofu registry](https://search.opentofu.org) and add it with [`pulumi package add`](#adding-a-terraform-provider).

## Learn more

- [Pulumi Registry: Terraform Provider](/registry/packages/terraform-provider/) - Installation and configuration guide
- [Resource providers](/docs/iac/concepts/providers/) - How providers work in Pulumi
- [Pulumi packages](/docs/iac/concepts/packages/) - Pulumi's package system
- [Local SDKs](/docs/iac/guides/building-extending/packages/local-sdks/) - Working with locally generated SDKs
- [Use Terraform Providers](/docs/iac/get-started/terraform/terraform-providers/) - Quick start guide
- [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) - Command reference
- [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) - Command reference
