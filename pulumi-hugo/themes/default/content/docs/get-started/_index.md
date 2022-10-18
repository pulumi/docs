---
title: Get Started with Pulumi
meta_desc: Step-by-step guides for creating, deploying, and managing infrastructure with
           Pulumi on the cloud using your favorite language.
no_on_this_page: true
menu:
  getstarted:
      name: Overview
      weight: 1

aliases:
  - /docs/quickstart/
  - /start/
  - /getting-started/
  - /get-started/
---

Pulumi is a [universal infrastructure as code]({{< relref "/what-is/what-is-infrastructure-as-code" >}}) platform that allows you to use familiar programming languages and tools to build, deploy, and manage cloud infrastructure.

Pulumi is free, [open source](https://github.com/pulumi/pulumi), and optionally pairs with the [Pulumi Service]({{< relref "/docs/intro/pulumi-service" >}}) to make managing infrastructure secure, reliable, and hassle-free.

Select one of the following options to get started:

{{% chooser cloud "aws,azure,gcp,kubernetes" / %}}

{{% choosable cloud aws %}}

<div class="tiles flex-wrap justify-center items-stretch mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-folder text-blue-400 pr-2"></i>Starter App</h4>
            <p>If you are new to Pulumi, this guide helps you install Pulumi, configure AWS, and run your first update.</p>
            <div class="flex flex-grow items-end">
                <a data-track="aws-get-started" href="{{< relref "/docs/get-started/aws" >}}" class="btn btn-primary">Get Started</a>
            </div>
        </div>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-cubes text-blue-400 pr-2"></i>Kubernetes with EKS</h4>
            <p>Create an EKS cluster that provides a managed Kubernetes control plane.</p>
            <div class="flex flex-grow items-end">
                <a data-track="aws-kubernetes" href="{{< relref "/templates/kubernetes/aws" >}}" class="btn btn-secondary">Get Started</a>
            </div>
        </div>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-cloud text-blue-400 pr-2"></i>S3 and Cloudfront Website</h4>
            <p>Create a static website hosted in S3 with a CloudFront Distribution to serve the website with caching and HTTPs.</p>
            <div class="flex flex-grow items-end">
                <a data-track="aws-static-website" href="{{< relref "/templates/static-website/aws" >}}" class="btn btn-secondary">Get Started</a>
            </div>
        </div>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-sitemap text-blue-400 pr-2"></i>Full Stack Serverless App</h4>
            <p>Create an API Gateway REST API and a static website that consumes that API.</p>
            <div class="flex flex-grow items-end">
                <a data-track="aws-serverless" href="{{< relref "/templates/serverless-application/aws" >}}" class="btn btn-secondary">Get Started</a>
            </div>
        </div>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-tasks text-blue-400 pr-2"></i>Containers with Fargate</h4>
            <p>Run your container on AWS using ECS and Fargate.</p>
            <div class="flex flex-grow items-end">
                <a data-track="aws-container-service" href="{{< relref "/templates/container-service/aws" >}}" class="btn btn-secondary">Get Started</a>
            </div>
        </div>
    </div>
</div>

{{< /choosable >}}

{{% choosable cloud azure %}}

<div class="tiles flex-wrap justify-center items-stretch mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-folder text-blue-400 pr-2"></i>Starter App</h4>
            <p>If you are new to Pulumi, this guide helps you install Pulumi, configure Azure, and run your first update.</p>
            <div class="flex flex-grow items-end">
                <a data-track="azure-get-started" href="{{< relref "/docs/get-started/azure" >}}" class="btn btn-primary">Get Started</a>
            </div>
        </div>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-cloud text-blue-400 pr-2"></i>Static Website with a CDN</h4>
            <p>Create a static website with a Blob storage and a CDN to serve the website with caching and HTTPs.</p>
            <div class="flex flex-grow items-end">
                <a data-track="azure-static-website" href="{{< relref "/templates/static-website/azure" >}}" class="btn btn-secondary">Get Started</a>
            </div>
        </div>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-sitemap text-blue-400 pr-2"></i>Full Stack Serverless App</h4>
            <p>Create a Function App and a static website that consumes that Function.</p>
            <div class="flex flex-grow items-end">
                <a data-track="azure-serverless" href="{{< relref "/templates/serverless-application/azure" >}}" class="btn btn-secondary">Get Started</a>
            </div>
        </div>
    </div>
    <!--<div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-cubes text-blue-400 pr-2"></i>Kubernetes on Azure</h4>
            <p>Coming soon! In the meantime you can select the link below to view a full list of Azure examples.</p>
            <div class="flex flex-grow items-end">
                <a data-track="azure-kubernetes-examples" href="https://github.com/pulumi/examples#azure" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">View examples</a>
            </div>
        </div>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-tasks text-blue-400 pr-2"></i>Containers on Azure</h4>
            <p>Coming soon! In the meantime you can select the link below to view a full list of Azure examples.</p>
            <div class="flex flex-grow items-end">
                <a data-track="azure-container-examples" href="https://github.com/pulumi/examples#azure" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">View examples</a>
            </div>
        </div>
    </div>-->
</div>

{{< /choosable >}}

{{% choosable cloud gcp %}}

<div class="tiles flex-wrap justify-center items-stretch mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-folder text-blue-400 pr-2"></i>Starter App</h4>
            <p>If you are new to Pulumi, this guide helps you install Pulumi, configure Google Cloud, and run your first update.</p>
            <div class="flex flex-grow items-end">
                <a data-track="google-get-started" href="{{< relref "/docs/get-started/gcp" >}}" class="btn btn-primary">Get Started</a>
            </div>
        </div>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-cloud text-blue-400 pr-2"></i>Static Website with a CDN</h4>
            <p>Create a static website with a Cloud Storage bucket and a CDN to serve the website with caching and HTTPs.</p>
            <div class="flex flex-grow items-end">
                <a data-track="google-static-website" href="{{< relref "/templates/static-website/gcp" >}}" class="btn btn-secondary">Get Started</a>
            </div>
        </div>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-sitemap text-blue-400 pr-2"></i>Full Stack Serverless App</h4>
            <p>Create a Cloud Function and a static website that consumes that function.</p>
            <div class="flex flex-grow items-end">
                <a data-track="google-serverless" href="{{< relref "/templates/serverless-application/gcp" >}}" class="btn btn-secondary">Get Started</a>
            </div>
        </div>
    </div>
    <!--<div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-cubes text-blue-400 pr-2"></i>Kubernetes on Google Cloud</h4>
            <p>Coming soon! In the meantime you can select the link below to view a full list of Google Cloud examples.</p>
            <div class="flex flex-grow items-end">
                <a data-track="google-kubernetes-examples" href="https://github.com/pulumi/examples#gcp" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">View examples</a>
            </div>
        </div>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-tasks text-blue-400 pr-2"></i>Containers on Google Cloud</h4>
            <p>Coming soon! In the meantime you can select the link below to view a full list of Google Cloud examples.</p>
            <div class="flex flex-grow items-end">
                <a data-track="google-container-examples" href="https://github.com/pulumi/examples#gcp" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">View examples</a>
            </div>
        </div>
    </div>-->
</div>

{{< /choosable >}}

{{% choosable cloud kubernetes %}}

<div class="tiles flex-wrap justify-center items-stretch mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-folder text-blue-400 pr-2"></i>Starter App</h4>
            <p>If you are new to Pulumi, this guide helps you install Pulumi, configure the Kubernetes Provider, and run your first update.</p>
            <div class="flex flex-grow items-end">
                <a data-track="kubernetes-get-started" href="{{< relref "/docs/get-started/kubernetes" >}}" class="btn btn-primary">Get Started</a>
            </div>
        </div>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-cubes text-blue-400 pr-2"></i>Kubernetes with EKS</h4>
            <p>Create an EKS cluster that provides a managed Kubernetes control plane.</p>
            <div class="flex flex-grow items-end">
                <a data-track="kubernetes-aws" href="{{< relref "/templates/kubernetes/aws" >}}" class="btn btn-secondary">Get Started</a>
            </div>
        </div>
    </div>
    <!--<div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-cubes text-blue-400 pr-2"></i>Kubernetes on Azure</h4>
            <p>Coming soon! In the meantime you can select the link below to view a full list of Kubernetes examples.</p>
            <div class="flex flex-grow items-end">
                <a data-track="kubernetes-azure-examples" href="https://github.com/pulumi/examples#kubernetes" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">View examples</a>
            </div>
        </div>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col">
            <h4><i class="fas fa-cubes text-blue-400 pr-2"></i>Kubernetes on Google Cloud</h4>
            <p>Coming soon! In the meantime you can select the link below to view a full list of Kubernetes examples.</p>
            <div class="flex flex-grow items-end">
                <a data-track="kubernetes-google-examples" href="https://github.com/pulumi/examples#kubernetes" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">View examples</a>
            </div>
        </div>
    </div>-->
</div>

{{< /choosable >}}

Or, watch how to do it in this video walkthrough:

<div class="rounded-md shadow border border-gray-300 w-3/4" style="position: relative; padding-bottom: 40.25%; height: 0; overflow: hidden;">
    <iframe
        src="//www.youtube.com/embed/6f8KF6UGN7g?rel=0"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;"
        allowfullscreen=""
        title="Introduction to Pulumi: Modern Infrastructure as Code"
        srcdoc="<style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img{position:absolute;width:100%;top:0;bottom:0;margin:auto}</style><a href=https://www.youtube.com/embed/6f8KF6UGN7g?autoplay=1><img src='/images/home/youtube-preview.svg' alt='Introduction to Pulumi: Modern Infrastructure as Code'></a>">
    </iframe>
</div>

See [Registry]({{< relref "/registry" >}}) on how to use other supported clouds.

## Pulumi Service

The Pulumi Service is a fully managed service that helps you adopt Pulumi’s open source SDK with ease. It provides built-in state and secrets management, integrates with source control and CI/CD, and offers a web console and API that make it easier to visualize and manage infrastructure. It is free for individual use, with features available for teams.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Create an Account</a>

## Additional resources

The following sections are also useful when first learning how to use Pulumi:

<div class="md:flex flex-row mt-6 mb-6">
    <div class="md:w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/intro/concepts" >}}"><i class="fas fa-file-alt pr-2"></i>Architecture & Concepts</a></h3>
        <p>Get details on the Pulumi programming model and core concepts.</p>
    </div>
    <div class="md:w-1/2 md:ml-4 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/docs/guides/adopting" >}}"><i class="fas fa-cloud pr-2"></i>Adopting Pulumi</a></h3>
        <p>Learn how to support, migrate, or convert existing cloud infrastructure with Pulumi.</p>
    </div>
</div>

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-full border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "/resources/introduction-to-pulumi" >}}"><i class="fas fa-users pr-2"></i>Live Workshops</a></h3>
        <p>Deploy your first Pulumi program in a live, instructor-led event.</p>
    </div>
</div>
