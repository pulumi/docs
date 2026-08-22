---
title: "Infrastructure as Code | Pulumi"
meta_desc: "Modern infrastructure as code in Python, TypeScript, Go, or C#. 200+ cloud providers, policy as code, secrets management. Open source. Free tier."
layout: gads-template
block_external_search_index: true

overline: "Pulumi IaC"
heading: "Infrastructure as Code"
subheading: |
    Define, deploy, and manage cloud infrastructure using programming languages you already know.
    Pulumi is free, open source, and supports 170+ cloud and SaaS providers including AWS, Azure,
    Google Cloud, and Kubernetes.

customer_quote:
    text: "Pulumi supercharged our infrastructure team by helping us create reusable building blocks that developers can leverage to provision new resources and enforce organizational policies for logging, permissions, resource tagging, and security."
    author: "Igor Shapiro"
    title: "Principal Engineer"
    company: "Lemonade"
    logo: lemonade
    link: /case-studies/lemonade

overview:
    title: Infrastructure as Code<br/>in Real Programming Languages
    description: |
        Looking for <span id="dki-placeholder" style="font-weight: bold;">an infrastructure as code tool</span>? Pulumi lets you define cloud infrastructure in Python, TypeScript, Go, C#, Java, or YAML — with full IDE support, testing, and package management. Deploy to 170+ providers including AWS, Azure, Google Cloud, and Kubernetes. Free and open source.

key_features_above:
    items:
        - title: "Author in any language, deploy to any cloud"
          sub_title: "Pulumi Infrastructure as Code Engine"
          description:
            Stop learning DSLs. Author infrastructure as code using programming languages you already know — Python, TypeScript, Go, C#, Java, and YAML. Get auto-completion, type checking, and refactoring from your IDE. Deploy to 170+ providers.
          features:
              - title: Code faster with real languages
                description: |
                    Write infrastructure in TypeScript, Python, Go, .NET, Java, and YAML. Use loops, conditionals, functions, and classes — not DSL workarounds.
                icon: code
              - title: Build on any cloud
                description: |
                    Access the full breadth of services in AWS, Azure, GCP, and 170+ providers through
                    a complete and consistent SDK interface.
                icon: global
              - title: Test and preview changes
                description: |
                    Write unit tests with standard frameworks. Run integration tests against ephemeral infrastructure. Preview every change before deploying.
                icon: eye

key_features:
    items:
        - title: "Build infrastructure faster with reusable components"
          sub_title: "Pulumi Packages"
          description: |
            Build and reuse higher-level abstractions for cloud architectures with multi-language Pulumi Packages. Create a VPC component once, share it across your organization, and let every team deploy consistently. Real package managers, real versioning, real code reuse.
          ide:
            - title: index.ts
              language: typescript
              code: |
                import * as pulumi from "@pulumi/pulumi";
                import * as aws from "@pulumi/aws";

                // Create an S3 bucket for static hosting.
                const bucket = new aws.s3.Bucket("my-site", {
                    website: { indexDocument: "index.html" },
                });

                // Upload a file to the bucket.
                const index = new aws.s3.BucketObject("index.html", {
                    bucket: bucket.id,
                    content: "<h1>Hello, Pulumi!</h1>",
                    contentType: "text/html",
                });

                export const url = bucket.websiteEndpoint;
            - title: __main__.py
              language: python
              code: |
                import pulumi
                import pulumi_aws as aws

                # Create an S3 bucket for static hosting.
                bucket = aws.s3.Bucket("my-site",
                    website={"index_document": "index.html"},
                )

                # Upload a file to the bucket.
                index = aws.s3.BucketObject("index.html",
                    bucket=bucket.id,
                    content="<h1>Hello, Pulumi!</h1>",
                    content_type="text/html",
                )

                pulumi.export("url", bucket.website_endpoint)
            - title: main.go
              language: go
              code: |
                    package main

                    import (
                      "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
                      "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
                    )

                    func main() {
                      pulumi.Run(func(ctx *pulumi.Context) error {
                        // Create an S3 bucket for static hosting.
                        bucket, err := s3.NewBucket(ctx, "my-site", &s3.BucketArgs{
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
            - title: MyStack.cs
              language: csharp
              code: |
                using Pulumi;
                using Pulumi.Aws.S3;

                await Deployment.RunAsync(() =>
                {
                  // Create an S3 bucket for static hosting.
                  var bucket = new Bucket("my-site", new()
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
            - title: Main.Java
              language: java
              code: |
                import com.pulumi.Context;
                import com.pulumi.Pulumi;
                import com.pulumi.aws.s3.Bucket;
                import com.pulumi.aws.s3.BucketArgs;
                import com.pulumi.aws.s3.inputs.BucketWebsiteArgs;

                public class App {
                    public static void main(String[] args) {
                        Pulumi.run(App::stack);
                    }

                    private static void stack(Context ctx) {
                      // Create an S3 bucket for static hosting.
                      var bucket = new Bucket("my-site", BucketArgs.builder()
                        .website(BucketWebsiteArgs.builder()
                          .indexDocument("index.html")
                          .build())
                        .build());
                      ctx.export("url", bucket.websiteEndpoint());
                    }
                }
            - title: Pulumi.yaml
              language: yaml
              code: |
                resources:
                  my-site:
                    type: aws:s3:Bucket
                    properties:
                      website:
                        indexDocument: index.html
                outputs:
                  url: ${my-site.websiteEndpoint}
          features:
              - title: 200+ cloud providers
                icon: cloud
                description: |
                    170+ cloud and SaaS providers, including AWS, Azure, Google Cloud, and Kubernetes. New services are covered as they ship.
              - title: Reusable components
                icon: abstract-shapes
                description: |
                    Build higher-level abstractions and share them as packages through npm, PyPI, NuGet, or Go modules. Real versioning, real dependency management.
              - title: AI-powered infrastructure
                icon: lightning
                description: |
                    Pulumi Neo plans, writes, and executes infrastructure changes across your stacks. Claude Code, Cursor, and Codex work with Pulumi too, through the MCP server and Agent Skills.

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

case_studies:
    title: Customers innovating with Pulumi Cloud
    items:
        - name: Atlassian
          link: /case-studies/atlassian/
          logo: atlassian-wordmark
          description: |
            Developers reduced their time spent on maintenance by 50%.

        - name: Elkjop
          link: /case-studies/elkjop-nordic/
          logo: elkjop-nordic
          description: |
            Increased developers' agility and speed through platform engineering.

        - name: Starburst
          link: /case-studies/starburst/
          logo: starburst
          description: |
            Cut multi-region blue/green deployments from two weeks to three hours.

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
            Built a multi-cloud, Kubernetes-based platform to standardize all deployments.
---
