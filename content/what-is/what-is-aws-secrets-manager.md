---
title: What is AWS Secrets Manager?
meta_desc: AWS Secrets Manager stores, retrieves, and rotates credentials, API keys, and tokens. Learn how it works, pricing, use cases, and Pulumi examples.

type: what-is
page_title: "What is AWS Secrets Manager?"
---

AWS Secrets Manager is a fully managed AWS service that lets you store, retrieve, and automatically rotate sensitive credentials such as database passwords, API keys, OAuth tokens, and other application secrets. It removes hard-coded credentials from your source code and replaces them with on-demand, IAM-controlled retrieval at runtime, encrypted in transit and at rest with AWS Key Management Service (KMS).

This guide covers how AWS Secrets Manager works, what you can store in it, how much it costs, how it compares to AWS Systems Manager Parameter Store, the most common use cases, and how to provision and manage secrets as code with Pulumi.

## What is AWS Secrets Manager?

AWS Secrets Manager is a cloud-based [secrets management](/what-is/what-is-secrets-management/) service from Amazon Web Services that securely stores, retrieves, and rotates secrets such as database credentials, API keys, OAuth tokens, and TLS certificates. Applications fetch secrets at runtime through a TLS-encrypted API call instead of reading them from configuration files, environment variables, or source code.

Each secret is encrypted at rest with an AWS KMS key, accessed through fine-grained AWS Identity and Access Management (IAM) policies, and audited through AWS CloudTrail. Secrets Manager natively integrates with Amazon RDS, Amazon Aurora, Amazon Redshift, Amazon DocumentDB, and AWS Lambda, and supports custom rotation logic for third-party services.

## How AWS Secrets Manager works

At a high level, AWS Secrets Manager sits between your applications and the credentials they need:

1. **Create a secret.** An administrator or an Infrastructure as Code tool such as Pulumi creates a secret. Secrets Manager encrypts the secret value using an AWS KMS customer master key (CMK).
1. **Grant access with IAM.** IAM identity-based policies and resource-based policies on the secret itself control which principals can read, write, or rotate it.
1. **Retrieve at runtime.** Your application calls `GetSecretValue` over TLS. Secrets Manager decrypts the value with KMS and returns it to the caller.
1. **Rotate on a schedule.** An AWS Lambda function (managed by AWS for supported databases, or custom for third-party services) periodically generates a new credential, updates the target system, and stores the new version in Secrets Manager.
1. **Audit every access.** Every API call is logged to AWS CloudTrail, giving you a complete record of who read or modified which secret and when.

Each secret in Secrets Manager can hold up to **65,536 bytes (64 KB)** of encrypted secret data and supports multiple versions so you can stage new credentials before promoting them.

## Key features of AWS Secrets Manager

AWS Secrets Manager combines storage, access control, rotation, and replication into a single managed service:

1. **Encryption at rest and in transit.** Secrets are encrypted with AWS KMS using AES-256 envelope encryption and only ever travel over TLS.
1. **Automatic rotation.** Built-in rotation for Amazon RDS, Aurora, Redshift, and DocumentDB, plus custom Lambda-based rotation for any other service.
1. **Fine-grained access control.** Combine IAM identity policies, resource policies on each secret, and KMS key policies to control access per secret, per principal, and per region.
1. **Multi-region replication.** Replicate secrets to additional AWS Regions for disaster recovery and low-latency reads from globally distributed applications.
1. **Versioning and staging labels.** Each secret keeps multiple versions tagged with staging labels (`AWSCURRENT`, `AWSPREVIOUS`, `AWSPENDING`) so you can roll back or stage rotations.
1. **Native AWS service integrations.** Used directly by Amazon RDS, Aurora, Redshift, DocumentDB, AWS Lambda environment variables, and AWS CodeBuild.
1. **Auditability.** Every API call is logged to AWS CloudTrail; you can configure Amazon EventBridge rules to trigger on secret events.

## What types of secrets can you store in AWS Secrets Manager?

AWS Secrets Manager is designed for short, structured secrets up to 64 KB. Common values include:

