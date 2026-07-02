---
title: "Is Kubernetes Infrastructure as Code?"
meta_desc: "Partly. Kubernetes reconciles YAML the way IaC does, but that loop stops at the cluster boundary. Pulumi extends the same model to the infrastructure underneath."

type: what-is
page_title: "Is Kubernetes Infrastructure as Code?"

authors:
  - alex-leventer

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - mercedes-benz
---

Kubernetes genuinely behaves like infrastructure as code within its own domain: you declare desired state in YAML, and a control loop continuously reconciles the live cluster toward it, correcting drift without being told to. That's the same declarative, convergent model IaC is built on, and it's a big part of why Kubernetes is often held up as the reference implementation of the idea. Where it falls short of infrastructure as code in the fuller, cross-cloud sense is the boundary of what it reconciles: the cluster, its node groups, the VPC it runs in, and the IAM roles behind it all have to exist before Kubernetes's control loop has anything to converge. Extending that same declarative, code-reviewable model to the infrastructure underneath the cluster is what a general-purpose tool like Pulumi or Terraform adds.

## What is the relationship between Kubernetes and infrastructure as code

Kubernetes and infrastructure as code share a common mechanism, declarative desired state reconciled by a control loop, but they apply it to different scopes, and the mismatch between those scopes is where most of the friction shows up in practice.

The **configuration layer** is what Kubernetes itself understands: Deployments, Services, ConfigMaps, and other API objects that the cluster's control plane continuously reconciles toward a desired state, the same way `pulumi up` reconciles a Pulumi program's desired state against the cloud, just scoped to what the Kubernetes API can express. The **infrastructure layer** is everything that has to exist before any of that reconciliation can happen: the cluster itself, its node groups, the VPC and subnets it runs in, and the IAM roles that let it talk to the rest of the cloud. Kubernetes has no built-in way to describe or converge that layer; its reconciliation loop simply doesn't run against it.

That boundary is also where several practical impedance mismatches show up. `kubectl apply` itself has no built-in plan step; it reconciles immediately. `kubectl diff` can show a preview against the live cluster as a separate command, but it's a raw object diff rather than a dependency-aware plan like `pulumi preview` or `terraform plan` produces across resources. Kubernetes also has no general-purpose language underneath it, so expressing "one of these per environment" means templating YAML with Helm or patching it with Kustomize rather than writing a loop. And its state is implicit and scattered across live object status in the API server, rather than a single explicit state file or backend a tool like Pulumi can diff, lock, and version end to end.

A useful way to hold both truths at once: **within the Kubernetes API boundary, manifests genuinely are a form of infrastructure as code. Outside that boundary, at the cluster and cloud layer, they aren't, because Kubernetes was never designed to reconcile that layer.** General-purpose IaC tools like Pulumi and Terraform provision the cluster in the first place, and can go on to manage everything running on it, closing that gap rather than replacing what Kubernetes already does well.

## What's the difference between Kubernetes YAML and infrastructure as code

A Kubernetes manifest is genuinely declarative and genuinely reconciled, which is exactly why it's easy to mistake it for the whole of infrastructure as code. What it lacks is everything a general-purpose IaC program adds around that reconciliation: a way to describe the cloud resources the cluster itself depends on (which creates a chicken-and-egg problem, since you can't apply a manifest to a cluster that the manifest was supposed to create), a dependency-aware plan step built into the apply workflow itself (`kubectl diff` gets you a raw pre-apply diff as a separate command, but not a `pulumi preview`-style plan across resources), and general-purpose logic like loops, functions, and conditionals rather than templating YAML by hand. The [Kubernetes documentation on declarative configuration](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/) is explicit that `kubectl apply` merges intent against live [object state](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/) inside the cluster; it says nothing about how that cluster came to exist, because that's outside the scope Kubernetes was built to reconcile.

