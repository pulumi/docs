---
title: "EC2 Linux WebServer Instance"
menu:
  reference:
    parent: tutorials-aws
---

In this tutorial, we'll use JavaScript to deploy a simple webserver EC2 instance in AWS. The [code for this tutorial](https://github.com/pulumi/examples/tree/master/aws-js-webserver) is available on GitHub.

{{< aws-js-prereqs >}}

## Create an EC2 instance with SSH access {#webserver}

1.  In a new folder `webserver`, create an empty project with `pulumi new`. Be sure to use `us-east-1` as the region:

    ```bash
    $ mkdir webserver && cd webserver
    $ pulumi new aws-javascript
    ...
    aws:region: (us-east-1)
    ```

1.  Open `index.js` and replace the contents with the following:

    ```javascript
    const aws = require("@pulumi/aws");

    let size = "t2.micro";     // t2.micro is available in the AWS free tier
    let ami  = "ami-0ff8a91507f77f867"; // AMI for Amazon Linux in us-east-1 (Virginia)

    let group = new aws.ec2.SecurityGroup("webserver-secgrp", {
        ingress: [
            { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
        ],
    });

    let server = new aws.ec2.Instance("webserver-www", {
        instanceType: size,
        securityGroups: [ group.name ], // reference the security group resource above
        ami: ami,
    });

    exports.publicIp = server.publicIp;
    exports.publicHostName = server.publicDns;
    ```

    This example uses the [@pulumi/aws] package to create and manage two AWS resources: an
    [aws.ec2.SecurityGroup][Security Group], which allows access for incoming SSH access, and an
    [aws.ec2.Instance][EC2 Instance], which is created in that security group using the appropriate Amazon
    Machine Image (AMI) for the region where you deploy the program.

1.  To preview and deploy changes, run `pulumi up`. The command shows a preview of the resources that will be created and prompts on whether to proceed with the deployment.  Note that the stack itself is counted as a resource, though it does not correspond to a physical cloud resource.

        $ pulumi up
        Previewing update of stack 'webserver-dev'
        Previewing changes:

            Type                      Name                               Plan       Info
        +   pulumi:pulumi:Stack       webserver-webserver-dev            create
        +   ├─ aws:ec2:SecurityGroup  webserver-secgrp                   create
        +   └─ aws:ec2:Instance       webserver-www                      create

        info: 3 changes previewed:
            + 3 resources to create

1.  Now, proceed with the deployment, which takes about 30 seconds to complete.

        Do you want to perform this update? yes
        Updating stack 'ec2-quickstart-dev'
        Performing changes:

            Type                      Name                               Status      Info
        +   pulumi:pulumi:Stack       webserver-webserver-testing        created
        +   ├─ aws:ec2:SecurityGroup  webserver-secgrp                   created
        +   └─ aws:ec2:Instance       webserver-www                      created

        ---outputs:---
        publicHostName: "ec2-34-224-93-18.compute-1.amazonaws.com"
        publicIp      : "34.224.93.18"

        info: 3 changes performed:
            + 3 resources created
        Update duration: 32.938640858s

        Permalink: https://app.pulumi.com/lindydonna/ec2-quickstart-dev/updates/3


    To see the full details of the deployment and the resources that are now part of the stack, open the update link in a browser. The **Resources** tab on pulumi.com has a link to the AWS console for the provisioned EC2 instance.

1.  To view the provisioned resources on the command line, run `pulumi stack`. You'll also see two [stack outputs]({{< relref "/docs/reference/stack#outputs" >}}) corresponding to the IP and full-qualified host name of the EC2 instance we've created.

    ```
    $ pulumi stack
    ...

    Current stack resources (3):
        TYPE                                    NAME
        pulumi:pulumi:Stack                     webserver-webserver-testing
        aws:ec2/securityGroup:SecurityGroup     webserver-secgrp
        aws:ec2/instance:Instance               webserver-www

    Current stack outputs (2):
        OUTPUT                                  VALUE
        publicHostName                          ec2-54-213-251-255.us-west-2.compute.amazonaws.com
        publicIp                                54.213.251.255
    ```

