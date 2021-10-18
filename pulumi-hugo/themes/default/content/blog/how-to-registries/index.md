---
title: "How to Build a Container Registry"
date: 2021-02-16
meta_desc: "How to build a registry and push Docker images with code."
meta_image: registry.png
authors:
    - sophia-parafina
tags:
    - containers
    - docker
---

Whether you are working with Kubernetes or serverless, your application uses containers. If you use the Docker desktop client, images are pushed to Docker Hub by default. Pulling images from Docker Hub is convenient, but there are many reasons to store images in your own registry. For example, Docker Hub doesn’t guarantee to produce the same image on repeated pulls, i.e., your base image might have changed. It’s also possible to inadvertently expose secrets in an intermediate image used to build the image stored on Docker Hub. There is also the possibility of vulnerabilities in even official images. This article shows how to create a repository and how to build and push images to that repository

<!--more-->

## Container registry offerings

AWS provides the [Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/), Azure has [Container Registry](https://azure.microsoft.com/en-us/services/container-registry/), and Google has it’s [Container Registry](https://cloud.google.com/container-registry). Each provider has associated services unique to their offering, but all support Docker or OCI compliant images.

## Build it

Let’s examine how to create a registry with the provider of your choice. In these examples, we create a registry, build a Docker image, and push the image to the registry. The [application](https://github.com/pulumi/examples/tree/master/aws-ts-containers/app) used for the image is NGINX.

Choose your cloud provider to learn how to build a registry.

{{< chooser cloud "aws,azure,gcp" >}}
{{% choosable cloud aws %}}

In this example, we create an ECR repository configured to scan an image’s Operating System components. Scanning for vulnerabilities in an application is currently [out of scope](https://aws.amazon.com/blogs/containers/amazon-ecr-native-container-image-scanning/). We also set a policy for the repository that controls the actions allowed and a lifecycle policy that expires an image after a set time.

With Pulumi, it’s possible to build an image locally using Docker and push it to your repository. To push the image, we obtain the credentials required to push from the registry. Finally, we export the credentials and the URL for the registry. Read more about ECR in the [API Reference]({{< relref "/registry/packages/aws/api-docs/ecr" >}}).

```typescript
import * as docker from "@pulumi/docker";
import * as aws from "@pulumi/aws";

// Create a repository and configure to scan the image on push
const repo = new aws.ecr.Repository("myrepository", {
    imageScanningConfiguration: {
        scanOnPush: true
    },
    imageTagMutability: "MUTABLE",
});

// Set a use policy for the repository
const repositoryPolicy = new aws.ecr.RepositoryPolicy("myrepositorypolicy", {
    repository: repo.id,
    policy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Sid: "new policy",
            Effect: "Allow",
            Principal: "*",
            Action: [
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload",
                "ecr:DescribeRepositories",
                "ecr:GetRepositoryPolicy",
                "ecr:ListImages",
                "ecr:DeleteRepository",
                "ecr:BatchDeleteImage",
                "ecr:SetRepositoryPolicy",
                "ecr:DeleteRepositoryPolicy"
            ]
        }]
    })
});

// Set a policy to control the lifecycle of an image
const lifecyclePolicy = new aws.ecr.LifecyclePolicy("mylifecyclepolicy", {
    repository: repo.id,
    policy: JSON.stringify({
        rules: [{
            rulePriority: 1,
            description: "Expire images older than 14 days",
            selection: {
                tagStatus: "untagged",
                countType: "sinceImagePushed",
                countUnit: "days",
                countNumber: 14
            },
            action: {
                type: "expire"
            }
        }]
    })
});

// Get the repository credentials we use to push to the repository
const repoCreds = repo.registryId.apply(async (registryId) => {
    const credentials = await aws.ecr.getCredentials({
        registryId: registryId,
    });
    const decodedCredentials = Buffer.from(credentials.authorizationToken, "base64").toString();
    const [username, password] = decodedCredentials.split(":");
    return { server: credentials.proxyEndpoint, username, password };
});

// Create a new image and push to the repository
const image = new docker.Image("myapp", {
    imageName: repo.repositoryUrl,
    build: "./app",
    registry: repoCreds,
})

// Export credentials and URL to the repository
export const credentials = repoCreds;
export const repoEndpoint = repo.repositoryUrl;
```

{{% /choosable %}}
{{% choosable cloud azure %}}

In this example, we create an [Azure Resource Group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#what-is-a-resource-group) to contain the resources for the registry, such as the [App Service](https://docs.microsoft.com/en-us/azure/app-service/) that hosts the registry.

We instantiate a registry with the [containerservice module]({{< relref "/registry/packages/azure/api-docs/containerservice" >}}) and use the [Image module]({{< relref "/registry/packages/docker/api-docs/image" >}}) in the [Docker package]({{< relref "/registry/packages/docker/api-docs" >}}) to build and push the image to the registry. We export the registry URL and the username and password in case we should want to push or pull and image using the Docker CLI.

```typescript
import * as azure from "@pulumi/azure";
import * as docker from "@pulumi/docker";
import * as pulumi from "@pulumi/pulumi";

// Create an Azure Resource Group
const resourceGroup = new azure.core.ResourceGroup("examples");

// Create a dedicated App Service Plan for Linux App Services
const plan = new azure.appservice.Plan("linux-apps", {
    resourceGroupName: resourceGroup.name,
    kind: "Linux",
    reserved: true,
    sku: {
        tier: "Basic",
        size: "B1",
    },
});

const repo = new azure.containerservice.Registry("myrepository", {
    resourceGroupName: resourceGroup.name,
    sku: "Basic",
    adminEnabled: true,
});

const myImage = new docker.Image("myapp", {
    imageName: pulumi.interpolate`${repo.loginServer}/${"myapp"}:v1.0.0`,
    build: {
        context: `./${"app"}`,
    },
    registry: {
        server: repo.loginServer,
        username: repo.adminUsername,
        password: repo.adminPassword,
    },
});

export const server = repo.loginServer;
export const username = repo.adminUsername;
export const password = repo.adminPassword;
```

{{% /choosable %}}
{{% choosable cloud gcp %}}

In this example, we’ll use the configuration and credentials from the gcloud CLI to build an image and push it into the GCP registry. Make sure the GCP project is set and you are logged into GCP and Docker is configured to use the GCR,

```bash
$ gcloud init
$ gcloud auth login
$ gcloud auth configure-docker
```

We use the [Image module]({{< relref "/registry/packages/docker/api-docs/image" >}}) in the [Docker package]({{< relref "/registry/packages/docker/api-docs" >}}) to build and push the image to the registry. We export the registry URL and the username and password in case we should want to push or pull an image using the Docker CLI.

```typescript
import * as docker from "@pulumi/docker";
import * as gcp from "@pulumi/gcp";
import * as pulumi from "@pulumi/pulumi";

// Build and push image to gcr repository

const imageName = "myapp";

const myImage = new docker.Image(imageName, {
    imageName: pulumi.interpolate`gcr.io/${gcp.config.project}/${imageName}:latest`,
    build: {
        context: "./app",
    },
});

// Export the repository end point
export const repoEndpoint = pulumi.interpolate`gcr.io/${gcp.config.project}`;
```

{{% /choosable %}}
{{< /chooser >}}

## Learn more

Container registries are just one of the many resources used for deploying modern applications. Implementations among cloud service providers differ by the functionality they offer and how they are deployed. The commonality among them is that they provide a secure place to store and retrieve Docker or OCI compliant container images. Explore how to create and manage resources for the cloud service provider of your choice with Pulumi. Great places to start are:

- [Tutorials]({{< relref "/registry" >}})
- [Examples](https://github.com/pulumi/examples)
- [API Reference]({{< relref "/docs/reference/pkg" >}})