1. **Database credentials** for Amazon RDS, Aurora, Redshift, DocumentDB, and self-managed databases such as PostgreSQL, MySQL, MariaDB, Microsoft SQL Server, and MongoDB.
1. **API keys and tokens** for third-party SaaS providers such as Stripe, Twilio, Datadog, GitHub, or Slack.
1. **OAuth client secrets and refresh tokens** used by web applications and machine-to-machine integrations.
1. **TLS private keys and certificates** for applications that need them at runtime (note: for managing public certificates AWS recommends [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)).
1. **SSH keys and passwords** used by automation scripts and CI/CD pipelines.
1. **Application configuration values** that are sensitive but don't fit other secret categories.

For other types of sensitive data, AWS recommends purpose-built services: [AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) for AWS credentials, [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) for encryption keys, and [Amazon EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html) for SSH access to EC2 instances.

## AWS Secrets Manager pricing

AWS Secrets Manager uses simple, pay-as-you-go pricing with no upfront fees or minimums:

| Item | Price | Notes |
|------|-------|-------|
| Per secret | **$0.40 per secret per month** | Prorated by the hour. Secrets marked for deletion are not billed. |
| API calls | **$0.05 per 10,000 API calls** | Applies to `GetSecretValue`, `DescribeSecret`, and other API operations. |
| AWS-managed KMS key (`aws/secretsmanager`) | **Free** | Default key, automatically created in your account. |
| Customer-managed KMS keys | Standard AWS KMS rates | Charged separately under AWS KMS pricing. |
| Free trial | **30 days per secret** | Each new secret gets a 30-day free trial before per-secret charges begin. |

