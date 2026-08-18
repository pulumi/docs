---
title: "Terraform and Kubernetes: A Practical Guide for 2026"
date: 2026-08-07
draft: false
meta_desc: "How teams manage Kubernetes infrastructure as code in 2026: what Terraform's Kubernetes provider does well, where it strains, and how Pulumi compares."
authors:
    - pulumi-content-team
tags:
    - kubernetes
    - terraform
    - infrastructure-as-code
    - platform-engineering
category: general
faq_schema: true
howto_schema: true
related_posts:
    - ai-agents-on-kubernetes
    - yaml-terraform-pulumi-whats-the-smart-choice-for-deployment-automation-with-kubernetes

social:
    twitter: |
        Terraform can manage Kubernetes — the hashicorp/kubernetes provider works. But HashiCorp's own docs flag two limits: plan-time API access and a provider-credential ordering trap.

        Here's how that plays out in 2026:
    linkedin: |
        Terraform's kubernetes provider is a legitimate, well-maintained way to manage cluster objects as code. It's also worth reading HashiCorp's own warnings closely: kubernetes_manifest needs API access at plan time, and mixing cluster-provisioning resources with Kubernetes-provider resources in one module produces "intermittent and unpredictable errors."

        We wrote a practical, fair look at what that means day to day — what Terraform does well, where teams hit friction, how a general-purpose language (Pulumi's approach) changes testing and CRD handling, and how AI agents are starting to operate inside these workflows. Includes a step-by-step guide to provisioning a Kubernetes app stack with Pulumi.
    bluesky: |
        Terraform + Kubernetes, without the hot takes.

        What the hashicorp/kubernetes provider does well, HashiCorp's own documented limits (plan-time API access, provider ordering), and how a general-purpose language changes testing and CRD handling.
---

Yes, Terraform can manage Kubernetes: the official `hashicorp/kubernetes` provider lets you declare Deployments, Services, and other objects as HCL resources, and community providers like `kubectl` fill in the gaps. It works well for many teams. The friction shows up around two well-documented limits — provider ordering and plan-time API access — and around testing, where a general-purpose language changes what's possible.

That friction matters more in 2026 than it did a few years ago. Kubernetes infrastructure now sits next to AI-driven engineering workflows: agents that propose changes, run previews, and open pull requests need infrastructure code they can read, test, and reason about with the same tools they use for application code. A cluster definition written in HCL and a workload definition written in YAML are both harder for an agent — and a person — to unit test, refactor, or type-check than the equivalent in TypeScript, Python, or Go.

This guide is about the *operating model* for Kubernetes infrastructure: how the cluster, the platform layer, and the workloads on top of it get provisioned, tested, and shipped. It's a different question from "should I write my Kubernetes manifests in YAML, HCL, or a real language," which we cover in detail in [YAML, Terraform, or Pulumi: what's the smart choice for deployment automation with Kubernetes?](/blog/yaml-terraform-pulumi-whats-the-smart-choice-for-deployment-automation-with-kubernetes/) Read that post first if you're deciding how to author manifests; read this one for the wider workflow — provisioning, testing, policy, and where AI agents fit.

## How does Terraform manage Kubernetes today?

The `hashicorp/kubernetes` provider (current release v3.2.1, requiring Terraform 1.0.0 or later) is the primary path, and teams typically combine it with one or two others depending on what they're deploying:

| Approach | What it's for | Notes |
| --- | --- | --- |
| Typed resources (`kubernetes_deployment_v1`, `kubernetes_service_v1`, etc.) | Core, well-known object types | Full HCL validation and typed attributes for the objects the provider models explicitly |
| `kubernetes_manifest` | Custom resources or object types the provider doesn't model yet | Requires live API access during `terraform plan`, which shapes how it can be sequenced ([details](#what-are-the-hard-parts-of-managing-kubernetes-with-terraform)) |
| `hashicorp/helm` provider | Installing Helm charts | Wraps the Helm SDK; chart internals aren't individually visible to Terraform's plan/diff |
| Community `kubectl` provider (`alekc/kubectl`, a maintained fork of `gavinbunney/kubectl`) | Applying free-form YAML manifests | Common workaround for `kubernetes_manifest`'s plan-time requirement; newer versions support Terraform 1.10+ ephemeral resources so secrets don't have to land in state |

