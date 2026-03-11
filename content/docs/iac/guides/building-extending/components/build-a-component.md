---
title_tag: "Build a Component"
meta_desc: "Learn the process for building a custom Pulumi Component."
title: Build a Component
h1: Build a Component
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Build a Component
        parent: iac-guides-components
        weight: 10
aliases:
- /docs/iac/using-pulumi/build-a-component/
- /docs/iac/using-pulumi/extending-pulumi/build-a-component/
---

This guide will walk you through the steps of making a Pulumi Component suitable for reuse in all languages and cloud environments.

{{< notes type="info" >}}
**Prerequisites:**

- The [Pulumi CLI](/docs/install/)
- One of Pulumi’s [supported language runtimes](/docs/languages-sdks/) installed
- Access to a Git hosting environment *(optional)*

{{< /notes >}}

## Why Write a Component?

[Pulumi Components](/docs/iac/concepts/resources/components/) provide a way to encapsulate best practices, ensuring that security policies and deployment patterns remain consistent across projects. They also help reduce code duplication by allowing you to define reusable infrastructure patterns. By structuring infrastructure as components, maintainability improves, and teams can work more efficiently.

### Key features:

- **Sharing and Reusability**: Do more with less code. Don't repeat yourself.
- **Best Practices and Policy**: Encode company standards and policy, across all languages and cloud environments.
- **Multi-language Support**: Write in one language, use in any language.

## How It Works

Pulumi Components are implemented as custom classes in any Pulumi-supported language. Once defined, they can be used locally, referenced from a Git repository, or published as a Pulumi package for broader distribution. A component extends `pulumi.ComponentResource` and groups multiple resources into a single, reusable abstraction. This approach enables developers to define infrastructure once and apply it consistently across multiple environments.

Pulumi Components inherently support multi-language use. Regardless of the language a component was written in, it is a fast one-step process to generate a SDK, allowing you to use it in all Pulumi-supported languages.