Automatic rotation invokes an AWS Lambda function. Lambda invocation costs apply at the [standard Lambda rate](https://aws.amazon.com/lambda/pricing/) but are typically pennies per month for normal rotation cadences. Always check the [AWS Secrets Manager pricing page](https://aws.amazon.com/secrets-manager/pricing/) for the most current figures in your region.

## AWS Secrets Manager vs. AWS Systems Manager Parameter Store

Both services can store secret values in AWS, but they target different use cases. Use this comparison to decide which one fits your workload:

| Capability | AWS Secrets Manager | AWS Systems Manager Parameter Store |
|------------|--------------------|-------------------------------------|
| Primary purpose | Managed secrets storage and rotation | General-purpose config + secrets |
| Automatic rotation | Yes, built-in for RDS/Aurora/Redshift/DocumentDB; custom via Lambda | No native rotation |
| Encryption | Always encrypted with AWS KMS | Standard parameters are plaintext; SecureString uses KMS |
| Cross-region replication | Yes, native | No (use SSM parameter sync tooling) |
| Maximum value size | 64 KB | 4 KB (Standard), 8 KB (Advanced) |
| Cost (per secret/month) | $0.40 | Free (Standard) or $0.05 (Advanced) |
| API cost | $0.05 per 10,000 calls | Free (Standard); higher-throughput tier on Advanced |
| Best for | Database credentials, API keys, rotated tokens | Plain config values, feature flags, lightweight secrets |

A common pattern is to use Parameter Store for non-sensitive configuration and AWS Secrets Manager for credentials that require rotation or larger payloads.

## Common use cases for AWS Secrets Manager

AWS Secrets Manager is most often used to solve four concrete problems:

1. **Remove hard-coded credentials from applications.** Replace credentials embedded in source code, `.env` files, or container images with a runtime `GetSecretValue` call.
1. **Rotate database credentials automatically.** Use the built-in rotation for Amazon RDS, Aurora, Redshift, and DocumentDB to rotate passwords on a schedule with no application downtime.
1. **Securely share credentials across accounts and services.** Use resource-based policies and AWS Organizations to grant cross-account access to specific secrets without copying values around.
1. **Meet compliance requirements.** Centralized audit logging through AWS CloudTrail and encryption with customer-managed KMS keys help satisfy controls under PCI DSS, HIPAA, SOC 2, and ISO 27001.

## How to create a secret in AWS Secrets Manager

You can create secrets through the AWS Management Console, AWS CLI, AWS SDKs, AWS CloudFormation, or an Infrastructure as Code tool such as Pulumi. The CLI is the quickest way to get started.

First, install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and run `aws configure` to [set up your credentials](https://docs.aws.amazon.com/cli/latest/reference/configure/):

```bash
$ aws configure

AWS Access Key ID [None]: ********
AWS Secret Access Key [None]:  ********
Default region name [None]:  ********
Default output format [None]:  ********
```

Create a secret with `aws secretsmanager create-secret`:

```bash
$ aws secretsmanager create-secret --name MySecretName --secret-string "MySecretValue"

{
    "ARN": "arn:aws:secretsmanager:eu-central-1:111111111111:secret:MySecretName-86zArI",
    "Name": "MySecretName",
    "VersionId": "41c3c47e-4542-438c-929f-92f02d3261e4"
}
```

Verify the secret with `aws secretsmanager list-secrets`:

```bash
$ aws secretsmanager list-secrets
{
    "SecretList": [
        {
            "ARN": "arn:aws:secretsmanager:eu-central-1:111111111111:secret:MySecretName-86zArI",
            "Name": "MySecretName",
            "LastChangedDate": "2023-11-28T17:16:05.840000+00:00",
            "SecretVersionsToStages": {
                "41c3c47e-4542-438c-929f-92f02d3261e4": [
                    "AWSCURRENT"
                ]
            },
            "CreatedDate": "2023-11-28T17:16:05.791000+00:00"
        }
    ]
}
```

{{< notes type="info" >}}

Creating secrets one-off via the CLI is fine for experimentation. For production environments, manage secrets declaratively with an Infrastructure as Code tool. See the [Pulumi Secrets documentation](/docs/concepts/secrets/) and the [Managing AWS Secrets Manager with Pulumi](#managing-aws-secrets-manager-with-pulumi) section below.

{{< /notes >}}

## How to retrieve a secret from AWS Secrets Manager

Once a secret exists, your application or a CLI user can read its value with `aws secretsmanager get-secret-value`:

```bash
$ aws secretsmanager get-secret-value --secret-id MySecretName
{
    "ARN": "arn:aws:secretsmanager:eu-central-1:111111111111:secret:MySecretName-86zArI",
    "Name": "MySecretName",
    "VersionId": "41c3c47e-4542-438c-929f-92f02d3261e4",
    "SecretString": "MySecretValue",
    "VersionStages": [
        "AWSCURRENT"
    ],
    "CreatedDate": "2023-11-28T17:16:05.836000+00:00"
}
```

Applications typically call `GetSecretValue` through an AWS SDK (Boto3 for Python, AWS SDK for JavaScript, AWS SDK for Go, and so on). Cache values in memory with a short TTL to avoid hitting API throttling limits in high-traffic services.

## How to rotate secrets in AWS Secrets Manager

Automatic rotation is one of the main reasons teams choose AWS Secrets Manager. Rotation works in four steps, all orchestrated by a Lambda function:

1. **`createSecret`** — Generate a new credential and store it as the `AWSPENDING` version.
1. **`setSecret`** — Apply the new credential to the target service (for example, change the database password).
1. **`testSecret`** — Verify the new credential works by connecting to the target service.
1. **`finishSecret`** — Promote `AWSPENDING` to `AWSCURRENT` and move the previous version to `AWSPREVIOUS` for safe rollback.

For Amazon RDS, Aurora, Redshift, and DocumentDB, AWS provides ready-made rotation Lambdas. For everything else, you can author a custom Lambda or use one of the [community rotation templates](https://github.com/aws-samples/aws-secrets-manager-rotation-lambdas). Schedule rotation in days, hours, or via a cron expression — AWS Secrets Manager supports rotation as frequently as every four hours.

## AWS Secrets Manager best practices

Follow these practices to get the most value from AWS Secrets Manager while keeping costs and blast radius low:

1. **Rotate on a schedule that matches your threat model.** Quarterly rotation is a safe baseline; rotate more aggressively for high-value credentials.
1. **Apply least-privilege IAM policies.** Grant `secretsmanager:GetSecretValue` only on the specific secret ARNs each principal needs.
1. **Use customer-managed KMS keys for sensitive secrets.** This lets you control key rotation and audit decrypt calls through CloudTrail.
1. **Enable AWS CloudTrail and Amazon EventBridge alerts.** Trigger alarms on unusual `GetSecretValue` patterns or unauthorized access attempts.
1. **Cache secrets on the client.** Use the [AWS Secrets Manager caching libraries](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) to reduce API calls and stay under throttling limits.
1. **Tag secrets consistently.** Use tags such as `environment`, `owner`, and `service` for cost allocation and access control.
1. **Replicate critical secrets cross-region.** Mirror secrets your production workloads depend on to a second region for disaster recovery.
1. **Manage secret resources as code.** Define secrets and their rotation policies with Pulumi or another IaC tool so they are versioned, peer reviewed, and reproducible across environments.

## Limitations and considerations

AWS Secrets Manager is powerful, but you should plan around a few constraints:

1. **Per-secret cost adds up.** At $0.40 per secret per month, fleets of thousands of secrets can become a meaningful line item. Consolidate related credentials into a single JSON-formatted secret where it makes sense.
1. **API throttling limits.** The combined rate of `DescribeSecret` and `GetSecretValue` is capped at 10,000 transactions per second (TPS) per region. Cache aggressively in high-throughput services.
1. **64 KB secret size limit.** Each secret value is capped at 65,536 bytes, which is plenty for credentials but unsuitable for large files or certificate bundles.
1. **Rotation requires Lambda.** Any custom rotation logic runs in AWS Lambda, which means cold starts, VPC configuration, and Lambda quotas apply.
1. **AWS-centric integrations.** Native integrations are strongest within AWS. On-premises systems and other clouds require additional plumbing such as Pulumi ESC or self-managed broker services.
1. **Region scope.** Each secret is regional by default. Use replication explicitly when you need multi-region availability.

## Managing AWS Secrets Manager with Pulumi

Provisioning secrets imperatively through the CLI or console is fine for ad-hoc work, but production environments benefit from defining secrets as code. Pulumi lets you declare AWS Secrets Manager secrets, versions, rotation schedules, and IAM policies in TypeScript, Python, Go, C#, or Java — alongside the rest of your AWS infrastructure.

{{< chooser language "typescript,python,go,csharp" / >}}

{{% choosable language typescript %}}

```typescript
// View the full example code here: https://github.com/pulumi/examples/tree/master/aws-ts-secrets-manager

import * as aws from "@pulumi/aws";

const secret = new aws.secretsmanager.Secret("secret");

const secretVersion = new aws.secretsmanager.SecretVersion("secretVersion", {
    secretId: secret.id,
    secretString: "mysecret",
});

export const secretId = secret.id;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# View the full example code here: https://github.com/pulumi/examples/tree/master/aws-py-secrets-manager

import pulumi
from pulumi_aws import secretsmanager

secret = secretsmanager.Secret("secret")

secret_version = secretsmanager.SecretVersion("secret_version",
                                              secret_id=secret.id,
                                              secret_string="mysecret"
                                              )

pulumi.export("secret_id", secret.id)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// View the full example code here: https://github.com/pulumi/examples/tree/master/aws-go-secrets-manager

package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/secretsmanager"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		secret, err := secretsmanager.NewSecret(ctx, "secretcontainer", nil)
		if err != nil {
			return err
		}

		_, err = secretsmanager.NewSecretVersion(ctx, "secret", &secretsmanager.SecretVersionArgs{
			SecretId:     secret.ID(),
			SecretString: pulumi.String("mysecret"),
		})
		if err != nil {
			return err
		}

		ctx.Export("secretContainer", secret.ID())
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// View the full example code here: https://github.com/pulumi/examples/tree/master/aws-cs-secrets-manager

using Pulumi;
using Pulumi.Aws.SecretsManager;

class MyStack : Stack
{
    public MyStack()
    {
        var secret = new Secret("secret");

        var secretVersion = new SecretVersion("secretVersion", new SecretVersionArgs
        {
            SecretId = secret.Id,
            SecretString = "mysecret"
        });

        this.SecretId = secret.Id;
    }

    [Output]
    public Output<string> SecretId { get; set; }
}
```

{{% /choosable %}}

Browse the full [AWS Secrets Manager API reference](/registry/packages/aws/api-docs/secretsmanager/secret/) and the [Pulumi AWS Provider documentation](/registry/packages/aws/) for additional resources such as `SecretRotation`, `SecretPolicy`, and `SecretVersion`.

For organizations that use AWS Secrets Manager alongside other secrets backends — HashiCorp Vault, Azure Key Vault, GCP Secret Manager, or 1Password — [Pulumi ESC (Environments, Secrets, and Configurations)](/docs/pulumi-cloud/esc/) provides a unified runtime layer. The [Pulumi ESC AWS Secrets provider](/docs/pulumi-cloud/esc/providers/aws-secrets/) pulls secrets from AWS Secrets Manager into hierarchical, composable environments, and ESC's OIDC integration can dynamically generate short-lived AWS credentials on demand, so you never need to store long-lived access keys.

## Frequently asked questions

### Is AWS Secrets Manager free?

No. AWS Secrets Manager charges $0.40 per secret per month and $0.05 per 10,000 API calls. Each new secret gets a 30-day free trial. There is no perpetual free tier, but the AWS-managed KMS key (`aws/secretsmanager`) is free to use for encryption.

### What is the difference between AWS Secrets Manager and AWS KMS?

AWS KMS manages cryptographic keys used to encrypt data, while AWS Secrets Manager stores and rotates the secrets themselves (such as database passwords). Secrets Manager actually uses KMS under the hood to encrypt every secret value at rest.

### What is the difference between AWS Secrets Manager and Parameter Store?

AWS Systems Manager Parameter Store is a general-purpose configuration store with optional encrypted SecureString parameters and no native rotation. AWS Secrets Manager is purpose-built for secrets, with automatic rotation, cross-region replication, and a larger 64 KB value size. Parameter Store is free for Standard parameters; Secrets Manager is $0.40 per secret per month.

### Can AWS Secrets Manager rotate non-AWS secrets?

Yes. AWS provides built-in rotation Lambdas for Amazon RDS, Aurora, Redshift, and DocumentDB, but you can author a custom AWS Lambda rotation function for any third-party service — SaaS API keys, on-premises databases, OAuth tokens, and so on.

### Is AWS Secrets Manager compliant with SOC 2, PCI DSS, and HIPAA?

Yes. AWS Secrets Manager is in scope for SOC 1/2/3, PCI DSS, ISO 27001, FedRAMP, HIPAA BAA, and other AWS compliance programs. See the [AWS Compliance Programs page](https://aws.amazon.com/compliance/services-in-scope/) for the current list.

### How many secrets can I store in AWS Secrets Manager?

There is a soft limit of 500,000 secrets per AWS account per region. You can request an increase through AWS Service Quotas. Each secret can hold up to 65,536 bytes (64 KB) of encrypted secret data.

### How do I migrate hard-coded credentials to AWS Secrets Manager?

Create a secret with `aws secretsmanager create-secret`, update the application to fetch the value with `GetSecretValue` at startup, and remove the hard-coded value from source control. For larger migrations, define the secret with Pulumi so the change is auditable and applied consistently across environments.

## Next steps

1. **Provision your first secret as code.** Pick a language and follow the [AWS Secrets Manager examples on GitHub](https://github.com/pulumi/examples?q=secrets-manager).
1. **Adopt Pulumi ESC for multi-backend secrets.** [Pulumi ESC](/docs/pulumi-cloud/esc/) gives you one place to compose, share, and rotate secrets across AWS Secrets Manager, HashiCorp Vault, Azure Key Vault, and more.
1. **Explore related services.** Read [What is Azure Key Vault?](/what-is/what-is-azure-key-vault/), [What are Kubernetes Secrets?](/what-is/what-are-kubernetes-secrets/), and [What is secrets management?](/what-is/what-is-secrets-management/) to see how AWS Secrets Manager fits in the broader landscape.
1. **Join the community.** Have a question or want to share how your team uses AWS Secrets Manager with Pulumi? Join the conversation on [Pulumi Community Slack](https://slack.pulumi.com/).
