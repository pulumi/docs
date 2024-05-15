---
title: "Pulumi for Platform Teams"
layout: internal-developer-platforms

meta_title: "Self-Service Developer Platforms with Pulumi"
meta_desc: Pulumi for Platform Teams! Accelerate productivity, enforce compliance, and maintain visibility with our internal developer platform-in-a-box.
meta_image: /images/product/platform-teams-meta.png

aliases:
    - /solutions/platforms/

challenges:
    items:
        - number: 1
          title: Developer speed
          description: Remove productivity obstacles like configuring cloud architectures, provisioning bottlenecks, and testing and deployment.
        - number: 2
          title: Security and compliance
          description: Set up guardrails that enforce compliance and standards while maintaining visibility over what’s being deployed and how.
        - number: 3
          title: Balancing agility and guardrails
          description: Accomplishing both speed and compliance with limited resources and without stifling developers’ autonomy and flow.

case_studies:
    title: Case Studies
    items:
        - company: Atlassian
          image: atlassian
          link: /case-studies/atlassian
          quote: |
            Atlassian Bitbucket reduced developers’ time spent on maintenance by 50% with a self-service platform built with Pulumi.

        - company: Washington Trust Bank
          image: washington-trust
          link: /blog/how-a-bank-modernized-its-software-engineering-with-infrastructure-as-code-automation/
          quote: |
            Washington Trust Bank maintains compliant and secure infrastructure deployments with policy packs and policy enforcement.

        - company: Mercedes-Benz
          image: mercedes-benz
          link: /case-studies/mercedes-benz/
          quote: |
            Mercedes-Benz enabled developers to provision Azure Kubernetes environments with a self-service platform built with Pulumi.

control:
    items:
        - title: Pulumi IaC
          description: Utilize open-source IaC in TypeScript/JavaScript, Python, Go, C#, Java, and YAML. Build and distribute reusable infrastructure components for 150+ cloud & SaaS providers, supporting modern and cloud-native architectures.
        - title: Pulumi Developer Portal
          description: Distribute standard private templates through an out-of-the-box Service Catalog experience, which developers can browse and deploy from using the Pulumi Cloud console. API integration with your VCS, Pulumi Deployments, CI/CD, and more.
        - title: Backstage Plugin
          description: Enable developers to browse, deploy, and monitor Pulumi infrastructure deployments from an existing Backstage portal. Use the plugin to integrate Backstage with Pulumi Developer Portal, where your private infrastructure templates are hosted.

integration:
    items:
        - title: Pulumi Deployments
          description: Centrally orchestrate automated deployment workflows with `git push to deploy`, UI triggers, and API. Advanced capabilities like ephemeral environments and extensibility for drift detection, TTL, blue/green, and more. Integrate with CI/CD, VCS, and more using the API. SaaS or self-hosted runners available.
        - title: Pulumi Automation API
          description: Build custom deployment and CI/CD workflows that integrate with Pulumi Developer Portal and custom portals or CLIs. Automation API is a programmatic interface for Pulumi CLI, allowing you to embed infrastructure automation into application code that runs on your servers.

security:
    items:
        - title: Pulumi CrossGuard
          description: Enforce policies across your organization. Utilize compliance-ready policies for any cloud to enhance compliance and use remediation policies to automatically correct configuration violations like auto-tagging, removing Internet access, and enabling storage encryption.
        - title: Pulumi Cloud
          description: Maintain control and tracking over deployed infrastructure, with complete history of updates and audit logs easily viewable from a console. Enhance security with RBAC, identity provider integrations, SSO, and more.
        - title: Pulumi ESC
          description: Centrally store and manage secrets and configuration from different providers. It provides a unified, secure location for all your configuration while managing developer access centrally.
---