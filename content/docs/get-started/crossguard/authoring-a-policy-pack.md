---
title: Authoring a Policy Pack
meta_desc: This page provides an overview on how to author a Policy Pack to enforce best practices
           and security compliance when creating coud resources.
linktitle: Authoring a Policy Pack
weight: 1
menu:
  getstarted:
    parent: pac
aliases: ["/docs/get-started/policy-as-code/authoring-a-policy-pack/"]
---
<!-- markdownlint-disable emphasis ul -->

Policies can be written in TypeScript/JavaScript (Node.js) or Python and can be applied to Pulumi stacks written in any language.

{{% notes %}}
Python support is currently in preview.
{{% /notes %}}

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

1. Install prerequisites.

   - [Install Pulumi]({{< relref "/docs/get-started/install" >}})
   - [Install Node.js](https://nodejs.org/en/download/)

1. Verify your version of Pulumi.

    ```sh
    $ pulumi version # should be v1.14.0 or later
    ```

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

   - [Install Pulumi]({{< relref "/docs/get-started/install" >}})
   - [Install Python](https://www.python.org/downloads/)

1. Verify your version of Pulumi.

    ```sh
    $ pulumi version # should be v1.14.0 or later
    ```

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

## Running Locally {#running-locally}

Now let's take a look at how to run the Policy Pack locally against a Pulumi program.

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

1. Run `npm install` in the Policy Pack directory.

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

1. Install dependencies for the Policy Pack.

    **macOS or Linux:**

    Create a virtual environment:

    ```sh
    $ python3 -m venv venv
    ```

    Activate the environment:

    ```sh
    $ source venv/bin/activate
    ```

    Install dependencies:

    ```sh
    $ pip3 install -r requirements.txt
    ```

    **Windows:**

    Create a virtual environment:

    ```bat
    > python -m venv venv
    ```

    Activate the environment:

    ```bat
    > venv\Scripts\activate
    ```

    Install dependencies:

    ```bat
    > pip3 install -r requirements.txt
    ```

1. Use the `--policy-pack` flag with `pulumi preview` or `pulumi up` to specify the path to the directory containing your Policy Pack when previewing/updating a Pulumi program.

    If you don’t have a Pulumi program readily available, you can create a new program for testing by running `pulumi new aws-python` in an empty directory. This AWS example will create an S3 bucket, which is perfect for testing our Policy.

    > Note: We recommend installing dependencies in a virtual environment. If the Pulumi program is also Python, both the Policy Pack and Pulumi program can use the same virtual environment.

    In the Pulumi program's directory, from an activated virtual environment shell, run:

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

{{< get-started-stepper >}}

<!-- markdownlint-enable emphasis ul -->
