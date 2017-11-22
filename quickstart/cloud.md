---
layout: default 
nav_section: "quickstart"
---

<p><a href="/quickstart">Quickstart</a> &gt; <b>Programming the Cloud</b></p>

# Programming the Cloud

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

### Prerequisites

Since this example builds a custom container, you should first have [Docker](https://docs.docker.com/engine/installation/) installed. 

### Set up the project

1. Clone or download the `examples` repo at the [tutorial-initial branch](https://github.com/pulumi/examples/tree/tutorial-initial). This has the project setup and Flask app, but not the Pulumi program itself.

1. In the `voting-app` folder, add the following file as `index.ts`:

   ```typescript
    import * as cloud from "@pulumi/cloud";

    // To simplify this example, we have defined the password directly in code
    // In a real app, would add the secret via `pulumi config secret <key> <value>` and
    // access via pulumi.Config APIs
    let redisPassword = "SECRETPASSWORD"; 

    let redisPort = 6379;

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

    let frontend = new cloud.Service("voting-app-frontend", {
        containers: {
            votingAppFrontend: {
                build: "./frontend",
                memory: 128,
                ports: [{ port: 80 }],            
                environment: { 
                    // pass in the created container info in environment variables
                    // the awkward nested promises will be improved soon; see pulumi/pulumi #331
                    "REDIS": redisCache.getEndpoint("redis", redisPort).then(e => e.hostname),
                    "REDIS_PORT": redisCache.getEndpoint("redis", redisPort).then(e => e.port).then(port => port.toString()),
                    "REDIS_PWD": redisPassword
                }
            },
        },
    });

    frontend.getEndpoint().then(e => console.log(`http://${e.hostname}:${e.port}`));
   ```

#### Understanding the code

Even though this Pulumi program is just over 36 lines long, it does quite a bit:

- It creates two containers, a Redis cache with container port 6379 and a custom Docker container for the app frontend.
- Stores the port in the variable `redisPort`, since the frontend app needs to connect to the Redis container.
- Creates a container `redisCache`. This is a Redis cache that uses the `redis` image with tag `alpine` from DockerHub. Since it's a built image, you just have to specify the port and startup command.
- Creates a second container `frontend`, which is more interesting. If you look at `frontend/app/main.py` in the `voting-app` folder, you'll see that the app expects the Redis connection information to be provided in environment variables:

   ```python
   redis_server =   os.environ['REDIS']
   redis_port =     os.environ['REDIS_PORT']
   redis_password = os.environ['REDIS_PWD']
   ```

   We can use Pulumi APIs to statically lookup the server name and port for the container `redisCache`. So, it is very easy to connect containers to each other.

### Build, preview, and update

Now, lets deploy this elegant program to AWS.

1. Run `yarn install` or `npm install` to install the dependencies to your `node_modules` directory.

1. Link with the Pulumi SDK packages so that your `require`s will find the right thing, using either `yarn` or `npm`:

    ```bash
    $ yarn link pulumi @pulumi/cloud
    ```

1. Compile the code via `yarn build`.

1. Create a new Pulumi repository and stack:

    ```bash
    $ pulumi init
    $ pulumi stack init testing
    ```

1. Set your AWS region via `pulumi config set aws:config:region us-west-2` (or whichever region you prefer).

1. The `cloud.Service` component can either create a new ECS cluster or deploy into an existing one. Let's use the "autocluster" functionality:

   ```bash
   $ pulumi config set cloud-aws:config:ecsAutoCluster true
   ```

1. Preview changes via `pulumi preview`. This step will create the Docker container but will not provision resources.

1. Deploy the changes with `pulumi update`. This is when the resources are provisioned and will take 20-30 minutes. In the future, Pulumi will parallelize resource creations so that the experience is smoother.
   
   The frontend URL can get lost amid the output (this will be improved, see [\#454](https://github.com/pulumi/pulumi/issues/454)). As a workaround, once the deployment is complete, run `pulumi update` again. 

1. In a browser, navigate to the URL. You should see the voting app webpage. 

   ![Voting app screenshot](./voting-app-webpage.png)

### Cleanup resources

Clean up your resources with `pulumi destroy`. This will take a few minutes, as deletes for some AWS resources can take some time.

## Summary

That's a quick tour of the `@pulumi/cloud` framework.  There is a lot you can do with this powerful cloud programming 
framework, and we are excited to see what the community builds on top of it.  Many more examples will be coming
soon; however, in the meantime, please check out the [API documentation](/packages/pulumi-cloud/) for more details.

## Next Up: [Further Reading](./reading.html)

