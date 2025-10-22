---
title: Local Packages
meta_desc: This page provides an overview of working with locally generated Pulumi packages.
menu:
  iac:
    parent: iac-guides-packages
    weight: 65
aliases:
  - /docs/using-pulumi/pulumi-packages/local-packages/
  - /docs/iac/build-with-pulumi/local-packages/
---

Pulumi Packages are the core technology that enables cloud infrastructure resource provisioning to be defined once and made available to users in all Pulumi languages. While many packages are published to the [Pulumi Registry](/registry/), there are cases where you might need to work with locally generated packages that haven't been published.

## Understanding local packages

Local packages are Pulumi packages with SDKs generated on your computer, instead of being checked into a provider repository and published to the Pulumi Registry. Given a [package schema](/docs/iac/using-pulumi/pulumi-packages/schema/) `pulumi` can generate your package SDK for you. These packages are frequently part of the Pulumi experience in several contexts:

- When using parameterized providers like [`terraform-provider`](/registry/packages/terraform-provider/).
- When working with components as packages.
- During package development and testing.
- For private or organization-specific resources.

Local packages allow you to generate SDKs in any Pulumi language for resources or components before they're published.

## Adding local packages with `pulumi package add`

The preferred way to add a local package is with the [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) command, which:

1. Locally generates an SDK in your currently selected Pulumi language.
1. Adds the package to your project configuration file (Pulumi.yaml).
1. Prints instructions on how to link the package into your project.

### Command syntax

```bash
pulumi package add <provider|schema|path> [provider-parameter...] [flags]
```

### Command examples

#### From a local path

```bash
pulumi package add ./my-provider
```

This executes the provider binary to extract its package schema, useful when developing a custom provider locally.

#### From a schema file

```bash
pulumi package add ./my/schema.json
```

This generates an SDK directly from a schema file, which is useful for component resources or when working with pre-defined schema definitions. For details on the structure and syntax of Pulumi package schemas, refer to the [Schema Reference](/docs/iac/using-pulumi/pulumi-packages/schema/).

#### From a git repository

```bash
pulumi package add example.com/org/repo.git/path[@version]
```

This clones the repo and executes the source, enabling you to use packages from private or public git repositories with specific version control. You can specify a branch, tag, or commit hash to control which version is used.

#### Using `terraform-provider`

```bash
pulumi package add terraform-provider hashicorp/random
```

Refer to the [Terraform Provider documentation](/docs/iac/using-pulumi/pulumi-packages/terraform-provider/) for more details.

## Using generated SDKs

After adding a local package, reference it in your project:

{{< chooser language "typescript,python,go,csharp,yaml" >}}
{{% choosable language typescript %}}

```bash
npm install ./sdks/my-package
```

```typescript
import * as myPackage from "my-package";

const example = new myPackage.ExampleResource("example");
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
pip install -e ./sdks/my-package
```

```python
import my_package

example = my_package.ExampleResource("example")
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
go get my-package@file:sdks/my-package
```

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/my-package/sdk/go/my_package"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		example := my_package.NewExampleResource("example", nil)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
dotnet add package my-package --source ./sdks/my-package
```

```csharp
using Pulumi;
using MyPackage;

await Deployment.RunAsync(ctx =>
{
  var example = new ExampleResource("example");
});
```

{{% /choosable %}}
{{% /chooser %}}

You can then import and use the package in your code just like any other Pulumi package.

## Managing generated SDKs

When working with locally generated SDKs, you need to decide whether to commit them to your repository or regenerate them as needed:

### Option 1: Don't check in the generated SDK (recommended)

- Add the generated SDK directory to your `.gitignore` file.
- Document the process for other developers to regenerate the SDK with `pulumi install`.
- Include the `pulumi package add` command in your setup instructions.

### Option 2: Check in the generated SDK

- Pros: Ensures consistent builds and eliminates the need for regeneration.
- Cons: Increases repository size and can lead to noisy PRs, possible merge conflicts.

## Updating local packages

As underlying providers evolve with new features or bug fixes, you'll need to update your local packages to take advantage of these improvements. To update a local package:

```bash
pulumi package add <provider|schema|path> [provider-parameter...] [flags]
```

1. Re-run the `pulumi package add` command with the updated source.
1. This will regenerate the SDK with the latest schema.
1. Update your imports and code as needed if there are breaking changes.

For packages from Git repositories, specify a version tag or commit hash to control which version is used.

After regenerating the SDK, ensure you reinstall or relink the SDK in your project using your language's package manager (e.g., `npm add`, `pip install -e`, etc.).

## Versioning considerations

- For native providers (e.g., `azure-native`, `aws-native`), versioning is managed via the language package manager (e.g., `npm`, `pip`, etc.).
- For the `terraform-provider` specifically, you can specify a version with the `--version` flag:
  
  ```bash
  pulumi package add terraform-provider hashicorp/random --version=3.5.1
  ```

  This version information will be stored in your `Pulumi.yaml` file, ensuring that anyone using your project gets the same provider version. The `--version` flag is only supported for parameterized providers.
- Document the version of the source provider you're using:
  - In your project documentation, note the specific version used.
  - Include version information in your README to help others understand compatibility requirements.
  - Consider creating a VERSION file for packages you develop.
- Consider using Git tags or specific commit hashes when referencing repositories:
  - **Pinning** (using specific versions): Ensures reproducible builds and stability, but may miss security patches or important updates.
  - **Non-pinning** (using latest): Automatically gets the newest features and fixes, but may introduce unexpected breaking changes.
  - Choose pinned versions for production systems where stability is critical, and unpinned/floating versions for development where you want the latest features.

## Managing breaking changes

When working with local packages, it's important to understand how breaking changes are handled:

- For standard providers (like `azure-native`), the provider version is recorded in your `Pulumi.yaml` file automatically.
- When using `terraform-provider` specifically, you're working with two different components:
  - The Pulumi `terraform-provider` bridge (which converts Terraform providers to Pulumi)
  - The actual Terraform provider you're accessing (e.g., `hashicorp/random`)

  To ensure stability, you should specify the version of both:

  ```bash
  pulumi package add terraform-provider hashicorp/random --version=3.5.1
  ```

  This pins the Terraform provider version, protecting you from unexpected breaking changes when the underlying provider is updated.

## See also

For more information about developing and publishing your own packages, see the [Publishing Packages](/docs/iac/build-with-pulumi/publishing-packages/) guide.
