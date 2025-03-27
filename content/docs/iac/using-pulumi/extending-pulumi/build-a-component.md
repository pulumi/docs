---
title_tag: "Build a Component"
meta_desc: "Learn the process for building a custom Pulumi Component."
title: Build a Component
h1: Build a Component
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Build a Component
        parent: iac-extending-pulumi
        weight: 1
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

## Structure of a Component

A Pulumi Component consists of three main parts. The **component resource** encapsulates multiple Pulumi resources, grouping them into a logical unit. The **component resource arguments** define configurable input properties, allowing users to specify parameters that tailor the component’s behavior to specific needs. The **provider host** defines and registers resource types, acting as the foundational layer for component creation.

## Example: Static Web Page Component

In this example, we'll create a static website component in AWS Simple Storage Service (S3). The component will manage the following five sub-resources necessary to implement a basic S3 hosted static website:

- a [`BucketV2`](/registry/packages/aws/api-docs/s3/bucketV2/) resource
- a [`BucketWebsiteConfigurationV2`](/registry/packages/aws/api-docs/s3/bucketWebsiteConfigurationV2/) resource to set up the website configuration
- a [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) resource to hold the raw site content
- a [`BucketPublicAccessBlock`](/registry/packages/aws/api-docs/s3/bucketPublicAccessBlock/) resource to manage public access
- a [`BucketPolicy`](/registry/packages/aws/api-docs/s3/bucketpolicy/) resource to set the Bucket policy

The component will take as input the contents of the file you wish to host, and will output the S3 endpoint used to access it.

***Example:** Using a custom StaticPage component in a Pulumi Program*

```yaml
name: static-page-yaml
description: A minimal Pulumi YAML program
runtime: yaml
packages:
  static-page-component: ../
resources:
  mystaticpage:
    type: static-page-component:StaticPage
    properties:
      indexContent: "<h1>Hello, World!</h1>"
```

The core implementation of the AWS API is handled by the [Pulumi AWS Provider](/registry/packages/aws/), which gives us those five underlying resource types. Our `StaticPage` component will work with those existing types and create a new type of resource with a simpler API.

### Setting up your Component project

A Pulumi Component is a seperate project from your Pulumi program. So, let's create a new directory for it, and create some project files:

```bash
$ mkdir static-page-component
$ cd static-page-component
```

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

Authoring sharable components in JavaScript is not currently supported. Considering writing in TypeScript instead!

{{% /choosable %}}

{{% choosable language typescript %}}

#### PulumiPlugin.yaml

The `PulumiPlugin.yaml` file tells Pulumi that this directory is a component, rather than a Pulumi program. In it, we define the language runtime needed to load the plugin.

***Example:** `PulumiPlugin.yaml` for TypeScript*

```yaml
runtime: nodejs
```

#### Manage dependencies

Next, we need to define our dependencies in `package.json`.

***Example:** `package.json` for a Pulumi Component*

```json
{
    "name": "static-page-component",
    "description": "Static Page Component",
    "dependencies": {
        "@pulumi/aws": "6.73.0",
        "@pulumi/pulumi": "^3.159.0"
    },
    "devDependencies": {
        "@types/node": "^18.0.0",
        "typescript": "^4.6.0"
    }
}
```

The `@pulumi/pulumi` SDK contains everything we need for making a component. It should be version `3.157.0` or newer. The `@pulumi/aws` package is the AWS provider that we are building on top of.

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
        "staticpage.ts"
    ]
}
```

Finally, install dependencies via NPM:

```bash
$ npm install
```

{{% /choosable %}}

{{% choosable language python %}}

#### PulumiPlugin.yaml

The `PulumiPlugin.yaml` file tells Pulumi that this directory is a component, rather than a Pulumi program. In it, we define the language runtime needed to load the plugin.

***Example:** `PulumiPlugin.yaml` for Python*

```yaml
runtime: python
```

#### Manage dependencies

Next, we need to define our dependencies in `requirements.txt`.

***Example:** `requirements.txt` for a Pulumi Component*

```toml
pulumi>=3.159.0,<4.0
pulumi_aws>=6.0.0
```

The `pulumi` SDK contains everything we need for making a component. It should be version `3.153.0` or newer. The `pulumi_aws` package is the AWS provider that we are building on top of.
{{% /choosable %}}

{{% choosable language go %}}

#### PulumiPlugin.yaml

The `PulumiPlugin.yaml` file tells Pulumi that this directory is a component, rather than a Pulumi program. In it, we define the language runtime needed to load the plugin.

***Example:** `PulumiPlugin.yaml` for Go*

```yaml
runtime: go
```

#### Manage dependencies

Next, we need to define our dependencies in `go.mod`.

***Example:** `go.mod` for a Pulumi Component*

```
TODO: language-specific package management info
```

The `pulumi` SDK contains everything we need for making a component. It should be version `3.157.0` or newer. The `pulumi-aws` package is the AWS provider that we are building on top of.

{{% /choosable %}}

{{% choosable language csharp %}}

#### PulumiPlugin.yaml

The `PulumiPlugin.yaml` file tells Pulumi that this directory is a component, rather than a Pulumi program. In it, we define the language runtime needed to load the plugin.

***Example:** `PulumiPlugin.yaml` for C#*

```yaml
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
    <AssemblyName>static-page-component</AssemblyName>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Pulumi" Version="3.77.0" />
    <PackageReference Include="Pulumi.Aws" Version="6.*" />
    <PackageReference Include="Newtonsoft.Json" Version="13.*" />
  </ItemGroup>
</Project>
```

The `Pulumi` SDK contains everything we need for making a component. It should be version `3.77.0` or newer. The `Pulumi.Aws` package is the AWS provider that we are building on top of.

Note that the `AssemblyName` specifies the name of the component package. This name will be important later on in the component implementation, so make sure it's something unique and descriptive!

{{% /choosable %}}

{{% choosable language java %}}

#### PulumiPlugin.yaml

The `PulumiPlugin.yaml` file tells Pulumi that this directory is a component, rather than a Pulumi program. In it, we define the language runtime needed to load the plugin.

***Example:** `PulumiPlugin.yaml` for Java*

```yaml
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
  <artifactId>static-page-component</artifactId>
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
      <version>1.7.36</version>
    </dependency>
    <dependency>
      <groupId>com.google.code.gson</groupId>
      <artifactId>gson</artifactId>
      <version>2.8.9</version>
    </dependency>
    <dependency>
      <groupId>com.pulumi</groupId>
      <artifactId>pulumi</artifactId>
      <version>[1.8,)</version>
    </dependency>
    <dependency>
      <groupId>com.pulumi</groupId>
      <artifactId>aws</artifactId>
      <version>(6.0.2,6.99]</version>
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

The `com.pulumi.pulumi` SDK contains everything we need for making a component. It should be version `1.8` or newer. The `com.pulumi.aws` package is the AWS provider that we are building on top of. We've also included a couple helper libraries like `gson` and `slf4j-nop` which are helpful for this example.

{{% /choosable %}}

{{% choosable language yaml %}}

#### PulumiPlugin.yaml

The `PulumiPlugin.yaml` file tells Pulumi that this directory is a component, rather than a Pulumi program. It's also where we will define the component implementation later. For now, just add the `runtime` and `name` properties.

***Example:** `PulumiPlugin.yaml` for YAML*

```yaml
runtime: yaml
name: static-page-component
```

{{% /choosable %}}

{{< /chooser >}}

#### Define the entrypoint

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

Authoring sharable components in JavaScript is not currently supported. Considering writing in TypeScript instead!

{{% /choosable %}}

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
from pulumi.provider.experimental import Metadata, component_provider_host
from staticpage import StaticPage

if __name__ == "__main__":
    component_provider_host(name="static-page-component", components=[StaticPage])
```

Here, the `component_provider_host` call invokes a Pulumi provider implmentation which acts as a shim for the component. The name we pass to it will be important later on in the component implementation, so make sure it's something unique and descriptive!

{{% /choosable %}}

{{% choosable language go %}}

First, create the `main.go` file, where we will define an entry point for the component.

***Example:** `main.go` component entry point*

```go
package main

import (
	"github.com/pulumi/pulumi-go-provider/infer"
)

func main() {
	err := infer.NewProviderBuilder().
		WithName("static-page-component").
		WithComponents(
			infer.Component(NewStaticPage),
		).
		BuildAndRun()

	if err != nil {
		panic(err)
	}
}
```

Here, the `BuildAndRun` method creates and runs a Pulumi provider which acts as a shim for the component. We use `NewProviderBuilder()` to construct our provider and configure it with various parameters.

The `WithName` method specifies the name of the component resource provider. This name will be important later on in the component implementation, so make sure it's something unique and descriptive!

The `WithComponents` method registers the components that will be available through this provider. The `infer.Component` call tells the Pulumi SDK which types to look at for our component implementation. The `infer` library scans these structs and does a lot of heavy lifting to infer schema and necessary middleware, so that our component implementations can involve minimal coding.

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

Here, the `ComponentProviderHost.Serve` call invokes a Pulumi provider implmentation which acts as a shim for the component. Everything else about your component will be inferred by the Pulumi SDK.

{{% /choosable %}}

{{% choosable language java %}}

First, create the `src/main/java/staticpagecomponent` sub-directory and in it, create the `App.java` file, where we will define an entry point for the component.

***Example:** `App.java` component entry point*

```java
package staticpagecomponent;

