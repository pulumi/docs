---
title_tag: Deploy the Changes | AWS
title: Deploy the changes
h1: "Deploy the changes"
meta_desc: Learn how to deploy changes to an AWS + Pulumi project in this guide.
weight: 8
menu:
    iac:
        name: Deploy the changes
        parent: aws-get-started
        weight: 8

aliases:
    - /docs/get-started/aws/deploy-changes/
    - /docs/quickstart/aws/deploy-changes/
    - /docs/clouds/aws/get-started/deploy-changes/
---

Now deploy the changes with `pulumi up`. Pulumi computes the minimal set of changes needed to reach your program's new desired state, leaving unchanged resources as-is:

```bash
$ pulumi up
```

As before, you'll see a preview of the resources to be created:

```
Previewing update (dev):

     Type                                    Name                 Plan       Info
     pulumi:pulumi:Stack                     quickstart-dev
 +   ├─ aws:s3:BucketWebsiteConfiguration    website              create
 +   ├─ aws:s3:BucketOwnershipControls       ownership-controls   create
 +   ├─ aws:s3:BucketPublicAccessBlock       public-access-block  create
 +   └─ aws:s3:BucketObject                  index.html           create

Outputs:
  + url: output<string>

Resources:
    + 4 to create
    4 changes. 1 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choose `yes` to proceed with the update, and in a few seconds, the website will be live. You can `curl` the endpoint with `pulumi stack output` to see it:

{{% choosable os "linux,macos" %}}

```bash
$ curl $(pulumi stack output url)
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> curl (pulumi stack output url)
```

{{% /choosable %}}

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
