---
title: Kubernetes
title_tag: Pulumi ESC Kubernetes integrations
h1: Kubernetes
meta_desc: Project Pulumi ESC values into Kubernetes via External Secrets Operator or mount them into pods with the Secrets Store CSI Driver.
menu:
  esc:
    identifier: esc-kubernetes-integrations
    parent: esc-integrations
    weight: 50
aliases:
  - /docs/esc/kubernetes-integrations
---

Two operators consume ESC values inside a Kubernetes cluster. Pick based on whether you want ESC values exposed as `Secret` objects or mounted directly into pods at runtime.

| Pattern | What it does |
|---|---|
| [External Secrets Operator (ESO)](/docs/esc/integrations/kubernetes/external-secrets-operator/) | Sync ESC values into Kubernetes `Secret` objects via ESO. |
| [Secrets Store CSI Driver](/docs/esc/integrations/kubernetes/secret-store-csi-driver/) | Mount ESC values directly into pods as files via the upstream CSI driver. |

For using ESC to store and serve `kubeconfig` files for `kubectl`, `helm`, or the Pulumi Kubernetes provider, see the [Kubernetes cluster access](/docs/esc/guides/integrate-with/kubernetes-cluster-access/) guide.
