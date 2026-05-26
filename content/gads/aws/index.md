---
title: "AWS Infrastructure as Code | Pulumi"
meta_desc: "Manage AWS with Python, TypeScript, Go, or C#. Full API coverage, same-day updates, built-in best practices with Crosswalk. Free tier, no resource caps."
layout: gads-template
block_external_search_index: true

heading: "AWS Infrastructure as Code"
subheading: |
    Manage any AWS service with real programming languages. Pulumi's AWS provider offers
    full API coverage with same-day updates, plus higher-level Crosswalk components
    for production-ready architectures out of the box.

hide_platform_details: true

customer_quote:
    text: "What used to take a week and a half now, with Pulumi, took under a day."
    author: "Raman Hariharan"
    title: "Director of Cloud Platform Engineering"
    company: "Snowflake"
    logo: snowflake
    link: /case-studies/snowflake

overview:
    title: Full AWS API Coverage.<br/>Real Languages. Same-Day Updates.
    description: |
        Looking for <span id="dki-placeholder" style="font-weight: bold;">AWS infrastructure as code</span>? Pulumi gives you full coverage of every AWS service — EC2, EKS, Lambda, S3, RDS, and more — with same-day updates when new services launch. Write infrastructure in Python, TypeScript, Go, or C# with full IDE support, testing, and auto-completion.

key_features_above:
    items:
        - title: "Author in any language, deploy to AWS"
          sub_title: "Pulumi AWS Provider"
          description:
            Manage any AWS resource using programming languages you already know. Pulumi's AWS provider covers every service and updates the same day AWS releases new features. Use Crosswalk for AWS to adopt well-architected best practices instantly.
          features:
              - title: Every AWS service, day one
                description: |
                    Full API coverage for EC2, EKS, Lambda, S3, RDS, DynamoDB, and every other AWS service. Same-day updates when new services and features launch.
                icon: global
                color: yellow
              - title: Crosswalk for AWS
                description: |
                    Deploy production-ready VPCs, ECS Fargate services, and EKS clusters in just a few lines of code using Pulumi's Crosswalk library.
                icon: code
                color: yellow
              - title: AI-powered infrastructure
                description: |
                    Generate Pulumi code for AWS from natural language or convert existing CloudFormation and Terraform with built-in migration tools.
                icon: lightning
                color: yellow

