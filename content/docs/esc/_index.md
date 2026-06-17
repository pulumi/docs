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
description: <p>Pulumi ESC (Environments, Secrets, and Configuration) provides centralized secrets management and orchestration across all your infrastructure and applications.</p>

link_buttons:
  primary:
    label: Get Started
    link: /docs/esc/get-started/

sections:
- type: cards-logo-label-link
  heading: Secrets Integrations
  description: <p>Integrate with popular secrets stores to pull and synchronize secrets and configuration data, including <a href="/docs/esc/providers/secrets/aws-secrets/">AWS Secrets Manager</a>, <a href="/docs/esc/providers/secrets/azure-secrets/">Azure Key Vault</a>, <a href="/docs/esc/providers/secrets/gcp-secrets/">GCP Secret Manager</a>, <a href="/docs/esc/providers/secrets/vault-secrets/">HashiCorp Vault</a>, and <a href="/docs/esc/providers/secrets/1password-secrets/">1Password</a>.</p>
  cards:
  - label: AWS Secrets Manager
    icon: aws-40
    link: /docs/esc/providers/secrets/aws-secrets/
  - label: Azure Key Vault
    icon: azure-40
    link: /docs/esc/providers/secrets/azure-secrets/
  - label: GCP Secret Manager
    icon: google-cloud-40
    link: /docs/esc/providers/secrets/gcp-secrets/
  - label: HashiCorp Vault
    icon: vault-40
    link: /docs/esc/providers/secrets/vault-secrets/
- type: cards-logo-label-link
  heading: Languages & SDKs
  description: <p>Use the ESC SDKs to retrieve environment values from your application workloads at runtime and to manage environments programmatically. To consume an environment from a Pulumi IaC program, use <a href="/docs/esc/guides/integrate-with-pulumi-iac/">config</a> instead.</p>
  cards:
  - label: Node.js
    icon: icon-32-32 node-color-32-32
    link: /docs/esc/languages-sdks/javascript/
  - label: Python
    icon: icon-32-32 python-color-32-32
    link: /docs/esc/languages-sdks/python/
  - label: Go
    icon: icon-32-32 go-color-32-32
    link: /docs/esc/languages-sdks/go/
  - label: .NET
    icon: icon-32-32 dotnet-color-32-32
    link: /docs/esc/languages-sdks/dotnet/
- type: button-cards
  heading: Operations
  description: Day-to-day workflows for running Pulumi ESC.
  cards:
  - icon: lock-key
    heading: Manage secrets
    description: Store, retrieve, and organize secrets in ESC environments.
    link: /docs/esc/operations/managing-secrets/
  - icon: play
    heading: Run commands with pulumi env run
    description: Inject environment values into any command or script.
    link: /docs/esc/guides/running-commands/
  - icon: pulumi-iac
    heading: Use ESC with Pulumi IaC
    description: Consume environments from a Pulumi program.
    link: /docs/esc/guides/integrate-with-pulumi-iac/
  - icon: package
    heading: Compose environments
    description: Import environments to share configuration across teams.
    link: /docs/esc/concepts/imports/
- type: button-cards
  heading: Capabilities
  cards:
  - icon: desktop
    heading: Pulumi CLI
    link: /docs/iac/cli/commands/pulumi_env/
    description: Command-line interface for managing environments, secrets, and configuration.
  - icon: key
    heading: Login providers
    description: Issue short-lived OIDC credentials for AWS, Azure, GCP, GitHub, and more.
    link: /docs/esc/providers/login/
  - icon: lock-key
    heading: Secrets providers
    description: Dynamically import secrets from external stores into your environment.
    link: /docs/esc/providers/secrets/
  - icon: bell
    heading: Webhooks
    description: Automate processes with environment event webhooks.
    link: /docs/esc/concepts/webhooks/
- type: button-cards
  heading: Resources
  cards:
  - icon: lightbulb
    heading: Concepts
    description: Understand core ESC concepts including environments, sources, targets, and composition.
    link: /docs/esc/concepts/
  - icon: folder
    heading: Environments
    description: Reference for the ESC YAML syntax, imports, versioning, and webhooks.
    link: /docs/esc/concepts/environments/
  - icon: link
    heading: Guides
    description: Use ESC with Docker, direnv, GitHub Actions, Kubernetes, Cloudflare, and Pulumi IaC.
    link: /docs/esc/guides/
  - icon: wrench
    heading: Languages & SDKs
    description: Manage ESC programmatically from .NET, Go, JavaScript, and Python.
    link: /docs/esc/languages-sdks/
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
