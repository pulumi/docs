---
title_tag: "Stack operations | Pulumi Kubernetes Operator"
meta_desc: Configure drift detection, state refresh, cleanup, prerequisites, external triggers, and preview mode for Pulumi stacks managed by the Kubernetes Operator.
title: Stack operations
h1: "Pulumi Kubernetes Operator: Stack operations"
menu:
    integrations:
        parent: kubernetes-clouds-operator
        identifier: kubernetes-clouds-operator-stack-operations
        weight: 3
---

The `Stack` resource provides several options for controlling how the operator runs Pulumi deployment operations. Detailed documentation on the Stack API is available in the [operator repository][pko-stacks].

[pko-stacks]: https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/stacks.md

## Drift detection

Drift detection means to detect unwanted changes to your provisioned infrastructure.
The operator supports drift detection and remediation by periodically running `pulumi up`. This is referred to as re-synchronization.

Use the `spec.continueResyncOnCommitMatch` field to enable periodic resyncs. Use the `spec.resyncFrequencySeconds` field to set the resync frequency.

## State refresh

Use the `spec.refresh` field to refresh the state of the stack's resources before each update.

{{< notes type="info" >}}
  It is recommended that `spec.refresh` be enabled.
{{< /notes >}}

## Stack cleanup

Use the `spec.destroyOnFinalize` field to automatically destroy the Pulumi stack (i.e. `pulumi destroy -f`)
when the `Stack` object is deleted. Enable this option to link the lifecycle of the Pulumi stack, and the resources it contains, to its `Stack` object.

{{< notes type="info" >}}
  Stack object deletion is slower when this option is enabled, because a Pulumi deployment operation
  must be run during object finalization.
{{< /notes >}}

## Stack prerequisites

It is possible to declare that a particular `Stack` be dependent on another `Stack`.
The dependent stack waits for the other stack to be successfully deployed.
Use the `succeededWithinDuration` field to set a duration within which the prerequisite must have reached success; otherwise the dependency is automatically re-synced.

## External triggers

It is possible to trigger a stack update for a stack at any time by applying
the `pulumi.com/reconciliation-request` annotation:

```bash
kubectl annotate stack $STACK_NAME "pulumi.com/reconciliation-request=$(date)" --overwrite
```

The value of the annotation is arbitrary, and we recommend using a timestamp.

## Preview mode

Preview mode enables you to run Pulumi stacks in dry-run fashion, allowing you to visualize what infrastructure changes would occur without actually applying them. When `spec.preview` is set to `true`, the operator runs `pulumi preview` instead of `pulumi up`.

This is useful for:

- Validating infrastructure changes before deployment
- Comparing different configurations using multiple Stack resources pointing to the same Pulumi stack
- Creating tick-tock rollout patterns where you toggle preview mode on and off

Here's an example Stack with preview mode enabled:

```yaml
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: my-infrastructure-preview
spec:
  serviceAccountName: pulumi
  stack: my-org/my-project/prod
  projectRepo: https://github.com/example/infra
  branch: feature-branch
  preview: true  # Only runs pulumi preview
  envRefs:
    PULUMI_ACCESS_TOKEN:
      type: Secret
      secret:
        name: pulumi-api-secret
        key: accessToken
```

The Stack's Ready condition indicates preview success, and status includes preview links, standard output, and program outputs—all without making actual infrastructure changes.
