---
title: "Announcing Infrastructure as Code with Java and Pulumi"
date: 2022-05-04T06:59:00-07:00
draft: false
meta_desc: Learn about Pulumi's new support for Java and JVM languages, which enable you to use infrastructure as code on any cloud with the JVM ecosystem.
meta_image: meta.png
authors: 
    - mikhail-shilkov
tags:
    - java
    - cloud-engineering
    - infrastructure-as-code
---

Today we are excited to announce the preview of Java support for all of your modern infrastructure as code needs. This announcement means that you can build, deploy, and manage your infrastructure, on any cloud&mdash;including all of AWS, Azure, Google Cloud, Kubernetes, Oracle Cloud, and more&mdash;using Java and other JVM languages. This brings the entire cloud to your fingertips without ever having to leave your code editor, while using production-ready infrastructure as code techniques.

<!--more-->

Infrastructure has become a core part of application development as modern cloud capabilities such as microservices, containers, serverless, and data stores define your application's architecture. The term "infrastructure" covers all of the cloud resources your application needs to run. Modern architectures require thinking deeply about infrastructure while building your application, instead of treating it as an afterthought. Pulumi's approach helps developers, infrastructure engineers, and platform teams work together to leverage everything the modern cloud has to offer.

Pulumi has worked with hundreds of companies to get cloud applications into production, and Java has quickly risen to become one of the most frequently requested features by the community. Today we are thrilled to make Pulumi for Java available for your cloud engineering needs.

