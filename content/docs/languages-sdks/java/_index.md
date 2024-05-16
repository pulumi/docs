---
title_tag: "Java | Languages & SDKs"
meta_desc: An overview of how to use the Java language with Pulumi for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: Java
h1: Pulumi & Java
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    languages:
        identifier: java
        weight: 5
aliases:
- /docs/intro/languages/java/
- /java/
---

<img src="/logos/tech/java.svg" align="right" width="90" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code using the Java language running on any [supported version](https://www.oracle.com/java/technologies/java-se-support-roadmap.html) of Java 11 or later.

We support running Maven Pulumi programs, Gradle Pulumi programs, and Pulumi programs packaged as JAR files.

{{% notes "info" %}}
Java is currently in preview. Feedback is greatly appreciated!

Please post any Bug Reports or Feature Requests in [GitHub Issues](https://github.com/pulumi/pulumi-java/issues/new/choose).
{{% /notes %}}

## Prerequisites

{{< install-java >}}

## Templates

This section describes starting a basic project that you can start to explore with.

From an empty directory, create a new project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new java
```

{{% notes "info" %}}
To write a Pulumi Java program using Gradle

```bash
$ mkdir myproject && cd myproject
$ pulumi new java-gradle
```

For details around using JAR, please check our docs on [Pulumi.yaml](/docs/reference/pulumi-yaml/)

{{% /notes %}}

This will create a maven project with a `pom.xml` and a `Pulumi.yaml` [project file](/docs/concepts/projects/) containing some minimal metadata about your project (including a name and description which you may wish to change) and an `App.java` file in the `src/main/java/myproject` directory containing your program.

To deploy your infrastructure, run `pulumi up` and Pulumi will build your app using maven (gradle is also supported) and perform the operations needed to deploy the infrastructure you have declared.

To destroy your infrastructure, run `pulumi destroy` and Pulumi will terminate the resources that you've declared.

This `java` template is cloud agnostic, and you will need to install additional Java modules for the cloud provider of your choice. Additional templates are available that do this for you:

* `pulumi new aws-java`: creates a starter AWS Java project
* `pulumi new azure-java`: creates a starter Azure Java project
* `pulumi new gcp-java`: creates a starter Google Cloud Java project

## Entrypoint

In your `main` method, you will want to call `Pulumi.run` and pass it a method to run that will construct the resources that you'd like to deploy.

```java
package main;

import com.pulumi.Pulumi;

public class Main {
    public static void main(String[] args) {
        Pulumi.run(Main::stack);
    }
    public static void stack(Context ctx) {
        // construct your resources here
    }
}
```

You can also use lambda expressions like such:

```java
public static void main(String[] args) {
    Pulumi.run(ctx -> {
        // construct your resources here
    });
}
```

## Datasource Methods

In order to get information from cloud providers, there are classes that allow you to query cloud services for data. They are named using the convention `com.pulumi.providername.servicename.[Servicename]Functions` and return a `java.util.concurrent.CompletableFuture<T>`.

## Pulumi Java implementation details

{{% notes "info" %}}
Java is currently in preview. These implementation details around how Pulumi integrates with the Java ecosystem are subject to change based on community feedback which is greatly appreciated!

Please post any Bug Reports or Feature Requests in [GitHub Issues](https://github.com/pulumi/pulumi-java/issues/new/choose).
{{% /notes %}}
The Java Pulumi SDK is available to Go/Java developers in source form on [GitHub](https://github.com/pulumi/pulumi-java).

### Plugin Acquisition

Pulumi will try to auto-detect which [plugins](/docs/cli/commands/pulumi_plugin/?language=java) your program is using by analyzing your Java project dependencies and then auto-install them. For example, if a program references `com.pulumi.aws` it will automatically issue the equivalent of `$ pulumi plugin install resource aws`.

### Running Pulumi with Maven and Gradle

To support running a Pulumi program with Maven, we use the `exec:java` target. This requires adding the `mainClass` property to `pom.xml`

```xml
<properties>
    <mainClass>myproject.App</mainClass>
</properties>
```

To support running a Pulumi program with Gradle, we use the `run` target. To support plugin resolution and running a
Pulumi program in Gradle we check if the `mainClass` property is set. If it's set, we're in plugin resolution. Otherwise, we interpret it as we're running a Pulumi program.

```groovy
application {
    mainClass = project.hasProperty("mainClass")
            ? project.getProperty("mainClass")
            : 'myproject.App'
}
```

## Pulumi Programming Model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as code programs using
Pulumi. [Concepts](/docs/concepts/?language=java) describes these concepts
with examples available in Java. These concepts are made available to you in the Pulumi SDK.

The Pulumi programming model includes a core concept of `Output` values, which are used to track how outputs of one resource flow in as inputs to another resource to resolve dependencies. This concept is important to understand when getting started with Pulumi, and the [Inputs and Outputs](/docs/concepts/inputs-outputs/?language=java) documentation is recommended to get a feel for how to work with this core part of Pulumi in common cases.

Unlike other Pulumi languages, Pulumi Java does not have a dedicated `Input<T> = T | Output<T>` type. Instead, when constructing resource arguments, builders have overloads that accept both a `T` and an `Output<T>` value.

## Java Packages

The [Pulumi Registry](/registry/) houses 100+ Java packages.
