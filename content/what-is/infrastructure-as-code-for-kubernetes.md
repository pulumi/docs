---
title: "Kubernetes Infrastructure as Code: Tools and Best Practices"
meta_desc: "Kubernetes infrastructure as code defines the cluster, its workloads, and the cloud resources around them in version-controlled code. Tools and best practices."

meta_image: /images/what-is/infrastructure-as-code-for-kubernetes-meta.png
type: what-is
page_title: "Kubernetes Infrastructure as Code"

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
      - ro
authors: ["cam-soper"]
---

**Infrastructure as code for Kubernetes is the practice of defining a cluster, the workloads that run on it, and the supporting cloud resources around it in version-controlled code, then letting an engine reconcile the real world to match.** It covers both halves of the platform: the cluster lifecycle (control plane, node groups, IAM, networking, storage classes) and the workload lifecycle (Deployments, Services, Ingress, ConfigMaps, Secrets), often in the same program.

Kubernetes is itself already declarative. Every object you create is described as a desired state that the control plane reconciles. The job of [infrastructure as code (IaC)](/what-is/what-is-infrastructure-as-code/) is to put that desired state under the same engineering discipline as the rest of your platform: reviewed in pull requests, tested in CI, gated by policy, and deployed by automation. Once both the cluster and its workloads live in IaC, "deploying" stops being a sequence of `kubectl apply` commands and becomes an ordinary code review.

In this article, we'll cover the key questions about IaC for Kubernetes:

* Why does Kubernetes need infrastructure as code?
* What are the two layers of IaC for Kubernetes?
* What Kubernetes objects are managed as IaC?
* How does IaC relate to containers and container orchestration?
* How does IaC for Kubernetes compare to GitOps?
* What does Kubernetes infrastructure as code look like in practice?
* What tools support IaC for Kubernetes?
* How do you secure Kubernetes infrastructure as code?
* What are best practices for IaC on Kubernetes?
* How does Pulumi handle Kubernetes as code?
* Frequently asked questions about IaC for Kubernetes

## Why does Kubernetes need infrastructure as code?

Kubernetes is the densest, most fast-changing layer of most cloud-native stacks. A single production cluster can hold thousands of objects across hundreds of namespaces, and the cluster itself is just one of many that span dev, staging, prod, and per-region replicas. Three forces make IaC the only realistic operating model:

* **Scale.** Even one production cluster crosses any threshold where hand-edited YAML is workable. With multiple clusters, the only way to keep them consistent is to derive them from the same code.
* **Drift.** Kubernetes lets anyone with the right RBAC run `kubectl apply`. Without an authoritative source of truth, the cluster drifts away from whatever was last reviewed. IaC makes the gap between intended and actual state visible.
* **Day-2 changes.** Most of a platform team's work isn't standing up new clusters; it's rolling node-group upgrades, swapping CNIs, rotating certificates, changing storage classes. Each of those changes is much safer when the proposed diff is something a reviewer can read.

## What are the two layers of IaC for Kubernetes?

A complete IaC program for Kubernetes covers two distinct concerns.

| Layer | What it manages | Typical lifecycle |
|---|---|---|
| **Cluster lifecycle** | EKS / GKE / AKS clusters, node groups, IAM roles, VPC and subnets, addons, CNI, ingress controllers, observability agents | Weeks to months between substantive changes |
| **Workload lifecycle** | Deployments, StatefulSets, Services, Ingress, ConfigMaps, Secrets, Jobs, CronJobs, namespaces, RBAC | Hours to days; tied to application releases |

Some teams keep the two layers in separate Pulumi programs (one for the platform, one for the app), so the platform team owns the cluster repo and product teams own their workload repos. Other teams keep them in a single program when the cluster and the app are tightly coupled (a managed service offered to customers, for example). Both shapes work; the deciding factor is who needs to ship changes to what.

## What Kubernetes objects are managed as IaC?

The most common Kubernetes resources that end up in IaC programs:

