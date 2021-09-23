---
title: "Getting Started with Kubernetes: Stateful Applications"
date: 2020-07-21
meta_desc: "How to deploy stateful applications in Kubernetes with Pulumi"
meta_image: getting-started.png
authors:
    - sophia-parafina
tags:
    - Kubernetes
---

This article is the fourth in a series using infrastructure as code to deploy applications with Kubernetes. This series walks you through:

- [Building a Kubernetes cluster on cloud providers]({{< relref "/blog/getting-started-with-k8s-part1" >}})
- [Basic application deployment]({{< relref "/blog/getting-started-with-k8s-part2" >}})
- [Advance application deployment and Helm charts]({{< relref "/blog/getting-started-with-k8s-part3" >}})
- Stateful applications
- Networking
- “Day 2” activities such as migrating node groups.

In the previous post, we examined different methods for deploying applications. We worked through examples of a boilerplate deployment, to one using `ComponentResources` to automate deployment further, and deploying with Helm charts. In this installment, we’ll look at how to deploy stateful applications, such as databases, in Kubernetes. Unlike stateless applications, stateful apps require persistent storage, which presents scaling and availability challenges.

<!--more-->

## Stateful vs. Stateless

Stateless applications don’t require information from a previous transaction because they are single request and response. For example, the [“Hello World” example](https://www.pulumi.com/blog/getting-started-with-k8s-part2/#examples) that we deployed in an earlier article is a stateless application. The critical thing to remember is that in Kubernetes, any container with that application in any pod can respond to that request.
Stateful applications can read or store information about previous transactions, and a transaction is executed within the context of a previous extraction. Email is an example of a stateful application; an email can be unread or read, or it can be grouped according to keywords or by content. In stateless applications, access to storage must be coordinated, either by sending all requests to the same Pod, or by synchronizing across multiple Pods.

## Stateful sets

Stateful sets are the Kubernetes workload object for managing stateful applications. They are a specialized type of [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), where the Pods maintain a persistent identity during updates and rescheduling.

You would use a [StatefulSet for](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#using-statefulsets):

- stable and unique network identifiers
- stable and persistent storage
- applications that require ordered deployment and scaling
- applications that require ordered and rolling updates

When a StatefulSet is created, each Pod is assigned a unique and persistent identifier. Pods are named numerically starting from 0, e.g., pod-0, pod-1, pod-n. StatefulSets use a [Headless Service](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services) resource, which sets the `clusterIP` property to `none`. Pods in a StatefulSet will have an IP address mapped directly to them instead of a virtual IP address. This lets other Pods in the cluster directly communicate to an application, as in database connections.

StatefulSets can control the order of starting and stopping Pods. Some applications require a resource to be available before the Pod can be marked healthy. A Pod in a StatefulSet can be mounted to a dedicated [persistent volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) by declaring a `PersistentVolumeClaim`. If a Pod in a StatefulSet shuts down, the StatefulSet Controller will relaunch a replacement Pod with the same network identifier and reattach it to the persistent Volume.

StatefulSets have two update strategies. The [OnDelete](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#on-delete) strategy does not automatically update the Pods, and they must be manually deleted for the controller to create new Pods. [Rolling updates](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#rolling-updates) automatically deletes and creates a replacement for Pods in a StatefulSet. It creates replacement in the same order as they are deleted, which is from the highest to the smallest numbered Pod. A replacement Pod must be ‘Running and Ready’ before it replaces the preceding Pod.

## Example

Let’s see how this works in practice with a [MariaDB deployment in Kubernetes](https://github.com/pulumi/kubernetes-guides/tree/master/apps/statefulset). The example begins with defining the cluster configuration and the MariaDB configuration using a [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/). We’ll skip over this and go straight to the StatefulSet.

### Headless Service

In the previous section, we described the Headless Service. The key parts are setting the `ClusterIP` to `"None"`, which allocates an IP address and port so that applications can establish a database connection.

{{< gist pulumipus 057ca0abb4758161a4d3ce2698e9683a >}}

### Deployment

Let’s look at the StatefulSet, step-by-step. The `spec` matches the StatefulSet to the Headless Service using a selector that matches the labels. We assign it a service name, specify a single replica, and a `RollingUpdate` update strategy. Note that this is the default update strategy, but it’s a good practice to declare it.

{{< gist pulumipus a8177859dad6efbadc600c49ab678008 >}}

### Pod scheduling

The next section declares variables for MariaDB, such as the `serviceAccountName` and the `securityContext`. However, of interest is the [`podAntiAffinity`](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) parameter, which ensures that the Pod will not be deployed on a Node with a Pod with the labels ‘mariadb’ and ‘example’. The `weight` is set for the preferred rule, where a node with a higher weight is preferred. We prevent another instance from being deployed on the same host by setting `topologyKey: "kubernetes.io/hostname"`.

Putting it all together, we’ve told the Kubernetes Scheduler never to co-locate two Pods that have the app labels “mariadb” and “example” in the same domain (or Node) defined by setting `topologyKey:”kubernetes.io/hostname”`. These parameters control Pod scheduling to ensure that if a Pod is replaced, the new Pod is addressable by other resources in the application.

{{< gist pulumipus fbf24163a0506c4d678500a92ac56981 >}}

### Configure the MariaDB container

The following section configures the MariaDB container. We’ll skip the part of the container configuration and look at healthchecks that impact the Pod's scheduling. The `livenessProbe` is useful for detecting if a long-running application, such as a database, is broken and cannot recover except by a restart.  In this example, we call the mysql init script as a status check. If the container fails the `livenessProbe`, the Kubernetes scheduler will kill the Pod and replace it. A `readinessProbe` is similar to a `livenessProbe`; if the probe fails, Kubernetes won’t send traffic to the Pod. Unlike a `livenessProbe`, the Pod remains running and is not terminated and replaced by the scheduler. Probe field or settings are described in the [Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes).

We also configure two `volumeMounts`. The first `volumeMount` sets the MariaDB data path to the data `Volume`. The second `volumeMount` mounts the MariaDB configMap that was defined earlier.

{{< gist pulumipus 7e86db630aabd7e451ffced10c0277d6 >}}

### Create a Volume for storage

The final section of code creates a Persistent Volume using a `volumeClaimTemplate`. This object requests a PVC (`PersistentVolumeClaim`) from the storage class dynamically. We set the `accessModes` to “ReadWriteOnce”, which means the volume can be mounted as read-write by a single node. Other [`accessModes`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes) are “ReadOnlyMany”, where the volume can be mounted read-only by many nodes, and “ReadWriteMany”, where the volume can be mounted as read-write by many nodes. We also set the size of the Volume to 8 gigabytes.

{{< gist pulumipus 0520c6f917eaf0a532b99a2279d71118 >}}

To summarize, we deployed MariaDB using a `StatefulSet` by creating a `headlessService` which assigns a persistent IP address to the Pod instead of using `clusterIP` and `nodePorts` to route traffic to the application. We then defined Node Affinity/AntiAffinity to set rules on which nodes are selected by the scheduler for creating Pods. Next, we configured the container and set `livenessProbes` and `readinessProbes` to tell the Scheduler if a Pod needs to be terminated and restarted  or not to route traffic to the Pod until it is ready. We also configure `volumeMounts` and `volumes` to store configuration information and data for MariaDB.

## Conclusion

Stateful applications present additional challenges when deployed in Kubernetes. Many applications require a stateful resource, such as a database or a component that maintains a login and session id. Stateful applications route traffic to a stable and persistent resource. Kubernetes accomplishes this with `StatefulSets`, which creates resources with a persistent id and unique address. We can configure scheduling and replacement of Pods, to allow resources to continue using a persistent id and address. We can also configure containers with health checks to signal if a Pod should be terminated or if it should continue to receive requests. We can also control which Node can access a `PersistentVolume` with a volumeClaimTemplate, and in our example, we limit access to only one Node. Make sure to try out the complete [example on Github](https://github.com/pulumi/kubernetes-guides/tree/master/apps/statefulset).

 In the next series installment, we'll examine Kubernetes networking. Until then, you can learn more about Kubernetes with these resources:

- Watch educational content on [Pulumi TV](https://www.youtube.com/pulumitv)
- Learn more about Pulumi's [support for Kubernetes]({{< relref "/registry/packages/kubernetes" >}})
- Practice [Kubernetes Tutorials]({{< relref "/docs/tutorials/kubernetes" >}}) using Pulumi
