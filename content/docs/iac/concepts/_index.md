---
title_tag: What is Pulumi?
meta_desc: Learn about what Pulumi is, how it works, and how its components work together to deliver a robust platform for creating and managing cloud infrastructure.
title: Concepts
h1: What is Pulumi?
menu:
    iac:
        name: Concepts
        weight: 15
        parent: iac-home
        identifier: iac-concepts
    concepts:
        name: Overview
        weight: 4
aliases:
- /docs/reference/concepts/
- /docs/intro/concepts/
- /docs/concepts/
- /docs/iac/concepts/miscellaneous/
---

Pulumi is a modern [infrastructure as code](/what-is/what-is-infrastructure-as-code/) platform. It uses existing programming languages---TypeScript, JavaScript, Python, Go, .NET, Java, and markup languages like YAML---and their native ecosystems to interact with cloud resources. A [downloadable CLI](/docs/install/), runtime, libraries, and a hosted service work together to deliver a robust platform for provisioning, updating, and managing cloud infrastructure.

{{< notes >}}
If this is your first time using Pulumi, you likely want to begin with [the Getting Started guide](/docs/get-started/) for your cloud of choice. It will walk you through an [AWS](/docs/iac/get-started/aws/), [Azure](/docs/iac/get-started/azure/), [Google Cloud](/docs/iac/get-started/gcp/), or [Kubernetes](/docs/iac/get-started/kubernetes/) deployment from start to finish.
{{< /notes >}}

Pulumi is free and [open source](https://github.com/pulumi/pulumi). It optionally pairs with [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/), a managed backend that stores your state and adds access control, reusable configuration and secrets, policy enforcement, and drift detection for teams.

## Supported languages and SDKs

As a multi-language infrastructure as code tool, Pulumi supports many of today's most common general-purpose programming and markup languages. Every Pulumi-supported language is equally capable of provisioning and managing infrastructure across all major clouds, though some languages may provide functionality that's not yet available in others. The following languages and runtimes are currently supported:

- [TypeScript & JavaScript (Node.js)](/docs/iac/languages-sdks/javascript/)
- [Python](/docs/iac/languages-sdks/python/)
- [Go](/docs/iac/languages-sdks/go/)
- [C#, VB, F# (.NET)](/docs/iac/languages-sdks/dotnet/)
- [Java](/docs/iac/languages-sdks/java/)
- [Pulumi YAML](/docs/iac/languages-sdks/yaml/)

{{< notes >}}
If you don't see your favorite language listed, it may be on its way soon. [Pulumi is open source](https://github.com/pulumi/pulumi), and it is possible to add your own language. For additional language questions, visit [Pulumi's languages and SDK docs](/docs/iac/languages-sdks/).
{{< /notes >}}

## How does Pulumi work?

You write a Pulumi program against a language SDK and run it with the Pulumi CLI, which drives a deployment engine. Three components do the work:

- **Software development kit (SDK)**: The Pulumi SDK provides bindings for each resource type that a provider can manage, along with the libraries you use to define and manage cloud resources on any cloud and with any provider.

- **Command-line interface (CLI)**: You control Pulumi primarily through the [CLI](/docs/iac/cli/). It works with [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) to deploy changes to your cloud apps and infrastructure, and it records who on your team updated what, and when. The CLI is designed both for a fast inner development loop and for continuous integration and delivery.

- **Deployment engine**: The deployment engine computes the set of operations needed to drive the current state of your infrastructure into the desired state expressed by your program.

For a step-by-step account of how these pieces interact at runtime — including the language host and resource providers — see [How Pulumi IaC works](/docs/iac/guides/basics/how-pulumi-works/).

The following diagram shows how the building blocks you write relate to each other: a project holding a program, the resources that program declares, and the stacks it deploys into.

![Diagram of the Pulumi programming model: a project contains a program that declares three resources chained by inputs and outputs, deployed into dev, qa, and prod stacks.](/images/docs/pulumi-programming-model-diagram.svg)

Pulumi *programs*, written in general-purpose [programming languages](/docs/iac/languages-sdks/), describe how your cloud infrastructure should be composed. To declare new infrastructure in your program, you allocate *resource* objects whose properties correspond to the desired state of your infrastructure. These properties are also used between resources to handle any necessary dependencies and can be exported outside of the stack, if needed.

Programs live in a *project*, which is a directory that contains source code for the program and metadata on how to run the program. After writing your program, you run the [Pulumi CLI](/docs/iac/cli/) command `pulumi up` from within your project directory. This command creates an isolated and configurable instance of your program, known as a *stack*. Stacks are similar to different deployment environments that you use when testing and rolling out application updates. For instance, you can have distinct development, staging, and production stacks that you create and test against.

### Example

To illustrate these concepts, the following program shows how to create an AWS EC2 security group named `web-sg` with a single ingress rule and a `t2.micro`-sized EC2 instance using that security group.

To use the security group, the EC2 resource requires the security group's ID. Pulumi enables this through the output property `id` on the security group resource. Pulumi tracks the dependencies between resources and uses them to maximize parallelism while preserving correct ordering when a stack is deployed.

Finally, the server's resulting IP address and DNS name are exported as stack outputs so that their values can be accessed through either a CLI command or by another stack.

{{< example-program path="aws-ec2-instance-with-sg" >}}

## Concepts in depth

### Core concepts

- [How Pulumi IaC Works](/docs/iac/guides/basics/how-pulumi-works/) — Learn how the language host, deployment engine, and resource providers work together under the hood.
- [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) — Learn how Pulumi Cloud relates to the open source tool and what it offers for teams.
- [Projects](/docs/iac/concepts/projects/) — Learn how Pulumi projects are organized and configured.
- [Stacks](/docs/iac/concepts/stacks/) — Learn how to create and deploy stacks.
- [Resources](/docs/iac/concepts/resources/) — Learn more about how to use and manage resources in your programs.
- [Resource options](/docs/iac/concepts/resources/options/) — Learn more about how to use and manage resource options in your program.
- [Inputs and outputs](/docs/iac/concepts/inputs-outputs/) — Learn how to use resource properties to handle dependencies between resources.

### Configuration and state

- [Configuration](/docs/iac/concepts/config/) — Learn how to configure stacks for different deployment scenarios.
- [Secrets](/docs/iac/concepts/secrets/) — Learn how to handle sensitive data and store secret encrypted settings in Pulumi.
- [Environments (ESC)](/docs/esc/concepts/) — Learn how to configure your deployment environments with Pulumi ESC.
- [State and backends](/docs/iac/concepts/state-and-backends/) — Learn how Pulumi stores state and manages concurrency.
- [Update plans](/docs/iac/operations/stack-management/update-plans/) — Learn about how to constrain your deployments with update plans.

### Reference

- [Glossary](/docs/reference/glossary/) — Look up definitions for commonly used terms.
- [Comparisons](/docs/iac/comparisons/) — Learn about how Pulumi compares to other infrastructure tools.
- [Converters](/docs/iac/concepts/converters/) — Learn how to translate IaC from other tools into Pulumi programs.