## What are the hard parts of managing Kubernetes with Terraform?

Two limitations show up often enough in practice that HashiCorp documents them directly, and they're worth quoting rather than paraphrasing:

- **Plan-time API access.** From the `kubernetes_manifest` resource docs: "This resource requires API access during planning time. This means the cluster has to be accessible at plan time and thus cannot be created in the same apply operation. We recommend only using this resource for custom resources or resources not yet fully supported by the provider." In practice this means you can't create a cluster and populate it with `kubernetes_manifest` resources in a single `terraform apply` — the cluster has to exist and be reachable before Terraform can even plan the manifest resources.
- **Provider-credential ordering.** From the provider's own index documentation: "When using interpolation to pass credentials to the Kubernetes provider from other resources, these resources SHOULD NOT be created in the same Terraform module where Kubernetes provider resources are also used. This will lead to intermittent and unpredictable errors which are hard to debug and diagnose. The root issue lies with the order in which Terraform itself evaluates the provider blocks vs. actual resources." HashiCorp's prescribed fix, also verbatim: "The most reliable way to configure the Kubernetes provider is to ensure that the cluster itself and the Kubernetes provider resources can be managed with separate `apply` operations. Data-sources can be used to convey values between the two stages as needed."

Both are solvable — split cluster provisioning and workload deployment into separate applies (or separate Terraform workspaces/modules), and pass values between them with data sources or remote state. It's a real pattern, and plenty of teams run it in production. It does mean two-stage pipelines and extra state plumbing wherever a cluster and its workloads are managed together.

## What changes when Kubernetes infrastructure is written in a general-purpose language?

Pulumi's Kubernetes provider is generated directly from the Kubernetes OpenAPI specifications (current version v4.33.0), so it stays current with the Kubernetes API surface automatically, and it runs inside a single Pulumi program in TypeScript, Python, Go, C#, Java, or YAML. Because the cluster resource and the workloads that depend on it are ordinary values in that program, sequencing them doesn't require splitting into separate applies — Pulumi's dependency graph resolves the ordering, and Server-Side Apply (the provider's default since v4.0) handles upserts consistently across resource types.

The provider also has built-in await logic for common object types — it knows a Deployment isn't "done" until its replicas are available, a Service isn't ready until it has endpoints or a load balancer ingress, and a Pod isn't ready until its readiness probe passes. That behavior is tunable with annotations: `pulumi.com/skipAwait`, `pulumi.com/timeoutSeconds`, the experimental `pulumi.com/waitFor` (supports a JSONPath value check, a JSONPath existence check, `condition=Synced`, or a JSON array of conditions), and `pulumi.com/deletionPropagationPolicy`.

For Helm, there are three options with different tradeoffs:

| Resource | How it works | Best for |
| --- | --- | --- |
| `helm.sh/v4.Chart` | Renders the chart client-side and manages each object as a distinct Pulumi resource; implemented as a component, so it works the same way across every Pulumi language, including Java and YAML; supports OCI registries | Teams that want every rendered object visible in the resource graph, diffable, and enforceable by policy |
| `helm.sh/v3.Chart` | Same client-side rendering approach, the previous major version | Existing usage; Pulumi has said it expects to deprecate this in a future release in favor of `v4.Chart` |
| `helm.sh/v3.Release` | Embeds the real Helm SDK and creates an actual Helm release, including hooks; can import chart releases installed via the Helm CLI | Charts that rely on Helm hooks, or environments already managed with the Helm CLI |

The practical distinction: `Chart` resources give you a resource graph you can diff and enforce policy against, one object at a time, but no Helm hooks and no CLI interop. `Release` gives you full Helm behavior, but policy enforcement can't reach into the resources a Helm release creates.