* **Cluster shape.** Cluster spec, version, region, node groups, addons.
* **Networking.** VPC and subnets, security groups, CNI configuration, NetworkPolicies, Ingress, Service mesh resources (Istio, Linkerd).
* **Identity and access.** IAM roles for the cluster and workloads (IRSA on EKS, Workload Identity on GKE, Microsoft Entra Workload ID on AKS), Kubernetes RBAC (ClusterRoles, RoleBindings).
* **Workloads.** Deployments, StatefulSets, DaemonSets, Jobs, CronJobs.
* **Configuration.** ConfigMaps and Secrets (with the actual secret values pulled from a vault like [Pulumi ESC](/product/esc/), not stored in code).
* **Service exposure.** Services, Ingress, Gateway API resources.
* **Storage.** PersistentVolumes, StorageClasses, PVCs.
* **Custom resources.** ArgoCD Applications, Flux Kustomizations, cert-manager Certificates, ExternalSecret objects, and any operator-defined CRDs.

Pulumi's Kubernetes provider supports every resource type Kubernetes itself supports, including CRDs through a dynamic provider. See the [Pulumi Kubernetes documentation](/docs/iac/clouds/kubernetes/) for full coverage.

## How does IaC relate to containers and container orchestration?

Containers and IaC split the work at the image boundary. The container image carries the application and its runtime dependencies; everything about *running* that image — which orchestrator, how many replicas, what network and storage it gets, what secrets it can read — is infrastructure, and that's the part IaC describes. For a containerized stack, the pieces line up like this:

1. **The image build.** CI builds the container image and pushes it to a registry (ECR, GCR, ACR, Docker Hub). The registry itself, its access policies, and its lifecycle rules are cloud resources provisioned by IaC.
1. **The orchestrator.** Kubernetes is the dominant container orchestration layer, and the cluster's whole lifecycle (control plane, node groups, networking, addons) lives in IaC.
1. **The workload definition.** Deployments, Services, and the rest of the objects that tell the orchestrator how to run the image are declarative by design, which makes them natural IaC material, whether applied by an IaC engine or reconciled by a GitOps controller.
1. **Templating layers.** Helm charts and Kustomize overlays generate workload definitions. They're inputs to the IaC layer, not competitors to it: an IaC engine can render a Helm chart or a Kustomize directory and manage the result like any other resource.

The practical consequence: "IaC for container orchestration" isn't a separate discipline with separate tools. It's the same desired-state model Kubernetes already uses internally, extended one level up so the cluster, the registry, and the workload definitions all come from reviewed, version-controlled code.

## How does IaC for Kubernetes compare to GitOps?

GitOps and IaC aren't competing approaches. They're complementary, and most production Kubernetes shops use both.

| Aspect | IaC engine for Kubernetes (e.g. `pulumi up` from CI) | GitOps controller (ArgoCD, Flux) |
|---|---|---|
| Source of truth | Git repo containing IaC program | Git repo containing manifests or Kustomize/Helm output |
| Apply mechanism | CI pipeline runs IaC engine | In-cluster controller reconciles toward Git |
| Cluster-level resources | Excellent (cloud accounts, IAM, networks) | Limited — most controllers reconcile Kubernetes API objects, not cloud-side resources like VPCs or IAM |
| Workload-level resources | Good | Excellent |
| Drift detection | Engine compares declared state to live state | Controller continuously reconciles |
| Rollback | Re-run with previous code | Revert the Git commit; controller reconciles |

A common production pattern: Pulumi (or another IaC tool) manages the cluster, the IAM, the cloud resources around it, and seeds the cluster with the GitOps controller. The GitOps controller then manages the application workloads. Both halves are version-controlled, both halves are reviewable, and neither is doing work the other is better suited for.

## What does Kubernetes infrastructure as code look like in practice?

Here's a complete program that creates an Amazon EKS cluster and deploys a workload onto it. The cluster and the Deployment live in one TypeScript file; Pulumi knows the Deployment depends on the cluster and sequences them correctly:

