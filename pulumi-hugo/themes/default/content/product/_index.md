---
title: Products
meta_desc: Learn how Pulumi's products enable your team to get code to any cloud productively, securely, and reliably, using your favorite languages.
type: page
layout: product

heading: Pulumi Overview
subheading: |
    Pulumi is a free, open source infrastructure as code tool, and works best with Pulumi Cloud to
    make managing infrastructure secure, reliable, and hassle-free.<br><br>
    Pulumi helps developers and infrastructure teams collaborate
    and tame cloud complexity -- something we call Cloud Engineering.

overview:
    title: Infrastructure as Code<br/>in any Programming Language
    description: |
        Build and ship infrastructure faster using languages you know and love. Use Pulumi’s open source SDK to provision infrastructure on any cloud, and securely and collaboratively build and manage infrastructure using Pulumi Cloud.

key_features_above:
    items:
        - title: "Author in any language, deploy to any cloud"
          sub_title: "Pulumi Infrastructure as Code Engine"
          description:
            Define infrastructure as code (IaC) in TypeScript/JavaScript, Python, Go, C#, Java, and YAML using your IDE and test frameworks for a fast inner dev loop. Deploy to [150+ providers](/registry/) like AWS, Azure, Google Cloud, and Kubernetes.
          image: "/images/product/pulumi-iac-code.png"
          button:
            text: "Learn more about Pulumi SDK"
            link: "/docs/languages-sdks/"
          features:
              - title: Code faster
                description: |
                    Write infrastructure code in languages you love using your IDE and any language ecosystem tool.
                icon: code
                color: yellow
              - title: Generate code with AI
                description: |
                    Ask [Pulumi AI](/ai/) to create your desired infrastructure code with natural language prompts.
                icon: cycle
                color: salmon
              - title: Write Policy as Code
                description: |
                    Write Policy as Code in programming languages to enforce best practices with [Crossguard](/crossguard/).
                icon: shield
                color: blue
        - title: One source of truth for your Secrets and Configurations
          sub_title: "Pulumi ESC: Environments, Secrets and Configurations"
          description:
            Centralized environments, secrets, and configurations management for cloud applications and infrastructure. Define environments as collections of secrets and configurations, which can be pulled from any source and locked down with RBAC, versioning and audit controls.
          image: "/images/product/pulumi-iac-code.png"
          button:
            text: "Learn more about Pulumi ESC"
            link: "/product/esc/"
          features:
              - title: Frictionless Security
                description: |
                    Easy-to-use single source of truth for all configurations with guardrails. Seamlessly adopt short-lived dynamic secrets.
                icon: lock
                color: purple
              - title: Improve Developer Efficiency
                description: |
                    Never have downtime over changed configurations. Change once and have it updated everywhere. 
                icon: lightning
                color: yellow
              - title: Control Access and Compliance
                description: |
                    Enforce least-privileged access through role-based access controls. All changes are fully logged for auditing.
                icon: gavel
                color: salmon
        
key_features:
    title: Key features
    items:

        - title: "Create infrastructure automation workflows"
          sub_title: "Pulumi Automation API"
          description: |
            Create workflows that coordinate provisioning, previewing, refreshing, and destroying cloud resources by using the Pulumi engine as a library in your application code.
          image: "/images/product/automation-api.png"
          button:
            text: "Learn more about Automation API"
            link: "/automation/"
          features:
              - title: 10x productivity
                description: |
                   Engineers can manage 10x more cloud resources using Automation API compared to traditional CLI tools.
              - title: Create custom CLIs
                description: |
                    Build atop Pulumi to create CLIs that make it easy for end-users to provision prebuilt cloud architectures.
              - title: Power up your SaaS
                description: |
                    Enable your services and APIs to dynamically provision and manage cloud resources at scale.

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
          button:
            text: "Learn more about Pulumi Packages"
            link: "/product/packages/"
          features:
              - title: Native cloud providers
                description: |
                    Full API coverage for AWS, Azure, Google Cloud, and Kubernetes with same-day updates.
              - title: Crosswalk for AWS
                description: |
                    Adopt well-architected best practices for your infrastructure easily with the [Crosswalk library](/docs/clouds/aws/guides/).
              - title: Cloud Native support
                description: |
                    Use a single workflow to manage both [Kubernetes](/kubernetes/) resources and infrastructure.

        - title: "Deliver infrastructure through software delivery pipelines"
          sub_title: "CI/CD Integrations"
          description: |
            Version, review, test, and deploy infrastructure code through the same tools and processes used for your application code.
          image: "/images/product/pulumi-cicd.png"
          button:
            text: "Learn more about CI/CD Integrations"
            link: "/docs/using-pulumi/continuous-delivery/"
          features:
              - title: Version and review
                description: |
                    Manage infrastructure code in Git and approve changes through pull requests.
              - title: Shift left
                description: |
                    Get rapid feedback on your code with fast [unit tests](/docs/using-pulumi/testing/unit/), and run [integration tests](/docs/using-pulumi/testing/integration/) against ephemeral infrastructure.
              - title: Continuous delivery
                description: |
                    [Integrate your CI/CD provider](/docs/using-pulumi/continuous-delivery/) with Pulumi or use GitOps to [manage Kubernetes clusters](/docs/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/).

        - title: "Scale and secure infrastructure as code for teams"
          sub_title: "Pulumi Cloud"
          description: |
             Store infrastructure state & secrets, collaborate within teams, view and search infrastructure, and manage security and compliance using Pulumi Cloud. The fastest and easiest way to use Pulumi at scale.
          image: "/images/product/pulumi-cloud-dashboard.png"
          button:
            text: "Learn more about Pulumi Cloud"
            link: "/product/pulumi-service/"
          features:
              - title: Pulumi IaC
                description: |
                    Utilize open-source IaC in TypeScript, Python, Go, C#, Java and YAML. Build and distribute reusable components for 150+ cloud & SaaS providers.
              - title: Automate deployment workflows
                description: |
                    Orchestrate secure deployment workflows through GitHub or an API.
              - title: Search and analytics
                description: |
                    View resources from any cloud in one place. Search for resources across clouds with simple queries and filters.
              - title: Pulumi Automation API
                description: |
                    Build custom deployment and CI/CD workflows that integrate with Pulumi Developer Portal, custom portals, or CLIs.
              - title: Developer Portals
                description: |
                    Create internal developer portals to distribute infrastructure templates to developers using Pulumi or the Backstage-plugin.
              - title: State & secrets
                description: |
                    Securely store state with built-in secrets manager or bring your own KMS.
              - title: Identity and access control
                description: |
                    Manage teams with SCIM, SAML SSO, GitHub, GitLab, or Atlassian. Set permissions and access tokens.
              - title: Policy enforcement
                description: |
                    Build policy packs from 150 policies or write your own. Leverage compliance-ready policies for any cloud to increase compliance posture and compliance as code for instant remediation.
              - title: Audit logs
                description: |
                    Track and store user actions and change history with option to export logs.

get_started:
    title: Getting started

    get_started:
        title: Get started now
        description: |
            Deploy your first app in just five minutes. Follow our tutorials for AWS, Azure, Google Cloud, Kubernetes, and more.
        cta_text: Get Started

    migrate:
        title: Migrating from other tools
        description: |
            Transition from existing infrastructure tools or continue using both. Pulumi has converter tools for Terraform, AWS CloudFormation, Azure Resource Manager, and Kubernetes.
        cta_text: Explore Converter Tools
---
