---
title_tag: Get Started with Pulumi
meta_desc: Step-by-step guides for creating, deploying, and managing infrastructure with Pulumi on the cloud using your favorite language.
title: Get started
h1: Get started with Pulumi
no_on_this_page: true
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Get started
        identifier: iac-get-started
        parent: iac-home
        weight: 20
    getstarted:
        name: Overview
        weight: 2
aliases:
    - /docs/quickstart/
    - /start/
    - /getting-started/
    - /get-started/
    - /docs/tour/
    - /docs/get-started
---

Pulumi is a modern [infrastructure as code](/what-is/what-is-infrastructure-as-code/) and [secrets management](/what-is/what-is-secrets-management/) platform that allows you to use familiar programming languages and tools to automate, secure and manage everything you run in the cloud.

Pulumi IaC is free, [open source](https://github.com/pulumi/pulumi), and optionally pairs with the [Pulumi Cloud](/docs/pulumi-cloud/) to make managing infrastructure secure, reliable, and hassle-free.

Select one of the following options to get started:

{{% chooser cloud "aws,azure,gcp,kubernetes" / %}}

{{% choosable cloud aws %}}

<div class="tiles flex-wrap justify-center items-stretch mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="aws-get-started" href="/docs/clouds/aws/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-folder text-blue-400 pr-2"></i>Pulumi IaC</h4>
                <p>If you are new to Pulumi, this guide helps you install Pulumi IaC, configure AWS, and run your first update.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-primary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="esc-get-started" href="/docs/esc/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-key text-blue-400 pr-2"></i>Pulumi ESC</h4>
                <p>This guide helps you install Pulumi ESC, create an environment and manage your first secret.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="insights-get-started" href="/docs/insights/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-search-plus text-blue-400 pr-2"></i>Pulumi Insights</h4>
                <p>This guide helps you get started with Pulumi Insight to discover and manage any cloud infrastructure</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="aws-kubernetes" href="/templates/kubernetes/aws/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cubes text-blue-400 pr-2"></i>Amazon Elastic Kubernetes Service (EKS)</h4>
                <p>Create an EKS cluster that provides a managed Kubernetes control plane.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="aws-static-website" href="/templates/static-website/aws/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cloud text-blue-400 pr-2"></i>S3 and Cloudfront Website</h4>
                <p>Create a static website hosted in S3 with a CloudFront Distribution to serve the website with caching and HTTPs.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="aws-serverless" href="/templates/serverless-application/aws/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-sitemap text-blue-400 pr-2"></i>Serverless with API Gateway</h4>
                <p>Create an API Gateway REST API and a static website that consumes that API.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
 </div>

{{< /choosable >}}

{{% choosable cloud azure %}}

<div class="tiles flex-wrap justify-center items-stretch mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="azure-get-started" href="/docs/clouds/azure/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-folder text-blue-400 pr-2"></i>Starter</h4>
                <p>If you are new to Pulumi, this guide helps you install Pulumi, configure Azure, and run your first update.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-primary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
         <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="esc-get-started" href="/docs/esc/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-key text-blue-400 pr-2"></i>Pulumi ESC</h4>
                <p>This guide helps you install Pulumi ESC, create an environment and manage your first secret.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
        <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="insights-get-started" href="/docs/insights/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-search-plus text-blue-400 pr-2"></i>Pulumi Insights</h4>
                <p>This guide helps you get started with Pulumi Insight to discover and manage any cloud infrastructure</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
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
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="azure-static-website" href="/templates/static-website/azure/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cloud text-blue-400 pr-2"></i>Static Website with a CDN</h4>
                <p>Create a static website with a Blob storage and a CDN to serve the website with caching and HTTPs.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="azure-serverless" href="/templates/serverless-application/azure/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-sitemap text-blue-400 pr-2"></i>Full Stack Serverless App</h4>
                <p>Create a Function App and a static website that consumes that Function.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
</div>

{{< /choosable >}}

{{% choosable cloud gcp %}}

<div class="tiles flex-wrap justify-center items-stretch mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="google-get-started" href="/docs/clouds/gcp/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-folder text-blue-400 pr-2"></i>Starter</h4>
                <p>If you are new to Pulumi, this guide helps you install Pulumi, configure Google Cloud, and run your first update.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-primary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="esc-get-started" href="/docs/esc/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-key text-blue-400 pr-2"></i>Pulumi ESC</h4>
                <p>This guide helps you install Pulumi ESC, create an environment and manage your first secret.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="insights-get-started" href="/docs/insights/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-search-plus text-blue-400 pr-2"></i>Pulumi Insights</h4>
                <p>This guide helps you get started with Pulumi Insight to discover and manage any cloud infrastructure</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
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
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="google-static-website" href="/templates/static-website/gcp/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cloud text-blue-400 pr-2"></i>Static Website with a CDN</h4>
                <p>Create a static website with a Cloud Storage bucket and a CDN to serve the website with caching and HTTPs.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="google-serverless" href="/templates/serverless-application/gcp/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-sitemap text-blue-400 pr-2"></i>Full Stack Serverless App</h4>
                <p>Create a Cloud Function and a static website that consumes that function.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
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
                <h4 class="no-anchor"><i class="fas fa-folder text-blue-400 pr-2"></i>Starter</h4>
                <p>If you are new to Pulumi, this guide helps you install Pulumi, configure the Kubernetes Provider, and run your first update.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-primary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
         <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="esc-get-started" href="/docs/esc/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-key text-blue-400 pr-2"></i>Pulumi ESC</h4>
                <p>This guide helps you install Pulumi ESC, create an environment and manage your first secret.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="insights-get-started" href="/docs/insights/get-started/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-search-plus text-blue-400 pr-2"></i>Pulumi Insights</h4>
                <p>This guide helps you get started with Pulumi Insight to discover and manage any cloud infrastructure</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="kubernetes-helm" href="/templates/kubernetes-application/helm-chart/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cloud text-blue-400 pr-2"></i>Helm Chart</h4>
                <p>Deploy a Helm chart to an existing cluster using Pulumi.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="kubernetes-web-app" href="/templates/kubernetes-application/web-application/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-sitemap text-blue-400 pr-2"></i>Web App</h4>
                <p>Deploy and example web application into an existing Kubernetes cluster.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a data-track="kubernetes-aws" href="/templates/kubernetes/aws" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
                <h4 class="no-anchor"><i class="fas fa-cubes text-blue-400 pr-2"></i>Amazon Elastic Kubernetes Service (EKS)</h4>
                <p>Create an EKS cluster that provides a managed Kubernetes control plane.</p>
                <div class="flex flex-grow items-end">
                    <div class="btn btn-secondary">Get Started</div>
                </div>
            </div>
        </a>
    </div>
</div>

{{< /choosable >}}

Alternatively, you can watch the following video which provides a high level overview of how Pulumi works:

<div class="rounded-md shadow border border-gray-300 w-3/4 mx-auto my-4" style="position: relative; padding-bottom: 40.25%; height: 0; overflow: hidden;">
    <iframe
        src="//www.youtube.com/embed/Q8tw6YTD3ac?rel=0"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;"
        allowfullscreen=""
        title="Introduction to Pulumi in Three Minutes"
        srcdoc="<style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img{position:absolute;width:100%;top:0;bottom:0;margin:auto}</style><a href=https://www.youtube.com/embed/Q8tw6YTD3ac?autoplay=1><img src='/images/home/youtube-getting-started.png' alt='Introduction to Pulumi in Three Minutes'></a>">
    </iframe>
</div>

## Pulumi Cloud

The Pulumi Cloud is a fully managed service that helps you adopt Pulumi’s open source SDK with ease. It provides built-in state and secrets management, integrates with source control and CI/CD, and offers a web console and API that make it easier to visualize and manage infrastructure. It is free for individual use, with features available for teams.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Create an Account</a>

## Additional resources

The following sections are also useful when first learning how to use Pulumi:

<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/intro/concepts"><i class="fas fa-file-alt pr-2"></i>Concepts</a></h3>
        <p>Get details on the Pulumi programming model and core concepts.</p>
    </div>
    <div class="md:w-1/2 md:ml-4 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="/docs/using-pulumi/adopting-pulumi/"><i class="fas fa-cloud pr-2"></i>Adopting Pulumi</a></h3>
        <p>Learn how to support, migrate, or convert existing cloud infrastructure with Pulumi.</p>
    </div>
</div>
