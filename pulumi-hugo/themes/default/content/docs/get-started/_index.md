---
title: Get Started
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
---

Pulumi is a modern [infrastructure as code]({{< relref "/what-is/what-is-infrastructure-as-code" >}}) platform that allows you to use familiar programming languages and tools to build, deploy, and manage cloud infrastructure.

Select one of the following options to deploy a simple application in your cloud using Pulumi:

<div class="tiles flex-wrap mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a class="tile p-8" href="{{< relref "/docs/get-started/aws" >}}">
            <img class="h-10 mx-auto" src="/logos/tech/aws.svg" alt="AWS">
        </a>
    </div>
    <div class="pb-4 md:w-1/2">
        <a class="tile p-8" href="{{< relref "/docs/get-started/kubernetes" >}}">
            <img class="h-10 mx-auto" src="/logos/tech/k8s.svg" alt="Kubernetes">
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a class="tile p-8" href="{{< relref "/docs/get-started/azure" >}}">
            <img class="h-10 mx-auto" src="/logos/tech/azure.svg" alt="Azure">
        </a>
    </div>
    <div class="pb-4 md:w-1/2">
        <a class="tile p-8" href="{{< relref "/docs/get-started/gcp" >}}">
            <img class="h-10 mx-auto" src="/logos/tech/gcp.svg" alt="Google Cloud">
        </a>
    </div>
</div>

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
