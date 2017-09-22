---
layout: default
nav_section: "quickstart"
---

# Getting Started

Welcome to Pulumi, a new way to program the cloud! ☁️

In this guide, we'll introduce the core concepts, tools and frameworks for
building and deploying Pulumi cloud applications.

With Pulumi, you write __programs__ that describe your cloud infrastructure and
application behaviour.  These programs have access to __packages__ which provide
cloud primitives you can use to build your application.  You can also build new
custom packages with new components and reuse those components across your cloud
programs.  With the `pulumi` __command-line tool__, you can manage the
deployment of these applications into your cloud provider.

In the current release, Pulumi programs can be authored in JavaScript or
TypeScript (we recommend TypeScript to get the most benefits from the tools and
frameworks).  

> _Note_: We expect to introduce additional languages in future releases.

The current release include three packages to use as building blocks for your
Pulumi programs.  
* [`pulumi`](/libraries/pulumi/index.html) - Core primitives for interacting with the Pulumi runtime
* [`@pulumi/aws`](/libraries/pulumi-aws/index.html) - A library of the full suite of AWS resources (265 resources)
* [`@pulumi/cloud`](/libraries/pulumi-cloud/index.html) - A highly-productive, cloud-neutral library for rapid cloud
  application development

> _Note_: We expect to introduce additional cloud providers and cloud components
> in future releases:

## Setup and Installation

Download `pulumi.zip`, unpack to XXX.  Put YYY on your PATH.  To verify you have
the tools installed, run `pulumi version`.

```bash
$ pulumi version
Pulumi version 0.0.1

```

