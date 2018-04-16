---
title: Part 1. Your First Pulumi Program
---

<!-- Common links -->
[EC2 Instance]: /packages/pulumi-aws/classes/_ec2_instance_.instance.html
[Security Group]: /packages/pulumi-aws/classes/_ec2_securitygroup_.securitygroup.html
[@pulumi/aws]: /packages/pulumi-aws/index.html
<!-- End common links -->

This quickstart presents a guided tour of Pulumi's core features and how you can use them to build a variety of cloud applications. 

Pulumi is a programming platform for the cloud. You can easily create and manage infrastructure and higher-level services, or deploy application code to containers and serverless functions. This quickstart starts by creating a few individual resources, then continues to full applications built from a combination of cloud resources, such as cloud storage, containers, and serverless functions. 

This quickstart uses **JavaScript** to build applications deployed on **AWS**.

> **Note:** Pulumi also supports [TypeScript](../reference/javascript.html#TypeScript) and [Python](../reference/python.html), with more languages coming in the future. For clouds, you can also target [Azure](../reference/azure.html), [GCP](../reference/gcp.html) and [Kubernetes](../reference/kubernetes.html), with more clouds supported in the future.

{% include aws-resource-note.md %}

# Setup

First, make sure you have 1) [installed Pulumi](../install), 2) [set up the AWS CLI](../install/aws-config.html) and 3) [configured your NPM client](../install/configure-npm.html) to access the Pulumi NPM packages.

Let's create a new Pulumi project for our first application, which is a simple webserver EC2 instance in AWS.

1.  Create a folder `webserver`:

    ```bash
    $ mkdir webserver
    $ cd webserver
    ```

1.  Create an empty project with `pulumi new`:

    ```
    $ pulumi new javascript
    ```

1.  Initialize a Pulumi repository with `pulumi init`, using your GitHub username. (Note: this step will be removed in the future.)

    ```
    $ pulumi init --owner gitHubUsername
    ```

# A first Pulumi program

Pulumi programs are written in your favorite general purpose programming language (JavaScript in this example), and
define the resources you want to exist in your target cloud environment.  We'll start with a program that deploys a
virtual machine in the cloud.

