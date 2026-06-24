---
title: "Infrastructure as code in Any Language – Pulumi IaC"
meta_desc: Write infrastructure code using TypeScript, Python, Go, .NET, Java, or YAML. Deploy to any cloud with built-in previews and testing.
meta_image: /images/product/infrastructure-as-code/iac-meta.png
type: page
layout: product-page
aliases:
  - /product/iac
  - /product/pulumi-iac

sections:
  - type: hero
    title_primary: Infrastructure as code
    title_secondary: in any language.
    description: |
      Use the programming languages you already know to build infrastructure on AWS, Azure, Google Cloud, Kubernetes, and hundreds more providers.
    anchor: hero
    code_overlay_image: /images/product/infrastructure-as-code/iac-hero-code-overlay.svg
    code_aspect_ratio: "858/500"
    code_visual_max_width: 860px
    code_offsets:
      top: "0%"
      right: "28.5%"
      bottom: "30%"
      left: "0%"
    code_title: "index.ts"
    code_snippets:
      - language: typescript
        label: TypeScript
        title: "index.ts"
        code: |
          import * as pulumi from "@pulumi/pulumi";
          import * as aws from "@pulumi/aws";

          const bucket = new aws.s3.Bucket("my-bucket");

          export const bucketName = bucket.id;
      - language: python
        label: Python
        title: "__main__.py"
        code: |
          import pulumi
          from pulumi_aws import s3

          bucket = s3.Bucket("my-bucket")

          pulumi.export("bucketName", bucket.id)
      - language: go
        label: Go
        title: "main.go"
        code: |
          package main

          import (
            "github.com/pulumi/pulumi-aws/sdk/v3/go/aws/s3"
            "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
          )

          func main() {
            pulumi.Run(func(ctx *pulumi.Context) error {
              bucket, err := s3.NewBucket(ctx, "my-bucket", nil)
              if err != nil {
                return err
              }
              ctx.Export("bucketName", bucket.ID())
              return nil
            })
          }
      - language: csharp
        label: C#
        title: "MyStack.cs"
        code: |
          using Pulumi;
          using Pulumi.Aws.S3;

          class MyStack : Stack
          {
              public MyStack()
              {
                  var bucket = new Bucket("my-bucket");
                  this.BucketName = bucket.Id;
              }

              [Output]
              public Output<string> BucketName { get; set; }
          }
      - language: java
        label: Java
        title: "App.java"
        code: |
          package s3site;

          import com.pulumi.Context;
          import com.pulumi.Pulumi;
          import com.pulumi.core.Output;
          import com.pulumi.aws.s3.Bucket;

          public class Infra {
              public static void main(String[] args) {
                  Pulumi.run(Infra::stack);
              }

              private static void stack(Context ctx) {
                  final var myBucket = new Bucket("my-bucket");
                  ctx.export("bucketName",
                      myBucket.bucketDomainName());
              }
          }
      - language: yaml
        label: YAML
        title: "Pulumi.yaml"
        code: |
          name: my-stack
          runtime: yaml
          resources:
              bucket:
                  type: aws:s3:Bucket
          outputs:
              bucketName: ${bucket.id}

  - type: feature_split
    heading: Write infrastructure code in your favorite language
    description: |
      TypeScript/JavaScript, Python, Go, C#, Java, and YAML. Get autocomplete, type checking, and all your favorite IDE features.

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
      Get started with Pulumi Cloud for free, state management and secrets included. Our [open source engine](https://github.com/pulumi/pulumi) powers everything underneath. Scale to enterprise features when you need them, and run the same platform [fully self-hosted](/product/self-hosted/) in your own cloud or data center.
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
    icon_style: black
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
    icon_style: black
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
          Integrates with [any CI/CD system](/docs/iac/packages-and-automation/continuous-delivery/). GitHub Actions, GitLab, Jenkins, CircleCI – your choice. Or use the [Kubernetes operator](/docs/iac/packages-and-automation/continuous-delivery/pulumi-kubernetes-operator/) for GitOps.

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
    icon_style: black
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
      - icon: buildings
        title: Self-host the whole platform
        description: |
          Run all of Pulumi Cloud in your own cloud account or data center. Full control over data, identity, and network, including air-gapped deployments. [Learn about self-hosting](/product/self-hosted/).
---
