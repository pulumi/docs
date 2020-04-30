---
title: Kubernetes Tutorials
meta_desc: A collection of tutorails for learning basic and advanced techniques for Kubernetes. Choose
           from basic provisioning to complex Day 2 tasks.
linktitle: "Kubernetes"
menu:
  userguides:
    parent: tutorials
    identifier: tutorials-kubernetes

aliases: ["/docs/reference/tutorials/kubernetes/"]
---

The following tutorials highlight the Kubernetes platform using complete end-to-end scenarios.

> If this is your first time getting started with Pulumi for Kubernetes, try the
> easy <a href="{{< prelref "/docs/get-started/kubernetes" >}}">Get Started guide</a> first.

## Featured Tutorials

Tutorials are available for a number of Kubernetes tasks:

* [Clusters](#clusters) - provisioning a new Kubernetes cluster
* [Workloads](#workloads) - effectively running applications
* [Day Two Tasks](#day-two-tasks) - complex tasks for managing existing Kubernetes environments

### Clusters

These tutorials will help you provision a Kubernetes cluster on your cloud of choice:

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/3 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <a href="{{< prelref "aks" >}}" style="color: #4387c7">
                <img class="h-5" src="/logos/tech/azure.svg" alt="Azure">
                AKS
            </a>
        </h3>
    </div>
    <div class="w-1/3 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <a href="{{< prelref "eks" >}}" style="color: #4387c7">
                <img class="h-5" src="/logos/tech/aws.svg" alt="AWS">
                EKS
            </a>
        </h3>
    </div>
    <div class="w-1/3 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <a href="{{< prelref "gke" >}}" style="color: #4387c7">
                <img class="h-5" src="/logos/tech/gcp.svg" alt="GCP">
                GKE
            </a>
        </h3>
    </div>
</div>

### Workloads

These tutorials deploy application workloads to any Kubernetes cluster, managed or self-managed:

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-boxes pr-2"></i>
            <a href="{{< prelref "exposed-deployment" >}}" style="color: #4387c7">
                Hello, World
            </a>
        </h3>
        <p>
            Deploy an Nginx web server to Kubernetes and expose it to
            the Internet with a public IP address.
        </p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-map pr-2"></i>
            <a href="{{< prelref "wordpress-chart" >}}" style="color: #4387c7">
                Helm Charts
            </a>
        </h3>
        <p>
            Deploy the WordPress Helm Chart to your cluster.
        </p>
    </div>
</div>

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-book pr-2"></i>
            <a href="{{< prelref "guestbook" >}}" style="color: #4387c7">
                Guestbook App
            </a>
        </h3>
        <p>
            Deploy a multi-service, load balanced Guestbook application
            using Redis and Nginx.
        </p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-spinner pr-2"></i>
            <a href="{{< prelref "configmap-rollout" >}}" style="color: #4387c7">
                Graceful App Rollout
            </a>
        </h3>
        <p>
            Deploy an application, perform a cascading update,
            and monitor deployment progress visually as it occurs.
        </p>
    </div>
</div>

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-bolt pr-2"></i>
            <a href="{{< prelref "stateless-app" >}}" style="color: #4387c7">
                Stateless Application
            </a>
        </h3>
        <p>
            Deploy a stateless application using a Kubernetes Deployment,
            and then dynamically scale it out.
        </p>
    </div>
</div>

### Day Two Tasks

These tutorials tackle difficult "day two" tasks:

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-signal pr-2"></i>
            <a href="{{< prelref "p8s-rollout" >}}" style="color: #4387c7">
                Gated Rollouts
            </a>
        </h3>
        <p>
            Stage a rollout from a 3-replica canary to 10-replica
            staging environment, gating progress on Prometheus health checks.
        </p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4">
            <i class="fas fa-stopwatch pr-2"></i>
            <a href="{{< prelref "eks-migrate-nodegroups" >}}" style="color: #4387c7">
                Zero Downtime Upgrades
            </a>
        </h3>
        <p>
            See how to migrate workloads using node groups in an EKS cluster
            to accomplish zero downtime upgrades.
        </p>
    </div>
</div>

## Other Examples and Tutorials

{{< chooser language "javascript,typescript,python" / >}}
{{< tutorials-index-kubernetes >}}

If you'd like to see a new tutorial, please [request one](
https://github.com/pulumi/docs/issues/new?title=New%20Kubernetes%20Tutorial%20Request).
Pull requests are also welcome!
