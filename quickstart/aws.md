---
title: Programming AWS
---

<!-- Common links -->
[EC2 Instance]: /packages/pulumi-aws/classes/_ec2_instance_.instance.html
[Security Group]: /packages/pulumi-aws/classes/_ec2_securitygroup_.securitygroup.html
[`@pulumi/aws`]: /packages/pulumi-aws/index.html
<!-- End common links -->

The `@pulumi/aws` package allows you use Pulumi to create and manage AWS resources using JavaScript or TypeScript. You can use regular programming language constructs, such as objects, functions, and control flow. Resource definitions are declarative: they describe the desired end state of your infrastructure. Pulumi will automatically make resource changes based on the current state of what has already been provisioned.

Each AWS resource is exposed as a class under a submodule of `aws`. For example, here are some commonly used services:

* EC2 VM instances, `aws.ec2.Instance`
* S3 buckets, `aws.s3.Bucket`, and objects, `aws.s3.Object`
* DynamoDB tables, `aws.dynamodb.Table`
* Lambda functions, `aws.lambda.Function`

## Prerequisites

-  [Install the Pulumi SDK for your platform](../install)
-  [Configure the AWS CLI](../install/aws-config.html)
-  [Set up your NPM token](../install/configure-npm.html)

{% include aws-resource-warning.md %}

## Provision EC2 instances

For our first JavaScript application, we'll create an AWS [EC2 Instance] and associated [Security Group] using Pulumi. 

### Set up the project

1.  Create a folder `webserver`:

    ```bash
    $ mkdir webserver
    $ cd webserver
    ```

1.  Create an empty project via `pulumi new`:

    ```
    $ pulumi new javascript
    ```

1. Run `npm install` to install package dependencies.

### Add code to provision an EC2 instance

Create a new file `index.js` with the following contents:

```javascript
"use strict";

const aws = require("@pulumi/aws");

let size = "t2.micro";    // t2.micro is available in the AWS free tier
let ami  = "ami-7172b611" // AMI for Amazon Linux in us-west-2 (Oregon)
// let ami  = "ami-6869aa05" // AMI for Amazon Linux in us-east-1 (Virginia)

// create a new security group for port 80
let group = new aws.ec2.SecurityGroup("web-secgrp", { 
    description: "Enable HTTP access",
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

let server = new aws.ec2.Instance("web-server-www", {
    tags: { "Name": "web-server-www" },
    instanceType: size,
    securityGroups: [ group.name ], // reference the group object above
    ami: ami,
});

exports.publicIp = server.publicIp;
exports.publicDns = server.publicDns;
```

This example uses the [`@pulumi/aws`] package to create and manage AWS resources.  It creates two resources: an [`aws.ec2.SecurityGroup`][Security Group], which allows access for incoming HTTP requests, and an [`aws.ec2.Instance`][EC2 Instance], which will be created in that security group using the appropriate Amazon Machine Image (AMI) for the region where you deploy the program.

This simple example shows some of the power of Pulumi. To define a security group, we simply create a top-level object [`aws.ec2.SecurityGroup`][Security Group], which allows access for incoming HTTP requests. We can then reference this security group anywhere in the code. Pulumi will automatically turn the object reference into a resource reference.

### Stacks, updates and previews

Now let's deploy the code. Pulumi programs are deployed to a [stack](../reference/stack.html), which is an isolated, independently configurable instance of a Pulumi program.

1.  Run `init` to set up a location for local state. Note: In future releases, the `init` command won't be necessary.

    ```bash
    $ pulumi init
    Initialized Pulumi repository in /Users/donnam/src/hello-world/.pulumi
    ```

1.  Create a new Pulumi stack called `testing`: 

    ```bash
    $ pulumi stack init testing
    ```

1.  Set the AWS region to `us-west-2`. If you want to use a different region, modify the code so that you're using the right AMI.

    ```bash
    $ pulumi config set aws:region us-west-2
    warning: saved config key 'aws:region' value 'us-west-2' as plaintext; re-run with --secret to encrypt the value instead. Use--plaintext to avoid this warning
    ```

    You can view config values for the current stack via `pulumi config`:

    ```bash
    $ pulumi config
    KEY                              VALUE
    aws:config:region                us-west-2
    ```

1.  To see what will happen when the program is deployed, without actually creating any resources, run `pulumi preview`: 

    ```
    $ pulumi preview
    Previewing changes:
    + pulumi:pulumi:Stack: (create)
        [urn=urn:pulumi:testing::webserver::pulumi:pulumi:Stack::webserver-testing]
        + aws:ec2/securityGroup:SecurityGroup: (create)
            [urn=urn:pulumi:testing::webserver::aws:ec2/securityGroup:SecurityGroup::web-secgrp]
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
            name               : "web-secgrp-a4bfc6a"
            revokeRulesOnDelete: false
        + aws:ec2/instance:Instance: (create)
            [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www]
            ami            : "ami-7172b611"
            instanceType   : "t2.micro"
            securityGroups : [
                [0]: "web-secgrp-a4bfc6a"
            ]
            sourceDestCheck: true
            tags           : {
                Name: "web-server-www"
            }
    ---outputs:---
    publicDns: computed<string>
    publicIp : computed<string>
    info: 3 changes previewed:
        + 3 resources to create
    ```

    Note the output values `publicDns` and `publicIp` are not yet available, as they depend on the properties of a provisioned resource. The update shows that it will create 3 resources, rather than 2. The stack itself is counted as a resource, even though it does not correspond to physical infrastructure. 

    To see a summarized view of what will be deployed, use the `--summary` flag.

