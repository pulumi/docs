---
title: Management
linktitle: Management
capability: management
docs_home: true
notitle: true
menu:
    management:
        identifier: management-home
        weight: 1
expanded_menu_ids:
    - management-deployments
    - management-governance
meta_desc: Operational oversight and governance for infrastructure. Manage deployments, policies, access controls, compliance, and audit across your organization.
meta_image: /images/docs/meta-images/docs-meta.png
h1: Infrastructure<strong> management</strong> and governance
description: <p>Operational oversight and governance tools for managing deployments, enforcing policies, controlling access, and maintaining compliance across your cloud infrastructure.</p>
link_buttons:
  primary:
    label: Cloud Console
    link: /docs/pulumi-cloud/
  secondary:
    label: View Insights
    link: /docs/insights/

sections:
- type: full-width-cards
  heading: Core Management Capabilities
  cards:
  - icon: deploy-blue-21-21
    heading: Deployments
    description: Monitor and manage infrastructure deployments across environments with automated workflows.
    link: /docs/pulumi-cloud/deployments/
  - icon: shield-blue-21-21
    heading: Policy & Governance
    description: Enforce organizational standards, compliance rules, and security policies through code.
    link: /docs/iac/crossguard/
  - icon: users-blue-21-21
    heading: Access Management
    description: Control who can access and modify infrastructure with role-based permissions and teams.
    link: /docs/pulumi-cloud/access-management/
  - icon: audit-blue-21-21
    heading: Compliance & Audit
    description: Track changes, monitor compliance, and generate audit reports for regulatory requirements.
    link: /docs/insights/
- type: button-cards
  heading: Management Services
  description: Enterprise-grade tools for infrastructure governance and operational control.
  cards:
  - heading: Pulumi Cloud Deployments
    description: "Centralized deployment management with approval workflows, drift detection, and automated remediation."
    link: /docs/pulumi-cloud/deployments/
    primary_button_label: Get Started
    primary_button_link: /docs/pulumi-cloud/deployments/get-started/
  - heading: Pulumi Insights
    description: "Asset discovery, compliance monitoring, and AI-powered insights across your cloud infrastructure."
    link: /docs/insights/
    primary_button_label: Explore Insights
    primary_button_link: /docs/insights/get-started/
  - heading: Policy as Code (CrossGuard)
    description: "Define and enforce infrastructure policies using familiar programming languages with automated validation."
    link: /docs/iac/crossguard/
    primary_button_label: Learn CrossGuard
    primary_button_link: /docs/iac/crossguard/get-started/
- type: full-width-cards
  heading: Governance & Control
  cards:
  - icon: approval-blue-21-21
    heading: Approval Workflows
    description: Require approvals for infrastructure changes with customizable review processes.
    link: /docs/pulumi-cloud/deployments/
  - icon: drift-blue-21-21
    heading: Drift Detection
    description: Automatically detect and remediate infrastructure drift from your desired state.
    link: /docs/pulumi-cloud/deployments/drift/
  - icon: cost-blue-21-21
    heading: Cost Management
    description: Track and optimize cloud spending with cost insights and budget alerts.
    link: /docs/insights/
  - icon: security-blue-21-21
    heading: Security Scanning
    description: Continuously scan infrastructure for security vulnerabilities and misconfigurations.
    link: /docs/insights/
- type: cards-logo-label-link
  heading: Enterprise Features
  description: Advanced management capabilities for large organizations and regulated industries.
  cards:
  - label: SAML/SSO
    icon: saml-40
    link: /docs/pulumi-cloud/access-management/saml-sso/
  - label: SCIM Provisioning
    icon: scim-40
    link: /docs/pulumi-cloud/access-management/scim/
  - label: Audit Logs
    icon: audit-40
    link: /docs/pulumi-cloud/audit-logs/
  - label: Private Hosting
    icon: private-40
    link: /docs/pulumi-cloud/self-hosted/
- type: full-width-cards
  heading: Operational Excellence
  cards:
  - icon: monitor-blue-21-21
    heading: Observability
    description: Monitor infrastructure health, performance, and availability across all environments.
    link: /docs/insights/
  - icon: alert-blue-21-21
    heading: Alerting & Notifications
    description: Get notified about deployment failures, policy violations, and infrastructure issues.
    link: /docs/pulumi-cloud/webhooks/
  - icon: backup-blue-21-21
    heading: Backup & Recovery
    description: Protect against configuration loss with automated backups and point-in-time recovery.
    link: /docs/pulumi-cloud/deployments/
  - icon: scale-blue-21-21
    heading: Multi-Environment Management
    description: Consistently manage infrastructure across development, staging, and production environments.
    link: /docs/pulumi-cloud/
- type: flat
  heading: Ready to govern at scale?
  description: <p>Start with <a href="/docs/pulumi-cloud/deployments/">Deployments</a>, explore <a href="/docs/insights/">Insights</a>, or set up <a href="/docs/iac/crossguard/">Policy as Code</a>. Enterprise customers can learn about <a href="/docs/pulumi-cloud/access-management/">access management</a> and <a href="/docs/pulumi-cloud/audit-logs/">audit logging</a>.</p>
---