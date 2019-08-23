---
title: Deploy the Changes
weight: 9
menu:
  getstarted:
    parent: azure
    identifier: azure-deploy-changes

aliases: ["/docs/quickstart/azure/deploy-changes/"]
---

Now let's deploy our changes.

```bash
$ pulumi up
```

Pulumi computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                      Name                     Plan       Info
     pulumi:pulumi:Stack       update-az-templates-dev             
 ~   └─ azure:storage:Account  storage                  update     [diff: ~enableHttpsTrafficOnly]
 
Resources:
    ~ 1 to update
    2 unchanged

Do you want to perform this update?
  yes
> no
  details
```

Pulumi will update the storage account to enable the HTTPS-only enforcement. The resource group hasn't changed so it remains as-is.

Choosing `yes` will proceed with the update.

```
Do you want to perform this update? yes
Updating (dev):

     Type                      Name                     Status      Info
     pulumi:pulumi:Stack       update-az-templates-dev              
 ~   └─ azure:storage:Account  storage                  updated     [diff: ~enableHttpsTrafficOnly]

Outputs:
    connectionString: "DefaultEndpointsProtocol=https;AccountName=storagefeda4143;AccountKey=...;EndpointSuffix=core.windows.net"

Resources:
<<<<<<< HEAD
    ~ 1 updated
    2 unchanged
=======
    + 1 created
    - 1 deleted
    2 changes. 2 unchanged

Duration: 1m11s
```

We can use `pulumi stack output` to get the value of [stack outputs]({{< relref "/docs/intro/concepts/stack.md#outputs" >}}) from the CLI. So we can `curl` the endpoint.

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
>>>>>>> 1a65311f... Intermediate commit for fixing paths

Duration: 4s
```

Next, we'll destroy the stack.

{{< get-started-stepper >}}
