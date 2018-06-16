---
title: Destroying
---

Finally, if we want to delete all of our resources from the cloud, we can run the appropriately-alarming named
`pulumi destroy` command.  This will delete all resources in your stack.

Just like the `update` command, `destroy` will show you a preview of its actions first, followed by a prompt.

```bash
$ pulumi destroy
Previewing destroy of stack 'ahoy-pulumi-dev'
Previewing changes:

     Type                 Name                          Plan
 -   pulumi:pulumi:Stack  ahoy-pulumi-ahoy-pulumi-dev   delete
 -   └─ aws:s3:Bucket     my-bucket                     delete

info: 2 changes previewed:
    - 2 resources to delete

Do you want to perform this destroy?
  yes
> no
  details
```

By selecting `yes`, the destruction will proceed:

```bash
$ pulumi destroy
...
Destroying stack 'ahoy-pulumi-dev'
Performing changes:

     Type                 Name                          Status
 -   pulumi:pulumi:Stack  ahoy-pulumi-ahoy-pulumi-dev   deleted
 -   └─ aws:s3:Bucket     my-bucket                     deleted

info: 2 changes performed:
    - 2 resources deleted
Update duration: 4.236708384s

Permalink: https://app.pulumi.com/broomllc/ahoy-pulumi-dev/updates/3
```

Although we have deleted the resources, our stack will still exist.  To remove it too, run `pulumi stack rm`:

> Be extremely careful when doing this operation.  It will remove all history and is, at the moment, irrecoverable!

```bash
$ pulumi stack rm
This will permanently remove the 'ahoy-pulumi-dev' stack!
Please confirm that this is what you'd like to do by typing ("ahoy-pulumi-dev"): ahoy-pulumi-dev
Stack 'ahoy-pulumi-dev' has been removed!
```

***

That concludes our first lesson.  Please proceed to learn a bit more about the concepts we've just encountered and
how to extend this basic knowledge to build even more powerful cloud programs using Pulumi.

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-previewing.html" title="Performing updates">◀</a>
    <span class="tour-index"><strong>8</strong>/8</span>
    <a class="tour-button enabled" href="programs.html" title="Beyond the Basics">▶</a>
</div>
