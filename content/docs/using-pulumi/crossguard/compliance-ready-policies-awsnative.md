---
title_tag: "Compliance Ready Policies (Awsnative) | CrossGuard"
meta_desc: This page contains the list of Compliance Ready Policies for Awsnative.
title: Compliance Ready Awsnative Policies
h1: List of Compliance Ready Policies for Awsnative
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  usingpulumi:
    parent: crossguard-compliance-ready-policies
---
There's a total of 54 Compliance Ready Policies for the Awsnative provider.

All those policies are available in the `@pulumi/aws-compliance-policies` package.

Please refer to our [Documentation](../compliance-ready-policies/#manual-installation) for more details.

## apigateway

### DomainName

#### awsnative-apigateway-domainname-configure-security-policy

Policy name: `awsnative-apigateway-domainname-configure-security-policy`

Code path: `awsnative.apigateway.DomainName.configureSecurityPolicy`

Checks that ApiGateway Domain Name Security Policy uses secure/modern TLS encryption.

Service: Apigateway

Resource: DomainName

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, network

Link: <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html>

## appflow

### ConnectorProfile

#### awsnative-appflow-connectorprofile-configure-customer-managed-key

Policy name: `awsnative-appflow-connectorprofile-configure-customer-managed-key`

Code path: `awsnative.appflow.ConnectorProfile.configureCustomerManagedKey`

Check that AppFlow ConnectorProfile uses a customer-managed KMS key.

Service: Appflow

Resource: ConnectorProfile

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/appflow/latest/userguide/data-protection.html#encryption-transit>

### Flow

#### awsnative-appflow-flow-configure-customer-managed-key

Policy name: `awsnative-appflow-flow-configure-customer-managed-key`

Code path: `awsnative.appflow.Flow.configureCustomerManagedKey`

Check that AppFlow Flow uses a customer-managed KMS key.

Service: Appflow

Resource: Flow

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/appflow/latest/userguide/data-protection.html#encryption-transit>

#### awsnative-appflow-flow-missing-description

Policy name: `awsnative-appflow-flow-missing-description`

Code path: `awsnative.appflow.Flow.missingDescription`

Checks that AppFlow Flows have a description.

Service: Appflow

Resource: Flow

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/appflow/latest/userguide/create-flow-console.html>

## athena

### DataCatalog

#### awsnative-athena-datacatalog-missing-description

Policy name: `awsnative-athena-datacatalog-missing-description`

Code path: `awsnative.athena.DataCatalog.missingDescription`

Checks that Athena DataCatalogs have a description.

Service: Athena

Resource: DataCatalog

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/athena/latest/ug/understanding-tables-databases-and-the-data-catalog.html>

### NamedQuery

#### awsnative-athena-namedquery-missing-description

Policy name: `awsnative-athena-namedquery-missing-description`

Code path: `awsnative.athena.NamedQuery.missingDescription`

Checks that Athena NamedQueries have a description.

Service: Athena

Resource: NamedQuery

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/athena/latest/ug/saved-queries.html>

### WorkGroup

#### awsnative-athena-workgroup-configure-customer-managed-key

Policy name: `awsnative-athena-workgroup-configure-customer-managed-key`

Code path: `awsnative.athena.WorkGroup.configureCustomerManagedKey`

Checks that Athena Workgroups use a customer-managed-key.

Service: Athena

Resource: WorkGroup

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/athena/latest/ug/workgroups-procedure.html>

#### awsnative-athena-workgroup-disallow-unencrypted-workgroup

Policy name: `awsnative-athena-workgroup-disallow-unencrypted-workgroup`

Code path: `awsnative.athena.WorkGroup.disallowUnencryptedWorkgroup`

Checks that Athena Workgroups are encrypted.

Service: Athena

Resource: WorkGroup

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/athena/latest/ug/workgroups-procedure.html>

#### awsnative-athena-workgroup-enforce-configuration

Policy name: `awsnative-athena-workgroup-enforce-configuration`

Code path: `awsnative.athena.WorkGroup.enforceConfiguration`

Checks that Athena Workgroups enforce their configuration to their clients.

Service: Athena

Resource: WorkGroup

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/athena/latest/ug/workgroups-procedure.html>

#### awsnative-athena-workgroup-missing-description

Policy name: `awsnative-athena-workgroup-missing-description`

Code path: `awsnative.athena.WorkGroup.missingDescription`

Checks that Athena WorkGroups have a description.

Service: Athena

Resource: WorkGroup

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/athena/latest/ug/workgroups-procedure.html>

## cloudfront

### Distribution

#### awsnative-cloudfront-distribution-configure-access-logging

Policy name: `awsnative-cloudfront-distribution-configure-access-logging`

Code path: `awsnative.cloudfront.Distribution.configureAccessLogging`

Checks that any CloudFront distributions have access logging configured.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: hitrust, iso27001, pcidss

Topics: logging, network

Link: <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html>

#### awsnative-cloudfront-distribution-configure-secure-tls

Policy name: `awsnative-cloudfront-distribution-configure-secure-tls`

Code path: `awsnative.cloudfront.Distribution.configureSecureTls`

Checks that CloudFront distributions uses secure/modern TLS encryption.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, network

Link: <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html>

#### awsnative-cloudfront-distribution-configure-secure-tls-to-origin

Policy name: `awsnative-cloudfront-distribution-configure-secure-tls-to-origin`

Code path: `awsnative.cloudfront.Distribution.configureSecureTlsToOrigin`

Checks that CloudFront distributions communicate with custom origins using TLS 1.2 encryption only.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, network

Link: <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-s3-origin.html>

#### awsnative-cloudfront-distribution-configure-waf-acl

Policy name: `awsnative-cloudfront-distribution-configure-waf-acl`

Code path: `awsnative.cloudfront.Distribution.configureWafAcl`

Checks that CloudFront distributions have a WAF ACL associated.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: network

Link: <https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-features.html>

#### awsnative-cloudfront-distribution-disallow-unencrypted-traffic

Policy name: `awsnative-cloudfront-distribution-disallow-unencrypted-traffic`

Code path: `awsnative.cloudfront.Distribution.disallowUnencryptedTraffic`

Checks that CloudFront distributions only allow encypted ingress traffic.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: hitrust, iso27001, pcidss

Topics: network

Link: <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>

#### awsnative-cloudfront-distribution-enable-access-logging

Policy name: `awsnative-cloudfront-distribution-enable-access-logging`

Code path: `awsnative.cloudfront.Distribution.enableAccessLogging`

Checks that any CloudFront distributions have access logging enabled.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: hitrust, iso27001, pcidss

Topics: logging, network

Link: <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html>

#### awsnative-cloudfront-distribution-enable-tls-to-origin

Policy name: `awsnative-cloudfront-distribution-enable-tls-to-origin`

Code path: `awsnative.cloudfront.Distribution.enableTlsToOrigin`

Checks that CloudFront distributions communicate with custom origins using TLS encryption.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, network

Link: <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-s3-origin.html>

## ec2

### Volume

#### awsnative-ec2-volume-configure-customer-managed-key

Policy name: `awsnative-ec2-volume-configure-customer-managed-key`

Code path: `awsnative.ec2.Volume.configureCustomerManagedKey`

Check that encrypted EBS volumes use a customer-managed KMS key.

Service: Ec2

Resource: Volume

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>

#### awsnative-ec2-volume-disallow-unencrypted-volume

Policy name: `awsnative-ec2-volume-disallow-unencrypted-volume`

Code path: `awsnative.ec2.Volume.disallowUnencryptedVolume`

Checks that EBS volumes are encrypted.

Service: Ec2

Resource: Volume

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>

## ecr

### Repository

#### awsnative-ecr-repository-configure-customer-managed-key

Policy name: `awsnative-ecr-repository-configure-customer-managed-key`

Code path: `awsnative.ecr.Repository.configureCustomerManagedKey`

Checks that ECR repositories use a customer-managed KMS key.

Service: Ecr

Resource: Repository

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: hitrust, iso27001, pcidss

Topics: container, encryption, storage

Link: <https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html>

#### awsnative-ecr-repository-configure-image-scan

Policy name: `awsnative-ecr-repository-configure-image-scan`

Code path: `awsnative.ecr.Repository.configureImageScan`

Checks that ECR repositories have 'scan-on-push' configured.

Service: Ecr

Resource: Repository

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: container, vulnerability

Link: <https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html>

#### awsnative-ecr-repository-disallow-mutable-image

Policy name: `awsnative-ecr-repository-disallow-mutable-image`

Code path: `awsnative.ecr.Repository.disallowMutableImage`

Checks that ECR Repositories have immutable images enabled.

Service: Ecr

Resource: Repository

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: container

Link: <https://sysdig.com/blog/toctou-tag-mutability/>

#### awsnative-ecr-repository-disallow-unencrypted-repository

Policy name: `awsnative-ecr-repository-disallow-unencrypted-repository`

Code path: `awsnative.ecr.Repository.disallowUnencryptedRepository`

Checks that ECR Repositories are encrypted.

Service: Ecr

Resource: Repository

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: container, encryption, storage

Link: <https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html>

#### awsnative-ecr-repository-enable-image-scan

Policy name: `awsnative-ecr-repository-enable-image-scan`

Code path: `awsnative.ecr.Repository.enableImageScan`

Checks that ECR repositories have 'scan-on-push' enabled.

Service: Ecr

Resource: Repository

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: container, vulnerability

Link: <https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html>

## efs

### FileSystem

#### awsnative-efs-filesystem-configure-customer-managed-key

Policy name: `awsnative-efs-filesystem-configure-customer-managed-key`

Code path: `awsnative.efs.FileSystem.configureCustomerManagedKey`

Check that encrypted EFS File system uses a customer-managed KMS key.

Service: Efs

Resource: FileSystem

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>

#### awsnative-efs-filesystem-disallow-bypass-policy-lockout-safety-check

Policy name: `awsnative-efs-filesystem-disallow-bypass-policy-lockout-safety-check`

Code path: `awsnative.efs.FileSystem.disallowBypassPolicyLockoutSafetyCheck`

Checks that EFS File systems do not bypass the File System policy lockout safety check.

Service: Efs

Resource: FileSystem

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: none

Topics: encryption

Link: <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-bypasspolicylockoutsafetycheck>

#### awsnative-efs-filesystem-disallow-single-availability-zone

Policy name: `awsnative-efs-filesystem-disallow-single-availability-zone`

Code path: `awsnative.efs.FileSystem.disallowSingleAvailabilityZone`

Check that EFS File system doesn't use single availability zone.

Service: Efs

Resource: FileSystem

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: none

Topics: availability, storage

Link: <https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html>

#### awsnative-efs-filesystem-disallow-unencrypted-file-system

Policy name: `awsnative-efs-filesystem-disallow-unencrypted-file-system`

Code path: `awsnative.efs.FileSystem.disallowUnencryptedFileSystem`

Checks that EFS File Systems do not have an unencrypted file system.

Service: Efs

Resource: FileSystem

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/efs/latest/ug/encryption-at-rest.html>

## eks

### Cluster

#### awsnative-eks-cluster-disallow-api-endpoint-public-access

Policy name: `awsnative-eks-cluster-disallow-api-endpoint-public-access`

Code path: `awsnative.eks.Cluster.disallowApiEndpointPublicAccess`

Check that EKS Clusters API Endpoint are not publicly accessible.

Service: Eks

Resource: Cluster

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: hitrust, iso27001, pcidss

Topics: network

Link: <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>

#### awsnative-eks-cluster-enable-cluster-encryption-config

Policy name: `awsnative-eks-cluster-enable-cluster-encryption-config`

Code path: `awsnative.eks.Cluster.enableClusterEncryptionConfig`

Check that EKS Cluster Encryption Config is enabled.

Service: Eks

Resource: Cluster

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, kubernetes

Link: <https://aws.amazon.com/blogs/containers/using-eks-encryption-provider-support-for-defense-in-depth/>

## kms

### Key

#### awsnative-kms-key-enable-key-rotation

Policy name: `awsnative-kms-key-enable-key-rotation`

Code path: `awsnative.kms.Key.enableKeyRotation`

Checks that KMS Keys have key rotation enabled.

Service: Kms

Resource: Key

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption

Link: <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>

#### awsnative-kms-key-missing-description

Policy name: `awsnative-kms-key-missing-description`

Code path: `awsnative.kms.Key.missingDescription`

Checks that KMS Keys have a description.

Service: Kms

Resource: Key

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html>

## lambda

### Function

#### awsnative-lambda-function-configure-tracing-config

Policy name: `awsnative-lambda-function-configure-tracing-config`

Code path: `awsnative.lambda.Function.configureTracingConfig`

Checks that Lambda functions have tracing configured.

Service: Lambda

Resource: Function

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: logging, performance

Link: <https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html>

#### awsnative-lambda-function-enable-tracing-config

Policy name: `awsnative-lambda-function-enable-tracing-config`

Code path: `awsnative.lambda.Function.enableTracingConfig`

Checks that Lambda functions have tracing enabled.

Service: Lambda

Resource: Function

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: logging, performance

Link: <https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html>

#### awsnative-lambda-function-missing-description

Policy name: `awsnative-lambda-function-missing-description`

Code path: `awsnative.lambda.Function.missingDescription`

Checks that Lambda Functions have a description.

Service: Lambda

Resource: Function

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html>

## rds

### DbCluster

#### awsnative-rds-dbcluster-configure-backup-retention

Policy name: `awsnative-rds-dbcluster-configure-backup-retention`

Code path: `awsnative.rds.DbCluster.configureBackupRetention`

Checks that RDS DB Cluster backup retention policy is configured.

Service: Rds

Resource: DbCluster

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: hitrust, iso27001, pcidss

Topics: backup, resilience

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupRetention>

#### awsnative-rds-dbcluster-configure-customer-managed-key

Policy name: `awsnative-rds-dbcluster-configure-customer-managed-key`

Code path: `awsnative.rds.DbCluster.configureCustomerManagedKey`

Checks that RDS DB Cluster storage uses a customer-managed KMS key.

Service: Rds

Resource: DbCluster

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

#### awsnative-rds-dbcluster-disallow-single-availability-zone

Policy name: `awsnative-rds-dbcluster-disallow-single-availability-zone`

Code path: `awsnative.rds.DbCluster.disallowSingleAvailabilityZone`

Check that RDS DB Cluster doesn't use single availability zone.

Service: Rds

Resource: DbCluster

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust

Topics: availability

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>

#### awsnative-rds-dbcluster-disallow-unencrypted-storage

Policy name: `awsnative-rds-dbcluster-disallow-unencrypted-storage`

Code path: `awsnative.rds.DbCluster.disallowUnencryptedStorage`

Checks that RDS DB Cluster storage is encrypted.

Service: Rds

Resource: DbCluster

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

#### awsnative-rds-dbcluster-enable-backup-retention

Policy name: `awsnative-rds-dbcluster-enable-backup-retention`

Code path: `awsnative.rds.DbCluster.enableBackupRetention`

Checks that RDS DB Clusters backup retention policy is enabled.

Service: Rds

Resource: DbCluster

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: hitrust, iso27001, pcidss

Topics: backup, resilience

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupRetention>

### DbInstance

#### awsnative-rds-dbinstance-configure-backup-retention

Policy name: `awsnative-rds-dbinstance-configure-backup-retention`

Code path: `awsnative.rds.DbInstance.configureBackupRetention`

Checks that RDS DB Instances backup retention policy is adequate.

Service: Rds

Resource: DbInstance

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: backup, resilience

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupRetention>

#### awsnative-rds-dbinstance-configure-customer-managed-key

Policy name: `awsnative-rds-dbinstance-configure-customer-managed-key`

Code path: `awsnative.rds.DbInstance.configureCustomerManagedKey`

Checks that RDS DB Instance storage uses a customer-managed KMS key.

Service: Rds

Resource: DbInstance

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

#### awsnative-rds-dbinstance-disallow-public-access

Policy name: `awsnative-rds-dbinstance-disallow-public-access`

Code path: `awsnative.rds.DbInstance.disallowPublicAccess`

Checks that RDS DB Instances public access is not enabled.

Service: Rds

Resource: DbInstance

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: hitrust, iso27001, pcidss

Topics: network

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.Connect.html>

#### awsnative-rds-dbinstance-disallow-unencrypted-performance-insights

Policy name: `awsnative-rds-dbinstance-disallow-unencrypted-performance-insights`

Code path: `awsnative.rds.DbInstance.disallowUnencryptedPerformanceInsights`

Checks that RDS DB Instances performance insights is encrypted.

Service: Rds

Resource: DbInstance

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: none

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

#### awsnative-rds-dbinstance-disallow-unencrypted-storage

Policy name: `awsnative-rds-dbinstance-disallow-unencrypted-storage`

Code path: `awsnative.rds.DbInstance.disallowUnencryptedStorage`

Checks that RDS DB Instance storage is encrypted.

Service: Rds

Resource: DbInstance

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

#### awsnative-rds-dbinstance-enable-backup-retention

Policy name: `awsnative-rds-dbinstance-enable-backup-retention`

Code path: `awsnative.rds.DbInstance.enableBackupRetention`

Checks that RDS DB Instances backup retention policy is enabled.

Service: Rds

Resource: DbInstance

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: hitrust, iso27001, pcidss

Topics: backup, resilience

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupRetention>

#### awsnative-rds-dbinstance-enable-performance-insights

Policy name: `awsnative-rds-dbinstance-enable-performance-insights`

Code path: `awsnative.rds.DbInstance.enablePerformanceInsights`

Checks that RDS DB Instances have performance insights enabled.

Service: Rds

Resource: DbInstance

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: logging, performance

Link: <https://aws.amazon.com/rds/performance-insights/>

## s3

### Bucket

#### awsnative-s3-bucket-configure-replication-configuration

Policy name: `awsnative-s3-bucket-configure-replication-configuration`

Code path: `awsnative.s3.Bucket.configureReplicationConfiguration`

Checks that S3 Bucket have cross-region replication configured.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: availability

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html>

#### awsnative-s3-bucket-configure-server-side-encryption-customer-managed-key

Policy name: `awsnative-s3-bucket-configure-server-side-encryption-customer-managed-key`

Code path: `awsnative.s3.Bucket.configureServerSideEncryptionCustomerManagedKey`

Check that S3 Buckets Server-Side Encryption (SSE) is using a customer-managed KMS Key.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-kms-encryption.html>

#### awsnative-s3-bucket-configure-server-side-encryption-kms

Policy name: `awsnative-s3-bucket-configure-server-side-encryption-kms`

Code path: `awsnative.s3.Bucket.configureServerSideEncryptionKms`

Check that S3 Buckets Server-Side Encryption (SSE) uses AWS KMS.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html>

#### awsnative-s3-bucket-disallow-public-read

Policy name: `awsnative-s3-bucket-disallow-public-read`

Code path: `awsnative.s3.Bucket.disallowPublicRead`

Checks that S3 Bucket ACLs don't allow 'PublicRead', 'PublicReadWrite' or 'AuthenticatedRead'.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: cis, hitrust, iso27001, pcidss

Topics: security, storage

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html>

#### awsnative-s3-bucket-enable-replication-configuration

Policy name: `awsnative-s3-bucket-enable-replication-configuration`

Code path: `awsnative.s3.Bucket.enableReplicationConfiguration`

Checks that S3 Bucket have cross-region replication enabled.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: availability

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html>

#### awsnative-s3-bucket-enable-server-side-encryption

Policy name: `awsnative-s3-bucket-enable-server-side-encryption`

Code path: `awsnative.s3.Bucket.enableServerSideEncryption`

Check that S3 Bucket Server-Side Encryption (SSE) is enabled.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: hitrust, iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html>

#### awsnative-s3-bucket-enable-server-side-encryption-bucket-key

Policy name: `awsnative-s3-bucket-enable-server-side-encryption-bucket-key`

Code path: `awsnative.s3.Bucket.enableServerSideEncryptionBucketKey`

Check that S3 Buckets Server-Side Encryption (SSE) is using a Bucket key.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: cost, encryption, storage

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html>
