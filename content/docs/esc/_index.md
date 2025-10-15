---
title: Secrets & Configuration
linktitle: Secrets & Configuration
docs_home: true
notitle: true
norightnav: true
menu:
  esc:
    identifier: esc-home
    weight: 1
aliases:
  - /docs/pulumi-cloud/esc/

meta_desc: Learn how to tame secrets sprawl and configuration complexity securely across all your cloud infrastructure and applications.
meta_image: /images/docs/meta-images/docs-meta.png
h1: Secrets & Configuration
description: <p>Centralized secrets management and orchestration for environments, secrets, and configuration across all your infrastructure and applications.</p>

link_buttons:
  primary:
    label: Get Started
    link: /docs/esc/get-started/

sections:
- type: cards-logo-label-link
  heading: Secrets Integrations
  description: <p>Integrate with popular secrets stores to pull and synchronize secrets and configuration data, including <a href="/docs/esc/integrations/dynamic-secrets/aws-secrets/">AWS Secrets Manager</a>, <a href="/docs/esc/integrations/dynamic-secrets/azure-secrets/">Azure Key Vault</a>, <a href="/docs/esc/integrations/dynamic-secrets/gcp-secrets/">GCP Secret Manager</a>, <a href="/docs/esc/integrations/dynamic-secrets/vault-secrets/">HashiCorp Vault</a>, and <a href="/docs/esc/integrations/dynamic-secrets/1password-secrets/">1Password</a>.</p>
  cards:
  - label: AWS Secrets Manager
    icon: aws-40
    link: /docs/esc/integrations/dynamic-secrets/aws-secrets/
  - label: Azure Key Vault
    icon: azure-40
    link: /docs/esc/integrations/dynamic-secrets/azure-secrets/
  - label: GCP Secret Manager
    icon: google-cloud-40
    link: /docs/esc/integrations/dynamic-secrets/gcp-secrets/
  - label: HashiCorp Vault
    icon: vault-40
    link: /docs/esc/integrations/dynamic-secrets/vault-secrets/
- type: cards-logo-label-link
  heading: Languages
  description: Manage configuration and secrets intuitively on any cloud using familiar languages.
  cards:
  - label: Node.js
    icon: icon-32-32 node-color-32-32
    link: /docs/esc/development/languages-sdks/javascript/
  - label: Python
    icon: icon-32-32 python-color-32-32
    link: /docs/esc/development/languages-sdks/python/
  - label: Go
    icon: icon-32-32 go-color-32-32
    link: /docs/esc/development/languages-sdks/go/
  - label: YAML
    icon: icon-32-32 yaml-color-32-32
    link: /docs/reference/esc-syntax/
- type: button-cards
  heading: Capabilities
  cards:
  - emoji: 💻
    heading: ESC CLI
    link: /docs/esc/cli/
    description: Command-line interface for managing environments, secrets, and configuration.
  - emoji: 🔑
    heading: Dynamic Login Credentials
    description: Support for short-lived OIDC login credentials for popular cloud providers.
    link: /docs/esc/integrations/dynamic-login-credentials/
  - emoji: 🔐
    heading: Dynamic Secrets Providers
    description: Integrate with secrets stored in external providers using dynamic configuration providers.
    link: /docs/esc/integrations/dynamic-secrets/
  - emoji: 🔔
    heading: ESC Webhooks
    description: Automate your processes with environment event webhooks.
    link: /docs/esc/environments/webhooks/
- type: button-cards
  heading: Resources
  cards:
  - emoji: 💡
    heading: Concepts
    description: Understand core ESC concepts including environments, sources, targets, and management.
    link: /docs/esc/concepts/
  - emoji: 📁
    heading: Environments
    description: Create and manage environments for organizing secrets and configuration.
    link: /docs/esc/environments/
  - emoji: 🔗
    heading: Integrations
    description: Connect to external secret stores, cloud providers, and development tools.
    link: /docs/esc/integrations/
  - emoji: 🛠️
    heading: Development
    description: Use SDKs, Pulumi Service Provider, and Automation API for programmatic access.
    link: /docs/esc/development/
# - type: full-width-cards
#   heading: Reference
#   cards:
#     - icon: code-tree-blue-21-21
#       heading: Pulumi Cloud REST API docs
#       description: Leverage automation with the Pulumi Cloud REST API.
#       link: /docs/pulumi-cloud/cloud-rest-api/
#     - icon: terminal-blue-21-21
#       heading: Pulumi CLI docs
#       description: Browse the complete documentation of available CLI commands.
#       link: /docs/cli/
- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---
