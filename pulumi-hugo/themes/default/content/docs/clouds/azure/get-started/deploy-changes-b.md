---
title_tag: Deploy the Changes | Azure
meta_desc: Learn how to deploy changes to an Azure project in this guide.
title: Deploy changes
h1: "Pulumi & Azure: Deploy changes"
block_external_search_index: true
---

Deploy your changes by using `pulumi up` again.

```bash
$ pulumi up
```

Pulumi will run the `preview` step of the update, which computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                                                   Name                 Plan
     pulumi:pulumi:Stack                                    quickstart-dev
 +   ├─ azure-native:storage:StorageAccountStaticWebsite    staticWebsite        create
 +   └─ azure-native:storage:Blob                           index.html           create

Outputs:
  + staticEndpoint   : "https://sa8dd8af62.z22.web.core.windows.net/"

Resources:
    + 2 to create
    3 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choosing `yes` will proceed with the update by uploading the `index.html` file to a storage container in your account and enabling static website support on the container.

```
Do you want to perform this update? yes
Updating (dev):

     Type                                                   Name                Status
     pulumi:pulumi:Stack                                    quickstart-dev
 +   ├─ azure-native:storage:StorageAccountStaticWebsite    staticWebsite       created
 +   └─ azure-native:storage:Blob                           index.html          created

Outputs:
    primaryStorageKey: "<key_value>"
  + staticEndpoint   : "https://sa8dd8af62.z22.web.core.windows.net/"

Resources:
    + 2 created
    3 unchanged

Duration: 4s
```

You can check out your new static website at the URL in the `Outputs` section of your update or you can make a `curl` request and see the contents of your `index.html` object printed out in your terminal.

{{% choosable language typescript %}}

```bash
$ curl $(pulumi stack output staticEndpoint)
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ curl $(pulumi stack output staticEndpoint)
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ curl $(pulumi stack output staticEndpoint)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ curl $(pulumi stack output staticEndpoint)
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ curl $(pulumi stack output staticEndpoint)
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ curl $(pulumi stack output staticEndpoint)
```

{{% /choosable %}}

And in a few moments, you should see:

```bash
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

Now that you have deployed your site, you will destroy the resources.

<div class="mt-6">
    <a data-track="previous-step" class="btn btn-secondary" href="/docs/clouds/azure/get-started/modify-program-b/">&larr; Previous Step</a>
    <a data-track="next-step" class="btn" href="/docs/clouds/azure/get-started/destroy-stack-b/">Destroy Stack &rarr;</a>
</div>
