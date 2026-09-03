---
title: "Infrastructure as code in Any Language – Pulumi IaC"
meta_desc: Write infrastructure code using TypeScript, Python, Go, .NET, Java, YAML, or HCL. Deploy to any cloud with built-in previews and testing.
meta_image: /images/product/infrastructure-as-code/iac-meta.png
type: page
layout: template-page
include_floqer: true
aliases:
  - /product/iac
  - /product/pulumi-iac

sections:
  - type: hero
    title: "*Infrastructure as code* <br>in any language."
    description: |
      Use the programming languages you already know to build infrastructure on AWS, Azure, Google Cloud, Kubernetes, and hundreds more providers.
    anchor: hero
    code_overlay_image: /images/product/infrastructure-as-code/iac-hero-code-overlay.svg
    code_aspect_ratio: "666/513"
    code_visual_max_width: 700px
    code_offsets:
      top: "0%"
      right: "0%"
      left: "23%"
      bottom: "30%"
    code_title: "index.ts"
    code_snippets:
      - language: typescript
        label: TypeScript
        title: "index.ts"
        code: |
          import * as aws from "@pulumi/aws";
          import * as awsx from "@pulumi/awsx";

          const vpc = new awsx.ec2.Vpc("vpc");
          const azs = await aws.getAvailabilityZones({ state: "available" });

          const subnets = azs.names.map((az, i) =>
            new aws.ec2.Subnet(`subnet-${i}`, {
              vpcId: vpc.vpcId,
              cidrBlock: `10.0.${i}.0/24`,
              availabilityZone: az,
            })
          );

      - language: python
        label: Python
        title: "__main__.py"
        code: |
          import pulumi_aws as aws
          import pulumi_awsx as awsx

          azs = aws.get_availability_zones(state="available")
          vpc = awsx.ec2.Vpc("vpc")

          for i, az in enumerate(azs.names):
              aws.ec2.Subnet(f"subnet-{i}",
                  vpc_id=vpc.vpc_id,
                  cidr_block=f"10.0.{i}.0/24",
                  availability_zone=az,
              )

      - language: go
        label: Go
        title: "main.go"
        code: |
          package main

          import (
              "fmt"

              "github.com/pulumi/pulumi-aws/sdk/v6/go/aws"
              "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
              awsx "github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
              "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
          )

          func main() {
              pulumi.Run(func(ctx *pulumi.Context) error {
                  vpc, _ := awsx.NewVpc(ctx, "vpc", nil)
                  azs, _ := aws.GetAvailabilityZones(ctx, &aws.GetAvailabilityZonesArgs{State: pulumi.StringRef("available")}, nil)

                  for i, az := range azs.Names {
                      ec2.NewSubnet(ctx, fmt.Sprintf("subnet-%d", i), &ec2.SubnetArgs{
                          VpcId:            vpc.VpcId,
                          CidrBlock:        pulumi.String(fmt.Sprintf("10.0.%d.0/24", i)),
                          AvailabilityZone: pulumi.String(az),
                      })
                  }
                  return nil
              })
          }

      - language: csharp
        label: C#
        title: "MyStack.cs"
        code: |
          using System.Linq;
          using Pulumi;
          using Pulumi.Aws;
          using Pulumi.Aws.Ec2;

          return await Deployment.RunAsync(() =>
          {
              var vpc = new Pulumi.Awsx.Ec2.Vpc("vpc");
              var azs = GetAvailabilityZones.Invoke(new() { State = "available" });

              var subnets = azs.Apply(result =>
                  result.Names.Select((az, i) =>
                      new Subnet($"subnet-{i}", new()
                      {
                          VpcId = vpc.VpcId,
                          CidrBlock = $"10.0.{i}.0/24",
                          AvailabilityZone = az,
                      })
                  ).ToList()
              );
          });

      - language: java
        label: Java
        title: "App.java"
        code: |
          package myproject;

          import com.pulumi.Pulumi;
          import com.pulumi.aws.ec2.Vpc;
          import com.pulumi.aws.ec2.Subnet;
          import com.pulumi.aws.ec2.SubnetArgs;
          import com.pulumi.aws.AwsFunctions;
          import com.pulumi.aws.inputs.GetAvailabilityZonesPlainArgs;

          public class App {
              public static void main(String[] args) {
                  Pulumi.run(ctx -> {
                      var vpc = new Vpc("vpc");

                      var azs = AwsFunctions.getAvailabilityZonesPlain(
                          GetAvailabilityZonesPlainArgs.builder()
                              .state("available")
                              .build()
                      ).join();

                      var names = azs.names();
                      for (int i = 0; i < names.size(); i++) {
                          new Subnet("subnet-" + i, SubnetArgs.builder()
                              .vpcId(vpc.id())
                              .cidrBlock("10.0." + i + ".0/24")
                              .availabilityZone(names.get(i))
                              .build());
                      }
                  });
              }
          }

      - language: hcl
        label: HCL
        title: "main.tf"
        code: |
          terraform {
            required_providers {
              aws = {
                source  = "pulumi/aws"
              }
              awsx = {
                source  = "pulumi/awsx"
              }
            }
          }

          resource "awsx_ec2_vpc" "vpc" {}

          data "aws_availability_zones" "available" {
            state = "available"
          }

          resource "aws_subnet" "subnet" {
            count             = length(data.aws_availability_zones.available.names)
            vpc_id            = awsx_ec2_vpc.vpc.vpc_id
            cidr_block        = "10.0.${count.index}.0/24"
            availability_zone = data.aws_availability_zones.available.names[count.index]
          }

      - language: yaml
        label: YAML
        title: "Pulumi.yaml"
        code: |
          variables:
            azs:
              fn::invoke:
                function: aws:getAvailabilityZones
                arguments:
                  state: available

          resources:
            vpc:
              type: awsx:ec2:Vpc

            subnet-0:
              type: aws:ec2:Subnet
              properties:
                vpcId: ${vpc.vpcId}
                cidrBlock: "10.0.0.0/24"
                availabilityZone: ${azs.names[0]}

            subnet-1:
              type: aws:ec2:Subnet
              properties:
                vpcId: ${vpc.vpcId}
                cidrBlock: "10.0.1.0/24"
                availabilityZone: ${azs.names[1]}

  - type: feature_split
    heading: Write infrastructure code in your favorite language
    description: |
      TypeScript/JavaScript, Python, Go, .NET, Java, YAML, and HCL. Get autocomplete, type checking, and all your favorite IDE features.
      Build on AWS, Azure, Google Cloud, Kubernetes, and hundreds of other providers. Our open source engine is Apache 2.0 licensed and will always be free.
    cards:
      - icon: code
        title: Use real code, not DSLs
        description: |
          Write infrastructure with loops, conditionals, functions, and classes. Reuse code, catch errors at compile time, and refactor with confidence.
      - icon: cloud
        title: Build on any cloud
        description: |
          Access AWS, Azure, Google Cloud, Kubernetes, and hundreds of providers through a unified, consistent API. Same-day updates for new cloud features.
      - icon: check
        title: Test before you ship
        description: |
          Preview changes before deploying them. Write unit tests for your infrastructure. Run integration tests against ephemeral environments.
    anchor: languages

  - type: section_header
    title: Open source core.
    title_line_2: Pulumi Cloud built-in.
    description: |
      Get started with Pulumi Cloud for free, state management and secrets included. Our [open source engine](https://github.com/pulumi/pulumi) powers everything underneath. Scale to enterprise features when you need them, or self-host if required.
    image: /images/product/infrastructure-as-code/pulumi-concentric-circles.svg
    image_alt: Open source core and Pulumi Cloud
    image_above: true
    anchor: open-source

  - type: counter_cards
    anchor: stats
    cards:
      - number: "350,000+"
        label: engineers building with Pulumi
      - number: "4,000+"
        label: companies in production
      - number: "300+"
        label: cloud and service providers

  - type: testimonial
    quote: |
      Our developers needed a fast, modular, and testable platform for managing cloud infrastructure. Nothing is better than having standard programming languages for building and managing infrastructure.
    author: Austin Byers
    title: Principal Platform Engineer
    company: Panther Labs
    logo: /logos/customers/panther.svg
    anchor: testimonial

  - type: section_header_with_code
    tag_line: Infrastructure building blocks
    title: "Ship faster with  \nreusable components"
    description: |
      Create reusable infrastructure components that can be used in any language. Package common patterns once and use them everywhere. Publish your components to the Pulumi Registry, npm, PyPI, NuGet, or any package manager.
    cta_text: Learn more about Pulumi components
    cta_link: /docs/iac/concepts/components
    code_title: "index.ts"
    code_snippets:
      - language: typescript
        label: TypeScript
        title: "index.ts"
        code: |
          import * as awsx from "@pulumi/awsx";

          const vpc = new awsx.ec2.Vpc("vpc", {
              subnetSpecs: [
                  { type: awsx.ec2.SubnetType.Public, cidrMask: 22 },
                  { type: awsx.ec2.SubnetType.Private, cidrMask: 20 },
              ],
          }, { protect: true });

          export const vpcId = vpc.vpcId;
          export const privateSubnetIds = vpc.privateSubnetIds;
          export const publicSubnetIds = vpc.publicSubnetIds;
      - language: python
        label: Python
        title: "__main__.py"
        code: |
          import pulumi
          import pulumi_awsx as awsx

          vpc = awsx.ec2.Vpc("vpc",
              awsx.ec2.VpcArgs(
                  subnet_specs=[
                      awsx.ec2.SubnetSpecArgs(type=awsx.ec2.SubnetType.PUBLIC, cidr_mask=22),
                      awsx.ec2.SubnetSpecArgs(type=awsx.ec2.SubnetType.PRIVATE, cidr_mask=20),
                  ],
              ),
              opts=pulumi.ResourceOptions(protect=True),
          )

          pulumi.export("vpcId", vpc.vpc_id)
          pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
          pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
      - language: go
        label: Go
        title: "main.go"
        code: |
          package main

          import (
              "github.com/pulumi/pulumi-awsx/sdk/v3/go/awsx/ec2"
              "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
          )

          func main() {
              pulumi.Run(func(ctx *pulumi.Context) error {
                  vpc, err := ec2.NewVpc(ctx, "vpc", &ec2.VpcArgs{
                      SubnetSpecs: []ec2.SubnetSpecArgs{
                          {Type: ec2.SubnetTypePublic, CidrMask: pulumi.IntRef(22)},
                          {Type: ec2.SubnetTypePrivate, CidrMask: pulumi.IntRef(20)},
                      },
                  }, pulumi.Protect(true))
                  if err != nil {
                      return err
                  }

                  ctx.Export("vpcId", vpc.VpcId)
                  ctx.Export("privateSubnetIds", vpc.PrivateSubnetIds)
                  ctx.Export("publicSubnetIds", vpc.PublicSubnetIds)
                  return nil
              })
          }
      - language: csharp
        label: C#
        title: "Program.cs"
        code: |
          using Pulumi;
          using System.Collections.Generic;
          using Pulumi.Awsx.Ec2.Inputs;
          using Ec2 = Pulumi.Awsx.Ec2;

          return await Deployment.RunAsync(() =>
          {
              var vpc = new Ec2.Vpc("vpc", new()
              {
                  SubnetSpecs =
                  {
                      new SubnetSpecArgs { Type = Ec2.SubnetType.Public, CidrMask = 22 },
                      new SubnetSpecArgs { Type = Ec2.SubnetType.Private, CidrMask = 20 },
                  },
              }, new ComponentResourceOptions { Protect = true });

              return new Dictionary<string, object?>
              {
                  ["vpcId"] = vpc.VpcId,
                  ["privateSubnetIds"] = vpc.PrivateSubnetIds,
                  ["publicSubnetIds"] = vpc.PublicSubnetIds,
              };
          });
      - language: java
        label: Java
        title: "App.java"
        code: |
          package myproject;

          import java.util.Arrays;
          import com.pulumi.Pulumi;
          import com.pulumi.awsx.ec2.Vpc;
          import com.pulumi.awsx.ec2.VpcArgs;
          import com.pulumi.awsx.ec2.enums.SubnetType;
          import com.pulumi.awsx.ec2.inputs.SubnetSpecArgs;
          import com.pulumi.resources.ComponentResourceOptions;

          public class App {
              public static void main(String[] args) {
                  Pulumi.run(ctx -> {
                      var vpc = new Vpc("vpc",
                          VpcArgs.builder()
                              .subnetSpecs(Arrays.asList(
                                  SubnetSpecArgs.builder().type(SubnetType.Public).cidrMask(22).build(),
                                  SubnetSpecArgs.builder().type(SubnetType.Private).cidrMask(20).build()
                              ))
                              .build(),
                          ComponentResourceOptions.builder().protect(true).build());

                      ctx.export("vpcId", vpc.vpcId());
                      ctx.export("privateSubnetIds", vpc.privateSubnetIds());
                      ctx.export("publicSubnetIds", vpc.publicSubnetIds());
                  });
              }
          }
    anchor: packages

  - type: three_column
    anchor: packages-features
    icon_layout: above
    columns:
      - icon: check-square
        title: Production-ready patterns
        description: |
          Ship EKS clusters, serverless apps, or entire platforms with one line of code using well-architected components.
      - icon: squares-four
        title: Hundreds of providers
        description: |
          Full API coverage for AWS, Azure, Google Cloud, Kubernetes, plus Cloudflare, Datadog, GitHub, and hundreds more.
      - icon: rocket
        title: From VMs to Kubernetes
        description: |
          Manage traditional infrastructure, containers, serverless, and Kubernetes with one tool, one workflow.

  - type: icon_grid
    tag_line: GitOps & CI/CD Native
    title: Ship infrastructure
    title_line_2: like software
    description: |
      Infrastructure as code means infrastructure in Git. Review changes in pull requests. Run tests in CI. Ship through GitHub Actions, GitLab, Jenkins, or any CI/CD system.
    image: /images/product/infrastructure-as-code/iac-logos.svg
    image_alt: GitOps and CI/CD tools
    anchor: gitops

  - type: three_column
    anchor: cicd-features
    icon_layout: above
    columns:
      - icon: git-branch
        title: Git-native workflow
        description: |
          Every infrastructure change is a pull request. Review, comment, approve. Full audit trail built in.
      - icon: bug
        title: Catch bugs before production
        description: |
          Run [unit tests](/docs/iac/guides/testing/unit/) in milliseconds. Spin up ephemeral environments for [integration tests](/docs/iac/guides/testing/integration/). Fail fast, fix fast.
      - icon: gear-six
        title: Works with your CI/CD
        description: |
          Integrates with [any CI/CD system](/docs/iac/operations/continuous-delivery/). GitHub Actions, GitLab, Jenkins, CircleCI – your choice. Or use the [Kubernetes operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) for GitOps.

  - type: section_header
    title: Scale confidently with Pulumi Cloud
    description: |
      Encrypted state storage, secrets management, and collaboration built in. When you scale, enterprise features like RBAC, policy enforcement, and SSO are ready. All powered by our open source engine.
    image: /images/product/infrastructure-as-code/iac-stack-example.svg
    image_alt: Pulumi Cloud dashboard
    image_visible_from: md
    anchor: scale

  - type: three_column
    anchor: cloud-features
    icon_layout: above
    columns:
      - icon: lock
        title: Encrypted state management
        description: |
          Never lose state again. Automatic versioning and encryption at rest. Pulumi Cloud handles it all, or self-host with S3/Azure Blob.
      - icon: key
        title: Built-in secrets management
        description: |
          No more secrets in plaintext. Automatic encryption for sensitive values. Integrate with AWS Secrets Manager, Azure Key Vault, or use [Pulumi ESC](/product/secrets-management/) for centralized secrets.
      - icon: check-circle
        title: Ship with confidence
        description: |
          Review every change before it ships. Full history and audit logs. Roll back to any previous state when needed.
      - icon: globe
        title: See everything, everywhere
        description: |
          Unified view across all your clouds. Search across AWS, Azure, and GCP. Find that rogue EC2 instance in seconds.
      - icon: plug
        title: Automation API
        description: |
          Infrastructure as code as a library. Embed Pulumi in your app. Build custom CLIs, portals, or platforms. Full programmatic control.
      - icon: users
        title: Self-service infrastructure
        description: |
          Let engineers provision their own infrastructure safely. Templates, guardrails, and approval workflows. Works with Backstage or build your own.
      - icon: shield-check
        title: Enterprise SSO & RBAC
        description: |
          SAML, SCIM, GitHub, GitLab, Atlassian. Fine-grained permissions. Temporary access tokens. SOC 2 Type II compliant.
      - icon: gavel
        title: Policy as code
        description: |
          Enforce security and compliance automatically. Hundreds of built-in policies or write your own. Block non-compliant infrastructure before it ships.
      - icon: clock-counter-clockwise
        title: Complete audit trail
        description: |
          Every action logged. Who changed what, when, and why. Export to SIEM. Compliance reports at your fingertips.
---