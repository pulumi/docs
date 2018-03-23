---
title: Programming AWS
---

The `@pulumi/aws` package allows you use Pulumi to create and manage AWS resources using JavaScript or TypeScript. You can use regular programming language constructs, such as objects, functions, and control flow. Resource definitions are declarative: they describe the desired end state of your infrastructure. Pulumi will automatically make resource changes based on the current state of what has already been provisioned.

Each AWS resource is exposed as a class under a submodule of `aws`. For example, here are some commonly used services:

* EC2 VM instances, `aws.ec2.Instance`
* S3 buckets, `aws.s3.Bucket`, and objects, `aws.s3.Object`
* DynamoDB tables, `aws.dynamodb.Table`
* Lambda functions, `aws.lambda.Function`

## Provision an EC2 instance with AMI lookup

For our first application, we'll create an AWS [EC2 Instance](/packages/pulumi-aws/classes/_ec2_instance_.instance.html)
and associated [Security Group](/packages/pulumi-aws/classes/_ec2_securitygroup_.securitygroup.html) using Pulumi. We'll do a lookup to get the appropriate AMI for the AWS region and machine type. This example uses TypeScript to get improved validation of the program, but you can also use JavaScript.

{% include aws-resource-warning.md %}

### Set up the project

1. Create a folder `webserver`:

   ```bash
   $ mkdir webserver
   $ cd webserver
   ```

1. Since this example uses TypeScript, create `package.json` in the project folder:

   ```json
   {
      "name": "url-shortener",
      "version": "1.0.0",
      "license": "MIT",
      "main": "bin/index.js",
      "typings": "bin/index.d.ts",
      "scripts": {
         "build": "tsc"
      },
      "devDependencies": {
         "typescript": "^2.1.4"
      },
      "peerDependencies": {
         "@pulumi/cloud": "*"
      },
      "dependencies": {
         "@types/node": "^8.0.26"
      }  
   }
   ```

1. Create a `tsconfig.json` file with the TypeScript compiler settings and a list of your program files:

   ```json
   {
      "compilerOptions": {
         "outDir": "bin",
         "target": "es6",
         "lib": [
               "es6"
         ],
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

1. Create `Pulumi.yaml` with the following contents:

   ```yaml
   name: webserver
   runtime: nodejs
   description: Basic example of an AWS web server accessible over HTTP.
   ```

1. Run `yarn install` or `npm install` to install the dependencies to your `node_modules` directory.

1. Link with the Pulumi SDK packages so that your `require`s will find the right thing, using either `yarn` or `npm`:

   ```bash
   $ yarn link pulumi @pulumi/aws
   ```

### Add code to provision an EC2 instance

Create a new file `index.ts` with the following contents:

```typescript
import * as aws from "@pulumi/aws";

// the type InstanceType contains friendly names for AWS instance sizes
let size: aws.ec2.InstanceType = "t2.micro"; 

