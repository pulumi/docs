---
title: "New: ConfigGroup, ConfigFile resources for Java, YAML SDKs"
date: 2024-04-12T00:00:00-07:00
meta_image: meta.png
meta_desc: >-
  Pulumi Kubernetes v4.10 offers new resources for applying Kubernetes manifests consistently across Pulumi SDKs, and broadens support to the Java and YAML SDKs.

authors:
    - eron-wright

tags:
    - kubernetes
    - yaml
    - java
---

The Pulumi Kubernetes provider makes it easy to deploy Kubernetes resources to your cluster, giving you options
based on how your application or workload is packaged. The options include strongly-typed resources for
standard Kubernetes types, [Helm](https://helm.sh/) charts, [Kustomizations](https://kustomize.io/), and Kubernetes manifests.

In v4.10, we leveled up the support for working with Kubernetes manifests with the introduction of the `yaml/v2` package.
The package provides new implementations of the [`ConfigGroup`](/registry/packages/kubernetes/api-docs/yaml/v2/configgroup/)
and [`ConfigFile`](/registry/packages/kubernetes/api-docs/yaml/v2/configfile/) resources, expanding support to the
Pulumi Java SDK and to Pulumi YAML. The new implementations are also smarter about applying the objects in the correct order.

Please note that these resources are in a preview stage of maturity, as we continue to round out the feature set.
These new resources are provided side-by-side with the existing implementations.

Let's explore how it's easier than ever to deploy diverse Kubernetes workloads using Pulumi.

## kubernetes.yaml/v2.ConfigGroup

The `ConfigGroup` resource creates a set of Kubernetes objects from Kubernetes manifests and/or object literals.
The Kubernetes manifest may be supplied using any combination of the following methods:

1. a filename or a list of filenames.
2. a file pattern or a list of file patterns.
3. a literal string containing YAML or JSON text.
4. a literal object or a list of objects.

The `ConfigGroup` resource accepts the following input properties:

| Property         | Description                                                                                                                                              |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `files`          | Set of files, patterns and/or URLs to Kubernetes manifest files. Filenames containing any of the characters `*`, `?`, and `[` are treated as _patterns_. |
| `objs`           | Set of Kubernetes objects.                                                                                                                               |
| `yaml`           | A Kubernetes manifest as a YAML or JSON string.                                                                                                          |
| `resourcePrefix` | A prefix for auto-generated names of the child resources. Defaults to the `ConfigGroup` name.                                                            |
| `skipAwait`      | Skips over the readiness checks on the child resources.                                                                                                  |

Note that all objects defined within the manifest must have a `metadata.name` field;
Pulumi [autonaming](https://www.pulumi.com/docs/concepts/resources/names/#autonaming) is not supported.

See the [API Reference documentation](/registry/packages/kubernetes/api-docs/yaml/v2/configgroup/)
for more information.

### Manifest Files

Here's an example of applying a Kubernetes manifest file to your cluster.

```yaml
name: demo-cg-1
runtime: yaml
resources:
  cg:
    type: kubernetes:yaml/v2:ConfigGroup
    properties:
      files:
      - ./manifest.yaml
```

### YAML Text

Here's how to apply an inline manifest.

```yaml
name: demo-cg-2
runtime: yaml
resources:
  cg:
    type: kubernetes:yaml/v2:ConfigGroup
    properties:
      yaml: |
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: my-server-config
        data:
          altGreeting: "Good Morning!"
        ---
        apiVersion: v1
        kind: Secret
        metadata:
          name: my-dotfile-secret
        data:
          .secret-file: dmFsdWUtMg0KDQo=
```

### Object Literals

With `ConfigGroup` it's easy to define a Kubernetes object using Pulumi property values. Let's create a
Kubernetes namespace and deploy a custom resource into that namespace.

```yaml
name: demo-cg-3
runtime: yaml
resources:
  ns:
    type: kubernetes:core/v1:Namespace
  cg:
    type: kubernetes:yaml/v2:ConfigGroup
    properties:
      objs:
      - apiVersion: stable.example.com/v1
        kind: CronTab
        metadata:
          namespace: ${ns.metadata.name}
          name: my-crontab
        spec:
          cronSpec: "* * * * */5"
```

This feature is expecially useful for Pulumi YAML, since the `apiextensions.k8s.io:CustomResource` resource isn't
supported yet (see [pulumi-kubernetes#2787](https://github.com/pulumi/pulumi-kubernetes/issues/2787)).

### Resource Ordering

The `ConfigGroup` resource automatically detects dependencies between resources in the manifest(s).
For example, it knows to install namespaces and Custom Resource Definitions (CRDs) first.

Use the `config.kubernetes.io/depends-on` annotation to declare an explicit resource dependency.
The annotation accepts a list of resource references, delimited by commas.

It consists of the group, kind, name, and optionally the namespace, delimited by forward slashes.

| Resource Scope   | Format                                         |
| :--------------- | :--------------------------------------------- |
| namespace-scoped | `<group>/namespaces/<namespace>/<kind>/<name>` |
| cluster-scoped   | `<group>/<kind>/<name>`                        |

For resources in the “core” group, the empty string is used instead (for example: `/namespaces/test/Pod/pod-a`).

### Resource Prefixes

The purpose of the resource prefix is to ensure the uniqueness
of child resource names, as described in [Pulumi: Resource Names](https://www.pulumi.com/docs/concepts/resources/names/#urns).
The best practice is to use the component name as a prefix, and now that's the default behavior.

Note that the resource prefix is __not__ applied to the Kubernetes object names.

### Transformation Support

The Kubernetes provider generally supports resource transformations, e.g. to apply a resource alias or
to apply an object name prefix or object label. Transformations aren't yet possible with the
new `ConfigGroup` resource (see [pulumi/pulumi#12996](https://github.com/pulumi/pulumi/issues/12996)),
but stay tuned as we work towards a GA release later this year.

## kubernetes.yaml/v2.ConfigFile

The `ConfigFile` resource creates a set of Kubernetes objects from a Kubernetes manifest. While `ConfigGroup` offers
a superset of functionality, the `ConfigFile` gives a concise way to apply a specific manifest.

The `ConfigFile` resource accepts the following input properties:

| Property         | Description                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------- |
| `file`           | A file or URL to a Kubernetes manifest file.                                                  |
| `resourcePrefix` | A prefix for auto-generated names of the child resources. Defaults to the `ConfigFile` name. |
| `skipAwait`      | Skips over the readiness checks on the child resources.                                       |

See the [API Reference documentation](/registry/packages/kubernetes/api-docs/yaml/v2/configfile/)
for more information.

### Manifest File

Here's an example of applying a Kubernetes manifest file to your cluster:

```yaml
name: demo-cg-1
runtime: yaml
resources:
  cf:
    type: kubernetes:yaml/v2:ConfigFile
    properties:
      file: ./manifest.yaml
```

## Example: Certificate Manager

Here's a complete example of how to install and use cert-manager using `ConfigGroup` resources.

```yaml
name: cert-manager
runtime: yaml
description: Installs cert-manager.  See https://cert-manager.io/docs/installation/kubectl/ for details.
variables: {}
resources:
  install:
    type: kubernetes:yaml/v2:ConfigGroup
    properties:
      files:
      - https://github.com/cert-manager/cert-manager/releases/download/v1.14.4/cert-manager.yaml
  test:
    type: kubernetes:yaml/v2:ConfigGroup
    options:
      dependsOn:
      - ${install}
    properties:
      yaml: |
        apiVersion: v1
        kind: Namespace
        metadata:
          name: cert-manager-test
        ---
        apiVersion: cert-manager.io/v1
        kind: Issuer
        metadata:
          name: test-selfsigned
          namespace: cert-manager-test
        spec:
          selfSigned: {}
        ---
        apiVersion: cert-manager.io/v1
        kind: Certificate
        metadata:
          name: selfsigned-cert
          namespace: cert-manager-test
          annotations:
            config.kubernetes.io/depends-on: cert-manager.io/namespaces/cert-manager-test/Issuer/test-selfsigned
        spec:
          dnsNames:
            - example.com
          secretName: selfsigned-cert-tls
          issuerRef:
            name: test-selfsigned
```

## Conclusion

With the new resources in `yaml/v2`, we're excited to enable new scenarios in Pulumi YAML and the Pulumi Java SDK.
Stay tuned for new editions of the `Chart` and `Directory` resources, coming soon.

This is part of a broad initiative to use Multi-Language Component (MLC) technology to offer a consistent experience
across the Pulumi SDKs. See [pulumi-kubernetes#1971](https://github.com/pulumi/pulumi-kubernetes/issues/1971) for details.

Check out the following links to learn more about Pulumi Kubernetes today!

* [Getting Started](/docs/clouds/kubernetes/get-started/)
* [Documentation](/docs/clouds/kubernetes/)
* [Open Source](https://github.com/pulumi/pulumi-kubernetes)
* [Community Slack](https://slack.pulumi.com/)
