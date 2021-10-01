---
title: "re:Invent 2020 EKS Feature Releases"
date: 2020-12-07
meta_desc: "A recap of the re:Invent 2020 EKS announcements and their impacts"
meta_image: reinvent-2020.png
authors:
    - sophia-parafina
tags:
    - kubernetes
    - aws
    - pulumi-events
---

Amazon announced several Elastic Kubernetes Service feature releases and updates during the first week of AWS re:Invent 2020. If we look at all the announcements as a whole, we can see the Kubernetes ecosystem maturing to make deployments and management easier for organizations. Let's take a look at how they can benefit your use of EKS.

<!--more-->

## Amazon EKS Distro

First and foremost is the release of Amazon EKS Distro, also called EKS Anywhere. This is the same Kubernetes distro available to Amazon EKS customers on AWS as an open-source project. You can take advantage of a fully supported Kubernetes distribution built from open source with version aligned dependency updates and Common Vulnerabilities and Exposures (CVE) patches. Notifications for patches are sent from Amazon Simple Notification Service (SNS) with support for backported patches. Read more about [EKS Distro](https://aws.amazon.com/blogs/opensource/introducing-amazon-eks-distro/) here.

You can create a cluster using kubeadm, kops, or tools such as Pulumi. Learn more about creating infrastructure with EKS Distro and Pulumi on our [blog]({{< relref "/blog/amazon-eks-distro" >}}).

## Logging support for AWS Fargate

Amazon EKS pods running on AWS Fargate can now forward container logs to various AWS services, including Cloudwatch, S3, Elasticsearch, and Kinesis, to enable log storage and analytics. EKS with Fargate includes a native log router, eliminating the need for a sidecar. You can use ConfigMap to send routers to the service of your choice. Read more about it on the AWS [blog post](https://aws.amazon.com/blogs/containers/fluent-bit-for-amazon-eks-on-aws-fargate-is-here/).

## Simplified install and management for Kubernetes CNI plugin

Amazon EKS now supports installation and management of the [VPC CNI](https://docs.aws.amazon.com/eks/latest/userguide/pod-networking.html). The AWS VPC CNI provides integrated AWS Virtual Private Cloud (VPC) networking for Kubernetes clusters. You can use AWS VPC networking and security best practices for building Kubernetes clusters that include VPC routing policies and security groups for network traffic isolation.

You can install and manage the CNI plugin with the Amazon EKS console, CLI, and API. Previously, you needed to install and maintain it manually after a Kubernetes upgrade. Amazon EKS lets you install, manage, and through the EKS console, CLI, and API, where it is validated by AWS and can be deployed and updated.  To learn more, read the [announcement](https://aws.amazon.com/blogs/containers/introducing-amazon-eks-add-ons/).

## EC2 Spot Instances in managed node groups

Spot Instances are deeply discounted On-Demand EC2 instances. EKS now supports using Spot Instances with EKS managed node groups. If you are running batch process such as ETL with Apache Spark or stateless endpoint, Spot Instances are a cost-effective way for managing surge requests in EKS.

Previously, to use Spot Instances, you had to manually configure EC2 Auto Scaling groups and upgrade the Spot nodes to the current version of Kubernetes. You can now set capacity type as SPOT and the EC2 instance types when creating a managed node group. The managed node group will provision and manage Spot nodes automatically according to best practices. You can create the node group through the EKS console, the EKS API, and eksctl. To learn more about configuring EKS node groups with Spot Instance, read the [blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-provisioning-and-managing-ec2-spot-instances-in-managed-node-groups/).

{{% notes %}}
Want some hands-on training with EKS? Join our workshop on Thursday, December 10th where you will create a production-ready EKS cluster, install add-ons to prepare your cluster for developers, and finally ship an application to your cluster. [Register Now]({{< relref "/events-workshops/building-a-kubernetes-platform-in-amazon-eks" >}})
{{% /notes %}}
