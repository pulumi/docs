---
title: "Top 5 Things an Azure Developer Needs to Know: Kubernetes Applications"
date: 2021-08-16
allow_long_title: True
meta_desc: "Deploying applications on Azure Kubernetes Service (AKS) with the Azure CLI and Infrastructure as Code."
meta_image: azure-top-5.png
authors:
    - sophia-parafina
tags:
    - kubernetes
    - Azure
    - helm

---

All modern software is cloud software, and it's more than likely that it runs on Kubernetes. Developers are faced with the challenge of deploy applications composed of many microservices. And each microservice adds to the complexity of the deployment.

This article reviews the different methods for deploying applications on Azure Kubernetes Service (AKS).

<!--more-->

## A quick review on application deployment

If you're not familiar with deploying applications on Kubernetes, these articles cover the basic and advance cases:

- [Getting Started With Kubernetes: Application Basics]({{< relref "/blog/getting-started-with-k8s-part2" >}})
- [Getting Started With Kubernetes: Advanced Deployment]({{< relref "/blog/getting-started-with-k8s-part3" >}})
- [Getting Started with Kubernetes: Stateful Applications]({{< relref "/blog/getting-started-with-k8s-part4" >}})

## Setting up the AKS sandbox

We'll set up an AKS sandbox composed of an AKS cluster and Azure Container Registry (ACR) for this article. Make sure you have the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed, and you're logged into Azure, e.g., `az login`.

### Create a container registry

We'll create a resource group first, followed by the registry.

```bash
$ az group create --resource-group aks-group --location westus2
$ az acr create --resource-group aks-group   --name pulumipusContainerRegistry --sku Basic
```

When the registry is created, the Azure CLI returns JSON with metadata about the registry. Under the `id` key, you'll find the URL to the login server.

```text
...
  "id": "/subscriptions/fceb55a3-db15-4f3a-bffa-81271e7b7676/resourceGroups/myResourceGroup/providers/Microsoft.ContainerRegistry/registries/azContainerRegistryPulumi",
  "identity": null,
  "location": "eastus",
  "loginServer": "pulumipuscontainerregistry.azurecr.io",
  "name": "azContainerRegistryPulumi",
...
```

At this point, you can push and pull container images from your registry. If you want to try out the registry and push an image, you'll need [Docker installed](https://docs.docker.com/get-docker/). This example pulls an image from Docker Hub and tags it with the URL to the Azure container registry. We then log into the registry and push the image. To verify the image, we use the Azure CLI to list the images in the registry.

```bash
$ docker pull hello-world
$ docker tag hello-world pulumipuscontainerregistry.azurecr.io/hello-world:v1
$ az acr login --name pulumipusContainerRegistry
$ docker push  pulumipuscontainerregistry.azurecr.io/hello-world:v1
$ az acr repository list --name pulumipusContainerRegistry
[
  "hello-world"
]
```

### Create an AKS cluster

The previous article this series demonstrated how to create an AKS cluster with the Azure portal and code to illustrate creating an AKS cluster. For this example, we'll use the CLI. In the example below, the first line creates a basic cluster, and the second line retrieves the cluster credentials that let us connect to it.

```bash
$ az aks create --resource-group aks-group --name aks-cluster --node-count 3 --generate-ssh-keys -s Standard_B2ms --disable-rbac
$ az aks get-credentials -g aks-group -n aks-cluster
```

## Deploy an NGINX container on AKS with Helm

