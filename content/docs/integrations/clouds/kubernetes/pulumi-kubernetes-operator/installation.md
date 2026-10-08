---
title_tag: "Installation | Pulumi Kubernetes Operator"
meta_desc: Install the Pulumi Kubernetes Operator, create a service account, and configure Pulumi Cloud access and Pulumi ESC.
title: Installation
h1: "Pulumi Kubernetes Operator: Installation"
menu:
    integrations:
        parent: kubernetes-clouds-operator
        identifier: kubernetes-clouds-operator-installation
        weight: 1
---

This page covers installing the Pulumi Kubernetes Operator, creating a service account for stack operations, and configuring access to Pulumi Cloud and Pulumi ESC.

## Install the operator

### Using Helm

Use [Helm 3.x][helm] to install the Pulumi Kubernetes Operator into your cluster.

```bash
helm install --create-namespace -n pulumi-kubernetes-operator pulumi-kubernetes-operator \
    oci://ghcr.io/pulumi/helm-charts/pulumi-kubernetes-operator --version 2.3.0
```

[helm]: https://helm.sh/

### Dev install

A simple "quickstart" installation manifest is provided for non-production environments.

Install with `kubectl`:

```bash
kubectl apply -f https://raw.githubusercontent.com/pulumi/pulumi-kubernetes-operator/refs/tags/v2.2.0/deploy/quickstart/install.yaml
```

Note: the installation manifest creates a usable Kubernetes service account named `default/pulumi`
for your convenience.

## Create a service account

The operator uses Kubernetes pods as the execution environment for Pulumi stack operations,
with each Stack having a dedicated pod. A pod service account is needed to serve as the stack's identity
and to authenticate users.

Create a `ServiceAccount` named `default/pulumi` and grant the `system:auth-delegator` cluster role:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  namespace: default
  name: pulumi
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: default:pulumi:system:auth-delegator
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:auth-delegator # permissions: TokenReview, SubjectAccessReview
subjects:
- kind: ServiceAccount
  namespace: default
  name: pulumi
```

If your Pulumi program uses the [Kubernetes Provider][] to manage resources within the cluster, the stack's service account will need extra permissions, e.g. a `ClusterRoleBinding` to the `cluster-admin` cluster role.

See ["Kubernetes: Service Accounts"][service-accounts] for more information.

[Kubernetes Provider]: https://www.pulumi.com/registry/packages/kubernetes/
[service-accounts]: https://kubernetes.io/docs/concepts/security/service-accounts/

## Configure Pulumi Cloud access

By default, the operator uses Pulumi Cloud as the state backend for your stacks.
Please create a `Secret` containing a Pulumi access token to be used to authenticate to Pulumi Cloud. Follow [these instructions][tokens] to create a personal, organization, or team access token.

Here's an easy way to create a secret named `default/pulumi-api-secret`:

```bash
kubectl create secret generic -n default pulumi-api-secret \
  --from-literal=accessToken=$PULUMI_ACCESS_TOKEN
```

In the Stack specification, use `spec.envRefs` to reference the secret:

```yaml
spec:
  envRefs:
    PULUMI_ACCESS_TOKEN:
      type: Secret
      secret:
        name: pulumi-api-secret
        key: accessToken
```

To use a DIY state backend, set the `spec.backend` field to a storage endpoint URL.
Use `spec.envRefs` to attach credentials and to set environment variables for the backend as necessary.

See ["States & Backends"][states-backends] for more information.

{{< notes type="info" >}}
To avoid storing long-lived Pulumi access tokens in your cluster, you can register the cluster as a Pulumi Cloud OIDC Issuer and have workspace pods exchange their projected service account tokens for short-lived Pulumi tokens. See [Configuring OpenID Connect for Amazon EKS](/docs/administration/guides/oidc-issuers/kubernetes-eks/) or [Configuring OpenID Connect for Google Kubernetes Engine](/docs/administration/guides/oidc-issuers/kubernetes-gke/).
{{< /notes >}}

[tokens]: https://www.pulumi.com/docs/administration/concepts/access-tokens/
[states-backends]: https://www.pulumi.com/docs/iac/concepts/state-and-backends/

## Use Pulumi ESC for centralized configuration

[Pulumi ESC (Environments, Secrets, and Configuration)][pulumi-esc] provides centralized management of secrets and configuration. You can attach ESC environments to Stack objects to access shared configuration and secrets across multiple stacks.

Use the `spec.environment` field to specify one or more ESC environment names:

```yaml
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: my-app
spec:
  serviceAccountName: pulumi
  stack: my-org/my-app/prod
  projectRepo: https://github.com/example/app
  branch: main
  environment:
    - prod-shared-config
    - aws-credentials
  envRefs:
    PULUMI_ACCESS_TOKEN:
      type: Secret
      secret:
        name: pulumi-api-secret
        key: accessToken
```

ESC environments are accessed using your Pulumi access token. The configuration and secrets from these environments become available to your Pulumi program automatically.

[pulumi-esc]: https://www.pulumi.com/docs/esc/
