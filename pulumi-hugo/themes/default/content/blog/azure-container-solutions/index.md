---
title: "Which Azure Container Solution is right for you?"
date: 2021-10-12T08:00:00-07:00
draft: false
meta_desc: "A look at the container solutions available in Azure"
meta_image: "azure-top-5.png"
authors:
    - lee-briggs
tags:
    - azure
    - containers
---

Containers have emerged as one of the de facto standards for running software. When adopted with the right mindset, they can drastically improve the development lifecycle and help to close the loop between local development and running your applications in the cloud.

If you're at the stage of trying to run your application in Microsoft Azure, the choices can be overwhelming. The Azure Container [product page](https://azure.microsoft.com/en-gb/product-categories/containers/) lists 7 different products on their landing page, and for new users it can often be difficult to decide which of the myriad products is right for their use case. What can make it even more confusing is that often these container services can be interoperable, meaning you can use one container product from another!

In this post, we're going to examine each of the main container services offered in Azure and then examine what they're good for and what they might not be so good for. Let's take a look!

<!--more-->

## Azure Container Instances

[Azure Container Instances](https://azure.microsoft.com/en-us/services/container-instances/) (ACI) bills itself as an offering that lets you "easily run containers on Azure without managing servers."

Launched in July 2017, it was arguably the first "serverless" container offering from the major cloud providers.

### What's good about it?

ACI is a Platform-as-a-Service (PaaS) type of product that is designed to remove the burden of launching and running containers.

#### Simplicity

Azure Container Instances has been designed from the ground up to be straightforward to use. It’s designed to get your container launched as quickly as possible, even including integrations with many of the tools you’re probably already familiar with if you’re using containers. One example is the integration with the [Docker CLI](https://docs.microsoft.com/en-gb/azure/container-instances/quickstart-docker-cli).

In many cases, the only configuration options you need to pass to your ACI provisioning mechanism is the image you’re running and some sizing decisions, like how many CPUs and how much memory you need. There is some flexibility in this decision process, but having fewer required options means you’re not bogged down with complex architectural decisions when trying to get your container running.

This lends itself particularly well to web server projects, especially at smaller scales. You can launch applications very quickly and easily by specifying the image you've built, and your application can be running in very short order.

#### Start-Up Times

ACI Containers start fast&mdash;often in a matter of seconds. This speed really helps the developer lifecycle and helps to create productivity when you're developing your application.

#### Pricing

ACI will only bill you for the time your applications are running. It offers no start-up costs (which goes great with the fast start times!) and per-second billing, meaning you only pay for every second the application is actually up. The pricing is also extremely competitive against other cloud providers.

#### The Other Stuff

From a security perspective, ACI separates your container from others running in the same environment, meaning your application will have the same level of security as if it was running on a different virtual machine. This separation really helps to provide peace of mind and is yet another benefit of the serverless model&mdash;less infrastructure means less worries.

As expected from Microsoft, ACI has excellent support for Windows containers and .NET platform applications, which is lacking around other cloud providers. If you need to run Windows containers, this support is a huge benefit.

### What's not great about it?

#### Scaling

ACI supports customizing the amount of resources you can assign to a container, but it will only run one copy. There’s no horizontal scaling available, so if you need more resources, you only have one option: scaling vertically. It is possible to run N number of ACI instances and configuring load balancers across them, but it's a very manual process and can be awkward to manage and scale successfully.

If you’re running a webserver application, horizontal scaling behind a load balancer might be a better option, so this lack of scaling flexibility and manual processing can be a real shortcoming.

In addition to this opinionated scaling mechanism, there’s also no auto scaling option for ACI. If you’re finding that you’re hitting the limits of your ACI deployment, you’ll need to manually scale the service.

#### Configuration

ACI has some configuration options missing, which you’d expect would be there from the beginning. One glaring omission is port mapping (for example mapping public port 80 to container port 8080). This omission can mean modifying your container just to get it running in ACI.

ACI’s opinionated architecture seems to have been designed for ease-of-use, which often means more complex workloads just aren’t possible. If you have some unique configuration options, like needing access to privileged container options or complex network requirements, ACI might not be able to support you.

### What we’d use it for

The lack of flexibility in ACI means that some workloads just aren’t able to run there. If you have full control over the container images you’re building and if you just want to get off the ground quickly with minimal fuss and configuration, ACI is a great choice.

Applications with smaller and more predictable usage patterns are a great use case for ACI. The lack of horizontal scaling could be seen as a negative, but from another perspective, it means the use case is straightforward and simple. If you just want to get your application into the hands of your users and think you can accurately predict your usage patterns, choose ACI.

## Azure App Service

Azure App Service is a more fully-featured offering for hosting applications, focusing more on WebApps and API services. It started life as several differing offerings (Azure Websites, Azure Mobile Service, and Azure BizTalk) before being bundled into a single service in March 2015. Its origins as multiple solutions means it has developed tight integrations with other Azure solutions and offers many value-add features depending on your use case.

Because of the myriad features Azure App Service offers, running containers is only a small part of what you can do with it.

With that in mind, let's take a look at where it shines with regard to running containers.

### What’s it good for?

Azure App Services is designed to be a one-stop shop for your web application needs, so it's highly opinionated and pushes you in a certain direction.

#### Integrations

Azure App Service has many integrations with Azure. As an example, if you need to add a CDN to your web service, it’s extremely straightforward to do so with Azure CDN.

This tight integration with Azure’s many other services makes it likely to meet the needs of your application and extend it as needed, introducing common architecture components like message queues and databases. This is particularly useful when it comes to the integration with Azure's networking model. You can run an Azure App Service inside an [Azure Virtual Network](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) which is extremely useful in many scenarios where network separation is needed, like enterprise applications.

#### Scaling & Availability

Azure App Service has a myriad of available scaling capabilities built out of the box. Not only can you scale the actual container you’ve deployed (while also simultaneously placing pricing caps on your service), but you can also scale related resources if necessary, which fits well with the tight integration we mentioned previously.

App service scaling for your container can either scale up (i.e., increase the amount of resources associated with your container) or scale out (ie: have more containers behind your load balancer).

This flexibility in scaling means you can be safe to assume your application will meet spiking traffic requirements and service your users’ needs.

### What’s not great about it?

#### Opinionated

Azure App Service is highly opinionated. Its tight integrations with other Azure services mean that you're expected to follow established patterns for achieving your goals.

This opinionated implementation means that the initial learning curve can be steep. The origins of app services means the product has grown in complexity along with its opinionated implementation, and as a result it can be overwhelming when getting started.

In addition to the learning curve, App Service is primarily focused towards web app workloads, and support for running other applications is limited at best.

### What we’d use it for

The scaling options available to App Service means that it’s extremely well positioned to handle your large scale, fluctuating web applications. If you expect to have traffic spikes during peak hours, you can configure App Service to scale relatively easily in a manner that suits your budget and needs.

## Azure Kubernetes Service

Azure Kubernetes Service (AKS) is Azure's managed Kubernetes offering, which has been available since October 2017.

Azure was very quick to market with its Kubernetes offering and hired several prominent Kubernetes engineers like Brendan Burns to head up the engineering departments building the service.

Kubernetes is a very fully featured product, and AKS is a very conformant implementation of Kubernetes. Therefore, a lot of our good and bad considerations next will be an evaluation of Kubernetes, as well as AKS.

### What’s it good for?

#### Extensibility

Kubernetes is incredibly feature rich. Out of the box with AKS, you’ll get application self-healing capabilities via the mechanism of reconcile loops built into Kubernetes, the ability to run different types of workload via native Kubernetes resources such as StatefulSets, Deployments and Jobs, and a large amount of extensibility via Kubernetes’ Custom Resource Definitions capability.

#### Familiarity

Kubernetes also offers a familiar API regardless of the cloud provider you’re working with. If you’re new to AKS, but have used a managed Kubernetes service from another cloud provider, you might find it relatively easy to get your container up and running in AKS.

### What’s not great about it?

#### Complexity

Kubernetes has a steep learning curve, and AKS is no exception. A lot of the knowledge needed to run and operate Kubernetes is handled by AKS itself, but you still have to have an in-depth understanding of how Kubernetes works to get your container running.

In addition, the specification for a simple Kubernetes job can often be hundreds of lines of code. You have to learn not only how to run the container but also understand how Kubernetes exposes services to the world.

### What we’d use it for

The flexibility and extensibility offered by Kubernetes as a platform means it’s possible to run many types of workloads. Large companies have battle-tested Kubernetes (and by extension, AKS), running everything from web applications to machine learning.

If you're able to invest time into learning and understanding the ecosystem and can dedicate people to maintaining and managing your Kubernetes implementation, AKS is a fantastic option for almost any workload you might consider.

## Everything Else

### Azure Red Hat OpenShift

Azure Red Hat OpenShift is an enterprise grade implementation of Kubernetes developed by Red Hat. OpenShift builds on Kubernetes by adding support, enterprise-grade security, and Platform-as-a-Service integrations.

If the idea of using Kubernetes for your container solutions seems appealing but you need service level agreements (SLAs) around support and integrations, Azure’s Red Hat OpenShift solution is a great option.

### Azure Service Fabric

Azure Service Fabric is a container service focused on distributed applications, like microservice architectures or complex distributed compute environments.

If you’re planning on running a complex architecture, Azure Service Fabric can be a great fit. It provides more orchestration capabilities than Azure App Service. Service Fabric can also extend outside Azure's cloud into your on-premise data center if necessary.

If your application has needs related to low latency, especially across distributed regions, Service Fabric is a great fit.

However, Azure Service Fabric can be extremely difficult to use. It is only targeted towards distributed, complex systems - if you're not planning on building one of those, it's probably not the correct choice.

### Azure Batch

Azure Batch is a service focused on High Performance Compute (HPC) workloads. These workloads can often scale horizontally to thousands of processes and can be difficult to orchestrate.

Azure Batch makes this process simpler by providing a managed service to handle the difficult processes.

If you’re planning on passing large amounts of data to your application via a queuing mechanism and having that data processed very quickly, Azure Batch is definitely a service you should consider.

### Azure Functions

Azure Functions is Azure’s Function-as-a-Service implementation. It supports launching “function apps” inside containers as a deployment mechanism.

Function-as-a-Service products are often designed for short-lived, event-driven workloads. If you need to run a script to react to a worker queue or other event, Azure Functions are a great option. It's important to remember that Functions are often billed based on how long they run, so short-lived workloads are often better suited.

## Wrap-Up

There are a number of options for running containers in Azure, and choosing the right one for your workload might be difficult. We've tried to give an overview of the current state of the world, but Microsoft continues to add options and capabilities to all these products.

If you’ve settled on a container solution, and are ready to get started, Pulumi’s [Azure Native provider]({{< relref "/registry/packages/azure-native" >}}) supports all of the methods of running containers and can quickly get you started. Check out our [Azure  getting started guide]({{< relref "/docs/get-started/azure" >}}), or join one of our upcoming [Azure Workshops]({{< relref "/resources" >}})!
