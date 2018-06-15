---
title: Spinning up
---

As soon as we're ready to deploy changes, we can run `pulumi update` (or `pulumi up`, for short).

This will re-run our program and show us a preview again.  Because of this, we don't necessarily need to run
`pulumi preview` manually each time.  If you want to be safe, however, it's always there for you when you need it.

Running `pulumi up` will show us all the same things we just saw, followed by a prompt:

```bash
$ pulumi update
Previewing update of stack 'ahoy-pulumi-dev'
Previewing changes:

     Type                 Name                          Plan
 +   pulumi:pulumi:Stack  ahoy-pulumi-ahoy-pulumi-dev   create
 +   └─ aws:s3:Bucket     my-bucket                     create

info: 2 changes previewed:
    + 2 resources to create

Do you want to perform this update?
> yes
  no
  details
```

To proceed, select the `yes` option (or, alternatively, `details` to see a full diff view).  If you want to skip the
preview because you've already done it, pass `--skip-preview`, and to auto-confirm the update, pass `--yes`.

Proceeding with the update will actually provision our resources in the cloud:

```bash
Updating stack 'ahoy-pulumi-dev'
Performing changes:

     Type                 Name                          Status
 +   pulumi:pulumi:Stack  ahoy-pulumi-ahoy-pulumi-dev   created
 +   └─ aws:s3:Bucket     my-bucket                     created

info: 2 changes performed:
    + 2 resources created
Update duration: 8.374486431s

Permalink: https://app.pulumi.com/broomllc/ahoy-pulumi-dev/updates/1
```

At the end, we'll find a link to the Pulumi service that we can use to see detailed history for our program.

***

Now that we've stood up our first program, let's see how to update it incrementally afterwards.

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-previewing.html" title="Previewing">◀</a>
    <span class="tour-index"><strong>6</strong>/8</span>
    <a class="tour-button enabled" href="basics-updating.html" title="Performing updates">▶</a>
</div>
