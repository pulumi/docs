---
title: "Web Server Virtual Machine Instance"
menu:
  reference:
    parent: tutorials-gcp
---

In this tutorial, we'll use JavaScript to deploy a simple webserver Virtual Machine instance to Google Compute Engine. The [code for this tutorial](https://github.com/pulumi/examples/tree/master/gcp-js-webserver) is available on GitHub. 

## Prerequisites

1.  [Install Pulumi]({{< relref "/docs/reference/install.md" >}})
1.  [Configure GCP credentials]({{< relref "/docs/reference/clouds/gcp/setup.md" >}})

## Create a Virtual Machine with SSH access {#webserver}

1.  In a new folder `webserver`, create an empty project with `pulumi new`. Choose a Google Cloud `project` you have access to create Virtual Machines within.

    ```bash
    $ mkdir webserver && cd webserver
    $ pulumi new gcp-javascript
    ...
    gcp:project: The Google Cloud project to deploy into: <your project>
    ```

1.  Open `index.js` and replace the contents with the following:

    ```javascript
    const gcp = require("@pulumi/gcp");

    // Create a network
    const network = new gcp.compute.Network("network");
    const computeFirewall = new gcp.compute.Firewall("firewall", {
        network: network.id,
        allows: [{
            protocol: "tcp",
            ports: [ "22" ],
        }],
    });

    // Create a Virtual Machine Instance
    const computeInstance = new gcp.compute.Instance("instance", {
        machineType: "f1-micro",
        zone: "us-central1-a",
        bootDisk: { initializeParams: { image: "debian-cloud/debian-9" } },
        networkInterfaces: [{
            network: network.id,
            // accessConfigus must includ a single empty config to request an ephemeral IP
            accessConfigs: [{}], 
        }],
    });

    // Export the name and IP address of the Instance
    exports.instanceName = computeInstance.name;
    exports.instanceIP = computeInstance.networkInterfaces.apply(ni => ni[0].accessConfigs[0].natIp);
    ```

    This example uses the [@pulumi/gcp]({{< relref "/docs/reference/pkg/nodejs/pulumi/gcp" >}}) package to create and manage three Google Cloud resources: a [gcp.compute.Network]({{< relref "/docs/reference/pkg/nodejs/pulumi/gcp/compute#Network" >}}) in which the virtual machine will run, a [gcp.compute.Firewall]({{< relref "/docs/reference/pkg/nodejs/pulumi/gcp/compute#Firewall" >}}) which allows access for incoming SSH access, and a [gcp.compute.Instance]({{< relref "/docs/reference/pkg/nodejs/pulumi/gcp/compute#Instance" >}}) which is created inside the network from the Debian 9 base image.

1.  To preview and deploy changes, run `pulumi up`. The command shows a preview of the resources that will be created and prompts on whether to proceed with the deployment.  Note that the stack itself is counted as a resource, though it does not correspond to a physical cloud resource.

        $ pulumi up
        Previewing update (webservergcp-dev):

            Type                     Name                           Plan
            pulumi:pulumi:Stack      webservergcp-webservergcp-dev
        +   ├─ gcp:compute:Network   network                        create
        +   ├─ gcp:compute:Firewall  firewall                       create
        +   └─ gcp:compute:Instance  instance                       create

        Resources:
            + 3 to create
            1 unchanged

1.  Now, proceed with the deployment, which will take around a minute to complete. 

        Do you want to perform this update? yes
        Updating (webservergcp-dev):

            Type                     Name                           Status
            pulumi:pulumi:Stack      webservergcp-webservergcp-dev
        +   ├─ gcp:compute:Network   network                        created
        +   ├─ gcp:compute:Instance  instance                       created
        +   └─ gcp:compute:Firewall  firewall                       created

        Outputs:
        + instanceIP  : "173.255.117.131"
        + instanceName: "instance-bf0ab1f"

        Resources:
            + 3 created
            1 unchanged

        Duration: 1m20s

        Permalink: https://app.pulumi.com/lukehoban/webservergcp-dev/updates/1

    To see the full details of the deployment and the resources that are now part of the stack, open the update permalink in a browser.