import java.io.IOException;
import com.pulumi.provider.internal.Metadata;
import com.pulumi.provider.internal.ComponentProviderHost;

public class App {
    public static void main(String[] args) throws IOException, InterruptedException {
        new ComponentProviderHost("static-page-component", App.class.getPackage()).start(args);
    }
}
```

Here, the `ComponentProviderHost.start(...)` call invokes a Pulumi provider implmentation which acts as a shim for the component. The name we pass to it will be important later on in the component implementation, so make sure it's something unique and descriptive!

We also need to pass the Java package so that your component classes can be inferred by the Pulumi SDK.

{{% /choosable %}}

{{% choosable language yaml %}}

Because YAML is entirely declarative, unlike in our other languages, there's no need define an entry point.

{{% /choosable %}}

{{< /chooser >}}

### Implement the Component

Next we will define the classes that implement our custom component.

Components typically require two parts: a subclass of `pulumi.ComponentResource` that implements the component, and an *arguments* class, which is used to configure the component during construction.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

Authoring sharable components in JavaScript is not currently supported. Considering writing in TypeScript instead!

{{% /choosable %}}

{{% choosable language typescript %}}

#### Add the required imports

First create a file called `staticpage.ts`, and add the imports we will need:

***Example:** `staticpage.ts` required imports*

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
```

### Define the Component arguments

Next, we will implement the arguments class. In our example here, we will pass the contents of the webpage we want to host to the component.

***Example:** `staticpage.ts` the Component arguments implmentation*

```typescript
export interface StaticPageArgs {
    // The HTML content for index.html
    indexContent: pulumi.Input<string>;
}
```

Note that argument classes must be *serializable* and use `pulumi.Input` types, rather than the language's default types.

### Define the Component resource

Now we can implement the component itself. Components should inherit from `pulumi.ComponentResource`, and should accept the required arguments class we just defined in the constructor. All the work for our component happens in the constructor, and outputs are returned via class properties. At the end of the process a calling `self.registerOutputs` signals Pulumi that the process of creating the component resource has completed.

***Example:** `staticpage.ts` the Component implmentation*

