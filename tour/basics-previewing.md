---
title: Previewing
---

Pulumi lets you preview changes before carrying them out.

This applies both for your first deployment and all subsequent ones.

From your project's working directory, simply run `pulumi preview`.  This will run your program and show you a summary
of all changes that would be made if you were to proceed with your update.

```bash
$ pulumi preview
Previewing update of stack 'ahoy-pulumi-dev'
Previewing changes:

     Type                 Name                          Plan
 +   pulumi:pulumi:Stack  ahoy-pulumi-ahoy-pulumi-dev   create
 +   └─ aws:s3:Bucket     my-bucket                     create

info: 2 changes previewed:
    + 2 resources to create
```

This simply says that deploying `ahoy-pulumi` will create two resources:

* A `pulumi:pulumi:Stack`, which is a logical container for all resources in your stack
* A physical `aws:s3:Bucket`, named `my-bucket`, representing the `Bucket` object created by your program

Any stdout, stderr, or unhandled error diagnostics will be shown as part of the summary output.

Preview can be run before you've stood up your program the first time, or before making any subsequent updates to it.

Remember, no changes have been made to your cloud yet!

***

Now that we've successfully previewed an update, let's do it for real.

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-deploying.html" title="Deploying code">◀</a>
    <span class="tour-index"><strong>5</strong>/8</span>
    <a class="tour-button enabled" href="basics-up.html" title="Spinning up">▶</a>
</div>
