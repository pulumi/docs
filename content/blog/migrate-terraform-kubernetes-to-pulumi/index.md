---
title: "Migrate a Terraform Kubernetes Setup to Pulumi"
date: 2026-09-09
draft: false
meta_desc: "How to move a Terraform-managed Kubernetes stack to Pulumi: converting HCL, handling kubernetes_manifest by hand, and importing live objects into a stack."
authors:
    - pulumi-content-team
tags:
    - kubernetes
    - terraform
    - infrastructure-as-code
    - migration
category: general
schema_type: auto
related_posts:
    - terraform-kubernetes
    - yaml-terraform-pulumi-whats-the-smart-choice-for-deployment-automation-with-kubernetes

social:
    twitter: |
        Already decided to move a Terraform-managed Kubernetes stack to Pulumi? Here's the path: convert the HCL, hand-write the kubernetes_manifest and CRD resources the converter can't reach, then import what's already running.
    linkedin: |
        Teams that adopt Pulumi for Kubernetes usually arrive with an existing Terraform stack, not a green field. This guide covers the actual migration mechanics: running `pulumi convert` against the HCL, rewriting `kubernetes_manifest` blocks and CRDs by hand (the converter's biggest gap), importing objects Terraform already created with `pulumi import`, and running both tools against one cluster during the cutover without fighting over the same resources.
    bluesky: |
        A step-by-step guide to migrating a Terraform Kubernetes setup to Pulumi: convert the HCL, hand-write what doesn't convert, import the live objects, and cut over safely.
---

This guide walks through migrating a Kubernetes stack from Terraform's `hashicorp/kubernetes` provider to Pulumi: converting the HCL, rewriting the pieces the converter can't reach, importing objects Terraform already created, and running both tools against one cluster during the cutover.

It assumes you've already decided to migrate. If you're still weighing whether Terraform can manage Kubernetes well in the first place, [our practical guide to Terraform and Kubernetes](/blog/terraform-kubernetes/) covers that question directly.

<!--more-->

## What you need before you start

Have these ready before touching any resources:

- The [Pulumi CLI](/docs/iac/cli/) installed, plus an account for [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/) or another supported state backend.
- Access to the same cluster your Terraform stack manages: a working `kubeconfig` and the credentials `kubectl` already uses.
- Your Terraform state and `.tf` source available locally, since `pulumi convert` reads the HCL directly and doesn't need the state file for the conversion step itself.
- A scratch Pulumi stack pointed at a non-production namespace or a disposable cluster, so you can run the first `pulumi up` somewhere a mistake costs nothing.
- A decision on target language. Where an example is language-specific, it's shown in TypeScript, Python, and Go; pick the one your team already writes application code in, since that's the whole point of moving off a Terraform-specific DSL. For a fuller look at how the two platforms differ beyond Kubernetes specifically, see our [Terraform comparison](/docs/iac/comparisons/terraform/).

## Convert the Terraform config with `pulumi convert`

Pulumi's converter reads Terraform HCL and emits a working Pulumi program in the language of your choice. Point it at the directory holding your `.tf` files:

```bash
pulumi convert --from terraform --language typescript --out ./pulumi-converted
```

Swap `--language` for `python`, `go`, `csharp`, `java`, or `yaml`. A few flags matter for a Kubernetes migration specifically:

- `--generate-only` writes the converted program without installing dependencies or provisioning anything, which is what you want while you're still reviewing the output.
- `--strict` fails the conversion on errors such as missing variables, instead of emitting code with placeholders you might miss.
- `--out` controls where the new project lands; it defaults to the current directory, so pointing it somewhere clean keeps the converted project separate from your original Terraform files while you compare them.

The command defaults to reading `.tf` files from the current working directory, so run it from the root of your Terraform module (or pass the source directory as a positional argument).

Full flag reference: [`pulumi convert`](/docs/iac/cli/commands/pulumi_convert/). Background on the converter architecture: [Convert code](/docs/iac/guides/migration/converters/) and [Convert HCL code](/docs/iac/get-started/terraform/convert-hcl/).

## What converts cleanly, and what needs hand work

The converter handles typed Kubernetes resources well, because they map cleanly onto the provider's typed classes. It does not handle everything, and knowing the gap in advance saves a debugging session later.

| Terraform resource | Converts cleanly to | Notes |
| --- | --- | --- |
| `kubernetes_namespace` | `kubernetes.core.v1.Namespace` | Direct field mapping |
| `kubernetes_deployment` / `kubernetes_deployment_v1` | `kubernetes.apps.v1.Deployment` | Direct field mapping |
| `kubernetes_service` | `kubernetes.core.v1.Service` | Direct field mapping |
| `kubernetes_config_map` | `kubernetes.core.v1.ConfigMap` | Direct field mapping |
| `kubernetes_secret` | `kubernetes.core.v1.Secret` | Direct field mapping; re-check how secret values are sourced during review |
| `kubernetes_ingress_v1` | `kubernetes.networking.v1.Ingress` | Direct field mapping |
| `kubernetes_manifest` | No 1:1 converter output | Rewrite by hand; see [below](#rewriting-kubernetes_manifest-and-crds-by-hand) |
| `helm_release` | Partial | Review generated Helm resource options against the Terraform release config |
| CRDs and CRD instances | No 1:1 converter output | Rewrite by hand; see [below](#rewriting-kubernetes_manifest-and-crds-by-hand) |

Treat `kubernetes_manifest` as the resource type most worth reviewing line by line. Terraform's `kubernetes_manifest` accepts arbitrary Kubernetes API objects as a generic escape hatch, which is exactly why there's no single typed Pulumi resource it maps to; this follows from the resource's schemaless shape rather than from a documented converter behavior, so treat the table row above as the expected outcome to verify against your own `pulumi convert` output rather than a guaranteed one.

## Rewriting `kubernetes_manifest` and CRDs by hand

For a single custom resource, the Pulumi equivalent is `apiextensions.CustomResource`, which takes the same `apiVersion`, `kind`, and spec fields your Terraform block already has:

{{< chooser language "typescript,python,go" >}}
{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

const cert = new k8s.apiextensions.CustomResource("app-cert", {
    apiVersion: "cert-manager.io/v1",
    kind: "Certificate",
    metadata: {
        name: "app-cert",
        namespace: "default",
    },
    spec: {
        secretName: "app-tls",
        dnsNames: ["app.example.com"],
        issuerRef: {
            name: "letsencrypt-prod",
            kind: "ClusterIssuer",
        },
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_kubernetes as k8s

cert = k8s.apiextensions.CustomResource(
    "app-cert",
    api_version="cert-manager.io/v1",
    kind="Certificate",
    metadata={
        "name": "app-cert",
        "namespace": "default",
    },
    spec={
        "secretName": "app-tls",
        "dnsNames": ["app.example.com"],
        "issuerRef": {
            "name": "letsencrypt-prod",
            "kind": "ClusterIssuer",
        },
    },
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := apiextensions.NewCustomResource(ctx, "app-cert", &apiextensions.CustomResourceArgs{
			ApiVersion: pulumi.String("cert-manager.io/v1"),
			Kind:       pulumi.String("Certificate"),
			Metadata: metav1.ObjectMetaArgs{
				Name:      pulumi.String("app-cert"),
				Namespace: pulumi.String("default"),
			},
			OtherFields: kubernetes.UntypedArgs{
				"spec": map[string]any{
					"secretName": "app-tls",
					"dnsNames":   []string{"app.example.com"},
					"issuerRef": map[string]any{
						"name": "letsencrypt-prod",
						"kind": "ClusterIssuer",
					},
				},
			},
		})
		return err
	})
}
```

{{% /choosable %}}
{{< /chooser >}}

If your Terraform config applies a whole directory of raw manifests, whether hand-written YAML or a rendered Helm template, `kubernetes.yaml.ConfigFile` and `kubernetes.yaml.ConfigGroup` (`yaml.v2.ConfigGroup` in current SDK versions) apply an entire file or directory of YAML as a single Pulumi resource, which is usually less rewriting than converting each object individually.

CRD definitions themselves (the `CustomResourceDefinition` objects, as opposed to instances of the custom resource) follow the same pattern: apply them with `yaml.ConfigFile` if they ship as static YAML, or with `apiextensions.CustomResource` if you're generating them programmatically.

## Adopt the objects already running in the cluster with `pulumi import`

Converting the code gives you a Pulumi program, but the resources it describes already exist in the cluster, created by Terraform. Running `pulumi up` against that program without importing first would try to create duplicates. `pulumi import` brings existing resources under Pulumi's management instead, generating the resource declaration for you:

```bash
pulumi import kubernetes:core/v1:ConfigMap app-config default/app-config
```

For a Kubernetes provider, the id you pass is the object's identity in the cluster: namespaced objects use `<namespace>/<name>`, and cluster-scoped objects (a `ClusterRole`, for example) use just `<name>`. This isn't spelled out on a single reference page the way an AWS resource's ARN format is; it's the convention the Kubernetes provider expects, and the worked example above reflects how teams doing this migration have applied it in practice. Treat it as a starting point rather than a guarantee: if `pulumi import` rejects an id, run it again with `--out preview.ts` (or your target language) against a single resource first, using the id shape shown above, before batching the rest through `--file`.

Importing one resource at a time works for a small stack. For anything larger, `pulumi import --file` takes a JSON file listing every resource at once:

```json
{
    "resources": [
        { "type": "kubernetes:core/v1:ConfigMap", "name": "app-config", "id": "default/app-config" },
        { "type": "kubernetes:apps/v1:Deployment", "name": "app", "id": "default/app" },
        { "type": "kubernetes:core/v1:Service", "name": "app-svc", "id": "default/app-svc" }
    ]
}
```

```bash
pulumi import --file import.json
```

Import protects every resource from deletion by default; pass `--protect=false` if you don't want that. Use `--parent` and `--provider` when a resource needs to be attached under a specific parent or provider in the resulting program. Full reference: [`pulumi import`](/docs/iac/cli/commands/pulumi_import/) and [Import resources](/docs/iac/guides/migration/import/).

A CRD-installing Helm chart plus resources that depend on those CRDs is a common ordering trap during import: the custom resource's type has to exist in the cluster (and in your Pulumi program's dependency graph) before Pulumi tries to import or create instances of it. Import the CRDs first, using a bare `<name>` id since a `CustomResourceDefinition` is cluster-scoped rather than namespaced, or split them into their own stack and read its outputs from the resource stack with a [stack reference](/docs/iac/concepts/stacks/).

## Run Terraform and Pulumi against one cluster during the cutover

Most teams don't cut over a whole cluster in one step. A namespace-by-namespace or resource-type-by-resource-type cutover, where Terraform keeps managing some objects while Pulumi takes ownership of others, is more common and lower-risk. Two things make that safe:

**Draw the ownership line before you start.** Decide which namespaces or resource types move to Pulumi first, and don't let both tools manage the same object at the same time; that produces drift and confusing plan/preview output on both sides.

**Read values out of the Terraform state you haven't migrated yet.** If your new Pulumi program needs an output from a Terraform-managed resource, such as a cluster endpoint or a generated secret name, the `@pulumi/terraform` package's `state.getLocalReferenceOutput` reads a local state file directly, and `RemoteStateReference` reads a remote backend (S3, Terraform Cloud, and others). That lets you migrate consumers before you migrate the resources they depend on. Details: [Reference Terraform state](/docs/iac/get-started/terraform/reference-state/).

**Detach, don't destroy, on either side of the handoff.** When you finish migrating a resource and remove its Terraform block, a plain `terraform destroy` (or a `terraform apply` that drops the resource from config) would delete the live object unless you've already told Terraform to forget it (`terraform state rm`, or the equivalent lifecycle handling). On the Pulumi side, if you ever need to remove a resource from a Pulumi stack without touching the underlying object, `retainOnDelete: true` removes it from state without calling the provider's delete: `pulumi.CustomResourceOptions({ retainOnDelete: true })` in TypeScript, `ResourceOptions(retain_on_delete=True)` in Python, `pulumi.RetainOnDelete(true)` in Go. `protect` is a different guarantee: it blocks deletion outright rather than letting you detach state, so use it once a resource is fully owned by Pulumi and you want to prevent an accidental `pulumi destroy` from touching it.

## Verify before you cut over

Before pointing anything at production, confirm the converted and imported program actually matches the state Terraform left behind:

```bash
pulumi preview --diff
```

`--diff` shows the full property-level diff for every resource Pulumi would change, not just a summary, which is what you want when comparing against a Terraform-managed baseline. Once the program is stable and you don't expect further changes:

```bash
pulumi preview --expect-no-changes
pulumi refresh --expect-no-changes
```

Both flags return a non-zero exit code if Pulumi detects any drift, which makes them useful as a gate in CI: run them after every import batch to confirm nothing changed underneath you, and again right before you decommission the Terraform side.

## Where to go next

Once your Kubernetes stack runs on Pulumi, the same conversion and import process applies to whatever else that Terraform configuration touches: the cloud provider resources it provisions alongside the cluster, the networking, the IAM. Start with the [Terraform migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) for the non-Kubernetes parts of your stack, and the [Kubernetes migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes/) if any part of your setup comes from raw YAML or Helm rather than Terraform. To get hands-on with the target side of this migration before you start, [get started with Pulumi and Kubernetes](/docs/iac/get-started/kubernetes/) walks through provisioning a cluster app stack from scratch.