```typescript
export class StaticPage extends pulumi.ComponentResource {
    // The URL of the static website.
    public readonly endpoint: pulumi.Output<string>;

    constructor(name: string, args: StaticPageArgs, opts?: pulumi.ComponentResourceOptions) {
        super("static-page-component:index:StaticPage", name, args, opts);

        // Create a bucket
        const bucket = new aws.s3.BucketV2(`${name}-bucket`, {}, { parent: this });

        // Configure the bucket website
        const bucketWebsite = new aws.s3.BucketWebsiteConfigurationV2(`${name}-website`, {
            bucket: bucket.bucket,
            indexDocument: { suffix: "index.html" },
        }, { parent: bucket });

        // Create a bucket object for the index document.
        const bucketObject = new aws.s3.BucketObject(`${name}-index-object`, {
            bucket: bucket.bucket,
            key: 'index.html',
            content: args.indexContent,
            contentType: 'text/html',
        }, { parent: bucket });

        // Create a public access block for the bucket
        const publicAccessBlock = new aws.s3.BucketPublicAccessBlock(`${name}-public-access-block`, {
            bucket: bucket.id,
            blockPublicAcls: false,
        }, { parent: bucket });

        // Set the access policy for the bucket so all objects are readable
        const bucketPolicy = new aws.s3.BucketPolicy(`${name}-bucket-policy`, {
            bucket: bucket.id, // refer to the bucket created earlier
            policy: bucket.bucket.apply(this.allowGetObjectPolicy),
        }, { parent: bucket, dependsOn: publicAccessBlock });

        this.endpoint = bucketWebsite.websiteEndpoint;

        // By registering the outputs on which the component depends, we ensure
        // that the Pulumi CLI will wait for all the outputs to be created before
        // considering the component itself to have been created.
        this.registerOutputs({
            endpoint: bucketWebsite.websiteEndpoint,
        });
    }

    allowGetObjectPolicy(bucketName: string) {
        return JSON.stringify({
            Version: "2012-10-17",
            Statement: [{
                Effect: "Allow",
                Principal: "*",
                Action: [
                    "s3:GetObject"
                ],
                Resource: [
                    `arn:aws:s3:::${bucketName}/*`
                ]
            }]
        });
    }
}
```

### Detailed implementation breakdown

Let's dissect this component implementation piece-by-piece:

#### Inheriting from the base class

```typescript
export class StaticPage extends pulumi.ComponentResource {
    // ...
}
```

Inheriting from `pulumi.ComponentResource` gives us some built-in behind-the-scenes behavior that allows the component state to be tracked and run within the Pulumi engine and within its host provider. It also allows the underlying library to find and infer the schema of the component.

#### Outputs as class properties

```typescript
export class StaticPage extends pulumi.ComponentResource {
    // The URL of the static website
    public readonly endpoint: pulumi.Output<string>;
// ...
}
```

We use a class property to store the output value. Note that it's using `pulumi.Output<string>` instead of just a regular string. This allows the end-user to access this in an asynchronous manner when writing their Pulumi program.

#### The Component constructor

```typescript
// ...
    constructor(name: string, args: StaticPageArgs, opts?: pulumi.ComponentResourceOptions) {
        super("static-page-component:index:StaticPage", name, args, opts);
// ...
```

The constructor has a few standard arguments:

- `name`: The name given to an instance of this component. When writing a Pulumi program, resources are named by the end-user. Later on in the implementation we will use this base component name to uniquely name the resources it contains.
- `args`: This is an instance of the argument class we defined earlier, containing the required inputs for our component.
- `opts`: This is an *optional* set of common resource configuration values. The [`ResourceOptions`](/docs/iac/concepts/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our sub-resources later on.

Since we're inheriting, we also need to call the base class constructor `super(...)`. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:index:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The `index` portion of this type name is a required implmentation detail. Otherwise, we pass the `name`, `args`, and `opts` values from our component constructor into the base constructor.

#### Creating and managing sub-resources, dependencies, and execution order

Next we implement the `BucketV2`, `BucketWebsiteConfigurationV2`, `BucketObject`, `BucketPublicAccessBlock` and `BucketPolicy` sub-resources.

```typescript
// ...
        // Create a bucket
        const bucket = new aws.s3.BucketV2(`${name}-bucket`, {}, { parent: this });

        // Configure the bucket website
        const bucketWebsite = new aws.s3.BucketWebsiteConfigurationV2(`${name}-website`, {
            bucket: bucket.bucket,
            indexDocument: { suffix: "index.html" },
        }, { parent: bucket });

        // Create a bucket object for the index document.
        const bucketObject = new aws.s3.BucketObject(`${name}-index-object`, {
            bucket: bucket.bucket,
            key: 'index.html',
            content: args.indexContent,
            contentType: 'text/html',
        }, { parent: bucket });

        // Create a public access block for the bucket
        const publicAccessBlock = new aws.s3.BucketPublicAccessBlock(`${name}-public-access-block`, {
            bucket: bucket.id,
            blockPublicAcls: false,
        }, { parent: bucket });

        // Set the access policy for the bucket so all objects are readable
        const bucketPolicy = new aws.s3.BucketPolicy(`${name}-bucket-policy`, {
            bucket: bucket.id, // refer to the bucket created earlier
            policy: bucket.bucket.apply(this.allowGetObjectPolicy),
        }, { parent: bucket, dependsOn: publicAccessBlock });
// ...
```

##### The Bucket sub-resource

The `BucketV2` resource represents an S3 bucket, which is similar to a directory. This is our public-facing entry point for hosting website content on the internet.

Notice the use of the `name` parameter and format string to create a unique name for the bucket resource. Every resource must have a unique name. We will use the same pattern in all the sub-resources.

Another important implementation detail here is the `opts` value being passed to the sub-resource constructor. We create a new instance of `ResourceOptions` and pass the component instance as the `parent` of the `BucketV2` resource, via `parent: this` in the `ResourceOptions` class. This is an essential step to tie the sub-resources into the dependency graph.

##### The BucketWebsiteConfigurationV2 and BucketObject sub-resources

The `BucketWebsiteConfigurationV2` represents the website configuration and the `BucketObject` represents the contents of the file we will host as `index.html`.

Notice that this time we pass the `BucketV2` instance in as the `parent` to the `ResourceOptions` instances for these sub-resources, as opposed to `this` (e.g. the component). That creates a resource relationship graph like: `StaticPage` -> `BucketV2` -> `BucketObject`. We do the same thing in the `BucketPublicAccessBlock` and `BucketPolicy` resource.

Managing the dependency graph of your sub-resources is very important in a component!

Another point of interest here is the use of `args`. In the `BucketObject` constructor, we pass the contents of the `index.html` page we want to host via the `args` class. It's available as a strongly typed property accessor on the args class.

##### The BucketPublicAccessBlock and BucketPolicy sub-resources

By default the `BucketObject` we created is not accessible to the public, so we need to unlock that access with the `BucketPublicAccessBlock` and `BucketPolicy` resources.

The `BucketPolicy` resource shows an important coding technique when implementing components: handling asynchronous output values. We use `bucket.bucket.apply(...)` to generate an S3 policy document using the `allowGetObjectPolicy` helper function. This respects the asynchronous workflow, materializing that value only after the bucket has been created. If we attempted to create a `BucketPolicy` before the `Bucket` existed, the operation would fail. That's because the S3 policy document needs to use the bucket's name within its definition, and we won't know what that value is until the Bucket creation operation has completed. Using `apply` here will ensure that execution of the `allowGetObjectPolicy` function doesn't happen until the bucket has been created successfully.

Just like in a Pulumi program, it's important to understand and respect the asynchronous flow of resource creation within our code. The `apply` function encodes the dependency and required order-of-operations.

The `BucketPolicy` resource also shows another technique: resource dependencies. We use the `dependsOn` resource option to indicate that the `BucketPolicy` depends on the `BucketPublicAccessBlock`. This relationship is important to encode so that resource creation, modification, and deletion happens as expected.

#### Handling outputs

The last part of the constructor handles output values. First we set the `endpoint` class property to the website endpoint from the `BucketWebsiteConfigurationV2` class. Note that this is a `pulumi.Output<string>`, not a regular TypeScript string. Outputs must use `pulumi.Output` types.

Finally, calling `this.registerOutputs` signals Pulumi that the component creation process has completed.

```typescript
// ...
        this.endpoint = bucketWebsite.websiteEndpoint;

        // By registering the outputs on which the component depends, we ensure
        // that the Pulumi CLI will wait for all the outputs to be created before
        // considering the component itself to have been created.
        this.registerOutputs({
            endpoint: bucketWebsite.websiteEndpoint,
        });
// ...
```

#### Helper functions

In addition to the constructor logic, we also have a helper function `allowGetObjectPolicy`:

***Example:** `staticpage.ts` a helper function*

```typescript
// ...
    allowGetObjectPolicy(bucketName: string) {
        return JSON.stringify({
            Version: "2012-10-17",
            Statement: [{
                Effect: "Allow",
                Principal: "*",
                Action: [
                    "s3:GetObject"
                ],
                Resource: [
                    `arn:aws:s3:::${bucketName}/*`
                ]
            }]
        });
    }
// ...
```

This function is used to create a S3 policy document, allowing public access to the objects in our bucket. It will be invoked within the context of `apply(...)`. That means that the `bucketName`, which is normally a `pulumi.Output<str>` value, can be materialized as a normal TypeScript string, and is passed into this function that way. Note that you can't modify the value of `bucketName`, but you can *read* the value and use it to construct the policy document. The `JSON.stringify(...)` function takes the object as input and returns it as a JSON formatted string.

{{% /choosable %}}

{{% choosable language python %}}

#### Add the required dependencies

First create a file called `staticpage.py`, and add the imports we will need:

***Example:** `staticpage.py` required dependencies*

```python
import json
from typing import Optional, TypedDict

import pulumi
from pulumi import ResourceOptions
from pulumi_aws import s3
```

### Define the Component arguments

Next, we will implement the arguments class. In our example here, we will pass the contents of the webpage we want to host to the component.

***Example:** `staticpage.py` the Component arguments implmentation*

```python
class StaticPageArgs(TypedDict):
    index_content: pulumi.Input[str]
    """The HTML content for index.html."""
```

Note that argument classes must be *serializable* and use `pulumi.Input` types, rather than the language's default types.

### Define the Component resource

Now we can implement the component itself. Components should inherit from `pulumi.ComponentResource`, and should accept the required arguments class we just defined in the constructor. All the work for our component happens in the constructor, and outputs are returned via class properties. At the end of the process a calling `self.register_outputs` signals Pulumi that the process of creating the component resource has completed.

***Example:** `staticpage.py` the Component implmentation*

```python
class StaticPage(pulumi.ComponentResource):
    endpoint: pulumi.Output[str]
    """The URL of the static website."""

    def __init__(self,
                 name: str,
                 args: StaticPageArgs,
                 opts: Optional[ResourceOptions] = None) -> None:

        super().__init__('static-page-component:index:StaticPage', name, {}, opts)

        # Create a bucket
        bucket = s3.BucketV2(
            f'{name}-bucket',
            opts=ResourceOptions(parent=self))

        # Configure the bucket website
        bucket_website = s3.BucketWebsiteConfigurationV2(
            f'{name}-website',
            bucket=bucket.bucket,
            index_document={"suffix": "index.html"},
            opts=ResourceOptions(parent=bucket))

        # Create a bucket object for the index document
        s3.BucketObject(
            f'{name}-index-object',
            bucket=bucket.bucket,
            key='index.html',
            content=args.get("index_content"),
            content_type='text/html',
            opts=ResourceOptions(parent=bucket))

        # Create a public access block for the bucket
        bucket_public_access_block = s3.BucketPublicAccessBlock(
            f'{name}-public-access-block',
            bucket=bucket.id,
            block_public_acls=False,
            opts=ResourceOptions(parent=bucket))

        # Set the access policy for the bucket so all objects are readable.
        s3.BucketPolicy(
            f'{name}-bucket-policy',
            bucket=bucket.bucket,
            policy=bucket.bucket.apply(_allow_getobject_policy),
            opts=ResourceOptions(parent=bucket, depends_on=[bucket_public_access_block]))

        self.endpoint = bucket_website.website_endpoint

        # By registering the outputs on which the component depends, we ensure
        # that the Pulumi CLI will wait for all the outputs to be created before
        # considering the component itself to have been created.
        self.register_outputs({
            'endpoint': bucket_website.website_endpoint
        })


def _allow_getobject_policy(bucket_name: str) -> str:
    return json.dumps({
        'Version': '2012-10-17',
        'Statement': [
            {
                'Effect': 'Allow',
                'Principal': '*',
                'Action': ['s3:GetObject'],
                'Resource': [
                    f'arn:aws:s3:::{bucket_name}/*',  # policy refers to bucket name explicitly
                ],
            },
        ],
    })
```

### Detailed implementation breakdown

Let's dissect this component implementation piece-by-piece:

#### Inheriting from the base class

```python
class StaticPage(pulumi.ComponentResource):
# ...
```

Inheriting from `pulumi.ComponentResource` gives us some built-in behind-the-scenes behavior that allows the component state to be tracked and run within the Pulumi engine. It also allows the underlying library to find and infer the schema of the component.

#### Outputs as class properties

```python
class StaticPage(pulumi.ComponentResource):
    endpoint: pulumi.Output[str]
# ...
```

We use a class property to store the output value. Note that it's using `pulumi.Output[str]` instead of just a regular string. This allows the end-user to access this in an asynchronous manner when writing their Pulumi program.

#### The Component constructor

```python
# ...
    def __init__(self,
                 name: str,
                 args: StaticPageArgs,
                 opts: Optional[ResourceOptions] = None) -> None:

        super().__init__('static-page-component:index:StaticPage', name, {}, opts)
# ...
```

The constructor has a few standard arguments:

- `name`: The name given to an instance of this component. When writing a Pulumi program, resources are named by the end-user. Later on in the implementation we will use this base component name to uniquely name the resources it contains.
- `args`: This is an instance of the argument class we defined earlier, containing the required inputs for our component.
- `opts`: This is an *optional* set of common resource configuration values. The [`ResourceOptions`](/docs/iac/concepts/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our sub-resources later on.

Since we're inheriting, we also need to call the base class constructor `super().__init__`. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:index:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The `index` portion of this type name is a required implmentation detail. Otherwise, we pass the `name` value into the base constructor, as well as the `opts` value, and an empty object for the `args` value.

#### Creating and managing sub-resources, dependencies, and execution order

Next we implement the `BucketV2`, `BucketWebsiteConfigurationV2`, `BucketObject`, `BucketPublicAccessBlock` and `BucketPolicy` sub-resources.

```python
# ...
        # Create a bucket
        bucket = s3.BucketV2(
            f'{name}-bucket',
            opts=ResourceOptions(parent=self))

        # Configure the bucket website
        bucket_website = s3.BucketWebsiteConfigurationV2(
            f'{name}-website',
            bucket=bucket.bucket,
            index_document={"suffix": "index.html"},
            opts=ResourceOptions(parent=bucket))

        # Create a bucket object for the index document
        s3.BucketObject(
            f'{name}-index-object',
            bucket=bucket.bucket,
            key='index.html',
            content=args.get("index_content"),
            content_type='text/html',
            opts=ResourceOptions(parent=bucket))

        # Create a public access block for the bucket
        bucket_public_access_block = s3.BucketPublicAccessBlock(
            f'{name}-public-access-block',
            bucket=bucket.id,
            block_public_acls=False,
            opts=ResourceOptions(parent=bucket))

        # Set the access policy for the bucket so all objects are readable.
        s3.BucketPolicy(
            f'{name}-bucket-policy',
            bucket=bucket.bucket,
            policy=bucket.bucket.apply(_allow_getobject_policy),
            opts=ResourceOptions(parent=bucket, depends_on=[bucket_public_access_block]))
# ...
```

##### The Bucket sub-resource

The `BucketV2` resource represents an S3 bucket, which is similar to a directory. This is our public-facing entry point for hosting website content on the internet.

Notice the use of the `name` parameter and format string to create a unique name for the bucket resource. Every resource must have a unique name. We will use the same pattern in all the sub-resources.

Another important implementation detail here is the `opts` value being passed to the sub-resource constructor. We create a new instance of `ResourceOptions` and pass the component instance as the `parent` of the `BucketV2` resource, via `parent=self` in the `ResourceOptions` class. This is an essential step to tie the sub-resources into the dependency graph.

##### The BucketWebsiteConfigurationV2 and BucketObject sub-resources

The `BucketWebsiteConfigurationV2` represents the website configuration and the `BucketObject` represents the contents of the file we will host as `index.html`.

Notice that this time we pass the `BucketV2` instance in as the `parent` to the `ResourceOptions` instances for these sub-resources, as opposed to `self` (e.g. the component). That creates a resource relationship graph like: `StaticPage` -> `BucketV2` -> `BucketObject`. We do the same thing in the `BucketPublicAccessBlock` and `BucketPolicy` resource.

Managing the dependency graph of your sub-resources is very important in a component!

Another point of interest here is the use of `args`. In the `BucketObject` constructor, we pass the contents of the `index.html` page we want to host via the `args` class. Instead of using a property accessor on the args class, we use `args.get(...)` and pass the name of the value we want.

##### The BucketPublicAccessBlock and BucketPolicy sub-resources

By default the `BucketObject` we created is not accessible to the public, so we need to unlock that access with the `BucketPublicAccessBlock` and `BucketPolicy` resources.

The `BucketPolicy` resource shows an important coding technique when implementing components: handling asynchronous output values. We use `bucket.bucket.[apply](https://www.pulumi.com/docs/iac/concepts/inputs-outputs/apply/)(...)` to generate an S3 policy document using the `_allow_getobject_policy` helper function. This respects the asynchronous workflow, materializing that value only after the bucket has been created. If we attempted to create a `BucketPolicy` before the `Bucket` existed, the operation would fail. That's because the S3 Policy document needs to use the bucket's name within S3, and we won't know what that value is until the Bucket creation operation has completed. Using `apply` here will ensure that execution of the `_allow_getobject_policy` function doesn't happen until the Bucket has been created successfully.

Just like in a Pulumi program, it's important to understand and respect the asynchronous flow of resource creation within our code. The `apply` function encodes the dependency and required order-of-operations.

The `BucketPolicy` resource also shows another technique: resource dependencies. We use the `depends_on` resource option to indicate that the `BucketPolicy` depends on the `BucketPublicAccessBlock`. This relationship is important to encode so that resource creation, modification, and deletion happens as expected.

#### Handling outputs

The last part of the constructor handles output values. First we set the `endpoint` class property to the end-point URL from the `BucketWebsiteConfigurationV2` class. Note that this is a `pulumi.Output[str]`, not a regular Python string. Outputs must use `pulumi.Output` types.

Finally, calling `self.register_outputs` signals Pulumi that the component creation process has completed.

```python
# ...
        self.endpoint = bucket_website.website_endpoint

        # By registering the outputs on which the component depends, we ensure
        # that the Pulumi CLI will wait for all the outputs to be created before
        # considering the component itself to have been created.
        self.register_outputs({
            'endpoint': bucket_website.website_endpoint
        })

# ...
```

#### Helper functions

In addition to the constructor logic, we also have a helper function `_allow_getobject_policy`:

***Example:** `staticpage.py` a helper function*

```python
# ...
def _allow_getobject_policy(bucket_name: str) -> str:
    return json.dumps({
        'Version': '2012-10-17',
        'Statement': [
            {
                'Effect': 'Allow',
                'Principal': '*',
                'Action': ['s3:GetObject'],
                'Resource': [
                    f'arn:aws:s3:::{bucket_name}/*',  # policy refers to bucket name explicitly
                ],
            },
        ],
    })
# ...
```

This function is used to create a S3 policy document, allowing public access to the objects in our bucket. It will be invoked within the context of `apply(...)`. That means that the `bucket_name`, which is normally a `pulumi.Output[str]` value, can be materialized as a normal Python string, and is passed into this function that way. Note that you can't modify the value of `bucket_name`, but you can *read* the value and use it to construct the policy document. The `json.dumps(...)` function takes the dictionary as input and returns it as a JSON formatted string.

{{% /choosable %}}

{{% choosable language go %}}

TODO: Go component implementation

{{% /choosable %}}

{{% choosable language csharp %}}

#### Add the required imports

First create a file called `StaticPage.cs`, and add the imports we will need:

***Example:** `StaticPage.cs` required imports*

```csharp
using System;
using System.Collections.Generic;

using Pulumi;
using Pulumi.Aws.S3;
using Pulumi.Aws.S3.Inputs;

using Newtonsoft.Json;
```

### Define the Component arguments

Next, we will implement the arguments class. In our example here, we will pass the contents of the webpage we want to host to the component.

***Example:** `StaticPage.cs` the Component arguments implmentation*

```csharp
public sealed class StaticPageArgs : ResourceArgs {
    [Input("indexContent")]
    public Input<string> IndexContent { get; set; } = null!;
}
```

Note that argument classes must be *serializable* and use `Pulumi.Input` types, rather than the language's default types.

### Define the Component resource

Now we can implement the component itself. Components should inherit from `Pulumi.ComponentResource`, and should accept the required arguments class we just defined in the constructor. All the work for our component happens in the constructor, and outputs are returned via class properties. At the end of the process a calling `this.RegisterOutputs` signals Pulumi that the process of creating the component resource has completed.

***Example:** `StaticPage.cs` the Component implmentation*

```csharp
class StaticPage : ComponentResource {
    [Output("endpoint")]
    public Output<string> endpoint { get; set; }

    public StaticPage(string name, StaticPageArgs args, ComponentResourceOptions? opts = null)
        : base("static-page-component:index:StaticPage", name, args, opts)
    {
        // Create a bucket
        var bucket = new BucketV2($"{name}-bucket", new() { }, new() { Parent = this });

        // Configure the bucket website
        var bucketWebsite = new BucketWebsiteConfigurationV2($"{name}-website", new() {
            Bucket = bucket.Id,
            IndexDocument = new BucketWebsiteConfigurationV2IndexDocumentArgs { Suffix = "index.html" },
        }, new() { Parent = bucket });

        // Create a bucket object for the index document
        var bucketObject = new BucketObject($"{name}-index-object", new BucketObjectArgs {
            Bucket = bucket.Bucket,
            Key = "index.html",
            Content = args.IndexContent,
            ContentType = "text/html",
        }, new() { Parent = bucket });

        // Create a public access block for the bucket
        var publicAccessBlock = new BucketPublicAccessBlock($"{name}-public-access-block", new() {
            Bucket = bucket.Id,
            BlockPublicAcls = false,
        }, new() { Parent = bucket });

        // Set the access policy for the bucket so all objects are readable
        var bucketPolicy = new BucketPolicy($"{name}-bucket-policy", new() {
            Bucket = bucket.Id,
            Policy = bucket.Bucket.Apply(this.AllowGetObjectPolicy),
        }, new() { Parent = bucket, DependsOn = publicAccessBlock });

        this.endpoint = bucketWebsite.WebsiteEndpoint;

        // By registering the outputs on which the component depends, we ensure
        // that the Pulumi CLI will wait for all the outputs to be created before
        // considering the component itself to have been created.
        this.RegisterOutputs(new Dictionary<string, object?> {
            ["endpoint"] = bucketWebsite.WebsiteEndpoint
        });
    }

    private string AllowGetObjectPolicy(string bucketName) {
        return JsonConvert.SerializeObject(new {
            Version = "2012-10-17",
            Statement = new[] { new {
                Effect = "Allow",
                Principal = "*",
                Action = new[] {
                    "s3:GetObject"
                },
                Resource = new[] {
                    $"arn:aws:s3:::{bucketName}/*"
                }
            }}
        });
    }
}
```

### Detailed implementation breakdown

Let's dissect this component implementation piece-by-piece:

#### Inheriting from the base class

```csharp
class StaticPage : ComponentResource {
    // ...
}
```

Inheriting from `Pulumi.ComponentResource` gives us some built-in behind-the-scenes behavior that allows the component state to be tracked and run within the Pulumi engine and within its host provider. It also allows the underlying library to find and infer the schema of the component.

#### Outputs as class properties

```csharp
class StaticPage : ComponentResource {
    // The URL of the static website
    [Output("endpoint")]
    public Output<string> endpoint { get; set; }
    // ...
}
```

We use a class property to store the output value. Note that it's using `Pulumi.Output<string>` instead of just a regular string. This allows the end-user to access this in an asynchronous manner when writing their Pulumi program.

#### The Component constructor

```csharp
// ...
    public StaticPage(string name, StaticPageArgs args, ComponentResourceOptions? opts = null)
        : base("static-page-component:index:StaticPage", name, args, opts)

// ...
```

The constructor has a few standard arguments:

- `name`: The name given to an instance of this component. When writing a Pulumi program, resources are named by the end-user. Later on in the implementation we will use this base component name to uniquely name the resources it contains.
- `args`: This is an instance of the argument class we defined earlier, containing the required inputs for our component.
- `opts`: This is an *optional* set of common resource configuration values. The [`ComponentResourceOptions`](/docs/iac/concepts/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our sub-resources later on.

Since we're inheriting, we also need to call the base class constructor `base(...)`. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:<module>:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The module portion of this type name is always `index` and is a required implmentation detail. Otherwise, we pass the `name`, `args`, and `opts` values from our component constructor into the base constructor.

#### Creating and managing sub-resources, dependencies, and execution order

Next we implement the `BucketV2`, `BucketWebsiteConfigurationV2`, `BucketObject`, `BucketPublicAccessBlock` and `BucketPolicy` sub-resources.

```csharp
// ...
        // Create a bucket
        var bucket = new BucketV2($"{name}-bucket", new() { }, new() { Parent = this });

        // Configure the bucket website
        var bucketWebsite = new BucketWebsiteConfigurationV2($"{name}-website", new() {
            Bucket = bucket.Id,
            IndexDocument = new BucketWebsiteConfigurationV2IndexDocumentArgs { Suffix = "index.html" },
        }, new() { Parent = bucket });

        // Create a bucket object for the index document
        var bucketObject = new BucketObject($"{name}-index-object", new BucketObjectArgs {
            Bucket = bucket.Bucket,
            Key = "index.html",
            Content = args.IndexContent,
            ContentType = "text/html",
        }, new() { Parent = bucket });

        // Create a public access block for the bucket
        var publicAccessBlock = new BucketPublicAccessBlock($"{name}-public-access-block", new() {
            Bucket = bucket.Id,
            BlockPublicAcls = false,
        }, new() { Parent = bucket });

        // Set the access policy for the bucket so all objects are readable
        var bucketPolicy = new BucketPolicy($"{name}-bucket-policy", new() {
            Bucket = bucket.Id,
            Policy = bucket.Bucket.Apply(this.AllowGetObjectPolicy),
        }, new() { Parent = bucket, DependsOn = publicAccessBlock });
// ...
```

##### The Bucket sub-resource

The `BucketV2` resource represents an S3 bucket, which is similar to a directory. This is our public-facing entry point for hosting website content on the internet.

Notice the use of the `name` parameter and format string to create a unique name for the bucket resource. Every resource must have a unique name. We will use the same pattern in all the sub-resources.

Another important implementation detail here is the `opts` value being passed to the sub-resource constructor. We create a new object and pass the component instance as the `Parent` of the `BucketV2` resource, via `Parent = this` in the `opts` object. This is an essential step to tie the sub-resources into the dependency graph.

##### The BucketWebsiteConfigurationV2 and BucketObject sub-resources

The `BucketWebsiteConfigurationV2` represents the website configuration and the `BucketObject` represents the contents of the file we will host as `index.html`.

Notice that this time we pass the `BucketV2` instance in as the `Parent` in the `opts` for these sub-resources, as opposed to `this` (e.g. the component). That creates a resource relationship graph like: `StaticPage` -> `BucketV2` -> `BucketObject`. We do the same thing in the `BucketPublicAccessBlock` and `BucketPolicy` resource.

Managing the dependency graph of your sub-resources is very important in a component!

Another point of interest here is the use of `args`. In the `BucketObject` constructor, we pass the contents of the `index.html` page we want to host via the `args` class. It's available as a strongly typed property accessor on the `StaticPageArgs` class.

##### The BucketPublicAccessBlock and BucketPolicy sub-resources

By default the `BucketObject` we created is not accessible to the public, so we need to unlock that access with the `BucketPublicAccessBlock` and `BucketPolicy` resources.

The `BucketPolicy` resource shows an important coding technique when implementing components: handling asynchronous output values. We use `bucket.bucket.Apply(...)` to generate an S3 policy document using the `AllowGetObjectPolicy` helper function. This respects the asynchronous workflow, materializing that value only after the bucket has been created. If we attempted to create a `BucketPolicy` before the `Bucket` existed, the operation would fail. That's because the S3 policy document needs to use the bucket's name within its definition, and we won't know what that value is until the Bucket creation operation has completed. Using `Apply` here will ensure that execution of the `AllowGetObjectPolicy` function doesn't happen until the bucket has been created successfully.

Just like in a Pulumi program, it's important to understand and respect the asynchronous flow of resource creation within our code. The `Apply` function encodes the dependency and required order-of-operations.

The `BucketPolicy` resource also shows another technique: resource dependencies. We use the `DependsOn` resource option to indicate that the `BucketPolicy` depends on the `BucketPublicAccessBlock`. This relationship is important to encode so that resource creation, modification, and deletion happens as expected.

#### Handling outputs

The last part of the constructor handles output values. First we set the `endpoint` class property to the website endpoint from the `BucketWebsiteConfigurationV2` class. Note that this is a `Pulumi.Output<string>`, not a regular .NET string. Outputs must use `Pulumi.Output` types.

Finally, calling `this.RegisterOutputs` signals Pulumi that the component creation process has completed.

```csharp
// ...
        this.endpoint = bucketWebsite.WebsiteEndpoint;

        // By registering the outputs on which the component depends, we ensure
        // that the Pulumi CLI will wait for all the outputs to be created before
        // considering the component itself to have been created.
        this.RegisterOutputs(new Dictionary<string, object?> {
            ["endpoint"] = bucketWebsite.WebsiteEndpoint
        });
// ...
```

#### Helper functions

In addition to the constructor logic, we also have a helper function `AllowGetObjectPolicy`:

***Example:** `StaticPage.cs` a helper function*

```csharp
// ...
    private string AllowGetObjectPolicy(string bucketName) {
        return JsonConvert.SerializeObject(new {
            Version = "2012-10-17",
            Statement = new[] { new {
                Effect = "Allow",
                Principal = "*",
                Action = new[] {
                    "s3:GetObject"
                },
                Resource = new[] {
                    $"arn:aws:s3:::{bucketName}/*"
                }
            }}
        });
    }
// ...
```

This function is used to create a S3 policy document, allowing public access to the objects in our bucket. It will be invoked within the context of `Apply(...)`. That means that the `bucketName`, which is normally a `Pulumi.Output<string>` value, can be materialized as a regular .NET string, and is passed into this function that way. Note that you can't modify the value of `bucketName`, but you can *read* the value and use it to construct the policy document. The `JsonConvert.SerializeObject(...)` function takes the object as input and returns it as a JSON formatted string.

{{% /choosable %}}

{{% choosable language java %}}

#### Add the required imports

First create a file called `StaticPage.java`, and add the imports we will need:

***Example:** `StaticPage.java` required imports*

```java
package staticpagecomponent;

import java.util.Map;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import com.pulumi.aws.s3.BucketObject;
import com.pulumi.aws.s3.BucketObjectArgs;
import com.pulumi.aws.s3.BucketPolicy;
import com.pulumi.aws.s3.BucketPolicyArgs;
import com.pulumi.aws.s3.BucketPublicAccessBlock;
import com.pulumi.aws.s3.BucketPublicAccessBlockArgs;
import com.pulumi.aws.s3.BucketV2;
import com.pulumi.aws.s3.BucketWebsiteConfigurationV2;
import com.pulumi.aws.s3.BucketWebsiteConfigurationV2Args;
import com.pulumi.aws.s3.inputs.BucketWebsiteConfigurationV2IndexDocumentArgs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.Import;

import com.pulumi.resources.ComponentResource;
import com.pulumi.resources.ComponentResourceOptions;
import com.pulumi.resources.CustomResourceOptions;
import com.pulumi.resources.ResourceArgs;
```

### Define the Component arguments

Next, we will implement the arguments class. In our example here, we will pass the contents of the webpage we want to host to the component.

***Example:** `StaticPage.java` the Component arguments implmentation*

```java
class StaticPageArgs extends ResourceArgs {
    @Import(name = "indexContent", required = true)
    private Output<String> IndexContent;

    public Output<String> indexContent() {
        return this.IndexContent;
    }

    private StaticPageArgs() {
    }

    public StaticPageArgs(Output<String> indexContent) {
        this.IndexContent = indexContent;
    }
}
```

Note that argument classes must be *serializable* and use `com.pulumi.core.Output<T>` types, rather than the language's default types.

The `@Import` decorator marks this as a *required* input and allows use to give a name for the input that could be different from the implementation here.

### Define the Component resource

Now we can implement the component itself. Components should inherit from `Pulumi.ComponentResource`, and should accept the required arguments class we just defined in the constructor. All the work for our component happens in the constructor, and outputs are returned via class properties. At the end of the process a calling `this.registerOutputs` signals Pulumi that the process of creating the component resource has completed.

***Example:** `StaticPage.java` the Component implmentation*

```java
class StaticPage extends ComponentResource {
    @Export(name = "endpoint", refs = { String.class }, tree = "[0]")
    public final Output<String> endpoint;

    public StaticPage(String name, StaticPageArgs args, ComponentResourceOptions opts) {
        super("static-page-component:index:StaticPage", name, null, opts);

        // Create a bucket
        var bucket = new BucketV2(
                String.format("%s-bucket", name),
                null,
                CustomResourceOptions.builder()
                        .parent(this)
                        .build());

        // Configure the bucket website
        var bucketWebsite = new BucketWebsiteConfigurationV2(
                String.format("%s-website", name),
                BucketWebsiteConfigurationV2Args.builder()
                        .bucket(bucket.id())
                        .indexDocument(
                                BucketWebsiteConfigurationV2IndexDocumentArgs.builder()
                                        .suffix("index.html")
                                        .build())
                        .build(),
                CustomResourceOptions.builder()
                        .parent(bucket)
                        .build());

        // Create a bucket object for the index document
        var bucketObject = new BucketObject(
                String.format("%s-index-object", name),
                BucketObjectArgs.builder()
                        .bucket(bucket.bucket())
                        .key("index.html")
                        .content(args.indexContent())
                        .contentType("text/html")
                        .build(),
                CustomResourceOptions.builder()
                        .parent(bucket)
                        .build());

        // Create a public access block for the bucket
        var publicAccessBlock = new BucketPublicAccessBlock(
                String.format("%s-public-access-block", name),
                BucketPublicAccessBlockArgs.builder()
                        .bucket(bucket.id())
                        .blockPublicAcls(false)
                        .build(),
                CustomResourceOptions.builder()
                        .parent(bucket)
                        .build());

        // Set the access policy for the bucket so all objects are readable
        var bucketPolicy = new BucketPolicy(
                String.format("%s-bucket-policy", name),
                BucketPolicyArgs.builder()
                        .bucket(bucket.id())
                        .policy(bucket.bucket().applyValue(
                                bucketName -> this.allowGetObjectPolicy(bucketName)))
                        .build(),
                CustomResourceOptions.builder()
                        .parent(bucket)
                        .dependsOn(publicAccessBlock)
                        .build());

        this.endpoint = bucketWebsite.websiteEndpoint();

        // By registering the outputs on which the component depends, we ensure
        // that the Pulumi CLI will wait for all the outputs to be created before
        // considering the component itself to have been created.
        this.registerOutputs(Map.of(
                "endpoint", bucketWebsite.websiteEndpoint()));
    }

    private String allowGetObjectPolicy(String bucketName) {
        var policyDoc = new JsonObject();
        var statementArray = new JsonArray();
        var statement = new JsonObject();
        var actionArray = new JsonArray();
        var resourceArray = new JsonArray();

        policyDoc.addProperty("Version", "2012-10-17");
        policyDoc.add("Statement", statementArray);
        statementArray.add(statement);
        statement.addProperty("Effect", "Allow");
        statement.addProperty("Principal", "*");
        statement.add("Action", actionArray);
        actionArray.add("s3:GetObject");
        statement.add("Resource", resourceArray);
        resourceArray.add(String.format("arn:aws:s3:::%s/*", bucketName));

        return new Gson().toJson(policyDoc);
    }
}
```

### Detailed implementation breakdown

Let's dissect this component implementation piece-by-piece:

#### Inheriting from the base class

```java
class StaticPage extends ComponentResource {
    // ...
}
```

Inheriting from `com.pulumi.resources.ComponentResource` gives us some built-in behind-the-scenes behavior that allows the component state to be tracked and run within the Pulumi engine and within its host provider. It also allows the underlying library to find and infer the schema of the component.

#### Outputs as class properties

```java
class StaticPage extends ComponentResource {
    // The URL of the static website
    @Export(name = "endpoint", refs = { String.class }, tree = "[0]")
    public final Output<String> endpoint;
    // ...
}
```

We use a class property to store the output value. Note that it's using `com.pulumi.core.Output<String>` instead of just a regular string. This allows the end-user to access this in an asynchronous manner when writing their Pulumi program.

The `@Export` decorator marks this as an exported output, and allows us to set a specific name for the output value.

#### The Component constructor

```java
// ...
    public StaticPage(String name, StaticPageArgs args, ComponentResourceOptions opts) {
        super("static-page-component:index:StaticPage", name, null, opts);
// ...
```

The constructor has a few standard arguments:

- `name`: The name given to an instance of this component. When writing a Pulumi program, resources are named by the end-user. Later on in the implementation we will use this base component name to uniquely name the resources it contains.
- `args`: This is an instance of the argument class we defined earlier, containing the required inputs for our component.
- `opts`: This is an *optional* set of common resource configuration values. The [`ComponentResourceOptions`](/docs/iac/concepts/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our sub-resources later on.

Since we're inheriting, we also need to call the base class constructor `super(...)`. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:<module>:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The module portion of this type name is always `index` and is a required implmentation detail. Otherwise, we pass the `name`, `args`, and `opts` values from our component constructor into the base constructor.

#### Creating and managing sub-resources, dependencies, and execution order

Next we implement the `BucketV2`, `BucketWebsiteConfigurationV2`, `BucketObject`, `BucketPublicAccessBlock` and `BucketPolicy` sub-resources.

```java
// ...
        // Create a bucket
        var bucket = new BucketV2(
                String.format("%s-bucket", name),
                null,
                CustomResourceOptions.builder()
                        .parent(this)
                        .build());

        // Configure the bucket website
        var bucketWebsite = new BucketWebsiteConfigurationV2(
                String.format("%s-website", name),
                BucketWebsiteConfigurationV2Args.builder()
                        .bucket(bucket.id())
                        .indexDocument(
                                BucketWebsiteConfigurationV2IndexDocumentArgs.builder()
                                        .suffix("index.html")
                                        .build())
                        .build(),
                CustomResourceOptions.builder()
                        .parent(bucket)
                        .build());

        // Create a bucket object for the index document
        var bucketObject = new BucketObject(
                String.format("%s-index-object", name),
                BucketObjectArgs.builder()
                        .bucket(bucket.bucket())
                        .key("index.html")
                        .content(args.indexContent())
                        .contentType("text/html")
                        .build(),
                CustomResourceOptions.builder()
                        .parent(bucket)
                        .build());

        // Create a public access block for the bucket
        var publicAccessBlock = new BucketPublicAccessBlock(
                String.format("%s-public-access-block", name),
                BucketPublicAccessBlockArgs.builder()
                        .bucket(bucket.id())
                        .blockPublicAcls(false)
                        .build(),
                CustomResourceOptions.builder()
                        .parent(bucket)
                        .build());

        // Set the access policy for the bucket so all objects are readable
        var bucketPolicy = new BucketPolicy(
                String.format("%s-bucket-policy", name),
                BucketPolicyArgs.builder()
                        .bucket(bucket.id())
                        .policy(bucket.bucket().applyValue(
                                bucketName -> this.allowGetObjectPolicy(bucketName)))
                        .build(),
                CustomResourceOptions.builder()
                        .parent(bucket)
                        .dependsOn(publicAccessBlock)
                        .build());
// ...
```

##### The Bucket sub-resource

The `BucketV2` resource represents an S3 bucket, which is similar to a directory. This is our public-facing entry point for hosting website content on the internet.

Notice the use of the `name` parameter and format string to create a unique name for the bucket resource. Every resource must have a unique name. We will use the same pattern in all the sub-resources.

Another important implementation detail here is the `opts` value being passed to the sub-resource constructor. We create a new object and pass the component instance as the `parent` of the `BucketV2` resource, via `parent(this)` in the `opts` object. This is an essential step to tie the sub-resources into the dependency graph.

##### The BucketWebsiteConfigurationV2 and BucketObject sub-resources

The `BucketWebsiteConfigurationV2` represents the website configuration and the `BucketObject` represents the contents of the file we will host as `index.html`.

Notice that this time we pass the `BucketV2` instance in as the `parent` in the `opts` for these sub-resources, as opposed to `this` (e.g. the component). That creates a resource relationship graph like: `StaticPage` -> `BucketV2` -> `BucketObject`. We do the same thing in the `BucketPublicAccessBlock` and `BucketPolicy` resource.

Managing the dependency graph of your sub-resources is very important in a component!

Another point of interest here is the use of `args`. In the `BucketObject` constructor, we pass the contents of the `index.html` page we want to host via the `args` class. It's available as a strongly typed property accessor on the `StaticPageArgs` class.

##### The BucketPublicAccessBlock and BucketPolicy sub-resources

By default the `BucketObject` we created is not accessible to the public, so we need to unlock that access with the `BucketPublicAccessBlock` and `BucketPolicy` resources.

The `BucketPolicy` resource shows an important coding technique when implementing components: handling asynchronous output values. We use `bucket.bucket.applyValue(...)` to generate an S3 policy document using the `allowGetObjectPolicy` helper function. This respects the asynchronous workflow, materializing that value only after the bucket has been created. If we attempted to create a `BucketPolicy` before the `Bucket` existed, the operation would fail. That's because the S3 policy document needs to use the bucket's name within its definition, and we won't know what that value is until the Bucket creation operation has completed. Using `applyValue` here will ensure that execution of the `allowGetObjectPolicy` function doesn't happen until the bucket has been created successfully.

Just like in a Pulumi program, it's important to understand and respect the asynchronous flow of resource creation within our code. The `applyValue` function encodes the dependency and required order-of-operations.

The `BucketPolicy` resource also shows another technique: resource dependencies. We use the `DependsOn` resource option to indicate that the `BucketPolicy` depends on the `BucketPublicAccessBlock`. This relationship is important to encode so that resource creation, modification, and deletion happens as expected.

#### Handling outputs

The last part of the constructor handles output values. First we set the `endpoint` class property to the website endpoint from the `BucketWebsiteConfigurationV2` class. Note that this is a `com.pulumi.core.Output<String>`, not a regular Java string. Outputs must use `com.pulumi.core.Output<T>` types.

Finally, calling `this.registerOutputs` signals Pulumi that the component creation process has completed.

```java
// ...
        this.endpoint = bucketWebsite.websiteEndpoint();

        // By registering the outputs on which the component depends, we ensure
        // that the Pulumi CLI will wait for all the outputs to be created before
        // considering the component itself to have been created.
        this.registerOutputs(Map.of(
                "endpoint", bucketWebsite.websiteEndpoint()));
// ...
```

#### Helper functions

In addition to the constructor logic, we also have a helper function `allowGetObjectPolicy`:

***Example:** `StaticPage.java` a helper function*

```java
// ...
    private String allowGetObjectPolicy(String bucketName) {
        var policyDoc = new JsonObject();
        var statementArray = new JsonArray();
        var statement = new JsonObject();
        var actionArray = new JsonArray();
        var resourceArray = new JsonArray();

        policyDoc.addProperty("Version", "2012-10-17");
        policyDoc.add("Statement", statementArray);
        statementArray.add(statement);
        statement.addProperty("Effect", "Allow");
        statement.addProperty("Principal", "*");
        statement.add("Action", actionArray);
        actionArray.add("s3:GetObject");
        statement.add("Resource", resourceArray);
        resourceArray.add(String.format("arn:aws:s3:::%s/*", bucketName));

        return new Gson().toJson(policyDoc);
    }
// ...
```

This function is used to create a S3 policy document, allowing public access to the objects in our bucket. It will be invoked within the context of `applyValue(...)`. That means that the `bucketName`, which is normally a `com.pulumi.core.Output<String>` value, can be materialized as a normal Java string, and is passed into this function that way. Note that you can't modify the value of `bucketName`, but you can *read* the value and use it to construct the policy document. We use `JsonObject` and `JsonArray` to construct the necessary JSON object then pass those to the `Gson.toJson(...)` function which returns it as a JSON formatted string.

{{% /choosable %}}

{{% choosable language yaml %}}

TODO: YAML component implementation

{{% /choosable %}}

{{< /chooser >}}

### Use the Component in a Pulumi Program

Let's try it out in Pulumi program. For fun, try using it in a different languages than you wrote it in, like YAML!

#### Setup the Pulumi Program

First, let's create a simple Pulumi program project. Create a new directory and a `Pulumi.yaml` file.

```bash
$ cd ..
$ mkdir use-static-page-component
```

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in JavaScript*

```yaml
name: use-static-page-component
description: A minimal JavaScript Pulumi program that uses the custom Static Page component
runtime:
  name: nodejs
  options:
    typescript: false
```

{{% /choosable %}}

{{% choosable language typescript %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in TypeScript*

```yaml
name: use-static-page-component
description: A minimal TypeScript Pulumi program that uses the custom Static Page component
runtime:
  name: nodejs
```

{{% /choosable %}}

{{% choosable language python %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in Python*

```yaml
name: use-static-page-component
description: A minimal Python Pulumi program that uses the custom Static Page component
runtime:
  name: python
  options:
    toolchain: pip
    virtualenv: venv
```

{{% /choosable %}}

{{% choosable language go %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in Go*

```yaml
name: use-static-page-component
description: A minimal Go Pulumi program that uses the custom Static Page component
runtime:
  name: go
```

{{% /choosable %}}

{{% choosable language csharp %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in C#*

```yaml
name: use-static-page-component
description: A minimal C# Pulumi program that uses the custom Static Page component
runtime:
  name: dotnet
```

{{% /choosable %}}

{{% choosable language java %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in Java*

```yaml
name: use-static-page-component
description: A minimal Java Pulumi program that uses the custom Static Page component
runtime:
  name: java
```

{{% /choosable %}}

{{% choosable language yaml %}}

***Example:** A `Pulumi.yaml` file for a Pulumi project written in YAML*

```yaml
name: use-static-page-component
description: A minimal YAML Pulumi program that uses the custom Static Page component
runtime:
  name: yaml
```

{{% /choosable %}}

{{< /chooser >}}

#### Generate the SDK

In order to use our Pulumi component from source, we will need to generate a language-specific SDK, which will allow end users to use it in a Pulumi program. From the root directory of your `use-static-page-component` Pulumi project, run the following command:

```bash
pulumi package add ../static-page-component
```

This will create a new subdirectory called `sdks/`, and in it, there will be a directory for your language SDK. One of: `dotnet`, `go`, `java`, `nodejs`, and `python`.

{{% notes type="tip" %}}
If you're authoring your Pulumi project in YAML, it is not necessary to generate a SDK! Skip ahead to the next step.
{{% /notes %}}

#### Add the component reference in Pulumi.YAML

Now, in your `Pulumi.yaml` file add the following section to load the component from source:

```yaml
packages:
  static-page-component: ../static-page-component
```

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

#### Add the NodeJS project file

Now lets create our `package.json`. We'll need the standard `pulumi` SDK and our custom component. To use that, just add the path to the generated JavaScript SDK using the format `file:<path>` instead of a package version spec.

***Example:** `package.json`*

```json
{
    "name": "use-static-page-component",
    "dependencies": {
        "@pulumi/pulumi": "3.157.0",
        "@pulumi/static-page-component": "file:sdks/static-page-component"
    }
}
```

Note that we don't need to add the Pulumi AWS provider library here, because that dependency is handled by the component project, in whatever langauge you implemented it in. We just need to carry a reference to the component SDK which provides us access to the component via RPC to its provider host. This creates a clean separation of concerns between the component implmentation and the end users of the component.

#### Install dependencies

Next, install the `pulumi` dependencies:

```bash
pulumi install
```

#### Create the Pulumi program

***Example:** `index.js` that uses the Static Page component*

```javascript
"use strict";

const pulumi = require("@pulumi/pulumi");
const staticpagecomponent = require("@pulumi/static-page-component");

const pageHTML = "<h1>I love Pulumi!</h1>";

const page = new staticpagecomponent.StaticPage("my-static-page", {
    indexContent: pageHTML
})

// Export the URL to the index page
exports.websiteURL = pulumi.interpolate `http://${page.endpoint}`;
```

{{% /choosable %}}

{{% choosable language typescript %}}

#### Add the NodeJS and TypeScript project files

Now lets create our `package.json` and `tsconfig.json`. We'll need the standard `pulumi` SDK and our custom component. To use that, just add the path to the generated TypeScript SDK using the format `file:<path>` instead of a package version spec.

***Example:** `package.json`*

```json
{
    "name": "use-static-page-component",
    "devDependencies": {
        "@types/node": "22.13.5"
    },
    "dependencies": {
        "@pulumi/pulumi": "3.157.0",
        "@pulumi/static-page-component": "file:sdks/static-page-component"
    }
}
```

Note that we don't need to add the Pulumi AWS provider library here, because that dependency is handled by the component project, in whatever langauge you implemented it in. We just need to carry a reference to the component SDK which provides us access to the component via RPC to its provider host. This creates a clean separation of concerns between the component implmentation and the end users of the component.

The TypeScript config is the same as any standard Pulumi program.

***Example:** `tsconfig.json` for a Pulumi program*

```json
{
    "compilerOptions": {
        "outDir": "bin",
        "target": "es2016",
        "module": "commonjs",
        "moduleResolution": "node",
        "sourceMap": true,
        "experimentalDecorators": true,
        "pretty": true,
        "noFallthroughCasesInSwitch": true,
        "noImplicitAny": true,
        "noImplicitReturns": true,
        "forceConsistentCasingInFileNames": true,
        "strictNullChecks": true
    },
    "files": [
        "index.ts"
    ]
}
```

#### Install dependencies

Next, install the `pulumi` dependencies:

```bash
pulumi install
```

#### Create the Pulumi program

***Example:** `index.ts` that uses the Static Page component*

```typescript
import * as pulumi from "@pulumi/pulumi";
import { StaticPage } from "@pulumi/static-page-component";

const pageHTML = "<h1>I love Pulumi!</h1>";

const page = new StaticPage('my-static-page', {
    indexContent: pageHTML
});

// Export the URL to the index page
export const websiteURL = pulumi.interpolate`http://${page.endpoint}`;
```

{{% /choosable %}}

{{% choosable language python %}}

#### Add the package dependencies

Now lets create our `requirements.txt`. We'll need the standard `pulumi` SDK and our custom component. To use that, just add the path to the generated Python SDK:

```toml
sdk/python
pulumi>=3.153.0,<4.0
```

Note that we don't need to add the Pulumi AWS provider library here, because that dependency is handled by the component project, in whatever langauge you implemented it in. We just need to carry a reference to the component SDK which provides us access to the component via RPC to its provider host. This creates a clean separation of concerns between the component implmentation and the end users of the component.

#### Setup the virtual environment

Next, set up your virtual environment:

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

#### Create the Pulumi program

***Example:** `__main__.py` that uses the Static Page component*

```python
import pulumi
from pulumi_static_page_component import StaticPage

page_html = "<h1>I love Pulumi!</h1>"
page = StaticPage('my-static-page', index_content=page_html)

# Export the URL to the index page
website_url = page.endpoint.apply(lambda v: f"http://{v}")
pulumi.export('websiteURL', website_url)
```

{{% /choosable %}}

{{% choosable language go %}}

#### Add the Go project file

Now lets create our `go.mod`. We'll need the standard `pulumi` SDK and our custom component. To use the generated Go SDK, we'll use a `replace` directive to map the package name to the SDK source directory.

***Example:** `go.mod` for our Pulumi project*

```go
module use-static-page-component

go 1.20

require github.com/pulumi/pulumi/sdk/v3 v3.157.0

replace example.com/pulumi-static-page-component/sdk/go/static-page-component => ./sdks/static-page-component/staticpagecomponent
```

{{% notes type="warning" %}}
The `pulumi package add` command may have added a `replace` directive into your `go.mod` already. If so, remove it and replace with the above example. There's a known bug w/ Go SDK generation which causes this.

The same bug also causes the Go SDK to be generated without its necessary `go.mod`. Let's create that file in the `sdks/static-page-component/staticpagecomponent` directory with the following contents:

***Example:** `go.mod` patch for our generated SDK*

```
module example.com/pulumi-static-page-component/sdk/go/static-page-component

go 1.22

toolchain go1.23.5

require github.com/pulumi/pulumi/sdk/v3 v3.147.0
```

{{% /notes %}}

Note that we don't need to add the Pulumi AWS provider library here, because that dependency is handled by the component project, in whatever langauge you implemented it in. We just need to carry a reference to the component SDK which provides us access to the component via RPC to its provider host. This creates a clean separation of concerns between the component implmentation and the end users of the component.

#### Install dependencies

Next, install the `pulumi` dependencies:

```bash
pulumi install
```

#### Create the Pulumi program

***Example:** `main.go` that uses the Static Page component*

```go
package main

import (
	staticpagecomponent "example.com/pulumi-static-page-component/sdk/go/static-page-component"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		page, err := staticpagecomponent.NewStaticPage(ctx, "my-static-page", &staticpagecomponent.StaticPageArgs{
			IndexContent: pulumi.String("<h1>I love Pulumi!</h1>"),
		})
		if err != nil {
			return err
		}

		url := page.Endpoint.ApplyT(func(endpoint string) string {
			return "http://" + endpoint
		}).(pulumi.StringOutput)

		ctx.Export("websiteURL", url)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

#### Add the .NET project file

Now lets create our `.csproj`. We'll need the standard `pulumi` SDK and our custom component. To use the generated .NET SDK, just add the relative path to the project file in the `Include` attribute instead of the name of the library.

***Example:** `use-static-page-component.csproj`*

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <AssemblyName>use-static-page-component</AssemblyName>
    <DefaultItemExcludes>$(DefaultItemExcludes);sdks/**/*.cs</DefaultItemExcludes>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Pulumi" Version="3.*" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="sdks\static-page-component\Pulumi.StaticPageComponent.csproj" />
  </ItemGroup>
