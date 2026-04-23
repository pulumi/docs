---
title_tag: PulumiPlugin.yaml Reference
meta_desc: Documentation of the settings that are valid for the PulumiPlugin.yaml plugin manifest used by source-based component packages.
title: PulumiPlugin.yaml Reference
h1: PulumiPlugin.yaml Reference
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    reference:
        name: PulumiPlugin.yaml
        parent: reference-home
        weight: 20
---

`PulumiPlugin.yaml` is the manifest for a source-based component package. Place it at the root of a component package's source directory to declare the authoring language so Pulumi can load the plugin and introspect its components.

## Relationship to `Pulumi.yaml`

`PulumiPlugin.yaml` and [`Pulumi.yaml`](/docs/iac/concepts/projects/project-file/) serve different roles:

- `Pulumi.yaml` is a **program** manifest. It sits at the root of a Pulumi project and declares the project name, runtime, and configuration for `pulumi up`.
- `PulumiPlugin.yaml` is a **plugin** manifest. It sits at the root of a source-based component package and declares the runtime that the plugin itself is written in, so the Pulumi CLI knows how to launch it when a consumer runs `pulumi package add`.

A source-based component package that is also a runnable Pulumi program (for example, one used for local testing) can contain both files.

## Attributes

| Name | Required | Description | Options |
| - | - | - | - |
| `runtime` | required | Language runtime the plugin is authored in. | `nodejs`, `python`, `go`, `dotnet`, `java` |
| `main` | optional | Path to the plugin's entry point, relative to the manifest. Only needed when the entry point can't be auto-detected. | None |

### `runtime`

The value of `runtime` determines which language host Pulumi launches when loading the plugin, and which toolchain is used to introspect the plugin's components.

| Value | Authoring language |
| - | - |
| `nodejs` | TypeScript or JavaScript |
| `python` | Python |
| `go` | Go (via [`pulumi-go-provider`](https://github.com/pulumi/pulumi-go-provider)) |
| `dotnet` | C# or other .NET languages |
| `java` | Java |

YAML cannot be used to author source-based component packages; it is a consumer-only language.

### `main`

Most language runtimes can locate the plugin entry point by convention (for example, the `main` field of `package.json` for Node.js, or `__main__.py` at the package root for Python). Set `main` only when your project layout does not match the default.

## Example

```yaml
runtime: nodejs
```

```yaml
runtime: python
main: src/provider/__main__.py
```

## See also

- [Authoring a source-based component package](/docs/iac/guides/building-extending/packages/source-based-plugin/) — end-to-end guide that uses this file.
- [Components](/docs/iac/concepts/components/) — the concept page covering how components are consumed (including across languages) from a source-based plugin package.
- [`Pulumi.yaml` project file reference](/docs/iac/concepts/projects/project-file/).
