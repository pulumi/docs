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

If Pulumi's pre-built policy packs don't meet your organization's specific requirements, you can write custom policy packs tailored to your needs. Custom policies allow you to enforce any compliance, security, or operational rule that matters to your organization.

Policies can be written in TypeScript/JavaScript (Node.js) or Python and can be applied to Pulumi stacks written in any language. Learn more about [language support for policies](/docs/insights/policy/).

## Prerequisites

Before authoring your first policy pack, ensure you have:

- [Pulumi CLI installed](/docs/install/).
- For TypeScript/JavaScript policies: [Node.js installed](https://nodejs.org/en/download/).
- For Python policies: [Python installed](https://python.org/downloads/).
- Access to Pulumi Cloud.
- An understanding of [Policy as Code core concepts](/docs/insights/policy/).

## Creating a policy pack

Let's start by creating your first policy pack.

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

1. Create a directory for your new policy pack and set it as the working directory.

    ```sh
    $ mkdir policypack && cd policypack
    ```

1. Create a new typescript project with `pulumi policy new`.

    ```sh
    $ pulumi policy new aws-typescript
    ```

1. Replace the generated policy in the `index.ts` file with the following example. The template generates a policy that prohibits public ACLs, but we'll use a naming prefix validation example instead, which demonstrates a clearer pattern for organizational policy enforcement.

    Each policy must have a unique name, description, and validation function. Here we use the `validateResourceOfType` helper so that our validation function is only called for AWS S3 bucket resources. An enforcement level can be set on the policy pack (applies to all policies) and/or on each individual policy (overriding any policy pack value).

    ```typescript
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

1. Create a directory for your new policy pack, and change into it.

    ```sh
    $ mkdir policypack && cd policypack
    ```

1. Run the `pulumi policy new` command.

    ```sh
    $ pulumi policy new aws-python
    ```

    {{% notes type="info" %}}
**Virtual environment configuration**: Python policy packs use a virtual environment specified in `PulumiPolicy.yaml`. The default name is `venv`. If you use a different name (like `.venv`), update `PulumiPolicy.yaml`:

```yaml
runtime:
  name: python
  options:
    virtualenv: .venv
```

    {{% /notes %}}

1. Replace the generated policy in the `__main__.py` file with the following example. The template generates a policy that prohibits public ACLs, but we'll use a naming prefix validation example instead, which demonstrates a clearer pattern for organizational policy enforcement.

    Each policy must have a unique name, description, and validation function. An enforcement level can be set on the policy pack (applies to all policies) and/or on each individual policy (overriding any policy pack value).

    ```python
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

You can write unit tests for your policies to validate they behave correctly before publishing to your organization. Here's a simple test example:

```typescript
{{< example-program-snippet path="unit-test-policy" language="typescript" file="test/index.spec.ts" from="6" to="14" >}}
```

For a complete working example including test helpers and setup, see the [unit test policy example on GitHub](https://github.com/pulumi/docs/tree/master/static/programs/unit-test-policy-typescript).

## Resource validation vs stack validation

Pulumi policies can validate two different scopes:

### Resource validation policies

Resource validation policies run against individual resources during `pulumi preview` or `pulumi up`. These policies examine each resource before it's created or updated and can block non-compliant resources from being deployed.

Use resource validation policies when you need to:

- Enforce rules on specific resource types (e.g., "S3 buckets must have encryption enabled")
- Validate resource properties before deployment
- Block individual non-compliant resources

### Stack validation policies

Stack validation policies run against the entire stack after all resources have been registered. These policies can examine relationships between resources and enforce rules about the stack as a whole.

Use stack validation policies when you need to:

- Validate relationships between resources (e.g., "databases must be in private subnets")
- Enforce stack-wide rules (e.g., "stack must not exceed 50 resources")
- Examine the complete resource graph

Most policies are resource validation policies. Stack validation policies are useful for more complex scenarios that require understanding the full context of your infrastructure.

## Running policies locally

Before publishing your policy pack, test it locally against your Pulumi programs.

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

1. Use the `--policy-pack` flag with `pulumi preview` or `pulumi up` to specify the path to the directory containing your policy pack when previewing/updating a Pulumi program.

    If you don't have a Pulumi program readily available, you can create a new program for testing by running `pulumi new aws-typescript` in an empty directory. This AWS example will create an S3 bucket, which is perfect for testing our policy.

    ```sh
    $ mkdir test-program && cd test-program
    $ pulumi new aws-typescript
    ```

    {{% notes type="info" %}}
For AWS examples, ensure you have [AWS credentials configured](/registry/packages/aws/installation-configuration/) and set your region with `pulumi config set aws:region <region>`.
    {{% /notes %}}

    In the Pulumi program's directory run:

    ```sh
    $ pulumi preview --policy-pack <path-to-policy-pack-directory>
    ```

    If the Pulumi stack is in compliance, we expect the output to tell us which policy packs were run.

        Previewing update (dev):
             Type                 Name          Plan
         +   pulumi:pulumi:Stack  test-dev      create
         +   └─ aws:s3:Bucket     my-bucket     create

        Resources:
            + 2 to create

        Policy Packs run:
            Name                                                 Version
            aws-typescript (/Users/user/path/to/policy-pack)     (local)

1. We can then edit the stack code to specify a bucket prefix that doesn't match the required prefix.

    ```typescript
    const bucket = new aws.s3.Bucket("my-bucket", {
        bucketPrefix: "wrongprefix-",
    });
    ```

1. We then run the `pulumi preview` command again and this time get an error message indicating we failed the preview because of a policy violation.

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

{{% /choosable %}}
{{% choosable language python %}}

1. Use the `--policy-pack` flag with `pulumi preview` or `pulumi up` to specify the path to the directory containing your policy pack when previewing/updating a Pulumi program.

    If you don't have a Pulumi program readily available, you can create a new program for testing by running `pulumi new aws-python` in an empty directory. This AWS example will create an S3 bucket, which is perfect for testing our policy.

    ```sh
    $ mkdir test-program && cd test-program
    $ pulumi new aws-python
    ```

    {{% notes type="info" %}}
For AWS examples, ensure you have [AWS credentials configured](/registry/packages/aws/installation-configuration/) and set your region with `pulumi config set aws:region <region>`.
    {{% /notes %}}

    In the Pulumi program's directory, run:

    ```sh
    $ pulumi preview --policy-pack <path-to-policy-pack-directory>
    ```

    If the Pulumi stack is in compliance, we expect the output to tell us which policy packs were run.

        Previewing update (dev):
             Type                 Name          Plan
         +   pulumi:pulumi:Stack  test-dev      create
         +   └─ aws:s3:Bucket     my-bucket     create

        Resources:
            + 2 to create

        Policy Packs run:
            Name                                             Version
            aws-python (/Users/user/path/to/policy-pack)     (local)

1. We can then edit the stack code to specify a bucket prefix that doesn't match the required prefix.

    ```python
    bucket = s3.Bucket('my-bucket', bucket_prefix="wrongprefix-")
    ```

1. We then run the `pulumi preview` command again and this time get an error message indicating we failed the preview because of a policy violation.

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

### Using configuration files

#### Local execution

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

#### Pulumi Cloud configuration

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

## Publishing to your organization

{{% notes type="info" %}}
Server-side enforcement of policy packs across an organization is only available in **Pulumi Business Critical**. See [pricing](/pricing/) for more details.
{{% /notes %}}

Once you've validated the behavior of your policies locally, publish them to Pulumi Cloud to enforce them across your organization. Any Pulumi client (a developer's workstation, CI/CD tool, etc.) that interacts with a stack via Pulumi Cloud will have policy enforcement during the execution of `preview` and `update`.

Policy packs are versioned by Pulumi Cloud so that updated policies can be published and applied as ready and also reverted to previous versions as needed.

1. From within the policy pack directory, run the following command to publish your pack:

    ```sh
    $ pulumi policy publish <org-name>
    ```

    The output will tell you what version of the policy pack you just published. Pulumi Cloud provides a monotonic version number for policy packs.

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

Each version can only be published once. After publishing, that version can never be reused for that policy pack.

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

After publishing, your custom policy pack will appear in your organization's policy packs list in Pulumi Cloud. From there, you can apply it to stacks or cloud accounts using policy groups. See [Get Started with Pulumi Policy](/docs/insights/policy/get-started/) for details on applying policies via policy groups.

## Considerations for authoring policies

When authoring policy packs, keep the following best practices in mind:

### Naming policies

Each policy within a policy pack must have a unique name. The name must be between 1 and 100 characters and may contain letters, numbers, dashes (`-`), underscores (`_`), or periods (`.`).

### Policy assertions

Policy assertions should be complete sentences, specify the resource that has violated the policy, and be written using an imperative tone.

| ✅ Good | ❌ Poor |
| ------- | ------- |
| "The RDS cluster must specify a node type." | "Specify a node type." |
| "The RDS cluster must have audit logging enabled." | "Enable audit logging." |
| "S3 bucket must use 'mycompany-' prefix." | "Use correct prefix." |

This format provides clear messages to end users, allowing them to understand what and why a policy is failing.

## Examples and resources

### Compliance-ready policies

{{% notes type="warning" %}}
The compliance-ready policies repository is deprecated. We recommend using Pulumi's [pre-built policy packs](/docs/insights/policy/pre-built-packs/) instead, which offer more comprehensive coverage and are actively maintained.
{{% /notes %}}

For reference examples of policy pack implementations, you can review the [compliance-ready policies repository](https://github.com/pulumi/compliance-policies). While this repository is deprecated, it contains useful examples of policy pack structure and implementation patterns.

### Additional resources

- [Policy examples repository](https://github.com/pulumi/examples/tree/master/policy-packs)
- [Policy as Code overview](/docs/insights/policy/)

## Next steps

Now that you've authored and published your first policy pack, you can:

- [Apply policies to stacks and accounts using policy groups](/docs/insights/policy/get-started/)
- [View and manage policy findings](/docs/insights/policy/policy-findings/)
- [Learn about policy groups and enforcement modes](/docs/insights/policy/policy-groups/)
- [Learn about policy pack configuration](/docs/insights/policy/policy-packs/)
