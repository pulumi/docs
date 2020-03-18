---
title: "Architecture as Code"
date: 2020-03-18T13:42:35-05:00
meta_desc: " An overview of fnfrastructure architecture and implementations with Pulumi"
meta_image: architecture.png
authors:
    - sophia-parafina
tags:
    - virtual machines
    - Kubernetes
    - serverless
    - microservices
---

Abstraction in software is key to building resilient systems by encapsulating behavior and decoupling code. The same principles apply to infrastructure, where we want to declare behavior or state and not implementation details. As an industry, we've moved away from monolithic applications to distributed systems such as serverless, microservices, Kubernetes, and virtual machine deployments. In this article, we'll take a closer look at the characteristics of these architectures and how Pulumi can abstract the components that comprise these systems.

<!--more-->

## Virtual Machines

Virtual machines arose from the need to use expensive hardware more efficiently. VMs achieve efficiency by sharing the host with separate computing environments that decrease the number of servers needed to run applications. A group of hosts can also be aggregated so that it behaves as a single virtual host with large memory and processing capabilities. Virtual machines can also emulate other environments that have specific hardware requirements or capabilities that the host machine does not have. Finally, virtualization provides the host machine isolation from the guest virtual machines, limiting access to the host machine through an abstraction layer. Virtualization has the added advantage of enabling a fine degree of control over resources available to the virtual machine.

If virtual machines are part of your infrastructure, Pulumi lets you create virtual machines programmatically across cloud service providers. The Javascript example below illustrates how to deploy a virtual machine on Google Cloud Platform. The script spins up a Debian based instance and creates a network with an open port 22 to let you configure and manage the machine as needed.

```js
const gcp = require("@pulumi/gcp");
const fs = require(‘fs’);

// Create a network
const network = new gcp.compute.Network("network");
const computeFirewall = new gcp.compute.Firewall("firewall", {
    network: network.id,
    allows: [{
        protocol: "tcp",
        ports: [ "22",”80” ],
    }],
});

// Read the configuration script
const startupScript = fs.readFileSync(‘config.sh’, ‘utf-8’)

// Create a Virtual Machine Instance
const computeInstance = new gcp.compute.Instance("instance", {
    machineType: "f1-micro",
    zone: "us-central1-a",
    metadataStartupScript: startupScript,
    bootDisk: { initializeParams: { image: "debian-cloud/debian-9" } },
    networkInterfaces: [{
        network: network.id,
        // accessConfigus must includ a single empty config to request an ephemeral IP
        accessConfigs: [{}],
    }],
});

// Export the name and IP address of the Instance
exports.instanceName = computeInstance.name;
exports.instanceIP = computeInstance.networkInterfaces.apply(ni => ni[0].accessConfigs[0].natIp);
```
This is the configuration script.

```bash
#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &
```
When the virtual machine is created, it reads a configuration file that creates a webserver. This a basic example, but it shows how to configure virtual machines programmatically, which is useful for scaling horizontally.

## Serverless

Serverless is a computing architecture characterized by server-side logic running in stateless containers that are invoked by events. They are typically ephemeral (often are available for only one call), and managed by third-party cloud providers. Serverless is also called Functions as a Service, or `FaaS`, and well-known implementations include AWS Lambda and Fargate, Azure Functions, and Google Cloud Run and Cloud Functions.

A significant benefit of serverless is that it's a polyglot platform that allows developers to choose languages optimized for a task. For example, scripting languages like Javascript or Python may be more responsive than a language such as Java. Serverless functions should support both synchronous and asynchronous calls. There are use cases that require an immediate response such as processing a video stream and instances where returning the result is not critical as in an ETL batch job.

A key part of serverless architecture is an API Gateway that provides logical routes for mapping standard HTTP operations such as GET, PUT, POST, and DELETE to functions. The gateway makes development easier since these are standard and well-known interfaces. In addition to an API Gateway, the serverless platform should provide REST endpoints that allow you to manage the deploy with a CLI, portal, or an automation script. Finally, serverless architecture is extensible and supports integration with event sources and resources from the cloud provider through webhooks and other mechanisms.

