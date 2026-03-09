---
title_tag: "Compute Sizing | Self-Hosting Pulumi"
meta_desc: Container resource allocation and minimum infrastructure requirements for self-hosted Pulumi Cloud across ECS, EKS, and BYO deployments.
title: Compute Sizing
h1: Compute Sizing
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Compute Sizing
    parent: administration-security-compliance-self-hosted-operations
    weight: 3
    identifier: administration-security-compliance-self-hosted-operations-compute-sizing
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).
{{% /notes %}}

The API service and console are stateless containers. This page documents recommended container resource allocations and minimum infrastructure requirements.

For component configuration details, see [Components](/docs/administration/self-hosting/components/).

## Recommended container resources

| Service | CPU | Memory | Notes |
| :-- | :-- | :-- | :-- |
| API | 2048m (2 vCPU) | 1024 Mi (1 GB) | Scale horizontally for HA |
| Console | 512m (0.5 vCPU) | 512 Mi | Static web UI, low resource usage |
| Migrations | 128m | 128 Mi | Runs once per upgrade before service rollout |

For production, 2 vCPU / 1 GB RAM per API instance is a good starting point. Scale horizontally (more instances) rather than vertically for the API service, since it is stateless and benefits from running behind a load balancer across multiple AZs.

{{% notes type="info" %}}
The ECS installer exposes `apiTaskCpu` and `apiTaskMemory` Pulumi config options for customizing API service resources. Other installers can adjust resource requests/limits directly in the Kubernetes manifests.
{{% /notes %}}

## Minimum infrastructure requirements

### Production (high availability)

| Component | Specification |
| :-- | :-- |
| Database | MySQL 8.0.x, multi-AZ, 2+ instances (writer + reader), 20 GB+ SSD |
| Object storage | S3-compatible, 200 GB+ SSD, versioning enabled |
| Compute | 2+ instances/pods across 2+ AZs, 2 vCPU / 4 GB RAM per instance minimum |
| Load balancer | Application load balancer across 2+ AZs |
| Network | VPC with public and private subnets in 2+ AZs |
| DNS | Two A records: `api.{domain}` and `app.{domain}` |
| TLS | Certificates for both API and console domains |

### Development and evaluation

| Component | Specification |
| :-- | :-- |
| Database | MySQL 8.0, single instance, 20 GB SSD |
| Object storage | S3-compatible, 50 GB |
| Compute | Single instance, 2 vCPU / 4 GB RAM |
| DNS | Two DNS records (or use self-signed certificates with local hosts entries) |
