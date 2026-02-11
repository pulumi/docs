---
title: AWS with Pulumi
layout: aws
url: /aws

meta_desc: Automate, secure, and manage everything you run on AWS with Pulumi. Modern infrastructure as code and secrets management.

hero:
    title: Infrastructure Management for AWS
    subtitle: Modern IaC and secrets management
    description: |
        Pulumi empowers organizations to automate AWS cloud infrastructure through code, tame secrets sprawl through centralized secrets management, and manage cloud assets and compliance with the help of AI. Pulumi encourages infrastructure, platform, development, DevOps, and security teams to collaborate and accelerates time to market with greater control and minimized risk.

# Pulumi’s [infrastructure as code](/what-is/what-is-infrastructure-as-code/)
# SDK enables you to build, deploy, and manage your AWS infrastructure faster
# and with more confidence, using modern programming languages and software engineering
# practices. Leverage the full expressivity of general-purpose languages ([TypeScript/JavaScript](/docs/languages-sdks/javascript/),
# [Python](/docs/languages-sdks/python/), [Go](/docs/languages-sdks/go/), [C#](/docs/languages-sdks/dotnet/), [Java](/docs/languages-sdks/java/)
# or use markup languages (e.g., [YAML](/docs/languages-sdks/yaml/), CUE) to build any cloud architecture including containers, serverless, and server-based.