{{< notes type="warning" >}}
If your component uses a local package (such as any Terraform provider via `terraform-provider`, or another component that contains a local package), you must commit the generated SDK code to version control. See [Using components with local packages](/docs/iac/guides/building-extending/packages/local-packages/#components-with-local-packages) for details.
{{< /notes >}}

## Structure of a Component

A Pulumi Component consists of three main parts:

- The **component resource** encapsulates multiple Pulumi resources, grouping them into a logical unit.
- The **component resource arguments** define configurable input properties, allowing users to specify parameters that tailor the component's behavior to specific needs.
- The **provider host** registers and runs your component resources, acting as the foundational layer for component creation.

{{< notes type="info" >}}
Not all [resource options](/docs/iac/concepts/resources/options/) apply to component resources. For example, `ignoreChanges` and `customTimeouts` have no effect on components themselves. To see which options work with components and how to apply options to child resources using `transforms`, see [Resource options and component resources](/docs/iac/concepts/resources/options/#resource-options-and-component-resources).
{{< /notes >}}

## Example: Static Web Page Component

In this example, we'll create a static website component in AWS Simple Storage Service (S3). The component will manage the following five sub-resources necessary to implement a basic S3 hosted static website:

- a [`Bucket`](/registry/packages/aws/api-docs/s3/bucket/) resource
- a [`BucketWebsiteConfiguration`](/registry/packages/aws/api-docs/s3/bucketwebsiteconfiguration/) resource to set up the website configuration
- a [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) resource to hold the raw site content
- a [`BucketPublicAccessBlock`](/registry/packages/aws/api-docs/s3/bucketpublicaccessblock/) resource to manage public access
- a [`BucketPolicy`](/registry/packages/aws/api-docs/s3/bucketpolicy/) resource to set the Bucket policy

The component will take as input the contents of the file you wish to host, and will output the S3 endpoint used to access it.

***Example:** Using the custom StaticPage component in a Pulumi Program*

{{< example-program path="sample-components" languages="yaml" >}}

The core implementation of the AWS API is handled by the [Pulumi AWS Provider](/registry/packages/aws/), which gives us those five underlying resource types. Our `StaticPage` component will work with those existing types and create a new type of resource with a simpler API.

### Setting up your Component project

A Pulumi Component is a separate project from your Pulumi program. So, let's create a new directory for it, and create some project files:

```bash
$ mkdir sample-components
$ cd sample-components
```

#### PulumiPlugin.yaml

The `PulumiPlugin.yaml` file tells Pulumi that this directory is a component, rather than a Pulumi program. In it, we define the language runtime needed to load the plugin.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

***Example:** `PulumiPlugin.yaml` for TypeScript*

```yaml
name: sample-components
version: 0.1.0
runtime: nodejs
```

#### Manage dependencies

Next, we need to define our dependencies in `package.json`.

***Example:** `package.json` for a Pulumi Component*

```json
{
    "name": "sample-components",
    "description": "Static Page Component",
    "dependencies": {
        "@pulumi/aws": "^7.6.0",
        "@pulumi/pulumi": "^3.191.0"
    },
    "devDependencies": {
        "@types/node": "^24.0.0",
        "typescript": "^5.9.2"
    }
}
```

The `@pulumi/pulumi` SDK contains everything we need for making a component. The `@pulumi/aws` package is the AWS provider that we are building on top of.

{{< notes type="info" >}}
When building components that will be consumed by other projects, be aware of how package managers handle provider package versions. See [Provider package version management](/docs/iac/languages-sdks/javascript/provider-package-versions/) for guidance on managing provider dependencies across component boundaries.
{{< /notes >}}

#### TypeScript project file

We'll also need a TypeScript project file called `tsconfig.json`.

```json
{
    "compilerOptions": {
        "strict": true,
        "outDir": "bin",
        "target": "es2016",
        "module": "commonjs",
        "moduleResolution": "node",
        "sourceMap": true,
        "experimentalDecorators": true,
        "pretty": true,
        "noFallthroughCasesInSwitch": true,
        "noImplicitReturns": true,
        "forceConsistentCasingInFileNames": true
    },
    "files": [
        "index.ts",
        "StaticPage.ts"
    ]
}
```

Finally, install dependencies via NPM:

```bash
$ npm install
```

#### Build the component

Once dependencies are installed, build the TypeScript component:

```bash
$ npx tsc
```

This compiles the TypeScript files and generates the JavaScript output in the `bin` directory.

{{% /choosable %}}

{{% choosable language python %}}

***Example:** `PulumiPlugin.yaml` for Python*

```yaml
name: sample-components
version: 0.1.0
runtime: python
```

#### Manage dependencies

Next, we need to define our dependencies in `requirements.txt`.

***Example:** `requirements.txt` for a Pulumi Component*

```txt
pulumi>=3.191.0,<4.0
pulumi_aws>=7.6.0,<8.0
```

The `pulumi` SDK contains everything we need for making a component. The `pulumi_aws` package is the AWS provider that we are building on top of.
{{% /choosable %}}

{{% choosable language go %}}

***Example:** `PulumiPlugin.yaml` for Go*

```yaml
name: sample-components
version: 0.1.0
runtime: go
```

#### Manage dependencies

Next, we need to define our dependencies in `go.mod`.

***Example:** `go.mod` for a Pulumi Component*

```go
module github.com/sample-components

go 1.25

require (
	github.com/pulumi/pulumi-aws/sdk/v7 v7.6.0
	github.com/pulumi/pulumi/sdk/v3 v3.191.0
)
```

The `pulumi` SDK contains everything we need for making a component. The `pulumi-aws` package is the AWS provider that we are building on top of.

{{% /choosable %}}

{{% choosable language csharp %}}

***Example:** `PulumiPlugin.yaml` for C#*

```yaml
name: sample-components
version: 0.1.0
runtime: dotnet
```

#### Manage dependencies

Next, we need to define our dependencies in `StaticPageComponent.csproj`.

***Example:** `StaticPageComponent.csproj` for a Pulumi Component*

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <AssemblyName>sample-components</AssemblyName>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Pulumi" Version="3.87.0" />
    <PackageReference Include="Pulumi.AWS" Version="7.*" />
    <PackageReference Include="Newtonsoft.Json" Version="13.*" />
  </ItemGroup>
</Project>
```

The `Pulumi` SDK contains everything we need for making a component. The `Pulumi.Aws` package is the AWS provider that we are building on top of.

Note that the `AssemblyName` specifies the name of the component package. This name will be important later on in the component implementation, so make sure it's something unique and descriptive!

{{% /choosable %}}

{{% choosable language java %}}

***Example:** `PulumiPlugin.yaml` for Java*

```yaml
name: sample-components
version: 0.1.0
runtime: java
```

#### Manage dependencies

Next, we need to define our dependencies and project configuration in a Maven `pom.xml`.

***Example:** `pom.xml` for a Pulumi Component*

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.pulumi</groupId>
  <artifactId>sample-components</artifactId>
  <version>1.0-SNAPSHOT</version>

  <properties>
    <encoding>UTF-8</encoding>
    <maven.compiler.source>11</maven.compiler.source>
    <maven.compiler.target>11</maven.compiler.target>
    <maven.compiler.release>11</maven.compiler.release>
    <mainClass>staticpagecomponent.App</mainClass>
    <mainArgs/>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-nop</artifactId>
      <version>2.0.17</version>
    </dependency>
    <dependency>
      <groupId>com.google.code.gson</groupId>
      <artifactId>gson</artifactId>
      <version>2.13.1</version>
    </dependency>
    <dependency>
      <groupId>com.pulumi</groupId>
      <artifactId>pulumi</artifactId>
      <version>1.16.1</version>
    </dependency>
    <dependency>
      <groupId>com.pulumi</groupId>
      <artifactId>aws</artifactId>
      <version>(7.6.0,7.99]</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.0.0</version>
        <configuration>
          <mainClass>${mainClass}</mainClass>
          <commandlineArgs>${mainArgs}</commandlineArgs>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

The `com.pulumi.pulumi` SDK contains everything we need for making a component. The `com.pulumi.aws` package is the AWS provider that we are building on top of. We've also included a couple helper libraries like `gson` and `slf4j-nop` which are helpful for this example.

{{% /choosable %}}

{{< /chooser >}}

### Implement the entrypoint

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

First, create the `index.ts` file, where we will export the component class.

***Example:** `index.ts` component export*

```typescript
export { StaticPage } from "./staticpage";
```

{{% /choosable %}}

{{% choosable language python %}}

First, create the `__main__.py` file, where we will define an entry point for the component.

***Example:** `__main__.py` component entry point*

```python
from pulumi.provider.experimental import component_provider_host
from staticpage import StaticPage

if __name__ == "__main__":
    component_provider_host(name="sample-components", components=[StaticPage])
```

Here, the `component_provider_host` call invokes a Pulumi provider implementation which acts as a shim for the component. The name we pass to it will be important later on in the component implementation, so make sure it's something unique and descriptive!

{{% /choosable %}}

{{% choosable language go %}}

First, create the `main.go` file, where we will define an entry point for the component.

***Example:** `main.go` component entry point*

```go
package main

import (
	"context"
	"fmt"
	"os"

	p "github.com/pulumi/pulumi-go-provider"
	"github.com/pulumi/pulumi-go-provider/infer"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
)

func main() {
	provider, err := provider()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %s", err.Error())
		os.Exit(1)
	}
	err = provider.Run(context.Background(), "sample-components", "0.1.0")

	if err != nil {
		panic(err)
	}
}

func provider() (p.Provider, error) {
	return infer.NewProviderBuilder().
		WithNamespace("example.com").
		WithComponents(
			infer.ComponentF(NewStaticPage),
		).
		WithModuleMap(map[tokens.ModuleName]tokens.ModuleName{
			"sample-components": "index",
		}).
		Build()
}
```

Here, the `infer.NewProviderBuilder()..Build()` call builds a Pulumi provider implementation which acts as a shim for the component. Then, in the `main` function we call `provider.Run(...)` to execute the provider. The name we pass to this function and to the module map (`sample-components`) will be important later on in the component implementation, so make sure it's something unique and descriptive!

{{% /choosable %}}

{{% choosable language csharp %}}

First, create the `Program.cs` file, where we will define an entry point for the component.

***Example:** `Program.cs` component entry point*

```csharp
using System.Threading.Tasks;

class Program
{
    public static Task Main(string []args) =>
        Pulumi.Experimental.Provider.ComponentProviderHost.Serve(args);
}
```

Here, the `ComponentProviderHost.Serve` call invokes a Pulumi provider implementation which acts as a shim for the component. Everything else about your component will be inferred by the Pulumi SDK.

{{% /choosable %}}

{{% choosable language java %}}

First, create the `src/main/java/staticpagecomponent` sub-directory and in it, create the `App.java` file, where we will define an entry point for the component.

***Example:** `App.java` component entry point*

```java
package staticpagecomponent;

import java.io.IOException;
import com.pulumi.provider.internal.ComponentProviderHost;

public class App {
    public static void main(String[] args) throws IOException, InterruptedException {
        new ComponentProviderHost("sample-components", App.class.getPackage()).start(args);
    }
}
```

Here, the `ComponentProviderHost.start(...)` call invokes a Pulumi provider implementation which acts as a shim for the component. The name we pass to it will be important later on in the component implementation, so make sure it's something unique and descriptive!

We also need to pass the Java package so that your component classes can be inferred by the Pulumi SDK.

{{% /choosable %}}

{{% choosable language yaml %}}

Because YAML is entirely declarative, unlike in our other languages, there's no need define an entry point.

{{% /choosable %}}

{{< /chooser >}}

### Implement the Component

Next we will define the classes that implement our reusable component.

Components typically require two parts: a subclass of `pulumi.ComponentResource` that implements the component, and an *arguments* class, which is used to configure the component during construction.

#### Add the required imports

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

First create a file called `StaticPage.ts`, and add the imports we will need:

***Example:** `StaticPage.ts` required imports*

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:1-2" >}}

The `@pulumi/pulumi` package is the core Pulumi SDK, which provides the base classes and types needed to define components and resources. The `@pulumi/aws` package is the Pulumi AWS provider, which gives us the resource types we need to create AWS infrastructure.

{{% /choosable %}}

{{% choosable language python %}}

First create a file called `static_page.py`, and add the imports we will need:

***Example:** `static_page.py` required dependencies*

{{< example-program path="sample-components" languages="python:static_page.py:1-6" >}}

The `pulumi` package is the core Pulumi SDK, which provides the base classes and types needed to define components and resources. The `pulumi_aws` package is the Pulumi AWS provider, which gives us the resource types we need to create AWS infrastructure.

{{% /choosable %}}

{{% choosable language go %}}

First create a directory called `staticpagecomponent` and create a file called `static_page.go` inside it. This will be our importable Go package:

***Example:** `staticpagecomponent/static_page.go` required dependencies*

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:1-9" >}}

The `github.com/pulumi/pulumi/sdk/v3/go/pulumi` package is the core Pulumi SDK, which provides the base types needed to define components and resources. The `github.com/pulumi/pulumi-aws/sdk/v7/go/aws/s3` package is the Pulumi AWS provider's S3 module, which gives us the resource types we need to create AWS infrastructure.

{{% /choosable %}}

{{% choosable language csharp %}}

First create a file called `StaticPage.cs`, and add the imports we will need:

***Example:** `StaticPage.cs` required imports*

{{< example-program path="sample-components" languages="csharp:StaticPage.cs:1-8" >}}

The `Pulumi` namespace is the core Pulumi SDK, which provides the base classes and types needed to define components and resources. The `Pulumi.Aws.S3` namespace is from the Pulumi AWS provider, which gives us the resource types we need to create AWS infrastructure.

{{% /choosable %}}

{{% choosable language java %}}

First create a file called `StaticPage.java`, and add the imports we will need:

***Example:** `StaticPage.java` required imports*

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:1-24" >}}

The `com.pulumi.resources` and `com.pulumi.core` packages are from the core Pulumi SDK, which provide the base classes and types needed to define components and resources. The `com.pulumi.aws.s3` package is from the Pulumi AWS provider, which gives us the resource types we need to create AWS infrastructure.

{{% /choosable %}}

{{% choosable language yaml %}}

YAML components do not need to explicitly manage dependencies or import external libraries. The necessary packages will be resolved and automatically installed by the Pulumi engine, based on the unique resource type identifiers in the component's sub-resources.

{{% /choosable %}}

{{< /chooser >}}

### Define the Component arguments

Next, we will implement the arguments class. In our example here, we will pass the contents of the webpage we want to host to the component.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

***Example:** `StaticPage.ts` the Component arguments implementation*

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:4-6" >}}

Note that argument classes must be *serializable* and use `pulumi.Input` types, rather than the language's default types. Certain types like union types (e.g., `string | number`) and functions are not supported due to schema inference limitations. For details on type requirements and limitations, see [Component arguments and type requirements](/docs/iac/concepts/components/#component-arguments-and-type-requirements).

{{% /choosable %}}

{{% choosable language python %}}

***Example:** `static_page.py` the Component arguments implementation*

{{< example-program path="sample-components" languages="python:static_page.py:9-11" >}}

Note that argument classes must be *serializable* and use `pulumi.Input` types, rather than the language's default types. This means certain types like union types and functions are not supported. For details on type requirements and limitations, see [Component arguments and type requirements](/docs/iac/concepts/components/#component-arguments-and-type-requirements).

Python class properties are typically written in lowercase with words separated by underscores, known as [`snake_case`](https://en.wikipedia.org/wiki/Snake_case), however properties in the [Pulumi package schema](https://www.pulumi.com/docs/iac/using-pulumi/extending-pulumi/schema/) are usually written in [`camelCase`](https://en.wikipedia.org/wiki/Camel_case), where capital letters are used to separate words. To follow these conventions, the inferred schema for a component will have translated property names. In our example `index_content` will become `indexContent` in the schema. When using a component, the property names will follow the conventions of that language, for example if we use our component from TypeScript, we would refer to `indexContent`, but if we use it from Python, we would use `index_content`.

{{% /choosable %}}

{{% choosable language go %}}
***Example:** `static_page.go` the Component arguments implementation*

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:11-13" >}}

Note that argument classes must be *serializable* and use `pulumi.Input` types, rather than the language's default types. This means complex or platform-specific types may not be supported. For details on type requirements and limitations, see [Component arguments and type requirements](/docs/iac/concepts/components/#component-arguments-and-type-requirements).

Go struct fields are typically written in title case, with the first letter capitalized and capital letters used to separate words, however properties in the [Pulumi package schema](https://www.pulumi.com/docs/iac/using-pulumi/extending-pulumi/schema/) are usually written in [`camelCase`](https://en.wikipedia.org/wiki/Camel_case), with the first letter in lowercase and capital letters used to separate words. To follow these conventions, the inferred schema for a component will have translated property names. In our example `IndexContent` will become `indexContent` in the schema. When using a component, the property names will follow the conventions of that language, for example if we use our component from TypeScript, we would refer to `indexContent`, but if we use it from Go, we would use `IndexContent`.

{{% /choosable %}}

{{% choosable language csharp %}}

***Example:** `StaticPage.cs` the Component arguments implementation*

{{< example-program path="sample-components" languages="csharp:StaticPage.cs:10-13" >}}

Note that argument classes must be *serializable* and use `Pulumi.Input` types, rather than the language's default types. This means complex or platform-specific types may not be supported. For details on type requirements and limitations, see [Component arguments and type requirements](/docs/iac/concepts/components/#component-arguments-and-type-requirements).

{{% /choosable %}}

{{% choosable language java %}}

***Example:** `StaticPage.java` the Component arguments implementation*

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:26-40" >}}

Note that argument classes must be *serializable* and use `com.pulumi.core.Output<T>` types, rather than the language's default types. This means complex or platform-specific types may not be supported. For details on type requirements and limitations, see [Component arguments and type requirements](/docs/iac/concepts/components/#component-arguments-and-type-requirements).

The `@Import` decorator marks this as a *required* input and allows use to give a name for the input that could be different from the implementation here.

{{% /choosable %}}

{{% choosable language yaml %}}

In YAML, rather than defining a separate args class, the inputs are declared under the [`inputs` key](/docs/iac/languages-sdks/yaml/yaml-component-reference/#inputs):

***Example:** `PulumiPlugin.yaml` the Component arguments implementation*

{{< example-program path="sample-components" languages="yaml:sample-components/PulumiPlugin.yaml:5-7" >}}

Inputs can be any basic type (e.g. `boolean`, `integer`, `string`) or an `array` of any of those types. You can provide a default value via the `default` property.

{{% /choosable %}}

{{< /chooser >}}

### Define the Component resource

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

Now we can implement the component itself. Components should inherit from `pulumi.ComponentResource`, and should accept the arguments class we just defined in the constructor. All the work for our component happens in the constructor, and outputs are returned via class properties. At the end of the process a calling `self.registerOutputs` signals Pulumi that the process of creating the component resource has completed.

***Example:** `StaticPage.ts` the Component implementation*

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:8-67" >}}

{{% /choosable %}}

{{% choosable language python %}}

Now we can implement the component itself. Components should inherit from `pulumi.ComponentResource`, and should accept the arguments class we just defined in the constructor. All the work for our component happens in the constructor, and outputs are returned via class properties. At the end of the process a calling `self.register_outputs` signals Pulumi that the process of creating the component resource has completed.

***Example:** `static_page.py` the Component implementation*

{{< example-program path="sample-components" languages="python:static_page.py:14-59" >}}

{{% /choosable %}}

{{% choosable language go %}}
Now we can implement the component itself. Component structs should include `pulumi.ResourceState` and define the consumable outputs, which follow the same general rules as inputs. All the work for building our component happens in the `NewStaticPage` constructor.

***Example:** `static_page.go` the Component implementation*

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:15-96" >}}

{{% /choosable %}}

{{% choosable language csharp %}}

Now we can implement the component itself. Components should inherit from `Pulumi.ComponentResource`, and should accept the arguments class we just defined in the constructor. All the work for our component happens in the constructor, and outputs are returned via class properties. At the end of the process a calling `this.RegisterOutputs` signals Pulumi that the process of creating the component resource has completed.

***Example:** `StaticPage.cs` the Component implementation*

{{< example-program path="sample-components" languages="csharp:StaticPage.cs:15-68" >}}

{{% /choosable %}}

{{% choosable language java %}}

Now we can implement the component itself. Components should inherit from `Pulumi.ComponentResource`, and should accept the arguments class we just defined in the constructor. All the work for our component happens in the constructor, and outputs are returned via class properties. At the end of the process a calling `this.registerOutputs` signals Pulumi that the process of creating the component resource has completed.

***Example:** `StaticPage.java` the Component implementation*

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:42-125" >}}

{{% /choosable %}}

{{% choosable language yaml %}}

Now we can implement the component itself. Under the [`components` key](/docs/iac/languages-sdks/yaml/yaml-component-reference/), create one or more component definitions. A component in YAML follows the following structure:

```yaml
components:
  MyComponent:      # the component class name
    inputs:         # one or more input values
    resources:      # one or more sub-resource definitions
    variables:      # intermediate variable definitions
    outputs:        # one or more output values
```

Here's the full code for our `StaticPage` component:

***Example:** `PulumiPlugin.yaml` the Component implementation*

{{< example-program path="sample-components" languages="yaml:sample-components/PulumiPlugin.yaml:3-56" >}}

{{% /choosable %}}

{{< /chooser >}}

### Detailed implementation breakdown

Let's dissect this component implementation piece-by-piece:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

#### Inheriting from the base class

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:8-8" >}}

Inheriting from `pulumi.ComponentResource` gives us some built-in behind-the-scenes behavior that allows the component state to be tracked and run within the Pulumi engine and within its host provider. It also allows the underlying library to find and infer the schema of the component.

#### Outputs as class properties

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:9-9" >}}

We use a class property to store the output value. Component outputs should always use `pulumi.Output<T>` rather than plain types. This ensures that outputs can be passed directly to other Pulumi resource inputs, which also accept `pulumi.Output<T>`, without any additional unwrapping or conversion.

#### The Component constructor

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:11-12" >}}

The constructor has a few standard arguments:

- `name`: The name given to an instance of this component. When writing a Pulumi program, resources are named by the end-user. Later on in the implementation we will use this base component name to uniquely name the resources it contains.
- `args`: This is an instance of the argument class we defined earlier, containing the inputs for our component.
- `opts`: This is an *optional* set of common resource configuration values. The [`ComponentResourceOptions`](/docs/iac/concepts/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our sub-resources later on.

Since we're inheriting, we also need to call the base class constructor `super(...)`. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:index:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The `index` portion of this type name is a required implementation detail. Otherwise, we pass the `name`, `args`, and `opts` values from our component constructor into the base constructor.

{{< notes type="warning" >}}
Changing the resource type name after a component has been deployed will cause all existing resources of that type to be recreated. Change the type name with extreme caution.
{{< /notes >}}

#### Creating and managing sub-resources, dependencies, and execution order

Next we implement the `Bucket`, `BucketWebsiteConfiguration`, `BucketObject`, `BucketPublicAccessBlock` and `BucketPolicy` sub-resources.

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:14-45" >}}

##### The Bucket sub-resource

The `Bucket` resource represents an S3 bucket, which is similar to a directory. This is our public-facing entry point for hosting website content on the internet.

Notice the use of the `name` parameter and format string to create a unique name for the bucket resource. Every resource must have a unique name. We will use the same pattern in all the sub-resources.

Another important implementation detail here is the `opts` value being passed to the sub-resource constructor. We create a new instance of `ResourceOptions` and pass the component instance as the `parent` of the `Bucket` resource, via `parent: this` in the `ResourceOptions` class. This is an essential step to tie the sub-resources into the dependency graph.

##### The BucketWebsiteConfiguration and BucketObject sub-resources

The `BucketWebsiteConfiguration` represents the website configuration and the `BucketObject` represents the contents of the file we will host as `index.html`.

Managing the dependency graph of your sub-resources is very important in a component!

Another point of interest here is the use of `args`. In the `BucketObject` constructor, we pass the contents of the `index.html` page we want to host via the `args` class. It's available as a strongly typed property accessor on the args class.

##### The BucketPublicAccessBlock and BucketPolicy sub-resources

By default the `BucketObject` we created is not accessible to the public, so we need to unlock that access with the `BucketPublicAccessBlock` and `BucketPolicy` resources.

The `BucketPolicy` resource shows an important coding technique when implementing components: handling asynchronous output values. We use `bucket.bucket.apply(...)` to generate an S3 policy document using the `allowGetObjectPolicy` helper function. This respects the asynchronous workflow, materializing that value only after the bucket has been created. If we attempted to create a `BucketPolicy` before the `Bucket` existed, the operation would fail. That's because the S3 policy document needs to use the bucket's name within its definition, and we won't know what that value is until the Bucket creation operation has completed. Using `apply` here will ensure that execution of the `allowGetObjectPolicy` function doesn't happen until the bucket has been created successfully.

Just like in a Pulumi program, it's important to understand and respect the asynchronous flow of resource creation within our code. The `apply` function encodes the dependency and required order-of-operations.

The `BucketPolicy` resource also shows another technique: resource dependencies. We use the `dependsOn` resource option to indicate that the `BucketPolicy` depends on the `BucketPublicAccessBlock`. This relationship is important to encode so that resource creation, modification, and deletion happens as expected.

#### Handling outputs

The last part of the constructor handles output values. First we set the `endpoint` class property to the website endpoint from the `BucketWebsiteConfiguration` class. Note that this is a `pulumi.Output<string>`, not a regular TypeScript string. Outputs must use `pulumi.Output` types.

Finally, calling `this.registerOutputs` signals Pulumi that the component creation process has completed.

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:47-52" >}}

#### Helper functions

In addition to the constructor logic, we also have a helper function `allowGetObjectPolicy`:

***Example:** `StaticPage.ts` a helper function*

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:54-66" >}}

This function is used to create a S3 policy document, allowing public access to the objects in our bucket. It will be invoked within the context of `apply(...)`. That means that the `bucketName`, which is normally a `pulumi.Output<str>` value, can be materialized as a normal TypeScript string, and is passed into this function that way. Note that you can't modify the value of `bucketName`, but you can *read* the value and use it to construct the policy document. The `JSON.stringify(...)` function takes the object as input and returns it as a JSON formatted string.

{{% /choosable %}}

{{% choosable language python %}}

#### Inheriting from the base class

{{< example-program path="sample-components" languages="python:static_page.py:14-14" >}}

Inheriting from `pulumi.ComponentResource` gives us some built-in behind-the-scenes behavior that allows the component state to be tracked and run within the Pulumi engine. It also allows the underlying library to find and infer the schema of the component.

#### Outputs as class properties

{{< example-program path="sample-components" languages="python:static_page.py:15-16" >}}

We use a class property to store the output value. Component outputs should always use `pulumi.Output[T]` rather than plain types. This ensures that outputs can be passed directly to other Pulumi resource inputs, which also accept `pulumi.Output[T]`, without any additional unwrapping or conversion.

#### The Component constructor

{{< example-program path="sample-components" languages="python:static_page.py:18-23" >}}

The constructor has a few standard arguments:

- `name`: The name given to an instance of this component. When writing a Pulumi program, resources are named by the end-user. Later on in the implementation we will use this base component name to uniquely name the resources it contains.
- `args`: This is an instance of the argument class we defined earlier, containing the inputs for our component.
- `opts`: This is an *optional* set of common resource configuration values. The [`ComponentResourceOptions`](/docs/iac/concepts/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our sub-resources later on.

Since we're inheriting, we also need to call the base class constructor `super().__init__`. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:index:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The `index` portion of this type name is a required implementation detail. Otherwise, we pass the `name` value into the base constructor, as well as the `opts` value, and an empty object for the `args` value.

{{< notes type="warning" >}}
Changing the resource type name after a component has been deployed will cause all existing resources of that type to be recreated. Change the type name with extreme caution.
{{< /notes >}}

#### Creating and managing sub-resources, dependencies, and execution order

Next we implement the `Bucket`, `BucketWebsiteConfiguration`, `BucketObject`, `BucketPublicAccessBlock` and `BucketPolicy` sub-resources.

{{< example-program path="sample-components" languages="python:static_page.py:25-53" >}}

##### The Bucket sub-resource

The `Bucket` resource represents an S3 bucket, which is similar to a directory. This is our public-facing entry point for hosting website content on the internet.

Notice the use of the `name` parameter and format string to create a unique name for the bucket resource. Every resource must have a unique name. We will use the same pattern in all the sub-resources.

Another important implementation detail here is the `opts` value being passed to the sub-resource constructor. We create a new instance of `ResourceOptions` and pass the component instance as the `parent` of the `Bucket` resource, via `parent=self` in the `ResourceOptions` class. This is an essential step to tie the sub-resources into the dependency graph.

##### The BucketWebsiteConfiguration and BucketObject sub-resources

The `BucketWebsiteConfiguration` represents the website configuration and the `BucketObject` represents the contents of the file we will host as `index.html`.

Managing the dependency graph of your sub-resources is very important in a component!

Another point of interest here is the use of `args`. In the `BucketObject` constructor, we pass the contents of the `index.html` page we want to host via the `args` class. Instead of using a property accessor on the args class, we use `args.get(...)` and pass the name of the value we want.

##### The BucketPublicAccessBlock and BucketPolicy sub-resources

By default the `BucketObject` we created is not accessible to the public, so we need to unlock that access with the `BucketPublicAccessBlock` and `BucketPolicy` resources.

The `BucketPolicy` resource shows an important coding technique when implementing components: handling asynchronous output values. We use `bucket.bucket.[apply](https://www.pulumi.com/docs/iac/concepts/inputs-outputs/apply/)(...)` to generate an S3 policy document using the `_allow_getobject_policy` helper function. This respects the asynchronous workflow, materializing that value only after the bucket has been created. If we attempted to create a `BucketPolicy` before the `Bucket` existed, the operation would fail. That's because the S3 Policy document needs to use the bucket's name within S3, and we won't know what that value is until the Bucket creation operation has completed. Using `apply` here will ensure that execution of the `_allow_getobject_policy` function doesn't happen until the Bucket has been created successfully.

Just like in a Pulumi program, it's important to understand and respect the asynchronous flow of resource creation within our code. The `apply` function encodes the dependency and required order-of-operations.

The `BucketPolicy` resource also shows another technique: resource dependencies. We use the `depends_on` resource option to indicate that the `BucketPolicy` depends on the `BucketPublicAccessBlock`. This relationship is important to encode so that resource creation, modification, and deletion happens as expected.

#### Handling outputs

The last part of the constructor handles output values. First we set the `endpoint` class property to the end-point URL from the `BucketWebsiteConfiguration` class. Note that this is a `pulumi.Output[str]`, not a regular Python string. Outputs must use `pulumi.Output` types.

Finally, calling `self.register_outputs` signals Pulumi that the component creation process has completed.

{{< example-program path="sample-components" languages="python:static_page.py:55-59" >}}

#### Helper functions

In addition to the constructor logic, we also have a helper function `_allow_getobject_policy`:

***Example:** `static_page.py` a helper function*

{{< example-program path="sample-components" languages="python:static_page.py:62-75" >}}

This function is used to create a S3 policy document, allowing public access to the objects in our bucket. It will be invoked within the context of `apply(...)`. That means that the `bucket_name`, which is normally a `pulumi.Output[str]` value, can be materialized as a normal Python string, and is passed into this function that way. Note that you can't modify the value of `bucket_name`, but you can *read* the value and use it to construct the policy document. The `json.dumps(...)` function takes the dictionary as input and returns it as a JSON formatted string.

{{% /choosable %}}

{{% choosable language go %}}

#### Defining the struct

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:15-18" >}}

The struct must embed the `pulumi.ResourceState` struct. This gives us some built-in behind-the-scenes behavior that allows the component state to be tracked and run within the Pulumi engine and within its host provider. It also allows the underlying library to find and infer the schema of the component.

#### Outputs as struct fields

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:17-17" >}}

We use a struct field to store the output value. Component outputs should always use a `pulumi.*Output` type (such as `pulumi.StringOutput`) rather than plain types. This ensures that outputs can be passed directly to other Pulumi resource inputs, which also accept these output types, without any additional unwrapping or conversion. The `pulumi:"endpoint"` tag defines the name of the property and allows for reflection to generate schema.

#### The Component constructor

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:20-25" >}}

The constructor has a few standard arguments:

- `ctx`: The Pulumi context, which allows for interaction w/ the Pulumi engine
- `name`: The name given to an instance of this component. When writing a Pulumi program, resources are named by the end-user. Later on in the implementation we will use this base component name to uniquely name the resources it contains.
- `args`: This is an instance of the argument class we defined earlier, containing the inputs for our component.
- `opts`: This is an *optional* set of common resource configuration values. The [`ComponentResourceOptions`](/docs/iac/concepts/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our sub-resources later on.

The next step is to register our new component instance with Pulumi via the `ctx` instance. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:index:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The `index` portion of this type name is a required implementation detail. Otherwise, we pass the `name` value, our component instance, as well as the `opts` values.

{{< notes type="warning" >}}
Changing the resource type name after a component has been deployed will cause all existing resources of that type to be recreated. Change the type name with extreme caution.
{{< /notes >}}

#### Creating and managing sub-resources, dependencies, and execution order

Next we implement the `Bucket`, `BucketWebsiteConfiguration`, `BucketObject`, `BucketPublicAccessBlock` and `BucketPolicy` sub-resources.

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:27-91" >}}

##### The Bucket sub-resource

The `Bucket` resource represents an S3 bucket, which is similar to a directory. This is our public-facing entry point for hosting website content on the internet.

Notice the use of the `name` parameter and format string to create a unique name for the bucket resource. Every resource must have a unique name. We will use the same pattern in all the sub-resources.

Another important implementation detail here is the `opts` value being passed to the sub-resource constructor. We use `pulumi.Parent(comp)` to pass the component instance as the `parent` of the `Bucket` resource. This is an essential step to tie the sub-resources into the dependency graph.

##### The BucketWebsiteConfiguration and BucketObject sub-resources

The `BucketWebsiteConfiguration` represents the website configuration and the `BucketObject` represents the contents of the file we will host as `index.html`.

Managing the dependency graph of your sub-resources is very important in a component!

Another point of interest here is the use of `args`. In the `BucketObject` constructor, we pass the contents of the `index.html` page we want to host via the `args.IndexContent` field.

##### The BucketPublicAccessBlock and BucketPolicy sub-resources

By default the `BucketObject` we created is not accessible to the public, so we need to unlock that access with the `BucketPublicAccessBlock` and `BucketPolicy` resources.

The `BucketPolicy` resource shows an important coding technique when implementing components: handling asynchronous output values. We use `bucket.Bucket.[ApplyT](/docs/iac/concepts/inputs-outputs/apply/)(...)` to generate an S3 policy document using the `allowGetObjectPolicy` helper function. This respects the asynchronous workflow, materializing that value only after the bucket has been created. If we attempted to create a `BucketPolicy` before the `Bucket` existed, the operation would fail. That's because the S3 Policy document needs to use the bucket's name within S3, and we won't know what that value is until the Bucket creation operation has completed. Using `ApplyT` here will ensure that execution of the `allowGetObjectPolicy` function doesn't happen until the Bucket has been created successfully.

Just like in a Pulumi program, it's important to understand and respect the asynchronous flow of resource creation within our code. The `ApplyT` function encodes the dependency and required order-of-operations.

The `BucketPolicy` resource also shows another technique: resource dependencies. We use `pulumi.DependsOn([]pulumi.Resource{publicAccessBlock})` to set the `[dependsOn](/docs/iac/concepts/options/dependson/)` [resource option](/docs/iac/concepts/options/) to indicate that the `BucketPolicy` depends on the `BucketPublicAccessBlock`. This relationship is important to encode so that resource creation, modification, and deletion happens as expected.

#### Handling outputs

The last part of the constructor handles output values. First we set the `Endpoint` struct field to the end-point URL from the `BucketWebsiteConfiguration` resource. Note that this is a `pulumi.StringOutput`, not a regular Go string. Outputs must use `pulumi.Output` types.

Finally, return the component instance.

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:93-96" >}}

#### Helper functions

In addition to the resource constructor logic, we also had this inline helper function `allowGetObjectPolicy`:

***Example:** `static_page.go` a helper function*

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:64-81" >}}

This function is used to create a S3 policy document, allowing public access to the objects in our bucket. It will be invoked within the context of `ApplyT(...)`. That means that the `bucketName`, which is normally an asynchronous `pulumi.StringOutput` value, can be materialized as a normal Go string, and is passed into this function that way. Note that you can't modify the value of `bucketName`, but you can *read* the value and use it to construct the policy document. The `json.Marshal(...)` function takes the map as input and returns it as a JSON formatted string.

{{% /choosable %}}

{{% choosable language csharp %}}

#### Inheriting from the base class

{{< example-program path="sample-components" languages="csharp:StaticPage.cs:15-15" >}}

Inheriting from `Pulumi.ComponentResource` gives us some built-in behind-the-scenes behavior that allows the component state to be tracked and run within the Pulumi engine and within its host provider. It also allows the underlying library to find and infer the schema of the component.

#### Outputs as class properties

{{< example-program path="sample-components" languages="csharp:StaticPage.cs:16-17" >}}

We use a class property to store the output value. Component outputs should always use `Pulumi.Output<T>` rather than plain types. This ensures that outputs can be passed directly to other Pulumi resource inputs, which also accept `Pulumi.Output<T>`, without any additional unwrapping or conversion.

#### The Component constructor

{{< example-program path="sample-components" languages="csharp:StaticPage.cs:19-21" >}}

The constructor has a few standard arguments:

- `name`: The name given to an instance of this component. When writing a Pulumi program, resources are named by the end-user. Later on in the implementation we will use this base component name to uniquely name the resources it contains.
- `args`: This is an instance of the argument class we defined earlier, containing the inputs for our component.
- `opts`: This is an *optional* set of common resource configuration values. The [`ComponentResourceOptions`](/docs/iac/concepts/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our sub-resources later on.

Since we're inheriting, we also need to call the base class constructor `base(...)`. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:<module>:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The module portion of this type name is always `index` and is a required implementation detail. Otherwise, we pass the `name`, `args`, and `opts` values from our component constructor into the base constructor.

{{< notes type="warning" >}}
Changing the resource type name after a component has been deployed will cause all existing resources of that type to be recreated. Change the type name with extreme caution.
{{< /notes >}}

#### Creating and managing sub-resources, dependencies, and execution order

Next we implement the `Bucket`, `BucketWebsiteConfiguration`, `BucketObject`, `BucketPublicAccessBlock` and `BucketPolicy` sub-resources.

{{< example-program path="sample-components" languages="csharp:StaticPage.cs:22-44" >}}

##### The Bucket sub-resource

The `Bucket` resource represents an S3 bucket, which is similar to a directory. This is our public-facing entry point for hosting website content on the internet.

Notice the use of the `name` parameter and format string to create a unique name for the bucket resource. Every resource must have a unique name. We will use the same pattern in all the sub-resources.

Another important implementation detail here is the `opts` value being passed to the sub-resource constructor. We create a new object and pass the component instance as the `Parent` of the `Bucket` resource, via `Parent = this` in the `opts` object. This is an essential step to tie the sub-resources into the dependency graph.

##### The BucketWebsiteConfiguration and BucketObject sub-resources

The `BucketWebsiteConfiguration` represents the website configuration and the `BucketObject` represents the contents of the file we will host as `index.html`.

Managing the dependency graph of your sub-resources is very important in a component!

Another point of interest here is the use of `args`. In the `BucketObject` constructor, we pass the contents of the `index.html` page we want to host via the `args` class. It's available as a strongly typed property accessor on the `StaticPageArgs` class.

##### The BucketPublicAccessBlock and BucketPolicy sub-resources

By default the `BucketObject` we created is not accessible to the public, so we need to unlock that access with the `BucketPublicAccessBlock` and `BucketPolicy` resources.

The `BucketPolicy` resource shows an important coding technique when implementing components: handling asynchronous output values. We use `bucket.bucket.Apply(...)` to generate an S3 policy document using the `AllowGetObjectPolicy` helper function. This respects the asynchronous workflow, materializing that value only after the bucket has been created. If we attempted to create a `BucketPolicy` before the `Bucket` existed, the operation would fail. That's because the S3 policy document needs to use the bucket's name within its definition, and we won't know what that value is until the Bucket creation operation has completed. Using `Apply` here will ensure that execution of the `AllowGetObjectPolicy` function doesn't happen until the bucket has been created successfully.

Just like in a Pulumi program, it's important to understand and respect the asynchronous flow of resource creation within our code. The `Apply` function encodes the dependency and required order-of-operations.

The `BucketPolicy` resource also shows another technique: resource dependencies. We use the `DependsOn` resource option to indicate that the `BucketPolicy` depends on the `BucketPublicAccessBlock`. This relationship is important to encode so that resource creation, modification, and deletion happens as expected.

#### Handling outputs

The last part of the constructor handles output values. First we set the `endpoint` class property to the website endpoint from the `BucketWebsiteConfiguration` class. Note that this is a `Pulumi.Output<string>`, not a regular .NET string. Outputs must use `Pulumi.Output` types.

Finally, calling `this.RegisterOutputs` signals Pulumi that the component creation process has completed.

{{< example-program path="sample-components" languages="csharp:StaticPage.cs:46-51" >}}

#### Helper functions

In addition to the constructor logic, we also have a helper function `AllowGetObjectPolicy`:

***Example:** `StaticPage.cs` a helper function*

{{< example-program path="sample-components" languages="csharp:StaticPage.cs:53-67" >}}

This function is used to create a S3 policy document, allowing public access to the objects in our bucket. It will be invoked within the context of `Apply(...)`. That means that the `bucketName`, which is normally a `Pulumi.Output<string>` value, can be materialized as a regular .NET string, and is passed into this function that way. Note that you can't modify the value of `bucketName`, but you can *read* the value and use it to construct the policy document. The `JsonConvert.SerializeObject(...)` function takes the object as input and returns it as a JSON formatted string.

{{% /choosable %}}

{{% choosable language java %}}

#### Inheriting from the base class

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:42-42" >}}

Inheriting from `com.pulumi.resources.ComponentResource` gives us some built-in behind-the-scenes behavior that allows the component state to be tracked and run within the Pulumi engine and within its host provider. It also allows the underlying library to find and infer the schema of the component.

#### Outputs as class properties

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:43-44" >}}

We use a class property to store the output value. Component outputs should always use `com.pulumi.core.Output<T>` rather than plain types. This ensures that outputs can be passed directly to other Pulumi resource inputs, which also accept `Output<T>`, without any additional unwrapping or conversion.

The `@Export` decorator marks this as an exported output, and allows us to set a specific name for the output value.

#### The Component constructor

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:46-47" >}}

The constructor has a few standard arguments:

- `name`: The name given to an instance of this component. When writing a Pulumi program, resources are named by the end-user. Later on in the implementation we will use this base component name to uniquely name the resources it contains.
- `args`: This is an instance of the argument class we defined earlier, containing the inputs for our component.
- `opts`: This is an *optional* set of common resource configuration values. The [`ComponentResourceOptions`](/docs/iac/concepts/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our sub-resources later on.

Since we're inheriting, we also need to call the base class constructor `super(...)`. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:<module>:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The module portion of this type name is always `index` and is a required implementation detail. Otherwise, we pass the `name`, `args`, and `opts` values from our component constructor into the base constructor.

{{< notes type="warning" >}}
Changing the resource type name after a component has been deployed will cause all existing resources of that type to be recreated. Change the type name with extreme caution.
{{< /notes >}}

#### Creating and managing sub-resources, dependencies, and execution order

Next we implement the `Bucket`, `BucketWebsiteConfiguration`, `BucketObject`, `BucketPublicAccessBlock` and `BucketPolicy` sub-resources.

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:49-118" >}}

##### The Bucket sub-resource

The `Bucket` resource represents an S3 bucket, which is similar to a directory. This is our public-facing entry point for hosting website content on the internet.

Notice the use of the `name` parameter and format string to create a unique name for the bucket resource. Every resource must have a unique name. We will use the same pattern in all the sub-resources.

Another important implementation detail here is the `opts` value being passed to the sub-resource constructor. We create a new object and pass the component instance as the `parent` of the `Bucket` resource, via `parent(this)` in the `opts` object. This is an essential step to tie the sub-resources into the dependency graph.

##### The BucketWebsiteConfiguration and BucketObject sub-resources

The `BucketWebsiteConfiguration` represents the website configuration and the `BucketObject` represents the contents of the file we will host as `index.html`.

Managing the dependency graph of your sub-resources is very important in a component!

Another point of interest here is the use of `args`. In the `BucketObject` constructor, we pass the contents of the `index.html` page we want to host via the `args` class. It's available as a strongly typed property accessor on the `StaticPageArgs` class.

##### The BucketPublicAccessBlock and BucketPolicy sub-resources

By default the `BucketObject` we created is not accessible to the public, so we need to unlock that access with the `BucketPublicAccessBlock` and `BucketPolicy` resources.

The `BucketPolicy` resource shows an important coding technique when implementing components: handling asynchronous output values. We use `bucket.arn().applyValue(...)` to generate an S3 policy document. This respects the asynchronous workflow, materializing that value only after the bucket has been created. If we attempted to create a `BucketPolicy` before the `Bucket` existed, the operation would fail. That's because the S3 policy document needs to use the bucket's ARN within its definition, and we won't know what that value is until the Bucket creation operation has completed. Using `applyValue` here will ensure that the policy creation doesn't happen until the bucket has been created successfully.

Just like in a Pulumi program, it's important to understand and respect the asynchronous flow of resource creation within our code. The `applyValue` function encodes the dependency and required order-of-operations.

The `BucketPolicy` resource also shows another technique: resource dependencies. We use the `DependsOn` resource option to indicate that the `BucketPolicy` depends on the `BucketPublicAccessBlock`. This relationship is important to encode so that resource creation, modification, and deletion happens as expected.

#### Handling outputs

The last part of the constructor handles output values. First we set the `endpoint` class property to the website endpoint from the `BucketWebsiteConfiguration` class. Note that this is a `com.pulumi.core.Output<String>`, not a regular Java string. Outputs must use `com.pulumi.core.Output<T>` types.

Finally, calling `this.registerOutputs` signals Pulumi that the component creation process has completed.

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:120-124" >}}

#### Policy Creation

The bucket policy is created using a JSON string that defines the access policy for the S3 bucket. With AWS Provider v7.x, the `policy` field expects either a JSON string or a `PolicyDocumentArgs` object, wrapped in an `Either` type.

The policy JSON is created within the `applyValue(...)` context, where the `bucketArn` (normally a `com.pulumi.core.Output<String>` value) can be materialized as a regular Java string. We use `Either::ofLeft` to convert the JSON string into the expected `Either<String, PolicyDocumentArgs>` type that the AWS provider expects.

{{% /choosable %}}

{{% choosable language yaml %}}

#### Naming the component

{{< example-program path="sample-components" languages="yaml:sample-components/PulumiPlugin.yaml:2-4" >}}

YAML components rely on built-in behind-the-scenes behavior that allows the component state to be tracked and run within a host provider. The Pulumi SDK will scan the definitions and infer the schema of the component. All we need to provide is a unique name for the resource type. Later consumers of the component can reference it by the package name and component type like this:

{{< example-program path="sample-components" languages="yaml:sample-components/PulumiPlugin.yaml:2-4" >}}

It follows the schema of `<package_name>:<component_resource_name>`.

#### Output properties

{{< example-program path="sample-components" languages="yaml:sample-components/PulumiPlugin.yaml:55-56" >}}

The `outputs` section defines the outputs that will be shared to the consumer of the component. These will appear in consumer languages as `pulumi.Output<T>` equivalents, instead of just a regular string. This allows the end-user to access this in an asynchronous manner when writing their Pulumi program.

#### Creating and managing sub-resources, dependencies, and execution order

Next we implement the `Bucket`, `BucketWebsiteConfiguration`, `BucketObject`, `BucketPublicAccessBlock` and `BucketPolicy` sub-resources. Defining sub-resources in a YAML component works exactly the same as defining them in a YAML Pulumi program.

{{< example-program path="sample-components" languages="yaml:sample-components/PulumiPlugin.yaml:8-53" >}}

##### The Bucket sub-resource

The `Bucket` resource represents an S3 bucket, which is similar to a directory. This is our public-facing entry point for hosting website content on the internet.

<!-- Notice the use of the `name` parameter and format string to create a unique name for the bucket resource. Every resource must have a unique name. We will use the same pattern in all the sub-resources. -->

Another important implementation detail here is the `options` section. By default the component instance will be set as the `parent` of the `Bucket` resource, so there's no need to define that on this object.

##### The BucketWebsiteConfiguration and BucketObject sub-resources

The `BucketWebsiteConfiguration` represents the website configuration and the `BucketObject` represents the contents of the file we will host as `index.html`.

Managing the dependency graph of your sub-resources is very important in a component!

Another point of interest here is the use of the component input values. In the `BucketObject` definition, we pass the contents of the `index.html` page we want to host via `${indexContent}` string interpolation. All input values are available for string interpolation.

##### The BucketPublicAccessBlock and BucketPolicy sub-resources

By default the `BucketObject` we created is not accessible to the public, so we need to unlock that access with the `BucketPublicAccessBlock` and `BucketPolicy` resources.

The `BucketPublicAccessBlock` resource requires all four public access properties to be set to `false` to properly enable public access: `blockPublicAcls`, `blockPublicPolicy`, `ignorePublicAcls`, and `restrictPublicBuckets`. Setting only one or some of these properties will not allow the bucket policy to function correctly.

The `BucketPolicy` resource shows an important coding technique when implementing components: handling asynchronous output values. We use the `${bucket.bucket}` interpolation to generate an S3 policy document using the `fn::toJSON:` helper function. This respects the asynchronous workflow, waiting to create the `BucketPolicy` resource until after the bucket has been created. If the provider attempted to create a `BucketPolicy` before the `Bucket` existed, the operation would fail. That's because the S3 policy document needs to use the bucket's name within its definition, and we won't know what that value is until the Bucket creation operation has completed. Pulumi's YAML implementation handles that workflow automatically.

The `BucketPolicy` resource also shows another technique: resource dependencies. We use the `dependsOn` resource option to indicate that the `BucketPolicy` depends on the `BucketPublicAccessBlock`. This relationship is important to encode so that resource creation, modification, and deletion happens as expected.

#### Handling outputs

The last part of the component definition handles output values. First we set the `endpoint` class property to the website endpoint from the `BucketWebsiteConfiguration` class. This uses standard string interopolation and automatically handles asynchronous value resolution, waiting to assign the `endpoint` output until `bucketWebsite.websiteEndpoint` has completed completion and the value is available.

{{< example-program path="sample-components" languages="yaml:sample-components/PulumiPlugin.yaml:55-56" >}}

#### Helper functions

In addition to the component definitions, we are also using a helper function `fn::toJSON:`:

***Example:** YAML helper function*

{{< example-program path="sample-components" languages="yaml:sample-components/PulumiPlugin.yaml:41-53" >}}

This function is used to create a S3 policy document, allowing public access to the objects in our bucket. It will be invoked only when the interpolated value `${bucket.bucket}` is available as a standard string. We construct a YAML object which is then serialized to a JSON formatted string and assigned to the `policy` property.

{{% /choosable %}}

{{< /chooser >}}

### Use the Component in a Pulumi Program

Let's try it out in a Pulumi program.

#### Setup the Pulumi Program

First, let's create a simple Pulumi program project. Create a new directory and a `Pulumi.yaml` file.

```bash
$ cd ..
$ mkdir use-static-page-component
```

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in TypeScript*

{{< example-program path="sample-components" languages="typescript:Pulumi.yaml:" >}}

#### Generate the SDK

In order to use our Pulumi component from source, we'll need to generate a TypeScript-specific SDK to use in a Pulumi program. From the root directory of your `use-static-page-component` Pulumi project, run the following command:

```bash
pulumi package add ../sample-components
```

This creates a new subdirectory called `sdks/` that contains the generated SDK.

#### Add the NodeJS and TypeScript project files

Now lets create our `package.json` and `tsconfig.json`. We'll need the standard `pulumi` SDK and our custom component. To use that, just add the path to the generated TypeScript SDK using the format `file:<path>` instead of a package version spec.

***Example:** `package.json`*

{{< example-program path="sample-components" languages="typescript:package.json:" >}}

Note that we don't need to add the Pulumi AWS provider library here, because that dependency is handled by the component project, in whatever language you implemented it in. We just need to carry a reference to the component SDK which provides us access to the component via RPC to its provider host. This creates a clean separation of concerns between the component implementation and the end users of the component.

The TypeScript config is the same as any standard Pulumi program.

***Example:** `tsconfig.json` for a Pulumi program*

{{< example-program path="sample-components" languages="typescript:tsconfig.json:" >}}

#### Install dependencies

Next, install the `pulumi` dependencies:

```bash
pulumi install
```

#### Create the Pulumi program

***Example:** `index.ts` that uses the Static Page component*

{{< example-program path="sample-components" languages="typescript" >}}

{{% /choosable %}}

{{% choosable language python %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in Python*

{{< example-program path="sample-components" languages="python:Pulumi.yaml:" >}}

#### Generate the SDK

In order to use our Pulumi component from source, we'll need to generate a Python-specific SDK to use in a Pulumi program. From the root directory of your `use-static-page-component` Pulumi project, run the following command:

```bash
pulumi package add ../sample-components
```

This creates a new subdirectory called `sdks/` that contains the generated SDK.

#### Update Pulumi.yaml with packages reference

You need to manually add the packages section to your `Pulumi.yaml`:

{{< example-program path="sample-components" languages="python:Pulumi.yaml:" >}}

#### Add the package dependencies

Now lets create our `requirements.txt`. We'll need the standard `pulumi` SDK:

{{< example-program path="sample-components" languages="python:requirements.txt:" >}}

Note that we don't need to add the Pulumi AWS provider library here, because that dependency is handled by the component project, in whatever language you implemented it in. We just need to carry a reference to the component SDK which provides us access to the component via RPC to its provider host. This creates a clean separation of concerns between the component implementation and the end users of the component.

#### Setup the virtual environment

Next, set up your virtual environment:

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pulumi install
```

#### Create the Pulumi program

***Example:** `__main__.py` that uses the Static Page component*

{{< example-program path="sample-components" languages="python" >}}

{{% /choosable %}}

{{% choosable language go %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in Go*

{{< example-program path="sample-components" languages="go:Pulumi.yaml:" >}}

#### Add the Go project file

Now lets create our `go.mod`. We'll need the standard `pulumi` SDK and our custom component. Since our component is structured as a standard Go package, we can import it directly using a `replace` directive for local development.

***Example:** `go.mod` for our Pulumi project*

{{< example-program path="sample-components" languages="go:go.mod:" >}}

Note that we don't need to add the Pulumi AWS provider library here, because that dependency is handled by the component project. The `replace` directive tells Go to use our local component instead of trying to fetch it from a remote repository.

#### Install dependencies

Next, install the `pulumi` dependencies:

```bash
go mod tidy
```

#### Create the Pulumi program

***Example:** `main.go` that uses the Static Page component*

{{< example-program path="sample-components" languages="go" >}}

{{% /choosable %}}

{{% choosable language csharp %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in C#*

{{< example-program path="sample-components" languages="csharp:Pulumi.yaml:" >}}

#### Generate the SDK

In order to use our Pulumi component from source, we'll need to generate a .NET-specific SDK to use in a Pulumi program. From the root directory of your `use-static-page-component` Pulumi project, run the following command:

```bash
pulumi package add ../sample-components
```

This creates a new subdirectory called `sdks/` that contains the generated SDK.

#### Update Pulumi.yaml with packages reference

You need to manually add the packages section to your `Pulumi.yaml`:

{{< example-program path="sample-components" languages="csharp:Pulumi.yaml:" >}}

#### Add the .NET project file

Now lets create our `.csproj`. We'll need the standard `pulumi` SDK and our custom component. To use the generated .NET SDK, just add the relative path to the project file in the `Include` attribute instead of the name of the library.

***Example:** `use-static-page-component.csproj`*

{{< example-program path="sample-components" languages="csharp:sample-components-csharp.csproj:" >}}

Note that we don't need to add the Pulumi AWS provider library here, because that dependency is handled by the component project, in whatever language you implemented it in. We just need to carry a reference to the component SDK which provides us access to the component via RPC to its provider host. This creates a clean separation of concerns between the component implementation and the end users of the component.

#### Install dependencies

Next, install the `pulumi` dependencies:

```bash
pulumi install
```

#### Create the Pulumi program

***Example:** `Program.cs` that uses the Static Page component*

{{< example-program path="sample-components" languages="csharp" >}}

{{% /choosable %}}

{{% choosable language java %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in Java*

{{< example-program path="sample-components" languages="java:Pulumi.yaml:" >}}

#### Generate the SDK

In order to use our Pulumi component from source, we'll need to generate a Java-specific SDK to use in a Pulumi program. From the root directory of your `use-static-page-component` Pulumi project, run the following command:

```bash
pulumi package add ../sample-components
```

This creates a new subdirectory called `sdks/` that contains the generated SDK.

#### Add the Maven project file

Now lets create our `pom.xml`. We'll need the standard `pulumi` SDK and our custom component.

We'll need to add the sources from the generated SDK output into the build sources Maven looks for, and also add the dependencies. The output of the `pulumi package add` command should have given instructions on the necessary dependencies to add, in XML format. It will also suggest copying the source files into your `src/main` folder. Instead, we'll leave the SDK files in place, and modify our build configuration to look in that directory as well as our normal source directory.

***Example:** `pom.xml`*

{{< example-program path="sample-components" languages="java:pom.xml:" >}}

Note that we don't need to add the Pulumi AWS provider library here, because that dependency is handled by the component project, in whatever language you implemented it in. We just need to carry a reference to the component SDK, and add its dependencies, which will provide us access to the component via RPC, which is running inside of its provider host. This creates a clean separation of concerns between the component implementation and the end users of the component.

#### Install dependencies

Next, install the `pulumi` dependencies:

```bash
pulumi install
```

#### Create the Pulumi program

Make a new subdirectory called `src/main/java/myproject` and in it, create a file called `App.java`.

***Example:** `App.java` that uses the Static Page component*

{{< example-program path="sample-components" languages="java" >}}

{{% /choosable %}}

{{% choosable language yaml %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in YAML*

{{< example-program path="sample-components" languages="yaml:1-4" >}}

#### Add the component reference in `Pulumi.yaml`

Now, in your `Pulumi.yaml` file add the following section to load the component from source:

{{< example-program path="sample-components" languages="yaml:5-6" >}}

The `aws: "7.6.0"` entry ensures we use the latest AWS provider v7.x with all the most recent features and improvements.

#### Create the Pulumi program

Now we can define our Static Page component resource in the `Pulumi.yaml` file. Add the following section:

***Example:** `Pulumi.yaml` that uses the Static Page component*

{{< example-program path="sample-components" languages="yaml:7-13" >}}

{{% /choosable %}}

{{< /chooser >}}

Finally, run the Pulumi update and we will see our component resource creates, as well as its sub-resources.

```bash
$ pulumi up
...
     Type                                          Name                                Status
 +   pulumi:pulumi:Stack                           use-static-page-component-dev       created (8s)
 +   └─ sample-components:index:StaticPage     my-static-page                      created (5s)
 +      └─ aws:s3:Bucket                         my-static-page-bucket               created (2s)
 +         ├─ aws:s3:BucketPublicAccessBlock       my-static-page-public-access-block  created (0.84s)
 +         ├─ aws:s3:BucketWebsiteConfiguration  my-static-page-website              created (0.91s)
 +         ├─ aws:s3:BucketObject                  my-static-page-index-object         created (0.84s)
 +         └─ aws:s3:BucketPolicy                  my-static-page-bucket-policy        created (1s)

Policies:
    ✅ pulumi-internal-policies@v0.0.6

Outputs:
    websiteURL: "http://my-static-page-bucket-abcd123.s3-website-us-west-2.amazonaws.com"

Resources:
    + 7 created

Duration: 10s
```

Success! We were able to use our component as just a single resource within our Pulumi program and it managed five other resources under the hood for us. This greatly reduces the amount of code an end user has to write to be able to host an HTML file in S3.

## Next steps

Now that you've built a component, you can package and distribute it for reuse. See [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) to learn about single-language, cross-language, and provider-based packaging approaches.

For testing strategies, see [Testing Components](/docs/iac/guides/building-extending/components/testing-components/).
