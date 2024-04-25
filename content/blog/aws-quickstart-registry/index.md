---
title: "Using AWS Quick Starts with the Pulumi Registry"
date: 2022-01-05
meta_desc: "Pulumi releases AWS Quick Start packages in the Pulumi registry"
meta_image: pulumi-aws-quickstart-registry.png
authors:
    - aidan-hoolachan
tags:
    - aws
    - vpc
    - postgres
    - postgresql
    - aurora
    - redshift
    - registry
---

As somebody who works on AWS projects across numerous projects, teams, and industries; I see the following three common types of infrastructure problems. I think the Pulumi Registry provides an incredible solution to each of these problems and will fundamentally change how people interact with AWS.

<!--more-->

Common AWS infrastructure problems:

- **AWS Console Wizard Fever** - These companies use the AWS Console to deploy resources. They move very quickly initially but eventually their AWS accounts become cluttered with untracked resources and they need to do some heavy lifting to set up robust dev / staging / prod environments. Many AWS developers scoff at the idea of using the Console, but I actually think this is currently an okay approach for a lot of people / companies in the early stages of AWS development. The console provides a **lot** of assistance when doing deployments and most people don't need very complicated infrastructure initially. It's not ideal because of the tech debt but it's the right choice for many situations (at least, it was the right choice before the Pulumi registry).

- **YAML/JSON CloudFormation Template Ceiling** - These companies have the right idea to use Infrastructure as Code, but CloudFormation YAML/JSON templates or other limited frameworks like Amplify are unwieldy and have their own scaling problems. Most people who work closely with AWS advocate for Infrastructure as Code (I do too), but it really is a steep learning curve and can be a lot of overhead for many simple applications. Setting up email alarms when a database goes down requires specialized AWS knowledge to do correctly -- which makes a basic feature like email/slack alarm notifications feel like a sophisticated luxury. It shouldn't be complicated, but it is.

- **AWS Lock-in** - These are companies who lean into the AWS ecosystem for convenience sake. They might choose Cognito over a third-party Identity Provider even though the third-party Identity Provider might be a superior service.

The underlying cause of these problems is that AWS's core services are designed for modularity within the AWS ecosystem, which is great for flexibility and experienced AWS developers, but it makes building best-practice AWS environments surprisingly difficult. Most "best practice" features on AWS, like email alarms when a database goes down, should really be the standard practice, but those features currently require complicated cross-service relationships that are difficult to implement correctly. The AWS ecosystem has been waiting for a layer of abstraction on top of these resources.

