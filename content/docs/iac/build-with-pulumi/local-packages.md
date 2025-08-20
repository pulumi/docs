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

Pulumi Packages are the core technology that enables cloud infrastructure resource provisioning to be defined once and made available to users in all Pulumi languages. While many packages are published to the [Pulumi Registry](https://www.pulumi.com/registry/), there are cases where you might need to work with locally generated packages that haven't been published.

## What are Local Packages?

Local packages are Pulumi packages with sdks generated on your computer, instead of being checked into a provider repository and published to the Pulumi Registry. All Pulumi packages include a [schema](/docs/iac/using-pulumi/pulumi-packages/schema/) that defines the resources and functions exposed by the package. These packages are frequently part of the Pulumi experience in several contexts:

- When using parameterized providers like [pulumi-terraform-provider](https://www.pulumi.com/registry/packages/terraform-provider/).
- When working with components as packages.
- During package development and testing.
- For private or organization-specific resources.

Local packages allow you to generate SDKs in any Pulumi language for resources or components before they're published.

## Adding Local Packages with `pulumi package add`

The preferred way to add a local package is with the `pulumi package add` command. This command:

1. Locally generates an SDK in your currently selected Pulumi language.
2. Adds the package to your project configuration file (Pulumi.yaml).
3. Prints instructions on how to link the package into your project.

### Command Syntax

```bash
pulumi package add <provider|schema|path> [provider-parameter...] [flags]
```

### Adding a Package from Different Sources

The `pulumi package add` command can accept the package source in multiple ways:

#### From a Plugin Reference

```bash
pulumi package add PLUGIN[@VERSION]
```

This attempts to resolve a resource plugin, installing it on-demand similarly to:

```bash
pulumi plugin install resource PLUGIN [VERSION]
```

#### From a Local Path

```bash
pulumi package add ./my-provider
```

This executes the provider binary to extract its package schema.

#### From a Schema File

```bash
pulumi package add ./my/schema.json
```

When the path has a `.json`, `.yml`, or `.yaml` extension, the Pulumi package schema is read directly from it. For details on the structure and syntax of Pulumi package schemas, refer to the [Schema Reference](/docs/iac/using-pulumi/pulumi-packages/schema/). Understanding the schema format is particularly important if you're creating your own custom packages or components.

#### From a Git Repository

```bash
pulumi package add example.org/org/repo.git/path[@version]
```

This clones the repo and executes the source. The version can be a tag (in semver format) or a Git commit hash.

### Example: Using a Terraform Provider

One of the most common uses of local packages is with the `terraform-provider` to access any Terraform provider:

```bash
pulumi package add terraform-provider hashicorp/random
```

This will generate a local SDK for Hashicorp's random provider, which you can then use in your project:

```typescript
import * as random from "random";

new random.Pet("my-pet");
```

## Best Practices for Local Packages

When working with local packages, consider these best practices:

### Managing Generated SDKs

#### Option 1: Don't check in the generated SDK (recommended)

- Add the generated SDK directory to your `.gitignore` file
- Document the process for other developers to regenerate the SDK
- Include the `pulumi package add` command in your setup instructions

#### Option 2: Check in the generated SDK

- Pros: Ensures consistent builds and eliminates the need for regeneration
- Cons: Increases repository size and can lead to merge conflicts

### Updating Local Packages

To update a local package:

1. Re-run the `pulumi package add` command with the updated source
2. This will regenerate the SDK with the latest schema
3. Update your imports and code as needed if there are breaking changes

For packages from Git repositories, specify a version tag or commit hash to control which version is used.

### Versioning Considerations

- Consider using Git tags or specific commit hashes when referencing repositories to ensure reproducible builds
- Document the version of the source provider you're using
- Be aware that changes to the underlying provider can introduce breaking changes

## Using Generated SDKs

After adding a local package, follow the printed instructions to link it into your project:

1. For Node.js/TypeScript projects:

   ```bash
   npm add my-package@file:sdks/my-package
   ```

2. For Python projects:

   ```bash
   pip install -e ./sdks/my-package
   ```

3. For Go projects, add the appropriate import path as directed by the output.

4. For .NET projects, add a reference to the generated project file.

You can then import and use the package in your code just like any other Pulumi package.

## Troubleshooting Local Packages

If you encounter issues with local packages:

- Ensure you're using a compatible Pulumi version (≥3.147.0 for the terraform-provider)
- Check that all dependencies for the package are installed
- Verify that the schema file or provider binary is valid
- Look for error messages in the output of the `pulumi package add` command
- Try specifying an explicit version if available

## Conclusion

Local packages extend Pulumi's capabilities by allowing you to work with providers and components that aren't published to the Registry. The `pulumi package add` command makes it easy to generate and use these packages in your projects.

For more information about developing and publishing your own packages, see the [Publishing Packages](https://www.pulumi.com/docs/iac/build-with-pulumi/publishing-packages/) guide.
