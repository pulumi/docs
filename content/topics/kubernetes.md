---
title: Kubernetes with Pulumi
layout: product-page
type: page
url: /kubernetes

meta_desc: Pulumi provides a single infrastructure as code workflow for Kubernetes and underlying infrastructure, using general-purpose languages and YAML.

aliases:
  - /cloudnative

sections:
  - type: hero
    layout: split
    title: Kubernetes superpowers
    description: |
      Pulumi empowers organizations to automate Kubernetes applications, clusters, and entire cloud environments through code, tame secrets sprawl through centralized secrets management, and manage cloud assets and compliance with the help of AI. Pulumi encourages infrastructure, platform, development, DevOps, and security teams to collaborate and accelerates time to market with greater control and minimized risk.
    cta_primary_text: Get started
    cta_primary_link: /docs/iac/get-started/kubernetes/
    cta_secondary_text: Request a demo
    cta_secondary_link: /contact/?form=request-a-demo
    video_youtube_id: 2P8JLgAc5QI
    video_title: Watch how easy it is to set up Amazon Elastic Kubernetes Service (EKS) in 5 minutes with Pulumi.
    anchor: hero

  - type: logo_banner
    text: Powering top engineering teams
    logos:
      - src: /logos/customers/snowflake-logo.svg
        alt: Snowflake
      - src: /logos/customers/mercedes-benz-RDNA_logo.png
        alt: Mercedes-Benz Research and Development
      - src: /logos/customers/mindbody_logo.svg
        alt: MindBody
      - src: /logos/customers/nih.png
        alt: National Institutes of Health
      - src: /logos/customers/sourcegraph-logo.svg
        alt: Sourcegraph
      - src: /logos/customers/lemonade.svg
        alt: Lemonade
      - src: /logos/customers/bmw.svg
        alt: BMW Group
      - src: /logos/customers/unity.png
        alt: Unity
      - src: /logos/customers/starburst.png
        alt: Starburst
    anchor: customers

  - type: section_header_with_image
    flip: true
    title: Cloud native engineering with Pulumi
    description: |
      Pulumi Infrastructure as Code (IaC) streamlines Kubernetes cluster configuration, management, and app workload deployments to your clusters.

      With Pulumi for Kubernetes you can:

      - Manage Kubernetes clusters on all major cloud providers.
      - Increase productivity using the full ecosystem of dev tools such as IDE auto-completion, type & error checking, linting, refactoring, and test frameworks to validate Kubernetes clusters, app workloads, or both.
      - Automate Kubernetes deployments with CI/CD integrations for [Flux](/blog/pulumi-kubernetes-new-2022/#integration-with-flux-sources), [Spinnaker](/blog/unlocking-spinnaker-with-pulumi/), [Octopus](/blog/deploying-with-octopus-and-pulumi/), [GitHub Actions](/blog/continuous-delivery-to-any-cloud-using-github-actions-and-pulumi/), [GitLab](/blog/continuous-delivery-with-gitlab-and-pulumi-on-amazon-eks/), [Azure DevOps](/blog/cd-made-easy-with-pulumi-and-azure-pipelines/) and [more](/docs/iac/using-pulumi/continuous-delivery/).
      - Seamlessly manage both Kubernetes and cloud resources using GitOps with the [Pulumi Kubernetes Operator](/docs/iac/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/), including [ArgoCD integration](/docs/iac/using-pulumi/continuous-delivery/argocd/).
      - Use Kubernetes [Server-Side Apply](/registry/packages/kubernetes/how-to-guides/managing-resources-with-server-side-apply/) to safely manage shared Kubernetes resources with Pulumi and your existing controllers.
    image: /images/topics/kubernetes/k8s-diagram.png
    image_alt: Kubernetes architecture diagram
    cta_text: Learn more
    cta_link: /blog/new-kubernetes-superpowers
    anchor: overview

  - type: section_header_with_code
    title: Infrastructure as code for Kubernetes
    description: |
      Define your Kubernetes resources using the programming languages you know and love. With Pulumi's SDK, you can manage both your cloud infrastructure and Kubernetes workloads with the same tools.
    code_title: index.ts
    code_snippets:
      - language: typescript
        label: TypeScript
        title: index.ts
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
      - language: python
        label: Python
        title: __main__.py
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
      - language: go
        label: Go
        title: main.go
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
                  ns, err := corev1.NewNamespace(ctx, "devNamespace", &corev1.NamespaceArgs{
                      Metadata: &metav1.ObjectMetaArgs{
                          Name: pulumi.String("dev"),
                      },
                  })
                  if err != nil {
                      return err
                  }

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
      - language: csharp
        label: C#
        title: MyStack.cs
        code: |
          using Pulumi;
          using Kubernetes = Pulumi.Kubernetes;

          class MyStack : Stack
          {
              public MyStack()
              {
                  var devNamespace = new Kubernetes.Core.V1.Namespace("devNamespace", new Kubernetes.Types.Inputs.Core.V1.NamespaceArgs
                  {
                      Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
                      {
                          Name = "dev",
                      },
                  });

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
      - language: yaml
        label: YAML
        title: Pulumi.yaml
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
    cards:
      - icon: cloud
        title: Run on any cloud
        description: Support for all clouds including Amazon Elastic Kubernetes Service (EKS), Azure Kubernetes Service (AKS), Google Kubernetes Engine (GKE), DigitalOcean Kubernetes (DOKS), and more, with hundreds of integrations with popular infrastructure service providers.
      - icon: graph
        title: Intelligent cloud management
        description: Gain security, compliance, and cost insights into the entirety of an organization's Kubernetes applications and cloud assets and automatically remediate issues through AI-powered workflows.
      - icon: package
        title: Automate delivery
        description: You can integrate Pulumi directly with your favorite CI/CD systems and testing frameworks to continuously deliver Kubernetes infrastructure and applications. Improve the velocity and visibility into your deployments from simple to complex global environments.
      - icon: shapes
        title: Smart architecture
        description: YAML and templated DSLs force you to write the same boilerplate code over and over. Pulumi's Kubernetes library allows you to codify those patterns and best practices so you can stop reinventing the wheel and start inventing the platforms of the future.
      - icon: shield-check
        title: Be proactive, not reactive
        description: When you enable Pulumi's Policy as Code feature, you instantly gain the power to prevent mistakes from being deployed. Enforce security, compliance, cost controls, and best practices using policies defined in modern languages.
      - icon: lock
        title: Centralize secrets
        description: "[Pulumi ESC](/product/secrets-management/) is integrated with External Secrets Operator (ESO), enabling the passing of secrets from ESC directly as environment variables of applications running in Kubernetes."
    anchor: code-example

  - type: section_header
    title: Continue using the tools you love
    description: |
      Pulumi has first-class support for popular Kubernetes tools, such as Helm, Kustomize, YAML, Secret Managers, Open Policy Agent (OPA), Custom Resource Definitions (CRDs), and Server-Side Apply (SSA).
    cta_text: Learn more
    cta_link: /blog/kubecon-na-2024-roundup/
    cards_cols: 2
    cards:
      - icon: cloud
        title: Everything in one place
        description: Easily make the best use of existing Kubernetes tools such as Helm, and reduce the friction caused by multiple deployment tools and models across complex architectures.
      - icon: lightning
        title: Efficient adoption
        description: There's no need to rewrite your existing Kubernetes configurations to get started with Pulumi. You can efficiently adopt existing K8s resources to deploy your application to save time and effort.
      - icon: shield-check
        title: Secrets management
        description: Use Pulumi to ensure secret data is encrypted in transit, at rest, and physically anywhere it gets stored. Bring your own preferred cloud encryption provider or use Pulumi's native secrets provider.
      - icon: pen-nib
        title: Pulumi Kubernetes Operator
        description: Deploy both Kubernetes resources and cloud infrastructure from within the Kubernetes resource model using a GitOps workflow. Use Pulumi's Flux and ArgoCD integrations along with many other CI/CD integrations.
    anchor: tools

  - type: section_header
    title: AI-powered Kubernetes management
    description: |
      [Pulumi Copilot](/product/copilot/), an AI-powered assistant, makes discovering cost savings, running compliance checks, and debugging deployments across your Kubernetes resources as easy as typing a question.
    cta_text: Learn more
    cta_link: /product/copilot/
    cards_cols: 2
    cards:
      - icon: gauge
        title: Discover cost savings
        description: Pulumi Copilot can access infrastructure stack and resource data, so you can analyze the cost of your infrastructure and reclaim cloud waste.
      - icon: test-tube
        title: Run compliance checks
        description: Pulumi Copilot leverages knowledge about compliance frameworks to analyze your infrastructure and check for policy compliance.
      - icon: cloud
        title: Debug cloud failures
        description: Pulumi Copilot can access update and deployment logs of your stacks as well as access history, logs, and runtime metrics, so you can easily debug deployment and infrastructure failures.
      - icon: shield-check
        title: Stay secure
        description: Pulumi Copilot combines Pulumi's supergraph of your cloud infrastructure and knowledge about security best practices to identify security violations and detect anomalous activity.
    anchor: ai-management

  - type: two_column
    columns:
      - title: Need help with Kubernetes?
        description: Learn how top engineering teams are using Pulumi to manage Kubernetes clusters and workloads across every cloud.
        cta_primary_text: Request a demo
        cta_primary_link: /contact/?form=request-a-demo
      - title: Get started with Pulumi and Kubernetes
        description: Spin up your first cluster in minutes. Follow our quickstart guide, or talk to our team about your specific needs.
        cta_primary_text: Get started
        cta_primary_link: /docs/iac/get-started/kubernetes/
    anchor: get-started
    highlight_first_card: true
---
