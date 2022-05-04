---
title: Kubernetes with Pulumi
layout: kubernetes
url: /kubernetes

meta_desc: Pulumi provides a cloud native programming model for Kubernetes deployments and orchestration. Any code, any cloud, any app.

aliases:
  - /cloudnative

hero:
    title: Kubernetes Superpowers
    body: >
        Pulumi is the modern platform to manage all of your cloud native infrastructure using
        familiar engineering tools and workflows. Avoid complex YAML, JSON, and DSLs by using
        your favorite programming languages and automate deployments to AWS, Azure, GCP,
        multi-cloud, hybrid and on-premises clusters.
    cta_text: See what's new

video_section:
  title: Pulumi In Action
  subtitle: Watch how easy it is to set up Amazon Elastic Kubernetes Service (EKS) in 5 minutes with Pulumi.
  youtube_video_id: yA40w1ryMu8
  video_title: Watch how easy it is to setup Amazon Elastic Kubernetes Service (EKS) in 5 minutes with Pulumi.

kubernetes_overview:
    title: Cloud Native Engineering with Pulumi
    description: |
        Pulumi streamlines Kubernetes cluster configuration, management, and app workload deployments to your clusters.

        With Pulumi for Kubernetes you can:
    ide:
        tabs:
            - title: index.ts
              language: typescript
              code: |
                import * as pulumi from "@pulumi/pulumi";
                import * as kubernetes from "@pulumi/kubernetes";

                // Create a K8s namespace.
                const devNamespace = new kubernetes.core.v1.Namespace("devNamespace", {
                    metadata: {
                        name: "dev",
                    },
                });

                // Deploy the K8s nginx-ingress Helm chart into the created namespace.
                const nginxIngress = new kubernetes.helm.v3.Chart("nginx-ingress", {
                    chart: "nginx-ingress",
                    namespace: devNamespace.metadata.name,
                    fetchOpts:{
                        repo: "https://charts.helm.sh/stable/",
                    },
                });
            - title: __main__.py
              language: python
              code: |
                import pulumi_kubernetes as kubernetes

                # Create a K8s namespace.
                dev_namespace = kubernetes.core.v1.Namespace(
                    "devNamespace",
                    metadata={
                        "name": "dev",
                    })

                # Deploy the K8s nginx-ingress Helm chart into the created namespace.
                nginx_ingress = kubernetes.helm.v3.Chart(
                    "nginx-ingress",
                    kubernetes.helm.v3.ChartOpts(
                        chart="nginx-ingress",
                        namespace=dev_namespace.metadata["name"],
                        fetch_opts=kubernetes.helm.v3.FetchOpts(
                            repo="https://charts.helm.sh/stable/",
                        ),
                    ),
                )
            - title: main.go
              language: go
              code: |
                    package main

                    import (
                        corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/core/v1"
                        "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/helm/v3"
                        metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/meta/v1"
                        "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
                    )

                    func main() {
                        pulumi.Run(func(ctx *pulumi.Context) error {

                            // Create a K8s namespace.
                            ns, err := corev1.NewNamespace(ctx, "devNamespace", &corev1.NamespaceArgs{
                                Metadata: &metav1.ObjectMetaArgs{
                                    Name: pulumi.String("dev"),
                                },
                            })
                            if err != nil {
                                return err
                            }

                            // Deploy the K8s nginx-ingress Helm chart into the created namespace.
                            _, err = helm.NewChart(ctx, "nginx-ingress", helm.ChartArgs{
                                Chart: pulumi.String("nginx-ingress"),
                                Namespace: ns.Metadata.ApplyT(func(metadata interface{}) string {
                                    return *metadata.(*metav1.ObjectMeta).Name
                                }).(pulumi.StringOutput),
                                FetchArgs: helm.FetchArgs{
                                    Repo: pulumi.String("https://charts.helm.sh/stable/"),
                                },
                            })
                            if err != nil {
                                return err
                            }

                            return nil
                        })
                    }
            - title: MyStack.cs
              language: csharp
              code: |
                using Pulumi;
                using Kubernetes = Pulumi.Kubernetes;

                class MyStack : Stack
                {
                    public MyStack()
                    {
                        // Create a K8s namespace.
                        var devNamespace = new Kubernetes.Core.V1.Namespace("devNamespace", new Kubernetes.Types.Inputs.Core.V1.NamespaceArgs
                        {
                            Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
                            {
                                Name = "dev",
                            },
                        });

                        // Deploy the K8s nginx-ingress Helm chart into the created namespace.
                        var nginx = new Kubernetes.Helm.V3.Chart("nginx-ingress", new Kubernetes.Helm.ChartArgs
                        {
                            Chart = "nginx-ingress",
                            Namespace = devNamespace.Metadata.Apply(x => x.Name),
                            FetchOptions = new Kubernetes.Helm.ChartFetchArgs
                            {
                                Repo = "https://charts.helm.sh/stable/"
                            },
                        });
                    }
                }
            - title: Main.java
              language: java
              code: |
                package com.pulumi.example.infra;

                import com.pulumi.Context;
                import com.pulumi.Exports;
                import com.pulumi.Pulumi;
                import com.pulumi.kubernetes.core_v1.Namespace;
                import com.pulumi.kubernetes.core_v1.NamespaceArgs;
                import com.pulumi.kubernetes.meta_v1.inputs.ObjectMetaArgs;
                import com.pulumi.kubernetes.helm.sh_v3.Release;
                import com.pulumi.kubernetes.helm.sh_v3.ReleaseArgs;
                import com.pulumi.kubernetes.helm.sh_v3.inputs.RepositoryOptsArgs;

                public class Main {

                    public static void main(String[] args) {
                        Pulumi.run(Main::stack);
                    }

                    private static Exports stack(Context ctx) {
                        var devNamespace = new Namespace("devNamespace", NamespaceArgs.builder()
                                  .metadata(ObjectMetaArgs.builder()
                                            .name("dev")
                                            .build())
                                  .build());

                        var nginxIngress = new Release("nginx-ingress", ReleaseArgs.builder()
                                  .chart("nginx-ingress)
                                  .namespace(devNamespace.metadata.name)
                                  .repositoryOpts(RepositoryOptsArgs.builder()
                                            .repo("https://charts.helm.sh/stable/")
                                            .build())
                                  .build());

                        return ctx.exports();
                    }
                }

            - title: Pulumi.yaml
              language: yaml
              code: |
                name: simple-kubernetes
                runtime: yaml
                resources:
                  devNamespace:
                    type: kubernetes:core:Namespace
                    properties:
                      metadata:
                        name: "dev"
                  nginxIngress:
                    type: kubernetes:helm.sh:Chart
                    properties:
                      chart: "nginx-ingress"
                      namespace: ${devNamespace.metadata.name}
                      fetchOpts:
                          repo: "https://charts.helm.sh/stable/"

    list:
        - Manage Kubernetes clusters on all major cloud providers.
        - Increase productivity using the full ecosystem of dev tools such as IDE auto-completion, type & error checking, linting, refactoring, and test frameworks to validate Kubernetes clusters, app workloads, or both.
        - Automate Kubernetes deployments with CI/CD integrations for [Spinnaker](/blog/unlocking-spinnaker-with-pulumi/), [Octopus](/blog/deploying-with-octopus-and-pulumi/), [GitHub Actions](/blog/continuous-delivery-to-any-cloud-using-github-actions-and-pulumi/), [GitLab](/blog/continuous-delivery-with-gitlab-and-pulumi-on-amazon-eks/), [Azure DevOps](/blog/cd-made-easy-with-pulumi-and-azure-pipelines/) and [more](/docs/guides/continuous-delivery/).
        - Seamlessly manage cloud resources with the [Pulumi Kubernetes Operator](/docs/guides/continuous-delivery/pulumi-kubernetes-operator/).
    cta: Learn More
    cta_url: "/blog/new-kubernetes-superpowers"

superpowers:
    - title: Run On Any Cloud
      cta: Learn more
      cta_url: "/docs/get-started/kubernetes"
      icon_type: cloud
      description: |
        Support for all clouds including Amazon Elastic Kubernetes Service (EKS), Azure
        Kubernetes Service (AKS), Google Kubernetes Engine (GKE), DigitalOcean Kubernetes
        (DOKS), and more, with dozens of integrations with popular infrastructure service
        providers.

    - title: Reduce Provisioning Time
      cta: Learn more
      cta_url: "/docs/get-started/kubernetes"
      icon_type: provisioning
      description: |
        With Pulumi you are able to take advantage of the features of programming languages,
        helping you reduce boilerplate code and ultimately ship Kubernetes infrastructure and
        applications faster with greater consistency.

    - title: Automate Delivery
      cta: Learn more
      cta_url: "/docs/guides/continuous-delivery"
      icon_type: delivery
      description: |
        You can integrate Pulumi directly with your favorite CI/CD and SCM systems to
        continuously deliver Kubernetes infrastructure and applications. Improve the velocity
        and visibility into your deployments from simple to complex global environments.

    - title: Smart Architecture
      cta: Learn more
      cta_url: "/docs/intro/concepts"
      icon_type: architecture
      description: |
        YAML and templated DSLs force you to write the same boilerplate code over and over.
        Pulumi’s Kubernetes library allows you to codify those patterns and best practices so
        you can stop reinventing the wheel and start inventing the platforms of the future.

    - title: Be Proactive, Not Reactive
      cta: Learn more
      cta_url: "/docs/guides/crossguard"
      icon_type: policy
      description: |
        When you enable Pulumi's Policy as Code feature, you instantly gain the power to
        prevent mistakes from being deployed. Enforce security, compliance, cost controls,
        and best practices using policies defined in modern languages.

    - title: Reduce Deployment Complexity
      cta: Learn more
      cta_url: "/docs/guides/testing"
      icon_type: testing
      description: |
        Deploying untested code can lead to some unexpected results. Pulumi lets you take advantage
        of common tools, frameworks, and techniques to unit, integration, and property test your
        Kubernetes infrastructure. Ensure your infrastructure is correct before and after deployment.

detail_sections:
    - title: Continue using the tools you love
      description: |
        Pulumi has first-class support for popular Kubernetes tools, such as Helm, Kustomize,
        YAML, Secret Managers, Open Policy Agent (OPA) and Custom Resource Definitions (CRDs).
      cta: Learn More
      cta_url: "/blog/new-kubernetes-superpowers"
      items:
          - title: Everything In One Place
            icon: cloud-with-nodes
            icon_color: violet
            description: Easily make the best use of existing Kubernetes tools such as Helm, and reduce the friction caused by multiple deployment tools and models across complex architectures.

          - title: Efficient Adoption
            icon: lightning
            icon_color: yellow
            description: There’s no need to rewrite your existing Kubernetes configurations to get started with Pulumi. You can efficiently adopt existing K8s resources to deploy your application to save time and effort.

          - title: Secrets Management
            icon: security
            icon_color: salmon
            description: Use Pulumi to ensure secret data is encrypted in transit, at rest, and physically anywhere it gets stored. Bring your own preferred cloud encryption provider or use Pulumi's native secrets provider.

          - title: Pulumi Kubernetes Operator
            icon: pen
            icon_color: fuchsia
            description: The Pulumi Kubernetes Operator gives you a Kubernetes controller that deploys cloud infrastructure for you and your team.

    - title: Kubernetes Best Practices with Pulumi Crosswalk
      description: |
        Create, deploy, and manage production-ready infrastructure leveraging hosted Kubernetes offerings such as Amazon Elastic Kubernetes Service (EKS), Azure Kubernetes Service (AKS), or Google Kubernetes Engine (GKE).
      cta: Learn More
      cta_url: "/docs/guides/crosswalk/kubernetes"
      items:
          - title: Day 2 and Beyond
            icon: cycle
            icon_color: blue
            description: By using Pulumi Crosswalk for Kubernetes, you can benefit from tried-and-true “Day Two and beyond” integrations and playbooks, improving your infrastructure security, manageability, and cost effectiveness.

          - title: Accessible Kubernetes
            icon: collab
            icon_color: purple
            description: Through Pulumi's Crosswalk for Kubernetes library extensions, the authorship experience has improved to make the Kubernetes API more accessible and approachable to operators and developers of all backgrounds.

          - title: Focus on Delivering Value
            icon: nodes
            icon_color: salmon
            description: With Pulumi you'll focus more on functionality and business logic of your Kubernetes infrastructure and applications, and less on low-level implementation details.

          - title: Avoid Pitfalls
            icon: code
            icon_color: yellow
            description: Discover solutions to the hardest Kubernetes problems to avoid mitigating pitfalls around infrastructure, security, governance, reliability, and maintainability of the K8s cluster, its workloads, and underlying resources.

contact_us_form:
    section_id: contact
    hubspot_form_id: 30017141-1093-4b94-b0eb-20aabc08447b
    headline: Want a demo?
    quote:
        title: See why the world’s best engineering teams use Pulumi + Kubernetes to enable true collaboration between developers and operators.
        name: Fernando Carletti
        name_title: Head of DevOps, Credijusto
        content: |
            Pulumi enables our teams to deploy, scale and manage Kubernetes clusters in a fraction of the time that it took them previously, by giving them the ability to work with the languages they already know, bypassing YAML and unwieldy DSLs. It helps bring together application and infrastructure developers by eliminating silos and reducing friction in their workflows and interactions. We're excited that Pulumi Crosswalk for Kubernetes will simplify our infrastructure provisioning even further, advancing application lifecycle management throughout our organization.
---
