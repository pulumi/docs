---
title: Self-Hosted Pulumi Cloud
layout: self-hosted

meta_desc: Run Pulumi Cloud in your own cloud account, data center, or air-gapped network, including inside a FedRAMP authorization boundary.

overview:
    title: Try Self-Hosted Pulumi
    descriptionTop: |
        Maintain complete control over your hosting, network isolation, identity, and data ownership to satisfy compliance requirements, including [FedRAMP](#fedramp).  [Request a Proof of Concept](#self-hosted-trial) to evaluate self-hosted Pulumi.
    descriptionBottom: |
        Want Pulumi Cloud delivered as SaaS?  [Start Using Pulumi Cloud for free](https://app.pulumi.com/signin).
trial:
    title: Request a Proof of Concept
    description: |
        Fill out the form to connect with a solutions architect and start your evaluation.
    hubspot_form_id: b6ff58c0-2b40-4202-9a7f-d6d8aca4414a
regulated:
    title: Run Pulumi inside your FedRAMP boundary
    description: |
        Self-Hosted Pulumi is software you install and operate in your own environment, not a cloud service that Pulumi runs for you. It becomes a component of your system, inside your authorization boundary, so your infrastructure state, secrets, and configuration stay in the environment your assessor already reviews. Teams working toward FedRAMP certification and government authority to operate (ATO) run Pulumi this way today.
    items:
        - title: Your data stays in your boundary
          description: |
            All Self-Hosted Pulumi data is stored in a MySQL database and an encrypted object store that you run, in the cloud account, government cloud region, or data center you already operate.
        - title: No connection to Pulumi required
          description: |
            Run fully [air-gapped](/docs/administration/self-hosting/airgapped/), with no communication outside your private network. The install guide covers offline image transfer, private container registries, and internal mirrors for the CLI, SDKs, and providers.
        - title: Controls your assessor can read
          description: |
            Pulumi Policy as Code enforces security controls on every deployment and gives assessors code to review rather than documents and diagrams. [Spear AI](/customers/spear-ai/) gave auditors access to its policy packs and cut its government ATO timeline from 18 months to three.
        - title: Your identity provider and your secrets
          description: |
            Sign in through your own identity provider with SAML SSO and apply role-based access controls. [Pulumi ESC](/product/secrets-management/) is included, so secrets and configuration are managed inside your environment.
    scope:
        title: What this means for your certification
        description: |
            FedRAMP certifies cloud services. Pulumi Cloud, our SaaS offering, is not FedRAMP certified, and Self-Hosted Pulumi does not carry a certification of its own, because it is software you run and not a service we operate.

            If you are a cloud service provider, Self-Hosted Pulumi is assessed as part of your system, under your certification. If you are an agency installing it on your own systems, FedRAMP's [Minimum Assessment Scope](https://www.fedramp.gov/2026/reference/20x/c/minimum-assessment-scope/) treats separately delivered software that you operate yourself as outside the scope of FedRAMP.

            Certification decisions rest with your assessor and authorizing official. [Talk to our team](/contact/) about security documentation to support your package.
    cta:
        primary:
            label: Request a Proof of Concept
            link: "#self-hosted-trial"
        secondary:
            label: Air-gapped install guide
            link: /docs/administration/self-hosting/airgapped/
capabilities:
    title: Capabilities of Self-Hosted Pulumi
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
            All data in Self-Hosted Pulumi is stored in a MySQL database and an encrypted object store within your own network.
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
        [Install Self-Hosted Pulumi Cloud](/docs/administration/self-hosting/) in any on-premises or cloud provider environment, in [air-gapped networks](/docs/administration/self-hosting/airgapped/), and inside [FedRAMP authorization boundaries](#fedramp).
    descriptionBottom: |
        [Talk to a Pulumi team member](/contact/) if you don't see your desired deployment option.
pricing:
    title: Pricing
    description: |
        Self-Hosted Pulumi is available as an additional license for the Pulumi Enterprise edition and provided as part of a guided Proof of Concept.
questions:
    title: Talk to a Human
    description: |
        If you have any questions about Self-Hosted Pulumi, please contact us or visit the self-hosted docs.
---
