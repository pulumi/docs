---
title: Self-Hosted Pulumi Service
menu:
    userguides:
        identifier: self_hosted
        weight: 9
meta_desc: Pulumi Business Critical Edition gives you the option to self-host Pulumi within your organization's infrastructure.
---

{{% notes type="info" %}}
Self-hosting is available in the **Pulumi Business Critical** edition and when using the open source, self-managed backends. If you would like to evaluate the Self-Hosted Pulumi Service, sign up for the [30 day trial]({{< relref "/product/self-hosted#self-hosted-trial" >}}) or [contact us]({{< relref "/contact.md" >}}). To use a open source, self-managed backend, such as a cloud storage bucket, see [State and Backends]({{< relref "/docs/intro/concepts/state" >}}).
{{% /notes %}}

This guide presents the overall architecture for self-hosting the Pulumi Service as well as available reference architectures and related installers.

## Managed Pulumi Service vs Self-Hosted Pulumi Service

Pulumi Service (i.e., [app.pulumi.com](https://app.pulumi.com)) is a fully managed SaaS providing state management, a secrets manager and features such as single sign-on (SSO), audit logs, centralized stack and policy management to name a few. As a SaaS, Pulumi manages all aspects of the service.

The self-hosted version of the service provides all the same capabilities as the SaaS offering. The self-hosted deployment requires that the customer manages data backups and keeping the service running and up to date.  However, the self-hosted solution allows the customer to run the service fully within their own environment.

If you are unsure about whether a self-hosted version of the Pulumi Service is right for your organization, [contact us]({{< relref "/contact.md" >}}) to learn more.

## Deployment Topology

Pulumi can be installed in almost any on-premise or cloud provider environment. The self-hosted install can be integrated with your preferred identity provider as well, such as:

* GitHub Enterprise
* GitLab Enterprise
* SAML SSO
* Email/password identity

Here are some examples of deployment topologies:

{{< figure src="/images/docs/guides/self-hosted/on-prem-internet-config.png" caption="Internet-Accessible Deployment" >}}

{{< figure src="/images/docs/guides/self-hosted/on-prem-intranet-config.png" caption="Intranet-Only Deployment" >}}

## Deployment Options

The Pulumi Service [Docker container images]({{< relref "components" >}}) can be run using any OCI-compatible container orchestrator.

However, Pulumi provides [installers](https://github.com/pulumi/pulumi-self-hosted-installers) to support common deployment environments:

* [Quickstart Docker Compose Install]({{< relref "quickstart-docker-compose" >}}): Using a Pulumi-provided set of docker-compose files and bash scripts, one can deploy a small system for **testing** in a local Docker environment.
* [ECS-Hosted Install]({{< relref "ecs-hosted" >}}): Using a Pulumi-provided set of Pulumi programs written in TypeScript or Go, one can automate the deployment and maintenance of a production-grade self-hosted solution.
* [EKS-Hosted Install]({{< relref "eks-hosted" >}}): Using a Pulumi-provided set of Pulumi programs written in TypeScript, one can automate the deployment and maintenance of a production-grade self-hosted solution running on Amazon Elastic Kubernetes Sevice (EKS). This solution most closely matches the managed service deployment model.
* [AKS-Hosted Install]({{< relref "aks-hosted" >}}): Using a Pulumi-provided set of Pulumi programs written in TypeScript, one can automate the deployment and maintenance of a production-grade self-hosted solution on Azure Kubernetes Service (AKS).
* [Local-Docker Install]({{< relref "local-docker" >}}): Using a Pulumi-provided Pulumi program written in TypeScript, one can automate the deployment and maintenance of a production-grade self-hosted solution using a customer-provided docker environment,  a customer-provided MySQL database and a customer-provided object store (e.g. Minio).

## Components

The Pulumi self-hosted [Components]({{< relref "components" >}}) consist of Docker images for the Pulumi Service's frontend UI and backend API.
