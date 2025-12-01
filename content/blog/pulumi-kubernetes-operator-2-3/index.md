---
title: "Pulumi Kubernetes Operator v2.3.0: Preview Mode and Structured Configuration"
allow_long_title: true
date: 2025-11-25
draft: false
meta_desc: "Pulumi Kubernetes Operator v2.3.0 adds preview mode for safe infrastructure changes and structured config support for GitOps workflows."
meta_image: meta.png
authors:
    - eron-wright
tags:
    - kubernetes
    - pulumi-kubernetes-operator
    - continuous-delivery
    - gitops
    - operators
    - infrastructure-as-code
---

We're excited to announce the release of Pulumi Kubernetes Operator v2.3.0, introducing two powerful capabilities that enhance GitOps workflows: preview mode for validating infrastructure changes before deployment, and structured configuration support for managing complex data types. Building on the success of the v2.0 GA release, this update addresses long-standing community requests while maintaining full backwards compatibility. These features enable safer, more sophisticated infrastructure management patterns for platform engineering teams.

<!--more-->

## Preview mode: Validate infrastructure changes before deployment

Preview mode enables you to run Pulumi stacks in dry-run fashion, allowing you to visualize what infrastructure changes would occur without actually applying them. This capability is essential for GitOps workflows that require validation gates and incremental rollouts.

By adding `preview: true` to your Stack specification, the operator runs `pulumi preview` instead of `pulumi up`. The Stack's Ready condition indicates preview success, and you get full status including preview links, standard output, and program outputs—all without making actual infrastructure changes.

This unlocks sophisticated workflow patterns:

- **Multiple Stacks for what-if analysis**: Create several Stack resources pointing to the same Pulumi stack, with all-but-one operating in preview mode to compare different configurations
- **Branch validation**: Preview changes from feature branches before merging to production
- **Tick-tock rollout patterns**: Toggle the `preview` flag on and off with external verification steps between each deployment phase

Here's a simple example showing a production stack alongside its preview counterpart:

```yaml
# Production stack
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: my-infrastructure
spec:
  stack: org/project/prod
  projectRepo: https://github.com/example/infra
  branch: main
---
# Preview stack - same Pulumi stack, preview mode
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: my-infrastructure-preview
spec:
  stack: org/project/prod
  projectRepo: https://github.com/example/infra
  branch: feature-branch
  preview: true  # Only runs pulumi preview
```

Preview mode closes [issue #16](https://github.com/pulumi/pulumi-kubernetes-operator/issues/16), one of our longest-standing feature requests.

## Structured configuration: Native support for complex data types

Configuration management takes a significant step forward with native support for complex data types. Previously limited to string values, Stack configuration now supports objects, arrays, numbers, and booleans as first-class citizens.

This enhancement addresses the reality that complex environments require rich configuration. You can now express sophisticated configuration structures inline in your Stack manifests or load them from ConfigMaps with automatic JSON parsing—all using Kubernetes-native patterns.

The implementation leverages Pulumi CLI's JSON configuration support (available in v3.202.0+) with automatic version detection. If your workspace uses an earlier CLI version, you'll receive clear guidance to upgrade. Existing string-only configurations continue to work without modification, ensuring full backwards compatibility.

Here's an example of inline structured configuration:

```yaml
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: my-app
spec:
  stack: org/app/prod
  projectRepo: https://github.com/example/app
  branch: main
  config:
    # String values (existing behavior)
    environment: "production"

    # Objects (NEW)
    database:
      host: "db.example.com"
      port: 5432
      ssl: true

    # Arrays (NEW)
    regions: ["us-west-2", "us-east-1", "eu-west-1"]

    # Numbers and booleans (NEW)
    maxConnections: 100
    enableCaching: true
```

You can also reference ConfigMaps for more complex scenarios:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-settings
data:
  database.json: |
    {
      "host": "db.example.com",
      "port": 5432,
      "maxConnections": 100
    }
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: my-app
spec:
  stack: org/app/prod
  projectRepo: https://github.com/example/app
  branch: main
  configRefs:
    database:
      name: app-settings
      key: database.json
      json: true  # Parse as JSON
```

Note that Secrets are not a supported source of structured configuration values.

Structured configuration closes [issue #258](https://github.com/pulumi/pulumi-kubernetes-operator/issues/258) and [issue #872](https://github.com/pulumi/pulumi-kubernetes-operator/issues/872), addressing long-standing configuration management needs from the community.

## Bug fixes and reliability improvements

This release includes several fixes that improve operational reliability:

- **Stack name validation**: Added validation to limit Stack names to 42 characters, preventing resource naming conflicts ([#899](https://github.com/pulumi/pulumi-kubernetes-operator/issues/899))
- **secretsProvider fix**: The `secretsProvider` parameter now properly applies when creating new stacks ([#935](https://github.com/pulumi/pulumi-kubernetes-operator/issues/935))
- **Helm chart fix**: Resolved YAML parsing errors for `podLabels` containing special characters like colons ([#1014](https://github.com/pulumi/pulumi-kubernetes-operator/issues/1014))
- **Stack deletion**: Stack deletion is no longer blocked when prerequisite stacks are missing, enabling proper cleanup workflows ([#751](https://github.com/pulumi/pulumi-kubernetes-operator/issues/751))
- **Update TTL**: Completed Update objects now respect the `ttlAfterCompleted` setting for automatic garbage collection ([#960](https://github.com/pulumi/pulumi-kubernetes-operator/issues/960))

## Upgrading to v2.3.0

This release includes updates to the Custom Resource Definitions (CRDs) to support the new features. If you're using Helm, you'll need to manually apply the updated CRDs before upgrading, as Helm v3 does not automatically upgrade CRDs:

```bash
# Apply updated CRDs
kubectl apply --server-side -k 'github.com/pulumi/pulumi-kubernetes-operator//operator/config/crd?ref=v2.3.0'

# Upgrade via Helm
helm upgrade pulumi-kubernetes-operator \
  oci://ghcr.io/pulumi/helm-charts/pulumi-kubernetes-operator \
  --version 2.3.0 \
  -n pulumi-kubernetes-operator
```

If you're using the quickstart YAML installation method, the CRDs will update automatically when you apply the new manifest.

All changes are backwards compatible—existing Stack resources work without modification. For structured configuration support, ensure your workspace pods use Pulumi CLI v3.202.0 or later; the operator provides automatic version detection with clear upgrade guidance when needed.

## Get started today

The v2.3.0 release enhances the Pulumi Kubernetes Operator with safer deployment workflows and more flexible configuration management. Preview mode enables validation-first GitOps patterns, while structured configuration simplifies complex multi-environment setups.

Get started with the Pulumi Kubernetes Operator in our [documentation](https://www.pulumi.com/docs/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/), or view the complete [v2.3.0 release notes](https://github.com/pulumi/pulumi-kubernetes-operator/releases/tag/v2.3.0) on GitHub. Join the conversation in the [Pulumi Community Slack](https://slack.pulumi.com/) #kubernetes channel—we'd love to hear how these features impact your workflows.
