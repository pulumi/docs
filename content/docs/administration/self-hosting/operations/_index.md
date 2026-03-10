---
title_tag: "Operations Guide | Self-Hosting Pulumi"
meta_desc: Production operations guide for self-hosted Pulumi Cloud covering high availability, disaster recovery, monitoring, sizing, and security hardening.
title: Operations
h1: Self-Hosted Operations Guide
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Operations
    parent: administration-self-hosting
    weight: 6
    identifier: administration-security-compliance-self-hosted-operations
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).
{{% /notes %}}

This guide provides best practices for deploying and operating Pulumi Cloud in a self-hosted configuration with high availability (HA) and disaster recovery (DR). These recommendations are derived from how Pulumi operates its own managed service and adapted for self-hosted deployments.

## Production readiness checklist

Use this checklist when planning or validating your self-hosted deployment.

### Pre-deployment

- Choose deployment platform ([ECS](/docs/administration/self-hosting/deployment-options/ecs-hosted/), [EKS](/docs/administration/self-hosting/deployment-options/eks-hosted/), [AKS](/docs/administration/self-hosting/deployment-options/aks-hosted/), [GKE](/docs/administration/self-hosting/deployment-options/gke-hosted/), [BYO](/docs/administration/self-hosting/deployment-options/byo-infra-hosted/))
- Obtain Pulumi Cloud license key from your Pulumi contact
- Define domain names for API and console endpoints
- Obtain or generate TLS certificates
- Get SMTP server credentials (optional for testing, required for production)
- Set up Cloudflare Turnstile for bot protection (recommended for publicly accessible installations)
- Commit installer code as-is to your own source control before customizing

### Infrastructure

- Database deployed in [multi-AZ configuration](/docs/administration/self-hosting/operations/database/)
- Object storage buckets created with [versioning enabled](/docs/administration/self-hosting/operations/object-storage/)
- Network configured with public and private subnets across 2+ AZs
- Security groups restrict traffic between tiers

### Application

- API service and console deployed with 2+ replicas
- Database migrations run successfully
- DNS records configured for both API and console domains
- TLS termination configured on load balancer
- Health checks passing for all services

### Operations

- [Monitoring and alerting](/docs/administration/self-hosting/operations/monitoring/) configured (CPU, memory, error rates, storage)
- Database [backup schedule configured](/docs/administration/self-hosting/operations/backup-recovery/) with cross-region copies
- Object storage replication configured (if multi-region)
- Recovery procedures documented and tested
- Ingress allowlist configured (if restricting access)
- Deletion protection enabled on database and load balancer

### Validation

- `pulumi login https://api.{domain}` succeeds from CLI
- Console accessible at `https://app.{domain}` in browser
- User signup and login work correctly
- Stack create, update, and destroy operations work
- Email invitations work (if SMTP configured)
