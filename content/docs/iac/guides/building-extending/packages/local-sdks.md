---
title: Local SDKs
meta_desc: This page provides an overview of working with locally generated Pulumi SDKs.
menu:
  iac:
    parent: iac-guides-packages
    weight: 50
aliases:
  - /docs/using-pulumi/pulumi-packages/local-packages/
  - /docs/iac/build-with-pulumi/local-packages/
  - /docs/iac/guides/building-extending/packages/local-packages/
---

Pulumi Packages are the core technology that enables cloud infrastructure resource provisioning to be defined once and made available to users in all Pulumi languages. While many packages are published to the [Pulumi Registry](/registry/), there are cases where you might need to work with locally generated SDKs for packages that haven't been published.

## Understanding local SDKs

A local SDK is a Pulumi package SDK generated on your own computer, in the language of your program, instead of being checked into a provider repository and published to the Pulumi Registry. The package's source or executable is often downloaded from a remote source (for example, a registry or a Git repository), but the SDK itself is generated locally. Given a [package schema](/docs/iac/guides/building-extending/packages/schema/) `pulumi` can generate your package SDK for you. Local SDKs are frequently part of the Pulumi experience in these contexts:

- When using parameterized providers like [`terraform-provider`](/registry/packages/terraform-provider/).
- When working with components as packages.
- During package development and testing.
- For private or organization-specific resources.

Local SDKs allow you to generate SDKs in any Pulumi language for resources or components before they're published.

{{% notes type="info" %}}
Generating an SDK locally is not the only option. You can also **pre-publish** SDKs to your language's package registry ahead of time, which avoids the local generation step for consumers. See [Publishing Packages](/docs/iac/guides/building-extending/packages/publishing-packages/) for a comparison of the trade-offs, and [Authoring a component for distribution](/docs/iac/concepts/packages/#authoring-a-component-for-distribution) for guidance on which to choose.
{{% /notes %}}

## Adding a local SDK with `pulumi package add`

The preferred way to add a local SDK is with the [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) command, which:

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

This generates an SDK directly from a schema file, which is useful for component resources or when working with pre-defined schema definitions. For details on the structure and syntax of Pulumi package schemas, refer to the [Schema Reference](/docs/iac/guides/building-extending/packages/schema/).

#### From a git repository

```bash
pulumi package add example.com/org/repo.git/path[@version]
```

This clones the repo and executes the source, enabling you to use packages from private or public git repositories with specific version control. You can specify a branch, tag, or commit hash to control which version is used.

#### Using `terraform-provider`

```bash
pulumi package add terraform-provider hashicorp/random 3.5.1
```

Refer to the [Any Terraform Provider documentation](/docs/iac/get-started/terraform/terraform-providers/) for more details.

## Using generated SDKs

After adding a local SDK, reference it in your project:

{{< chooser language "typescript,python,go,csharp" >}}
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

## Updating local SDKs

As underlying providers evolve with new features or bug fixes, you'll need to update your local SDKs to take advantage of these improvements.

### How local SDK versions are tracked

When you run `pulumi package add`, the command registers the package and its version in your project's `Pulumi.yaml` file. For example, after adding a Terraform provider:

```yaml
packages:
  random:
    source: terraform-provider
    version: 0.10.0
    parameters:
      - hashicorp/random
      - 3.7.1
```

When adding a [source-based plugin package](/docs/iac/guides/building-extending/packages/source-based-plugin/) from a local path, the entry records the path directly:

```yaml
packages:
  my-components: ./path/to/my-components
```

You should commit `Pulumi.yaml` to source control so that your teammates can reproduce the same environment. When a collaborator clones your repository, they run [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) to install all packages defined in `Pulumi.yaml`, including generating any local SDKs.

### Upgrading a local SDK

To upgrade a local SDK, re-run the `pulumi package add` command with the updated source or version:

```bash
# Upgrade a Terraform provider to a new version
pulumi package add terraform-provider hashicorp/random 3.7.1

# Upgrade a component from a git repository to a new tag
pulumi package add example.com/org/repo.git/path@v2.0.0

# Regenerate from an updated local schema file
pulumi package add ./my/schema.json
```

This will:

1. Regenerate the SDK with the latest schema.
1. Update the package entry in your `Pulumi.yaml` file.

After regenerating the SDK, run [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) to install all dependencies, including the updated local SDK. Update your imports and code as needed if there are breaking changes.

### Checking your current version

To see which version of a local SDK your project is using, inspect the `packages` section of your `Pulumi.yaml` file. You can also run [`pulumi package info <package-name>`](/docs/iac/cli/commands/pulumi_package_info/) to view details about an installed package.

### Team workflow

A typical workflow for teams using local SDKs:

1. A developer upgrades a package by running `pulumi package add` with the new version.
1. The developer commits the updated `Pulumi.yaml` to source control. (If the team has chosen to [check in the generated SDK](#option-2-check-in-the-generated-sdk), the updated SDK should also be committed.)
1. Other team members pull the changes and run `pulumi install` to regenerate the SDK and install dependencies locally.

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

When working with local SDKs, it's important to understand how breaking changes are handled:

- For standard providers (like `azure-native`), the provider version is recorded in your `Pulumi.yaml` file automatically.
- When using `terraform-provider` specifically, you're working with two different components:
  - The Pulumi `terraform-provider` bridge (which converts Terraform providers to Pulumi)
  - The actual Terraform provider you're accessing (e.g., `hashicorp/random`)

  To ensure stability, you should specify the version of both:

  ```bash
  pulumi package add terraform-provider hashicorp/random 3.5.1
  ```

  This pins the Terraform provider version, protecting you from unexpected breaking changes when the underlying provider is updated.

## Using components with local SDKs {#components-with-local-packages}

When creating a component that contains a local SDK, you must ensure the generated SDK is available to consumers of your component. This applies when your component uses:

- Any Terraform provider via [`terraform-provider`](/registry/packages/terraform-provider/)
- Another component that itself contains a local SDK
- Any other Pulumi plugin that generates code in the `sdk` folder

### Requirements

1. You must be using Pulumi 3.200.0 or later.
1. In your component code, run `pulumi package add` to generate the upstream SDK.
1. Ensure the generated code in the `sdk` folder is committed to version control.

### Why this is necessary

When someone consumes your component, they need access to all the SDKs your component depends on. For published packages from the Pulumi Registry, these dependencies are automatically resolved. However, for local SDKs generated within your component, the generated SDK code must be available in your repository so that consumers can use it.

### Example workflow

If you're building a component that uses a Terraform provider:

```bash
cd my-component
pulumi package add terraform-provider hashicorp/random 3.5.1
git add sdk/
git commit -m "Add generated SDK for terraform-provider random"
```

Consumers of your component will then be able to use it without needing to regenerate the SDK themselves.

## Using local SDKs with Automation API

For documentation on how to use local SDKs with Pulumi's [Automation API](/docs/iac/concepts/automation-api/) see [Using local SDKs with Automation API](/docs/iac/guides/building-extending/automation-api/#using-local-packages-with-automation-api).

## See also

For more information about developing and publishing your own packages, see the [Publishing Packages](/docs/iac/guides/building-extending/packages/publishing-packages/) guide.
