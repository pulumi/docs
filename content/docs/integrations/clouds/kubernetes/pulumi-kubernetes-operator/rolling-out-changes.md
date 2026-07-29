---
title_tag: "Rolling out changes | Pulumi Kubernetes Operator"
meta_desc: Roll out changes safely with the Pulumi Kubernetes Operator by approving them upstream and previewing before a change reaches the operator.
title: Rolling out changes
h1: "Pulumi Kubernetes Operator: Rolling out changes"
menu:
    integrations:
        parent: kubernetes-clouds-operator
        identifier: kubernetes-clouds-operator-rolling-out-changes
        weight: 4
---

The Pulumi Kubernetes Operator keeps your infrastructure continuously reconciled with a specific version of a Pulumi program, declared in a `Stack` resource. By default it applies changes immediately: when the version a `Stack` tracks changes, the operator runs `pulumi up` and reconciles your infrastructure to it, with no built-in pause for review. The safety of a rollout therefore depends on approving a change *before* its version reaches the operator, and previewing it upstream where you need one.

(The operator reconciles when the tracked version changes. It can also re-run periodically to detect and remediate drift, but that is opt-in — you enable it with [drift detection](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/stack-operations/#drift-detection).)

## How your program reaches the operator

A `Stack` gets its Pulumi program in one of two ways, and each determines where "upstream" is — the source of truth you review before the operator sees a change:

- **From a Git repository.** `spec.projectRepo` with `spec.branch` or `spec.commit` (and an optional `spec.repoDir`). The operator clones the repository at that ref and runs it. Upstream is the repository: you review and gate changes in its pull requests and CI.
- **From an inline `Program`.** `spec.programRef` points at a [`Program` object](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/defining-stacks/#using-a-program-object) — a Pulumi YAML program stored in the cluster. Upstream is wherever you author and apply that `Program`: a manifests repository, whose programs are often composed from vetted [components](/docs/iac/concepts/components/).

## Approve changes before they reach the operator

Because the operator applies whatever version you point it at, immediately, your upstream workflow is the approval gate. The GitOps function that reconciliation depends on — the program itself — must be known to work before the operator sees it:

- Review and merge changes through pull requests, with [CI that previews the change](#preview-a-change-before-it-reaches-the-operator).
- Pin production `Stack`s to an immutable commit (`spec.commit`) rather than a moving branch, and promote by advancing that commit in a reviewed pull request. Advancing the pin *is* the approval; the operator reconciles the new commit once it merges.

```yaml
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: app-dev
spec:
  stack: my-org/my-app/dev
  projectRepo: https://github.com/example/app
  branch: main            # main is already reviewed; dev deploys every merge
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: app-prod
spec:
  stack: my-org/my-app/prod
  projectRepo: https://github.com/example/app
  commit: 03658b5514f08970f350618a6e6fdf1bd75f45d0   # advanced only in a reviewed pull request
```

Don't let an unreviewed version reach the operator and rely on staging afterward to catch problems. Because reconciliation applies immediately, a broken version is live before any gate downstream of it can help. Keep approval upstream, where a change can still be stopped.

## Preview a change before it reaches the operator

The Pulumi Kubernetes Operator does not hold a change for approval; it applies on reconcile. A preview (or a required approval) before a change goes live therefore has to run **upstream of the operator, in your CI**.

A `Stack` can be put in [preview mode](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/stack-operations/#preview-mode) with `spec.preview: true`, and it then only ever previews — it never applies. That is a mode on the `Stack` rather than a per-change gate, though: setting it back to `false` deploys whatever version the `Stack` currently points at.

When your program is in a Git repository, preview it in that repository's CI on every pull request. This is an ordinary `pulumi preview` and doesn't involve the operator. With GitHub Actions, previewing against your dev stack:

```yaml
# .github/workflows/preview.yml — in the program's repository
name: preview
on:
  pull_request:
jobs:
  preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pulumi/actions@v6
        with:
          command: preview
          stack-name: my-org/my-app/dev
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

This runs a real diff against the dev stack's live state. To preview against more than one environment, run the step once per stack — for example, a matrix over `dev`, `test`, and `prod` — since each previews against its own state and the diffs can differ.

For the CI preview to reflect what the operator does, config and secrets must resolve the same way in both places. If they live only in `spec.config`, `spec.secretsRef`, or `spec.envRefs` on the `Stack`, CI won't see them and the two previews diverge. Keep shared configuration in the stack's `Pulumi.<stack>.yaml` or in an [ESC](/docs/esc/) environment referenced from both the stack settings and the `Stack`'s `spec.environment`, so CI and the operator resolve identical inputs.

How you promote the previewed change — and whether a preview beforehand is even possible — depends on how the `Stack` references its source.

### A pinned commit

When the `Stack` pins `spec.commit`, previewing before promotion works cleanly. The commit is immutable, so CI previews the *exact* version you later promote:

1. Open a pull request against the program repository; CI previews it.
1. Merge once the preview is green.
1. Advance `spec.commit` on the `Stack` to the merged SHA in a reviewed pull request against your manifests.

The operator reconciles the new commit only after the manifest change merges, and that commit was already previewed. This is the recommended pattern for production.

### A moving branch or tag

When the `Stack` tracks a moving ref — a branch, or a tag you re-point such as `live` or `prod` — the manifest doesn't change on promotion. The operator applies whatever the ref resolves to as soon as it detects the move, so **the CI preview must gate the move of the ref itself**, not an edit to a manifest.

Preview the commit you're about to promote, and re-point the branch or tag only on a green preview — as a required status check, not a manual step. No second checkpoint exists after the ref moves: once you move it, the operator picks it up and applies immediately. If you re-point the tag by hand without a gating preview, the operator applies the change unpreviewed.

### An inline Program

When you define the program inline with a `Program` object (`spec.programRef`), there is no program repository to check out, and config comes from the `Stack` — so a standalone `pulumi preview` in CI has nothing to run against and no faithful way to reproduce the operator's inputs. **You can't run a faithful CI preview before promotion here.** Safety rests on reviewing the `Program` — and the components it composes — before you apply it. You can still get a dry-run plan in the cluster by setting [preview mode](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/stack-operations/#preview-mode) (`spec.preview: true`) on the `Stack`, which runs `pulumi preview` instead of applying; set it back to `false` to deploy.

One place inline `Program`s might fit is an internal developer platform, where users compose a program from a fixed set of well-vetted golden paths encoded as [components](/docs/iac/concepts/components/). There, the approval that matters has already happened upstream — in the review and testing of the components themselves — so a per-change preview is less critical: users assemble trusted building blocks rather than author arbitrary infrastructure.

## Verify application health

The operator gates on whether a deployment succeeded, not on whether the deployed application is healthy. To check that traffic and error rates look normal after a rollout, combine it with a progressive-delivery tool such as [Argo Rollouts](https://argoproj.github.io/rollouts/) or [Flagger](https://flagger.app/).

## Learn more

- [Defining stacks](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/defining-stacks/) — configure a `Stack`'s Git source or inline `Program`, including `spec.commit`, `spec.branch`, and `spec.programRef`.
- [Stack operations](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/stack-operations/) — drift detection, state refresh, prerequisites, external triggers, and preview mode.
- [Argo CD with Pulumi Kubernetes Operator](/docs/iac/operations/continuous-delivery/argocd/) — a trunk-based GitOps workflow, preview environments, and sync waves.
