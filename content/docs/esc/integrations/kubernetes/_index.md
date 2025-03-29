---
title: Kubernetes
title_tag: Kubernetes integrations | Pulumi ESC
h1: ESC Kubernetes integrations
meta_desc: Pulumi ESC integrates with Kubernetes to manage configurations, credentials,
  and kubeconfig files.
menu:
  esc:
    identifier: esc-kubernetes-integrations
    parent: esc-integrations
    weight: 5
aliases:
  - /docs/esc/kubernetes-integrations
search:
  keywords:
    - Kubernetes
    - integrations
    - External Secrets
    - kubeconfig files
---

Pulumi ESC's rich metadata and support for popular configuration formats enables easy integration with Kubernetes. This allows you to manage configurations, credentials, and `kubeconfig` files for Kubernetes clusters, and to interact with Kubernetes tools such as `kubectl` and `helm`. Additionally, Pulumi ESC integrates with different tools in the Kubernetes ecosystem, such as the Pulumi Kubernetes provider and the External Secrets Operator (ESO).

To learn how to configure Kubernetes with Pulumi ESC, see the following topics:

| Tool                                                                                              | Description                                                                                                                                               |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Kubernetes](/docs/esc/integrations/kubernetes/kubernetes)                                        | Pulumi ESC integrates with Kubernetes to manage configurations, credentials, and kubeconfig files, with kubectl and helm, and Pulumi Kubernetes provider. |
| [External Secrets Operator (ESO)](/docs/esc/integrations/kubernetes/external-secrets-operator)    | Pulumi ESC integrates with the External Secrets Operator (ESO) to manage and deliver secrets in Kubernetes clusters.                                      |                                                             |
| [Secrets Store CSI Driver](/docs/esc/integrations/kubernetes/secrets-store-csi-driver)            | Pulumi ESC integrates with the Secrets Store CSI driver to mount Pulumi ESC secrets directly into Kubernetes pods.                                        |                                                             |