For CRDs, `crd2pulumi` reads a CustomResourceDefinition's OpenAPI schema and generates strongly typed classes in your language, so custom resources get IDE autocompletion and compile-time checking instead of the untyped `apiextensions.CustomResource` path. For plain manifests and Kustomize output, current guidance favors the versioned APIs — `yaml/v2.ConfigFile`, `yaml/v2.ConfigGroup`, and `kustomize/v2.Directory` — over their unversioned predecessors.

## How do you manage Kubernetes infrastructure with Pulumi?

A typical workflow for standing up an application on Kubernetes with Pulumi looks like this:

1. Install the Pulumi CLI and create a new project with `pulumi new kubernetes-typescript` (or the `-python`, `-go`, `-csharp`, or `-java` variant for your language).
2. Configure the target cluster context — either point Pulumi at an existing `kubeconfig`, or provision the cluster itself in the same program using your cloud provider's Pulumi provider (EKS, AKS, GKE, and so on).
3. Import the Kubernetes provider package for your language and instantiate a `Provider` resource if you need a non-default context or credentials.
4. Define your workloads as typed resources — a `Deployment`, a `Service`, a `ConfigMap` — using the same objects, loops, and functions you'd use in any other program in that language.
5. For existing Helm charts, use `helm.sh/v4.Chart` to render and manage the chart's resources individually, or `helm.sh/v3.Release` if you need full Helm hook support.
6. For CustomResourceDefinitions, run `crd2pulumi` against the CRD's schema to generate typed classes, then instantiate custom resources the same way as built-in types.
7. Run `pulumi preview` to see a diff of what will change, and `pulumi up` to apply it — Server-Side Apply and the provider's await logic handle upsert and readiness semantics automatically.
8. Wire the stack into CI by running `pulumi preview` on pull requests and `pulumi up` on merge, using the same pipeline and secrets store your application code already uses.

Here's step 4 in TypeScript, deploying a Deployment and a Service together in one program:

```typescript
import * as k8s from "@pulumi/kubernetes";

const appLabels = { app: "my-service" };

const deployment = new k8s.apps.v1.Deployment("my-service", {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 3,
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: "my-service",
                    image: "my-registry/my-service:1.4.0",
                    ports: [{ containerPort: 8080 }],
                }],
            },
        },
    },
});

const service = new k8s.core.v1.Service("my-service", {
    spec: {
        selector: appLabels,
        ports: [{ port: 80, targetPort: 8080 }],
        type: "LoadBalancer",
    },
});

export const serviceIp = service.status.loadBalancer.ingress[0].ip;
```

And the same shape in Python:

```python
import pulumi
import pulumi_kubernetes as k8s

app_labels = {"app": "my-service"}

deployment = k8s.apps.v1.Deployment(
    "my-service",
    spec=k8s.apps.v1.DeploymentSpecArgs(
        selector=k8s.meta.v1.LabelSelectorArgs(match_labels=app_labels),
        replicas=3,
        template=k8s.core.v1.PodTemplateSpecArgs(
            metadata=k8s.meta.v1.ObjectMetaArgs(labels=app_labels),
            spec=k8s.core.v1.PodSpecArgs(containers=[
                k8s.core.v1.ContainerArgs(
                    name="my-service",
                    image="my-registry/my-service:1.4.0",
                    ports=[k8s.core.v1.ContainerPortArgs(container_port=8080)],
                ),
            ]),
        ),
    ),
)

service = k8s.core.v1.Service(
    "my-service",
    spec=k8s.core.v1.ServiceSpecArgs(
        selector=app_labels,
        ports=[k8s.core.v1.ServicePortArgs(port=80, target_port=8080)],
        type="LoadBalancer",
    ),
)

pulumi.export("service_ip", service.status.load_balancer.ingress[0].ip)
```

Because `deployment` and `service` are ordinary values in the program, Pulumi resolves their dependency order automatically — there's no separate apply stage to sequence by hand, even if the cluster itself were provisioned earlier in the same program.

## How do you test Kubernetes infrastructure code before it ships?

Testing is one of the sharpest differences between the two approaches, and it's worth being precise about what each side actually offers:

