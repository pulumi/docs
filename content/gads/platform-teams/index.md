---
title: "Platform Engineering | Pulumi"
meta_desc: "Build internal developer platforms that let engineers provision infrastructure safely. Policies, guardrails, templates, and full auditability built in."
layout: gads-template
block_external_search_index: true

heading: "Platform engineering"
subheading: |
    Give developers self-service infrastructure inside the guardrails your platform team defines.
    Policies, templates, and audit trails are built in.

customer_quote:
    text: "Pulumi supercharged our infrastructure team by helping us create reusable building blocks that developers can leverage to provision new resources and enforce organizational policies for logging, permissions, resource tagging, and security."
    author: "Igor Shapiro"
    title: "Principal Engineer"
    company: "Lemonade"
    logo: lemonade
    link: /case-studies/lemonade

overview:
    title: Enable self-service infrastructure <br/>without scaling your platform team
    description: |
        Looking for <span id="dki-placeholder" style="font-weight: bold;">a platform engineering solution</span>? Build internal developer platforms that let engineers provision infrastructure safely, with policies, guardrails, and full auditability built in.

key_features_above:
    items:
        - title: "Empower developers with guardrails"
          sub_title: "Pulumi Infrastructure as Code Engine"
          description:
            Write policies in TypeScript, Python, or Go to define what teams can provision, then let them self-service within boundaries
          features:
              - title: Ship infrastructure with AI
                description: |
                    Pulumi Neo plans and executes infrastructure changes inside the guardrails you set. Claude Code, Cursor, and Codex work with Pulumi through the MCP server and Agent Skills.
                icon: lightning
              - title: Prove platform ROI with metrics
                description: |
                    Track adoption, cost, and compliance across every stack and environment with centralized visibility
                icon: monitor
              - title: Reduce ticket backlog
                description: |
                    Developers get infrastructure on-demand while platform engineers maintain control and governance
                icon: security

key_features:
    items:
        - title: "Build infrastructure faster with reusable components"
          sub_title: "Pulumi Packages"
          description: |
            Build and reuse higher-level abstractions for cloud architectures with multi-language Pulumi Packages. Distribute the packages through repositories or package managers so your team members can reuse them.
          ide:
            - title: index.ts
              language: typescript
              code: |
                import * as eks from "@pulumi/eks";

                // Create an EKS cluster with the default configuration.
                const cluster = new eks.Cluster("eks-cluster");

                // Export the cluster's kubeconfig.
                export const kubeconfig = cluster.kubeconfig;
            - title: __main__.py
              language: python
              code: |
                import pulumi
                import pulumi_eks as eks

                # Create an EKS cluster with the default configuration.
                cluster = eks.Cluster("eks-cluster")

                # Export the cluster's kubeconfig.
                pulumi.export("kubeconfig", cluster.kubeconfig)
            - title: main.go
              language: go
              code: |
                    package main

                    import (
                      "github.com/pulumi/pulumi-eks/sdk/go/eks"
                      "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
                    )

                    func main() {
                      pulumi.Run(func(ctx *pulumi.Context) error {
                        // Create an EKS cluster with default settings.
                        cluster, err := eks.NewCluster(ctx, "eks-cluster", nil)
                        if err != nil {
                          return err
                        }

                        // Export the cluster's kubeconfig.
                        ctx.Export("kubeconfig", cluster.Kubeconfig)
                        return nil
                      })
                    }
            - title: MyStack.cs
              language: csharp
              code: |
                using System.Collections.Generic;
                using Pulumi;
                using Pulumi.Eks;

                await Deployment.RunAsync(() =>
                {
                  // Create an EKS cluster with default settings.
                  var cluster = new Cluster("eks-cluster");

                  // Export the cluster's kubeconfig.
                  return new Dictionary<string, object?>
                  {
                    ["kubeconfig"] = cluster.Kubeconfig
                  };
                });
            - title: Main.Java
              language: java
              code: |
                import com.pulumi.Context;
                import com.pulumi.Pulumi;
                import com.pulumi.eks.Cluster;

                public class App {
                    public static void main(String[] args) {
                        Pulumi.run(App::stack);
                    }

                    private static void stack(Context ctx) {
                    final var cluster = new Cluster("eks-cluster");
                    ctx.export("kubeconfig", cluster.kubeconfig());
                  }
                }
            - title: Pulumi.yaml
              language: yaml
              code: |
                resources:
                  eks-cluster:
                    type: eks:Cluster
                outputs:
                  kubeconfig: ${cluster.kubeconfig}
          features:
              - title: Native cloud providers
                icon: cloud
                description: |
                    Azure Native covers 100% of the Azure Resource Manager API, and the Kubernetes provider reaches any resource in the Kubernetes API.
              - title: Cloud Native support
                icon: clouds
                description: |
                    Use a single workflow to manage both Kubernetes resources and infrastructure.

        - title: "Deliver infrastructure through software delivery pipelines"
          sub_title: "CI/CD Integrations"
          description: |
            Version, review, test, and deploy infrastructure code through the same tools and processes used for your application code.
          image: "/images/product/pulumi-cicd.png"
          features:
              - title: Version and review
                icon: git-merged
                description: |
                    Manage infrastructure code in Git and approve changes through pull requests.
              - title: Shift left
                icon: eye
                description: |
                    Get rapid feedback on your code with fast unit tests, and run integration tests against ephemeral infrastructure.
              - title: Continuous delivery
                icon: cycle
                description: |
                    Integrate your CI/CD provider with Pulumi or use GitOps to manage Kubernetes clusters.

stats:
    title: Trusted by thousands
    description: |
        Pulumi's Infrastructure as Code CLI and SDK is an open-source project that's supported
        by an active community. We maintain a public roadmap and welcome feedback and contributions.
    community:
        number: "350,000+"
        description: developers
    company:
        number: "4,000+"
        description: organizations
    integration:
        number: "200+"
        description: Cloud and service integrations

case_studies:
    title: Customers innovating with Pulumi Cloud
    items:
        - name: Atlassian
          link: /case-studies/atlassian/
          logo: atlassian-wordmark
          description: |
            Developers reduced their time spent on maintenance by 50%.

        - name: Elkjop
          link: /case-studies/elkjop-nordic/
          logo: elkjop-nordic
          description: |
            Increased developers' agility and speed through platform engineering.

        - name: Starburst
          link: /case-studies/starburst/
          logo: starburst
          description: |
            Increased velocity and speed, with deployments that are up to 3x faster.

        - name: BMW
          link: /case-studies/bmw/
          logo: bmw
          description: |
            Enabled developers to deploy across hybrid cloud environments.

        - name: Lemonade
          link: /case-studies/lemonade/
          logo: lemonade
          description: |
            Standardized infrastructure architectures with reusable components.

        - name: Snowflake
          link: /case-studies/snowflake/
          logo: snowflake
          description: |
            Built a multicloud, Kubernetes-based platform to standardize all deployments
---
