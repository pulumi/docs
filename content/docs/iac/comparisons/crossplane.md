---
title_tag: "Pulumi vs. Crossplane"
meta_desc: "Pulumi vs. Crossplane: Pulumi is a multi-language IaC platform; Crossplane is a Kubernetes-native control plane for managing cloud infrastructure."
title: Crossplane
h1: Pulumi vs. Crossplane
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Crossplane
        parent: iac-comparisons
        weight: 9
    concepts:
        identifier: vs-crossplane
        parent: vs
        weight: 10
aliases:
- /docs/reference/vs/crossplane/
- /docs/intro/vs/crossplane/
- /docs/concepts/vs/crossplane/
- /docs/iac/concepts/vs/crossplane/
---

Pulumi and [Crossplane](https://www.crossplane.io/) are both declarative infrastructure as code tools that provision resources across clouds and SaaS platforms, but they take different architectural approaches. Pulumi lets you define infrastructure in general-purpose languages (Python, TypeScript, JavaScript, Go, C#, Java, or YAML) and runs through a CLI or an embeddable SDK. Crossplane extends Kubernetes into a control plane: infrastructure is defined as Kubernetes resources in YAML and reconciled continuously by controllers running inside a cluster.

This page covers what each tool is, a feature-by-feature comparison, the most important differences in detail, and the available paths for adopting Pulumi alongside or instead of Crossplane.

## What is Pulumi?

{{< what-is-pulumi >}}

For users coming from Crossplane, Pulumi does not require a Kubernetes cluster to run, but it works well with Kubernetes when you need it: the first-party [Kubernetes provider](/registry/packages/kubernetes/) is generated from the upstream Kubernetes API schema and can manage any resource type, including Custom Resource Definitions (CRDs) — so a Pulumi program can install and operate Crossplane itself.

## What is Crossplane?

Crossplane is an open-source control plane framework that extends Kubernetes to provision and manage infrastructure across clouds and SaaS platforms. It was created by [Upbound](https://www.upbound.io/) and is a [graduated](https://www.cncf.io/projects/crossplane/) project of the Cloud Native Computing Foundation (CNCF). Crossplane is licensed under the [Apache License 2.0](https://github.com/crossplane/crossplane/blob/main/LICENSE).

With Crossplane, infrastructure is expressed as Kubernetes resources written in YAML and applied to a cluster, where controllers continuously reconcile the actual state of cloud resources toward the declared state. Cloud and service support comes from [Crossplane providers](https://docs.crossplane.io/latest/packages/providers/), many of which are generated from Terraform providers using the [Upjet](https://github.com/crossplane/upjet) code-generation framework; official providers exist for AWS, Azure, and Google Cloud. Reusable abstractions are built with [Composite Resource Definitions (XRDs) and Compositions](https://docs.crossplane.io/latest/composition/compositions/). State lives in the Kubernetes cluster's etcd datastore rather than in a separate state file.

[Crossplane v2](https://blog.crossplane.io/announcing-crossplane-2-0/), released in August 2025, made composite and managed resources namespaced by default, removed the separate "claim" concept, replaced patch-and-transform composition with [composition functions](https://docs.crossplane.io/latest/composition/composition-functions/), and allowed compositions to include any Kubernetes resource — not just Crossplane-managed infrastructure. Crossplane itself has no commercial tier; managed control planes and an enterprise distribution are offered by Upbound.

## Detailed comparison

| Feature | Pulumi | Crossplane |
| --- | --- | --- |
| Language support | Python, TypeScript, JavaScript, Go, C#, Java, and YAML — general-purpose languages with familiar syntax for loops, conditionals, and abstractions | [Kubernetes YAML manifests](https://docs.crossplane.io/latest/) for declaring resources; Go is used to build providers and composition functions |
| Cloud and service support | [Pulumi Registry](/registry/) of packages, including [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers); first-party native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/) generated from upstream API schemas; [any OpenTofu or Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) can be generated into a Pulumi SDK with `pulumi package add terraform-provider <name>` | [Crossplane providers](https://docs.crossplane.io/latest/packages/providers/) installed into the cluster as packages; official AWS, Azure, and Google Cloud providers plus community providers, many generated from Terraform providers via [Upjet](https://github.com/crossplane/upjet) |
| Transpiled to another format? | No — programs run directly in their host language | No — YAML manifests are reconciled directly by Crossplane controllers |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, Google Cloud Storage, local files, and others | Stored in the Kubernetes cluster's etcd datastore as the status of resource objects; no separate state file |
| Secrets management | [Encrypted in transit and at rest](/docs/iac/concepts/secrets/) in the state file by default, with per-stack encryption keys; pluggable KMS providers (AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault) | [Kubernetes Secrets](https://docs.crossplane.io/latest/guides/connection-details-composition/) for provider credentials and connection details; secret data is not encrypted as a first-class primitive and relies on the cluster's secret-handling configuration |
| Execution model | Local CLI, programmatic via [Automation API](/docs/iac/automation-api/), or remote runs in [Pulumi Deployments](/docs/deployments/) | Centralized: controllers run inside a Kubernetes cluster and reconcile resources continuously; changes are applied with `kubectl` or a GitOps workflow |
| Rollback on failed operation | Failed updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code | No transactional rollback; controllers retry continuously until resources converge, and you roll forward by reapplying corrected manifests |
| Programmatic API for tools and platforms | [Automation API](/docs/iac/automation-api/) — a programmatic SDK for building custom CLIs, internal developer platforms, and services that drive `up`, `preview`, and `destroy` without shelling out to the Pulumi CLI | The Kubernetes API itself is the programmatic interface; tools and platforms interact with Crossplane by creating and reading Kubernetes resources |
| Modularity and reuse | [Component Resources](/docs/iac/concepts/components/) authored in any supported language; [Pulumi Packages](/docs/iac/concepts/packages/) let a component written in one language be consumed from any Pulumi language; language-native package managers (npm, PyPI, NuGet, Maven, Go modules); and the [Pulumi Registry](/registry/) for publicly available packages | [Composite Resource Definitions (XRDs) and Compositions](https://docs.crossplane.io/latest/composition/compositions/) define reusable APIs; [composition functions](https://docs.crossplane.io/latest/composition/composition-functions/) add programmatic logic; packaged and distributed as [Crossplane configuration packages](https://docs.crossplane.io/latest/packages/configurations/) |
| Import existing resources | [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/), both of which generate code in your language | Existing resources are brought under management by applying a manifest with the appropriate [external-name annotation](https://docs.crossplane.io/latest/guides/import-existing-resources/) so the controller adopts them |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) — open source, with rules written in Python, TypeScript, or Open Policy Agent Rego; Pulumi Cloud commercial plans add centralized policy management plus [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for compliance frameworks like CIS, PCI DSS, and SOC 2 | No built-in policy-as-code; teams typically use Kubernetes admission-control tools such as [Open Policy Agent Gatekeeper](https://open-policy-agent.github.io/gatekeeper/) or [Kyverno](https://kyverno.io/) to enforce policy on Crossplane resources |
| Open source | Yes — [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | Yes — [Apache License 2.0](https://github.com/crossplane/crossplane/blob/main/LICENSE) |
| Commercial option | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) | None from the Crossplane project itself; managed control planes and an enterprise distribution are offered by [Upbound](https://www.upbound.io/) |

## Key differences

### Language support and the authoring experience

Crossplane infrastructure is declared in Kubernetes YAML manifests. The model is fully declarative and integrates naturally with `kubectl` and GitOps tooling, but YAML on its own has no loops, conditionals, or types; programmatic logic for reusable APIs is added through [composition functions](https://docs.crossplane.io/latest/composition/composition-functions/), which are written in a general-purpose language and run as part of the reconciliation pipeline. Pulumi programs are written directly in general-purpose languages, so authors get loops, conditionals, classes, package management, IDE features (autocomplete, type checking, refactoring, go-to-definition), and the testing frameworks that already exist in those ecosystems. Pulumi also supports [YAML](/docs/iac/languages-sdks/yaml/) for users who prefer a markup format.

### Cloud and service coverage

Both tools target broadly the same set of clouds and SaaS platforms but reach them differently. Crossplane installs [providers](https://docs.crossplane.io/latest/packages/providers/) into the cluster as packages; the official AWS, Azure, and Google Cloud providers, along with many community providers, are generated from Terraform providers using the [Upjet](https://github.com/crossplane/upjet) framework. Pulumi pulls from the [Pulumi Registry](/registry/), which includes [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers). Pulumi also maintains native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/), generated directly from each platform's API schema for same-day coverage of new resources. When a provider is not packaged in the Pulumi Registry, the [Any Terraform Provider](/docs/iac/concepts/providers/any-terraform-provider/) feature generates a typed Pulumi SDK from any provider in the OpenTofu or Terraform registry.

### Execution model and reconciliation

This is the most fundamental difference between the two tools. Crossplane runs as a set of controllers inside a Kubernetes cluster. Once a manifest is applied, the controllers reconcile continuously: they detect drift and correct it automatically without a person running a command, which makes Crossplane well suited to always-on, GitOps-driven platforms. The trade-off is that Crossplane requires a running Kubernetes cluster as part of its operational footprint.

Pulumi runs on demand. Changes are applied through the local CLI, programmatically through the [Automation API](/docs/iac/automation-api/), or remotely through [Pulumi Deployments](/docs/deployments/), and `pulumi preview` shows the exact set of changes before they are made. Drift is detected when you run `pulumi preview` or `pulumi refresh` rather than corrected continuously. Pulumi does not require any cluster or long-running service to operate, though Pulumi Cloud and Pulumi Deployments are available when you want a managed service. Neither tool performs a transactional rollback on a failed operation: Pulumi leaves the stack partially updated and reconciles on the next run, while Crossplane's controllers retry until resources converge.

### Secrets handling

Pulumi treats secrets as a first-class primitive. Values marked as secrets are encrypted in transit and at rest in the state file, anything derived from a secret is also encrypted, and each stack has its own encryption key. The default encryption provider can be replaced with [AWS KMS, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault](/docs/iac/concepts/secrets/#available-encryption-providers). Crossplane stores provider credentials and resource [connection details](https://docs.crossplane.io/latest/guides/connection-details-composition/) as standard [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/); how strongly those are protected depends on the cluster's secret-handling configuration (for example, etcd encryption at rest or an external secrets store), rather than being encrypted by Crossplane itself.

### Policy as code

[Pulumi Policies](/docs/insights/policy/) is open source and free. Policies can be written in Python, TypeScript, or Open Policy Agent Rego, and Pulumi Cloud adds centralized management, policy groups, and enforcement across stacks. Pulumi Cloud commercial plans also include [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for common compliance frameworks (CIS, PCI DSS, SOC 2, HITRUST, NIST). Crossplane has no built-in policy-as-code feature; because Crossplane resources are Kubernetes objects, teams typically enforce policy with Kubernetes admission controllers such as [Open Policy Agent Gatekeeper](https://open-policy-agent.github.io/gatekeeper/) or [Kyverno](https://kyverno.io/).

### Modularity and reuse

Crossplane's reuse model is the [Composite Resource Definition (XRD) and Composition](https://docs.crossplane.io/latest/composition/compositions/): an XRD defines a new high-level API, and a Composition specifies the resources that back it, with [composition functions](https://docs.crossplane.io/latest/composition/composition-functions/) supplying programmatic logic. These abstractions are packaged and distributed as [configuration packages](https://docs.crossplane.io/latest/packages/configurations/) and consumed as Kubernetes resources. Pulumi's [Component Resources](/docs/iac/concepts/components/) are runtime objects with explicit parent/child relationships, so a component and the resources inside it form a coherent unit in plan output, deletion, and state. Components can be authored in one language and consumed from any other supported language by publishing them as a [Pulumi Package](/docs/iac/concepts/packages/), and they are distributed through language-native package managers and the [Pulumi Registry](/registry/).

### Automation API

The [Automation API](/docs/iac/automation-api/) lets a host application drive Pulumi without shelling out to the CLI. Practical uses include embedding stack creation in a SaaS product, building an internal developer platform that provisions environments per team or per branch, generating ephemeral preview environments from CI, and orchestrating cross-cloud deployments where each step runs as part of a larger workflow. Crossplane exposes its functionality through the Kubernetes API instead: applications and platforms integrate with Crossplane by creating and reading Kubernetes resources, which is a natural fit for teams already building on Kubernetes APIs and controllers.

## When to choose Pulumi vs. Crossplane

**Choose Pulumi when** you:

1. Want to write infrastructure in a general-purpose language with the testing frameworks, package managers, and IDE tooling that already exist in that ecosystem.
1. Do not want to run and operate a Kubernetes cluster as a prerequisite for managing infrastructure.
1. Need an embeddable SDK ([Automation API](/docs/iac/automation-api/)) to drive deployments from a host application — internal developer platforms, SaaS products, or ephemeral preview environments per pull request.
1. Want first-class encrypted secrets with pluggable KMS providers and per-stack encryption keys.

**Choose Crossplane when** you:

1. Are standardizing on Kubernetes as a control plane and want infrastructure managed through the same API, RBAC, and GitOps workflows as your applications.
1. Want controllers that continuously reconcile and automatically correct drift without a person running a command.
1. Prefer to define infrastructure declaratively in YAML and consume reusable platform APIs as Kubernetes resources.

The two can also coexist — see [Adoption](#adoption-coexistence-conversion-and-import) below.

## Adoption: coexistence, conversion, and import

There are several common paths for adopting Pulumi alongside or in place of Crossplane, and they can be combined:

1. **Use Crossplane alongside Pulumi.** Because Crossplane and its resources are Kubernetes objects, a Pulumi program using the [Kubernetes provider](/registry/packages/kubernetes/) can install Crossplane, install providers, and apply Crossplane manifests — for example with [`ConfigGroup` or `ConfigFile`](/registry/packages/kubernetes/api-docs/yaml/v2/configgroup/) to apply existing YAML, or [`crd2pulumi`](/docs/integrations/clouds/kubernetes/crd2pulumi/) to generate typed SDKs from Crossplane CRDs. This lets a team manage the cluster and bootstrap Crossplane with Pulumi while keeping Crossplane-managed resources where they are.
1. **Convert YAML with `pulumi convert`.** [`pulumi convert --from kubernetes`](/docs/iac/concepts/converters/) translates Kubernetes YAML manifests, including Crossplane resources, into a Pulumi program in the language of your choice.
1. **Import existing resources.** [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/) bring already-provisioned cloud resources under Pulumi management and generate the corresponding code in your chosen language.

For a walkthrough of moving Kubernetes-based infrastructure to Pulumi, see [Migrating from Kubernetes to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/).

## Frequently asked questions

### Is Crossplane the same as Terraform?

No. They are different tools, though they are related: many Crossplane providers are generated from Terraform providers using the [Upjet](https://github.com/crossplane/upjet) framework, so they cover similar cloud APIs. The execution models differ — Terraform runs on demand through a CLI, while Crossplane runs as controllers inside a Kubernetes cluster that reconcile continuously. Crossplane uses Kubernetes YAML and the Kubernetes API rather than HCL and the Terraform CLI.

### Does Pulumi require Kubernetes?

No. Pulumi runs as a CLI or through the [Automation API](/docs/iac/automation-api/) and does not need a Kubernetes cluster to manage infrastructure. Crossplane, by contrast, runs its controllers inside a Kubernetes cluster, so a cluster is part of its operational footprint. Pulumi does have a first-party [Kubernetes provider](/registry/packages/kubernetes/) for teams that want to manage Kubernetes resources — including Crossplane itself — but it is optional.

### Can Pulumi deploy and manage Crossplane resources?

Yes. Crossplane, its providers, and the custom resources it defines are all Kubernetes objects, so Pulumi's [Kubernetes provider](/registry/packages/kubernetes/) can install Crossplane and apply Crossplane manifests. You can apply existing YAML with [`ConfigGroup` or `ConfigFile`](/registry/packages/kubernetes/api-docs/yaml/v2/configgroup/), or use [`crd2pulumi`](/docs/integrations/clouds/kubernetes/crd2pulumi/) to generate typed SDKs from Crossplane CRDs.

### How do I migrate from Crossplane to Pulumi?

You have options that can be combined: convert Crossplane YAML manifests with [`pulumi convert --from kubernetes`](/docs/iac/concepts/converters/), bring already-provisioned cloud resources under Pulumi management with [`pulumi import`](/docs/iac/guides/migration/import/), or run both tools side by side and migrate incrementally. See [Migrating from Kubernetes to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/) for a walkthrough.

### Is Pulumi free like Crossplane?

The Pulumi CLI and SDKs are open source under Apache 2.0 and free to use. [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) has a free Individual tier and paid plans that add managed state, RBAC, audit logs, policy management, and other features for running Pulumi at organizational scale. Crossplane itself is free under Apache 2.0; managed control planes and an enterprise distribution are sold separately by Upbound.

## Next steps

- [Get started with Pulumi](/docs/iac/get-started/)
- [Get started with Pulumi and Kubernetes](/docs/iac/get-started/kubernetes/)
- [Pulumi Kubernetes provider](/registry/packages/kubernetes/)
- [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
