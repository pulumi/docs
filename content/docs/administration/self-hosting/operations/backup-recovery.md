---
title_tag: "Backup and Recovery | Self-Hosting Pulumi"
meta_desc: Backup strategies, recovery procedures, and RTO targets for self-hosted Pulumi Cloud deployments.
title: Backup and Recovery
h1: Backup and Recovery
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Backup and Recovery
    parent: administration-security-compliance-self-hosted-operations
    weight: 7
    identifier: administration-security-compliance-self-hosted-operations-backup-recovery
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).
{{% /notes %}}

A reliable backup and recovery strategy is essential for self-hosted Pulumi Cloud. This page covers database backups, object storage protection, and recovery procedures.

## Database backups

### Automated backups

- Enable automated daily backups.
- Schedule backups during low-traffic periods.
- Test restore procedures regularly.

### Cross-region backups

For disaster recovery, copy backups to a secondary region:

- Enable point-in-time recovery (PITR) on your database.
- With versioning and cross-region replication on object storage enabled, you have:
  - Protection against accidental deletion (versioning)
  - Regional failure protection (cross-region replication)

## Recovery procedures

Document and test these recovery scenarios:

| Scenario | Recovery approach | RTO target |
| :-- | :-- | :-- |
| Single AZ failure | Automatic failover (DB, compute, LB) | < 5 minutes |
| Database instance failure | Automatic failover to replica | < 1 minute (Aurora), < 5 minutes (RDS) |
| Object storage corruption | Restore from versioned object | < 15 minutes |
| Full region failure | Restore DB from cross-region backup, fail over storage | 1–4 hours |
| Accidental state deletion | Restore from S3 versioning or DB PITR | < 30 minutes |

## Resource protection

- Enable deletion protection on your database cluster and load balancer.
- Mark critical Pulumi resources as `protect: true` in your IaC code to prevent accidental destruction.
- Take a final snapshot before any planned database deletion.
