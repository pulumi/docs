---
title: Write your own
title_tag: "Write your own policy packs"
h1: Write your own policy packs
meta_desc: Learn how to write custom policy packs to enforce organization-specific compliance and security controls.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    name: Write your own
    parent: policy-packs
    weight: 2
aliases:
  - /docs/insights/policy/authoring/
  - /docs/insights/policy/policy-packs/authoring/
  - /docs/insights/policy/best-practices/
---

If Pulumi's pre-built policy packs don't meet your requirements, you can write custom policy packs. Custom policies let you enforce any compliance, security, or operational rule.

Policies can be written in TypeScript/JavaScript (Node.js) or Python and can be applied to Pulumi stacks written in any language. Learn more about [language support for policies](/docs/insights/policy/#languages).

### Creating a Policy Pack with Neo

This guide walks you through creating a policy pack manually, but [Neo](/product/neo/) can help streamline the process.  

Neo can generate policy pack content tailored to your preferred programming language and cloud providers, allowing you to quickly build policies that meet your specific requirements while reducing errors. When paired with the [GitHub App](/docs/iac/guides/continuous-delivery/github-app/), Neo can even open pull requests directly in your repository.  

Here are some example prompts to inspire your workflow:

> "Create a boilerplate TypeScript policy pack at `<GitHub Repository>`"  
> "Create a policy to enforce encryption of S3 buckets"  
> "Create a policy that requires environment tagging on all Google Cloud resources"

## Prerequisites

Before authoring your first policy pack, ensure you have:

- [Pulumi CLI installed](/docs/install/).
- For TypeScript/JavaScript policies: [Node.js installed](https://nodejs.org/en/download/).
- For Python policies: [Python installed](https://python.org/downloads/).
- (Optional) Access to Pulumi Cloud if you want to publish and centrally manage policy packs. Not required for local policy pack usage with open source Pulumi.
- An understanding of [Policy as Code core concepts](/docs/insights/policy/).

## Creating a policy pack

Create your first policy pack:

{{< chooser language "typescript,python" >}}

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
    - A validation function (this example uses `validateResourceOfType` to run only for AWS S3 bucket resources)
    - An enforcement level set at the policy pack level (applies to all policies) or per policy (overrides the pack level)

For more information on all available fields, see [policy metadata](/docs/insights/policy/policy-as-code/policy-metadata/).
    ```typescript
    import * as aws from "@pulumi/aws";
    import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

    // Create a new policy pack.
    new PolicyPack("policy-pack-typescript", {
        // Specify the policies in the policy pack.
        policies: [{
            // The name for the policy must be unique within the pack.
            name: "s3-bucket-prefix",

            // The description should document what the policy does and why it exists.
            description: "Ensures S3 buckets use the required naming prefix.",

            // The enforcement level can be "advisory", "mandatory", or "disabled". An "advisory" enforcement level
            // simply prints a warning for users, while a "mandatory" policy will block an update from proceeding, and
            // "disabled" disables the policy from running.
            enforcementLevel: "mandatory",

            // The validateResourceOfType function allows you to filter resources. In this case, the rule only
            // applies to S3 buckets and reports a violation if the bucket prefix doesn't match the required prefix.
            validateResource: validateResourceOfType(aws.s3.Bucket, (bucket, args, reportViolation) => {
                const requiredPrefix = "mycompany-";
                const bucketPrefix = bucket.bucketPrefix || "";
                if (!bucketPrefix.startsWith(requiredPrefix)) {
                    reportViolation(
                        `S3 bucket must use '${requiredPrefix}' prefix. Current prefix: '${bucketPrefix}'`);
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

2. Create a new Python project:

    ```sh
    $ pulumi policy new aws-python
    ```

    > **Virtual environment configuration**: Python policy packs use a virtual environment specified in `PulumiPolicy.yaml`. The default name is `venv`. If you use a different name (like `.venv`), update `PulumiPolicy.yaml`:
    >
    > ```yaml
    > runtime:
    > name: python
    > options:
    >     virtualenv: .venv
    > ```

3. Replace the generated policy in `__main__.py` with this example, which demonstrates a clearer pattern for organizational policy enforcement:

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
    # In this case, the rule only applies to S3 buckets and reports a violation if the
    # bucket prefix doesn't match the required prefix.
    REQUIRED_S3_PREFIX = "mycompany-"

    def s3_bucket_prefix_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
        if args.resource_type == "aws:s3/bucket:Bucket" and "bucketPrefix" in args.props:
            actual_prefix = args.props["bucketPrefix"]
            if not actual_prefix.startswith(REQUIRED_S3_PREFIX):
                report_violation(
                    f"S3 bucket must use '{REQUIRED_S3_PREFIX}' prefix. Current prefix: '{actual_prefix}'")

    s3_bucket_prefix = ResourceValidationPolicy(
        # The name for the policy must be unique within the pack.
        name="s3-bucket-prefix",

        # The description should document what the policy does and why it exists.
        description="Ensures S3 buckets use the required naming prefix.",

        # The enforcement level can be ADVISORY, MANDATORY, or DISABLED. An ADVISORY enforcement level
        # simply prints a warning for users, while a MANDATORY policy will block an update from proceeding, and
        # DISABLED disables the policy from running.
        enforcement_level=EnforcementLevel.MANDATORY,

        # The validation function, defined above.
        validate=s3_bucket_prefix_validator,
    )

    # Create a new policy pack.
    PolicyPack(
        name="policy-pack-python",
        # Specify the policies in the policy pack.
        policies=[
            s3_bucket_prefix,
        ],
    )
    ```

{{% /choosable %}}

{{< /chooser >}}

You can find more example policy packs in the [Pulumi examples repository](https://github.com/pulumi/examples/tree/master/policy-packs).

## Testing your policies

Write unit tests to verify your policies work correctly before publishing.

{{< chooser language "typescript,python" >}}

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
{{< example-program-snippet path="unit-test-policy" language="python" file="test_policy.py" from="16" to="33" >}}
```

For a complete example including additional test cases, see the [unit test policy example on GitHub](https://github.com/pulumi/docs/tree/master/static/programs/unit-test-policy-python).

{{% /choosable %}}

{{< /chooser >}}

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

## Running policies locally

Test your policy pack locally before publishing.

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

1. Use the `--policy-pack` flag to specify your policy pack directory:

    If you need a test program, create one with `pulumi new aws-typescript`. This creates an S3 bucket to test the policy.

    ```sh
    $ mkdir test-program && cd test-program
    $ pulumi new aws-typescript
    ```

    > For AWS examples, ensure you have [AWS credentials configured](/registry/packages/aws/installation-configuration/) and set your region with `pulumi config set aws:region <region>`.

1. In the Pulumi program's directory, run:

    ```sh
    $ pulumi preview --policy-pack <path-to-policy-pack-directory>
    ```

    If the stack is compliant, the output shows which policy packs ran.

    ```output
    Previewing update (dev):
            Type                 Name          Plan
        +   pulumi:pulumi:Stack  test-dev      create
        +   └─ aws:s3:Bucket     my-bucket     create

    Resources:
        + 2 to create

    Policy Packs run:
        Name                                                 Version
        aws-typescript (/Users/user/path/to/policy-pack)     (local)
    ```

1. Edit the stack code to specify a non-matching prefix:

    ```typescript
    const bucket = new aws.s3.Bucket("my-bucket", {
        bucketPrefix: "wrongprefix-",
    });
    ```

1. Run `pulumi preview` again. This time, the policy violation blocks the preview:

    ```output
    Previewing update (dev):
            Type                 Name          Plan       Info
        +   pulumi:pulumi:Stack  test-dev      create     1 error
        +   └─ aws:s3:Bucket     my-bucket     create

    Diagnostics:
        pulumi:pulumi:Stack (test-dev):
        error: preview failed

    Policy Violations:
        [mandatory]  aws-typescript v0.0.1  s3-bucket-prefix (my-bucket: aws:s3/bucket:Bucket)
        Ensures S3 buckets use the required naming prefix.
        S3 bucket must use 'mycompany-' prefix. Current prefix: 'wrongprefix-'
    ```

{{% /choosable %}}
{{% choosable language python %}}

1. Use the `--policy-pack` flag to specify your policy pack directory:

    If you need a test program, create one with `pulumi new aws-python`. This creates an S3 bucket to test the policy.

    ```sh
    $ mkdir test-program && cd test-program
    $ pulumi new aws-python
    ```

    > For AWS examples, ensure you have [AWS credentials configured](/registry/packages/aws/installation-configuration/) and set your region with `pulumi config set aws:region <region>`.

1. In the Pulumi program's directory, run:

    ```sh
    $ pulumi preview --policy-pack <path-to-policy-pack-directory>
    ```

    If the stack is compliant, the output shows which policy packs ran.

    ```output
    Previewing update (dev):
            Type                 Name          Plan
        +   pulumi:pulumi:Stack  test-dev      create
        +   └─ aws:s3:Bucket     my-bucket     create

        Resources:
            + 2 to create

        Policy Packs run:
            Name                                             Version
            aws-python (/Users/user/path/to/policy-pack)     (local)
    ```

1. Edit the stack code to specify a non-matching prefix:

    ```python
    bucket = s3.Bucket('my-bucket', bucket_prefix="wrongprefix-")
    ```

1. Run `pulumi preview` again. This time, the policy violation blocks the preview:

        Previewing update (dev):
             Type                 Name          Plan       Info
         +   pulumi:pulumi:Stack  test-dev      create     1 error
         +   └─ aws:s3:Bucket     my-bucket     create

        Diagnostics:
          pulumi:pulumi:Stack (test-dev):
            error: preview failed

        Policy Violations:
            [mandatory]  aws-python v0.0.1  s3-bucket-prefix (my-bucket: aws:s3/bucket:Bucket)
            Ensures S3 buckets use the required naming prefix.
            S3 bucket must use 'mycompany-' prefix. Current prefix: 'wrongprefix-'

{{% /choosable %}}

{{< /chooser >}}

## Configuring policy packs

Configuration makes policy packs flexible and reusable. Adjust enforcement levels, allowed values, and other settings without modifying code.

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

**Enforcement levels:**

- **advisory** — Issues warnings but allows deployments to proceed
- **mandatory** — Blocks deployments when violations are detected
- **disabled** — Skips policy evaluation entirely

### Custom configuration

Policy authors define configuration schemas using JSON Schema, enabling administrators to customize policy behavior without code changes.

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

## Publishing to your organization

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

- **TypeScript/JavaScript**: Set the `version` field in `package.json`
- **Python**: Set the `version` field in `PulumiPolicy.yaml`

Each version can only be published once.

**Publishing a new version:**

1. Update the version number:
   - TypeScript: Edit `package.json`: `"version": "0.0.2"`
   - Python: Edit `PulumiPolicy.yaml`: `version: 0.0.2`

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

After publishing, your policy pack appears in Pulumi Cloud's policy pack list. Apply it to stacks or cloud accounts using policy groups. See [Get Started with Pulumi Policy](/docs/insights/policy/get-started/) for details.

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
- [Policy Metadata fields](/docs/insights/policy/metadata.md)

## Next steps

- [Apply policies to stacks and accounts using policy groups](/docs/insights/policy/get-started/)
- [View and manage policy findings](/docs/insights/policy/policy-findings/)
- [Learn about policy groups and enforcement modes](/docs/insights/policy/policy-groups/#types-of-policy-groups)
- [Learn about policy pack configuration](/docs/insights/policy/policy-packs/)