1.  Now, let's deploy the program and provision resources, via `pulumi update`. The output below has been condensed. This time, there is a real URL for the server.

    ```bash
    $ pulumi update
    Performing changes:
    + pulumi:pulumi:Stack: (create)
        [urn=urn:pulumi:testing::webserver::pulumi:pulumi:Stack::webserver-testing]
        + aws:ec2/securityGroup:SecurityGroup: (create)
            [urn=urn:pulumi:testing::webserver::aws:ec2/securityGroup:SecurityGroup::web-secgrp]
            description        : "Enable HTTP access"
            ...
        ---outputs:---
            ...
    ---outputs:---
    publicDns: "ec2-54-201-96-130.us-west-2.compute.amazonaws.com"
    publicIp : "54.201.96.130"
    info: 3 changes performed:
        + 3 resources created
    Update duration: 19.949019861s
    ```

1.  Since this is an instance running in your own AWS account, you can view the instance properties in either the AWS console or by running `aws ec2 describe-instances`.

1.  To view your provisioned resources, run `pulumi stack`. To see full details, use the `--show-ids` or `-i` flag.

    ```
    $ pulumi stack
    Current stack is testing:
        Managed by donnam-sunshine.local
        Last updated 3 minutes ago (2018-03-21 23:43:37.067338 -0700 PDT)
        Pulumi version v0.11.0
        Plugin nodejs [language] version 0.11.0
        Plugin aws [resource] version 0.11.0

    Current stack resources (3):
        TYPE                                             NAME
        pulumi:pulumi:Stack                              webserver-testing
        aws:ec2/securityGroup:SecurityGroup              web-secgrp
        aws:ec2/instance:Instance                        web-server-www

    Current stack outputs (2):
        OUTPUT                                           VALUE
        publicDns                                        ec2-54-201-96-130.us-west-2.compute.amazonaws.com
        publicIp                                         54.201.96.130

    Use `pulumi stack select` to change stack; `pulumi stack ls` lists known ones
    ```

1.  To view stack output properties, run `pulumi stack output` or `pulumi stack output [propertyName]`:

    ```
    $ pulumi stack output
    Current stack outputs (2):
        OUTPUT                                           VALUE
        publicDns                                        ec2-54-201-96-130.us-west-2.compute.amazonaws.com
        publicIp                                         54.201.96.130
    ```

    ```
    $ pulumi stack output publicDns
    ec2-54-201-96-130.us-west-2.compute.amazonaws.com
    ```

### Add a startup script

The EC2 instance exists and is exposed to the internet, but doesn't actually do anything. A simple way to set up an HTTP endpoint is to use the `userData` property of `ec2.Instance`. 

Add the a definition for `userData` and use it in the `ec2.Instance` constructor call:

```javascript
let userData = 
`#!/bin/bash
nohup python -m SimpleHTTPServer 80 &`;

let server = new aws.ec2.Instance("web-server-www", {
    tags: { "Name": "web-server-www" },
    instanceType: size,
    securityGroups: [ group.name ], // reference the group object above
    ami: ami,
    // add this line
    userData: userData              // start a simple web server
});
```

Now, when you run `pulumi preview` and `pulumi update`, you'll see that the security group stays the same, but the EC2 instance is recreated. While it would be possible to stop the existing instance and [change the user data property](https://aws.amazon.com/premiumsupport/knowledge-center/execute-user-data-ec2/), the principle of [immutable infrastructure](../reference/index.html#immutable-infrastructure) means that it's preferable to create a new instance with the desired configuration, rather than modify a resource in place.

Give the instances a few minutes to initialize, then run `curl` on the URL:

```bash
curl `pulumi stack output webUrl`    
```

### Leverage a reusable component

Since a Pulumi program is a real JavaScript program, we can create abstractions. Let's create a function that creates instances, which we'll use to create two instances, `www` and `api`.

1.  Rename `index.js` to `webserver.js`.

1.  Remove the exported properties:

    ```javascript
    // remove these
    exports.publicIp = server.publicIp;
    exports.publicDns = server.publicDns;
    ```

1.  Remove the definition of `server` and replace with the following:

    ```javascript
    exports.createInstance = function (name, size) {
        return new aws.ec2.Instance(name, {
            tags: { "Name": name },
            instanceType: size,
            securityGroups: [ group.name ], // reference the group object above
            ami: ami,
            userData: userData              // start a simple web server
        });
    }
    ```

