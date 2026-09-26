---
title: "Composing platform golden paths: Crossplane and component models compared"
allow_long_title: true
date: 2026-09-25T06:00:00-07:00
draft: false
meta_desc: "Crossplane and Pulumi components take different bets on where composition lives. Here's how to decide which fits your platform team's golden paths."
feature_image: feature.png
authors:
    - joe-duffy
tags:
    - platform-engineering
    - kubernetes
    - infrastructure-as-code
    - components
    - crossplane
category: perspectives
schema_type: auto
social:
    twitter: "A golden path is only as good as the abstraction under it. Crossplane and Pulumi components make very different bets about where composition should live. Here's how to think about the tradeoff. #platformengineering #crossplane #iac"
    linkedin: "Every platform team building golden paths eventually asks the same question: where should the composition logic actually live? Crossplane answers it by putting a control plane in the middle, reconciling your custom APIs from inside Kubernetes. Pulumi's component model answers it by keeping composition inside the programming language and workflow you already use. Neither answer is wrong. They commit you to different operating surfaces, different team shapes, and different day-two costs. I wrote up how I think about the decision, and when each approach earns its keep. #platformengineering #iac #crossplane #kubernetes"
    bluesky: "Golden paths live or die on the abstraction underneath them. Crossplane and Pulumi components solve composition in very different places. Wrote up how to think about the tradeoff for platform teams."
---

Every platform team that builds a golden path is really making a decision about composition: how do you take a pile of cloud primitives and turn them into a handful of safe, opinionated building blocks that other teams can just use? The tool you reach for decides who operates the abstraction layer, where it lives, and what breaks when it does.

A **composition model** is the mechanism a platform uses to bundle lower-level resources into a higher-level, reusable unit. It decides three things: where the composition logic is authored, where it runs, and who is on the hook when the abstraction itself needs to change. Crossplane and Pulumi's component model are both mature, widely used answers to that question, and they land in different places on all three axes.

<!--more-->

## What a composition model actually decides

It's tempting to treat "composition" as a solved problem: define an abstraction once, let teams consume it, move on. In practice the model you pick commits your platform team to a specific operating surface, and that surface is what shows up in your on-call rotation six months later.

Three questions cut through most of the noise:

1. **Where does the abstraction get authored?** Inside a general-purpose language and its tooling, or inside a domain-specific schema that a control plane interprets?
2. **Where does reconciliation happen?** Continuously, by a long-running controller watching for drift, or on demand, when someone runs a deployment?
3. **What does the platform team have to operate to keep the abstraction alive?** A cluster and its controllers, or a CI/CD pipeline and a package registry?

Crossplane and Pulumi's component resources give different, defensible answers to all three, and the right choice depends more on what your platform team already runs well than on which tool is "better" in the abstract.

## How Crossplane's control-plane approach works

