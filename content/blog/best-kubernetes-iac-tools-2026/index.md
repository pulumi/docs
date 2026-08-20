---
title: "Best Kubernetes Infrastructure as Code Tools in 2026"
date: 2026-08-14
draft: false
meta_desc: "The best Kubernetes IaC tools in 2026: Pulumi, Terraform, Helm, Kustomize, Crossplane, Argo CD, Flux, cdk8s, and kro, compared honestly on fit."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - kubernetes
    - infrastructure-as-code
    - platform-engineering
    - devops
    - helm
category: general
faq_schema: true
howto_schema: true
itemlist_name: "Kubernetes Infrastructure as Code Tools"
itemlist:
    - name: "Pulumi"
      url: "https://www.pulumi.com/"
    - name: "Terraform"
    - name: "OpenTofu"
    - name: "Helm"
    - name: "Kustomize"
    - name: "Crossplane"
    - name: "Argo CD"
    - name: "Flux"
    - name: "cdk8s"
    - name: "kro"

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        "Kubernetes IaC" actually spans a cluster layer, a workload layer, and a delivery layer. Most roundups blur them together.

        We separated them and compared what fits each one: Pulumi, Terraform, Helm, Kustomize, Crossplane, Argo CD, Flux, cdk8s, and kro.
    linkedin: |
        Most "best Kubernetes IaC tools" lists compare Terraform, Helm, and Argo CD as if they compete for the same job. They don't.

        Provisioning the cluster and cloud resources around it, templating and shipping the workloads that run on it, and reconciling what's already running are three different problems. Conflating them is why so many Kubernetes IaC setups end up with three tools stitched together by scripts nobody trusts.

        We broke the landscape down by layer instead: Pulumi, Terraform and OpenTofu, Helm, Kustomize, Crossplane, Argo CD and Flux, cdk8s, and kro, each reviewed honestly, including where it isn't the right fit.

        A worked side-by-side (the same EKS cluster and workload in Terraform HCL and Pulumi TypeScript) and a five-step framework for picking a stack round it out.
    bluesky: |
        Kubernetes IaC roundups usually rank Terraform against Helm against Argo CD like they're interchangeable. They're solving different problems: cluster provisioning, workload templating, and reconciliation.

        We compared nine tools by layer instead, including where each one falls short.
---

There is no single best Kubernetes infrastructure as code tool, because "Kubernetes IaC" actually spans three different jobs. For provisioning the cluster and its cloud dependencies, Pulumi and Terraform (or OpenTofu) are the strongest general-purpose options. For templating and packaging workloads, Helm and Kustomize dominate. For continuous reconciliation once things are running, Argo CD and Flux lead the GitOps category. The right stack usually combines one tool from each layer, not a single tool that claims to do all three.

<!--more-->

## What counts as infrastructure as code for Kubernetes?

Kubernetes infrastructure as code work splits into three layers that get conflated constantly, and the confusion is where most tool comparisons go wrong.

The **cluster and cloud layer** provisions the things Kubernetes itself sits on top of: the managed control plane (EKS, GKE, AKS), node pools, the VPC and subnets, IAM roles, load balancers, and cluster add-ons. Terraform, Pulumi, and cloud-native tools like CloudFormation operate here.

The **in-cluster workload layer** defines what runs on the cluster once it exists: Deployments, Services, ConfigMaps, CustomResourceDefinitions, and the Helm charts or Kustomize overlays that template them. This is where Helm, Kustomize, and Crossplane's custom resources live.

The **delivery and reconciliation layer** keeps what's declared in Git in sync with what's actually running on the cluster, continuously, rather than as a one-shot apply. Argo CD and Flux own this layer, and they consume the output of the other two rather than replacing them.

Most real Kubernetes platforms use tools from at least two of these layers together. A team might provision EKS with Terraform, package its application with Helm, and let Argo CD reconcile it continuously. Knowing which layer a tool actually addresses, rather than treating "Kubernetes IaC" as one shopping list, is the first decision that matters.

## Pulumi provisions the cluster and the workloads on it in the same language

