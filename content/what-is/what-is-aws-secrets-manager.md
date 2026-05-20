---
title: What is AWS Secrets Manager?
meta_desc: "AWS Secrets Manager is a managed service for storing, rotating, and retrieving secrets. Learn its rotation model, IAM integration, pricing, and how Pulumi ESC fits."
meta_image: /images/what-is/what-is-aws-secrets-manager-meta.png
type: what-is
page_title: "What is AWS Secrets Manager?"
authors: ["torian-crane"]
---

**AWS Secrets Manager is a fully managed Amazon Web Services product that stores, rotates, and retrieves credentials, API keys, and other secrets used by applications running on AWS or elsewhere.** Secrets are encrypted at rest with AWS KMS, accessed via IAM-controlled APIs, audited through CloudTrail, and can be rotated automatically by an AWS Lambda function on a schedule you define.

Secrets Manager is the default secrets store for AWS-centric organizations because it shares the same identity, encryption, audit, and Region model as the rest of AWS. A workload running on EC2, ECS, EKS, or Lambda authenticates with its IAM role and reads a secret with one API call; the operator manages access through IAM policies and resource policies; everything that happened is in CloudTrail. [Pulumi ESC](/product/esc/) integrates with Secrets Manager as a [secrets provider](/docs/pulumi-cloud/esc/providers/aws-secrets/), pulling AWS-managed secrets into Pulumi programs, CI pipelines, and applications through a single audited interface.

In this article, we'll cover the key questions about AWS Secrets Manager:

* Why do teams use AWS Secrets Manager?
* What are the core features of AWS Secrets Manager?
* How does automatic rotation work?
* How does AWS Secrets Manager compare to Parameter Store?
* How does AWS Secrets Manager compare to other vaults?
* How does pricing work?
* How does AWS Secrets Manager handle replication and disaster recovery?
* What are the regional and service limits?
* How does Pulumi ESC integrate with AWS Secrets Manager?
* Frequently asked questions about AWS Secrets Manager

## Why do teams use AWS Secrets Manager?

Three reasons that AWS-centric workloads usually pick Secrets Manager over a self-hosted alternative.

### Native IAM and CloudTrail integration

Access to a secret is controlled by IAM policies (identity-based) and resource policies (secret-based) — the same model that controls every other AWS resource. Every read, write, and rotation is logged to CloudTrail with the IAM principal that performed it.

### Automatic rotation for native services

Secrets Manager natively supports automatic rotation for Amazon RDS (Aurora MySQL, Aurora PostgreSQL, MySQL, PostgreSQL, Oracle, SQL Server, MariaDB), Amazon Redshift, and Amazon DocumentDB. For other secret types, you provide a Lambda function that implements the rotation contract.

### Replication across Regions

A single secret can be replicated to multiple AWS Regions for disaster recovery and low-latency reads. Replica secrets are encrypted in the target Region's KMS keys; failover is handled by promoting a replica to primary.

## What are the core features of AWS Secrets Manager?

| Feature | What it does |
|---|---|
| **Encryption at rest** | AES-256 with a customer-managed or AWS-managed KMS key per secret |
| **Encryption in transit** | TLS for all API calls |
| **Access control** | IAM identity-based policies, resource-based policies on the secret, KMS key policies |
| **Versioning** | Multiple versions per secret with stage labels (AWSCURRENT, AWSPENDING, AWSPREVIOUS) |
| **Automatic rotation** | Built-in support for RDS, Redshift, DocumentDB; custom rotation via Lambda |
| **Cross-Region replication** | Replicate a secret to one or more secondary Regions |
| **Audit logging** | CloudTrail records every API call; integration with EventBridge for event-driven workflows |
| **Resource sharing** | Cross-account access via resource policies |
| **VPC endpoint** | Private connectivity via interface VPC endpoints (AWS PrivateLink) |

A secret in Secrets Manager is a versioned key/value document (typically JSON), encrypted with a KMS key, addressable by name or ARN.

## How does automatic rotation work?

Rotation in Secrets Manager follows a four-step state machine driven by an AWS Lambda function:

1. **createSecret.** The Lambda generates a new credential (e.g. a new database password) and stores it as a new version with the `AWSPENDING` label.
1. **setSecret.** The Lambda updates the downstream service (e.g. runs `ALTER USER` against RDS) to accept the new credential.
1. **testSecret.** The Lambda verifies the new credential works by connecting with it.
1. **finishSecret.** The Lambda swaps the version labels: the new version becomes `AWSCURRENT`, the old one becomes `AWSPREVIOUS`.

For RDS, Redshift, and DocumentDB, AWS supplies the rotation Lambda. For other secrets, you write one — patterns are well-documented and many open source templates exist. Rotation can be scheduled (every N days) or triggered on demand.

Multi-user rotation (alternating between two database users) is supported and recommended for zero-downtime rotations: while one user's password is rotated, the other handles application traffic.

## How does AWS Secrets Manager compare to Parameter Store?

Both store values in AWS, but they target different use cases.

