---
title_tag: "Kubernetes & Pulumi"
meta_desc: Pulumi offers full support for Kubernetes, with a provider, an operator, 3+ components, multiple templates, and several guides.
title: "Kubernetes"
meta_image: /images/docs/meta-images/docs-clouds-kubernetes-meta-image.png
h1: Kubernetes & Pulumi
menu:
  clouds:
    identifier: kube
    weight: 4
cloud_overview: true
description: Streamline Kubernetes cluster configuration, management, and application workload deployments using TypeScript, Python, Go, C#, Java or YAML. Use the Pulumi Kubernetes Operator to manage both Kubernetes and cloud resources.
get_started_guide:
  link: get-started/
  icon: kubernetes
providers:
  description: The Kubernetes provider can provision any resources available in the Kubernetes API. 
  provider_list:
  - display_name: Kubernetes
    content_links:
    - display_name: Overview
      icon: page-small-black
      url: kubernetes/
    - display_name: Install & config
      icon: gear-small-black
      url: kubernetes/installation-configuration/
    - display_name: API docs
      icon: book-small-black
      url: kubernetes/api-docs/
    - display_name: How-to guides
      icon: question-small-black
      url: kubernetes/how-to-guides/
components:
- display_name: Kubernetes Cert Manager
  url: kubernetes-cert-manager/
  description:
- display_name: Kubernetes CoreDNS
  url: kubernetes-coredns/
  description:
- display_name: Pulumi Kubernetes Extensions
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
  description:
  external_link: true
convert:
- heading: Convert Kubernetes YAML to Pulumi
  description: Convert or generate Kubernetes YAML manifests in the language of your choice with Pulumi's tools.
  tools:
  - display_name: Convert Kubernetes YAML manifests to Pulumi
    url: /kube2pulumi/
  - display_name: Generate types in Pulumi for Custom Resources
    url: /blog/introducing-crd2pulumi/
templates:
- display_name: Kubernetes cluster on AWS
  url: kubernetes/aws/
- display_name: Kubernetes cluster on Azure
  url: kubernetes/azure/
- display_name: Kubernetes cluster on Google Cloud
  url: kubernetes/gcp/
- display_name: Helm Chart on Kubernetes
  url: kubernetes-application/helm-chart/
- display_name: Web application on Kubernetes
  url: kubernetes-application/web-application/
guides-description: Learn how to use Pulumi & Kubernetes together.
guides:
  description: Learn how to use Kubernetes & Pulumi together.
  guides_list:
  - display_name: Crosswalk playbooks for Kubernetes
    url: guides/playbooks/
  - display_name: Control plane
    url: guides/control-plane/
  - display_name: Worker node creation
    url: guides/worker-nodes/
  - display_name: Accessing clusters
    url: guides/try-out-the-cluster/
  - display_name: Kubernetes cluster defaults
    url: guides/configure-defaults/
  - display_name: Kubernetes access control
    url: guides/configure-access-control/
  - display_name: Kubernetes cluster services
    url: guides/cluster-services/
  - display_name: Kubernetes App services
    url: guides/app-services/
  - display_name: Updating Kubernetes worker nodes
    url: guides/update-worker-nodes/
  - display_name: Kubernetes identity and access management (IAM)
    url: guides/identity/
  - display_name: Kubernetes Apps
    url: guides/apps/
  - display_name: Kubernetes infrastructure services
    url: guides/managed-infra/
  - display_name: Kubernetes FAQ
    url: guides/faq/
kubernetes_cluster_management:
  heading: Cluster management
  description: The following SDKs are available to work with IaaS resources, and managed or self-managed Kubernetes clusters. The packages are available in Node.js (Javascript and Typescript), Python, Go, .NET and Java.
  links:
    - display_name: AWS
      has_arrow: true
      url: https://github.com/pulumi/aws/
      icon: aws
      external_link: true
    - display_name: Azure
      has_arrow: true
      url: https://github.com/pulumi/pulumi-azure-native/
      icon: azure
      external_link: true
    - display_name: DigitalOcean
      has_arrow: true
      url: https://github.com/pulumi/pulumi-digitalocean/
      icon: digitalocean
      external_link: true
    - display_name: Google Cloud
      has_arrow: true
      url: https://github.com/pulumi/gcp/
      icon: google-cloud
      external_link: true
kubernetes_operator:
  heading: Pulumi Kubernetes Operator
  description_1: The Pulumi Kubernetes Operator is an extension pattern that enables Kubernetes users to create a Stack as a first-class API resource, and use the StackController to drive the updates of the Stack until success.
  description_2: Deploying Pulumi stacks in Kubernetes provides the capability to build out CI/CD and automation systems into your clusters, creating native support to manage your infrastructure alongside your Kubernetes workloads.
  links:
  - display_name: GitHub repository
    has_arrow: true
    url: https://github.com/pulumi/pulumi-kubernetes-operator
    icon: github-small
    external_link: true
  - display_name: Get started with Pulumi Kubernetes Operator
    url: /docs/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/
    icon: light-bulb-small-gray
---
