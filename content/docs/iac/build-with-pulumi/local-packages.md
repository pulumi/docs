---
title: Local Packages
meta_desc: This page provides an overview of working with locally generated Pulumi packages.
menu:
  iac:
    parent: iac-build-with-pulumi
    weight: 65
aliases:
  - /docs/using-pulumi/pulumi-packages/local-packages/
---

Pulumi Packages are the core technology that enables cloud infrastructure resource provisioning to be defined once and made available to users in all Pulumi languages. While many packages are published to the [Pulumi Registry](/registry/), there are cases where you might need to work with locally generated packages that haven't been published.

## Understanding local packages

Local packages are Pulumi packages with sdks generated on your computer, instead of being checked into a provider repository and published to the Pulumi Registry. Given a [package schema](/docs/iac/using-pulumi/pulumi-packages/schema/) `pulumi` can generate your package SDK for you. These packages are frequently part of the Pulumi experience in several contexts:

- When using parameterized providers like [pulumi-terraform-provider](/registry/packages/terraform-provider/).
- When working with components as packages.
- During package development and testing.
- For private or organization-specific resources.

Local packages allow you to generate SDKs in any Pulumi language for resources or components before they're published.

## Adding local packages with `pulumi package add`

The preferred way to add a local package is with the [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) command.

1. Locally generates an SDK in your currently selected Pulumi language.
1. Adds the package to your project configuration file (Pulumi.yaml).
1. Prints instructions on how to link the package into your project.

### Command syntax

```bash
pulumi package add <provider|schema|path> [provider-parameter...] [flags]
```

### Adding a package from different sources

The `pulumi package add` command can accept the package source in multiple ways:

#### From a plugin reference

```bash
pulumi package add PLUGIN[@VERSION]
```

This attempts to resolve a resource plugin, installing it on-demand similarly to:

```bash
pulumi plugin install resource PLUGIN [VERSION]
```

#### From a local path

```bash
pulumi package add ./my-provider
```

This executes the provider binary to extract its package schema.

#### From a schema file

```bash
pulumi package add ./my/schema.json
```

For details on the structure and syntax of Pulumi package schemas, refer to the [Schema Reference](/docs/iac/using-pulumi/pulumi-packages/schema/).

#### From a git repository

```bash
pulumi package add example.org/org/repo.git/path[@version]
```

This clones the repo and executes the source. The version can be a tag (in semver format) or a Git commit hash.

### Example: Using a Terraform provider

One of the most common uses of local packages is with the `terraform-provider` to access [any Terraform provider](/registry/packages/terraform-provider/):

```bash
pulumi package add terraform-provider hashicorp/random
```

This will generate a local SDK for Hashicorp's random provider, which you can then use in your project:

```typescript
import * as random from "random";

new random.Pet("my-pet");
```

## Best practices for local packages

When working with local packages, consider these best practices:

### Managing generated SDKs

#### Option 1: Don't check in the generated SDK (recommended)

- Add the generated SDK directory to your `.gitignore` file.
- Document the process for other developers to regenerate the SDK with `pulumi install`.
- Include the `pulumi package add` command in your setup instructions.

#### Option 2: Check in the generated SDK

- Pros: Ensures consistent builds and eliminates the need for regeneration.
- Cons: Increases repository size and can lead to noisy PRs, possible merge conflicts.

### Updating local packages

To update a local package:

```bash
pulumi package add <provider|schema|path> [provider-parameter...] [flags]
```

1. Re-run the `pulumi package add` command with the updated source.
1. This will regenerate the SDK with the latest schema.
1. Update your imports and code as needed if there are breaking changes.

For packages from Git repositories, specify a version tag or commit hash to control which version is used.

### Versioning considerations

- Consider using Git tags or specific commit hashes when referencing repositories to ensure reproducible builds.
- Document the version of the source provider you're using.
- Be aware that changes to the underlying provider can introduce breaking changes.

## Using generated SDKs

After adding a local package, reference it in your project:

{{< chooser language "typescript,python,go,csharp,yaml" >}}
{{% choosable language typescript %}}

```bash
npm add my-package@file:sdks/my-package
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
pip install -e ./sdks/my-package
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
go get my-package@file:sdks/my-package
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
dotnet add package my-package --source ./sdks/my-package
```

{{% /choosable %}}
{{% /chooser %}}

You can then import and use the package in your code just like any other Pulumi package.

## Troubleshooting local packages

If you encounter issues with local packages:

- Ensure you're using a compatible Pulumi version (≥3.147.0 for the terraform-provider).
- Check that all dependencies for the package are installed.
- Verify that the schema file or provider binary is valid.
- Look for error messages in the output of the `pulumi package add` command.
- Try specifying an explicit version if available.

## Conclusion

Local packages extend Pulumi's capabilities by allowing you to work with providers and components that aren't published to the Registry. Use the [`pulumi package add`](/docs/iac/cli/commands/pulumi_package_add/) command to generate and use these packages in your projects.

For more information about developing and publishing your own packages, see the [Publishing Packages](/docs/iac/build-with-pulumi/publishing-packages/) guide.
