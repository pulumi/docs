---
title: "FDA 21 CFR Part 11 Evidence Patterns with Pulumi"
date: 2026-07-16
draft: false
meta_desc: "Map FDA 21 CFR Part 11 expectations to Pulumi workflows for electronic records, audit trails, policy checks, and reviewable infrastructure evidence."
meta_image: meta.png
feature_image: feature.png
authors:
    - pablo-seibelt
tags:
    - compliance
    - neo
    - life-sciences
social:
    twitter: |
        21 CFR Part 11 work needs evidence, not vague promises.

        Map Pulumi workflows to audit trails, policy checks, and reviewable infrastructure changes.
    linkedin: |
        Regulated infrastructure teams need clear evidence for electronic records, signatures, audit trails, and change review.

        This guide maps FDA 21 CFR Part 11 expectations to practical Pulumi workflows without claiming automatic compliance.
    bluesky: |
        21 CFR Part 11 needs evidence.

        Map Pulumi workflows to audit trails, policy checks, and reviewable infra changes.
---

Life sciences organizations operate in a highly regulated environment where the integrity and traceability of data are paramount. The Food and Drug Administration (FDA) 21 CFR Part 11 regulation sets the standard for electronic records and electronic signatures, ensuring they are trustworthy, reliable, and equivalent to paper records.

As infrastructure moves to the cloud, the systems managing that infrastructure must also meet these rigorous standards. Teams in regulated industries need clear documentation on how Pulumi can support an FDA 21 CFR Part 11 compliance program.

In this post, we will explore how Pulumi features map to Part 11 controls and how you can use Infrastructure as Code (IaC) to support a compliance evidence workflow for your regulated workloads.

This post provides compliance documentation support for organizations meeting FDA 21 CFR Part 11 requirements. Note that while Pulumi tools support compliance efforts, they do not provide automated certification or guarantee regulatory approval. In this post, you will build a compliance evidence workflow for regulated workloads.

<!--more-->

## Understanding 21 CFR Part 11 in the Cloud

FDA 21 CFR Part 11 applies to records in electronic form that are created, modified, maintained, archived, retrieved, or transmitted under any records requirements set forth in agency regulations. For infrastructure, this means the configurations, deployment logs, and state history that define your regulated environments are considered electronic records.

The regulation focuses on several key areas:
1. **Validation**: Ensuring systems are accurate, reliable, and perform consistently.
2. **Audit Trails**: Computer-generated, time-stamped records of all actions.
3. **Record Protection**: Ensuring records are retained and can be retrieved throughout their retention period.
4. **Authority Checks**: Ensuring only authorized individuals can access the system and perform actions.

## Mapping Pulumi to Part 11 Controls

Pulumi provides a suite of features that can help address these requirements, allowing you to treat your infrastructure with the same level of rigor as your application code.

### 1. System Validation (11.10(a))

Validation is the process of demonstrating that a system does what it is intended to do. With Pulumi, validation starts before a single resource is deployed.

* **[Pulumi Policies](/docs/insights/policy/)**: You can enforce compliance rules across your entire organization. For example, you can require that all S3 buckets have versioning and encryption enabled, or that only approved instance types are used.
* **Testing**: Pulumi supports unit, property, and integration testing in familiar languages like TypeScript. This allows you to verify your infrastructure logic before deployment.

### 2. Audit Trails (11.10(e))

Part 11 requires a computer-generated, time-stamped audit trail that records the date and time of operator entries and actions that create, modify, or delete electronic records.

[Pulumi Cloud](/product/pulumi-cloud/) automatically maintains a comprehensive audit trail for infrastructure changes:

* **Audit Logs**: Every action taken in the Pulumi Cloud console or via the CLI is recorded, including who performed the action, what the action was, and when it occurred.
* **State History**: Every `pulumi up` creates a new checkpoint in your stack's history. You can see exactly what changed in each deployment, providing a clear lineage of your infrastructure.

Part 11 auditability also depends on the systems you deploy, not only the platform you use to deploy them. Use Pulumi to provision cloud-native audit trails for regulated workloads, such as AWS CloudTrail delivered to encrypted, versioned S3 buckets, integrated with CloudWatch Logs for monitoring and alerting. AWS maps Part 11 controls to capabilities such as CloudTrail log file validation, CloudTrail encryption, CloudWatch Logs integration, and S3 data event logging. Pulumi lets you define those controls as code and review every change before it reaches production.

### 3. Record Protection and Retrieval (11.10(b) and (c))

Electronic records must be protected to enable their accurate and ready retrieval throughout the records retention period.

* **State Management**: Pulumi Cloud stores your state files securely, with built-in versioning and history.
* **Human-Readable Exports**: You can export your stack state at any time using `pulumi stack export`, providing a JSON representation of your infrastructure that is both human-readable and suitable for long-term archiving.

### 4. Authority Checks (11.10(g))

Access to the system must be limited to authorized individuals.

* **Role-Based Access Control (RBAC)**: Pulumi Cloud allows you to define granular permissions for users and teams, ensuring that only authorized personnel can view or modify specific stacks.
* **Single Sign-On (SSO)**: Integration with identity providers like Okta or Azure AD ensures that your organization's existing security policies and multi-factor authentication (MFA) are applied to Pulumi.

Apply the same model to the cloud systems that hold regulated records. Pulumi can configure IAM roles, groups, permission boundaries, and service-specific access controls from a central identity provider (IdP) model so that access to audit logs, storage buckets, and application environments follows the same reviewable least-privilege baseline.

## Configuring Audit Trails for Regulated Workloads

The following AWS example shows the kind of infrastructure baseline Pulumi can manage for systems that need audit trails. It creates a versioned and encrypted S3 bucket for audit records, a CloudWatch Log Group for near real-time monitoring, and a multi-region CloudTrail trail with log file validation enabled.