You will also need to have the AWS CLI installed locally so that you can deploy
Pulumi programs into your AWS account.  Follow the [installation
instructions](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
and then run the following command to ensure you have AWS IAM credentials
configured on your development machine (use your own `Access Key ID`, `Secret
Access Key` and default region):

```
$ aws configure
AWS Access Key ID [****************EVUA]:
AWS Secret Access Key [****************Pd4/]:
Default region name [us-west-2]:
Default output format [None]:
```

Finally, you will need to install Yarn. Follow the [installation
instructions](https://yarnpkg.com/lang/en/docs/install/) and run `yarn
--version` to ensure it is set up correctly.

## Your First Program - AWS EC2 Instance

For our first application, we'll create an AWS [EC2
Instance](/libraries/pulumi-aws/classes/_ec2_instance_.instance.html) and
associated [Security
Group](/libraries/pulumi-aws/classes/_ec2_securitygroup_.securitygroup.html)
using Pulumi.

Create a folder `webserver`.  In that folder, save the following as `index.js`:

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

This example uses the [`@pulumi/aws`](/libraries/pulumi-aws/index.html) package
to create and manage AWS resources. It creates two resources - an
[`aws.ec2.SecurityGroup`](/libraries/pulumi-aws/classes/_ec2_securitygroup_.securitygroup.html)
which allows access for incoming HTTP requests and an
[`aws.ec2.Instance`](/libraries/pulumi-aws/classes/_ec2_instance_.instance.html)
which will be created in that security group using the appropriate Amazon
Machine Image (AMI) for the region where you deploy the program.

> Note that each resource expects a name as the first parameter - this name is
used by Pulumi to track the resources across deployments, and should be a unique
name among all resources of that type in your program.

We also need a `Pulumi.yaml` file to describe the Pulumi application - create
one in the same folder with the following contents:

```
name: webserver
description: Basic example of an AWS web server accessible over HTTP.
runtime: nodejs
```

Run `yarn init` to create a default Node.js `package.json` - since our Pulumi
program is using JavaScript and Node.js.

```
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

And finally `yarn link pulumi @pulumi/aws @pulumi/cloud` to get access to the
Pulumi packages you will use in your code.

You should now have the following files in your `webserver` folder:

```
$ ls
Pulumi.yaml	index.js	node_modules	package.json
```

## Environments, Plans and Deployments

Now that we have the code for our first program, let's deploy it!

Every Pulumi program is deployed to an __environment__.  To create an
environment called `testing`, run the following command:

```
$ pulumi env init testing
Environment 'testing' initialized; see `pulumi deploy` to deploy into it
```

You can now run `pulumi env ls` to see the newly created environment:

```
$ pulumi env ls
NAME                 LAST DEPLOYMENT                                  RESOURCE COUNT
testing*             n/a                                              n/a
```

We can get a preview of what will happen during a deployment by running `pulumi
plan`. Running that command we get an error `Error: Missing required
configuration variable 'aws:config:region'`.  As the error states, before we can
plan or deploy our application, we need to configure the AWS region we will be
targetting.

```
$ pulumi config aws:config:region us-west-2
```

We can now run `pulumi plan`.

```
$ pulumi plan
Planning changes:
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
info: 2 changes planned:
    + 2 resources to create
```

As expected, we see that deploying this program will create two resources.  So
let's go ahead and deploy.  This will take ~30 seconds while the EC2 instance
spins up.

```
$ pulumi deploy
Deploying changes:
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
info: 2 changes deployed:
    + 2 resources created
Deployment duration: 25.518253662s
```

We now have a running EC2 instance.  We can run `aws ec2 describe-instances
--filter Name=tag:name,Values=pulumi` (or open the AWS Console) to see that this
new instance is now running.

Let's now make a change to our program. Instead of creating just one instance,
we'll create a reusable function `createInstance` for creating instances in our
Security Group and use it to create two instances - one for `www` and one for
`api`.  We'll update `index.js` to the following:

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

We can run `pulumi plan` to see what changes this will make to our
infrastructure.  Note that only one new resource is created - the security group
and www instance are unchanged and so do not need to be updated or replaced.

```
$ pulumi plan
Planning changes:
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
info: 1 change planned:
    + 1 resource to create
      2 resources unchanged
```

Having verified that these changes are expected, run `pulumi deploy` to update our infrastructure.

```
$ pulumi deploy
Deploying changes:
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
info: 1 change deployed:
    + 1 resource created
      2 resources unchanged
Deployment duration: 34.714820388s
```

We can see the resources currently in our environment by running `pulumi env`.

```
$ pulumi env
Current environment is testing
    (use `lumi env select` to change environments; `lumi env ls` lists known ones)
Last deployment at 2017-09-22 12:23:31.2362587 -0700 PDT
1 configuration variables set (see `lumi config` for details)
3 resources currently in this environment:

TYPE                                             NAME
aws:ec2/securityGroup:SecurityGroup              web-secgrp
aws:ec2/instance:Instance                        web-server-www
aws:ec2/instance:Instance                        web-server-api
```

We've succesfully created a simple Pulumi program, added a new cloud abstraction
with `createInstance` and deployed and updated changes to our infrastructure!

To cleanup after ourselves, just run `pulumi destroy` and answer the
confirmation question at the prompt:

```
$ pulumi destroy
This will permanently destroy all resources in the 'testing' environment!
Please confirm that this is what you'd like to do by typing ("testing"): testing
Deploying changes:
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
Deployment duration: 2m13.232697769s
```

> _Note_: Pulumi currently runs all infrastructure updates sequentially to
> provide the greatest assurance of repeatable results.  Parallel execution of
> infrastructure updates is available with an experimental `--parallel N` flag
> is available, and this will likely become the default in the future.

That's it.  In the next section, we'll take a look at building a higher level
Pulumi Program using the `@pulumi/cloud` framework.

> __Aside: Lifecycle of a Pulumi Application__
>
>Ahen we re-deployed the application, we did not need to recreate all
>of the infrastructure.  Instead, Pulumi analyses the current state of the
>infrastructure and the requested new state represented by interpreting your
>Pulumi application.  From these, it computes the minimal delta needed to adjust
>the state of the running environment to match the new request.  For some
>resources, changes can be made directly in place with no interruption to your
>infrastructure.  For others, a resource may need to be replaced, and Pulumi
>will create the new resource first, then update any other resources dependent
>on this, before finally removing the no longer needed original resource.
> 
>Today, Pulumi tracks the state of the infrastrucutre in a __checkpoint__ file,
>stored inside the `.lumi` folder.  This checkpoint file file is needed to make
>updates to the infrastructure.  In future releases, Pulumi will support
>additional methods for managing infrastructure state across deployments. 

## Pulumi Cloud Application - URL shortener

The `@pulumi/cloud` package can be used just like any other Pulumi package, but offers several unique 

_TODO:
* `@pulumi/cloud`
* `HttpEndpoint`
* `Table`
* Getting logs from Cloudwatch

## Using TypeScript

You can write Pulumi programs in TypeScript to get additional verification and tooling benefits.  To use TypeScript, apply the following thress steps to an existing progrect:

First, update your `package.json` to look like the following:

```json
{
    "name": "webserver",
    "version": "0.1",
    "main": "bin/index.js",
    "typings": "bin/index.d.ts",
    "scripts": {
        "build": "tsc"
    },
    "devDependencies": {
        "typescript": "^2.1.4"
    },
    "peerDependencies": {
        "@pulumi/aws": "*",
        "@pulumi/pulumi-fabric": "*"
    },
    "dependencies": {
        "@types/node": "^8.0.26"
    }
}
```

Then run `yarn install` to install the new dependencies.

Next, create a `tsconfig.json` file with the following:

```json
{
    "compilerOptions": {
        "outDir": "bin",
        "target": "es6",
        "module": "commonjs",
        "moduleResolution": "node",
        "declaration": true,
        "sourceMap": true,
        "stripInternal": true,
        "experimentalDecorators": true,
        "pretty": true,
        "noFallthroughCasesInSwitch": true,
        "noImplicitAny": true,
        "noImplicitReturns": true,
        "forceConsistentCasingInFileNames": true,
        "strictNullChecks": true
    },
    "files": [
        "index.ts"
    ]
}
```

And finally, run `yarn build` any time you want to update yoru program prior to
running `lumi plan` or `lumi deploy`.

You can now use tools like VS Code to get completion lists, live error reporting
and inline documentation help.

![Pulumi TypeScript in VS Code](./vscode.png)

## Further Reading

Check out the [examples](/examples) and [package](/libraries) documentation for
more details on the kinds of programs you can build with Pulumi.

If you have questions of feedback on anything related to Pulumi, feel free to
reach out to us at inquiries@pulumi.com.

