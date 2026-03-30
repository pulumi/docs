---
title: "Kubernetes Infrastructure as Code | Pulumi"
meta_desc: "Manage Kubernetes clusters and workloads with Python, TypeScript, Go, or C#. Deploy to EKS, AKS, GKE, or any cluster. Full Helm and YAML support."
layout: gads-template
block_external_search_index: true
utm_source: gads-kubernetes

heading: "Kubernetes Infrastructure as Code"
subheading: |
    Manage Kubernetes clusters and workloads using real programming languages. Pulumi lets you
    provision EKS, AKS, and GKE clusters and deploy Helm charts, YAML manifests, and custom
    resources — all from a single workflow.

hide_platform_details: true

customer_quote:
    text: "Built a multi-cloud, Kubernetes-based platform to standardize all deployments."
    author: "Snowflake Engineering"
    logo: snowflake
    link: /case-studies/snowflake

overview:
    title: Clusters + Workloads.<br/>One Workflow. Real Languages.
    description: |
        Looking for <span id="dki-placeholder" style="font-weight: bold;">Kubernetes infrastructure as code</span>? Pulumi manages both the clusters and everything running on them in a single workflow. Provision EKS, AKS, or GKE with built-in best practices, then deploy Helm charts, YAML manifests, and custom resources — all in Python, TypeScript, Go, or C#.

key_features_above:
    items:
        - title: "Clusters and workloads in one workflow"
          sub_title: "Pulumi Kubernetes Provider"
          description:
            Stop juggling Terraform for clusters and kubectl for workloads. Pulumi manages both your cloud infrastructure and Kubernetes resources in a single program. Use real programming languages to define deployments, services, and config maps with full type safety and auto-completion.
          image: "/images/product/pulumi-iac-code.png"
          features:
              - title: Full Kubernetes API coverage
                description: |
                    Manage any Kubernetes resource — Deployments, Services, ConfigMaps, CRDs, and more — with full type safety and auto-completion in your IDE.
                icon: global
                color: yellow
              - title: Helm and YAML support
                description: |
                    Deploy existing Helm charts and YAML manifests directly from Pulumi. Mix and match with strongly-typed resources as needed.
                icon: code
                color: yellow
              - title: Multi-cluster management
                description: |
                    Manage workloads across EKS, AKS, GKE, and self-hosted clusters from a single Pulumi program with shared configuration and policies.
                icon: lightning
                color: yellow

