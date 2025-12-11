---
title_tag: "Write-only Fields | Pulumi Concepts"
meta_desc: This page provides an overview of write-only fields in Pulumi secrets handling.
title: Write-only Fields
h1: Write-only Fields
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Write-only Fields
        parent: iac-concepts-secrets
        weight: 1
    concepts:
        parent: secrets
        weight: 1
aliases:
- /docs/intro/concepts/secrets/write-only-fields/
- /docs/concepts/secrets/write-only-fields/
---

Write-only fields are resource properties that can be set during resource creation but are never returned by the cloud provider's API. This means Pulumi cannot read these values back from the cloud provider.

## Write-only arguments in Terraform

Write-only arguments are a concept that some providers inherit from their underlying Terraform providers. These providers have fields that are intentionally write-only for security reasons. For example, a database password might be set during creation but the provider will never return the actual password value in subsequent API calls.

{{%notes type="info"%}}
Pulumi supports these properties mainly for schema parity with the underlying Terraform provider. With Pulumi, sensitive data can always be stored in state as a Secret, which is the preferred paradigm when conventional fields are available.
{{%/notes%}}

## How Pulumi handles write-only fields

When Pulumi encounters a write-only field:

1. The value is used during resource creation or updates and sent to the cloud API.
2. Its initial value gets written to Pulumi state Inputs as a Secret. It will never appear in state Outputs.
3. On subsequent Read operations, the value will be set to `null`.
4. On subsequent previews or updates, Pulumi will not detect or show diffs on these fields since they are not tracked in state.

## Version control fields

Some providers gate updates to write-only fields with a write-only _version_ field. This version field is under full Pulumi lifecycle management and linked to the write-only field. In these implementations, a change to the version field will prompt Pulumi to re-apply the write-only field's value to your cloud infrastructure.

For example, the AWS SSM Parameter resource supports write-only fields for secure string values.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create an SSM Parameter with write-only fields
const testParameter = new aws.ssm.Parameter("test-param", {
    name: "/test/writeonly-parameter",
    type: aws.ssm.ParameterType.SecureString,
    description: "Test parameter with write-only fields",
    // Write-only fields
    valueWo: "write-only-secret-value",
    valueWoVersion: 1,
});
```

1. **Initial creation**: The `valueWo` field is sent to the cloud provider API and stored as a Secret in Pulumi state Inputs. The `valueWoVersion` is also stored and tracked in state.

2. **Subsequent reads**: After creation, when Pulumi reads the resource from the cloud provider:
   - The `valueWo` field will be `null` in the state Outputs (the provider doesn't return write-only values)
   - The `valueWoVersion` remains tracked in state and can be read back

3. **Updating the write-only value**: To update the `valueWo` field, you must increment the `valueWoVersion`:

   ```typescript
   const updatedParameter = new aws.ssm.Parameter("test-param", {
       name: "/test/writeonly-parameter",
       type: aws.ssm.ParameterType.SecureString,
       description: "Test parameter with write-only fields",
       valueWo: "new-write-only-secret-value",
       valueWoVersion: 2, // Increment to trigger update
   });
   ```
