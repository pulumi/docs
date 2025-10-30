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
---

If Pulumi's pre-built policy packs don't meet your organization's specific requirements, you can write custom policy packs tailored to your needs. Custom policies allow you to enforce any compliance, security, or operational rule that matters to your organization.

Policies can be written in TypeScript/JavaScript (Node.js) or Python and can be applied to Pulumi stacks written in any language. Learn more about [language support for policies](/docs/guides/crossguard#languages).

## Prerequisites

Before authoring your first policy pack, ensure you have:

- [Pulumi CLI installed](/docs/install/)
- For TypeScript/JavaScript policies: [Node.js installed](https://nodejs.org/en/download/)
- For Python policies: [Python installed](https://python.org/downloads/)
- Access to Pulumi Cloud (Business Critical edition for server-side enforcement)

## Key concepts

Before you begin authoring policies, understand these core concepts:

- **Policy Pack**: A set of related policies (e.g., "Security", "Cost Optimization", "Data Location"). The categorization of policies into a policy pack is left up to you.
- **Policy**: An individual policy (e.g., "prohibit use of instances larger than t3.medium").
- **Enforcement Level**: The impact of a policy violation:
  - **Advisory**: Prints warnings but allows operations to proceed
  - **Mandatory**: Blocks non-compliant deployments
  - **Disabled**: Disables the policy from running

Learn more about [Policy as Code core concepts](/docs/using-pulumi/crossguard/core-concepts/).

## Creating a policy pack

Let's start by creating your first policy pack.

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

1. Create a directory for your new policy pack, and change into it.

    ```sh
    $ mkdir policypack && cd policypack
    ```

1. Run the `pulumi policy new` command.

    ```sh
    $ pulumi policy new aws-typescript
    ```

1. Tweak the policy pack in the `index.ts` file as desired. The existing policy in the template (which is annotated below) mandates that an AWS S3 bucket not have public read or write permissions enabled.

    Each policy must have a unique name, description, and validation function. Here we use the `validateResourceOfType` helper so that our validation function is only called for AWS S3 bucket resources. An enforcement level can be set on the policy pack (applies to all policies) and/or on each individual policy (overriding any policy pack value).

    ```typescript
    // Create a new policy pack.
    new PolicyPack("policy-pack-typescript", {
        // Specify the policies in the policy pack.
        policies: [{
            // The name for the policy must be unique within the pack.
            name: "s3-no-public-read",

            // The description should document what the policy does and why it exists.
            description: "Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",

            // The enforcement level can be "advisory", "mandatory", or "disabled". An "advisory" enforcement level
            // simply prints a warning for users, while a "mandatory" policy will block an update from proceeding, and
            // "disabled" disables the policy from running.
            enforcementLevel: "mandatory",

            // The validateResourceOfType function allows you to filter resources. In this case, the rule only
            // applies to S3 buckets and reports a violation if the acl is "public-read" or "public-read-write".
            validateResource: validateResourceOfType(aws.s3.Bucket, (bucket, args, reportViolation) => {
                if (bucket.acl === "public-read" || bucket.acl === "public-read-write") {
                    reportViolation(
                        "You cannot set public-read or public-read-write on an S3 bucket. " +
                        "Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html");
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

1. Tweak the policy pack in the `__main__.py` file as desired. The existing policy in the template (which is annotated below) mandates that an AWS S3 bucket not have public read or write permissions enabled.

    Each policy must have a unique name, description, and validation function. An enforcement level can be set on the policy pack (applies to all policies) and/or on each individual policy (overriding any policy pack value).

    ```python
    # The validation function is called before each resource is created or updated.
    # In this case, the rule only applies to S3 buckets and reports a violation if the
    # acl is "public-read" or "public-read-write".
    def s3_no_public_read_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
        if args.resource_type == "aws:s3/bucket:Bucket" and "acl" in args.props:
            acl = args.props["acl"]
            if acl == "public-read" or acl == "public-read-write":
                report_violation(
                    "You cannot set public-read or public-read-write on an S3 bucket. " +
                    "Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html")

    s3_no_public_read = ResourceValidationPolicy(
        # The name for the policy must be unique within the pack.
        name="s3-no-public-read",

        # The description should document what the policy does and why it exists.
        description="Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",

        # The enforcement level can be ADVISORY, MANDATORY, or DISABLED. An ADVISORY enforcement level
        # simply prints a warning for users, while a MANDATORY policy will block an update from proceeding, and
        # DISABLED disables the policy from running.
        enforcement_level=EnforcementLevel.MANDATORY,

        # The validation function, defined above.
        validate=s3_no_public_read_validator,
    )

    # Create a new policy pack.
    PolicyPack(
        name="policy-pack-python",
        # Specify the policies in the policy pack.
        policies=[
            s3_no_public_read,
        ],
    )
    ```

{{% /choosable %}}

{{< /chooser >}}

You can find more example policy packs in the [examples repo](https://github.com/pulumi/examples/tree/master/policy-packs). [Policy Pack best practices](/docs/using-pulumi/crossguard/best-practices/) details the best practices for writing a policy pack.

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

1. We can then edit the stack code to specify the ACL to be public-read.

    ```typescript
    const bucket = new aws.s3.Bucket("my-bucket", {
        acl: "public-read",
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
            [mandatory]  aws-typescript v0.0.1  s3-no-public-read (my-bucket: aws:s3/bucket:Bucket)
            Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.
            You cannot set public-read or public-read-write on an S3 bucket. Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html

{{% /choosable %}}
{{% choosable language python %}}

1. Use the `--policy-pack` flag with `pulumi preview` or `pulumi up` to specify the path to the directory containing your policy pack when previewing/updating a Pulumi program.

    If you don't have a Pulumi program readily available, you can create a new program for testing by running `pulumi new aws-python` in an empty directory. This AWS example will create an S3 bucket, which is perfect for testing our policy.

    ```sh
    $ mkdir test-program && cd test-program
    $ pulumi new aws-python
    ```

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

1. We can then edit the stack code to specify the ACL to be public-read.

    ```python
    bucket = s3.Bucket('my-bucket', acl="public-read")
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
            [mandatory]  aws-python v0.0.1  s3-no-public-read (my-bucket: aws:s3/bucket:Bucket)
            Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.
            You cannot set public-read or public-read-write on an S3 bucket. Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html

{{% /choosable %}}

{{< /chooser >}}

Now that your policy pack is ready to go, let's publish it to your organization.

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

    The policy pack version is specified in the `package.json` file for TypeScript/JavaScript (Node.js) packs and in the `PulumiPolicy.yaml` file for Python packs. A version can only be used one time and once published the version can never be used by that policy pack again.

1. After publishing, your custom policy pack will appear in your organization's policy packs list in Pulumi Cloud. From there, you can apply it to stacks or cloud accounts using policy groups. See [Get Started with Pulumi Policy](/docs/insights/policy/get-started/) for details on applying policies via policy groups.

## Examples and resources

### Compliance-ready policies

{{% notes type="warning" %}}
The compliance-ready policies repository is deprecated. We recommend using Pulumi's [pre-built policy packs](/docs/insights/policy/pre-built-packs/) instead, which offer more comprehensive coverage and are actively maintained.
{{% /notes %}}

For reference examples of policy pack implementations, you can review the [compliance-ready policies repository](https://github.com/pulumi/compliance-policies). While this repository is deprecated, it contains useful examples of policy pack structure and implementation patterns.

### Additional resources

- [Policy examples repository](https://github.com/pulumi/examples/tree/master/policy-packs)
- [Policy pack best practices](/docs/using-pulumi/crossguard/best-practices/)
- [Policy as Code core concepts](/docs/using-pulumi/crossguard/core-concepts/)

## Next steps

Now that you've authored and published your first policy pack, you can:

- [Apply policies to stacks and accounts using policy groups](/docs/insights/policy/get-started/)
- [View and manage policy violations](/docs/insights/policy/policy-violations/)
- [Learn about preventative vs. audit policy enforcement](/docs/insights/policy/preventative-vs-audit-policies/)
- [Explore policy pack configuration options](/docs/insights/policy/configuration/)
