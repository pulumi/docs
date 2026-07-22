---
title_tag: "Rolling out changes | Pulumi Kubernetes Operator"
meta_desc: Roll changes out safely to stacks managed by the Pulumi Kubernetes Operator by staging promotions across environments with prerequisites.
title: Rolling out changes
h1: "Pulumi Kubernetes Operator: Rolling out changes"
menu:
    integrations:
        parent: kubernetes-clouds-operator
        identifier: kubernetes-clouds-operator-rolling-out-changes
        weight: 4
---

The `Stack` object supports safe rollouts with prerequisites and preview mode.

## Stage rollouts across environments

To roll a change through deployment stages, use `spec.prerequisites`. A `Stack` with a prerequisite waits for the referenced stack to reach a successful state before it runs. This enforces stage order declaratively, without manual sequencing.

In the example below, `dev` tracks the `main` branch and deploys every merge, while `test` and `prod` pin an immutable commit so they change only when that commit is promoted through a reviewed pull request.

```yaml
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: app-dev
spec:
  # ...stack configuration...
  branch: main            # dev tracks main and deploys every merge
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: app-test
spec:
  # ...stack configuration...
  commit: 03658b5514f08970f350618a6e6fdf1bd75f45d0   # the candidate commit
  prerequisites:
  - name: app-dev
    requirement:
      succeededWithinDuration: "1h"
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: app-prod
spec:
  # ...stack configuration...
  commit: 03658b5514f08970f350618a6e6fdf1bd75f45d0   # promoted only after test is green
  prerequisites:
  - name: app-test
    requirement:
      succeededWithinDuration: "1h"
```

The optional `requirement.succeededWithinDuration` sets a freshness window on the prerequisite: with `"1h"`, its last successful run must have completed within the last hour. If it is older, the operator re-syncs the prerequisite and waits for it to succeed again before the dependent stack proceeds.

Advancing the pinned commit on `app-test` and `app-prod` in a reviewed pull request then rolls the change out in order: `test` deploys first, and `prod` follows only once `test` is green.

To preview a change before promoting it, use [preview mode](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/stack-operations/#preview-mode); the [`preview-demo` example](https://github.com/pulumi/pulumi-kubernetes-operator/tree/master/examples/preview-demo) shows one setup.

## Verify application health

The operator gates on whether a deployment succeeded, not on whether the deployed application is healthy. To check that traffic and error rates look normal after a rollout, combine it with a progressive-delivery tool such as [Argo Rollouts](https://argoproj.github.io/rollouts/) or [Flagger](https://flagger.app/).

## Learn more

- [Defining stacks](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/defining-stacks/) — configure a `Stack`'s Git source, including `spec.commit` and `spec.branch`.
- [Stack operations](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/stack-operations/) — drift detection, state refresh, prerequisites, external triggers, and preview mode.
- [Argo CD with Pulumi Kubernetes Operator](/docs/iac/operations/continuous-delivery/argocd/) — a trunk-based GitOps workflow, preview environments, and sync waves.
