---
title_tag: "Object Storage Best Practices | Self-Hosting Pulumi"
meta_desc: Best practices for object storage configuration, bucket architecture, versioning, and lifecycle management for self-hosted Pulumi Cloud.
title: Object storage
h1: Object storage best practices
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Object Storage
    parent: administration-security-compliance-self-hosted-operations
    weight: 4
    identifier: administration-security-compliance-self-hosted-operations-object-storage
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).
{{% /notes %}}

Pulumi Cloud uses object storage for checkpoint (state) files, policy packs, and other data. This page covers the storage architecture and best practices for production deployments.

## Storage architecture

Pulumi Cloud uses multiple storage buckets. The exact set depends on your installer and which features are enabled:

| Bucket | Created by | Purpose |
| :-- | :-- | :-- |
| Checkpoints | All installers | Stack state files. Frequent read/write, versioning critical |
| Policy packs | All installers | Policy package artifacts. Infrequent write, frequent read |
| Service metadata / ESC | EKS, AKS, GKE, ECS | Service metadata and Pulumi ESC (Environments, Secrets, Configuration) data |
| Engine events | EKS | Engine event logs from `pulumi up` / `pulumi destroy` operations |

The **checkpoints** and **policy packs** buckets are required for all deployments. The **service metadata / ESC** bucket is required if you use Pulumi ESC. The **engine events** bucket is optional - engine events are stored in the database if this bucket is not configured.

The [BYO Infrastructure](/docs/administration/self-hosting/deployment-options/byo-infra-hosted/) installer does not create buckets. You must provide pre-existing S3-compatible buckets via configuration.

For bucket environment variable configuration, see [API component - Object storage](/docs/administration/self-hosting/components/api/#object-storage).

## High availability

- Use your cloud provider's natively redundant storage (S3, Azure Blob, GCS) - these replicate across AZs by default.
- For on-prem deployments with S3-compatible storage (MinIO, Ceph): deploy across multiple nodes with erasure coding.

## Cross-region replication

For disaster recovery, enable cross-region replication on your checkpoint and policy pack buckets:

- **AWS S3**: Enable S3 Cross-Region Replication (CRR) to a bucket in a secondary region.
- **Azure Blob Storage**: Use object replication or geo-redundant storage (GRS/GZRS).
- **GCP Cloud Storage**: Use dual-region or multi-region buckets, or configure Turbo Replication for faster RPO.

See [Backup and recovery](/docs/administration/self-hosting/operations/backup-recovery/) for full disaster recovery procedures.

## Versioning and lifecycle

- Enable versioning on the checkpoints bucket. This protects against accidental state corruption.
- Configure lifecycle rules:
  - Delete non-current object versions after 30 days.
  - Clean up incomplete multipart uploads after 14 days.
  - These reduce storage costs while maintaining a recovery window.