| Capability | Terraform | Pulumi |
| --- | --- | --- |
| Unit tests (no cloud calls) | `.tftest.hcl` files with `command = plan`, plus `mock_provider` (GA since v1.7.0) for provider-free assertions | `pulumi.runtime.setMocks` (TypeScript), `pulumi.runtime.set_mocks` (Python), or `pulumi.WithMocks` (Go), run inside the same test framework as application code |
| Integration tests (real infra) | `.tftest.hcl` files with `command = apply` against a real or ephemeral environment | Automation API drives real preview/up/destroy cycles against ephemeral stacks, orchestrated from your own code |
| Test language | A second, declarative, test-specific language (`.tftest.hcl`) | The same language and test runner already used for application code — Jest, pytest, `go test`, xUnit |
| Policy enforcement | Sentinel or OPA/Rego, evaluated against the plan | Pulumi Policies (policy packs in TypeScript/JavaScript or Python) or OPA/Rego via `pulumi-policy-opa`, evaluated against the resource graph of a stack written in any Pulumi language |

`terraform test` with `mock_provider` is a legitimate, GA capability, and teams that have standardized on HCL testing patterns can write real infrastructure-free unit tests with it. The practical difference isn't "Terraform can't test" — it's that Terraform tests live in a separate language and toolchain from the application code they support, while Pulumi's tests run in the same Jest, pytest, or `go test` suite a team already runs on every commit. Because Kubernetes objects created through `Chart`, `ConfigGroup`, or `CustomResource` resources appear individually in Pulumi's resource graph, Pulumi Policies apply to them the same way they'd apply to a cloud resource — there's no separately named "Kubernetes policy" product, only the same policy-as-code engine applied to whatever's in the graph.

## Where do AI agents fit into Kubernetes infrastructure management?

An AI agent operating on infrastructure needs to read the current state, propose a change, preview its effect, and — ideally — get that change reviewed like any other pull request. That loop is much easier for an agent to execute reliably against a TypeScript or Python program than against HCL or raw YAML, because the agent can use the same static analysis, type checking, and test suite a developer would use, rather than reasoning about a domain-specific configuration language from scratch.

Pulumi Neo is built for exactly this loop: an infrastructure agent with organizational context, policy guardrails, and human-in-the-loop approvals, working inside the same preview/policy/apply cycle described above. We cover the fuller picture of provisioning and governing agent workloads on Kubernetes — GPU-aware scheduling, session state, and the security boundary around what an agent is allowed to touch — in [How to Run AI Agents on Kubernetes with Pulumi](/blog/ai-agents-on-kubernetes/).

## When is Terraform still the right choice for Kubernetes?

Fair comparisons cut both ways, and there are good reasons a team keeps using Terraform for Kubernetes:

- **Provider and module catalog breadth.** Terraform's registry has the largest catalog of providers and community modules of any IaC tool, and that matters for teams integrating many third-party systems alongside Kubernetes.
- **A single tool across the whole estate.** Teams that have already standardized on Terraform for networking, IAM, and managed services often prefer one state model and one pipeline rather than introducing a second tool solely for Kubernetes.
- **HCL's simplicity for static configuration.** For infrastructure that's genuinely declarative and doesn't need loops, abstraction, or conditional logic, HCL reads and reviews cleanly.
- **Existing governance investment.** Teams with mature Sentinel or OPA policy libraries and deep in-house HCL expertise have real switching costs, and those costs are legitimate inputs to the decision.
- **The plan-time limitation is manageable in practice.** Once cluster provisioning and workload deployment are split into separate applies — HashiCorp's own documented pattern — the `kubernetes_manifest` plan-time requirement stops being a daily obstacle.

None of that is a reason to avoid Terraform outright; it's a reason to be clear-eyed about which parts of your Kubernetes workflow benefit most from a general-purpose language and which don't.

## How do you move Kubernetes infrastructure from Terraform to Pulumi?

Teams don't have to choose all-or-nothing. Pulumi's `pulumi convert` command translates existing Terraform HCL into a Pulumi program in your target language as a starting point for further editing, and Pulumi's guide to [migrating Kubernetes YAML and Helm charts](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/) and its [Terraform migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) both cover the mechanics in more depth.

