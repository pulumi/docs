---
layout: default 
nav_section: "quickstart"
---

<p><a href="/quickstart">Quickstart</a> &gt; <b>Programming AWS</b></p>

# Programming AWS

The `@pulumi/aws` package allows you use Pulumi to create and manage AWS resources using JavaScript or TypeScript. You can use regular programming language constructs, such as objects, functions, and control flow. Resource definitions are declarative: they describe the desired end state of your infrastructure. Pulumi will automatically make resource changes based on the current state of what has already been provisioned.

Each AWS resource is exposed as a class under a submodule of `aws`. For example, here are some commonly used services:

* EC2 VM instances, `aws.ec2.Instance`
* S3 buckets, `aws.s3.Bucket`, and objects, `aws.s3.Object`
* DynamoDB tables, `aws.dynamodb.Table`
* Lambda functions, `aws.lambda.Function`

## Provision an EC2 instance with AMI lookup

For our first application, we'll create an AWS [EC2 Instance](/packages/pulumi-aws/classes/_ec2_instance_.instance.html)
and associated [Security Group](/packages/pulumi-aws/classes/_ec2_securitygroup_.securitygroup.html) using Pulumi. We'll do a lookup to get the appropriate AMI for the AWS region and machine type. This example uses TypeScript to get improved validation of the program, but you can also use JavaScript.

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
export let size: aws.ec2.InstanceType = "t2.micro"; 

