---
title: Get Started with Policy as Code
meta_desc: Pulumi CrossGuard is a product that provides gated deployments via Policy as Code. Enforce best practices
           and security compliance when creating cloud resources.
linktitle: Get Started
weight: 1
aliases: [
    "/docs/get-started/policy-as-code",
    "/docs/get-started/crossguard",
    "/docs/get-started/crossguard/authoring-a-policy-pack",
    "/docs/get-started/crossguard/enforcing-a-policy-pack"
]

menu:
  userguides:
    parent: crossguard
---

Pulumi CrossGuard is a product that provides gated deployments via Policy as Code.

Often organizations want to empower developers to manage their infrastructure yet are concerned about giving them full access. CrossGuard allows administrators to provide autonomy to their developers while ensuring compliance to defined organization policies.

Using Policy as Code, users can express business or security rules as functions that are executed against resources in their stacks. Then using CrossGuard, organization administrators can apply these rules to particular stacks within their organization. When policies are executed as part of your Pulumi deployments, any violation will gate or block that update from proceeding.

Policies can be written in TypeScript/JavaScript (Node.js) or Python and can be applied to Pulumi stacks written in any language. Learn more about [language support for policies]({{< relref "/docs/guides/crossguard#languages" >}}).

## Terminology

* **Policy Pack** - a set of related policies - i.e. “Security”, “Cost Optimization”, “Data Location”. The categorization of policies into a policy pack is left up to the user.
* **Policy** - an individual policy - i.e. “prohibit use of instances larger than t3.medium”.
* **Enforcement Level** - the impact of a policy violation - i.e. “mandatory” or “advisory”.

Learn more about [Policy as Code core concepts]({{< relref "/docs/guides/crossguard/core-concepts" >}}).

## Creating a Policy Pack

Let's start with authoring your first Policy Pack.

Policies can be written in TypeScript/JavaScript (Node.js) or Python and can be applied to Pulumi stacks written in any language. [More information on language support for policies]({{< relref "/docs/guides/crossguard#languages" >}}).

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

