---
title: "Using Helm and Pulumi to define cloud native infrastructure as code"
authors: ["alex-clemmer"]
tags: ["Kubernetes","Azure"]
date: "2018-10-31"

meta_image: "helm-pulumi-deploy.gif"
---

The Helm community is one of the brightest spots in the infrastructure
ecosystem: collectively, it has accumulated person-decades of
operational expertise to produce Kubernetes manifests that "just work."

But for many users, it is not feasible to run *everything* in
Kubernetes, and the community is just starting to develop answers to
questions like: what happens when a Helm Chart needs to interface with,
for example, a managed database like AWS RDS or Azure CosmosDB?

Pulumi is a cloud native development platform designed to be able to
express any cloud native infrastructure as code in a natural,
intentional manner using real languages. The most natural way to solve
this challenge would be to stand up an instance of AWS RDS, populate a
Kubernetes Secret with the connection details, and then simply let my
application use these newly available resources. Pulumi gives users the
primitives they need in order to achieve tasks like this most
effectively.
<!--more-->

## How to connect a Kubernetes app with CosmosDB

In the following Pulumi program, we can manage both Azure and Kubernetes
resources, including the interconnected dependencies between the two.
Specifically, we:

- Create an AKS cluster,
- Create a MongoDB-flavored instance of Azure's CosmosDB,
- Create a Kubernetes Secret from the connection string exported by
  CosmosDB
- Deploy a Node.js Helm Chart that references it.

If you have the Azure command line, try [running the example](https://github.com/pulumi/examples/tree/master/azure-ts-aks-mean)
with `pulumi up`!

{{< highlight javascript >}}
import * as k8s from "@pulumi/kubernetes";
import * as azure from "@pulumi/azure";
import * as mongoHelpers from "./mongoHelpers";
import * as config from "./config";

// Create an AKS cluster.
import { k8sCluster, k8sProvider } from "./cluster";

// Create a MongoDB-flavored instance of CosmosDB.
const cosmosdb = new azure.cosmosdb.Account("cosmosDb", {
    kind: "MongoDB",
    resourceGroupName: config.resourceGroup.name,
    location: config.location,
    consistencyPolicy: {
        consistencyLevel: "BoundedStaleness",
        maxIntervalInSeconds: 10,
        maxStalenessPrefix: 200
    },
    offerType: "Standard",
    enableAutomaticFailover: true,
    geoLocations: [
        { location: config.location, failoverPriority: 0 },
        { location: config.failoverLocation, failoverPriority: 1 }
    ]);

// Create secret from MongoDB connection string.
const mongoConnStrings = new k8s.core.v1.Secret(
    "mongo-secrets",
    { data: mongoHelpers.parseConnString(cosmosdb.connectionStrings) },
    { provider: k8sProvider }
);

// Boot up nodejs Helm chart example using CosmosDB in place of in-cluster MongoDB.
const node = new k8s.helm.v2.Chart(
    "node",
    {
        repo: "bitnami",
        chart: "node",
        version: "4.0.1",
        values: {
            serviceType: "LoadBalancer",
            mongodb: { install: false },
            externaldb: { ssl: true, secretName: mongoConnStrings.metadata.apply(m => m.name) }
        }
    },
    { providers: { kubernetes: k8sProvider }, dependsOn: mongoConnStrings }
);
{{< /highlight >}}

Pulumi supports deploying resources to all the major cloud vendors, as
well as Kubernetes. Using the Pulumi programming model, it is possible
to define and deploy apps and infrastructure with an arbitrary mix of
resources from any combination of cloud providers. And, because Pulumi
uses normal `$KUBECONFIG` files, it is compatible anywhere you would use
Helm or `kubectl`.

The Pulumi CLI provides rich insight into the progress a deployment
makes. When you run `pulumi up`, the CLI will provide detailed
information about the progress we're making as we try to deploy the
Chart. To get a sense of what this looks like, take a look at the
progress reported as we deploy the Wordpress Chart:

![helm-pulumi-deploy](./helm-pulumi-deploy.gif)

## Toward Cloud Native Infrastructure as Code

As cloud native architectures mature, Pulumi can reduce the complexity
in choosing and using the available services from cloud vendors, and
combine those choices using a single, consistent programming model. This
can make the best use of existing tools such as Helm, and also reduce
the friction caused by multiple deployment tools and models across
complex architectures.

- Find out more about our [Azure]({{< ref "/azure" >}}) and
  [Kubernetes]({{< ref "/kubernetes" >}}) support
- Join the Slack community at <https://slack.pulumi.io> 
