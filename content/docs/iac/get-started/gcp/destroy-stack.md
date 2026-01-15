---
title_tag: Destroy the Stack | Google Cloud
title: Destroy stack
h1: "Get started with Pulumi and Google Cloud"
meta_desc: This page provides an overview of how to destroy a Pulumi stack of a Google Cloud project.
weight: 8
menu:
    iac:
        name: Cleanup & destroy
        identifier: gcp-get-started.destroy-stack
        parent: gcp-get-started
        weight: 8

aliases:
    - /docs/quickstart/gcp/destroy-stack/
    - /docs/clouds/gcp/get-started/destroy-stack/
---

## Cleanup & destroy the stack

Our final step is to clean up all of the resources we've allocated in this tutorial.

Run the `pulumi destroy` command to delete all cloud resources in this project/stack:

{{% choosable os "linux,macos" %}}

```bash
$ pulumi destroy
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> pulumi destroy
```

{{% /choosable %}}

Just like `pulumi up`, you'll be shown a preview to ensure that you want to proceed:

```
Previewing destroy (dev):

     Type                             Name               Plan
 -   pulumi:pulumi:Stack              quickstart-dev     delete
 -   ├─ gcp:storage:BucketIAMBinding  my-bucket-binding  delete
 -   ├─ gcp:storage:BucketObject      index.html         delete
 -   └─ gcp:storage:Bucket            my-bucket          delete

Outputs:
  - url       : "http://storage.googleapis.com/my-bucket-daa12be/index.html"

Resources:
    - 4 to delete

Do you want to perform this destroy?
> yes
  no
  details
```

As with an update, we can choose `no` or `details`; select `yes` to proceed:

```
Destroying (dev):

     Type                             Name               Status
 -   pulumi:pulumi:Stack              quickstart-dev     deleted (0.31s)
 -   ├─ gcp:storage:BucketIAMBinding  my-bucket-binding  deleted (6s)
 -   ├─ gcp:storage:BucketObject      index.html         deleted (0.78s)
 -   └─ gcp:storage:Bucket            my-bucket          deleted (1s)

Outputs:
  - url       : "http://storage.googleapis.com/my-bucket-daa12be/index.html"

Resources:
    - 4 deleted

Duration: 9s
```

At this stage, your stack still exists, but all cloud resources have been deleted from it.

## Remove the stack

The final step is to remove the stack itself. Destroy keeps the stack around so that you still have the full
history of what happened to the stack. Running [`pulumi stack rm`](/docs/cli/commands/pulumi_stack_rm) will
delete it entirely, including all history and state snapshots. Be careful, this step cannot be undone!

{{% choosable "os" "macos,linux" %}}

```bash
$ pulumi stack rm
```

{{% /choosable %}}
{{% choosable "os" "windows" %}}

```powershell
> pulumi stack rm
```

{{% /choosable %}}

You'll be prompted to confirm the removal. Confirm it to successfully complete this tutorial.

{{< get-started-stepper >}}