The following example illustrates how to deploy two functions, one written in Python and the other written in Go. You can find the [full example](https://github.com/pulumi/examples/tree/master/gcp-ts-serverless-raw) in the Pulumi Github repository.

```ts
import * as gcp from "@pulumi/gcp";
import { asset } from "@pulumi/pulumi";

const bucket = new gcp.storage.Bucket("bucket");

// Google Cloud Function in Python

const bucketObjectPython = new gcp.storage.BucketObject("python-zip", {
    bucket: bucket.name,
    source: new asset.AssetArchive({
        ".": new asset.FileArchive("./pythonfunc"),
    }),
});

const functionPython = new gcp.cloudfunctions.Function("python-func", {
    sourceArchiveBucket: bucket.name,
    runtime: "python37",
    sourceArchiveObject: bucketObjectPython.name,
    entryPoint: "handler",
    triggerHttp: true,
    availableMemoryMb: 128,
});

export const pythonEndpoint = functionPython.httpsTriggerUrl;

// Google Cloud Function in Go

const bucketObjectGo = new gcp.storage.BucketObject("go-zip", {
    bucket: bucket.name,
    source: new asset.AssetArchive({
        ".": new asset.FileArchive("./gofunc"),
    }),
});

const functionGo = new gcp.cloudfunctions.Function("go-func", {
    sourceArchiveBucket: bucket.name,
    runtime: "go111",
    sourceArchiveObject: bucketObjectGo.name,
    entryPoint: "Handler",
    triggerHttp: true,
    availableMemoryMb: 128,
});

export const goEndpoint = functionGo.httpsTriggerUrl;
```

## Kubernetes

Kubernetes is a container orchestration system for deploying, scaling, and managing your application. The components that make up the application are in containers, which packages the code with all dependencies included. Containers run on a cluster of nodes, and you declare how to allocate CPU and memory resources to each container. Kubernetes manages the containers by replacing containers that fail and killing containers that don't respond. It can also scale the number of containers as well as load balance the network traffic. These are some of the features that Kubernetes provides:

- Load balancing and traffic distribution across the cluster
Service discovery
- Create and manage containers
- Remove failed containers and reassign their resources to a new container
- Mount storage systems such as local storage and storage on public cloud providers
- Automated deployments based on different deploy methods such as canary or blue/green deployments
- Automated rollbacks to last known good state
Secrets management

The following example is based on the [Kubernetes Guestbook](https://kubernetes.io/docs/tutorials/stateless-application/guestbook/) application. The difference between this implementation and the original application is that instead of using YAML to declare the infrastructure, it uses a component written in TypeScript to create the service deployment which is implemented as `k8sjs`.

```ts
import * as k8s from "@pulumi/kubernetes";
import * as k8stypes from "@pulumi/kubernetes/types/input";
import * as pulumi from "@pulumi/pulumi";

/**
 * ServiceDeployment is an example abstraction that uses a class to fold together the common pattern of a
 * Kubernetes Deployment and its associated Service object.
 */
export class ServiceDeployment extends pulumi.ComponentResource {
    public readonly deployment: k8s.apps.v1.Deployment;
    public readonly service: k8s.core.v1.Service;
    public readonly ipAddress?: pulumi.Output<string>;

    constructor(name: string, args: ServiceDeploymentArgs, opts?: pulumi.ComponentResourceOptions) {
        super("k8sjs:service:ServiceDeployment", name, {}, opts);

        const labels = { app: name };
        const container: k8stypes.core.v1.Container = {
            name,
            image: args.image,
            resources: args.resources || { requests: { cpu: "100m", memory: "100Mi" } },
            env: [{ name: "GET_HOSTS_FROM", value: "dns" }],
            ports: args.ports && args.ports.map(p => ({ containerPort: p })),
        };
        this.deployment = new k8s.apps.v1.Deployment(name, {
            spec: {
                selector: { matchLabels: labels },
                replicas: args.replicas || 1,
                template: {
                    metadata: { labels: labels },
                    spec: { containers: [ container ] },
                },
            },
        }, { parent: this });

        this.service = new k8s.core.v1.Service(name, {
            metadata: {
                labels: this.deployment.metadata.labels,
            },
            spec: {
                ports: args.ports && args.ports.map(p => ({ port: p, targetPort: p })),
                selector: this.deployment.spec.template.metadata.labels,
                // Minikube does not implement services of type `LoadBalancer`; require the user to specify if we're
                // running on minikube, and if so, create only services of type ClusterIP.
                type: args.allocateIpAddress ? (args.isMinikube ? "ClusterIP" : "LoadBalancer") : undefined,
            },
        }, { parent: this });

        if (args.allocateIpAddress) {
            this.ipAddress = args.isMinikube ?
                this.service.spec.apply(spec => spec.clusterIP) :
                this.service.status.apply(status => status.loadBalancer.ingress[0].ip);
        }
    }
}

export interface ServiceDeploymentArgs {
    image: string;
    resources?: k8stypes.core.v1.ResourceRequirements;
    replicas?: number;
    ports?: number[];
    allocateIpAddress?: boolean;
    isMinikube?: boolean;
}
```

The main program deploys an instance of Redis and the guestbook application using containers pulled from the Google Container Registry.


```ts
import * as pulumi from "@pulumi/pulumi";
import * as k8sjs from "./k8sjs";

const config = new pulumi.Config();

const redisMaster = new k8sjs.ServiceDeployment("redis-master", {
    image: "k8s.gcr.io/redis:e2e",
    ports: [6379],
});

const redisReplica = new k8sjs.ServiceDeployment("redis-replica", {
    image: "gcr.io/google_samples/gb-redisslave:v1",
    ports: [6379],
});

const frontend = new k8sjs.ServiceDeployment("frontend", {
    replicas: 3,
    image: "gcr.io/google-samples/gb-frontend:v4",
    ports: [80],
    allocateIpAddress: true,
    isMinikube: config.getBoolean("isMinikube"),
});

export let frontendIp = frontend.ipAddress;
```

The [original example](https://github.com/kubernetes/examples/tree/master/guestbook) defines the Service and Deployment in YAML. In the example above, the YAML is abstracted in a reusable component written in a modern programming language. The [complete example](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook) is available on Github. As you can see, the ability to reuse components gets us closer to implementing architecture as code.

## Microservices

Microservices are based on the idea that a component in the application is an encapsulation of a business capability. Services are independently deployable and communicate via web service requests, which has the advantage of redeploying only one or selected services and leaving the remaining components up and running. The [12-Factor app](https://12factor.net/) is the canonical pattern for microservice, which is summarized by:

- Use declarative methods to configure and deploy applications.
- Enforce maximum portability between environments by establishing a clean contract with the underlying operating system.
- Deploy on modern cloud platforms that diminish the need for servers and the requisite system administration.
- Establish continuous deployment by keeping development, testing, and production stages similar.
- Use platforms with the ability to scale without significant changes to architecture, development, or tooling.

In addition to Kubernetes, there are other platforms for deploying container-based applications. AWS Elastic Container Service, Google Cloud Run, and Azure Container Service provide alternatives to Kubernetes for container orchestration. The following code snippet demonstrates deploying a container with a Ruby application in Google Cloud Run. Note that the image is built using a local Docker engine and pushed to the Google Cloud Repository. The code shows that you can also set memory limits and concurrency for the container. The [full example](https://github.com/pulumi/examples/tree/master/gcp-ts-cloudrun) is available on Github.

```ts
import * as docker from "@pulumi/docker";
import * as gcp from "@pulumi/gcp";
import * as pulumi from "@pulumi/pulumi";

// Location to deploy Cloud Run services
const location = gcp.config.region || "us-central1";

// -------------------------------------- //
// Deploy a custom container to Cloud Run //
// -------------------------------------- //

// Build a Docker image from our sample Ruby app and put it to Google Container Registry.
// Note: Run `gcloud auth configure-docker` in your command line to configure auth to GCR.
const imageName = "ruby-app";
const myImage = new docker.Image(imageName, {
    imageName: pulumi.interpolate`gcr.io/${gcp.config.project}/${imageName}:v1.0.0`,
    build: {
        context: "./app",
    },
});

// Deploy to Cloud Run. Some extra parameters like concurrency and memory are set for illustration purpose.
const rubyService = new gcp.cloudrun.Service("ruby", {
    location,
    template: {
        spec: {
            containers: [{
                image: myImage.imageName,
                resources: {
                    limits: {
                        memory: "1Gi",
                    },
                },
            }],
            containerConcurrency: 50,
        },
    },
});

// Open the service to public unrestricted access
const iamRuby = new gcp.cloudrun.IamMember("ruby-everyone", {
    service: rubyService.name,
    location,
    role: "roles/run.invoker",
    member: "allUsers",
});

// Export the URL
export const rubyUrl = rubyService.status.url;

```

## Conclusion

We've covered the major infrastructure architectural patterns use for deploying modern applications. Whether you use Virtual Machines, Serverless, Kubernetes or Microservices on Containers the goal is to create reusable components that abstract the configuration details and enable plug-and-play architecture. In subsequent articles, we'll take an in-depth look at each pattern and how to implement them on major providers using modern languages.