// create a new security group for port 80
let group = new aws.ec2.SecurityGroup("web-secgrp", { 
    description: "Enable HTTP access",
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

// a function to find the Amazon Linux AMI for the current region
async function getLinuxAmi() {
    let result = await aws.getAmi({
        owners: ["amazon"],
        filter: [{ name: "name", values: ["amzn-ami-hvm-2017.09.0.20170930-x86_64-gp2"] }]
    });
    return result.imageId;
}

// Create a simple web server using the startup script for the instance
// Use the AWS metadata service to get the availability zone for the instance
let userData = 
    `#!/bin/bash
    echo "Hello, World!\nInstance metadata:" > index.html
    curl http://169.254.169.254/latest/meta-data/placement/availability-zone >> index.html
    nohup python -m SimpleHTTPServer 80 &`;

let server = new aws.ec2.Instance("web-server-www", {
    instanceType: size,
    securityGroups: [ group.name ],     // reference the group object above
    ami: getLinuxAmi(),                 // call custom function
    tags: { "Name": "web-server-www" },
    userData: userData                  // set up a simple web server    
});

server.publicDns.then(url => console.log(`Server URL: http://${url}`));
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

1. Create a new Pulumi stack called "testing":

    ```bash
    $ pulumi stack init testing
    ```

1. We can get a preview of what will happen during a deployment by running `pulumi preview`. 

   You'll see an error:  `Error: Missing required configuration variable 'aws:config:region'`.  As the error states, before we can preview or update our application, we need to configure the AWS region we will be targeting. For example, to choose `us-west-2`:

    ```bash
    $ pulumi config set aws:config:region us-west-2
    ```

1. We can now successfully run `pulumi preview` to see the complete set of resources that will be created:

    ```bash
    $ pulumi preview
    Previewing changes:
    info: Server URL: http://undefined
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

    Note that the server URL is `http://undefined`. This is expected, as Pulumi won't know the resource name until it has been provisioned at least once.
    
    As expected, we see that updating this program will create two resources.

1. Let's go ahead and deploy the update. This will take about 30 seconds as it waits for the actual EC2 instance to finish spinning up:

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
        <snip>
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
        <snip>
    info: Server URL: http://ec2-52-43-64-227.us-west-2.compute.amazonaws.com                
    info: 2 changes performed:
        + 2 resources created
    Update duration: 25.518253662s
    ```

    This time, there is a real URL for the server.

1. We now have a running EC2 instance.  We can run `aws ec2 describe-instances --filter Name=tag:name,Values=pulumi`, or open the AWS Console, to see that this new instance is now running.

1. View the provisioned resources via `pulumi stack`:

    ```bash
    Current stack is testing
        (use `pulumi stack select` to change stack; `pulumi stack ls` lists known ones)
    Last update at 2017-10-30 13:59:23.606056356 -0700 PDT
    Additional update info:
    <snip>

    2 resources currently in this stack:

    TYPE                                             NAME
    aws:ec2/securityGroup:SecurityGroup              web-secgrp
    aws:ec2/instance:Instance                        web-server-www
    ```    

1. Give the instance a few minutes to initialize, then verify that the server is running:

    ```bash
    $ curl http://your-url.us-west-2.compute.amazonaws.com
    Hello, World!
    Instance metadata:
    us-west-2a    
    ```

## Leverage a reusable component

Now, let's create a function that creates instances. We can then use it to create two instances: one for `www` and one for `api`.

1. Rename `index.ts` to `webserver.ts`.

1. Remove the last line of code:

    ```typescript
    // delete this:
    server.publicDns.then(url => console.log(`Server URL: http://${url}`));
    ```

1. Remove the definition of `server` and replace with the following:

    ```typescript
    export function createInstance(name: string, size: aws.ec2.InstanceType): aws.ec2.Instance {
        let result = new aws.ec2.Instance(name, {
            instanceType: size,                 // use function argument for size
            securityGroups: [ group.name ],     // reference the group object above
            ami: getLinuxAmi(),                 // call custom function
            tags: { "Name": name },
            userData: userData                  // set up a simple web server    
        });

        result.publicDns.then(url => console.log(`Server URL: http://${url}`));

        return result;
    }
    ```

1. Create a new file `index.ts` with the following contents. This will provision two EC2 instances with different sizes.

    ```typescript
    import * as aws from "@pulumi/aws";
    import * as webserver from "./webserver"; // use our custom component

    let webInstance = webserver.createInstance("web-server-www", "t2.micro");
    let appInstance = webserver.createInstance("web-server-app", "t2.nano");
    ```

1. Compile via `yarn build`.

1. We can run `pulumi preview` to see what changes this will make to our infrastructure. Note that only one new resource is created: since the security group and `web-server-www` instance are unchanged, they do not need to be updated or replaced.

    ```bash
    $ pulumi preview
    Previewing changes:
    info: www address: http://ec2-52-24-173-163.us-west-2.compute.amazonaws.com
    info: app address: http://undefined
    + aws:ec2/instance:Instance: (create)
        [urn=urn:pulumi:testing::webserver::aws:ec2/instance:Instance::web-server-app]
        ami            : "ami-29f80351"
        instanceType   : "t2.nano"
        securityGroups : [
            [0]: "web-secgrp-241e97032e20c4c1"
        ]
        sourceDestCheck: true
        tags           : {
            Name: "web-server-app"
        }
        userData       : "#!/bin/bash\n  echo \"Hello, World!\nInstance metadata:\" > index.html\n  curl http://169.254.169.254/latest/meta-data/placement/availability-zone >> index.html\n  nohup python -m SimpleHTTPServer 80 &"
    info: 1 change previewed:
        + 1 resource to create
        2 resources unchanged
    ```

1. Run `pulumi update` to make the resource changes:

    ```bash
    $ pulumi update
    Performing changes:
    info: www address: http://ec2-52-24-173-163.us-west-2.compute.amazonaws.com
    + aws:ec2/instance:Instance: (create)
        <snip>
    info: app address: http://ec2-35-165-221-166.us-west-2.compute.amazonaws.com
    info: 1 change performed:
        + 1 resource created
        2 resources unchanged
    Update duration: 28.341593905s
    ```

With a simple and natural extension the the original code, we've created a true cloud component. Anyone who uses the `webserver` package can automatically leverage the logic we've defined.

### Create an instance in each availability zone

For a production service, you would typically deploy a virtual machine in each availability zone for the AWS region. For this, we'll use the function `aws.getAvailabilityZones()`, which calls an AWS API to get all zones. We can then loop over all availability zones and create an instance in that zone.

Since the list of availability zones is dynamic data, it is very difficult to create this infrastructure specification in CloudFormation or similar tools. Since Pulumi allows you to define infrastructure requirements directly in code, this scenario is very easy to define in Pulumi.

Make the following changes to the code:

1. In `webserver.ts`, add a new string function argument for availability zone in `createInstance`, and pass the property `availabilityZone: zone` to the `aws.ec2.Instance` constructor. 

1. In `index.ts`, remove the definitions of `webInstance` and `appInstance`. Add the following code to create an EC2 instance in each availability zone in the region:

    ```typescript
    (async () => {
        let zones: string[] = (await aws.getAvailabilityZones()).names;
        for (let i = 0; i < zones.length; i++) {
            let server = webserver.createInstance("web-server-www-" + i, "t2.micro", zones[i]);
        }
    })();    
    ```

1. Run `yarn build`.

1. Run `pulumi preview`. Since we changed the instance name, two resources will be deleted and 3 resources will be created (since there are 3 availability zones in west-us-2).

    ```bash
    $ pulumi preview
    Previewing changes:
    info: Server URL: http://undefined
    info: Server URL: http://undefined
    info: Server URL: http://undefined
    + aws:ec2/instance:Instance: (create)
        <snip>
    + aws:ec2/instance:Instance: (create)
        <snip>
    + aws:ec2/instance:Instance: (create)
        <snip>
    - aws:ec2/instance:Instance: (delete)
        <snip>
        tags           : {
            Name: "web-server-app"
        }
        <snip>
    - aws:ec2/instance:Instance: (delete)
        <snip>
        tags           : {
            Name: "web-server-www"
        }
        <snip>
    info: 5 changes previewed:
        + 3 resources to create
        - 2 resources to delete
        1 resource unchanged
    ```    

1. Run `pulumi update`.

    ```bash
    $ pulumi update
    Performing changes:
    + aws:ec2/instance:Instance: (create)
        <snip>
    info: Server URL: http://ec2-34-208-122-55.us-west-2.compute.amazonaws.com
    + aws:ec2/instance:Instance: (create)
        <snip>
    info: Server URL: http://ec2-35-160-70-200.us-west-2.compute.amazonaws.com
    + aws:ec2/instance:Instance: (create)
        <snip>
    info: Server URL: http://ec2-34-215-88-48.us-west-2.compute.amazonaws.com
    - aws:ec2/instance:Instance: (delete)
        <snip>
    - aws:ec2/instance:Instance: (delete)
        <snip>
    info: 5 changes performed:
        + 3 resources created
        - 2 resources deleted
        1 resource unchanged
    Update duration: 2m59.419848955s
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
> results.  Parallel execution of infrastructure updates is available with an experimental `--parallel N` flag, and this will likely become the default in the future.

## Summary

You've seen how easy it is to use Pulumi to provision infrastructure in a repeatable fashion. Pulumi programs specify infrastructure requirements and you can use a general-purpose programming language to define your infrastructure. You can easily use objects, functions, and control flow. And, if you use a language like TypeScript, you'll automatically get compile errors if you use an API incorrectly.

The `pulumi preview` command shows what changes will be made to your infrastructure before you actually update any resources, giving you confidence that the deployment will do what you expect.

In the next section, we'll take a look at building a higher level Pulumi Program using the
`@pulumi/cloud` framework.

## Next Up: [Programming the Cloud](./cloud.html)

