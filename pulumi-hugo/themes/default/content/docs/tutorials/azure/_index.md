---
title: "Azure Tutorials"
meta_desc: A collection of tutorials that highlight complete end-to-end scenarios when
           using the Azure platform.
linktitle: "Azure"
menu:
  userguides:
    parent: tutorials
    identifier: tutorials-azure

aliases: ["/docs/reference/tutorials/azure/"]
---

The following tutorials highlight the Azure platform using complete end-to-end scenarios.

> If this is your first time getting started with Pulumi for Azure, try the
> easy <a href="{{< relref "/docs/get-started/azure" >}}">Get Started guide</a> first.
>
> If you are looking to use Kubernetes on Azure, see [the AKS tutorial]({{< relref "../kubernetes/aks" >}}).

## Featured Tutorials

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-boxes pr-2"></i>
            <a href="{{< relref "container-webserver" >}}" style="color: #4387c7">
                Azure Container Instances
            </a>
        </h3>
        <p>
            Deploy a containerized web server using Azure Container Instances.
        </p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-server pr-2"></i>
            <a href="{{< relref "azure-ts-webserver" >}}" style="color: #4387c7">
                Azure Virtual Machine
            </a>
        </h3>
        <p>
            Provision a Linux web server VM with a public IP address.
        </p>
    </div>
</div>

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-globe pr-2"></i>
            <a href="{{< relref "azure-ts-serverless-url-shortener-global" >}}" style="color: #4387c7">
                CosmosDB and Functions
            </a>
        </h3>
        <p>
            Create a globally distributed serverless application using
            CosmosDB for storage and Azure Functions for compute.
        </p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-boxes pr-2"></i>
            <a href="{{< relref "azure-ts-appservice-springboot" >}}" style="color: #4387c7">
                Azure App Service
            </a>
        </h3>
        <p>
            Build and deploy a containerized Java Spring Boot application
            using Azure Container Registry and Azure App Service.
        </p>
    </div>
</div>

## Other Examples and Tutorials

{{< chooser language "javascript,typescript,python" / >}}
{{< tutorials-index-azure >}}

If you'd like to see a new tutorial, please [request one](
https://github.com/pulumi/docs/issues/new?title=New%20Azure%20Tutorial%20Request).
Pull requests are also welcome!
