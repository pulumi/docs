---
title_tag: Deploy the Changes | Google Cloud
title: Deploy the changes
h1: "Deploy the changes"
meta_desc: Learn how to deploy changes to a Google Cloud + Pulumi project in this guide.
weight: 8
menu:
    iac:
        name: Deploy the changes
        identifier: gcp-get-started.deploy-changes
        parent: gcp-get-started
        weight: 8
aliases:
    - /docs/get-started/gcp/deploy-changes/
    - /docs/quickstart/gcp/deploy-changes/
    - /docs/clouds/gcp/get-started/deploy-changes/
---

Now deploy the changes with `pulumi up`. Pulumi computes the minimal set of changes needed to reach your program's new desired state, leaving unchanged resources as-is:

```bash
$ pulumi up
```

As before, you'll see a preview of the changes to be made:

```
Previewing update (dev):

     Type                             Name               Plan
     pulumi:pulumi:Stack              quickstart-dev
 +   ├─ gcp:storage:BucketObject      index.html         create
 +   ├─ gcp:storage:BucketIAMBinding  my-bucket-binding  create
 ~   └─ gcp:storage:Bucket            my-bucket          update

Outputs:
  + url: "http://storage.googleapis.com/my-bucket-daa12be/index.html"

Resources:
    + 2 to create
    ~ 1 to update
    3 changes. 1 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choose `yes` to proceed with the update, and in a few seconds, the website will be live. You can `curl` the endpoint with `pulumi stack output` to see it:

```bash
$ curl $(pulumi stack output url)
```

```
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

Feel free to experiment. Try changing the contents of `index.html` and running `pulumi up` again.

Next you'll finish up by destroying the resources you created.

{{< get-started-stepper >}}
