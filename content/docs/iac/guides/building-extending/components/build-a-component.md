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

This guide will walk you through the steps of making a [Pulumi Component](/docs/iac/concepts/components/) suitable for reuse in all languages and cloud environments.

{{< notes type="info" >}}
**Prerequisites:**

- The [Pulumi CLI](/docs/install/)
- One of Pulumi’s [supported language runtimes](/docs/languages-sdks/) installed
- Access to a Git hosting environment *(optional)*

{{< /notes >}}

## Why Write a Component?

Pulumi Components provide a way to encapsulate best practices, ensuring that security policies and deployment patterns remain consistent across projects. They also help reduce code duplication by allowing you to define reusable infrastructure patterns. By structuring infrastructure as components, maintainability improves, and teams can work more efficiently.

- **Sharing and Reusability**: Do more with less code. Don't repeat yourself.
- **Best Practices and Policy**: Encode company standards and policy.
- **Multi-language Support**: When packaged as a Pulumi plugin package, a component written in one language can be consumed from any other Pulumi-supported language via a generated SDK.

## How It Works

Pulumi Components are implemented as custom classes in any Pulumi-supported language. A component extends `pulumi.ComponentResource` and groups multiple resources into a single, reusable abstraction, letting you define infrastructure once and apply it consistently across multiple environments.

Once you've written a component, you have a few options for how to share it:

- **Use it directly** in a Pulumi program written in the same language as the component — the simplest path when the component will only ever be used from that one language.
- **Publish it as a native-language package** (npm, PyPI, NuGet, Maven, Go modules) so other Pulumi programs in the same language can install it like any other library.
- **Package it as a Pulumi plugin package** so it can be consumed from any Pulumi-supported language via a generated SDK. This is the recommended path for components meant for broad reuse — see [Authoring a Source-Based Plugin Package](/docs/iac/guides/building-extending/packages/source-based-plugin/).

## Structure of a Component

A Pulumi Component consists of two main parts you write:

- The **component resource** encapsulates multiple Pulumi resources, grouping them into a logical unit.
- The **component resource arguments** define configurable input properties, allowing users to specify parameters that tailor the component's behavior to specific needs.

This guide focuses on writing those two parts. To turn the component into an installable plugin package — adding `PulumiPlugin.yaml`, the language manifest, and the entry file that hosts the provider — see [Authoring a Source-Based Plugin Package](/docs/iac/guides/building-extending/packages/source-based-plugin/) once you've written your class.

## Example: Static Web Page Component

In this example, we'll create a static website component in AWS Simple Storage Service (S3). The component will manage the following five child resources necessary to implement a basic S3 hosted static website:

- a [`Bucket`](/registry/packages/aws/api-docs/s3/bucket/) resource
- a [`BucketWebsiteConfiguration`](/registry/packages/aws/api-docs/s3/bucketwebsiteconfiguration/) resource to set up the website configuration
- a [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) resource to hold the raw site content
- a [`BucketPublicAccessBlock`](/registry/packages/aws/api-docs/s3/bucketpublicaccessblock/) resource to manage public access
- a [`BucketPolicy`](/registry/packages/aws/api-docs/s3/bucketpolicy/) resource to set the Bucket policy

The component will take as input the contents of the file you wish to host, and will output the S3 endpoint used to access it.

***Example:** Using the custom StaticPage component in a Pulumi Program*

{{< example-program path="sample-components" languages="yaml" >}}

The core implementation of the AWS API is handled by the [Pulumi AWS Provider](/registry/packages/aws/), which gives us those five underlying resource types. Our `StaticPage` component will work with those existing _resource_ types and create a new type of resource with a simpler API.

The walkthrough below focuses on the component class itself. The surrounding project layout — the directory, `PulumiPlugin.yaml`, language manifest (`package.json`, `pyproject.toml`, `go.mod`, `.csproj`, or `pom.xml`), and entry file — is covered in [Authoring a Source-Based Plugin Package](/docs/iac/guides/building-extending/packages/source-based-plugin/). You can scaffold the project there first and return here for the class implementation, or write the class first and wrap it later.

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

YAML components do not need to explicitly manage dependencies or import external libraries. The necessary packages will be resolved and automatically installed by the Pulumi engine, based on the unique resource type identifiers in the component's child resources.

{{% /choosable %}}

{{< /chooser >}}

### Define the Component arguments

Next, we will declare the component's arguments. Most languages model these as a class; Go uses a struct, and YAML uses an `inputs:` block. In our example, we'll pass the contents of the webpage we want to host into the component.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

***Example:** `StaticPage.ts` the Component arguments implementation*

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:4-6" >}}

Note that argument classes must be *serializable* and use `pulumi.Input` types, rather than the language's default types. Certain types like union types (e.g., `string | number`) and functions are not supported due to schema inference limitations. For details on type requirements and limitations, see [Component arguments and type requirements](#component-arguments-and-type-requirements).

{{% /choosable %}}

{{% choosable language python %}}

***Example:** `static_page.py` the Component arguments implementation*

{{< example-program path="sample-components" languages="python:static_page.py:9-11" >}}

Note that argument classes must be *serializable* and use `pulumi.Input` types, rather than the language's default types. This means certain types like union types and functions are not supported. For details on type requirements and limitations, see [Component arguments and type requirements](#component-arguments-and-type-requirements).

