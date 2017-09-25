---
layout: default 
nav_section: "quickstart"
---

# Getting Started

Welcome to Pulumi, a new way to program the cloud! ☁️

In this guide, we'll introduce the core concepts, tools and frameworks for
building and running Pulumi cloud applications.

* [Setup and Installation](#setup-and-installation)
* [Programming AWS](#programming-aws)
* [Programming the Cloud](#programming-the-cloud)
* [Further Reading](#further-reading)
    * [Pulumi CLI](#pulumi-cli)
    * [Using Typescript](#using-typescript)
* [Wrapping Up](#wrapping-up)

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
* [`pulumi`](/libraries/pulumi/index.html) - Core primitives for interacting
  with the Pulumi runtime
* [`@pulumi/aws`](/libraries/pulumi-aws/index.html) - A library of the full
  suite of AWS resources (265 resources)
* [`@pulumi/cloud`](/libraries/pulumi-cloud/index.html) - A highly-productive,
  cloud-neutral library for rapid cloud application development

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

Now that we've got Pulumi installed, in the next section we'll use Pulumi to to
write our first program using the AWS package.

## Programming AWS

With the `@pulumi/aws` you can use Pulumi to create and manage AWS resources for 
### A Simple Application

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
used by Pulumi to track the resources across updates, and should be a unique
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

### Environments, Updates and Previews

Now that we have the code for our first program, let's deploy it!

Every Pulumi program is deployed to an __environment__.  To create an
environment called `testing`, run the following command:

```
$ pulumi env init testing
Environment 'testing' initialized; see `pulumi update` to deploy into it
```

You can now run `pulumi env ls` to see the newly created environment:

```
$ pulumi env ls
NAME                 LAST UPDATE                                      RESOURCE COUNT
testing*             n/a                                              n/a
```

We can get a preview of what will happen during a deployment by running `pulumi
preview`. Running that command we get an error `Error: Missing required
configuration variable 'aws:config:region'`.  As the error states, before we can
preview or update our application, we need to configure the AWS region we will be
targetting.

```
$ pulumi config aws:config:region us-west-2
```

We can now run `pulumi preview`.

```
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

As expected, we see that updating this program will create two resources.  So
let's go ahead and deploy the update.  This will take ~30 seconds while the EC2 instance
spins up.

```
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

We can run `pulumi preview` to see what changes this will make to our
infrastructure.  Note that only one new resource is created - the security group
and www instance are unchanged and so do not need to be updated or replaced.

```
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

Having verified that these changes are expected, run `pulumi update` to update
our infrastructure.

```
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

We can see the resources currently in our environment by running `pulumi env`.

```
$ pulumi env
Current environment is testing
    (use `lumi env select` to change environments; `lumi env ls` lists known ones)
Last update at 2017-09-22 12:23:31.2362587 -0700 PDT
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

> _Note_: Pulumi currently runs all infrastructure updates sequentially to
> provide the greatest assurance of repeatable results.  Parallel execution of
> infrastructure updates is available with an experimental `--parallel N` flag
> is available, and this will likely become the default in the future.

That's it.  In the next section, we'll take a look at building a higher level
Pulumi Program using the `@pulumi/cloud` framework.

> __Aside: Lifecycle of a Pulumi Application__
>
>When we updated the application, we did not need to recreate all of the
>infrastructure.  Instead, Pulumi analyses the current state of the
>infrastructure and the requested new state represented by interpreting your
>Pulumi application.  From these, it computes the minimal delta needed to adjust
>the state of the running environment to match the new request.  For some
>resources, changes can be made directly in place with no interruption to your
>infrastructure.  For others, a resource may need to be replaced, and Pulumi
>will create the new resource first, then update any other resources dependent
>on this, before finally removing the no longer needed original resource.
> 
>Today, Pulumi tracks the state of the infrastructure in a __checkpoint__ file,
>stored inside the `.lumi` folder.  This checkpoint file file is needed to make
>updates to the infrastructure.  In future releases, Pulumi will support
>additional methods for managing infrastructure state across updates. 

## Pulumi Cloud Application - URL shortener

The `@pulumi/cloud` package lets you program both infrastructure and application
logic using simple, high-level cloud building blocks.  This package has three
key defining attributes:

* __Easy Cloud Development__: The `@pulumi/cloud` library makes it simple to
  build robust and scalable cloud applications with just a few lines of code.  
* __Cloud Agnostic__: The `@pulumi/cloud` library doesn't tie you to using any
  one particular cloud (AWS, Azure, Kubernetes). Applications built using the
  high-level `@pulumi/cloud` components like
  [Table](/libraries/pulumi-cloud/interfaces/_table_.table.html),
  [Topic](/libraries/pulumi-cloud/interfaces/_topic_.topic.html)
  and
  [HttpEndpoint](/libraries/pulumi-cloud/interfaces/_httpendpoint_.httpendpoint.html)
  can be deployed to a variety of cloud platforms.
* __Serverless__: The `@pulumi/cloud` makes it easy to build applications with
  minimal fixed infrastructure, event-driven application logic, and using
  resources that are charged only based on actual consumption.

As our first example, we'll build a simple URL shortener.

We start with just an `index.ts` file importing `@pulumi/cloud`.  (See the
secction on [Using TypeScript](#using-typescript) for additional details on
using TypeScript for your Pulumi program).  We can use the `HttpEndpoint` class
to create a publicly accessible HTTP endpoint.

```typescript
import * as cloud from "@pulumi/cloud";

let app = new cloud.HttpEndpoint("urlshortener");

app.get("/", (req,res) => {
    res.json({hello: "world"});
});

app.publish().then(url => console.log(`Serving at: ${url}`));
```

Note that the signature of the `get` method is similar to Node.js/Express with
request/response parameters and familiar res.json APIs.

We run `pulumi config aws:config:region us-west-2` to set the AWS region to
deploy this application into.  Then run `pulumi update` to deploy this code. 

```
$ pulumi update
...
<snip>
...
info: Serving at: https://hskuj2l449.execute-api.us-west-2.amazonaws.com/stage/
info: 14 changes performed:
    + 14 resources created
Update duration: 38.783839863s
```

And we can curl that endpoint to see our message:

```bash
$ curl https://hskuj2l449.execute-api.us-west-2.amazonaws.com/stage/
{"hello":"world"}
```

We can turn this into a robust hosted URL shortener service in just a few steps.
First, we add a `/shorten` route:

```typescript
app.post("/shorten", (req, res) => {
    let url = req.query["url"];
    let name = req.query["name"];
    console.log(`POST /shorten ${url} ${name}`);
    res.json({shortenedURLName: name});
});
```

Again, we see we can use Express-like APIs to define a simple service.

But we also need to persist the mapping between short name and url.  So we can
define the data store to use for this mapping directly within our application:

```typescript
let urls = new cloud.Table("urls", "name");
```

And then modify our `/shorten` handler to insert into this table.

```typescript
app.post("/shorten", async (req, res) => {
    let url = req.query["url"];
    let name = req.query["name"];
    console.log(`POST /shorten ${url} ${name}`);
    await urls.insert({name, url});
    res.json({shortenedURLName: name});
});
```

Note that we introduced `async` and `await` to wait for the insert to complete
before responding to the REST API request.

We can now push this updated code, which will provision the data store, update
the hosted REST API, and wire up the route handlers to the new code.  We can
then hit the new API endpoint to shorten a URL:

```
$ pulumi update
...
$ curl -X POST "https://hskuj2l449.execute-api.us-west-2.amazonaws.com/stage/shorten?name=g&url=http://www.google.com"
{"shortenedURL":"g"}
```

And finally, we can implement the `GET `handlers for any registered short name
to return a 301 response with Location header to redirect.

```
app.get("/{name}", async (req, res) => {
    let name = req.params["name"];
    let data = await urls.get({name});
    console.log(`GET /${name} => ${data.url}`)
    res.setHeader("Location", data.url);
    res.status(301);
    res.end("");
});
```

And invoke it:

```
$ pulumi update
...
$ curl https://hskuj2l449.execute-api.us-west-2.amazonaws.com/stage/g
<!doctype html>...contents of google.com ...
...
```

We have a working URL shortener with persistent storage and robust and scalable compute!

That's a quick tour of the `@pulumi/cloud` framework, check out the [documentation](/libraries/pulumi-cloud/) for more details.

## Further Reading

### Pulumi CLI

The `pulumi` CLI supports creating, configuring and updating Pulumi program
environments.  

An __environment__ represents a running Pulumi program.  `pulumi env init`
creates a new Pulumi environment for the program in the working directory.
Multiple environments can be managed in a single program directory, and you can
see all environments with `pulumi env ls`.  

Each environment has an associated set of __config__.  The config is a set of
key value pairs which are available to your Pulumi program.

The running application can be __updated__, combining the current config with
the current version of the program in the working directory and dploying those
updates into the running application - updating any necessary infrastructure and
deploying any new code or resources into the application.

An update can be __previewed__, displaying a summary of the expected changes
that will be made during an update operation based on the current state of the
program and config.  This preview is a convervative summary - it will include
updates which may not need to be made depending on the results of applying some
of the changes to the target infrastructure.  

```
Usage:
  pulumi [command]

Available Commands:
  config      Query, set, replace, or unset configuration values
  destroy     Destroy an existing environment and its resources
  env         Manage target environments
  help        Help about any command
  preview     Show a preview of updates to an environment's resources
  update      Update the resources in an environment
  version     Print Pulumi's version number

Flags:
  -h, --help          help for pulumi
      --logflow       Flow log settings to child processes (like plugins)
      --logtostderr   Log to stderr instead of to files
  -v, --verbose int   Enable verbose logging (e.g., v=3); anything >3 is very verbose

Use "pulumi [command] --help" for more information about a command.
```

__pulumi env__

```
Manage target environments

An environment is a named update target, and a single project may have many of them.
Each environment has a configuration and update history associated with it, stored in
the workspace, in addition to a full checkpoint of the last known good update.

Usage:
  pulumi env [flags]
  pulumi env [command]

Available Commands:
  init        Create an empty environment with the given name, ready for updates
  ls          List all known environments
  rm          Remove an environment and its configuration
  select      Switch the current workspace to the given environment

Flags:
  -h, --help        help for env
  -i, --show-ids    Display each resource's provider-assigned unique ID
  -u, --show-urns   Display each resource's Pulumi-assigned globally unique URN

Global Flags:
      --logflow       Flow log settings to child processes (like plugins)
      --logtostderr   Log to stderr instead of to files
  -v, --verbose int   Enable verbose logging (e.g., v=3); anything >3 is very verbose

Use "pulumi env [command] --help" for more information about a command.
```

__pulumi config__ 

```
Query, set, replace, or unset configuration values

Usage:
  pulumi config [<key> [value]] [flags]

Flags:
  -e, --env string   Choose an environment other than the currently selected one
  -h, --help         help for config
      --unset        Unset a configuration value

Global Flags:
      --logflow       Flow log settings to child processes (like plugins)
      --logtostderr   Log to stderr instead of to files
  -v, --verbose int   Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

__pulumi update__

```
Update the resources in an environment

This command updates an existing environment whose state is represented by the
existing snapshot file. The new desired state is computed by compiling and evaluating an
executable package, and extracting all resource allocations from its resulting object graph.
These allocations are then compared against the existing state to determine what operations
must take place to achieve the desired state. This command results in a full snapshot of the
environment's new resource state, so that it may be updated incrementally again later.

By default, the package to execute is loaded from the current directory. Optionally, an
explicit path can be provided using the [package] argument.

Usage:
  pulumi update [<package>] [-- [<args>]] [flags]

Flags:
      --analyzer stringSlice     Run one or more analyzers as part of this update
  -d, --debug                    Print detailed debugging output during resource operations
  -e, --env string               Choose an environment other than the currently selected one
  -h, --help                     help for update
  -p, --parallel int             Allow P resource operations to run in parallel at once (<=1 for no parallelism)
      --show-config              Show configuration keys and variables
      --show-replacement-steps   Show detailed resource replacement creates and deletes instead of a single step (default true)
      --show-sames               Show resources that needn't be updated because they haven't changed, alongside those that do
  -s, --summary                  Only display summarization of resources and operations

Global Flags:
      --logflow       Flow log settings to child processes (like plugins)
      --logtostderr   Log to stderr instead of to files
  -v, --verbose int   Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

__pulumi preview__

```
Show a preview of updates an environment's resources

This command displays a preview of the updates to an existing environment whose state is
represented by an existing snapshot file. The new desired state is computed by compiling
and evaluating an executable package, and extracting all resource allocations from its
resulting object graph. These allocations are then compared against the existing state to
determine what operations must take place to achieve the desired state. No changes to the
environment will actually take place.

By default, the package to execute is loaded from the current directory. Optionally, an
explicit path can be provided using the [package] argument.

Usage:
  pulumi preview [<package>] [-- [<args>]] [flags]

Flags:
      --analyzer stringSlice     Run one or more analyzers as part of this preview
  -d, --debug                    Print detailed debugging output during resource operations
  -e, --env string               Choose an environment other than the currently selected one
  -h, --help                     help for preview
  -p, --parallel int             Allow P resource operations to run in parallel at once (<=1 for no parallelism)
      --show-config              Show configuration keys and variables
      --show-replacement-steps   Show detailed resource replacement creates and deletes instead of a single step
      --show-sames               Show resources that needn't be updated because they haven't changed, alongside those that do
  -s, --summary                  Only display summarization of resources and operations

Global Flags:
      --logflow       Flow log settings to child processes (like plugins)
      --logtostderr   Log to stderr instead of to files
  -v, --verbose int   Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

### Using TypeScript

You can write Pulumi programs in TypeScript to get additional verification and
tooling benefits.  To use TypeScript, apply the following thress steps to an
existing progrect:

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
running `pulumi preview` or `pulumi update`.

You can now use tools like VS Code to get completion lists, live error reporting
and inline documentation help.

![Pulumi TypeScript in VS Code](./vscode.png)

## Wrapping Up

Check out the [examples](/examples) and [package](/libraries) documentation for
more details on the kinds of programs you can build with Pulumi.

If you have questions of feedback on anything related to Pulumi, feel free to
reach out to us at inquiries@pulumi.com.

