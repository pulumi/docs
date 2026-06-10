---
title_tag: "Java | Languages & SDKs"
meta_desc: An overview of how to use the Java language with Pulumi for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: Java
h1: Pulumi & Java
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Java
        parent: iac-languages
        weight: 5
        identifier: iac-languages-java
    languages:
        identifier: java
        weight: 5
aliases:
    - /docs/intro/languages/java/
    - /java/
    - /docs/languages-sdks/java/
---

<img src="/logos/tech/java.svg" alt="java" align="right" width="90" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code in Java running on the Java Virtual Machine (JVM). Using a general-purpose language for infrastructure as code provides several key advantages:

- **Familiar syntax**: Write infrastructure code using the same language and patterns you already know
- **Rich ecosystem**: Leverage the vast Maven Central package ecosystem in your infrastructure code
- **Native tooling**: Use your existing IDE, build tools, and test frameworks without requiring plugins or extensions
- **Type safety**: Catch errors at compile time with Java's static typing and IDE autocompletion

## Installation requirements

### Java runtime

Pulumi supports any [supported version](https://www.oracle.com/java/technologies/java-se-support-roadmap.html) of Java 11 or later. To use the Java runtime, set `runtime: java` in your `Pulumi.yaml`:

```yaml
runtime: java
```

Pulumi needs the `java` and `javac` executables on your `PATH` to build and run your Pulumi Java program. Depending on your build tool, the `mvn` executable may also be required.

### Build tools

Pulumi supports running Java programs with the following build tools:

- **Apache Maven**: Fully supported (requires Maven 3.6.1 or later). This is the default for the `java` template.
- **Gradle**: Fully supported. Use the `java-gradle` template to start a Gradle-based project.
- **JAR files**: You can run a Pulumi program packaged as a pre-built JAR by setting the `binary` runtime option to the path of the JAR. See [`runtime` options](/docs/iac/concepts/projects/project-file/#runtime-options) for details.

### Languages

Pulumi officially supports and documents **Java**. Because the Pulumi Java SDK is a standard JVM library distributed through Maven Central, it can also be consumed from other JVM languages such as Kotlin, Scala, or Groovy. However, only Java is officially supported, and all Pulumi templates and documentation examples use Java.

The Pulumi SDK is available to Java developers as a package on Maven Central. To learn more, refer to the [Pulumi SDK reference guide](/docs/reference/pkg/java/).

## Getting started

The fastest way to get started with Pulumi and Java is to use the Java template:

```bash
$ pulumi new java
```

This creates a Maven project with a `pom.xml`, a `Pulumi.yaml` [project file](/docs/iac/concepts/projects/), and an `App.java` file containing your program. To start a Gradle-based project instead, use the `java-gradle` template:

```bash
$ pulumi new java-gradle
```

You can discover additional templates by running `pulumi new` with no arguments, or you can initialize a Pulumi program by supplying a specific URL to the `pulumi new` command. For example:

```bash
$ pulumi new https://github.com/pulumi/templates/tree/master/aws-java
```

Cloud-specific starter templates are also available, including `aws-java`, `azure-java`, and `gcp-java`. See the [`pulumi new` documentation](/docs/iac/cli/commands/pulumi_new/) for full details.

### Program entrypoint

In your `main` method, call `Pulumi.run` and pass it a function that constructs the resources you'd like to deploy:

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.Context;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        // construct your resources here
    }
}
```

You can also pass a lambda expression:

```java
public static void main(String[] args) {
    Pulumi.run(ctx -> {
        // construct your resources here
    });
}
```

Pulumi locates the entrypoint through your build tool's configuration. With Maven, set the `mainClass` property in `pom.xml`:

```xml
<properties>
    <mainClass>myproject.App</mainClass>
</properties>
```

With Gradle, set the `mainClass` in the `application` block:

```groovy
application {
    mainClass = 'myproject.App'
}
```

## Defining resources

Writing a Pulumi program in Java involves declaring infrastructure resources using resource constructors. Here are the key concepts:

- **Declare resources**: Create infrastructure resources by instantiating resource classes from provider packages. Resource arguments are supplied using `Args` builders — for example, `new Bucket("my-bucket", BucketArgs.builder().build())`.
- **Inputs and outputs**: The Pulumi programming model uses `Output` values to track how the outputs of one resource flow in as inputs to another and to resolve dependencies between resources. Understanding inputs and outputs is essential for building infrastructure. See the [Inputs and Outputs](/docs/iac/concepts/inputs-outputs/) documentation for details.
- **Immutable infrastructure**: Once declared, resource properties are immutable within your program. Changes to resource definitions result in updates during the next deployment.
- **Stack outputs**: Export values from your program with `ctx.export(...)` to make them accessible from the CLI or to other Pulumi programs.

Unlike other Pulumi languages, Pulumi Java does not have a dedicated `Input<T> = T | Output<T>` type. Instead, the `Args` builders provide overloads that accept both a plain `T` value and an `Output<T>` value.

To query existing cloud resources, providers expose [provider functions](/docs/iac/concepts/functions/provider-functions/) named with the convention `com.pulumi.<provider>.<service>.<Service>Functions`. Each function comes in two forms: the **output form** (e.g., `getAmi()`) accepts `Input` values and returns an `Output<T>`, while the **direct form** (e.g., `getAmiPlain()`) accepts plain arguments and returns a `java.util.concurrent.CompletableFuture<T>`.

The Pulumi SDK provides constructs for working with key Pulumi concepts. For more information, see:

- [Pulumi Concepts](/docs/iac/concepts/)
- [How Pulumi Works](/docs/iac/guides/basics/how-pulumi-works/)

## Program execution

Pulumi programs are most commonly executed using the Pulumi CLI commands such as `pulumi up`, `pulumi preview`, and `pulumi destroy`. The CLI builds your program with your configured build tool, handles authentication and state management, and orchestrates resource operations.

Alternatively, you can use the [Automation API](/docs/iac/concepts/automation-api/) to programmatically control the Pulumi engine from within your Java code. The Automation API allows you to:

- Embed Pulumi operations in regular Java applications
- Build custom deployment tools and workflows
- Create self-service infrastructure platforms

With Automation API, your Java code controls Pulumi, rather than Pulumi controlling your code.

## Documentation and resources

### Pulumi SDK

The [Pulumi SDK (`com.pulumi`)](/docs/reference/pkg/java/) contains the core constructs for working with Pulumi, including resources, configuration, stack outputs, and more. You will need to reference it in most Pulumi programs. The Pulumi Java SDK is also available in source form on [GitHub](https://github.com/pulumi/pulumi-java).

### Provider SDKs

For managing resources in a Pulumi program, you can find the relevant SDK reference documentation for each provider in [the Pulumi Registry](/registry/). Pulumi auto-detects the [plugins](/docs/iac/cli/commands/pulumi_plugin/?language=java) your program uses by analyzing your project dependencies and installs them automatically. For example, a program that references `com.pulumi.aws` triggers the equivalent of `pulumi plugin install resource aws`.

### Policy SDK

Pulumi Policy as Code policies cannot be authored in Java. Policies are written in [TypeScript/JavaScript, Python, or OPA (Rego)](/docs/insights/policy/#languages) and can be applied to Pulumi programs written in any language, including Java.

### Dev versions

Pulumi does not publish pre-release (dev) builds of the Java SDK. Use the released versions available on Maven Central.

### Testing

- [Unit testing](/docs/iac/guides/testing/unit/): Test your infrastructure code in isolation
- [Integration testing](/docs/iac/guides/testing/integration/): Test your infrastructure deployments end-to-end
