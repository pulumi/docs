---
title: "Managing AWS Containers with Pulumi"
date: 2020-01-06
meta_desc: "Deploying containers on AWS, ECS and EKS with Pulumi's infrastructure as code approach."
meta_image: meta.png
authors:
    - sophia-parafina
tags:
    - EKS
    - ECS
    - Lambda
    - AWS
    - containers
---

The Amazon Web Services (AWS) Cloud ecosystem is large and vibrant, so vast and vibrant that at times, it can be challenging to know where best to start! In the case of [containers](https://www.pulumi.com/containers/), [Abby Fuller](https://twitter.com/abbyfuller) tweeted a descriptive summary about using AWS container services.

<!--more-->

{{< tweet 1202016116580605952 >}}

It looks straightforward, but it's easy to get lost in the details when configuring multiple services to get your application running on AWS. Although AWS has extensive documentation and a point and click interface to these services, replicating then can be challenging, and it isn't conducive to understanding the architecture. However, using infrastructure as code lets you see the details and results in a reproducible deployment that you can expand on. Let’s implement the diagram using Pulumi to deploy your container infrastructure with code in AWS.

## Store your images

The AWS Elastic Container Registry (ECR) is a container registry that supports private container registries. ECR makes it easy to store, build, manage, and deploy container images and eliminates the need to operate your registry or use public registries, all in a highly available and scalable architecture.

In this example, we use Pulumi’s [Crosswalk for AWS]({{< relref "/docs/guides/crosswalk/aws" >}}). Crosswalk for AWS is a collection of frequent tasks and best practices that simplify deploying infrastructure on AWS. We first declare a repository; this creates the AWS Container Repository resource. The last line of the code exports the URL so that we can access the repository after we have updated our Pulumi stack. After we’ve run `pulumi up`, the repository is ready to go, and you can use the Docker CLI to push, pull, and manage images.

```typescript
import * as awsx from "@pulumi/awsx";

// Create a repository, as before.
const repo = new awsx.ecr.Repository("my-repo");

// And publish its URL, so we can push to it if we'd like.
export const url = repo.repository.repositoryUrl;
```

## Choose your scheduler

{{< tweet 1204900986898137088 >}}

There are two services for running containers in the AWS Cloud: Elastic Cloud Service (ECS), or Elastic Kubernetes Service (EKS). ECS is a proprietary service for running containers in the AWS Cloud. In contrast, EKS is a managed Kubernetes service for containers using a Kubernetes control plane. It has three master nodes distributed across three availability zones to provide high availability.

ECS is designed to work with other AWS services and provides more straightforward configuration and integration with them while providing high availability. In contrast, EKS is a managed Kubernetes service, and because Kubernetes is open-source, your infrastructure is portable to other cloud providers. Also, Kubernetes can provide fine-grain control over deployed services. The choice of which scheduler to use depends on your requirements.

You can create either an ECS or EKS cluster using Pulumi. If you wish to use ECS, Crosswalk for AWS (@pulumi/awsx) provides all the primitives needed to build infrastructure on AWS.

```ts
import * as awsx from "@pulumi/awsx";

// Create an ECS cluster explicitly, and give it a name tag.
const cluster = new awsx.ecs.Cluster("custom", {
    tags: {
        "Name": "my-custom-ecs-cluster",
    },
});
```

If you wish to use EKS, use the Pulumi EKS library (@pulumi/eks) for Kubernetes primitives on AWS.

```ts
import * as eks from "@pulumi/eks";

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("my-cluster");

```

## Choose where/how to run, Fargate or EC2

Fargate is an AWS service that runs containers. It is suited to running small workloads or batch workloads with occasional bursts that require scaling quickly. AWS EC2 is ideal for large workloads requiring many CPU cores and gigabytes of memory.

### Fargate

In this example, we create a load balancer open on port 80, spin up two instances of our container, and publish the endpoint URL.

```ts
// load balancer on port 80
const lb = new awsx.lb.ApplicationListener("nginx", { port: 80 });
const nginx = new awsx.ecs.FargateService("nginx", {
    cluster,
    taskDefinitionArgs: {
        containers: {
            nginx: {
                image: image,
                memory: 512,
                portMappings: [ lb ],
            },
        },
    },
    desiredCount: 2,
});

// Export the load balancer's address so that it's easy to access.
export const appURL = lb.endpoint.hostname;
```

### EC2 with Kubernetes

With Kubernetes, we create a deployment for the application and a service to make the application accessible via port 80. We publish both application endpoint to make it accessible and cluster config for use with `kubectl` CLI.

```ts
// Deploy a small canary service (NGINX), to test that the cluster is working.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image: "nginx",
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
}, { provider: cluster.provider });
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
}, { provider: cluster.provider });

// Export the URL for the load balanced service.
export const url = service.status.loadBalancer.ingress[0].hostname;

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
```

## Build!

Let’s put it all together for both ECS and EKS. To get started, follow the [Pulumi AWS documentation]({{< relref "/docs/get-started/aws" >}}) to install Pulumi, [install AWS Client](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html) set your [AWS environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html), and [create a new project]({{< relref "/docs/get-started/aws/create-project" >}}) in Typescript.

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-typescript
```

In this example, we build the application in code using the ECR repository class `buildAndPushImage`. This class uses Docker to build the image locally and push it to our repository. Make sure that you have [Docker installed and running](https://docs.docker.com/v17.09/engine/installation/#supported-platforms).

The container application for this example is an HTML page in NGINX. Make a `./app` directory in your Pulumi project and add the Dockerfile below.

Dockerfile:

```yaml
FROM nginx
COPY content /usr/share/nginx/html
```

Create a `./content` director in the `./app` directory and add the HTML file below.

```html
<html>
    <head><meta charset="UTF-8">
        <title>Hello, Pulumi!</title>
    </head>
    <body>
        <p>Hello, containers!</p>
        <p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
    </body>
</html>

```

Now that setup is complete you project directory should look similar to this:

```bash
quickstart/
├── Pulumi.dev.yaml
├── Pulumi.yaml
├── app
│   ├── Dockerfile
│   └── content
│       └── index.html
├── index.ts
├── node_modules
├── package-lock.json
├── package.json
└── tsconfig.json
```

### ECS

Now we're ready to start building our infrastructure. Replace the generated `index.ts` file with the example below. The example shows how to deploy containers on ECS using Fargate.

```typescript
import * as awsx from "@pulumi/awsx";

// Create a repository
const repo = new awsx.ecr.Repository("my-repo");

// Build an image from the "./app" directory
// and publish it to our ECR repository.
export const image = repo.buildAndPushImage("./app");

// Create an ECS cluster explicitly, and give it a name tag.
const cluster = new awsx.ecs.Cluster("custom", {
    tags: {
        "Name": "my-custom-ecs-cluster",
    },
});

// load balancer on port 80
const lb = new awsx.lb.ApplicationListener("nginx", { port: 80 });
const service = new awsx.ecs.FargateService("nginx", {
    cluster,
    taskDefinitionArgs: {
        containers: {
            nginx: {
                image: image,
                memory: 512,
                portMappings: [ lb ],
            },
        },
    },
    desiredCount: 2,
});

// Publish the load balancer address so it's accessible.
export const appURL = lb.endpoint.hostname;

// Publish the repository URL, so we can push to it.
export const repoURL = repo.repository.repositoryUrl;

```

To deploy the application, run `pulumi up`. You'll see a preview of the resources to be deployed.  Accept the deployment by selecting `yes`, and when finished, your program lists the URLs for the application and the repository.

```bash
Outputs:
    appURL : "nginx-0296a2a-996897041.us-east-1.elb.amazonaws.com"
    image  : "153052954103.dkr.ecr.us-east-1.amazonaws.com/my-repo-41f69f4:37c8add0fbd01474806c9c2319e62a857737de9e1460b09f935133860a069f4e"
    repoURL: "153052954103.dkr.ecr.us-east-1.amazonaws.com/my-repo-41f69f4"
```

Test to see if your application is working using either a browser or curl to see the web page.

```html
$ curl nginx-0296a2a-996897041.us-east-1.elb.amazonaws.com
<html>
    <head><meta charset="UTF-8">
        <title>Hello, Pulumi!</title>
    </head>
    <body>
        <p>Hello, containers!</p>
    <p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
    </body>
</html>
```

### EKS

The EKS example uses the `@pulumi/eks` and `@pulumi/kubernetes` node modules. Add the [eks](https://www.npmjs.com/package/@pulumi/eks) and [kubernetes](https://www.npmjs.com/package/@pulumi/kubernetes) modules to the project.

```bash
$ node install “@plulumi/eks”
$ node install “@plulumi/kubernetes”
```

Like the ECS example, the EKS example builds the application image locally and pushes it into our custom repository. The application deployment has two replicas in the configuration. The service uses the EKS cluster, `my-cluster`, we declared to create a load balancer with port 80 open.

```ts
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Create a repository, as before.
const repo = new awsx.ecr.Repository("my-repo");

// Build an image from the "./app" directory. and publish it to our ECR repository.
export const image = repo.buildAndPushImage("./app");

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("my-cluster")

// Deploy a small canary service (NGINX), to test that the cluster is working.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image: image,
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
}, { provider: cluster.provider });
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
}, { provider: cluster.provider });

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;

// Publish the repository URL.
export const repoURL = repo.repository.repositoryUrl;

// Publish the URL for the load balanced service.
export const appURL = service.status.loadBalancer.ingress[0].hostname;

```

As with the ECS example, run `pulumi up` to deploy the application. To check the deployment, use either curl or a browser to see the page.

## Want to know more?

Although these examples are simple, they demonstrate the basic building blocks for building, storing, and managing containers. They also show how to create ECS or EKS clusters for deploying apps. To get started with AWS and Pulumi check out the [AWS Guide]({{< relref "/docs/get-started/aws" >}}) for core services and the [Crosswalk for AWS guide]({{< relref "/docs/guides/crosswalk/aws" >}}) for convenience APIs that simplify deploying infrastructure as code. For a deeper dive into managing containers on AWS, check out our blogs on [ECS vs Fargate vs EKS: The Lowdown on Containers in AWS](https://www.pulumi.com/blog/running-containers-in-aws-the-lowdown-ecs-fargate-and-eks/) and [How to Scale Your Amazon EKS Cluster: EC2, Managed Node Groups, and Fargate]({{< relref "/blog/aws-eks-managed-nodes-fargate" >}}).