key_features:
    title: Key features
    items:
        - title: "Production-ready Kubernetes clusters"
          sub_title: "Pulumi EKS, AKS, and GKE Components"
          description: |
            Spin up production-ready Kubernetes clusters in minutes, not days. Pulumi's higher-level components for EKS, AKS, and GKE handle VPCs, node groups, OIDC providers, and IAM roles with built-in best practices — so you don't have to wire it all together yourself.
          ide:
            - title: index.ts
              language: typescript
              code: |
                import * as pulumi from "@pulumi/pulumi";
                import * as eks from "@pulumi/eks";
                import * as k8s from "@pulumi/kubernetes";

                // Create a production-ready EKS cluster.
                const cluster = new eks.Cluster("my-cluster", {
                    instanceType: "t3.medium",
                    desiredCapacity: 3,
                });

                // Deploy an NGINX service to the cluster.
                const app = new k8s.apps.v1.Deployment("nginx", {
                    spec: {
                        replicas: 2,
                        selector: { matchLabels: { app: "nginx" } },
                        template: {
                            metadata: { labels: { app: "nginx" } },
                            spec: { containers: [{ name: "nginx", image: "nginx" }] },
                        },
                    },
                }, { provider: cluster.provider });

                export const kubeconfig = cluster.kubeconfig;
            - title: __main__.py
              language: python
              code: |
                import pulumi
                import pulumi_eks as eks
                import pulumi_kubernetes as k8s

                # Create a production-ready EKS cluster.
                cluster = eks.Cluster("my-cluster",
                    instance_type="t3.medium",
                    desired_capacity=3,
                )

                # Deploy an NGINX service to the cluster.
                app = k8s.apps.v1.Deployment("nginx",
                    spec={
                        "replicas": 2,
                        "selector": {"match_labels": {"app": "nginx"}},
                        "template": {
                            "metadata": {"labels": {"app": "nginx"}},
                            "spec": {"containers": [{"name": "nginx", "image": "nginx"}]},
                        },
                    },
                    opts=pulumi.ResourceOptions(provider=cluster.provider),
                )

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
                        // Create a production-ready EKS cluster.
                        cluster, err := eks.NewCluster(ctx, "my-cluster", &eks.ClusterArgs{
                          InstanceType:    pulumi.String("t3.medium"),
                          DesiredCapacity: pulumi.Int(3),
                        })
                        if err != nil {
                          return err
                        }

                        ctx.Export("kubeconfig", cluster.Kubeconfig)
                        return nil
                      })
                    }
            - title: MyStack.cs
              language: csharp
              code: |
                using Pulumi;
                using Pulumi.Eks;

                await Deployment.RunAsync(() =>
                {
                  // Create a production-ready EKS cluster.
                  var cluster = new Cluster("my-cluster", new()
                  {
                    InstanceType = "t3.medium",
                    DesiredCapacity = 3,
                  });

                  return new Dictionary<string, object?>
                  {
                    ["kubeconfig"] = cluster.Kubeconfig,
                  };
                });
            - title: Main.Java
              language: java
              code: |
                import com.pulumi.Context;
                import com.pulumi.Pulumi;
                import com.pulumi.eks.Cluster;
                import com.pulumi.eks.ClusterArgs;

                public class App {
                    public static void main(String[] args) {
                        Pulumi.run(App::stack);
                    }

                    private static void stack(Context ctx) {
                      // Create a production-ready EKS cluster.
                      var cluster = new Cluster("my-cluster", ClusterArgs.builder()
                        .instanceType("t3.medium")
                        .desiredCapacity(3)
                        .build());
                      ctx.export("kubeconfig", cluster.kubeconfig());
                    }
                }
            - title: Pulumi.yaml
              language: yaml
              code: |
                resources:
                  my-cluster:
                    type: eks:Cluster
                    properties:
                      instanceType: t3.medium
                      desiredCapacity: 3
                outputs:
                  kubeconfig: ${my-cluster.kubeconfig}
          features:
              - title: EKS, AKS, and GKE components
                description: |
                    Production-ready cluster components with built-in best practices for networking, IAM, and node management. Minutes, not days.
              - title: Deploy Helm charts
                description: |
                    Install and manage Helm charts as first-class Pulumi resources. Override values with real code instead of YAML templating.
              - title: Server-side apply
                description: |
                    Use Kubernetes server-side apply for conflict-free management of resources shared across multiple controllers and tools.

        - title: "Deliver infrastructure through software delivery pipelines"
          sub_title: "CI/CD Integrations"
          description: |
            Version, review, test, and deploy infrastructure code through the same tools and processes used for your application code.
          image: "/images/product/pulumi-cicd.png"
          features:
              - title: Version and review
                description: |
                    Manage infrastructure code in Git and approve changes through pull requests.
              - title: Shift left
                description: |
                    Get rapid feedback on your code with fast unit tests, and run integration tests against ephemeral infrastructure.
              - title: Continuous delivery
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
        number: "3,700+"
        description: "Companies in production"
    integration:
        number: "170+"
        description: "Cloud and service integrations"

key_features_below:
    items:
        - title: "The fastest and easiest way to use Pulumi IaC at scale"
          sub_title: "Pulumi Cloud"
          description: |
             A fully-managed service for Pulumi IaC plus so much more. Manage and store infrastructure state & secrets, collaborate within teams, view and search infrastructure, and manage security and compliance using Pulumi Cloud.
          image: "/images/product/pulumi-cloud-iac-stylized-01.png"
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
        - name: Snowflake
          link: /case-studies/snowflake/
          logo: snowflake
          description: |
            Built a multi-cloud, Kubernetes-based platform to standardize all deployments.

        - name: Elkjop
          link: /case-studies/elkjop-nordic/
          logo: elkjop-nordic
          description: |
            Increased developers' agility and speed through platform engineering.

        - name: BMW
          link: /case-studies/bmw/
          logo: bmw
          description: |
            Enabled developers to deploy across hybrid cloud environments.

        - name: Atlassian
          link: /case-studies/atlassian/
          logo: atlassian
          description: |
            Developers reduced their time spent on maintenance by 50%.

        - name: Lemonade
          link: /case-studies/lemonade/
          logo: lemonade
          description: |
            Standardized infrastructure architectures with reusable components.
---