</Project>
```

Note that we don't need to add the Pulumi AWS provider library here, because that dependency is handled by the component project, in whatever langauge you implemented it in. We just need to carry a reference to the component SDK which provides us access to the component via RPC to its provider host. This creates a clean separation of concerns between the component implmentation and the end users of the component.

#### Install dependencies

Next, install the `pulumi` dependencies:

```bash
pulumi install
```

#### Create the Pulumi program

***Example:** `Program.cs` that uses the Static Page component*

```csharp
using Pulumi;
using Pulumi.StaticPageComponent;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    var pageHTML = "<h1>I love Pulumi!</h1>";

    var page = new StaticPage("my-static-page", new() {
        IndexContent = pageHTML
    });

   // Export the URL of the page
   return new Dictionary<string, object?>
   {
      ["websiteURL"] = Output.Format($"http://{page.Endpoint}")
   };
});
```

{{% /choosable %}}

{{% choosable language java %}}

#### Add the Maven project file

Now lets create our `pom.xml`. We'll need the standard `pulumi` SDK and our custom component.

We'll need to add the sources from the generated SDK output into the build sources Maven looks for, and also add the dependencies. The output of the `pulumi package add` command should have given instructions on the necessary dependencies to add, in XML format. It will also suggest copying the source files into your `src/main` folder. Instead, we'll leave the SDK files in place, and modify our build configuration to look in that directory as well as our normal source directory.

***Example:** `pom.xml`*

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.pulumi</groupId>
    <artifactId>use-static-page-component</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <encoding>UTF-8</encoding>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <maven.compiler.release>11</maven.compiler.release>
        <mainClass>myproject.App</mainClass>
        <mainArgs />
    </properties>

    <dependencies>
        <dependency>
            <groupId>com.pulumi</groupId>
            <artifactId>pulumi</artifactId>
            <version>[1.3,2.0)</version>
        </dependency>
        <!-- Add the SDK's dependencies, based on the output from the `pulumi package add` command -->
        <dependency>
            <groupId>com.google.code.findbugs</groupId>
            <artifactId>jsr305</artifactId>
            <version>3.0.2</version>
        </dependency>
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.8.9</version>
        </dependency>
    </dependencies>

    <build>
        <!-- Change the root directory that Maven uses to look for sources -->
        <sourceDirectory>.</sourceDirectory>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.2.2</version>
                <configuration>
                    <archive>
                        <manifest>
                            <addClasspath>true</addClasspath>
                            <mainClass>${mainClass}</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-assembly-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <archive>
                        <manifest>
                            <addClasspath>true</addClasspath>
                            <mainClass>${mainClass}</mainClass>
                        </manifest>
                    </archive>
                    <descriptorRefs>
                        <descriptorRef>jar-with-dependencies</descriptorRef>
                    </descriptorRefs>
                </configuration>
                <executions>
                    <execution>
                        <id>make-my-jar-with-dependencies</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.0.0</version>
                <configuration>
                    <mainClass>${mainClass}</mainClass>
                    <commandlineArgs>${mainArgs}</commandlineArgs>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-wrapper-plugin</artifactId>
                <version>3.1.0</version>
                <configuration>
                    <mavenVersion>3.8.5</mavenVersion>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>11</source>
                    <target>11</target>

                    <!-- Add path glob specs for our two source locations -->
                    <includes>
                        <include>src/main/**/*.java</include>
                        <include>sdks/static-page-component/src/main/**/*.java</include>
                    </includes>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

Note that we don't need to add the Pulumi AWS provider library here, because that dependency is handled by the component project, in whatever langauge you implemented it in. We just need to carry a reference to the component SDK, and add its dependencies, which will provide us access to the component via RPC, which is running inside of its provider host. This creates a clean separation of concerns between the component implmentation and the end users of the component.

#### Install dependencies

Next, install the `pulumi` dependencies:

```bash
pulumi install
```

#### Create the Pulumi program

Make a new subdirectory called `src/main/java/myproject` and in it, create a file called `App.java`.

***Example:** `App.java` that uses the Static Page component*

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.staticpagecomponent.StaticPage;
import com.pulumi.staticpagecomponent.StaticPageArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            final var pageHTML = "<h1>I love Pulumi!</h1>";

            var page = new StaticPage("my-bucket", StaticPageArgs.builder()
                .indexContent(pageHTML).build()
            );

            ctx.export("websiteURL", page.endpoint().applyValue(v->String.format("http://%s", v)));
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

#### Create the Pulumi program

Now we can define our Static Page component resource in the `Pulumi.yaml` file. Add the following section:

***Example:** `Pulumi.yaml` that uses the Static Page component*

```yaml
resources:
  my-static-page:
    type: static-page-component:StaticPage
    properties:
      indexContent: "<h1>I love Pulumi!</h1>"
