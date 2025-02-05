---
title: "Pulumi's Java SDK is Now Generally Available"
date: 2025-02-06
draft: false

meta_desc: "Pulumi’s Java SDK is now generally available. It enables organizations of all sizes to build infrastructure using a proven, safe, and familiar language."
meta_image: meta.png

authors:
    - justin-vanpatten
    - mark-huber
tags:
    - java
    - features
    - releases

social:
    twitter: "☕ The Pulumi Java SDK is now Generally Available! Manage your infrastructure using the composable, strongly typed programming language you already know and love - now including the powerful Pulumi Automation API!"
    linkedin: "Java, the world’s most trusted enterprise programming language, is now generally available in Pulumi. You can now leverage Java’s familiar, expressive, and safe syntax to manage your infrastructure in a composable and scalable way.
    
    Learn more about automating everything you run in the cloud with Java: [Link]"
---

One of Pulumi’s core features is the ability to [model infrastructure](https://www.pulumi.com/docs/iac/concepts/) using well-traveled, familiar general-purpose programming languages. Users have built Pulumi programs with first-class support for TypeScript, Python, Go, YAML, and C# for the past seven years. Today, we’re welcoming another language into the mix, as Java is now officially generally available.

<!--more-->

We introduced Java in preview in 2022. Since then, we’ve grown our Java support based on feedback from the expanding set of companies that have adopted Pulumi Java in production workloads. Let’s look at some examples of using Java to power your Pulumi programs.

## Familiar Composability

Using Java with Pulumi lets you model your infrastructure using familiar patterns. Paired with our rich abstractions, you can efficiently build Pulumi programs. For instance, let’s take a look at an example from our docs that shows how, in a few lines of code, you can:

1. Instantiate and override the defaults for the default Pulumi AWS Provider

    ```java
    var useast1 = new Provider("useast1",
            ProviderArgs.builder().region("us-east-1").build());
    ```

2. Define an ACM certificate, passing along the defaults defined in Step 1

    ```java
    var cert = new Certificate("cert",
    CertificateArgs.builder()
        .domainName("pulumi.com")
        .validationMethod("EMAIL")
        .build(),
    CustomResourceOptions.builder()
        .provider(useast1)
        .build());
    ```

3. Instantiate an ELB listener, injecting the cert from above

    ```java
    var listener = new Listener("listener",
        ListenerArgs.builder()
            .loadBalancerArn(loadBalancerArn)
            .port(443)
            .protocol("HTTPS")
            .sslPolicy("ELBSecurityPolicy-2016-08")
            .certificateArn(cert.arn())
            .defaultActions(ListenerDefaultActionArgs.builder()
                    .targetGroupArn(targetGroupArn)
                    .type("forward")
                    .build())
            .build());
    ```

With just a few lines of code (especially by Java standards), we were able to use out-of-the-box abstractions (Pulumi providers) and the builder pattern (a Java favorite) to compose a set of strongly typed, easy-to-reason about resources.

## Automation Abstractions with the Pulumi Automation API

With the introduction of Java 1.0, we’re also excited to announce that the [Automation API](https://www.pulumi.com/docs/iac/using-pulumi/automation-api/) is now supported in Java. The Automation API is a fully typed SDK that allows you to interact with Pulumi programs outside the Pulumi CLI. You can directly access and orchestrate your Pulumi projects and stacks with the SDK. This allows you to integrate Pulumi into other systems, such as CI/CD pipelines or internal tooling.

```java
    TODO
```

We're excited to bring the Automation API to the Java SDK for the first time and anticipate rapid iterations as feedback comes in.

## Get Started with Pulumi Java

To learn more about and to get started with Pulumi Java, you can check out the following resources:

* [Java SDK Repo](https://github.com/pulumi/pulumi-java): The Java SDK is fully open-source, and we’re excited to get your feedback or review any pull requests

* [Examples Repo](https://github.com/pulumi/examples): The Pulumi examples repo has many examples of Pulumi Java programs to help you get up and running with Pulumi Java.

* [Pulumi Java Converter](https://www.pulumi.com/docs/iac/adopting-pulumi/converters/): The Pulumi converter tool efficiently migrates existing IaC applications, such as Terraform, ARM, and Bicep, to Pulumi Java.
