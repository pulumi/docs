---
title: "Terragrunt Alternative | Pulumi"
meta_desc: Infrastructure as Code in any programming language. Manage infrastructure at scale without the complexity of wrapper tools.
layout: gads-template
block_external_search_index: true

heading: "Terragrunt Alternative"
subheading: |
    Pulumi is a free, open source infrastructure as code tool, and works best with Pulumi Cloud to
    make managing infrastructure secure, reliable, and hassle-free.

overview:
    title: Infrastructure as Code<br/>in any Programming Language
    description: |
        Looking for a Terragrunt alternative? Pulumi Cloud provides native support for managing infrastructure at scale using programming languages you know and love, without needing wrapper tools or complex configuration management.

key_features_above:
    items:
        - title: "Scale infrastructure natively without wrapper tools"
          sub_title: "Pulumi Infrastructure as Code Engine"
          description:
            Author infrastructure as code (IaC) using programming languages you know and love – including TypeScript/JavaScript, Python, Go, C#, Java, and YAML. Built-in support for stacks, configuration, and environments eliminates the need for wrapper tools.
          image: "/images/product/pulumi-iac-code.png"
          button:
            text: "Try Pulumi Cloud for FREE"
            link: "https://app.pulumi.com/signup?utm_source=gads-terragrunt"
          features:
              - title: Native stack management
                description: |
                    Manage multiple environments and configurations natively with Pulumi stacks, no wrapper tools needed.
                icon: code
                color: yellow
              - title: DRY infrastructure code
                description: |
                    Use real programming languages to create reusable components and eliminate code duplication naturally.
                icon: global
                color: yellow
              - title: Built-in state management
                description: |
                    Secure, reliable state management with automatic locking and encryption, no extra tooling required.
                icon: eye
                color: yellow
        
