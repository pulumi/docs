---
title: "Kubernetes Fundamentals Part Two"
date: 2021-09-02T12:54:53-05:00
draft: false
meta_image: k8s-fundamentals.png
meta_desc: "Kubernetes is everywhere now, but it’s largely been the domain of people who work on the ops side of things. What about devs, though?"
authors:
    - kat-cosgrove
tags:
    - kubernetes
    - google-cloud
---
Kubernetes is everywhere now, but it’s primarily been the domain of people working on the ops side of infrastructure. What about devs, though? You benefit from knowing what Kubernetes is and how to use it, too&mdash;otherwise, we’re still putting teams in silos. In this blog, we're going to build off part one by learning about managed Kubernetes services: what they are, when they're useful, and how you can try deploying to one yourself, starting with Google's Kubernetes Engine (GKE).
<!--more-->

## What is a managed Kubernetes service?

Essentially, a managed Kubernetes service just means that someone else is responsible for some of the work involved in standing up and maintaining Kubernetes. It varies from provider to provider, but services can be pretty bare-bones or include everything under the sun, handing you a pre-configured environment and a dedicated support team to help you.

## What makes this option useful?

Kubernetes is very powerful, but also very complicated. The flexibility of the platform means that there's a lot of configuration you have to do just to get off the ground, and a managed service takes some of that off your plate. Some configurations are abstracted away, and some decisions are made for you. Things you would otherwise have to set up yourself, like load balancing, monitoring, and updates, are covered by the vendor. It's less effort to get started and less effort to maintain. Scaling is painless since you can just provision more resources. For most people, a managed service is flat-out more reliable.

## Okay, I want to try it for myself.

