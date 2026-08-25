---
title: Write your own
title_tag: "Write your own policy packs"
h1: Write your own policy packs
meta_desc: Learn how to write custom policy packs to enforce organization-specific compliance and security controls.
menu:
  insights:
    name: Write your own
    parent: policy-packs
    weight: 20
aliases:
  - /docs/insights/policy/authoring/
  - /docs/insights/policy/policy-packs/authoring/
  - /docs/insights/policy/best-practices/
  - /docs/iac/guides/testing/property-testing/
  - /docs/guides/testing/property-testing/
  - /docs/using-pulumi/testing/property-testing/
  - /docs/iac/concepts/testing/property-testing/
---

If Pulumi's pre-built policy packs don't meet your requirements, you can write custom policy packs. Custom policies let you enforce any compliance, security, or operational rule.

Policies can be written in TypeScript/JavaScript (Node.js), Python, or OPA (Rego) and can be applied to Pulumi stacks written in any language. Learn more about [language support for policies](/docs/insights/policy/#languages).

### Creating a Policy Pack with Neo

This guide walks you through creating a policy pack manually, but [Neo](/product/neo/) can help streamline the process.  

Neo can generate policy pack content tailored to your preferred programming language and cloud providers, allowing you to quickly build policies that meet your specific requirements while reducing errors. When paired with the [GitHub App](/docs/integrations/version-control/github-app/), Neo can even open pull requests directly in your repository.  

Here are some example prompts to inspire your workflow:

> "Create a boilerplate TypeScript policy pack at `<GitHub Repository>`"  
> "Create a policy to enforce encryption of S3 buckets"  
> "Create a policy that requires environment tagging on all Google Cloud resources"

## Prerequisites

Before authoring your first policy pack, ensure you have:

- [Pulumi CLI installed](/docs/install/).
- For TypeScript/JavaScript policies: [Node.js installed](https://nodejs.org/en/download/).
- For Python policies: [Python installed](https://python.org/downloads/).
- For OPA policies: Pulumi CLI v3.227.0+ automatically installs the OPA analyzer plugin on first use. No manual installation is needed.
- (Optional) Access to Pulumi Cloud if you want to publish and centrally manage policy packs. Not required for local policy pack usage with open source Pulumi.
- An understanding of [Policy as Code core concepts](/docs/insights/policy/).

The runtime you choose here also becomes a requirement for everyone who runs Pulumi against a stack your pack governs. See [runtime requirements](/docs/insights/policy/policy-packs/#runtime-requirements).

## Creating a policy pack

Create your first policy pack:

{{< chooser language "typescript,python,opa" >}}

{{% choosable language typescript %}}

1. Create a directory for your policy pack and navigate to it.

    ```sh
    $ mkdir policypack && cd policypack
    ```

1. Create a new TypeScript project:

    ```sh
    $ pulumi policy new aws-typescript
    ```

1. Replace the generated policy in `index.ts` with this example, which demonstrates a clearer pattern for organizational policy enforcement:

    Each policy must have:
    - A unique name, description, and validation function
    - A validation function (this example uses `validateResourceOfType` to run only for AWS RDS instance resources)
    - An enforcement level set at the policy pack level (applies to all policies) or per policy (overrides the pack level)

    > For more information on all available fields, see [policy metadata](/docs/insights/policy/policy-as-code/policy-metadata/).

    ```typescript
    import * as aws from "@pulumi/aws";
    import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

    // Create a new policy pack.
    new PolicyPack("policy-pack-typescript", {
        // Specify the policies in the policy pack.
        policies: [{
            // The name for the policy must be unique within the pack.
            name: "rds-storage-encryption",

            // The description should document what the policy does and why it exists.
            description: "Requires RDS instances to have storage encryption enabled, unless tagged as non-production data.",

            // The enforcement level can be "advisory", "mandatory", "remediate", or "disabled". An "advisory"
            // enforcement level simply prints a warning for users, a "mandatory" policy will block an update
            // from proceeding, "remediate" fixes the violation automatically, and "disabled" disables the
            // policy from running.
            enforcementLevel: "mandatory",

            // The validateResourceOfType function allows you to filter resources. In this case, the rule only
            // applies to RDS instances and reports a violation when storage encryption is not enabled.
            validateResource: validateResourceOfType(aws.rds.Instance, (instance, args, reportViolation) => {
                // Exempt instances explicitly tagged as non-production data.
                if (instance.tags?.["data-classification"] === "non-production") {
                    return;
                }
                if (!instance.storageEncrypted) {
                    reportViolation(
                        "RDS instance must have storage encryption enabled " +
                        "(or be tagged 'data-classification=non-production').");
                }
            }),
        }],
    });
    ```

{{% /choosable %}}
{{% choosable language python %}}

1. Create a directory for your policy pack and navigate to it.

    ```sh
    $ mkdir policypack && cd policypack
    ```

1. Create a new Python project:

    ```sh
    $ pulumi policy new aws-python
    ```

    > **Virtual environment configuration**: Python policy packs use a virtual environment specified in `PulumiPolicy.yaml`. The default name is `venv`. If you use a different name (like `.venv`), update `PulumiPolicy.yaml`. See the [project file reference](/docs/insights/policy/policy-packs/project-file/) for all available settings.
    >
    > ```yaml
    > runtime:
    > name: python
    > options:
    >     virtualenv: .venv
    > ```

    > **Using .gitignore to manage policy pack size**: Create a `.gitignore` file alongside `PulumiPolicy.yaml` to exclude unnecessary files from the published policy pack archive (`.tgz`). Add patterns to ignore Python bytecode files, virtual environments, and other development artifacts:
    >
    > ```
    > *.pyc
    > __pycache__/
    > venv/
    > .venv/
    > ```
    >
    > This keeps your published policy pack size small and ensures only the necessary policy code is distributed.

1. Replace the generated policy in `__main__.py` with this example, which demonstrates a clearer pattern for organizational policy enforcement:

    Each policy must have:
    - A unique name, description, and validation function
    - An enforcement level set at the policy pack level (applies to all policies) or per policy (overrides the pack level)

    ```python
    from pulumi_policy import (
        EnforcementLevel,
        PolicyPack,
        ReportViolation,
        ResourceValidationArgs,
        ResourceValidationPolicy,
    )

    # The validation function is called before each resource is created or updated.
    # In this case, the rule only applies to RDS instances and reports a violation
    # when storage encryption is not enabled.
    def rds_storage_encryption_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
        if args.resource_type == "aws:rds/instance:Instance":
            # Exempt instances explicitly tagged as non-production data.
            tags = args.props.get("tags", {}) or {}
            if tags.get("data-classification") == "non-production":
                return
            if not args.props.get("storageEncrypted"):
                report_violation(
                    "RDS instance must have storage encryption enabled "
                    "(or be tagged 'data-classification=non-production').")

    rds_storage_encryption = ResourceValidationPolicy(
        # The name for the policy must be unique within the pack.
        name="rds-storage-encryption",

        # The description should document what the policy does and why it exists.
        description="Requires RDS instances to have storage encryption enabled, unless tagged as non-production data.",

        # The enforcement level can be ADVISORY, MANDATORY, REMEDIATE, or DISABLED. An ADVISORY
        # enforcement level simply prints a warning for users, a MANDATORY policy will block an update
        # from proceeding, REMEDIATE fixes the violation automatically, and DISABLED disables the
        # policy from running.
        enforcement_level=EnforcementLevel.MANDATORY,

        # The validation function, defined above.
        validate=rds_storage_encryption_validator,
    )

    # Create a new policy pack.
    PolicyPack(
        name="policy-pack-python",
        # Specify the policies in the policy pack.
        policies=[
            rds_storage_encryption,
        ],
    )
    ```

{{% /choosable %}}

<a id="opa"></a>

{{% choosable language opa %}}

1. Create a directory for your policy pack and navigate to it.

    ```sh
    $ mkdir policypack && cd policypack
    ```

1. Create a new OPA project:

    ```sh
    $ pulumi policy new aws-opa
    ```

    This creates a `PulumiPolicy.yaml` (with `runtime: opa`) and a starter `policy.rego` file. Templates are available for AWS (`aws-opa`), Azure (`azure-opa`), GCP (`gcp-opa`), and Kubernetes (`kubernetes-opa`).

1. Replace the generated policy in `policy.rego` with this example, which demonstrates metadata annotations and multiple rules:

    Each resource is passed as `input` with metadata fields like `__name` (logical name), `__urn`, and `type`, plus all resource properties at the top level.

    Use [OPA metadata annotations](https://www.openpolicyagent.org/docs/latest/policy-reference/#annotations) (`# METADATA` comment blocks) to provide a `title`, `description`, and remediation guidance (`custom.message`) for each rule. The analyzer extracts these annotations and reports them to Pulumi:

    ```rego
    package aws

    # METADATA
    # title: Require RDS Storage Encryption
    # description: RDS instances must have storage encryption enabled, unless tagged as non-production data.
    # custom:
    #   message: Set storageEncrypted to true, or tag the instance data-classification=non-production.
    deny_unencrypted_rds[msg] {
        input.type == "aws:rds/instance:Instance"
        not input.storageEncrypted
        not non_production
        msg := sprintf("RDS instance '%s' must have storage encryption enabled", [input.__name])
    }

    # METADATA
    # title: Prohibit Public RDS Instances
    # description: RDS instances must not be publicly accessible.
    # custom:
    #   message: Set publiclyAccessible to false.
    deny_public_rds[msg] {
        input.type == "aws:rds/instance:Instance"
        input.publiclyAccessible
        msg := sprintf("RDS instance '%s' must not be publicly accessible", [input.__name])
    }

    # An instance is exempt from the encryption rule when tagged as non-production data.
    non_production {
        input.tags["data-classification"] == "non-production"
    }
    ```

    Each rule must use a recognized name prefix that determines its enforcement level: `deny` (or `violation`) for mandatory rules that block deployments, and `warn` for advisory rules. Rules can include a descriptive suffix (e.g., `deny_public_buckets`). An empty result set means the resource is compliant.

{{% /choosable %}}

{{< /chooser >}}

You can find more example policy packs in the [Pulumi examples repository](https://github.com/pulumi/examples/tree/master/policy-packs).

## Testing your policies

Write unit tests to verify your policies work correctly before publishing.

{{< chooser language "typescript,python,opa" >}}

{{% choosable language typescript %}}

Here's a simple test example using Mocha and assert:

```typescript
{{< example-program-snippet path="unit-test-policy" language="typescript" file="test/index.spec.ts" from="6" to="14" >}}
```

For a complete example including test helpers and setup, see the [unit test policy example on GitHub](https://github.com/pulumi/docs/tree/master/static/programs/unit-test-policy-typescript).

{{% /choosable %}}

{{% choosable language python %}}

Here's a simple test example using pytest:

```python
{{< example-program-snippet path="unit-test-policy" language="python" file="test_policy.py" from="18" to="34" >}}
```

For a complete example including additional test cases, see the [unit test policy example on GitHub](https://github.com/pulumi/docs/tree/master/static/programs/unit-test-policy-python).

{{% /choosable %}}

{{% choosable language opa %}}

OPA policies can be tested using the standard `opa test` command from the [OPA CLI](https://www.openpolicyagent.org/docs/latest/#running-opa). Create a test file (e.g., `s3_security_test.rego`) alongside your policy:

```rego
package aws

test_deny_unencrypted_rds {
    count(deny_unencrypted_rds) > 0 with input as {
        "type": "aws:rds/instance:Instance",
        "__name": "my-db",
        "storageEncrypted": false
    }
}

test_allow_encrypted_rds {
    count(deny_unencrypted_rds) == 0 with input as {
        "type": "aws:rds/instance:Instance",
        "__name": "my-db",
        "storageEncrypted": true
    }
}

test_allow_non_production_rds {
    count(deny_unencrypted_rds) == 0 with input as {
        "type": "aws:rds/instance:Instance",
        "__name": "my-db",
        "storageEncrypted": false,
        "tags": {"data-classification": "non-production"}
    }
}
```

Run the tests:

```sh
$ opa test .
```

{{% /choosable %}}

{{< /chooser >}}

<a id="resource-validation"></a>
<a id="stack-validation"></a>

## Resource validation vs stack validation

Pulumi policies validate at two scopes:

### Resource validation policies

Resource validation policies run during `pulumi preview` or `pulumi up`, examining each resource before creation or update. These policies execute **before** the desired state is sent to the engine, which means they can block non-compliant resources during both preview and update operations.

Use resource validation policies when you need to:

- Enforce rules on specific resource types (e.g., "S3 buckets must have encryption enabled")
- Validate resource properties before deployment
- Block individual non-compliant resources

### Stack validation policies

Stack validation policies run after resource registration completes. These policies execute **after** resources have been created or updated, and only run during `pulumi up` (not during `pulumi preview`). They examine relationships between resources and enforce stack-wide rules.

Use stack validation policies when you need to:

- Validate relationships between resources (e.g., "databases must be in private subnets")
- Enforce stack-wide rules (e.g., "stack must not exceed 50 resources")
- Examine the complete resource graph

Most policies are resource validation policies. Stack validation policies are useful for more complex scenarios that require understanding the full context of your infrastructure.

The following example limits the number of S3 buckets in a stack:

{{< chooser language "typescript,python,opa" >}}

{{% choosable language typescript %}}

In TypeScript, use the `validateStack` callback to access all resources in the stack:

```typescript
import { PolicyPack } from "@pulumi/policy";

new PolicyPack("stack-policies", {
    policies: [{
        name: "maximum-s3-bucket-count",
        description: "Limits the number of S3 buckets per stack.",
        enforcementLevel: "mandatory",
        validateStack: (args, reportViolation) => {
            const buckets = args.resources.filter(
                r => r.type === "aws:s3/bucket:Bucket"
            );
            if (buckets.length > 3) {
                reportViolation(
                    `Stack has ${buckets.length} S3 buckets, maximum allowed is 3.`);
            }
        },
    }],
});
```

{{% /choosable %}}

{{% choosable language python %}}

In Python, use `StackValidationPolicy` to access all resources in the stack:

```python
from pulumi_policy import EnforcementLevel, PolicyPack, StackValidationPolicy

def max_bucket_count(args, report_violation):
    buckets = [r for r in args.resources if r.resource_type == "aws:s3/bucket:Bucket"]
    if len(buckets) > 3:
        report_violation(
            f"Stack has {len(buckets)} S3 buckets, maximum allowed is 3.")

PolicyPack(
    "stack-policies",
    policies=[
        StackValidationPolicy(
            name="maximum-s3-bucket-count",
            description="Limits the number of S3 buckets per stack.",
            enforcement_level=EnforcementLevel.MANDATORY,
            validate=max_bucket_count,
        ),
    ],
)
```

{{% /choosable %}}

{{% choosable language opa %}}

In OPA, the rule name prefix determines the validation scope. Use `stack_deny` or `stack_warn` prefixes for stack-level rules. These rules receive all resources in the stack via `input.resources`:

```rego
package aws

# METADATA
# title: Maximum S3 Bucket Count
# description: Limits the number of S3 buckets per stack.
stack_deny_too_many_buckets[msg] {
    buckets := [r | r := input.resources[_]; r.type == "aws:s3/bucket:Bucket"]
    n := count(buckets)
    n > 3
    msg := sprintf("Stack has %d S3 buckets, maximum allowed is 3", [n])
}
```

{{% /choosable %}}

{{< /chooser >}}

### Using stack tags in policies

Stack validation policies can access tags assigned to the stack via `args.stackTags` (TypeScript) or `args.stack_tags` (Python). This lets you enforce tagging standards, like requiring every stack to declare an environment or owning team, as a governance gate.

The following example requires `env` and `team` tags on every stack. Because `args.stackTags` only contains tags that existed before the current update, the policy also checks for [`StackTag`](/registry/packages/pulumiservice/api-docs/stacktag/) resources in the stack so it passes on the first deployment when tags are created declaratively.

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
import { PolicyPack } from "@pulumi/policy";

const requiredTags = ["env", "team"];

new PolicyPack("stack-tag-policies", {
    policies: [{
        name: "require-stack-tags",
        description: "Requires 'env' and 'team' tags on every stack.",
        enforcementLevel: "mandatory",
        validateStack: (args, reportViolation) => {
            // Collect tag names set via StackTag resources in this deployment.
            const resourceTagNames = args.resources
                .filter(r => r.type === "pulumiservice:index:StackTag")
                .map(r => r.props.name as string);

            for (const tag of requiredTags) {
                const inStackTags = args.stackTags.has(tag);
                const inResources = resourceTagNames.includes(tag);
                if (!inStackTags && !inResources) {
                    reportViolation(`Missing required stack tag: '${tag}'.`);
                }
            }
        },
    }],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi_policy import EnforcementLevel, PolicyPack, StackValidationPolicy

REQUIRED_TAGS = ["env", "team"]

def require_stack_tags(args, report_violation):
    # Collect tag names set via StackTag resources in this deployment.
    resource_tag_names = [
        r.props.get("name")
        for r in args.resources
        if r.resource_type == "pulumiservice:index:StackTag"
    ]

    for tag in REQUIRED_TAGS:
        in_stack_tags = tag in args.stack_tags
        in_resources = tag in resource_tag_names
        if not in_stack_tags and not in_resources:
            report_violation(f"Missing required stack tag: '{tag}'.")

PolicyPack(
    "stack-tag-policies",
    policies=[
        StackValidationPolicy(
            name="require-stack-tags",
            description="Requires 'env' and 'team' tags on every stack.",
            enforcement_level=EnforcementLevel.MANDATORY,
            validate=require_stack_tags,
        ),
    ],
)
```

{{% /choosable %}}

{{< /chooser >}}

{{% notes type="info" %}}
Stack tags are available on both `StackValidationArgs` and `ResourceValidationArgs`, so resource-level policies can also make decisions based on stack metadata.

You can assign tags to a stack using the CLI ([`pulumi stack tag set`](/docs/iac/cli/commands/pulumi_stack_tag_set/)), the [`pulumi:tags` config](/docs/iac/concepts/config/#pulumitags) in your `Pulumi.yaml` or `Pulumi.<stack>.yaml` file, the [`StackTag`](/registry/packages/pulumiservice/api-docs/stacktag/) resource from the [Pulumi Cloud provider](/registry/packages/pulumiservice/), the Pulumi Cloud console, or the [Stack Tags REST API](/docs/reference/cloud-rest-api/stack-tags/). To learn how to apply policy packs to groups of stacks, see [policy groups](/docs/insights/policy/policy-groups/).
{{% /notes %}}

{{% notes type="info" %}}
Stack tags are not currently accessible in OPA policies. OPA stack-level policies can validate the full set of resources using `input.resources` (see [Creating a policy pack](#opa) for rule prefix conventions), but they cannot read stack tag metadata. Use TypeScript or Python policies if you need to enforce stack tag requirements.
{{% /notes %}}

## Remediating policy violations

A `remediate` enforcement level goes a step further than `mandatory`: instead of only reporting a violation, the policy inspects the resource's properties, fixes the problem, and returns the corrected properties. The engine substitutes the remediated state for the state the Pulumi program originally produced, so the deployment proceeds with compliant resources rather than being blocked or merely flagged.

Remediation is only available to resource validation policies. Stack validation policies examine relationships across the whole resource graph after registration completes, by which point there is no single resource left to substitute a fix into, so a stack policy set to `remediate` is treated as `mandatory` instead.

The following example remediates, rather than validates, the RDS storage encryption policy shown earlier: instead of blocking an unencrypted instance, it turns on encryption automatically.

{{< chooser language "typescript,python,opa" >}}

{{% choosable language typescript %}}

Use `remediateResource`, built with the `remediateResourceOfType` helper, in place of `validateResource`:

```typescript
import * as aws from "@pulumi/aws";
import { PolicyPack, remediateResourceOfType } from "@pulumi/policy";

new PolicyPack("policy-pack-typescript", {
    policies: [{
        name: "rds-storage-encryption",
        description: "Requires RDS instances to have storage encryption enabled, unless tagged as non-production data.",
        enforcementLevel: "remediate",
        remediateResource: remediateResourceOfType(aws.rds.Instance, (instance, args) => {
            // Exempt instances explicitly tagged as non-production data.
            if (instance.tags?.["data-classification"] === "non-production") {
                return;
            }
            if (!instance.storageEncrypted) {
                instance.storageEncrypted = true;
                return instance;
            }
        }),
    }],
});
```

If a policy needs to both validate and remediate, `validateRemediateResourceOfType` builds a matched pair of `validateResource` and `remediateResource` callbacks from a single validation function.

{{% /choosable %}}
{{% choosable language python %}}

Pass a `remediate` callback in place of `validate` when constructing the `ResourceValidationPolicy`. A policy must define one or the other (or use `validate_remediate` to derive both from a single function); it cannot omit both:

```python
from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ResourceValidationPolicy,
)

def rds_storage_encryption_remediation(args):
    if args.resource_type != "aws:rds/instance:Instance":
        return None

    # Exempt instances explicitly tagged as non-production data.
    if args.props.get("tags", {}).get("data-classification") == "non-production":
        return None

    if not args.props.get("storageEncrypted"):
        args.props["storageEncrypted"] = True
        return args.props

    return None

rds_storage_encryption = ResourceValidationPolicy(
    name="rds-storage-encryption",
    description="Requires RDS instances to have storage encryption enabled, unless tagged as non-production data.",
    enforcement_level=EnforcementLevel.REMEDIATE,
    remediate=rds_storage_encryption_remediation,
)

PolicyPack(
    name="policy-pack-python",
    policies=[
        rds_storage_encryption,
    ],
)
```

{{% /choosable %}}
{{% choosable language opa %}}

OPA/Rego policies do not support remediation. The OPA analyzer's `Remediate` method always returns an empty response, so an OPA policy pack set to `remediate` reports violations but never fixes them. Use TypeScript or Python if you need a policy to remediate rather than just validate.

{{% /choosable %}}

{{< /chooser >}}

A few behaviors are specific to remediation:

- If a resource still triggers a violation after remediation runs, the reported level is downgraded from `remediate` to `mandatory`, and the deployment is blocked rather than silently allowed through with an unresolved problem.
- When more than one policy pack applies to a resource, their remediations run sequentially in the order the packs were loaded, and each remediation sees the resource state as modified by the ones that ran before it, so a later remediation can build on an earlier one.
- A policy whose enforcement level is `remediate` but which does not implement a remediation function is reported as not implementing remediation, so a resource going through it is neither fixed nor blocked.
- The `remediationSteps` metadata field (see [policy metadata](/docs/insights/policy/policy-packs/metadata/)) is unrelated to automatic remediation: the field is manual guidance shown to a user for policies that only validate, describing how to fix a violation by hand.

## Writing policies for dynamic providers

[Dynamic providers](/docs/iac/concepts/providers/dynamic-providers/) allow you to create custom resource types directly in your Pulumi programs. When writing policies for dynamic providers, you need to account for a key constraint: **all dynamic resources share the same resource type** (`pulumi-nodejs:dynamic:Resource` for TypeScript/JavaScript or `pulumi-python:dynamic:Resource` for Python).

Since you cannot rely on the resource type alone to identify which dynamic provider a resource uses, you must inspect the resource's properties to differentiate between different dynamic provider implementations.

### Example: Validating a specific dynamic provider

This example shows how to write a policy that validates resources from a specific dynamic provider by checking for a unique property:

{{< chooser language "typescript,python,opa" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import { PolicyPack, ResourceValidationPolicy } from "@pulumi/policy";

new PolicyPack("dynamic-provider-policies", {
    policies: [{
        name: "environment-name-validation",
        description: "Validates that environment dynamic resources use the correct name.",
        enforcementLevel: "mandatory",
        validateResource: (args, reportViolation) => {
            // All dynamic resources in TypeScript/JavaScript have the type "pulumi-nodejs:dynamic:Resource".
            // To identify a specific dynamic provider, check for unique properties.
            if (args.type === "pulumi-nodejs:dynamic:Resource" && args.props.environmentName !== undefined) {
                const envName = args.props.environmentName;
                if (envName !== "myTestEnv") {
                    reportViolation(
                        `Environment name must be 'myTestEnv'. Current value: '${envName}'`);
                }
            }
        },
    }],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

def env_dynprov_check(args: ResourceValidationArgs, report_violation: ReportViolation):
    # All dynamic resources in Python have the type "pulumi-python:dynamic:Resource"
    # To identify a specific dynamic provider, check for unique properties
    # In this case, we look for resources with an "environment_name" property
    if args.resource_type == "pulumi-python:dynamic:Resource" and "environment_name" in args.props:
        environment_name = args.props["environment_name"]
        if environment_name != "myTestEnv":
            report_violation(
                f"Environment name must be 'myTestEnv'. Current value: '{environment_name}'")

dyn_prov_policy = ResourceValidationPolicy(
    name="environment-name-validation",
    description="Validates that environment dynamic resources use the correct name.",
    enforcement_level=EnforcementLevel.MANDATORY,
    validate=env_dynprov_check,
)

PolicyPack(
    name="dynamic-provider-policies",
    policies=[
        dyn_prov_policy,
    ],
)
```

{{% /choosable %}}

{{% choosable language opa %}}

OPA policies can validate dynamic resources using the same `input.type` field. Dynamic resources use `pulumi-nodejs:dynamic:Resource` (TypeScript/JavaScript) or `pulumi-python:dynamic:Resource` (Python) as their resource type:

```rego
package dynamic

# METADATA
# title: Environment Name Validation
# description: Dynamic environment resources must use the correct name.
# custom:
#   message: Set the environmentName property to 'myTestEnv'.
# This rule only fires for dynamic resources that have an environmentName
# property. Other dynamic resources are silently skipped.
deny_environment_name[msg] {
    input.type == "pulumi-nodejs:dynamic:Resource"
    input.environmentName
    input.environmentName != "myTestEnv"
    msg := sprintf("Environment name must be 'myTestEnv'. Current value: '%s'",
                   [input.environmentName])
}
```

{{% /choosable %}}

{{< /chooser >}}

### Best practices for dynamic provider policies

When writing policies for dynamic providers:

1. **Identify unique properties**: Determine which properties uniquely identify the dynamic provider you want to validate. In the example above, the `environment_name` (or `environmentName`) property indicates this is an environment resource.

1. **Be specific with property checks**: Since all dynamic resources share the same type, check for specific property names or combinations that distinguish your dynamic provider from others.

1. **Handle missing properties gracefully**: Use property existence checks (like `"environment_name" in args.props`) before accessing property values to avoid errors when the policy runs against other dynamic providers.

1. **Document your assumptions**: Clearly document which properties your policy uses to identify dynamic providers so that changes to the dynamic provider implementation don't inadvertently break policy enforcement.

## Inspecting resource options

Resource validation callbacks receive an `args.opts` object of type `PolicyResourceOptions`. It mirrors the [resource options](/docs/iac/concepts/options/) set on the resource under validation, letting policies make decisions based on how a resource is configured rather than only its properties. The available fields are:

- `protect` — whether the resource is protected from deletion.
- `ignoreChanges` (`ignore_changes` in Python) — properties whose changes the engine ignores.
- `deleteBeforeReplace` (`delete_before_replace`) — whether the resource is deleted before its replacement is created.
- `aliases` — additional URNs aliased to the resource.
- `customTimeouts` (`custom_timeouts`) — custom create, update, and delete timeouts.
- `additionalSecretOutputs` (`additional_secret_outputs`) — outputs always treated as secrets.
- `parent` — the [URN](/docs/iac/concepts/resources/names/#urns) of the resource's [parent](/docs/iac/concepts/options/parent/). For a resource created directly at the stack root rather than as a child of another resource or component, this is the URN of the root stack resource (type `pulumi:pulumi:Stack`).

### Example: Enforcing a resource's parent

The `parent` option is useful for enforcing that certain resources are only created as children of the component that is supposed to manage them, rather than loose at the stack root or under the wrong parent. Because `parent` is the parent's URN, you can extract the parent's type token from it: a URN has the form `urn:pulumi:{stack}::{project}::{parentType}${resourceType}::{name}`, so the type is the third `::`-delimited segment, and the resource's own type is the token after the last `$`.

The following example requires that every `aws:rds/instance:Instance` is a child of a `my:components:Database` component:

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

const requiredParentType = "my:components:Database";

new PolicyPack("parent-policies", {
    policies: [{
        name: "rds-instance-parent",
        description: "Requires RDS instances to be managed by a Database component.",
        enforcementLevel: "mandatory",
        validateResource: validateResourceOfType(aws.rds.Instance, (instance, args, reportViolation) => {
            // args.opts.parent is the parent's URN; for a resource at the stack root it is the root stack's URN (type pulumi:pulumi:Stack).
            const parentUrn = args.opts.parent;
            const parentType = parentUrn?.split("::")[2]?.split("$").pop();
            if (parentType !== requiredParentType) {
                reportViolation(
                    `RDS instances must be a child of a '${requiredParentType}' component.`);
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
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

REQUIRED_PARENT_TYPE = "my:components:Database"

def rds_instance_parent(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "aws:rds/instance:Instance":
        # args.opts.parent is the parent's URN; for a resource at the stack root it is the root stack's URN (type pulumi:pulumi:Stack).
        parent_urn = args.opts.parent
        parent_type = parent_urn.split("::")[2].split("$")[-1] if parent_urn else None
        if parent_type != REQUIRED_PARENT_TYPE:
            report_violation(
                f"RDS instances must be a child of a '{REQUIRED_PARENT_TYPE}' component.")

PolicyPack(
    "parent-policies",
    policies=[
        ResourceValidationPolicy(
            name="rds-instance-parent",
            description="Requires RDS instances to be managed by a Database component.",
            enforcement_level=EnforcementLevel.MANDATORY,
            validate=rds_instance_parent,
        ),
    ],
)
```

{{% /choosable %}}

{{< /chooser >}}

{{% notes type="info" %}}
`args.opts` is available on `ResourceValidationArgs` (resource validation policies), not on `StackValidationArgs`. To reason about parent-child relationships across the full resource graph, use a [stack validation policy](#stack-validation-policies) and inspect `args.resources`. See [resource options](/docs/iac/concepts/options/) for what each option means on the resource side.
{{% /notes %}}

## Running policies locally

Test your policy pack locally before publishing.

{{< chooser language "typescript,python,opa" >}}

{{% choosable language typescript %}}

1. Use the `--policy-pack` flag to specify your policy pack directory:

    If you need a test program, create one with `pulumi new aws-typescript` and replace the generated code with a compliant (encrypted) RDS instance:

    ```typescript
    import * as aws from "@pulumi/aws";

    const db = new aws.rds.Instance("my-db", {
        engine: "postgres",
        instanceClass: "db.t3.micro",
        allocatedStorage: 20,
        username: "admin",
        manageMasterUserPassword: true,
        skipFinalSnapshot: true,
        storageEncrypted: true,
    });
    ```

    > For AWS examples, ensure you have [AWS credentials configured](/registry/packages/aws/installation-configuration/) and set your region with `pulumi config set aws:region <region>`.

1. In the Pulumi program's directory, run:

    ```sh
    $ pulumi preview --policy-pack <path-to-policy-pack-directory>
    ```

    If the stack is compliant, the output shows which policy packs ran.

    ```output
    Previewing update (dev):
            Type                  Name          Plan
        +   pulumi:pulumi:Stack   test-dev      create
        +   └─ aws:rds:Instance   my-db         create

    Resources:
        + 2 to create

    Policy Packs run:
        Name                                                 Version
        aws-typescript (/Users/user/path/to/policy-pack)     (local)
    ```

1. Edit the stack code to disable storage encryption:

    ```typescript
    storageEncrypted: false,
    ```

1. Run `pulumi preview` again. This time, the policy violation blocks the preview:

    ```output
    Previewing update (dev):
            Type                  Name          Plan       Info
        +   pulumi:pulumi:Stack   test-dev      create     1 error
        +   └─ aws:rds:Instance   my-db         create

    Diagnostics:
        pulumi:pulumi:Stack (test-dev):
        error: preview failed

    Policy Violations:
        [mandatory]  aws-typescript v0.0.1  rds-storage-encryption (my-db: aws:rds/instance:Instance)
        Requires RDS instances to have storage encryption enabled, unless tagged as non-production data.
        RDS instance must have storage encryption enabled (or be tagged 'data-classification=non-production').
    ```

{{% /choosable %}}
{{% choosable language python %}}

1. Use the `--policy-pack` flag to specify your policy pack directory:

    If you need a test program, create one with `pulumi new aws-python` and replace the generated code with a compliant (encrypted) RDS instance:

    ```python
    import pulumi_aws as aws

    db = aws.rds.Instance("my-db",
        engine="postgres",
        instance_class="db.t3.micro",
        allocated_storage=20,
        username="admin",
        manage_master_user_password=True,
        skip_final_snapshot=True,
        storage_encrypted=True,
    )
    ```

    > For AWS examples, ensure you have [AWS credentials configured](/registry/packages/aws/installation-configuration/) and set your region with `pulumi config set aws:region <region>`.

1. In the Pulumi program's directory, run:

    ```sh
    $ pulumi preview --policy-pack <path-to-policy-pack-directory>
    ```

    If the stack is compliant, the output shows which policy packs ran.

    ```output
    Previewing update (dev):
            Type                  Name          Plan
        +   pulumi:pulumi:Stack   test-dev      create
        +   └─ aws:rds:Instance   my-db         create

        Resources:
            + 2 to create

        Policy Packs run:
            Name                                             Version
            aws-python (/Users/user/path/to/policy-pack)     (local)
    ```

1. Edit the stack code to disable storage encryption:

    ```python
    storage_encrypted=False,
    ```

1. Run `pulumi preview` again. This time, the policy violation blocks the preview:

        Previewing update (dev):
             Type                  Name          Plan       Info
         +   pulumi:pulumi:Stack   test-dev      create     1 error
         +   └─ aws:rds:Instance   my-db         create

        Diagnostics:
          pulumi:pulumi:Stack (test-dev):
            error: preview failed

        Policy Violations:
            [mandatory]  aws-python v0.0.1  rds-storage-encryption (my-db: aws:rds/instance:Instance)
            Requires RDS instances to have storage encryption enabled, unless tagged as non-production data.
            RDS instance must have storage encryption enabled (or be tagged 'data-classification=non-production').

{{% /choosable %}}

{{% choosable language opa %}}

1. Use the `--policy-pack` flag to specify your policy pack directory:

    If you need a test program, create one with `pulumi new aws-typescript` or `pulumi new aws-python` and replace the generated code with an unencrypted RDS instance to trigger the policy:

    ```typescript
    import * as aws from "@pulumi/aws";

    const db = new aws.rds.Instance("my-db", {
        engine: "postgres",
        instanceClass: "db.t3.micro",
        allocatedStorage: 20,
        username: "admin",
        manageMasterUserPassword: true,
        skipFinalSnapshot: true,
        storageEncrypted: false,
    });
    ```

    > For AWS examples, ensure you have [AWS credentials configured](/registry/packages/aws/installation-configuration/) and set your region with `pulumi config set aws:region <region>`.

1. In the Pulumi program's directory, run:

    ```sh
    $ pulumi preview --policy-pack <path-to-opa-policy-pack-directory>
    ```

    Because the instance is not encrypted, the policy violation blocks the preview:

    ```output
    Previewing update (dev):
            Type                  Name          Plan       Info
        +   pulumi:pulumi:Stack   test-dev      create     1 error
        +   └─ aws:rds:Instance   my-db         create

    Diagnostics:
        pulumi:pulumi:Stack (test-dev):
        error: preview failed

    Policy Violations:
        [mandatory]  Require RDS Storage Encryption  deny_unencrypted_rds (my-db: aws:rds/instance:Instance)
        RDS instances must have storage encryption enabled, unless tagged as non-production data.
        RDS instance 'my-db' must have storage encryption enabled
    ```

    Set `storageEncrypted: true` (or tag the instance `data-classification=non-production`) and the preview succeeds.

{{% /choosable %}}

{{< /chooser >}}

## Configuring policy packs

Configuration makes policy packs flexible and reusable. Adjust enforcement levels, allowed values, and other settings without modifying code.

<a id="enforcement-levels"></a>

### Enforcement levels

All policies support configurable enforcement levels. Set enforcement for all policies in a pack or override individual policies:

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

As shorthand, specify enforcement levels directly:

```json
{
    "all": "advisory",
    "critical-security-policy": "mandatory"
}
```

<a id="advisory"></a>
<a id="mandatory"></a>
<a id="remediate"></a>
**Enforcement levels:**

- **advisory** - Issues warnings but allows deployments to proceed
- **mandatory** - Blocks deployments when violations are detected
- **remediate** - Automatically fixes violations in place, available in the [Enterprise+ edition](/pricing/#policy-enforcement-modes); see [Remediating policy violations](#remediating-policy-violations)
- **disabled** - Skips policy evaluation entirely

### Custom configuration

Policy authors define configuration schemas using JSON Schema, enabling administrators to customize policy behavior without code changes.

**Example: Optional configuration with defaults**

{{< chooser language "typescript,python,opa" >}}

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
    validateResource: validateResourceOfType(aws.rds.Instance, (_, args, reportViolation) => {
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

{{% choosable language opa %}}

OPA policies access configuration values through `data.config.<rule_name>.<key>`. Access the configuration in your Rego rule like any other data reference:

```rego
package aws

# METADATA
# title: Restrict EC2 Instance Size
# description: EC2 instances must not exceed the configured maximum size.
# custom:
#   message: Use an instance type at or below the configured maxInstanceSize.
deny_large_instances[msg] {
    input.type == "aws:ec2/instance:Instance"
    max_size := data.config.deny_large_instances.maxInstanceSize
    sizes := {"t3.micro": 1, "t3.small": 2, "t3.medium": 3, "t3.large": 4,
              "t3.xlarge": 5, "m5.xlarge": 6, "m5.2xlarge": 7, "m5.4xlarge": 8}
    sizes[input.instanceType] > sizes[max_size]
    msg := sprintf("Instance '%s' type '%s' exceeds maximum allowed size '%s'",
                   [input.__name, input.instanceType, max_size])
}
```

Pass configuration values using the standard Pulumi policy configuration. The values inside the `"properties"` object are injected as `data.config.<rule_name>`. The `"properties"` wrapper key is required in the configuration JSON:

```json
{
    "deny_large_instances": {
        "properties": {
            "maxInstanceSize": "m5.xlarge"
        }
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

**Example: Required configuration**

To require configuration values, add them to the `required` list:

{{< chooser language "typescript,python,opa" >}}

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

{{% choosable language opa %}}

For OPA policies, declare a configuration schema in a `config-schema.json` file alongside your Rego files. Pulumi validates configuration against this schema before evaluation:

```json
{
    "deny_large_instances": {
        "properties": {
            "maxInstanceSize": {
                "type": "string",
                "default": "m5.xlarge"
            }
        },
        "required": ["maxInstanceSize"]
    }
}
```

If a rule declares a config schema but no configuration is provided, the analyzer emits a warning because rules that reference `data.config` will silently not fire without configuration.

{{% /choosable %}}

{{< /chooser >}}

### Using configuration files

#### Local execution

Pass configuration via JSON file:

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

#### Pulumi Cloud configuration

{{< pulumi-cloud "policy-enforcement" />}}

After publishing, administrators configure policy packs through the Pulumi Cloud console or CLI.

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

### Using ESC environments

Policy packs can also receive configuration and secrets from [Pulumi ESC](/docs/esc/) environments. When you attach an ESC environment to a policy pack in a policy group, values defined under the [`policyConfig`](/docs/esc/concepts/outputs/#policyconfig) reserved property are available to your policies at runtime. You can also use [`environmentVariables`](/docs/esc/concepts/outputs/#environmentvariables) to inject environment variables into the policy runtime.

## Publishing to your organization

{{< pulumi-cloud "policy-enforcement" />}}

After local validation, publish your policy pack to Pulumi Cloud. Policy enforcement runs automatically during `preview` and `update` for any stack using Pulumi Cloud.

Pulumi Cloud versions policy packs, enabling updates, rollbacks, and gradual rollouts.

1. From the policy pack directory, publish:

    ```sh
    $ pulumi policy publish <org-name>
    ```

    Pulumi Cloud assigns a monotonic version number:

    ```
    Obtaining policy metadata from policy plugin
    Compressing policy pack
    Uploading policy pack to Pulumi Cloud
    Publishing my-policy-pack to myorg
    Published as version 1.0.0
    ```

### Managing policy pack versions

Policy pack versions are managed differently by language:

- **TypeScript/JavaScript**: Set the `version` field in `package.json`. You can also set `version` in `PulumiPolicy.yaml` to override it.
- **Python**: Set the `version` field in `PulumiPolicy.yaml`
- **OPA**: Set the `version` field in `PulumiPolicy.yaml`

For a complete list of `PulumiPolicy.yaml` fields, see the [project file reference](/docs/insights/policy/policy-packs/project-file/).

Each version can only be published once.

**Publishing a new version:**

1. Update the version number:
   - TypeScript: Edit `package.json`: `"version": "0.0.2"`
   - Python: Edit `PulumiPolicy.yaml`: `version: 0.0.2`
   - OPA: Edit `PulumiPolicy.yaml`: `version: 0.0.2`

1. Publish:

   ```bash
   pulumi policy publish <org-name>
   ```

**If you try to republish an existing version**, you'll see:

```
error: [400] Bad Request: Policy Pack "aws-typescript" (Version 0.0.1) has already been published.
Please specify a new version tag.
```

We recommend [semantic versioning](https://semver.org/):

- **Major** (1.0.0 → 2.0.0): Breaking changes to policy behavior
- **Minor** (1.0.0 → 1.1.0): New policies added
- **Patch** (1.0.0 → 1.0.1): Bug fixes

After publishing, your policy pack appears in Pulumi Cloud's policy pack list. Apply it to stacks or cloud accounts using policy groups. See [Get Started with Pulumi Policies](/docs/insights/policy/get-started/) for details.

## Considerations for authoring policies

Best practices for authoring policy packs:

### Naming policies

Each policy within a policy pack must have a unique name. The name must be between 1 and 100 characters and may contain letters, numbers, dashes (`-`), underscores (`_`), or periods (`.`).

### Policy assertions

Write policy assertions as complete sentences in imperative tone, specifying which resource violated the policy.

| ✅ Good | ❌ Poor |
| ------- | ------- |
| "The RDS cluster must specify a node type." | "Specify a node type." |
| "The RDS cluster must have audit logging enabled." | "Enable audit logging." |
| "S3 bucket must use 'mycompany-' prefix." | "Use correct prefix." |

This format helps users understand which resource failed and why.

## Examples and resources

- [Policy examples repository](https://github.com/pulumi/examples/tree/master/policy-packs) - Example policy packs demonstrating various implementation patterns
- [Policy as Code overview](/docs/insights/policy/)
- [Policy Metadata fields](/docs/insights/policy/metadata/)

## Next steps

- [Apply policies to stacks and accounts using policy groups](/docs/insights/policy/get-started/)
- [View and manage policy findings](/docs/insights/policy/policy-findings/)
- [Learn about policy groups and enforcement modes](/docs/insights/policy/policy-groups/#types-of-policy-groups)
- [Learn about policy pack configuration](/docs/insights/policy/policy-packs/)