1.  Create `index.js` with the following contents. This will provision two EC2 instances with different sizes.

    ```javascript
    const webserver = require("./webserver.js");

    let webInstance = webserver.createInstance("web-server-www", "t2.nano");
    let appInstance = webserver.createInstance("web-server-app", "t2.micro");

    exports.webUrl = webInstance.publicDns.apply(dns => `http://${dns}`); // apply transformation to output property
    ```

1.  Run `pulumi preview` to see what changes this will make to your infrastructure. Note that only one new resource is created: since the security group and `web-server-www` instance are unchanged, they do not need to be updated or replaced.

    ```
    $ pulumi preview
    Previewing changes:
    * pulumi:pulumi:Stack: (same)
        [urn=urn:pulumi:testing::webserver::pulumi:pulumi:Stack::webserver-testing]
    ---outputs:---
    publicDns: "ec2-54-218-126-61.us-west-2.compute.amazonaws.com"
    publicIp : "54.218.126.61"
        ~ aws:ec2/instance:Instance: (update)
            [id=i-0d4825f3ba8d290dd]
            [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www]
            ami            : "ami-7172b611"
          - instanceType   : "t2.micro"
          + instanceType   : "t2.nano"
            securityGroups : [
                [0]: "web-secgrp-387bb0d"
            ]
            sourceDestCheck: true
            tags           : {
                Name: "web-server-www"
            }
            userData       : "#!/bin/bash\n    echo \"Hello, World!\" > index.html\n    nohup python -m SimpleHTTPServer 80 &"
        + aws:ec2/instance:Instance: (create)
            [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-app]
            ami            : "ami-7172b611"
            instanceType   : "t2.micro"
            securityGroups : [
                [0]: "web-secgrp-387bb0d"
            ]
            sourceDestCheck: true
            tags           : {
                Name: "web-server-app"
            }
            userData       : "#!/bin/bash\n    echo \"Hello, World!\" > index.html\n    nohup python -m SimpleHTTPServer 80 &"
    ---outputs:---
    webUrl: computed<string>
    info: 2 changes previewed:
        + 1 resource to create
        ~ 1 resource to update
          2 resources unchanged
    ```

1.  Run `pulumi update` to make the resource changes. 

So, with a simple and natural extension the the original code, we've created a true cloud component. Anyone who uses the `webserver` package can automatically leverage the logic we've defined.

### Create an instance in each availability zone

For a production service, you would typically deploy a virtual machine in each availability zone for the AWS region. For this, we'll use the function `aws.getAvailabilityZones()`, which calls an AWS API to get all zones. We can then loop over all availability zones and create an instance in that zone.

Since the list of availability zones is dynamic data, it is very difficult to create this infrastructure specification in CloudFormation or similar tools. Since Pulumi allows you to define infrastructure requirements directly in code, this scenario is very easy to define in Pulumi.

TODO: link to examples.zip

For an example of this, see the example `webserver-zones` in [examples.zip]()

## Clean up

1. To clean up the provisioned resources, run `pulumi destroy` and answer the confirmation question at the prompt:

   ```
   $ pulumi destroy
   This will permanently destroy all resources in the 'testing' stack!
   Please confirm that this is what you'd like to do by typing ("testing"): testing
   Performing changes:
   - aws:ec2/instance:Instance: (delete)
      [id=i-0de2b82c7cedbc0dc]
      [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www-2]
      <snip>
   - aws:ec2/instance:Instance: (delete)
      [id=i-0f442c1c4b7326fb4]
      [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www-1]
      <snip>
   - aws:ec2/instance:Instance: (delete)
      [id=i-00b2217ec6726d66d]
      [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www-0]
      <snip>
   - aws:ec2/securityGroup:SecurityGroup: (delete)
      [id=sg-14f97668]
      [urn=urn:pulumi:testing::webserver::aws:ec2/securityGroup:SecurityGroup::web-secgrp]
      <snip>
   - pulumi:pulumi:Stack: (delete)
      [urn=urn:pulumi:testing::webserver::pulumi:pulumi:Stack::webserver-testing]
   info: 5 changes performed:
      - 5 resources deleted
   Update duration: 3m4.947625452s
   ```

## Summary

You've seen how easy it is to use Pulumi to provision infrastructure in a repeatable fashion. Pulumi programs specify infrastructure requirements and you can use a general-purpose programming language to define your infrastructure. You can easily use objects, functions, and control flow. And, if you use a language like TypeScript, you'll automatically get compile errors if you use an API incorrectly.

The `pulumi preview` command shows what changes will be made to your infrastructure before you actually update any resources, giving you confidence that the deployment will do what you expect.

In the next section, we'll take a look at building a higher level Pulumi Program using the
`@pulumi/cloud` framework.

## Next Steps

To learn how to use Pulumi's high-level programming model, see [Programming the cloud](./cloud.html)

