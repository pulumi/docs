---
title: Tutorials
meta_desc: A collection of tutorials for interacting and deploying resources
           to different cloud providers.
menu:
  userguides:
    identifier: tutorials
    weight: 1

aliases: ["/docs/reference/tutorials/"]
---

Please select from the following cloud providers or tutorials:

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <p>
            <a href="{{< prelref "aws" >}}"><img class="h-10" src="/logos/tech/aws.svg" alt="AWS"></a>
        </p>
        <ul class="p2 ml-2">
            <li><a href="{{< prelref "aws/ec2-webserver" >}}">EC2 Virtual Machine</a></li>
            <li><a href="{{< prelref "aws/ecs-fargate" >}}">ECS Fargate Containers</a></li>
            <li><a href="{{< prelref "aws/rest-api" >}}">API Gateway and Lambda</a></li>
            <li><a href="{{< prelref "aws/s3-website" >}}">S3 Static Website</a></li>
        </ul>
        <p class="mt-6">
            <a class="btn btn-secondary" href="{{< prelref "aws" >}}">VIEW MORE</a>
        </p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <p>
            <a href="{{< prelref "azure" >}}"><img class="h-10" src="/logos/tech/azure.svg" alt="Azure"></a>
        </p>
        <ul class="p2 ml-2">
            <li><a href="{{< prelref "azure/container-webserver" >}}">Azure Container Instances</a></li>
            <li><a href="{{< prelref "azure/azure-ts-webserver" >}}">Azure Virtual Machine</a></li>
            <li><a href="{{< prelref "azure/azure-ts-serverless-url-shortener-global" >}}">CosmosDB and Functions</a></li>
            <li><a href="{{< prelref "azure/azure-ts-appservice-springboot" >}}">Azure App Service</a></li>
        </ul>
        <p class="mt-6">
            <a class="btn btn-secondary" href="{{< prelref "azure" >}}">VIEW MORE</a>
        </p>
    </div>
</div>

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <p>
            <a href="{{< prelref "gcp" >}}"><img class="h-10" src="/logos/tech/gcp.svg" alt="Google Cloud"></a>
        </p>
        <ul class="p2 ml-2">
            <li><a href="{{< prelref "gcp/gce-webserver" >}}">GCE Virtual Machine</a></li>
            <li><a href="{{< prelref "kubernetes/gke" >}}">GKE Cluster</a></li>
            <li><a href="{{< prelref "gcp/gcp-ts-functions" >}}">Google Functions</a></li>
            <li><a href="{{< prelref "gcp/gcp-ts-k8s-ruby-on-rails-postgresql" >}}">Containerized App</a></li>
        </ul>
        <p class="mt-6">
            <a class="btn btn-secondary" href="{{< prelref "gcp" >}}">VIEW MORE</a>
        </p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <p>
            <a href="{{< prelref "kubernetes" >}}"><img class="h-10" src="/logos/tech/k8s.svg" alt="Kubernetes"></a>
        </p>
        <ul class="p2 ml-2">
            <li>
                <a href="{{< prelref "kubernetes/aks" >}}">AKS</a>,
                <a href="{{< prelref "kubernetes/eks" >}}">EKS</a>,
                or <a href="{{< prelref "kubernetes/gke" >}}">GKE</a>
            </li>
            <li><a href="{{< prelref "kubernetes/exposed-deployment" >}}">Hello, World</a></li>
            <li><a href="{{< prelref "kubernetes/wordpress-chart" >}}">Helm Charts</a></li>
            <li><a href="{{< prelref "kubernetes/guestbook" >}}">Guestbook App</a></li>
        </ul>
        <p class="mt-6">
            <a class="btn btn-secondary" href="{{< prelref "kubernetes" >}}">VIEW MORE</a>
        </p>
    </div>
</div>
