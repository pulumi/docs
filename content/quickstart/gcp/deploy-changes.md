---
title: Deploy the Changes
weight: 8
menu:
  quickstart:
    parent: gcp
    identifier: gcp-deploy-changes
---

Now let's deploy our changes.

```bash
$ pulumi up
```

Pulumi computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                     Name            Plan
     pulumi:pulumi:Stack      quickstart-dev
 +   ├─ gcp:compute:Network   network         create
 +   ├─ gcp:compute:Firewall  firewall        create
 +   ├─ gcp:compute:Instance  instance        create
 -   └─ gcp:storage:Bucket    my-bucket       delete

Resources:
    + 3 to create
    - 1 to delete
    2 changes. 1 unchanged

Do you want to perform this update?
  yes
> no
  details
```

Pulumi will delete the bucket since we're no longer defining it in our program, and it will create the network, firewall, and compute instance resources since those are now defined in the program.

Choosing `yes` will proceed with the update.

```
Do you want to perform this update? yes
Updating (dev):

     Type                     Name            Status
     pulumi:pulumi:Stack      quickstart-dev
 +   ├─ gcp:compute:Network   network         created
 +   ├─ gcp:compute:Firewall  firewall        created
 +   ├─ gcp:compute:Instance  instance        created
 -   └─ gcp:storage:Bucket    my-bucket       deleted

Outputs:
  - bucketName: "gs://my-bucket-62f8bc7"
  + ip        : "35.222.165.202"

Resources:
    + 3 created
    - 1 deleted
    2 changes. 1 unchanged

Duration: 1m48s
```

We can use `pulumi stack output` to get the value of [stack outputs]({{< relref "/reference/stack.md#outputs" >}}) from the CLI. So we can `curl` the endpoint to see the HTTP server running there.

```bash
$ curl $(pulumi stack output ip)
Hello, World!
```

Next, we'll destroy the stack.

{{< get-started-stepper >}}
