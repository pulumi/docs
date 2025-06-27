---
title_tag: "Using ArgoCD with Pulumi Kubernetes Operator | CI/CD"
meta_desc: This page details how to use ArgoCD with the Pulumi Kubernetes Operator to deploy infrastructure and applications through GitOps workflows.
title: ArgoCD
h1: ArgoCD with Pulumi Kubernetes Operator
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: ArgoCD
        parent: iac-using-pulumi-cicd
        weight: 2
aliases:
- /docs/guides/continuous-delivery/argocd/
- /docs/using-pulumi/continuous-delivery/argocd/
- /docs/iac/packages-and-automation/continuous-delivery/argocd/
---

ArgoCD (Argo Continuous Deployment) is a declarative, GitOps continuous delivery tool for Kubernetes. When combined with the Pulumi Kubernetes Operator (PKO), ArgoCD provides powerful capabilities for managing both infrastructure and applications through GitOps workflows.

This integration allows you to:

- **Manage multiple clusters**: Use ArgoCD's dashboard to control and monitor Pulumi deployments across multiple Kubernetes clusters
- **Deploy complete environments**: Create entire clusters and deploy applications into them in a single workflow
- **Maintain separation of concerns**: ArgoCD users work with familiar Stack objects while Pulumi handles the complex infrastructure provisioning
- **Leverage GitOps principles**: All changes flow through Git, providing audit trails and rollback capabilities

## Why combine ArgoCD with Pulumi?

Traditional GitOps tools like ArgoCD work well with Kubernetes manifests but are limited when it comes to provisioning infrastructure beyond Kubernetes resources. While tools like Crossplane can create some cloud resources, they're typically limited to generating Kubernetes manifests and objects.

Pulumi with PKO breaks these limitations:

- **Provision entire clusters**: Create new Kubernetes clusters, then deploy applications into them
- **Use real programming languages**: Write infrastructure as code using TypeScript, Python, Go, .NET, Java, or YAML
- **Access the full cloud API**: Provision any cloud resource supported by your cloud provider
- **Manage complex dependencies**: Handle intricate relationships between cloud resources and applications

## How it works

The integration works through Kubernetes custom resources:

1. **ArgoCD manages Stack objects**: ArgoCD treats Pulumi `Stack` resources like any other Kubernetes manifest
2. **PKO executes Pulumi operations**: The Pulumi Kubernetes Operator watches for Stack objects and runs `pulumi up` to create infrastructure
3. **Clean separation**: ArgoCD users think in terms of Stack objects, while Pulumi handles the infrastructure details

## Prerequisites

Before you begin, ensure you have:

- A Kubernetes cluster with ArgoCD installed
- [Pulumi Kubernetes Operator](/docs/iac/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/) installed in your cluster
- A Git repository containing your Pulumi programs
- Access to Pulumi Cloud or a self-managed backend

## Basic setup

### 1. Install ArgoCD

If you haven't already installed ArgoCD, you can install it using the official manifests:

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Alternatively, use the Helm chart for more configuration options:

```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm install argocd argo/argo-cd -n argocd --create-namespace
```

### 2. Create a Pulumi Stack manifest

Create a Kubernetes manifest file that defines your Pulumi Stack. This example creates a simple web application:

```yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: pulumi-stack-sa
  namespace: default
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: pulumi-stack-sa:system:auth-delegator
  annotations:
    argocd.argoproj.io/sync-wave: "1"
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:auth-delegator
subjects:
- kind: ServiceAccount
  name: pulumi-stack-sa
  namespace: default
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: pulumi-stack-sa:cluster-admin
  annotations:
    argocd.argoproj.io/sync-wave: "1"
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: pulumi-stack-sa
  namespace: default
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: webapp-dev
  namespace: default
  annotations:
    argocd.argoproj.io/sync-wave: "2"
    link.argocd.argoproj.io/external-link: https://app.pulumi.com/myorg/webapp/dev
spec:
  serviceAccountName: pulumi-stack-sa
  stack: myorg/webapp/dev
  projectRepo: "https://github.com/myorg/pulumi-webapp.git"
  branch: main
  refresh: true
  continueResyncOnCommitMatch: true
  resyncFrequencySeconds: 300
  destroyOnFinalize: true
  envRefs:
    PULUMI_ACCESS_TOKEN:
      type: Secret
      secret:
        name: pulumi-access-token
        key: token
  config:
    webapp:environment: development
    webapp:replicas: "2"
```

### 3. Create an ArgoCD Application

Create an ArgoCD Application that monitors your Git repository:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: webapp-dev
  namespace: argocd
  finalizers:
    - resources-finalizer.argocd.argoproj.io/background
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/webapp-infrastructure.git
    targetRevision: main
    path: manifests/dev
  destination:
    server: https://kubernetes.default.svc
    namespace: default
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
```

### 4. Configure secrets

Create a Kubernetes Secret containing your Pulumi access token:

```bash
kubectl create secret generic pulumi-access-token \
  --from-literal=token=$PULUMI_ACCESS_TOKEN \
  -n default
```

## Advanced patterns

### Multi-cluster deployments

ArgoCD excels at managing deployments across multiple clusters. You can use this capability with Pulumi to provision infrastructure in different regions or environments:

```yaml
# Production cluster in us-west-2
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: webapp-prod-usw2
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/webapp-infrastructure.git
    targetRevision: main
    path: manifests/prod
  destination:
    server: https://prod-usw2-cluster.example.com
    namespace: default
  syncPolicy:
    automated:
      prune: true
---
# Production cluster in eu-west-1
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: webapp-prod-euw1
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/webapp-infrastructure.git
    targetRevision: main
    path: manifests/prod
  destination:
    server: https://prod-euw1-cluster.example.com
    namespace: default
  syncPolicy:
    automated:
      prune: true
