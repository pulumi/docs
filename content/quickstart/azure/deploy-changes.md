---
title: Deploy the Changes
weight: 8
menu:
  quickstart:
    parent: azure
    identifier: azure-deploy-changes
---

Now let's deploy our changes.

```bash
$ pulumi up
```

Pulumi computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                             Name            Plan
     pulumi:pulumi:Stack              quickstart-dev
 +   ├─ azure:containerservice:Group  nginx           create
 -   └─ azure:storage:Account         storage         delete

Resources:
    + 1 to create
    - 1 to delete
    2 changes. 2 unchanged

Do you want to perform this update?
  yes
> no
  details
```

Pulumi will delete the storage account since we're no longer defining it in our program, and it will create the container group since it is now defined in the program. The resource group hasn't changed so it remains as-is.

Choosing `yes` will proceed with the update.

```
Do you want to perform this update? yes
Updating (dev):

     Type                             Name            Status
     pulumi:pulumi:Stack              quickstart-dev
 +   ├─ azure:containerservice:Group  nginx           created
 -   └─ azure:storage:Account         storage         deleted

Outputs:
  - connectionString: "DefaultEndpointsProtocol=https;AccountName=storagec10b9cad;AccountKey=f5JxKN8M7mECDlzdB9zTwfJWSplo8jFTFFKRTzGAldscILf1ftrJPaspSA69tzLe24WBbWJ9yTu+mzjaqmPEew==;EndpointSuffix=core.windows.net"
  + ip              : "40.85.154.213"

Resources:
    + 1 created
    - 1 deleted
    2 changes. 2 unchanged

Duration: 1m11s
```

We can use `pulumi stack output` to get the value of [stack outputs]({{< relref "/reference/stack.md#outputs" >}}) from the CLI. So we can `curl` the endpoint.

```bash
$ curl $(pulumi stack output ip)
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

Next, we'll destroy the stack.

{{< get-started-stepper >}}
