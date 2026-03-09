---
title_tag: "Networking and Load Balancing | Self-Hosting Pulumi"
meta_desc: Best practices for multi-AZ deployment, network architecture, auto-scaling, load balancing, TLS, and DNS for self-hosted Pulumi Cloud.
title: Networking
h1: Networking and load balancing
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Networking
    parent: administration-security-compliance-self-hosted-operations
    weight: 5
    identifier: administration-security-compliance-self-hosted-operations-networking
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).
{{% /notes %}}

This page covers network architecture, multi-AZ deployment, auto-scaling, load balancing, and DNS configuration for production self-hosted deployments.

For ingress/egress port requirements, see [Network requirements](/docs/administration/self-hosting/network/).

## Multi-AZ deployment

Deploy compute resources across at least two availability zones:

- **Kubernetes**: Spread pods across AZs using pod anti-affinity or topology spread constraints.
- **ECS/Fargate**: Configure services to launch tasks across multiple subnets in different AZs.
- **VMs**: Use auto-scaling groups spanning multiple AZs.

## Network architecture

Deploy a VPC/VNet with subnets in 2+ AZs, separated by tier:

- **Public subnets**: Load balancers, NAT gateways
- **Private subnets**: Application containers
- **Database subnets**: Database instances (no public access)

Additional recommendations:

- Deploy one NAT gateway per AZ to avoid cross-AZ NAT bottlenecks.
- Use VPC endpoints or private endpoints for object storage access to reduce NAT traffic and improve performance.

## Auto-scaling

Configure auto-scaling for the API service based on CPU utilization:

- **Target**: 50-60% average CPU utilization
- **Minimum instances**: 2 (for HA across AZs)
- **Maximum instances**: 4x desired count (to handle burst traffic)
- **Scale-in protection**: Use graceful draining to allow in-flight requests to complete before terminating instances

## Graceful shutdown

When scaling in or deploying updates, ensure containers have time to finish in-flight requests:

- Set container stop timeout to at least 120 seconds.
- **Kubernetes**: Set `terminationGracePeriodSeconds: 130` on the API pod spec.
- **ECS**: Configure deregistration delay on the target group and set `stopTimeout` on the container definition.
- Use lifecycle hooks (ECS) or preStop hooks (Kubernetes) to drain connections before shutdown.

## Load balancer configuration

- Deploy an Application Load Balancer (or equivalent).
- Enable deletion protection on the load balancer in production.
- Configure health checks for the API service (`/api/status` endpoint).
- Set health check grace period to 120 seconds to allow containers to start.

## DNS

Configure two DNS records pointing to your load balancer:

- `api.{domain}` - for CLI and API access
- `app.{domain}` - for web console access
