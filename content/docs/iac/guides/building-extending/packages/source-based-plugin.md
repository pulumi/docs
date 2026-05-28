---
title: Authoring a Source-Based Plugin Package
meta_desc: How to author a Pulumi plugin package distributed as source code in TypeScript, Python, Go, C#, or Java so it can be consumed from any Pulumi language.
menu:
  iac:
    parent: iac-guides-packages
    weight: 10
---

A **source-based plugin package** is a Pulumi plugin package distributed as source code rather than a pre-built executable. When a consumer runs `pulumi package add` against your repository or a local path, Pulumi introspects the package and generates an SDK in the consumer's language.

Source-based plugin packages are the recommended way to package and share [components](/docs/iac/concepts/components/) — they enable multi-language consumption with minimal authoring overhead. For a detailed comparison against the other ways to distribute components, see [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/).

{{< notes type="info" >}}
Source-based packages most commonly contain components, and the rest of this guide focuses on that case. When authoring in Go via [`pulumi-go-provider`](https://github.com/pulumi/pulumi-go-provider), a source-based package can also expose [custom resources](/docs/iac/concepts/resources/) and [functions](/docs/iac/concepts/functions/) (invokes); see [Package contents by authoring language](#package-contents-by-authoring-language). For custom resources or functions in other languages, or for publishing to the public [Pulumi Registry](/registry/), author an [executable-based plugin package](/docs/iac/guides/building-extending/packages/executable-plugin/) instead.
{{< /notes >}}

The key wins of the source-based model are:

- **Author in your language of choice, consume in any Pulumi language.** You write the package once in TypeScript, Python, Go, C#, or Java; consumers can use it from any supported Pulumi language, including YAML.
- **No pre-publishing required.** You don't have to build, version, and push per-language SDKs to npm, PyPI, NuGet, Maven, and Go module proxies — a git tag (or even a local path) is enough for consumers to use the package.

{{< notes type="info" >}}
SDKs can still be pre-published for a source-based package, and some teams do so to avoid regenerating the SDK on every consumer's machine or committing the generated SDK to source control. This is uncommon in practice — for internal packages it typically requires maintaining a **private package feed for every consumer language** (private npm registry, private PyPI index, etc.), which is a large amount of infrastructure to stand up just to avoid local SDK generation. The common path is to generate the SDK locally at `pulumi package add` time.
{{< /notes >}}

This guide covers how to author a source-based plugin package: the minimum layout, an end-to-end walkthrough, per-language discovery rules, and per-language features.

For how consumers use the package in their programs, see the [Components](/docs/iac/concepts/components/) concept page. For writing the component code itself, see [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/).

## Minimum plugin layout

Every source-based plugin package has four ingredients:

1. A [`PulumiPlugin.yaml`](/docs/reference/pulumiplugin-yaml/) manifest declaring the authoring language.
1. A language-specific project manifest (`package.json`, `pyproject.toml`, `go.mod`, `.csproj`, or `pom.xml`).
1. An entry file that the language host launches.
1. One or more [`ComponentResource`](/docs/iac/guides/building-extending/components/build-a-component/) subclasses.

A single plugin package can expose **multiple components**; you do not need one package per component. The discovery mechanism described below picks up every component in the package.

## Walkthrough

This walkthrough shows the packaging flow end-to-end. The component implementation itself is intentionally left as a stub — for how to write a component, see [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/).

### 1. Create the plugin directory

```bash
mkdir my-components && cd my-components
```

### 2. Write `PulumiPlugin.yaml`

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```yaml
runtime: nodejs
```

{{% /choosable %}}
{{% choosable language python %}}

```yaml
runtime: python
```

{{% /choosable %}}
{{% choosable language go %}}

```yaml
runtime: go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```yaml
runtime: dotnet
```

{{% /choosable %}}
{{% choosable language java %}}

```yaml
runtime: java
```

{{% /choosable %}}

{{< /chooser >}}

See the [`PulumiPlugin.yaml` reference](/docs/reference/pulumiplugin-yaml/) for all supported fields.

### 3. Assemble the plugin

Below is the minimum directory layout for a plugin containing one component. The shape of the component class itself is up to you — refer to [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/) for authoring guidance. You can add more components to the same package without changing the entry file; they'll be picked up automatically (or via explicit registration, in Go).

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```plain
my-components/
├── PulumiPlugin.yaml
├── package.json       # the name field determines the generated SDK name
├── tsconfig.json
└── index.ts           # entry file — exports your components
```

`index.ts`:

```typescript
import * as pulumi from "@pulumi/pulumi";

export class MyComponent extends pulumi.ComponentResource {
    constructor(name: string, opts?: pulumi.ComponentResourceOptions) {
        super("my-components:index:MyComponent", name, {}, opts);
        this.registerOutputs({});
    }
}
```

Exporting the class from the module named by `main` in `package.json` is all that's required — Pulumi auto-discovers it.

{{% /choosable %}}

{{% choosable language python %}}

```plain
my-components/
├── PulumiPlugin.yaml
├── pyproject.toml         # the name field determines the generated SDK name
├── __main__.py            # entry file — imports your components as top-level names
└── my_components/
    └── components.py      # your ComponentResource classes
```

`__main__.py`:

```python
from my_components.components import MyComponent
```

Importing the class so it becomes a top-level name on the entry module is all that's required — Pulumi auto-discovers it.

{{% /choosable %}}

{{% choosable language go %}}

```plain
my-components/
├── PulumiPlugin.yaml
├── go.mod
├── main.go                # entry file — registers components via pulumi-go-provider
└── provider/
    └── my_component.go    # your ComponentResource struct
```

`main.go`:

```go
package main

import (
    "context"
    "log"

    "github.com/pulumi/pulumi-go-provider/infer"

    "mymodule/provider"
)

func main() {
    prov, err := infer.NewProviderBuilder().
        WithNamespace("my-org").
        WithComponents(infer.ComponentF(provider.NewMyComponent)).
        Build()
    if err != nil {
        log.Fatal(err)
    }
    _ = prov.Run(context.Background(), "my-components", "v0.0.1")
}
```

The generated SDK name is the string passed as the first argument to `prov.Run` (`"my-components"` above). Each component must be listed explicitly in `WithComponents` — Go does not auto-discover.

{{% /choosable %}}

{{% choosable language csharp %}}

```plain
my-components/
├── PulumiPlugin.yaml
├── my-components.csproj   # the assembly name determines the generated SDK name
├── Program.cs             # entry file — hands control to ComponentProviderHost
└── MyComponent.cs         # your ComponentResource class
```

`Program.cs`:

```csharp
using System.Threading.Tasks;
using Pulumi.Experimental.Provider;

class Program
{
    public static Task Main(string[] args) => ComponentProviderHost.Serve(args);
}
```

`ComponentProviderHost.Serve` scans the calling assembly and exposes every `ComponentResource` subclass it finds.

{{% /choosable %}}

{{% choosable language java %}}

```plain
my-components/
├── PulumiPlugin.yaml
├── pom.xml                                     # the artifactId determines the generated SDK name
└── src/main/java/com/example/provider/
    ├── App.java                                # entry file — hands the host a package to scan
    └── MyComponent.java                        # your ComponentResource class
```

`App.java`:

```java
package com.example.provider;

import java.io.IOException;
import com.pulumi.provider.internal.ComponentProviderHost;

public class App {
    public static void main(String[] args) throws IOException, InterruptedException {
        new ComponentProviderHost("my-components", App.class.getPackage()).start(args);
    }
}
```

The generated SDK name is the first argument to the `ComponentProviderHost` constructor (`"my-components"` above). Every `ComponentResource` subclass in the supplied package is exposed automatically.

{{% /choosable %}}

{{< /chooser >}}

### 4. Consume the package from another project

Create a separate Pulumi program — in any supported language, not just the one the plugin was authored in — and add the package by local path:

```bash
cd ..
pulumi new typescript -n consumer --yes
cd consumer
pulumi package add ../my-components
```

Pulumi reads `PulumiPlugin.yaml`, introspects the plugin, generates a local SDK in the consumer's language, and prints the import statement to use. Every component in the package is available under the generated SDK.

To distribute the package more broadly, push it to a Git repository and tag a release; consumers can then run `pulumi package add <repo-url>@<tag>`. See [Distribution](#distribution) below for all available options.

## Per-language authoring

Each language has its own rules for what the entry file must contain, how components are exposed to consumers, and how argument types are inferred for the generated SDK. These differences are a direct consequence of how each language is designed.

Two models are used across the supported languages:

- **Automatic component discovery** scans the plugin at load time and exposes every `ComponentResource` subclass it finds. Depending on the language you may still need a small entry file that hands the provider host an assembly or package to scan, but no per-component registration is required — adding a new component to the package is enough to publish it.
- **Explicit component registration** requires the author to list each component in the entry file. Only listed components are exposed.

### Automatic component discovery

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

Export your component classes from the module named by `main` in your `package.json`. No registration code is required. A minimum plugin consists of `PulumiPlugin.yaml`, `package.json`, `tsconfig.json`, and an entry file like:

```typescript
import * as pulumi from "@pulumi/pulumi";

export interface MyComponentArgs {
    message: pulumi.Input<string>;
}

export class MyComponent extends pulumi.ComponentResource {
    public readonly output: pulumi.Output<string>;
    constructor(name: string, args: MyComponentArgs, opts?: pulumi.ComponentResourceOptions) {
        super("my-package:index:MyComponent", name, args, opts);
        this.output = pulumi.output(args.message);
        this.registerOutputs({ output: this.output });
    }
}
```

{{< notes type="info" >}}
Under the hood, the `pulumi-language-nodejs` host recursively walks the entry module's exports and collects every value whose prototype chain reaches `ComponentResource`. Nested objects and re-exported namespaces are traversed; non-component exports are ignored.

Your args types also appear in the generated SDK, so consumers can construct them in their own language. You don't need to export or register args classes separately — Pulumi finds them by reading the second parameter of each component's constructor using the TypeScript compiler API, then follows the property types (and any types they reference) through imports to build the schema. No decorators or base class are required on the args type.
{{< /notes >}}

{{% /choosable %}}

{{% choosable language python %}}

Make your `ComponentResource` subclasses top-level names in your entry module. A minimum `__main__.py` is just:

```python
from my_package.components import StaticSite, Database
```

{{< notes type="info" >}}
Under the hood, the `pulumi-language-python` host imports the entry module and iterates over its `__dict__`, collecting every class that is a subclass of `ComponentResource`. Only top-level names are scanned — classes imported but not re-exported at module level are skipped.

Your args types also appear in the generated SDK, so consumers can construct them in their own language. You don't need to export or register args classes separately — Pulumi finds them by reading the type annotation on each component's `__init__` `args` parameter. Each field of the args class becomes a property on the generated schema; `Optional[...]` fields become optional. The args class must be type-annotated on `args` and importable from the module being analyzed. No decorators are required.
{{< /notes >}}

{{% /choosable %}}

{{% choosable language go %}}

Not supported. Go lacks the runtime package introspection that the other languages rely on for scanning, so every component must be registered explicitly.

{{% /choosable %}}

{{% choosable language csharp %}}

Call `ComponentProviderHost.Serve` from `Program.cs`. Every `ComponentResource` subclass in your assembly is exposed automatically — no per-component registration is needed.

```csharp
using System.Threading.Tasks;
using Pulumi.Experimental.Provider;

class Program
{
    public static Task Main(string[] args) => ComponentProviderHost.Serve(args);
}
```

{{< notes type="info" >}}
Under the hood, `ComponentProviderHost.Serve` scans the calling assembly via reflection and collects every non-abstract type that inherits from `ComponentResource`, regardless of namespace or visibility. Passing a type that does not inherit from `ComponentResource` causes startup to fail with a clear error.

Your args types also appear in the generated SDK, so consumers can construct them in their own language. You don't need to register args classes separately — Pulumi finds them by looking for a constructor with exactly three parameters (`string`, a `ResourceArgs` subclass, and `ComponentResourceOptions`) and using the second parameter's type. The args class is analyzed via reflection: public fields and properties become schema properties. Nullable CLR types and `[Input(IsRequired = false)]` mark properties optional.
{{< /notes >}}

{{% /choosable %}}

{{% choosable language java %}}

Instantiate `ComponentProviderHost` with the package that contains your components and call `start`. Every `ComponentResource` subclass in that package (and its subpackages) is exposed automatically.

```java
package com.example.provider;

import java.io.IOException;
import com.pulumi.provider.internal.ComponentProviderHost;

public class App {
    public static void main(String[] args) throws IOException, InterruptedException {
        new ComponentProviderHost("my-package", App.class.getPackage()).start(args);
    }
}
```

{{< notes type="info" >}}
Under the hood, the runtime uses the [Reflections](https://github.com/ronmamo/reflections) library to scan the supplied package and its subpackages, collecting every class that extends `ComponentResource`.

Your args types also appear in the generated SDK, so consumers can construct them in their own language. You don't need to register args classes separately — Pulumi finds them by looking for a single constructor that takes `String`, a `ResourceArgs` subclass, and `ComponentResourceOptions`, and using the second parameter's type. The args class is inspected via reflection: public fields become schema properties. `Optional<T>` fields and `@Import(required = false)` mark properties optional.
{{< /notes >}}

{{% /choosable %}}

{{< /chooser >}}

### Explicit component registration

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

Supported but rarely needed — to hide a component from consumers, don't export it from the entry module. If you want the explicit model anyway (for example, to expose a subset of exported classes), call `componentProviderHost` yourself and pass the component classes you want:

```typescript
import { componentProviderHost } from "@pulumi/pulumi/provider/experimental";
import { StaticSite } from "./static-site";
import { Database } from "./database";

componentProviderHost({ components: [StaticSite, Database], name: "my-package" });
```

{{% /choosable %}}

{{% choosable language python %}}

Supported. Call `component_provider_host` yourself and pass the list of components you want to expose:

```python
from pulumi.provider.experimental import component_provider_host
from my_package import StaticSite, Database

if __name__ == "__main__":
    component_provider_host([StaticSite, Database], "my-package", version="1.0.0")
```

{{% /choosable %}}

{{% choosable language go %}}

Go plugins are built using [`pulumi-go-provider`](https://github.com/pulumi/pulumi-go-provider). Each component must be passed to the provider builder's `WithComponents` method. Only components that are explicitly registered are exposed in the generated SDK.

```go
package main

import (
    "context"
    "log"

    "github.com/pulumi/pulumi-go-provider/infer"

    "mymodule/provider"
)

func main() {
    prov, err := infer.NewProviderBuilder().
        WithNamespace("my-org").
        WithComponents(
            infer.ComponentF(provider.NewStaticSite),
            infer.ComponentF(provider.NewDatabase),
        ).
        Build()
    if err != nil {
        log.Fatal(err)
    }
    _ = prov.Run(context.Background(), "my-components", "v0.0.1")
}
```

{{< notes type="info" >}}
Your args types also appear in the generated SDK, so consumers can construct them in their own language. Under the hood, Pulumi finds them by walking the `Args` struct you declare on each component and mapping each field — using the `pulumi:"..."` struct tags, including the `,optional` marker — into the generated schema.
{{< /notes >}}

{{% /choosable %}}

{{% choosable language csharp %}}

Not supported. The .NET provider host always scans an assembly for component types; there is no public API for passing an explicit list of types. To narrow the scan, place components in their own assembly and pass that assembly to `ComponentProviderHost.Serve`.

{{% /choosable %}}

{{% choosable language java %}}

Not supported. The Java provider host always scans a package for component types; there is no public API for passing an explicit list of classes. To narrow the scan, place components in their own package and pass that package to the `ComponentProviderHost` constructor.

{{% /choosable %}}

{{< /chooser >}}

### Consumer runtime requirements

The runtime requirements on the consumer's machine are the same as any Pulumi program written in the authoring language.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}
See the [JavaScript/TypeScript language docs](/docs/iac/languages-sdks/javascript/).
{{% /choosable %}}

{{% choosable language python %}}
See the [Python language docs](/docs/iac/languages-sdks/python/).
{{% /choosable %}}

{{% choosable language go %}}
See the [Go language docs](/docs/iac/languages-sdks/go/).
{{% /choosable %}}

{{% choosable language csharp %}}
See the [.NET language docs](/docs/iac/languages-sdks/dotnet/).
{{% /choosable %}}

{{% choosable language java %}}
See the [Java language docs](/docs/iac/languages-sdks/java/).
{{% /choosable %}}

{{< /chooser >}}

## Package contents by authoring language

Source-based plugins were designed around `ComponentResource`. Custom resources (direct CRUD against an external API) and functions (invokes) are only supported when authoring in Go via `pulumi-go-provider`. In every other language today, anything that isn't a `ComponentResource` is either rejected or silently ignored.

| Language | `ComponentResource` | `CustomResource` | Functions (invokes) |
| --- | --- | --- | --- |
| TypeScript | Supported | Silently ignored | Unsupported |
| Python | Supported | Silently ignored | Unsupported |
| C# / .NET | Supported | Rejected at startup | Unsupported |
| Java | Supported | Silently filtered | Unsupported |
| Go | Supported (`WithComponents`) | **Supported** (`WithResources`) | **Supported** (`WithFunctions`) |

{{< notes type="info" >}}
In a future version of Pulumi, TypeScript and Python will emit a warning when a non-`ComponentResource` is passed where a component is expected, rather than silently ignoring it. See [pulumi/pulumi#22616](https://github.com/pulumi/pulumi/issues/22616) (TypeScript) and [pulumi/pulumi#22617](https://github.com/pulumi/pulumi/issues/22617) (Python).
{{< /notes >}}

## Patterns shared by all languages

Despite the language-specific mechanics, every source-based plugin follows the same four patterns:

1. **Args are discovered transitively.** You never register an args class separately — it is found by analyzing the component's constructor or struct signature.
1. **Schema is inferred from type information.** No explicit schema declaration is needed. Python reads annotations, C# and Java use reflection, TypeScript uses the compiler API, and Go uses struct tags.
1. **Decorators are optional.** Go uses struct tags for metadata; C# and Java offer `[Input]`/`@Import` for fine-grained control but do not require them.
1. **All-or-nothing export.** Once a component is discoverable, every public property of its args class is automatically included in the generated schema.

## Distribution

Once your plugin package is working locally, you have three ways to make it available to consumers.

### Sharing via Git

Storing your package in a Git repository allows for version control, collaboration, and easier integration into multiple projects. Consumers add the package to their programs with:

```bash
pulumi package add <repo_url>[/path/to/component]@<release-version>
```

The only steps to enable this are pushing your package to a Git repo and tagging a release. Pulumi supports both GitHub and GitLab releases, and can also reference self-hosted Git servers — in that case omit the `<release-version>` portion.

Pulumi generates the consumer's language-specific SDK automatically. For example, if the consuming program is Python, `pulumi package add` detects that, generates the Python SDK on-the-fly, adds the dependency to `requirements.txt`, and runs `pip install -r requirements.txt`. The output also prints the correct import statement:

```plain
$ pulumi package add https://github.com/pulumi/staticpagecomponent@v0.1.0
Downloading provider: github.com_pulumi_staticpagecomponent.git
Successfully generated a Python SDK for the staticpagecomponent package at /example/use-static-page-component/sdks/staticpagecomponent

[...]

You can then import the SDK in your Python code with:

  import pulumi_static_page_component as static_page_component
```

{{< notes type="tip" >}}
Pulumi supports private repos in GitHub and GitLab. Pulumi reads standard environment variables like `GITHUB_TOKEN` and `GITLAB_TOKEN` to authenticate access during `pulumi package add`.
{{< /notes >}}

### Publishing to the Pulumi IDP Private Registry

A source-based plugin package can be published to the [IDP Private Registry](/docs/idp/concepts/private-registry/) so it shows up alongside the rest of your organization's infrastructure building blocks — the same [components](/docs/iac/concepts/resources/components/) and [templates](/docs/idp/developer-portals/templates/) that power golden path workflows in Pulumi. See the [Pulumi Private Registry guide](/docs/idp/concepts/private-registry/) for publishing instructions.

### Pre-publishing language SDKs

By default, each consumer generates the SDK locally at `pulumi package add` time. You can instead pre-publish SDKs to language registries (npm, PyPI, Maven, NuGet, Go module proxies) so consumers install them like any other dependency. A typical CI/CD pipeline for one language looks like:

```bash
git tag v1.0.0
git push origin v1.0.0
pulumi package publish github.com/myorg/my-component@1.0.0
pulumi package gen-sdk . --language nodejs --out sdk/nodejs
npm publish
```

Repeat the `pulumi package gen-sdk` and publish steps for each language you want to support. Consumers then install the SDK directly via their package manager (e.g., `npm install my-component`) without generating it themselves.

## Next steps

- [PulumiPlugin.yaml reference](/docs/reference/pulumiplugin-yaml/) — full field reference for the plugin manifest.
- [Local Packages](/docs/iac/guides/building-extending/packages/local-packages/) — develop and iterate on a package before publishing.
- [Publishing Packages](/docs/iac/guides/building-extending/packages/publishing-packages/) — distribute your package via Git, the IDP Private Registry, or language-specific registries.
- [Package Schema](/docs/iac/guides/building-extending/packages/schema/) — the schema format that drives SDK generation.
- [Components](/docs/iac/concepts/components/) — how consumers pull your package into their programs.