key_features:
    title: Key features
    items:
        - title: "Production-ready AWS in minutes"
          sub_title: "Pulumi Crosswalk for AWS"
          description: |
            Stop writing hundreds of lines of boilerplate for VPCs, subnets, and security groups. Crosswalk for AWS gives you production-ready architectures with built-in best practices for ECS, EKS, API Gateway, and more — in just a few lines of code.
          ide:
            - title: index.ts
              language: typescript
              code: |
                import * as pulumi from "@pulumi/pulumi";
                import * as aws from "@pulumi/aws";
                import * as awsx from "@pulumi/awsx";

                // Create a VPC with best-practice defaults.
                const vpc = new awsx.ec2.Vpc("my-vpc");

                // Create an ECS Fargate service.
                const cluster = new aws.ecs.Cluster("cluster");
                const service = new awsx.ecs.FargateService("service", {
                    cluster: cluster.arn,
                    networkConfiguration: {
                        subnets: vpc.privateSubnetIds,
                    },
                });
            - title: __main__.py
              language: python
              code: |
                import pulumi
                import pulumi_aws as aws
                import pulumi_awsx as awsx

                # Create a VPC with best-practice defaults.
                vpc = awsx.ec2.Vpc("my-vpc")

                # Create an ECS Fargate service.
                cluster = aws.ecs.Cluster("cluster")
                service = awsx.ecs.FargateService("service",
                    cluster=cluster.arn,
                    network_configuration={
                        "subnets": vpc.private_subnet_ids,
                    },
                )
            - title: main.go
              language: go
              code: |
                    package main

                    import (
                      "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ecs"
                      "github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
                      "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
                    )

                    func main() {
                      pulumi.Run(func(ctx *pulumi.Context) error {
                        // Create a VPC with best-practice defaults.
                        vpc, err := ec2.NewVpc(ctx, "my-vpc", nil)
                        if err != nil {
                          return err
                        }

                        // Create an ECS cluster.
                        cluster, err := ecs.NewCluster(ctx, "cluster", nil)
                        if err != nil {
                          return err
                        }

                        ctx.Export("vpcId", vpc.VpcId)
                        ctx.Export("clusterId", cluster.ID())
                        return nil
                      })
                    }
            - title: MyStack.cs
              language: csharp
              code: |
                using Pulumi;
                using Pulumi.Aws.Ecs;
                using Pulumi.Awsx.Ec2;
                using Pulumi.Awsx.Ecs;

                await Deployment.RunAsync(() =>
                {
                  // Create a VPC with best-practice defaults.
                  var vpc = new Vpc("my-vpc");

                  // Create an ECS cluster and Fargate service.
                  var cluster = new Cluster("cluster");
                  var service = new FargateService("service", new()
                  {
                    Cluster = cluster.Arn,
                  });
                });
            - title: Main.Java
              language: java
              code: |
                import com.pulumi.Context;
                import com.pulumi.Pulumi;
                import com.pulumi.awsx.ec2.Vpc;
                import com.pulumi.aws.ecs.Cluster;

                public class App {
                    public static void main(String[] args) {
                        Pulumi.run(App::stack);
                    }

                    private static void stack(Context ctx) {
                      // Create a VPC with best-practice defaults.
                      var vpc = new Vpc("my-vpc");

                      // Create an ECS cluster.
                      var cluster = new Cluster("cluster");
                      ctx.export("vpcId", vpc.vpcId());
                    }
                }
            - title: Pulumi.yaml
              language: yaml
              code: |
                resources:
                  my-vpc:
                    type: awsx:ec2:Vpc
                  cluster:
                    type: aws:ecs:Cluster
                outputs:
                  vpcId: ${my-vpc.vpcId}
          features:
              - title: Native AWS provider
                icon: cloud
                description: |
                    Full API coverage for every AWS service with same-day updates when new features launch. No waiting for third-party support.
              - title: Crosswalk for AWS
                icon: abstract-shapes
                description: |
                    Adopt well-architected best practices for VPC, ECS, EKS, API Gateway, and more with pre-built high-level components.
              - title: Migrate from CloudFormation
                icon: exchange
                description: |
                    Use cf2pulumi to convert existing CloudFormation templates to Pulumi in your language of choice. Import existing stacks with zero downtime.

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

key_features_below:
    items:
        - title: "The fastest and easiest way to use Pulumi IaC at scale"
          sub_title: "Pulumi Cloud"
          description: |
             A fully-managed service for Pulumi IaC plus so much more. Manage and store infrastructure state & secrets, collaborate within teams, view and search infrastructure, and manage security and compliance using Pulumi Cloud.
          image: "/images/product/pulumi-cloud-iac-stylized-01.png"
          features:
              - title: Pulumi IaC
                icon: code
                description: |
                    Utilize open-source IaC in TypeScript, Python, Go, C#, Java and YAML. Build and distribute reusable components for 170+ cloud & SaaS providers.
              - title: Pulumi ESC
                icon: lock
                description: |
                    Centralized secrets management & orchestration. Tame secrets sprawl and configuration complexity securely across all your cloud infrastructure and applications.
              - title: Automate deployment workflows
                icon: cycle
                description: |
                    Orchestrate secure deployment workflows through GitHub or an API.
              - title: Search and analytics
                icon: eye
                description: |
                    View resources from any cloud in one place. Search for resources across clouds with simple queries and filters.
              - title: Pulumi Automation API
                icon: gear
                description: |
                    Build custom deployment and CI/CD workflows that integrate with Pulumi Developer Portal, custom portals, or CLIs.
              - title: Developer portals
                icon: buildings
                description: |
                    Create internal developer portals to distribute infrastructure templates using Pulumi or the Backstage-plugin.
              - title: Identity and access control
                icon: security
                description: |
                    Manage teams with SCIM, SAML SSO, GitHub, GitLab, or Atlassian. Set permissions and access tokens.
              - title: Policy enforcement
                icon: gavel
                description: |
                    Build policy packs from 150 policies or write your own. Leverage compliance-ready policies for any cloud to increase compliance posture and remediation policies to correct violations.
              - title: Audit logs
                icon: clipboard
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

        - name: Atlassian
          link: /case-studies/atlassian/
          logo: atlassian-wordmark
          description: |
            Developers reduced their time spent on maintenance by 50%.

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

        - name: Starburst
          link: /blog/how-starburst-data-creates-infrastructure-automation-magic-with-code/
          logo: starburst
          description: |
            Deployments up to 3x faster with Pulumi infrastructure automation.
---