Pulumi is a general-purpose infrastructure as code platform that supports Python, TypeScript, Go, C#, Java, and YAML, backed by a [dedicated Kubernetes provider](https://www.pulumi.com/registry/packages/kubernetes/) that covers both the cluster layer and the workload layer in the same program. A single Pulumi stack can create an EKS cluster, its VPC and node groups, and the Deployments and Services that run inside it, with full dependency tracking between the two: Pulumi knows a Deployment depends on a cluster that does not exist yet, and sequences accordingly.

For workloads, Pulumi offers two distinct ways to work with Helm charts. [`kubernetes.helm.v4.Chart`](https://www.pulumi.com/registry/packages/kubernetes/how-to-guides/choosing-the-right-helm-resource-for-your-use-case/) renders a chart client-side via `helm template` into individual resources, giving full Pulumi state, diffing, and policy visibility into every object a chart creates, at the cost of not producing a real Helm release. `kubernetes.helm.sh/v3.Release` installs through the embedded Helm SDK instead, producing an actual release with hooks, and can even import releases installed by the Helm CLI. Teams pick based on whether they need release semantics or resource-level visibility; Pulumi's documentation is upfront that these are genuinely different tradeoffs, not that one supersedes the other. Kustomize overlays are supported directly through [`kubernetes.kustomize.v2.Directory`](https://www.pulumi.com/registry/packages/kubernetes/api-docs/kustomize/v2/directory/).

As of the v4 provider, Server-Side Apply is the default for managing resources, which lets Pulumi share ownership of an object with other controllers safely instead of overwriting whatever they changed. Await and readiness logic (waiting for a Deployment's rollout to finish before considering it "done") is handled natively for common resource types, with `skipAwait` and `waitFor` escape hatches for anything unusual. As Pulumi engineer Bryce Lampe put it when the improved await logic shipped, "One of the advantages of using Pulumi to manage Kubernetes resources is that it natively and intuitively handles this problem of readiness and dependencies," which matters more than it sounds: a naive apply-and-move-on model is a common source of flaky CI in Kubernetes pipelines.

Pulumi also plugs into an existing GitOps workflow rather than requiring you to replace it: the [Kubernetes provider's `renderYamlToDirectory` option](https://www.pulumi.com/registry/packages/kubernetes/api-docs/provider/) renders manifests to disk instead of applying them directly, a pattern Pulumi's own provider documentation calls out as an Argo CD Config Management Plugin use case. The provider currently labels this a developer-preview beta feature, disabled by default, so treat it as a bridge worth piloting rather than a settled default for a GitOps handoff. For CRDs, [`crd2pulumi`](https://www.pulumi.com/docs/integrations/clouds/kubernetes/crd2pulumi/) generates strongly typed SDKs from CRD definitions, so a custom resource gets the same autocomplete and type-checking as a built-in one. Teams running Pulumi as a standing service inside the cluster can use the [Pulumi Kubernetes Operator](https://www.pulumi.com/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) to drive stack updates from in-cluster custom resources.

The honest tradeoff: Pulumi is a commercial platform with an open-source core, and a team fully committed to a YAML-only, kubectl-native workflow will find a general-purpose language layer to be more machinery than it needs for a handful of static manifests. Materialize, which runs multi-region Amazon EKS clusters, [adopted Pulumi from day one to manage that complexity in Python](https://www.pulumi.com/case-studies/materialize/#executive-summary), after finding that tools like Terraform required developers to learn a proprietary configuration language and created unnecessary friction; new engineers reach their first meaningful contribution in a week rather than the month the team estimates it would otherwise take. A team with one cluster and no cross-region variation may not have that problem to solve.

## Terraform and OpenTofu remain the default for the cluster layer, with real friction at the workload layer

Terraform (and its community-governed fork, OpenTofu, since HashiCorp's Business Source License change) is still the most widely deployed way to provision the cluster itself: the AWS, Google, and Azure providers are mature, and the Kubernetes and Helm providers (currently at 3.2.1 and 3.2.0 respectively) let the same HCL codebase reach into the cluster afterward. That reach is also where the friction shows up. Terraform plans at plan time, before it has ever talked to a live cluster, so it frequently cannot know what a CRD's schema actually looks like until it's already been applied; this is a well-documented source of "plan differs from apply" surprises when CRDs and their consumers live in the same configuration. The common workaround is a two-stage apply, provisioning the cluster in one Terraform run and the workloads that depend on its CRDs in a second, which works but adds operational ceremony that a single-language, single-run tool doesn't need.

HCL itself is also a genuine limit at the workload layer: templating a Deployment's environment variables across ten similar services means either heavy use of `for_each` and dynamic blocks, or accepting a lot of copy-pasted HCL, because HCL was designed as a configuration language rather than a general-purpose one with functions and reusable abstractions. None of this makes Terraform a poor choice for the cluster layer, where it remains a defensible default with a huge ecosystem of examples and modules. It's a reason many Terraform shops hand workload templating off to Helm rather than fighting the Kubernetes provider for it.

## Helm is the default packaging format, and now defaults to safer applies

[Helm](https://helm.sh/) is the de facto package manager for Kubernetes: charts bundle a set of manifests with a templating layer and values files, and the public Artifact Hub ecosystem aggregates charts from vendors and the community, so most common software (databases, ingress controllers, observability stacks) has a chart available, official or otherwise. Helm 4 made Server-Side Apply the default instead of the old three-way merge against a stored last-applied-configuration annotation, which reduces a class of drift bugs that plagued Helm 3 installs sharing objects with other controllers. It also added WASM-based plugins and an experimental v3 chart format.

Helm's real weakness is templating itself: charts are YAML run through Go's text/template engine, which has no real type system, awkward conditionals, and error messages that point at rendered output rather than the source template. Values files also tend to sprawl as a chart tries to expose every possible customization, and a chart author's defaults are a starting point you inherit rather than infrastructure you designed. Helm is excellent for consuming someone else's well-maintained chart and mediocre as an authoring experience for your own complex, multi-service application, which is exactly why tools like Pulumi and Kustomize exist to sit on either side of it.

## Kustomize is the built-in choice for environment-specific overlays

[Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) ships inside `kubectl` and takes a patch-based approach instead of a templating one: you write a base set of plain YAML manifests, then layer environment-specific overlays (a different replica count for staging, a different image tag for production) that patch the base without touching it. That model avoids Helm's templating-language problem entirely, at the cost of being far less expressive for anything beyond structural changes to existing YAML: generating a resource conditionally, or computing a value, is awkward or impossible.

The practical friction is version lag: the Kustomize binary bundled inside a given `kubectl` release trails the standalone Kustomize CLI's releases, so a team relying on kubectl's bundled version can be several minor versions behind what's documented upstream. Teams that hit this usually install the standalone `kustomize` binary directly rather than depend on kubectl's copy.

## Crossplane turns cloud resources into Kubernetes-native APIs

[Crossplane](https://www.crossplane.io/), which graduated to a CNCF top-level project on November 6, 2025, takes a fundamentally different approach: instead of a CLI that applies configuration, cloud resources become [managed resources](https://docs.crossplane.io/latest/managed-resources/managed-resources/), native Kubernetes custom resources that a control-plane cluster reconciles continuously, overriding drift back to the desired state, the same way Kubernetes reconciles a Deployment. This is a genuinely different mental model from Terraform, Pulumi, or Helm, and it's the right one for platform teams building a self-service layer where application teams request infrastructure (an S3 bucket, a Postgres instance) through the same `kubectl apply` and RBAC model they already use for everything else.

Crossplane v2 removed native patch-and-transform composition and introduced namespaced Composite Resources (XRs) alongside an alpha "Operations" feature for one-off imperative tasks. Claims, the v1 abstraction that let application teams request infrastructure without touching the (cluster-scoped) XR directly, were already namespaced; what changes in v2 is that they [aren't supported](https://docs.crossplane.io/v2.0/whats-new/) by the new namespaced or cluster-scoped XRs at all, and survive only when an XRD opts into the `LegacyCluster` scope for backward compatibility. Teams on Crossplane v1 migrating to v2 should plan to move application teams onto namespaced XRs directly rather than assume claims carry forward as-is. It also means Crossplane's learning curve is steeper than a CLI-based tool: composing custom APIs out of managed resources requires understanding Crossplane's own compositional model in addition to the cloud provider's resource shapes. Teams that don't need a self-service internal platform, and just want to provision infrastructure for their own team, usually find Terraform or Pulumi a faster path to the same cloud resources.

## Argo CD and Flux reconcile what's running, and assume something else already authored it

[Argo CD](https://argo-cd.readthedocs.io/) (CNCF graduated December 2022, now at 3.5.1) and [Flux](https://fluxcd.io/) (CNCF graduated November 2022, now at 2.9.4) are the two dominant GitOps controllers: both watch a Git repository and continuously compare the cluster's actual state against what's declared there, surfacing drift as it appears and correcting it automatically when self-healing is enabled, rather than waiting for the next scheduled apply. This is the delivery layer from the three-layer breakdown above, and it's genuinely complementary to, not competitive with, Terraform, Pulumi, Helm, and Kustomize: Argo CD and Flux consume rendered manifests or chart references, they don't generate cloud infrastructure or author application configuration themselves.

The CNCF's 2025 annual survey found that GitOps adoption tracks organizational maturity closely: 58% of self-identified "cloud native innovators" use GitOps extensively, compared to 23% of "adopters" earlier in their journey, which suggests GitOps is a practice teams grow into rather than a day-one requirement. Neither Argo CD nor Flux replaces the need for a provisioning tool at the cluster layer; a common and reasonable pattern is Terraform or Pulumi for the cluster and cloud dependencies, then Argo CD or Flux reconciling the workloads that run on it, with Pulumi's `renderYamlToDirectory` option (currently a developer-preview beta feature) designed to feed that second stage.

## cdk8s and kro bring code and native APIs to workload definitions

[cdk8s](https://github.com/cdk8s-team/cdk8s) applies the AWS CDK model to Kubernetes manifests: you define Deployments, Services, and other objects in TypeScript, Python, Java, or Go, and cdk8s synthesizes plain YAML at build time, which plays nicely with existing GitOps pipelines since the output is still just manifests. It's a narrower tool than Pulumi in scope, generating Kubernetes YAML only rather than also provisioning the cluster and cloud resources around it, and it has no equivalent to Pulumi's state-tracked diffing or drift detection since it only emits manifests for something else to apply. The core `cdk8s` library is stable on the 2.x line; the higher-level `cdk8s+` construct libraries are versioned and released separately per supported Kubernetes version.

[kro](https://github.com/kubernetes-sigs/kro) takes Crossplane's "infrastructure as a native API" idea and generalizes it: it [composes any native Kubernetes resource as well as any CRD installed in the cluster](https://docs.aws.amazon.com/eks/latest/userguide/kro.html), Crossplane's managed resources included, into a new custom API that platform teams expose to their users. kro recently moved into the `kubernetes-sigs` organization as a SIG Cloud Provider subproject, which is a credibility signal, but it remains genuinely alpha (`v1alpha1` APIs, releases still in the 0.7 to 0.9.3 range) and is not yet a CNCF top-level project. It's worth watching and piloting, not yet a safe default for anything you can't easily rebuild.

A handful of other projects are worth knowing about without needing a full section: [Timoni](https://timoni.sh/) applies CUE's type system to Kubernetes packaging as a Helm alternative; [KubeVela](https://kubevela.io/) builds an application-delivery abstraction on top of the Open Application Model; [Tanka](https://tanka.dev/) uses Jsonnet for templated manifests in the Grafana Labs ecosystem; and Ansible's Kubernetes modules remain common in shops that already standardized on Ansible for configuration management generally.

## How the tools compare across cluster, workload, and delivery layers

Reconciliation model is the dimension most roundups leave out, and it matters as much as authoring language: a one-shot apply tool and a continuously reconciling controller solve different problems even when they touch the same YAML.

| Tool | Authoring language | Provisions cloud + cluster? | Reconciliation model | Maturity / governance | Best fit |
|---|---|---|---|---|---|
| Pulumi | Python, TypeScript, Go, C#, Java, YAML | Yes | One-shot apply (`pulumi up`), continuous via Kubernetes Operator | Open-source core, commercial platform | Teams wanting one codebase for cluster + workloads |
| Terraform / OpenTofu | HCL | Yes | One-shot apply | Terraform: HashiCorp/IBM; OpenTofu: Linux Foundation | Cluster and cloud provisioning, HCL-standardized shops |
| Helm | YAML + Go templates | No (workload only) | One-shot install/upgrade | CNCF graduated | Packaging and consuming shared application charts |
| Kustomize | YAML (patch-based) | No (workload only) | One-shot apply | Built into `kubectl`, part of Kubernetes SIG-CLI | Environment overlays on plain manifests |
| Crossplane | Kubernetes YAML / CRDs | Yes (via managed resources) | Continuous reconciliation | CNCF graduated Nov 2025 | Self-service internal platforms |
| Argo CD | Kubernetes YAML (consumed) | No (delivery only) | Continuous reconciliation | CNCF graduated | GitOps delivery, UI-driven ops |
| Flux | Kubernetes YAML (consumed) | No (delivery only) | Continuous reconciliation | CNCF graduated | GitOps delivery, GitOps Toolkit composability |
| cdk8s | TypeScript, Python, Java, Go | No (workload only) | One-shot synth to YAML | Stable 2.x core, CNCF Sandbox | Code-first manifest generation feeding existing GitOps |
| kro | Kubernetes YAML / CRDs | Yes (composes existing CRDs) | Continuous reconciliation | Alpha, `kubernetes-sigs` subproject | Composing custom platform APIs, early adopters |

## The same task in Terraform and Pulumi

The clearest way to see the practical difference is the same job in both: create a managed EKS cluster and deploy a single workload onto it.

Terraform provisions the cluster with the AWS provider, then reaches into it with the Kubernetes provider in the same configuration:

```hcl
resource "aws_eks_cluster" "main" {
  name     = "app-cluster"
  role_arn = aws_iam_role.eks.arn

  vpc_config {
    subnet_ids = aws_subnet.private[*].id
  }
}

provider "kubernetes" {
  host                   = aws_eks_cluster.main.endpoint
  cluster_ca_certificate = base64decode(aws_eks_cluster.main.certificate_authority[0].data)
  token                  = data.aws_eks_cluster_auth.main.token
}

resource "kubernetes_deployment" "app" {
  metadata {
    name = "app"
  }

  spec {
    replicas = 3

    selector {
      match_labels = { app = "app" }
    }

    template {
      metadata {
        labels = { app = "app" }
      }

      spec {
        container {
          name  = "app"
          image = "myorg/app:1.4.0"
        }
      }
    }
  }
}
```

Pulumi, in TypeScript, does the same two-stage job with the dependency between them tracked automatically, rather than requiring a separate provider block wired up by hand:

```typescript
import * as aws from "@pulumi/aws";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

const cluster = new eks.Cluster("app-cluster", {
    instanceType: "t3.medium",
    desiredCapacity: 3,
});

const provider = new k8s.Provider("k8s-provider", {
    kubeconfig: cluster.kubeconfig,
});

const app = new k8s.apps.v1.Deployment("app", {
    spec: {
        replicas: 3,
        selector: { matchLabels: { app: "app" } },
        template: {
            metadata: { labels: { app: "app" } },
            spec: {
                containers: [{ name: "app", image: "myorg/app:1.4.0" }],
            },
        },
    },
}, { provider });
```

Both are legitimate. Terraform's version separates concerns across a provider block and requires knowing the Kubernetes provider's HCL shape for a Deployment resource; Pulumi's version is fewer moving pieces because the cluster's kubeconfig flows directly into the next resource as a normal object reference, and the whole thing can be unit tested with the same test framework used for the application code it deploys.

## How to choose a Kubernetes IaC tool

Most teams end up combining tools across the three layers rather than picking one. Working through these five steps in order avoids the most common mistake, which is picking a workload-layer tool (like Helm) and then trying to stretch it to also provision the cluster.

1. Decide who provisions the cluster and its cloud dependencies (VPC, node pools, IAM), and pick a cluster-layer tool for that job: Pulumi or Terraform/OpenTofu for most teams, or a cloud-native tool if you're single-cloud and want the tightest console integration.
2. Decide how workloads get packaged. If you're consuming other people's software (databases, ingress controllers, observability agents), Helm's chart ecosystem is hard to beat. If you're authoring your own application manifests, Kustomize overlays or a code-first approach (Pulumi, cdk8s) usually scale better than hand-templated Helm charts.
3. Decide whether you need a self-service internal platform. If application teams should be able to request infrastructure through `kubectl apply` without touching Terraform or Pulumi directly, Crossplane or kro are worth the steeper learning curve. If your platform team is the only one touching infrastructure, you likely don't need this layer yet.
4. Decide whether you need continuous reconciliation or a one-shot apply is enough. A small team deploying a few times a week can live with `terraform apply` or `pulumi up` in CI. A team running many clusters, or one where configuration drift is a recurring incident cause, benefits from Argo CD or Flux catching and correcting drift automatically.
5. Match the result to your team's actual skills, not the tool with the most GitHub stars. A team of application engineers who already write Python or TypeScript daily will move faster in a tool that speaks their language than in a new DSL, and a platform team that already lives in YAML and kubectl will get more value from Kustomize and Argo CD than from introducing a new language to learn.

## Is Terraform or Pulumi better for Kubernetes?

Neither is universally better; the choice depends on what happens after the cluster exists. Terraform's ecosystem of provider modules and examples is larger for pure cluster provisioning, and HCL is a smaller thing to learn than a full programming language. Pulumi's advantage shows up once workloads enter the picture: because the cluster and its workloads live in the same general-purpose language, dependencies between them are tracked automatically, the same testing and CI tools used for application code apply to infrastructure code, and CRD-heavy workloads avoid the plan-time unknowns that come from HCL not having talked to a live cluster yet. Teams already standardized on HCL across their infrastructure will find less reason to switch; teams that want one codebase and one language for cluster and workloads together tend to prefer Pulumi.

## What are the alternatives to Helm?

Kustomize is the most common alternative for teams that find Helm's templating language awkward, trading some expressiveness for patch-based simplicity on plain YAML. cdk8s replaces Helm's templating with a real programming language that synthesizes YAML at build time. Pulumi can render Helm charts directly through kubernetes.helm.v4.Chart for full state visibility, or install them as genuine Helm releases through kubernetes.helm.sh/v3.Release, without requiring a separate templating tool at all. Timoni applies CUE's type system as a more strictly typed alternative to Helm's Go templates. None of these fully replace Helm's chart ecosystem for consuming third-party software; they're strongest for authoring your own application's manifests.

## How do you manage a managed Kubernetes service like EKS, GKE, or AKS as code?

Managed Kubernetes services expose the control plane as a cloud resource like any other, so the tools that provision it are the same cluster-layer tools used for the rest of your cloud footprint: Terraform, OpenTofu, or Pulumi, using each cloud's native provider (aws_eks_cluster, google_container_cluster, azurerm_kubernetes_cluster, or Pulumi's equivalent resources and the higher-level @pulumi/eks package). The node pools, VPC, subnets, and IAM roles the control plane depends on get provisioned in the same run. What happens after the cluster exists, deploying and reconciling workloads, is a separate decision covered by the workload and delivery layers above, not something the cluster-provisioning tool needs to also own.

## Is GitOps a replacement for infrastructure as code?

No. GitOps tools like Argo CD and Flux reconcile what's already declared in Git against what's running on the cluster; they don't generate that declaration or provision the cloud infrastructure underneath it. A GitOps workflow still needs something upstream producing the manifests it reconciles, whether that's Helm charts, Kustomize overlays, cdk8s output, or Pulumi's renderYamlToDirectory rendering a stack to disk. GitOps is a delivery and drift-correction practice layered on top of infrastructure as code, not a substitute for the provisioning step itself.

## Do you need Kubernetes-specific IaC tooling at all?

Not always. A team running a single small cluster with a handful of stable workloads can reasonably manage everything with plain kubectl apply against version-controlled YAML and skip templating tools entirely; the complexity Helm, Kustomize, and Crossplane solve only shows up once you have multiple environments, multiple similar services, or multiple teams needing self-service access. The honest signal that it's time to adopt tooling is repetition: the same YAML copied and hand-edited across environments, or the same cluster-provisioning steps run manually more than once, is worth automating before it causes an incident.

## Which Kubernetes IaC tool should you choose?

There's no single winner because "Kubernetes IaC" spans three different jobs. Most production setups combine a cluster-layer tool (Pulumi or Terraform), a workload-layer tool (Helm, Kustomize, or a code-first option), and often a delivery-layer tool (Argo CD or Flux) once the team is large enough to need continuous reconciliation. The five-step framework above is a better starting point than any single ranked list, because the right combination depends on your team's language preferences, how many environments you run, and whether you need to expose infrastructure to other teams as a self-service API.

## Frequently asked questions

### Does Pulumi replace Helm and Kustomize?

Not entirely. Pulumi can render Helm charts and apply Kustomize overlays directly from its Kubernetes provider, so a team can consume the existing Helm and Kustomize ecosystems from inside a Pulumi program rather than needing a separate CLI step. For authoring new manifests from scratch, Pulumi's general-purpose language is an alternative to writing Helm templates or Kustomize bases, but plenty of teams use Pulumi for the cluster layer while still authoring workload manifests as Helm charts.

### Can you use more than one of these tools together?

Yes, and most real deployments do. A common combination is a cluster-layer tool (Terraform or Pulumi) for the control plane and cloud dependencies, a workload-layer tool (Helm or Kustomize) for packaging what runs on it, and a delivery-layer tool (Argo CD or Flux) for continuous reconciliation. The three-layer breakdown at the top of this post exists precisely because these tools are usually complementary rather than competing for the same job.

### Is Crossplane a replacement for Terraform or Pulumi?

Not for most teams. Crossplane's strength is exposing infrastructure as native Kubernetes APIs so application teams can self-serve through kubectl, which is a platform-engineering pattern, not a general substitute for a cluster-provisioning tool. A platform team still typically uses Terraform or Pulumi to provision the Crossplane control-plane cluster itself and configure Crossplane's provider credentials.

### Why did the CNCF's 2025 survey findings matter for this comparison?

The CNCF's 2025 Annual Cloud Native Survey found 82% of container users now run Kubernetes in production, up from 66% in 2023, and 47% cited cultural change, more than training or security, as the top adoption challenge. Those numbers matter for tool choice because Kubernetes adoption has moved well past early adopters into mainstream production use, which means the tooling decision is increasingly about fitting an existing team's skills and processes rather than picking a tool for a greenfield experiment.

## Where to go next

For the cluster-provisioning layer specifically, the [Pulumi Kubernetes getting-started guide](https://www.pulumi.com/docs/iac/get-started/kubernetes/) walks through creating a cluster and deploying a first workload. The [Pulumi vs. Helm comparison](https://www.pulumi.com/docs/iac/comparisons/helm/) and [Pulumi vs. Crossplane comparison](https://www.pulumi.com/docs/iac/comparisons/crossplane/) go deeper on the workload- and platform-layer tradeoffs summarized here, and the [Pulumi vs. Terraform comparison](https://www.pulumi.com/docs/iac/comparisons/terraform/) covers the cluster-layer decision in more depth than a roundup can. If your infrastructure spans more than Kubernetes, [our broader infrastructure as code tools roundup](https://www.pulumi.com/blog/infrastructure-as-code-tools/) compares the cloud-provisioning landscape beyond the cluster.

For running AI workloads specifically on Kubernetes, [our companion piece on provisioning and governing infrastructure for AI agents](https://www.pulumi.com/blog/ai-agents-on-kubernetes/) covers GPU-aware scheduling, credentials, and where policy as code and Pulumi's Neo agent fit into that picture. And if a self-service platform for other teams is the eventual goal, [Pulumi's IDP documentation](https://www.pulumi.com/docs/idp/) covers the components, templates, and policy guardrails that turn infrastructure code into something other teams can safely consume without needing to understand Pulumi themselves.

Whatever combination you land on, the layer breakdown here is the durable part: know whether you're solving a cluster problem, a workload problem, or a reconciliation problem before you compare tools, because most of the disagreement in "best Kubernetes IaC tool" debates comes from comparing tools that were never solving the same problem in the first place.
