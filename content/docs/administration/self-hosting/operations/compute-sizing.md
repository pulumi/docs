---
title_tag: "Compute Sizing | Self-Hosting Pulumi"
meta_desc: Container resource allocation and minimum infrastructure requirements for self-hosted Pulumi Cloud across ECS, EKS, and BYO deployments.
title: Compute Sizing
h1: Compute Sizing
menu:
  administration:
    name: Compute Sizing
    parent: administration-security-compliance-self-hosted-operations
    weight: 3
    identifier: administration-security-compliance-self-hosted-operations-compute-sizing
---

{{< self-hosting-trial-note />}}

The API service and console are stateless containers. This page documents recommended container resource allocations and minimum infrastructure requirements.

For component configuration details, see [Components](/docs/administration/self-hosting/components/).

## Recommended container resources

| Service | CPU | Memory | Notes |
| :-- | :-- | :-- | :-- |
| API | 2048m (2 vCPU) | 4096 Mi (4 GB) | Scale horizontally for HA |
| Console | 512m (0.5 vCPU) | 512 Mi | Static web UI, low resource usage |
| Migrations | 128m | 128 Mi | Runs once per upgrade before service rollout |

For production, 2 vCPU / 4 GB RAM per API instance is a good starting point. Scale horizontally (more instances) rather than vertically for the API service, since it is stateless and benefits from running behind a load balancer across multiple AZs.

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
