---
title_tag: "Compliance Ready Policies (Aws) | CrossGuard"
meta_desc: This page contains the list of Compliance Ready Policies for Aws.
title: Compliance Ready Aws Policies
h1: List of Compliance Ready Policies for Aws
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  usingpulumi:
    parent: crossguard-compliance-ready-policies
---
There's a total of 89 Compliance Ready Policies for the Aws provider.

All those policies are available in the `@pulumi/aws-compliance-policies` package.

Please refer to our [Documentation](../compliance-ready-policies/#manual-installation) for more details.

## alb

### Listener

#### aws-alb-listener-configure-secure-tls

Policy name: `aws-alb-listener-configure-secure-tls`

Code path: `aws.alb.Listener.configureSecureTls`

Checks that ALB Load Balancers uses secure/modern TLS encryption.

Service: Alb

Resource: Listener

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, network

Link: <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies>

#### aws-alb-listener-disallow-unencrypted-traffic

Policy name: `aws-alb-listener-disallow-unencrypted-traffic`

Code path: `aws.alb.Listener.disallowUnencryptedTraffic`

Check that ALB Load Balancers do not allow unencrypted (HTTP) traffic.

Service: Alb

Resource: Listener

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: iso27001, pcidss

Topics: network

Link: <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html>

### LoadBalancer

#### aws-alb-loadbalancer-configure-access-logging

Policy name: `aws-alb-loadbalancer-configure-access-logging`

Code path: `aws.alb.LoadBalancer.configureAccessLogging`

Checks that ALB loadbalancers have access logging configured and enabled.

Service: Alb

Resource: LoadBalancer

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: logging, network

Link: <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html>

#### aws-alb-loadbalancer-enable-access-logging

Policy name: `aws-alb-loadbalancer-enable-access-logging`

Code path: `aws.alb.LoadBalancer.enableAccessLogging`

Checks that ALB loadbalancers have access logging enabled.

Service: Alb

Resource: LoadBalancer

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: logging, network

Link: <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html>

## apigateway

### DomainName

#### aws-apigateway-domainname-configure-security-policy

Policy name: `aws-apigateway-domainname-configure-security-policy`

Code path: `aws.apigateway.DomainName.configureSecurityPolicy`

Checks that ApiGateway Domain Name Security Policy uses secure/modern TLS encryption.

Service: Apigateway

Resource: DomainName

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, network

Link: <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html>

## apigatewayv2

### DomainName

#### aws-apigatewayv2-domainname-configure-domain-name-security-policy

Policy name: `aws-apigatewayv2-domainname-configure-domain-name-security-policy`

Code path: `aws.apigatewayv2.DomainName.configureDomainNameSecurityPolicy`

Checks that any ApiGatewayV2 Domain Name Security Policy uses secure/modern TLS encryption.

Service: Apigatewayv2

Resource: DomainName

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, network

Link: <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html>

#### aws-apigatewayv2-domainname-enable-domain-name-configuration

Policy name: `aws-apigatewayv2-domainname-enable-domain-name-configuration`

Code path: `aws.apigatewayv2.DomainName.enableDomainNameConfiguration`

Checks that any ApiGatewayV2 Domain Name Configuration is enabled.

Service: Apigatewayv2

Resource: DomainName

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: none

Topics: network

Link: <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html>

### Stage

#### aws-apigatewayv2-stage-configure-access-logging

Policy name: `aws-apigatewayv2-stage-configure-access-logging`

Code path: `aws.apigatewayv2.Stage.configureAccessLogging`

Checks that any ApiGatewayV2 Stages have access logging configured.

Service: Apigatewayv2

Resource: Stage

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: logging, network

Link: <https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html>

#### aws-apigatewayv2-stage-enable-access-logging

Policy name: `aws-apigatewayv2-stage-enable-access-logging`

Code path: `aws.apigatewayv2.Stage.enableAccessLogging`

Checks that any ApiGatewayV2 Stages have access logging enabled.

Service: Apigatewayv2

Resource: Stage

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: logging, network

Link: <https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html>

## appflow

### ConnectorProfile

#### aws-appflow-connectorprofile-configure-customer-managed-key

Policy name: `aws-appflow-connectorprofile-configure-customer-managed-key`

Code path: `aws.appflow.ConnectorProfile.configureCustomerManagedKey`

Check that AppFlow ConnectorProfile uses a customer-managed KMS key.

Service: Appflow

Resource: ConnectorProfile

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/appflow/latest/userguide/data-protection.html#encryption-transit>

### Flow

#### aws-appflow-flow-configure-customer-managed-key

Policy name: `aws-appflow-flow-configure-customer-managed-key`

Code path: `aws.appflow.Flow.configureCustomerManagedKey`

Check that AppFlow Flow uses a customer-managed KMS key.

Service: Appflow

Resource: Flow

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/appflow/latest/userguide/data-protection.html#encryption-transit>

#### aws-appflow-flow-missing-description

Policy name: `aws-appflow-flow-missing-description`

Code path: `aws.appflow.Flow.missingDescription`

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

#### aws-athena-datacatalog-missing-description

Policy name: `aws-athena-datacatalog-missing-description`

Code path: `aws.athena.DataCatalog.missingDescription`

Checks that Athena DataCatalogs have a description.

Service: Athena

Resource: DataCatalog

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/athena/latest/ug/understanding-tables-databases-and-the-data-catalog.html>

### Database

#### aws-athena-database-configure-customer-managed-key

Policy name: `aws-athena-database-configure-customer-managed-key`

Code path: `aws.athena.Database.configureCustomerManagedKey`

Checks that Athena Databases storage uses a customer-managed-key.

Service: Athena

Resource: Database

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/athena/latest/ug/encryption.html>

#### aws-athena-database-disallow-unencrypted-database

Policy name: `aws-athena-database-disallow-unencrypted-database`

Code path: `aws.athena.Database.disallowUnencryptedDatabase`

Checks that Athena Databases storage is encrypted.

Service: Athena

Resource: Database

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/athena/latest/ug/encryption.html>

#### aws-athena-database-missing-description

Policy name: `aws-athena-database-missing-description`

Code path: `aws.athena.Database.missingDescription`

Checks that Athena Databases have a description.

Service: Athena

Resource: Database

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/athena/latest/ug/creating-databases.html>

### NamedQuery

#### aws-athena-namedquery-missing-description

Policy name: `aws-athena-namedquery-missing-description`

Code path: `aws.athena.NamedQuery.missingDescription`

Checks that Athena NamedQueries have a description.

Service: Athena

Resource: NamedQuery

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/athena/latest/ug/saved-queries.html>

### Workgroup

#### aws-athena-workgroup-configure-customer-managed-key

Policy name: `aws-athena-workgroup-configure-customer-managed-key`

Code path: `aws.athena.Workgroup.configureCustomerManagedKey`

Checks that Athena Workgroups use a customer-managed-key.

Service: Athena

Resource: Workgroup

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/athena/latest/ug/workgroups-procedure.html>

#### aws-athena-workgroup-disallow-unencrypted-workgroup

Policy name: `aws-athena-workgroup-disallow-unencrypted-workgroup`

Code path: `aws.athena.Workgroup.disallowUnencryptedWorkgroup`

Checks that Athena Workgroups are encrypted.

Service: Athena

Resource: Workgroup

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/athena/latest/ug/workgroups-procedure.html>

#### aws-athena-workgroup-enforce-configuration

Policy name: `aws-athena-workgroup-enforce-configuration`

Code path: `aws.athena.Workgroup.enforceConfiguration`

Checks that Athena Workgroups enforce their configuration to their clients.

Service: Athena

Resource: Workgroup

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/athena/latest/ug/workgroups-procedure.html>

#### aws-athena-workgroup-missing-description

Policy name: `aws-athena-workgroup-missing-description`

Code path: `aws.athena.Workgroup.missingDescription`

Checks that Athena Workgroups have a description.

Service: Athena

Resource: Workgroup

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/athena/latest/ug/workgroups-procedure.html>

## cloudfront

### Distribution

#### aws-cloudfront-distribution-configure-access-logging

Policy name: `aws-cloudfront-distribution-configure-access-logging`

Code path: `aws.cloudfront.Distribution.configureAccessLogging`

Checks that any CloudFront distributions have access logging configured.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: logging, network

Link: <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html>

#### aws-cloudfront-distribution-configure-secure-tls

Policy name: `aws-cloudfront-distribution-configure-secure-tls`

Code path: `aws.cloudfront.Distribution.configureSecureTls`

Checks that CloudFront distributions uses secure/modern TLS encryption.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, network

Link: <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html>

#### aws-cloudfront-distribution-configure-secure-tls-to-origin

Policy name: `aws-cloudfront-distribution-configure-secure-tls-to-origin`

Code path: `aws.cloudfront.Distribution.configureSecureTlsToOrigin`

Checks that CloudFront distributions communicate with custom origins using TLS 1.2 encryption only.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, network

Link: <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-s3-origin.html>

#### aws-cloudfront-distribution-configure-waf

Policy name: `aws-cloudfront-distribution-configure-waf`

Code path: `aws.cloudfront.Distribution.configureWaf`

Checks that any CloudFront distribution has a WAF ACL associated.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: network

Link: <https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-features.html>

#### aws-cloudfront-distribution-disallow-unencrypted-traffic

Policy name: `aws-cloudfront-distribution-disallow-unencrypted-traffic`

Code path: `aws.cloudfront.Distribution.disallowUnencryptedTraffic`

Checks that CloudFront distributions only allow encypted ingress traffic.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: iso27001, pcidss

Topics: network

Link: <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>

#### aws-cloudfront-distribution-enable-access-logging

Policy name: `aws-cloudfront-distribution-enable-access-logging`

Code path: `aws.cloudfront.Distribution.enableAccessLogging`

Checks that any CloudFront distributions have access logging enabled.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: logging, network

Link: <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html>

#### aws-cloudfront-distribution-enable-tls-to-origin

Policy name: `aws-cloudfront-distribution-enable-tls-to-origin`

Code path: `aws.cloudfront.Distribution.enableTlsToOrigin`

Checks that CloudFront distributions communicate with custom origins using TLS encryption.

Service: Cloudfront

Resource: Distribution

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: iso27001, pcidss

Topics: encryption, network

Link: <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-s3-origin.html>

## ebs

### Volume

#### aws-ebs-volume-configure-customer-managed-key

Policy name: `aws-ebs-volume-configure-customer-managed-key`

Code path: `aws.ebs.Volume.configureCustomerManagedKey`

Check that encrypted EBS volumes use a customer-managed KMS key.

Service: Ebs

Resource: Volume

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>

#### aws-ebs-volume-disallow-unencrypted-volume

Policy name: `aws-ebs-volume-disallow-unencrypted-volume`

Code path: `aws.ebs.Volume.disallowUnencryptedVolume`

Checks that EBS volumes are encrypted.

Service: Ebs

Resource: Volume

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>

## ec2

### Instance

#### aws-ec2-instance-disallow-public-ip

Policy name: `aws-ec2-instance-disallow-public-ip`

Code path: `aws.ec2.Instance.disallowPublicIp`

Checks that EC2 instances do not have a public IP address.

Service: Ec2

Resource: Instance

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: network

#### aws-ec2-instance-disallow-unencrypted-block-device

Policy name: `aws-ec2-instance-disallow-unencrypted-block-device`

Code path: `aws.ec2.Instance.disallowUnencryptedBlockDevice`

Checks that EC2 instances do not have unencrypted block devices.

Service: Ec2

Resource: Instance

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>

#### aws-ec2-instance-disallow-unencrypted-root-block-device

Policy name: `aws-ec2-instance-disallow-unencrypted-root-block-device`

Code path: `aws.ec2.Instance.disallowUnencryptedRootBlockDevice`

Checks that EC2 instances does not have unencrypted root volumes.

Service: Ec2

Resource: Instance

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/RootDeviceStorage.html>

### LaunchConfiguration

#### aws-ec2-launchconfiguration-disallow-public-ip

Policy name: `aws-ec2-launchconfiguration-disallow-public-ip`

Code path: `aws.ec2.LaunchConfiguration.disallowPublicIp`

Checks that EC2 Launch Configurations do not have a public IP address.

Service: Ec2

Resource: LaunchConfiguration

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: network

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html>

#### aws-ec2-launchconfiguration-disallow-unencrypted-block-device

Policy name: `aws-ec2-launchconfiguration-disallow-unencrypted-block-device`

Code path: `aws.ec2.LaunchConfiguration.disallowUnencryptedBlockDevice`

Checks that EC2 Launch Configurations do not have unencrypted block devices.

Service: Ec2

Resource: LaunchConfiguration

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>

#### aws-ec2-launchconfiguration-disallow-unencrypted-root-block-device

Policy name: `aws-ec2-launchconfiguration-disallow-unencrypted-root-block-device`

Code path: `aws.ec2.LaunchConfiguration.disallowUnencryptedRootBlockDevice`

Checks that EC2 launch configuration do not have unencrypted root block device.

Service: Ec2

Resource: LaunchConfiguration

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/RootDeviceStorage.html>

### LaunchTemplate

#### aws-ec2-launchtemplate-configure-customer-managed-key

Policy name: `aws-ec2-launchtemplate-configure-customer-managed-key`

Code path: `aws.ec2.LaunchTemplate.configureCustomerManagedKey`

Check that encrypted EBS volume uses a customer-managed KMS key.

Service: Ec2

Resource: LaunchTemplate

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>

#### aws-ec2-launchtemplate-disallow-public-ip

Policy name: `aws-ec2-launchtemplate-disallow-public-ip`

Code path: `aws.ec2.LaunchTemplate.disallowPublicIp`

Checks that EC2 Launch Templates do not have public IP addresses.

Service: Ec2

Resource: LaunchTemplate

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: network

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html>

#### aws-ec2-launchtemplate-disallow-unencrypted-block-device

Policy name: `aws-ec2-launchtemplate-disallow-unencrypted-block-device`

Code path: `aws.ec2.LaunchTemplate.disallowUnencryptedBlockDevice`

Checks that EC2 Launch Templates do not have unencrypted block device.

Service: Ec2

Resource: LaunchTemplate

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>

### SecurityGroup

#### aws-ec2-securitygroup-disallow-inbound-http-traffic

Policy name: `aws-ec2-securitygroup-disallow-inbound-http-traffic`

Code path: `aws.ec2.SecurityGroup.disallowInboundHttpTraffic`

Check that EC2 Security Groups do not allow inbound HTTP traffic.

Service: Ec2

Resource: SecurityGroup

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: iso27001, pcidss

Topics: encryption, network

Link: <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>

#### aws-ec2-securitygroup-disallow-public-internet-ingress

Policy name: `aws-ec2-securitygroup-disallow-public-internet-ingress`

Code path: `aws.ec2.SecurityGroup.disallowPublicInternetIngress`

Check that EC2 Security Groups do not allow ingress traffic from the Internet.

Service: Ec2

Resource: SecurityGroup

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: none

Topics: network

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html>

#### aws-ec2-securitygroup-missing-description

Policy name: `aws-ec2-securitygroup-missing-description`

Code path: `aws.ec2.SecurityGroup.missingDescription`

Checks that all security groups have a description.

Service: Ec2

Resource: SecurityGroup

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html>

#### aws-ec2-securitygroup-missing-egress-rule-description

Policy name: `aws-ec2-securitygroup-missing-egress-rule-description`

Code path: `aws.ec2.SecurityGroup.missingEgressRuleDescription`

Checks that all Egress Security Groups rules have a description.

Service: Ec2

Resource: SecurityGroup

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html>

#### aws-ec2-securitygroup-missing-ingress-rule-description

Policy name: `aws-ec2-securitygroup-missing-ingress-rule-description`

Code path: `aws.ec2.SecurityGroup.missingIngressRuleDescription`

Checks that all Ingress Security Groups rules have a description.

Service: Ec2

Resource: SecurityGroup

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html>

## ecr

### Repository

#### aws-ecr-repository-configure-customer-managed-key

Policy name: `aws-ecr-repository-configure-customer-managed-key`

Code path: `aws.ecr.Repository.configureCustomerManagedKey`

Checks that ECR repositories use a customer-managed KMS key.

Service: Ecr

Resource: Repository

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: iso27001, pcidss

Topics: container, encryption, storage

Link: <https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html>

#### aws-ecr-repository-configure-image-scan

Policy name: `aws-ecr-repository-configure-image-scan`

Code path: `aws.ecr.Repository.configureImageScan`

Checks that ECR repositories have 'scan-on-push' configured.

Service: Ecr

Resource: Repository

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss, soc2

Topics: container, vulnerability

Link: <https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html>

#### aws-ecr-repository-disallow-mutable-image

Policy name: `aws-ecr-repository-disallow-mutable-image`

Code path: `aws.ecr.Repository.disallowMutableImage`

Checks that ECR Repositories have immutable images enabled.

Service: Ecr

Resource: Repository

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: container

Link: <https://sysdig.com/blog/toctou-tag-mutability/>

#### aws-ecr-repository-disallow-unencrypted-repository

Policy name: `aws-ecr-repository-disallow-unencrypted-repository`

Code path: `aws.ecr.Repository.disallowUnencryptedRepository`

Checks that ECR Repositories are encrypted.

Service: Ecr

Resource: Repository

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: container, encryption, storage

Link: <https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html>

#### aws-ecr-repository-enable-image-scan

Policy name: `aws-ecr-repository-enable-image-scan`

Code path: `aws.ecr.Repository.enableImageScan`

Checks that ECR repositories have 'scan-on-push' enabled.

Service: Ecr

Resource: Repository

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss, soc2

Topics: container, vulnerability

Link: <https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html>

## efs

### FileSystem

#### aws-efs-filesystem-configure-customer-managed-key

Policy name: `aws-efs-filesystem-configure-customer-managed-key`

Code path: `aws.efs.FileSystem.configureCustomerManagedKey`

Check that encrypted EFS File system uses a customer-managed KMS key.

Service: Efs

Resource: FileSystem

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>

#### aws-efs-filesystem-disallow-single-availability-zone

Policy name: `aws-efs-filesystem-disallow-single-availability-zone`

Code path: `aws.efs.FileSystem.disallowSingleAvailabilityZone`

Check that EFS File system doesn't use single availability zone.

Service: Efs

Resource: FileSystem

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: none

Topics: availability, storage

Link: <https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html>

#### aws-efs-filesystem-disallow-unencrypted-file-system

Policy name: `aws-efs-filesystem-disallow-unencrypted-file-system`

Code path: `aws.efs.FileSystem.disallowUnencryptedFileSystem`

Checks that EFS File Systems do not have an unencrypted file system.

Service: Efs

Resource: FileSystem

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/efs/latest/ug/encryption-at-rest.html>

## eks

### Cluster

#### aws-eks-cluster-disallow-api-endpoint-public-access

Policy name: `aws-eks-cluster-disallow-api-endpoint-public-access`

Code path: `aws.eks.Cluster.disallowApiEndpointPublicAccess`

Check that EKS Clusters API Endpoint are not publicly accessible.

Service: Eks

Resource: Cluster

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: iso27001, pcidss

Topics: network

Link: <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>

#### aws-eks-cluster-enable-cluster-encryption-config

Policy name: `aws-eks-cluster-enable-cluster-encryption-config`

Code path: `aws.eks.Cluster.enableClusterEncryptionConfig`

Check that EKS Cluster Encryption Config is enabled.

Service: Eks

Resource: Cluster

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, kubernetes

Link: <https://aws.amazon.com/blogs/containers/using-eks-encryption-provider-support-for-defense-in-depth/>

## elb

### LoadBalancer

#### aws-elb-loadbalancer-configure-access-logging

Policy name: `aws-elb-loadbalancer-configure-access-logging`

Code path: `aws.elb.LoadBalancer.configureAccessLogging`

Check that ELB Load Balancers uses access logging.

Service: Elb

Resource: LoadBalancer

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: logging, network

#### aws-elb-loadbalancer-configure-multi-availability-zone

Policy name: `aws-elb-loadbalancer-configure-multi-availability-zone`

Code path: `aws.elb.LoadBalancer.configureMultiAvailabilityZone`

Check that ELB Load Balancers uses more than one availability zone.

Service: Elb

Resource: LoadBalancer

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: none

Topics: availability, network

Link: <https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-az.html>

#### aws-elb-loadbalancer-disallow-unencrypted-traffic

Policy name: `aws-elb-loadbalancer-disallow-unencrypted-traffic`

Code path: `aws.elb.LoadBalancer.disallowUnencryptedTraffic`

Check that ELB Load Balancers do not allow unencrypted (HTTP) traffic.

Service: Elb

Resource: LoadBalancer

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: iso27001, pcidss

Topics: network

Link: <https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-https-load-balancers.html>

#### aws-elb-loadbalancer-enable-health-check

Policy name: `aws-elb-loadbalancer-enable-health-check`

Code path: `aws.elb.LoadBalancer.enableHealthCheck`

Check that ELB Load Balancers have a health check enabled.

Service: Elb

Resource: LoadBalancer

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: none

Topics: availability, network

Link: <https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html>

## kms

### Key

#### aws-kms-key-disallow-bypass-policy-lockout-safety-check

Policy name: `aws-kms-key-disallow-bypass-policy-lockout-safety-check`

Code path: `aws.kms.Key.disallowBypassPolicyLockoutSafetyCheck`

Checks that KMS Keys do not bypass the key policy lockout safety check.

Service: Kms

Resource: Key

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: none

Topics: encryption

Link: <https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-bypass-policy-lockout-safety-check>

#### aws-kms-key-enable-key-rotation

Policy name: `aws-kms-key-enable-key-rotation`

Code path: `aws.kms.Key.enableKeyRotation`

Checks that KMS Keys have key rotation enabled.

Service: Kms

Resource: Key

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: encryption

Link: <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>

#### aws-kms-key-missing-description

Policy name: `aws-kms-key-missing-description`

Code path: `aws.kms.Key.missingDescription`

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

#### aws-lambda-function-configure-tracing-config

Policy name: `aws-lambda-function-configure-tracing-config`

Code path: `aws.lambda.Function.configureTracingConfig`

Checks that Lambda functions have tracing configured.

Service: Lambda

Resource: Function

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: logging, performance

Link: <https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html>

#### aws-lambda-function-enable-tracing-config

Policy name: `aws-lambda-function-enable-tracing-config`

Code path: `aws.lambda.Function.enableTracingConfig`

Checks that Lambda functions have tracing enabled.

Service: Lambda

Resource: Function

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: logging, performance

Link: <https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html>

#### aws-lambda-function-missing-description

Policy name: `aws-lambda-function-missing-description`

Code path: `aws.lambda.Function.missingDescription`

Checks that all Lambda Functions have a description.

Service: Lambda

Resource: Function

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html>

### Permission

#### aws-lambda-permission-configure-source-arn

Policy name: `aws-lambda-permission-configure-source-arn`

Code path: `aws.lambda.Permission.configureSourceArn`

Checks that lambda function permissions have a source arn specified.

Service: Lambda

Resource: Permission

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: iso27001, pcidss

Topics: permissions, security

Link: <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html>

## rds

### Cluster

#### aws-rds-cluster-configure-backup-retention

Policy name: `aws-rds-cluster-configure-backup-retention`

Code path: `aws.rds.Cluster.configureBackupRetention`

Checks that RDS Cluster backup retention policy is configured.

Service: Rds

Resource: Cluster

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: backup, resilience

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupRetention>

#### aws-rds-cluster-configure-customer-managed-key

Policy name: `aws-rds-cluster-configure-customer-managed-key`

Code path: `aws.rds.Cluster.configureCustomerManagedKey`

Checks that RDS Clusters storage uses a customer-managed KMS key.

Service: Rds

Resource: Cluster

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

#### aws-rds-cluster-disallow-single-availability-zone

Policy name: `aws-rds-cluster-disallow-single-availability-zone`

Code path: `aws.rds.Cluster.disallowSingleAvailabilityZone`

Check that RDS Cluster doesn't use single availability zone.

Service: Rds

Resource: Cluster

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: none

Topics: availability

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html>

#### aws-rds-cluster-disallow-unencrypted-storage

Policy name: `aws-rds-cluster-disallow-unencrypted-storage`

Code path: `aws.rds.Cluster.disallowUnencryptedStorage`

Checks that RDS Clusters storage is encrypted.

Service: Rds

Resource: Cluster

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

#### aws-rds-cluster-enable-backup-retention

Policy name: `aws-rds-cluster-enable-backup-retention`

Code path: `aws.rds.Cluster.enableBackupRetention`

Checks that RDS Clusters backup retention policy is enabled.

Service: Rds

Resource: Cluster

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: backup, resilience

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupRetention>

### ClusterInstance

#### aws-rds-clusterinstance-disallow-public-access

Policy name: `aws-rds-clusterinstance-disallow-public-access`

Code path: `aws.rds.ClusterInstance.disallowPublicAccess`

Checks that RDS Cluster Instances public access is not enabled.

Service: Rds

Resource: ClusterInstance

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: iso27001, pcidss

Topics: network

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.Connect.html>

#### aws-rds-clusterinstance-disallow-unencrypted-performance-insights

Policy name: `aws-rds-clusterinstance-disallow-unencrypted-performance-insights`

Code path: `aws.rds.ClusterInstance.disallowUnencryptedPerformanceInsights`

Checks that RDS Cluster Instances performance insights is encrypted.

Service: Rds

Resource: ClusterInstance

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: none

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

#### aws-rds-clusterinstance-enable-performance-insights

Policy name: `aws-rds-clusterinstance-enable-performance-insights`

Code path: `aws.rds.ClusterInstance.enablePerformanceInsights`

Checks that RDS Cluster Instances have performance insights enabled.

Service: Rds

Resource: ClusterInstance

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: logging, performance

Link: <https://aws.amazon.com/rds/performance-insights/>

### Instance

#### aws-rds-instance-configure-backup-retention

Policy name: `aws-rds-instance-configure-backup-retention`

Code path: `aws.rds.Instance.configureBackupRetention`

Checks that backup retention policy is adequate.

Service: Rds

Resource: Instance

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: backup, resilience

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupRetention>

#### aws-rds-instance-configure-customer-managed-key

Policy name: `aws-rds-instance-configure-customer-managed-key`

Code path: `aws.rds.Instance.configureCustomerManagedKey`

Checks that RDS Instance storage uses a customer-managed KMS key.

Service: Rds

Resource: Instance

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

#### aws-rds-instance-disallow-public-access

Policy name: `aws-rds-instance-disallow-public-access`

Code path: `aws.rds.Instance.disallowPublicAccess`

Checks that RDS Instance public access is not enabled.

Service: Rds

Resource: Instance

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: iso27001, pcidss

Topics: network

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.Connect.html>

#### aws-rds-instance-disallow-unencrypted-performance-insights

Policy name: `aws-rds-instance-disallow-unencrypted-performance-insights`

Code path: `aws.rds.Instance.disallowUnencryptedPerformanceInsights`

Checks that RDS Instance performance insights is encrypted.

Service: Rds

Resource: Instance

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: none

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.htm>

#### aws-rds-instance-disallow-unencrypted-storage

Policy name: `aws-rds-instance-disallow-unencrypted-storage`

Code path: `aws.rds.Instance.disallowUnencryptedStorage`

Checks that RDS instance storage is encrypted.

Service: Rds

Resource: Instance

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

#### aws-rds-instance-enable-backup-retention

Policy name: `aws-rds-instance-enable-backup-retention`

Code path: `aws.rds.Instance.enableBackupRetention`

Checks that RDS Instances backup retention policy is enabled.

Service: Rds

Resource: Instance

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: backup, resilience

Link: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupRetention>

#### aws-rds-instance-enable-performance-insights

Policy name: `aws-rds-instance-enable-performance-insights`

Code path: `aws.rds.Instance.enablePerformanceInsights`

Checks that RDS instances have performance insights enabled.

Service: Rds

Resource: Instance

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: logging, performance

Link: <https://aws.amazon.com/rds/performance-insights/>

## s3

### Bucket

#### aws-s3-bucket-configure-replication-configuration

Policy name: `aws-s3-bucket-configure-replication-configuration`

Code path: `aws.s3.Bucket.configureReplicationConfiguration`

Checks that S3 Bucket have cross-region replication configured.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: availability

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html>

#### aws-s3-bucket-configure-server-side-encryption-customer-managed-key

Policy name: `aws-s3-bucket-configure-server-side-encryption-customer-managed-key`

Code path: `aws.s3.Bucket.configureServerSideEncryptionCustomerManagedKey`

Check that S3 Buckets Server-Side Encryption (SSE) is using a customer-managed KMS Key.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-kms-encryption.html>

#### aws-s3-bucket-configure-server-side-encryption-kms

Policy name: `aws-s3-bucket-configure-server-side-encryption-kms`

Code path: `aws.s3.Bucket.configureServerSideEncryptionKms`

Check that S3 Buckets Server-Side Encryption (SSE) uses AWS KMS.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html>

#### aws-s3-bucket-disallow-public-read

Policy name: `aws-s3-bucket-disallow-public-read`

Code path: `aws.s3.Bucket.disallowPublicRead`

Checks that S3 Bucket ACLs don't allow 'public-read' or 'public-read-write' or 'authenticated-read'.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #E4A5A5;'>critical</span>

Frameworks: cis, iso27001, pcidss

Topics: security, storage

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html>

#### aws-s3-bucket-enable-replication-configuration

Policy name: `aws-s3-bucket-enable-replication-configuration`

Code path: `aws.s3.Bucket.enableReplicationConfiguration`

Checks that S3 Bucket have cross-region replication enabled.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: availability

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html>

#### aws-s3-bucket-enable-server-side-encryption

Policy name: `aws-s3-bucket-enable-server-side-encryption`

Code path: `aws.s3.Bucket.enableServerSideEncryption`

Check that S3 Bucket Server-Side Encryption (SSE) is enabled.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html>

#### aws-s3-bucket-enable-server-side-encryption-bucket-key

Policy name: `aws-s3-bucket-enable-server-side-encryption-bucket-key`

Code path: `aws.s3.Bucket.enableServerSideEncryptionBucketKey`

Check that S3 Buckets Server-Side Encryption (SSE) is using a Bucket key.

Service: S3

Resource: Bucket

Associated metadata for this policy:

Severity: <span style='background-color: #F9F88A;'>medium</span>

Frameworks: iso27001, pcidss

Topics: cost, encryption, storage

Link: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html>

## secretsmanager

### Secret

#### aws-secretsmanager-secret-configure-customer-managed-key

Policy name: `aws-secretsmanager-secret-configure-customer-managed-key`

Code path: `aws.secretsmanager.Secret.configureCustomerManagedKey`

Check that Secrets Manager Secrets use a customer-manager KMS key.

Service: Secretsmanager

Resource: Secret

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: iso27001, pcidss

Topics: encryption

Link: <https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html>

#### aws-secretsmanager-secret-missing-description

Policy name: `aws-secretsmanager-secret-missing-description`

Code path: `aws.secretsmanager.Secret.missingDescription`

Checks that Secrets Manager Secrets have a description.

Service: Secretsmanager

Resource: Secret

Associated metadata for this policy:

Severity: <span style='background-color: #B7E4C7;'>low</span>

Frameworks: none

Topics: documentation

Link: <https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html>