outputs:
  websiteURL: http://${my-static-page.endpoint}
```

{{% /choosable %}}

{{< /chooser >}}

Finally, run the Pulumi update and we will see our component resource creates, as well as its sub-resources.

```bash
$ pulumi up
...
     Type                                          Name                                Status
 +   pulumi:pulumi:Stack                           use-static-page-component-dev       created (8s)
 +   └─ static-page-component:index:StaticPage     my-static-page                      created (5s)
 +      └─ aws:s3:BucketV2                         my-static-page-bucket               created (2s)
 +         ├─ aws:s3:BucketPublicAccessBlock       my-static-page-public-access-block  created (0.84s)
 +         ├─ aws:s3:BucketWebsiteConfigurationV2  my-static-page-website              created (0.91s)
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

## Sharing and Reuse

In the above examples, the component was referenced from a nearby directory, local to the machine. In order to share a component, it needs to be accessed outside of your local machine. There are two main ways to do that; sharing via a Git repo, or publishing as a Pulumi Package.

### Sharing via Git

Storing a component in a Git repository allows for version control, collaboration, and easier integration into multiple projects. Developers can add the component to their Pulumi projects using the command:

```bash
$ pulumi package add <repo_url>@<release-version>
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

### Sharing via Pulumi Package

Publishing a component as a Pulumi package makes it easier to distribute and integrate into Pulumi workflows. This method enables community contributions and ensures that infrastructure components remain modular and maintainable. By packaging the component, it becomes easier to reuse across teams and projects, improving consistency and efficiency in infrastructure management. It also makes your component available for use within Pulumi Cloud Deployments.

Learn more in the [Package and publish a Component](/docs/iac/using-pulumi/extending-pulumi/package-and-publish-a-component/) guide.
