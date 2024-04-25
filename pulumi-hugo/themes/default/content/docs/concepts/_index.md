---
title_tag: What is Pulumi?
meta_desc: Learn about what Pulumi is, how it works, and how its components work together to deliver a robust platform for creating and managing cloud infrastructure.
title: Concepts
h1: What is Pulumi?
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    name: Overview
    weight: 4

aliases:
- /docs/reference/concepts/
- /docs/intro/concepts/
---

Pulumi is a modern [infrastructure as code](/what-is/what-is-infrastructure-as-code/) platform. It leverages existing programming languages---TypeScript, JavaScript, Python, Go, .NET, Java, and markup languages like YAML---and their native ecosystems to interact with cloud resources. A [downloadable CLI](/docs/install/), runtime, libraries, and a hosted service work together to deliver a robust platform for provisioning, updating, and managing cloud infrastructure.

{{< notes >}}
If this is your first time using Pulumi, you likely want to begin with [the Getting Started guide](/docs/get-started/) for your cloud of choice. It will walk you through an [AWS](/docs/clouds/aws/get-started/), [Azure](/docs/clouds/azure/get-started/), [Google Cloud](/docs/clouds/gcp/get-started/), or [Kubernetes](/docs/clouds/kubernetes/get-started/) deployment from start to finish.
{{< /notes >}}

## What is Pulumi?

Pulumi is an [infrastructure as code](/what-is/what-is-infrastructure-as-code/) platform that allows you to use familiar programming languages and tools to build, deploy, and manage cloud infrastructure.

