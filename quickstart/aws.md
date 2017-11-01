---
layout: default 
nav_section: "quickstart"
---

<p><a href="/quickstart">Quickstart</a> &gt; <b>Programming AWS</b></p>

# Programming AWS

The `@pulumi/aws` package lets you use Pulumi to create and manage AWS resources.

Every kind of resource available in the AWS cloud is available as a distinct class underneath discoverable submodules.
A few examples:

* EC2 VM instances, `aws.ec2.Instance`
* S3 buckets, `aws.s3.Bucket`, and objects, `aws.s3.Object`
* DynamoDB tables, `aws.dynamodb.Table`
* Lambda functions, `aws.lambda.Function`

## A Simple Application

For our first application, we'll create an AWS [EC2 Instance](/packages/pulumi-aws/classes/_ec2_instance_.instance.html)
and associated [Security Group](/packages/pulumi-aws/classes/_ec2_securitygroup_.securitygroup.html) using Pulumi.

1. Create a folder `webserver`:

    ```bash
    $ mkdir webserver
    $ cd webserver
    ```

1. In that folder, save the following as `index.js`:

    ```javascript
    let aws = require("@pulumi/aws");

    let group = new aws.ec2.SecurityGroup("web-secgrp", {
        description: "Enable HTTP access",
        ingress: [
            { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
        ],
    });

    let server = new aws.ec2.Instance("web-server-www", {
        instanceType: "t2.micro",
        securityGroups: [ group.name ],
        ami: aws.ec2.getLinuxAMI("t2.micro"),
        tags: { name: "pulumi"},
    });
    ```

    This example uses the [`@pulumi/aws`](/packages/pulumi-aws/index.html) package to create and manage AWS resources.  It
    creates two resources: an [`aws.ec2.SecurityGroup`](
    /packages/pulumi-aws/classes/_ec2_securitygroup_.securitygroup.html), which allows access for incoming HTTP requests,
    and an [`aws.ec2.Instance`](/packages/pulumi-aws/classes/_ec2_instance_.instance.html), which will be created in that
    security group using the appropriate Amazon Machine Image (AMI) for the region where you deploy the program.

    *Note that each resource expects a name as the first parameter - this name is used by Pulumi to track the resources
    across updates, and should be a unique name among all resources of that type in your program.*

1. Create a `Pulumi.yaml` file to describe the Pulumi application:

    ```yaml
    name: webserver
    description: Basic example of an AWS web server accessible over HTTP.
    runtime: nodejs
    ```

1. Run `npm init` or `yarn init` to create a default Node.js `package.json`, since our Pulumi program uses Node.js:

    ```bash
    $ yarn init
    yarn init v0.24.6
    question name (webserver):
    question version (1.0.0):
    question description:
    question entry point (index.js):
    question repository url:
    question author:
    question license (MIT):
    success Saved package.json
    ✨  Done in 1.44s.
    ```

1. Link with the Pulumi SDK packages so that your `require`s will find the right thing:

    ```bash
    $ yarn link pulumi @pulumi/aws @pulumi/cloud
    ```

1. You should now have the following files in your `webserver` folder:

    ```bash
    $ ls
    Pulumi.yaml	index.js	node_modules	package.json
    ```

## Stacks, Updates and Previews

Now that we have the code for our first program, let's deploy it!

Every Pulumi program is deployed to an __stack__.  An stack is an isolated, independently configurable
target in which programs will run.  It's reasonable to have many stack: often you'll have different development,
staging, and production stack, and may in fact have multiple of each kind, like east coast vs. west coast
production.

1. Create a Pulumi repository. A repository is a collection of Pulumi projects:

    ```bash
    $ pulumi init
    Initialized Pulumi repository in /Users/donnam/src/hello-world/.pulumi
    ```

1. Create a stack called `testing`:

    ```bash
    $ pulumi stack init testing
	```

    You can now run `pulumi stack ls` to see the newly created stack:

    ```bash
    $ pulumi stack ls
    NAME                 LAST UPDATE                                      RESOURCE COUNT
    testing*             n/a                                              n/a
    ```


1. We can get a preview of what will happen during a deployment by running `pulumi preview`.  Running that command we get an error `Error: Missing required configuration variable 'aws:config:region'`.  As the error states, before we can preview or update our application, we need to configure the AWS region we will be targeting.

    ```bash
    $ pulumi config text aws:config:region us-west-2
    ```

1. We can now successfully run `pulumi preview` to see the complete set of resources that will be created:

    ```bash
    $ pulumi preview
    Previewing changes:
    + aws:ec2/securityGroup:SecurityGroup: (create)
        [urn=urn:lumi:testing::webserver::aws:ec2/securityGroup:SecurityGroup::web-secgrp]
        description: "Enable HTTP access"
        ingress    : [
            [0]: {
                    cidrBlocks: [
                        [0]: "0.0.0.0/0"
                    ]
                    fromPort  : 80
                    protocol  : "tcp"
                    toPort    : 80
                }
        ]
        name       : "web-secgrp-f552bbcd376c5f94"
    + aws:ec2/instance:Instance: (create)
        [urn=urn:lumi:testing::webserver::aws:ec2/instance:Instance::web-server-www]
        ami            : "ami-7172b611"
        instanceType   : "t2.micro"
        securityGroups : [
            [0]: computed<string>
        ]
        sourceDestCheck: true
        tags           : {
            name: "pulumi"
        }
    info: 2 changes previewed:
        + 2 resources to create
    ```

