---
title: "Pulumi Java is Now Generally Available"
date: 2025-02-10T16:15:00-08:00
draft: false

meta_desc: "The Pulumi Java SDK is now generally available. It enables organizations
  of all sizes to build infrastructure using a proven, safe, and familiar language."
meta_image: meta.png

authors:
  - mark-huber
  - justin-vanpatten
tags:
  - java
  - features
  - releases

social:
  twitter: "☕ The Pulumi Java SDK is now Generally Available! Manage your infrastructure
    using the composable, strongly typed programming language you already know and
    love - now including the powerful Pulumi Automation API!"
  linkedin: "Java, the world’s most trusted enterprise programming language, is now
    generally available in Pulumi. You can now leverage Java’s familiar, expressive,
    and safe syntax to manage your infrastructure in a composable and scalable way.\n
    Learn more about automating everything you run in the cloud with Java: [Link]"
search:
  keywords:
    - java
    - sizes
    - generally
    - available
    - proven
    - safe
    - var
---

One of Pulumi's core Infrastructure as Code (IaC) features is the ability to [model infrastructure](https://www.pulumi.com/docs/iac/concepts/) using well-traveled, familiar general-purpose programming languages. Today, we're thrilled to announce that Java, one of the world's most popular programming languages, is now generally available in Pulumi. This release joins our existing first-class support for TypeScript, Python, Go, YAML, and C#, enabling Java developers to manage cloud infrastructure using the language they know and trust.

<!--more-->

{{< youtube "GJLp6NjC2rE" >}}

We’ve grown our Java support based on feedback from the expanding set of companies that have adopted Pulumi Java in production workloads. Let’s look at some examples of using Java to power your Pulumi programs.

## Familiar Composability

Using Java with Pulumi lets you model your infrastructure using familiar patterns. Paired with rich abstractions, you can efficiently build Pulumi programs. It only seems appropriate that we take a look at a Java example using Oracle Cloud:

