---
title: "Pulumi Kubernetes v4.34.0: CRDs as provider extensions"
date: 2026-08-28
draft: false
meta_desc: "Extend the Pulumi Kubernetes provider with any CustomResourceDefinition using the new --extension flag."
feature_image: feature.png
authors:
    - guinevere-saenger
tags:
    - kubernetes
    - releases
    - providers
category: product
schema_type: auto

social:
    twitter:
    linkedin:
    bluesky:
---

We're really excited to bring you v4.34.0, the newest version of the [Pulumi Kubernetes provider](/registry/packages/kubernetes/), which includes improved support for Kubernetes Custom Resource Definitions (CRDs).
As with any release, we've also shipped standard dependency updates and bug fixes.
This provider release includes the newest resources for Kubernetes v1.37.0, which was recently cut.
So that in itself is very exciting!

<!--more-->

But the feature we're proudest of is that you can now [extend the Kubernetes provider with any Kubernetes Custom Resource Definition of your choice](/registry/packages/kubernetes/how-to-guides/typed-customresources-with-provider-extensions/) by passing its manifest file to Pulumi, using the new `--extension` flag.
We believe first-class CRD support in Pulumi is becoming more important than ever.
For example, since the retirement of the ingress-nginx controller earlier this year, the recommended path for cluster ingress is Gateway API, which is maintained and shipped as CRDs.

## Generating a Pulumi SDK for CRDs

In your Pulumi project root, run:

```bash
pulumi package add kubernetes --extension "name=gateway-networking crd-manifest=gateway-api-crds.yaml"
```

You will see the custom SDK appear in a new `sdks/` folder, as well as a new parameterization reference in `Pulumi.yaml`.

## Single provider instance

Your new CRD schema exists as an extension to your existing provider and will be managed under the same provider instance, allowing you to use a single provider configuration and kubeconfig.

## SDKs as dependencies

Additionally, your code no longer needs to ship SDK files as part of the project.
The provider extension is referenced in your project file and its SDK, like all dependencies, can be regenerated via `pulumi install`.
You can choose to version the extension SDK, or continue to check the files into version control if you so desire.

## Full language support, including for YAML

Kubernetes CRDs can now be provisioned with Pulumi in all supported languages.

## Unified CLI experience

`pulumi package add --extension` extends your CRD schema into the Pulumi Kubernetes provider, using the same CLI as any other Pulumi operation.
It generates validated, schematized types that will be discoverable with autocomplete tools in your codebase.

## Migration from crd2pulumi

If you've been using `crd2pulumi` in the past, pivoting to using the new provider extension is possible by referencing the new SDK package name in your Pulumi program, without any changes to your stack state.
Migrating should result in a seamless no-op on `pulumi up`.
Read more in [Migrating from crd2pulumi](/registry/packages/kubernetes/how-to-guides/typed-customresources-with-provider-extensions/#migrating-from-crd2pulumi).

Available from Pulumi v3.255.0 and the Pulumi Kubernetes provider v4.34.0.