1.  Open `index.js` and replace the contents with the following:

    ```javascript
    const aws = require("@pulumi/aws");

    let size = "t2.micro";     // t2.micro is available in the AWS free tier
    let ami  = "ami-7172b611"; // AMI for Amazon Linux in us-west-2 (Oregon)

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

    This simple example highlights several core features of Pulumi:
    * [Resources](../reference/programming-model.html#resources) are defined by allocating resource objects in code (e.g.
      `new aws.ec2.Instance(...)`).  The first argument passed to the resource constructor is its `name`, which must be
      unique within the Pulumi program.
    * Dependencies between resources are represented as simple references to [output
      properties](../reference/programming-model.html#outputs) of a resource (e.g. the `group.name` property of the
      `SecurityGroup`).
    * [Variables](../reference/programming-model.html#programs) can be used just like you would expect to store constants, or
      to precompute and share values that are used in the program.
    * [Packages](../reference/programming-model.html#packages) (e.g. `@pulumi/aws`) provide access to Resources and
      Components you can use to build your applications.
    * Module [exports](../reference/programming-model.html#exports) (e.g. `exports.publicIP = ...`) are used to publish
      values that you want to access from outside your application.
    
1.  Since we are using the `@pulumi/aws` NPM package, we need to add it and install all NPM dependencies.

    ```bash
    $ npm install --save @pulumi/pulumi @pulumi/aws
    ```

1.  Pulumi programs are deployed to a [stack](../reference/stack.html), which is an isolated and independently
   configurable instance of a Pulumi program.  We'll create a new stack for our program.

    ```bash
    $ pulumi stack init webserver-testing
    Created stack 'webserver-testing'.
    ```

    You can see all the stacks for your program via `pulumi stack ls`:

    ```bash
    $ pulumi stack ls
    NAME                                             LAST UPDATE              RESOURCE COUNT     CLOUD
    webserver-testing*                               n/a                      0                  https://api.pulumi.com/:lukehoban/pulumi
    ```

    The new stack is marked with an asterisk to indicate that it is the currently active stack. All deployment operations target this stack.

1.  Pulumi programs also support [configuration](../reference/config.html) which is defined per-stack to decide how that
   instance of the program should be parameterized.  We need to configure the AWS region we'll deploy to, such as 
   `us-west-2`.

    ```bash
    $ pulumi config set aws:region us-west-2
    ```

    You can view config values for the current stack via `pulumi config`:

    ```bash
    $ pulumi config
    KEY                              VALUE
    aws:region                       us-west-2
    ```

1.  Before we actually deploy our program, we can preview it to see what resources it will create in AWS.

    ```
    $ pulumi preview
    Previewing stack 'webserver-testing' in the Pulumi Cloud ☁️
    Previewing changes:

    pulumi:Stack("webserver-webserver-testing"): Completed
    aws:SecurityGroup("web-secgrp"):             + Would create
    aws:Instance("web-server-www"):              + Would create
    info: 3 changes previewed:
        + 3 resources to create
    ```

    The update shows that it will create 3 resources, rather than 2, as the stack is itself counted as a component which owns all resources being created. Components are covered in more details in [part 2](./part2.html).

1.  Now, let's deploy the program and provision resources, via `pulumi update`. It takes about 30 seconds to
    provision the EC2 instance. While the resources of the stack are being created, you will see a `Running...` progress indicator for the stack component. 
    
    ```
    $ pulumi update
    Updating stack 'webserver-testing' in the Pulumi Cloud ☁️
    Performing changes:

    pulumi:Stack("webserver-webserver-testing"): Completed
    aws:SecurityGroup("web-secgrp"):             + Created
    aws:Instance("web-server-www"):              + Created
    info: 3 changes performed:
        + 3 resources created
    Update duration: 25.828272189s

    Permalink: https://pulumi.com/lindydonna/examples/webserver/webserver-testing/updates/1
    ```

    Now that the program is deployed, Pulumi link to the pulumi.com console where you can see additional details
    about the deployment and the resources that are now part of the stack.

1.  To view your provisioned resources, run `pulumi stack`. You'll see two [stack outputs](../reference/stack.html#output) corresponding to the IP and full-qualified host name of the EC2 instances we've created.  

    ```
    $ pulumi stack
    Current stack is webserver-testing:
        Managed by https://api.pulumi.com ☁️
        Organization lindydonna
        PPC pulumi
        Last update time unknown
        Pulumi version ?

    Current stack resources (3):
        TYPE                                             NAME
        pulumi:pulumi:Stack                              webserver-webserver-testing
        aws:ec2/securityGroup:SecurityGroup              web-secgrp
        aws:ec2/instance:Instance                        web-server-www

    Current stack outputs (2):
        OUTPUT                                           VALUE
        publicHostName                                   ec2-34-217-59-219.us-west-2.compute.amazonaws.com
        publicIp                                         34.217.59.219

    Use `pulumi stack select` to change stack; `pulumi stack ls` lists known ones
    ```

# Updating the Pulumi program

Now that we have an instance of our Pulumi program deployed, we may want to make changes. We do this by updating our
Pulumi program to define the new state we want our infrastructure to be in, and re-running `pulumi preview` and, if it
looks as we expect, `pulumi update` to commit the changes.

1.  Replace the creation of the two resources with the following. This exposes an additional port and adds a startup
    script to run a simple HTTP server on the instance at startup.

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

1.  Run `pulumi preview` to see that two changes will be made when this is deployed.

    ```
    $ pulumi preview
    Previewing stack 'webserver-testing' in the Pulumi Cloud ☁️
    Previewing changes:

    pulumi:Stack("webserver-webserver-testing"): Completed
    aws:SecurityGroup("web-secgrp"):             ~ Would update. Changes: +-ingress
    aws:Instance("web-server-www"):              +-Would replace. Changes: + userData
    info: 2 changes previewed:
        ~ 1 resource to update
        +-1 resource to replace
          1 resource unchanged

    ```

    We see that two changes will be applied.  First, the `ingress` property of the `SecurityGroup` will be _updated_ in-place.  Second, the `Instance` will be _replaced_ with a new EC2 Instance which will run the new 
    script on startup. Pulumi understands which changes to a given cloud resource can be made in-place, and which
    require replacement, and computes the minimally disruptive change to achieve the desired state.

1.  Now, run `pulumi update` to deploy the changes.

    ```
    $ pulumi update
    Updating stack 'webserver-testing' in the Pulumi Cloud ☁️
    Performing changes:

    pulumi:Stack("webserver-webserver-testing"): Completed
    aws:SecurityGroup("web-secgrp"):             ~ Updated. Changes: +-ingress
    aws:Instance("web-server-www"):              +-Replaced. Changes: + userData
    info: 2 changes performed:
        ~ 1 resource updated
        +-1 resource replaced
          1 resource unchanged
    Update duration: 1m14.133839913s

    Permalink: https://pulumi.com/lindydonna/examples/webserver/webserver-testing/updates/4
    ```

1.  We can use `pulumi stack output` to get the value of stack outputs from the CLI.  So we can `curl` the EC2 instance to see the HTTP server running there:

    ```
    $ curl $(pulumi stack output publicHostName)
    Hello, World!
    ```

# Cleanup

Before moving on, let's tear down the resources that are part of our stack.

1.  Run `pulumi destroy` to tear down all resources.  You'll be prompted to make sure you really want to delete these
   resources.  This takes about 60 seconds; Pulumi waits for the EC2 instance to finish shutting down before
   it considers the destroy operation to be complete.

    ```
    $ pulumi destroy
    This will permanently destroy all resources in the 'webserver-testing' stack!
    Please confirm that this is what you'd like to do by typing ("webserver-testing"): webserver-testing
    Destroying stack 'webserver-testing' in the Pulumi Cloud ☁️
    Performing changes:

    aws:Instance("web-server-www"):    - Deleted
    aws:SecurityGroup("web-secgrp"):   - Deleted
    pulumi:Stack("webserver-webserver-testing"): Completed
    info: 3 changes performed:
        - 3 resources deleted
    Update duration: 51.623097429s

    Permalink: https://pulumi.com/lindydonna/examples/webserver/webserver-testing/updates/3
    ```

1.  We can also remove the stack itself with `pulumi stack rm`.

    ```
    $ pulumi stack rm
    This will permanently remove the 'webserver-testing' stack!
    Please confirm that this is what you'd like to do by typing ("webserver-testing"): webserver-testing
    Stack 'webserver-testing' has been removed!
    ```

# Next Steps

In this first tutorial, we saw how to use Pulumi programs to create and manage cloud resources in AWS. We saw that we can use plain JavaScript and NPM packages, and that Pulumi programs are executed during `preview` and `update` to determine that state we want our infrastructure to be in.  We also saw the core lifecycle of a Pulumi stack.

For the same example in other languages and clouds, see the [Web Server examples collection](https://github.com/pulumi/examples#web-server).

In the [next section](./part2.html), we'll look at ways we can use programming languages to make defining infrastructure
even easier by using loops, conditionals, functions and classes.  And we'll see how these can be combined to build
reusable abstractions, libraries and new packages.

After that, in [part 3](./part3.html) and [part 4](./part4.html), we'll see examples of some powerful libraries that can be built
from these abstractions for serverless application development and for highly-productive cloud-agnostic app development.
We'll see that the foundational principles of Pulumi programs and stacks covered in this tutorial apply in all of these
other cases as well.

And finally, in [part 5](./part5.html), we'll see how we can mix and match the kind of raw cloud infrastructure we defined in
this tutorial with the higher level libraries in later sections.

[Continue with part 2 of the quickstart.](./part2.html)
