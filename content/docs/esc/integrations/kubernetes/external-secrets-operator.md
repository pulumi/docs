---
title: External Secrets Operator (ESO)
title_tag: Integrate with External Secrets Operator (ESO) | Pulumi ESC
h1: "Pulumi ESC: Integrate with External Secrets Operator (ESO)"
meta_desc: Pulumi ESC integrates with the External Secrets Operator (ESO) to manage
  and deliver secrets in Kubernetes clusters.
weight: 2
menu:
  esc:
    identifier: esc-external-secrets-operator
    parent: esc-kubernetes-integrations
aliases:
  - /docs/esc/other-integrations/external-secrets-operator/
search:
  keywords:
    - eso
    - operator
    - secrets
    - kubernetes
    - external
    - deliver
    - integrates
---

## Overview

[External Secrets Operator](https://external-secrets.io/latest/) is a Kubernetes operator that integrates external secret management systems with Kubernetes. By using External Secrets Operator, you have several advantages over Kubernetes native secrets:

- Sensitive data is stored and managed by an external service outside the Kubernetes cluster and this leads to better security and compliance.
- External Secrets Operator supports multiple different sources, so you can use the same operator to manage secrets and configuration from different sources.
- Take advantage of the advanced features of the secret provider, such as encryption of data at rest and scenarios like secret rotation.

Since version `0.10.0` External Secrets Operator supports [Pulumi ESC as a secret provider](https://external-secrets.io/latest/provider/pulumi/).

## Authentication

Pulumi [Access Tokens](/docs/pulumi-cloud/access-management/access-tokens/) are recommended to access Pulumi ESC.

## Creating a SecretStore

A Pulumi `SecretStore` can be created by specifying the `organization`, `project` and `environment` and referencing a Kubernetes secret containing the `accessToken`.

```yaml
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: secret-store
spec:
  provider:
    pulumi:
      organization: <NAME_OF_THE_ORGANIZATION>
      project: <NAME_OF_THE_PROJECT>
      environment: <NAME_OF_THE_ENVIRONMENT>
      accessToken:
        secretRef:
          name: <NAME_OF_KUBE_SECRET>
          key: <KEY_IN_KUBE_SECRET>
```

If required, the API URL (`apiUrl`) can be customized as well. If not specified, the default value is `https://api.pulumi.com/api/esc`.

## Creating a ClusterSecretStore

Similarly, a `ClusterSecretStore` can be created by specifying the `namespace` and referencing a Kubernetes secret containing the `accessToken`.

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ClusterSecretStore
metadata:
  name: secret-store
spec:
  provider:
    pulumi:
      organization: <NAME_OF_THE_ORGANIZATION>
      project: <NAME_OF_THE_PROJECT>
      environment: <NAME_OF_THE_ENVIRONMENT>
      accessToken:
        secretRef:
          name: <NAME_OF_KUBE_SECRET>
          key: <KEY_IN_KUBE_SECRET>
          namespace: <NAMESPACE>
```

## Referencing Secrets

Secrets can be referenced by defining the `key` containing the JSON path to the secret. Pulumi ESC secrets are internally organized as a JSON object.

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: secret
spec:
  refreshInterval: 1h
  secretStoreRef:
    kind: SecretStore
    name: secret-store
  data:
  - secretKey: <KEY_IN_KUBE_SECRET>
    remoteRef:
      key: <PULUMI_PATH_SYNTAX>
```

**Note:** `key` is not following the JSON Path syntax, but rather the Pulumi path syntax.

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

## PushSecrets

With the latest release of Pulumi ESC, secrets can be pushed to the Pulumi service. This can be done by creating a [`PushSecrets`](https://external-secrets.io/latest/api/pushsecret/) object.

Here is a basic example of how to define a `PushSecret` object:

```yaml
apiVersion: external-secrets.io/v1alpha1
kind: PushSecret
metadata:
  name: push-secret-example
spec:
  refreshInterval: 1h
  selector:
    secret:
      name: <NAME_OF_KUBE_SECRET>
  secretStoreRefs:
  - kind: ClusterSecretStore
    name: secret-store
  data:
  - match:
      secretKey: <KEY_IN_KUBE_SECRET>
      remoteRef:
        remoteKey: <PULUMI_PATH_SYNTAX>
```

This will then push the secret to the Pulumi service. If the secret already exists, it will be updated.

## Limitations

Currently, the Pulumi provider only supports nested objects up to a depth of 1. Any nested objects beyond this depth will be stored as a string with the JSON representation.

This Pulumi ESC environment:

```yaml
values:
  backstage:
    my: test
    test: hello
    test22:
      my: hello
    test33:
      world: true
    x: true
    num: 42
```

Will result in the following Kubernetes secret:

```yaml
my: test
num: "42"
test: hello
test22: '{"my":{"trace":{"def":{"begin":{"byte":72,"column":11,"line":6},"end":{"byte":77,"column":16,"line":6},"environment":"tgif-demo"}},"value":"hello"}}'
test33: '{"world":{"trace":{"def":{"begin":{"byte":103,"column":14,"line":8},"end":{"byte":107,"column":18,"line":8},"environment":"tgif-demo"}},"value":true}}'
x: "true"
```
