---
meta_desc: Build internal developer platforms that enable self-service infrastructure with policies and guardrails.
layout: gads-template
block_external_search_index: true
heading: "Platform Engineering"
subheading: |
  Pulumi enables platform teams to build self-service infrastructure with governance built in.

overview:
  title: Enable Self-Service Infrastructure<br/>Without Scaling Your Platform Team
  description: |
    Build internal developer platforms that let engineers provision infrastructure safely, with policies, guardrails, and full auditability built in.

key_features_above:
  items:
    - title: "Empower developers with guardrails"
      description: |
        Write policies in TypeScript, Python, or Go to define what teams can provision, then let them self-service within boundaries
      icon: code
      color: yellow
    - title: Prove platform ROI with metrics
      description: |
        Track adoption, cost, and compliance across every stack and environment with centralized visibility
      icon: dashboard
      color: yellow
    - title: Reduce ticket backlog
      description: |
        Developers get infrastructure on-demand while platform engineers maintain control and governance
      icon: check
      color: yellow
    - title: Scale without headcount
      description: |
        Support 10x more teams without growing your platform engineering org
      icon: growth
      color: yellow

key_features:
  title: Build infrastructure faster with reusable components
  items:
    - title: "Pulumi Packages"
      sub_title: "Multi-language component library"
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
        - title: Program.cs
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
        - title: App.java
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
      cta:
        - label: Native cloud providers
          description: |
            Full API coverage for AWS, Azure, Google Cloud, and Kubernetes with same-day updates.
        - label: Crosswalk for AWS
          description: |
            Adopt well-architected best practices for your infrastructure easily with the Crosswalk library.
        - label: Cloud Native support
          description: |
            Use a single workflow to manage both Kubernetes resources and infrastructure.

    - title: "Deliver infrastructure through software delivery pipelines"
      sub_title: "CI/CD Integrations"
      description: |
        Version, review, test, and deploy infrastructure code through the same tools and processes used for your application code.
      image: /images/product/pulumi-cicd.png
      cta:
        - label: Version and review
          description: |
            Manage infrastructure code in Git and approve changes through pull requests.
        - label: Shift left
          description: |
            Get rapid feedback on your code with fast unit tests, and run integration tests against ephemeral infrastructure.
        - label: Continuous delivery
          description: |
            Integrate your CI/CD provider with Pulumi or use GitOps to manage Kubernetes clusters.

stats:
  title: Trusted by thousands
  description: |
    Pulumi's Infrastructure as Code CLI and SDK is an open-source project that's supported
    by an active community. We maintain a public roadmap and welcome feedback and contributions.
  community:
    number: "150,000+"
    description: developers
  company:
    number: "3,000+"
    description: organizations
  integration:
    number: "170+"
    description: Cloud and service integrations

key_features_below:
  items:
    - title: "Use Pulumi IaC at scale"
      sub_title: "Pulumi Cloud"
      description: |
        A fully-managed service for Pulumi IaC plus so much more. Manage and store infrastructure state & secrets, collaborate within teams, view and search infrastructure, and manage security and compliance using Pulumi Cloud.
      image: /images/product/pulumi-cloud-iac-stylized-01.png
      cta:
        - label: Pulumi IaC
          description: |
            Utilize open-source IaC in TypeScript, Python, Go, C#, Java and YAML. Build and distribute reusable components for 170+ cloud & SaaS providers.
        - label: Pulumi ESC
          description: |
            Centralized secrets management & orchestration. Tame secrets sprawl and configuration complexity securely across all your cloud infrastructure and applications.
        - label: Automate deployment workflows
          description: |
            Orchestrate secure deployment workflows through GitHub or an API.
        - label: Search and analytics
          description: |
            View resources from any cloud in one place. Search for resources across clouds with powerful queries and filters.
        - label: Pulumi Automation API
          description: |
            Build custom deployment and CI/CD workflows that integrate with Pulumi Developer Portal, custom portals, or CLIs.
        - label: Developer portals
          description: |
            Create internal developer portals to distribute infrastructure templates using Pulumi or the Backstage-plugin.
        - label: Identity and access control
          description: |
            Manage teams with SCIM, SAML SSO, GitHub, GitLab, or Atlassian. Set permissions and access tokens.
        - label: Policy enforcement
          description: |
            Build policy packs from 150 policies or write your own. Leverage compliance-ready policies for any cloud to increase compliance posture and remediation policies to correct violations.
        - label: Audit logs
          description: |
            Track and store user actions and change history with option to export logs.

case_studies:
  items:
    - name: Atlassian
      description: Developers reduced their time spent on maintenance by 50%.
    - name: Elkjop
      description: Increased developers' agility and speed through platform engineering.
    - name: Starburst
      description: Increased velocity and speed, with deployments that are up to 3x faster.
    - name: BMW
      description: Enabled developers to deploy across hybrid cloud environments.
    - name: Lemonade
      description: Standardized infrastructure architectures with reusable components.
    - name: Snowflake
      description: Built a multi-cloud, Kubernetes-based platform to standardize all deployments
---
