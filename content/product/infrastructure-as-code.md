---
title: Infrastructure as Code
meta_desc: Write infrastructure as code in any programming language. The open source foundation of Pulumi - free forever.
layout: infrastructure-as-code
aliases:
    - /product/iac

heading: Infrastructure as Code
subheading: |
    Write infrastructure in real programming languages.<br>
    TypeScript, Python, Go, C#, Java, or YAML. Your choice.

overview:
    title: The Open Source Foundation
    description: |
        Pulumi's infrastructure as code engine is **100% open source and free forever**. Write infrastructure using programming languages you already know. Deploy to AWS, Azure, Google Cloud, Kubernetes, and thousands of providers. Self-manage your state or use Pulumi Cloud for team collaboration.

why_real_languages:
    title: Why Real Programming Languages?
    items:
        - title: "Your IDE Already Works"
          description: "Autocomplete, type checking, inline docs, refactoring. No custom tooling required."
          
        - title: "Use Real Logic"
          description: "Loops, conditionals, functions, classes. No more copy-paste. No more string interpolation hell."
          
        - title: "Test Like Software"
          description: "Unit tests, integration tests, property tests. Catch errors at compile time, not runtime."
          
        - title: "Share and Reuse"
          description: "Package infrastructure as libraries. Share via npm, PyPI, NuGet, or any package manager."

key_features:
    title: Core Capabilities
    items:
        - title: "Multi-Language Support"
          sub_title: "Use the language that fits your team"
          description: |
            Write infrastructure in TypeScript, Python, Go, C#, Java, or YAML. Same infrastructure model, different syntax. Pick what works for you.
          ide:
            - title: TypeScript
              language: typescript
              code: |
                import * as aws from "@pulumi/aws";

                const bucket = new aws.s3.Bucket("my-bucket", {
                    website: {
                        indexDocument: "index.html",
                    },
                });

                export const url = bucket.websiteEndpoint;
            - title: Python
              language: python
              code: |
                import pulumi
                import pulumi_aws as aws

                bucket = aws.s3.Bucket("my-bucket",
                    website=aws.s3.BucketWebsiteArgs(
                        index_document="index.html",
                    ))

                pulumi.export("url", bucket.website_endpoint)
            - title: Go
              language: go
              code: |
                package main

                import (
                    "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
                    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
                )

                func main() {
                    pulumi.Run(func(ctx *pulumi.Context) error {
                        bucket, err := s3.NewBucket(ctx, "my-bucket", &s3.BucketArgs{
                            Website: &s3.BucketWebsiteArgs{
                                IndexDocument: pulumi.String("index.html"),
                            },
                        })
                        if err != nil {
                            return err
                        }
                        ctx.Export("url", bucket.WebsiteEndpoint)
                        return nil
                    })
                }
            - title: C#
              language: csharp
              code: |
                using Pulumi;
                using Pulumi.Aws.S3;

                return await Deployment.RunAsync(() =>
                {
                    var bucket = new Bucket("my-bucket", new BucketArgs
                    {
                        Website = new BucketWebsiteArgs
                        {
                            IndexDocument = "index.html",
                        },
                    });

                    return new Dictionary<string, object?>
                    {
                        ["url"] = bucket.WebsiteEndpoint,
                    };
                });
            - title: YAML
              language: yaml
              code: |
                resources:
                  my-bucket:
                    type: aws:s3:Bucket
                    properties:
                      website:
                        indexDocument: index.html
                outputs:
                  url: ${my-bucket.websiteEndpoint}
          
        - title: "Any Cloud Provider"
          sub_title: "One workflow for everything"
          description: |
            Deploy to AWS, Azure, Google Cloud, Kubernetes, Cloudflare, DigitalOcean, and [thousands more providers](/registry/). Same CLI, same workflow, same great experience.
          features:
              - title: Native providers
                description: "Full API coverage with same-day updates for major clouds"
              - title: Kubernetes native
                description: "Deploy and manage Kubernetes resources alongside cloud infrastructure"
              - title: Cloud agnostic
                description: "Mix and match providers in a single program"

        - title: "Components and Packages"
          sub_title: "Build once, reuse everywhere"
          description: |
            Create higher-level abstractions that encapsulate best practices. Share them across teams via package managers.
          features:
              - title: Multi-language packages
                description: "Write in one language, use from any language"
              - title: Versioned and typed
                description: "Semantic versioning with full type safety"
              - title: Standard distribution
                description: "Share via npm, PyPI, NuGet, or any package registry"

how_it_works:
    title: How It Works
    description: |
        1. **Write** - Define infrastructure in your favorite programming language
        2. **Preview** - See exactly what will change before you deploy
        3. **Deploy** - Update your infrastructure with a single command
        4. **Manage** - Track state locally or with Pulumi Cloud

open_source:
    title: Proudly Open Source
    description: |
        Pulumi IaC is developed in the open on [GitHub](https://github.com/pulumi/pulumi). Join thousands of contributors making infrastructure better for everyone.
    stats:
        - number: "20k+"
          label: "GitHub Stars"
        - number: "10k+"
          label: "Community Members"
        - number: "1000s"
          label: "Companies Using Pulumi"

with_pulumi_cloud:
    title: Better Together with Pulumi Cloud
    description: |
        While Pulumi IaC is powerful on its own, Pulumi Cloud makes it even better for teams:
        
        • **Managed State** - Never worry about corrupted state files
        • **Secrets Management** - Built-in encryption for sensitive data
        • **Team Collaboration** - RBAC, audit logs, and deployment history
        • **Policy Enforcement** - Ensure compliance before deployment
        
        Free for individuals, with team plans starting at $1 per resource.
    cta_text: "Try Pulumi Cloud"
    cta_link: "https://app.pulumi.com/signup"

get_started:
    title: Getting started

    get_started:
        title: Install the open source CLI
        description: |
            Download Pulumi and deploy your first infrastructure in minutes. Works on macOS, Linux, and Windows.
        cta_text: Download Pulumi

    migrate:
        title: Coming from Terraform?
        description: |
            Convert your existing HCL to real programming languages. Import existing resources. Run side-by-side.
        cta_text: Migration Guide
---