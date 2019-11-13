---
title: Authoring a Policy Pack (Preview)
linktitle: Authoring a Policy Pack
weight: 1
menu:
  getstarted:
    parent: pac
    identifier: pac-authoring-a-policy-pack
---
{{% pac-preview %}}

1. Create a directory for your new Policy Pack, and change into it.

    ```sh
    $ mkdir policypack && cd policypack
    ```

1. Run the `pulumi policy new` command. Since Policy as Code is a beta feature, you will need to set `PULUMI_DEBUG_COMMANDS=true` as an environment variable or simply pre-append it to your commands as shown. (Note: Pulumi 1.4.1 or later is required to use `pulumi policy new` command.)

    ```sh
    $ PULUMI_DEBUG_COMMANDS=true pulumi policy new aws-typescript
    Created Policy Pack!
    Installing dependencies...
    ...
    Finished installing dependencies

    Your new Policy Pack is ready to go! ✨

    Once you're done editing your Policy Pack, run `pulumi policy publish <org-name>/<policy-pack-name>` to publish the pack.
    ```

2. Tweak the Policy Pack in the `index.ts` file as desired. The existing policy in the template (which is annotated below) mandates that an AWS S3 bucket not have public read or write permissions enabled. Each Policy must have a unique name, an enforcement level, and a validation function. Here we use `validateTypedResource` that allows us to validate S3 Bucket resources.

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

            // The validateTypedResource function allows you to filter resources. In this case, the rule only
            // applies to S3 buckets and reports a violation if the acl is "public-read" or "public-read-write".
            validateResource: validateTypedResource(aws.s3.Bucket, (bucket, args, reportViolation) => {
                if (bucket.acl === "public-read" || bucket.acl === "public-read-write") {
                    reportViolation(
                        "You cannot set public-read or public-read-write on an S3 bucket. " +
                        "Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html");
                }
            }),
        }],
    });
    ```

    You can find more example Policy Packs in the [examples repo](https://github.com/pulumi/examples/tree/master/policy-packs). Best practices for writing a Policy Pack can be found [here]({{< relref "best-practices" >}}).

## Testing the Policy Pack Locally

Policy Packs can be tested on a user’s local workstation to facilitate rapid development and testing of policies. This removes the step of publishing and applying policy packs to the Pulumi Console and lets developers reference a policy pack on their local workstation.

1. Run `npm install` in the Policy Pack directory.

1. Use the `--policy-pack` flag with `pulumi preview` or `pulumi up` to specify the path to the directory containing your Policy Pack when previewing/updating a Pulumi project.

    If you don’t have a Pulumi project readily available, you can create a new project for testing by running `pulumi new aws-typescript` in an empty directory. This AWS example will create an S3 bucket, which is perfect for testing our Policy.

    In the Pulumi project's directory run:

    ```sh
    PULUMI_DEBUG_COMMANDS=true pulumi preview --policy-pack <path-to-policy-pack-directory>
    ```

    If the stack is in compliance, we expect the output to simply tell us which Policy Packs were run.

    {{< highlight sh >}}
$ PULUMI_DEBUG_COMMANDS=true pulumi preview --policy-pack policy-pack-typescript
Previewing update (dev):

     Type                 Name          Plan
 +   pulumi:pulumi:Stack  test-dev  	create
 +   └─ aws:s3:Bucket     my-bucket     create

Resources:
    + 2 to create

Permalink:
...
{{< /highlight >}}

1. We can then edit the stack code to specify the ACL to be public-read.

    ```typescript
    const bucket = new aws.s3.Bucket("my-bucket", {
        acl: "public-read",
    });
    ```

1. We then run the `pulumi preview` command again and this time get an error message indicating we failed the preview because of a policy violation.

    {{< highlight sh >}}
$ PULUMI_DEBUG_COMMANDS=true pulumi preview --policy-pack ~/policy-pack-typescript
Previewing update (dev):

     Type                 Name          Plan       Info
 +   pulumi:pulumi:Stack  test-dev  	create     1 error
 +   └─ aws:s3:Bucket     my-bucket     create     1 error

Diagnostics:
  pulumi:pulumi:Stack (test-dev):
    error: preview failed

  aws:s3:Bucket (my-bucket):
    mandatory: [s3-no-public-read] Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.
    You cannot set public-read or public-read-write on an S3 bucket. Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html

Permalink:
...
{{< /highlight >}}

Now that your Policy Pack is ready to go, let's enforce the pack across your organization.

{{< get-started-stepper >}}