sections:
    - title: Automate
      icon: architecture
      color: violet
      subtitle: Use familiar software practices and tools to build cloud infrastructure
      description: Build cloud applications and infrastructure by combining the safety and reliability of [infrastructure as code](/what-is/what-is-infrastructure-as-code/) with the power of familiar programming languages and tools.
      image: home/ide
      points:
        - header: IDE Autocomplete
          body: With Pulumi, you can use your preferred IDE and productivity features like autocompletion so that you author infrastructure code faster and with more accuracy.
        - header: Native Testing Frameworks
          body: Use your favorite programming languages and popular testing frameworks to validate your infrastructure and applications through their entire lifecycle. Pulumi can also mock cloud resources for you so that you can perform offline testing that’s faster and cheaper.
        - header: Sharing and Reuse
          body: Sharing and reusing your infrastructure code is available right out of the box with [Pulumi Packages](/product/packages/). You can use your preferred programming language's native package managers to share and distribute infrastructure code within your organization. Or, browse publicly available packages in [Pulumi Registry](/registry/).
        - header: Continuous delivery for infrastructure
          body: Pulumi gives you the power to continuously test and deliver your cloud infrastructure by [integrating](/docs/iac/packages-and-automation/continuous-delivery/) with your favorite CI/CD platforms. By automating your testing and delivery you can focus more on delivering value to your customers.
        - header: Architect for self-service
          body: Pulumi's unique approach to [Infrastructure as Code](/what-is/what-is-infrastructure-as-code/) allows you to build self-service infrastructure platforms. You can abstract away complexity for your teammates, allowing folks to focus on what's important.
        - header: Full Coverage of AWS
          body: You can deploy the entire breadth of AWS services with Pulumi’s AWS Provider and AWS Cloud Control Provider SDKs.
    - title: Secure
      icon: rocketship
      color: salmon
      subtitle: Tame secrets sprawl and configuration complexity
      description: |
        [Secrets](/docs/iac/concepts/secrets/) sprawl can lead to security breaches. Pulumi ESC provides centralized environments, secrets, and configuration management and orchestration that helps streamline operations, improve traceability, and ensure consistent security practices.
      image: /images/product/esc-screenshot-2.png
      points:
        - header: Stop secrets sprawl
          body: Pull and sync secrets and configuration with any secrets store – AWS Secrets Manager, HashiCorp Vault, and more – and consume in any application, tool, or CI/CD platform.
        - header: Trust (and prove) your secrets are secure
          body: Adopt dynamic, short-lived secrets on demand as a best practice. Lock down every environment with [role-based access controls](/docs/pulumi-cloud/admin/organizations/#organization-roles), [versioning](/docs/esc/environments/versioning/), and a full audit log of all changes.
        - header: Ditch .env files
          body: No more copying-and-pasting secrets or storing them in plaintext on dev computers. Easily access secrets via CLI, API, Kubernetes operator, the Pulumi Cloud UI, and SDKs.
    - title: Manage
      icon: testing
      color: blue
      subtitle: Gain full auditability and visibility into all your environments to tame complexity and put security first
      description: Manage cloud infrastructure with dashboards that provide visibility into your infrastructure and any changes, [role-based access controls](/docs/pulumi-cloud/admin/organizations/#organization-roles), and [Policy as Code](/docs/insights/policy/) enforcement across your organization.
      image: /images/product/insights-resource-search.png
      points:
        - header: Converse about your infrastructure
          body: |
            [Pulumi Copilot](/product/copilot/) makes discovering cost savings, running compliance checks, and debugging deployments across your Kubernetes resources as easy as typing a question.
        - header: Enforce compliance
          body: Enable [Policy as Code](/docs/insights/policy/) within your organization so that you can define guardrails for your infrastructure, ensuring engineers are following best practices and putting security first. This helps you prevent mistakes before they occur and respond rapidly to any incidents.
        - header: Clear visibility across AWS resources
          body: Ask any questions about your AWS infrastructure. Pulumi Insights helps you find that needle in the haystack – locating a single resource across regions and accounts. See every resource running in each stack with deep links to the AWS Console, actions performed by team members, Git-like diffs for infrastructure changes, and much more.

customers:
    - name: Snowflake
      link: /case-studies/snowflake
      logo: /logos/customers/snowflake-logo.svg
    - name: Mercedes-Benz Research and Development
      link: /case-studies/mercedes-benz/
      logo: /logos/customers/mercedes-benz-RDNA_logo.png
    - name: MindBody
      logo: /logos/customers/mindbody_logo.svg
    - name: National Institutes of Health
      logo: /logos/customers/nih.png
    - name: BMW
      link: /case-studies/bmw
      logo: /logos/customers/bmw.svg
    - name: Unity
      link: /case-studies/unity
      logo: /logos/customers/unity.png
    - name: Starburst
      link: /case-studies/starburst
      logo: /logos/customers/starburst.png

automation_api:
    header: Programmatic Infrastructure as Code
    body: Pulumi [Automation API](/automation/) exposes the full power of infrastructure as code through a programmatic interface, instead of through CLI commands. Automation API lets you use the Pulumi engine as an SDK, enabling you to create software that can create, update, configure, and destroy infrastructure dynamically. This enables you to build custom cloud interfaces that are tailored to your team, organization, or customers.
    cta: Learn More About Automation API
    link: /blog/automation-api/

crosswalk: 
    header: Use Well-Architected Practices
    body: Pulumi Crosswalk for AWS is a collection of libraries that use automatic well-architected best practices to make common infrastructure-as-code tasks in AWS easier and more secure. Secure and cost-conscious defaults are chosen so that simple programs automatically use best practices for the underlying infrastructure, enabling better productivity with confidence.
    points:
        - header: Deploy CDK Constructs with Pulumi
          body: You can deploy any AWS CDK construct from within a Pulumi deployment. If you're already using AWS CDK, you can now use Pulumi to orchestrate deployments instead of CloudFormation. This gives you [improved deployment speed](/case-studies/panther-labs/#proving-pulumis-advantages/) and integration with all features of Pulumi (like [Policy as Code](/docs/insights/policy/), [Audit Logs](/docs/pulumi-cloud/audit-logs/), Secrets, and much more).
        - header: Application and Infrastructure Together
          body: Crosswalk enables you to blur the lines between application and infrastructure code enabling you to author an entire full-stack application in one program. With support for inline Lambda functions and ease-of-use helper functions, building robust applications on AWS has never been easier.
    cta: Learn More About Crosswalk
    link: /docs/iac/clouds/aws/guides/

awsx:
    yaml: |
        name: aws-eks
        runtime: yaml
        description: An EKS cluster
        resources:
            cluster:
                type: eks:Cluster
                properties:
                    instanceType: "t2.medium"
                    desiredCapacity: 2
                    minSize: 1
                    maxSize: 2
        outputs:
            kubeconfig: ${cluster.kubeconfig}
    java: |
        package com.pulumi.example.eks;

        import com.pulumi.Context;
        import com.pulumi.Exports;
        import com.pulumi.Pulumi;
        import com.pulumi.core.Output;
        import com.pulumi.eks.Cluster;
        import com.pulumi.eks.ClusterArgs;

        import java.util.stream.Collectors;

        public class App {
            public static void main(String[] args) {
                Pulumi.run(App::stack);
            }

            private static Exports stack(Context ctx) {
                var cluster = new Cluster("my-cluster", ClusterArgs.builder()
                        .instanceType("t2.micro")
                        .desiredCapacity(2)
                        .minSize(1)
                        .maxSize(2)
                        .build());

                ctx.export("kubeconfig", cluster.kubeconfig());
                return ctx.exports();
            }
        }
    csharp: |
        using System;
        using System.Threading.Tasks;
        using Pulumi;
        using Pulumi.Eks.Cluster;

        class EksStack : Stack
        {
            public EksStack()
            {
                // Create an EKS cluster.
                var cluster = new Cluster("cluster", new ClusterArgs
                {
                    InstanceType = "t2.medium",
                    DesiredCapacity = 2,
                    MinSize = 1,
                    MaxSize = 2,
                });

                // Export the cluster's kubeconfig.
                this.Kubeconfig = cluster.Kubeconfig;
            }

            [Output("kubeconfig")]
            public Output<string> Kubeconfig { get; set; }
        }

        class Program
        {
            static Task<int> Main(string[] args) => Deployment.RunAsync<EksStack>();
        }
    go: |
        package main

        import (
            "github.com/pulumi/pulumi-eks/sdk/go/eks/cluster"
            "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
        )

        func main() {
            pulumi.Run(func(ctx *pulumi.Context) error {
            // Create an EKS cluster.
            cluster, err := cluster.NewCluster(ctx, "cluster",
                cluster.ClusterArgs{
                    InstanceType:    pulumi.String("t2.medium"),
                    DesiredCapacity: pulumi.Int(2),
                    MinSize:         pulumi.Int(1),
                    MaxSize:         pulumi.Int(2),
                },
            )
            if err != nil {
                return err
            }

            // Export the cluster's kubeconfig.
            ctx.Export("kubeconfig", cluster.Kubeconfig)

            return nil
            })
        }
    py: |
        import pulumi
        import pulumi_eks as eks

        # Create an EKS cluster.
        cluster = eks.Cluster(
            "cluster",
            instance_type="t2.medium",
            desired_capacity=2,
            min_size=1,
            max_size=2,
        )

        # Export the cluster's kubeconfig.
        pulumi.export("kubeconfig", cluster.kubeconfig)
    ts: |
       import * as eks from "@pulumi/eks";

        // Create an EKS cluster.
        const cluster = new eks.Cluster("cluster", {
            instanceType: "t2.medium",
            desiredCapacity: 2,
            minSize: 1,
            maxSize: 2,
        });

        // Export the cluster's kubeconfig.
        export const kubeconfig = cluster.kubeconfig;

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

contact_us_form:
    section_id: contact-us
    hubspot_form_id: 8a0e0f30-b43e-468e-98cc-6b5d481e8660
    headline: Need help with cloud-native infrastructure as code on AWS?
    quote:
        title: Learn how top engineering teams are using Pulumi's SDK to create, deploy, and manage AWS resources.
        name: Josh Imhoff
        name_title: Site Reliability Engineer, Cockroach Labs
        content: |
            We are building a distributed-database-as-a-service product that runs on Kubernetes clusters across
            multiple public clouds including Google Cloud, AWS and others. Pulumi's declarative model, the support for real
            programming languages, and the uniform workflow on any cloud make our SRE team much more efficient.
---