General-purpose infrastructure as code closes that gap rather than competing with what Kubernetes already does well. Because Pulumi programs are written in real languages (TypeScript, Python, Go, C#, Java), they extend the same declarative, convergent model past the Kubernetes API boundary: `pulumi preview` shows a diff before anything changes, loops and functions express repeated patterns without copy-pasting YAML, and the same testing and packaging tools your application code already uses apply to your infrastructure code too.

## Can you manage Kubernetes with Pulumi

Yes, and in one stack rather than two separate tools. Pulumi's [Kubernetes provider](/registry/packages/kubernetes/) applies any Kubernetes resource, including custom resources (CRDs), and can wait for resources to reach a ready state before moving on, the same way `kubectl apply --wait` would. It can also ingest existing YAML directly through `kubernetes.yaml.ConfigFile` and `ConfigGroup`, so a migration doesn't require rewriting manifests from scratch on day one.

Provisioning the cluster and deploying to it in a single Pulumi program looks like this, using [Amazon EKS](/registry/packages/eks/) as the example:

1. Provision a managed EKS cluster. The [`@pulumi/eks`](/registry/packages/eks/) component handles the VPC, IAM roles, and node groups behind the scenes.
2. Point a Kubernetes provider at the new cluster, using the cluster's `kubeconfigJson` output.
3. Deploy a Helm chart onto that cluster with the current `helm.v4.Chart` resource, targeting the provider from step 2.

{{< chooser language "typescript,python" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// 1. Provision a managed EKS cluster (VPC, IAM, and node groups included).
const cluster = new eks.Cluster("eks-cluster", {});

// 2. Point a Kubernetes provider at the new cluster. Use kubeconfigJson
//    (the stringified-JSON output), not the bare kubeconfig object.
const eksProvider = new k8s.Provider("eks-provider", {
    kubeconfig: cluster.kubeconfigJson,
});

// 3. Deploy a Helm chart onto that cluster with the current helm.v4.Chart resource.
const nginxIngress = new k8s.helm.v4.Chart("nginx-ingress", {
    chart: "ingress-nginx",
    namespace: "ingress-nginx",
    repositoryOpts: {
        repo: "https://kubernetes.github.io/ingress-nginx",
    },
}, { provider: eksProvider, dependsOn: [cluster] });

export const kubeconfig = cluster.kubeconfigJson;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_eks as eks
import pulumi_kubernetes as kubernetes
from pulumi_kubernetes.helm.v4 import Chart, RepositoryOptsArgs

# 1. Provision a managed EKS cluster (VPC, IAM, and node groups included).
cluster = eks.Cluster("eks-cluster")

# 2. Point a Kubernetes provider at the new cluster. Use kubeconfig_json
#    (the stringified-JSON output), not the bare kubeconfig object.
eks_provider = kubernetes.Provider("eks-provider", kubeconfig=cluster.kubeconfig_json)

# 3. Deploy a Helm chart onto that cluster with the current helm.v4.Chart resource.
nginx_ingress = Chart(
    "nginx-ingress",
    chart="ingress-nginx",
    namespace="ingress-nginx",
    repository_opts=RepositoryOptsArgs(
        repo="https://kubernetes.github.io/ingress-nginx",
    ),
    opts=pulumi.ResourceOptions(provider=eks_provider, depends_on=[cluster]),
)

pulumi.export("kubeconfig", cluster.kubeconfig_json)
```

{{% /choosable %}}

The `provider` option in step 3 is what routes a resource to a specific cluster's API; leaving it off silently falls back to whatever kubeconfig is ambient on the machine running `pulumi up`. And because Pulumi tracks the dependency between the cluster and the chart, a single `pulumi up` provisions the cluster and deploys the chart in the right order, without the two-phase apply that a separately-configured Kubernetes provider block often forces in other tools.

At scale, this is exactly how [Wiz manages thousands of Kubernetes clusters across hundreds of data centers worldwide with Pulumi's Automation API](/case-studies/wiz/), maintaining more than 1M cloud resources and hundreds of thousands of infrastructure updates daily.

## How does Pulumi compare to Helm and Kustomize

Helm and Kustomize both operate one layer up from infrastructure: they shape what gets applied to a cluster that already exists, rather than provisioning that cluster. [Helm](https://helm.sh/) is a package manager for Kubernetes, templating manifests and versioning them as charts. Kustomize, built into `kubectl`, patches and overlays existing YAML for different environments without templating. Neither can create the cluster, the VPC, or the IAM roles it depends on.

Pulumi doesn't replace the Helm ecosystem, it consumes it. [`helm.v4.Chart`](/docs/iac/comparisons/helm/) renders a chart the way `helm template` would, then brings every resulting resource under Pulumi state, so you get per-resource diffs, policy checks, and transformations on top of charts you didn't have to rewrite. For teams that need native Helm semantics like hooks or `helm list` interoperability, `helm.v3.Release` drives the Helm SDK directly instead. Either way, the cluster those charts land on can be provisioned in the very same Pulumi program.

## Should you use Terraform or Pulumi for Kubernetes

Both are legitimate answers to "is there IaC for Kubernetes," and the [comparison between Pulumi and Terraform](/docs/iac/comparisons/terraform/) is a fair one to make: both provision the cluster and can manage the workloads that run on it.

The difference is in how you write and evolve that code. Pulumi programs are TypeScript, Python, Go, C#, or Java, so they get IDE autocomplete, unit tests, and existing package managers for free, and one stack can describe the cluster and its workloads together. Terraform added a native `terraform test` framework in v1.6, but HCL is still a purpose-built configuration language rather than a general-purpose one, so it lacks general-purpose loops and functions, and its Kubernetes and Helm providers typically can't be configured until the cluster they target already exists, which is why many Terraform setups split cluster and workload management into two separate applies.

## Frequently asked questions about Kubernetes and infrastructure as code

### Is a Kubernetes YAML manifest infrastructure as code?

Within the Kubernetes API's own scope, yes: a manifest declares desired state and a control loop continuously reconciles the live cluster toward it, the same declarative, convergent model infrastructure as code is built on. It falls short of the fuller, cross-cloud sense of the term because that reconciliation never reaches the cluster, node groups, or cloud resources the manifest depends on, it has no dependency-aware plan step built into the apply workflow (`kubectl diff` offers a separate, raw pre-apply diff, but not a `pulumi preview`-style plan across resources), and it has no general-purpose logic like loops and conditionals. Pairing manifests with a general-purpose IaC tool that provisions the underlying cluster is what extends that same model across the whole stack.

### Is Helm infrastructure as code?

Helm is a package manager for Kubernetes, not infrastructure as code. It templates and versions manifests so they're reusable across environments, but like a raw manifest, it assumes a cluster already exists and can't provision one. Pulumi can consume Helm charts directly through `helm.v4.Chart` while also provisioning the cluster the chart deploys to.

### Is Kustomize infrastructure as code?

No. Kustomize overlays and patches existing Kubernetes YAML for different environments, and ships built into `kubectl`. It operates entirely within the configuration layer, with no concept of the cloud infrastructure a cluster runs on.

### Is `kubectl apply` infrastructure as code?

`kubectl apply` is the mechanism Kubernetes uses to reconcile manifests against live cluster state, and it's version-controllable if the manifests behind it are stored in Git. But it operates only within the configuration layer: it can't create the cluster it's targeting, it has no plan step of its own (`kubectl diff` offers a separate, less integrated pre-apply diff), and it can't express repeated patterns as code the way a general-purpose IaC program can.

### Can Terraform manage Kubernetes?

Yes. Terraform can provision a Kubernetes cluster and, through its Kubernetes and Helm providers, manage resources running on it, making it a general-purpose IaC option for Kubernetes alongside Pulumi. See the [Pulumi vs. Terraform comparison](/docs/iac/comparisons/terraform/) for how the two differ in language and workflow.

### Can Pulumi manage both the cluster and the workloads?

Yes, in a single program and a single `pulumi up`. Pulumi provisions the cluster (through packages like `@pulumi/eks`), then deploys resources onto it, including raw manifests, Helm charts, and custom resources, tracking the dependency between the two so the cluster exists before anything is deployed to it.

## Learn more

Pulumi turns the cluster, the workloads on it, and the cloud resources around it into one reviewable program in the language your team already uses. For a deeper look at Kubernetes IaC tooling, patterns, and best practices, see [Kubernetes Infrastructure as Code: Tools and Best Practices](/what-is/infrastructure-as-code-for-kubernetes/). [Get started today](/docs/iac/get-started/kubernetes/).

Related reading:

* [Kubernetes Infrastructure as Code: Tools and Best Practices](/what-is/infrastructure-as-code-for-kubernetes/)
* [What is Infrastructure as Code (IaC)?](/what-is/what-is-infrastructure-as-code/)
* [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
* [Pulumi and Helm](/docs/iac/comparisons/helm/)
* [Deploying an EKS Cluster](/docs/iac/guides/clouds/aws/eks/)
* [Announcing Kubernetes Chart v4](/blog/kubernetes-chart-v4/)
* [Easily Create and Manage AWS EKS Kubernetes Clusters with Pulumi](/blog/easily-create-and-manage-aws-eks-kubernetes-clusters-with-pulumi/)
