---
title: "Migrate from Terraform | Pulumi"
meta_desc: "Migrate from Terraform to Python, TypeScript, Go, or C#. Free tf2pulumi converter. Pulumi Cloud manages existing Terraform state. Migrate at your pace."
layout: gads-template
block_external_search_index: true
utm_source: gads-terraform-migration

heading: "Migrate from Terraform"
subheading: |
    Free migration tools. Pulumi is free, open source, and works with your existing Terraform.
    Keep your Terraform running while you migrate at your pace.

hide_platform_details: true

customer_quote:
    text: "When we did it with Terraform, it took two weeks to do infrastructure deployments. Now we do it in about three hours a day."
    author: "Matt Stephenson, Senior Principal Software Engineer, Starburst"
    logo: starburst
    link: /case-studies/starburst/

overview:
    title: Free Migration Tools.<br/>Keep Your Terraform Running.
    description: |
        Looking for <span id="dki-placeholder" style="font-weight: bold;">a Terraform migration path</span>? Convert HCL to Python, TypeScript, Go, or C# with the free tf2pulumi tool. Pulumi Cloud manages your existing Terraform state directly. Migrate at your pace, stack by stack. [Try the converter](/migrate/tf2pulumi/).

key_features_above:
    items:
        - title: "Convert HCL to real code with tf2pulumi"
          sub_title: "Free Migration Tools"
          description:
            Use the free tf2pulumi converter to turn Terraform .tf files into Pulumi programs in Python, TypeScript, Go, or C#. No resource caps. No forced deadlines. Keep your current infrastructure running while you migrate.
          ide:
            - title: main.tf
              language: hcl
              code: |
                resource "aws_s3_bucket" "example" {
                  bucket = "my-pulumi-bucket"
                }

                output "bucket_name" {
                  value = aws_s3_bucket.example.bucket
                }
            - title: __main__.py
              language: python
              code: |
                import pulumi
                from pulumi_aws import s3

                bucket = s3.Bucket("example", bucket="my-pulumi-bucket")

                pulumi.export("bucket_name", bucket.bucket)
          features:
              - title: tf2pulumi converter
                description: |
                    Convert .tf files to Pulumi in your language of choice. Try it at [pulumi.com/migrate/tf2pulumi](/migrate/tf2pulumi/).
                icon: code
                color: yellow
              - title: Import existing state
                description: |
                    Import Terraform state into Pulumi without re-provisioning. Zero downtime.
                icon: cloud
                color: yellow
              - title: No resource caps
                description: |
                    Pulumi Cloud's free tier has no managed resource limits. Scale when you're ready.
                icon: shield
                color: yellow

        - title: "Pulumi Cloud manages Terraform state"
          sub_title: "Coexistence"
          description: |
            You don't have to migrate everything at once. Pulumi Cloud can manage your existing Terraform state directly. Run Terraform and Pulumi side by side. Drift detection and policy enforcement work on Terraform-managed resources too.
          features:
              - title: State management
                description: |
                    Store and manage Terraform state in Pulumi Cloud. Same workflows, one place.
                icon: global
                color: yellow
              - title: Drift detection
                description: |
                    Detect when Terraform-managed resources change outside of IaC. Stay in sync.
                icon: eye
                color: yellow
              - title: Policy on TF resources
                description: |
                    Apply Pulumi Policies to Terraform-managed resources. Govern before you migrate.
                icon: lightning
                color: yellow

        - title: "Neo accelerates Terraform migrations"
          sub_title: "AI-Native Infrastructure"
          description: |
            Pulumi Neo understands your Terraform code and can help convert it, suggest improvements, and answer questions. Use AI to speed up your migration without leaving your workflow.
          features:
              - title: Convert with Neo
                description: |
                    Neo can help convert Terraform to Pulumi and reason about your existing stacks.
                icon: lightning
                color: yellow

key_features:
    title: Key features
    items:
        - title: "Migrate from Terraform in minutes"
          sub_title: "Free Migration Tools"
          description: |
            Use tf2pulumi to convert your existing Terraform HCL to Python, TypeScript, Go, or C#. Import existing state with pulumi import. Keep your current infrastructure running while you migrate at your own pace. No forced deadlines. No resource caps.
          image: "/images/product/pulumi-iac-code.png"
          features:
              - title: Convert HCL to real code
                description: |
                    The tf2pulumi tool converts your .tf files to Pulumi programs in your language of choice. [Try it at pulumi.com/migrate/tf2pulumi](/migrate/tf2pulumi/).
              - title: Import existing state
                description: |
                    Already have infrastructure managed by Terraform? Import your state directly into Pulumi without re-provisioning. Zero downtime migration.
              - title: No 500 resource limit
                description: |
                    Pulumi Cloud's free tier has no managed resource caps. Manage as many resources as you need. Scale when you're ready.

        - title: "Build infrastructure faster with reusable components"
          sub_title: "Pulumi Packages"
          description: |
            Build and reuse higher-level abstractions for cloud architectures with multi-language Pulumi Packages. Distribute the packages through repositories or package managers so your team members can reuse them.
          ide:
            - title: __main__.py
              language: python
              code: |
                import pulumi
                import pulumi_eks as eks

                cluster = eks.Cluster("eks-cluster")
                pulumi.export("kubeconfig", cluster.kubeconfig)
            - title: index.ts
              language: typescript
              code: |
                import * as eks from "@pulumi/eks";
                const cluster = new eks.Cluster("eks-cluster");
                export const kubeconfig = cluster.kubeconfig;
          features:
              - title: Native cloud providers
                description: |
                    Full API coverage for AWS, Azure, Google Cloud, and Kubernetes with same-day updates.
              - title: Crosswalk for AWS
                description: |
                    Adopt well-architected best practices for your infrastructure easily with the Crosswalk library.
              - title: Cloud Native support
                description: |
                    Use a single workflow to manage both Kubernetes resources and infrastructure.

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
        - name: Starburst
          link: /case-studies/starburst/
          logo: starburst
          description: |
            Deployments reduced from two weeks to about three hours a day with Pulumi.

        - name: Snowflake
          link: /case-studies/snowflake/
          logo: snowflake
          description: |
            Switched from HCL to Go with Pulumi. Deployment time cut from 1.5 weeks to under a day.

        - name: Atlassian
          link: /case-studies/atlassian/
          logo: atlassian
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
---