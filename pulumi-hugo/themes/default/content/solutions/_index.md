---
title: Solutions
meta_desc: This is a description about the solutions page and it does a good job of describing what this page is.

type: page
layout: solutions

overview:
    title: Deliver and manage modern cloud applications
    description: Any cloud, any workload, any language

use_cases:
    title: Use Cases
    items:
        - name: Shared services platforms
          case_studies:
            - name: Atlassian
              link: /case-studies/atlassian
            - name: Mercedes-Benz
              link: /case-studies/mercedes-benz
            - name: Lemonade
              link: /case-studies/lemonade
          description: |
            Create reusable infrastructure components or self-service infrastructure platforms
            that empower your application developers to easily and quickly deploy and use
            infrastructure they need to build applications.

            [Learn more about shared services platforms](/solutions/shared-services-platforms/)

        - name: Infrastructure CI/CD
          case_studies:
            - name: Atlassian
              link: /case-studies/atlassian/
            - name: Panther Labs
              link: /case-studies/panther-labs/
          description: |
            Automate your infrastructure provisioning and management through a CI/CD pipeline. Run all infrastructure updates through a standard set of unit and integration tests, allowing reduced errors, greater security, and increased delivery velocity.

            [Learn more about CI/CD](/solutions/infrastructure-ci-cd/)

        - name: Terraform Migration
          case_studies:
            - name: Lemonade
              link: /case-studies/lemonade/
            - name: Panther Labs
              link: /case-studies/sans-institute/
          description: |
            Modernize how your teams provision and manage infrastructure in order to adapt to the changes in technologies (containers, serverless), architectures (distributed), and software release automation associated with the cloud.

            [Learn more about Terraform migration](/solutions/terraform-migration)

        - name: Greenfield modern applications
          case_studies:
            - name: Snowflake
              link: /case-studies/snowflake
            - name: Menta Network
              link: /case-studies/menta-network
          description: |
            Use Pulumi to develop your next greenfield application that uses modern cloud technologies, like containers and serverless. Pulumi is designed for building
            these types of complex and distributed applications.

        - name: AI and ML workloads
          description: |
            Easily provision and maintain machine learning (ML) batch jobs and data processing pipelines. Pulumi provides an easy and automated way to deploy ML stacks
            for data scientists and developers.

        - name: Migrate from an existing infrastructure tool
          description: |
            Adopt Pulumi when your existing infrastructure provisioning tool has reached its limits. Pulumi provides YAML or JSON file converters or you can use Pulumi
            alongside existing tools.

        - name: On-premises to cloud migration
          description: |
            Simplify your cloud migration with Modern Infrastructure-as-Code. Pulumi lets you model and automate the provisioning of infrastructure being migrated
            to the cloud to increase speed and success.

architectures:
    title: Common Architecture Types
    items:
        - name: Containers
          cta_link: /containers
          cta_text: Learn More
          description: |
            Manage clusters and deploy containers with ease for Kubernetes, Amazon ECS, Azure ACI,
            or Google GKE.
          case_studies:
            - logo: sourcegraph
              link: /case-studies/sourcegraph
            - logo: credijusto
              link: /case-studies/credijusto
            - logo: snowflake
              link: /case-studies/snowflake

        - name: Serverless
          cta_link: /serverless
          cta_text: Learn More
          description: |
            Focus on business logic and managing infrastructure in the same familiar language you’re already using to write code.
          case_studies:
            - logo: menta
              link: /case-studies/menta-network
            - logo: lemonade
              link: /case-studies/lemonade
            - logo: hyland
              link: /case-studies/learning-machine

        - name: Server-based
          cta_link: /docs/tutorials/aws/ec2-webserver
          cta_text: Learn More
          description: |
            Define and manage cloud infrastructure using server-based architectures, such as compute and database instances.
          case_studies:
            - logo: menta
              link: /case-studies/menta-network

        - name: Kubernetes
          cta_link: /kubernetes
          cta_text: Learn More
          description: |
            The easiest way to deploy, configure, and monitor Kubernetes clusters on any cloud, with a single tool, and in your favorite language.
          case_studies:
            - logo: sourcegraph
              link: /case-studies/sourcegraph
            - logo: credijusto
              link: /case-studies/credijusto
            - logo: snowflake
              link: /case-studies/snowflake

personas:
    title: Pulumi
    developers:
        label: Developers
        items:
            - title: Write in your favorite language
              icon: code
              icon_color: purple
              description: |
                Define [infrastructure as code](/what-is/what-is-infrastructure-as-code/) using
                familiar languages and IDEs: JavaScript, TypeScript, Python, Go, and .NET.
            - title: Cloud programming model
              icon: program
              icon_color: yellow
              description: |
                Use a programming model designed to make you maximally productive across any cloud,
                AWS, Azure, GCP, or Kubernetes.
            - title: Real abstractions for the cloud
              icon: abstract-shapes
              icon_color: salmon
              description: |
                Build true cloud abstractions, reduce copy-and-paste, and share and reuse them
                in your favorite package manager.

    devops:
        label: DevOps / Infra Teams
        items:
            - title: Modern Infrastructure as Code
              icon: code-window
              icon_color: purple
              description: |
                Use cloud engineering best practices to plan and version deployments and perform
                them with perfect auditability.
            - title: Multi-Cloud DevOps
              icon: cloud-with-nodes
              icon_color: yellow
              description: |
                It’s easier to go multi-cloud by using a single tool to manage each cloud, which eliminates
                YAML and DSL sprawl.
            - title: Deploy Continuously
              icon: cycle
              icon_color: salmon
              description: |
                Integrate with existing SCM and ALM systems to continuously deliver to many clouds
                with a single consistent workflow.

    security:
        label: Security Engineers
        items:
            - title: Policy as Code
              icon: shield
              icon_color: purple
              description: |
                Pulumi CrossGuard lets you author policies in programming languages to enforce best practices and correct configuration drift.
            - title: Built-in Secrets
              icon: security
              icon_color: yellow
              description: |
                Use Pulumi’s built-in secrets management to ensure that sensitive infrastructure as code configuration is always encrypted.
            - title: Enforce Standards
              icon: gavel
              icon_color: salmon
              description: |
                Codify and reuse standard organizational patterns with standard packaging techniques, versioning, and easy patching.
    leader:
        label: Engineering Leaders
        items:
            - title: Embrace modern architectures
              icon: nodes-and-rays
              icon_color: purple
              description: |
                Easily adopt container and serverless architectures across applications and infrastructure, and Dev and DevOps.
            - title: Go Multi-Cloud
              icon: clouds
              icon_color: yellow
              description: |
                Build multi-cloud applications with a single workflow across all clouds &mdash; AWS, Azure, GCP, Kubernetes, hybrid or on-premises.
            - title: Enterprise-Grade
              icon: buildings
              icon_color: salmon
              description: |
                Use robust security, compliance, and auditing tools with an extensible policy engine for enforcing your organization’s practices.

get_started:
    title: Get started today
    description: Pulumi is open source and free to get started. Deploy your first stack today.
    cta_text: Get Started
---
