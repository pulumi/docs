---
title: Step 1 - Your First Pulumi Program
---

<!-- Common links -->
[EC2 Instance]: /packages/pulumi-aws/classes/_ec2_instance_.instance.html
[Security Group]: /packages/pulumi-aws/classes/_ec2_securitygroup_.securitygroup.html
[`@pulumi/aws`]: /packages/pulumi-aws/index.html
[Pulumi examples zipfile]: /examples/pulumi-examples.zip
<!-- End common links -->

In this quickstart we'll give you a guided tour of the core features of Pulumi, and how to apply them to build a variety
of cloud applications.

Pulumi is a programming platform for the cloud, enabling you to create and manage cloud infrastructure and managed
services as well as application code deployed to containers and serverless functions.  We'll cover all of these in the
quickstart, from a couple individual cloud resources in this first section, to components comprised of many managed
cloud services, and applications built from a combination of cloud resources, containers and serverless functions in
later sections.

We'll focus in this quickstart on using **JavaScript** and on building applications deployed to **AWS**. 

Pulumi supports authoring programs in additional languages ([TypeScript](../reference/javascript#TypeScript),
[Python](../reference/python), and more in the future), and targeting additional clouds ([Azure](../reference/aws),
[GCP](../reference/gcp), [Kubernetes](../reference/kubernetes) and more in the future) - but JavaScript and AWS are
currently supported for the [broadest set of use cases](TODO), so we'll use that combination to highlight the full set of
features of Pulumi.

> **NOTE:** If you do not already have an AWS account, you can [create an account](https://aws.amazon.com/free/) to use
> for these examples.  Most of the resources used in these examples are free within the Free Tier, but we encourage you
> to follow the steps at the end of each section to delete the applications you deploy when you are done to avoid paying
> for anything you aren't using.

# Setup

Make sure you have followed the steps to [install Pulumi](../install), and to setup the [AWS
CLI](../install/aws-config.html) and your [NPM token](../install/configure-npm.html) to access the Pulumi NPM packages.

Let's create our first Pulumi application - a simple webserver EC2 instance in AWS.

1.  Create a folder `webserver`:

    ```bash
    $ mkdir webserver
    $ cd webserver
    ```

1.  Create an empty project with `pulumi new`:

    ```
    $ pulumi new javascript
    ```


# A first Pulumi program

Pulumi programs are written in your favorite general purpose programming language (JavaScript in this example), and
define the resources you want to exist in your target cloud environment.  We'll start with a program that deploys a
virtual machine in the cloud.

1. Open `index.js` and replace the contents with the following:

    ```javascript
    const aws = require("@pulumi/aws");

    let size = "t2.micro";     // t2.micro is available in the AWS free tier
    let ami  = "ami-7172b611"; // AMI for Amazon Linux in us-west-2 (Oregon)

    // create a new security group for port 80
    let group = new aws.ec2.SecurityGroup("webserver-secgrp", { 
        description: "Enable HTTP access",
        ingress: [
            { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
        ],
    });

    let server = new aws.ec2.Instance("webserver-www", {
        tags: { "Name": "webserver-www" },
        instanceType: size,
        securityGroups: [ group.name ], // reference the security group resource above
        ami: ami,
    });

    exports.publicIp = server.publicIp;
    exports.publicDns = server.publicDns;
    ```

    This example uses the [`@pulumi/aws`] package to create and manage two AWS resources: an
    [`aws.ec2.SecurityGroup`][Security Group], which allows access for incoming HTTP requests, and an
    [`aws.ec2.Instance`][EC2 Instance], which will be created in that security group using the appropriate Amazon
    Machine Image (AMI) for the region where you deploy the program.

    This simple example highlights several core features of Pulumi:
    * [Resources](../reference/programming-model#resources) are defined by creating resource objects in code (e.g. `new
      aws.ec2.Instance(...)`).
    * Dependencies between resources are represented as simple references to [output properties]() of a resource (e.g.
      the `group.name` property of the `SecurityGroup`).
    * [Variables](../reference/programming-model#programs) can be used just like you would expect to store constants, or
      to precompute and share values that will be used in the program.
    * [Packages](../reference/programming-model#packages) (e.g. `@pulumi/aws`) provide access to Resources and
      Components you can use to build your applications.
    * Module [exports](../reference/programming-model#exports) (e.g. `exports.publicIP = ...`) are used to publish
      values that you want to access from outside your application.
    
1. Since we are using the `@pulumi/aws` NPM package, we need to add it and install all NPM dependencies.

    ```bash
    $ npm add @pulumi/aws@0.11.1
    $ npm install
    ```

1. Pulumi programs are deployed to a [stack](../reference/stack.html), which is an isolated and independently
   configurable instance of a Pulumi program.  We'll create a new stack for our program.

    ```bash
    $ pulumi stack init webserver-testing
    Created stack 'webserver-testing' hosted in Pulumi Cloud PPC pulumi
    ```

    You can see all the stacks for your program via `pulumi stack ls`:

    ```bash
    $ pulumi stack ls
    NAME                                             LAST UPDATE              RESOURCE COUNT     CLOUD
    webserver-testing*                               n/a                      0                  https://api.pulumi.com/:lukehoban/pulumi
    ```

1. Pulumi programs also support [configuration](../reference/config) which is defined per-stack to decide how that
   instance of the program should be parameterized.  We need to configure the AWS region we'll deploy to - we'll use
   `us-west-2`.

    ```bash
    $ pulumi config set aws:region us-west-2
    Created stack 'webserver-testing' hosted in Pulumi Cloud PPC pulumi
    ```

    You can view config values for the current stack via `pulumi config`:

    ```bash
    $ pulumi config
    KEY                              VALUE
    aws:config:region                us-west-2
    ```

1. Before we actually deploy our program, we can preview it to see what resources it will create in AWS.

    ```
    $ pulumi preview
    Previewing stack 'webserver-testing' in the Pulumi Cloud ☁️
    Previewing changes:
    + pulumi:pulumi:Stack: (create)
        [urn=urn:pulumi:webserver-testing::webserver2::pulumi:pulumi:Stack::webserver2-webserver-testing]
        + aws:ec2/securityGroup:SecurityGroup: (create)
            [urn=urn:pulumi:webserver-testing::webserver2::aws:ec2/securityGroup:SecurityGroup::webserver-secgrp]
            description        : "Enable HTTP access"
            ingress            : [
                [0]: {
                    cidrBlocks: [
                        [0]: "0.0.0.0/0"
                    ]
                    fromPort  : 80
                    protocol  : "tcp"
                    self      : false
                    toPort    : 80
                }
            ]
            name               : "webserver-secgrp-26e0bb6"
            revokeRulesOnDelete: false
        + aws:ec2/instance:Instance: (create)
            [urn=urn:pulumi:webserver-testing::webserver2::aws:ec2/instance:Instance::webserver-www]
            ami            : "ami-7172b611"
            getPasswordData: false
            instanceType   : "t2.micro"
            securityGroups : [
                [0]: "webserver-secgrp-26e0bb6"
            ]
            sourceDestCheck: true
            tags           : {
                Name: "webserver-www"
            }
    ---outputs:---
    publicDns: computed<string>
    publicIp : computed<string>
    info: 3 changes previewed:
        + 3 resources to create
    ```

    Note the output values `publicDns` and `publicIp` are not yet available, as they depend on the properties of a
    provisioned resource. The update shows that it will create 3 resources, rather than 2 - the stack itself is counted
    as a component which owns all of the resources we'll create.  Components will be covered in more details in [step
    2](./step2).

1.  Now, let's deploy the program and provision resources, via `pulumi update`. This will take 20-30 seconds to provision the EC2 instance.  **NOTE**: The output below has been condensed.
    
    ```
    $ pulumi update
    Updating stack 'webserver-testing' in the Pulumi Cloud ☁️
    [ ...details omitted... ]
    ---outputs:---
    publicDns: "ec2-34-210-112-213.us-west-2.compute.amazonaws.com"
    publicIp : "34.210.112.213"
    info: 3 changes performed:
        + 3 resources created
    Update duration: 20.233032918s
    Permalink: https://pulumi.com/lukehoban/webserver2/webserver2/webserver-testing/updates/1
    ```

    Note that this time, we see real values for the two outputs, corresponding to the IP and DNS name of the EC2 instances we've created.  Pulumi also provides a link to the pulumi.com console where you can see additional details about the eployment and the resources that are now part of the stack.

1. To view your provisioned resources, run `pulumi stack`.

    ```
    $ pulumi stack
    Current stack is webserver-testing:
        Managed by https://api.pulumi.com/ ☁️
        Organization lukehoban
        PPC pulumi
        Last update time unknown
        Pulumi version ?

    Current stack resources (3):
        TYPE                                             NAME
        pulumi:pulumi:Stack                              webserver2-webserver-testing
        aws:ec2/securityGroup:SecurityGroup              webserver-secgrp
        aws:ec2/instance:Instance                        webserver-www

    Current stack outputs (2):
        OUTPUT                                           VALUE
        publicDns                                        ec2-34-210-112-213.us-west-2.compute.amazonaws.com
        publicIp                                         34.210.112.213
    ```

# Updating the Pulumi program

Now that we have an instance of our Pulumi program deployed, we may want to make changes. We do this by updating our Pulumi program to define the new state we want our infrastructure to be in, and re-running `pulumi update`.

1. Replace the creation of the `aws.ec2.Instance` with the following.  This will add a startup script to our instance.

    ```javascript
    ...

    let userData = 
    `#!/bin/bash
    echo "Hello, World!" > index.html
    nohup python -m SimpleHTTPServer 80 &`;

    let server = new aws.ec2.Instance("web-server-www", {
        tags: { "Name": "web-server-www" },
        instanceType: size,
        securityGroups: [ group.name ], // reference the group object above
        ami: ami,
        userData: userData,             // <-- ADD THIS LINE
    });

    ...
    ```

    Note that we defined the `userData` script inline in a string.  Because we are using JavaScript, we could also read
    this from a file, construct this string programmaticaly, or even build up a string that depends on other resources
    defined in our program.  We'll see in later sections how we can deploy and version the application code of our
    program in a variety of different ways using Pulumi.

1. Run `pulumi preview` to see that that only one resource will be replaced.

    ```
    $ pulumi preview
    Previewing stack 'webserver-testing' in the Pulumi Cloud ☁️
    Previewing changes:
    * pulumi:pulumi:Stack: (same)
        [urn=urn:pulumi:webserver-testing::webserver2::pulumi:pulumi:Stack::webserver2-webserver-testing]
    ---outputs:---
    publicDns: "ec2-34-210-112-213.us-west-2.compute.amazonaws.com"
    publicIp : "34.210.112.213"
        +-aws:ec2/instance:Instance: (replace)
            [id=i-066813fbe532d6b1b]
            [urn=urn:pulumi:webserver-testing::webserver2::aws:ec2/instance:Instance::webserver-www]
            ami            : "ami-7172b611"
            getPasswordData: false
            instanceType   : "t2.micro"
            securityGroups : [
                [0]: "webserver-secgrp-cf10413"
            ]
            sourceDestCheck: true
            tags           : {
                Name: "webserver-www"
            }
        + userData       : "#!/bin/bash\necho \"Hello, World!\" > index.html\nnohup python -m SimpleHTTPServer 80 &"
    ---outputs:---
    publicDns: computed<string>
    publicIp : computed<string>
    info: 1 change previewed:
        +-1 resource to replace
        2 resources unchanged
    ```

1. Then run `pulumi update` to deploy the changes.

    ```
    $ pulumi update
    Updating stack 'webserver-testing' in the Pulumi Cloud ☁️
    [ ...details omitted... ]
    publicDns: "ec2-52-37-221-116.us-west-2.compute.amazonaws.com"
    publicIp : "52.37.221.116"
    info: 1 change performed:
        +-1 resource replaced
        2 resources unchanged
    Update duration: 1m4.980730307s
    Permalink: https://pulumi.com/lukehoban/webserver2/webserver2/webserver-testing/updates/2
    ```

1. We can use `pulumi stack output` to get the value of stack outputs from the CLI.  So we can `curl` the EC2 instance to see the HTTP server running there:

    ```
    $ curl $(pulumi stack output publicDns)
    Hello, World!
    ```

# Cleanup

Before moving on, let's tear down the resources that are part of our stack.

1. Run `pulumi destroy` to tear down all resources.  You'll be prompted to make sure you really want to delete these resources.  This will take 50-60 seconds.

    ```
    $ pulumi destroy
    This will permanently destroy all resources in the 'webserver-testing' stack!
    Please confirm that this is what you'd like to do by typing ("webserver-testing"): webserver-testing
    Destroying stack 'webserver-testing' in the Pulumi Cloud ☁️
    [ ...details omitted... ]
    info: 3 changes performed:
        - 3 resources deleted
    Update duration: 52.746125589s
    Permalink: https://pulumi.com/lukehoban/webserver2/webserver2/webserver-testing/updates/3
    ```

1. We can also remove the stack itself with `pulumi stack rm`.

    ```
    $ pulumi stack rm
    This will permanently remove the 'webserver-testing' stack!
    Please confirm that this is what you'd like to do by typing ("webserver-testing"): webserver-testing
    Stack 'webserver-testing' has been removed!
    ```

# Next Steps

In this first tutorial, we saw how to use Pulumi programs to create and manage cloud resources.  We saw that we can use
plain JavaScript, and that Pulumi programs are executed during `preview` and `update` to determine that state we want
our infrastructure to be in.  We also saw the core lifecycle of a Pulumi stack.

In the [next section](./step2), we'll look at ways we can use programming languages to make defining infrastructure
even easier by using loops, conditionals, functions and classes.  And we'll see how these can be combined to build
reusable abstractions, libraries and new pacakges.

After that, in [step 3](./step3) and [step 4](./step4), we'll see examples of some powerful libraries that can be built
from these abstractions for serverless application development and for highly-productive cloud-agnostic app development.
We'll see that the foundational principles of Pulumi programs and stacks covered in this tutorial apply in all of these
other cases as well.

And finally, in [step 5](./step5), we'll see how we can mix and match the kind of raw cloud infrastructure we defined in
this tutorial with the higher level libraries in later sections.

[Continue with step 2 of the quickstart.](./step2)