Pulumi also now meets Terraform-standardized teams partway: Pulumi IaC supports native HCL as a language option, Pulumi Cloud can serve as a state backend for existing Terraform configurations, and Pulumi supports consuming Terraform modules directly. That coexistence story — not a forced rewrite — is often the more realistic starting point for a team with a large existing Terraform estate, including Kubernetes-adjacent infrastructure. Wiz, for example, uses Pulumi's Automation API to manage more than 1 million cloud resources, including tens of thousands of Kubernetes clusters across hundreds of data centers, with more than 100,000 daily infrastructure updates.

## Frequently asked questions

Common questions that come up when teams evaluate Terraform and Pulumi for Kubernetes specifically.

### Can Terraform manage a Kubernetes cluster and its workloads in one apply?

Not reliably, per HashiCorp's own documentation. The `kubernetes_manifest` resource needs live API access at plan time, so the cluster must already exist and be reachable before Terraform can plan workload resources against it. The documented pattern is to split cluster provisioning and workload deployment into separate `apply` operations and pass values between them with data sources or remote state.

### Does Pulumi replace kubectl and Helm?

No. Pulumi's Kubernetes provider applies the Kubernetes API the same way `kubectl` and Helm do — it doesn't replace the cluster API or the Helm packaging format. What it replaces is the imperative or templated workflow around applying manifests: instead of running `kubectl apply` or `helm install` by hand or from a shell script, you declare the desired state in a Pulumi program and let `pulumi up` reconcile it, with the same preview, diff, and rollback behavior Pulumi provides for any other cloud resource.

### Is Terraform's Kubernetes provider actively maintained?

Yes. The `hashicorp/kubernetes` provider is on major version 3 (v3.2.1 as of this writing, with v3.0.0 shipping in December 2025) and requires Terraform 1.0.0 or later. It's a first-party HashiCorp provider with regular releases.

### What's the difference between kubernetes_manifest and the community kubectl provider?

`kubernetes_manifest`, from HashiCorp's own provider, needs the cluster's API reachable at plan time and is recommended mainly for custom resources not yet modeled as typed resources. The community `alekc/kubectl` provider (a maintained fork of `gavinbunney/kubectl`) applies free-form YAML through its `kubectl_manifest` resource and is a common workaround for the plan-time requirement; recent versions also support Terraform's ephemeral resources so sensitive values don't have to be written to state.

### Can Pulumi and Terraform manage the same Kubernetes cluster at once?

Yes, in the sense that both talk to the same Kubernetes API and don't inherently conflict — the risk is the same one you'd have with any two tools managing overlapping objects: whichever tool last wrote a resource's desired state "owns" it until the other reconciles again. Most teams that run a mixed estate assign ownership by namespace, resource type, or workload boundary rather than letting both tools manage the same objects.

## Where to go next

Related reading on Pulumi and Kubernetes:

- [YAML, Terraform, or Pulumi: what's the smart choice for deployment automation with Kubernetes?](/blog/yaml-terraform-pulumi-whats-the-smart-choice-for-deployment-automation-with-kubernetes/) — the manifest-authoring comparison this guide deliberately doesn't repeat
- [How to Run AI Agents on Kubernetes with Pulumi](/blog/ai-agents-on-kubernetes/) — provisioning and governing infrastructure for agent workloads specifically
- [Kubernetes infrastructure as code: tools and best practices](/what-is/infrastructure-as-code-for-kubernetes/) — a broader look at the IaC options for Kubernetes
- [Unit testing Pulumi programs](/docs/iac/guides/testing/unit/) — the full mock API reference across languages
- [crd2pulumi](/docs/integrations/clouds/kubernetes/crd2pulumi/) — generating typed SDKs from CustomResourceDefinitions
- [Migrating to Pulumi from Terraform](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) and [from Kubernetes YAML and Helm](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/)
- [Pulumi's Kubernetes provider in the registry](/registry/packages/kubernetes/)
