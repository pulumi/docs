---
title: "Google Cloud"
meta_desc: Complete list of Pulumi Best Practices compliance policies for Google Cloud.
h1: "Pulumi Best Practices - Google Cloud"
menu:
  reference:
    identifier: reference-pre-built-policy-packs-pulumi-best-practices-google-cloud
    parent: reference-pre-built-policy-packs-pulumi-best-practices
    weight: 3
---

This page lists all 35 policies in the **Pulumi Best Practices** pack for **Google Cloud**.

| Policy Name | Description | Framework Reference | Framework Specification |
| ----- | ----- | ----- | ----- |
| bucket-iam-least-privilege | Enforce least privilege access for Cloud Storage bucket IAM policies | 1. Least Privilege | Ensure all identities and services have only the minimum permissions required to perform their tasks. |
| iam-no-broad-roles | Enforce least privilege access control by prohibiting overly broad roles | 1. Least Privilege | Ensure all identities and services have only the minimum permissions required to perform their tasks. |
| pubsub-topic-iam-least-privilege | Enforce least privilege IAM policies for Pub/Sub topics | 1. Least Privilege | Ensure all identities and services have only the minimum permissions required to perform their tasks. |
| compute-instance-encrypted-attached-disk | Require Compute Engine instances to have encrypted attached disks | 2. Resource Encryption at Rest | Encrypt all stored data using approved encryption mechanisms to protect against unauthorized access. |
| compute-instance-encrypted-boot-disk | Require Compute Engine instances to have encrypted boot disks | 2. Resource Encryption at Rest | Encrypt all stored data using approved encryption mechanisms to protect against unauthorized access. |
| gke-secrets-encryption | Require GKE clusters to have Application-layer Secrets Encryption enabled | 2. Resource Encryption at Rest | Encrypt all stored data using approved encryption mechanisms to protect against unauthorized access. |
| bucket-customer-managed-kms | Require Cloud Storage buckets to use customer-managed Cloud KMS keys for encryption | 2. Resource Encryption at Rest | Encrypt all stored data using approved encryption mechanisms to protect against unauthorized access. |
| cloudsql-ssl | Require Cloud SQL connections to use SSL/TLS encryption | 3. Transport Layer Encryption | Require secure protocols (e.g., TLS) for all data in transit to prevent interception or tampering. |
| cloud-cdn-origin-tls | Require Cloud CDN to use secure TLS to origin | 3. Transport Layer Encryption | Require secure protocols (e.g., TLS) for all data in transit to prevent interception or tampering. |
| load-balancer-tls | Require Cloud Load Balancers to disallow unencrypted traffic | 3. Transport Layer Encryption | Require secure protocols (e.g., TLS) for all data in transit to prevent interception or tampering. |
| gke-private-endpoints | Require GKE cluster API endpoints to be private | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| bucket-no-public-read | Require Cloud Storage buckets to disallow public read access | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| cloudsql-private-ip | Require Cloud SQL instances to be deployed with private IP only | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| compute-no-public-ip | Require Compute Engine instances to disallow public IP addresses | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| resource-labeling | Require all GCP resources to have proper labeling for change tracking | 5. Tagging | Enforce standardized resource tags for ownership, environment, and compliance tracking. |
| environment-label | Require all labelable resources to have an environment label | 5. Tagging | Enforce standardized resource tags for ownership, environment, and compliance tracking. |
| cloud-build-logging | Require Cloud Build triggers to have secure logging configurations | 6. Enforce Logging | Enable and retain audit logs for all security-relevant actions and events. |
| bucket-access-logging | Require Cloud Storage buckets to have access logging enabled for audit trails | 6. Enforce Logging | Enable and retain audit logs for all security-relevant actions and events. |
| load-balancer-logging | Require Cloud Load Balancers to configure access logging | 6. Enforce Logging | Enable and retain audit logs for all security-relevant actions and events. |
| cloudsql-high-availability | Require Cloud SQL instances to have high availability configuration across zones | 7. High Availability | Deploy resources in redundant, fault-tolerant configurations to ensure service continuity. |
| load-balancer-multi-zone | Require Cloud Load Balancers to be configured across multiple zones for high availability | 7. High Availability | Deploy resources in redundant, fault-tolerant configurations to ensure service continuity. |
| load-balancer-health-checks | Require Cloud Load Balancers to enable health checks for monitoring backend instance health | 7. High Availability | Deploy resources in redundant, fault-tolerant configurations to ensure service continuity. |
| bucket-multi-region | Require Cloud Storage buckets to have multi-region replication for business continuity | 7. High Availability | Deploy resources in redundant, fault-tolerant configurations to ensure service continuity. |
| pubsub-dead-letter-queue | Require Pub/Sub subscriptions to have dead letter queue configuration | 8. Require DLQ | Ensure all asynchronous messaging systems are configured with a dead-letter queue to handle failures. |
| cloud-tasks-retry-configuration | Require Cloud Tasks queues to have proper retry configuration for business continuity | 9. Resource Availability | Define and enforce timeouts, quotas, and capacity limits to prevent resource exhaustion. |
| firewall-ssh-rdp | Enforce firewall rule restrictions for SSH and RDP access | 11. Networking | Only allow required inbound and outbound traffic through network security groups, firewalls, or ACLs. |
| firewall-strict | Enforce strict firewall rules with explicit allow/deny configuration | 11. Networking | Only allow required inbound and outbound traffic through network security groups, firewalls, or ACLs. |
| firewall-no-http-ingress | Require firewall rules to disallow inbound HTTP traffic from unauthorized sources | 11. Networking | Only allow required inbound and outbound traffic through network security groups, firewalls, or ACLs. |
| firewall-no-public-ingress | Require firewall rules to disallow public internet ingress unless specifically authorized | 11. Networking | Only allow required inbound and outbound traffic through network security groups, firewalls, or ACLs. |
| cloudfunctions-documentation | Require Cloud Functions to have adequate documentation | 12. Documentation | Maintain up-to-date documentation of architectures, configurations, policies, and procedures to ensure clarity, consistency, and auditability. |
| bucket-versioning | Require Cloud Storage buckets to have versioning enabled for data protection | 13. Data Backup and Recovery | Regularly back up critical data and systems, store backups securely, and test recovery procedures to ensure timely restoration after failures or disasters. |
| cloudsql-backup | Require Cloud SQL instances to have backup retention enabled | 13. Data Backup and Recovery | Regularly back up critical data and systems, store backups securely, and test recovery procedures to ensure timely restoration after failures or disasters. |
| kms-key-rotation | Require Cloud KMS keys to have key rotation enabled | 14. Key Management & Rotation | Manage encryption keys securely and enforce periodic key rotation to reduce the risk of compromise. |
| kms-key-configuration | Require proper Cloud KMS key creation and configuration | 14. Key Management & Rotation | Manage encryption keys securely and enforce periodic key rotation to reduce the risk of compromise. |
| kms-key-lifecycle | Require proper Cloud KMS key deletion and lifecycle management | 14. Key Management & Rotation | Manage encryption keys securely and enforce periodic key rotation to reduce the risk of compromise. |