```

### Creating clusters and applications together

One of the most powerful features of this integration is the ability to provision entire environments, including the Kubernetes cluster itself:

```yaml
# First, create the cluster
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: cluster-dev
  namespace: argocd
  annotations:
    argocd.argoproj.io/sync-wave: "1"
spec:
  serviceAccountName: pulumi-stack-sa
  stack: myorg/eks-cluster/dev
  projectRepo: "https://github.com/myorg/pulumi-eks.git"
  branch: main
  destroyOnFinalize: true
  envRefs:
    PULUMI_ACCESS_TOKEN:
      type: Secret
      secret:
        name: pulumi-access-token
        key: token
  config:
    aws:region: us-west-2
    cluster:nodeCount: "3"
    cluster:instanceType: t3.medium
---
# Then deploy applications to the cluster
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: apps-dev
  namespace: argocd
  annotations:
    argocd.argoproj.io/sync-wave: "2"
spec:
  serviceAccountName: pulumi-stack-sa
  stack: myorg/k8s-apps/dev
  projectRepo: "https://github.com/myorg/pulumi-apps.git"
  branch: main
  prerequisites:
  - type: Stack
    requirement: cluster-dev
    succeededWithinDuration: 30m
  envRefs:
    PULUMI_ACCESS_TOKEN:
      type: Secret
      secret:
        name: pulumi-access-token
        key: token
    KUBECONFIG:
      type: StackOutput
      stack: cluster-dev
      output: kubeconfig
```

### Using ArgoCD sync waves

ArgoCD sync waves allow you to control the order of resource deployment. This is particularly useful when you have dependencies between different Pulumi stacks:

```yaml
# Wave 1: Create secrets and service accounts
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "1"
---
# Wave 2: Deploy infrastructure
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "2"
---
# Wave 3: Deploy applications
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "3"
```

## Best practices

### Resource organization

- **Separate repositories**: Keep infrastructure code and manifests in separate repositories for better security and access control
- **Environment branching**: Use different branches or directories for different environments (dev, staging, prod)
- **Stack naming**: Use consistent naming conventions for your Pulumi stacks that align with your ArgoCD applications

### Security considerations

- **Service account permissions**: Grant minimal required permissions to your Pulumi stack service accounts
- **Secret management**: Use Kubernetes secrets for sensitive data and consider external secret management tools
- **Access control**: Leverage ArgoCD's RBAC features to control who can deploy to which environments

### Monitoring and observability

- **External links**: Use ArgoCD's external link annotations to link directly to Pulumi Cloud for detailed deployment information:

  ```yaml
  annotations:
    link.argocd.argoproj.io/external-link: https://app.pulumi.com/myorg/mystack/dev
  ```

- **Health checks**: Configure appropriate health checks for your Pulumi Stack resources
- **Notifications**: Set up ArgoCD notifications for deployment failures or successes

### Performance optimization

- **Resync frequency**: Adjust `resyncFrequencySeconds` based on your needs - shorter intervals provide faster drift detection but consume more resources
- **Refresh settings**: Enable `refresh: true` to ensure state accuracy, but be aware of the performance impact
- **Resource limits**: Set appropriate resource limits in your PKO workspace templates

## Troubleshooting

### Common issues

**Stack deployment fails**

- Check the Pulumi Stack's status in the ArgoCD UI
- Examine the PKO pod logs: `kubectl logs -l app.kubernetes.io/name=pulumi-kubernetes-operator`
- Verify your Pulumi access token is correct and has the required permissions

**ArgoCD shows Stack as "Unknown" or "Progressing"**

- The PKO includes custom health checks for Stack resources
- Check if the Stack is waiting for dependencies to be resolved
- Verify that the referenced Git repository and path are accessible

**Stack stuck in "Updating" state**

- Check for resource conflicts or locks in your cloud provider
- Review the Pulumi deployment logs in the workspace pod
- Consider enabling `refresh: true` to resolve state inconsistencies

### Getting help

- Review the [Pulumi Kubernetes Operator documentation](/docs/iac/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/)
- Check the [PKO GitHub repository](https://github.com/pulumi/pulumi-kubernetes-operator) for known issues
- Visit the [ArgoCD documentation](https://argo-cd.readthedocs.io/) for ArgoCD-specific guidance
- Join the [Pulumi Community Slack](https://slack.pulumi.com/) for community support

## Example: GitOps workflow

Here's a example that demonstrates a typical GitOps workflow/directory strucvture using ArgoCD and PKO:

1. **Infrastructure repository** (`infrastructure/`): Contains Pulumi programs for creating cloud resources
2. **Application repository** (`applications/`): Contains Pulumi programs for deploying applications
3. **GitOps repository** (`gitops/`): Contains Kubernetes manifests for ArgoCD Applications and Pulumi Stacks

```bash
# Repository structure
gitops-repo/
├── clusters/
│   ├── dev/
│   │   ├── infrastructure.yaml      # Stack for dev cluster creation
│   │   └── applications.yaml        # Stack for dev applications
│   └── prod/
│       ├── infrastructure.yaml      # Stack for prod cluster creation
│       └── applications.yaml        # Stack for prod applications
└── argocd/
    ├── dev-app.yaml                 # ArgoCD App for dev environment
    └── prod-app.yaml                # ArgoCD App for prod environment
```

This separation allows different teams to manage different aspects:

- **Platform team**: Manages infrastructure Pulumi programs and cluster creation
- **Application teams**: Manage application Pulumi programs and deployments
- **Operations team**: Manages GitOps repository and ArgoCD configuration

The result is a powerful, scalable GitOps workflow that combines the best of ArgoCD's orchestration capabilities with Pulumi's infrastructure provisioning power.
