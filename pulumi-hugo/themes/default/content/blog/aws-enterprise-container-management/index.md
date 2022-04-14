---
title: AWS Enterprise Container Management with Pulumi

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-04-14

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
meta_desc: We're excited to be launch partners for the new Enterprise Container Management category of the AWS Container Competency program.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - isaac-harris

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - aws
    - containers
    - kubernetes

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---

Managing containers and Kubernetes clusters are consistently popular topic areas on the Pulumi blog and in our docs. Our customers regularly cite that Pulumi simplifies container management scenarios, making it the primary reason for choosing Pulumi to define, deploy and manage all of their cloud resources. This includes teams that are just starting their cloud journey and spinning up their first project, as well as teams that want to modernize their apps and services with cloud-native architectures or even scale from one to many clouds.

We’re excited to be launch partners for the new [Enterprise Container Management category](https://aws.amazon.com/blogs/apn/aws-container-competency-expands-to-include-enterprise-container-management-category) of the AWS Container Competency program because it perfectly encapsulates Pulumi’s capabilities across the entire lifecycle of container-based architectures and applications. These scenarios are critical to the success of every cloud engineering and DevOps team and include provisioning, governance, security, and observability across [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks) (EKS) and [Amazon Elastic Container Service](https://aws.amazon.com/ecs) (ECS). Here is a handy guide to some of the features that make Pulumi a great Enterprise Container Management Solution and how Pulumi makes each container scenario easier for your team.

### Provisioning Container Infrastructure

Pulumi manages multi-region, multi-account, multi-cluster Kubernetes deployments with ease on any cloud.  With [Pulumi Crosswalk for Kubernetes]({{< relref "/docs/guides/crosswalk/kubernetes" >}}) we’ve provided a set of [Day 0 and Day 1 playbooks]({{< relref "/docs/guides/crosswalk/kubernetes/playbooks" >}}) that take the guesswork out of the provisioning process from creating a control plane to [deploying your apps]({{< relref "/docs/guides/crosswalk/kubernetes/apps" >}}) and updating workers.

### Managing AWS Container Services

Pulumi gives you the flexibility to pick the container services that meet the needs of your workloads and the requirements of your organization. Choosing the right services can be a challenge, so we’ve assembled a short overview to help you [get started managing AWS containers]({{< relref "/blog/managing-containers-on-aws-with-pulumi" >}}). Once you’ve chosen your scheduler, Pulumi has a host of examples to guide you through [deploying Amazon ECS]({{< relref "/docs/guides/crosswalk/aws/ecs" >}}) and [Amazon EKS]({{< relref "/docs/guides/crosswalk/aws/eks" >}}). There is also a [Pulumi EKS component]({{< relref "/registry/packages/eks" >}}) that provides multi-language convenience functions and boilerplate to simplify EKS deployments.

### Support for the Entire Kubernetes API

Once you’ve provisioned a cluster, the [Pulumi Kubernetes Provider]({{< relref "/registry/packages/kubernetes" >}}) enables you to provision any resource available in the Kubernetes API. This provides native support for features like [Helm]({{< relref "/registry/packages/kubernetes/api-docs/helm/v3/chart" >}}) as well as the ability to configure [Namespacing]({{< relref "/registry/packages/kubernetes/api-docs/core/v1/namespace" >}}) providing powerful multi-tenancy capabilities for your clusters.

### Cluster Observability

Logging and monitoring are critical capabilities for keeping tabs on the health and security of your clusters. Fortunately, Pulumi has a host of integrations that simplify these scenarios including open-source tools like [metrics-server](https://github.com/timmyers/pulumi-k8s-metrics-server) and [Prometheus]({{< relref "/registry/packages/kubernetes/how-to-guides/p8s-rollout" >}}) as well as support for industry-leading platforms like [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) and [Datadog](https://datadog.com).

### Authentication and Authorization

Adhering to the principle of least privilege for users and roles is an important step in securing your clusters and Pulumi has many capabilities to help you manage the complexities of authentication and authorization. For example, with Pulumi you can [create and manage AWS IAM roles]({{< relref "/docs/aws/iam" >}}) and you can integrate Pulumi Enterprise with your centralized identity and access management platform of choice via [SAML 2.0]({{< relref "/docs/guides/saml/sso" >}}) and [OIDC]({{< relref "/blog/eks-oidc" >}}).

### Centralized Governance and Compliance Controls

Many customers are using Pulumi and Kubernetes to stand up shared services platforms (SSP) to empower their developers to self-service new infrastructure environments. To keep these environments compliant with internal policies, Pulumi Business Critical Edition includes [CrossGuard]({{< relref "/docs/guides/crossguard" >}}) policy-as-code capabilities built-in.  This helps operators to ensure that configuration mistakes won’t reach production with policies that are enforced organization-wide.

### Support for Hybrid Deployments

Many users need to manage container-based workloads on AWS as well as on-prem and on other clouds. Fortunately, Pulumi has built-in support for [Amazon ECS Anywhere]({{< relref "/blog/ecs-anywhere-launch" >}}), so teams can use the familiar ECS control plane regardless of where their workloads need to run. Pulumi also supports the [EKS Distro]({{< relref "/blog/amazon-eks-distro" >}}) which brings the familiar managed Kubernetes capabilities of EKS to on-prem clusters.

### Automated Deployment of Infrastructure and Applications

One of the benefits of Pulumi is that it enables infrastructure and application development to leverage the same tooling and processes familiar to software engineers. Adding infrastructure to your CI/CD workflow is easy with Pulumi because it supports a wide variety of [test frameworks]({{< relref "/docs/guides/testing/unit" >}}), simplifies the process of integration testing using ephemeral environments, and includes a [CI/CD Integration Assistant]({{< relref "/docs/intro/pulumi-service/ci-cd-integration-assistant" >}}) to guide you through the process of connecting Pulumi to popular platforms such as [GitHub Actions]({{< relref "/docs/guides/continuous-delivery/github-actions" >}}), [AWS Code Services]({{< relref "/docs/guides/continuous-delivery/aws-code-services" >}}) and many more.

Once you have your cluster provisioned, you can also deploy workloads into your cluster with GitOps style workflows using the [Pulumi Kubernetes Operator]({{< relref "/docs/guides/continuous-delivery/pulumi-kubernetes-operator" >}}).

### Conclusion

This is just a sample of the many ways that Pulumi makes it easier than ever to manage containers and Kubernetes clusters in enterprise scenarios. [Give it a try]({{< relref "/docs/get-started" >}}) for yourself and let us know what you think in our [Community Slack](https://slack.pulumi.com).
