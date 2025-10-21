---
title_tag: "Self-hosting the Pulumi Cloud"
meta_desc: Pulumi Business Critical Edition gives you the option to self-host Pulumi within your organization's infrastructure.
title: Self-hosting
linktitle: Self-hosting
docs_home: true
notitle: true
norightnav: true
h1: Self-hosting the Pulumi Cloud
description: <p>Deploy Pulumi Cloud in your own infrastructure with full control over data, security, and operations.</p>
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Self-Hosting
    parent: administration-home
    weight: 40
    identifier: administration-self-hosting
aliases:
  - /docs/guides/self-hosted/
  - /docs/pulumi-cloud/self-hosted/
  - /docs/pulumi-cloud/admin/self-hosted/
  - /docs/administration/self-hosting/

sections:
- type: flat
  heading: Overview
  description_md: |
    Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).

    The self-hosted version provides all the same capabilities as the SaaS offering at [app.pulumi.com](https://app.pulumi.com). You manage data backups, keep the service running, and maintain updates, while gaining full control over the deployment environment.

    Pulumi can be deployed in any on-premise or cloud environment and integrated with your preferred identity provider: GitHub Enterprise, GitLab Enterprise, SAML SSO, or email/password authentication.

- type: button-cards
  heading: Deployment options
  cards:
  - emoji: 🐳
    heading: Quickstart Docker Compose
    link: /docs/administration/self-hosting/deployment-options/quickstart-docker-compose/
    description: Testing deployment using Docker Compose for local environments.

  - emoji: ☁️
    heading: ECS-Hosted
    link: /docs/administration/self-hosting/deployment-options/ecs-hosted/
    description: Production deployment on AWS ECS with TypeScript or Go automation.

  - emoji: ☸️
    heading: EKS-Hosted
    link: /docs/administration/self-hosting/deployment-options/eks-hosted/
    description: Production deployment on Amazon EKS with TypeScript automation.

  - emoji: 🔷
    heading: AKS-Hosted
    link: /docs/administration/self-hosting/deployment-options/aks-hosted/
    description: Production deployment on Azure Kubernetes Service with TypeScript automation.

  - emoji: 🌐
    heading: GKE-Hosted
    link: /docs/administration/self-hosting/deployment-options/gke-hosted/
    description: Production deployment on Google Kubernetes Engine with TypeScript automation.

  - emoji: 🛠️
    heading: Bring Your Own Infrastructure
    link: /docs/administration/self-hosting/deployment-options/byo-infra-hosted/
    description: Deploy on your own Kubernetes, MySQL, and S3-compatible storage.

  - emoji: 🐋
    heading: Local-Docker
    link: /docs/administration/self-hosting/deployment-options/local-docker/
    description: Production deployment using custom Docker environment with MySQL and object storage.

- type: button-cards
  heading: Configuration
  cards:
  - emoji: 📦
    heading: Components
    link: /docs/administration/self-hosting/components/
    description: Docker images for the Pulumi Cloud frontend UI and backend API.

  - emoji: 🌐
    heading: Network Requirements
    link: /docs/administration/self-hosting/network/
    description: Ingress, egress, and infrastructure requirements for self-hosted deployments.

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---
