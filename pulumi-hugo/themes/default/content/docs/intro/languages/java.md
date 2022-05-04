---
title: "Java"
meta_desc: An overview of how to use the Java language for infrastructure as code
           on any cloud (AWS, Azure, GCP, Kubernetes, etc.).
menu:
  intro:
    parent: languages
    weight: 4
---

<img src="/logos/tech/java.svg" align="right" width="90" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code using the Java language. Java 11 or later is required. We support running Maven Pulumi programs, Gradle Pulumi programs, and Pulumi programs packaged as JAR files.

{{% notes "info" %}}
Java is currently in preview. Feedback is greatly appreciated!

Please post any Bug Reports or Feature Requests in [GitHub Issues](https://github.com/pulumi/pulumi-java/issues/new/choose).
{{% /notes %}}

## Prerequisites

{{< install-java >}}

## Getting Started

The fastest way to get up and running is to choose from one of the following Getting Started guides:

<div class="tiles mt-4">
    <div class="flex-1 pb-4 md:mr-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/aws" >}}?language=java">
            <img class="h-8 mx-auto" src="/logos/tech/aws.svg" alt="AWS">
        </a>
    </div>
    <div class="flex-1 pb-4 md:mr-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/azure" >}}?language=java">
            <img class="h-8 mx-auto" src="/logos/tech/azure.svg" alt="Azure">
        </a>
    </div>
    <div class="flex-1 pb-4 md:mr-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/gcp" >}}?language=java">
            <img class="h-8 mx-auto" src="/logos/tech/gcp.svg" alt="Google Cloud">
        </a>
    </div>
    <div class="flex-1 pb-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/kubernetes" >}}?language=java">
            <img class="h-8 mx-auto" src="/logos/tech/k8s.svg" alt="Kubernetes">
        </a>
    </div>
</div>

## Templates

The getting started guides shown above will help you write a Pulumi Java program via tutorial, but this section describes starting a basic project that you can start to explore with.

From an empty directory, create a new project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new java
```

{{% notes "info" %}}
To write a Pulumi Java program using Gradle

```
$ mkdir myproject && cd myproject
$ pulumi new java-gradle
```

For details around using JAR, please check our docs on [Pulumi.yaml]({{< relref "/docs/reference/pulumi-yaml" >}})

{{% /notes %}}

This will create a maven project with a `pom.xml` and a `Pulumi.yaml` [project file]({{< relref "../concepts/project" >}}) containing some minimal metadata about your project (including a name and description which you may wish to change) and an `App.java` file in the `src/main/java/myproject` directory containing your program.

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

Pulumi will try to auto-detect which [plugins]({{< relref "/docs/reference/cli/pulumi_plugin" >}}?language=java) your program is using by analyzing your Java project dependencies and then auto-install them. For example, if a program references `com.pulumi.aws` it will automatically issue the equivalent of `$ pulumi plugin install resource aws`.

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
Pulumi. [Architecture & Concepts]({{< relref "/docs/intro/concepts" >}}?language=java) describes these concepts
with examples available in Java. These concepts are made available to you in the Pulumi SDK.

The Pulumi programming model includes a core concept of `Output` values, which are used to track how outputs of one resource flow in as inputs to another resource to resolve dependencies. This concept is important to understand when getting started with Pulumi, and the [Inputs and Outputs]({{< relref "/docs/intro/concepts/inputs-outputs" >}}?language=java) documentation is recommended to get a feel for how to work with this core part of Pulumi in common cases.

Unlike other Pulumi languages, Pulumi Java does not have a dedicated `Input<T> = T | Output<T>` type. Instead, when constructing resource arguments, builders have overloads that accept both a `T` and an `Output<T>` value.
