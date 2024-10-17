---
date: "2024-10-17"
title: "Pulumi Kubernetes Operator 2.0"
authors: ["eron-wright"]
tags: ["Kubernetes", "Continuous-Delivery", "operators"]
meta_desc: "Pulumi Kubernetes Operator 2.0: Horizontal Scaling, Multi-Tenancy"
meta_image: operator.png
---

A few years ago we released the [Pulumi Kubernetes Operator](/blog/pulumi-kubernetes-operator-1-0/), a cloud-native way to manage and deploy cloud infrastructure using Pulumi from within your Kubernetes environment. We've heard your feedback about limitations related to scalability and isolation.
Today, we're excited to make [2.0 beta 1](https://github.com/pulumi/pulumi-kubernetes-operator/releases/tag/v2.0-beta.1) of the Pulumi Kubernetes Operator available.
We've put a new architecture in place to address these limitations and to provide new customization options. Let's dig in!

## What is the Pulumi Kubernetes Operator?

The Pulumi Kubernetes Operator defines a Kubernetes Custom Resource called `pulumi.com/v1/Stack`, which represents a Pulumi [stack](/docs/concepts/stack/). The Pulumi stack can be authored in any supported Pulumi language (TypeScript, Python, Go, .NET, Java, YAML) and can deploy and manage cloud infrastructure in any supported cloud (AWS, Azure, GCP, Kubernetes and 60+ additional cloud and SaaS providers). The Pulumi Kubernetes Operator triggers cloud deployments based on changes to the `Stack` Custom Resource or the resources it uses.

As a result, the Pulumi Kubernetes Operator enables users to specify the desired state of their cloud infrastructure using resources managed directly in their Kubernetes cluster, which trigger creation, update and deletion of the detailed cloud infrastructure they need.

<!--more-->

For example, the following Kubernetes resource can be created to deploy a Pulumi program which provisions cloud infrastructure to manage NGINX provided in the target Git repo and commit, and future updates to the commit or config settings will deploy updates to the infrastructure.

```yaml
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: nginx-k8s-stack-production
spec:
  stack: acmecorp/nginx/production
  projectRepo: https://github.com/acmecorp/pulumi-nginx
  commit: 2b0889718d3e63feeb6079ccd5e4488d8601e353
```

The Pulumi Kubernetes Operator can also be used along with Pulumi’s [Kubernetes provider](/registry/packages/kubernetes/), which allows Pulumi programs to deploy resources to Kubernetes, either in the same cluster as the operator, or in another cluster. This can be used to package up complex Kubernetes infrastructure into more abstracted units, to mix Kubernetes and cloud infrastructure into a single unit of deployment, to define how application workloads are deployed into a cluster, or for a wide variety of additional use cases. The Pulumi Kubernetes provider has full support for the Kubernetes API available in every Pulumi language, including support for [Helm](/blog/full-access-to-helm-features-through-new-helm-release-resource-for-kubernetes/).

## What’s New in Pulumi Kubernetes Operator 2.0?

The 2.0 release is based on a whole new architecture for running Pulumi programs in your Kubernetes cluster.
The operator now allocates a dedicated pod for each `Stack` to serve as the execution environment for Pulumi stack operations.
Previously, all stack operations took place within the operator's own pod. This new approach effectively isolates
each stack's compute and memory resources, improves the isolation of secrets, and opens up new customization options.

These pods are referred to as *workspace pods*.  Under the hood, a new `Workspace` Custom Resource handles the lifecycle
of the workspace pod, and is created automatically by the system. A related `Update` Custom Resource applies a stack operation to a given workspace.

The `Stack` Custom Resource is still the primary API for using the Pulumi Kubernetes Operator and is largely unchanged.
See the Migration section below to understand how to prepare your `Stack` objects for use with the 2.0 release.

Note: a key limitation of the new system is that cross-namespace references are strictly forbidden. For example, a `Stack` cannot refer
to a `Secret` in another namespace.

### Installation

