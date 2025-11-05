---
title: "Pulumi Best Practices - Azure"
meta_desc: Complete list of Pulumi Best Practices compliance policies for Azure.
h1: "Pulumi Best Practices policies for Azure"
---

This page lists all 29 policies in the **Pulumi Best Practices** pack for **Azure**.

| Policy Name | Description | Framework Reference | Framework Specification |
| ----- | ----- | ----- | ----- |
| vm-approved-images | Require pre-approved hardened VM images from trusted publishers | 10. Approved Versions | Only allow deployment of approved, patched, and supported versions of runtimes, images, and dependencies. |
| nsg-disallow-public-internet-ingress | Require Network Security Groups to disallow public internet ingress | 11. Networking | Only allow required inbound and outbound traffic through network security groups, firewalls, or ACLs. |
| nsg-strict-rules | Require strict Network Security Group rules with explicit allow/deny configuration | 11. Networking | Only allow required inbound and outbound traffic through network security groups, firewalls, or ACLs. |
| cosmos-db-backup-policies | Require Cosmos DB account to have backup policies configured | 13. Data Backup and Recovery | Regularly back up critical data and systems, store backups securely, and test recovery procedures to ensure timely restoration after failures or disasters. |
| key-vault-soft-delete | Require Key Vault to have soft delete enabled with appropriate retention | 13. Data Backup and Recovery | Regularly back up critical data and systems, store backups securely, and test recovery procedures to ensure timely restoration after failures or disasters. |
| sql-database-backup-retention | Require Azure SQL Database to have backup retention configured with redundant storage | 13. Data Backup and Recovery | Regularly back up critical data and systems, store backups securely, and test recovery procedures to ensure timely restoration after failures or disasters. |
| storage-account-geo-replication | Require Storage Accounts to have geo-replication enabled for business continuity | 13. Data Backup and Recovery | Regularly back up critical data and systems, store backups securely, and test recovery procedures to ensure timely restoration after failures or disasters. |
| key-vault-key-configuration | Require proper Key Vault key creation and configuration | 14. Key Management & Rotation | Manage encryption keys securely and enforce periodic key rotation to reduce the risk of compromise. |
| key-vault-key-lifecycle | Require proper Key Vault key deletion and lifecycle management | 14. Key Management & Rotation | Manage encryption keys securely and enforce periodic key rotation to reduce the risk of compromise. |
| key-vault-key-rotation | Require Key Vault keys to have rotation policies configured | 14. Key Management & Rotation | Manage encryption keys securely and enforce periodic key rotation to reduce the risk of compromise. |
| sql-database-customer-managed-keys | Require Azure SQL databases to use customer-managed keys for transparent data encryption | 2. Resource Encryption at Rest | Encrypt all stored data using approved encryption mechanisms to protect against unauthorized access. |
| storage-account-uses-customer-managed-keys | Require Storage Accounts to use customer-managed keys for encryption | 2. Resource Encryption at Rest | Encrypt all stored data using approved encryption mechanisms to protect against unauthorized access. |
| vm-requires-managed-disks | Require VMs to use managed disks only | 2. Resource Encryption at Rest | Encrypt all stored data using approved encryption mechanisms to protect against unauthorized access. |
| application-gateway-tls | Require Application Gateway to have secure TLS configuration | 3. Transport Layer Encryption | Require secure protocols (e.g., TLS) for all data in transit to prevent interception or tampering. |
| front-door-tls | Require Front Door custom domains to use secure TLS configuration | 3. Transport Layer Encryption | Require secure protocols (e.g., TLS) for all data in transit to prevent interception or tampering. |
| storage-account-https-only | Require Storage Accounts to enforce HTTPS-only traffic | 3. Transport Layer Encryption | Require secure protocols (e.g., TLS) for all data in transit to prevent interception or tampering. |
| network-interface-no-public-ip | Require Network Interfaces to have no public IP address associations | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| sql-server-disable-public-access | Require Azure SQL Server to disable public network access | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| storage-account-public-access | Require Storage Accounts to disable public blob access | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| resources-change-tracking-tags | Require all Azure resources to have proper tagging for change tracking | 5. Tagging | Enforce standardized resource tags for ownership, environment, and compliance tracking. |
| resources-environment-tags | Require all resources to have environment tags | 5. Tagging | Enforce standardized resource tags for ownership, environment, and compliance tracking. |
| sql-server-audit-logging | Require Azure SQL Server to have audit logging enabled | 6. Enforce Logging | Enable and retain audit logs for all security-relevant actions and events. |
| log-analytics-retention | Require Log Analytics workspace to have appropriate retention policies | 6. Enforce Logging | Enable and retain audit logs for all security-relevant actions and events. |
| application-gateway-multi-az | Require Application Gateway to be configured across multiple availability zones | 7. High Availability | Deploy resources in redundant, fault-tolerant configurations to ensure service continuity. |
| load-balancer-multi-az | Require Load Balancer to be configured across multiple availability zones | 7. High Availability | Deploy resources in redundant, fault-tolerant configurations to ensure service continuity. |
| sql-database-high-availability | Require Azure SQL Database to have high availability configuration | 7. High Availability | Deploy resources in redundant, fault-tolerant configurations to ensure service continuity. |
| service-bus-dead-letter-queue | Validate Service Bus queues have proper dead letter queue configuration | 8. Require DLQ | Ensure all asynchronous messaging systems are configured with a dead-letter queue to handle failures. |
| application-gateway-has-health-probes | Require Application Gateway to enable health probes | 9. Resource Availability | Define and enforce timeouts, quotas, and capacity limits to prevent resource exhaustion. |
| load-balancer-health-probes | Require Load Balancer to enable health probes | 9. Resource Availability | Define and enforce timeouts, quotas, and capacity limits to prevent resource exhaustion. |
