---
title: Pulumi Documentation
noindex: true
menu:
    header:
        name: Docs
        weight: 4
---

Pulumi is an <a href="https://github.com/pulumi/pulumi" target="_blank">open source</a> platform for building and
deploying cloud infrastructure and applications in your favorite language on any cloud.

Describe your resources in code -- VMs, networks, databases, containers, Kubernetes clusters & workloads, serverless
functions -- and the CLI safely and reliably manages your cloud resources using an infrastructure-as-code approach.

<div class="flex justify-center py-6">
    <a class="btn btn-lg mx-1 my-1" href="{{< relref "/docs/quickstart" >}}">GET STARTED</a>
    <a class="btn btn-lg btn-secondary mx-1 my-1" href="{{< relref "/docs/reference" >}}">LEARN</a>
</div>

<div class="my-4 bg-gray-100 border-t border-b border-gray-300 md:flex justify-center py-8 max-w-6xl">
    <a href="{{< relref "/docs/quickstart/aws" >}}"><img src="/images/docs/quickstart/aws-purple.png"></a>
    <a href="{{< relref "/docs/quickstart/azure" >}}"><img src="/images/docs/quickstart/azure-purple.png"></a>
    <a href="{{< relref "/docs/quickstart/gcp" >}}"><img src="/images/docs/quickstart/gcp-purple.png"></a>
    <a href="{{< relref "/docs/quickstart/kubernetes" >}}"><img src="/images/docs/quickstart/k8s-purple.png"></a>
</div>

<div class="my-4 md:flex py-8">
    <div>
        <h3 class="no-anchor">Why Pulumi?</h3>
        <p class="text-sm text-gray-600">
            By using <a href="{{< relref "/docs/reference/languages" >}}">general purpose languages</a>
            for infrastructure as code,
            you get all the benefits of real languages -- IDEs, abstractions and
            reuse thanks to functions, classes, and packages, debugging, testability,
            and more. The result is far less copy and paste and greater productivity,
            and it works the same way no matter which cloud you're targeting.
        </p>
    </div>
    <div class="md:mx-8">
        <h3 class="no-anchor">Alternatives</h3>
        <p class="text-sm text-gray-600">
            <a href="{{< relref "/docs/reference/vs" >}}">Other approaches</a> use YAML,
            JSON, or bespoke DSLs that you need to
            master -- and convince your team to use. These "languages" fall short of
            general purpose languages, lacking abstractions and reuse, and reinvent
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
        <a href="{{< relref "/docs/reference/tutorials/aws/tutorial-service" >}}">
            <img class="inline-block w-24" src="/images/docs/icon-feature-containers.svg">
            <h3 class="no-anchor mt-2 mb-0">Containers</h3>
        </a>
        <p class="mb-8 text-sm text-gray-600">
            Deploy a Docker container to production in 5 minutes using your favorite orchestrator.
        </p>
        <a class="btn btn-sm btn-secondary" href="{{< relref "/docs/reference/tutorials/aws/tutorial-service" >}}">
            Start Now
        </a>
    </div>
    <div class="flex flex-col justify-between text-center h-full md:w-1/4 md:px-2 mb-12 md:mb-0">
        <a href="{{< relref "/docs/reference/tutorials/aws/tutorial-rest-api" >}}">
            <img class="inline-block w-24" src="/images/docs/icon-feature-serverless.svg">
            <h3 class="no-anchor mt-2 mb-0">Serverless</h3>
        </a>
        <p class="mb-8 text-sm text-gray-600">
            Stand up a serverless API or event handler in 5 minutes using a real lambda in code.
        </p>
        <a class="btn btn-sm btn-secondary" href="{{< relref "/docs/reference/tutorials/aws/tutorial-rest-api" >}}">
            Start Now
        </a>
    </div>
    <div class="flex flex-col justify-between text-center h-full md:w-1/4 md:px-2 mb-12 md:mb-0">
        <a href="{{< relref "/docs/reference/tutorials/aws/tutorial-ec2-webserver" >}}">
            <img class="inline-block w-24" src="/images/docs/icon-feature-data.svg">
            <h3 class="no-anchor mt-2 mb-0">Infrastructure</h3>
        </a>
        <p class="mb-8 text-sm text-gray-600">
            Manage cloud infrastructure or hosted services using infrastructure as code.
        </p>
        <a class="btn btn-sm btn-secondary" href="{{< relref "/docs/reference/tutorials/aws/tutorial-ec2-webserver" >}}">
            Start Now
        </a>
    </div>
    <div class="flex flex-col justify-between text-center h-full md:w-1/4 md:px-2">
        <a href="{{< relref "/docs/quickstart/kubernetes" >}}">
            <img class="inline-block w-24" src="/images/docs/icon-feature-kubernetes.svg">
            <h3 class="no-anchor mt-2 mb-0">Kubernetes</h3>
        </a>
        <p class="mb-8 text-sm text-gray-600">
            Deploy and orchestrate cloud native Kubernetes services in real code, no YAML needed.
        </p>
        <a class="btn btn-sm btn-secondary" href="{{< relref "/docs/quickstart/kubernetes" >}}">
            Start Now
        </a>
    </div>
</div>

For questions or feedback, reach us in our [community Slack channel](https://slack.pulumi.io),
on [GitHub](https://github.com/pulumi), or by emailing [support@pulumi.com](mailto:support@pulumi.com).