## Updating the Pulumi program

Now that we have an instance of our Pulumi program deployed, we may want to make changes. We do this by updating our
Pulumi program to define the new state we want our infrastructure to be in, then and running `pulumi up` to commit the changes.

1.  Replace the creation of the two resources with the following. This exposes an additional port and adds a startup
    script to run a simple HTTP server at startup.

    ```javascript
    ...

    let group = new aws.ec2.SecurityGroup("webserver-secgrp", {
        ingress: [
            { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
            { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
            // ^-- ADD THIS LINE
        ],
    });

    let userData = // <-- ADD THIS DEFINITION
    `#!/bin/bash
    echo "Hello, World!" > index.html
    nohup python -m SimpleHTTPServer 80 &`;

    let server = new aws.ec2.Instance("web-server-www", {
        instanceType: size,
        securityGroups: [ group.name ], // reference the group object above
        ami: ami,
        userData: userData,             // <-- ADD THIS LINE
    });

    ...
    ```

    Note that we defined the `userData` script inline in a string.  Because we are using JavaScript, we could also read
    this from a file, construct this string programmatically, or even build up a string that depends on other resources
    defined in our program.  We'll see in later sections how we can deploy and version the application code of our
    program in a variety of different ways using Pulumi.

1.  Run `pulumi up` to preview and deploy the changes. You'll see two changes: the `ingress` property of the `SecurityGroup` will be _updated_ in-place.  Second, the `Instance` will be _replaced_ with a new EC2 Instance which will run the new script on startup. Pulumi understands which changes to a given cloud resource can be made in-place, and which require replacement, and computes the minimally disruptive change to achieve the desired state.

        $ pulumi up
        Previewing update of stack 'ec2-quickstart-dev'
        ...

        Updating stack 'ec2-quickstart-dev'
        Performing changes:

            Type                      Name                               Status       Info
        *   pulumi:pulumi:Stack       ec2-quickstart-ec2-quickstart-dev  done
        ~   ├─ aws:ec2:SecurityGroup  webserver-secgrp                   updated      changes: ~ ingress
        +-  └─ aws:ec2:Instance       webserver-www                      replaced     changes: + userData

        ---outputs:---
        publicHostName: "ec2-52-23-161-125.compute-1.amazonaws.com"
        publicIp      : "52.23.161.125"

        info: 2 changes performed:
            ~ 1 resource updated
            +-1 resource replaced
            1 resource unchanged
        Update duration: 1m44.50461533s

        Permalink: https://app.pulumi.com/lindydonna/ec2-quickstart-dev/updates/6


1.  We can use `pulumi stack output` to get the value of stack outputs from the CLI.  So we can `curl` the EC2 instance to see the HTTP server running there. Stack outputs can also be viewed on the Pulumi Console.

    ```bash
    $ curl $(pulumi stack output publicHostName)
    Hello, World!
    ```

## Clean up

Before moving on, let's tear down the resources that are part of our stack.

1.  Run `pulumi destroy` to tear down all resources.  You'll be prompted to make sure you really want to delete these
   resources. This takes about 60 seconds; Pulumi waits for the EC2 instance to finish shutting down before
   it considers the destroy operation to be complete.

1.  To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Console.

## Summary

In this tutorial, we saw how to use Pulumi programs to create and manage cloud resources in AWS, using regular JavaScript and NPM packages. To preview and update infrastructure, use `pulumi up`. To clean up resources, run `pulumi destroy`.

For a similar example in other languages and clouds, see the [Web Server examples collection](https://github.com/pulumi/examples#web-server).

<!-- Common links -->
[EC2 Instance]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ec2#Instance" >}}
[Security Group]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ec2#SecurityGroup" >}}
[@pulumi/aws]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws" >}}
<!-- End common links -->
