---
title_tag: "Pulumi vs. Helm"
faq_schema: true
authors: ["joe-duffy"]
meta_desc: "Pulumi vs. Helm: Pulumi is multi-cloud IaC in general-purpose languages; Helm is a Kubernetes-only package manager. Many teams use them together."
title: Helm
h1: Pulumi vs. Helm
menu:
    iac:
        name: Helm
        parent: iac-comparisons
        weight: 50
        identifier: iac-comparisons-helm
---

Pulumi and [Helm](https://helm.sh/) solve different problems that often appear in the same workflow. Pulumi is an infrastructure as code platform that provisions resources across any cloud or SaaS platform from general-purpose languages. Helm is a package manager for Kubernetes that installs applications onto a cluster from templated YAML charts. Many teams use them together: Pulumi provisions clusters and cloud resources, then installs Helm charts inside the same program.

This page covers what each tool is, a feature-by-feature comparison, the most important differences in detail, the patterns for using Pulumi and Helm together, and the available paths for adopting Pulumi alongside or in place of Helm.

## What is Pulumi?

{{< what-is-pulumi >}}

For Helm users, the most relevant entry points are the [Pulumi Kubernetes provider](/registry/packages/kubernetes/) and its first-class Helm support through the [`helm.v4.Chart`](/registry/packages/kubernetes/api-docs/helm/v4/chart/) and [`helm.v3.Release`](/registry/packages/kubernetes/api-docs/helm/v3/release/) resources, which let a Pulumi program install Helm charts directly without invoking the `helm` CLI.

## What is Helm?

Helm is a [graduated Cloud Native Computing Foundation project](https://www.cncf.io/projects/helm/) that packages Kubernetes applications as [charts](https://helm.sh/docs/topics/charts/): directories of templated YAML manifests, a `values.yaml` file of default inputs, and metadata. The `helm` CLI renders chart templates using [Go template syntax](https://helm.sh/docs/chart_template_guide/) and either installs the resulting manifests into a cluster as a [release](https://helm.sh/docs/glossary/#release) or prints them to stdout. Charts are distributed through [Helm repositories](https://helm.sh/docs/topics/chart_repository/) and indexed publicly on [Artifact Hub](https://artifacthub.io/). Helm is open source under [Apache License 2.0](https://github.com/helm/helm/blob/main/LICENSE); the project does not ship a commercial tier.

## Detailed comparison

| Feature | Pulumi | Helm |
| --- | --- | --- |
| Primary purpose | Infrastructure as code platform for any cloud or SaaS platform | Package manager for Kubernetes applications |
| Scope | Any resource available in the [Pulumi Registry](/registry/), including AWS, Azure, Google Cloud, Kubernetes, Datadog, Cloudflare, GitHub, Auth0, and others | Kubernetes resources only |
| Authoring language | {{< pulumi-languages "general-purpose" >}} (general-purpose languages with loops, conditionals, classes, and package management), plus [YAML](/docs/iac/languages-sdks/yaml/) and [HCL](/docs/iac/languages-sdks/hcl/) | YAML manifests with [Go template syntax](https://helm.sh/docs/chart_template_guide/) and a `values.yaml` file for inputs |
| Templating model | Real code in the host language; resource inputs are typed values, including [outputs](/docs/iac/concepts/inputs-outputs/) from other resources | Text templating over YAML; values flow in through `values.yaml`, `--set` flags, or `--values` files |
| Resource ordering | Derived from the [dependency graph](/docs/iac/concepts/resources/options/dependson/): each resource waits for its dependencies to become ready, and independent resources deploy in parallel | [Fixed order by Kubernetes kind](https://github.com/helm/helm/blob/main/pkg/release/v1/util/kind_sorter.go); chart authors can't declare dependencies between resources or subcharts, except through [hook weights](https://helm.sh/docs/topics/charts_hooks/#hooks-and-the-release-lifecycle) |
| State management | [Managed by Pulumi Cloud by default](/docs/iac/concepts/state-and-backends/); self-managed backends include Amazon S3, Azure Blob Storage, Google Cloud Storage, and local files | [Release metadata stored as Secrets](https://helm.sh/docs/topics/advanced/#storage-backends) (or ConfigMaps) inside the target Kubernetes cluster |
| Secrets management | [Encrypted in transit and at rest](/docs/iac/concepts/secrets/) in the state file by default, per-stack encryption keys, pluggable KMS providers (AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault) | No built-in secrets primitive; values typically come from external secret stores or community plugins like [`helm-secrets`](https://github.com/jkroepke/helm-secrets) |
| Execution model | Local CLI, programmatic via [Automation API](/docs/iac/concepts/automation-api/), or remote runs in [Pulumi Deployments](/docs/deployments/) | Local `helm` CLI run against a Kubernetes cluster; no managed service from the Helm project |
| Rollback on failed operation | Failed updates leave the stack in a partially-updated state; `pulumi up` reconciles toward desired state and [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) detects drift | [`helm rollback`](https://helm.sh/docs/helm/helm_rollback/) restores a release to a previous revision recorded in release history |
| Programmatic API for tools and platforms | [Automation API](/docs/iac/concepts/automation-api/): a programmatic SDK in every supported language for embedding `up`, `preview`, and `destroy` in a host application | [Helm SDK](https://helm.sh/docs/topics/advanced/#go-sdk) in Go only; other languages must shell out to the `helm` CLI |
| Modularity and reuse | [Component Resources](/docs/iac/concepts/components/) authored in any supported language; [Pulumi Packages](/docs/iac/concepts/packages/) let a component written in one language be consumed from any other; package managers (npm, PyPI, NuGet, Maven, Go modules) | [Chart dependencies](https://helm.sh/docs/topics/charts/#chart-dependencies), [subcharts](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/), and [library charts](https://helm.sh/docs/topics/library_charts/) |
| Import existing resources | [`pulumi import`](/docs/iac/guides/migration/import/) and the [`import` resource option](/docs/iac/concepts/resources/options/import/), both of which generate code in your language | No direct equivalent; existing in-cluster resources can be adopted into a release through [resource ownership annotations](https://helm.sh/docs/howto/charts_tips_and_tricks/#take-ownership-of-existing-resources) |
| Policy as code | [Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/): open source, with rules in Python, TypeScript, or Open Policy Agent Rego; Pulumi Cloud adds centralized policy management, and the Enterprise edition adds [Pulumi-maintained policy packs](/docs/discovery-governance/guides/pre-built-policy-packs/) for CIS, PCI DSS, HITRUST, and NIST | No native policy engine; policy is typically delegated to Kubernetes admission controllers such as Kyverno or OPA Gatekeeper |
| Open source | Yes, [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE) | Yes, [Apache License 2.0](https://github.com/helm/helm/blob/main/LICENSE) |
| Commercial option | [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) | None from the Helm project |

## Key differences

### Resource ordering and dependencies

Helm doesn't let a chart author declare that one resource depends on another. When Helm installs or upgrades a release, [the Helm docs](https://helm.sh/docs/topics/charts/#operational-aspects-of-using-dependencies) state that "the Kubernetes objects from the charts and all its dependencies are aggregated into a single set; then sorted by type followed by name; and then created/updated in that order." The order is a [hardcoded list of Kubernetes kinds](https://github.com/helm/helm/blob/main/pkg/release/v1/util/kind_sorter.go) in the Helm source: Namespaces first, then Secrets and ConfigMaps, then CustomResourceDefinitions and RBAC, then Services and workloads, with any kind not on the list (including custom resources) last. Uninstall runs the same list in reverse. Helm sends the sorted manifests to the API server in a single pass and doesn't wait for one resource to become ready before applying the next.

[Chart dependencies](https://helm.sh/docs/topics/charts/#chart-dependencies) don't change this. They're a packaging mechanism: a subchart's objects are merged into the parent chart's set and sorted by kind along with everything else, so a chart can't express "install the database subchart before the application subchart" or "start this Deployment after that Job completes." The workarounds are [chart hooks](https://helm.sh/docs/topics/charts_hooks/) ordered with `helm.sh/hook-weight` annotations, whose resources Helm doesn't manage as part of the release, or sequencing logic built into the application itself, such as init containers that poll for a dependency. Native sequencing for resources and subcharts has been proposed in [HIP-0025](https://helm.sh/community/hips/hip-0025/), which is still a draft.

Pulumi orders operations from the program's actual dependencies. Passing one resource's [output](/docs/iac/concepts/inputs-outputs/) into another, or setting the [`dependsOn`](/docs/iac/concepts/resources/options/dependson/) resource option, creates an edge in the dependency graph. The Kubernetes provider waits for each resource to become ready before creating the resources that depend on it, and deploys independent resources in parallel, so updates are both correctly ordered and faster than a strict serial sequence. Deletes follow the same graph in reverse. When you install a chart through Pulumi, [`helm.v4.Chart`](/registry/packages/kubernetes/api-docs/helm/v4/chart/) supports the `config.kubernetes.io/depends-on` annotation for ordering between objects inside the chart, and `dependsOn` on the chart for dependencies on resources outside it.

### Language support and the authoring experience

Helm charts are YAML manifests interleaved with [Go templates](https://helm.sh/docs/chart_template_guide/), and dynamic behavior comes from template helpers and a `values.yaml` file. The model keeps charts portable across clusters but couples templating logic to text manipulation, which becomes harder to read as charts grow. Pulumi programs are written in general-purpose languages, so authors get typed inputs and outputs, loops, conditionals, classes, IDE features (autocomplete, refactoring, go-to-definition), and the testing frameworks that already exist in those ecosystems. Pulumi also supports [YAML](/docs/iac/languages-sdks/yaml/) for users who prefer a markup format.

### Scope of resources managed

Helm manages Kubernetes resources only. A chart can install Custom Resource Definitions, workloads, services, and other manifests into a cluster, but anything outside the cluster, such as a managed database, a DNS record, an IAM role, or a managed Redis instance, needs another tool. Pulumi manages those resources and Kubernetes resources in one program through the [Pulumi Registry](/registry/), which covers AWS, Azure, Google Cloud, Kubernetes, and SaaS platforms like Datadog, Auth0, GitHub, and Cloudflare.

### Execution and rollbacks

Helm runs as the `helm` CLI against a cluster and records each install or upgrade as a numbered release revision; [`helm rollback`](https://helm.sh/docs/helm/helm_rollback/) restores a prior revision. Pulumi runs through the local CLI, programmatically through the [Automation API](/docs/iac/concepts/automation-api/), or remotely through [Pulumi Deployments](/docs/deployments/). A failed Pulumi update leaves the stack partially updated, and you roll forward by reverting program code and running `pulumi up`. Helm favors fast revision-based rollback of a single release; Pulumi favors scriptable control over resources from many providers in one update.

### Secrets handling

Pulumi treats secrets as a first-class primitive. Values marked as secrets are encrypted in transit and at rest in the state file, anything derived from a secret is also encrypted, and each stack has its own encryption key. The default encryption provider can be replaced with [AWS KMS, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault](/docs/iac/concepts/secrets/#available-encryption-providers). Helm has no built-in secrets primitive; secret values are typically pulled from external stores like AWS Secrets Manager, Vault, or sealed-secrets controllers in the cluster, or stored encrypted on disk through community plugins such as [`helm-secrets`](https://github.com/jkroepke/helm-secrets).

### Policy as code

[Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/) is open source and free. Policies can be written in Python, TypeScript, or Open Policy Agent Rego, and Pulumi Cloud adds centralized management, policy groups, and enforcement across stacks. Pulumi Cloud commercial plans also include [Pulumi-maintained policy packs](/docs/discovery-governance/guides/pre-built-policy-packs/) for common compliance frameworks (CIS, PCI DSS, HITRUST, NIST). Helm has no native policy engine; cluster operators typically rely on Kubernetes admission controllers like Kyverno or OPA Gatekeeper to enforce constraints on the manifests a chart installs.

### Modularity and reuse

Pulumi's [Component Resources](/docs/iac/concepts/components/) are runtime objects with explicit parent/child relationships, so a component and the resources inside it form a coherent unit in plan output, deletion, and state. Components authored in one language can be consumed from any other supported language by publishing them as a [Pulumi Package](/docs/iac/concepts/packages/). Helm composes through [chart dependencies](https://helm.sh/docs/topics/charts/#chart-dependencies), [subcharts](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/), and [library charts](https://helm.sh/docs/topics/library_charts/), all of which operate at the YAML manifest level.

### Automation API

The [Automation API](/docs/iac/concepts/automation-api/) lets a host application drive Pulumi without shelling out to the CLI. Practical uses include embedding stack creation in a SaaS product, building an internal developer platform that provisions environments per team or per branch, generating ephemeral preview environments from CI, and orchestrating cross-cloud deployments where Kubernetes is one step in a larger workflow. Helm's official SDK is Go-only; other languages typically shell out to the `helm` CLI.

## Using Pulumi and Helm together

Helm and Pulumi are commonly used in combination rather than as substitutes. Pulumi handles cluster provisioning and any non-Kubernetes resources, then installs Helm charts inside the same program, either upstream charts from the broader Helm ecosystem or charts authored in-house. Two patterns cover most production deployments:

1. **Orchestrating a production-ready cluster end-to-end.** A single Pulumi program creates the cluster (EKS, AKS, or GKE), configures networking and IAM, and installs the operational stack, for example [cert-manager](https://cert-manager.io/), [ingress-nginx](https://kubernetes.github.io/ingress-nginx/), and [external-dns](https://kubernetes-sigs.github.io/external-dns/), through [`helm.v4.Chart`](/registry/packages/kubernetes/api-docs/helm/v4/chart/) or [`helm.v3.Release`](/registry/packages/kubernetes/api-docs/helm/v3/release/). The [EKS guide](/docs/iac/guides/clouds/aws/eks/) walks through this pattern end-to-end.
1. **Wiring Pulumi outputs into chart values.** Resource outputs from elsewhere in the program, such as a database connection string from `aws.rds.Instance`, a KMS key ARN, a managed Redis endpoint, or a Cloudflare zone ID, flow into a chart's `values` input as typed Pulumi outputs. Pulumi resolves the values at deploy time and orders the chart install after its dependencies, so charts can consume infrastructure that did not exist when the program started.

For choosing between `helm.v4.Chart` and `helm.v3.Release`, see [What's the difference between `helm.Chart` and `helm.Release`?](#whats-the-difference-between-helmchart-and-helmrelease) below.

## When to choose Pulumi vs. Helm

**Choose Pulumi when** you:

1. Manage infrastructure beyond Kubernetes (cloud accounts, networking, databases, SaaS platforms) and want one tool for all of it.
1. Need resources created and deleted in dependency order, with each resource ready before the ones that depend on it, rather than in a fixed order by kind.
1. Want to author infrastructure in a general-purpose language with the testing frameworks, package managers, and IDE tooling that already exist in that ecosystem.
1. Need an embeddable SDK ([Automation API](/docs/iac/concepts/automation-api/)) to drive deployments from a host application, such as an internal developer platform, a SaaS product, or ephemeral preview environments per pull request.
1. Want built-in secrets encryption, pluggable KMS providers, and per-stack encryption keys without bolting on a separate service.

**Choose Helm when** you:

1. Publish or consume charts from the broader Helm ecosystem (Artifact Hub, vendor-maintained repositories) and want compatibility with the standard `helm` CLI.
1. Have a narrowly Kubernetes-scoped workflow where templated YAML and revision-based rollback are a good fit.

**Use both when** Pulumi handles cluster provisioning and non-Kubernetes resources and you install third-party Helm charts inside that Pulumi program. This is the most common pattern among Pulumi users who already work with Helm.

## Adoption: coexistence, conversion, and import

There are three common paths for adopting Pulumi alongside or in place of Helm, and they can be combined:

1. **Use Helm charts directly from a Pulumi program** with [`helm.v4.Chart`](/registry/packages/kubernetes/api-docs/helm/v4/chart/) or [`helm.v3.Release`](/registry/packages/kubernetes/api-docs/helm/v3/release/), and migrate incrementally. This is the most common adoption pattern.
1. **Convert charts to native Pulumi code** by rendering them with `helm template` and converting the YAML with [`pulumi convert --from kubernetes`](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/).
1. **Import existing in-cluster resources** with [`pulumi import`](/docs/iac/guides/migration/import/) or the [`import` resource option](/docs/iac/concepts/resources/options/import/), which generate the corresponding code.

For a complete walkthrough, see [Migrating from Kubernetes YAML or Helm Charts to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/).

## Frequently asked questions

### Can I use Helm charts in a Pulumi program?

Yes. The Pulumi Kubernetes provider exposes Helm charts as first-class resources through [`helm.v4.Chart`](/registry/packages/kubernetes/api-docs/helm/v4/chart/) and [`helm.v3.Release`](/registry/packages/kubernetes/api-docs/helm/v3/release/). A Pulumi program can pull charts from any Helm repository (public or private), pass values as typed Pulumi inputs, including outputs from other Pulumi resources, and manage chart lifecycle alongside other infrastructure.

### What's the difference between `helm.Chart` and `helm.Release`?

[`helm.v4.Chart`](/registry/packages/kubernetes/api-docs/helm/v4/chart/) renders chart templates locally and registers each Kubernetes object the chart produces as an individual Pulumi resource, so every child shows up in plan output, drift detection, and state. [`helm.v3.Release`](/registry/packages/kubernetes/api-docs/helm/v3/release/) uses the embedded Helm SDK and creates a real Helm release in the cluster, preserving Helm-specific behaviors like [chart hooks](https://helm.sh/docs/topics/charts_hooks/), [post-rendering](https://helm.sh/docs/topics/advanced/#post-rendering), and release history. Choose `Chart` for fine-grained visibility into every rendered resource; choose `Release` when the chart relies on hooks or other Helm-specific lifecycle behavior.

### Can Helm chart dependencies control the order resources are installed in?

No. Helm merges the objects from a chart and all of its dependencies into a single set, sorts them by Kubernetes kind, and applies them in that order, so declaring a subchart as a dependency doesn't make it install first. Ordering within a release requires chart hooks with hook weights or logic in the application itself. See [Resource ordering and dependencies](#resource-ordering-and-dependencies) for details and for how Pulumi orders resources by their actual dependencies.

### Can Pulumi replace Helm?

It can, but it doesn't have to. Teams can keep installing upstream charts from inside a Pulumi program, or move off Helm entirely by converting charts to native Pulumi code. See [Adoption: coexistence, conversion, and import](#adoption-coexistence-conversion-and-import).

### How do I pass values from other Pulumi resources into a Helm chart?

Supply them on the chart's `values` input, which accepts the same shape as a `values.yaml` file but lets each leaf be a Pulumi [output](/docs/iac/concepts/inputs-outputs/). Pulumi resolves the values at deploy time and installs the chart after the resources it depends on.

### Does Pulumi support private Helm repositories?

Yes. Both [`helm.v4.Chart`](/registry/packages/kubernetes/api-docs/helm/v4/chart/) and [`helm.v3.Release`](/registry/packages/kubernetes/api-docs/helm/v3/release/) accept repository options for authenticated chart pulls, including username, password, and TLS certificate fields, so charts can be installed from private HTTP repositories or OCI registries.

### How do I migrate from Helm to Pulumi?

Install existing charts from a Pulumi program and migrate incrementally, convert rendered charts to native Pulumi code with `pulumi convert --from kubernetes`, or import already-provisioned in-cluster resources. See the [migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/) for a full walkthrough.

### Is Pulumi a package manager like Helm?

No. Pulumi is an infrastructure as code platform, not a Kubernetes package manager. The closest Pulumi concept to a Helm chart is a [Component Resource](/docs/iac/concepts/components/) published as a [Pulumi Package](/docs/iac/concepts/packages/), which packages a reusable abstraction in any supported language and can be consumed from any other supported language. The [Pulumi Registry](/registry/) is the discovery surface for those packages.

## Next steps

- [Get started with Pulumi on Kubernetes](/docs/iac/get-started/kubernetes/)
- [Pulumi Kubernetes provider](/registry/packages/kubernetes/)
- [Pulumi vs. Kubernetes YAML and DSLs](/docs/iac/comparisons/k8s-yaml-dsls/)
- [Migrating from Kubernetes YAML or Helm Charts to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/)
