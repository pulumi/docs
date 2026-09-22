---
title_tag: "Policy fields reference | Pulumi Policies"
meta_desc: Reference for the fields you set on policies and policy packs in TypeScript, Python, and OPA, such as severity and remediation steps.
title: Policy fields
h1: Policy fields
menu:
  discovery-governance:
    name: Policy fields
    parent: dg-reference
    weight: 40
aliases:
  - /docs/insights/policy/policy-as-code/policy-metadata/
  - /docs/insights/policy/metadata.md
  - /docs/insights/policy/policy-packs/metadata/
  - /docs/discovery-governance/policy/policy-packs/metadata/
---

Every policy in a policy pack carries a set of fields that describe it: its name, what it checks, how strictly it's enforced, how severe a violation is, and how to fix one. You set these fields in the policy pack's source code, next to the validation logic. When you run `pulumi policy publish`, they're published with the pack, and Pulumi Cloud uses them when it displays policies and their violations.

Where you write the fields depends on the language:

- **TypeScript**: properties on each policy object in the `policies` array passed to `new PolicyPack()`.
- **Python**: keyword arguments to `ResourceValidationPolicy` or `StackValidationPolicy`. Python uses snake_case names, such as `remediation_steps`.
- **OPA**: `# METADATA` annotations on each Rego rule. OPA supports a smaller set of fields. See [OPA](#opa).

A second, smaller set of fields describes the [policy pack as a whole](#policy-pack-fields).

## Example

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

new PolicyPack("aws-security", {
    enforcementLevel: "advisory",
    policies: [{
        name: "rds-storage-encrypted",
        description: "RDS instances must have storage encryption enabled.",
        displayName: "Encrypt RDS storage",
        enforcementLevel: "mandatory",
        severity: "high",
        tags: ["security", "rds"],
        remediationSteps: "Set storageEncrypted to true on the RDS instance.",
        url: "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html",
        framework: {
            name: "Internal security baseline",
            version: "2026.1",
            reference: "DATA-01",
            specification: "Databases must encrypt data at rest.",
        },
        validateResource: validateResourceOfType(aws.rds.Instance, (instance, args, reportViolation) => {
            if (!instance.storageEncrypted) {
                reportViolation("RDS instances must have storage encryption enabled.");
            }
        }),
    }],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
from pulumi_policy import (
    EnforcementLevel,
    PolicyComplianceFramework,
    PolicyPack,
    ResourceValidationPolicy,
    Severity,
)


def rds_storage_encrypted(args, report_violation):
    if args.resource_type == "aws:rds/instance:Instance" and not args.props.get("storageEncrypted"):
        report_violation("RDS instances must have storage encryption enabled.")


PolicyPack(
    name="aws-security",
    enforcement_level=EnforcementLevel.ADVISORY,
    policies=[
        ResourceValidationPolicy(
            name="rds-storage-encrypted",
            description="RDS instances must have storage encryption enabled.",
            display_name="Encrypt RDS storage",
            enforcement_level=EnforcementLevel.MANDATORY,
            severity=Severity.HIGH,
            tags=["security", "rds"],
            remediation_steps="Set storageEncrypted to true on the RDS instance.",
            url="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html",
            framework=PolicyComplianceFramework(
                name="Internal security baseline",
                version="2026.1",
                reference="DATA-01",
                specification="Databases must encrypt data at rest.",
            ),
            validate=rds_storage_encrypted,
        ),
    ],
)
```

{{% /choosable %}}

{{< /chooser >}}

## Policy fields

| TypeScript | Python | Required | Description |
|------------|--------|----------|-------------|
| `name` | `name` | Yes | Identifier for the policy. Must be unique within the policy pack. |
| `description` | `description` | Yes | Short summary of what the policy checks and why. |
| `enforcementLevel` | `enforcement_level` | No | What happens on a violation: `advisory` (warn only), `mandatory` (block the update), `remediate` (fix the resource automatically), or `disabled` (turn the policy off). Overrides the pack's default enforcement level. In Python, use the `EnforcementLevel` enum. Organization-managed `mandatory` enforcement is available with Pro and Enterprise. The `remediate` level is available with [Enterprise](/pricing/#policy-enforcement-modes). |
| `severity` | `severity` | No | How serious a violation is: `low`, `medium`, `high`, or `critical`. In Python, use the `Severity` enum. |
| `displayName` | `display_name` | No | Human-readable name, shown instead of `name`. |
| `remediationSteps` | `remediation_steps` | No | Guidance for fixing a violation by hand. This is unrelated to the `remediate` enforcement level, which fixes resources automatically. |
| `url` | `url` | No | Link to more information about the policy. |
| `tags` | `tags` | No | Labels for grouping and filtering policies. |
| `framework` | `framework` | No | The compliance framework the policy belongs to. See [Framework fields](#framework-fields). |
| `configSchema` | `config_schema` | No | Schema for the policy's configurable parameters. See [Configuration schema fields](#configuration-schema-fields). |

### Framework fields

| TypeScript | Python | Description |
|------------|--------|-------------|
| `name` | `name` | Name of the compliance framework, for example `"PCI DSS"`, `"HIPAA"`, or `"SOC 2"`. |
| `version` | `version` | Framework version, for example `"4.0"`. |
| `reference` | `reference` | The specific control or requirement within the framework. |
| `specification` | `specification` | Description of the related compliance requirement. |

In TypeScript, all four fields are required when you set `framework`. In Python, `PolicyComplianceFramework` accepts each one as optional.

### Configuration schema fields

| TypeScript | Python | Required | Description |
|------------|--------|----------|-------------|
| `properties` | `properties` | Yes | The configuration options and their JSON Schema types. |
| `required` | `required` | No | Names of properties that must be supplied when the policy is configured. |

For how to read configuration values inside a policy, see [Configuring policy packs](/docs/discovery-governance/guides/write-a-policy-pack/#configuring-policy-packs).

## Policy pack fields

These fields describe the pack as a whole. In TypeScript, set them on the arguments to `new PolicyPack()`. In Python, pass them as keyword arguments to `PolicyPack`.

| TypeScript | Python | Description |
|------------|--------|-------------|
| `policies` | `policies` | The policies in the pack. Required. |
| `enforcementLevel` | `enforcement_level` | Default enforcement level for every policy in the pack. Defaults to `advisory`. Individual policies can override it. |
| `description` | `description` | Brief description of the pack. Overrides the description in [`PulumiPolicy.yaml`](/docs/discovery-governance/reference/policy-project-file/). |
| `displayName` | `display_name` | Human-readable name for the pack. |
| `readme` | `readme` | README text for the pack. |
| `provider` | `provider` | The cloud provider or platform the pack applies to, such as AWS or Azure. |
| `tags` | `tags` | Labels for the pack. |
| `repository` | `repository` | URL of the repository where the pack is defined. |

## OPA

OPA policy packs set fields with [OPA metadata annotations](https://www.openpolicyagent.org/docs/latest/policy-reference/#annotations), in a `# METADATA` comment block directly above each rule:

```rego
# METADATA
# title: Require RDS storage encryption
# description: RDS instances must have storage encryption enabled.
# custom:
#   message: Set storageEncrypted to true.
deny_unencrypted_rds[msg] {
    input.type == "aws:rds/instance:Instance"
    not input.storageEncrypted
    msg := sprintf("RDS instance '%s' must have storage encryption enabled", [input.__name])
}
```

The OPA analyzer reads these annotations and maps them to policy fields:

| OPA | Policy field | Notes |
|-----|--------------|-------|
| Rule name | `name` | For example, `deny_unencrypted_rds`. |
| Rule name prefix | `enforcementLevel` | `deny` or `violation` for mandatory rules, `warn` for advisory rules. |
| `title` | `displayName` | Defaults to the rule name. |
| `description` | `description` | |
| `custom.message` | Violation message | Shown with each violation of the rule. |
| `config-schema.json` | `configSchema` | A file next to your Rego files. See [Configuring policy packs](/docs/discovery-governance/guides/write-a-policy-pack/#configuring-policy-packs). |

A `title` annotation with package scope sets the pack's display name. OPA policies don't support `severity`, `remediationSteps`, `url`, `tags`, or `framework`.
