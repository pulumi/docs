---
title: AWS Index of Services
meta_desc: Pulumi Crosswalk for AWS supports all AWS services. This page provides a complete list of supported services.
menu:
  userguides:
    parent: crosswalk-aws
    weight: 11
aliases:
- /docs/reference/crosswalk/aws/other/
- /docs/guides/crosswalk/aws/other/
---

<a href="{{< relref "./" >}}">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

Pulumi Crosswalk for AWS supports all AWS services, not just those with dedicated articles in this User Guide.
This includes services like DynamoDB, EC2, S3, and RDS, to name a few, and includes support for all of their features.
If your favorite service isn't listed here, contact us by [filing an issue in the docs repo](
https://github.com/pulumi/docs) or by [joining the Pulumi Community Slack channel](https://slack.pulumi.com).

## Index of Services

Here is a complete list of services supported by Pulumi Crosswalk for AWS, with a user guide link where available.
The Pulumi API documentation includes a full list of classes, their properties, and typically one or more examples, for each
service.

<style>
table {
    margin-bottom: 20px;
    font-size: 14px;
}

td, th {
    padding: 8px 8px;
    text-align: left;
    border: 1px solid rgba(0,0,0,0.13);
}

thead tr th {
    background-color: #e0e0e0;
    font-weight: 800;
}

thead tr th:first-child {
    text-align: left;
}

tbody tr td:first-child {
    text-align: left;
}
</style>

