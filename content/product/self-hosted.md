---
title: Self-Hosted Pulumi Cloud
meta_desc: Run the full Pulumi Cloud platform in your own AWS, Azure, Google Cloud, or on-premises environment, including fully air-gapped networks.
meta_image: /images/product/self-hosted/self-hosted-meta.png
type: page
layout: template-page
include_floqer: true

sections:
  - type: hero
    title_primary: Pulumi Cloud,
    title_secondary: running inside your network.
    description: |
      Install the Pulumi Cloud API and console into your own AWS, Azure, Google Cloud, or on-premises environment. State, secrets, and audit history live in a database and object store you own, and the installation can run with no route to the public internet.
    cta_primary_text: Request a proof of concept
    cta_primary_link: "#self-hosted-trial"
    cta_secondary_text: Read the install guide
    cta_secondary_link: /docs/administration/self-hosting/install/
    anchor: hero

  - type: feature_split
    heading: For teams that can't hand infrastructure state to a vendor
    description: |
      Most Pulumi customers run on the hosted service at app.pulumi.com, and most should. Self-hosting exists for the organizations that can't: regulators who dictate where data lives, programs that operate with no internet route, and contracts that name a country.
    cta_text: Compare hosted and self-hosted
    cta_link: /docs/administration/onboarding-guide/choose-edition/
    cards:
      - icon: bank
        title: Regulated industries
        description: |
          Financial services, insurance, and healthcare teams that keep infrastructure metadata inside an audited boundary and have to produce evidence for it on demand.
      - icon: wall
        title: Air-gapped networks
        description: |
          Installations with no egress at all. Mirror the container images and provider plugins into your environment and run from there — see the [air-gapped guide](/docs/administration/self-hosting/airgapped/).
      - icon: globe
        title: Data sovereignty
        description: |
          Statutory or contractual requirements that stack state, secrets, and audit logs never leave a named region or cloud account.
    anchor: audience

  - type: testimonial
    quote: |
      We gave our auditors access to our policy packs because it's far easier to understand and prove controls in code than in docs and diagrams. With Pulumi's Policy as Code approach, that manual review process has gone away. We've reduced our Authority to Operate (ATO) timeline from a year and a half to expecting approval in three months.
    author: Michael Hunter
    title: CEO
    company: Spear AI
    anchor: testimonial

  - type: section_header
    title: The whole platform, not a state backend
    description: |
      A self-hosted installation runs the Pulumi Cloud API and console as container images you pull and operate, backed by a MySQL 8.0 database, object storage, and an OpenSearch cluster you provide. Everything below is part of it.
    cards_cols: 3
    cards:
      - icon: custom/pulumi-iac
        title: Pulumi IaC
        description: |
          Encrypted state, stack history, role-based access control, and audit logs, stored in your own database and object store.
      - icon: custom/pulumi-secrets
        title: Pulumi ESC
        description: |
          Environments, secrets, and configuration ship with the install — no separate deployment.
      - icon: custom/pulumi-insights
        title: Discovery and Policies
        description: |
          Run Discovery scans and policy evaluations on [customer-managed runners](/docs/insights/self-hosted/) inside your network, so cloud credentials never leave it.
      - icon: custom/pulumi-neo
        title: Pulumi Neo
        description: |
          Pulumi's infrastructure agent works against a self-hosted installation, so teams keep AI-assisted infrastructure work inside their own boundary.
      - icon: identification-card
        title: Your identity provider
        description: |
          SAML 2.0 SSO against any IdP — Okta, Microsoft Entra ID, Ping — plus GitHub, GitLab, and Bitbucket OAuth, or email and password. SCIM keeps users and groups in sync.
      - icon: magnifying-glass
        title: Resource search
        description: |
          Point the API at an OpenSearch cluster you run and resource search indexes across every stack in the installation.
    anchor: capabilities

  - type: card_grid
    title: Seven supported installations
    description: |
      Every option below ships as a Pulumi program in [pulumi-self-hosted-installers](https://github.com/pulumi/pulumi-self-hosted-installers). Run them as they are, or treat them as reference architectures and fold the resources into your own pipeline — plenty of customers do.
    small_cards_cols: 4
    small_cards:
      - icon: cube
        title: Docker Compose
        description: |
          Evaluation only. Brings up the API, console, database, and search on one host so you can try the product before designing a production topology.
        cta_text: Docker Compose guide
        cta_link: /docs/administration/self-hosting/deployment-options/quickstart-docker-compose/
      - icon: cloud
        title: AWS ECS
        description: |
          Fargate services behind a load balancer with Aurora MySQL, S3, ACM, and Route 53. TypeScript and Go installers.
        cta_text: ECS guide
        cta_link: /docs/administration/self-hosting/deployment-options/ecs-hosted/
      - icon: tree-structure
        title: AWS EKS
        description: |
          Nine composable Pulumi projects on Kubernetes. Bring your own IAM, VPC, or state buckets when another team owns them.
        cta_text: EKS guide
        cta_link: /docs/administration/self-hosting/deployment-options/eks-hosted/
      - icon: tree-structure
        title: Azure AKS
        description: |
          Azure Kubernetes Service with Azure Database for MySQL and Blob Storage, behind an NGINX ingress.
        cta_text: AKS guide
        cta_link: /docs/administration/self-hosting/deployment-options/aks-hosted/
      - icon: tree-structure
        title: Google GKE
        description: |
          Google Kubernetes Engine with Cloud SQL for MySQL and Cloud Storage buckets.
        cta_text: GKE guide
        cta_link: /docs/administration/self-hosting/deployment-options/gke-hosted/
      - icon: wrench
        title: Bring your own Kubernetes
        description: |
          Any conformant cluster plus MySQL 8.0 and S3-compatible object storage. This is the path for on-premises clusters and air-gapped networks.
        cta_text: BYO infrastructure guide
        cta_link: /docs/administration/self-hosting/deployment-options/byo-infra-hosted/
      - icon: hard-drives
        title: Docker on your own hosts
        description: |
          For data centers with no Kubernetes platform: run the container images directly against an external MySQL and object store.
        cta_text: Docker Engine guide
        cta_link: /docs/administration/self-hosting/deployment-options/local-docker/
      - icon: chats-circle
        title: Something else?
        description: |
          The images run on any OCI-compatible orchestrator. Tell us what you operate and a solutions architect will size the installation.
        cta_text: Talk to a solutions architect
        cta_link: /contact/?form=sales
    anchor: deploy

  - type: section_header
    tag_line: Day 2
    title: You own uptime. We document the job.
    description: |
      The [operations guide](/docs/administration/self-hosting/operations/) covers architecture, compute sizing, database and object storage configuration, network layout, and security hardening. These are the four things platform teams ask about first.
    cards_cols: 4
    cards:
      - icon: pulse
        title: High availability
        description: |
          Stateless API and console services across availability zones, in front of a managed MySQL cluster and replicated object storage.
      - icon: floppy-disk
        title: Recovery targets
        description: |
          Under 5 minutes for an availability zone failure, under 1 minute for an Aurora failover, and 1 to 4 hours to rebuild a region from cross-region backups.
      - icon: arrows-clockwise
        title: Upgrades
        description: |
          Pin the image tag, run migrations before rolling services, stage through a test environment. Every release lands in the [changelog](/docs/administration/self-hosting/changelog/).
      - icon: chart-line-up
        title: Observability
        description: |
          The API exposes Prometheus metrics and OpenTelemetry traces. The [monitoring guide](/docs/administration/self-hosting/operations/monitoring/) gives a three-tier alerting strategy and the metrics worth paging on.
    anchor: operations

  - type: three_column
    tag_line: Compliance
    title: What we claim, and what we don't
    subtitle: Security reviews move faster when the vendor is precise. Here is the posture in plain terms.
    icon_layout: above
    columns:
      - icon: certificate
        title: SOC 2 Type II
        description: |
          Pulumi Cloud is covered by an annual SOC 2 Type II audit performed by an independent CPA firm. The report is available under NDA. Architecture, key hierarchy, and operational controls are documented in the security whitepaper.
        cta_text: Read the whitepaper
        cta_link: /security/pulumi-cloud-security-whitepaper/
      - icon: wall
        title: Inside a boundary you already authorized
        description: |
          Because you install and operate it, the assessment surface is your own infrastructure under your own controls, rather than a third-party service your assessor has to scope separately.
        cta_text: Air-gapped deployment guide
        cta_link: /docs/administration/self-hosting/airgapped/
      - icon: warning
        title: No FedRAMP authorization
        description: |
          Pulumi holds no FedRAMP authorization. There is no Pulumi ATO and no FedRAMP Marketplace listing. If your program requires a FedRAMP-authorized service, Pulumi Cloud does not meet that requirement today, and self-hosting does not change it — it changes who owns the boundary.
        cta_text: Talk to us about your program
        cta_link: /contact/?form=sales
    anchor: compliance

  - type: two_column
    highlight_first_card: true
    columns:
      - label: Business Critical
        title: How self-hosting is licensed
        description: |
          Self-hosting is part of [Pulumi Business Critical](/pricing/), along with self-hosted Pulumi ESC and self-hosted Discovery scans and policy evaluations. Pricing is custom, and evaluations run as a guided proof of concept with a solutions architect.
        cta_text: See pricing
        cta_link: /pricing/
      - title: Would the hosted service do?
        description: |
          For most teams, yes, and it is a great deal less work. Pulumi Cloud at app.pulumi.com gives you high availability, disaster recovery, and upgrades without operating anything, and it is free to start.
        cta_text: Compare editions
        cta_link: /docs/administration/onboarding-guide/choose-edition/
    anchor: pricing

  - type: hubspot_form
    anchor: self-hosted-trial
    title: Request a proof of concept
    description: |
      A solutions architect will walk through your target environment, size the installation, and get you the installer package and an evaluation license key. If you would rather ask a question first, [contact us](/contact/).
    hubspot_form_id: b6ff58c0-2b40-4202-9a7f-d6d8aca4414a
---
