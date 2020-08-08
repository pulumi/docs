---
title: Kubernetes with Pulumi
layout: kubernetes
url: /kubernetes

meta_desc: Pulumi provides a cloud native programming model for Kubernetes deployments and orchestration. Any code, any cloud, any app.

hero:
    title: Kubernetes Superpowers
    body: >
        Pulumi is the modern platform to manage all of your cloud native infrastructure using familiar engineering tools and workflows. Avoid complex YAML by using your favorite programming languages and automate your deployments to Amazon EKS, Azure AKS, Google GKE, DigitalOcean DOKS, multi-cloud, hybrid and on-premises clusters with leading ecosystem integrations.

video_section:
  title: Pulumi In Action
  subtitle: Watch how easy it is to setup Amazon EKS in 5 minutes with Pulumi
  youtube_video_id: yA40w1ryMu8
  video_title: Get Started with Amazon EKS in 5 Minutes

kubernetes_overview:
    title: Cloud Native Engineering with Pulumi
    description: |
        Pulumi streamlines Kubernetes cluster configuration, management, and app workload deployments to your clusters.

        With Pulumi you can:
    ide:
        tabs:
            - title: index.ts
              language: typescript
              code: |
                import * as pulumi from "@pulumi/pulumi";
                import * as kubernetes from "@pulumi/kubernetes";

                // Create a namespace.
                const devNamespace = new kubernetes.core.v1.Namespace("devNamespace", {
                    apiVersion: "v1",
                    kind: "Namespace",
                    metadata: {
                        name: "dev",
                    },
                });

                // Deploy the nginx-ingress Helm chart into the created namespace.
                const nginxIngress = new kubernetes.helm.v3.Chart("nginx-ingress", {
                    chart: "nginx-ingress",
                    namespace: devNamespace.metadata.name,
                    fetchOpts:{
                        repo: "https://kubernetes-charts.storage.googleapis.com/",
                    },
                });
            - title: __main__.py
              language: python
              code: |
                import pulumi_kubernetes as kubernetes

                # Create a namespace.
                dev_namespace = kubernetes.core.v1.Namespace(
                    "devNamespace",
                    api_version="v1",
                    kind="Namespace",
                    metadata={
                        "name": "dev",
                    })

                # Deploy the nginx-ingress Helm chart into the created namespace.
                nginx_ingress = kubernetes.helm.v3.Chart(
                    "nginx-ingress",
                    kubernetes.helm.v3.ChartOpts(
                        chart="nginx-ingress",
                        namespace=dev_namespace.metadata["name"],
                        fetch_opts=kubernetes.helm.v3.FetchOpts(
                            repo="https://kubernetes-charts.storage.googleapis.com/",
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

                            // Create a namespace.
                            ns, err := corev1.NewNamespace(ctx, "devNamespace", &corev1.NamespaceArgs{
                                ApiVersion: pulumi.String("v1"),
                                Kind:       pulumi.String("Namespace"),
                                Metadata: &metav1.ObjectMetaArgs{
                                    Name: pulumi.String("dev"),
                                },
                            })
                            if err != nil {
                                return err
                            }

                            // Deploy the nginx-ingress Helm chart into the created namespace.
                            _, err = helm.NewChart(ctx, "nginx-ingress", helm.ChartArgs{
                                Chart: pulumi.String("nginx-ingress"),
                                Namespace: ns.Metadata.ApplyT(func(metadata interface{}) string {
                                    return *metadata.(*metav1.ObjectMeta).Name
                                }).(pulumi.StringOutput),
                                FetchArgs: helm.FetchArgs{
                                    Repo: pulumi.String("https://kubernetes-charts.storage.googleapis.com/"),
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
                        // Create a namespace.
                        var devNamespace = new Kubernetes.Core.V1.Namespace("devNamespace", new Kubernetes.Types.Inputs.Core.V1.NamespaceArgs
                        {
                            ApiVersion = "v1",
                            Kind = "Namespace",
                            Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
                            {
                                Name = "dev",
                            },
                        });

                        // Deploy the nginx-ingress Helm chart into the created namespace.
                        var nginx = new Kubernetes.Helm.V3.Chart("nginx-ingress", new Kubernetes.Helm.ChartArgs
                        {
                            Chart = "nginx-ingress",
                            Namespace = devNamespace.Metadata.Apply(x => x.Name),
                            FetchOptions = new Kubernetes.Helm.ChartFetchArgs
                            {
                                Repo = "https://kubernetes-charts.storage.googleapis.com/"
                            },
                        });
                    }
                }
    list:
        - Provision Kubernetes clusters on all major cloud providers.
        - Increase productivity using the full ecosystem of dev tools such as IDE auto-completion, type & error checking, linting, refactoring, and test frameworks to validate Kubernetes clusters, app workloads, or both.
        - Automate deployments with CI/CD integrations for [Spinnaker](https://www.pulumi.com/blog/unlocking-spinnaker-with-pulumi/), [Octopus](https://www.pulumi.com/blog/deploying-with-octopus-and-pulumi/), [GitHub Actions](https://www.pulumi.com/blog/continuous-delivery-to-any-cloud-using-github-actions-and-pulumi/), [GitLab](https://www.pulumi.com/blog/continuous-delivery-with-gitlab-and-pulumi-on-amazon-eks/), [Azure DevOps](https://www.pulumi.com/blog/cd-made-easy-with-pulumi-and-azure-pipelines/) and [more](https://www.pulumi.com/docs/guides/continuous-delivery/).
        - Seamlessly manage cloud resources with the Pulumi Kubernetes Operator.

    cta: REQUEST MORE INFORMATION

superpowers:
    - title: Run On Any Cloud
      cta: Learn more
      cta_url: "/docs/get-started"
      icon_type: cloud
      description: |
        With support for all public clouds and dozens of popular infrastructure service
        providers including private and hybrid clouds, Pulumi gives you the flexibility
        to run your clusters and workloads where you want to.

    - title: Reduce Provisioning Time
      cta: Learn more
      cta_url: "/docs/get-started"
      icon_type: provisioning
      description: |
        With Pulumi you are able to take advantage of the features of programming
        languages, helping you reduce boilerplate code and ultimately ship applications
        and infrastructure faster with greater consistency.

    - title: Automate Delivery
      cta: Learn more
      cta_url: "/docs/get-started"
      icon_type: delivery
      description: |
        You can integrate Pulumi directly with your favorite CI/CD and SCM systems to
        continuously deliver apps and infrastructure. Improve the velocity and visibility
        into your deployments from simple to complex global environments.

    - title: Smart Architecture
      cta: Learn more
      cta_url: "/docs/get-started"
      icon_type: architecture
      description: |
        YAML and templated DSLs force you to write the same boilerplate code over and over. Using
        Pulumi allows you to codify those patterns and best practices so you can stop reinventing
        the wheel and start inventing the platforms of the future.

    - title: Be Proactive, Not Reactive
      cta: Learn more
      cta_url: "/docs/get-started"
      icon_type: policy
      description: |
        When you enable Pulumi's Policy as Code feature, you instantly gain the power to prevent
        mistakes from being deployed. Enforce security, compliance, cost controls, and best
        practices using policies defined in real languages.

    - title: Reduce Deployment Anxiety
      cta: Learn more
      cta_url: "/docs/get-started"
      icon_type: testing
      description: |
        Deploying untested code can lead to some unexpected results. Pulumi lets you take advantage
        of common tools, frameworks, and techniques to unit, integration, and property test your
        infrastructure. Ensure your infrastructure is correct before and after deployment.

detail_sections:
    - title: Continue using the tools you love
      description: |
        Pulumi has first-class support for the Kubernetes tools you might already be working with such as
        Helm, Kustomize, YAML, Secret Managers, Open Policy Agent (OPA) and Custom Resource Definitions (CRDs).
      cta: Learn More
      cta_url: "/"
      items:
          - title: First Class Support
            description: Easily make the best use of existing tools such as Helm, and reduce the friction caused by multiple deployment tools and models across complex architectures.
            icon: fa-tools

          - title: Efficient Adoption
            description: There’s no need to rewrite your existing configurations to get started with Pulumi. You can efficiently adopt existing resources to deploy your application to save time and effort.
            icon: fa-book

          - title: Secrets Management
            description: Use Pulumi to ensure secret data is encrypted in transit, at rest, and physically anywhere it gets stored. Bring your own preferred cloud encryption provider or use Pulumi's native secrets provider.
            icon: fa-key

          - title: A Unified Toolchain
            description: Use Pulumi to organize all your tools in one place and give you the flexibility to build sophisticated, cloud native stacks in one unified toolchain.
            icon: fa-people-carry

    - title: Kubernetes Best Practices with Pulumi Crosswalk
      description: |
        Create, deploy, and manage production-ready infrastructure leveraging hosted Kubernetes offerings such as Amazon Elastic Kubernetes Service (EKS), Azure Kubernetes Service (AKS), or Google Kubernetes Engine (GKE).
      cta: Learn More
      cta_url: "/docs/guides/crosswalk/kubernetes"
      items:
          - title: Day 2 and Beyond
            description: By using Pulumi Crosswalk, you can benefit from tried-and-true “Day Two and beyond” integrations and playbooks, improving your infrastructure security, manageability, and cost effectiveness.
            icon: fa-sun

          - title: Accessible Kubernetes
            description: Through Pulumi's Crosswalk library extensions, the authorship experience has improved to make the API more accessible and approachable to operators and developers of all backgrounds.
            icon: fa-users

          - title: Focus on Delivering Value
            description: With Pulumi you'll focus more on functionality and business logic, and less on YAML formatting or learning bespoke domain-specific languages (DSLs).
            icon: fa-chalkboard-teacher

          - title: Avoid Pitfalls
            description: Discover solutions to the hardest Kubernetes problems to avoid mitigating pitfalls around infrastructure, security, governance, reliability, and maintainability of the cluster, it’s workloads, and underlying resources.
            icon: fa-pager

contact_us_form:
    section_id: contact
    hubspot_form_id: 212ce93d-e081-4998-b14b-f26a974da4fb
    headline: Want a demo?
    quote:
        title: See why the world’s best engineering teams use Pulumi to enable true collaboration between developers and operators.
        name: Fernando Carletti
        name_title: Head of DevOps, Credijusto
        content: |
            Pulumi enables our teams to deploy, scale and manage Kubernetes clusters in a fraction of the time that it took them previously, by giving them the ability to work with the languages they already know, bypassing YAML and unwieldy DSLs. It helps bring together application and infrastructure developers by eliminating silos and reducing friction in their workflows and interactions. We're excited that Pulumi Crosswalk for Kubernetes will simplify our infrastructure provisioning even further, advancing application lifecycle management throughout our organization.
---
