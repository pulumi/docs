---
title_tag: Private Registry | Pulumi IDP
title: Private Registry
h1: "Private Registry"
meta_desc: Learn how to publish and manage components and templates in Pulumi's Private Registry.
aliases:
  - /docs/idp/get-started/private-registry/
menu:
  idp:
    parent: idp-concepts
    identifier: idp-concepts-private-registry
    weight: 10
---

Pulumi Private Registry is the source of truth for an organization's infrastructure building blocks like [components](/docs/iac/concepts/resources/components/) and [templates](/docs/idp/concepts/organization-templates/). Platform engineers publish components to the private registry so that developers can discover them, browse auto-generated API documentation, and use them in their Pulumi programs.

For detailed information about different component packaging approaches, see [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/).

## Before you begin

1. You need a [Pulumi Cloud](https://app.pulumi.com) account on the Enterprise or Business Critical plan.
1. You need the [Pulumi CLI](/docs/install/) installed.
1. Your component must be pushed to a GitHub or GitLab repository that Pulumi can access. Private repositories are supported — see [Authenticating with private repositories](#authenticating-with-private-repositories).
1. If you haven't built a component yet, see [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/).

## Quick start

The following example publishes a component from a GitHub repository to your organization's private registry:

```bash
# Tag a version in your component repository
git tag v1.0.0
git push origin v1.0.0

# Publish to your organization's private registry
pulumi package publish github.com/<org>/<component-name>@1.0.0
```

That's it. Pulumi introspects your component, generates API documentation, and makes it available in your organization's private registry. The sections below cover each step in detail.

## Publish a component

The [`pulumi package publish`](/docs/iac/cli/commands/pulumi_package_publish/) command publishes a component to the private registry:

```bash
pulumi package publish <provider|schema>
```

For example, if your GitHub organization is ACME and you are publishing the `k8s-cluster` component:

```bash
pulumi package publish github.com/acme/k8s-cluster
```

## Versioning

Pulumi uses git tags for versioning components. By default, the latest version tag will be used. The tag must adhere to [the semantic versioning standard](https://semver.org/) plus a "v" prefix (e.g. `v1.2.3`).

To publish a specific version, append an `@` followed by the semver version (excluding the "v") after the git source:

```bash
git tag v1.2.3
git push origin v1.2.3
pulumi package publish github.com/acme/k8s-cluster@1.2.3
```

## README

A README is required when publishing a component. Pulumi renders markdown README files in the private registry. They're a great way to provide context for a component. By default, the Pulumi CLI looks for a README in the component's root directory. The `--readme` flag can be used to specify a custom source.

```bash
pulumi package publish github.com/acme/k8s-cluster --readme README_LOCATION
```

## Authenticating with private repositories

If your repository is private, a valid `GITHUB_TOKEN` or `GITLAB_TOKEN` is required for all commands, including `publish`, `get schema`, and when using the component in a program (`pulumi install`, `pulumi up`, etc.).

By default, the Pulumi CLI will look for a token in the `GITHUB_TOKEN` and `GITLAB_TOKEN` environment variables.

```bash
GITHUB_TOKEN="$(gh auth token)"
pulumi package publish github.com/acme/k8s-cluster
```

## Specifying an organization

If you're part of multiple organizations and do not have a [default organization](/docs/iac/cli/commands/pulumi_org_set-default/) set, you must specify the org by using the `--publisher` flag.

```bash
pulumi package publish github.com/acme/k8s-cluster --publisher ORG_NAME
```

## API documentation

When a new component or component version is published, API documentation is automatically generated listing the component's inputs and outputs.

Input and output descriptions are generated based on annotations in the code as follows:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
// Use JSDocs-like comments to annotate inputs and outputs.
export interface PetAbstractedArgs {
    /**
     * This input represents the size of the pet name to generate. Valid values are "small", "medium", "large", "xlarge", or a number representing the length of the pet name.
     **/
    size: string;
}

export class PetAbstracted extends pulumi.ComponentResource {
    /**
     * This output provides the generated pet name.
     **/
    public readonly petName: pulumi.Output<string>;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# Use Python docstrings to annotate inputs and outputs.
class PetAbstractedArgs(TypedDict):
    size: pulumi.Input[str]
    """This input represents the size of the pet name to generate. Valid values are "small", "medium", "large", "xlarge", or a number representing the length of the pet name."""

class AppImage(pulumi.ComponentResource):
    pet_name: pulumi.Output[str]
    """This output provides the generated pet name."""
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Use Annotate() to create annotations for go component inputs and outputs.
type PetAbstractedArgs struct {
	Size pulumi.StringInput 	`pulumi:"size"`
}

func (f *PetAbstractedArgs) Annotate(a infer.Annotator) {
	a.Describe(&f.Size, "This input represents the size of the pet name to generate. Valid values are "small", "medium", "large", "xlarge", or a number representing the length of the pet name.")
}

type PetAbstractedOutputs struct {
  PetName pulumi.StringOutput `pulumi:"petName"`
}
func (f *PetAbstractedOutputs) Annotate(a infer.Annotator) {
	a.Describe(&f.PetName, "This output provides the generated pet name.")
}

```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Component API Docs annotations are not currently supported in .NET.
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Component API Docs annotations are not currently supported in Java.
```

{{% /choosable %}}

{{< /chooser >}}

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `error: no README found` | Add a `README.md` to your component's root directory, or use the `--readme` flag to specify a custom location. |
| `error: no version tag found` | Tag your repository with a semver tag (e.g. `git tag v1.0.0`) and push it (`git push origin v1.0.0`). |
| Authentication failures with private repos | Set the `GITHUB_TOKEN` or `GITLAB_TOKEN` environment variable. For GitHub, use `GITHUB_TOKEN="$(gh auth token)"`. |
| Wrong organization | Use the `--publisher` flag to specify the correct organization, or set a default with `pulumi org set-default`. |

## Browsing the registry

The Platform menu in the Pulumi Cloud console includes two package views:

### Registry

![Platform menu showing Registry tab](/docs/idp/concepts/platform-menu.png)

Browse all packages available to your organization, including public providers and components from [pulumi.com/registry](https://www.pulumi.com/registry/) plus your organization's private packages. Features include:

- View documentation for any version of a package
- See usage data showing how packages are adopted across your organization
- Filter by usage status to find packages that need attention

### Private components

This tab shows only the component packages published by your organization via `pulumi package publish`.

### Usage tracking

![Package list showing usage columns and filters](/docs/idp/concepts/usage-columns.png)

Both package list views display usage columns for each package: how many stacks are on the latest version, how many are on older versions, and the total number of stacks using the package. You can filter the list to show only used packages, unused packages, or packages where stacks are running older versions.

Each package page also includes a "Used by" tab showing which stacks use that package, including the stack name, project, version in use, and last update timestamp. This helps you assess the impact of changes before updating versions and identify stacks that may need upgrading.

## Templates

[Organization templates](/docs/idp/concepts/organization-templates/) are an efficient way to scaffold new Pulumi programs. Templates are available to users in the private registry and [New Project Wizard](/docs/idp/concepts/new-project-wizard/).

{{% notes type="info" %}}
Organization templates require the Enterprise or Business Critical plan
{{% /notes %}}

Templates can be published directly to the Private Registry using the `pulumi template publish` command, or sourced from configured GitHub or GitLab repositories. For detailed information on template publishing and management, see [Organization Templates](/docs/idp/concepts/organization-templates/).