Pulumi is an open source product, and we are grateful to our awesome community members who bootstrapped Pulumi for Java last year and were instrumental in helping us with this public preview. Thank you to [Paweł Prażak](https://twitter.com/pawelprazak) and his [VirtusLab](https://virtuslab.com) colleagues!

## What is Pulumi?

Pulumi lets you build, deploy, and manage infrastructure on any cloud using general-purpose programming languages (TypeScript, Python, Go, .NET, Java) and markup languages (YAML, CUE) to express your application's infrastructure needs, using a powerful technique called "infrastructure as code." You declare desired infrastructure, and an engine provisions it for you, so that it's automated, easy to replicate, and robust enough for demanding production requirements. Pulumi takes this approach a step further by leveraging programming languages and software engineering tools to make modern cloud infrastructure patterns, such as containers and serverless programs, easy and first-class citizens.

With Pulumi for Java you can:

- **Declare infrastructure** using programs, classes, and libraries written in Java or other JVM languages (Kotlin, Scala, Clojure, Groovy, etc.).

- **Automatically create, update, or delete cloud resources** using Pulumi's infrastructure as code engine, removing manual point-and-clicking in web consoles and ad-hoc scripts.

- **Use your favorite IDEs and tools**, including IntelliJ IDEA and Visual Studio Code, taking advantage of features like auto-completion, refactoring, and interactive documentation.

- **Catch mistakes early on** with standard compiler errors, analyzers, and an infrastructure-specific policy engine for enforcing security, compliance, and best practices.

- **Reuse any existing Java package**, or distribute your own, whether that's for infrastructure best practices, productivity, or just general programming patterns.

- **Deploy continuously, predictably, and reliably** using GitHub Actions, or one of over a dozen CI integrations.

- **Build scalable cloud applications** using cloud native technologies like Kubernetes, Docker containers, serverless functions, and PaaS services into your core development experience, bringing them closer to your application code.

Pulumi's free open source SDK, which includes a CLI and an assortment of libraries, enables these capabilities.

## Example: Provision a GKE cluster with a Kubernetes namespace

The following Java snippet demonstrates the power of Pulumi for Java ([full source code](https://github.com/pulumi/pulumi-java/blob/main/tests/examples/gcp-java-gke-hello-world/)). The program defines a Google Kubernetes Engine cluster, calculates its `kubeconfig` and exports it for user's needs, and deploys a Kubernetes namespace into the newly provisioned cluster.

```java
package gke_sample;

import java.util.*;
import java.io.*;
import java.nio.*;
import com.pulumi.*;
import com.pulumi.gcp.container.*;
import com.pulumi.kubernetes.core_v1.*;

public class Program {
   private static void stack(Context ctx) {
       // Create a GKE cluster
       var cluster = new Cluster("mygke",
           ClusterArgs.builder()
               .initialNodeCount(1)
               .minMasterVersion("1.20.7")
               .build()
       );

       // Build and export a Kubeconfig for the newly created cluster.
       var kubeconfig = Utils.buildKubeconfig(cluster);
       ctx.export("kubeconfig", kubeconfig);

       // Create a Kubernetes provider instance that uses our cluster from above.
       var clusterProvider = new Provider("gke-provider",
           ProviderArgs.builder().kubeconfig(kubeconfig).build());

       // Create a Kubernetes Namespace
       var ns = new Namespace("test",
           NamespaceArgs.Empty,
           CustomResourceOptions.builder().provider(clusterProvider).build()
       );
   }

   public static void main(String[] args) {
       Pulumi.run(App::stack);
   }
}
```

Resources are defined declaratively using class constructors and argument builders. Dependencies between resources are managed automatically by the Pulumi engine based on the way you use variables in the program. You are free to use any libraries, helper functions&mdash;for instance, to build the kubeconfig string above, classes, if statements, for loops, and all the other tools available to Java developers.

## Why is Java great for infrastructure too?

Many of us love using Java to author our applications, so why not use it for infrastructure as code too? By using Java, you get many helpful features for your infrastructure code:

- **Familiarity**: No need to learn DSLs or markup templating languages.

- **Expressiveness**: Use loops, conditionals, pattern matching, async code, and more, to dynamically create infrastructure that meets the target environment's needs.

- **Abstraction**: Encapsulate common patterns into classes and functions to hide complexity and avoid copy-and-pasting the same boilerplate repeatedly.

- **Sharing and reuse**: Tap into a community of cloud applications and infrastructure experts by sharing and reusing Maven or Gradle packages with your team or the global community.

- **Productivity**: Use your favorite IDE and get statement completion, go to definition, live error checking, refactoring, static analysis, and interactive documentation.

- **Project organization**: Use common code structuring techniques to manage your infrastructure across one or more projects.

- **Application lifecycle**: Use existing ALM systems and techniques to manage and deploy your infrastructure projects, including source control, code review, testing, and continuous integration (CI) and delivery (CD).

Pulumi unlocks access to the entire JVM ecosystem&mdash;something that's easy to take for granted but is missing from other solutions based on DSLs or CLI scripts. This approach also helps developers and operators work better together using a shared foundation. Add all of the above together, and you get things done faster and more reliably.

## Join the community and get started

Today we've released the first preview of Pulumi for Java, including support for the entire breadth of services in AWS, Azure, Google Cloud, and more. To give Pulumi a try, visit the [Pulumi for Java docs](https://www.pulumi.com/docs/intro/languages/java/).

There you will find several instructions on installing and getting started with Pulumi for Java. The following resources provide additional useful information:

- [Full example code](https://github.com/pulumi/pulumi-java/blob/main/tests/examples/gcp-java-gke-hello-world/)

- [Getting started with Pulumi](https://www.pulumi.com/docs/get-started/)

- [General Pulumi overview (concepts and architecture)](https://www.pulumi.com/docs/intro/concepts/)

- [Overview of premium Pulumi features for teams and Enterprises](https://www.pulumi.com/pricing/)

Although Pulumi for Java is listed in "preview" status, it supports all of the most essential Pulumi programming model features (and the rest is on its way). Our goal is to gather feedback over the next few weeks, and we will be working hard to improve the Java experience across the board, including more examples and better documentation.

Please [join the community in Slack](https://slack.pulumi.com/) to discuss your scenarios, ideas, and to get any needed assistance from the team and other end users. Pulumi is [open source on GitHub](https://github.com/pulumi/pulumi) and you can find the Java plugin at [pulumi/pulumi-java](https://github.com/pulumi/pulumi-java).

There is an [Introduction to Infrastructure as Code in Java](https://www.pulumi.com/resources/introduction-to-infrastructure-as-code/) coming up on May 5th.

We look forward to seeing the new and amazing cloud applications you build with Pulumi for Java!
