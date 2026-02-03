---
title_tag: "Policy Metadata"
meta_desc: Policies include metadata that describes their purpose, behavior, and how violations are handled within Pulumi.
title: Policy Metadata
h1: Policy Metadata
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    name: Policy Metadata
    parent: policy-packs
    weight: 30
aliases:
  - /docs/insights/policy/policy-as-code/policy-metadata/
  - /docs/insights/policy/metadata.md
---

Each policy includes metadata that defines its identity, purpose, and behavior. Metadata provides important context for how a policy is displayed, enforced, and remediated. This information helps both authors and users understand what the policy does, how severe its violations are, and how to resolve them.

The table below describes all supported metadata fields and their usage:

| Field | Required | Description |
|-------|-----------|-------------|
| `name` | Yes | Unique identifier for the policy within the policy pack. |
| `description` | Yes | Short summary of what the policy checks or enforces. |
| `enforcementLevel` | No | Defines how the policy behaves on violation. Options: `advisory` (warn only), `mandatory` (block deployment), `remediate` (auto-fix violations), or `disabled` (turn off policy). |
| `severity` | No | Indicates the seriousness of violations. Valid values: `low`, `medium`, `high`, `critical`. |
| `displayName` | No | Human-readable name for the policy (used for display instead of `name`). |
| `remediationSteps` | No | Guidance for how to fix a violation or bring a resource into compliance. |
| `url` | No | Link to external documentation, references, or remediation guides. |
| `tags` | No | Array of labels or categories for grouping and filtering policies. |
| `framework` | No | Associates the policy with a compliance framework or standard. |
| `framework.name` | Yes* | Name of the compliance framework (e.g., `"PCI-DSS"`, `"HIPAA"`, `"SOC 2"`). |
| `framework.version` | Yes* | Framework version (e.g., `"3.2.1"`, `"2022"`). |
| `framework.reference` | Yes* | Specific control or requirement reference within the framework. |
| `framework.specification` | Yes* | Detailed description of the related compliance requirement. |
| `configSchema` | No | Schema defining user-configurable parameters for the policy. For more information on configSchema, see [authoring](/docs/insights/policy/authoring/)|
| `configSchema.properties` | Yes* | Object describing available configuration options and their types. |
| `configSchema.required` | No | Array of property names that must be supplied when configuring the policy. |

\* Required if the parent field is defined.
