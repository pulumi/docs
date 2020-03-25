---
title: Infrastrucutre as Code
layout: infrastructure-as-code
url: /infrastructure-as-code

meta_desc: Pulumi is an open source infrastructure as code tool for creating, deploying, and managing cloud infrastructure. Pulumi works with traditional infrastructure like VMs, networks, and databases, in addition to modern architectures, including containers, Kubernetes clusters, and serverless functions.

hero:
    title: "Infrastructure as Code"
    body: >
        Infrastructure as Code (IaC) is the process of managing and provisioning cloud or bare metal infrastructure
        resources through machine-readable definition files, rather than physical hardware configuration
        or interactive configuration tools.<br /><br />

        Pulumi delivers on the Infrastructure as Code promise. Instead of defining instructure with configuration
        files (YAML) or proprietary configuration languages (HCL), Pulumi gives users the ability to choose the programming
        language of their choice. You finally have the ability to define and manage in your infrastructure in common languages
        such as TypeScript, Python, .NET, and Go.
    code: |
        package main

        import (
            "github.com/pulumi/pulumi-aws/sdk/go/aws/s3"
            "github.com/pulumi/pulumi/sdk/go/pulumi"
        )

        func main() {
            pulumi.Run(func(ctx *pulumi.Context) error {
                // Create an AWS resource (S3 Bucket)
                bucket, err := s3.NewBucket(ctx, "my-bucket", nil)
                if err != nil {
                    return err
                }

                // Export the name of the bucket
                ctx.Export("bucketName", bucket.ID())
                return nil
            })
        }

contact_us_form:
    section_id: contact
    hubspot_form_id: abf0bd4b-5e71-44a9-aad1-b55b5cce561d
    headline: Need help with container management?
    quote:
        title: Learn how top engineering teams are using Pulumi to manage containers in any cloud.
        name: Josh Imhoff
        name_title: Site Reliability Engineer, Cockroach Labs
        content: |
            We are building a distributed-database-as-a-service product that runs on Kubernetes clusters across multiple
            public clouds including GCP, AWS and others. Pulumi's declarative model, the support for real programming
            languages, and the uniform workflow on any cloud make our SRE team much more efficient.
---