key_features:
    title: Key features
    items:
        - title: "Manage multiple environments with native stack support"
          sub_title: "Pulumi Stacks"
          description: |
            Deploy the same infrastructure code to multiple environments using Pulumi's native stack feature. Each stack maintains its own state and configuration, making it easy to manage dev, staging, and production environments.
          ide:
            - title: index.ts
              language: typescript
              code: |
                import * as pulumi from "@pulumi/pulumi";
                import * as aws from "@pulumi/aws";

                // Get configuration for the current stack
                const config = new pulumi.Config();
                const environment = pulumi.getStack();
                const instanceSize = config.require("instanceSize");

                // Create infrastructure that adapts to the environment
                const vpc = new aws.ec2.Vpc(`vpc-${environment}`, {
                    cidrBlock: config.get("vpcCidr") || "10.0.0.0/16",
                    enableDnsHostnames: true,
                    tags: {
                        Environment: environment,
                        ManagedBy: "Pulumi",
                    },
                });

                // Create different resources based on environment
                const instance = new aws.ec2.Instance(`web-${environment}`, {
                    instanceType: instanceSize,
                    ami: config.require("amiId"),
                    subnetId: vpc.publicSubnetIds[0],
                    tags: {
                        Environment: environment,
                        Name: `web-server-${environment}`,
                    },
                });

                // Export outputs
                export const vpcId = vpc.id;
                export const instanceId = instance.id;
            - title: __main__.py
              language: python
              code: |
                import pulumi
                from pulumi import Config
                import pulumi_aws as aws

                # Get configuration for the current stack
                config = Config()
                environment = pulumi.get_stack()
                instance_size = config.require("instanceSize")

                # Create infrastructure that adapts to the environment
                vpc = aws.ec2.Vpc(f"vpc-{environment}",
                    cidr_block=config.get("vpcCidr") or "10.0.0.0/16",
                    enable_dns_hostnames=True,
                    tags={
                        "Environment": environment,
                        "ManagedBy": "Pulumi",
                    })

                # Create different resources based on environment
                instance = aws.ec2.Instance(f"web-{environment}",
                    instance_type=instance_size,
                    ami=config.require("amiId"),
                    subnet_id=vpc.public_subnet_ids[0],
                    tags={
                        "Environment": environment,
                        "Name": f"web-server-{environment}",
                    })

                # Export outputs
                pulumi.export("vpcId", vpc.id)
                pulumi.export("instanceId", instance.id)
            - title: main.go
              language: go
              code: |
                    package main

                    import (
                      "fmt"
                      "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
                      "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
                      "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
                    )

                    func main() {
                      pulumi.Run(func(ctx *pulumi.Context) error {
                        // Get configuration for the current stack
                        cfg := config.New(ctx, "")
                        environment := ctx.Stack()
                        instanceSize := cfg.Require("instanceSize")

                        // Create infrastructure that adapts to the environment
                        vpc, err := ec2.NewVpc(ctx, fmt.Sprintf("vpc-%s", environment), &ec2.VpcArgs{
                          CidrBlock:           pulumi.String(cfg.Get("vpcCidr")),
                          EnableDnsHostnames:  pulumi.Bool(true),
                          Tags: pulumi.StringMap{
                            "Environment": pulumi.String(environment),
                            "ManagedBy":   pulumi.String("Pulumi"),
                          },
                        })
                        if err != nil {
                          return err
                        }

                        // Create different resources based on environment
                        instance, err := ec2.NewInstance(ctx, fmt.Sprintf("web-%s", environment), &ec2.InstanceArgs{
                          InstanceType: pulumi.String(instanceSize),
                          Ami:          pulumi.String(cfg.Require("amiId")),
                          SubnetId:     vpc.PublicSubnetIds.Index(pulumi.Int(0)),
                          Tags: pulumi.StringMap{
                            "Environment": pulumi.String(environment),
                            "Name":        pulumi.Sprintf("web-server-%s", environment),
                          },
                        })
                        if err != nil {
                          return err
                        }

                        // Export outputs
                        ctx.Export("vpcId", vpc.ID())
                        ctx.Export("instanceId", instance.ID())
                        return nil
                      })
                    }
            - title: MyStack.cs
              language: csharp
              code: |
                using System.Collections.Generic;
                using Pulumi;
                using Pulumi.Aws.Ec2;

                await Deployment.RunAsync(() =>
                {
                  // Get configuration for the current stack
                  var config = new Config();
                  var environment = Deployment.Instance.StackName;
                  var instanceSize = config.Require("instanceSize");

                  // Create infrastructure that adapts to the environment
                  var vpc = new Vpc($"vpc-{environment}", new VpcArgs
                  {
                    CidrBlock = config.Get("vpcCidr") ?? "10.0.0.0/16",
                    EnableDnsHostnames = true,
                    Tags = new Dictionary<string, string>
                    {
                      ["Environment"] = environment,
                      ["ManagedBy"] = "Pulumi"
                    }
                  });

                  // Create different resources based on environment
                  var instance = new Instance($"web-{environment}", new InstanceArgs
                  {
                    InstanceType = instanceSize,
                    Ami = config.Require("amiId"),
                    SubnetId = vpc.PublicSubnetIds.Apply(ids => ids[0]),
                    Tags = new Dictionary<string, string>
                    {
                      ["Environment"] = environment,
                      ["Name"] = $"web-server-{environment}"
                    }
                  });

                  // Export outputs
                  return new Dictionary<string, object?>
                  {
                    ["vpcId"] = vpc.Id,
                    ["instanceId"] = instance.Id
                  };
                });
            - title: Main.Java
              language: java
              code: |
                import com.pulumi.Context;
                import com.pulumi.Pulumi;
                import com.pulumi.Config;
                import com.pulumi.aws.ec2.Vpc;
                import com.pulumi.aws.ec2.VpcArgs;
                import com.pulumi.aws.ec2.Instance;
                import com.pulumi.aws.ec2.InstanceArgs;

                public class App {
                    public static void main(String[] args) {
                        Pulumi.run(App::stack);
                    }

                    private static void stack(Context ctx) {
                    // Get configuration for the current stack
                    var config = ctx.config();
                    var environment = ctx.stackName();
                    var instanceSize = config.require("instanceSize");

                    // Create infrastructure that adapts to the environment
                    var vpc = new Vpc(String.format("vpc-%s", environment), VpcArgs.builder()
                        .cidrBlock(config.get("vpcCidr").orElse("10.0.0.0/16"))
                        .enableDnsHostnames(true)
                        .tags(Map.of(
                            "Environment", environment,
                            "ManagedBy", "Pulumi"
                        ))
                        .build());

                    // Create different resources based on environment
                    var instance = new Instance(String.format("web-%s", environment), InstanceArgs.builder()
                        .instanceType(instanceSize)
                        .ami(config.require("amiId"))
                        .subnetId(vpc.publicSubnetIds().applyValue(ids -> ids.get(0)))
                        .tags(Map.of(
                            "Environment", environment,
                            "Name", String.format("web-server-%s", environment)
                        ))
                        .build());

                    // Export outputs
                    ctx.export("vpcId", vpc.id());
                    ctx.export("instanceId", instance.id());
                  }
                }
            - title: Pulumi.yaml
              language: yaml
              code: |
                config:
                  instanceSize:
                    type: string
                  amiId:
                    type: string
                  vpcCidr:
                    type: string
                    default: "10.0.0.0/16"
                
                resources:
                  vpc:
                    type: aws:ec2:Vpc
                    properties:
                      cidrBlock: ${vpcCidr}
                      enableDnsHostnames: true
                      tags:
                        Environment: ${pulumi.stack}
                        ManagedBy: Pulumi
                  
                  webInstance:
                    type: aws:ec2:Instance
                    properties:
                      instanceType: ${instanceSize}
                      ami: ${amiId}
                      subnetId: ${vpc.publicSubnetIds[0]}
                      tags:
                        Environment: ${pulumi.stack}
                        Name: web-server-${pulumi.stack}
                
                outputs:
                  vpcId: ${vpc.id}
                  instanceId: ${webInstance.id}
          button:
            text: "Try Pulumi Cloud for FREE"
            link: "https://app.pulumi.com/signup?utm_source=gads-terragrunt"
          features:
              - title: Native multi-environment support
                description: |
                    Manage dev, staging, and production with built-in stack support, no wrapper tools needed.
              - title: Configuration management
                description: |
                    Built-in configuration system with secrets encryption, environment variables, and stack-specific settings.
              - title: Remote backend locking
                description: |
                    Automatic state locking prevents concurrent modifications without additional tooling.

        - title: "Eliminate code duplication with real programming languages"
          sub_title: "Component Resources"
          description: |
            Create reusable infrastructure components using real programming language features like functions, classes, and packages. Share components across teams through standard package managers.
          image: "/images/product/pulumi-cicd.png"
          button:
            text: "Try Pulumi Cloud for FREE"
            link: "https://app.pulumi.com/signup?utm_source=gads-terragrunt"
          features:
              - title: True code reusability
                description: |
                    Use functions, classes, and modules to create truly reusable infrastructure components.
              - title: Package management
                description: |
                    Distribute infrastructure components through npm, PyPI, NuGet, Maven, or Go modules.
              - title: Type safety
                description: |
                    Catch configuration errors at compile time with strongly-typed infrastructure code.

