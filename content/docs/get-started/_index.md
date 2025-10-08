---
title_tag: Get Started with Pulumi
meta_desc: Step-by-step guides for creating, deploying, and managing infrastructure with Pulumi on the cloud using your favorite language.
title: Get started
h1: Get started with Pulumi
no_on_this_page: true
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    get-started:
        name: Get started
        identifier: get-started-home
        weight: 1
aliases:
    - /docs/iac/get-started/
    - /docs/quickstart/
    - /start/
    - /getting-started/
    - /get-started/
    - /docs/tour/
    - /docs/get-started
---

Pulumi is a modern [infrastructure as code](/what-is/what-is-infrastructure-as-code/) and [secrets management](/what-is/what-is-secrets-management/) platform that allows you to use familiar programming languages and tools to automate, secure and manage everything you run in the cloud.

Pulumi IaC is free, [open source](https://github.com/pulumi/pulumi), and optionally pairs with the [Pulumi Platform](/docs/platform/) to make managing infrastructure secure, reliable, and hassle-free.

Select one of the following options to get started:

{{% chooser cloud "aws,azure,gcp,kubernetes" / %}}

{{% choosable cloud aws %}}

<div class="tiles flex-wrap justify-center items-stretch mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="aws-get-started" href="/docs/iac/get-started/aws/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-folder text-blue-400 pr-2"></i>Infrastructure as Code</h4>
                <p>Install the CLI, configure AWS, and deploy your first infrastructure.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="esc-get-started" href="/docs/esc/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-key text-blue-400 pr-2"></i>Secrets & Configuration</h4>
                <p>Create your first environment and manage secrets and configuration.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="insights-get-started" href="/docs/insights/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-search-plus text-blue-400 pr-2"></i>Insights & Governance</h4>
                <p>Discover and manage cloud infrastructure across all your resources.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="aws-kubernetes" href="/templates/kubernetes/aws/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cubes text-blue-400 pr-2"></i>Amazon Elastic Kubernetes Service (EKS)</h4>
                <p>Create an EKS cluster that provides a managed Kubernetes control plane.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="aws-static-website" href="/templates/static-website/aws/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cloud text-blue-400 pr-2"></i>S3 and Cloudfront Website</h4>
                <p>Create a static website hosted in S3 with a CloudFront Distribution to serve the website with caching and HTTPs.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="aws-serverless" href="/templates/serverless-application/aws/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-sitemap text-blue-400 pr-2"></i>Serverless with API Gateway</h4>
                <p>Create an API Gateway REST API and a static website that consumes that API.</p>
            </div>
        </a>
    </div>
 </div>

{{< /choosable >}}

{{% choosable cloud azure %}}

<div class="tiles flex-wrap justify-center items-stretch mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="azure-get-started" href="/docs/iac/get-started/azure/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-folder text-blue-400 pr-2"></i>Infrastructure as Code</h4>
                <p>Install the CLI, configure Azure, and deploy your first infrastructure.</p>
            </div>
        </a>
    </div>
         <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="esc-get-started" href="/docs/esc/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-key text-blue-400 pr-2"></i>Secrets & Configuration</h4>
                <p>Create your first environment and manage secrets and configuration.</p>
            </div>
        </a>
    </div>
        <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="insights-get-started" href="/docs/insights/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-search-plus text-blue-400 pr-2"></i>Insights & Governance</h4>
                <p>Discover and manage cloud infrastructure across all your resources.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="azure-kubernetes" href="/templates/kubernetes/azure/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cubes text-blue-400 pr-2"></i>Azure Kubernetes Service (AKS)</h4>
                <p>
                    Create an Azure Virtual Network with three subnets and deploy an Azure Kubernetes Service (AKS) cluster.
                </p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="azure-static-website" href="/templates/static-website/azure/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cloud text-blue-400 pr-2"></i>Static Website with a CDN</h4>
                <p>Create a static website with a Blob storage and a CDN to serve the website with caching and HTTPs.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="azure-serverless" href="/templates/serverless-application/azure/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-sitemap text-blue-400 pr-2"></i>Full Stack Serverless App</h4>
                <p>Create a Function App and a static website that consumes that Function.</p>
            </div>
        </a>
    </div>
</div>

{{< /choosable >}}

{{% choosable cloud gcp %}}

<div class="tiles flex-wrap justify-center items-stretch mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="google-get-started" href="/docs/iac/get-started/gcp/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-folder text-blue-400 pr-2"></i>Infrastructure as Code</h4>
                <p>Install the CLI, configure Google Cloud, and deploy your first infrastructure.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="esc-get-started" href="/docs/esc/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-key text-blue-400 pr-2"></i>Secrets & Configuration</h4>
                <p>Create your first environment and manage secrets and configuration.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="insights-get-started" href="/docs/insights/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-search-plus text-blue-400 pr-2"></i>Insights & Governance</h4>
                <p>Discover and manage cloud infrastructure across all your resources.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="google-kubernetes" href="/templates/kubernetes/gcp/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cubes text-blue-400 pr-2"></i>Google Kubernetes Engine (GKE)</h4>
                <p>
                    Create a VPC network with a subnet and deploy a Google Kubernetes Engine (GKE) cluster.
                </p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="google-static-website" href="/templates/static-website/gcp/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cloud text-blue-400 pr-2"></i>Static Website with a CDN</h4>
                <p>Create a static website with a Cloud Storage bucket and a CDN to serve the website with caching and HTTPs.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="google-serverless" href="/templates/serverless-application/gcp/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-sitemap text-blue-400 pr-2"></i>Full Stack Serverless App</h4>
                <p>Create a Cloud Function and a static website that consumes that function.</p>
            </div>
        </a>
    </div>
</div>

{{< /choosable >}}

{{% choosable cloud kubernetes %}}

<div class="tiles flex-wrap justify-center items-stretch mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="kubernetes-get-started" href="/docs/iac/get-started/kubernetes/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-folder text-blue-400 pr-2"></i>Infrastructure as Code</h4>
                <p>Install the CLI, configure the Kubernetes Provider, and deploy your first infrastructure.</p>
            </div>
        </a>
    </div>
         <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="esc-get-started" href="/docs/esc/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-key text-blue-400 pr-2"></i>Secrets & Configuration</h4>
                <p>Create your first environment and manage secrets and configuration.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="insights-get-started" href="/docs/insights/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-search-plus text-blue-400 pr-2"></i>Insights & Governance</h4>
                <p>Discover and manage cloud infrastructure across all your resources.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="kubernetes-helm" href="/templates/kubernetes-application/helm-chart/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cloud text-blue-400 pr-2"></i>Helm Chart</h4>
                <p>Deploy a Helm chart to an existing cluster using Pulumi.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="kubernetes-web-app" href="/templates/kubernetes-application/web-application/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-sitemap text-blue-400 pr-2"></i>Web App</h4>
                <p>Deploy and example web application into an existing Kubernetes cluster.</p>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="kubernetes-aws" href="/templates/kubernetes/aws" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cubes text-blue-400 pr-2"></i>Amazon Elastic Kubernetes Service (EKS)</h4>
                <p>Create an EKS cluster that provides a managed Kubernetes control plane.</p>
            </div>
        </a>
    </div>
</div>

{{< /choosable >}}

## Additional resources

The following sections are also useful when first learning how to use Pulumi:

<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/iac/concepts/"><i class="fas fa-file-alt pr-2"></i>Concepts</a></h3>
        <p>Get details on the Pulumi programming model and core concepts.</p>
    </div>
    <div class="md:w-1/2 md:ml-4 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/iac/guides/migration/"><i class="fas fa-cloud pr-2"></i>Migration</a></h3>
        <p>Learn how to support, migrate, or convert existing cloud infrastructure with Pulumi.</p>
    </div>
</div>
