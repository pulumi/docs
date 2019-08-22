---
title: Documentation
linktitle: Docs
meta_desc: Learn how to create, deploy, and manage infrastructure on any cloud using Pulumi's open source infrastructure as code SDK.
noindex: true
no_on_this_page: true
menu:
    header:
        weight: 4
---

Pulumi is an <a href="https://github.com/pulumi/pulumi" target="_blank">open source</a> platform for building and
deploying cloud infrastructure and applications in your favorite language on any cloud.

Describe your resources in code---VMs, networks, databases, containers, Kubernetes clusters and workloads, serverless functions---and the CLI safely and reliably manages your cloud resources using an infrastructure-as-code approach.

<div class="flex justify-center py-6">
    <a class="btn btn-lg mx-1 my-1" href="{{< relref "/docs/get-started" >}}">GET STARTED</a>
</div>

<div class="my-4 bg-gray-100 border-t border-b border-gray-300 md:flex justify-between items-center px-4 py-2 max-w-6xl">
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

<div class="my-4 md:flex py-8">
    <div>
        <h3 class="no-anchor">Why Pulumi?</h3>
        <p class="text-sm text-gray-600">
            By using <a href="{{< relref "/docs/intro/languages" >}}">general-purpose languages</a>
            for infrastructure as code,
            you get all the benefits of real languages&mdash;IDEs, abstractions, and
            reuse thanks to functions, classes, and packages, debugging, testability,
            and more. The result is greater productivity with far less copy and paste,
            and it works the same way no matter which cloud you're targeting.
        </p>
    </div>
    <div class="md:mx-8">
        <h3 class="no-anchor">Alternatives</h3>
        <p class="text-sm text-gray-600">
            <a href="{{< relref "/docs/intro/vs" >}}">Other approaches</a> use YAML,
            JSON, or bespoke DSLs (Domain-Specific Languages) that you need to
            master and convince your team to use. These "languages" fall short of
            general purpose languages, since they lack abstractions and reuse, and reinvent
            familiar concepts like package managers. Worse, these solutions are usually
            unique to every given cloud that you need to target.
        </p>
    </div>
    <div>
        <h3 class="no-anchor">Community</h3>
        <p class="text-sm text-gray-600">
            Pulumi's SDK is fully <a href="https://github.com/pulumi/pulumi" target="_blank">open source</a>
            and extensible, enabling you to
            participate in a rich ecosystem of libraries that ease common tasks,
            ranging from containers to serverless to infrastructure, and everything
            in between. Languages and clouds are supported using an extensible
            plugin model, enabling public, private, and even hybrid cloud support.
        </p>
    </div>
</div>

<div class="my-4 bg-gray-100 border-t border-b border-gray-300 md:flex py-8 px-4 max-w-3xl">
    <div class="flex flex-col justify-between text-center h-full md:w-1/4 md:px-2 mb-12 md:mb-0">
        <a href="{{< relref "/docs/tutorials/aws/ecs-fargate" >}}">
            <img class="inline-block w-24" src="/images/docs/icon-feature-containers.svg">
            <h3 class="no-anchor mt-2 mb-0">Containers</h3>
        </a>
        <p class="mb-8 text-sm text-gray-600">
            Deploy a Docker container to production in 5 minutes using your favorite orchestrator.
        </p>
        <a class="btn btn-sm btn-secondary" href="{{< relref "/docs/tutorials/aws/ecs-fargate" >}}">
            Start Now
        </a>
    </div>
    <div class="flex flex-col justify-between text-center h-full md:w-1/4 md:px-2 mb-12 md:mb-0">
        <a href="{{< relref "/docs/tutorials/aws/rest-api" >}}">
            <img class="inline-block w-24" src="/images/docs/icon-feature-serverless.svg">
            <h3 class="no-anchor mt-2 mb-0">Serverless</h3>
        </a>
        <p class="mb-8 text-sm text-gray-600">
            Stand up a serverless API or event handler in 5 minutes using a real lambda in code.
        </p>
        <a class="btn btn-sm btn-secondary" href="{{< relref "/docs/tutorials/aws/rest-api" >}}">
            Start Now
        </a>
    </div>
    <div class="flex flex-col justify-between text-center h-full md:w-1/4 md:px-2 mb-12 md:mb-0">
        <a href="{{< relref "/docs/tutorials/aws/ec2-webserver" >}}">
            <img class="inline-block w-24" src="/images/docs/icon-feature-data.svg">
            <h3 class="no-anchor mt-2 mb-0">Infrastructure</h3>
        </a>
        <p class="mb-8 text-sm text-gray-600">
            Manage cloud infrastructure or hosted services using infrastructure as code.
        </p>
        <a class="btn btn-sm btn-secondary" href="{{< relref "/docs/tutorials/aws/ec2-webserver" >}}">
            Start Now
        </a>
    </div>
    <div class="flex flex-col justify-between text-center h-full md:w-1/4 md:px-2">
        <a href="{{< relref "/docs/get-started/kubernetes" >}}">
            <img class="inline-block w-24" src="/images/docs/icon-feature-kubernetes.svg">
            <h3 class="no-anchor mt-2 mb-0">Kubernetes</h3>
        </a>
        <p class="mb-8 text-sm text-gray-600">
            Deploy and orchestrate cloud native Kubernetes services in real code, no YAML needed.
        </p>
        <a class="btn btn-sm btn-secondary" href="{{< relref "/docs/get-started/kubernetes" >}}">
            Start Now
        </a>
    </div>
</div>

For questions or feedback, reach us through our [community Slack channel](https://slack.pulumi.com),
[GitHub](https://github.com/pulumi), or email [support@pulumi.com](mailto:support@pulumi.com).
