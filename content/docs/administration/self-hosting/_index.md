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
  - /docs/administration/self-hosting/pulumi-cloud

sections:
- type: flat
  heading: Overview
  description_md: |
    Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, [request a Proof of Concept (PoC)](/product/self-hosted/#self-hosted-trial) or [contact us](/contact/).

    The self-hosted version provides all the same capabilities as the SaaS offering at [app.pulumi.com](https://app.pulumi.com/signin). You manage data backups, keep the service running, and maintain updates, while gaining full control over the deployment environment.

    Pulumi can be deployed in any on-premise or cloud environment and integrated with your preferred identity provider: GitHub Enterprise, GitLab Enterprise, SAML SSO, or email/password authentication.

- type: button-cards
  heading: Deployment options
  cards:
  - icon: cube
    heading: Quickstart Docker Compose
    link: /docs/administration/self-hosting/deployment-options/quickstart-docker-compose/
    description: Testing deployment using Docker Compose for local environments.

  - icon: cloud
    heading: ECS-Hosted
    link: /docs/administration/self-hosting/deployment-options/ecs-hosted/
    description: Production deployment on AWS ECS with TypeScript or Go automation.

  - icon: cube
    heading: EKS-Hosted
    link: /docs/administration/self-hosting/deployment-options/eks-hosted/
    description: Production deployment on Amazon EKS with TypeScript automation.

  - icon: file-code
    heading: AKS-Hosted
    link: /docs/administration/self-hosting/deployment-options/aks-hosted/
    description: Production deployment on Azure Kubernetes Service with TypeScript automation.

  - icon: globe
    heading: GKE-Hosted
    link: /docs/administration/self-hosting/deployment-options/gke-hosted/
    description: Production deployment on Google Kubernetes Engine with TypeScript automation.

  - icon: wrench
    heading: Bring Your Own Infrastructure
    link: /docs/administration/self-hosting/deployment-options/byo-infra-hosted/
    description: Deploy on your own Kubernetes, MySQL, and S3-compatible storage.

  - icon: cube
    heading: Local-Docker
    link: /docs/administration/self-hosting/deployment-options/local-docker/
    description: Production deployment using custom Docker environment with MySQL and object storage.

- type: button-cards
  heading: Configuration
  cards:
  - icon: package
    heading: Components
    link: /docs/administration/self-hosting/components/
    description: Docker images for the Pulumi Cloud frontend UI and backend API.

  - icon: globe
    heading: Network Requirements
    link: /docs/administration/self-hosting/network/
    description: Ingress, egress, and infrastructure requirements for self-hosted deployments.

- type: button-cards
  heading: Operations
  cards:
  - icon: chart-bar
    heading: Operations Guide
    link: /docs/administration/self-hosting/operations/
    description: HA, DR, monitoring, sizing, and security hardening for production deployments.

  - icon: floppy-disk
    heading: Backup and Recovery
    link: /docs/administration/self-hosting/operations/backup-recovery/
    description: Backup strategies, recovery procedures, and RTO targets.

  - icon: chart-line-up
    heading: Monitoring and Alerting
    link: /docs/administration/self-hosting/operations/monitoring/
    description: Three-tier alerting strategy and key metrics to watch.

  - icon: lock
    heading: Security Hardening
    link: /docs/administration/self-hosting/operations/security-hardening/
    description: Network security, encryption, SMTP, and bot protection.

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---
