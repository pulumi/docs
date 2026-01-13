---
title_tag: Using Any Terraform Provider
meta_desc: Learn how to use any Terraform or OpenTofu provider with Pulumi by generating local packages in your preferred programming language.
title: Any Terraform provider
h1: Using any Terraform provider
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Any Terraform provider
        parent: iac-concepts-providers
        weight: 5
---

Pulumi enables you to use any [Terraform](https://registry.terraform.io) or [OpenTofu](https://search.opentofu.org) provider from within your Pulumi programs. This feature gives you access to thousands of providers beyond those available in the [Pulumi Registry](/registry/), including community providers, custom internal providers, and the long tail of cloud and SaaS platforms that have Terraform providers.

## Overview

The Any Terraform Provider feature allows you to generate a Pulumi SDK locally for any Terraform or OpenTofu provider. When you run `pulumi package add terraform-provider <provider-name>`, Pulumi generates a fully-typed [local package](/docs/iac/guides/building-extending/packages/local-packages/) in your programming language (TypeScript, Python, Go, C#, Java, or YAML) that works just like any other Pulumi provider. You get the same developer experience: strong typing, IDE autocompletion, inline documentation, and the full power of general-purpose programming languages.

Common scenarios for generating local packages include:

- Using providers not available in the [Pulumi Registry](/registry/)
- Working with internal or custom Terraform providers developed by your organization
- Using a different version of a provider than what's published in the Registry
- Evaluating a provider before committing to it

{{% notes type="info" %}}
Some providers in the Pulumi Registry, such as the [Honeycomb provider](/registry/packages/honeycombio/), already use this feature. For these providers, the Registry provides documentation and installation instructions, but you still generate the SDK locally.
{{% /notes %}}

## OpenTofu registry compatibility

By default, Pulumi pulls Terraform providers from the [OpenTofu registry](https://search.opentofu.org), which is API-compatible with the Terraform registry and hosts the same providers. This means you can use any provider available in either registry.

You can also specify:

- A specific version of a provider
- A fully-qualified reference to any Terraform registry API-compatible server
- A local path to a provider binary (useful for custom or internal providers)

## Adding a Terraform provider

Use the [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) command to add any Terraform provider to your project:

```bash
pulumi package add terraform-provider [<registry>/]<author>/<name> [version]
```

### Basic example

To add the HashiCorp random provider:

```bash
pulumi package add terraform-provider hashicorp/random
```

This command generates a local SDK in your project's language and automatically adds an entry to your `Pulumi.yaml` file:

```yaml
packages:
  random:
    source: terraform-provider
    version: 0.10.0
    parameters:
      - hashicorp/random
```

### Specifying a version

For reproducible builds, specify the version of the Terraform provider you want to use:

```bash
pulumi package add terraform-provider hashicorp/random 3.7.1
```

This pins the Terraform provider version in your `Pulumi.yaml`:

```yaml
packages:
  random:
    source: terraform-provider
    version: 0.10.0  # Version of the terraform-provider package
    parameters:
      - hashicorp/random
      - 3.7.1  # Version of the hashicorp/random Terraform provider
```

{{% notes type="info" %}}
If you don't specify a Terraform provider version, Pulumi uses the latest version available from the registry. For consistent builds across environments and over time, always specify a version.
{{% /notes %}}

### Using a local provider binary

For custom or internal providers not published to a registry:

```bash
pulumi package add terraform-provider /path/to/my/terraform-provider-binary
```

## Walkthrough

Let's walk through using the Honeycomb Terraform provider with Pulumi. [Honeycomb](https://www.honeycomb.io/) is an observability platform that appears in the Pulumi Registry but uses the Any Terraform Provider feature.

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

This command generates a local SDK for the Honeycomb provider in your project's `sdks/` directory (except for YAML projects, where the provider is automatically available through the `Pulumi.yaml` configuration). Run [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) to complete the installation.

### Step 3: Install the SDK

```bash
pulumi install
```

This installs the generated SDK and its dependencies. For YAML projects, skip this step as the provider is automatically available through the `Pulumi.yaml` configuration.

### Step 4: Use the provider in your code

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

You'll see your IDE provide autocomplete, type checking, and inline documentation for the Honeycomb provider, just as it would for any other Pulumi provider.

### Step 5: Deploy your infrastructure

```bash
pulumi up
```

## Version control considerations

You can choose whether to commit the generated SDK directory to version control:

- **Commit the SDK directory**: Faster setup for team members and CI/CD pipelines, but increases repository size. The generated SDK includes a `.gitignore` file that excludes dependencies while allowing the SDK code itself to be committed.
- **Don't commit the SDK directory**: Smaller repository size, but team members must run [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) to generate the SDK locally.

The provider binary is always downloaded to a shared location outside your project directory and cached, so it only needs to be downloaded once per machine.

When team members clone your repository (if you didn't commit the SDK directory), they run:

```bash
pulumi install
```

This command reads the `packages` configuration in your `Pulumi.yaml` file and generates the local SDK.

## How local packages work

Local packages are generated SDKs stored in your project directory rather than pulled from package registries like npm or PyPI. For Terraform providers, the SDK files are generated in a language-specific subdirectory (typically `./sdks/<provider-name>`).

The generated SDK includes:

- Strongly typed resource and function definitions
- Inline documentation from the provider's schema
- Language-specific idioms (e.g., camelCase in TypeScript, snake_case in Python)
- A `.gitignore` file to exclude generated dependencies

Local packages are versioned, and the version information is stored in your `Pulumi.yaml` file. This ensures consistent builds across different environments and team members.

## Relationship to the Pulumi Registry

The [Pulumi Registry](/registry/) contains providers with pre-built SDKs published to package managers for the most popular cloud and SaaS platforms. The Registry also contains many providers that use the Any Terraform Provider feature to generate local SDKs. These registry entries provide documentation and installation instructions, but you generate the SDK locally. For example, the [Honeycomb provider](/registry/packages/honeycombio/) uses this approach.

For providers not in the Registry, or for custom internal providers, you can use the Any Terraform Provider feature to generate a local SDK directly.

## Best practices

1. **Pin provider versions**: Specify provider versions in your `Pulumi.yaml` to ensure consistent builds across environments and over time.

   ```bash
   # Good: Specify a version
   pulumi package add terraform-provider honeycombio/honeycombio 0.5.0

   # Risky: No version specified (uses latest)
   pulumi package add terraform-provider honeycombio/honeycombio
   ```

1. **Use `pulumi install`**: Always use [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) to set up projects, as it handles both standard package manager dependencies and local packages.

## Limitations

While the Any Terraform Provider feature is powerful, there are some considerations:

- **Documentation**: Generated SDKs for local packages include inline documentation, but you won't have dedicated web documentation in the Pulumi Registry (unless the provider has been added to the Registry).
- **Support**: For issues with the provider's functionality (not the bridge itself), you'll need to work with the Terraform provider's maintainers.

## Related resources

- [Pulumi Registry: Terraform Provider](/registry/packages/terraform-provider/) - Installation and configuration guide
- [Pulumi Packages](/docs/iac/concepts/packages/) - Learn about Pulumi's package system
- [Local Packages](/docs/iac/guides/building-extending/packages/local-packages/) - Deep dive into local package generation
- [Resource Providers](/docs/iac/concepts/providers/) - Understanding Pulumi's provider system
- [Getting Started: Use Terraform Providers](/docs/iac/get-started/terraform/terraform-providers/) - Quick start guide
- [Pulumi CLI: `pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) - Command reference
- [Pulumi CLI: `pulumi install`](/docs/iac/cli/commands/pulumi_install/) - Command reference