| Aspect | Secrets Manager | Systems Manager Parameter Store |
|---|---|---|
| Primary use | Secrets that need rotation | Configuration values (with or without encryption) |
| Built-in rotation | Yes | No |
| Cross-Region replication | Yes (native) | No (Advanced parameters via custom tooling) |
| Encryption | Always (KMS-backed) | Optional (SecureString uses KMS) |
| Versioning | Multiple labeled versions | History up to 100 versions per parameter |
| Pricing | Per secret/month + API calls | Standard parameters: free. Advanced: per parameter + API calls |
| Free tier | No (always paid) | Standard parameters are free up to limits |
| Common use | Database passwords, API keys, OAuth client secrets | Application config, feature flags, non-rotating tokens |

A common pattern is to use Parameter Store SecureString for general configuration and reserve Secrets Manager for credentials that genuinely need rotation. Many teams use both.

## How does AWS Secrets Manager compare to other vaults?

| Capability | AWS Secrets Manager | [HashiCorp Vault](/what-is/what-is-hashicorp-vault/) | [Azure Key Vault](/what-is/what-is-azure-key-vault/) | [Google Cloud Secret Manager](/what-is/what-is-google-cloud-secret-manager/) |
|---|---|---|---|---|
| Hosting | Fully managed (AWS) | Self-hosted or HCP managed | Fully managed (Azure) | Fully managed (GCP) |
| Cloud scope | AWS-native | Multi-cloud, hybrid, on-prem | Azure-native | GCP-native |
| Built-in rotation | RDS, Redshift, DocumentDB; Lambda for others | Dynamic secrets engines | Certificates (built-in); secrets via Functions | Not built-in |
| Encryption-as-a-service | Use AWS KMS separately | Yes (transit engine) | Use Key Vault keys separately | Use Cloud KMS separately |
| Compliance | SOC 1/2/3, PCI DSS, HIPAA, FedRAMP High, IRAP, others | Vault Enterprise FIPS 140-2 | FIPS 140-2 (Premium / Managed HSM) | FIPS 140-2 (Cloud HSM via CMEK) |
| Best fit | AWS-centric workloads | Multi-cloud, dynamic-secrets-heavy | Azure-centric workloads | GCP-centric workloads |

For workloads that run mostly inside AWS, Secrets Manager is almost always the right default. For multi-cloud or hybrid deployments, organizations frequently pair it with HashiCorp Vault and use [Pulumi ESC](/product/esc/) to compose both under a single interface.

## How does pricing work?

AWS Secrets Manager pricing has two components:

