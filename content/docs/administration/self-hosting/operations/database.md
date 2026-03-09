---
title_tag: "Database Best Practices | Self-Hosting Pulumi"
meta_desc: Best practices for MySQL database configuration, high availability, sizing, and migrations for self-hosted Pulumi Cloud.
title: Database
h1: Database Best Practices
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Database
    parent: administration-security-compliance-self-hosted-operations
    weight: 2
    identifier: administration-security-compliance-self-hosted-operations-database
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).
{{% /notes %}}

Pulumi Cloud uses MySQL 8.0 for metadata, stack state references, and user/organization data. This page covers best practices for database configuration in production self-hosted deployments.

## Use a managed MySQL service

Deploy MySQL 8.0 on a managed service rather than self-managing:

- **AWS**: Amazon Aurora MySQL (recommended) or RDS MySQL
- **Azure**: Azure Database for MySQL Flexible Server
- **GCP**: Cloud SQL for MySQL
- **On-prem**: MySQL 8.0 with InnoDB, configured for replication

## High availability configuration

### Multi-AZ and read replicas

Deploy your database cluster across multiple availability zones with at least one read replica:

- **Aurora**: Use a cluster with a writer instance and one or more reader instances in separate AZs. Aurora handles automatic failover to a reader within approximately 30 seconds.
- **RDS**: Enable Multi-AZ deployment for automatic standby failover.
- **Cloud SQL / Azure MySQL**: Enable high-availability configuration (regional availability).

### Instance sizing

The self-hosted installers default to the following database instance types:

| Installer | Default instance type | Notes |
| :-- | :-- | :-- |
| ECS | db.t3.medium (4 GB RAM) | Suitable for small-to-medium workloads |
| EKS | db.r5.large (16 GB RAM) | Memory-optimized, better for production |
| GKE | db-g1-small (1.7 GB RAM) | Minimal; upgrade for production use |

For production workloads, start with a memory-optimized instance (db.r5.large, db.r6g.large, or equivalent with 16 GB RAM) and scale based on monitoring. Burstable instances (db.t3.*) are acceptable for development and light workloads but may throttle under sustained load.

### Connection pooling

For AWS deployments with many concurrent users, consider placing [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/) in front of your Aurora or RDS instance. RDS Proxy pools and shares database connections, reducing connection overhead and improving failover times.

## Zero-downtime migrations

Pulumi Cloud runs database migrations as a separate task before deploying new application versions. For self-hosted deployments:

- Run migrations before updating service containers.
- The self-hosted installers handle this automatically via a dedicated migration task/job.
- If running migrations manually, ensure they complete before restarting services.

See [Upgrades](/docs/administration/self-hosting/operations/upgrades/) for the full update process.