1. We start our program by grabbing our [configuration](https://www.pulumi.com/docs/iac/concepts/config/) values that describe which distro and AD to use.

    ```java
    var config = ctx.config();
    var compartmentId =  config.require("compartmentId");
    var availabilityDomain =  config.require("availabilityDomain");
    var ubuntuId =  config.require("ubuntuId");
    ```

2. Next, we create a set of abstractions to describe the networking and OS.

    ```java
    var vcn = new VirtualNetwork("virtualNetworkResource", VirtualNetworkArgs.builder()
            .compartmentId(compartmentId)
            .cidrBlock("10.0.0.0/16")
            .build());

    var subnet = new Subnet("testSubnet", SubnetArgs.builder()
            .cidrBlock("10.0.0.0/24")
            .compartmentId(compartmentId)
            .vcnId(vcn.id())
            .availabilityDomain(availabilityDomain)
            .build());

    var vnicDetails = InstanceCreateVnicDetailsArgs.builder()
            .subnetId(subnet.id())
            .assignPublicIp("true")
            .build();

    var sourceDetails = InstanceSourceDetailsArgs.builder()
            .sourceType("image")
            .sourceId(ubuntuId)
            .build();
    ```

3. Finally, we compose our instance.

    ```java
    var instance = new Instance("instanceResource", InstanceArgs.builder()
            .availabilityDomain(availabilityDomain)
            .compartmentId(compartmentId)
            .shape("VM.Standard.E2.1.Micro")
            .preserveBootVolume(false)
            .createVnicDetails(vnicDetails)
            .sourceDetails(sourceDetails)
            .build());
    ```

With just a few lines of code (especially by Java standards), we composed a set of strongly typed, easy-to-reason about resources using the builder pattern (a Java favorite) and without introducing any new language paradigms.

## New: Java Automation API

With the general availability of our Java language support, we’re also excited to announce that the [Automation API](https://www.pulumi.com/docs/iac/using-pulumi/automation-api/) is now supported in Java. The Automation API is a fully typed SDK that allows you to interact with Pulumi programs outside the Pulumi CLI. You can directly access and orchestrate your Pulumi projects and stacks with the SDK, allowing you to supercharge your Infrastructure as Code.

In our Automation API [examples repo](https://github.com/pulumi/automation-api-examples), we have an example demonstrating how you could construct a Pulumi program with the Automation API to [perform a database migration](https://github.com/pulumi/automation-api-examples/tree/main/java/databaseMigration). Let's take a look at a few of the interesting aspects:

1. Like regular Pulumi programs, we're able to obtain the current operating context and use the details to construct new resources, inline with the rest of the Automation API program.

    ```java
    Consumer<Context> program = ctx -> {
        ...

        var subnetGroup = new SubnetGroup("db-subnet", ...);

        // Make a public security group for our cluster for the migration
        var securityGroup = new SecurityGroup("public-security-group", ...);

        // Example values for our db
        var dbName = "hellosql";
        var dbUser = "hellosql";
        var dbPassword = "hellosql";

        // Provision our db
        var cluster = new Cluster("db", ClusterArgs.builder()
                .engine(EngineType.AuroraMysql)
                .engineVersion("8.0.mysql_aurora.3.08.0")
                .databaseName(dbName)
                .masterUsername(dbUser)
                .masterPassword(dbPassword)
                .skipFinalSnapshot(true)
                .dbSubnetGroupName(subnetGroup.name())
                .vpcSecurityGroupIds(securityGroup.id().applyValue(List::of))
                .build());

        var clusterInstance = new ClusterInstance("db-instance", ClusterInstanceArgs.builder()
                .clusterIdentifier(cluster.clusterIdentifier())
                .instanceClass("db.t3.medium")
                .engine(EngineType.AuroraMysql.getValue())
                .engineVersion("8.0.mysql_aurora.3.08.0")
                .publiclyAccessible(true)
                .dbSubnetGroupName(subnetGroup.name())
                .build());

        ctx.export("host", cluster.endpoint());
        ctx.export("db_name", dbName);
        ctx.export("db_user", dbUser);
        ctx.export("db_pass", dbPassword);
    };
    ```

2. With the Automation API, however, we're also able to directly interact with project and stack objects, giving us the opportunity to orchestrate workflows. This could include scaffolding
projects, working across stacks, or in our case, completing a one-time workflow to migrate a database.

    ```java
    var projectName = "database_migration_project";
    var stackName = "dev";

    try (var stack = LocalWorkspace.createOrSelectStack(projectName, stackName, program)) {
        ...

        stack.workspace().installPlugin("aws", "v6.68.0");

        stack.setConfig("aws:region", new ConfigValue("us-west-2"));

        System.out.println("updating stack...");
        var result = stack.up(UpOptions.builder()
                .onStandardOutput(System.out::println)
                .build());

        var changes = result.summary().resourceChanges();
        if (!changes.isEmpty()) {
            System.out.println("update summary:");
            changes.forEach((key, value) -> {
                System.out.printf("    %s: %d%n", key, value);
            });
        }

        System.out.printf("db host url: %s%n", result.outputs().get("host").value());
        configureDatabase(
            ...
        );
    }
    ```

The full example, along with others, is available in our Automation API [examples repo](https://github.com/pulumi/automation-api-examples/tree/main/java). We're excited to bring the Automation API to the [Java SDK](https://www.pulumi.com/docs/iac/languages-sdks/java/) for the first time and we're looking forward to your feedback.

## Get Started with Pulumi Java

To learn more about and to get started with Pulumi Java, you can check out the following resources:

* [Java SDK Repo](https://github.com/pulumi/pulumi-java): The Java SDK is fully open-source, and we’re excited to get your feedback or review any pull requests.

* [Examples Repo](https://github.com/pulumi/examples): The Pulumi examples repo has many examples of Pulumi Java programs to help you get up and running with Pulumi Java.

* [Pulumi Java Converter](https://www.pulumi.com/docs/iac/adopting-pulumi/converters/): The Pulumi converter tool efficiently migrates existing IaC applications, such as Terraform, ARM, and Bicep, to Pulumi Java.
