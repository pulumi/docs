---
title: Documentation
linktitle: Docs
meta_desc: Learn how to create, deploy, and manage infrastructure on any cloud using Pulumi's open source infrastructure as code SDK.
exclude_from_pulumi_search_index: true
no_on_this_page: true
menu:
    header:
        weight: 3
---

Welcome to the Pulumi documentation! These pages cover what Pulumi is, how to get started using it, and reference materials for its features and supported cloud providers.

### What is Pulumi?

Pulumi is an <a href="https://github.com/pulumi/pulumi" target="_blank">open source</a> infrastructure as code tool for creating, deploying, and managing cloud infrastructure. Pulumi works with traditional infrastructure like VMs, networks, and databases, in addition to modern architectures, including containers, Kubernetes clusters, and serverless functions. Pulumi supports dozens of public, private, and hybrid cloud service providers.

<div class="flex justify-center py-6">
    <a class="btn btn-lg mx-1 my-1" href="{{< relref "/docs/get-started" >}}">GET STARTED</a>
</div>

<div class="bg-gray-100 border-t border-b border-gray-300 max-w-6xl my-4 px-4 py-2">
    <div class="md:flex justify-between items-center">
        <a class="block rounded hover:bg-gray-200 transition-all my-2 py-4 text-center px-6" href="{{< relref "/docs/get-started/aws" >}}">
            <img class="inline-block h-8 w-auto -mb-2" src="/logos/tech/aws.svg">
        </a>
        <a class="block rounded hover:bg-gray-200 transition-all my-2 text-center md:mx-2 py-4 px-6" href="{{< relref "/docs/get-started/azure" >}}">
            <img class="inline-block h-8 w-auto" src="/logos/tech/azure.svg">
        </a>
        <a class="block rounded hover:bg-gray-200 transition-all my-2 text-center md:mx-2 py-4 px-6" href="{{< relref "/docs/get-started/gcp" >}}">
            <img class="inline-block h-8 w-auto" src="/logos/tech/gcp.svg">
        </a>
        <a class="block rounded hover:bg-gray-200 transition-all my-2 py-4 text-center px-6" href="{{< relref "/docs/get-started/kubernetes" >}}">
            <img class="inline-block h-8 w-auto" src="/logos/tech/k8s.svg">
        </a>
    </div>
</div>

<div class="my-4 md:flex py-8">
    <div class="md:w-1/3">
        <h3 class="no-anchor">Why Pulumi?</h3>
        <p class="text-sm text-gray-600">
            By using <a href="{{< relref "/docs/intro/languages" >}}">real languages</a>
            for infrastructure as code, you get many benefits: IDEs, abstractions including functions, classes,
            and packages, existing debugging and testing tools, and more. The result is greater productivity
            with far less copy and paste, and it works the same way no matter which cloud you're targeting.
        </p>
    </div>
    <div class="md:mx-8 md:w-1/3">
        <h3 class="no-anchor">Alternatives</h3>
        <p class="text-sm text-gray-600">
            <a href="{{< relref "/docs/intro/vs" >}}">Other approaches</a> use YAML,
            JSON, or proprietary domain-specific languages (DSLs) that you need to
            master and train your team to use. These alternative approaches reinvent
            familiar concepts like sharing and reuse, don't tap into existing
            ecosystems, and are often different for every cloud that you need to target.
        </p>
    </div>
    <div class="md:w-1/3">
        <h3 class="no-anchor">Community</h3>
        <p class="text-sm text-gray-600">
            Pulumi is <a href="https://github.com/pulumi/pulumi" target="_blank">open source</a>,
            extensible, and is backed by a growing community of cloud practitioners.
            Benefit from reusable libraries for common architectures, or share your own. Languages
            and clouds are supported using an extensible plugin model, enabling public,
            private, and even hybrid cloud support.
        </p>
    </div>
</div>

For questions or feedback, reach us through our [community Slack channel](https://slack.pulumi.com),
[GitHub](https://github.com/pulumi), or email [support@pulumi.com](mailto:support@pulumi.com).
