---
title: Deploy to Azure Container Instance (ACI)
meta_desc: This tutorial will teach you how to deploy a simple NGINX container to
           Azure Container Instance (ACI).
aliases: ["/docs/reference/tutorials/azure/tutorial-container-webserver/"]
---

In this tutorial, we'll use JavaScript to deploy a simple nginx container to Azure Container Instance (ACI).

## Prerequisites

1. [Install Pulumi]({{< relref "/docs/get-started/install" >}})
1. [Configure Azure credentials]({{< relref "/docs/intro/cloud-providers/azure/setup" >}})

## Create a container in Azure Container Instance {#ACI}

1. In a new folder `webserver`, create an empty project with `pulumi new`. Make sure you have run `az login` or configured credentials for Azure.

    ```bash
    $ mkdir webserver && cd webserver
    $ pulumi new azure-javascript
    ```

1. Open `index.js` and replace the contents with the following:

    ```javascript
    const pulumi = require("@pulumi/pulumi");
    const azure = require("@pulumi/azure");

    let resourceGroup = new azure.core.ResourceGroup("webserver", {
        location: "West US 2",
    });

    let container = new azure.containerservice.Group("nginx", {
        containers: [{
            name: "nginx",
            image: "nginx",
            memory: 1,
            cpu: 1,
            ports: [{
                    port: 80,
                    protocol: "TCP"
            }],
        }],
        osType: "Linux",
        resourceGroupName: resourceGroup.name,
        location: resourceGroup.location,
    });

    exports.publicIP = container.ipAddress;
    ```

    This example uses the [@pulumi/azure]({{< relref "/docs/reference/pkg/nodejs/pulumi/azure" >}}) package to create and manage two Azure resources including: an [azure.core.ResourceGroup]({{< relref "/docs/reference/pkg/nodejs/pulumi/azure/core#ResourceGroup" >}}) which will contain the ACI instance and [azure.containerservice.Group]({{< relref "/docs/reference/pkg/nodejs/pulumi/azure/containerservice#Group" >}}) which will run an `nginx` Docker container.

1. To preview and deploy changes, run `pulumi up`. The command shows a preview of the resources that will be created and prompts on whether to proceed with the deployment.  Note that the stack itself is counted as a resource, though it does not correspond to an actual cloud resource.

        $ pulumi up
        Previewing update (azurewebserver-dev):

            Type                             Name                               Plan
        +   pulumi:pulumi:Stack              azurewebserver-azurewebserver-dev  create
        +   ├─ azure:core:ResourceGroup      webserver                          create
        +   └─ azure:containerservice:Group  nginx                              create

        Resources:
            + 3 to create

1. Now, proceed with the deployment.

        Do you want to perform this update? yes
        Updating (azurewebserver-dev):

            Type                             Name                               Status
        +   pulumi:pulumi:Stack              azurewebserver-azurewebserver-dev  created
        +   ├─ azure:core:ResourceGroup      webserver                          created
        +   └─ azure:containerservice:Group  nginx                              created

        Outputs:
            publicIP: "13.66.202.166"

        Resources:
            + 3 created

        Duration: 10s

        Permalink: https://app.pulumi.com/lukehoban/azurewebserver-dev/updates/51

    To see the full details of the deployment and the resources that are now part of the stack, open the update permalink in a browser.

1. To view the provisioned resources on the command line, run `pulumi stack`. You'll also see a [stack output]({{< relref "/docs/intro/concepts/stack#output" >}}) corresponding to the private IP address of the nginx container we've created.

        $ pulumi stack
        ...
        Current stack resources (4):
            TYPE                                             NAME
            pulumi:pulumi:Stack                              azurewebserver-azurewebserver-dev
            pulumi:providers:azure                           default
            azure:core/resourceGroup:ResourceGroup           webserver
            azure:containerservice/group:Group               nginx

        Current stack outputs (1):
            OUTPUT                                           VALUE
            publicIP                                         13.66.202.166

1. Test out the container by `curl`ing the endpoint:

        $ curl $(pulumi stack output publicIP)
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

## Clean up

Before moving on, let's tear down the resources that are part of our stack.

1. Run `pulumi destroy` to tear down all resources.  You'll be prompted to make sure you really want to delete these resources. This takes some time; Pulumi waits for the ACI to shutdown and for the resource group to be removed before it considers the destroy operation to be complete.

1. To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Console.

## Summary

In this tutorial, we saw how to use Pulumi programs to create and manage cloud resources in Microsoft Azure, using regular JavaScript and NPM packages. To preview and update infrastructure, use `pulumi up`. To clean up resources, run `pulumi destroy`.
