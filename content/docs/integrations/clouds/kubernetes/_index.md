---
title_tag: "Kubernetes | Pulumi Integrations"
meta_desc: Kubernetes integration with Pulumi — providers, packages, the Pulumi Kubernetes Operator, architecture templates, and ESC integrations.
title: Kubernetes
linktitle: Kubernetes
h1: Kubernetes
meta_image: /images/docs/meta-images/docs-clouds-kubernetes-meta-image.png
menu:
  integrations:
    name: Kubernetes
    identifier: kubernetes-clouds
    parent: integrations-clouds
    weight: 4
aliases:
- /docs/iac/clouds/kubernetes/
- /docs/clouds/kubernetes/
---

Manage Kubernetes clusters, deploy application workloads, and drive in-cluster automation with Pulumi. This page links to every Pulumi capability for Kubernetes: Infrastructure as Code, the Pulumi Kubernetes Operator, and ESC integrations.

To start from scratch, follow the [Kubernetes get-started guide](/docs/iac/get-started/kubernetes/).

## Infrastructure as Code

[Pulumi IaC](/docs/iac/) lets you define cloud infrastructure using TypeScript, Python, Go, C#, Java, or YAML — with deterministic deployments, a state backend, and a rich ecosystem of packages.

- [Kubernetes provider](/registry/packages/kubernetes/) — provision any resource available in the Kubernetes API.
- [Helm charts](/registry/packages/kubernetes/api-docs/helm/v4/chart/) — deploy Helm charts via the Kubernetes provider, with full lifecycle management and value inputs as typed Pulumi resources.
- [Kubernetes YAML manifests](/registry/packages/kubernetes/api-docs/yaml/v2/configfile/) — apply existing YAML manifests (single file or [a whole directory](/registry/packages/kubernetes/api-docs/yaml/v2/configgroup/)) through the Kubernetes provider without rewriting them.
- [Kubernetes Cert Manager](/registry/packages/kubernetes-cert-manager/) — higher-level component for installing cert-manager.
- [Kubernetes CoreDNS](/registry/packages/kubernetes-coredns/) — higher-level component for installing CoreDNS.
- [Docker](/registry/packages/docker/) — build and push Docker images to any registry.
- [crd2pulumi](/docs/integrations/clouds/kubernetes/crd2pulumi/) — generate typed SDKs for Kubernetes Custom Resource Definitions.

### Cluster management packages

Use a cloud provider package to create and manage Kubernetes clusters on your preferred infrastructure:

- [Amazon EKS](/registry/packages/eks/) — high-level EKS component.
- [AWS provider](/registry/packages/aws/) — lower-level EKS resources.
- [Azure Native provider](/registry/packages/azure-native/) — for AKS.
- [Google Cloud provider](/registry/packages/gcp/) — for GKE.
- [DigitalOcean provider](/registry/packages/digitalocean/) — for DigitalOcean Kubernetes.

## Pulumi Kubernetes Operator

The [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) enables Kubernetes users to create a Pulumi `Stack` as a first-class API resource, with a controller that drives updates to success. This lets you build CI/CD and automation into your clusters and manage infrastructure alongside your Kubernetes workloads. See the [GitHub repository](https://github.com/pulumi/pulumi-kubernetes-operator) for source and releases.

## Architecture templates

[Pulumi templates](/templates/) are ready-to-deploy starting points for common architectures. Run `pulumi new <template>` to bootstrap a new project.

Start new Kubernetes projects from a pre-built template:

- [Kubernetes cluster on AWS](/templates/kubernetes/aws/)
- [Kubernetes cluster on Azure](/templates/kubernetes/azure/)
- [Kubernetes cluster on Google Cloud](/templates/kubernetes/gcp/)
- [Helm chart on Kubernetes](/templates/kubernetes-application/helm-chart/)
- [Web application on Kubernetes](/templates/kubernetes-application/web-application/)

## Secrets & configuration (ESC)

[Pulumi ESC (Environments, Secrets, and Configuration)](/docs/esc/) is a centralized service for managing secrets, configuration, and short-lived credentials. It integrates with Kubernetes to deliver ESC-managed values into cluster workloads.

- [Kubernetes cluster access](/docs/esc/integrations/kubernetes/kubernetes/) — centrally manage kubeconfig files and cluster credentials for `kubectl`, `helm`, and Pulumi programs.
- [Kubernetes External Secrets Operator integration](/docs/esc/integrations/kubernetes/external-secrets-operator/) — sync Pulumi ESC values into Kubernetes secrets via External Secrets Operator.
- [Kubernetes Secret Store CSI driver integration](/docs/esc/integrations/kubernetes/secret-store-csi-driver/) — mount ESC values into pods via the Secret Store CSI driver.

## Policy packs

[Pulumi Policies](/docs/insights/policy/) lets you enforce rules on infrastructure at preview and update time, rejecting stacks that violate security, cost, or compliance standards. [Pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) are maintained by Pulumi and cover common regulatory and best-practice frameworks.

For Kubernetes:

- [CIS Kubernetes Benchmark on AWS](/docs/reference/pre-built-policy-packs/cis-kubernetes/aws/) — for EKS.
- [CIS Kubernetes Benchmark on Azure](/docs/reference/pre-built-policy-packs/cis-kubernetes/azure/) — for AKS.
- [CIS Kubernetes Benchmark on Google Cloud](/docs/reference/pre-built-policy-packs/cis-kubernetes/google-cloud/) — for GKE.

## Migration

Migrate existing Kubernetes infrastructure from another IaC tool to Pulumi.

- [From Kubernetes YAML](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/) — convert YAML manifests to Pulumi programs in your preferred language.
- [From Terraform](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) — convert Terraform HCL and state to Pulumi.
