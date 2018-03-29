---
title: Programming containers
---

<!-- LINKS: -->
[Pulumi examples zipfile]: /examples/pulumi-examples.zip
<!-- END LINKS -->

The `@pulumi/cloud` package lets you program infrastructure and application logic, side by side in harmony, using
simple, high-level cloud building blocks.  This package has three key defining attributes:

* __Easy Cloud Development__: The `@pulumi/cloud` library makes it simple to build robust and scalable cloud
  applications with just a few lines of code.
* __Cloud Agnostic__: The `@pulumi/cloud` library doesn't tie you to using any one particular cloud (AWS, Azure,
  Google Cloud, Kubernetes, and various on-premises clouds).  Applications built using the high-level `@pulumi/cloud`
  components like [Service](/packages/pulumi-cloud/interfaces/_service_.service.html), [Table](/packages/pulumi-cloud/interfaces/_table_.table.html), [Topic](
  /packages/pulumi-cloud/interfaces/_topic_.topic.html) and [HttpEndpoint](
  /packages/pulumi-cloud/interfaces/_httpendpoint_.httpendpoint.html) can be deployed to a variety of cloud platforms. (Currently, only support for AWS is implemented, but we plan to support all major providers.)
* __Serverless__: The `@pulumi/cloud` makes it easy to build applications with minimal fixed infrastructure,
  event-driven application logic, and using resources that are charged only based on actual consumption.

## A voting app with two containers

In this example, we'll show how a Pulumi application is deployed to AWS managed services, the same services you would use if you had authored the application manually. Pulumi does not reinvent the infrastructure, but makes it dramatically easier to author and evolve your application.

To solve the never-ending debate of "tabs vs. spaces" once and for all, we'll create a voting app. The app has two containers: Redis for the data store, and a Python Flask app for the frontend. In future tutorials, we'll add a database hosted in a container, then show how easy it is to move to a managed database and cache service (such as AWS RDS and ElastiCache).

Even in this simple example, it would be tedious and error prone to define this infrastructure with CloudFormation and similar tools. In AWS terms, the application needs an ECS cluster, a load balancer, an AWS Container Registry (ECR) instance, IAM roles, and so forth. If we were to do this manually, we'd provision around 38 resources. Pulumi handles this automatically!

{% include aws-resource-warning.md %}

> **Note**: since this example provisions an number of resources, it can take 20-30 minutes to deploy. For a quicker tutorial, see the `url-shortener` or `video-thumnailer` examples in the [Pulumi examples zipfile].

### Prerequisites

