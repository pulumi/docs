---
title: "Azure NextGen Tutorials"
meta_desc: A collection of tutorials that highlight complete end-to-end scenarios when
           using the Azure platform and the Azure NextGen provider.
linktitle: "Azure NextGen"
menu:
  userguides:
    parent: tutorials
    identifier: tutorials-azure-nextgen
    weight: 2

---

The following tutorials highlight the Azure platform using complete end-to-end scenarios.

> If this is your first time getting started with Pulumi for Azure, try the
> easy <a href="{{< relref "/docs/get-started/azure" >}}">Get Started guide</a> first.

## Featured Tutorials

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-boxes pr-2"></i>
            <a href="{{< relref "azure-nextgen-cs-aci" >}}" style="color: #4387c7">
                Azure Container Instances
            </a>
        </h3>
        <p>
            Deploy a containerized web server using Azure Container Instances.
        </p>
        <p>
            <a href="{{< relref "azure-nextgen-cs-aci" >}}" style="color: #4387c7">
                C#
            </a>&bull;
            <a href="{{< relref "azure-nextgen-ts-aci" >}}" style="color: #4387c7">
                TypeScript
            </a>&bull;
            <a href="{{< relref "azure-nextgen-py-aci" >}}" style="color: #4387c7">
                Python
            </a>&bull;
            <a href="{{< relref "azure-nextgen-go-aci" >}}" style="color: #4387c7">
                Go
            </a>
        </p>
    </div>
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-globe pr-2"></i>
            <a href="{{< relref "azure-nextgen-cs-aks" >}}" style="color: #4387c7">
                Azure Kubernetes Service
            </a>
        </h3>
        <p>
            Deploy an AKS cluster and set credentials to manage access to the cluster.
        </p>
        <p>
            <a href="{{< relref "azure-nextgen-cs-aks" >}}" style="color: #4387c7">
                C#
            </a>&bull;
            <a href="{{< relref "azure-nextgen-ts-aks" >}}" style="color: #4387c7">
                TypeScript
            </a>&bull;
            <a href="{{< relref "azure-nextgen-py-aks" >}}" style="color: #4387c7">
                Python
            </a>&bull;
            <a href="{{< relref "azure-nextgen-go-aks" >}}" style="color: #4387c7">
                Go
            </a>
        </p>
    </div>
</div>

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-boxes pr-2"></i>
            <a href="{{< relref "azure-nextgen-cs-appservice-docker" >}}" style="color: #4387c7">
                Azure App Service
            </a>
        </h3>
        <p>
            Build and deploy a containerized application
            using Azure Container Registry and Azure App Service.
        </p>
        <p>
            <a href="{{< relref "azure-nextgen-cs-appservice-docker" >}}" style="color: #4387c7">
                C#
            </a>&bull;
            <a href="{{< relref "azure-nextgen-ts-appservice-docker" >}}" style="color: #4387c7">
                TypeScript
            </a>&bull;
            <a href="{{< relref "azure-nextgen-py-appservice-docker" >}}" style="color: #4387c7">
                Python
            </a>&bull;
            <a href="{{< relref "azure-nextgen-go-appservice-docker" >}}" style="color: #4387c7">
                Go
            </a>
        </p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-server pr-2"></i>
            <a href="{{< relref "azure-nextgen-ts-webserver" >}}" style="color: #4387c7">
                Azure Virtual Machine
            </a>
        </h3>
        <p>
            Provision a Linux web server VM with a public IP address.
        </p>
        <p>
            <a href="{{< relref "azure-nextgen-ts-webserver" >}}" style="color: #4387c7">
                TypeScript
            </a>&bull;
            <a href="{{< relref "azure-nextgen-py-webserver" >}}" style="color: #4387c7">
                Python
            </a>&bull;
    </div>
</div>

## Other Examples and Tutorials

{{< chooser language "typescript,python,go,csharp" / >}}
{{< tutorials-index-azure-nextgen >}}

If you'd like to see a new tutorial, please [request one](
https://github.com/pulumi/docs/issues/new?title=New%20Azure%20NextGen%20Tutorial%20Request).
Pull requests are also welcome!
