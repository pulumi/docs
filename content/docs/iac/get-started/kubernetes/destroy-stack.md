---
title_tag: Destroy the Stack | Kubernetes
title: Destroy the stack
h1: "Destroy the stack"
meta_desc: This page provides an overview of how to destroy a Pulumi stack of a Kubernetes project.
weight: 9
menu:
    iac:
        name: Destroy the stack
        identifier: kubernetes-get-started.destroy-stack
        parent: kubernetes-get-started
        weight: 9
aliases:
    - /docs/quickstart/kubernetes/destroy-stack/
---

Now that you've seen how to provision and manage resources with Pulumi, you can clean up the resources you created. Run `pulumi destroy` to delete every cloud resource in the stack:

```bash
$ pulumi destroy
```

Once again, you'll see a preview before anything happens:

```
Previewing destroy (dev):

     Type                              Name            Plan
 -   pulumi:pulumi:Stack               quickstart-dev  delete
 -   ├─ kubernetes:core/v1:Service     nginx           delete
 -   └─ kubernetes:apps/v1:Deployment  nginx           delete

Outputs:
  - ip: "10.110.183.208"

Resources:
    - 3 to delete

Do you want to perform this destroy?
> yes
  no
  details
```

Choose `yes` to destroy the stack. When the operation completes, your cloud resources no longer exist, but the stack and its configuration settings still do. You can delete the stack, including all of its state and update history, with [`pulumi stack rm`](/docs/iac/cli/commands/pulumi_stack_rm/):

```bash
$ pulumi stack rm
```

Confirm the removal when prompted, and you're done.

{{< get-started-stepper >}}
