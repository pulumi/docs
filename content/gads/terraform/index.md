---
title: "Terraform Alternative | Pulumi"
meta_desc: "Use Python, TypeScript, Go, or .NET — or HCL — for infrastructure as code. Free migration tools, no resource caps on the free tier, 170+ cloud providers."
layout: gads-template
block_external_search_index: true

heading: "Terraform Alternative"
subheading: |
    Use the programming languages your team already knows. Pulumi is free, open source,
    and works with your existing Terraform. Migrate at your pace.

customer_quote:
    text: "What used to take a week and a half now, with Pulumi, took under a day."
    author: "Raman Hariharan"
    title: "Director of Cloud Platform Engineering"
    company: "Snowflake"
    logo: snowflake
    link: /case-studies/snowflake

overview:
    title: Your Choice of Language. No Resource Caps.<br/>Migrate at Your Pace.
    description: |
        Looking for <span id="dki-placeholder" style="font-weight: bold;">a Terraform alternative</span>? HCP Terraform's free tier caps you at 500 managed resources per organization. Pulumi Cloud has no resource caps. Write infrastructure in Python, TypeScript, JavaScript, Go, or .NET with full IDE support, testing, and 170+ cloud providers. Free migration tooling included: convert your existing Terraform with the Pulumi CLI.

key_features_above:
    items:
        - title: "Author infrastructure in the language you prefer"
          sub_title: "Pulumi Infrastructure as Code Engine"
          description:
            Author infrastructure as code using programming languages you already know, including Python, TypeScript, JavaScript, Go, .NET, Java, YAML, and HCL. Use `pulumi convert`, the free converter built into the Pulumi CLI, to migrate your existing Terraform files. Deploy to 170+ providers.
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
        - title: "Migrate from Terraform in minutes"
          sub_title: "Free Migration Tools"
          description: |
            Use `pulumi convert` to turn your existing Terraform HCL into Python, TypeScript, JavaScript, Go, or .NET. Import existing state with `pulumi import`. Keep your current infrastructure running while you migrate at your own pace. No forced deadlines. No resource caps.
          image: "/images/product/pulumi-iac-code.png"
          features:
              - title: Convert HCL to a general-purpose language
                icon: exchange
                description: |
                    `pulumi convert --from terraform` turns your .tf files into Pulumi programs in your language of choice. [Read the migration guide](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/).
              - title: Import existing state
                icon: exchange
                description: |
                    Already have infrastructure managed by Terraform? Import your state directly into Pulumi without re-provisioning. Zero downtime migration.
              - title: No 500 resource limit
                icon: lightning
                description: |
                    Pulumi Cloud's free tier has no managed resource caps. Manage as many resources as you need. Scale when you're ready.

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

        - name: Starburst
          link: /case-studies/starburst/
          logo: starburst
          description: |
            Cut multi-region blue/green deployments from two weeks to three hours.

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
            Switched from HCL to Go with Pulumi. Deployment time cut from 1.5 weeks to under a day.
---
