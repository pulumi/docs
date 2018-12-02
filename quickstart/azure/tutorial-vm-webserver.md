---
title: "Tutorial: Web Server Virtual Machine Instance"
---

In this tutorial, we'll use JavaScript to deploy a simple webserver Virtual Machine instance to Azure. The [code for this tutorial](https://github.com/pulumi/examples/tree/master/azure-js-webserver) is available on GitHub. 

## Prerequisites

1.  [Install Pulumi](../install.html)
1.  [Configure Azure credentials](./setup.html)

## Create a Virtual Machine with SSH access {#webserver}

1.  In a new folder `webserver`, create an empty project with `pulumi new`. Make sure you have run `az login` or configured credentials for Azure.
    ```
    $ pulumi new gcp-javascript --dir webserver
    $ cd webserver
    ```

1.  Open `index.js` and replace the contents with the following:

    ```javascript
    const pulumi = require("@pulumi/pulumi");
    const azure = require("@pulumi/azure");

    let config = new pulumi.Config();
    let username = config.require("username");
    let password = config.require("password");

    let resourceGroup = new azure.core.ResourceGroup("server", {
        location: "West US",
    });

    let network = new azure.network.VirtualNetwork("server-network", {
        resourceGroupName: resourceGroup.name,
        location: resourceGroup.location,
        addressSpaces: ["10.0.0.0/16"],
        // Workaround two issues:
        // (1) The Azure API recently regressed and now fails when no subnets are defined at Network creation time.
        // (2) The Azure Terraform provider does not return the ID of the created subnets - so this cannot actually be used.
        subnets: [{
            name: "default",
            addressPrefix: "10.0.1.0/24",
        }],
    });

    let subnet = new azure.network.Subnet("server-subnet", {
        resourceGroupName: resourceGroup.name,
        virtualNetworkName: network.name,
        addressPrefix: "10.0.2.0/24",
    });

    let publicIP = new azure.network.PublicIp("server-ip", {
        resourceGroupName: resourceGroup.name,
        location: resourceGroup.location,
        publicIpAddressAllocation: "Dynamic",
    });

    let networkInterface = new azure.network.NetworkInterface("server-nic", {
        resourceGroupName: resourceGroup.name,
        location: resourceGroup.location,
        ipConfigurations: [{
            name: "webserveripcfg",
            subnetId: subnet.id,
            privateIpAddressAllocation: "Dynamic",
            publicIpAddressId: publicIP.id,
        }],
    });

    let userData = 
    `#!/bin/bash
    echo "Hello, World!" > index.html
    nohup python -m SimpleHTTPServer 80 &`;

    let vm = new azure.compute.VirtualMachine("server-vm", {
        resourceGroupName: resourceGroup.name,
        location: resourceGroup.location,
        networkInterfaceIds: [networkInterface.id],
        vmSize: "Standard_A0",
        deleteDataDisksOnTermination: true,
        deleteOsDiskOnTermination: true,
        osProfile: {
            computerName: "hostname",
            adminUsername: username,
            adminPassword: password,
            customData: userData,
        },
        osProfileLinuxConfig: {
            disablePasswordAuthentication: false,
        },
        storageOsDisk: {
            createOption: "FromImage",
            name: "myosdisk1",
        },
        storageImageReference: {
            publisher: "canonical",
            offer: "UbuntuServer",
            sku: "16.04-LTS",
            version: "latest",
        },
    });

    // The public IP address is not allocated until the VM is running, so we wait
    // for that resource to create, and then lookup the IP address again to report
    // its public IP.
    exports.publicIP = pulumi.all({ id: vm.id, name: publicIP.name, resourceGroupName: publicIP.resourceGroupName }).apply(ip =>
        azure.network.getPublicIP({
            name: ip.name,
            resourceGroupName: ip.resourceGroupName,
        }).then(ip => ip.ipAddress)
    );
    ```

    This example uses the [@pulumi/azure](https://pulumi.io/reference/pkg/nodejs/@pulumi/azure/) package to create and manage several Azure resources including: an [azure.core.ResourceGroup](https://pulumi.io/reference/pkg/nodejs/@pulumi/azure/core/#ResourceGroup) in which all other resources will live, an [azure.network.VirtualNetwork](https://pulumi.io/reference/pkg/nodejs/@pulumi/azure/network/#VirtualNetwork) and related subnet and network interface, and an [azure.compute.VirtualMachine](https://pulumi.io/reference/pkg/nodejs/@pulumi/azure/compute/#VirtualMachine) in that network running Ubuntu.


1.  To preview and deploy changes, run `pulumi update`. The command shows a preview of the resources that will be created and prompts on whether to proceed with the deployment.  Note that the stack itself is counted as a resource, though it does not correspond to a physical cloud resource.

    ```bash
    $ pulumi update
    Previewing update (azurewebserver-dev):

        Type                               Name                               Plan
    +   pulumi:pulumi:Stack                azurewebserver-azurewebserver-dev  create
    +   ├─ azure:core:ResourceGroup        server                             create
    +   ├─ azure:network:VirtualNetwork    server-network                     create
    +   ├─ azure:network:Subnet            server-subnet                      create
    +   ├─ azure:network:NetworkInterface  server-nic                         create
    +   └─ azure:compute:VirtualMachine    server-vm                          create

    Resources:
        + 6 to create
    ```

1.  Now, proceed with the deployment, which will take a couple minutes to complete. 

    ```bash
    Do you want to perform this update? yes
    Updating (azurewebserver-dev):

        Type                               Name                               Status
    +   pulumi:pulumi:Stack                azurewebserver-azurewebserver-dev  created
    +   ├─ azure:core:ResourceGroup        server                             created
    +   ├─ azure:network:VirtualNetwork    server-network                     created
    +   ├─ azure:network:Subnet            server-subnet                      created
    +   ├─ azure:network:NetworkInterface  server-nic                         created
    +   └─ azure:compute:VirtualMachine    server-vm                          created

    Outputs:
        privateIP: "10.0.1.4"

    Resources:
        + 6 created

    Duration: 2m5s

    Permalink: https://app.pulumi.com/lukehoban/azurewebserver-dev/updates/1
    ```

    To see the full details of the deployment and the resources that are now part of the stack, open the update permalink in a browser.

1.  To view the provisioned resources on the command line, run `pulumi stack`. You'll also see a [stack output](/reference/stack.html#output) corresponding to the private IP address of the virtual machine instance we've created.  

    ```
    $ pulumi stack
    ...
    Current stack resources (7):
        TYPE                                             NAME
        pulumi:pulumi:Stack                              azurewebserver-azurewebserver-dev
        pulumi:providers:azure                           default
        azure:core/resourceGroup:ResourceGroup           server
        azure:network/virtualNetwork:VirtualNetwork      server-network
        azure:network/subnet:Subnet                      server-subnet
        azure:network/networkInterface:NetworkInterface  server-nic
        azure:compute/virtualMachine:VirtualMachine      server-vm

    Current stack outputs (1):
        OUTPUT                                           VALUE
        privateIP                                        10.0.1.4
    ```

## Clean up

Before moving on, let's tear down the resources that are part of our stack.

1.  Run `pulumi destroy` to tear down all resources.  You'll be prompted to make sure you really want to delete these resources. This takes about 60 seconds; Pulumi waits for the virtual machine instance to shutdown and for the compute network to be removed before it considers the destroy operation to be complete.

1.  To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Console.

## Summary

In this tutorial, we saw how to use Pulumi programs to create and manage cloud resources in Google Cloud, using regular JavaScript and NPM packages. To preview and update infrastructure, use `pulumi update`. To clean up resources, run `pulumi destroy`.

For a similar example in other languages and clouds, see the [Web Server examples collection](https://github.com/pulumi/examples#web-server).
