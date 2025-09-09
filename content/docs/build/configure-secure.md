---
title: Configure & Secure
h1: Configure & Secure
capability: build
menu:
    build:
        name: Configure & Secure
        identifier: build-configure-secure
        parent: build-core-concepts
        weight: 50
meta_desc: Configure applications and manage secrets during individual development with Pulumi ESC and IaC configuration.
meta_image: /images/docs/meta-images/docs-meta.png
---

Configure applications and manage secrets during individual development. Learn how to handle configuration, environments, secrets, and infrastructure integration for your daily engineering work.

## Basic Configuration

Manage configuration settings for your infrastructure and applications:

- [Configuration fundamentals](/docs/iac/concepts/config/) - Core configuration concepts
- [Project configuration](/docs/iac/concepts/projects/) - Configure projects and stacks

## Environment Management

Use Pulumi ESC for environment configuration:

- [Environment fundamentals](/docs/esc/environments/) - ESC environment basics
- [Working with environments](/docs/esc/environments/working-with-environments/) - Environment workflows
- [Environment composition](/docs/esc/environments/imports/) - Environment imports and composition

## Development Secrets & Login

Securely handle secrets and dynamic credentials during development:

- [Dynamic secrets](/docs/esc/integrations/dynamic-secrets/) - Dynamic secrets providers
- [AWS login credentials](/docs/esc/integrations/dynamic-login-credentials/aws-login/) - AWS OIDC login
- [Azure login credentials](/docs/esc/integrations/dynamic-login-credentials/azure-login/) - Azure OIDC login
- [GCP login credentials](/docs/esc/integrations/dynamic-login-credentials/gcp-login/) - GCP OIDC login

## Infrastructure Integration

Connect ESC with your infrastructure:

- [Infrastructure integrations](/docs/esc/integrations/infrastructure/) - ESC infrastructure integration overview
- [Pulumi IaC integration](/docs/esc/integrations/infrastructure/pulumi-iac/) - Using ESC with Pulumi IaC
- [Kubernetes integration](/docs/esc/integrations/kubernetes/) - ESC with Kubernetes

## Getting Started

- [Get started with ESC](/docs/esc/get-started/) - Create your first environment
- [Configuration best practices](/docs/iac/concepts/config/) - Configuration patterns and security
