---
title: Destroy the Stack
weight: 10
menu:
  quickstart:
    parent: aws
    identifier: aws-destroy-stack
---

Now that we've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of our stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

You'll be prompted to make sure you really want to delete these resources. This can take a minute or two; Pulumi waits for the EC2 instance to finish shutting down before it considers the destroy operation to be complete.

```
Previewing destroy (dev):

     Type                      Name            Plan
 -   pulumi:pulumi:Stack       quickstart-dev  delete
 -   ├─ aws:ec2:Instance       web-server-www  delete
 -   └─ aws:ec2:SecurityGroup  web-secgrp      delete

Resources:
    - 3 to delete

Do you want to perform this destroy? yes
Destroying (dev):

     Type                      Name            Status
 -   pulumi:pulumi:Stack       quickstart-dev  deleted
 -   ├─ aws:ec2:Instance       web-server-www  deleted
 -   └─ aws:ec2:SecurityGroup  web-secgrp      deleted

Resources:
    - 3 deleted

Duration: 36s
```

To delete the stack itself, run `pulumi stack rm`.

Next, we'll look at some next steps.

{{< get-started-stepper >}}
