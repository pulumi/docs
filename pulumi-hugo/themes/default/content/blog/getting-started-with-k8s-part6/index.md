---
title: "Getting Started With Kubernetes: Day 2"
date: 2020-08-10
meta_desc: "How to use infrastructure as code for day 2 maintenance tasks in Kubernetes."
meta_image: day_2.png
authors:
    - sophia-parafina
tags:
    - kubernetes
---

Your application made it out of the dev stage, passed the testing stage, and arrived in production. As a developer, you might think that it's an ops problem now. However, DevOps is a collaborative effort between developers and operators to build and maintain applications using shared techniques and processes, often called "Day 2" activities.

<!--more-->

Day 2 tasks fall into three categories. The first category is managing cluster components. It involves managing nodes, users and groups, ingress and egress, networking, storage, and [operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/). The second category is changing cluster components, including setting optimal resource quota, reclaiming unneeded resources, scaling, tuning and updating clusters, and managing [CRDs](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#customresourcedefinitions). The third category of tasks is cluster monitoring and [logging](https://kubernetes.io/docs/tasks/debug-application-cluster/), which involves collecting and analyzing metrics, and monitoring the health of the cluster.

Although this subject is much deeper than we can cover in a single article, let’s take a look at how infrastructure as code can simplify some of these tasks.

## Managing secrets

In addition to managing users and groups, managing secrets such as credentials is an important task. The Pulumi CLI lets you rotate the secrets provider for a stack. This is particularly important when people leave an organization or if you want to change to a different secrets provider, e.g., from Vault to AWS KMS. Also, we can copy secrets from one stack to another. A frequent use of this capability is to copy database account credentials from one stack to another. You can read more about [managing secrets]({{< relref "/blog/managing-secrets-with-pulumi" >}}) and the using the [CLI]({{< relref "blog/rotating-secret-providers" >}}) to rotate providers on the Pulumi blog.

## Updating clusters

When you first deploy an application in production, you make assumptions about the configuration. However, as the number of users increases or features are added, the cluster configuration will change. Moving to larger machines that can support more nodes is common; however, we want to make that change without disrupting the service. To accomplish the update, we want to create the new larger node group, migrate the application, and decommission the preceding node group. Pulumi shows you how to do this in a [tutorial]({{< relref "/registry/packages/kubernetes/eks-migrate-nodegroups" >}}). A more descriptive [blog post]({{< relref "/blog/how-to-guides/day-2-kubernetes-migrating-eks-nodegroups-with-zero-downtime" >}}) walks you through the project [source code](https://github.com/pulumi/examples/tree/master/aws-ts-eks-migrate-nodegroups).

In addition to zero downtime cluster migrations, we can also control scaling. The following tutorial shows how to stage an application rollout from dev to testing controlled by performance collecting metrics. In this [tutorial]({{< relref "/registry/packages/kubernetes/how-to-guides/p8s-rollout" >}}), we move a three replica canary to a ten replica staging deployment. Replicas are added based on a P90 response time, i.e., 90% of requests are processed within 2.75 seconds. The example uses [Prometheus](https://prometheus.io/) to collect the response times and a [utility class](https://github.com/pulumi/examples/blob/master/kubernetes-ts-staged-rollout-with-prometheus/util.ts) to perform the health check. Check out the complete [code on Github](https://github.com/pulumi/examples/tree/master/kubernetes-ts-staged-rollout-with-prometheus).

Pulumi also lets you keep an eye on your Kubernetes resources in real-time with Pulumi watch. Results are updated live as you make changes like adding replicas or exposing an application with a load balancer.

{{< youtube "X96EMLi8uJY?rel=0" >}}

## Monitoring

There are many [logging and monitoring](https://kubernetes.io/docs/tasks/debug-application-cluster/) solutions available for Kubernetes. In the previous section, we used Prometheus for generating metrics. Pulumi supports logging and monitoring tools to assist with cluster and application management.

Kubernetes Cluster Services provide logging and monitoring at the cluster level or a subset of apps and workloads. Check out our tutorials for setting up logging and monitoring for Kubernetes on [AWS, Azure, and GCP]({{< relref "/docs/guides/crosswalk/kubernetes/cluster-services" >}}). The tutorial also shows how to configure [DataDog](https://www.datadoghq.com/) to log and monitor applications. The [example code](https://github.com/pulumi/kubernetes-guides/tree/master/general-cluster-services/datadog-daemonset) is on Github.

## Summary

Maintaining a Kubernetes cluster and modern applications can be varied and complex. However, infrastructure as code lets developers and operators use a common language to manage the cluster and resources. Pulumi has a rich toolset to help you accomplish Day 2 tasks, whether managing cluster components such as secrets, changing cluster components to scale applications, or logging and monitoring your cluster and resources.

Each article in this series is intended to be independent of each other. However, we build upon concepts introduced in previous articles. If some concepts or terminology are unfamiliar, I encourage reading the earlier articles:

- [Building a Kubernetes cluster on cloud providers]({{< relref "/blog/getting-started-with-k8s-part1" >}})
- [Basic application deployment]({{< relref "/blog/getting-started-with-k8s-part2" >}})
- [Advance application deployment and Helm charts]({{< relref "/blog/getting-started-with-k8s-part3" >}})
- [Stateful applications]({{< relref "/blog/getting-started-with-k8s-part4" >}})
- [Networking]({{< relref "/blog/getting-started-with-k8s-part5" >}})
