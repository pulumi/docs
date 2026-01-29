---
title_tag: "Cross-language Components"
meta_desc: "Learn how to create Pulumi components that can be consumed in any language with auto-generated SDKs."
title: Cross-language Components
h1: Cross-language Components
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        parent: iac-concepts-components
        weight: 5
aliases:
- /docs/iac/concepts/components/cross-language-components/
---

Cross-language components support consumption in any Pulumi language. You implement the component once in your preferred language, and Pulumi automatically generates SDKs for other languages.

## Adding multi-language support

By default, components are authored and consumed in the same programming language by extending the `ComponentResource` class. The class can then be imported or referenced using the language's applicable pattern. To support consuming components in other languages, Pulumi can introspect your component class and generate the necessary SDKs. To support multi-language consumption, a couple additional steps are required.

### Define a PulumiPlugin.yaml file

In your component directory, create a `PulumiPlugin.yaml` file and specify the runtime the component is authored in.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
runtime: nodejs
```

{{% /choosable %}}
{{% choosable language python %}}

```python
runtime: python
```

{{% /choosable %}}
{{% choosable language go %}}

```go
runtime: go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
runtime: dotnet
```

{{% /choosable %}}
{{% choosable language java %}}

```java
runtime: java
```

{{% /choosable %}}

{{< /chooser >}}

### Define an entry point

The entrypoint analyzes components to automatically build a schema, and interact with the Pulumi engine to manage the component lifecycle.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

Not required for TypeScript.

{{% /choosable %}}
{{% choosable language python %}}

1. Create a `_main_.py` file in your component directory
1. In the `main` function, add a call to `component_provider_host`, specifying a list of components for the `components` argument

```python
from pulumi.provider.experimental import Metadata, component_provider_host
from staticpage import MyComponent

if __name__ == "__main__":
    component_provider_host(name="python-components", components=[MyComponent])
```

{{% /choosable %}}
{{% choosable language go %}}

1. Define a `main.go` file
1. Declare an instance of `NewProviderBuilder`,  passing in a name, namespace and the components being built

{{% notes type="info" %}}
The code below uses the new pulumi-go-provider v1 APIs. Make sure you are using the latest version of `github.com/pulumi/pulumi-go-provider`.
{{% /notes %}}

```go
package main

import (
    "context"
    "log"

    "github.com/pulumi/pulumi-go-provider/infer"
)

func main() {
    prov, err := infer.NewProviderBuilder().
            WithNamespace("your-org-name").
            WithComponents(
                infer.ComponentF(MyComponent),
            ).
            Build()
    if err != nil {
        log.Fatal(err.Error())
    }

    _ = prov.Run(context.Background(), "go-components", "v0.0.1")
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

1. Create a `Program.cs` file
1. Add an entry point that calls the `ComponentProviderHost`

```csharp
using System.Threading.Tasks;

class Program
{
    public static Task Main(string []args) =>
        Pulumi.Experimental.Provider.ComponentProviderHost.Serve(args);
}
```

{{% /choosable %}}
{{% choosable language java %}}

1. Create an `App.java` file
1. Create a new instance of `ComponentProviderHost` in the entry point

```java
package com.example.components;

import java.io.IOException;
import com.pulumi.provider.internal.Metadata;
import com.pulumi.provider.internal.ComponentProviderHost;

public class App {
    public static void main(String[] args) throws IOException, InterruptedException {
        new ComponentProviderHost("java-components", App.class.getPackage()).start(args);
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

## Distribution

### Sharing via Git

Storing a component in a Git repository allows for version control, collaboration, and easier integration into multiple projects. Developers can add the component to their Pulumi projects using the command:

```bash
$ pulumi package add <repo_url>[/path/to/component]@<release-version>
```

The only steps necessary to enable this are to push your component project to a git repo, and create a release tag for the versioning. Pulumi supports referencing both GitHub and GitLab releases. You can also target a standard internally hosted git service, just by providing the repo URL without the `<release-version>` portion.

Pulumi will automatically generate the needed language-specific end user SDK for your project. For example, if the Pulumi project was written in Python, the `pulumi package add` command would detect this and generate the Python SDK on-the-fly, as well as adding the dependency to your `requirements.txt` and running `pip install -r requirements.txt` for you. The output will also give you an example of the correct `import` statement to use the component.

```
$ pulumi package add https://github.com/pulumi/staticpagecomponent@v0.1.0
Downloading provider: github.com_pulumi_staticpagecomponent.git
Successfully generated a Python SDK for the staticpagecomponent package at /example/use-static-page-component/sdks/staticpagecomponent

[...]

You can then import the SDK in your Python code with:

  import pulumi_static_page_component as static_page_component
```

{{< notes type="tip" >}}

Pulumi also supports private repos in GitHub and GitLab. Pulumi will read standard environment variables like `GITHUB_TOKEN` and `GITLAB_TOKEN` if available in order to authenticate access to a private repo during `pulumi package add`.

{{< /notes >}}

### Generating local SDKs with pulumi install

Once you've added an entry to the packages section of your Pulumi.yaml file, you can run `pulumi install` to generate a local SDK in your project. This command will process all packages listed in your Pulumi.yaml and create the necessary SDK files. Check in these files if you want fully reproducible builds, or add them to .gitignore if you prefer to regenerate them on each checkout. When using .gitignore, team members will need to run `pulumi install` after checkout to regenerate the SDK.

### Publishing to Pulumi IDP Private Registry

Once a component is authored, it can be published to the [IDP Private Registry](/docs/idp/get-started/private-registry/) or consumed directly from a git repo.

Pulumi Private Registry is the source of truth for an organization's infrastructure building blocks like components and templates -- the same [components](/docs/iac/concepts/resources/components/) and [templates](/docs/idp/developer-portals/templates/) that power golden path workflows in Pulumi. To learn more about publishing packages to the private registry, check out the [Pulumi Private Registry guide](/docs/idp/get-started/private-registry/).

## Consumption

In the consuming Pulumi application, add the component as a dependency.

```bash
pulumi package add github.com/myorg/my-component
```

If you're using version tags, you can specify those as well.

```bash
pulumi package add github.com/myorg/my-component@v1.0.0
```

Under the hood, Pulumi:

- Fetches your code from GitHub
- Generates a [local package](/docs/iac/guides/building-extending/packages/local-packages/) SDK from the component's schema
- Makes the generated SDK available to your Pulumi program in your chosen language

{{< notes type="info" >}}
For detailed information about working with local packages, including SDK generation and dependency management, see the [Local Packages](/docs/iac/guides/building-extending/packages/local-packages/) guide.
{{< /notes >}}

### Referencing components locally

For scenarios like monorepos, rapid development iterations, or when you're working with components that don't need to be published to a repository, you can reference local source code directly:

```bash
pulumi package add /path/to/local/secure-s3-component
```

Pulumi will identify the folder as a Pulumi component project, generate a local package SDK, and make it available for import in your program—even if your consumer program is in a different language.
