---
title_tag: Install Helm Charts using the Chart resource
allow_long_title: true
title: Install Helm Charts using the Chart resource
layout: single
description: |
  Learn how to use the `Chart` resource from the Pulumi Kubernetes provider to install Helm charts on Kubernetes.
meta_desc: Using Pulumi to install Helm Charts on Kubernetes is a great way to manage to install third-party applications on your Kubernetes cluster.
meta_image: meta.png
weight: 999
summary: |
  This is the second part of the tutorial on how to install Helm on Kubernetes using Pulumi.

  In this tutorial, we will learn how to install a Helm chart on Kubernetes using the Pulumi Kubernetes provider and the `Chart` resource. In the first part, we used the `Release` resource to install a Helm chart on Kubernetes, here is the link to the first part: [How to Install Helm Charts on Kubernetes with Pulumi - Part 1](/tutorials/kubernetes-helm-part-one/).

  Most of the third-party applications that you want to install on your Kubernetes cluster, like whole monitoring stacks, databases, and other applications, are most likely available as Helm charts.

  On services like [Artifact Hub](https://artifacthub.io/), you can find a lot of Helm charts that you can use to install applications on your Kubernetes cluster.

  The Pulumi Kubernetes provider offers two different ways to install Helm on Kubernetes:

  - Using the `Release` resource
  - Using the `Chart` resource

  The Helm [Chart](/registry/packages/kubernetes/api-docs/helm/v3/chart) resource renders the templates from your chart and then manages the objects directly with the Pulumi Kubernetes provider. There was recently a new version of the `Chart` resource released, and in this [blog post](/blog/kubernetes-chart-v4/) you will learn more about the improvements.

  The Helm [Release](/registry/packages/kubernetes/api-docs/helm/v3/release) resource uses the Helm SDK to install the Helm chart on your Kubernetes cluster.
  
youll_learn:
- How to install Helm on Kubernetes using Pulumi

estimated_time: 10
collections_weight: 2
prereqs:
- "A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)"
- "The [Pulumi CLI](/docs/install/)"
- "A Kubernetes cluster (for example, [kind](https://kind.sigs.k8s.io/))"
- "[kubectl](https://kubernetes.io/releases/download/#kubectl)"
- "[helm](https://helm.sh/docs/intro/install/)"

collections:
- kubernetes
---

## Why using the `Chart` resource over the `Release` resource?

The [`Helm Chart`](/registry/packages/kubernetes/api-docs/helm/v4/chart) resource renders the templates from your chart and then manages the objects directly with the Pulumi Kubernetes provider. `Chart` is implemented as a [`Component Resource`](/docs/concepts/resources/components) which provide a number of benefits for Pulumi users:

### Benefits

1. Visibility into all resources encapsulated by the Chart in Pulumi's state, allowing users to directly query properties of individual resources.
2. Tight integration with Pulumi's Policy-as-Code framework - [`CrossGuard`](/docs/guides/crossguard/) to enforce policies on all resources installed by Helm charts
3. Ability to leverage [transformations](/docs/concepts/options/transformations/) to programmatically manipulate resources installed by Helm charts in any of the Pulumi supported programming languages
4. Detailed previews and diffs rendered in the Pulumi CLI and Console for each Kubernetes resource resulting from Helm Chart config changes

We have seen significant adoption of `Chart` over the years. However, since these resources are not directly managed by Helm, the following limitations apply:

### Limitations

1. No support for [Helm Chart Hooks](https://helm.sh/docs/topics/charts_hooks/) - i.e. equivalent of running `helm install` with the `--no-hooks` option
2. No ability to import existing Helm releases into Pulumi state
3. No interoperability using the Helm CLI on resources installed by Pulumi

## Deploying a Helm chart with `Chart` resource

To start, [login to the Pulumi CLI](/tutorials/cli-authentication/) and create a new Pulumi project. You can use the following command to create a new Pulumi project and select from the list of templates the `kubernetes-<your-programming-language>` template.

```bash
# Choose your favorite Pulumi supported language
pulumi new kubernetes-<your-programming-language>
```

This will create a new Pulumi project with the necessary files to deploy Kubernetes resources and some example resources. Copy the following code snippet into your `index.ts`, `index.py`, `index.go`, `Program.cs`, or `Pulumi.yaml` file.

{{< chooser language "typescript,python,go,csharp,yaml" />}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="helm-kubernetes-part-two" language="typescript" from="1" to="99" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="helm-kubernetes-part-two" language="python" from="1" to="99" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="helm-kubernetes-part-two" language="go" from="1" to="99" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="helm-kubernetes-part-two" language="csharp" from="1" to="99" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="helm-kubernetes-part-two" language="yaml" from="1" to="99" >}}
```

{{% /choosable %}}



## Deploying the Helm chart

Now run the `pulumi up` command to preview and deploy the resources you’ve just defined in your project.

```bash
Please choose a stack, or create a new one: dev
Previewing update (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/dirien/helm-kubernetes-part-two-typescript/dev/previews/e88dbf07-434c-453c-b49c-dba176957abc

     Type                                                                             Name                                                              Plan       
 +   pulumi:pulumi:Stack                                                              helm-kubernetes-part-two-typescript-dev                           create     
 +   └─ kubernetes:helm.sh/v4:Chart                                                   cert-manager                                                      create     
 +      ├─ kubernetes:core/v1:ServiceAccount                                          cert-manager:cert-manager/cert-manager-controller                 create     
 +      ├─ kubernetes:policy/v1:PodDisruptionBudget                                   cert-manager:cert-manager/cert-manager-cainjector                 create     
 +      ├─ kubernetes:core/v1:ServiceAccount                                          cert-manager:cert-manager/cert-manager-webhook                    create     
 +      ├─ kubernetes:core/v1:ServiceAccount                                          cert-manager:cert-manager/cert-manager-cainjector                 create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:Role                               cert-manager:kube-system/cert-manager-cainjector-leader-election  create     
 +      ├─ kubernetes:admissionregistration.k8s.io/v1:MutatingWebhookConfiguration    cert-manager:cert-manager/cert-manager-webhook                    create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-view                         create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:RoleBinding                        cert-manager:cert-manager/cert-manager-webhook-dynamic-serving    create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:RoleBinding                        cert-manager:kube-system/cert-manager-cainjector-leader-election  create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-certificates      create     
 +      ├─ kubernetes:core/v1:Service                                                 cert-manager:cert-manager/cert-manager-webhook                    create     
 +      ├─ kubernetes:networking.k8s.io/v1:NetworkPolicy                              cert-manager:cert-manager/cert-manager-controller                 create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-webhook-subjectaccessreviews            create     
 +      ├─ kubernetes:core/v1:Service                                                 cert-manager:cert-manager/cert-manager-controller-metrics         create     
 +      ├─ kubernetes:networking.k8s.io/v1:NetworkPolicy                              cert-manager:cert-manager/cert-manager-cainjector                 create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-orders            create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-challenges        create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-issuers           create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-edit                         create     
 +      ├─ kubernetes:networking.k8s.io/v1:NetworkPolicy                              cert-manager:cert-manager/cert-manager-webhook                    create     
 +      ├─ kubernetes:policy/v1:PodDisruptionBudget                                   cert-manager:cert-manager/cert-manager-controller                 create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-orders            create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-approve           create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-clusterissuers    create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-cainjector                              create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-ingress-shim      create     
 +      ├─ kubernetes:admissionregistration.k8s.io/v1:ValidatingWebhookConfiguration  cert-manager:cert-manager/cert-manager-webhook                    create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-webhook-subjectaccessreviews            create     
 +      ├─ kubernetes:policy/v1:PodDisruptionBudget                                   cert-manager:cert-manager/cert-manager-webhook                    create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:RoleBinding                        cert-manager:kube-system/cert-manager-controller-leader-election  create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:Role                               cert-manager:kube-system/cert-manager-controller-leader-election  create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-certificates      create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-challenges        create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-clusterissuers    create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-cainjector                              create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-ingress-shim      create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:Role                               cert-manager:cert-manager/cert-manager-webhook-dynamic-serving    create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-approve           create     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-issuers           create     
 +      ├─ kubernetes:apps/v1:Deployment                                              cert-manager:cert-manager/cert-manager-cainjector                 create     
 +      ├─ kubernetes:apps/v1:Deployment                                              cert-manager:cert-manager/cert-manager-webhook                    create     
 +      └─ kubernetes:apps/v1:Deployment                                              cert-manager:cert-manager/cert-manager-controller                 create     

Resources:
    + 44 to create

Do you want to perform this update? yes
Updating (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/dirien/helm-kubernetes-part-two-typescript/dev/updates/4

     Type                                                                             Name                                                              Status              
 +   pulumi:pulumi:Stack                                                              helm-kubernetes-part-two-typescript-dev                           created (37s)       
 +   ├─ kubernetes:core/v1:Namespace                                                  cert-manager                                                      created (0.23s)     
 +   └─ kubernetes:helm.sh/v4:Chart                                                   cert-manager                                                      created             
 +      ├─ kubernetes:admissionregistration.k8s.io/v1:MutatingWebhookConfiguration    cert-manager:cert-manager/cert-manager-webhook                    created (0.27s)     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:Role                               cert-manager:kube-system/cert-manager-controller-leader-election  created (0.49s)     
 +      ├─ kubernetes:core/v1:Service                                                 cert-manager:cert-manager/cert-manager-controller-metrics         created (11s)       
 +      ├─ kubernetes:core/v1:ServiceAccount                                          cert-manager:cert-manager/cert-manager-controller                 created (0.71s)     
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:RoleBinding                        cert-manager:kube-system/cert-manager-cainjector-leader-election  created (2s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-certificates      created (3s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-clusterissuers    created (4s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-ingress-shim      created (4s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-cainjector                              created (1s)        
 +      ├─ kubernetes:core/v1:ServiceAccount                                          cert-manager:cert-manager/cert-manager-webhook                    created (1s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:Role                               cert-manager:kube-system/cert-manager-cainjector-leader-election  created (1s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:Role                               cert-manager:cert-manager/cert-manager-webhook-dynamic-serving    created (2s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-challenges        created (3s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:RoleBinding                        cert-manager:kube-system/cert-manager-controller-leader-election  created (3s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-approve           created (4s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-approve           created (7s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-orders            created (6s)        
 +      ├─ kubernetes:core/v1:ServiceAccount                                          cert-manager:cert-manager/cert-manager-cainjector                 created (7s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-edit                         created (5s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-certificates      created (6s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-issuers           created (6s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-controller-controller-orders            created (5s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:RoleBinding                        cert-manager:cert-manager/cert-manager-webhook-dynamic-serving    created (7s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-clusterissuers    created (8s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-webhook-subjectaccessreviews            created (8s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-issuers           created (8s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-cainjector                              created (5s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-view                         created (9s)        
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-ingress-shim      created (7s)        
 +      ├─ kubernetes:policy/v1:PodDisruptionBudget                                   cert-manager:cert-manager/cert-manager-cainjector                 created (9s)        
 +      ├─ kubernetes:admissionregistration.k8s.io/v1:ValidatingWebhookConfiguration  cert-manager:cert-manager/cert-manager-webhook                    created (11s)       
 +      ├─ kubernetes:core/v1:Service                                                 cert-manager:cert-manager/cert-manager-webhook                    created (19s)       
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRoleBinding                 cert-manager:cert-manager-webhook-subjectaccessreviews            created (10s)       
 +      ├─ kubernetes:policy/v1:PodDisruptionBudget                                   cert-manager:cert-manager/cert-manager-webhook                    created (11s)       
 +      ├─ kubernetes:rbac.authorization.k8s.io/v1:ClusterRole                        cert-manager:cert-manager-controller-controller-challenges        created (10s)       
 +      ├─ kubernetes:networking.k8s.io/v1:NetworkPolicy                              cert-manager:cert-manager/cert-manager-cainjector                 created (12s)       
 +      ├─ kubernetes:policy/v1:PodDisruptionBudget                                   cert-manager:cert-manager/cert-manager-controller                 created (10s)       
 +      ├─ kubernetes:networking.k8s.io/v1:NetworkPolicy                              cert-manager:cert-manager/cert-manager-controller                 created (12s)       
 +      ├─ kubernetes:apps/v1:Deployment                                              cert-manager:cert-manager/cert-manager-cainjector                 created (17s)       
 +      ├─ kubernetes:networking.k8s.io/v1:NetworkPolicy                              cert-manager:cert-manager/cert-manager-webhook                    created (13s)       
 +      ├─ kubernetes:apps/v1:Deployment                                              cert-manager:cert-manager/cert-manager-webhook                    created (19s)       
 +      └─ kubernetes:apps/v1:Deployment                                              cert-manager:cert-manager/cert-manager-controller                 created (19s)       

Resources:
    + 45 created

Duration: 39s
```

As you can see, the Pulumi CLI shows all the resources that will be created in your Kubernetes cluster. This is due to the `Chart` resource that renders the templates from the Helm chart and then manages the objects directly with the Pulumi Kubernetes provider.

With following command you can check the resources created by the Helm chart where also successful annotated with the `cost-center` label.

```bash
 kubectl get svc -n cert-manager -o jsonpath="{..metadata.annotations}" | tr ' ' '\n' | sort | uniq 

```

And you should see the resources that were created by the Helm chart.

```bash                                                       READY   STATUS    RESTARTS   AGE
{"cost-center":"12345"}
```

## Housekeeping

Before moving on, tear down the resources that are part of your stack to avoid incurring any charges.

1. Run `pulumi destroy` to tear down all resources. You'll be prompted to make sure you really want to delete these resources. A destroy operation may take some time, since Pulumi waits for the resources to finish shutting down before it considers the destroy operation to be complete.
2. To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Service.

## Next steps

In this tutorial, you learned how to install Helm on Kubernetes using the Kubernetes provider from Pulumi and the `Release` resource.

- Learn more about Pulumi and Kubernetes in the [Kubernetes documentation](/docs/iac/clouds/kubernetes/).
- Learn more about the `Chart` resource in the [Pulumi Kubernetes API documentation](/registry/packages/kubernetes/api-docs/helm/v4/chart/).
- Try the out the `Release` [tutorial](/tutorials/kubernetes-helm-part-one) to learn how to install Helm charts on Kubernetes using the `Release` resource.
- Or give the tutorial about [Creating Resources on Kubernetes](/tutorials/creating-resources-kubernetes/) a try.
