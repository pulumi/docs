---
title: "Pulumi Best Practices - AWS"
meta_desc: Complete list of Pulumi Best Practices compliance policies for AWS.
h1: "Pulumi Best Practices policies for AWS"
---

This page lists all 54 policies in the **Pulumi Best Practices** pack for **AWS**.

| Policy Name | Description | Framework Reference | Framework Specification |
| ----- | ----- | ----- | ----- |
| ec2-instance-disallow-unencrypted-root-block-device | Checks that EC2 instances does not have unencrypted root volumes. |  |  |
| ec2-instance-disallow-unencrypted-block-device | Checks that EC2 instances do not have unencrypted block devices. |  |  |
| ec2-launch-template-disallow-unencrypted-block-device | Checks that EC2 Launch Templates do not have unencrypted block device. |  |  |
| ec2-launch-configuration-disallow-unencrypted-block-device | Checks that EC2 Launch Configurations do not have unencrypted block devices. |  |  |
| pubsub-least-privilege-iam | Ensures IAM policies follow least privilege principles for Pub/Sub services (SNS, SQS, Kinesis) | 1. Least Privilege | Ensure all identities and services have only the minimum permissions required to perform their tasks. |
| s3-bucket-least-privilege | Prevents overly permissive S3 bucket policies | 1. Least Privilege | Ensure all identities and services have only the minimum permissions required to perform their tasks. |
| iam-policy-least-privilege | Ensures IAM policies follow least privilege principles | 1. Least Privilege | Ensure all identities and services have only the minimum permissions required to perform their tasks. |
| iam-role-least-privilege | Ensures IAM roles follow least privilege principles | 1. Least Privilege | Ensure all identities and services have only the minimum permissions required to perform their tasks. |
| iam-role-policy-least-privilege | Ensures IAM role policies follow least privilege principles | 1. Least Privilege | Ensure all identities and services have only the minimum permissions required to perform their tasks. |
| iam-user-policy-least-privilege | Ensures IAM user policies follow least privilege principles | 1. Least Privilege | Ensure all identities and services have only the minimum permissions required to perform their tasks. |
| iam-group-policy-least-privilege | Ensures IAM group policies follow least privilege principles | 1. Least Privilege | Ensure all identities and services have only the minimum permissions required to perform their tasks. |
| security-group-ssh-rdp | Ensures security groups do not allow SSH/RDP from the internet | 11. Networking | Only allow required inbound and outbound traffic through network security groups, firewalls, or ACLs. |
| security-group-default-deny | Ensures Security Groups follow default deny with explicit allow principle | 11. Networking | Only allow required inbound and outbound traffic through network security groups, firewalls, or ACLs. |
| security-group-strict | Ensures security groups follow strict firewall rules with default deny | 11. Networking | Only allow required inbound and outbound traffic through network security groups, firewalls, or ACLs. |
| lambda-function-documentation | Ensures all AWS Lambda functions have a documented description attribute | 12. Documentation | Maintain up-to-date documentation of architectures, configurations, policies, and procedures to ensure clarity, consistency, and auditability. |
| s3-bucket-replication | Ensures S3 buckets have replication configured for enhanced availability | 13. Data Backup and Recovery | Regularly back up critical data and systems, store backups securely, and test recovery procedures to ensure timely restoration after failures or disasters. |
| s3-bucket-versioning | S3 buckets must have versioning enabled using BucketVersioning resource | 13. Data Backup and Recovery | Regularly back up critical data and systems, store backups securely, and test recovery procedures to ensure timely restoration after failures or disasters. |
| rds-instance-enable-backup-retention | Checks that RDS Instances backup retention policy is enabled. | 13. Data Backup and Recovery | Regularly back up critical data and systems, store backups securely, and test recovery procedures to ensure timely restoration after failures or disasters. |
| kms-key-creation | Validates KMS key creation with appropriate specifications and origins | 14. Key Management & Rotation | Manage encryption keys securely and enforce periodic key rotation to reduce the risk of compromise. |
| kms-key-deletion-lifecycle | Validates KMS key deletion windows and lifecycle management | 14. Key Management & Rotation | Manage encryption keys securely and enforce periodic key rotation to reduce the risk of compromise. |
| kms-key-rotation-enabled | Checks that KMS Keys have key rotation enabled. | 14. Key Management & Rotation | Manage encryption keys securely and enforce periodic key rotation to reduce the risk of compromise. |
| rds-cluster-disallow-unencrypted-storage | Checks that RDS Clusters storage is encrypted. | 2. Resource Encryption at Rest | Encrypt all stored data using approved encryption mechanisms to protect against unauthorized access. |
| ebs-volume-encryption-required | Checks that EBS volumes are encrypted. | 2. Resource Encryption at Rest | Encrypt all stored data using approved encryption mechanisms to protect against unauthorized access. |
| s3-bucket-encryption | S3 buckets must have server-side encryption configured using BucketServerSideEncryptionConfiguration resource | 2. Resource Encryption at Rest | Encrypt all stored data using approved encryption mechanisms to protect against unauthorized access. |
| rds-encryption-enabled | Checks that RDS instance storage is encrypted. | 2. Resource Encryption at Rest | Encrypt all stored data using approved encryption mechanisms to protect against unauthorized access. |
| dynamodb-kms-encryption-enabled | Ensures DynamoDB tables have encryption enabled using KMS keys. | 2. Resource Encryption at Rest | Encrypt all stored data using approved encryption mechanisms to protect against unauthorized access. |
| rds-instance-ssl-encryption | Ensures RDS instances have SSL/TLS encryption enabled through parameter group configuration | 3. Transport Layer Encryption | Require secure protocols (e.g., TLS) for all data in transit to prevent interception or tampering. |
| rds-clusterinstance-ssl-encryption | Ensures RDS cluster instances have SSL/TLS encryption enabled through parameter group configuration | 3. Transport Layer Encryption | Require secure protocols (e.g., TLS) for all data in transit to prevent interception or tampering. |
| rds-ssl-encryption | Ensures RDS instances have SSL/TLS encryption enabled | 3. Transport Layer Encryption | Require secure protocols (e.g., TLS) for all data in transit to prevent interception or tampering. |
| api-gateway-ssl-certificate-required | Ensures API Gateway REST API stages have client certificates configured for SSL/TLS authentication to protect data in transit. | 3. Transport Layer Encryption | Require secure protocols (e.g., TLS) for all data in transit to prevent interception or tampering. |
| elb-disallow-unencrypted-traffic | Check that ELB Load Balancers do not allow unencrypted (HTTP) traffic. | 3. Transport Layer Encryption | Require secure protocols (e.g., TLS) for all data in transit to prevent interception or tampering. |
| rds-cluster-instance-disallow-public-access | Checks that RDS Cluster Instances public access is not enabled. | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| neptune-clusterinstance-no-public-access | Checks that Neptune Cluster Instances public access is not enabled. | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| rds-private-subnet-validation | Validates that RDS DB subnet groups contain only private subnets | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| s3-bucket-public-access-block | Ensures each S3 bucket has a public access block with all settings enabled | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| ec2-instance-disallow-public-ip | Checks that EC2 instances do not have a public IP address. | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| dms-no-public-access | Ensures DMS replication instances are not publicly accessible to maintain security. | 4. No Public Access | Prohibit direct public exposure of resources unless explicitly approved and required. |
| environment-separation-tagging | Ensures that resources are tagged to distinguish between production and non-production environments | 5. Tagging | Enforce standardized resource tags for ownership, environment, and compliance tracking. |
| resource-tagging | Ensures all AWS resources must include tags for proper change tracking | 5. Tagging | Enforce standardized resource tags for ownership, environment, and compliance tracking. |
| vpc-flow-logs | Ensures VPC flow logs use approved destinations for centralized monitoring | 6. Enforce Logging | Enable and retain audit logs for all security-relevant actions and events. |
| api-gateway-access-logging | Ensures API Gateway stages have access logging enabled | 6. Enforce Logging | Enable and retain audit logs for all security-relevant actions and events. |
| api-gateway-v2-access-logging | Ensures API Gateway V2 stages have access logging enabled | 6. Enforce Logging | Enable and retain audit logs for all security-relevant actions and events. |
| s3-bucket-access-logging | Ensures each S3 bucket has access logging enabled | 6. Enforce Logging | Enable and retain audit logs for all security-relevant actions and events. |
| elb-access-logging-enabled | Check that ELB Load Balancers uses access logging. | 6. Enforce Logging | Enable and retain audit logs for all security-relevant actions and events. |
| cloudtrail-enabled | Ensures CloudTrail is enabled with at least one active trail for audit logging. | 6. Enforce Logging | Enable and retain audit logs for all security-relevant actions and events. |
| cloudwatch-log-retention | Ensures CloudWatch log groups have appropriate retention periods for compliance. | 6. Enforce Logging | Enable and retain audit logs for all security-relevant actions and events. |
| rds-instance-high-availability | Ensures RDS instances have Multi-AZ deployment enabled for high availability | 7. High Availability | Deploy resources in redundant, fault-tolerant configurations to ensure service continuity. |
| elb-cross-zone-load-balancing-enabled | Classic Load Balancers must have cross-zone load balancing enabled | 7. High Availability | Deploy resources in redundant, fault-tolerant configurations to ensure service continuity. |
| sqs-dead-letter-queue | Ensures SQS queues have dead letter queue configuration | 8. Require DLQ | Ensure all asynchronous messaging systems are configured with a dead-letter queue to handle failures. |
| lambda-dead-letter-queue-required | Lambda functions must have dead letter queues configured for error handling and incident response | 8. Require DLQ | Ensure all asynchronous messaging systems are configured with a dead-letter queue to handle failures. |
| limit-lambda-execution-time | Ensures that AWS Lambda functions are configured to time out after a specified duration to prevent extended access | 9. Resource Availability | Define and enforce timeouts, quotas, and capacity limits to prevent resource exhaustion. |
| dynamodb-streams-enabled | Enforces that all DynamoDB tables have Stream settings enabled to capture all changes | 9. Resource Availability | Define and enforce timeouts, quotas, and capacity limits to prevent resource exhaustion. |
| lambda-concurrent-execution-limits-required | Lambda functions must have concurrent execution limits configured to protect resource availability | 9. Resource Availability | Define and enforce timeouts, quotas, and capacity limits to prevent resource exhaustion. |
| dynamodb-auto-scaling-enabled | Ensures DynamoDB tables have auto-scaling or on-demand mode enabled for capacity management. | 9. Resource Availability | Define and enforce timeouts, quotas, and capacity limits to prevent resource exhaustion. |
