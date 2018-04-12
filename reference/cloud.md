---
title: Cloud Framework
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

## Prerequisites

Since this example builds a custom container, you should first have [Docker](https://docs.docker.com/engine/installation/) installed. 

## Set up the project

1.  In the [Pulumi examples zipfile], open the `voting-app` directory in your favorite editor. You'll see a Python Flask app in the `frontend` folder and a Pulumi program in `index.ts`. You may ignore the details of the Python app. 

1.  Open the file `index.ts`, which has the contents below.

    ```typescript
    import * as pulumi from "@pulumi/pulumi";
    import * as cloud from "@pulumi/cloud";

    // Get the password to use for Redis from config.
    let config = new pulumi.Config("voting-app");
    let redisPassword = config.require("redisPassword"); 
    let redisPort = 6379;

    // The data layer for the application
    // Use the 'image' property to point to a pre-built Docker image.
    let redisCache = new cloud.Service("voting-app-cache", {
        containers: {
            redis: {
                image: "redis:alpine",
                memory: 128,
                ports: [{ port: redisPort }],
                command: ["redis-server", "--requirepass", redisPassword],
            },
        },
    });

    let redisEndpoint = redisCache.endpoints.apply(endpoints => endpoints.redis[redisPort]);

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
                    "REDIS":      redisEndpoint.apply(e => e.hostname),
                    "REDIS_PORT": redisEndpoint.apply(e => e.port.toString()),
                    "REDIS_PWD":  redisPassword
                }
            },
        },
    });

    // Export a variable that will be displayed during 'pulumi update'
    export let frontendURL = frontend.endpoints.apply(e => `http://${e.hostname}:${e.port}`);
    ```

### Understanding the code

Even though this Pulumi program is just over 40 lines long, it does quite a bit:

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

### Output properties

The code exports the output `frontendURL`, via the declaration `export let frontEndUrl`. You can view the last deployed value for the output property using `pulumi stack output varName` and use it as part of a shell script.

## Build, preview, and update

Now, let's deploy this elegant program to AWS.

### Configure the deployment  

1.  Run `pulumi init`. (Note: this command will not be required in a future SDK release.)

1.  Login via `pulumi login`:

    ```bash
    $ pulumi login
    Enter your Pulumi access token (located at https://pulumi.com/account): 7hisis4r34llys3cr374cc3ss70k3ns0d0n7l34ki7=
    ```

1.  Create a new stack:

    ```
    $ pulumi stack init
    Enter a stack name: testing
    ```

1.  Set AWS as the provider:

    ```
    $ pulumi config set cloud:provider aws
    ```

1.  Configure Pulumi to use AWS Fargate, which is currently only available in `us-east-1`:

    ```
    $ pulumi config set aws:region us-east-1
    $ pulumi config set cloud-aws:useFargate true
    ```

1.  Set a value for the Redis password. The value can be an encrypted secret, specified with the `--secret` flag. If this flag is not provided, the value will be saved as plaintext in `Pulumi.testing.yaml` (since `testing` is the current stack name).

    ```
    $ pulumi config set --secret redisPassword S3cr37Password
    Enter your passphrase to protect config/secrets: 
    Re-enter your passphrase to confirm:     
    ```

### Compile the TypeScript program

1.  Restore NPM modules via `npm install`.

1.  Compile the program via `tsc` or `npm run build`.

### Preview and deploy

1.  Ensure the Docker daemon is running on your machine, then preview changes via `pulumi preview`. This step will create the Docker container but will not provision resources. If you encrypted the value for the `redisPassword` key, you'll be prompted for your password before each `preview` and `update` operation.

    ```
    $ pulumi preview --summary
    [...details omitted...]
    info: 34 changes previewed:
        + 34 resources to create
    ```

1.  Deploy the changes with `pulumi update`. Since this actually deploys a number of resources, it will take about 20-30 minutes to complete. (An upcoming improvement in `@pulumi/cloud` will substantially reduce the deployment time.) Note the stack output property `frontendUrl`, which shows the URL and port of the deployed app:

    ```bash
    $ pulumi update
    [...details omitted...]
    ---outputs:---
    frontendURL: "http://pulumi-vo-ne2-d7f97ef-7c5e2c22a22ec44a.elb.us-west-2.amazonaws.com:34567"
    Permalink: https://pulumi.com/pulumi/examples/voting-app/testing/updates/1
    ```

1.  In a browser, navigate to the URL for `frontendURL`. You should see the voting app webpage.

    ![Voting app screenshot](./voting-app-webpage.png)

### Clean up resources

Clean up your resources with `pulumi destroy`. This will take a few minutes, as deletes for some AWS resources can take some time.

## Summary

That's a quick tour of the `@pulumi/cloud` framework.  There is a lot you can do with this powerful cloud programming 
framework, and we are excited to see what the community builds on top of it.  Many more examples will be coming
soon. In the meantime, please check out the [API documentation](/packages/pulumi-cloud/) for more details.