Python class properties are typically written in lowercase with words separated by underscores, known as [`snake_case`](https://en.wikipedia.org/wiki/Snake_case), however properties in the [Pulumi package schema](https://www.pulumi.com/docs/iac/using-pulumi/extending-pulumi/schema/) are usually written in [`camelCase`](https://en.wikipedia.org/wiki/Camel_case), where capital letters are used to separate words. To follow these conventions, the inferred schema for a component will have translated property names. In our example `index_content` will become `indexContent` in the schema. When using a component, the property names will follow the conventions of that language, for example if we use our component from TypeScript, we would refer to `indexContent`, but if we use it from Python, we would use `index_content`.

{{% /choosable %}}

{{% choosable language go %}}
***Example:** `static_page.go` the Component arguments implementation*

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:11-13" >}}

Note that argument struct fields must be *serializable* and use `pulumi.*Input` types, rather than the language's default types. This means complex or platform-specific types may not be supported. For details on type requirements and limitations, see [Component arguments and type requirements](#component-arguments-and-type-requirements).

Go struct fields are typically written in title case, with the first letter capitalized and capital letters used to separate words, however properties in the [Pulumi package schema](https://www.pulumi.com/docs/iac/using-pulumi/extending-pulumi/schema/) are usually written in [`camelCase`](https://en.wikipedia.org/wiki/Camel_case), with the first letter in lowercase and capital letters used to separate words. To follow these conventions, the inferred schema for a component will have translated property names. In our example `IndexContent` will become `indexContent` in the schema. When using a component, the property names will follow the conventions of that language, for example if we use our component from TypeScript, we would refer to `indexContent`, but if we use it from Go, we would use `IndexContent`.

{{% /choosable %}}

{{% choosable language csharp %}}

***Example:** `StaticPage.cs` the Component arguments implementation*

{{< example-program path="sample-components" languages="csharp:StaticPage.cs:10-13" >}}

Note that argument classes must be *serializable* and use `Pulumi.Input` types, rather than the language's default types. This means complex or platform-specific types may not be supported. For details on type requirements and limitations, see [Component arguments and type requirements](#component-arguments-and-type-requirements).

{{% /choosable %}}

{{% choosable language java %}}

***Example:** `StaticPage.java` the Component arguments implementation*

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:26-40" >}}

Note that argument classes must be *serializable* and use `com.pulumi.core.Output<T>` types, rather than the language's default types. This means complex or platform-specific types may not be supported. For details on type requirements and limitations, see [Component arguments and type requirements](#component-arguments-and-type-requirements).

The `@Import` annotation marks this as a *required* input and allows us to give a name for the input that could be different from the implementation here.

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

Now we can implement the component itself. Components should inherit from `pulumi.ComponentResource`, and should accept the arguments class we just defined in the constructor. All the work for our component happens in the constructor, and outputs are returned via class properties. At the end of the process, calling `self.registerOutputs` signals Pulumi that the process of creating the component resource has completed.

***Example:** `StaticPage.ts` the Component implementation*

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:8-83" >}}

{{% /choosable %}}

{{% choosable language python %}}

Now we can implement the component itself. Components should inherit from `pulumi.ComponentResource`, and should accept the arguments class we just defined in the constructor. All the work for our component happens in the constructor, and outputs are returned via class properties. At the end of the process, calling `self.register_outputs` signals Pulumi that the process of creating the component resource has completed.

***Example:** `static_page.py` the Component implementation*

{{< example-program path="sample-components" languages="python:static_page.py:14-59" >}}

{{% /choosable %}}

{{% choosable language go %}}
Now we can implement the component itself. Component structs should include `pulumi.ResourceState` and define the consumable outputs, which follow the same general rules as inputs. Go has no constructors, so all the work for building our component happens in the `NewStaticPage` factory function.

***Example:** `static_page.go` the Component implementation*

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:15-96" >}}

{{% /choosable %}}

{{% choosable language csharp %}}

Now we can implement the component itself. Components should inherit from `Pulumi.ComponentResource`, and should accept the arguments class we just defined in the constructor. All the work for our component happens in the constructor, and outputs are returned via class properties. At the end of the process, calling `this.RegisterOutputs` signals Pulumi that the process of creating the component resource has completed.

***Example:** `StaticPage.cs` the Component implementation*

{{< example-program path="sample-components" languages="csharp:StaticPage.cs:15-68" >}}

{{% /choosable %}}

{{% choosable language java %}}

Now we can implement the component itself. Components should inherit from `Pulumi.ComponentResource`, and should accept the arguments class we just defined in the constructor. All the work for our component happens in the constructor, and outputs are returned via class properties. At the end of the process, calling `this.registerOutputs` signals Pulumi that the process of creating the component resource has completed.

***Example:** `StaticPage.java` the Component implementation*

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:42-125" >}}

{{% /choosable %}}

{{% choosable language yaml %}}

Now we can implement the component itself. Under the [`components` key](/docs/iac/languages-sdks/yaml/yaml-component-reference/), create one or more component definitions. A component in YAML follows the following structure:

```yaml
components:
  MyComponent:      # the component name
    inputs:         # one or more input values
    resources:      # one or more child resource definitions
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
- `opts`: This is an *optional* set of common resource configuration values. The [`ComponentResourceOptions`](/docs/iac/concepts/resources/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our child resources later on.

Since we're inheriting, we also need to call the base class constructor `super(...)`. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:index:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The `index` portion of this type name is a required implementation detail. Otherwise, we pass the `name`, `args`, and `opts` values from our component constructor into the base constructor.

{{< notes type="warning" >}}
Changing the resource type name after a component has been deployed will cause all existing resources of that type to be recreated. Change the type name with extreme caution.
{{< /notes >}}

#### Child resources

All five child resources — `Bucket`, `BucketWebsiteConfiguration`, `BucketObject`, `BucketPublicAccessBlock`, and `BucketPolicy` — are created inside the constructor:

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:14-61" >}}

When creating child resources inside the component:

- **Set `parent: this`** on every child resource so it appears under the component in the resource graph and inherits the component's provider configuration.
- **Template each child resource's name** with the component's `name` parameter (e.g., `` `${name}-bucket` ``).

{{< notes type="warning" >}}
Always template child resource names with the component's `name` parameter. If you hard-code a name like `"bucket"`, every instance of the component will try to register a resource with the same name and Pulumi will fail with a duplicate-URN error. Renaming a component instance also won't propagate to its hard-coded children, which can cause replacement conflicts on the next update.
{{< /notes >}}

#### Handling outputs

The last part of the constructor handles output values. First we set the `endpoint` class property to the website endpoint from the `BucketWebsiteConfiguration` class. Note that this is a `pulumi.Output<string>`, not a regular TypeScript string. Outputs must use `pulumi.Output` types.

Finally, calling `this.registerOutputs` signals Pulumi that the component creation process has completed.

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:63-67" >}}

#### Helper functions

In addition to the constructor logic, we also have a helper function `allowGetObjectPolicy`:

***Example:** `StaticPage.ts` a helper function*

{{< example-program path="sample-components" languages="typescript:StaticPage.ts:70-82" >}}

This function is used to create a S3 policy document, allowing public access to the objects in our bucket. It will be invoked within the context of `apply(...)`. That means that the `bucketName`, which is normally a `pulumi.Output<string>` value, can be materialized as a normal TypeScript string, and is passed into this function that way. Note that you can't modify the value of `bucketName`, but you can *read* the value and use it to construct the policy document. The `JSON.stringify(...)` function takes the object as input and returns it as a JSON formatted string.

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
- `opts`: This is an *optional* set of common resource configuration values. The [`ComponentResourceOptions`](/docs/iac/concepts/resources/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our child resources later on.

Since we're inheriting, we also need to call the base class constructor `super().__init__`. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:index:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The `index` portion of this type name is a required implementation detail. Otherwise, we pass the `name` value into the base constructor, as well as the `opts` value, and an empty object for the `args` value.

{{< notes type="warning" >}}
Changing the resource type name after a component has been deployed will cause all existing resources of that type to be recreated. Change the type name with extreme caution.
{{< /notes >}}

#### Child resources

All five child resources — `Bucket`, `BucketWebsiteConfiguration`, `BucketObject`, `BucketPublicAccessBlock`, and `BucketPolicy` — are created inside the constructor:

{{< example-program path="sample-components" languages="python:static_page.py:25-53" >}}

When creating child resources inside the component:

- **Set `parent=self`** via `pulumi.ResourceOptions(parent=self)` on every child resource so it appears under the component in the resource graph and inherits the component's provider configuration.
- **Template each child resource's name** with the component's `name` parameter (e.g., `f"{name}-bucket"`).

{{< notes type="warning" >}}
Always template child resource names with the component's `name` parameter. If you hard-code a name like `"bucket"`, every instance of the component will try to register a resource with the same name and Pulumi will fail with a duplicate-URN error. Renaming a component instance also won't propagate to its hard-coded children, which can cause replacement conflicts on the next update.
{{< /notes >}}

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

#### The component factory function

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:20-25" >}}

The factory function has a few standard arguments:

- `ctx`: The Pulumi context, which allows for interaction w/ the Pulumi engine
- `name`: The name given to an instance of this component. When writing a Pulumi program, resources are named by the end-user. Later on in the implementation we will use this base component name to uniquely name the resources it contains.
- `args`: This is an instance of the argument struct we defined earlier, containing the inputs for our component.
- `opts`: This is an *optional* set of common resource configuration values. The [`ComponentResourceOptions`](/docs/iac/concepts/resources/options/) struct is part of the basic API for all Pulumi resources, and will be passed to the factory functions of our child resources later on.

The next step is to register our new component instance with Pulumi via the `ctx` instance. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:index:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The `index` portion of this type name is a required implementation detail. Otherwise, we pass the `name` value, our component instance, as well as the `opts` values.

{{< notes type="warning" >}}
Changing the resource type name after a component has been deployed will cause all existing resources of that type to be recreated. Change the type name with extreme caution.
{{< /notes >}}

#### Child resources

All five child resources — `Bucket`, `BucketWebsiteConfiguration`, `BucketObject`, `BucketPublicAccessBlock`, and `BucketPolicy` — are created inside the factory function:

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:27-91" >}}

When creating child resources inside the component:

- **Pass `pulumi.Parent(comp)`** (using whatever variable name holds your component instance) to every child resource's factory function so it appears under the component in the resource graph and inherits the component's provider configuration.
- **Template each child resource's name** with the `name` parameter (e.g., `fmt.Sprintf("%s-bucket", name)`).

{{< notes type="warning" >}}
Always template child resource names with the component's `name` parameter. If you hard-code a name like `"bucket"`, every instance of the component will try to register a resource with the same name and Pulumi will fail with a duplicate-URN error. Renaming a component instance also won't propagate to its hard-coded children, which can cause replacement conflicts on the next update.
{{< /notes >}}

#### Handling outputs

The last part of the factory function handles output values. First we set the `Endpoint` struct field to the end-point URL from the `BucketWebsiteConfiguration` resource. Note that this is a `pulumi.StringOutput`, not a regular Go string. Outputs must use `pulumi.Output` types.

Finally, return the component instance.

{{< example-program path="sample-components" languages="go:staticpagecomponent/static_page.go:93-96" >}}

#### Helper functions

In addition to the factory function logic, we also had this inline helper function `allowGetObjectPolicy`:

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
- `opts`: This is an *optional* set of common resource configuration values. The [`ComponentResourceOptions`](/docs/iac/concepts/resources/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our child resources later on.

Since we're inheriting, we also need to call the base class constructor `base(...)`. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:<module>:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The module portion of this type name is always `index` and is a required implementation detail. Otherwise, we pass the `name`, `args`, and `opts` values from our component constructor into the base constructor.

{{< notes type="warning" >}}
Changing the resource type name after a component has been deployed will cause all existing resources of that type to be recreated. Change the type name with extreme caution.
{{< /notes >}}

#### Child resources

All five child resources — `Bucket`, `BucketWebsiteConfiguration`, `BucketObject`, `BucketPublicAccessBlock`, and `BucketPolicy` — are created inside the constructor:

{{< example-program path="sample-components" languages="csharp:StaticPage.cs:22-44" >}}

When creating child resources inside the component:

- **Set `Parent = this`** via `new CustomResourceOptions { Parent = this }` on every child resource so it appears under the component in the resource graph and inherits the component's provider configuration.
- **Template each child resource's name** with the `name` parameter (e.g., `$"{name}-bucket"`).

{{< notes type="warning" >}}
Always template child resource names with the component's `name` parameter. If you hard-code a name like `"bucket"`, every instance of the component will try to register a resource with the same name and Pulumi will fail with a duplicate-URN error. Renaming a component instance also won't propagate to its hard-coded children, which can cause replacement conflicts on the next update.
{{< /notes >}}

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

The `@Export` annotation marks this as an exported output, and allows us to set a specific name for the output value.

#### The Component constructor

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:46-47" >}}

The constructor has a few standard arguments:

- `name`: The name given to an instance of this component. When writing a Pulumi program, resources are named by the end-user. Later on in the implementation we will use this base component name to uniquely name the resources it contains.
- `args`: This is an instance of the argument class we defined earlier, containing the inputs for our component.
- `opts`: This is an *optional* set of common resource configuration values. The [`ComponentResourceOptions`](/docs/iac/concepts/resources/options/) class is part of the basic API for all Pulumi resources, and will be passed to the constructors of our child resources later on.

Since we're inheriting, we also need to call the base class constructor `super(...)`. The first parameter is the name of the resource type, which is very important to get right. The resource type name has the following format: `<package-name>:<module>:<component-class-name>`. It must match *exactly*. Keep this in mind if you refactor the name of your package or the component's class name. The module portion of this type name is always `index` and is a required implementation detail. Otherwise, we pass the `name`, `args`, and `opts` values from our component constructor into the base constructor.

{{< notes type="warning" >}}
Changing the resource type name after a component has been deployed will cause all existing resources of that type to be recreated. Change the type name with extreme caution.
{{< /notes >}}

#### Child resources

All five child resources — `Bucket`, `BucketWebsiteConfiguration`, `BucketObject`, `BucketPublicAccessBlock`, and `BucketPolicy` — are created inside the constructor:

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:49-118" >}}

When creating child resources inside the component:

- **Call `.parent(this)`** on the resource options builder for every child resource so it appears under the component in the resource graph and inherits the component's provider configuration.
- **Template each child resource's name** with the `name` parameter (e.g., `String.format("%s-bucket", name)`).

{{< notes type="warning" >}}
Always template child resource names with the component's `name` parameter. If you hard-code a name like `"bucket"`, every instance of the component will try to register a resource with the same name and Pulumi will fail with a duplicate-URN error. Renaming a component instance also won't propagate to its hard-coded children, which can cause replacement conflicts on the next update.
{{< /notes >}}

#### Handling outputs

The last part of the constructor handles output values. First we set the `endpoint` class property to the website endpoint from the `BucketWebsiteConfiguration` class. Note that this is a `com.pulumi.core.Output<String>`, not a regular Java string. Outputs must use `com.pulumi.core.Output<T>` types.

Finally, calling `this.registerOutputs` signals Pulumi that the component creation process has completed.

{{< example-program path="sample-components" languages="java:src/main/java/myproject/StaticPage.java:120-124" >}}

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

#### Child resources

All five child resources — `Bucket`, `BucketWebsiteConfiguration`, `BucketObject`, `BucketPublicAccessBlock`, and `BucketPolicy` — are declared under the `resources:` block:

{{< example-program path="sample-components" languages="yaml:sample-components/PulumiPlugin.yaml:8-53" >}}

In YAML, child resources declared under the `resources:` key are automatically parented to the component instance, and their names are scoped under the component instance at runtime — so neither an explicit `parent` option nor manual name templating is required. Use input values via `${input-name}` interpolation to pass arguments into child resource properties.

#### Handling outputs

The last part of the component definition handles output values. First we set the `endpoint` output to the website endpoint from the `BucketWebsiteConfiguration` resource. This uses standard string interpolation and automatically handles asynchronous value resolution, waiting to assign the `endpoint` output until `bucketWebsite.websiteEndpoint` is available.

{{< example-program path="sample-components" languages="yaml:sample-components/PulumiPlugin.yaml:55-56" >}}

#### Helper functions

In addition to the component definitions, we are also using a helper function `fn::toJSON:`:

***Example:** YAML helper function*

{{< example-program path="sample-components" languages="yaml:sample-components/PulumiPlugin.yaml:41-53" >}}

This function is used to create a S3 policy document, allowing public access to the objects in our bucket. It will be invoked only when the interpolated value `${bucket.bucket}` is available as a standard string. We construct a YAML object which is then serialized to a JSON formatted string and assigned to the `policy` property.

{{% /choosable %}}

{{< /chooser >}}

### Use the Component in a Pulumi Program

You can either reference the component directly from a Pulumi program in the same language, or package it for distribution so it can be consumed from any Pulumi-supported language. See [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) for the packaging options and how to choose between them.

## Implementation details

The walkthrough above demonstrated a complete component implementation. The sections below cover the rules and requirements in detail as a reference. Define the arguments first, then write the component resource that consumes them, then add child resources, outputs, and any provider configuration.

### Component arguments and type requirements

When packaging a component as a Pulumi plugin package, the arguments class has specific requirements due to schema generation and serialization. These constraints ensure component arguments can be transmitted to the Pulumi engine and reconstructed in the consumer's language when the component is consumed from a different language than it was authored in. Components used directly in the same language (without packaging) can be more flexible, but following these guidelines keeps the door open to packaging later.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

**Args shape**

Define your args as a TypeScript `interface`. The analyzer rejects classes and `type` aliases. The interface doesn't need to be exported, but it must be reachable from the entry point through normal imports.

```typescript
export interface MyComponentArgs {
    name: pulumi.Input<string>;
    count?: pulumi.Input<number>;
}
```

**Supported types**

- `string`, `number`, `boolean`
- `T[]` arrays
- Index-signature objects: `{ [key: string]: T }`
- `pulumi.Input<T>`, `pulumi.Output<T>`
- Nested interfaces
- `pulumi.Asset`, `pulumi.Archive`
- Resource types
- `Partial<T>`, `Required<T>`
- Enums — both the `enum` keyword and the "as const object" pattern are recognized:

```typescript
enum MyEnum { Value1 = "Value1", Value2 = "Value2" }

const MyEnum = { Value1: "Value1", Value2: "Value2" } as const;
type MyEnum = typeof MyEnum[keyof typeof MyEnum];
```

**Optional vs required**

Use `?:` or `| undefined`. `| null` alone is **not** optional — strict null checks are enabled, so `null` and `undefined` are distinct.

**Unsupported types**

- Arbitrary union types beyond `T | undefined`, `Input<T>`, `Output<T>`, `Partial<T>`, and `Required<T>`
- Functions and callbacks (they can't be represented in the schema)

```typescript
// ❌ Won't work — union types and functions are not supported
export interface MyComponentArgs {
    value: string | number;  // Union — unsupported
    callback: () => void;    // Function — unsupported
}

// ✅ Use primitives wrapped in Input types
export interface MyComponentArgs {
    value: pulumi.Input<string>;
    count: pulumi.Input<number>;
}
```

**Naming**

Field names pass through to the schema verbatim — `myFoo` becomes `myFoo`, not `my_foo`. Use camelCase, which matches both the TypeScript convention and the schema convention.

**Best practices**

- Wrap every scalar in `pulumi.Input<T>` so consumers can pass plain values or outputs from other resources without `apply`.
- Mark optional fields with `?:` and document their default behavior.
- Keep the args interface flat — deeply nested structures make components harder to use.

{{% /choosable %}}

{{% choosable language python %}}

**Args shape**

Any class with type-annotated attributes works — a plain class, a `@dataclass`, or a `TypedDict`. `@dataclass` is recommended for ergonomics but not required.

```python
import pulumi
from dataclasses import dataclass
from typing import Optional

@dataclass
class MyComponentArgs:
    name: pulumi.Input[str]
    count: Optional[pulumi.Input[int]] = None
```

**Supported types**

- `str`, `int`, `float`, `bool`
- `list[T]` (or `List[T]`)
- `dict[str, T]` (or `Dict[str, T]`) — string keys only
- `pulumi.Input[T]`, `pulumi.Output[T]`
- Nested classes and dataclasses
- `pulumi.Asset`, `pulumi.Archive`
- Resource types
- `enum.Enum` subclasses — emitted as separate schema type definitions:

```python
from enum import Enum

class MyEnum(Enum):
    VALUE1 = "Value1"
    VALUE2 = "Value2"
```

**Optional vs required**

Use `Optional[T]` or `T | None`. The presence of a default value does **not** make a field optional in the schema — only the type annotation does.

**Unsupported types**

- Arbitrary unions beyond `Optional[T]` (a `Union` with anything other than `None` raises an error)
- Functions and callbacks

**Naming**

Use Python's `snake_case` for attributes — the analyzer converts to `camelCase` in the schema. Example: `rsa_bits` becomes `rsaBits`.

**Best practices**

- Wrap scalars in `pulumi.Input[T]` so consumers can pass plain values or outputs from other resources.
- Use `Optional[T]` with a sensible default for fields the consumer can omit.
- Use `@dataclass` for cleaner constructor and `repr` behavior.
- Prefer `enum.Enum` over magic strings for constrained values.

{{% /choosable %}}

{{% choosable language go %}}

**Args shape**

A plain struct (no embedded base). The factory function takes a pointer to it.

```go
type MyComponentArgs struct {
    Name  pulumi.StringInput `pulumi:"name"`
    Count pulumi.IntInput    `pulumi:"count,optional"`
}
```

**Supported types**

- `pulumi.StringInput`, `pulumi.IntInput`, `pulumi.BoolInput`, `pulumi.Float64Input`
- Pointer variants for optional scalars: `pulumi.StringPtrInput`, etc.
- Array variants: `pulumi.StringArrayInput`, etc.
- Map variants: `pulumi.StringMapInput`, etc. (string keys only)
- `pulumi.AssetOrArchiveInput`
- Nested args structs (also tagged with `pulumi:""`)

**Struct tags**

- `pulumi:"fieldName"` — required; the value is the schema name verbatim, so use camelCase.
- `pulumi:"fieldName,optional"` — optional.
- `pulumi:"fieldName,skip"` — exclude from marshaling/unmarshaling entirely.

**Optional vs required**

Use the `,optional` tag suffix. Pointer types like `*string` also signal optionality but the `,optional` tag is the canonical pattern.

**Unsupported types**

- Enums — Go has no native enum type, and the `infer` package does not synthesize them from string constants.
- Plain Go primitives (`string`, `int`, etc.) in args — use the `pulumi.*Input` wrappers so consumers can pass outputs from other resources.
- Map keys other than `string`.

**Naming**

The tag value is the schema name verbatim — author it in camelCase. The Go field name itself follows Go conventions (PascalCase for exported fields).

**Best practices**

- Always use `pulumi.*Input` wrappers in args, never plain Go types.
- Mark optional fields with `,optional` and use the `Ptr` input variants where consumers may pass nothing.
- Validate cross-field invariants in the factory function before registering child resources.
- Keep args structs flat — deep nesting is harder for consumers to construct.

{{% /choosable %}}

{{% choosable language csharp %}}

**Args shape**

A `public class MyComponentArgs : ResourceArgs`. The component's constructor must accept exactly three parameters: `(string name, MyComponentArgs args, ComponentResourceOptions opts)`. The analyzer doesn't recognize other constructor signatures.

```csharp
using Pulumi;

public class MyComponentArgs : ResourceArgs
{
    [Input("name", required: true)]
    public Input<string> Name { get; set; } = null!;

    [Input("count")]
    public Input<int>? Count { get; set; }
}
```

**Supported types**

- `string`, `int`, `long`, `double`, `bool`
- `T[]`, `List<T>`, `IList<T>`
- `Dictionary<string, V>`, `IDictionary<string, V>` (string keys only)
- `Input<T>`, `InputList<T>`, `InputMap<V>` (inputs); `Output<T>` (outputs)
- `Nullable<T>` for value types
- Nested types extending `ResourceArgs`
- C# `enum` types
- `Asset`, `Archive`

**Required attribute**

Every input property must carry an `[Input("name")]` attribute, and every output property must carry `[Output("name")]` — the analyzer throws when a public property has neither.

**Optional vs required**

For inputs, use the attribute parameter: `[Input("name", required: true)]` is required; `[Input("name")]` defaults to optional. The `?` nullable type marker is conventional for documenting intent but doesn't drive the analyzer's decision for inputs.

For outputs, the analyzer inspects the type wrapped in `Output<T>`: if `T` is a nullable reference type or `Nullable<TValue>`, the output is optional.

**Unsupported types**

- Mixing `Output<T>` in args (input-only) or `Input<T>` in outputs — the analyzer throws an explicit error.
- Dictionary keys other than `string`.
- `CustomResource` references.

**Naming**

Use C# `PascalCase` for properties; pass the `camelCase` schema name as the `[Input]`/`[Output]` attribute's first parameter (the analyzer uses the attribute name verbatim).

**Best practices**

- Always wrap scalars in `Input<T>` so consumers can pass plain values or outputs from other resources.
- Mark required inputs with `required: true` so the schema and runtime validation match.
- Use `[Output("name")]` on output properties so the analyzer can find them.
- Use nested classes extending `ResourceArgs` for nested object inputs.

{{% /choosable %}}

{{% choosable language java %}}

**Args shape**

A `public final class MyComponentArgs extends ResourceArgs`. Fields are `private` with `@Import` annotations; expose getters as needed. The component's constructor must take exactly one parameter assignable to `ResourceArgs`.

```java
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.resources.ResourceArgs;
import java.util.Optional;
import javax.annotation.Nullable;

public final class MyComponentArgs extends ResourceArgs {
    @Import(name = "name", required = true)
    private Output<String> name;

    @Import(name = "count")
    private @Nullable Output<Integer> count;

    public Output<String> name() { return this.name; }
    public Optional<Output<Integer>> count() { return Optional.ofNullable(this.count); }
}
```

**Supported types**

- `String`, `Integer`/`int`, `Long`/`long`, `Double`/`double`, `Float`/`float`, `Boolean`/`boolean`
- `List<T>`
- `Map<String, V>` (string keys only)
- `Output<T>` — Java args fields wrap values in `Output<T>` (not `Input<T>`)
- Nested classes
- Java `enum` types annotated with `@EnumType`
- `Asset`, `Archive`

**Required annotation**

Every input field must carry `@Import(name = "fieldName")` from `com.pulumi.core.annotations`. Add `required = true` to make the field required; omit (or set `required = false`) for optional fields.

**Optional vs required**

The analyzer checks `@Import(required = ...)` first. If `required` is missing, it falls back to inspecting the field type — `Optional<T>` or a `@Nullable`-annotated field is optional; otherwise the field is required.

**Unsupported types**

- Map keys other than `String`.
- Interface types as field types — the analyzer requires concrete classes for nested types.

**Naming**

If `@Import(name = "...")` is provided, that wire name is used. Otherwise the Java field name is used as-is. Author the `name` value in `camelCase` to match the schema convention.

**Best practices**

- Always wrap scalars in `Output<T>` so consumers can pass plain values or outputs from other resources.
- Mark required inputs with `required = true`.
- Use `Optional<Output<T>>` getters for optional fields and unwrap with `Optional.ofNullable(this.field)`.
- Annotate enums with `@EnumType` so they're emitted as schema enums rather than plain strings.

{{% /choosable %}}

{{% choosable language yaml %}}

YAML components don't have a separate "args class" — inputs are declared inline under each component's `inputs:` map in `PulumiPlugin.yaml`.

```yaml
components:
  StaticPage:
    inputs:
      indexContent:
        type: string
      retentionDays:
        type: integer
        default: 30
    resources:
      # ...
    outputs:
      endpoint: ${bucketWebsite.websiteEndpoint}
```

**Supported input `type` values**

- `string`
- `integer`
- `boolean`
- `array` (requires an `items:` block to declare the element type)

**Optional vs required**

Provide a `default:` value to make an input optional; omit `default:` to make it required.

**Unsupported**

- Enums (no enum declaration syntax in YAML components)
- Nested object types with their own properties
- `Input`/`Output` wrapping — YAML has no analogous wrapping; the engine handles dependency tracking declaratively

For the full schema, see the [YAML component reference](/docs/iac/languages-sdks/yaml/yaml-component-reference/).

{{% /choosable %}}

{{< /chooser >}}

### Defining a component resource

Once your arguments are defined, write the component itself. The pattern differs by language: TypeScript, Python, C#, and Java use a class with a constructor; Go uses a struct paired with a factory function (Go has no constructors); YAML uses a declarative definition (no class) under the [`components` key](/docs/iac/languages-sdks/yaml/yaml-component-reference/).

In all cases, the component must register a unique type name with the engine. The type name takes the form `<package-name>:index:<component-class-name>` — the `index` portion is required. Type names are namespaced alongside non-component resources such as `aws:lambda:Function`.

{{< notes type="warning" >}}
Changing the type name after a component has been deployed will cause Pulumi to recreate every existing resource of that type. Settle on a name early.
{{< /notes >}}

Inside the constructor (or factory function), allocate any child resources, passing the component itself as the [`parent`](/docs/iac/concepts/resources/options/parent/) option so they appear under the component in the resource graph and inherit provider configuration.

#### Required signature by language

Each language has specific requirements for the component's entry point so that schema can be generated correctly when the component is packaged as a Pulumi plugin.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

**Requirements:**

- The constructor must have an argument named exactly `args`
- The `args` parameter must have a type declaration (e.g., `args: MyComponentArgs`)

```typescript
class MyComponent extends pulumi.ComponentResource {
    constructor(name: string, args: MyComponentArgs, opts?: pulumi.ComponentResourceOptions) {
        super("pkg:index:MyComponent", name, args, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

**Requirements:**

- The `__init__` method must have an argument named exactly `args`
- The `args` parameter must have a type annotation (e.g., `args: MyComponentArgs`)

```python
class MyComponent(pulumi.ComponentResource):
    def __init__(self, name: str, args: MyComponentArgs, opts: Optional[pulumi.ResourceOptions] = None):
        super().__init__('pkg:index:MyComponent', name, args, opts)
```

{{% /choosable %}}
{{% choosable language go %}}

Go has no constructors. Define a factory function (by convention, `NewMyComponent`) that returns a pointer to your component struct.

**Requirements:**

- The factory function should accept a context, a name, an args struct, and variadic resource options
- The args should be a struct type

```go
type MyComponent struct {
    pulumi.ResourceState
}

func NewMyComponent(
    ctx *pulumi.Context,
    name string,
    args *MyComponentArgs,
    opts ...pulumi.ResourceOption,
) (*MyComponent, error) {
    myComponent := &MyComponent{}
    err := ctx.RegisterComponentResource(
        "pkg:index:MyComponent", name, myComponent, opts...)
    if err != nil {
        return nil, err
    }
    return myComponent, nil
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

**Requirements:**

- The constructor must have exactly 3 arguments:
  1. A `string` for the name (or any unspecified first argument)
  1. An argument that is assignable from `ResourceArgs` (must extend `ResourceArgs`)
  1. An argument that is assignable from `ComponentResourceOptions`

```csharp
public class MyComponent : ComponentResource
{
    public MyComponent(string name, MyComponentArgs args, ComponentResourceOptions? opts = null)
        : base("pkg:index:MyComponent", name, opts)
    {
    }
}

public sealed class MyComponentArgs : ResourceArgs
{
    [Input("value")]
    public Input<string>? Value { get; set; }
}
```

{{% /choosable %}}
{{% choosable language java %}}

**Requirements:**

- The constructor must have exactly one argument that extends `ResourceArgs`
- Other arguments (name, options) are not restricted but typically follow the standard pattern

```java
public class MyComponent extends ComponentResource {
    public MyComponent(String name, MyComponentArgs args, ComponentResourceOptions opts) {
        super("pkg:index:MyComponent", name, null, opts);
    }
}

class MyComponentArgs extends ResourceArgs {
    @Import(name = "value")
    private Output<String> value;

    public Output<String> getValue() {
        return this.value;
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

The base call (`super` / `base` / `ctx.RegisterComponentResource`) registers the component instance with the Pulumi engine, recording its state and tracking it across deployments — even though component resources have no provider logic of their own, they still appear as resources you can diff and inspect.

### Creating child resources

Component resources contain child resources. Child resource names must include the component resource's name as part of their names (e.g., as a prefix). This ensures uniqueness across multiple instances of the component and ensures that if the component is renamed, the child resources are renamed as well. Also, when constructing a resource, children must be registered as such. To do this, pass the component resource itself as the `parent` option.

This example demonstrates both the naming convention and how to designate the component resource as the parent:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
class MyComponent extends pulumi.ComponentResource {
    bucket: aws.s3.Bucket;

    constructor(name: string, myComponentArgs: MyComponentArgs, opts: pulumi.ComponentResourceOptions) {
        super("pkg:index:MyComponent", name, {}, opts);

        // Create Child Resource
        this.bucket = new aws.s3.Bucket(`${name}-bucket`,
            {}, { parent: this });
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
class MyComponent(pulumi.ComponentResource):
    def __init__(self, name, my_component_args, opts = None):
        super().__init__('pkg:index:MyComponent', name, None, opts)

        # Create Child Resource
        self.bucket = s3.Bucket(f"{name}-bucket",
            opts=pulumi.ResourceOptions(parent=self))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
type MyComponent struct {
    pulumi.ResourceState
    Bucket *s3.Bucket
}

func NewMyComponent(
    ctx *pulumi.Context,
    name string,
    myComponentArgs MyComponentArgs,
    opts ...pulumi.ResourceOption,
) (*MyComponent, error) {
    myComponent := &MyComponent{}
    err := ctx.RegisterComponentResource(
        "pkg:index:MyComponent", name, myComponent, opts...)
    if err != nil {
        return nil, err
    }

    // Create Child Resource
    bucket, err := s3.NewBucket(ctx, fmt.Sprintf("%s-bucket", name),
        &s3.BucketArgs{}, pulumi.Parent(myComponent))
    if err != nil {
        return nil, err
    }
    myComponent.Bucket = bucket

    return myComponent, nil
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.S3;

class MyComponent : ComponentResource
{
    public Bucket Bucket { get; private set; }

    public MyComponent(string name, MyComponentArgs myComponentArgs, ComponentResourceOptions opts)
        : base("pkg:index:MyComponent", name, opts)
    {
        // Create Child Resource
        this.Bucket = new Bucket($"{name}-bucket",
            new BucketArgs(), new CustomResourceOptions { Parent = this });
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.resources.ComponentResource;
import com.pulumi.resources.ComponentResourceOptions;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketArgs;
import com.pulumi.resources.CustomResourceOptions;

class MyComponent extends ComponentResource {
    private final Bucket bucket;

    public MyComponent(String name, MyComponentArgs myComponentArgs, ComponentResourceOptions opts) {
        super("pkg:index:MyComponent", name, null, opts);

        // Create Child Resource
        this.bucket = new Bucket(String.format("%s-bucket", name),
            BucketArgs.builder().build(),
            CustomResourceOptions.builder()
                .parent(this)
                .build());
    }

    public Bucket bucket() {
        return this.bucket;
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

{{% notes type="warning" %}}
Always set `parent` when creating resources inside a component. Omitting it causes the following problems:

- **Resource graph**: Child resources won't appear under the component in `pulumi preview` and the Pulumi Console, making the resource hierarchy unclear.
- **Provider inheritance**: Child resources won't automatically inherit provider configuration (such as region or credentials) passed to the component via the `providers` option.
- **Dependency tracking**: Other resources that depend on the component won't automatically wait for un-parented resources to finish creating, which can cause race conditions or incomplete deployments.
{{% /notes %}}

### Registering component outputs

Component resources can define their own output properties. Outputs in a component must be registered with the Pulumi IaC engine by calling `registerOutputs`. The Pulumi engine uses this information to display the logical outputs of the component resource and any changes to those outputs will be shown during an update.

For example, this code registers an S3 bucket's computed domain name, which won't be known until the bucket is created:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
class MyComponent extends pulumi.ComponentResource {
    bucket: aws.s3.Bucket;

    constructor(name: string, myComponentArgs: MyComponentArgs, opts: pulumi.ComponentResourceOptions) {
        super("pkg:index:MyComponent", name, {}, opts);

        this.bucket = new aws.s3.Bucket(`${name}-bucket`,
            {}, { parent: this });

        // Registering Component Outputs
        this.registerOutputs({
            bucketDnsName: this.bucket.bucketDomainName
        });
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
class MyComponent(pulumi.ComponentResource):
    bucket_dns_name: pulumi.Output[str]
    """The DNS name of the bucket"""

    def __init__(self, name, my_component_args, opts = None):
        super().__init__('pkg:index:MyComponent', name, None, opts)

        self.bucket = s3.Bucket(f"{name}-bucket",
            opts=pulumi.ResourceOptions(parent=self))

        # Registering Component Outputs
        self.register_outputs({
            "bucket_dns_name": self.bucket.bucket_domain_name
        })
```

{{% /choosable %}}
{{% choosable language go %}}

```go
type MyComponent struct {
    pulumi.ResourceState
    Bucket *s3.Bucket
}

func NewMyComponent(
    ctx *pulumi.Context,
    name string,
    myComponentArgs MyComponentArgs,
    opts ...pulumi.ResourceOption,
) (*MyComponent, error) {
    myComponent := &MyComponent{}
    err := ctx.RegisterComponentResource(
        "pkg:index:MyComponent", name, myComponent, opts...)
    if err != nil {
        return nil, err
    }

    bucket, err := s3.NewBucket(ctx, fmt.Sprintf("%s-bucket", name),
        &s3.BucketArgs{}, pulumi.Parent(myComponent))
    if err != nil {
        return nil, err
    }
    myComponent.Bucket = bucket

    // Registering Component Outputs
    ctx.RegisterResourceOutputs(myComponent, pulumi.Map{
        "bucketDnsName": bucket.BucketDomainName,
    })

    return myComponent, nil
}

```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.S3;

class MyComponent : ComponentResource
{
    public Bucket Bucket { get; private set; }

    public MyComponent(string name, MyComponentArgs myComponentArgs, ComponentResourceOptions opts)
        : base("pkg:index:MyComponent", name, opts)
    {

        this.Bucket = new Bucket($"{name}-bucket",
            new BucketArgs(), new CustomResourceOptions { Parent = this });

        // Registering Component Outputs
        this.RegisterOutputs(new Dictionary<string, object?>
        {
            { "bucketDnsName", Bucket.BucketDomainName }
        });
    }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.resources.ComponentResource;
import com.pulumi.resources.ComponentResourceOptions;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketArgs;
import com.pulumi.resources.CustomResourceOptions;

class MyComponent extends ComponentResource {
    private final Bucket bucket;

    public MyComponent(String name, MyComponentArgs myComponentArgs, ComponentResourceOptions opts) {
        super("pkg:index:MyComponent", name, null, opts);

        this.bucket = new Bucket(String.format("%s-bucket", name),
            BucketArgs.builder().build(),
            CustomResourceOptions.builder()
                .parent(this)
                .build());

        // Registering Component Outputs
        this.registerOutputs(Map.of(
            "bucketDnsName", bucket.bucketDomainName()
        ));
    }

    public Bucket bucket() {
        return this.bucket;
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

The call to `registerOutputs` typically happens at the very end of the component's constructor (or factory function, in Go).

#### What registerOutputs does

The `registerOutputs` call serves two purposes:

1. **Marks the component as fully constructed**: It signals to the Pulumi engine that the component resource has finished registering all its child resources and should be considered complete.
1. **Saves outputs to state**: It saves the component's output properties to the state file so they appear in the Pulumi Console and CLI.

{{% notes type="warning" %}}
Always call `registerOutputs`, even when you have no outputs to register (pass an empty object). Without this call:

- Resource [hooks](/docs/iac/concepts/resources/options/hooks/) such as `afterCreate` will not fire on the component. Hooks are often used for security, compliance, or notification logic, so silently skipping them can be harmful.
- The component will appear as "creating..." in the CLI and Pulumi Console until the entire deployment completes, rather than when the component itself finishes.
- The component's output properties will not be saved to the state file. (Child resource state is unaffected.)
{{% /notes %}}

{{% notes type="info" %}}
**.NET**: Since `pulumi-dotnet` 3.59.0, calling `RegisterOutputs()` without arguments automatically registers all properties decorated with `[Output]`.
{{% /notes %}}

### Passing resource options to components

Like any resource, a component accepts a third argument of resource options when it's instantiated. Some options are component-only (notably [`providers`](/docs/iac/concepts/resources/options/providers/), which lets a consumer target the component at a specific provider configuration).

{{< notes type="warning" >}}
Not all [resource options](/docs/iac/concepts/resources/options/) apply to component resources. For example, `ignoreChanges` and `customTimeouts` have no effect on components themselves. To see which options work with components and how to apply options to child resources using `transforms`, see [Resource options and component resources](/docs/iac/concepts/resources/options/#resource-options-and-component-resources).
{{< /notes >}}

The `providers` option is the most common reason to pass options to a component instance — it flows the consumer's chosen provider configuration through to every child resource the component creates. See the [`providers` resource option](/docs/iac/concepts/resources/options/providers/) for details and a worked example targeting one component at multiple provider configurations from a single program.

## Next steps

Now that you've written a component, the next step is to package it so it can be installed and used from any Pulumi program in any supported language.

- [Authoring a Source-Based Plugin Package](/docs/iac/guides/building-extending/packages/source-based-plugin/) — wrap the component class you just wrote in the project layout (`PulumiPlugin.yaml`, language manifest, entry file) that makes it installable via `pulumi package add`. This is the recommended next step for most component authors.
- [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) — compares the source-based, native-language, and executable-based plugin approaches if you're not sure which fits your use case.
- [Testing Components](/docs/iac/guides/building-extending/components/testing-components/) — strategies for testing component behavior.
