---
title: Destroy the Stack
weight: 10
menu:
  get-started:
    parent: gcp
    identifier: gcp-destroy-stack
---

Now that we've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of our stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

You'll be prompted to make sure you really want to delete these resources. This can take several minutes; Pulumi waits for the virtual machine instance to shutdown and for the compute network to be removed before it considers the destroy operation to be complete.

```
Previewing destroy (dev):

     Type                     Name            Plan
 -   pulumi:pulumi:Stack      quickstart-dev  delete
 -   ├─ gcp:compute:Instance  instance        delete
 -   ├─ gcp:compute:Firewall  firewall        delete
 -   └─ gcp:compute:Network   network         delete

Resources:
    - 4 to delete

Do you want to perform this destroy? yes
Destroying (dev):

     Type                     Name            Status
 -   pulumi:pulumi:Stack      quickstart-dev  deleted
 -   ├─ gcp:compute:Instance  instance        deleted
 -   ├─ gcp:compute:Firewall  firewall        deleted
 -   └─ gcp:compute:Network   network         deleted

Resources:
    - 4 deleted

Duration: 6m1s
```

To delete the stack itself, run `pulumi stack rm`.

Next, we'll look at some next steps.

{{< get-started-stepper >}}