1. As expected, we see that updating this program will create two resources.  So let's go ahead and deploy the update.
This will take ~30 seconds as it waits for the actual EC2 instance to finish spinning up:

    ```bash
    $ pulumi update
    Performing changes:
    + aws:ec2/securityGroup:SecurityGroup: (create)
        [urn=urn:lumi:testing::webserver::aws:ec2/securityGroup:SecurityGroup::web-secgrp]
        description: "Enable HTTP access"
        ingress    : [
            [0]: {
                    cidrBlocks: [
                        [0]: "0.0.0.0/0"
                    ]
                    fromPort  : 80
                    protocol  : "tcp"
                    toPort    : 80
                }
        ]
        name       : "web-secgrp-cea08d71378cb4fe"
        ---outputs:---
        egress     : []
        id         : "sg-4bfe3a36"
        ingress    : [
            [0]: {
                    cidrBlocks    : [
                        [0]: "0.0.0.0/0"
                    ]
                    fromPort      : "80"
                    ipv6CidrBlocks: []
                    protocol      : "tcp"
                    securityGroups: []
                    self          : false
                    toPort        : "80"
                }
        ]
        name       : "web-secgrp-cea08d71378cb4fe"
        ownerId    : "153052954103"
        tags       : {}
        vpcId      : "vpc-c93b06ae"
    + aws:ec2/instance:Instance: (create)
        [urn=urn:lumi:testing::webserver::aws:ec2/instance:Instance::web-server-www]
        ami            : "ami-7172b611"
        instanceType   : "t2.micro"
        securityGroups : [
            [0]: "web-secgrp-cea08d71378cb4fe"
        ]
        sourceDestCheck: true
        tags           : {
            name: "pulumi"
        }
        ---outputs:---
        associatePublicIpAddress : true
        availabilityZone         : "us-west-2b"
        disableApiTermination    : false
        ebsBlockDevice           : []
        ebsOptimized             : false
        ephemeralBlockDevice     : []
        iamInstanceProfile       : ""
        id                       : "i-0b12d17d90b9d343e"
        instanceState            : "running"
        ipv6Addresses            : []
        keyName                  : ""
        monitoring               : false
        networkInterface         : []
        networkInterfaceId       : "eni-735f6342"
        primaryNetworkInterfaceId: "eni-735f6342"
        privateDns               : "ip-172-31-42-228.us-west-2.compute.internal"
        privateIp                : "172.31.42.228"
        publicDns                : "ec2-34-210-14-208.us-west-2.compute.amazonaws.com"
        publicIp                 : "34.210.14.208"
        rootBlockDevice          : [
            [0]: {
                    deleteOnTermination: true
                    iops               : "100"
                    volumeSize         : "8"
                    volumeType         : "gp2"
                }
        ]
        sourceDestCheck          : true
        subnetId                 : "subnet-00412149"
        tenancy                  : "default"
        volumeTags               : {}
        vpcSecurityGroupIds      : []
    info: 2 changes performed:
        + 2 resources created
    Update duration: 25.518253662s
    ```

1. We now have a running EC2 instance.  We can run `aws ec2 describe-instances --filter Name=tag:name,Values=pulumi` (or
open the AWS Console) to see that this new instance is now running.

1. Let's now make a change to our program.  Instead of creating just one instance, we'll create a reusable function
`createInstance` for creating instances in our Security Group and use it to create two instances -- one for `www` and
one for `api`.  We'll update `index.js` to the following:

    ```javascript
    let aws = require("@pulumi/aws");

    let group = new aws.ec2.SecurityGroup("web-secgrp", {
        description: "Enable HTTP access",
        ingress: [
            { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
        ],
    });

    function createInstance(size, name) {
        let server = new aws.ec2.Instance(name, {
            instanceType: size,
            securityGroups: [ group.name ],
            ami: aws.ec2.getLinuxAMI(size),
            tags:  { name: "pulumi" },
        });
        return server;
    }

    let www = createInstance("t2.micro", "web-server-www");
    let api = createInstance("t2.nano", "web-server-api");
    ```

1. We can run `pulumi preview` to see what changes this will make to our infrastructure.  Note that only one new resource
is created: the security group and `web-server-www` instance are unchanged and so do not need to be updated or replaced.

    ```bash
    $ pulumi preview
    Previewing changes:
    + aws:ec2/instance:Instance: (create)
        [urn=urn:lumi:testing::webserver::aws:ec2/instance:Instance::web-server-api]
        ami            : "ami-7172b611"
        instanceType   : "t2.nano"
        securityGroups : [
            [0]: "web-secgrp-cea08d71378cb4fe"
        ]
        sourceDestCheck: true
        tags           : {
            name: "pulumi"
        }
    info: 1 change previewed:
        + 1 resource to create
        2 resources unchanged
    ```

