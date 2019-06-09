---
title: "Other AWS Services"
menu:
  reference:
    parent: crosswalk-aws
    name: Other AWS Services
    weight: 11
---

Pulumi Crosswalk for AWS supports all AWS services, not just those with dedicated articles in this User Guide.
This includes services like DynamoDB, EC2, S3, and RDS, to name a few, and includes support for all of their features.
If your favorite service isn't listed here, please contact us by [filing an issue in the docs repo](
https://github.com/pulumi/docs) or by [joining the Pulumi Community Slack channel](https://slack.pulumi.io).

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
| [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) | Manage TLS/SSL certificates | | [acm](/reference/pkg/nodejs/pulumi/aws/acm) |
| [AWS Certificate Manager Private Certificate Authority](https://docs.aws.amazon.com/acm-pca/latest/userguide/PcaWelcome.html) | Managed private CA service | | [acmpca](/reference/pkg/nodejs/pulumi/aws/acmpca) |
| [Amazon API Gateway](https://aws.amazon.com/api-gateway/) | Secure, scalable APIs | [User Guide]({{< relref "api-gateway.md" >}}) | [apigateway](/reference/pkg/nodejs/pulumi/aws/apigateway) |
| [AWS App Mesh](https://aws.amazon.com/app-mesh/) | App-level service networking | | [appmesh](/reference/pkg/nodejs/pulumi/aws/appmesh) |
| [AWS AppSync](https://aws.amazon.com/app-mesh/) | Data-driven apps and APIs | | [appsync](/reference/pkg/nodejs/pulumi/aws/appsync) |
| [Amazon Athena](https://aws.amazon.com/athena/) | Serverless queries over S3 | | [athena](/reference/pkg/nodejs/pulumi/aws/athena) |
| [AWS Auto Scaling](https://aws.amazon.com/autoscaling) | Automatic scaling policies | [User Guide]({{< relref "autoscaling.md" >}}) | [autoscaling](/reference/pkg/nodejs/pulumi/aws/autoscaling) |
| [AWS Backup](https://aws.amazon.com/backup/) | Centrally managed backups | | [backup](/reference/pkg/nodejs/pulumi/aws/backup) |
| [AWS Batch](https://aws.amazon.com/batch/) | Easy and efficient batch computing | | [batch](/reference/pkg/nodejs/pulumi/aws/batch) |
| [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) | Custom budgets and alerting | | [budgets](/reference/pkg/nodejs/pulumi/aws/budgets) |
| [AWS Config](https://aws.amazon.com/config/) | Record and evaluate resource config | | [cfg](/reference/pkg/nodejs/pulumi/aws/cfg) |
| [AWS Cloud9](https://aws.amazon.com/cloud9/) | Cloud IDE | | [cloud9](/reference/pkg/nodejs/pulumi/aws/cloud9) |
| [AWS CloudFormation](https://aws.amazon.com/cloudformation/) | Provision resources in YAML/JSON | | [cloudformation](/reference/pkg/nodejs/pulumi/aws/cloudformation) |
| [Amazon CloudFront](https://aws.amazon.com/cloudfront/) | Fast and secure CDN | | [cloudfront](/reference/pkg/nodejs/pulumi/aws/cloudfront) |
| [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) | Managed hardware security module (HSM) | | [cloudhsmv2](/reference/pkg/nodejs/pulumi/aws/cloudhsmv2) |
| [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) | Track user activity and API usage | | [cloudtrail](/reference/pkg/nodejs/pulumi/aws/cloudtrail) |
| [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) | Application and infrastructure monitoring | [User Guide]({{< relref "cloudwatch.md" >}}) | [cloudwatch](/reference/pkg/nodejs/pulumi/aws/cloudwatch) |
| [AWS CodeBuild](https://aws.amazon.com/codebuild/) | Build and test code | [User Guide](/reference/cd-aws-code-services/) | [codebuild](/reference/pkg/nodejs/pulumi/aws/codebuild) |
| [AWS CodeCommit](https://aws.amazon.com/codecommit/) | Host private Git repos | [User Guide](/reference/cd-aws-code-services/) | [codecommit](/reference/pkg/nodejs/pulumi/aws/codecommit) |
| [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) | Automate code deployments | [User Guide](/reference/cd-aws-code-services/) | [codedeploy](/reference/pkg/nodejs/pulumi/aws/codedeploy) |
| [AWS CodePipeline](https://aws.amazon.com/codepipeline) | Continuous delivery pipelines | [User Guide](/reference/cd-aws-code-services/) | [codepipeline](/reference/pkg/nodejs/pulumi/aws/codepipeline) |
| [Amazon Cognito](https://aws.amazon.com/cognito/) | Simple and secure user identity | | [cognito](/reference/pkg/nodejs/pulumi/aws/cognito) |
| [AWS Cost and Usage Reporting](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) | Report on usage and cost | | [cur](/reference/pkg/nodejs/pulumi/aws/cur) |
| [AWS DataSync](https://aws.amazon.com/datasync/) | Easily transfer data | | [datasync](/reference/pkg/nodejs/pulumi/aws/datasync) |
| [Amazon DynamoDB Accelerator (DAX)](https://aws.amazon.com/dynamodb/dax/) | Fully managed, in memory cache | | [dax](/reference/pkg/nodejs/pulumi/aws/dax) |
| [AWS Device Farm](https://aws.amazon.com/device-farm/) | Test mobile apps | | [devicefarm](/reference/pkg/nodejs/pulumi/aws/devicefarm) |
| [AWS Direct Connect](https://aws.amazon.com/directconnect/) | Private, dedicated networks | | [directconnect](/reference/pkg/nodejs/pulumi/aws/directconnect) |
| [AWS Directory Service](https://aws.amazon.com/directoryservice/) | Managed Active Directory | | [directoryservice](/reference/pkg/nodejs/pulumi/aws/directoryservice) |
| [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/dlm) | Manage resource lifecycle | | [dlm](/reference/pkg/nodejs/pulumi/aws/dlm) |
| [Amazon Data Migration Service](https://aws.amazon.com/dms/) | Migrate databases to AWS | | [dms](/reference/pkg/nodejs/pulumi/aws/dms) |
| [Amazon DocumentDB](https://aws.amazon.com/documentdb/) | MongoDB-compatible document database | | [docdb](/reference/pkg/nodejs/pulumi/aws/docdb) |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) | Fast and flexible NoSQL database | | [dynamodb](/reference/pkg/nodejs/pulumi/aws/dynamodb) |
| [Amazon Elastic Block Store (EBS)](https://aws.amazon.com/ebs/) | Persistent block storage for EC2 | | [ebs](/reference/pkg/nodejs/pulumi/aws/ebs) |
| [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/) | Secure and resizable compute | | [ec2](/reference/pkg/nodejs/pulumi/aws/ec2) |
| [AWS VPN](https://aws.amazon.com/vpn/) | Extend on-prem networks to the cloud | | [ec2clientvpn](/reference/pkg/nodejs/pulumi/aws/ec2clientvpn) |
| [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) | Connect across VPCs | | [ec2transitgateway](/reference/pkg/nodejs/pulumi/aws/ec2transitgateway) |
| [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) | Private container registries | [User Guide]({{< relref "ecr.md" >}}) | [ecr](/reference/pkg/nodejs/pulumi/aws/ecr) |
| [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/) | Run containerized apps | [User Guide]({{< relref "ecs.md" >}}) | [ecs](/reference/pkg/nodejs/pulumi/aws/ecs) |
| [Amazon Elastic File System (EFS)](https://aws.amazon.com/efs/) | Scalable, elastic file system | | [efs](/reference/pkg/nodejs/pulumi/aws/efs) |
| [Amazon Elastic Container Service for Kubernetes (EKS)](https://aws.amazon.com/eks/) | Managed Kubernetes service | [User Guide]({{< relref "eks.md" >}}) | [eks](/reference/pkg/nodejs/pulumi/aws/eks) |
| [Amazon ElastiCache](https://aws.amazon.com/elasticache/) | Managed Redis or Memcached service | | [elasticache](/reference/pkg/nodejs/pulumi/aws/elasticache) |
| [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) | Deploy and scale web apps | | [elasticbeanstalk](/reference/pkg/nodejs/pulumi/aws/elasticbeanstalk) |
| [AWS Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/) | Scale across many instances | [User Guide]({{< relref "elb.md" >}}) | [elasticloadbalancingv2](/reference/pkg/nodejs/pulumi/aws/elasticloadbalancingv2) |
| [Amazon Elasticsearch Service](https://aws.amazon.com/elasticsearch-service/) | Fully managed Elasticsearch service | | [elasticsearch](/reference/pkg/nodejs/pulumi/aws/elasticsearch) |
| [Amazon Elastic Transcoder](https://aws.amazon.com/elastictranscoder/) | Media transcoding in the cloud | | [elastictranscoder](/reference/pkg/nodejs/pulumi/aws/elastictranscoder) |
| [Amazon EMR](https://aws.amazon.com/emr/) | Spark, Hadoop, HBase, and other big data | | [emr](/reference/pkg/nodejs/pulumi/aws/emr) |
| [Amazon GameLift](https://aws.amazon.com/gamelift/) | Game server hosting | | [gamelift](/reference/pkg/nodejs/pulumi/aws/gamelift) |
| [Amazon S3 Glacier](https://aws.amazon.com/glacier/) | Long term archived data storage | | [glacier](/reference/pkg/nodejs/pulumi/aws/glacier) |
| [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) | Improve global availability | | [globalaccelerator](/reference/pkg/nodejs/pulumi/aws/globalaccelerator) |
| [AWS Glue](https://aws.amazon.com/glue/) | Extract, transform, and load (ETL) | | [glue](/reference/pkg/nodejs/pulumi/aws/glue) |
| [Amazon GuardDuty](https://aws.amazon.com/guardduty/) | Protect your accounts and workloads | | [guardduty](/reference/pkg/nodejs/pulumi/aws/guardduty) |
| [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) | Securely manage access | [User Guide]({{< relref "iam.md" >}}) | [iam](/reference/pkg/nodejs/pulumi/aws/iam) |
| [Amazon Inspector](https://aws.amazon.com/inspector/) | Automated security assessments | | [inspector](/reference/pkg/nodejs/pulumi/aws/inspector) |
| [AWS IoT](https://aws.amazon.com/iot/) | Internet of Things | | [iot](/reference/pkg/nodejs/pulumi/aws/iot) |
| [Amazon Kinesis](https://aws.amazon.com/kinesis/) | Collect, process, and analyze data streams | | [kinesis](/reference/pkg/nodejs/pulumi/aws/kinesis) |
| [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) | Create and control encryption keys | | [kms](/reference/pkg/nodejs/pulumi/aws/kms) |
| [AWS Lambda](https://aws.amazon.com/lambda/) | Run serverless code | [User Guide]({{< relref "lambda.md" >}}) | [lambda](/reference/pkg/nodejs/pulumi/aws/lambda) |
| [AWS License Manager](https://aws.amazon.com/license-manager/) | Manage, discover, and report license usage | | [licensemanager](/reference/pkg/nodejs/pulumi/aws/licensemanager) |
| [Amazon Lightsail](https://aws.amazon.com/lightsail/) | Easy cloud apps | | [lightsail](/reference/pkg/nodejs/pulumi/aws/lightsail) |
| [Amazon Macie](https://aws.amazon.com/macie/) | ML-powered security | | [macie](/reference/pkg/nodejs/pulumi/aws/macie) |
| [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/) | Prepare and protect video | | [mediapackage](/reference/pkg/nodejs/pulumi/aws/mediapackage) |
| [AWS Elemental MediaStore](https://aws.amazon.com/mediastore/) | Store and deliver streaming video | | [mediastore](/reference/pkg/nodejs/pulumi/aws/mediastore) |
| [Amazon MQ](https://aws.amazon.com/amazon-mq/) | Managed ActiveMQ message broker | | [mq](/reference/pkg/nodejs/pulumi/aws/mq) |
| [Amazon Managed Streaming for Apache Kafka (MSK)](https://aws.amazon.com/msk/) | Managed Apache Kafka service | | [msk](/reference/pkg/nodejs/pulumi/aws/msk) |
| [Amazon Neptune](https://aws.amazon.com/neptune/) | Fast, reliable graph database | | [neptune](/reference/pkg/nodejs/pulumi/aws/neptune) |
| [AWS OpsWorks](https://aws.amazon.com/opsworks/) | Automate ops with Chef or Puppet | | [opsworks](/reference/pkg/nodejs/pulumi/aws/opsworks) |
| [AWS Organizations](https://aws.amazon.com/organizations/) | Central management of many accounts | | [organizations](/reference/pkg/nodejs/pulumi/aws/organizations) |
| [Amazon Pinpoint](https://aws.amazon.com/pinpoint/) | Engage customers | | [pinpoint](/reference/pkg/nodejs/pulumi/aws/pinpoint) |
| [AWS Resource Access Manager](https://aws.amazon.com/ram/) | Share AWS resources | | [ram](/reference/pkg/nodejs/pulumi/aws/ram) |
| [Amazon Relational Database Service (RDS)](https://aws.amazon.com/rds/) | Managed relational databases | | [rds](/reference/pkg/nodejs/pulumi/aws/rds) |
| [Amazon Redshift](https://aws.amazon.com/redshift/) | Managed data warehouse | | [redshift](/reference/pkg/nodejs/pulumi/aws/redshift) |
| [Amazon Route 53](https://aws.amazon.com/route53/) | Managed Domain Name System (DNS) service | | [route53](/reference/pkg/nodejs/pulumi/aws/route53) |
| [Simple Storage Service (S3)](https://aws.amazon.com/s3/) | Simple object storage | | [s3](/reference/pkg/nodejs/pulumi/aws/s3) |
| [Amazon SageMaker](https://aws.amazon.com/s3/) | Machine learning training and optimization | | [sagemaker](/reference/pkg/nodejs/pulumi/aws/sagemaker) |
| [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) | Store and protect secrets | | [secretsmanager](/reference/pkg/nodejs/pulumi/aws/secretsmanager) |
| [AWS Security Hub](https://aws.amazon.com/security-hub/) | Centrally view and manage compliance | | [securityhub](/reference/pkg/nodejs/pulumi/aws/securityhub) |
| [AWS Service Catalog](https://aws.amazon.com/servicecatalog/) | Manage catalogs of IT services | | [servicecatalog](/reference/pkg/nodejs/pulumi/aws/servicecatalog) |
| [AWS Cloud Map](https://aws.amazon.com/cloud-map/) | Service discovery for cloud resources | | [servicediscovery](/reference/pkg/nodejs/pulumi/aws/servicediscovery) |
| [Amazon Simple Email Service (SES)](https://aws.amazon.com/ses/) | Send and receive email | | [ses](/reference/pkg/nodejs/pulumi/aws/ses) |
| [AWS Step Functions](https://aws.amazon.com/step-functions/) | Build distributed workflows | | [sfn](/reference/pkg/nodejs/pulumi/aws/sfn) |
| [AWS Shield](https://aws.amazon.com/shield/) | Managed DDoS protection | | [shield](/reference/pkg/nodejs/pulumi/aws/shield) |
| [Amazon SimpleDB](https://aws.amazon.com/simpledb/) | Simple NoSQL database | | [simpledb](/reference/pkg/nodejs/pulumi/aws/simpledb) |
| [Amazon Simple Notification Service (SNS)](https://aws.amazon.com/sns/) | Managed pub/sub messaging | | [sns](/reference/pkg/nodejs/pulumi/aws/sns) |
| [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/sqs/) | Managed, reliable queuing | | [sqs](/reference/pkg/nodejs/pulumi/aws/sqs) |
| [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/) | Automate management tasks | | [ssm](/reference/pkg/nodejs/pulumi/aws/ssm) |
| [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) | Hybrid cloud storage | | [storagegateway](/reference/pkg/nodejs/pulumi/aws/storagegateway) |
| [Amazon Simple Workflow Service (SWF)](https://aws.amazon.com/swf/) | Background jobs with steps | | [swf](/reference/pkg/nodejs/pulumi/aws/swf) |
| [AWS Transfer for SFTP](https://aws.amazon.com/sftp/) | Managed SFTP service | | [transfer](/reference/pkg/nodejs/pulumi/aws/transfer) |
| [Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/) | Secure, isolated networks | [User Guide]({{< relref "vpc.md" >}}) | [vpc](/reference/pkg/nodejs/pulumi/awsx/ec2/#Vpc) |
| [AWS Web Application Firewall (WAF)](https://aws.amazon.com/waf/) | Protect web apps from exploits | | [waf](/reference/pkg/nodejs/pulumi/aws/waf) |
| [Amazon WorkLink](https://aws.amazon.com/worklink/) | Secure mobile access to internal apps | | [worklink](/reference/pkg/nodejs/pulumi/aws/worklink) |
| [Amazon WorkSpaces](https://aws.amazon.com/workspaces/) | Remote desktop access | | [workspaces](/reference/pkg/nodejs/pulumi/aws/workspaces) |
| [AWS X-Ray](https://aws.amazon.com/xray/) | Analyze and debug distributed apps | | [xray](/reference/pkg/nodejs/pulumi/aws/xray) |

## Additional AWS Resources

For more information about using Pulumi with AWS, please see the following:

* [Pulumi AWS QuickStart](/quickstart/aws)
* [Pulumi AWS API documentation](/reference/pkg/nodejs/pulumi/aws)
* [Pulumi Blog entries tagged with "AWS"](https://blog.pulumi.com/tag/aws)
* [Pulumi Examples repository](https://github.com/pulumi/examples)