stats:
    title: Open source. Enterprise ready.
    description: |
        Pulumi's Infrastructure as Code CLI and SDK is an open-source project that's supported
        by an active community. We maintain a public roadmap and welcome feedback and contributions.
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
        - title: "Enterprise-grade infrastructure management without the complexity"
          sub_title: "Pulumi Cloud"
          description: |
             A fully-managed service for Pulumi IaC that provides everything Terragrunt adds to Terraform, but natively integrated. Manage state, secrets, team collaboration, and compliance without wrapper tools or complex configurations.
          image: "/images/product/pulumi-cloud-iac-stylized-01.png"
          button:
            text: "Try Pulumi Cloud for FREE"
            link: "https://app.pulumi.com/signup?utm_source=gads-terragrunt"
          features:
              - title: Pulumi IaC
                description: |
                    Open-source IaC with native support for multiple environments, DRY principles, and remote state management.
              - title: Pulumi ESC
                description: |
                    Centralized secrets and configuration management across all environments and stacks.
              - title: Stack dependencies
                description: |
                    Reference outputs from one stack in another, enabling modular infrastructure architectures.
              - title: Drift detection
                description: |
                    Automatically detect when infrastructure has drifted from desired state.
              - title: Pulumi Automation API
                description: |
                    Build custom infrastructure automation workflows programmatically.
              - title: Stack policies
                description: |
                    Enforce governance and compliance policies across all stacks and environments.
              - title: Team collaboration
                description: |
                    Built-in RBAC, stack permissions, and collaborative features for teams.
              - title: Deployment orchestration
                description: |
                    Coordinate deployments across multiple stacks with deployment workflows.
              - title: Audit logs
                description: |
                    Complete audit trail of all infrastructure changes across all environments.

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