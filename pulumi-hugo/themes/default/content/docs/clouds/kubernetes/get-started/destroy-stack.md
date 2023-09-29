---
title_tag: Destroy the Stack | Kubernetes
meta_desc: This page provides an overview of how to destroy a Pulumi stack of a Kubernetes project.
title: Destroy stack
h1: "Pulumi & Kubernetes: Destroy stack"
weight: 8
menu:
  clouds:
    parent: kubernetes-get-started
    identifier: kubernetes-destroy-stack

aliases:
- /docs/quickstart/kubernetes/destroy-stack/
- /docs/get-started/kubernetes/destroy-stack/
---

Now that we've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of our stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

You'll be prompted to make sure you really want to delete these resources.

```bash
Previewing destroy (dev)

     Type                              Name            Plan
 -   pulumi:pulumi:Stack               quickstart-dev  delete
 -   ├─ kubernetes:core/v1:Service     nginx           delete
 -   └─ kubernetes:apps/v1:Deployment  nginx           delete


Outputs:
  - ip: "10.103.199.118"

Resources:
    - 3 to delete

Do you want to perform this destroy?  [Use arrows to move, type to filter]
  yes
> no
  details
```

Select `yes` using the arrows and hit enter to delete the resources in Kubernetes.

```bash
Do you want to perform this destroy? yes
Destroying (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/diana-pulumi-corp/quickstart/dev/updates/3

     Type                              Name            Status
 -   pulumi:pulumi:Stack               quickstart-dev  deleted
 -   ├─ kubernetes:core/v1:Service     nginx           deleted (0.42s)
 -   └─ kubernetes:apps/v1:Deployment  nginx           deleted (2s)


Outputs:
  - ip: "10.103.199.118"

Resources:
    - 3 deleted

Duration: 5s

The resources in the stack have been deleted, but the history and configuration associated with the stack are still maintained.
If you want to remove the stack completely, run `pulumi stack rm dev`.
```

To delete the stack itself, run [`pulumi stack rm`](/docs/cli/commands/pulumi_stack_rm). Note that this removes the stack
entirely from the Pulumi Cloud, along with all of its update history.

```bash
$ pulumi stack rm
This will permanently remove the 'dev' stack!
Please confirm that this is what you`d like to do by typing `dev`:
```

Type `dev` and hit enter to remove the stack.

```bash
Please confirm that this is what you`d like to do by typing `dev`: dev
Stack 'dev' has been removed!
```

Next, we'll look at some next steps.

{{< get-started-stepper >}}