1.  To view the provisioned resources on the command line, run `pulumi stack`. You'll also see two [stack outputs]({{< relref "/docs/reference/stack.md#output" >}}) corresponding to the IP and full-qualified host name of the virtual machine instance we've created.  

    ```
    $ pulumi stack
    ...
    Current stack resources (5):
        TYPE                                             NAME
        pulumi:pulumi:Stack                              webservergcp-webservergcp-dev
        pulumi:providers:gcp                             default
        gcp:compute/network:Network                      network
        gcp:compute/firewall:Firewall                    firewall
        gcp:compute/instance:Instance                    instance

    Current stack outputs (2):
        OUTPUT                                           VALUE
        instanceIP                                       173.255.117.131
        instanceName                                     instance-bf0ab1f
    ```

## Updating the Pulumi program

Now that we have an instance of our Pulumi program deployed, we may want to make changes. We do this by updating our
Pulumi program to define the new state we want our infrastructure to be in, then and running `pulumi up` to commit the changes.

1.  Replace the creation of the two firewall and instance with the following. This exposes an additional port and adds a startup
    script to run a simple HTTP server at startup.

    ```javascript
    ...

    const computeFirewall = new gcp.compute.Firewall("firewall", {
        network: computeNetwork.id,
        allows: [{
            protocol: "tcp",
            ports: [ "22", "80" ], // <-- ADD "80" HERE
        }],
    });

    // v-- ADD THIS DEFINITION
    const startupScript = `#!/bin/bash
    echo "Hello, World!" > index.html
    nohup python -m SimpleHTTPServer 80 &`;

    const computeInstance = new gcp.compute.Instance("instance", {
        machineType: "f1-micro",
        zone: "us-central1-a",
        metadataStartupScript: startupScript, // <-- ADD THIS LINE
        bootDisk: { initializeParams: { image: "debian-cloud/debian-9" } },
        networkInterfaces: [{
            network: network.id,
            // accessConfigus must include a single empty config to request an ephemeral IP
            accessConfigs: [{}], 
        }],
    });

    ...
    ```

    Note that we defined the `metadataStartupScript` script inline in a string.  Because we are using JavaScript, we could also read
    this from a file, construct this string programmatically, or even build up a string that depends on other resources
    defined in our program.  We'll see in later sections how we can deploy and version the application code of our
    program in a variety of different ways using Pulumi.

1.  Run `pulumi up` to preview and deploy the changes. You'll see two changes: the `allows` property of the `Firewall` will be _updated_ in-place.  Second, the `Instance` will be _replaced_ with a new virtual machine Instance which will run the new script on startup. Pulumi understands which changes to a given cloud resource can be made in-place, and which require replacement, and computes the minimally disruptive change to achieve the desired state.

    ```bash
    $ pulumi up
    Previewing update (webservergcp-dev):
    ...

    Updating (webservergcp-dev):

        Type                     Name                           Status       Info
        pulumi:pulumi:Stack      webservergcp-webservergcp-dev
    ~   ├─ gcp:compute:Firewall  firewall                       updated      [diff: ~allows]
    +-  └─ gcp:compute:Instance  instance                       replaced     [diff: +metadataStartupScript~name]

    Outputs:
    ~ instanceIP  : "173.255.117.131" => "35.202.30.129"
    ~ instanceName: "instance-bf0ab1f" => "instance-31bbd12"

    Resources:
        ~ 1 updated
        +-1 replaced
        2 changes. 2 unchanged

    Duration: 2m41s

    Permalink: https://app.pulumi.com/lukehoban/webservergcp-dev/updates/2
    ```

1.  We can use `pulumi stack output` to get the value of stack outputs from the CLI.  So we can `curl` the virtual machine instance to see the HTTP server running there. Stack outputs can also be viewed on the Pulumi Console.

    ```bash
    $ curl $(pulumi stack output instanceIP)
    Hello, World!
    ```

## Clean up

Before moving on, let's tear down the resources that are part of our stack.

1.  Run `pulumi destroy` to tear down all resources.  You'll be prompted to make sure you really want to delete these resources. This takes about 60 seconds; Pulumi waits for the virtual machine instance to shutdown and for the compute network to be removed before it considers the destroy operation to be complete.

1.  To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Console.

## Summary

In this tutorial, we saw how to use Pulumi programs to create and manage cloud resources in Google Cloud, using regular JavaScript and NPM packages. To preview and update infrastructure, use `pulumi up`. To clean up resources, run `pulumi destroy`.

For a similar example in other languages and clouds, see the [Web Server examples collection](https://github.com/pulumi/examples#web-server).