First things first, we need [Pulumi](https://www.pulumi.com/docs/get-started/install/), [Node.js](https://nodejs.org/en/download/), and [npm](https://www.npmjs.com/get-npm) installed.

We're going to do this on Google Cloud Product (GCP), so you'll also need the [Google Cloud SDK](https://cloud.google.com/sdk/docs/downloads-interactive) set up. From there, log in with `gcloud`:

```
$ gcloud auth login
$ gcloud config set project <YOUR_GCP_PROJECT_HERE>
$ gcloud auth application-default login
```

## Creating a Cluster with Google Kubernetes Engine

Next, we need a cluster. Start by creating a new directory, navigating into it, and initializing a new Pulumi project using TypeScript.

```bash
mkdir gke-hello-world && cd gke-hello-world && pulumi new typescript
```

We also need to install some dependencies, and set some required configuration values.

```bash
npm install --save @pulumi/pulumi @pulumi/gcp @pulumi/kubernetes
pulumi config set gcp:project <YOUR_GCP_PROJECT_HERE>
pulumi config set gcp:zone us-west1-a     // any valid GCP Zone here
```

Now, in `index.ts`, add the following code:

```typescript
import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const name = "helloworld";

// Create a GKE cluster. We start with two nodes, each running an n1-standard-1 machine, which provides the best balance of price for performance ratio for the most common workloads. Replicas of our application will be distributed across these two nodes, ensuring that if one node goes down, our application remains up in the other node.

const engineVersion = gcp.container.getEngineVersions().then(v => v.latestMasterVersion);
const cluster = new gcp.container.Cluster(name, {
    initialNodeCount: 2,
    minMasterVersion: engineVersion,
    nodeVersion: engineVersion,
    nodeConfig: {
        machineType: "n1-standard-1",
        oauthScopes: [
            "https://www.googleapis.com/auth/compute",
            "https://www.googleapis.com/auth/devstorage.read_only",
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring"
        ],
    },
});

// Export the Cluster name
export const clusterName = cluster.name;

// Manufacture a GKE-style kubeconfig. Note that this is slightly "different"
// because of the way GKE requires gcloud to be in the picture for cluster
// authentication (rather than using the client cert/key directly).
export const kubeconfig = pulumi.
    all([ cluster.name, cluster.endpoint, cluster.masterAuth ]).
    apply(([ name, endpoint, masterAuth ]) => {
        const context = `${gcp.config.project}_${gcp.config.zone}_${name}`;
        return `apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: ${masterAuth.clusterCaCertificate}
    server: https://${endpoint}
  name: ${context}
contexts:
- context:
    cluster: ${context}
    user: ${context}
  name: ${context}
current-context: ${context}
kind: Config
preferences: {}
users:
- name: ${context}
  user:
    auth-provider:
      config:
        cmd-args: config config-helper --format=json
        cmd-path: gcloud
        expiry-key: '{.credential.token_expiry}'
        token-key: '{.credential.access_token}'
      name: gcp
`;
    });

// Create a Kubernetes provider instance that uses our cluster from above.
const clusterProvider = new k8s.Provider(name, {
    kubeconfig: kubeconfig,
});
```

This code is the entrypoint for our program and is what's setting up the cluster for us. We're defining the resources we want, the `kubeconfig` that'll be used to access the cluster, and also the Kubernetes provider so that we can deploy resources to it next.

Now just run `pulumi up` to preview the changes, select `yes` when prompted, and watch the cluster stand up! You'll see some work happening in your terminal as well as in [your Pulumi account](https://app.pulumi.com), and when it's all done, you can look at your GCP dashboard and see the cluster there, too.

But we should actually put something in the cluster, shouldn't we?

## A Deployment for the Cluster

Let's work on that Kubernetes Provider. Using a Kubernetes Provider allows us to abstract away some of the specifics of operating a cluster on one cloud provider or another. That way, your experience from here on out is fairly consistent regardless of where you're hosting this.

In the same `index.ts` file from before, add this to the end:

```typescript
// Create a Kubernetes Namespace
const ns = new k8s.core.v1.Namespace(name, {}, { provider: clusterProvider });

// Export the Namespace name
export const namespaceName = ns.metadata.apply(m => m.name);

// Create a NGINX Deployment
const appLabels = { appClass: name };
const deployment = new k8s.apps.v1.Deployment(name,
    {
        metadata: {
            namespace: namespaceName,
            labels: appLabels,
        },
        spec: {
            replicas: 1,
            selector: { matchLabels: appLabels },
            template: {
                metadata: {
                    labels: appLabels,
                },
                spec: {
                    containers: [
                        {
                            name: name,
                            image: "nginx:latest",
                            ports: [{ name: "http", containerPort: 80 }]
                        }
                    ],
                }
            }
        },
    },
    {
        provider: clusterProvider,
    }
);

// Export the Deployment name
export const deploymentName = deployment.metadata.apply(m => m.name);

// Create a LoadBalancer Service for the NGINX Deployment
const service = new k8s.core.v1.Service(name,
    {
        metadata: {
            labels: appLabels,
            namespace: namespaceName,
        },
        spec: {
            type: "LoadBalancer",
            ports: [{ port: 80, targetPort: "http" }],
            selector: appLabels,
        },
    },
    {
        provider: clusterProvider,
    }
);

// Export the Service name and public LoadBalancer endpoint
export const serviceName = service.metadata.apply(m => m.name);
export const servicePublicIP = service.status.apply(s => s.loadBalancer.ingress[0].ip)
```

Here, we're creating a [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) and adding an NGINX [deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) with an accompanying LoadBalancer [service](https://kubernetes.io/docs/concepts/services-networking/service/) and exporting everything we need to run it. Run `pulumi up` once again, double-check the preview, and select `yes` to update the deployment. Now everything's up and running on a managed Kubernetes service that you didn't have to stand up by hand, and won't have to expend as much effort maintaining.  

## Talking to the Cluster

In case you're curious, you can still interact with the cluster using `kubectl` when running on a managed provider, just like when you're running everything locally. Run this command to have Pulumi export your kubeconfig with its secrets:

`pulumi stack output kubeconfig --show-secrets > kubeconfig`

Then just export it:

`export KUBECONFIG=$PWD/kubeconfig`

At that point, regular `kubectl` commands will work. If you followed along, make sure you run `pulumi destroy` to tear down this stack and all of its resources so you don't run up a bill!

## Coming Up Next

So, that was pretty quick. But I only talked about GKE. What about other cloud providers? Yeah, those work, too. And yes, it's also fairly quick. Now that I've explained the basics of Kubernetes and what managed Kubernetes is, things will get more practical&mdash;tune in next time for deploying to EKS!
