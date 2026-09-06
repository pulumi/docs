---
title: "Crossplane Alternative | Pulumi"
meta_desc: "Cloud + Kubernetes in one workflow. Real languages instead of YAML CRDs. No K8s cluster required for cloud provisioning. 170+ providers."
layout: gads-template
block_external_search_index: true

heading: "Crossplane Alternative"
subheading: |
    Manage cloud and Kubernetes infrastructure in TypeScript, JavaScript, Python, Go, or .NET — with no control
    plane to install and no compositions or XRDs to author in YAML.

customer_quote:
    text: "If Kubernetes is AC power, Pulumi is like the universal travel adapter that lets us plug into all these resources and abstract away the complexities of each individual platform."
    author: "Raman Hariharan"
    title: "Director of Cloud Platform Engineering"
    company: "Snowflake"
    logo: snowflake
    link: /case-studies/snowflake

overview:
    title: "Cloud + Kubernetes in One Workflow."
    description: 'Looking for <span id="dki-placeholder" style="font-weight: bold;">a Crossplane alternative</span>? Manage cloud and Kubernetes infrastructure with real programming languages, not YAML and custom resource definitions. No Kubernetes cluster required as a prerequisite. One tool for AWS, Azure, GCP, and K8s.'

key_features_above:
    items:
        - title: "Author in any language, deploy to any cloud"
          sub_title: "Pulumi Infrastructure as Code Engine"
          description:
            Author infrastructure as code (IaC) using programming languages you know and love – including TypeScript, JavaScript, Python, Go, .NET, Java, YAML, and HCL. Deploy to 170+ providers like AWS, Azure, Google Cloud, and Kubernetes.
          features:
              - title: Code faster
                description: |
                    Write infrastructure code in TypeScript, JavaScript, Python, Go, .NET, Java, YAML, and HCL using your IDE and any language ecosystem tools.
                icon: code
              - title: Build on any cloud
                description: |
                    Access the full breadth of services in AWS, Azure, GCP, and 170+ providers through
                    a complete and consistent SDK interface.
                icon: global
              - title: AI-powered infrastructure
                description: |
                    Convert existing Terraform with `pulumi convert`, or hand the migration to Pulumi Neo. Claude Code, Cursor, and Codex work with Pulumi through the MCP server and Agent Skills.
                icon: lightning
        
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
    title: "Trusted by thousands of companies"
    description: |
        Pulumi's Infrastructure as Code CLI and SDK is an open-source project that's supported by an active community. We maintain a public roadmap and welcome feedback and contributions.
    community:
        number: "350,000+"
        description: "Community members"
    company:
        number: "4,000+"
        description: "Companies in production"
    integration:
        number: "170+"
        description: "Cloud and service integrations"

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
            Built a multi-cloud, Kubernetes-based platform to standardize all deployments
---