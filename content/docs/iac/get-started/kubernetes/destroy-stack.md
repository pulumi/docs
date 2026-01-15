---
title_tag: Destroy the Stack | Kubernetes
meta_desc: This page provides an overview of how to destroy a Pulumi stack of a Kubernetes project.
title: Destroy stack
h1: "Get started with Pulumi and Kubernetes"
weight: 8
menu:
  iac:
    name: Cleanup & destroy
    identifier: kubernetes-get-started.destroy-stack
    parent: kubernetes-get-started
    weight: 8

aliases:
    - /docs/quickstart/kubernetes/destroy-stack/
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

```bash
Previewing destroy (dev):

     Type                                        Name            Plan
 -   pulumi:pulumi:Stack                         quickstart-dev  delete
 -   └─ quickstart:index:KubernetesNginxService  my-nginx        delete
 -      ├─ kubernetes:core/v1:Service            nginx           delete
 -      └─ kubernetes:apps/v1:Deployment         nginx           delete

Outputs:
  - ip: "172.183.217.156"

Resources:
    - 4 to delete

Do you want to perform this destroy?  [Use arrows to move, type to filter]
> yes
  no
  details
```

As with an update, we can choose `no` or `details`; select `yes` to proceed:

```
Do you want to perform this destroy? yes
Destroying (dev)

     Type                                        Name            Status
 -   pulumi:pulumi:Stack                         quickstart-dev  deleted (0.08s)
 -   └─ quickstart:index:KubernetesNginxService  my-nginx        deleted (0.08s)
 -      ├─ kubernetes:core/v1:Service            nginx           deleted (16s)
 -      └─ kubernetes:apps/v1:Deployment         nginx           deleted (0.59s)

Outputs:
  - ip: "172.183.217.156"

Resources:
    - 4 deleted

Duration: 18s
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
