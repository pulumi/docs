---
title: "re:Invent 2020 Tech Takeaways"
date: 2020-12-21
meta_desc: "A summary of product releases announced at AWS re:Invent 2020."
meta_image: reinvent-2020.png
authors:
    - sophia-parafina
tags:
    - AWS re:Invent
    - observability
    - chaos engineering

---

This was the year of virtual conferences and AWS re:Invent 2020 was no exception. We missed seeing our friends and customers, and mostly we missed introducing Pulumi and infrastructure as code at the booth and in hallway conversations. In an earlier article, we reviewed  the AWS Kubernetes announcements that will have a definite impact in the coming year. In this article, we'll take a look at Werner Vogel's, Amazon VP and CTO, keynote address.

<!--more-->

## Technology Announcements

Werner announced several new services that demonstrate AWS' commitment to building robust and sustainable infrastructure while reducing complexity.

### VPC Reachability Analyzer

Virtual networking can be complex especially in applications that require controlling access to resources. For example, your application may use a public gateway and private subnets for databases and application servers that should not be exposed to the Internet. This is typically done through security groups, access control lists, and IAM policies. Your application may also depend on services outside the VPC such as AWS Lambda or S3 storage.

Having fine grain control over your virtual network enables you to build robust, secure, and efficient infrastructure. However, the challenge of securing your virtual network can lead to connectivity issues due to conflicts or mismatches in configuration of resources. The [VPC Reachability Analyzer](https://aws.amazon.com/blogs/aws/new-vpc-insights-analyzes-reachability-and-visibility-in-vpcs/) can diagnose connectivity issues without sending a single packet. This is possible because of Amazon's investments in [automated reasoning](https://www.amazon.science/latest-news/how-awss-automated-reasoning-group-helps-make-aws-and-other-amazon-products-more-secure) which creates a [mathematical model](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/) for analyzing a set of rules and ensuring that all conditions are satisfied. You can add the VPC Reachability Analyzer to your devops toolchain to troubleshoot your networks.

### Fault Injector Simulator

Chaos engineering began with the [Netflix engineering](https://www.gremlin.com/chaos-monkey/the-origin-of-chaos-monkey/) idea that "to avoid failure you must fail constantly. Distributed microservice architectures increase the complexity of infrastructure, making it difficult to pinpoint bottlenecks and points of failure. Chaos engineering stresses testing or production environments to proactively find these issues.

The AWS [Fault Injector Simulator](https://aws.amazon.com/fis/) is a managed chaos engineering service. The Fault Injector Simulator uses pre-built templates to generate service disruptions to show how the system responds and can be used to generate recommendations to ameliorate performance and scaling issues. These experiments can be run in production because it provides guardrails that enable roll backs and automated stopping points if certain conditions are met.

### Amazon Managed Service for Prometheus and Grafana

Observability is the process of understanding the state of a system's internal components based on it's outputs. The complexity of cloud infrastructure necessitates observability to ensure that resources are healthy and running as expected. This is especially true of container based infrastructure where the basic unit of compute, the container, is ephemeral and replaced frequently.

[Prometheus](https://prometheus.io/) is a popular open source monitoring solution for container architectures that enables collection of time series data. AWS released [Amazon Managed Service for Prometheus (AMP)](https://aws.amazon.com/blogs/aws/join-the-preview-amazon-managed-service-for-prometheus-amp/) which is a manage Prometheus service that can easily scale to ingest, store, and query millions of time series metrics. AMP is fully compatible with Prometheus and supports PromQL queries, the same metrics, and Prometheus exporters.

Prometheus is often paired with [Grafana](https://grafana.com/) to create dashboards for the metrics collected with Prometheus. AWS also released [Amazon Managed Service for Grafana (AMG)](https://aws.amazon.com/blogs/aws/announcing-amazon-managed-grafana-service-in-preview/) which manages provisioning, setup, maintenance, and scaling as a cloud service. In addition to using Grafana with Prometheus, it also supports other AWS data sources such as Amazon ElasticSearch Service and Cloudwatch.

The release of AMP and AMG as cloud services provides a single source for implementing observability for your infrastructure.

### CloudShell

It's common practice to use a CLI tool to deploy and maintain infrastructure. However, there are instances when you either don't have access to your shell environment or are working remotely. [AWS CloudShell](https://aws.amazon.com/blogs/aws/aws-cloudshell-command-line-access-to-aws-resources/) lets you open an AWS enabled shell in your browser complete with Python and Node runtimes.

CloudShell is based on the Amazon Linux2 and comes with 1 GB of storage per shell in each region, this includes .bashrc, shell history files, and dot files for configuring your environment. Shells are accessible vi SSO or as a principal that can log into the AWS Management Console.

CloudShell has the following features:

- A CloudShell session times out after 20 minutes of inactivity.
- It is available in these regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Ireland), and Asia Pacific (Tokyo) Regions.
- Persistent Storage has a limit of 1 GB per region; all other storage is ephemeral
- Sessions can make outbound connections to the Internet, but do not allow any type of inbound connections.
- Runtimes include Python, Node, Bash, PowerShell, jq, git, the ECS CLI, the SAM CLI, npm, and pip already installed and ready to use.
- Ten concurrent shells in each region are available at no charge.

Check out how you can use CloudShell with Pulumi on [Modern Infrastructure Wednesdays](https://www.youtube.com/playlist?list=PLyy8Vx2ZoWloyj3V5gXzPraiKStO2GGZw).

{{< youtube eAGNFN5NcL4 >}}