1. Install prerequisites.

   * [Install Pulumi]({{< relref "/docs/get-started/install" >}})
   * [Install Node.js](https://nodejs.org/en/download/)

1. Create a directory for your new Policy Pack, and change into it.

    ```sh
    $ mkdir policypack && cd policypack
    ```

1. Run the `pulumi policy new` command.

    ```sh
    $ pulumi policy new aws-typescript
    ```

1. Tweak the Policy Pack in the `index.ts` file as desired. The existing policy in the template (which is annotated below) mandates that an AWS S3 bucket not have public read or write permissions enabled.

    Each Policy must have a unique name, description, and validation function. Here we use the `validateResourceOfType` helper so that our validation function is only called for AWS S3 bucket resources. An enforcement level can be set on the Policy Pack (applies to all policies) and/or on each individual policy (overriding any Policy Pack value).

    ```typescript
    // Create a new Policy Pack.
    new PolicyPack("policy-pack-typescript", {
        // Specify the Policies in the Policy Pack.
        policies: [{
            // The name for the Policy must be unique within the Pack.
            name: "s3-no-public-read",

            // The description should document what the Policy does and why it exists.
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

1. Install prerequisites.

   * [Install Pulumi]({{< relref "/docs/get-started/install" >}})
   * [Install Python](https://www.python.org/downloads/)

1. Create a directory for your new Policy Pack, and change into it.

    ```sh
    $ mkdir policypack && cd policypack
    ```

1. Run the `pulumi policy new` command.

    ```sh
    $ pulumi policy new aws-python
    ```

1. Tweak the Policy Pack in the `__main__.py` file as desired. The existing policy in the template (which is annotated below) mandates that an AWS S3 bucket not have public read or write permissions enabled.

    Each Policy must have a unique name, description, and validation function. An enforcement level can be set on the Policy Pack (applies to all policies) and/or on each individual policy (overriding any Policy Pack value).

    ```python
    # The validation function is called before each resource is created or updated.
    # In this case, the rule only applies to S3 buckets and reports a violation if the
    # acle is "public-read" or "public-read-write".
    def s3_no_public_read_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
        if args.resource_type == "aws:s3/bucket:Bucket" and "acl" in args.props:
            acl = args.props["acl"]
            if acl == "public-read" or acl == "public-read-write":
                report_violation(
                    "You cannot set public-read or public-read-write on an S3 bucket. " +
                    "Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html")

    s3_no_public_read = ResourceValidationPolicy(
        # The name for the Policy must be unique within the Pack.
        name="s3-no-public-read",

        # The description should document what the Policy does and why it exists.
        description="Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",

        # The enforcement level can be ADVISORY, MANDATORY, or DISABLED. An ADVISORY enforcement level
        # simply prints a warning for users, while a MANDATORY policy will block an update from proceeding, and
        # DISABLED disables the policy from running.
        enforcement_level=EnforcementLevel.MANDATORY,

        # The validation function, defined above.
        validate=s3_no_public_read_validator,
    )

    # Create a new Policy Pack.
    PolicyPack(
        name="policy-pack-python",
        # Specify the Policies in the Policy Pack.
        policies=[
            s3_no_public_read,
        ],
    )
    ```

{{% /choosable %}}

{{< /chooser >}}

You can find more example Policy Packs in the [examples repo](https://github.com/pulumi/examples/tree/master/policy-packs). [Policy Pack best practices]({{< relref "/docs/guides/crossguard/best-practices" >}}) details the best practices for writing a Policy Pack.

### Running Locally {#running-locally}

Now let's take a look at how to run the Policy Pack locally against a Pulumi program.

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

1. Use the `--policy-pack` flag with `pulumi preview` or `pulumi up` to specify the path to the directory containing your Policy Pack when previewing/updating a Pulumi program.

    If you don’t have a Pulumi program readily available, you can create a new program for testing by running `pulumi new aws-typescript` in an empty directory. This AWS example will create an S3 bucket, which is perfect for testing our Policy.

    In the Pulumi program's directory run:

    ```sh
    $ pulumi preview --policy-pack <path-to-policy-pack-directory>
    ```

    If the Pulumi stack is in compliance, we expect the output to simply tell us which Policy Packs were run.

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

1. Use the `--policy-pack` flag with `pulumi preview` or `pulumi up` to specify the path to the directory containing your Policy Pack when previewing/updating a Pulumi program.

    If you don’t have a Pulumi program readily available, you can create a new program for testing by running `pulumi new aws-python` in an empty directory. This AWS example will create an S3 bucket, which is perfect for testing our Policy.

    In the Pulumi program's directory, run:

    ```sh
    $ pulumi preview --policy-pack <path-to-policy-pack-directory>
    ```

    If the Pulumi stack is in compliance, we expect the output to simply tell us which Policy Packs were run.

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

Now that your Policy Pack is ready to go, let's enforce the pack across your organization.

## Enforcing a Policy Pack

{{% notes type="info" %}}
Server-side enforcement of policy packs across an organization is only available in **Pulumi Business Critical**. See [pricing]({{<relref "/pricing">}}) for more details.
{{% /notes %}}

Once you’ve validated the behavior of your policies, an organization administrator can publish them to the Pulumi Service to be enforced across your organization. Any Pulumi client (a developer’s workstation, CI/CD tool, etc) that interacts with a stack via the Pulumi Service will have policy enforcement during the execution of `preview` and `update`. Policy Packs are versioned by the Pulumi Service so that updated policies can be published and applied as ready and also reverted to previous versions as needed.

1. From within the Policy Pack directory, run the following command to publish your pack:

    ```sh
    $ pulumi policy publish <org-name>
    ```

    The output will tell you what version of the Policy Pack you just published. The Pulumi service provides a monotonic version number for Policy Packs.

    ```
    Obtaining policy metadata from policy plugin
    Compressing policy pack
    Uploading policy pack to Pulumi service
    Publishing my-policy-pack to myorg
    Published as version 1.0.0
    ```

    The Policy Pack version is specified in the `package.json` file for TypeScript/JavaScript (Node.js) packs and in the `PulumiPolicy.yaml` file for Python packs. A version can only be used one time and once published the version can never be used by that Policy Pack again.

    <!-- markdownlint-disable ul -->
1. You can enable this Policy Pack to your organization’s default Policy Group by running:

    ```sh
    $ pulumi policy enable <org-name>/<policy-pack-name> <latest|version>
    ```

    For example, to enable the Policy Pack created in the previous step:

    ```sh
    $ pulumi policy enable myorg/my-policy-pack latest
    ```

    The CLI by default enables the Policy Pack to your default Policy Group. If you would like to add the Policy Pack to a different Policy Group, you can use the `--policy-group` flag.

## Next Steps

Now that you have published your first Policy Pack, you now have all the tools needed to enforce compliance amongst your organization. For more example Policy Packs, you can check out the [examples repo](https://github.com/pulumi/examples/tree/master/policy-packs). You can also find more documentation in the [CrossGuard guide]({{< relref "/docs/guides/crossguard" >}}).