| Service | Description | User Guide | API Docs |
|---------|-------------|------------|----------|
| [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) | Manage TLS/SSL certificates | | [acm]({{< relref "/registry/packages/aws/api-docs/acm" >}}) |
| [AWS Certificate Manager Private Certificate Authority](https://docs.aws.amazon.com/acm-pca/latest/userguide/PcaWelcome.html) | Managed private CA service | | [acmpca]({{< relref "/registry/packages/aws/api-docs/acmpca" >}}) |
| [Amazon API Gateway](https://aws.amazon.com/api-gateway/) | Secure, scalable APIs | [User Guide]({{< relref "api-gateway" >}}) | [apigateway]({{< relref "/registry/packages/aws/api-docs/apigateway" >}}) |
| [AWS App Mesh](https://aws.amazon.com/app-mesh/) | App-level service networking | | [appmesh]({{< relref "/registry/packages/aws/api-docs/appmesh" >}}) |
| [AWS AppSync](https://aws.amazon.com/app-mesh/) | Data-driven apps and APIs | | [appsync]({{< relref "/registry/packages/aws/api-docs/appsync" >}}) |
| [Amazon Athena](https://aws.amazon.com/athena/) | Serverless queries over S3 | | [athena]({{< relref "/registry/packages/aws/api-docs/athena" >}}) |
| [AWS Auto Scaling](https://aws.amazon.com/autoscaling) | Automatic scaling policies | [User Guide]({{< relref "autoscaling" >}}) | [autoscaling]({{< relref "/registry/packages/aws/api-docs/autoscaling" >}}) |
| [AWS Backup](https://aws.amazon.com/backup/) | Centrally managed backups | | [backup]({{< relref "/registry/packages/aws/api-docs/backup" >}}) |
| [AWS Batch](https://aws.amazon.com/batch/) | Easy and efficient batch computing | | [batch]({{< relref "/registry/packages/aws/api-docs/batch" >}}) |
| [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) | Custom budgets and alerting | | [budgets]({{< relref "/registry/packages/aws/api-docs/budgets" >}}) |
| [AWS Config](https://aws.amazon.com/config/) | Record and evaluate resource config | | [cfg]({{< relref "/registry/packages/aws/api-docs/cfg" >}}) |
| [AWS Cloud9](https://aws.amazon.com/cloud9/) | Cloud IDE | | [cloud9]({{< relref "/registry/packages/aws/api-docs/cloud9" >}}) |
| [AWS CloudFormation](https://aws.amazon.com/cloudformation/) | Provision resources in YAML/JSON | | [cloudformation]({{< relref "/registry/packages/aws/api-docs/cloudformation" >}}) |
| [Amazon CloudFront](https://aws.amazon.com/cloudfront/) | Fast and secure CDN | | [cloudfront]({{< relref "/registry/packages/aws/api-docs/cloudfront" >}}) |
| [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) | Managed hardware security module (HSM) | | [cloudhsmv2]({{< relref "/registry/packages/aws/api-docs/cloudhsmv2" >}}) |
| [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) | Track user activity and API usage | | [cloudtrail]({{< relref "/registry/packages/aws/api-docs/cloudtrail" >}}) |
| [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) | Application and infrastructure monitoring | [User Guide]({{< relref "cloudwatch" >}}) | [cloudwatch]({{< relref "/registry/packages/aws/api-docs/cloudwatch" >}}) |
| [AWS CodeBuild](https://aws.amazon.com/codebuild/) | Build and test code | [User Guide]({{< relref "/docs/guides/continuous-delivery/aws-code-services" >}}) | [codebuild]({{< relref "/registry/packages/aws/api-docs/codebuild" >}}) |
| [AWS CodeCommit](https://aws.amazon.com/codecommit/) | Host private Git repos | [User Guide]({{< relref "/docs/guides/continuous-delivery/aws-code-services" >}}) | [codecommit]({{< relref "/registry/packages/aws/api-docs/codecommit" >}}) |
| [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) | Automate code deployments | [User Guide]({{< relref "/docs/guides/continuous-delivery/aws-code-services" >}}) | [codedeploy]({{< relref "/registry/packages/aws/api-docs/codedeploy" >}}) |
| [AWS CodePipeline](https://aws.amazon.com/codepipeline) | Continuous delivery pipelines | [User Guide]({{< relref "/docs/guides/continuous-delivery/aws-code-services" >}}) | [codepipeline]({{< relref "/registry/packages/aws/api-docs/codepipeline" >}}) |
| [Amazon Cognito](https://aws.amazon.com/cognito/) | Simple and secure user identity | | [cognito]({{< relref "/registry/packages/aws/api-docs/cognito" >}}) |
| [AWS Cost and Usage Reporting](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) | Report on usage and cost | | [cur]({{< relref "/registry/packages/aws/api-docs/cur" >}}) |
| [AWS DataSync](https://aws.amazon.com/datasync/) | Easily transfer data | | [datasync]({{< relref "/registry/packages/aws/api-docs/datasync" >}}) |
| [Amazon DynamoDB Accelerator (DAX)](https://aws.amazon.com/dynamodb/dax/) | Fully managed, in memory cache | | [dax]({{< relref "/registry/packages/aws/api-docs/dax" >}}) |
| [AWS Device Farm](https://aws.amazon.com/device-farm/) | Test mobile apps | | [devicefarm]({{< relref "/registry/packages/aws/api-docs/devicefarm" >}}) |
| [AWS Direct Connect](https://aws.amazon.com/directconnect/) | Private, dedicated networks | | [directconnect]({{< relref "/registry/packages/aws/api-docs/directconnect" >}}) |
| [AWS Directory Service](https://aws.amazon.com/directoryservice/) | Managed Active Directory | | [directoryservice]({{< relref "/registry/packages/aws/api-docs/directoryservice" >}}) |
| [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/dlm) | Manage resource lifecycle | | [dlm]({{< relref "/registry/packages/aws/api-docs/dlm" >}}) |
| [Amazon Data Migration Service](https://aws.amazon.com/dms/) | Migrate databases to AWS | | [dms]({{< relref "/registry/packages/aws/api-docs/dms" >}}) |
| [Amazon DocumentDB](https://aws.amazon.com/documentdb/) | MongoDB-compatible document database | | [docdb]({{< relref "/registry/packages/aws/api-docs/docdb" >}}) |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) | Fast and flexible NoSQL database | | [dynamodb]({{< relref "/registry/packages/aws/api-docs/dynamodb" >}}) |
| [Amazon Elastic Block Store (EBS)](https://aws.amazon.com/ebs/) | Persistent block storage for EC2 | | [ebs]({{< relref "/registry/packages/aws/api-docs/ebs" >}}) |
| [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/) | Secure and resizable compute | | [ec2]({{< relref "/registry/packages/aws/api-docs/ec2" >}}) |
| [AWS VPN](https://aws.amazon.com/vpn/) | Extend on-prem networks to the cloud | | [ec2clientvpn]({{< relref "/registry/packages/aws/api-docs/ec2clientvpn" >}}) |
| [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) | Connect across VPCs | | [ec2transitgateway]({{< relref "/registry/packages/aws/api-docs/ec2transitgateway" >}}) |
| [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) | Private container registries | [User Guide]({{< relref "ecr" >}}) | [ecr]({{< relref "/registry/packages/aws/api-docs/ecr" >}}) |
| [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/) | Run containerized apps | [User Guide]({{< relref "ecs" >}}) | [ecs]({{< relref "/registry/packages/aws/api-docs/ecs" >}}) |
| [Amazon Elastic File System (EFS)](https://aws.amazon.com/efs/) | Scalable, elastic file system | | [efs]({{< relref "/registry/packages/aws/api-docs/efs" >}}) |
| [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) | Managed Kubernetes service | [User Guide]({{< relref "eks" >}}) | [eks]({{< relref "/registry/packages/aws/api-docs/eks" >}}) |
| [Amazon ElastiCache](https://aws.amazon.com/elasticache/) | Managed Redis or Memcached service | | [elasticache]({{< relref "/registry/packages/aws/api-docs/elasticache" >}}) |
| [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) | Deploy and scale web apps | | [elasticbeanstalk]({{< relref "/registry/packages/aws/api-docs/elasticbeanstalk" >}}) |
| [AWS Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/) | Scale across many instances | [User Guide]({{< relref "elb" >}}) | [lb]({{< relref "/registry/packages/aws/api-docs/lb" >}}) |
| [Amazon Elasticsearch Service](https://aws.amazon.com/elasticsearch-service/) | Fully managed Elasticsearch service | | [elasticsearch]({{< relref "/registry/packages/aws/api-docs/elasticsearch" >}}) |
| [Amazon Elastic Transcoder](https://aws.amazon.com/elastictranscoder/) | Media transcoding in the cloud | | [elastictranscoder]({{< relref "/registry/packages/aws/api-docs/elastictranscoder" >}}) |
| [Amazon EMR](https://aws.amazon.com/emr/) | Spark, Hadoop, HBase, and other big data | | [emr]({{< relref "/registry/packages/aws/api-docs/emr" >}}) |
| [Amazon GameLift](https://aws.amazon.com/gamelift/) | Game server hosting | | [gamelift]({{< relref "/registry/packages/aws/api-docs/gamelift" >}}) |
| [Amazon S3 Glacier](https://aws.amazon.com/glacier/) | Long term archived data storage | | [glacier]({{< relref "/registry/packages/aws/api-docs/glacier" >}}) |
| [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) | Improve global availability | | [globalaccelerator]({{< relref "/registry/packages/aws/api-docs/globalaccelerator" >}}) |
| [AWS Glue](https://aws.amazon.com/glue/) | Extract, transform, and load (ETL) | | [glue]({{< relref "/registry/packages/aws/api-docs/glue" >}}) |
| [Amazon GuardDuty](https://aws.amazon.com/guardduty/) | Protect your accounts and workloads | | [guardduty]({{< relref "/registry/packages/aws/api-docs/guardduty" >}}) |
| [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) | Securely manage access | [User Guide]({{< relref "iam" >}}) | [iam]({{< relref "/registry/packages/aws/api-docs/iam" >}}) |
| [Amazon Inspector](https://aws.amazon.com/inspector/) | Automated security assessments | | [inspector]({{< relref "/registry/packages/aws/api-docs/inspector" >}}) |
| [AWS IoT](https://aws.amazon.com/iot/) | Internet of Things | | [iot]({{< relref "/registry/packages/aws/api-docs/iot" >}}) |
| [Amazon Kinesis](https://aws.amazon.com/kinesis/) | Collect, process, and analyze data streams | | [kinesis]({{< relref "/registry/packages/aws/api-docs/kinesis" >}}) |
| [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) | Create and control encryption keys | | [kms]({{< relref "/registry/packages/aws/api-docs/kms" >}}) |
| [AWS Lambda](https://aws.amazon.com/lambda/) | Run serverless code | [User Guide]({{< relref "lambda" >}}) | [lambda]({{< relref "/registry/packages/aws/api-docs/lambda" >}}) |
| [AWS License Manager](https://aws.amazon.com/license-manager/) | Manage, discover, and report license usage | | [licensemanager]({{< relref "/registry/packages/aws/api-docs/licensemanager" >}}) |
| [Amazon Lightsail](https://aws.amazon.com/lightsail/) | Easy cloud apps | | [lightsail]({{< relref "/registry/packages/aws/api-docs/lightsail" >}}) |
| [Amazon Macie](https://aws.amazon.com/macie/) | ML-powered security | | [macie]({{< relref "/registry/packages/aws/api-docs/macie" >}}) |
| [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/) | Prepare and protect video | | [mediapackage]({{< relref "/registry/packages/aws/api-docs/mediapackage" >}}) |
| [AWS Elemental MediaStore](https://aws.amazon.com/mediastore/) | Store and deliver streaming video | | [mediastore]({{< relref "/registry/packages/aws/api-docs/mediastore" >}}) |
| [Amazon MQ](https://aws.amazon.com/amazon-mq/) | Managed ActiveMQ message broker | | [mq]({{< relref "/registry/packages/aws/api-docs/mq" >}}) |
| [Amazon Managed Streaming for Apache Kafka (MSK)](https://aws.amazon.com/msk/) | Managed Apache Kafka service | | [msk]({{< relref "/registry/packages/aws/api-docs/msk" >}}) |
| [Amazon Neptune](https://aws.amazon.com/neptune/) | Fast, reliable graph database | | [neptune]({{< relref "/registry/packages/aws/api-docs/neptune" >}}) |
| [AWS OpsWorks](https://aws.amazon.com/opsworks/) | Automate ops with Chef or Puppet | | [opsworks]({{< relref "/registry/packages/aws/api-docs/opsworks" >}}) |
| [AWS Organizations](https://aws.amazon.com/organizations/) | Central management of many accounts | | [organizations]({{< relref "/registry/packages/aws/api-docs/organizations" >}}) |
| [Amazon Pinpoint](https://aws.amazon.com/pinpoint/) | Engage customers | | [pinpoint]({{< relref "/registry/packages/aws/api-docs/pinpoint" >}}) |
| [AWS Resource Access Manager](https://aws.amazon.com/ram/) | Share AWS resources | | [ram]({{< relref "/registry/packages/aws/api-docs/ram" >}}) |
| [Amazon Relational Database Service (RDS)](https://aws.amazon.com/rds/) | Managed relational databases | | [rds]({{< relref "/registry/packages/aws/api-docs/rds" >}}) |
| [Amazon Redshift](https://aws.amazon.com/redshift/) | Managed data warehouse | | [redshift]({{< relref "/registry/packages/aws/api-docs/redshift" >}}) |
| [Amazon Route 53](https://aws.amazon.com/route53/) | Managed Domain Name System (DNS) service | | [route53]({{< relref "/registry/packages/aws/api-docs/route53" >}}) |
| [Simple Storage Service (S3)](https://aws.amazon.com/s3/) | Simple object storage | | [s3]({{< relref "/registry/packages/aws/api-docs/s3" >}}) |
| [Amazon SageMaker](https://aws.amazon.com/s3/) | Machine learning training and optimization | | [sagemaker]({{< relref "/registry/packages/aws/api-docs/sagemaker" >}}) |
| [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) | Store and protect secrets | | [secretsmanager]({{< relref "/registry/packages/aws/api-docs/secretsmanager" >}}) |
| [AWS Security Hub](https://aws.amazon.com/security-hub/) | Centrally view and manage compliance | | [securityhub]({{< relref "/registry/packages/aws/api-docs/securityhub" >}}) |
| [AWS Service Catalog](https://aws.amazon.com/servicecatalog/) | Manage catalogs of IT services | | [servicecatalog]({{< relref "/registry/packages/aws/api-docs/servicecatalog" >}}) |
| [AWS Cloud Map](https://aws.amazon.com/cloud-map/) | Service discovery for cloud resources | | [servicediscovery]({{< relref "/registry/packages/aws/api-docs/servicediscovery" >}}) |
| [Amazon Simple Email Service (SES)](https://aws.amazon.com/ses/) | Send and receive email | | [ses]({{< relref "/registry/packages/aws/api-docs/ses" >}}) |
| [AWS Step Functions](https://aws.amazon.com/step-functions/) | Build distributed workflows | | [sfn]({{< relref "/registry/packages/aws/api-docs/sfn" >}}) |
| [AWS Shield](https://aws.amazon.com/shield/) | Managed DDoS protection | | [shield]({{< relref "/registry/packages/aws/api-docs/shield" >}}) |
| [Amazon SimpleDB](https://aws.amazon.com/simpledb/) | Simple NoSQL database | | [simpledb]({{< relref "/registry/packages/aws/api-docs/simpledb" >}}) |
| [Amazon Simple Notification Service (SNS)](https://aws.amazon.com/sns/) | Managed pub/sub messaging | | [sns]({{< relref "/registry/packages/aws/api-docs/sns" >}}) |
| [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/sqs/) | Managed, reliable queuing | | [sqs]({{< relref "/registry/packages/aws/api-docs/sqs" >}}) |
| [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/) | Automate management tasks | | [ssm]({{< relref "/registry/packages/aws/api-docs/ssm" >}}) |
| [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) | Hybrid cloud storage | | [storagegateway]({{< relref "/registry/packages/aws/api-docs/storagegateway" >}}) |
| [Amazon Simple Workflow Service (SWF)](https://aws.amazon.com/swf/) | Background jobs with steps | | [swf]({{< relref "/registry/packages/aws/api-docs/swf" >}}) |
| [AWS Transfer for SFTP](https://aws.amazon.com/sftp/) | Managed SFTP service | | [transfer]({{< relref "/registry/packages/aws/api-docs/transfer" >}}) |
| [Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/) | Secure, isolated networks | [User Guide]({{< relref "vpc" >}}) | [vpc]({{< relref "/docs/reference/pkg/nodejs/pulumi/awsx/ec2#Vpc" >}}) |
| [AWS Web Application Firewall (WAF)](https://aws.amazon.com/waf/) | Protect web apps from exploits | | [waf]({{< relref "/registry/packages/aws/api-docs/waf" >}}) |
| [Amazon WorkLink](https://aws.amazon.com/worklink/) | Secure mobile access to internal apps | | [worklink]({{< relref "/registry/packages/aws/api-docs/worklink" >}}) |
| [Amazon WorkSpaces](https://aws.amazon.com/workspaces/) | Remote desktop access | | [workspaces]({{< relref "/registry/packages/aws/api-docs/workspaces" >}}) |
| [AWS X-Ray](https://aws.amazon.com/xray/) | Analyze and debug distributed apps | | [xray]({{< relref "/registry/packages/aws/api-docs/xray" >}}) |

## Additional AWS Resources

For more information about using Pulumi with AWS, see the following:

* [Pulumi AWS Get Started guide]({{< relref "/docs/get-started/aws" >}})
* [Pulumi AWS API documentation]({{< relref "/registry/packages/aws/api-docs" >}})
* [Pulumi Blog entries tagged with "AWS"](/blog/tag/aws/)
* [Pulumi Examples repository](https://github.com/pulumi/examples)
