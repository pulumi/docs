---
title_tag: "Pulumi vs. Kubernetes YAML Manifests"
meta_desc: "How Pulumi compares to Kubernetes YAML Manifests: a multi-cloud IaC platform in general-purpose languages versus Kubernetes' native declarative config format."
title: Kubernetes YAML Manifests
h1: Pulumi vs. Kubernetes YAML Manifests
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Kubernetes YAML Manifests
        parent: iac-comparisons
        weight: 7
        identifier: iac-comparisons-k8s-yaml
    concepts:
        identifier: vs-k8s-yaml
        parent: vs
        weight: 8
aliases:
- /docs/reference/vs/k8s_yaml_dsls/
- /docs/intro/vs/k8s_yaml_dsls/
- /docs/concepts/vs/k8s-yaml-dsls/
- /docs/iac/concepts/vs/k8s-yaml-dsls/
---

Pulumi and [Kubernetes YAML manifests](https://kubernetes.io/docs/concepts/overview/working-with-objects/) are both declarative ways to define the desired state of infrastructure. Pulumi lets you define infrastructure in general-purpose languages (Python, TypeScript, JavaScript, Go, C#, Java, or YAML) across any cloud or SaaS provider; Kubernetes YAML manifests are the native configuration format of the Kubernetes API and describe Kubernetes objects only.

This page covers what each tool is, a feature-by-feature comparison, the most important differences in detail, and the available paths for adopting Pulumi alongside or instead of Kubernetes YAML manifests.

## What is Pulumi?

{{< what-is-pulumi >}}

For users coming from Kubernetes YAML, Pulumi maintains a first-party [Kubernetes provider](/registry/packages/kubernetes/) generated from the Kubernetes OpenAPI spec, so every Kubernetes API object is available with the same fidelity as a hand-written manifest. The same Pulumi program can also provision the cluster itself and any non-Kubernetes cloud resources it depends on.

## What are Kubernetes YAML Manifests?

Kubernetes YAML manifests are the native declarative configuration format of the [Kubernetes](https://kubernetes.io/) API. Each manifest is a YAML (or JSON) document describing the desired state of a Kubernetes API object — a `Deployment`, `Service`, `ConfigMap`, `Namespace`, and so on. Manifests are applied to a cluster with `kubectl apply` or by a GitOps controller such as [Argo CD](https://argo-cd.readthedocs.io/) or [Flux](https://fluxcd.io/), and the Kubernetes control plane reconciles the cluster toward the state they describe.

Kubernetes is an open-source project governed by the [Cloud Native Computing Foundation](https://www.cncf.io/projects/kubernetes/) and licensed under Apache 2.0. Manifests target any conformant Kubernetes cluster — Amazon EKS, Azure AKS, Google GKE, or self-managed — but can only describe Kubernetes resources; cloud resources outside the cluster require separate tooling or an in-cluster operator. There is no separate state file: the live cluster, backed by etcd, is the source of truth, and `kubectl apply` tracks managed fields directly on each object. Manifests have no commercial product of their own — they are simply the input format of the Kubernetes API — and [Kustomize](https://kustomize.io/) is the common native tool for layering and patching them.

## Detailed comparison

| Feature | Pulumi | Kubernetes YAML Manifests |
| --- | --- | --- |
| Language support | Python, TypeScript, JavaScript, Go, C#, Java, and YAML — general-purpose languages with familiar syntax for loops, conditionals, and abstractions | YAML or JSON documents describing Kubernetes API objects; no loops, conditionals, or variables. [Kustomize](https://kustomize.io/) adds bases and overlays but remains declarative YAML |
| Cloud and service support | [Pulumi Registry](/registry/) of packages, including [bridged, native, parameterized, and dynamic providers](/docs/iac/concepts/providers/#types-of-providers); first-party native providers for [Kubernetes](/registry/packages/kubernetes/) and [Azure Native](/registry/packages/azure-native/) generated from upstream API schemas; [any Terraform provider](/docs/iac/concepts/providers/any-terraform-provider/) can be adapted into a Pulumi provider | Kubernetes API objects only, on any conformant cluster (EKS, AKS, GKE, or self-managed); non-Kubernetes cloud resources require separate tooling or an in-cluster operator such as [AWS Controllers for Kubernetes](https://aws-controllers-k8s.github.io/community/) or [Crossplane](https://www.crossplane.io/) |
| Transpiled to another format? | No — programs run directly in their host language | No — manifests are sent directly to the Kubernetes API server |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, Google Cloud Storage, local files, and others | No separate state file; the live cluster (etcd) is the source of truth, and `kubectl apply` records managed fields via [server-side apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/) |
| Secrets management | [Encrypted in transit and at rest](/docs/iac/concepts/secrets/) in the state file by default, with per-stack encryption keys; pluggable KMS providers (AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault) | Kubernetes [`Secret`](https://kubernetes.io/docs/concepts/configuration/secret/) objects are base64-encoded, not encrypted, in the manifest; [encryption at rest in etcd](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) is configured separately at the cluster level |
| Execution model | Local CLI, programmatic via [Automation API](/docs/iac/automation-api/), or remote runs in [Pulumi Deployments](/docs/deployments/) | Local `kubectl` CLI against a cluster, or a GitOps controller (Argo CD, Flux) running inside the cluster; no centralized service ships with Kubernetes itself |
| Rollback on failed operation | Failed updates leave the stack in a partially-updated state; subsequent `pulumi up` runs reconcile toward the desired state, and you can roll forward by reverting program code | `kubectl apply` has no transactional rollback; workload controllers support [`kubectl rollout undo`](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment) for revision history, and re-applying a previous manifest reconciles back |
| Programmatic API for tools and platforms | [Automation API](/docs/iac/automation-api/) — a programmatic SDK for building custom CLIs, internal developer platforms, and services that drive `up`, `preview`, and `destroy` without shelling out to the Pulumi CLI | The [Kubernetes API](https://kubernetes.io/docs/reference/using-api/) and client libraries operate on individual objects, but there is no orchestration SDK for driving a full apply/preview/destroy lifecycle |
| Modularity and reuse | [Component Resources](/docs/iac/concepts/components/) authored in any supported language; [Pulumi Packages](/docs/iac/concepts/packages/) let a component written in one language be consumed from any Pulumi language; language-native package managers (npm, PyPI, NuGet, Maven, Go modules); and the [Pulumi Registry](/registry/) for publicly available packages | Reuse is by copying manifests or by [Kustomize](https://kustomize.io/) bases and overlays; there is no package manager or typed interface for sharing manifest libraries |
| Import existing resources | [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/), both of which generate code in your language | The cluster is itself the source of truth; `kubectl get -o yaml` exports an object's current state as a manifest |
| Policy as code | [Pulumi Policies](/docs/insights/policy/) — open source, with rules written in Python, TypeScript, or Open Policy Agent Rego; Pulumi Cloud commercial plans add centralized policy management plus [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for compliance frameworks like CIS, PCI DSS, and SOC 2 | No built-in policy-as-code; admission controllers such as [OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/) or [Kyverno](https://kyverno.io/) enforce policy inside the cluster as a separate component |
| Open source | Yes — [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | Yes — Kubernetes and `kubectl` are [Apache License 2.0](https://github.com/kubernetes/kubernetes/blob/master/LICENSE) |
| Commercial option | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) | None — manifests are the input format of the Kubernetes API; managed Kubernetes is sold by cloud providers, but the manifest format itself has no commercial tier |

## Key differences

### Language support and the authoring experience

Kubernetes YAML manifests are static documents: each one describes a single object's desired state with no loops, conditionals, or variables. Generating many similar objects, or parameterizing them per environment, means copying YAML or layering [Kustomize](https://kustomize.io/) overlays on top of base manifests. Pulumi programs are written in general-purpose languages, so authors get loops, conditionals, functions, classes, package management, IDE features (autocomplete, type checking, refactoring, go-to-definition), and the testing frameworks that already exist in those ecosystems — while still producing the same Kubernetes API objects. Pulumi also supports [YAML](/docs/iac/languages-sdks/yaml/) for users who prefer a markup format.

### Cloud and service coverage

Kubernetes YAML manifests describe Kubernetes API objects and nothing else. Provisioning the cluster they run on, or the cloud resources an application depends on — a managed database, an object store, a DNS record — requires separate tooling, or an in-cluster operator such as [AWS Controllers for Kubernetes](https://aws-controllers-k8s.github.io/community/) or [Crossplane](https://www.crossplane.io/) that maps cloud resources onto Kubernetes objects. Pulumi pulls from the [Pulumi Registry](/registry/), which covers all major clouds and SaaS platforms, and includes a first-party [Kubernetes provider](/registry/packages/kubernetes/) generated from the Kubernetes OpenAPI spec. A single Pulumi program can provision an EKS, AKS, or GKE cluster, deploy workloads to it, and create the cloud resources those workloads use — without switching tools.

### Execution and rollbacks

Manifests are applied with the local `kubectl` CLI or by an in-cluster GitOps controller such as Argo CD or Flux; Kubernetes itself ships no centralized orchestration service. Pulumi runs through the local CLI, programmatically through the [Automation API](/docs/iac/automation-api/), or remotely through [Pulumi Deployments](/docs/deployments/). Neither approach performs a transactional rollback on failure: `kubectl apply` leaves successfully-applied objects in place, and workload controllers offer [`kubectl rollout undo`](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment) against revision history, while Pulumi leaves the stack partially-updated and reconciles on the next run. The difference is in surface area — Pulumi adds a preview step, an embeddable SDK, and a first-party managed runner on top of the same declarative reconciliation model.

### Secrets handling

A Kubernetes [`Secret`](https://kubernetes.io/docs/concepts/configuration/secret/) object stores values base64-encoded, not encrypted, so a secret committed in a manifest is effectively plaintext; protecting it requires [encryption at rest in etcd](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) configured at the cluster level, plus an external tool such as Sealed Secrets or an external secrets operator to keep cleartext out of source control. Pulumi treats secrets as a first-class primitive: values marked as secrets are encrypted in transit and at rest in the state file, anything derived from a secret is also encrypted, and each stack has its own encryption key. The default encryption provider can be replaced with [AWS KMS, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault](/docs/iac/concepts/secrets/#available-encryption-providers).

### Policy as code

Kubernetes manifests have no built-in policy-as-code mechanism; enforcement is done inside the cluster by an admission controller such as [OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/) or [Kyverno](https://kyverno.io/), installed and managed as a separate component. [Pulumi Policies](/docs/insights/policy/) is open source and free, with rules written in Python, TypeScript, or Open Policy Agent Rego that run during `pulumi preview` and `pulumi up` — before resources are created. Pulumi Cloud adds centralized management, policy groups, and enforcement across stacks, and commercial plans include [Pulumi-maintained policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for common compliance frameworks (CIS, PCI DSS, SOC 2, HITRUST, NIST).

### Modularity and reuse

Sharing Kubernetes YAML means copying manifests or building [Kustomize](https://kustomize.io/) bases and overlays — there is no package manager and no typed interface for distributing reusable manifest libraries. Pulumi's [Component Resources](/docs/iac/concepts/components/) are runtime objects with explicit parent/child relationships, so a component and the resources inside it form a coherent unit in plan output, deletion, and state. Components can be authored in one language and consumed from any other supported language by publishing them as a [Pulumi Package](/docs/iac/concepts/packages/), and they distribute through language-native package managers (npm, PyPI, NuGet, Maven, Go modules) and the [Pulumi Registry](/registry/).

### Automation API

The [Automation API](/docs/iac/automation-api/) lets a host application drive Pulumi without shelling out to the CLI. Practical uses include embedding stack creation in a SaaS product, building an internal developer platform that provisions a namespace or a whole cluster per team or per branch, generating ephemeral preview environments from CI, and orchestrating multi-step deployments where each step runs as part of a larger workflow. The Kubernetes API and its client libraries can create and update individual objects, but there is no equivalent SDK for driving a full apply, preview, and destroy lifecycle.

## When to choose Pulumi vs. Kubernetes YAML Manifests

**Choose Pulumi when** you:

1. Want to write Kubernetes configuration in a general-purpose language with the loops, conditionals, testing frameworks, package managers, and IDE tooling that already exist in that ecosystem.
1. Need to provision the cluster and the surrounding cloud resources (databases, object stores, DNS) in the same program that deploys your workloads.
1. Want a preview step, first-class encrypted secrets, and policy-as-code that runs before resources are created.
1. Need an embeddable SDK ([Automation API](/docs/iac/automation-api/)) to drive deployments from a host application — internal developer platforms, SaaS products, or per-branch preview environments.

**Choose Kubernetes YAML manifests when** you:

1. Want the native, dependency-free input format of the Kubernetes API, with no additional tooling to install or learn.
1. Have an existing GitOps workflow (Argo CD, Flux) and tooling built around raw manifests that you don't want to change.
1. Are managing Kubernetes resources only, and provisioning the cluster and cloud resources is handled by a separate team or tool.

The two can also coexist — see [Adoption](#adoption-coexistence-conversion-and-import) below.

## Adoption: coexistence, conversion, and import

There are several common paths for adopting Pulumi alongside or in place of Kubernetes YAML manifests, and they can be combined:

1. **Consume existing YAML in a Pulumi program.** The [Kubernetes provider](/registry/packages/kubernetes/) can deploy your existing manifests unchanged through its `ConfigFile` and `ConfigGroup` resources, so you can adopt Pulumi for orchestration without rewriting any YAML. See [Migrating from Kubernetes YAML or Helm Charts](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/#deploying-kubernetes-yaml).
1. **Coexist via rendered YAML.** Pulumi can [render a program to Kubernetes YAML](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/#rendering-kubernetes-yaml) instead of applying it directly, so you can author configuration in a general-purpose language while still deploying with `kubectl` or an existing GitOps pipeline.
1. **Convert manifests with `pulumi convert`.** [`pulumi convert --from kubernetes`](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/#converting-kubernetes-yaml) translates existing manifests into a Pulumi program in the language of your choice.
1. **Import existing resources.** [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/) bring already-running cluster resources under Pulumi management and generate the corresponding code in your chosen language.

For a complete walkthrough including coexistence patterns, conversion, and rendering, see [Migrating from Kubernetes YAML or Helm Charts to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/).

## Frequently asked questions

### Can Pulumi deploy my existing Kubernetes YAML unchanged?

Yes. The [Kubernetes provider](/registry/packages/kubernetes/) includes `ConfigFile` and `ConfigGroup` resources that read existing manifests and register every object in them with Pulumi, so you can adopt Pulumi for orchestration without rewriting any YAML. See the [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/#deploying-kubernetes-yaml).

### How do I migrate from Kubernetes YAML to Pulumi?

You have options that can be combined: deploy your existing manifests as-is through `ConfigFile`/`ConfigGroup`, convert them to program code with [`pulumi convert --from kubernetes`](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/#converting-kubernetes-yaml), or bring already-running resources under management with [`pulumi import`](/docs/iac/guides/migration/import/). The [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/) walks through each path.

### Does Pulumi replace `kubectl`?

For provisioning, yes — `pulumi up` applies your desired state to the cluster the same way `kubectl apply` does, with an added preview step. `kubectl` remains useful for ad-hoc inspection and debugging (`kubectl get`, `kubectl logs`, `kubectl describe`), and Pulumi can also [render to YAML](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/#rendering-kubernetes-yaml) if you want to keep applying with `kubectl` or a GitOps controller.

### Can Pulumi manage non-Kubernetes cloud resources too?

Yes. Unlike raw manifests, which describe Kubernetes objects only, a single Pulumi program can provision the cluster itself and any cloud resources your workloads depend on — managed databases, object stores, DNS records — using the [Pulumi Registry](/registry/) of providers for AWS, Azure, Google Cloud, and SaaS platforms.

### Is Pulumi free like Kubernetes manifests?

The Pulumi CLI and SDKs are open source under Apache 2.0 and free to use, as are Kubernetes and `kubectl`. [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) has a free Individual tier and paid plans that add managed state, RBAC, audit logs, policy management, and other features for running Pulumi at organizational scale.

### Can Pulumi and raw YAML or GitOps coexist during migration?

Yes — and this is a common adoption pattern. Pulumi can deploy existing manifests through `ConfigFile`/`ConfigGroup` and can render programs back to YAML for an existing `kubectl` or GitOps pipeline, so teams typically keep some resources on raw manifests while moving others to Pulumi, converting or importing incrementally as the project allows.

## Next steps

- [Get started with Pulumi](/docs/iac/get-started/)
- [Get started with Pulumi on Kubernetes](/docs/iac/get-started/kubernetes/)
- [Pulumi Kubernetes provider](/registry/packages/kubernetes/)
- [Migrating from Kubernetes YAML or Helm Charts to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/)
