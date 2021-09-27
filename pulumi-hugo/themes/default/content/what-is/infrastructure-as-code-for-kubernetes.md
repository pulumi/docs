---
title: Infrastructure as Code for Kubernetes
meta_desc: |
     Infrastructure as code for Kubernetes is a truly effective way to manage your clusters, making them versionable, testable and scalable.

type: what-is
page_title: "Infrastructure as Code for Kubernetes"

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro
---

[Infrastructure as Code]({{< relref "/what-is/what-is-infrastructure-as-code" >}}) (IaC) means that you use code to define and manage your infrastructure automatically rather than with manual processes. In a broader sense, IaC allows you to effectively apply software engineering practices to your infrastructure. With IaC, you can automatically build, deploy and manage your infrastructure much more effectively and reliably than you can manually. IaC makes your whole infrastructure, including your Kubernetes clusters, versionable, testable and repeatable.

## What is Kubernetes?

[Kubernetes]({{< relref "/blog/kubernetes-fundamentals-part-one" >}}) is a container orchestration tool. Modern applications are increasingly built using containers, which are microservices packaged with their dependencies and configurations. Kubernetes is open-source software for deploying and managing those containers. Keeping containerized apps up and running can be complex because they often use many containers deployed across different machines. Kubernetes provides a way to schedule and deploy those containers—at scale. Those words “at scale” are important because they underline the need for IaC. A simple script or a point-and-click approach simply won’t work. Kubernetes demands an automated approach and an automated approach means IaC.

### The Kubernetes cluster

A [Kubernetes cluster]({{< relref "/blog/kubernetes-fundamentals-part-one#anatomy-of-a-cluster" >}}) is a set of node machines that run containerized applications. If you’re running Kubernetes, you’re running a cluster. At a minimum, a cluster contains a control plane and one or more compute machines, or nodes. The control plane maintains the desired state of the cluster, such as which applications are running and which container images they use. Nodes actually run the applications and workloads.

### Deployment

A [Deployment]({{< relref "/blog/kubernetes-fundamentals-part-one#deployment" >}}) is an abstraction of your deployment configuration. It specifies what container image your application is running, which version, the environment variables it needs, and so on. A deployment governs another two Kubernetes components: the Pod and the ReplicaSet.

### The Kubernetes Pod

A pod is the smallest Kubernetes building block. Within a cluster, a pod represents a process that’s running. The inside of a pod can have one or more containers.

### ReplicaSet

A ReplicaSet makes sure that an x number of pods are running at any given time.

### Services

Pods don’t know how to communicate with the outer world or to pods from other deployments. A service defines how you expose your pods and how other pods can discover your pods.

## General Benefits of Infrastructure as Code for Kubernetes

As we said, IaC is the only effective way to manage a Kubernetes cluster. The benefits you get are similar to the benefits you get from IaC for the rest of your infrastructure.

- **Tracking and Auditability.** IaC code can be stored in git repositories, and along with allowing automation, it also acts as a history of your infrastructure. You can test the IaC code and track who has made changes to the code.
- **Speed.** With IaC and automation you can provision Kubernetes clusters very quickly.
- **Reusability.** IaC code acts as a template that’s been tested and reviewed. You can predictably provision Kubernetes clusters across various regions in the cloud and easily deploy microservices on different Kubernetes clusters.
- **Consistency.** Manual provisioning always results in inconsistencies. IaC systemizes the provisioning process and guarantees that the same infrastructure is built over and over. Microservices will be deployed with the same configuration on different Kubernetes clusters.

## Evaluate Your Platform for Infrastructure as Code for Kubernetes

If you’re evaluating platforms that will help you adopt infrastructure as code for Kubernetes, make sure your final choice helps you adopt best practices for your Kubernetes infrastructure. Here are a few examples.

### Applications shouldn’t crash because a dependency isn’t ready.

Kubernetes starts all services concurrently, letting containers crash and restart until all the resources have started. Look for a platform that can attempt to start all services concurrently but also understands resource dependencies that can prevent a resource from starting. In other words, the platform should understand the correct starting order for a service.

### Prohibit naked pods

Pods not bound to a ReplicaSet or Deployment (known as naked pods) aren’t rescheduled if a node fails. An automated strategy to replace Pods is preferable to creating them directly. Your platform should help you write policies as code, where a policy is code that enforces your organization's cloud governance in terms of security, compliance, cost controls and so on. For example you can write a policy that checks for naked Pods.

### Keep your production clusters separate

Your production environment should be separate from other environments. One way to separate environments is to tag resources such as clusters and use a policy to enforce that the cluster is only used for production. Again, you want a platform that makes it easy to write policies that, for example, check to see if environments such as test or dev are in your production environment.

## Learn More

[Pulumi](/) streamlines Kubernetes cluster configuration, management, and app workload deployments to your clusters. With Pulumi infrastructure as code for Kubernetes you can, for example, manage your Kubernetes clusters, automate Kubernetes deployments and increase your productivity by using standard programming languages, IDEs and test frameworks. [Get started for free today]({{< relref "/docs/get-started" >}}), or check out our on-demand workshops for tutorials on [IaC and Kubernetes]({{< relref "/resources/from-zero-to-production-in-kubernetes" >}}).
