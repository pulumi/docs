---
title: "Other AWS Services"
meta_desc: Pulumi Crosswalk for AWS supports all AWS services. This page provides a complete list of supported services.
menu:
  userguides:
    parent: crosswalk-aws
    weight: 11

aliases: ["/docs/reference/crosswalk/aws/other/"]
---

<a href="{{< relref "_index.md" >}}">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

Pulumi Crosswalk for AWS supports all AWS services, not just those with dedicated articles in this User Guide.
This includes services like DynamoDB, EC2, S3, and RDS, to name a few, and includes support for all of their features.
If your favorite service isn't listed here, please contact us by [filing an issue in the docs repo](
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
| [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) | Manage TLS/SSL certificates | | [acm]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/acm/_index.md" >}}) |
| [AWS Certificate Manager Private Certificate Authority](https://docs.aws.amazon.com/acm-pca/latest/userguide/PcaWelcome.html) | Managed private CA service | | [acmpca]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/acmpca/_index.md" >}}) |
| [Amazon API Gateway](https://aws.amazon.com/api-gateway/) | Secure, scalable APIs | [User Guide]({{< relref "api-gateway.md" >}}) | [apigateway]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/apigateway/_index.md" >}}) |
| [AWS App Mesh](https://aws.amazon.com/app-mesh/) | App-level service networking | | [appmesh]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/appmesh/_index.md" >}}) |
| [AWS AppSync](https://aws.amazon.com/app-mesh/) | Data-driven apps and APIs | | [appsync]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/appsync/_index.md" >}}) |
| [Amazon Athena](https://aws.amazon.com/athena/) | Serverless queries over S3 | | [athena]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/athena/_index.md" >}}) |
| [AWS Auto Scaling](https://aws.amazon.com/autoscaling) | Automatic scaling policies | [User Guide]({{< relref "autoscaling.md" >}}) | [autoscaling]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/autoscaling/_index.md" >}}) |
| [AWS Backup](https://aws.amazon.com/backup/) | Centrally managed backups | | [backup]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/backup/_index.md" >}}) |
| [AWS Batch](https://aws.amazon.com/batch/) | Easy and efficient batch computing | | [batch]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/batch/_index.md" >}}) |
| [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) | Custom budgets and alerting | | [budgets]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/budgets/_index.md" >}}) |
| [AWS Config](https://aws.amazon.com/config/) | Record and evaluate resource config | | [cfg]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/cfg/_index.md" >}}) |
| [AWS Cloud9](https://aws.amazon.com/cloud9/) | Cloud IDE | | [cloud9]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/cloud9/_index.md" >}}) |
| [AWS CloudFormation](https://aws.amazon.com/cloudformation/) | Provision resources in YAML/JSON | | [cloudformation]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/cloudformation/_index.md" >}}) |
| [Amazon CloudFront](https://aws.amazon.com/cloudfront/) | Fast and secure CDN | | [cloudfront]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/cloudfront/_index.md" >}}) |
| [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) | Managed hardware security module (HSM) | | [cloudhsmv2]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/cloudhsmv2/_index.md" >}}) |
| [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) | Track user activity and API usage | | [cloudtrail]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/cloudtrail/_index.md" >}}) |
| [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) | Application and infrastructure monitoring | [User Guide]({{< relref "cloudwatch.md" >}}) | [cloudwatch]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/cloudwatch/_index.md" >}}) |
| [AWS CodeBuild](https://aws.amazon.com/codebuild/) | Build and test code | [User Guide]({{< relref "/docs/guides/continuous-delivery/aws-code-services.md" >}}) | [codebuild]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/codebuild/_index.md" >}}) |
| [AWS CodeCommit](https://aws.amazon.com/codecommit/) | Host private Git repos | [User Guide]({{< relref "/docs/guides/continuous-delivery/aws-code-services.md" >}}) | [codecommit]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/codecommit/_index.md" >}}) |
| [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) | Automate code deployments | [User Guide]({{< relref "/docs/guides/continuous-delivery/aws-code-services.md" >}}) | [codedeploy]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/codedeploy/_index.md" >}}) |
| [AWS CodePipeline](https://aws.amazon.com/codepipeline) | Continuous delivery pipelines | [User Guide]({{< relref "/docs/guides/continuous-delivery/aws-code-services.md" >}}) | [codepipeline]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/codepipeline/_index.md" >}}) |
| [Amazon Cognito](https://aws.amazon.com/cognito/) | Simple and secure user identity | | [cognito]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/cognito/_index.md" >}}) |
| [AWS Cost and Usage Reporting](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) | Report on usage and cost | | [cur]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/cur/_index.md" >}}) |
| [AWS DataSync](https://aws.amazon.com/datasync/) | Easily transfer data | | [datasync]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/datasync/_index.md" >}}) |
| [Amazon DynamoDB Accelerator (DAX)](https://aws.amazon.com/dynamodb/dax/) | Fully managed, in memory cache | | [dax]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/dax/_index.md" >}}) |
| [AWS Device Farm](https://aws.amazon.com/device-farm/) | Test mobile apps | | [devicefarm]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/devicefarm/_index.md" >}}) |
| [AWS Direct Connect](https://aws.amazon.com/directconnect/) | Private, dedicated networks | | [directconnect]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/directconnect/_index.md" >}}) |
| [AWS Directory Service](https://aws.amazon.com/directoryservice/) | Managed Active Directory | | [directoryservice]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/directoryservice/_index.md" >}}) |
| [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/dlm) | Manage resource lifecycle | | [dlm]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/dlm/_index.md" >}}) |
| [Amazon Data Migration Service](https://aws.amazon.com/dms/) | Migrate databases to AWS | | [dms]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/dms/_index.md" >}}) |
| [Amazon DocumentDB](https://aws.amazon.com/documentdb/) | MongoDB-compatible document database | | [docdb]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/docdb/_index.md" >}}) |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) | Fast and flexible NoSQL database | | [dynamodb]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/dynamodb/_index.md" >}}) |
| [Amazon Elastic Block Store (EBS)](https://aws.amazon.com/ebs/) | Persistent block storage for EC2 | | [ebs]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ebs/_index.md" >}}) |
| [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/) | Secure and resizable compute | | [ec2]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ec2/_index.md" >}}) |
| [AWS VPN](https://aws.amazon.com/vpn/) | Extend on-prem networks to the cloud | | [ec2clientvpn]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ec2clientvpn/_index.md" >}}) |
| [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) | Connect across VPCs | | [ec2transitgateway]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ec2transitgateway/_index.md" >}}) |
| [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) | Private container registries | [User Guide]({{< relref "ecr.md" >}}) | [ecr]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ecr/_index.md" >}}) |
| [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/) | Run containerized apps | [User Guide]({{< relref "ecs.md" >}}) | [ecs]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ecs/_index.md" >}}) |
| [Amazon Elastic File System (EFS)](https://aws.amazon.com/efs/) | Scalable, elastic file system | | [efs]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/efs/_index.md" >}}) |
| [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) | Managed Kubernetes service | [User Guide]({{< relref "eks.md" >}}) | [eks]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/eks/_index.md" >}}) |
| [Amazon ElastiCache](https://aws.amazon.com/elasticache/) | Managed Redis or Memcached service | | [elasticache]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/elasticache/_index.md" >}}) |
| [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) | Deploy and scale web apps | | [elasticbeanstalk]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/elasticbeanstalk/_index.md" >}}) |
| [AWS Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/) | Scale across many instances | [User Guide]({{< relref "elb.md" >}}) | [lb]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/lb/_index.md" >}}) |
| [Amazon Elasticsearch Service](https://aws.amazon.com/elasticsearch-service/) | Fully managed Elasticsearch service | | [elasticsearch]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/elasticsearch/_index.md" >}}) |
| [Amazon Elastic Transcoder](https://aws.amazon.com/elastictranscoder/) | Media transcoding in the cloud | | [elastictranscoder]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/_index.md" >}}) |
| [Amazon EMR](https://aws.amazon.com/emr/) | Spark, Hadoop, HBase, and other big data | | [emr]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/emr/_index.md" >}}) |
| [Amazon GameLift](https://aws.amazon.com/gamelift/) | Game server hosting | | [gamelift]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/gamelift/_index.md" >}}) |
| [Amazon S3 Glacier](https://aws.amazon.com/glacier/) | Long term archived data storage | | [glacier]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/glacier/_index.md" >}}) |
| [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) | Improve global availability | | [globalaccelerator]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/globalaccelerator/_index.md" >}}) |
| [AWS Glue](https://aws.amazon.com/glue/) | Extract, transform, and load (ETL) | | [glue]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/glue/_index.md" >}}) |
| [Amazon GuardDuty](https://aws.amazon.com/guardduty/) | Protect your accounts and workloads | | [guardduty]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/guardduty/_index.md" >}}) |
| [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) | Securely manage access | [User Guide]({{< relref "iam.md" >}}) | [iam]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/iam/_index.md" >}}) |
| [Amazon Inspector](https://aws.amazon.com/inspector/) | Automated security assessments | | [inspector]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/inspector/_index.md" >}}) |
| [AWS IoT](https://aws.amazon.com/iot/) | Internet of Things | | [iot]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/iot/_index.md" >}}) |
| [Amazon Kinesis](https://aws.amazon.com/kinesis/) | Collect, process, and analyze data streams | | [kinesis]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/kinesis/_index.md" >}}) |
| [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) | Create and control encryption keys | | [kms]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/kms/_index.md" >}}) |
| [AWS Lambda](https://aws.amazon.com/lambda/) | Run serverless code | [User Guide]({{< relref "lambda.md" >}}) | [lambda]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/lambda/_index.md" >}}) |
| [AWS License Manager](https://aws.amazon.com/license-manager/) | Manage, discover, and report license usage | | [licensemanager]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/licensemanager/_index.md" >}}) |
| [Amazon Lightsail](https://aws.amazon.com/lightsail/) | Easy cloud apps | | [lightsail]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/lightsail/_index.md" >}}) |
| [Amazon Macie](https://aws.amazon.com/macie/) | ML-powered security | | [macie]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/macie/_index.md" >}}) |
| [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/) | Prepare and protect video | | [mediapackage]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/mediapackage/_index.md" >}}) |
| [AWS Elemental MediaStore](https://aws.amazon.com/mediastore/) | Store and deliver streaming video | | [mediastore]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/mediastore/_index.md" >}}) |
| [Amazon MQ](https://aws.amazon.com/amazon-mq/) | Managed ActiveMQ message broker | | [mq]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/mq/_index.md" >}}) |
| [Amazon Managed Streaming for Apache Kafka (MSK)](https://aws.amazon.com/msk/) | Managed Apache Kafka service | | [msk]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/msk/_index.md" >}}) |
| [Amazon Neptune](https://aws.amazon.com/neptune/) | Fast, reliable graph database | | [neptune]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/neptune/_index.md" >}}) |
| [AWS OpsWorks](https://aws.amazon.com/opsworks/) | Automate ops with Chef or Puppet | | [opsworks]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/opsworks/_index.md" >}}) |
| [AWS Organizations](https://aws.amazon.com/organizations/) | Central management of many accounts | | [organizations]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/organizations/_index.md" >}}) |
| [Amazon Pinpoint](https://aws.amazon.com/pinpoint/) | Engage customers | | [pinpoint]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/pinpoint/_index.md" >}}) |
| [AWS Resource Access Manager](https://aws.amazon.com/ram/) | Share AWS resources | | [ram]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ram/_index.md" >}}) |
| [Amazon Relational Database Service (RDS)](https://aws.amazon.com/rds/) | Managed relational databases | | [rds]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/rds/_index.md" >}}) |
| [Amazon Redshift](https://aws.amazon.com/redshift/) | Managed data warehouse | | [redshift]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/redshift/_index.md" >}}) |
| [Amazon Route 53](https://aws.amazon.com/route53/) | Managed Domain Name System (DNS) service | | [route53]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/route53/_index.md" >}}) |
| [Simple Storage Service (S3)](https://aws.amazon.com/s3/) | Simple object storage | | [s3]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/s3/_index.md" >}}) |
| [Amazon SageMaker](https://aws.amazon.com/s3/) | Machine learning training and optimization | | [sagemaker]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/sagemaker/_index.md" >}}) |
| [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) | Store and protect secrets | | [secretsmanager]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/secretsmanager/_index.md" >}}) |
| [AWS Security Hub](https://aws.amazon.com/security-hub/) | Centrally view and manage compliance | | [securityhub]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/securityhub/_index.md" >}}) |
| [AWS Service Catalog](https://aws.amazon.com/servicecatalog/) | Manage catalogs of IT services | | [servicecatalog]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/servicecatalog/_index.md" >}}) |
| [AWS Cloud Map](https://aws.amazon.com/cloud-map/) | Service discovery for cloud resources | | [servicediscovery]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/servicediscovery/_index.md" >}}) |
| [Amazon Simple Email Service (SES)](https://aws.amazon.com/ses/) | Send and receive email | | [ses]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ses/_index.md" >}}) |
| [AWS Step Functions](https://aws.amazon.com/step-functions/) | Build distributed workflows | | [sfn]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/sfn/_index.md" >}}) |
| [AWS Shield](https://aws.amazon.com/shield/) | Managed DDoS protection | | [shield]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/shield/_index.md" >}}) |
| [Amazon SimpleDB](https://aws.amazon.com/simpledb/) | Simple NoSQL database | | [simpledb]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/simpledb/_index.md" >}}) |
| [Amazon Simple Notification Service (SNS)](https://aws.amazon.com/sns/) | Managed pub/sub messaging | | [sns]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/sns/_index.md" >}}) |
| [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/sqs/) | Managed, reliable queuing | | [sqs]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/sqs/_index.md" >}}) |
| [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/) | Automate management tasks | | [ssm]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ssm/_index.md" >}}) |
| [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) | Hybrid cloud storage | | [storagegateway]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/storagegateway/_index.md" >}}) |
| [Amazon Simple Workflow Service (SWF)](https://aws.amazon.com/swf/) | Background jobs with steps | | [swf]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/swf/_index.md" >}}) |
| [AWS Transfer for SFTP](https://aws.amazon.com/sftp/) | Managed SFTP service | | [transfer]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/transfer/_index.md" >}}) |
| [Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/) | Secure, isolated networks | [User Guide]({{< relref "vpc.md" >}}) | [vpc]({{< relref "/docs/reference/pkg/nodejs/pulumi/awsx/ec2/_index.md#Vpc" >}}) |
| [AWS Web Application Firewall (WAF)](https://aws.amazon.com/waf/) | Protect web apps from exploits | | [waf]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/waf/_index.md" >}}) |
| [Amazon WorkLink](https://aws.amazon.com/worklink/) | Secure mobile access to internal apps | | [worklink]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/worklink/_index.md" >}}) |
| [Amazon WorkSpaces](https://aws.amazon.com/workspaces/) | Remote desktop access | | [workspaces]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/workspaces/_index.md" >}}) |
| [AWS X-Ray](https://aws.amazon.com/xray/) | Analyze and debug distributed apps | | [xray]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/xray/_index.md" >}}) |

## Additional AWS Resources

For more information about using Pulumi with AWS, please see the following:

* [Pulumi AWS Get Started guide]({{< relref "/docs/get-started/aws" >}})
* [Pulumi AWS API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws" >}})
* [Pulumi Blog entries tagged with "AWS"](/blog/tag/aws/)
* [Pulumi Examples repository](https://github.com/pulumi/examples)
