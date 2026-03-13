---
title: "Infrastructure as Code in Python | Pulumi"
meta_desc: "Infrastructure as Code in Python. Define AWS, Azure, GCP resources with type checking, testing, and full IDE support. 170+ providers. Free tier."
layout: gads-template
block_external_search_index: true
utm_source: gads-python-iac

heading: "Infrastructure as Code in Python"
subheading: |
    Pulumi is a free, open source infrastructure as code tool, and works best with Pulumi Cloud to
    make managing infrastructure secure, reliable, and hassle-free.

hide_platform_details: true

customer_quote:
    text: "Since it's just another programming language with control structures and external packages, it makes for a good transition from application code to infrastructure as code."
    author: "Paul Cioanca, Platform Engineer, Supabase"
    logo: supabase
    link: /case-studies/supabase/

overview:
    title: Write Cloud Infrastructure in Python.<br/>Not YAML. Not HCL.
    description: |
        Looking for <span id="dki-placeholder" style="font-weight: bold;">infrastructure as code python</span>? Define AWS, Azure, GCP, and Kubernetes resources in Python with full IDE support, type checking, and testing. 170+ cloud providers. Free tier.

key_features_above:
    items:
        - title: "Write infrastructure like software"
          sub_title: "Pulumi Infrastructure as Code Engine"
          description:
            Author infrastructure as code (IaC) using Python and the ecosystem you already know. Use pip, pytest, and mypy. Deploy to 170+ providers like AWS, Azure, Google Cloud, and Kubernetes.
          features:
              - title: Python ecosystem
                description: |
                    Use pip packages, pytest for testing, and mypy for type checking. No new toolchain.
                icon: code
                color: yellow
              - title: Full IDE support
                description: |
                    Autocomplete, type checking, refactoring, and debugging in VS Code, PyCharm, and your favorite editor.
                icon: eye
                color: yellow
              - title: AI code generation
                description: |
                    Pulumi AI understands Python natively. Generate and refine infrastructure code from natural language.
                icon: lightning
                color: yellow

key_features:
    title: Key features
    items:
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

                # Create an EKS cluster with the default configuration.
                cluster = eks.Cluster("eks-cluster")

                # Export the cluster's kubeconfig.
                pulumi.export("kubeconfig", cluster.kubeconfig)
            - title: index.ts
              language: typescript
              code: |
                import * as eks from "@pulumi/eks";

                // Create an EKS cluster with the default configuration.
                const cluster = new eks.Cluster("eks-cluster");

                // Export the cluster's kubeconfig.
                export const kubeconfig = cluster.kubeconfig;
          features:
              - title: Native cloud providers
                description: |
                    Full API coverage for AWS, Azure, Google Cloud, and Kubernetes with same-day updates.
              - title: AWSx
                description: |
                    Adopt well-architected best practices for your infrastructure easily with the AWSx library.
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
    title: Trusted by thousands
    description: |
        Pulumi's Infrastructure as Code CLI and SDK is an open-source project that's supported
        by an active community. We maintain a public roadmap and welcome feedback and contributions.
    community:
        number: "350,000+"
        description: developers
    company:
        number: "3,700+"
        description: organizations
    integration:
        number: "170+"
        description: Cloud and service integrations

key_features_below:
    items:
        - title: "Use Pulumi IaC at scale"
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
                    View resources from any cloud in one place. Search for resources across clouds with powerful queries and filters.
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
        - name: Supabase
          link: /case-studies/supabase/
          logo: supabase
          description: |
            Infrastructure contributors grew from 1-2 people to over 40 active engineers. 80,000+ resources across 16 regions.

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

        - name: Snowflake
          link: /case-studies/snowflake/
          logo: snowflake
          description: |
            Built a multi-cloud, Kubernetes-based platform to standardize all deployments
---