[Helm](https://helm.sh/) is an application package manager for Kubernetes. Follow the directions on **helm.sh** to [install Helm](https://helm.sh/docs/intro/install/). Helm can install packages from repositories such as [ArtifactHUB](https://artifacthub.io/), [Bitnami](https://bitnami.com/), and the [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=helm%20charts).

First, we'll add the Azure Marketplace repository to helm and update it. Next, we install the NGINX helm chart to our AKS cluster.

```bash
$ helm repo add azure-marketplace https://marketplace.azurecr.io/helm/v1/repo
$ helm repo update
$ helm install my-release azure-marketplace/nginx
NAME: my-release
LAST DEPLOYED: Mon Aug 16 13:58:26 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
The NGINX Ingress Controller has been installed.
```

To find the URL for our NGINX deployment, use `kubectl` to get the external IP address.

```bash
$ kubectl get service
NAME               TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes         ClusterIP      10.0.0.1       <none>        443/TCP        3h21m
my-release-nginx   LoadBalancer   10.0.212.197   20.72.78.59   80:31251/TCP   175m
```

## Deploy a custom container

In the previous section, we used a Helm chart to deploy an application from a repository. But what if we want to deploy our custom application. In this example, we'll build our NGINX container, push it to our registry, and deploy it on the AKS cluster.

### Create our application container

For this example, you will need Docker. We will replace the default NGINX page with our welcome page. Copy the sample below and save it as `index.html`.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AKS NGINX</title>
</head>
<body>
  <h2>Hello from Azure AKS</h2>
</body>
</html>
```

Next, we'll make a Dockerfile to build our custom NGINX container. Copy and save the following to a file called Dockerfile.

```dockerfile
FROM nginx:latest
COPY ./index.html /usr/share/nginx/html/index.html
```

Build and tag the image with this command and push it to the repository we created earlier.

```bash
$ docker build -t pulumipuscontainerregistry.azurecr.io/my-nginx:v1
$ az acr login --name pulumipusContainerRegistry
$ docker push pulumipuscontainerregistry.azurecr.io/my-nginx:v1
```

### Create a deployment manifest

In the previous example, we deployed NGINX with Helm. Manifests are another way to deploy applications. A manifest contains a `deployment` that defines [`pods`]({{< relref "/blog/getting-started-with-k8s-part2#pods" >}}) that run a containerized application. It also contains [`services`]({{< relref "/blog/getting-started-with-k8s-part2#services" >}}) that route traffic to `pods`.

Copy and save the example below to a file named `manifest.yml`.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: my-nginx
  name: my-nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-nginx
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: my-nginx
    spec:
      containers:
      - image: pulumipuscontainerregistry.azurecr.io/my-nginx:v1
        name: my-nginx
        imagePullPolicy: Always
        resources: {}
        ports:
          - containerPort: 80
status: {}

---

apiVersion: v1
kind: Service
metadata:
  name: my-nginx
  labels:
    run: my-nginx
spec:
  ports:
  - port: 80
    protocol: TCP
  selector:
    app: my-nginx
  type: LoadBalancer
  ```

### Deploy the application to AKS

We'll use `kubectl` to deploy the application with the manifest. But before we can do this, we need to attach the ACR `pulumipuscontainerregistry` to the AKS cluster, `aks-cluster`. Once the registry is added to the cluster configuration, we can deploy our application with `kubectl`.

```bash
$ az aks update --resource-group aks-group --name aks-cluster --attach-acr pulumipuscontainerregistry
$ kubectl create -f manifest.yml
```

Use `kubectl get service` to get the load balancer's external IP as we did with the Helm example.

## Deploy with Pulumi

The [previous article]({{< relref "/blog/top-5-things-for-azure-devs-kubernetes-infrastructure" >}}) in this series showed how to deploy AKS with code. Starting with the [Python example](https://github.com/pulumi/examples/tree/master/azure-py-aks) from Github and add to it to create a complete solution

### Create a container registry and custom container

First, we create the image registry to hold our custom NGINX container. Put the `index.html` and the `Dockerfile` files in a directory called `app`. The `app` directory is the context Docker uses to build an image. Note that the Docker provider builds and pushes the image to our repository.

```python
# Create a private ACR registry.
rg = azure.core.ResourceGroup('azure-native-py-aks')
registry = azure.containerservice.Registry('pulumipuscontainerrepository',
    resource_group_name=rg.name,
    admin_enabled=True,
    sku='Basic'

# Get registry info (creds and endpoint).
image_name = "pulumipuscontainerrepository/my-nginx"
registry_info = docker.ImageRegistry(
    server=registry.login_server,
    username=registry.admin_username,
    password=registry.admin_password
)

import pulumi_docker as docker

# Build and publish the container image.
image = docker.Image('my-image',
    build='app',
    image_name=image_name,
    registry=registry_info,
)
```

### Deploy the container

The code below creates a Deployment and a LoadBalancer Service similar to the manifest we used earlier. The script exports the IP address of the LoadBalancer at the end of the script.

```python

# Create a NGINX Deployment
app_labels = { 'app': 'my-nginx' }
app_dep = k8s.apps.v1.Deployment('my-aks-deployment',
    spec={
        'selector': { 'matchLabels': app_labels },
        'replicas': 3,
        'template': {
            'metadata': { 'labels': app_labels },
            'spec': {
                'containers': [{
                    'name': 'pulumipuscontainerrepository/my-nginx',
                    'image': 'my-nginx;,
                    'ports': [
                        {
                            'name': 'http',
                            'containerPort': 80
                        }
                    ]
                }],
            },
        },
    },
)

# Create a Service
app_svc = k8s.core.v1.Service('my-aks-service',
    metadata={ 'labels': app_labels },
    spec={
        'type': 'LoadBalancer',
        'ports': [
            {
                'port': 80,
                'targetPort': 80,
                'protocol': 'TCP'
            }
        ],
        'selector': app_labels,
    }
)
pulumi.export('application IP', app_svc.status.apply(lambda status: status.loadbalancer.ingress[0].ip))
```

This example provides a sketch of the process to create an AKS cluster and deploy a custom container. For a fully worked example, check out the [`Azure Kubernetes Service (AKS) - Hello World!`]({{< relref "/registry/packages/kubernetes/how-to-guides/aks" >}}) tutorial.

## Summary

There are many ways to deploy applications on AKS, including  [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/) and [Kustomize](https://kustomize.io/) which were not discussed. We've covered deploying with Helm, manifests, and infrastructure as code. This article covers the basics of application deployment using Deployments and Services. To review, Deployments are declarative updates to a Pod such as specifying a container to run, and Services route traffic to Pods either within the cluster or permitting ingress with a LoadBalancer. We should note that templating methods such as Helm or manifests require file management, whereas using cloud engineering practices enables managing both infrastructure and application deployment in a versioned and repeatable way.

The following article will wrap up the series. We'll examine how to implement DevOps practices with Azure.