```typescript
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

const cluster = new eks.Cluster("web", {
    desiredCapacity: 3,
    minSize: 2,
    maxSize: 5,
});

const nginx = new k8s.apps.v1.Deployment("nginx", {
    spec: {
        replicas: 2,
        selector: { matchLabels: { app: "nginx" } },
        template: {
            metadata: { labels: { app: "nginx" } },
            spec: {
                containers: [{ name: "nginx", image: "nginx:1.29" }],
            },
        },
    },
}, { provider: cluster.provider });

export const kubeconfig = cluster.kubeconfig;
```

Every field in that program is typed: misspell `replicas` or pass a string where a number belongs and the program fails at compile time, not at `kubectl apply` time. Getting from zero to a running cluster is three commands:

1. **Create a project.** `pulumi new aws-typescript` scaffolds the program, then `npm install @pulumi/eks @pulumi/kubernetes` adds the cluster and Kubernetes SDKs.
1. **Preview the change.** `pulumi preview` shows the full plan — cluster, node group, IAM, Deployment — before anything is created.
1. **Deploy.** `pulumi up` provisions the cluster, waits for it to become ready, and applies the workload in dependency order.

The same program shape works for GKE and AKS; see [Get started with Pulumi Kubernetes](/docs/iac/get-started/kubernetes/) for each provider's flow.

## What tools support IaC for Kubernetes?

The Kubernetes IaC tooling landscape is wider than for any other cloud target because the community has produced both general IaC tools and Kubernetes-specific layers.

| Category | Representative tools |
|---|---|
| General IaC (cluster + workloads) | [Pulumi](/), Terraform, OpenTofu |
| Cluster provisioning (focused) | eksctl, gcloud, az aks, ClusterAPI |
| Workload templating | Helm, Kustomize, jsonnet |
| GitOps controllers | ArgoCD, Flux |
| Policy as code | [Pulumi policy as code](/docs/insights/policy/), Kyverno, OPA Gatekeeper |
| Secrets | [Pulumi ESC](/product/esc/), External Secrets Operator, Sealed Secrets, Vault |
| Cluster security scanning | Trivy, kube-bench, Falco |
| Service mesh | Istio, Linkerd, Cilium |

Most teams use a combination: a general IaC tool for the cloud-and-cluster layer, Helm or Kustomize for some workload templating, ArgoCD or Flux for continuous reconciliation, and policy as code for guardrails.

## How do you secure Kubernetes infrastructure as code?

Misconfiguration, not exotic exploits, drives most Kubernetes security incidents — and misconfiguration is exactly what IaC makes checkable before it reaches a cluster. The controls stack up in layers:

* **Scan before merge.** Static scanners (Trivy, Checkov) run against rendered manifests on every commit and catch known-bad configurations: privileged containers, host-path mounts, missing resource limits. kube-bench complements them at runtime, checking the running cluster against the CIS Kubernetes Benchmark.
* **Enforce policy in two places.** In CI, [policy as code](/docs/insights/policy/) blocks non-compliant changes from merging at all. In the cluster, admission controllers (Kyverno, OPA Gatekeeper) backstop anything that arrives by another path. The CI check is faster feedback; the admission controller is the last line of defense.
* **Keep secret material out of code and Git.** The IaC program defines *which* secrets a workload references; the values live in [Pulumi ESC](/product/esc/), HashiCorp Vault, or a cloud secrets manager and are pulled at deploy time.
* **Use per-workload cloud identity.** IRSA on EKS, Workload Identity on GKE, and Microsoft Entra Workload ID on AKS replace long-lived static credentials with scoped, rotatable, auditable identities, all declared in the same IaC program as the workloads that use them.
* **Declare RBAC as code.** ClusterRoles and RoleBindings written in IaC get the same least-privilege review as IAM policies. Hand-granted `cluster-admin` stops being invisible.
* **Watch for drift.** Out-of-band `kubectl` edits and console changes surface as diffs against the declared state, so a quietly weakened NetworkPolicy or a manually widened RBAC grant gets noticed instead of persisting.

Each of these works because the desired state is code: there's an artifact to scan, a diff to review, and a source of truth to compare the live cluster against.

## What are best practices for IaC on Kubernetes?

A few patterns that hold up across providers and team sizes:

* **Keep clusters in version control.** Cluster spec, addons, node groups, RBAC: everything in code, even (especially) for managed clusters. Reproducing a cluster from scratch should be a CI job, not a wiki page.
* **Avoid naked pods.** A bare `Pod` isn't rescheduled when the node fails. Use Deployments, StatefulSets, or DaemonSets so the workload survives. Enforce this with a policy in CI.
* **Use IRSA / Workload Identity / Entra Workload ID.** Long-lived static credentials inside Kubernetes are an anti-pattern. The cloud providers all offer per-workload identity that's much easier to scope, rotate, and audit.
* **Separate production from everything else.** Different clusters, different cloud accounts, different IAM, different secrets backends. Don't rely on namespace boundaries to keep dev workloads out of prod.
* **Pull secrets at runtime.** Don't bake secret values into IaC code or Git history. Store them in a central vault like [Pulumi ESC](/product/esc/), HashiCorp Vault, or a cloud secrets manager, and pull them into Kubernetes at deploy time — either directly through your IaC program or through the External Secrets Operator (which can sync from ESC and other vaults into Kubernetes Secrets).
* **Codify policy.** No naked pods, no privileged containers, no `:latest` tags in production, mandatory resource requests and limits, mandatory liveness/readiness probes. Enforce in CI with [Pulumi policy as code](/docs/insights/policy/) or in the cluster with Kyverno / OPA Gatekeeper.
* **Encode dependency ordering.** Some resources have to come up before others (CRDs before the operators that consume them, namespaces before everything in them). An IaC tool that understands resource dependencies prevents the half-converged states a naive `kubectl apply -R` produces.
* **Test the workloads, not just the YAML.** Helm chart `helm test`, end-to-end smoke tests via the automation API, and chaos exercises against ephemeral clusters all catch problems that template linting misses.

## How does Pulumi handle Kubernetes as code?

Pulumi treats Kubernetes the same way it treats every other cloud target: as resources in a real programming language, with dependencies, types, and tests. Common patterns:

