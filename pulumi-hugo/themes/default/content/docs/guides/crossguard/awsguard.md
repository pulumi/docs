---
title: Pulumi CrossGuard policies for AWS (AWSGuard)
meta_desc: AWSGuard codifies best practices for AWS in a library that you can configure and
           use to enforce these best practices for your own Pulumi stacks or organization.
linktitle: AWSGuard
weight: 2

menu:
  userguides:
    parent: crossguard
---
<!-- markdownlint-disable ul code -->
{{% crossguard-preview %}}

## Overview

[AWSGuard](https://github.com/pulumi/pulumi-policy-aws) codifies best practices for AWS. It is an [open source](https://github.com/pulumi/pulumi-policy-aws) library that you can configure and use to enforce these best practices for your own Pulumi stacks or organization.

For more information on Pulumi's Policy as Code solution, visit our [docs]({{< relref "/docs/get-started/crossguard" >}}).

## Trying AWSGuard

In this guide, we'll show you how to create a Policy Pack that configures and uses the policies available in AWSGuard.

### Prerequisites

- [Install Pulumi]({{< relref "/docs/get-started/install" >}})
- [Install Node.js version 8 or later](https://nodejs.org/en/download/)

### Verify your version of the Pulumi CLI

```sh
pulumi version # should be v1.6.1 or later
```

### Authoring a Policy Pack that uses AWSGuard policies

To use AWSGuard policies, you must create a Policy Pack that references the `@pulumi/awsguard` npm package and creates a new instance of the `AwsGuard` class.

1. Create a directory for your new Policy Pack, and change into it.

    ```sh
    mkdir awsguard && cd awsguard
    ```
1. Run the `pulumi policy new` command. Since Policy as Code is in preview, you will need to set `PULUMI_EXPERIMENTAL=true` as an environment variable.

    {{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

On macOS, you can run `export PULUMI_EXPERIMENTAL=true` or simply prepend it to your commands as shown.

```sh
$ PULUMI_EXPERIMENTAL=true pulumi policy new awsguard-typescript
```
{{% /choosable %}}

{{% choosable os linux %}}

On Linux, you can run `export PULUMI_EXPERIMENTAL=true` or simply prepend it to your commands as shown.

```sh
$ PULUMI_EXPERIMENTAL=true pulumi policy new awsguard-typescript
```

{{% /choosable %}}

{{% choosable os windows %}}

On Windows, you must first set the environment variable before running the command.

Windows cmd.exe:

```bat
> set PULUMI_EXPERIMENTAL=true
> pulumi policy new awsguard-typescript
```

Windows PowerShell:

```powershell
> $env:PULUMI_EXPERIMENTAL = 'true'
> pulumi policy new awsguard-typescript
```

{{% /choosable %}}

{{< /chooser >}}

1. Tweak the code in the `index.ts` file as desired. The default implementation provided by the `awsguard-typescript` template simply creates a new instance of `AwsGuard` with all policies set to have an enforcement level of advisory.

    ```typescript
    new AwsGuard({ all: "advisory" });
    ```

    From here, you can change the enforcement level for all policies or configure individual policies.

    For example:

    To make all policies mandatory rather than advisory:

    ```typescript
    new AwsGuard({ all: "mandatory" });
    ```

    To make all policies mandatory, but change certain policies to be advisory:

    ```typescript
    new AwsGuard({
        all: "mandatory",
        ec2InstanceNoPublicIP: "advisory",
        elbAccessLoggingEnabled: "advisory",
    });
    ```

    To disable a particular policy:

    ```typescript
    new AwsGuard({
        ec2InstanceNoPublicIP: "disabled",
    });
    ```

    To disable all policies except ones explicitly enabled:

    ```typescript
    new AwsGuard({
        all: "disabled",
        ec2InstanceNoPublicIP: "mandatory",
        elbAccessLoggingEnabled: "mandatory",
    });
    ```

    To specify additional configuration for policies that support it:

    ```typescript
    new AwsGuard({
        ec2VolumeInUseCheck: { checkDeletion: false },
        encryptedVolumes: { enforcementLevel: "mandatory", kmsId: "id" },
        redshiftClusterMaintenanceSettingsCheck: { preferredMaintenanceWindow: "Mon:09:30-Mon:10:00" },
        acmCheckCertificateExpiration: { maxDaysUntilExpiration: 10 },
    });
    ```

### Test the new Policy Pack

Policy Packs can be tested on a user's local workstation to facilitate rapid development and testing of policies.

1. Run `npm install` in the Policy Pack directory.

1. Use the `--policy-pack` flag with `pulumi preview` or `pulumi up` to specify the path to the directory containing your Policy Pack when previewing/updating a Pulumi program.

    If you don’t have a Pulumi program readily available, you can create a new project for testing by running `pulumi new aws-typescript` in an empty directory. This AWS example will create an S3 bucket, which is perfect for testing our Policy.

    In the Pulumi project's directory run:

    {{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

```sh
$ PULUMI_EXPERIMENTAL=true pulumi preview --policy-pack <path-to-policy-pack-directory>
```

{{% /choosable %}}

{{% choosable os linux %}}

```sh
$ PULUMI_EXPERIMENTAL=true pulumi preview --policy-pack <path-to-policy-pack-directory>
```

{{% /choosable %}}

{{% choosable os windows %}}

Windows cmd.exe:

```bat
> set PULUMI_EXPERIMENTAL=true
> pulumi preview --policy-pack <path-to-policy-pack-directory>
```

Windows PowerShell:

```powershell
> $env:PULUMI_EXPERIMENTAL = 'true'
> pulumi preview --policy-pack <path-to-policy-pack-directory>
```

{{% /choosable %}}

{{< /chooser >}}

    If the stack is not in compliance, the policy violation will be displayed. Since the enforcement level for all policies are set to advisory, a warning is shown for any resources that are not in compliance with the AWSGuard policies. In this case, logging must be defined for S3 buckets.

    {{< highlight sh >}}
Previewing update (dev):

    Type                 Name           Plan       Info
+   pulumi:pulumi:Stack  test-dev       create
+   └─ aws:s3:Bucket     my-bucket      create     1 warning

Diagnostics:
aws:s3:Bucket (my-bucket):
    advisory: [s3-bucket-logging-enabled] Checks whether logging is enabled for your S3 buckets.
    Bucket logging must be defined.

Resources:
    + 2 to create
{{< /highlight >}}

1. If you had wanted the preview to fail for any policy violations, the Policy Pack can be modified to configure all policies to be mandatory.

    ```typescript
    new AwsGuard({ all: "mandatory" });
    ```

1. Running the `pulumi preview` command again will now fail the preview operation.

    {{< highlight sh >}}
Previewing update (dev):

    Type                 Name           Plan       Info
+   pulumi:pulumi:Stack  test-dev       create     1 error
+   └─ aws:s3:Bucket     my-bucket      create     1 error

Diagnostics:
pulumi:pulumi:Stack (test-dev):
    error: preview failed

aws:s3:Bucket (my-bucket):
    mandatory: [s3-bucket-logging-enabled] Checks whether logging is enabled for your S3 buckets.
    Bucket logging must be defined.
{{< /highlight >}}

1. If you do not want to enforce this particular policy, you can modify the Policy Pack to disable it.

    ```typescript
    new AwsGuard({
        all: "mandatory",
        s3BucketLoggingEnabled: "disabled",
    });
    ```

## Next Steps

Once you've validated the behavior of the AWSGuard policies you've configured in your Policy Pack, an organization administrator can publish the Policy Pack to the Pulumi Console to be enforced across your organization. To learn more see [Enforcing a Policy Pack Across an Organization]({{< relref "/docs/get-started/crossguard/enforcing-a-policy-pack" >}}).

Now that you've seen how to configure and use AWSGuard policies, you may want to write your own policies. See the [Getting Started tutorial]({{< relref "/docs/get-started/crossguard" >}}) to get started.
