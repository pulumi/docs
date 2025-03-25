---
title: Secrets Store CSI Driver
title_tag: Integrate with Kubernetes Secrets Store CSI Driver | Pulumi ESC
h1: "Pulumi ESC Integration with the Kubernetes Secrets Store CSI Driver"
meta_desc: Learn how to integrate Pulumi ESC with Kubernetes Secrets Store CSI Driver
  to securely mount ESC secrets directly into Kubernetes pods and follow K8 security
  best practices.
allow_long_title: true
weight: 2
menu:
  esc:
    identifier: esc-secrets-store-csi-driver
    parent: esc-kubernetes-integrations
aliases:
  - /docs/esc/integrations/kubernetes/secrets-store-csi-driver/
search:
  keywords:
    - csi
    - driver
    - store
    - secrets
    - k8
    - esc
    - kubernetes
---

## Overview

[Secrets Store CSI Driver](https://secrets-store-csi-driver.sigs.k8s.io/introduction) is a Kubernetes project that allows you to mount secrets stored in external secret management systems into your Kubernetes pods. By using the Secrets Store CSI Driver, you can:

- Store and manage sensitive data in an external service outside the Kubernetes cluster, which leads to better security and compliance.
- Use the same driver to manage secrets and configuration from different sources.
- Take advantage of advanced features of the secret provider, such as encryption of data at rest and scenarios like secret rotation.
- Mount Pulumi ESC secrets directly into your Kubernetes pods without using Kubernetes-native secrets.

## Authentication

Pulumi [Access Tokens](/docs/pulumi-cloud/access-management/access-tokens/) are recommended to access Pulumi ESC.

## Installation

Install the Secrets Store CSI Driver using Helm:

```bash
helm repo add secrets-store-csi-driver https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts
helm install csi-secrets-store secrets-store-csi-driver/secrets-store-csi-driver --namespace kube-system
```

Running the above helm install command will install the Secrets Store CSI Driver on Linux nodes in the kube-system namespace.

Install the [Pulumi ESC Secret Store CSI Driver](https://github.com/pulumi/pulumi-esc-csi-provider.git) using Helm:

```bash
helm install pulumi-esc-csi-provider oci://ghcr.io/pulumi/helm-charts/pulumi-esc-csi-provider --version 0.1.5 --namespace kube-system
```

After a few seconds, the `pulumi-esc-csi-provider` should be running.

## Creating a SecretProviderClass

Configuration is passed to the Pulumi ESC via a [`SecretProviderClass`](https://secrets-store-csi-driver.sigs.k8s.io/concepts#secretproviderclass) through the `spec.parameters` field.

```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: example-provider-pulumi-esc
  namespace: default
spec:
  provider: pulumi
  parameters:
    apiUrl: https://api.pulumi.com/api/esc
    organization: <NAME_OF_THE_ORGANIZATION>
    project: <NAME_OF_THE_PROJECT>
    environment: <NAME_OF_THE_ENVIRONMENT>
    authSecretName: <NAME_OF_KUBE_SECRET_WITH_ACCESS_TOKEN>
    authSecretNamespace: <NAMESPACE_OF_KUBE_SECRET>
    secrets: |
      - secretPath: "<SECRET_PATH>"
        fileName: "<FILE_NAME>"
        secretKey: <PULUMI_PATH_SYNTAX>
```

See the [SecretProviderClass configuration](#secretproviderclass) table for additional customization options.

**Note:** `secretKey` does not follow the JSON Path syntax, but rather the Pulumi path syntax.

### `SecretProviderClass`

The following table lists the configurable parameters on the Conjur Provider's
`SecretProviderClass` instances.

| Field                                 | Description                                                           | Example                                                              |
|---------------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------------|
| `spec.parameters.apiUrl`              | Pulumi API URL                                                        | `https://api.pulumi.com/api/esc`                                     |
| `spec.parameters.organization`        | Pulumi organization name                                              | `my-org`                                                             |
| `spec.parameters.project`             | Pulumi project name                                                   | `my-project`                                                         |
| `spec.parameters.environment`         | Pulumi environment name                                               | `my-env`                                                             |
| `spec.parameters.authSecretName`      | Name of the Kubernetes secret containing the Pulumi access token      | `pulumi-esc-access-token`                                            |
| `spec.parameters.authSecretNamespace` | Namespace of the Kubernetes secret containing the Pulumi access token | `default`                                                            |
| `spec.parameters.secrets`             | List of secrets to retrieve from Pulumi ESC                           | `- secretPath: "/" fileName: "my-secret-file" secret: "root.nested"` |

### Examples

- `root`
- `root.nested`
- `root["nested"]`
- `root.double.nest`
- `root["double"].nest`
- `root["double"]["nest"]`
- `root.array[0]`
- `root.array[100]`
- `root.array[0].nested`
- `root.array[0][1].nested`
- `root.nested.array[0].double[1]`
- `root["key with \"escaped\" quotes"]`
- `root["key with a ."]`
- `["root key with \"escaped\" quotes"].nested`
- `["root key with a ."][100]`
- `root.array[*].field`
- `root.array["*"].field`
