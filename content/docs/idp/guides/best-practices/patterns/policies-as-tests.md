---
title: "IDP Pattern: Policies as tests"
linktitle: "Policies as tests"
menu:
  idp:
    parent: idp-patterns
    weight: 60
aliases:
  - /docs/idp/best-practices/patterns/policies-as-tests/
meta_desc: Implement governance and compliance requirements using Pulumi policies that run as automated tests
h1: "IDP Pattern: Policies as tests"
description: <p>Implement governance and compliance requirements using Pulumi policies that run as automated tests.</p>
---

## Description

This pattern involves writing Pulumi policies that enforce organizational standards, security requirements, and compliance rules by running them as automated tests during deployment. Policies act as guardrails that prevent non-compliant infrastructure from being deployed.

## When to use this pattern

- **Compliance requirements**: When you need to enforce regulatory or organizational standards
- **Security governance**: When you want to prevent security misconfigurations automatically
- **Standardization**: When you need consistent infrastructure patterns across teams
- **Automated enforcement**: When manual reviews are too slow or error-prone

## When NOT to use this pattern

- **Rapid prototyping**: When you need to quickly test ideas without governance overhead
- **Unique requirements**: When applications legitimately need to deviate from standard policies
- **Small teams**: When policy maintenance overhead exceeds the benefits

## How to use this pattern

Policies are written as code and can be integrated into CI/CD pipelines to automatically validate infrastructure before deployment.

### Example

Organization creates policies for common security requirements:

```typescript
// policies/security-policies.ts
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";
import { aws } from "@pulumi/aws";

new PolicyPack("security-policies", {
  policies: [
    {
      name: "s3-bucket-encryption",
      description: "S3 buckets must have encryption enabled",
      enforcementLevel: "mandatory",
      validateResource: validateResourceOfType(aws.s3.Bucket, (bucket, args, reportViolation) => {
        if (!bucket.serverSideEncryptionConfiguration) {
          reportViolation("S3 bucket must have encryption enabled");
        }
      }),
    },
    {
      name: "rds-backup-retention",
      description: "RDS instances must have backup retention >= 7 days",
      enforcementLevel: "mandatory",
      validateResource: validateResourceOfType(aws.rds.Instance, (instance, args, reportViolation) => {
        if (!instance.backupRetentionPeriod || instance.backupRetentionPeriod < 7) {
          reportViolation("RDS instance must have backup retention >= 7 days");
        }
      }),
    },
  ],
});
```

Teams run policies as part of their deployment process:

```bash
# In CI/CD pipeline
pulumi preview --policy-pack ./policies/security-policies
pulumi up --policy-pack ./policies/security-policies
```

This ensures that all infrastructure deployments automatically comply with organizational security and governance standards.

## Related patterns

- [IDP Pattern: Validating Component Inputs using Policy functions](/docs/idp/guides/best-practices/patterns/validating-component-inputs-using-policy-functions) - For input validation at the component level
- [IDP Pattern: Cost control using Components, Policies, and constrained inputs](/docs/idp/guides/best-practices/patterns/cost-control-using-components-policies-constrained-inputs) - For cost governance
- [IDP Pattern: Security Updates using Components](/docs/idp/guides/best-practices/patterns/security-updates-using-components) - For maintaining secure infrastructure