1. **Per secret, per month.** Each secret incurs a flat charge regardless of size; in most AWS Regions this is around $0.40 per secret per month (check the [AWS Secrets Manager pricing page](https://aws.amazon.com/secrets-manager/pricing/) for current rates in your Region).
1. **Per 10,000 API calls.** A small per-API-call charge applies for retrievals and other operations.

Replica secrets are billed at the same per-secret rate in each Region they're replicated to. The first 30 days of any new secret are typically free as part of a free trial. KMS key usage is billed separately under KMS pricing.

The pricing model means cost scales with the *number* of secrets more than with read volume. For applications that read the same secret thousands of times per day, the cost-effective pattern is to cache the secret in memory and refresh on rotation.

## How does AWS Secrets Manager handle replication and disaster recovery?

A secret has a primary Region and can be replicated to any number of secondary Regions. Properties of the replication model:

* **Same name, different Region.** Replicas share the secret name; applications in each Region read the local copy.
* **Per-Region KMS keys.** Each replica is encrypted with a KMS key in the local Region; the source key is never copied.
* **Eventual consistency.** Updates to the primary propagate to replicas within seconds under normal conditions.
* **Promotion on failure.** A replica can be promoted to primary if the source Region is unavailable. The original primary then becomes a replica when it returns.

For DR purposes, replicate every secret your DR workload depends on, and include the promotion step in your runbook. For pure low-latency reads, replicate to the same Regions where your application runs.

## What are the regional and service limits?

A few service quotas to plan around:

| Limit | Value |
|---|---|
| Maximum secret value size | 64 KB |
| Default secrets per Region per account | 500,000 (soft limit; can be raised) |
| Default API rate (GetSecretValue, DescribeSecret) | 10,000 RPS per Region |
| Default API rate (other operations) | Lower; see the AWS Secrets Manager quotas docs |
| Maximum versions per secret | 100 |
| Rotation function timeout | Inherits Lambda timeout (max 15 minutes) |

Hitting the API rate limit returns `ThrottlingException`. The standard mitigation is client-side caching (the AWS Secrets Manager Java, Python, Node.js, .NET, and Go caching libraries implement this for you).

## How does Pulumi ESC integrate with AWS Secrets Manager?

[Pulumi ESC](/product/esc/) treats AWS Secrets Manager as one of many secret sources. The [AWS Secrets provider](/docs/pulumi-cloud/esc/providers/aws-secrets/) lets an ESC environment read secrets from Secrets Manager and broker them to Pulumi programs, CI jobs, and applications.

Concrete patterns:

* **Dynamic AWS credentials via OIDC.** ESC mints short-lived AWS credentials at the moment a consumer opens the environment, removing the need for long-lived access keys anywhere. See the [aws-login provider](/docs/pulumi-cloud/esc/providers/aws-login/).
* **Compose with other vaults.** A single ESC environment can pull a database credential from AWS Secrets Manager, an OAuth client secret from HashiCorp Vault, and an OIDC client secret from Azure Key Vault.
* **Broker secrets to non-AWS consumers.** A workload running outside AWS can still read Secrets Manager secrets via an ESC environment, without having to manage IAM credentials directly.
* **Audit trail unification.** ESC logs every environment open with identity and timestamp; CloudTrail still records the underlying Secrets Manager API call. The two together produce a complete chain of custody.

The [aws.secretsmanager Pulumi resource](/registry/packages/aws/api-docs/secretsmanager/secret/) lets you define and manage AWS Secrets Manager resources as code in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about AWS Secrets Manager

### How much does AWS Secrets Manager cost?

Per the [AWS Secrets Manager pricing page](https://aws.amazon.com/secrets-manager/pricing/), pricing in most Regions is roughly $0.40 per secret per month plus a small per-API-call fee, with a 30-day free trial for new secrets. Cross-Region replicas are billed at the per-secret rate in each Region. KMS usage is billed separately.

### Does AWS Secrets Manager rotate secrets automatically?

Yes for natively supported services (Amazon RDS engines, Amazon Redshift, Amazon DocumentDB) using AWS-supplied rotation Lambdas. For other secret types, you provide a Lambda implementing the four-step rotation contract (createSecret, setSecret, testSecret, finishSecret). Rotation can be scheduled or triggered on demand.

### How is AWS Secrets Manager different from Parameter Store?

Secrets Manager always encrypts, supports automatic rotation, and replicates across Regions. Parameter Store is cheaper, supports both plain and encrypted (SecureString) parameters, has no built-in rotation, and is a better fit for general configuration. Many teams use both.

### Can I use AWS Secrets Manager outside AWS?

Yes. The API is reachable from anywhere the caller has AWS credentials. In practice, workloads running outside AWS often use AWS IAM Roles Anywhere or OIDC federation to obtain temporary credentials, then call Secrets Manager.

### Is AWS Secrets Manager HIPAA-eligible?

Yes. AWS Secrets Manager is a HIPAA-eligible service under the AWS Business Associate Addendum. It's also in scope for SOC 1, SOC 2, SOC 3, PCI DSS, ISO 27001, FedRAMP High, and several other AWS compliance programs.

### How do I share a secret across AWS accounts?

Attach a resource-based policy to the secret that grants access to the target account's IAM principals, and grant `kms:Decrypt` on the underlying KMS key. The target account can then call `GetSecretValue` directly. For programmatic creation, see the [Pulumi AWS provider's SecretPolicy resource](/registry/packages/aws/api-docs/secretsmanager/secretpolicy/).

### What happens if I exceed the API rate limit?

You get `ThrottlingException` and the standard AWS SDK retry-with-backoff applies. For applications that read secrets frequently, use the AWS Secrets Manager client-side caching libraries (Java, Python, Node.js, .NET, Go) which cache secrets in memory and refresh on rotation.

### How does AWS Secrets Manager work in a VPC?

Create an interface VPC endpoint for `com.amazonaws.<region>.secretsmanager`. API calls then stay on the AWS network and never traverse the public internet. The endpoint can have its own security group and endpoint policy.

### Can I migrate secrets from AWS Secrets Manager to HashiCorp Vault?

Yes, though it's a one-time export-and-import. List secrets via the AWS API, fetch each value, write into Vault's KV v2 engine, and update your applications to read from Vault. [Pulumi ESC](/product/esc/) often makes migration unnecessary by sitting above both and brokering whichever vault each secret happens to live in.

### How does AWS Secrets Manager integrate with EKS?

Use the AWS Secrets and Configuration Provider for the Kubernetes Secrets Store CSI Driver. Workloads in EKS mount secrets as files in the pod or sync them into Kubernetes Secret resources. Authentication uses IAM roles for service accounts (IRSA) or EKS Pod Identity.

## Learn more

Pulumi makes AWS Secrets Manager part of a coherent secrets program: [Pulumi ESC](/docs/pulumi-cloud/esc/) brokers Secrets Manager values to Pulumi programs, CI jobs, and applications under a single audited interface, and the [Pulumi AWS provider](/registry/packages/aws/) lets you declare every Secrets Manager resource as code in TypeScript, Python, Go, C#, Java, or YAML.

Related reading:

* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is HashiCorp Vault?](/what-is/what-is-hashicorp-vault/)
* [What is Azure Key Vault?](/what-is/what-is-azure-key-vault/)
* [What is Google Cloud Secret Manager?](/what-is/what-is-google-cloud-secret-manager/)
* [What is Cloud Security?](/what-is/what-is-cloud-security/)
* [What is SOC 2?](/what-is/what-is-soc-2/)
