---
title: Destroy the Stack
weight: 10
menu:
  getstarted:
    parent: kubernetes
    identifier: kubernetes-destroy-stack
---

Now that we've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of our stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

You'll be prompted to make sure you really want to delete these resources.

```
Previewing destroy (dev):

     Type                           Name            Plan
 -   pulumi:pulumi:Stack            quickstart-dev  delete
 -   ├─ kubernetes:core:Service     nginx           delete
 -   └─ kubernetes:apps:Deployment  nginx           delete

Resources:
    - 3 to delete

Do you want to perform this destroy? yes
Destroying (dev):

     Type                           Name            Status
 -   pulumi:pulumi:Stack            quickstart-dev  deleted
 -   ├─ kubernetes:core:Service     nginx           deleted
 -   └─ kubernetes:apps:Deployment  nginx           deleted

Resources:
    - 3 deleted

Duration: 1s
```

To delete the stack itself, run `pulumi stack rm`.

Next, we'll look at some next steps.

{{< get-started-stepper >}}