With the 2.0 release, the supported installation modes are limited to a cluster-wide installation. You'll need to be
a cluster admin to install the operator. The operator is able to handle stacks across all the namespaces of your cluster.

We provide three ways to install the operator:

1. a Pulumi program (see: `deploy/pulumi-operator-yaml/`)
2. a Helm chart (see: `deploy/helm/pulumi-operator/`)
3. a simple manifest file (see: `deploy/yaml/install.yaml`)

Please uninstall any earlier version of the Pulumi Kubernetes Operator, then install the new version using one of the above options.
Note that this will remove any existing `Stack` objects in your cluster, so be sure to export their manifests or have
a way to restore them.

### Security

To protect your Kubernetes cluster, workspace pods are configured to have minimal permissions as defined
by the 'restricted' profile of the [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/).
If necessary, you may configure a stack to use the 'baseline' profile.

A Kubernetes `ServiceAccount` provides an identity for your workspace pod, and we recommend that you create
a service account for your stack rather than using the `default` account. If your Pulumi program uses the
Kubernetes provider to manage resources within the cluster, the stack's service account will need permissions, e.g.
a `RoleBinding` to the `ClusterRole` named `cluster-admin`. See ["Service Accounts"](https://kubernetes.io/docs/concepts/security/service-accounts/) for more information.

The workspace pod has a RPC endpoint that is used by the operator to run stack operations. The pod protects the
RPC endpoint using Kubernetes RBAC, and for that reason you must bind the `ClusterRole` named `system:auth-delegator` to the
stack's service account.

<!--more-->

Here's an example of a service account and associated role binding for use by a given stack:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-program
  namespace: default
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: my-program:system:auth-delegator
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:auth-delegator
subjects:
- kind: ServiceAccount
  name: my-program
  namespace: default
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: my-program
  namespace: default
spec:
  serviceAccountName: my-program
  ...
```

### Scalability

Each stack is run in its own "workspace" pod, and so the system scales horizontally to support many stacks.
The workspace pod is, by default, configured to use minimal resources when idle, and to 'burst' into the unused
memory and compute resources of the node during a stack operation. You may customize the resource constraints to
fit the needs of your stack. If your Kubernetes cluster has high utilization, we recommend increasing the resource requests
and limits. See ["Pod Quality of Service Classes"](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/) for more information.

The pod is not discarded at the end of a stack operation, it remains in-place unless the stack is deleted.
We're considering introducing the option to clean up the workspace pod after each operation, to enable you to make a trade-off
decision between performance and efficiency.

### Robustness

A Kubernetes cluster is a dynamic environment where a given pod may be terminated at any time, e.g. due to maintenance operations,
unplanned node events, or resource pressure. This can cause problems for ongoing stack operations, and historically
may cause a stack to become "locked" (thus necessitating the use of `pulumi cancel`).

The new system has been made more resilient by being responsive to pod termination requests. It responds by
proactively sending CTRL-C to the ongoing stack operation, to gracefully wind down the operation.

If your stack has a lot of resources, consider increasing the pod's termination grace period (default: 10 minutes).

### Customization and Extensibility

Let's discuss how to customize the stack's environment. The `Stack` resource continues to provide ways to set environment variables
and to set [stack configuration values](/docs/iac/concepts/config/). What's new is the ability to:

- use a custom Docker image for your stack environment
- set the stack environment's compute and storage resources
- attach volumes, init containers, and sidecars

This is accomplished using the `workspaceTemplate` field of the `Stack` resource, to customize the `Workspace` object
that is automatically created by the system for a given stack.

By default, the system uses the official [pulumi/pulumi](https://hub.docker.com/r/pulumi/pulumi) Docker image.
You may wish to create your own Docker image that is based on it, e.g. to pre-install your program's dependencies
(using `pulumi install`) for performance reasons. Be prepared to update the image over time to incorporate the latest version of the Pulumi CLI.

One use case for an extra init container is to customize how your program's sources are obtained. The system supports
Git repositories and Flux sources out-of-the-box, but you have the option of handling it yourself, e.g. to generate
a Pulumi project or to download from another source. You simply inject an init container, mount the `share` volume to `/share`,
and then place the project files into `/share/workspace`. Contact us to learn more.

Here's an example of a stack with some customizations applied:

```yaml
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: my-stack
spec:
  workspaceTemplate:
    spec:
      image: example/pulumi-with-dependencies:v3.334
      podTemplate:
        metadata:
          labels:
            example.com/mylabel: bar
        spec:
          terminationGracePeriodSeconds: 3600
          tolerations:
          - key: "example.com/foo"
            operator: "Exists"
            effect: "NoSchedule"
          initContainers:
          - name: extra # add an extra init container
            image: busybox
            command: ["sh", "-c", "echo 'Hello, extra init container!'"]
            securityContext:
              allowPrivilegeEscalation: false
              capabilities:
                add:
                - NET_BIND_SERVICE
                drop:
                - ALL
            volumeMounts:
            - name: share
              mountPath: /share
          containers:
            - name: pulumi # customize the main container where Pulumi stack operations are executed
            volumeMounts:
            - name: oidc-token
              mountPath: /var/run/secrets/pulumi
          volumes:
          - name: oidc-token # mount an OIDC token
            projected:
              sources:
              - serviceAccountToken:
                  audience: urn:pulumi:org:ORG_NAME
                  path: token
                  expirationSeconds: 3600
```

### Operability

Since each stack has its own long-running pod, you may inspect the console output for a given stack by accessing
the pod logs. The pod's name is based on the stack name; for example, given a stack named `my-stack`, look for
a pod named `my-stack-workspace-0`. We recommend the [stern](/opt/homebrew/bin/stern) tool to access pod logs.
See ["Pod and container logs"](https://kubernetes.io/docs/concepts/cluster-administration/logging/#basic-logging-in-kubernetes) for more information.

If you need to run an interactive Pulumi command for your stack, e.g. `pulumi import`, exec into the workspace pod. Navigate to the
`/share/workspace` directory and you should find your program there.

### Migration

The `Stack` custom resource continues to be the primary way to use the Pulumi Kubernetes Operator, and your existing
stack definitions should continue to work after you follow a simple migration procedure:

1. Create a `ServiceAccount` and associated `ClusterRoleBinding` as shown in the Security section.
2. If your stack uses the [Pulumi Kubernetes Provider](/registry/packages/kubernetes/), create a `RoleBinding` or a `ClusterRoleBinding` to grant the necessary permissions, e.g. to the well-known `ClusterRole` named `cluster-admin`. See ["Using RBAC Authorization"](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) for more information.
3. Edit your `Stack` manifest(s) to use the service account, by setting the `spec.serviceAccountName` field.
4. Double-check that your `Stack` objects do not make use of cross-namespace references.

If you're using a private Git repository as your program source, use the Stack's `secretRefs` field to reference Git credentials.
SSH-based access to the repository isn't fully supported; contact us to learn more.

If you're using Flux integration, there's an additional step to be performed by your cluster administrator.
Please create a `NetworkPolicy` to allow the workspace pods to access the Flux source controller. Here's the manifest
to be applied:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-pulumi-fetch-flux-artifacts
  namespace: flux-system
spec:
  podSelector:
    matchLabels:
      app: source-controller
  ingress:
    - ports:
        - protocol: TCP
          port: http
      from:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: default
        - podSelector:
            matchLabels:
              app.kubernetes.io/managed-by: pulumi-kubernetes-operator
              app.kubernetes.io/name: pulumi
              app.kubernetes.io/component: workspace
  policyTypes:
    - Ingress
```

## Conclusion

The Pulumi Kubernetes Operator is a great way to deploy and manage cloud infrastructure from within your Kubernetes environment. With the 2.0 release,
we've solved the scalability and isolation limitations that affected early adopters. You can [get started with the Pulumi Kubernetes Operator today](/docs/iac/packages-and-automation/continuous-delivery/pulumi-kubernetes-operator/). Please join us on the #kubernetes channel of
the [Pulumi Community Slack workspace](https://slack.pulumi.com) to give feedback, and enjoy!
