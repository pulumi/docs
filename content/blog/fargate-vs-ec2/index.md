---
title: "EKS Fargate vs EC2"
date: 2024-11-18T08:42:34-05:00
# you want to be able to merge the post without publishing it.
draft: false
meta_desc: Explore the differences between AWS EKS Fargate and EC2-backed clusters for your Kubernetes EKS workloads.
meta_image: meta.png
authors:
    - adam-gordon-bell
tags:
    - aws
social:
    twitter:
    linkedin:

---

So, I'm setting up an EKS cluster for a video demo and my simplified Pulumi code is this:

```python
import pulumi
import pulumi_awsx as awsx
import pulumi_eks as eks
import pulumi_kubernetes as k8s

# Create VPC with default CIDR
eks_vpc = awsx.ec2.Vpc("eks-vpc",
    enable_dns_hostnames=True)

# Create minimal EKS cluster
eks_cluster = eks.Cluster("eks-cluster",
    vpc_id=eks_vpc.vpc_id,
    private_subnet_ids=eks_vpc.private_subnet_ids,
    fargate=True,  
)

pulumi.export("kubeconfig", eks_cluster.kubeconfig)
```
<!--more-->

And look in k9s I get this:

![k9s fargate demo](k9s-fargate.gif)

You can see that each pod is on it's own node. Even the core-dns pods in the system namespace are each on their own nodes.

If I change my cluster to be backed by EC2 nodes I get something different.

```diff
eks_cluster = eks.Cluster("eks-cluster",
    vpc_id=eks_vpc.vpc_id,
    private_subnet_ids=eks_vpc.private_subnet_ids,
-   fargate=True,  
+   instance_type="t3.medium",
+   desired_capacity=2,
+   min_size=1,
+   max_size=2,
)
```

Now there are only two nodes, with the pods distributed among them. Those are my two `t3.medium`s.

![k9s eks demo](k9s-eks.gif)

So when should you use Fargate and when EC2 for EKS? And what's going on here, with the nodes.

Let's get to the bottom of that.

## Bin Packing

Normally, the Kubernetes scheduler has to solve a bin-packing problem—fitting M pods across N nodes based on available resources. This is a straight-up resource optimization problem of balancing CPU, memory, and other resource demands across the cluster.

With Fargate, AWS sidesteps this challenge by providing a "just-in-time" bin for each pod. Each Fargate pod runs on its own dynamically provisioned, right-sized mini-environment, where the "bin" (the Fargate instance) is exactly sized to match the pod's requested resources. This means there’s no need for Kubernetes to optimize for resource usage across a pool of shared nodes, as each pod effectively has its own “container” provided by Fargate that fits it precisely.

In other words, AWS effectively pushes this bin-packing responsibility to itself, so you don't have to worry about it.

{{% notes type="info" %}}
While Fargate abstracts away node management, it's important to understand that Fargate pods [still run on EC2 instances](https://justingarrison.com/blog/2024-02-08-fargate-is-not-firecracker/) behind the scenes. And that each Fargate pod gets its own ENI (Elastic Network Interface) and that can sometimes limit your scaling, because pods aren't sharing a network namespace.
{{% /notes %}}

## Pros of Fargate

By shifting bin-packing to AWS, Fargate abstracts the complexity of managing nodes and scaling clusters. AWS, with its extensive infrastructure, is arguably better positioned to optimize placements at scale. They can monitor their entire cloud landscape, placing Fargate instances dynamically across available resources. This allows them to potentially leverage underutilized resources in ways that would be challenging or impractical at an individual accounts’s scale.

This can mean simplified operations, scaling, and no need to manage node pools or worry about scheduling pods efficiently on shared instances. Ideally, this frees you to focus on the services rather than on the underlying infrastructure.

## Cons of Fargate

Ok, but there's downsides though. Since each task is treated as a standalone instance, you lose out on the cost efficiencies of co-locating multiple pods on a single node. Even though AWS is “solving” the bin-packing problem globally, to do so they need to introduce hard barriers, and while noisy neighbors therefore aren't a problem, sharing resources is now impossible. In a way, you are throwing away the run time benefit of containers, the shared kernel virtualization, for something more like VMs. And just like VMs, Fargate pods take longer to start than pods on existing EC2 nodes (typically 30-60 seconds vs near-immediate starts).

Maybe this will make more sense with an example.

## Workload Example: Static Analysis

Have you ever had to run CPU-intensive batch jobs alongside lighter web services? In a previous role, when my team and I were tasked with putting our static container image analyzer into production, we went the typical Kubernetes route, throwing it into an EC2-backed K8s cluster. The analyzer was built in Scala, running on the JVM, and was designed to take in work from a Kafka topic. Each analysis ultimately led to the results being sent to a database. We also had scheduled daily rescans of existing images whenever vulnerability lists updated.