Since this example builds a custom container, you should first have [Docker](https://docs.docker.com/engine/installation/) installed. 

### Set up the project

1.  In the [Pulumi examples zipfile], open the `voting-app` directory in your favorite editor. You'll see a Python Flask app in the `frontend` folder and a Pulumi program in `index.ts`. You may ignore the details of the Python app. 

1.  Open the file `index.ts`, which has the contents below.

    ```typescript
    import * as pulumi from "@pulumi/pulumi";
    import * as cloud from "@pulumi/cloud";

    // Get the password to use for Redis from config.
    let config = new pulumi.Config("voting-app");
    let redisPassword = config.require("redisPassword"); 

    // The data layer for the application
    // Use the 'image' property to point to a pre-built Docker image.
    let redisCache = new cloud.Service("voting-app-cache", {
        containers: {
            redis: {
                image: "redis:alpine",
                memory: 128,
                ports: [{ port: 6379 }],
                command: ["redis-server", "--requirepass", redisPassword],
            },
        },
    });

    // A custom container for the frontend, which is a Python Flask app
    // Use the 'build' property to specify a folder that contains a Dockerfile.
    // Pulumi builds the container for you and pushes to an ECR registry
    let frontend = new cloud.Service("voting-app-frontend", {
        containers: {
            votingAppFrontend: {
                build: "./frontend",   // path to the folder containing the Dockerfile
                memory: 128,
                ports: [{ port: 80 }],            
                environment: { 
                    // pass the Redis container info in environment variables
                    // (the use of promises will be improved in the future)
                    "REDIS": redisCache.getEndpoint().then(e => e.hostname),
                    "REDIS_PORT": redisCache.getEndpoint().then(e => e.port.toString()),
                    "REDIS_PWD": redisPassword
                }
            },
        },
    });

    // Export a variable that will be displayed during 'pulumi update'
    export let frontendURL = frontend.getEndpoint().then(e => `http://${e.hostname}:${e.port}`);
    ```

#### Understanding the code

Even though this Pulumi program is just over 36 lines long, it does quite a bit:

**`redisCache` container**

- A Redis cache that simply uses the Docker Hub `redis` image with tag `alpine`. Since it's a built image, you just have to specify the port and startup command.

**`frontend` custom container**

- Uses the `build` property to point to a folder with a Dockerfile. Pulumi automatically invokes `docker build` for you and pushes the container to ECR.
- Uses Pulumi APIs, to set environment variables by statically looking up the server name and port for the container `redisCache`. This makes it easy to connect containers to each other. The Flask app uses these environment variables to connect to the Redis cache container. See the usage in `voting-app/frontend/app/main.py`:

  ```python
  redis_server =   os.environ['REDIS']
  redis_port =     os.environ['REDIS_PORT']
  redis_password = os.environ['REDIS_PWD']
  ```

#### Output properties

The code exports the output `frontendURL`, via the declaration `export let frontEndUrl`. You can view the last deployed value for the output property using `pulumi stack output varName` and use it as part of a shell script.

### Build, preview, and update

Now, lets deploy this elegant program to AWS.

1.  Run `npm install` .

1.  Compile the code via `tsc` or `npm run build`.

1.  Create a new Pulumi repository and stack:

    ```bash
    $ pulumi init
    $ pulumi stack init votingapp-testing
    ```

1.  Set your AWS region via `pulumi config set aws:config:region us-west-2` (or whichever region you prefer).

1.  Set AWS as the provider for the `@pulumi/cloud` library:

    ```bash
    $ pulumi config set cloud:provider aws
    ```

1.  Set a value for the password configuration value:

    ```
    $ pulumi config set --secret voting-app:redisPassword passw0rd
    ```

1. The `cloud.Service` component can either create a new ECS cluster or deploy into an existing one. Let's use the "autocluster" functionality:

   ```bash
   $ pulumi config set cloud-aws:config:ecsAutoCluster true
   ```

1. Ensure the Docker daemon is running on your machine, then preview changes via `pulumi preview`. This step will create the Docker container but will not provision resources.

   There are a number of resources that are automatically created for you, such as the ECS cluster, EFS instance, networking resources, log group, and so on. This is all implemented using the patterns specified in AWS reference architectures, freeing you to think in terms of high-level concepts.

   ```bash
   $ pulumi preview --summary
   Previewing changes:
   + pulumi:pulumi:Stack: (create)
      [urn=urn:pulumi:votingapp-testing::voting-app::pulumi:pulumi:Stack::voting-app-votingapp-testing]
      + aws:ec2/vpc:Vpc: (create)
         [urn=urn:pulumi:votingapp-testing::voting-app::aws:ec2/vpc:Vpc::pulumi-votingapp--global]
      .. 98 lines elided
   info: 50 changes previewed:
       + 50 resources to create
   ```

1. Deploy the changes with `pulumi update`. This is when the resources are provisioned and will take 20-30 minutes. (In the future, Pulumi will parallelize resource creations so that the experience is smoother.) You'll see that there is a stack output `frontendUrl`:

   ```bash
   ---outputs:---
   frontendURL: "http://pulumi-vo-ne2-d7f97ef-7c5e2c22a22ec44a.elb.us-west-2.amazonaws.com:34567"
   ```

1. In your terminal, view the stack output property:

   ```bash
   $ pulumi stack output frontendURL
   http://pulumi-vo-ne2-d7f97ef-7c5e2c22a22ec44a.elb.us-west-2.amazonaws.com:34567
   ```

1. In a browser, navigate to the URL from the previous step. You should see the voting app webpage.

   ![Voting app screenshot](./voting-app-webpage.png)

### Clean up resources

Clean up your resources with `pulumi destroy`. This will take a few minutes, as deletes for some AWS resources can take some time.

## Summary

That's a quick tour of the `@pulumi/cloud` framework.  There is a lot you can do with this powerful cloud programming 
framework, and we are excited to see what the community builds on top of it.  Many more examples will be coming
soon. In the meantime, please check out the [API documentation](/packages/pulumi-cloud/) for more details.

