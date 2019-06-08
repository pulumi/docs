---
title: "TODO Port frontmatter"
authors: ["chris-smith"]
tags: ["todo"]
date: "2017-01-01"
draft: true
description: "TODO: Put in a reasonable summary"
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

How to connect a Kubernetes app with CosmosDB
---------------------------------------------

In the following Pulumi program, we can manage both Azure and Kubernetes
resources, including the interconnected dependencies between the two.
Specifically, we

-   create an AKS cluster,
-   create a MongoDB-flavored instance of Azure's CosmosDB,
-   create a Kubernetes Secret from the connection string exported by
    CosmosDB
-   deploy a Node.js Helm Chart that references it.

If you have the Azure command line, try [running the
example](https://github.com/pulumi/examples/tree/master/azure-ts-aks-mean)
with `pulumi up`!

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

![helm-pulumi-deploy](https://blog.pulumi.com/hs-fs/hubfs/Blog/helm-pulumi-deploy.gif?width=800&name=helm-pulumi-deploy.gif){width="800"
sizes="(max-width: 800px) 100vw, 800px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/Blog/helm-pulumi-deploy.gif?width=400&name=helm-pulumi-deploy.gif 400w, https://blog.pulumi.com/hs-fs/hubfs/Blog/helm-pulumi-deploy.gif?width=800&name=helm-pulumi-deploy.gif 800w, https://blog.pulumi.com/hs-fs/hubfs/Blog/helm-pulumi-deploy.gif?width=1200&name=helm-pulumi-deploy.gif 1200w, https://blog.pulumi.com/hs-fs/hubfs/Blog/helm-pulumi-deploy.gif?width=1600&name=helm-pulumi-deploy.gif 1600w, https://blog.pulumi.com/hs-fs/hubfs/Blog/helm-pulumi-deploy.gif?width=2000&name=helm-pulumi-deploy.gif 2000w, https://blog.pulumi.com/hs-fs/hubfs/Blog/helm-pulumi-deploy.gif?width=2400&name=helm-pulumi-deploy.gif 2400w"}

Toward Cloud Native Infrastructure as Code
------------------------------------------

As cloud native architectures mature, Pulumi can reduce the complexity
in choosing and using the available services from cloud vendors, and
combine those choices using a single, consistent programming model. This
can make the best use of existing tools such as Helm, and also reduce
the friction caused by multiple deployment tools and models across
complex architectures.

-   Find out more about our [Azure](https://www.pulumi.com/azure) and
    [Kubernetes](https://www.pulumi.com/kubernetes) support
-   Try Pulumi at <https://pulumi.io> 
-   Join the Slack community at <https://slack.pulumi.io> 