```typescript
import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

const current = aws.getCallerIdentity({});
const auditBucket = new aws.s3.BucketV2("part11-audit-records");

const auditBucketVersioning = new aws.s3.BucketVersioningV2("part11-audit-records-versioning", {
    bucket: auditBucket.id,
    versioningConfiguration: {
        status: "Enabled",
    },
});

const auditBucketEncryption = new aws.s3.BucketServerSideEncryptionConfigurationV2("part11-audit-records-encryption", {
    bucket: auditBucket.id,
    rules: [{
        applyServerSideEncryptionByDefault: {
            sseAlgorithm: "aws:kms",
        },
    }],
});

const auditLogGroup = new aws.cloudwatch.LogGroup("part11-cloudtrail-events", {
    retentionInDays: 365,
});

const auditBucketPolicy = new aws.s3.BucketPolicy("part11-audit-records-policy", {
    bucket: auditBucket.id,
    policy: pulumi.all([auditBucket.arn, current]).apply(([bucketArn, identity]) => JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Sid: "AWSCloudTrailAclCheck",
            Effect: "Allow",
            Principal: {
                Service: "cloudtrail.amazonaws.com",
            },
            Action: "s3:GetBucketAcl",
            Resource: bucketArn,
        }, {
            Sid: "AWSCloudTrailWrite",
            Effect: "Allow",
            Principal: {
                Service: "cloudtrail.amazonaws.com",
            },
            Action: "s3:PutObject",
            Resource: `${bucketArn}/AWSLogs/${identity.accountId}/*`,
            Condition: {
                StringEquals: {
                    "s3:x-amz-acl": "bucket-owner-full-control",
                },
            },
        }],
    })),
});

const cloudTrailRole = new aws.iam.Role("part11-cloudtrail-role", {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({
        Service: "cloudtrail.amazonaws.com",
    }),
});

const cloudTrailRolePolicy = new aws.iam.RolePolicy("part11-cloudtrail-log-delivery", {
    role: cloudTrailRole.id,
    policy: pulumi.interpolate`{
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": ["logs:CreateLogStream", "logs:PutLogEvents"],
            "Resource": "${auditLogGroup.arn}:*"
        }]
    }`,
});

const trail = new aws.cloudtrail.Trail("part11-audit-trail", {
    s3BucketName: auditBucket.id,
    includeGlobalServiceEvents: true,
    isMultiRegionTrail: true,
    enableLogFileValidation: true,
    cloudWatchLogsGroupArn: pulumi.interpolate`${auditLogGroup.arn}:*`,
    cloudWatchLogsRoleArn: cloudTrailRole.arn,
}, {
    dependsOn: [auditBucketVersioning, auditBucketEncryption, auditBucketPolicy, cloudTrailRolePolicy],
});
```

This does not make an environment compliant by itself. It gives the validation team a concrete, reviewable definition of where audit records are stored, how they are protected, and which services generate them.

## Neo-Assisted Compliance and Documentation

[Pulumi Neo](/product/neo/), our AI-powered infrastructure agent, can assist in maintaining and documenting your compliance posture. While Neo does not replace the need for human oversight, it can significantly accelerate the documentation process.

### Generating Validation Documentation

You can use Neo to generate summaries of your infrastructure state and policy compliance for your validation reports. For example, you might use a prompt like this:

> "Neo, generate a report of all resources in the 'production' stack. Include their encryption status and any active Pulumi policy violations. Format this as a table suitable for a system validation document."

### Continuous Compliance and Drift Detection

Maintaining compliance is not a one-time event. Pulumi's scheduled drift detection can automatically check your environment for changes made outside of Pulumi. When drift is detected, it can trigger an alert or a review workflow, ensuring your "as-built" infrastructure matches your "as-validated" code.

## Enforcing Audit Trail Controls with Pulumi Policies

Once you define an approved audit-trail baseline, use Pulumi Policies to prevent drift from that baseline. For example, the following policy requires CloudTrail resources to use multi-region logging, log file validation, and CloudWatch Logs integration.

```typescript
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";
import { Trail } from "@pulumi/aws/cloudtrail";

new PolicyPack("part11-audit-trail-controls", {
    policies: [{
        name: "cloudtrail-audit-controls-required",
        description: "CloudTrail trails must be multi-region, validated, and integrated with CloudWatch Logs.",
        enforcementLevel: "mandatory",
        validateResource: validateResourceOfType(Trail, (trail, args, reportViolation) => {
            if (!trail.isMultiRegionTrail) {
                reportViolation("CloudTrail must be configured as a multi-region trail.");
            }
            if (!trail.enableLogFileValidation) {
                reportViolation("CloudTrail log file validation must be enabled.");
            }
            if (!trail.cloudWatchLogsGroupArn || !trail.cloudWatchLogsRoleArn) {
                reportViolation("CloudTrail must stream events to CloudWatch Logs.");
            }
        }),
    }],
});
```

You can combine this with policies for S3 versioning, S3 encryption, S3 public access blocks, and IAM access patterns. That moves Part 11 support from a manual checklist to a deployment gate: non-compliant infrastructure fails before it is created.

## Conclusion

Pulumi provides tools that can help build and manage infrastructure in alignment with the high standards of FDA 21 CFR Part 11. By using Infrastructure as Code, Pulumi Policies, IdP-backed access controls, cloud-native audit trails, and the audit capabilities of Pulumi Cloud, life sciences organizations can configure regulated systems with clearer evidence and stronger deployment guardrails.

*Disclaimer: This post provides implementation guidance and illustrates how Pulumi features can support compliance efforts. It does not constitute legal advice or a formal compliance attestation for FDA 21 CFR Part 11. Organizations are responsible for their own regulatory validation and compliance.*
