---
title: What Is GitOps?
meta_desc: "GitOps manages infrastructure and apps with Git as the single source of truth and agents that reconcile live state to match. Learn how it works."
type: what-is
page_title: "What Is GitOps?"
authors: ["alex-leventer"]
---

**GitOps is an operational model that manages infrastructure and applications by treating a Git repository as the single source of truth for the desired state of a system, with automated agents that continuously reconcile the live environment to match what is declared in Git.** Every change happens through a Git commit and a pull request, and software running inside the environment pulls those changes and applies them, so the repository, not a person running commands, is the authority on what should be deployed.

The model takes the same practices that software teams already use for application code (version control, pull requests, code review, and automation) and applies them to the operation of the systems that code runs on. The result is that operations become auditable, repeatable, and reversible: the state of production is whatever the repository says it is, and rolling back is a `git revert`.

In this article, we'll cover the key questions about GitOps:

* What is GitOps?
* Why does GitOps matter?
* What are the four principles of GitOps?
* How does GitOps work?
* What are the benefits of GitOps?
* What GitOps tools are available?
* Push-based vs. pull-based GitOps: what's the difference?
* How does Pulumi support GitOps?
* Frequently asked questions about GitOps

## What is GitOps?

GitOps is a way of operating cloud-native systems in which the desired state of the entire system (infrastructure, configuration, and applications) is described declaratively, stored in Git, and applied automatically by software agents that reconcile the running environment against the repository.

The term was coined by Weaveworks in 2017, drawing on the model Kubernetes had popularized: describe what you want as declarative configuration, and let a controller work continuously to make reality match. GitOps generalizes that idea. Instead of a person running `kubectl apply` or `terraform apply` from a laptop or a CI job, the source of truth lives in a Git repository, and an agent running inside the cluster or platform watches that repository and applies whatever it finds.

The distinction matters because it changes where authority lives. In a traditional pipeline, whoever can run the deploy command controls production. In GitOps, the only way to change production is to change Git, which means every change inherits the guarantees Git already provides: a reviewer approved it, the history records who changed what and when, and any state can be restored by reverting to an earlier commit.

## Why does GitOps matter?

As organizations adopt Kubernetes and multi-cloud infrastructure, the number of things that must be deployed, configured, and kept in sync grows faster than any team can manage by hand. Manual `kubectl` and imperative scripts don't scale, and they leave no reliable record of what was actually applied or by whom.

GitOps matters because it solves three problems that compound at scale. **Drift**: live environments diverge from their intended configuration when people make out-of-band changes, and without continuous reconciliation, no one notices until something breaks. **Auditability**: compliance and security teams need to know exactly what is running and how it got there, which is impossible when changes come from ad-hoc commands. **Recovery**: when a bad change reaches production, teams need to roll back quickly and confidently, which requires a known-good state to return to.

By making Git the source of truth and running agents that reconcile against it, GitOps gives every change an approval trail, surfaces drift automatically, and turns disaster recovery into re-applying the repository to a fresh cluster. These properties are why GitOps became the dominant delivery pattern for Kubernetes and why the practice has expanded to cloud infrastructure more broadly.

## What are the four principles of GitOps?

