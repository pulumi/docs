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

{{% crossguard-preview %}}

1. Install prerequisites.

   - [Install Pulumi]({{< relref "/docs/get-started/install" >}})
   - [Install Node.js version 8 or later](https://nodejs.org/en/download/)

1. Verify your version of Pulumi.

    ```sh
    $ pulumi version # should be v1.6.1 or later
    ```

1. Create a directory for your new Policy Pack, and change into it.

    ```sh
    $ mkdir policypack && cd policypack
    ```

1. Run the `pulumi policy new` command. Since Policy as Code is a beta feature, you will need to set `PULUMI_EXPERIMENTAL=true` as an environment variable or simply pre-append it to your commands as shown.

    {{< oschoose >}}

    <div class="os-prologue-macos"></div>
    <div class="mt-4">
{{% md %}}
On macOS, you can run `export PULUMI_EXPERIMENTAL=true` or simply prepend it to your commands as shown.

```sh
$ PULUMI_EXPERIMENTAL=true pulumi policy new aws-typescript
```

{{% /md %}}
    </div>

    <div class="os-prologue-linux"></div>
    <div class="mt-4">
{{% md %}}
On Linux, you can run `export PULUMI_EXPERIMENTAL=true` or simply prepend it to your commands as shown.

```sh
$ PULUMI_EXPERIMENTAL=true pulumi policy new aws-typescript
```

{{% /md %}}
    </div>

    <div class="os-prologue-windows"></div>
    <div class="mt-4">
{{% md %}}
On Windows, you must first set the environment variable before running the command.

**Windows cmd.exe**

```bat
set PULUMI_EXPERIMENTAL=true
pulumi policy new aws-typescript
```

**Windows PowerShell**

```powershell
$env:PULUMI_EXPERIMENTAL = 'true'
pulumi policy new aws-typescript
```

{{% /md %}}
    </div>

1. Tweak the Policy Pack in the `index.ts` file as desired. The existing policy in the template (which is annotated below) mandates that an AWS S3 bucket not have public read or write permissions enabled. Each Policy must have a unique name, an enforcement level, and a validation function. Here we use `validateResourceOfType` that allows us to validate S3 Bucket resources.

    ```typescript
    // Create a new Policy Pack.
    new PolicyPack("policy-pack-typescript", {
        // Specify the Policies in the Policy Pack.
        policies: [{
            // The name for the Policy must be unique within the Pack.
            name: "s3-no-public-read",

            // The description should document what the Policy does and why it exists.
            description: "Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",

            // The enforcement level can either be "advisory" or "mandatory". An "advisory" enforcement level
            // simply prints a warning for users, while a "mandatory" policy will block an update from proceeding.
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

    You can find more example Policy Packs in the [examples repo](https://github.com/pulumi/examples/tree/master/policy-packs). [Policy Pack best practices]({{< relref "/docs/guides/crossguard/best-practices" >}}) documentation details the best practices for writing a Policy Pack.

## Testing the Policy Pack Locally

Policy Packs can be tested on a user’s local workstation to facilitate rapid development and testing of policies. This removes the step of publishing and applying policy packs to the Pulumi Console and lets developers reference a policy pack on their local workstation.

1. Run `npm install` in the Policy Pack directory.

1. Use the `--policy-pack` flag with `pulumi preview` or `pulumi up` to specify the path to the directory containing your Policy Pack when previewing/updating a Pulumi project.

    If you don’t have a Pulumi project readily available, you can create a new project for testing by running `pulumi new aws-typescript` in an empty directory. This AWS example will create an S3 bucket, which is perfect for testing our Policy.

    In the Pulumi project's directory run:

    {{< oschoose >}}

    <div class="os-prologue-macos"></div>
    <div class="mt-4">
{{% md %}}

```sh
$ PULUMI_EXPERIMENTAL=true pulumi preview --policy-pack <path-to-policy-pack-directory>
```

{{% /md %}}
    </div>

    <div class="os-prologue-linux"></div>
    <div class="mt-4">
{{% md %}}

```sh
$ PULUMI_EXPERIMENTAL=true pulumi preview --policy-pack <path-to-policy-pack-directory>
```

{{% /md %}}
    </div>

    <div class="os-prologue-windows"></div>
    <div class="mt-4">
{{% md %}}
**Windows cmd.exe**

```bat
set PULUMI_EXPERIMENTAL=true
pulumi preview --policy-pack <path-to-policy-pack-directory>
```

**Windows PowerShell**

```powershell
$env:PULUMI_EXPERIMENTAL = 'true'
pulumi preview --policy-pack <path-to-policy-pack-directory>
```

{{% /md %}}
    </div>

    If the stack is in compliance, we expect the output to simply tell us which Policy Packs were run.

    {{< highlight sh >}}
Previewing update (dev):

     Type                 Name          Plan
 +   pulumi:pulumi:Stack  test-dev  	create
 +   └─ aws:s3:Bucket     my-bucket     create

Resources:
    + 2 to create
{{< /highlight >}}

1. We can then edit the stack code to specify the ACL to be public-read.

    ```typescript
    const bucket = new aws.s3.Bucket("my-bucket", {
        acl: "public-read",
    });
    ```

1. We then run the `pulumi preview` command again and this time get an error message indicating we failed the preview because of a policy violation.

    {{< highlight sh >}}
Previewing update (dev):

     Type                 Name          Plan       Info
 +   pulumi:pulumi:Stack  test-dev  	create     1 error
 +   └─ aws:s3:Bucket     my-bucket     create     1 error

Diagnostics:
  pulumi:pulumi:Stack (test-dev):
    error: preview failed

  aws:s3:Bucket (my-bucket):
    mandatory: [s3-no-public-read] Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.
    You cannot set public-read or public-read-write on an S3 bucket. Read more about ACLs here: [https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html)
{{< /highlight >}}

Now that your Policy Pack is ready to go, let's enforce the pack across your organization.

{{< get-started-stepper >}}

<!-- markdownlint-enable emphasis ul -->
