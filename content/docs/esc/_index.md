---
title: Pulumi ESC
linktitle: Pulumi ESC
docs_home: true
notitle: true
menu:
  esc:
    identifier: esc-home
    weight: 1
expanded_menu_ids:
    - esc-environments
    - esc-integrations
    - esc-development
aliases:
  - /docs/pulumi-cloud/esc/

meta_desc: Learn how to tame secrets sprawl and configuration complexity securely across all your cloud infrastructure and applications with Pulumi ESC.
meta_image: /images/docs/meta-images/docs-meta.png
h1: Pulumi ESC Docs
description: <p>Pulumi ESC is a secrets management & orchestration service for environments, secrets, and configurations.</p>

link_buttons:
  primary:
    label: Get Started
    link: /docs/esc/get-started/
  secondary:
    label: Install
    link: /docs/esc/download-install/

sections:
- type: flat
  heading: Overview
  description_md: |
    Pulumi ESC (Environments, Secrets, and Configuration) allows teams to tackle secrets and configuration complexity for modern cloud environments, alleviating maintenance burden and reducing costly mistakes, and creating a “secure by default” posture.

    Pulumi ESC is a new category of configuration as code product, motivated by our experience working with hundreds of Pulumi IaC customers to address their needs in managing secrets and configuration at scale within their Pulumi infrastructure and across other cloud applications and infrastructure projects.
- type: cards-logo-label-link
  heading: Secrets Integrations
  description: <p>Pulumi ESC integrates with all of the most popular secrets stores to pull and synchronize secrets and configuration data, including <a href="/docs/esc/integrations/dynamic-secrets/aws-secrets/">AWS Secrets Manager</a>, <a href="/docs/esc/integrations/dynamic-secrets/azure-secrets/">Azure Key Vault</a>, <a href="/docs/esc/integrations/dynamic-secrets/gcp-secrets/">GCP Secret Manager</a>, <a href="/docs/esc/integrations/dynamic-secrets/vault-secrets/">HashiCorp Vault</a>, and <a href="/docs/esc/integrations/dynamic-secrets/1password-secrets/">1Password</a>.</p>
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
  # - label: 1Password
  #   icon: onepassword-40
  #   link: /docs/esc/integrations/dynamic-secrets/1password-secrets/
# - type: cards-logo-label-link
#   heading: Clouds
#   description: <p>Pulumi ESC supports AWS, Azure, Google Cloud, Kubernetes, and <a href="/docs/esc/integrations/">more</a>.</p>
#   cards:
#   - label: AWS & Pulumi ESC
#     icon: aws-40
#     link: /docs/esc/integrations/dynamic-login-credentials/aws-login/
#   - label: Azure & Pulumi ESC
#     icon: azure-40
#     link: /docs/esc/integrations/dynamic-login-credentials/azure-login/
#   - label: Google Cloud & Pulumi ESC
#     icon: google-cloud-40
#     link: /docs/esc/integrations/dynamic-login-credentials/gcp-login/
#   - label: Kubernetes & Pulumi ESC
#     icon: kubernetes-40
#     link: /docs/esc/integrations/kubernetes/
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
    link: /docs/esc/reference/
- type: button-cards
  heading: Featured Capabilities
  cards:
  - heading: ESC CLI
    link: /docs/esc/cli/
    description: An overview of the Pulumi ESC CLI.
    primary_button_label: Get Started
    primary_button_link: /docs/esc/cli/
    secondary_button_label: Install
    secondary_button_link: /docs/esc/download-install/
  - heading: Dynamic Login Credentials
    description: Support for short-lived OIDC login credentials for popular cloud providers.
    link: /docs/esc/integrations/dynamic-login-credentials/
  - heading: Dynamic Secrets Providers
    description: Support for dynamic configuration providers allow Pulumi ESC to integrate with secrets stored in any other provider.
    link: /docs/esc/integrations/dynamic-secrets/
  - heading: ESC Webhooks
    description: Automate your processes with environment event webhooks.
    link: /docs/esc/environments/webhooks/
- type: full-width-cards
  heading: Featured docs
  cards:
  - icon: lightbulb-blue-21-21
    heading: Detailed overview of environments
    description: Learn more about managing environments using Pulumi ESC.
    link: /docs/esc/environments/working-with-environments/
  - icon: terminal-blue-21-21
    heading: Integration with Docker
    description: Pulumi ESC integrates with Docker to manage configuration and secrets while running docker commands.
    link: /docs/esc/integrations/dev-tools/docker/
  - icon: swap-blue-21-21
    heading: Pulumi ESC vs HashiCorp Vault
    description: Learn about the major differences between Pulumi ESC and HashiCorp Vault.
    link: /docs/esc/vs/vault/
- type: blue-sparkle
  heading: Why Pulumi ESC?
  description: Pulumi ESC is a centralized secrets management & orchestration service. Easily access, share, and manage secrets securely on any cloud using your favorite programming languages. Pull and sync secrets with any secrets store, and consume secrets in any application, tool, or CI/CD platform.
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
