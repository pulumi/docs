---
title: Deploy the Changes
weight: 9
menu:
  quickstart:
    parent: aws
    identifier: aws-deploy-changes
---

Now let's deploy our changes.

```bash
$ pulumi up
```

Pulumi computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                      Name            Plan
     pulumi:pulumi:Stack       quickstart-dev
 +   ├─ aws:ec2:SecurityGroup  web-secgrp      create
 +   ├─ aws:ec2:Instance       web-server-www  create
 -   └─ aws:s3:Bucket          my-bucket       delete

Resources:
    + 2 to create
    - 1 to delete
    2 changes. 1 unchanged

Do you want to perform this update?
  yes
> no
  details
```

Pulumi will delete the bucket since we're no longer defining it in our program, and it will create the EC2 security group and EC2 instance since those are now defined in the program.

Choosing `yes` will proceed with the update.

```
Do you want to perform this update? yes
Updating (dev):

     Type                      Name            Status
     pulumi:pulumi:Stack       quickstart-dev
 +   ├─ aws:ec2:SecurityGroup  web-secgrp      created
 +   ├─ aws:ec2:Instance       web-server-www  created
 -   └─ aws:s3:Bucket          my-bucket       deleted

Outputs:
  - bucketName : "my-bucket-68e33ec"
  + host       : "ec2-3-86-229-103.compute-1.amazonaws.com"

Resources:
    + 2 created
    - 1 deleted
    2 changes. 1 unchanged

Duration: 44s
```

We can use `pulumi stack output` to get the value of [stack outputs]({{< relref "/reference/stack.md#outputs" >}}) from the CLI. So we can `curl` the EC2 instance to see the HTTP server running there.

```bash
$ curl $(pulumi stack output host)
Hello, World!
```

Next, we'll destroy the stack.

{{< get-started-stepper >}}