1. Having verified that these changes are expected, run `pulumi update` to update our infrastructure:

    ```bash
    $ pulumi update
    Performing changes:
    + aws:ec2/instance:Instance: (create)
        [urn=urn:lumi:testing::webserver::aws:ec2/instance:Instance::web-server-api]
        ami            : "ami-7172b611"
        instanceType   : "t2.nano"
        securityGroups : [
            [0]: "web-secgrp-cea08d71378cb4fe"
        ]
        sourceDestCheck: true
        tags           : {
            name: "pulumi"
        }
        ---outputs:---
        associatePublicIpAddress : true
        availabilityZone         : "us-west-2c"
        disableApiTermination    : false
        ebsBlockDevice           : []
        ebsOptimized             : false
        ephemeralBlockDevice     : []
        iamInstanceProfile       : ""
        id                       : "i-01ea9554bb9d44ca8"
        instanceState            : "running"
        ipv6Addresses            : []
        keyName                  : ""
        monitoring               : false
        networkInterface         : []
        networkInterfaceId       : "eni-b25f75b1"
        primaryNetworkInterfaceId: "eni-b25f75b1"
        privateDns               : "ip-172-31-3-189.us-west-2.compute.internal"
        privateIp                : "172.31.3.189"
        publicDns                : "ec2-34-210-217-86.us-west-2.compute.amazonaws.com"
        publicIp                 : "34.210.217.86"
        rootBlockDevice          : [
            [0]: {
                    deleteOnTermination: true
                    iops               : "100"
                    volumeSize         : "8"
                    volumeType         : "gp2"
                }
        ]
        sourceDestCheck          : true
        subnetId                 : "subnet-fd19eaa6"
        tenancy                  : "default"
        volumeTags               : {}
        vpcSecurityGroupIds      : []
    info: 1 change performed:
        + 1 resource created
        2 resources unchanged
    Deployment duration: 34.714820388s
    ```

1. We can see the resources currently in our stack by running `pulumi stack`:

    ```bash
    $ pulumi stack
    Current stack is testing
    Last update at 2017-09-22 12:23:31.2362587 -0700 PDT
    3 resources currently in this stack:

    TYPE                                             NAME
    aws:ec2/securityGroup:SecurityGroup              web-secgrp
    aws:ec2/instance:Instance                        web-server-www
    aws:ec2/instance:Instance                        web-server-api
    ```

    We've successfully created a simple Pulumi program, added a new cloud abstraction with `createInstance` and deployed and updated changes to our infrastructure!

1. To clean up after ourselves, just run `pulumi destroy` and answer the confirmation question at the prompt:

    ```bash
    $ pulumi destroy
    This will permanently destroy all resources in the 'testing' stack!
    Please confirm that this is what you'd like to do by typing ("testing"): testing
    Performing changes:
    - aws:ec2/instance:Instance: (delete)
        [id=i-01ea9554bb9d44ca8]
        [urn=urn:lumi:testing::webserver::aws:ec2/instance:Instance::web-server-api]
        ami            : "ami-7172b611"
        instanceType   : "t2.nano"
        securityGroups : [
            [0]: "web-secgrp-cea08d71378cb4fe"
        ]
        sourceDestCheck: true
        tags           : {
            name: "pulumi"
        }
    - aws:ec2/instance:Instance: (delete)
        [id=i-0b12d17d90b9d343e]
        [urn=urn:lumi:testing::webserver::aws:ec2/instance:Instance::web-server-www]
        ami            : "ami-7172b611"
        instanceType   : "t2.micro"
        securityGroups : [
            [0]: "web-secgrp-cea08d71378cb4fe"
        ]
        sourceDestCheck: true
        tags           : {
            name: "pulumi"
        }
    - aws:ec2/securityGroup:SecurityGroup: (delete)
        [id=sg-4bfe3a36]
        [urn=urn:lumi:testing::webserver::aws:ec2/securityGroup:SecurityGroup::web-secgrp]
        description: "Enable HTTP access"
        ingress    : [
            [0]: {
                    cidrBlocks: [
                        [0]: "0.0.0.0/0"
                    ]
                    fromPort  : 80
                    protocol  : "tcp"
                    toPort    : 80
                }
        ]
        name       : "web-secgrp-cea08d71378cb4fe"
    info: 3 changes deployed:
        - 3 resources deleted
    Update duration: 2m13.232697769s
    ```

> _Note_: Pulumi currently runs all infrastructure updates sequentially to provide the greatest assurance of repeatable
> results.  Parallel execution of infrastructure updates is available with an experimental `--parallel N` flag is
> available, and this will likely become the default in the future.

That's it.  In the next section, we'll take a look at building a higher level Pulumi Program using the
`@pulumi/cloud` framework.

## Next Up: [Programming the Cloud](./cloud.html)