[Crossplane](https://www.crossplane.io/) turns a Kubernetes cluster into a control plane for your cloud. A **Provider** is a Crossplane package that adds a set of external APIs, AWS, Azure, GCP, and others, as Kubernetes custom resources called managed resources. Each managed resource is reconciled continuously by the provider's controller, the same pattern Kubernetes uses to keep a Deployment's pods running.

Composition sits a layer above that. A `CompositeResourceDefinition` (XRD) defines a new custom API that other teams can request; a `Composition` defines how that API gets fulfilled: which managed resources get created and how their fields map to the request. As of Crossplane v2, that mapping runs through a pipeline of composition functions, small programs written in Go templates, KCL, or plain patch-and-transform, rather than the native YAML patching that earlier versions relied on and has since been removed.

Crossplane v2 also changed the consumption model: composite resources and managed resources are namespaced by default, and Compositions can now assemble any Kubernetes resource, not only Crossplane's own managed resources. Claims, the old handoff object between a composite resource and the team consuming it, are gone in the new namespaced model, though a legacy cluster-scoped mode preserves them for existing setups. Crossplane [graduated to the CNCF's top maturity tier in November 2025](https://www.cncf.io/announcements/2025/11/06/cloud-native-computing-foundation-announces-crossplane-graduation/), with Upbound as the primary corporate steward of the open source project.

What this buys a platform team is continuous reconciliation: drift gets corrected automatically because the same controllers that created a resource keep watching it, the same mechanism that makes Kubernetes itself self-healing. What it costs is an operating surface: the cluster's own lifecycle, RBAC for who can create XRs and managed resources, credentials for every provider that talks to a cloud, and upgrades of core Crossplane plus every installed provider and function. Namespaced managed resources are fully available for AWS today; other major providers are still catching up as of this writing, which is worth checking before you commit a golden path to a specific one.

A composition, at a shape level, looks like this once you strip away most of the fields:

```yaml
apiVersion: apiextensions.crossplane.io/v1
kind: Composition
metadata:
  name: xpostgresinstances.database.example.org
spec:
  compositeTypeRef:
    apiVersion: database.example.org/v1
    kind: XPostgresInstance
  mode: Pipeline
  pipeline:
    - step: compose-rds
      functionRef:
        name: function-patch-and-transform
      input:
        apiVersion: pt.fn.crossplane.io/v1beta1
        kind: Resources
        resources:
          - name: rds-instance
            base:
              apiVersion: rds.aws.upbound.io/v1beta2
              kind: Instance
```

The consuming team requests an `XPostgresInstance`; the pipeline decides what that turns into underneath, and the cluster's controllers keep reconciling it from that point forward.

## How Pulumi's component model compares

Pulumi takes a different starting point: composition happens inside the same general-purpose language you already write your infrastructure in, not inside a separate schema a control plane interprets. A [component resource](/docs/iac/concepts/components/) is a class that extends `ComponentResource`, wraps a set of child resources, and exposes just the outputs a consumer needs. You write it in TypeScript, Python, Go, C#, Java, or YAML, the same way you'd write any other reusable abstraction, and Pulumi tracks parent/child relationships for dependency ordering and deletion, the way Terraform modules or AWS CDK constructs work but with a real language's control flow, tests, and package manager underneath.

The part that matters for a platform team building golden paths is that a component authored in one language is consumable from any of them. Package it once, publish it to the [Pulumi Registry](/registry/) or an organization's private registry, and a consuming team pulls it with `pulumi package add`, which fetches the source and generates an SDK in whatever language that team already uses. A component gets versioned like any other piece of software, with semver, changelogs, and a deprecation policy, because it is software.

The equivalent shape, authored as a component rather than a schema, reads like ordinary application code:

```typescript
class PostgresInstance extends pulumi.ComponentResource {
    public readonly connectionString: pulumi.Output<string>;

    constructor(name: string, args: PostgresArgs, opts?: pulumi.ComponentResourceOptions) {
        super("example:database:PostgresInstance", name, {}, opts);

        const instance = new aws.rds.Instance(`${name}-rds`, {
            engine: "postgres",
            instanceClass: args.instanceClass ?? "db.t3.medium",
        }, { parent: this });

        this.connectionString = instance.endpoint;
        this.registerOutputs({ connectionString: this.connectionString });
    }
}
```

A consuming team imports `PostgresInstance` the way they'd import any other package, in whichever language they use, and gets an IDE's autocomplete and type checking along with it.

Reconciliation in this model happens when someone runs `pulumi up`, typically from CI/CD on every merge, rather than continuously in the background. Teams that want the always-on, drift-correcting behavior Crossplane provides natively can run the [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/), which reconciles Pulumi stacks from inside a cluster via a `Stack` custom resource, without requiring the platform team to also own a general-purpose composition schema. Guardrails come from [Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/) enforced at `pulumi up` time and from [Pulumi ESC](/docs/esc/) for centralized secrets and configuration, both consumed the same way regardless of which language authored the component.

## When each fits a golden-path strategy

Neither model is the right default. The decision comes down to what your platform team already operates well and what your consuming teams already know.

Crossplane earns its keep when your golden paths are fundamentally Kubernetes-native, when you already have a team comfortable operating cluster infrastructure and provider upgrades, and when continuous drift correction across a fleet of resources matters more than the convenience of authoring in a general-purpose language. It shines when the resources being composed genuinely benefit from living alongside application workloads in the same cluster, sharing the same RBAC and GitOps tooling those workloads already use.

Pulumi's component model earns its keep when your platform spans more than Kubernetes, when the teams consuming your golden paths want to stay in their own language and IDE rather than learn a new schema, and when you'd rather version and test an abstraction the way you'd version and test any other library than operate a cluster whose sole job is running your composition logic. It also tends to fit better when the platform team is small: publishing a package and running `pulumi up` from CI/CD is a lighter operating commitment than standing up and maintaining a control plane, even a well-supported one.

A few concrete questions tend to settle the decision faster than a feature comparison would:

- **Is your consuming audience already fluent in Kubernetes manifests and CRDs, or in a general-purpose language?** Crossplane asks teams to request infrastructure through a custom API; components ask them to import a package.
- **Does your platform team already run and upgrade production Kubernetes clusters as a core competency?** If yes, adding Crossplane's control plane is incremental cost. If not, it's a new discipline to staff for.
- **How much of your estate needs continuous drift correction versus periodic, CI-driven reconciliation?** Fleets of long-lived, frequently-drifting resources favor a control plane; infrastructure that mostly changes when someone deploys favors the pipeline model.
- **Does composition need to span outside Kubernetes**, into SaaS providers, on-prem systems, or clouds without a clean CRD-based API? Components travel more easily there than a Kubernetes-native control plane does.

The two aren't mutually exclusive. It's common for a platform team to run Crossplane for the Kubernetes-resident parts of their estate while using Pulumi components everywhere composition needs to reach beyond the cluster, across clouds, SaaS providers, or on-prem systems that were never going to have a clean Kubernetes-native API in the first place.

## Choosing deliberately

The mistake worth avoiding is picking a composition model by default, because it's the one your team happened to reach for first, rather than because you've actually weighed the operating surface it commits you to. A control plane that nobody wants to run becomes a bottleneck as fast as a component library that nobody bothers to version. Golden paths are supposed to remove friction from your platform, not relocate it into a system your team didn't sign up to operate.

Whichever model you choose, the underlying goal is the same: give the teams building on your platform a small number of trustworthy, well-tested building blocks, and spend your own platform team's time on the abstraction rather than on the plumbing underneath it. If you're weighing that tradeoff for your own organization, [Pulumi's platform](/product/) is built around exactly this kind of self-service infrastructure, with components, policy, and secrets management as first-class parts of the same workflow your teams already use to ship software.
