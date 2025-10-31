---
title: Policy Packs
title_tag: Policy Packs | Pulumi Policy
h1: Policy Packs
meta_desc: Learn how to use Policy Packs to enforce organizational standards and best practices across your Pulumi infrastructure as code.
menu:
  insights:
    parent: insights-policy
    weight: 20
aliases:
  - /docs/insights/policy/configuration/
  - /docs/using-pulumi/crossguard/configuration/
  - /docs/guides/crossguard/configuration/
  - /docs/iac/packages-and-automation/crossguard/configuration/
  - /docs/iac/crossguard/configuration/
  - /docs/iac/using-pulumi/crossguard/configuration/
  - /docs/insights/policy/policy-as-code/configuration/
---

Policy packs are collections of rules that enforce compliance and best practices across your infrastructure. Each policy pack contains one or more policies that validate resource properties, configurations, or relationships between resources.

## Types of policy packs

### Pre-built policy packs

Pulumi provides ready-to-use policy packs for common compliance frameworks including CIS, PCI DSS, ISO 27001, and SOC 2. These packs are maintained by Pulumi and cover security, cost, and operational best practices for AWS, Azure, and Google Cloud.

[Explore pre-built policy packs →](/docs/insights/policy/policy-packs/pre-built-packs/)

### Custom policy packs

Write your own policies in TypeScript or Python to enforce organization-specific requirements. Custom policies can validate individual resources or entire stack configurations, with full control over enforcement levels and error messages.

[Learn to author custom policies →](/docs/insights/policy/policy-packs/authoring/)

## Configuring policy packs

Configuration makes policy packs flexible and reusable across your organization. You can adjust enforcement levels, set allowed values, or customize behavior without modifying policy code.

### Enforcement levels

All policies automatically support configurable enforcement levels. You can set enforcement for all policies in a pack or override individual policies:

```json
{
    "all": {
        "enforcementLevel": "advisory"
    },
    "critical-security-policy": {
         "enforcementLevel": "mandatory"
    }
}
```

As a shorthand, you can specify enforcement levels directly:

```json
{
    "all": "advisory",
    "critical-security-policy": "mandatory"
}
```

**Enforcement levels:**

- **advisory** — Issues warnings but allows deployments to proceed
- **mandatory** — Blocks deployments when violations are detected
- **disabled** — Skips policy evaluation entirely

### Custom configuration

Policy authors define configuration schemas using JSON Schema. This allows organization administrators to customize policy behavior—like setting allowed instance types or cost thresholds—without changing policy code.

**Example: Optional configuration with defaults**

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
const examplePolicy: ResourceValidationPolicy = {
    name: "example-policy-with-schema",
    description: "Example policy with configurable message.",
    configSchema: {
        properties: {
            message: {
                type: "string",
                minLength: 5,
                maxLength: 50,
            }
        },
    },
    validateResource: validateResourceOfType(aws.s3.Bucket, (_, args, reportViolation) => {
        const config = args.getConfig<{ message?: string }>();
        const message = config.message || "Using default message";
        reportViolation("Configured message: " + message);
    }),
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
def example_policy_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    config = args.get_config()
    message = config.get("message", "Using default message")
    report_violation(f"Configured message: {message}")

example_policy = ResourceValidationPolicy(
    name="example-policy-with-schema",
    description="Example policy with configurable message.",
    config_schema=PolicyConfigSchema(
        properties={
            "message": {
                "type": "string",
                "minLength": 5,
                "maxLength": 50,
            },
        }
    ),
    validate=example_policy_validator,
)
```

{{% /choosable %}}

{{< /chooser >}}

**Example: Required configuration**

To require configuration values, add them to the `required` list:

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
configSchema: {
    properties: {
        message: {
            type: "string",
            minLength: 5,
            maxLength: 50,
        }
    },
    required: ["message"],
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
config_schema=PolicyConfigSchema(
    properties={
        "message": {
            "type": "string",
            "minLength": 5,
            "maxLength": 50,
        },
    },
    required=["message"]
)
```

{{% /choosable %}}

{{< /chooser >}}

## Running with configuration

### Local execution

Store configuration in a JSON file and pass it to the Pulumi CLI:

**config.json:**

```json
{
    "all": "mandatory",
    "example-policy-with-schema": {
        "message": "Resources must follow naming standards"
    }
}
```

**Run with configuration:**

```bash
pulumi preview --policy-pack <path-to-policy-pack> --policy-pack-config config.json
```

### Pulumi Cloud configuration

Once a policy pack is published, organization administrators can configure it through the Pulumi Cloud console or CLI.

**Using the console:**

1. Navigate to your Policy Group
2. Click **Add Policy Pack**
3. Select the policy pack
4. Fill in the configuration form (automatically validated against the schema)
5. Save the configuration

**Using the CLI:**

Validate configuration before enabling:

```bash
pulumi policy validate-config <org>/<pack-name> <version> --config config.json
```

Enable with configuration:

```bash
pulumi policy enable <org>/<pack-name> <version> --config config.json
```

Or for a specific policy group:

```bash
pulumi policy enable <org>/<pack-name> <version> --config config.json --policy-group <group-name>
```

## Next steps

- [Browse pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/)
- [Write custom policy packs](/docs/insights/policy/policy-packs/authoring/)
- [Configure policy groups](/docs/insights/policy/policy-groups/)
- [View policy findings](/docs/insights/policy/policy-findings/)
