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

key_features_above:
    items:
        - title: "Write in Any Language, Deploy to Any Cloud"
          sub_title: "Real programming languages for real infrastructure"
          description: |
            Use TypeScript, Python, Go, C#, Java, or YAML to define infrastructure. Get autocomplete, type checking, and all the power of your favorite programming language. Deploy to AWS, Azure, Google Cloud, Kubernetes, and [thousands of providers](/registry/).
          button:
            text: "Browse language docs"
            link: "/docs/languages-sdks/"
          features:
              - title: Your IDE already works
                description: |
                    Autocomplete, type checking, inline docs, refactoring. No custom tooling required.
                icon: code
                color: yellow
              - title: Use real logic
                description: |
                    Loops, conditionals, functions, classes. No more copy-paste. No more string interpolation hell.
                icon: cycle
                color: yellow
              - title: Test like software
                description: |
                    Unit tests, integration tests, property tests. Catch errors at compile time, not runtime.
                icon: testing
                color: yellow

key_features:
    title: Core Capabilities
    items:
        - title: "Multi-Language Support"
          sub_title: "Use the language that fits your team"
          description: |
            Write infrastructure in TypeScript, Python, Go, C#, Java, or YAML. Same infrastructure model, different syntax. Pick what works for you.
          button:
            text: "Learn more about languages"
            link: "/docs/languages-sdks/"
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
          features:
              - title: Multi-language packages
                description: "Write in one language, use from any language"
              - title: Versioned and typed
                description: "Semantic versioning with full type safety"
              - title: Standard distribution
                description: "Share via npm, PyPI, NuGet, or any package registry"

        - title: "Components and Packages"
          sub_title: "Build once, reuse everywhere"
          description: |
            Create higher-level abstractions that encapsulate best practices. Share them across teams via package managers. Build reusable cloud architectures.
          button:
            text: "Explore packages"
            link: "/registry/"
          image: "/images/product/pulumi-packages.png"
          features:
              - title: Native cloud providers
                description: "Full API coverage for AWS, Azure, Google Cloud, and Kubernetes with same-day updates"
              - title: Crosswalk for AWS
                description: "Adopt well-architected best practices for your infrastructure easily"
              - title: Cloud agnostic
                description: "Mix and match providers in a single program"

        - title: "CI/CD Integration"
          sub_title: "Deploy through your existing pipelines"
          description: |
            Integrate with GitHub Actions, GitLab, CircleCI, Jenkins, and more. Preview infrastructure changes in pull requests. Deploy on merge.
          button:
            text: "View integrations"
            link: "/docs/iac/packages-and-automation/continuous-delivery/"
          image: "/images/product/pulumi-cicd.png"
          features:
              - title: Version and review
                description: "Manage infrastructure code in Git and approve changes through pull requests"
              - title: Shift left
                description: "Get rapid feedback with unit tests and preview deployments"
              - title: GitOps ready
                description: "Deploy using GitOps patterns with the Pulumi Kubernetes Operator"

stats:
    title: Proudly Open Source
    description: |
        Pulumi IaC is developed in the open on [GitHub](https://github.com/pulumi/pulumi). Join thousands of contributors making infrastructure better for everyone.
    community:
        number: "20k+"
        description: GitHub Stars
    company:
        number: "10k+"
        description: Community Members
    integration:
        number: "1000s"
        description: Companies Using Pulumi

key_features_below:
    items:
        - title: "Better Together with Pulumi Cloud"
          sub_title: "The easiest way to use Pulumi at scale"
          description: |
            While Pulumi IaC is powerful on its own, Pulumi Cloud makes it even better for teams. Get managed state storage, secrets encryption, team collaboration, policy enforcement, and more. Free for individuals, with team plans starting at $1 per resource.
          button:
            text: "Try Pulumi Cloud"
            link: "https://app.pulumi.com/signup"
          image: "/images/product/pulumi-cloud-iac-stylized-01.png"
          features:
              - title: Managed state
                description: "Never worry about corrupted state files or DIY backends"
              - title: Built-in secrets
                description: "Automatic encryption for sensitive configuration"
              - title: Team collaboration
                description: "RBAC, audit logs, deployment history, and concurrent updates"
              - title: Policy as code
                description: "Enforce security and compliance rules before deployment"
              - title: AI assistance
                description: "Pulumi Copilot helps you write, debug, and understand infrastructure"
              - title: Enterprise ready
                description: "SAML SSO, SCIM provisioning, and premium support"

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