---
title: "Pulumi Kubernetes 4.10: ConfigGroup/ConfigFile resources for Java, YAML SDKs"
date: 2024-03-30T00:00:00-07:00

meta_desc: >-
  Pulumi Kubernetes v4.10 offers new resources for applying Kubernetes manifests consistently across Pulumi SDKs, and broaden support to the Java and YAML SDKs.

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
The package provides new implementations of the `ConfigGroup` and `ConfigFile` resources, expanding support to the
Pulumi Java SDK and to Pulumi YAML.

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

### Manifest Files
Here's an example of applying a Kubernetes manifest file to your cluster:

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
Here's how to apply an inline manifest:

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
With `ConfigGroup` it is possible to define a Kubernetes object using Pulumi property values.

```yaml
name: demo-cg-3
runtime: yaml
resources:
  cg:
    type: kubernetes:yaml/v2:ConfigGroup
    properties:
      objs:
      - apiVersion: stable.example.com/v1
        kind: CronTab
        metadata:
          name: my-crontab
        spec:
          cronSpec: "* * * * */5"
```

This feature is expecially useful for Pulumi YAML, since the `apiextensions.k8s.io:CustomResource` resource isn't 
supported yet (see [pulumi-kubernetes#2787](https://github.com/pulumi/pulumi-kubernetes/issues/2787)).

### Resource Prefixes
A notable change from 'v1' is how resource prefixes work. The purpose of the resource prefix is to ensure the uniqueness
of child resource names, as described in [Pulumi: Resource Names](https://www.pulumi.com/docs/concepts/resources/names/#urns).

Note that the resource prefix is +not+ applied to the Kubernetes object names.

### Transformation Support
The Kubernetes provider generally supports resource transformations, e.g. to apply a resource alias or
to apply an object name prefix or object label. Unfortunately, transformations aren't yet possible with the
new `ConfigGroup` resource, but stay tuned as we work towards a GA release later this year.

## kubernetes.yaml/v2.ConfigFile

The `ConfigFile` resource creates a set of Kubernetes objects from a Kubernetes manifest. While `ConfigGroup` offers
a superset of functionality, the `ConfigFile` gives a concise way to apply a specific manifest.

The `ConfigFile` resource accepts the following input properties:

| Property         | Description                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------- |
| `file`           | A file or URL to a Kubernetes manifest file.                                                  |
| `resourcePrefix` | A prefix for auto-generated names of the child resources. Defaults to the `ConfigFile` name. |
| `skipAwait`      | Skips over the readiness checks on the child resources.                                       |

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