The [OpenGitOps](https://opengitops.dev/) project, a CNCF-backed working group, defines GitOps through four principles. A system is doing GitOps when all four hold:

1. **Declarative.** The desired state of the whole system is expressed declaratively. You describe *what* the system should look like, not the step-by-step commands to get there.

2. **Versioned and immutable.** That desired state is stored in a way that enforces immutability and versioning, and retains a complete history. Git is the canonical implementation, but the principle is about the storage guarantees, not the specific tool.

3. **Pulled automatically.** Software agents automatically pull the desired state from the source of truth. Nothing is pushed from an external system; the agent inside the environment fetches the declarations.

4. **Continuously reconciled.** Agents continuously observe the actual system state and reconcile it against the desired state, correcting drift whenever the two diverge.

The fourth principle is what separates GitOps from "storing YAML in Git." Reconciliation is an ongoing loop, not a one-time deploy: if someone changes a resource by hand, the agent notices the divergence from Git and either corrects it or flags it, depending on configuration.

## How does GitOps work?

A GitOps workflow follows a consistent lifecycle regardless of which tool implements it.

**Declare the desired state.** Engineers describe infrastructure and applications as declarative configuration (Kubernetes manifests, Helm charts, or infrastructure as code programs) and commit it to a Git repository. This repository becomes the single source of truth.

**Propose changes through pull requests.** A change to the system is a change to the repository. An engineer opens a pull request, which goes through code review, automated tests, and policy checks before merging. The pull request is the control point: nothing reaches production without passing through it.

**Merge to the source of truth.** When the pull request is approved and merged, the repository now reflects the new desired state. No deployment has happened yet; only Git has changed.

**Agents pull and reconcile.** A GitOps agent running inside the environment detects the new commit, pulls the updated configuration, and applies it to the live system. The agent then continues watching, comparing actual state against the repository on an ongoing basis.

**Reconcile drift continuously.** If the live environment drifts from what Git declares (a manual change, a failed node, a deleted resource), the agent detects the divergence and either reconciles automatically or reports it, so the running system converges back to the declared state.

Because the entire flow runs through Git and an in-cluster agent, the audit trail is complete, rollbacks are a revert, and disaster recovery is re-pointing an agent at the repository.

## What are the benefits of GitOps?

**A complete audit trail.** Every change to production is a Git commit with an author, a timestamp, a reviewer, and a diff. Compliance evidence is the repository history, not a reconstruction after the fact.

**Fast, reliable rollbacks.** Reverting a change is reverting a commit. Because the agent reconciles to whatever Git says, rolling back is as simple and as tested as rolling forward.

**Drift detection and self-healing.** Continuous reconciliation means out-of-band changes are caught automatically. Depending on configuration, the agent can correct drift on its own, keeping the live environment faithful to its declared state.

**Improved developer experience.** Developers interact with infrastructure the same way they interact with application code: pull requests, reviews, and merges. There is no separate deploy tooling to learn and no privileged access to production required to ship a change.

**Stronger security posture.** Because changes are pulled by an agent inside the environment rather than pushed from outside, credentials for the cluster never need to leave it. CI systems don't need production access; they only need to merge to Git.

## What GitOps tools are available?

Several mature tools implement GitOps, most of them focused on Kubernetes.

**Argo CD** is a declarative, pull-based GitOps continuous delivery tool for Kubernetes and a CNCF graduated project. It runs in the cluster, watches Git repositories, and reconciles application state, with a web UI that visualizes sync status and drift. Argo CD is widely adopted for application delivery and is often paired with Argo Rollouts for progressive delivery.

**Flux** is a set of continuous delivery and GitOps tools for Kubernetes, also a CNCF graduated project. Flux is built from composable controllers (source, kustomize, helm, notification) and integrates tightly with the Kubernetes API. It emphasizes a toolkit approach, letting platform teams assemble the reconciliation behavior they need.

**Pulumi Kubernetes Operator** brings GitOps to full infrastructure as code, not just Kubernetes manifests. It runs in the cluster, treats a Pulumi Stack as a Kubernetes custom resource, and reconciles cloud infrastructure (across every provider Pulumi supports) from a Git repository using a pull-based model.

| Tool | Primary scope | Model | Governance |
|---|---|---|---|
| Argo CD | Kubernetes application delivery | Pull-based | CNCF graduated |
| Flux | Kubernetes delivery (composable controllers) | Pull-based | CNCF graduated |
| Pulumi Kubernetes Operator | Cloud infrastructure as code + Kubernetes (every provider Pulumi supports) | Pull-based | Open source (Apache 2.0) |

Argo CD and Flux focus on reconciling Kubernetes resources. The Pulumi Kubernetes Operator extends the same GitOps discipline to the underlying cloud infrastructure (databases, networks, IAM, serverless) so a single workflow can manage both the cluster and everything it depends on.

## Push-based vs. pull-based GitOps: what's the difference?

GitOps implementations fall into two models, and the distinction has real security implications.

**Push-based** delivery has an external system (typically a CI pipeline) apply changes to the target environment after a merge. It's simpler to set up and reuses existing CI tooling, but it requires that the external system hold credentials for production, widening the attack surface.

**Pull-based** delivery has an agent running *inside* the target environment pull changes from Git and apply them. Credentials never leave the environment, the environment can sit in a private network unreachable from the internet, and reconciliation is continuous rather than triggered only at merge time. Pull-based is the model the OpenGitOps principles describe, and it's what Argo CD, Flux, and the Pulumi Kubernetes Operator implement.

Most teams treat pull-based reconciliation as the target state for security-sensitive environments, while push-based pipelines remain common for simpler setups or as a transitional step.

## How does Pulumi support GitOps?

Pulumi supports GitOps through several complementary paths, extending the model beyond Kubernetes manifests to the full breadth of cloud [infrastructure as code](/what-is/what-is-infrastructure-as-code/).

**Pulumi Kubernetes Operator.** The [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) implements pull-based GitOps for infrastructure. It runs inside the cluster and exposes a Pulumi stack as a first-class Kubernetes custom resource called `Stack`. You point a `Stack` resource at a Git repository and a branch, and the operator watches that branch, automatically running `pulumi up` whenever new code is pushed. Because it's pull-based, the operator can run in a private network with no inbound access, and it reconciles cloud resources across every provider Pulumi supports, not only Kubernetes objects.

**Pulumi Deployments and Git Push to Deploy.** [Pulumi Deployments](/docs/deployments/) provides a managed way to run Pulumi operations in response to Git activity. Git Push to Deploy connects a repository so that a push to a chosen branch drives a deployment for a given project path, and pull-request workflows can preview changes and post the results back to the PR before anything merges.

**Review stacks and pull-request previews.** Pulumi can stand up an ephemeral [review stack](/docs/deployments/concepts/review-stacks/) for each pull request, deploying a full copy of the infrastructure so reviewers see the actual effect of a change, then tearing it down when the PR closes. This keeps the pull request as the control point that GitOps depends on.

**Drift detection.** Pulumi Deployments can run scheduled [drift detection](/docs/deployments/concepts/drift/), comparing the live state of your infrastructure against what your Pulumi program declares and alerting (or remediating) when they diverge, which is the continuous-reconciliation principle applied to cloud infrastructure.

Because Pulumi programs are written in general-purpose languages (TypeScript, JavaScript, Python, Go, .NET, or Java) as well as YAML or HCL, the same GitOps workflow covers application config and the cloud infrastructure underneath it, and teams already running Argo CD or Flux can drive it from there through the [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/): [Argo CD syncs the operator's `Stack` resource](/docs/iac/operations/continuous-delivery/argocd/) from Git like any other manifest, and a `Stack` can take its program from a [Flux source](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/defining-stacks/#using-a-flux-source).

The through-line never changes, whichever tool you reach for: the repository holds the truth, and software keeps production faithful to it.

## Frequently asked questions about GitOps

### What is GitOps in simple terms?

GitOps means using a Git repository as the single source of truth for your systems. You describe what your infrastructure and applications should look like as declarative files in Git, and automated software applies those files to your environment and keeps the environment matching them. To change anything, you change Git; to undo a change, you revert the commit.

### Is GitOps only for Kubernetes?

No. GitOps originated in the Kubernetes community and the best-known tools (Argo CD and Flux) are Kubernetes-focused, but the principles apply to any declarative system. Infrastructure as code tools like Pulumi extend GitOps to cloud resources across 200+ providers, so the same model can manage databases, networks, and serverless functions, not just cluster workloads.

### What is the difference between GitOps and DevOps?

[DevOps](/what-is/what-is-devops/) is a broad cultural and organizational movement about collaboration between development and operations. GitOps is a specific operational pattern, one concrete way to implement continuous delivery, that uses Git as the source of truth and automated reconciliation to apply changes. GitOps is a way to practice DevOps for delivery, not a replacement for it.

### What is the difference between GitOps and CI/CD?

[CI/CD](/what-is/what-is-ci-cd/) automates building, testing, and delivering software, typically by pushing changes to environments from a pipeline. GitOps changes the delivery half: instead of a pipeline pushing to production, an agent inside the environment pulls the desired state from Git and reconciles continuously. GitOps and CI/CD are complementary; CI still builds and tests, and GitOps handles the deployment and reconciliation.

### What are the four principles of GitOps?

The OpenGitOps project defines them as declarative (the desired state is expressed declaratively), versioned and immutable (that state is stored with versioning and full history), pulled automatically (agents pull the desired state from the source), and continuously reconciled (agents continuously make the live system match the declared state).

### What is the difference between push-based and pull-based GitOps?

In push-based GitOps, an external system such as a CI pipeline applies changes to the environment, which means that system needs production credentials. In pull-based GitOps, an agent running inside the environment pulls changes from Git and applies them, so credentials stay inside the environment and reconciliation runs continuously. Pull-based is the model the OpenGitOps principles describe and the one most security-sensitive teams prefer.

### Does GitOps work with infrastructure as code?

Yes, and it's a natural fit. Infrastructure as code provides the declarative source of truth that GitOps requires. With Pulumi, the Kubernetes Operator reconciles infrastructure from Git in a pull-based model, while Pulumi Deployments drives changes from Git activity and runs scheduled drift detection, applying all four GitOps principles to cloud infrastructure.

## Learn more

Pulumi brings GitOps to your entire cloud footprint: the Pulumi Kubernetes Operator reconciles infrastructure from Git in a pull-based model, and Pulumi Deployments adds Git Push to Deploy, pull-request previews, and drift detection across 200+ providers. [Get started with the Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) to run your first GitOps reconciliation loop.

Related reading:

* [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/)
* [Pulumi Deployments](/docs/deployments/)
* [Review stacks for pull requests](/docs/deployments/concepts/review-stacks/)
* [Drift detection](/docs/deployments/concepts/drift/)
* [What is infrastructure as code?](/what-is/what-is-infrastructure-as-code/)
* [What is infrastructure drift?](/what-is/what-is-infrastructure-drift/)
* [What is CI/CD?](/what-is/what-is-ci-cd/)
* [What is DevOps?](/what-is/what-is-devops/)
* [What is platform engineering?](/what-is/what-is-platform-engineering/)
