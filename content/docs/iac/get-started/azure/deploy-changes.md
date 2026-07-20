---
title_tag: Deploy the Changes | Azure
title: Deploy the changes
h1: "Deploy the changes"
meta_desc: Learn how to deploy changes to an Azure + Pulumi project in this guide.
weight: 8
menu:
    iac:
        name: Deploy the changes
        identifier: azure-get-started.deploy-changes
        parent: azure-get-started
        weight: 8
aliases:
    - /docs/get-started/azure/deploy-changes/
    - /docs/quickstart/azure/deploy-changes/
    - /docs/clouds/azure/get-started/deploy-changes/
---

Now deploy the changes with `pulumi up`. Pulumi computes the minimal set of changes needed to reach your program's new desired state, leaving unchanged resources as-is:

```bash
$ pulumi up
```

As before, you'll see a preview of the resources to be created:

```
Previewing update (dev):

     Type                                                   Name             Plan
     pulumi:pulumi:Stack                                    quickstart-dev
 +   ├─ azure-native:storage:StorageAccountStaticWebsite    staticWebsite    create
 +   └─ azure-native:storage:Blob                           index.html       create

Outputs:
  + staticEndpoint: "https://sa8deefa78.z22.web.core.windows.net/"

Resources:
    + 2 to create
    3 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choose `yes` to proceed with the update, and in a few seconds, the website will be live. You can `curl` the endpoint with `pulumi stack output` to see it:

{{% choosable os "linux,macos" %}}

```bash
$ curl $(pulumi stack output staticEndpoint)
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> curl (pulumi stack output staticEndpoint)
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