// create a new security group for port 80
let group = new aws.ec2.SecurityGroup("web-secgrp", { 
    description: "Enable HTTP access",
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

// (optional) create a simple web server using the startup script for the instance
// use the AWS metadata service to get the availability zone for the instance
let userData = 
    `#!/bin/bash
    echo "Hello, World!\nInstance metadata:" > index.html
    curl http://169.254.169.254/latest/meta-data/placement/availability-zone >> index.html
    nohup python -m SimpleHTTPServer 80 &`;

let server = new aws.ec2.Instance("web-server-www", {
    tags: { "Name": "web-server-www" },
    instanceType: size,
    securityGroups: [ group.name ],     // reference the group object above
    ami: aws.ec2.getLinuxAMI(size),     // call built-in function (can also be custom)
    userData: userData                  // set up a simple web server    
});

server.publicDns.then(dns => console.log(`Server URL: http://${dns}`));
```

This example uses the [`@pulumi/aws`](/packages/pulumi-aws/index.html) package to create and manage AWS resources.  It creates two resources: an [`aws.ec2.SecurityGroup`](/packages/pulumi-aws/classes/_ec2_securitygroup_.securitygroup.html), which allows access for incoming HTTP requests, and an [`aws.ec2.Instance`](/packages/pulumi-aws/classes/_ec2_instance_.instance.html), which will be created in that security group using the appropriate Amazon Machine Image (AMI) for the region where you deploy the program.

*Note that each resource expects a name as the first parameter. This name is used by Pulumi to track the resources across updates, and should be a unique name among all resources of that type in your program.*

This example shows the power of Pulumi:
- The `pulumi/aws` package contains the type `aws.ec2.InstanceType`, which has the friendly names of all AWS instance sizes. If you mistype the instance size, you'll have a TypeScript compile error.
- To define a security group, we simply create a top-level object [`aws.ec2.SecurityGroup`](/packages/pulumi-aws/classes/_ec2_securitygroup_.securitygroup.html), which allows access for incoming HTTP requests. We can then reference this security group anywhere in the code. Pulumi will automatically turn the object reference into a resource reference.
- The AMI for the Amazon Linux image varies based on region. So, we wrote a custom function that looks up the correct image ID based on the current region using the `aws.getAmi()` function.
- When we create the EC2 instance, we can simply reference other objects in the program, such as the security group and the `getLinuxAmi()` helper function. 

### Stacks, updates and previews

Now that we have the code for our first program, let's deploy it!

Every Pulumi program is deployed to a __stack__.  A stack is an isolated, independently configurable
target in which programs will run.  It's reasonable to have many stacks: often you'll have different development,
staging, and production stacks. In fact, you may have multiple of each kind, such as east coast and west coast
production.

1. Compile the code via `yarn build` or `tsc`.

1. Create a Pulumi repository. A repository is a collection of Pulumi projects:

   ```bash
   $ pulumi init
   Initialized Pulumi repository in /Users/donnam/src/hello-world/.pulumi
   ```

1. Create a new Pulumi stack called "testing". (Be sure to pass the `--local` flag, as otherwise the command will attempt to create a stack in the Pulumi hosted service.)

   ```bash
   $ pulumi stack init testing --local
   ```

1. We can get a preview of what will happen during a deployment by running `pulumi preview`. If you run it now, you'll see an error, because the AWS region has not yet been selected:

   ```
   Previewing changes:
    error: Missing required configuration variable 'aws:config:region'
           please set a value using the command `pulumi config set aws:config:region <value>`
    error: An error occurred while advancing the preview: an unhandled error occurred: Program exited with non-zero exit code: 1
    ```
   
   To configure the region, use the `config set` command. For example, to choose `us-west-2`:

   ```bash
   $ pulumi config set aws:config:region us-west-2
   warning: saved config key 'aws:config:region' value 'us-west-2' as plaintext; re-run with --secret to encrypt the value instead
   ```

   You can view config values for the current stack via `pulumi config`:

   ```bash
   $ pulumi config
   KEY                              VALUE
   aws:config:region                us-west-2
   ```

1. We can now successfully run `pulumi preview` to see the complete set of resources that will be created. This does not actually provision anything.

   ```bash
   $ pulumi preview --summary
   Previewing changes:
   + pulumi:pulumi:Stack: (create)
      [urn=urn:pulumi:testing::webserver::pulumi:pulumi:Stack::webserver-testing]
      + aws:ec2/securityGroup:SecurityGroup: (create)
         [urn=urn:pulumi:testing::webserver::aws:ec2/securityGroup:SecurityGroup::web-secgrp]
      + aws:ec2/instance:Instance: (create)
         [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www]
   info: Server URL: http://undefined
   info: 3 changes previewed:
      + 3 resources to create
   ```

   Note that the server URL is `http://undefined`. This is expected, as Pulumi won't know the resource name until it has been provisioned at least once.
   
   Note that the update shows that it will create 3 resources, rather than 2. The stack itself is counted as a resource, even though it does not correspond to physical infrastructure. 

   To see full details of what will be deployed, leave off the `--summary` flag.

1. Let's go ahead and deploy the update. This will take about 30 seconds as it waits for the actual EC2 instance to finish spinning up:

   ```bash
   $ pulumi update
   Performing changes:
   + pulumi:pulumi:Stack: (create)
      [urn=urn:pulumi:testing::webserver::pulumi:pulumi:Stack::webserver-testing]
      + aws:ec2/securityGroup:SecurityGroup: (create)
         [urn=urn:pulumi:testing::webserver::aws:ec2/securityGroup:SecurityGroup::web-secgrp]
         <snip>
      + aws:ec2/instance:Instance: (create)
         [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www]
         ami            : "ami-7172b611"
         instanceType   : "t2.micro"
         securityGroups : [
               [0]: "web-secgrp-1522198"
         ]
         <snip>
   info: Server URL: http://ec2-52-26-240-166.us-west-2.compute.amazonaws.com
   info: 3 changes performed:
      + 3 resources created
   Update duration: 29.867075499s
   ```

   This time, there is a real URL for the server.

1. Give the instance a few minutes to initialize, then verify that the server is running:

   ```bash
   $ curl http://your-url.us-west-2.compute.amazonaws.com
   Hello, World!
   Instance metadata:
   us-west-2a    
   ```

1. Since this is an instance running in your own AWS account, you can run `aws ec2 describe-instances --filter Name=tag:name,Values=pulumi`, or open the AWS Console, to view the instance properties.

1. You can always view your provisioned resources via `pulumi stack`. To see full details, use the `--show-ids` or `-i` flag:

   ```bash
   Current stack is testing:
      Managed by Donnas-MacBook-Pro.local
      Last updated at 2017-12-14 17:33:27.40281 -0800 PST
      Pulumi version v0.9.3
      Plugin pulumi-provider-aws [resource] version v0.9.3
      Plugin pulumi-langhost-nodejs [language] version v0.9.3

   Current stack resources (3):
      TYPE                                             NAME
      pulumi:pulumi:Stack                              webserver-testing
      aws:ec2/securityGroup:SecurityGroup              web-secgrp
      aws:ec2/instance:Instance                        web-server-www

   Current stack outputs (0):
      No output values currently in this stack

   Use `pulumi stack select` to change stack; `pulumi stack ls` lists known ones
   ```    

## Leverage a reusable component

Now, let's create a function that creates instances. We can then use it to create two instances: one for `www` and one for `api`.

1. Rename `index.ts` to `webserver.ts`.

1. Remove the last line of code:

   ```typescript
   // remove this line:
   server.publicDns.then(url => console.log(`Server URL: http://${url}`));
   ```

1. Remove the definition of `server` and replace with the following:

   ```typescript
   export function createInstance(name: string, size: aws.ec2.InstanceType): aws.ec2.Instance {
      let result = new aws.ec2.Instance(name, {
         tags: { "Name": name },             // use the `name` parameter
         instanceType: size,                 // use function argument for size
         securityGroups: [ group.name ],     // reference the group object above
         ami: getLinuxAmi(),                 // call custom function
         userData: userData                  // set up a simple web server    
      });

      result.publicDns.then(url => console.log(`Server URL: http://${url}`));

      return result;
   }
   ```

1. Create a new file `index.ts` with the following contents. This will provision two EC2 instances with different sizes.

   ```typescript
   import * as aws from "@pulumi/aws";
   import * as webserver from "./webserver"; // use the new custom component

   let webInstance = webserver.createInstance("web-server-www", "t2.micro");
   let appInstance = webserver.createInstance("web-server-app", "t2.nano");
   ```

1. Compile via `yarn build` or `tsc`.

1. Run `pulumi preview` to see what changes this will make to your infrastructure. Note that only one new resource is created: since the security group and `web-server-www` instance are unchanged, they do not need to be updated or replaced. So, only the new server has a undefined URL.

   ```bash
   $ pulumi preview
   Previewing changes:
   * pulumi:pulumi:Stack: (same)
      [urn=urn:pulumi:testing::webserver::pulumi:pulumi:Stack::webserver-testing]
   info: Server URL: http://ec2-34-216-29-77.us-west-2.compute.amazonaws.com
      + aws:ec2/instance:Instance: (create)
         [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-app]
         ami            : "ami-7172b611"
         instanceType   : "t2.nano"
         securityGroups : [
               [0]: "web-secgrp-f8391fc"
         ]
         sourceDestCheck: true
         tags           : {
               Name: "web-server-app"
         }
         userData       : "#!/bin/bash\n    echo \"Hello, World!\nInstance metadata:\" > index.html\n    curl http://169.254.169.254/latest/meta-data/placement/availability-zone >> index.html\n    nohup python -m SimpleHTTPServer 80 &"
   info: Server URL: http://undefined
   info: 1 change previewed:
      + 1 resource to create
      3 resources unchanged
   ```

1. Run `pulumi update` to make the resource changes:

   ```bash
   $ pulumi update
   Performing changes:
   * pulumi:pulumi:Stack: (same)
      [urn=urn:pulumi:testing::webserver::pulumi:pulumi:Stack::webserver-testing]
   info: Server URL: http://ec2-34-216-29-77.us-west-2.compute.amazonaws.com
      + aws:ec2/instance:Instance: (create)
      <snip>
   info: Server URL: http://ec2-52-89-84-84.us-west-2.compute.amazonaws.com
   info: 1 change performed:
      + 1 resource created
      3 resources unchanged
   Update duration: 16.105927027s
   ```

With a simple and natural extension the the original code, we've created a true cloud component. Anyone who uses the `webserver` package can automatically leverage the logic we've defined.

### Create an instance in each availability zone

For a production service, you would typically deploy a virtual machine in each availability zone for the AWS region. For this, we'll use the function `aws.getAvailabilityZones()`, which calls an AWS API to get all zones. We can then loop over all availability zones and create an instance in that zone.

Since the list of availability zones is dynamic data, it is very difficult to create this infrastructure specification in CloudFormation or similar tools. Since Pulumi allows you to define infrastructure requirements directly in code, this scenario is very easy to define in Pulumi.

Make the following changes to the code:

1. In `webserver.ts`, add a new string function argument for availability zone in `createInstance`, and pass the property `availabilityZone: zone` to the `aws.ec2.Instance` constructor. 

   ```typescript
   export function createInstance(name: string, size: aws.ec2.InstanceType, zone: string): aws.ec2.Instance {
      let result = new aws.ec2.Instance(name, {
         availabilityZone: zone,
      // ...
   ```    

1. In `index.ts`, remove the definitions of `webInstance` and `appInstance`. Add the following code to create an EC2 instance in each availability zone in the region:

   ```typescript
   // the async block is currently required, due to the use of `await` 
   // this will be improved in the future
   (async () => {
      let zones: string[] = (await aws.getAvailabilityZones()).names;
      for (let i = 0; i < zones.length; i++) {
         let server = webserver.createInstance("web-server-www-" + i, "t2.micro", zones[i]);
      }
   })();    
   ```

1. Run `yarn build`.

1. Run `pulumi preview`. Since we changed the instance name, two resources will be deleted and 3 resources will be created, as there are 3 availability zones in west-us-2:

   ```bash
   $ pulumi preview --summary
   Previewing changes:
   * pulumi:pulumi:Stack: (same)
      [urn=urn:pulumi:testing::webserver::pulumi:pulumi:Stack::webserver-testing]
   + aws:ec2/instance:Instance: (create)
      [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www-0]
   info: Server URL: http://undefined
   + aws:ec2/instance:Instance: (create)
      [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www-1]
   info: Server URL: http://undefined
   + aws:ec2/instance:Instance: (create)
      [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www-2]
   info: Server URL: http://undefined
      - aws:ec2/instance:Instance: (delete)
         [id=i-0411117ebe29fa49e]
         [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-app]
      - aws:ec2/instance:Instance: (delete)
         [id=i-0057df76ac1324fce]
         [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www]
   info: 5 changes previewed:
      + 3 resources to create
      - 2 resources to delete
      2 resources unchanged
   ```    

1. Run `pulumi update`.

   ```bash
   $ pulumi update --summary
   Performing changes:
   * pulumi:pulumi:Stack: (same)
      [urn=urn:pulumi:testing::webserver::pulumi:pulumi:Stack::webserver-testing]
   + aws:ec2/instance:Instance: (create)
      [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www-0]
   info: Server URL: http://ec2-34-208-200-113.us-west-2.compute.amazonaws.com
   + aws:ec2/instance:Instance: (create)
      [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www-1]
   info: Server URL: http://ec2-35-161-236-236.us-west-2.compute.amazonaws.com
   + aws:ec2/instance:Instance: (create)
      [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www-2]
   info: Server URL: http://ec2-34-215-170-73.us-west-2.compute.amazonaws.com
      - aws:ec2/instance:Instance: (delete)
         [id=i-0411117ebe29fa49e]
         [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-app]
      - aws:ec2/instance:Instance: (delete)
         [id=i-0057df76ac1324fce]
         [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-www]
   info: 5 changes performed:
      + 3 resources created
      - 2 resources deleted
      2 resources unchanged
   Update duration: 2m14.896208211s
   ```

1. Give the instances a few minutes to initialize, then `curl` each URL that was printed out. You will see that each instance is in a different availability zone. 

   Tip: to see just the instance URLs, run `pulumi update` again. Since there will be no changes, it will print just the `console.log` statements.

   ```bash
   $ curl http://your-url.us-west-2.compute.amazonaws.com
   Hello, World!
   Instance metadata:
   us-west-2a
   ```

This example shows the power of using real programming language constructs to define infrastructure. Markup languages simply aren't expressive enough to describe these common patterns. 

## Clean up

1. To clean up after ourselves, just run `pulumi destroy` and answer the confirmation question at the prompt:

   ```bash
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

> _Note_: Pulumi currently runs all infrastructure updates sequentially to provide the greatest assurance of repeatable
> results.  Parallel execution of infrastructure updates is available with an experimental `--parallel N` flag, and this will likely become the default in the future.

## Summary

You've seen how easy it is to use Pulumi to provision infrastructure in a repeatable fashion. Pulumi programs specify infrastructure requirements and you can use a general-purpose programming language to define your infrastructure. You can easily use objects, functions, and control flow. And, if you use a language like TypeScript, you'll automatically get compile errors if you use an API incorrectly.

The `pulumi preview` command shows what changes will be made to your infrastructure before you actually update any resources, giving you confidence that the deployment will do what you expect.

In the next section, we'll take a look at building a higher level Pulumi Program using the
`@pulumi/cloud` framework.

## Next Steps

To learn how to use Pulumi's high-level programming model, see [Programming the cloud](./cloud.html)