Pulumi and the AWS Quick Starts in the [Pulumi Registry](https://www.pulumi.com/registry/) use higher-order components to abstract away that underlying complexity which makes configuring, deploying, and managing critical AWS resources straightforward -- like it should be.

Configuring an Aurora Postgresql database with best practices (again, what should really just be the standard practices) requires specialized AWS knowledge and provisioning a zoo of other critical resources:

- Encryption (2 resources) - KMS Key + KMS Key Policy
- Access logging (4 resources) - S3 + S3 Bucket Policy + Encryption (KMS, again) + IAM Role
- Alarms with notifications (3 Resources) - Cloudwatch Events + SNS + SNS Subscription
- Networking infrastructure - (4+ resources) VPCs + Subnets + Gateways, etc.
- Username and password - (1 resource) Secrets Manager Secret
- Redundancy - (multiple resources) RDS multi-AZ clusters
- IAM - (too many resources) Various IAM roles and policies

If "Aurora Postgres RDS" were a third-party SaaS or PaaS service provider, the service would abstract away the above details and provide simple parameters for enabling encryption, alarms, notifications, network security, redundancy, monitoring, and logging. With Pulumi, that abstraction is possible while providing open-source access to the underlying AWS resource definitions and with much more flexibility than traditional CloudFormation or Terraform. Those features can even be enabled by default. I believe that AWS "best practices" will also become the easiest approach with Pulumi as the ecosystem matures around the best packages.

When writing the Pulumi providers for AWS Quick Start VPC, AWS Quick Start Aurora Postgres, and AWS Quick Start Redshift, we were able to fight through the complexity and implement the best practices listed above. Those practices are enabled by default but can be disabled using a flag (eg `enableEncryption: false`). The result is a simple interface for deploying a VPC, an Aurora Postgresql cluster, and a Redshift cluster along with all of the other resources needed for best practice deployments. The process for writing these AWS providers was straightforward and intuitive. The Pulumi deployment and debug process was pleasant and I was able to go through most of the deploy + debug + tear down lifecycle without leaving the terminal.

The following code deploys a VPC, an Aurora Postgresql Cluster, a Redshift Cluster, and the various helper resources needed for encryption, logging, database alarms, vpc flow logs, etc. -- for a total of 47 resources deployed using only three functions with simple parameters.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as vpcQuickstart from "@pulumi/aws-quickstart-vpc";
import * as redshiftQuickstart from "@pulumi/aws-quickstart-redshift";
import * as auroraQuickstart from "@pulumi/aws-quickstart-aurora-postgres";

const notificationEmail = process.env.notificationEmail;
const dbPasswordSecret = pulumi.secret(process.env.databasePassword);

// Create a best-practices VPC
// Deploys 21 resources
const multiAvailabilityZoneVpc = new vpcQuickstart.Vpc("example-aurora-vpc", {
    cidrBlock: "10.0.0.0/16",
    availabilityZoneConfig: [{
        availabilityZone: "us-east-1a",
        publicSubnetCidr: "10.0.128.0/20",
        privateSubnetACidr: "10.0.32.0/19",
    }, {
        availabilityZone: "us-east-1b",
        privateSubnetACidr: "10.0.64.0/19",
    }]
})

// Create a best-practices Aurora Postgresql cluster
// Deploys 17 resources
const multiAvaialabilityZoneAuroraCluster = new auroraQuickstart.Cluster("example-aurora-cluster", {
  vpcID: multiAvailabilityZoneVpc.vpcID,
  dbName: "myDemoDatabase",
  dbEngineVersion: "11.9",
  dbInstanceClass: "db.t3.medium",
  availabilityZoneNames: ["us-east-1a", "us-east-1b"],
  dbNumDbClusterInstances: 2,
  dbMasterUsername: "mainuser",
  snsNotificationEmail: databaseNotificationEmail,
  enableEventSubscription: true,
  dbMasterPassword: dbPasswordSecret,
  dbParameterGroupFamily: "aurora-postgresql11",
  privateSubnetID1: multiAvailabilityZoneVpc.privateSubnetIDs.apply(x => x![0]),
  privateSubnetID2: multiAvailabilityZoneVpc.privateSubnetIDs.apply(x => x![1]),
});

// Create a best-practices Redshift cluster
// Deploys 8 resources
const cluster = new redshiftQuickstart.Cluster("example-redshift-cluster", {
  vpcID: multiAvailabilityZoneVpc.vpcID,
  dbPort: 5432,
  dbClusterIdentifier: "example-redshift-cluster",
  dbMasterUsername: "mainuser",
  notificationEmail: notificationEmail,
  enableEventSubscription: true,
  dbMasterPassword: dbPasswordSecret,
  dbName: "main",
  dbNodeType: "dc2.large",
  subnetIDs: multiAvailabilityZoneVpc.privateSubnetIDs as pulumi.Output<string[]>
})

```

These AWS Quick Start components are recommended for developers with all levels of AWS skill. For developers who don't work with AWS frequently, these Quick Starts can replace the AWS Console Wizards for confidently provisioning resources.

For experienced AWS developers who want to use these components and are concerned about abstraction, there are several options: (1) review the underlying open source code, (2) do a quick proof-of-concept deployment and use Pulumi's resource management tools to review the resources, and (3) when necessary, alter the underlying code! In my experience, because I was so accustomed to defining every painful detail of AWS infrastructure, the abstractions felt almost too easy to use. However, once I became comfortable with the underlying design patterns, these packages made deploying complicated AWS architectures incredibly easy, quick, and reliable.

For service providers considering providing a Pulumi package for their service offering -- as an AWS developer, the most exciting part of this toolset is the ability to choose non-AWS tools without sacrificing convenience. I sometimes choose Cognito over Okta simply because Cognito is in the AWS ecosystem. If service provider packages are as convenient as using native AWS tools, they become more competitive with AWS' native services.

Returning to the initial three problems:

- **AWS Console Wizard Fever** - By creating many of the "helper" resources (like email notifications when the database goes down), the Pulumi registry serves the same purpose as the AWS Console wizards -- "best practice" infrastructure / applications are available at the click of a button.

- **YAML/JSON CloudFormation Template Ceiling** - Software / programming languages are much easier to work with than YAML or JSON templates. Programming languages provide simpler logic, abstraction, auto-complete, guardrails, open-source imports, and all of the other benefits of programming languages. Furthermore, the Pulumi framework provides infrastructure review tools during deployments, which mitigates the risks of programming language bugs affecting deployments (eg. there are robust safeguards against an infinite "for" loop spinning up an infinite number of EC2 instances).

- **AWS Lock-in** - In addition to Pulumi making it substantially easier to use AWS services, Pulumi makes it substantially easier to use other SAAS and cloud providers alongside AWS resources. As the registry matures around standard abstractions, I can imagine constructs for "Postgres Database" or "Serverless Website" or "Next.js Deployment" that are implemented by multiple SAAS or cloud providers such that a developer can switch clouds with a few minor configuration changes.

For getting started, I recommend starting with the examples for the [AWS Quick Start VPC](https://github.com/pulumi/pulumi-aws-quickstart-vpc/tree/main/examples), [AWS Quick Start Aurora Postgres](https://github.com/pulumi/pulumi-aws-quickstart-aurora-postgres/tree/master/examples), and [Aurora Quick Start Redshift](https://github.com/pulumi/pulumi-aws-quickstart-redshift/tree/main/examples).
