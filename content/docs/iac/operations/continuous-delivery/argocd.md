---
title_tag: "Using Argo CD with Pulumi | CI/CD"
meta_desc: This page details how to use Argo CD with the Pulumi Kubernetes Operator to deploy infrastructure and applications through pull-based GitOps workflows.
title: Argo CD
h1: Using Argo CD with Pulumi
menu:
    iac:
        name: Argo CD
        parent: iac-operations-cicd
        weight: 10
aliases:
- /docs/iac/guides/continuous-delivery/argocd/
- /docs/iac/using-pulumi/continuous-delivery/argocd/
- /docs/guides/continuous-delivery/argocd/
- /docs/using-pulumi/continuous-delivery/argocd/
- /docs/iac/packages-and-automation/continuous-delivery/argocd/
---

[Argo CD](https://argo-cd.readthedocs.io/) is a declarative, pull-based GitOps continuous delivery tool for Kubernetes. Pulumi integrates with Argo CD through the [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) (PKO), which lets Argo CD manage Pulumi infrastructure the same way it manages any other Kubernetes manifest. This means you can use Argo CD to provision and update cloud resources beyond the Kubernetes API—including the clusters themselves.

## How Pulumi works with Argo CD

Argo CD does not run `pulumi` commands directly. Instead, Pulumi infrastructure is represented as a [`Stack` custom resource](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/#create-a-stack-resource)—a Kubernetes manifest that the Pulumi Kubernetes Operator knows how to reconcile.

{{% notes type="info" %}}
The `Stack` custom resource is not the same thing as a [Pulumi stack](/docs/iac/concepts/stacks/). A Pulumi stack is an isolated instance of a Pulumi program, identified as `organization/project/stack`. The `Stack` custom resource is a Kubernetes object that tells PKO which Pulumi stack to deploy and how—each one targets a single Pulumi stack through its `spec.stack` field.
{{% /notes %}}

The integration relies on two pieces:

- **Argo CD** syncs `Stack` manifests from Git to your cluster, like any other Kubernetes resource.
- **The Pulumi Kubernetes Operator** watches for `Stack` objects and runs the Pulumi deployment in a dedicated workspace pod.

A change flows through the system like this:

1. You commit a change to a `Stack` manifest (or to the Pulumi program it points at).
1. Argo CD detects the change in Git and syncs the `Stack` object to the cluster.
1. PKO reconciles the `Stack`, running `pulumi up` in a workspace pod.
1. PKO reports the result back through the `Stack` object's status, which Argo CD surfaces in its UI.

Because the deployment runs inside the operator, there is no pipeline step that invokes the Pulumi CLI. Argo CD's role is to keep the desired `Stack` specification in sync with Git.

## Prerequisites

Before you begin, make sure you have:

- A Kubernetes cluster with [Argo CD installed](https://argo-cd.readthedocs.io/en/stable/getting_started/).
- The [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) installed in the cluster.
- A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
- A Git repository containing your Pulumi program.
- A Git repository (or a directory within an existing repository) for the Kubernetes manifests that Argo CD will sync.

This guide assumes you are using Pulumi Cloud. PKO also supports self-managed state backends through the `Stack` resource's `spec.backend` field—see [States & backends](/docs/iac/concepts/state-and-backends/) for details.

## Authenticate with Pulumi Cloud

Your cluster needs a Pulumi Cloud identity. Give it one in one of two ways. **Choose one — you don't need both:**

- **OIDC token exchange** — no stored secret; PKO workspace pods exchange their projected service account tokens for short-lived Pulumi access tokens. Recommended.
- **A static access token** — a long-lived Pulumi access token stored in a Kubernetes Secret.

Whichever you choose, [Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) then delivers cloud credentials, secrets, and configuration to every `Stack` consistently, so you don't have to store separate cloud provider keys in the cluster for each stack.

### Eliminate static tokens with OIDC

The recommended way to give the cluster its Pulumi Cloud identity is OpenID Connect (OIDC). Register the Kubernetes cluster as a Pulumi Cloud [OIDC Issuer](/docs/administration/access-identity/oidc-issuers/), and PKO workspace pods exchange their projected service account tokens for short-lived Pulumi access tokens. No long-lived `PULUMI_ACCESS_TOKEN` secret is stored in the cluster.

See [Configuring OpenID Connect for Amazon EKS](/docs/administration/access-identity/oidc-issuers/kubernetes-eks/) or [Configuring OpenID Connect for Google Kubernetes Engine](/docs/administration/access-identity/oidc-issuers/kubernetes-gke/) for setup steps. Once the issuer is configured, the `Stack` manifests in this guide need no `envRefs.PULUMI_ACCESS_TOKEN` block.

### Use a static access token (alternative)

For clusters that are not registered as OIDC issuers, store a Pulumi [access token](/docs/administration/access-identity/access-tokens/) in a Kubernetes Secret and reference it from the `Stack`. Prefer an organization or team token over a personal token:

```bash
kubectl create secret generic pulumi-access-token \
  --from-literal=token=$PULUMI_ACCESS_TOKEN \
  -n pulumi
```

Reference the secret with `spec.envRefs`:

```yaml
spec:
  envRefs:
    PULUMI_ACCESS_TOKEN:
      type: Secret
      secret:
        name: pulumi-access-token
        key: token
```

{{% notes type="info" %}}
Static tokens are long-lived credentials stored in the cluster. Where possible, use the [OIDC approach](#eliminate-static-tokens-with-oidc) instead so workspace pods receive short-lived tokens.
{{% /notes %}}

### Attach an ESC environment

Once the cluster is authenticated, use the `spec.environment` field on a `Stack` to attach one or more ESC environment names. The configuration and secrets from those environments—including dynamically brokered, short-lived cloud credentials—become available to your Pulumi program automatically:

```yaml
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: webapp-staging
  namespace: pulumi
spec:
  serviceAccountName: webapp
  stack: myorg/webapp/staging
  projectRepo: https://github.com/myorg/pulumi-webapp.git
  branch: main
  environment:
    - aws-credentials
    - shared-config
```

## Define a Stack custom resource

A `Stack` custom resource tells PKO which Pulumi stack to deploy, where the program lives, and how to run it. The example below also declares a service account and the cluster role bindings the deployment needs to create resources in the cluster.

```yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: webapp
  namespace: pulumi
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: webapp:system:auth-delegator
  annotations:
    argocd.argoproj.io/sync-wave: "1"
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:auth-delegator
subjects:
- kind: ServiceAccount
  name: webapp
  namespace: pulumi
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: webapp:cluster-admin
  annotations:
    argocd.argoproj.io/sync-wave: "1"
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: webapp
  namespace: pulumi
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: webapp-dev
  namespace: pulumi
  annotations:
    argocd.argoproj.io/sync-wave: "2"
    pulumi.com/reconciliation-request: "before-first-update"
    link.argocd.argoproj.io/external-link: https://app.pulumi.com/myorg/webapp/dev
spec:
  serviceAccountName: webapp
  stack: myorg/webapp/dev
  projectRepo: https://github.com/myorg/pulumi-webapp.git
  branch: main
  refresh: true
  destroyOnFinalize: true
  environment:
    - aws-credentials
  config:
    webapp:replicas: "2"
```

The key `spec` fields are:

- `serviceAccountName`: the service account the workspace pod runs as.
- `stack`: the fully qualified Pulumi stack name, in `organization/project/stack` form.
- `projectRepo` and `branch`: the Git location of the Pulumi program PKO executes. Use `commit` instead of `branch` to pin an exact revision.
- `refresh`: refreshes Pulumi state before each update so it reflects the real state of your infrastructure.
- `destroyOnFinalize`: runs `pulumi destroy` when the `Stack` object is deleted, so removing the manifest from Git tears the infrastructure down.

The Pulumi program referenced by `projectRepo` can be written in any supported language—TypeScript, Python, Go, .NET, Java, or YAML. The `Stack` manifest itself is language-agnostic, so this guide uses a single set of YAML examples.

{{% notes type="warning" %}}
The `cluster-admin` binding above is shown for simplicity. For production, grant the service account only the permissions its Pulumi program actually needs.
{{% /notes %}}

## Create an Argo CD Application

An Argo CD `Application` tells Argo CD which Git directory to sync and where to apply the resulting manifests. Point its `source.path` at the directory containing your `Stack` manifest:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: webapp-dev
  namespace: argocd
  finalizers:
    - resources-finalizer.argocd.argoproj.io/background
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/webapp-manifests.git
    targetRevision: main
    path: manifests/dev
  destination:
    server: https://kubernetes.default.svc
    namespace: pulumi
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

The `syncPolicy.automated` block keeps the cluster in sync with Git without manual intervention: `prune` removes resources deleted from Git, and `selfHeal` reverts out-of-band changes. For background on when continuous reconciliation is the right fit (and when it isn't), see [GitOps and continuous reconciliation](/docs/iac/operations/stack-management/drift/#gitops-and-continuous-reconciliation). The `resources-finalizer.argocd.argoproj.io/background` finalizer pairs with `destroyOnFinalize` on the `Stack`—when the `Application` is deleted, Argo CD removes the `Stack` object in the background, which triggers PKO to destroy the infrastructure.

## Build a trunk-based GitOps workflow

In trunk-based development, contributors merge small changes into a single main branch frequently. Because Argo CD reconciles `Stack` manifests from Git rather than running pipeline steps, each environment is represented by its own `Stack` manifest in its own directory, watched by its own `Application`. Promoting a change means changing which Git ref a `Stack` tracks—not running a deploy command.

### Preview infrastructure changes in a pull request

When a pull request is opened against a Pulumi program, you want a dry run rather than a deployment. Add a `Stack` manifest with `spec.preview: true` and point `spec.branch` at the PR's feature branch:

```yaml
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: webapp-preview
  namespace: pulumi
spec:
  serviceAccountName: webapp
  stack: myorg/webapp/preview
  projectRepo: https://github.com/myorg/pulumi-webapp.git
  branch: feature/add-cache
  preview: true
  environment:
    - aws-credentials
```

PKO runs `pulumi preview` instead of `pulumi up`. The `Stack` status surfaces the preview link and program outputs without changing any infrastructure, and Argo CD shows the preview `Stack` as healthy once the dry run succeeds. Point the preview `Stack` at a dedicated Pulumi stack (`myorg/webapp/preview` above) to avoid state contention with your real environments. See [Preview mode](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/#preview-mode) in the PKO documentation for more detail.

### Deploy to dev or staging on merge to main

Your dev or staging `Stack` tracks the main branch:

```yaml
spec:
  stack: myorg/webapp/staging
  branch: main
```

When a pull request merges, PKO's branch polling detects the new commit on `main` and runs `pulumi up` against the staging environment. Tune the polling interval with `spec.resyncFrequencySeconds`, or trigger an immediate Argo CD sync.

### Promote to production with a release branch

Production should not track `main` directly. PKO's `spec.branch` field takes a branch reference, so the Argo CD equivalent of a moving release tag is a long-lived `release` branch that you fast-forward to a vetted commit to promote:

```yaml
spec:
  stack: myorg/webapp/production
  branch: release
```

To promote, advance the `release` branch to the commit you have validated in staging and push it. PKO reconciles production to that commit on its next sync.

If you need fully immutable, auditable releases, pin `spec.commit` to an exact SHA and update it for each promotion instead:

```yaml
spec:
  stack: myorg/webapp/production
  commit: a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0
```

A moving `release` branch makes promotion a single Git operation; a pinned `commit` records exactly which revision is live. Either way, promotion is an explicit, reviewable change in Git.

A typical repository layout for this workflow keeps one directory per environment:

```text
webapp-manifests/
├── manifests/
│   ├── preview/
│   │   └── stack.yaml        # tracks the PR branch, preview: true
│   ├── staging/
│   │   └── stack.yaml        # tracks main
│   └── production/
│       └── stack.yaml        # tracks the release branch
└── applications/
    ├── preview.yaml          # Argo CD Application for manifests/preview
    ├── staging.yaml          # Argo CD Application for manifests/staging
    └── production.yaml       # Argo CD Application for manifests/production
```

## Order deployments with sync waves

Argo CD sync waves control the order in which resources are applied. Annotate resources with `argocd.argoproj.io/sync-wave`; lower numbers are applied first. The [`Stack` custom resource above](#define-a-stack-custom-resource) uses waves to apply the RBAC resources (wave `1`) before the `Stack` itself (wave `2`):

```yaml
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "1"
```

For dependencies between Pulumi stacks—for example, creating a cluster before deploying applications into it—use the `Stack` resource's own `spec.prerequisites` field, which lets one `Stack` wait for another to succeed. See [Stack Prerequisites](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/#stack-prerequisites) in the PKO documentation.

## Monitor deployments

- **Link to Pulumi Cloud**: The `link.argocd.argoproj.io/external-link` annotation adds a link from the Argo CD UI directly to the stack in Pulumi Cloud, where you can see detailed deployment information:

  ```yaml
  metadata:
    annotations:
      link.argocd.argoproj.io/external-link: https://app.pulumi.com/myorg/webapp/dev
  ```

- **Health status**: PKO ships custom Argo CD health checks for the `Stack` resource, so Argo CD reports an accurate `Healthy`, `Progressing`, or `Degraded` status that reflects the underlying Pulumi deployment.
- **Force a sync**: The `pulumi.com/reconciliation-request` annotation triggers PKO to reconcile the `Stack`. Setting it to a new value—`"before-first-update"` for the initial deployment, or any unique string afterward—requests a fresh update.

## Troubleshooting

**Stack deployment fails**

- Check the `Stack` object's status in the Argo CD UI or with `kubectl describe stack <name> -n pulumi`.
- PKO runs each deployment in a workspace pod. List the pods with `kubectl get pods -n pulumi` and inspect the logs of the one for the failing stack with `kubectl logs <pod-name> -n pulumi`.
- Verify that the cluster can authenticate to Pulumi Cloud—confirm the OIDC issuer is configured, or that the access token secret exists and has the required permissions.

**Argo CD shows the Stack as `Unknown` or `Progressing`**

- PKO provides custom health checks for `Stack` resources. A `Progressing` status means the deployment is still in flight; if it persists, check the workspace pod logs.
- Check whether the `Stack` is waiting on a prerequisite to be satisfied.
- Verify that the referenced Git repository and path are accessible from the cluster.

**Stack stuck in an updating state**

- Check for resource conflicts or locks in your cloud provider.
- Review the workspace pod logs for the stack.
- Enable `refresh: true` so PKO reconciles Pulumi state with the real state of your infrastructure before each update.

## Additional resources

- [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) — the operator that reconciles Pulumi stacks from inside your cluster.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to stacks and developers consistently.
- [OIDC issuers](/docs/administration/access-identity/oidc-issuers/) — exchange a cluster's OIDC token for a short-lived Pulumi access token.
- [Kubernetes provider](/registry/packages/kubernetes/) — manage Kubernetes resources with Pulumi.
- [Continuous delivery](/docs/iac/operations/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [Argo CD documentation](https://argo-cd.readthedocs.io/) — official Argo CD project documentation.
