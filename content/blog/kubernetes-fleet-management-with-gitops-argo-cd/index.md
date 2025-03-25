---
title: "Kubernetes Fleet Management Made Easy with Pulumi and GitOps"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-03-26T07:54:32Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Learn how Imagine Learning optimized Kubernetes fleet management with Pulumi and GitOps, automating deployments to boost speed, reliability, and productivity.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - sara-huddleston

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - kubernetes
    - gitops
    - argo-cd
    - kubernetes-fleet-management


# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
    twitter:
    linkedin:

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Kubernetes adoption for managing containerized workloads continues to grow, and so does the complexity of Kubernetes fleet management. Imagine Learning, a digital-first K-12 education company, experience the same growing pains. Their struggled to scale their internal developer platform to meet their growing enterprise needs, leading them to reevaluate their approach to managing multiple Kubernetes clusters efficiently.

Learn how Imagine Learning transformed its Kubernetes fleet management using Pulumi and a GitOps bridge pattern with Argo CD. The outcome? Faster deployments, increased reliability, and reduced cognitive load for their teams.

<!--more-->

> [!INFO]
> Let's talk about Kubernetes and platform engineering with Pulumi. Meet us at:
>
> - **KubeCon Europe Booth S450** - [Request a 1:1 Demo](https://www.pulumi.com/kubecon-europe/)
> - **Google Next'25 booth 1589** - [Join us for a Happy House and/or Request your 1:1 Demo](https://www.pulumi.com/google-next/)
>
> Don’t miss the chance to see Pulumi in action, ask questions, and explore why Kubernetes + Pulumi go better together. 

## Challenges in Scaling the Internal Developer Platform and Kubernetes

Imagine Learning had an existing internal developer platform (IDP) that was not built to scale and meet its current enterprise needs. Before making any changes, they decided to evaluate their core challenges:

- **Limited visibility** into the current state of clusters, making it difficult to track and maintain consistency.
- **Fragmented deployment workflows** with multiple pipelines depending on the resource type.
- **High learning curve**, requiring developers to master an additional language for infrastructure provisioning.

These challenges are common among enterprises. Many have the same issues as they attempt to scale their Kubernetes environments, highlighting the need for a more robust, scalable, automated, and developer-friendly solution.

## Implementing the GitOps Bridge Pattern with Pulumi

To address these challenges and streamline Kubernetes fleet management, Imagine Learning adopted the GitOps bridge pattern, integrating Pulumi for infrastructure as code (IaC) and Argo CD for Kubernetes environment synchronization. This approach ensured infrastructure and application configurations remained consistent and automated.

### How the GitOps Bridge Pattern Works

The core of Imagine Learning's solution lies in the GitOps bridge pattern, which connects their infrastructure code (managed by Pulumi) with their Kubernetes environments (managed by Argo CD). Here's how it works:

- **Infrastructure as Code with Pulumi**: Imagine Learning uses Pulumi to define their infrastructure resources, such as AWS VPCs, EKS clusters, and other platform-specific resources, in their preferred programming language (in this case, TypeScript).
- **Bridging to Kubernetes**: Once the infrastructure resources are created, Imagine Learning takes the relevant outputs from their Pulumi code (e.g., IAM role ARNs) and pushes them into a Kubernetes Secret managed by Argo CD. This secret serves as the bridge between their infrastructure code and their Kubernetes environments.
- **GitOps with Argo CD**: Argo CD, a popular GitOps tool, picks up the changes in the Kubernetes Secret and automatically reconciles the desired state in the Kubernetes clusters, ensuring that the infrastructure and application configurations are in sync.
- **Automated Deployments with GitHub Actions**: Every Git merge triggers a Pulumi deployment that updates the Kubernetes Secret. Argo CD then detects the changes and applies them to the Kubernetes clusters.

This GitOps bridge pattern allows Imagine Learning to maintain a single source of truth for its infrastructure and application configurations. This ensures consistency and reliability across its Kubernetes environments, eliminates manual interventions, and reduces deployment risks.

## Why Imagine Learning Chose Pulumi

Imagine Learning selected Pulumi for its developer-first approach to Kubernetes fleet management, offering:

- **Familiar Programming Languages**—Pulumi allows developers to write infrastructure code in the same programming languages they use for their application code, such as TypeScript, Python, or Go. This reduces the need to learn domain-specific languages, reducing the cognitive load and context-switching required, enabling the team to be more productive.
- **Code Reusability** – Teams can manage multiple stacks (environments) with different configurations using the same codebase, promoting code reuse and maintainability.
- **Deploy to Multiple Regions or Clouds**—Imagine Learning uses this ability to deploy to multiple regions, such as US East 1, US East 2, and US West 2, within a single stack and to providers like GitHub to manage files within GitHub, allowing power automation.
- **Powerful Abstractions** – Pulumi provides powerful abstractions, such as the Crosswalk for AWS library, which encapsulates best practices for deploying resources like VPCs and EKS clusters. This allows the Imagine Learning team to focus on the high-level infrastructure design rather than the low-level details.
- **Seamless GitOps Integration** – Pulumi's integration with Git and GitHub enables Imagine Learning to leverage the GitOps bridge pattern, where their infrastructure code is the source of truth and automatically deployed through GitHub Actions.
- **Visibility and Auditability** – The Pulumi UI provides a clear history of infrastructure changes, allowing the team to quickly understand and review the history of their deployments in each one of their environments. It also allows them to see what is in the state since Pulumi manages the state and contains all its information.

## Technical Implementation of the GitOps Bridge Pattern

Let's dive into the technical implementation of Imagine Learning's GitOps bridge pattern using Pulumi.

{{< youtube "1Q3XPmenthg?rel=0" >}}

See the implementation examples below and [explore the demo code](https://github.com/blakeromano/gitops-bridge-demo) provided by Blake Romano, Imagine Learning.

### Defining Infrastructure with Pulumi

Imagine Learning uses Pulumi to define its infrastructure resources, such as VPCs and EKS clusters. Here's an example of how they create a VPC using the Crosswalk for AWS library:

```
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const vpc = new awsx.network.VPC("main-vpc", {
    cidrBlock: "10.0.0.0/16",
    numberOfAvailabilityZones: 3,
    natGatewayStrategy: "single_nat_gateway",
});
...
```

### Updating Kubernetes Configurations Dynamically

Imagine Learning also uses Pulumi to dynamically update Kubernetes resources based on the infrastructure they've created. For example, they update the AWS EKS ConfigMap with the IAM role ARN created in their Pulumi code:

```
const eksConfigMap = new k8s.core.v1.ConfigMap("eks-config-map", {
    metadata: { name: "aws-auth", namespace: "kube-system" },
    data: { mapRoles: JSON.stringify([{ rolearn: eksCluster.roleArn, username: "system:node:{{EC2PrivateDNSName}}", groups: ["system:bootstrappers", "system:nodes"] }]) }
});
...
```

### Bridging to Kubernetes with Argo CD

To bridge the gap between their infrastructure code and Kubernetes, Imagine Learning uses Argo CD to manage a Kubernetes secret that contains the relevant metadata from their Pulumi deployments. Here's an example of how they create this secret:

```
const clusterSecret = new k8s.core.v1.Secret("cluster-secret", {
metadata: {
name: "cluster-secret",
annotations: {
"pulumi.com/secret": "true",
"pulumi.com/secret-encryption-context": JSON.stringify({
"pulumi:project": pulumi.getProject(),
"pulumi:stack": pulumi.getStack(),
}),
},
},
type: "Opaque",
stringData: {
"eks-cluster-name": eksCluster.name,
"eks-cluster-arn": eksCluster.arn,
"eks-cluster-endpoint": eksCluster.endpoint,
"eks-cluster-certificate-authority": eksCluster.certificateAuthority.data,
},
}, { provider: k8s.provider });
...
```

In this example, Imagine Learning is creating a Kubernetes secret that contains the relevant metadata from their EKS cluster deployment, such as the cluster name, ARN, endpoint, and certificate authority. They use Pulumi's GitHub provider to manage this secret in a Git repository, ensuring that the desired state of their infrastructure is tracked in version control.

### Automating Deployments with GitHub Actions

To streamline their deployment process, Imagine Learning leverages GitHub Actions to automate the deployment of their infrastructure changes. When a pull request is merged into the main branch, the GitHub Actions workflow triggers a Pulumi deployment, which in turn updates the Kubernetes secret in the Git repository. Argo CD then detects the changes and applies them to the Kubernetes clusters.

This automated deployment process allows Imagine Learning to quickly and reliably deploy changes to all of their Kubernetes environments, reducing the manual effort and the risk of inconsistencies between their infrastructure and application configurations.

## Results:  Faster Deployments, Increased Reliability, and Reduced Cognitive Load

Imagine Learning's adoption of the GitOps bridge pattern with Pulumi and Argo CD has transformed their Kubernetes fleet management capabilities:

- **Faster Deployments** –  Imagine Learning can deploy changes to all their Kubernetes environments within 5-10 minutes.
- **Increased Reliability** – Improved deployment trust since the team can easily preview changes and validate the desired state before merging to the main branch.
- **Reduced Cognitive Load** – Using Pulumi, Imagine Learning's developers can write infrastructure code in the same programming languages they use for their application code, eliminating the need to learn a new language and reducing context-switching.
- **GitOps Continuity**  – The GitOps bridge pattern has allowed Imagine Learning to maintain a consistent GitOps approach across its infrastructure code and Kubernetes configurations, ensuring a unified source of truth.
- **Automatic Change Propagation** – Updates to the infrastructure code in Pulumi automatically propagate to the Kubernetes environments through the Argo CD-managed Kubernetes secret, reducing the manual effort required to keep environments in sync.
- **Built-in Auditing** – The team can quickly check and understand the changes to the environments.
- **Faster Environment Provisioning** – Building new environments used to take weeks or months now, they can be spun up in hours or minutes.

## Conclusion

Imagine Learning's journey with Pulumi and the GitOps bridge pattern is an example of how organizations can overcome the scalability growing pains of internal developer platform and the challenges of Kubernetes fleet management. By bridging infrastructure provisioning with Kubernetes orchestration, Imagine Learning improved deployment speed, reliability, and developer productivity.

Adopting Pulumi and GitOps can unlock scalability, automation, and operational efficiency for organizations facing similar Kubernetes fleet management challenges. If you're interested in learning more about Pulumi and the GitOps bridge pattern, be sure to check

- Get started with [Pulumi Tutorials](https://www.pulumi.com/tutorials/)
- Attend an [upcoming workshop](https://www.pulumi.com/events/#upcoming)
- But most importantly, [try Pulumi](https://app.pulumi.com/signup) today!

Explore how you can leverage the power of Pulumi and GitOps bridge pattern to scale, simplify, and streamline your Kubernetes fleet management.
