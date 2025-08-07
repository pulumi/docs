---
title: "OpenTofu Alternative | Pulumi"
meta_desc: Infrastructure as Code in any programming language. Enable your team to get code to any cloud productively, securely, and reliably.
layout: gads-template
block_external_search_index: true
aliases:
    - /gads/gads-template

heading: "OpenTofu Alternative"
subheading: |
    Pulumi is a free, open source infrastructure as code tool, and works best with Pulumi Cloud to
    make managing infrastructure secure, reliable, and hassle-free.

overview:
    title: Infrastructure as Code<br/>in any Programming Language
    description: |
        Pulumi Cloud is the smartest and easiest way to automate, secure, and manage everything you run in the cloud using programming languages you know and love.

key_features_above:
    items:
        - title: "Author in any language, deploy to any cloud"
          sub_title: "Pulumi Infrastructure as Code Engine"
          description:
            Author [infrastructure as code (IaC)](/what-is/what-is-infrastructure-as-code/) using programming languages you know and love – including TypeScript/JavaScript, Python, Go, C#, Java, and YAML. Deploy to 170+ providers like AWS, Azure, Google Cloud, and Kubernetes.
          image: "/images/product/pulumi-iac-code.png"
          button:
            text: "Try Pulumi Cloud for FREE"
            link: "https://app.pulumi.com/signup"
          features:
              - title: Code faster
                description: |
                    Write infrastructure code in TypeScript, JavaScript, Python, Go, .NET, Java, and YAML using your IDE and any language ecosystem tools.
                icon: code
                color: yellow
              - title: Build on any cloud
                description: |
                    Access the full breadth of services in AWS, Azure, GCP, and [170+ providers](/registry/) through
                    a complete and consistent SDK interface.
                icon: global
                color: yellow
              - title: Preview and test changes
                description: |
                    Test and validate infrastructure with standard [unit test frameworks](/docs/guides/testing/#unit-testing) and
                    [integration tests](/docs/guides/testing/integration/). Preview changes before deploying.
                icon: eye
                color: yellow
        
key_features:
    title: Key features
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
          button:
            text: "Try Pulumi Cloud for FREE"
            link: "https://app.pulumi.com/signup"
          features:
              - title: Native cloud providers
                description: |
                    Full API coverage for AWS, Azure, Google Cloud, and Kubernetes with same-day updates.
              - title: Crosswalk for AWS
                description: |
                    Adopt well-architected best practices for your infrastructure easily with the [Crosswalk library](/docs/iac/clouds/aws/guides/).
              - title: Cloud Native support
                description: |
                    Use a single workflow to manage both [Kubernetes](/kubernetes/) resources and infrastructure.

        - title: "Deliver infrastructure through software delivery pipelines"
          sub_title: "CI/CD Integrations"
          description: |
            Version, review, test, and deploy infrastructure code through the same tools and processes used for your application code.
          image: "/images/product/pulumi-cicd.png"
          button:
            text: "Try Pulumi Cloud for FREE"
            link: "https://app.pulumi.com/signup"
          features:
              - title: Version and review
                description: |
                    Manage infrastructure code in Git and approve changes through pull requests.
              - title: Shift left
                description: |
                    Get rapid feedback on your code with fast [unit tests](/docs/iac/concepts/testing/unit/), and run [integration tests](/docs/iac/concepts/testing/integration/) against ephemeral infrastructure.
              - title: Continuous delivery
                description: |
                    [Integrate your CI/CD provider](/docs/iac/packages-and-automation/continuous-delivery/) with Pulumi or use GitOps to [manage Kubernetes clusters](/docs/iac/packages-and-automation/continuous-delivery/pulumi-kubernetes-operator/).

stats:
    title: Open source. Enterprise ready.
    description: |
        Pulumi's Infrastructure as Code CLI and SDK is an [open-source project](https://github.com/pulumi/) that's supported
        by an active community. We maintain a [public roadmap](https://github.com/orgs/pulumi/projects/44) and welcome feedback and contributions.
    community:
        number: "10,000s"
        description: of community members
    company:
        number: "1,000s"
        description: of companies
    integration:
        number: "170+"
        description: Cloud and service integrations

key_features_below:
    items:
        - title: "The fastest and easiest way to use Pulumi IaC at scale"
          sub_title: "Pulumi Cloud"
          description: |
             A fully-managed service for Pulumi IaC plus so much more. Manage and store infrastructure state & secrets, collaborate within teams, view and search infrastructure, and manage security and compliance using Pulumi Cloud.
          image: "/images/product/pulumi-cloud-iac-stylized-01.png"
          button:
            text: "Try Pulumi Cloud for FREE"
            link: "https://app.pulumi.com/signup"
          features:
              - title: Pulumi IaC
                description: |
                    Utilize open-source IaC in TypeScript, Python, Go, C#, Java and YAML. Build and distribute reusable components for 170+ cloud & SaaS providers.
              - title: Pulumi ESC
                description: |
                    Centralized secrets management & orchestration. Tame secrets sprawl and configuration complexity securely across all your cloud infrastructure and applications.
              - title: Automate deployment workflows
                description: |
                    Orchestrate secure deployment workflows through GitHub or an API.
              - title: Search and analytics
                description: |
                    View resources from any cloud in one place. Search for resources across clouds with simple queries and filters.
              - title: Pulumi Automation API
                description: |
                    Build custom deployment and CI/CD workflows that integrate with Pulumi Developer Portal, custom portals, or CLIs.
              - title: Developer portals
                description: |
                    Create internal developer portals to distribute infrastructure templates using Pulumi or the Backstage-plugin.
              - title: Identity and access control
                description: |
                    Manage teams with SCIM, SAML SSO, GitHub, GitLab, or Atlassian. Set permissions and access tokens.
              - title: Policy enforcement
                description: |
                    Build policy packs from 150 policies or write your own. Leverage compliance-ready policies for any cloud to increase compliance posture and remediation policies to correct violations.
              - title: Audit logs
                description: |
                    Track and store user actions and change history with option to export logs.

case_studies:
    title: Customers innovating with Pulumi Cloud
    items:
        - name: Atlassian
          link: /case-studies/atlassian/
          logo: atlassian
          description: |
            Developers reduced their time spent on maintenance by 50%.

        - name: Elkjop
          link: /case-studies/elkjop-nordic/
          logo: elkjop-nordic
          description: |
            Increased developers' agility and speed through platform engineering.

        - name: Starburst
          link: /blog/how-starburst-data-creates-infrastructure-automation-magic-with-code/
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