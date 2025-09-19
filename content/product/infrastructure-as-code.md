---
title: "Infrastructure as Code in Any Language – Pulumi IaC"
meta_desc: Write infrastructure code using TypeScript, Python, Go, .NET, Java, or YAML. Deploy to any cloud with built-in previews and testing.
layout: infrastructure-as-code
aliases:
    - /product/iac
    - /product/pulumi-iac

heading: Infrastructure as Code<br/>in Any Language
subheading: |
    The core of the Pulumi platform. Write cloud infrastructure using real programming languages – TypeScript, Python, Go, .NET, Java, or YAML – and ship to any cloud in minutes.

overview:
    title: Real Languages. Any Cloud. Open Source.
    description: |
        Stop wrestling with DSLs. Use the programming languages you already know to build infrastructure on AWS, Azure, Google Cloud, Kubernetes, and thousands of providers. Powered by Pulumi's open source IaC engine with 20k+ GitHub stars. Get started in 5 minutes.

key_features_above:
    items:
        - title: "Write infrastructure code in your favorite language"
          sub_title: "Powered by Apache 2.0 Licensed Open Source"
          description:
            Pulumi lets you write [infrastructure as code](/what-is/what-is-infrastructure-as-code/) using standard programming languages – TypeScript/JavaScript, Python, Go, C#, Java, and YAML. Get autocomplete, type checking, and all your favorite IDE features. Build on AWS, Azure, Google Cloud, Kubernetes, and [thousands of providers](/registry/). Our [open source engine](https://github.com/pulumi/pulumi) is Apache 2.0 licensed and will always remain free.
          image: "/images/product/pulumi-iac-code.png"
          features:
              - title: Use real code, not DSLs
                description: |
                    Write infrastructure with loops, conditionals, functions, and classes. Reuse code, catch errors at compile time, and refactor with confidence.
                icon: code
                color: yellow
              - title: Build on any cloud
                description: |
                    Access AWS, Azure, Google Cloud, Kubernetes, and [thousands of providers](/registry/) through a unified, consistent API. Same-day updates for new cloud features.
                icon: global
                color: yellow
              - title: Test before you ship
                description: |
                    Preview changes before deploying them. Write [unit tests](/docs/guides/testing/#unit-testing) for your infrastructure. Run [integration tests](/docs/guides/testing/integration/) against ephemeral environments.
                icon: eye
                color: yellow

key_features:
    title: Key features
    items:
        - title: "Ship faster with reusable components"
          sub_title: "Pulumi Packages - Infrastructure Building Blocks"
          description: |
            Stop copy-pasting and create reusable infrastructure components that can be used in any language. Package common patterns once, use everywhere. Share via Pulumi's registry, npm, PyPI, NuGet, or any package manager.
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
          button:
            text: "Learn more about Pulumi Packages"
            link: "/product/packages/"
          features:
              - title: Production-ready patterns
                description: |
                    Ship EKS clusters, serverless apps, or entire platforms with one line of code using [well-architected components](/docs/iac/clouds/aws/guides/).
              - title: Thousands of providers
                description: |
                    Full API coverage for AWS, Azure, Google Cloud, Kubernetes, plus Cloudflare, Datadog, GitHub, and thousands more.
              - title: From VMs to Kubernetes
                description: |
                    Manage traditional infrastructure, containers, serverless, and [Kubernetes](/kubernetes/) with one tool, one workflow.

        - title: "Ship infrastructure like software"
          sub_title: "GitOps & CI/CD Native"
          description: |
            Infrastructure as code means infrastructure in Git. Review changes in pull requests. Run tests in CI. Ship through GitHub Actions, GitLab, Jenkins, or any CI/CD system.
          image: "/images/product/pulumi-cicd.png"
          button:
            text: "Learn more about CI/CD Integrations"
            link: "/docs/iac/packages-and-automation/continuous-delivery/"
          features:
              - title: Git-native workflow
                description: |
                    Every infrastructure change is a pull request. Review, comment, approve. Full audit trail built in.
              - title: Catch bugs before production
                description: |
                    Run [unit tests](/docs/iac/concepts/testing/unit/) in milliseconds. Spin up ephemeral environments for [integration tests](/docs/iac/concepts/testing/integration/). Fail fast, fix fast.
              - title: Works with your CI/CD
                description: |
                    Integrates with [any CI/CD system](/docs/iac/packages-and-automation/continuous-delivery/). GitHub Actions, GitLab, Jenkins, CircleCI - your choice. Or use the [Kubernetes operator](/docs/iac/packages-and-automation/continuous-delivery/pulumi-kubernetes-operator/) for GitOps.

stats:
    title: Open Source Core. Pulumi Cloud Built In.
    description: |
        Get started with Pulumi Cloud for free, state management and secrets included. Our [open source engine](https://github.com/pulumi/pulumi) powers everything underneath. Scale to enterprise features when you need them, or self-host if required.
    community:
        number: "350,000+"
        description: engineers building with Pulumi
    company:
        number: "3,700+"
        description: companies in production
    integration:
        number: "1,000s"
        description: of cloud and service providers

customer_quotes:
    panther:
        text: |
            "Our developers needed a fast, modular, and testable platform for managing cloud infrastructure. <b>Nothing is better than having standard programming languages for building and managing infrastructure</b>"
        author: Austin Byers, Principal Platform Engineer
        logo: panther-labs

key_features_below:
    items:
        - title: "Scale Confidently with Pulumi Cloud"
          sub_title: "Built for Teams from Day One"
          description: |
             Start free with Pulumi Cloud - encrypted state storage, secrets management, and collaboration built in. When you scale, enterprise features like RBAC, policy enforcement, and SSO are ready. All powered by our open source engine.
          image: "/images/product/pulumi-cloud-iac-stylized-01.png"
          button:
            text: "Learn more about Pulumi Cloud"
            link: "/product/pulumi-cloud/"
          features:
              - title: Encrypted state management
                description: |
                    Never lose state again. Automatic versioning and encryption at rest. Pulumi Cloud handles it all, or self-host with S3/Azure Blob.
              - title: Secrets that actually work
                description: |
                    No more secrets in plaintext. Automatic encryption for sensitive values. Integrate with AWS Secrets Manager, Azure Key Vault, or use [Pulumi ESC](/product/secrets-configuration/) for centralized secrets.
              - title: Ship with confidence
                description: |
                    Review every change before it ships. Full history and audit logs. Roll back to any previous state when needed.
              - title: See everything, everywhere
                description: |
                    Single pane of glass for all your clouds. Search across AWS, Azure, and GCP. Find that rogue EC2 instance in seconds.
              - title: Automation API
                description: |
                    Infrastructure as code as a library. Embed Pulumi in your app. Build custom CLIs, portals, or platforms. Full programmatic control.
              - title: Self-service infrastructure
                description: |
                    Let engineers provision their own infrastructure safely. Templates, guardrails, and approval workflows. Works with Backstage or build your own.
              - title: Enterprise SSO & RBAC
                description: |
                    SAML, SCIM, GitHub, GitLab, Atlassian. Fine-grained permissions. Temporary access tokens. SOC 2 Type II compliant.
              - title: Policy as code
                description: |
                    Enforce security and compliance automatically. Hundreds of built-in policies or write your own. Block non-compliant infrastructure before it ships.
              - title: Complete audit trail
                description: |
                    Every action logged. Who changed what, when, and why. Export to SIEM. Compliance reports at your fingertips.

learn:
    title: Get started with Infrastructure as Code
    items:
        - title: Ship your first infrastructure today
          description: |
            Get started in just five minutes. Follow our tutorials for AWS, Azure, Google Cloud, Kubernetes, and more.
          buttons:
            - link: /docs/iac/get-started/
              type: primary
              action: Start Free
            - link: /contact/?form=request-a-demo
              type: secondary
              action: Book a Demo
        - title: Migrating from other tools
          description: |
            Transition from existing infrastructure tools or continue using both. Pulumi has converter tools for Terraform, CloudFormation, ARM, and Kubernetes.
          buttons:
            - link: /docs/iac/adopting-pulumi/converters/
              type: primary
              action: Explore Converters
            - link: /docs/iac/adopting-pulumi/migrating-to-pulumi/from-terraform/
              type: secondary
              action: Migration Guide
---