Then there was a web app, that connected to this database and showed all your results. It was stateless and did far less work per request, mainly just answering a http request by talking to a database.

Here is the hard part though: each analysis job involved uncompressing and analyzing Docker layers from S3, and could use a lot of CPU. Memory needs were around 2 GB per instance, which kept the JVM happy, but long sustained bursts in CPU usage were common, especially during intensive parts of the analysis.

In our K8s setup, the biggest pain point was handling the burstiness of this analysis workload and also keep a bunch of stateless webapps up and answering requests. We ran multiple instances of the static analyzer but the analyzer was the worst type of noisy neighbor to other services in the cluster and so we’d end up over-provisioning to ensure we had enough headroom, which led to wasted resources and extra cost. The setup worked, but was not great.

Thinking back, I can see how Fargate could’ve streamlined things here. With Fargate, each static analyzer instance would run in its own isolated environment, so there’d be no resource contention or need for pre-provisioned node capacity. Each pod would be fully provisioned with the exact CPU and memory needed and we could do some sort of on-demand scaling to deal with backlogs of analysis work in the kafka topic.

For this type of chunky, resource heavy, macro-services, it seems like Fargate on EKS could be a great solution. There are probably other ways to handle this situation and we did work on decomposing the analysis into smaller chunks, but Fargate might have been a good solution.

But there are lots of situations where Fargate is less of a fit.

## Example: Go Services for Ecommerce

Ok, another workload that comes to mind, this one from a friend - He worked on an e-commerce backend with many lightweight Go services, each handling specific tasks—user profiles, catalog browsing, order processing, and notifications. These services were network-heavy, handling gRPC calls and database requests, but they didn’t need much CPU or memory per instance.

Fargate wouldn’t have made sense here—it would have isolated each pod, preventing resource sharing and driving up costs without real benefit. For lightweight services like these, EC2-backed Kubernetes is perfect, keeping costs low and maximizing resources by sharing nodes across small, efficient services.

So, for light-weight micro-services that can share resources, EC2 nodes with many pods each are probably the way to go.

## Other Fargate Cases

There are lots of other case for using Fargate though. Building demos is one. Another is short-lived or bursty workloads, where things run briefly or unpredictably. In that case, Fargate’s on-demand scaling could be a win.

Event-driven architectures can be fit. Systems that respond to specific events, like file uploads or new data processing, work well with Fargate's scale-up and tear-down flexibility, assuming the start up time isn't an issue.

And the big reason is simplified DevOps. For teams that want to avoid managing EC2 instances and focus on deploying apps, Fargate simplifies scaling and infrastructure management.

Of course there are lots of limitations to watch out for. Fargate isn’t ideal for applications requiring persistent storage, privileged mode, custom networking, GPU access, DaemonSets, or shared memory, all of which benefit from the flexibility and host-level access provided by EC2-backed Kubernetes.

{{% notes type="info" %}}
Fargate has some hard limitations that might rule it out for your use case:

- No DaemonSets
- Maximum of 4 vCPU and 30GB memory per pod
- No persistent volumes for stateful workloads
- No GPU support

{{% /notes %}}

Also Fargate only offers ephemeral storage, capped at 20 GB per task or pod. Applications needing larger or persistent file systems may find this limiting, especially if they require data to persist beyond the task lifecycle. And if you have constant, predictable workloads then EC2-backed clusters with optimized nodes are generally cheaper than paying per pod.

## Fargate vs EC2 Pricing

Ok, EC2 costs less than fargate, on a pure cost of compute basis. If my t3.medium ($0.0416/hr) can typically run 6-8 pods reliably this works out to under $0.01/hr per pod. Comparable Fargate pods (0.5 vCPU/1GB) cost about $0.025/hr each, so 2.5x. But we need headroom on EC2 and these pure compute comparisons don't account for the operational overhead of managing EC2 nodes. Also, maybe you are scaling up and down or maybe the isolation and simplied management is what you need.

Really, pure compute cost calculations are an insufficient metric for making this decision - you need to factor in your team's operational capacity, scaling patterns, and isolation requirements.

As they say *It Depends*.

Also if Fargate makes sense, because of your workload but the cost is a concern, then take a look at Fargate Spot instances, which can be up to 70% cheaper, but be aware that they can be terminated by AWS to reclaim capacity.

## Conclusions

I hope my examples point to a straightforward approach: use Fargate when you need isolation and / or scaling speed. Just make sure you can fit in its constraints. The static analyser case, for example. Also use it when you don't want to worry about EC2 nodes. Use EC2 when you've got efficient microservices that can share resources, like our Go e-commerce setup. Fargate trades potentially higher costs for operational simplicity. It's less flexible but often more important: it's easy to get started with — which is why I'm using it today.

If you’re interested in trying this out yourself, here’s a [practical EKS setup guide](/docs/iac/clouds/aws/guides/eks/). Now, back to getting this demo working!
