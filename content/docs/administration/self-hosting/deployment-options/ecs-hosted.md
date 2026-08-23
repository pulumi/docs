---
title_tag: ECS Install | Self-Hosting Pulumi
meta_desc: Install self-hosted Pulumi Cloud on Amazon ECS Fargate — prerequisites, the three Pulumi projects, configuration reference, and how to verify the installation.
title: ECS
h1: Install Self-Hosted Pulumi Cloud on Amazon ECS
menu:
  administration:
        name: ECS
        parent: administration-self-hosting-deployment-options
        weight: 2
        identifier: administration-self-hosting-deployment-options-ecs
aliases:
  - /docs/guides/self-hosted/ecs-hosted/
  - /docs/pulumi-cloud/self-hosted/deployment-options/ecs-hosted/
  - /docs/pulumi-cloud/admin/self-hosted/deployment-options/ecs-hosted/
pulumi_cloud_feature: self-hosting
---

{{< self-hosting-trial-note />}}

The [ECS installer](https://github.com/pulumi/pulumi-self-hosted-installers/tree/master/ecs-hosted) runs the Pulumi API and console as Fargate services behind Application Load Balancers, backed by Aurora MySQL and S3. Pick this option when you want a production installation on AWS without operating Kubernetes.

The installer ships in TypeScript and Go. The commands below use the TypeScript version; the Go version lives in `ecs-hosted/go` and takes the same configuration.

## What gets deployed

| Service | Purpose |
| :-- | :-- |
| ECS on Fargate | Runs the API and console containers |
| Aurora MySQL | Persistent state, with automated replication and snapshots |
| S3 | Checkpoints, policy packs, and service metadata |
| OpenSearch | Resource search (optional) |
| Application Load Balancer | Traffic routing and TLS termination |
| Route 53 | DNS records for the API and console |
| VPC endpoints | Private connectivity to AWS services |

## Prerequisites

You provide the network, DNS, certificate, and key material. The installer builds everything else.

**AWS access.** `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in the environment, plus `AWS_SESSION_TOKEN` if you use temporary credentials.

**Networking.** An existing VPC with at least two public, two private, and two isolated subnets.

**DNS and TLS.** A Route 53 hosted zone, and an ACM certificate covering the base domain plus `app.{sub}.example.com` and `api.{sub}.example.com`.

**Encryption.** A KMS key for the service to encrypt and decrypt secrets.

**Images.** ECR repositories holding the Pulumi API, console, and migrations images.

**License.** A `PULUMI_LICENSE_KEY` and an AG Grid license key.

See [System requirements](/docs/administration/self-hosting/system-requirements/) for database, storage, and sizing details that apply to every installation.

## Sizing

Defaults are deliberately small so a first deployment comes up quickly. Raise them before running production workloads.

| Setting | Default |
| :-- | :-- |
| `dbInstanceType` | `db.t3.small` — burstable; see [Database](/docs/administration/self-hosting/operations/database/) |
| `apiTaskCpu` / `apiTaskMemory` | 512 / 1024 MB |
| `consoleTaskCpu` / `consoleTaskMemory` | 256 / 512 MB |
| `apiDesiredNumberTasks` | 1 — raise to at least 2 for high availability |

## Install

The installer is itself a set of Pulumi programs, so you need a state backend for them. These use an S3 bucket, which keeps the installer's own state independent of the installation it creates.

Deploy the three projects in order. Each consumes outputs from the one before it.

### 1. Get the installer

```bash
git clone https://github.com/pulumi/pulumi-self-hosted-installers.git
cd pulumi-self-hosted-installers/ecs-hosted/ts
pulumi login s3://<your-state-bucket>
```

### 2. Deploy base infrastructure

Creates the Aurora cluster, VPC endpoints, and security groups.

```bash
cd infrastructure
npm install
pulumi stack init
pulumi config set aws:region us-west-2
pulumi config set vpcId vpc-0123456789abcdef0
pulumi config set publicSubnetIds '["subnet-aaa","subnet-bbb"]'
pulumi config set privateSubnetIds '["subnet-ccc","subnet-ddd"]'
pulumi config set isolatedSubnetIds '["subnet-eee","subnet-fff"]'
pulumi up
```

### 3. Deploy the application

Creates the ECS clusters and the API and console services.

```bash
cd ../application
npm install
pulumi stack init
pulumi config set aws:region us-west-2
pulumi config set imageTag <image-tag>
pulumi config set acmCertificateArn <acm-certificate-arn>
pulumi config set kmsServiceKeyId <kms-key-id>
pulumi config set licenseKey <license-key> --secret
pulumi config set route53ZoneName example.com
pulumi config set route53Subdomain pulumi
pulumi up
```

The database, security group, and OpenSearch values come from the previous stack's outputs. Set them with `pulumi config set` as shown in the [configuration reference](#configuration-reference) below.

{{% notes type="info" %}}
Pin `imageTag` to a specific version rather than `latest`, so an unrelated `pulumi up` cannot roll the service forward unintentionally. Tags are listed on [Docker Hub](https://hub.docker.com/r/pulumi/service/tags).
{{% /notes %}}

### 4. Create DNS records

```bash
cd ../dns
npm install
pulumi stack init
pulumi config set aws:region us-west-2
pulumi config set route53ZoneName example.com
pulumi config set route53Subdomain pulumi
pulumi config set apiLoadBalancerDnsName <api-lb-dns-name>
pulumi config set apiLoadBalancerZoneId <api-lb-zone-id>
pulumi config set consoleLoadBalancerDnsName <console-lb-dns-name>
pulumi config set consoleLoadBalancerZoneId <console-lb-zone-id>
pulumi up
```

## Configuration reference

### Base infrastructure

| Key | Required | Default | Description |
| :-- | :-- | :-- | :-- |
| `aws:region` | Yes | | AWS region |
| `vpcId` | Yes | | Existing VPC |
| `publicSubnetIds` | Yes | | At least two public subnet IDs |
| `privateSubnetIds` | Yes | | At least two private subnet IDs |
| `isolatedSubnetIds` | Yes | | At least two isolated subnet IDs |
| `dbInstanceType` | No | `db.t3.small` | RDS instance type |
| `enableOpenSearch` | No | | Deploy an OpenSearch domain for resource search |
| `openSearchInstanceType` | No | `t3.medium.search` | OpenSearch instance type |
| `openSearchInstanceCount` | No | `2` | Cannot be lower than 2 |
| `openSearchDomainName` | No | `pulumi` | OpenSearch domain name |
| `openSearchDedicatedMasterCount` | No | none | Dedicated master nodes |

### Application

| Key | Required | Default | Description |
| :-- | :-- | :-- | :-- |
| `aws:region` | Yes | | AWS region |
| `vpcId` | Yes | | Existing VPC |
| `publicSubnetIds` / `privateSubnetIds` / `isolatedSubnetIds` | Yes | | Subnet IDs, as above |
| `imageTag` | Yes | | Pulumi container image tag |
| `licenseKey` | Yes | | Set with `--secret` |
| `acmCertificateArn` | Yes | | Covers the Route 53 domain |
| `kmsServiceKeyId` | Yes | | KMS key securing secrets |
| `route53ZoneName` | Yes | | Hosted zone name |
| `route53Subdomain` | Yes | | Subdomain for DNS records |
| `dbClusterEndpoint` | Yes | | Aurora cluster endpoint |
| `dbPort` | Yes | `3306` | MySQL port |
| `dbName` | Yes | | Database name |
| `dbUsername` / `dbPassword` | Yes | | Database credentials |
| `dbSecurityGroupId` | Yes | | Database security group |
| `endpointSecurityGroupId` | Yes | | Security group for VPC endpoints |
| `openSearchUser` / `openSearchPassword` | Yes | | OpenSearch credentials |
| `openSearchEndpoint` / `openSearchDomain` | Yes | | OpenSearch endpoint and domain |
| `apiDesiredNumberTasks` | No | `1` | API task count |
| `apiTaskCpu` / `apiTaskMemory` | No | `512` / `1024` | API task-level CPU and memory |
| `apiContainerCpu` | No | task CPU | CPU for the API container |
| `apiContainerMemoryReservation` | No | task memory | Memory reserved for the API container |
| `apiDisabledEmailLogin` / `apiDisabledEmailSignup` | No | | Disable the email login and signup handlers |
| `consoleDesiredNumberTasks` | No | `1` | Console task count |
| `consoleTaskCpu` / `consoleTaskMemory` | No | `256` / `512` | Console task-level CPU and memory |
| `consoleContainerCpu` | No | task CPU | CPU for the console container |
| `consoleContainerMemoryReservation` | No | task memory | Memory reserved for the console container |
| `consoleHideEmailLogin` / `consoleHideEmailSignup` | No | | Hide email login and signup in the UI |
| `smtpServer` | No | | Fully qualified SMTP address |
| `smtpUsername` / `smtpPassword` | No | | SMTP credentials |
| `smtpGenericSender` | No | | From address for outgoing email |
| `logType` | No | none | Log driver, for example `awslogs` |
| `logArgs` | No | | Log driver arguments |
| `agGridLicenseKey` | No | | AG Grid license key for the console |

Hiding email login in the console does not disable the API handler behind it. To turn the handler off, set `apiDisabledEmailLogin` and `apiDisabledEmailSignup` as well.

### DNS

| Key | Required | Description |
| :-- | :-- | :-- |
| `aws:region` | Yes | AWS region |
| `route53ZoneName` | Yes | Route 53 zone name |
| `route53Subdomain` | Yes | Subdomain |
| `apiLoadBalancerDnsName` / `apiLoadBalancerZoneId` | Yes | API load balancer |
| `consoleLoadBalancerDnsName` / `consoleLoadBalancerZoneId` | Yes | Console load balancer |

## Verify the installation

```bash
curl -fsS https://api.{sub}.example.com/api/status
pulumi login https://api.{sub}.example.com
pulumi whoami
```

Then open `https://app.{sub}.example.com` and create the first account.

{{< self-hosted-first-admin-note />}}

Confirm an end-to-end update works:

```bash
pulumi new aws-typescript --stack dev --yes
pulumi up --yes
pulumi destroy --yes
```

## Upgrade

{{< self-hosting-schema-v2-note />}}

```bash
pulumi login s3://<your-state-bucket>
cd pulumi-self-hosted-installers/ecs-hosted/ts/application
pulumi config set imageTag <new-image-tag>
pulumi up
```

Migrations run before the services roll. See [Upgrades](/docs/administration/self-hosting/operations/upgrades/) for staged rollouts and ordering.

## Uninstall

Destroy the projects in reverse order — `dns`, then `application`, then `infrastructure`. Aurora and S3 carry deletion protection, so remove that first if you intend to delete the data.

## Maintenance

The installer configures Aurora for replication and automated snapshots, so no routine database work is needed. For S3, consider enabling AWS Backup on the buckets the installer creates, which are named `pulumi-checkpoint-*` and `pulumi-policy-*`.

## Troubleshooting

- Migrations failing with `ALGORITHM=INPLACE is not supported` means `sql_mode` is missing `STRICT_TRANS_TABLES`. Aurora MySQL 8.0 does not set it by default.
- The API cannot start without `licenseKey`.

See [Troubleshooting](/docs/administration/self-hosting/troubleshooting/) for the full list.