Pulumi is free, [open source](https://github.com/pulumi/pulumi), and optionally pairs with the [Pulumi Cloud](https://www.pulumi.com/docs/pulumi-cloud/) to make managing infrastructure secure, reliable, and hassle-free.

## Supported languages and SDKs

As a multi-language infrastructure as code tool, Pulumi supports many of today's most common general-purpose programming and markup languages. Every Pulumi-supported language is equally capable of provisioning and managing infrastructure across all major clouds, though some languages may provide functionality that's not yet available in others. The following languages and runtimes are currently supported:

- [TypeScript & JavaScript (Node.js)](https://www.pulumi.com/docs/languages-sdks/javascript/)
- [Python](https://www.pulumi.com/docs/languages-sdks/python/)
- [Go](https://www.pulumi.com/docs/languages-sdks/go/)
- [C#, VB, F# (.NET)](https://www.pulumi.com/docs/languages-sdks/dotnet/)
- [Java](https://www.pulumi.com/docs/languages-sdks/java/)
- [Pulumi YAML](https://www.pulumi.com/docs/languages-sdks/yaml/)

{{< notes >}}
If you don't see your favorite language listed, it may be on its way soon. [Pulumi is open source](https://github.com/pulumi/pulumi), and it is possible to [add your own language](https://www.pulumi.com/docs/support/faq/#how-can-i-add-support-for-my-favorite-language). For additional language questions, visit [Pulumi's languages and SDK docs](https://www.pulumi.com/docs/languages-sdks/).
{{< /notes >}}

## How does Pulumi work?

The Pulumi platform comprises several components:

- **Software development kit (SDK)**: Pulumi Software Development Kit (SDK) provides bindings for each type of resource that the provider can manage. This provides the necessary tools and libraries for defining and managing cloud resources on any cloud and with any provider.

- **Command-Line interface (CLI)**: Pulumi is controlled primarily using the command line interface [(CLI)](https://www.pulumi.com/docs/cli/). It works in conjunction with the [Pulumi Cloud](https://www.pulumi.com/docs/pulumi-cloud/) to deploy changes to your cloud apps and infrastructure. It keeps a history of who updated what in your team and when. This CLI has been designed for great inner loop productivity, in addition to continuous integration and delivery scenarios.

- **Deployment engine** The deployment engine is responsible for computing the set of operations needed to drive the current state of your infrastructure into the desired state expressed by your program.

This diagram illustrates the structure and major components of Pulumi.

![Pulumi programming model diagram.](/images/docs/pulumi-programming-model-diagram.svg)

Pulumi *programs*, written in general-purpose [programming languages](/docs/languages-sdks/), describe how your cloud infrastructure should be composed. To declare new infrastructure in your program, you allocate *resource* objects whose properties correspond to the desired state of your infrastructure. These properties are also used between resources to handle any necessary dependencies and can be exported outside of the stack, if needed.

Programs reside in a *project*, which is a directory that contains source code for the program and metadata on how to run the program. After writing your program, you run the [Pulumi CLI](/docs/cli/) command `pulumi up` from within your project directory. This command creates an isolated and configurable instance of your program, known as a *stack*. Stacks are similar to different deployment environments that you use when testing and rolling out application updates. For instance, you can have distinct development, staging, and production stacks that you create and test against.

### Example

To illustrate these concepts, the following program shows how to create an AWS EC2 security group named `web-sg` with a single ingress rule and a `t2.micro`-sized EC2 instance using that security group.

To use the security group, the EC2 resource requires the security group's ID. Pulumi enables this through the output property `id` on the security group resource. Pulumi understands dependencies between resources and uses the relationships between resources to maximize parallelism and ensures correct ordering when a stack is instantiated.

Finally, the server's resulting IP address and DNS name are exported as stack outputs so that their values can be accessed through either a CLI command or by another stack.

{{< example-program path="aws-ec2-instance-with-sg">}}

## Concepts in depth

The following topics provide more details on the core concepts of Pulumi and how to use it:

<!-- how & projects -->
<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/how-pulumi-works"><i class="fas fa-laptop-code pr-2"></i>How Pulumi works</a></h3>
        <p>Learn about how Pulumi performs deployments under the hood.</p>
    </div>
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/projects"><i class="fas fa-folder-open pr-2"></i>Projects</a></h3>
        <p>Learn how Pulumi projects are organized and configured.</p>
    </div>
</div>

<!-- stacks & resources -->
<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/stack"><i class="fas fa-cloud pr-2"></i>Stacks</a></h3>
        <p>Learn how to create and deploy stacks.</p>
    </div>
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/resources"><i class="fas fa-server pr-2"></i>Resources</a></h3>
        <p>Learn more about how to use and manage resources in your programs.</p>
    </div>
</div>

<!-- resource options & inputs/outputs -->
<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/options"><i class="fas fa-swatchbook pr-2"></i>Resource options</a></h3>
        <p>Learn more about how to use and manage resource options in your program.</p>
    </div>
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/inputs-outputs"><i class="fas fa-file-import pr-2"></i>Inputs and outputs</a></h3>
        <p>Learn how to use resource properties to handle dependencies between resources.</p>
    </div>
</div>

<!-- config & secrets -->
<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/config"><i class="fas fa-toolbox pr-2"></i>Configuration</a></h3>
        <p>Learn how to configure stacks for different deployment scenarios.</p>
    </div>
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/secrets"><i class="fas fa-key pr-2"></i>Secrets</a></h3>
        <p>Learn how to handle sensitive data and how to store secret encrypted settings in Pulumi.</p>
    </div>
</div>

<!--  esc & state backends-->
<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/environments"><i class="fas fa-cubes pr-2"></i>Environments (ESC)</a></h3>
        <p>Learn how to configure your deployment environments with Pulumi ESC.</p>
    </div>
     <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/state"><i class="fas fa-file-alt pr-2"></i>State and backends</a></h3>
        <p>Learn how Pulumi stores state and manages concurrency.</p>
    </div>
</div>

<!-- logging & update plans -->
<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/logging"><i class="fas fa-clipboard-list pr-2"></i>Logging</a></h3>
        <p>Learn about how to access log information for diagnostics and debugging.</p>
    </div>
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/update-plans"><i class="fas fa-upload pr-2"></i>Update plans</a></h3>
        <p>Learn about how to constrain your deployments with update plans.</p>
    </div>
</div>

<!-- glossary & compare-->
<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid md:ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/glossary"><i class="fas fa-book pr-2"></i>Glossary</a></h3>
        <p>Look up definitions to commonly used terms.</p>
    </div>
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/concepts/vs"><i class="fas fa-table pr-2"></i>Compare</a></h3>
        <p>Learn about how Pulumi compares to other solutions.</p>
    </div>
</div>