* **Unified cluster + workload programs.** The same Pulumi program creates the EKS / GKE / AKS cluster, sets up IAM, deploys the CNI and ingress controller, and applies the application workloads. Resource dependencies are explicit, so the order is correct without manual sequencing.
* **Import existing Kubernetes artifacts.** Pulumi exposes dedicated resources for each common source format — `ConfigFile` and `ConfigGroup` for raw Kubernetes YAML manifests, `Chart` for Helm charts, and `Directory` for Kustomize bundles — so adoption can be incremental without re-authoring the source artifacts.
* **Higher-level components and guides.** For EKS, the [`@pulumi/eks`](https://github.com/pulumi/pulumi-eks) component package bundles sensible networking and IAM defaults so you don't hand-wire VPCs, subnets, and roles. For GKE and AKS, the [Pulumi Kubernetes docs](/docs/iac/clouds/kubernetes/) include reference programs covering Workload Identity, managed addons, and other cluster patterns.
* **Strong typing.** Kubernetes API objects come through as typed values in TypeScript, Python, Go, C#, and Java. In TypeScript, Go, C#, and Java, misspelled field names fail at compile time rather than at `kubectl apply` time.
* **Policy as code.** Write Kubernetes-aware policies in the same language as the program. Block naked pods, missing resource limits, or `latest` tags before they merge.
* **Secrets through Pulumi ESC.** Pull secret values into Kubernetes Secrets at deploy time. No plaintext secrets in code or state.
* **[Automation API](/docs/iac/automation-api/).** Wrap Pulumi programs in software (a service, a CLI, a CI job) so platform teams can offer self-service cluster and workload provisioning through whatever interface they prefer.

[Get started with Pulumi Kubernetes](/docs/iac/get-started/kubernetes/) to manage a cluster and its workloads in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about IaC for Kubernetes

### Isn't Kubernetes already declarative?

Yes, inside the cluster. What Kubernetes doesn't provide is a single source of truth, versioning, code review, or testing for the desired state. IaC sits in front of the cluster and produces those properties. The two layers compose: IaC describes the desired Kubernetes state, Kubernetes reconciles to it.

### Should I use Pulumi or Helm for Kubernetes?

They're not really substitutes. Helm packages and templates Kubernetes manifests; Pulumi defines and applies them (and can consume Helm charts directly). Most teams use Pulumi for the cluster and the platform-level Kubernetes objects, and use Helm or Kustomize for community-maintained workload charts that they consume rather than author.

### Should I use Pulumi or ArgoCD/Flux?

Most production teams use both. Pulumi manages the cluster, IAM, networking, and bootstraps the GitOps controller. The GitOps controller then continuously reconciles application workloads from Git. The split avoids the weaknesses of either tool alone: GitOps controllers aren't great at cloud-level resources, and a CI-driven IaC tool isn't great at continuous reconciliation inside a cluster.

### Can I import existing Kubernetes manifests into IaC?

Yes. Pulumi has `ConfigFile` (single manifest), `ConfigGroup` (multiple manifests), and `Chart` (Helm) resources that consume existing artifacts without rewriting them. Most teams use this to wrap operator installs (cert-manager, ingress-nginx, ArgoCD) without re-authoring the maintainers' charts.

### How do I keep Kubernetes Secrets out of Git?

Don't put secret values in IaC code. Use [Pulumi ESC](/product/esc/), HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, or the External Secrets Operator to pull secrets at runtime. The IaC defines *what* secret references look like; the secret material lives in the vault.

### How do you test Kubernetes IaC?

Unit-test the program with mocks, run static scans (Checkov, Trivy) against the rendered manifests, run policy-as-code checks in CI (Pulumi policy as code, OPA), and run integration tests that deploy to an ephemeral cluster (kind, k3d, or a sandbox managed cluster) and exercise the workload before tearing it down. See [How to step up cloud infrastructure testing](/what-is/how-to-step-up-cloud-infrastructure-testing/) for the broader pattern.

### What's "naked pods" and why are they bad?

A naked pod is a `Pod` object created directly, not through a controller like a Deployment, StatefulSet, or DaemonSet. If the node hosting a naked pod fails or is drained, the pod isn't rescheduled. It just disappears. Controllers re-create the pod automatically. A Pulumi policy-as-code or Kyverno policy that fails any naked-pod definition is a small but high-value guardrail.

### Can a single Pulumi program span multiple Kubernetes clusters?

Yes. Pulumi providers can be parameterized by a kubeconfig, so a single program can address multiple clusters by instantiating multiple providers. This is how multi-region or multi-cloud Kubernetes platforms are typically defined.

### How does IaC for Kubernetes support compliance?

The same way IaC supports compliance for the broader cloud: every change is a reviewed pull request with author and timestamp; every policy violation is logged in CI; every deploy is recorded in state. For SOC 2, HIPAA, and HITRUST, auditors get a concrete artifact for each control rather than a written-down policy that may or may not be enforced.

### How do I migrate an existing console-managed cluster to IaC?

Start with the simplest thing that gives you a baseline: a Pulumi program that imports the existing cluster spec and the high-value workloads. Use [`pulumi import`](/docs/iac/cli/commands/pulumi_import/) to bring resources under management without recreating them. Once that program runs in CI, layer policies on top to prevent regression. Migrate additional workloads as their owners are ready; there's no need to convert everything at once.

## Learn more

Pulumi turns the cluster, the workloads on it, and the cloud resources around it into one reviewable program in the language your team already uses. Combined with [policy as code](/docs/insights/policy/) and [ESC](/product/esc/) for secrets, that gives you everything Kubernetes can be operated with: the cluster as code, the workloads as code, the policies as code. [Get started today](/docs/iac/get-started/kubernetes/).

Related reading:

* [What is Infrastructure as Code (IaC)?](/what-is/what-is-infrastructure-as-code/)
* [What is DevOps?](/what-is/what-is-devops/)
* [What is Platform Engineering?](/what-is/what-is-platform-engineering/)
* [How to Step Up Cloud Infrastructure Testing](/what-is/how-to-step-up-cloud-infrastructure-testing/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)
* [What are Kubernetes Secrets?](/what-is/what-are-kubernetes-secrets/)
