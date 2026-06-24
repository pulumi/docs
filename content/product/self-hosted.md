---
title: Self-Hosted Pulumi Cloud
layout: self-hosted

meta_desc: Run Pulumi Cloud self-hosted in your own cloud or data center — the same IaC, secrets, and governance as the SaaS, with full control over your data and network.

aliases:
    - /self-hosted/
    - /try-self-hosted/

overview:
    title: Run Pulumi Cloud in your own environment
    descriptionTop: |
        Run the complete Pulumi Cloud platform in your own cloud account or data center. You get the same IaC, secrets, insights, and governance capabilities as the SaaS, with full control over data, identity, network isolation, and air-gapped operation.
    descriptionBottom: |
        Deploy it yourself in about ten minutes with Docker Compose, then move to production on AWS, Azure, Google Cloud, or Kubernetes.
    ctaPrimary:
        label: Deploy it yourself
        link: /docs/administration/self-hosting/install/
    ctaSecondary:
        label: Talk to us about a guided rollout
        link: "#self-hosted-trial"
trial:
    title: Want a guided rollout?
    description: |
        You can [deploy self-hosted Pulumi Cloud yourself](/docs/administration/self-hosting/install/) in minutes. If you'd prefer help planning a production deployment, connect with a solutions architect.
    hubspot_form_id: b6ff58c0-2b40-4202-9a7f-d6d8aca4414a
capabilities:
    title: Capabilities of Self-Hosted Pulumi Cloud
    items:
        - title: Cloud Engineering Platform
          icon: rocketship
          icon_color: violet
          description: |
            All the capabilities of Pulumi Cloud: state management, role-based access controls, policy and compliance guardrails.
        - title: Full Control of Data
          icon: gear
          icon_color: violet
          description: |
            All data in Self-Hosted Pulumi Cloud is stored in a MySQL database and an encrypted object store within your own network.
        - title: Air-gapped Communications
          icon: abstract-shapes
          icon_color: blue
          description: |
            No communication outside of your private network, eliminating all communication over the public internet.
        - title: Federated Identity & Group Management
          icon: shield
          icon_color: yellow
          description: |
            Integrate with your preferred identity provider and manage permissions across your organization.
          items:
            - image: /logos/pkg/azuread.svg
              text: Azure Active Directory
            - image: /logos/pkg/github.svg
              text: GitHub
            - image: /logos/pkg/gitlab.svg
              text: GitLab
            - image: /images/self-hosted/bitbucket.svg
              text: Bitbucket
            - image: /images/self-hosted/samlsso.svg
              text: SAML SSO
deployment:
    title: Hosting Options
    descriptionTop: |
        [Install Self-Hosted Pulumi Cloud](/docs/administration/self-hosting/install/) in any on-premises or cloud provider environment or run in air-gapped environments, including those requiring FedRAMP.
    descriptionBottom: |
        [Talk to a Pulumi team member](/contact/) if you don't see your desired deployment option.
pricing:
    title: Pricing
    description: |
        Self-Hosted Pulumi Cloud is available with the Business Critical edition. Evaluate it yourself with an evaluation license, then move to production with a Business Critical license.
questions:
    title: Talk to a Human
    description: |
        If you have any questions about Self-Hosted Pulumi Cloud, please contact us or visit the self-hosted docs.
---
