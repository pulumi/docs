Building and Publishing Docker Images to a Private Amazon ECR Repository

Amazon Elastic Container Registry ([ECR](https://aws.amazon.com/ecr/)) is a fully-managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images. Amazon ECR is integrated with Amazon Elastic Container Service ([ECS](https://aws.amazon.com/ecs/)), simplifying your development to production workflow. Amazon ECR eliminates the need to operate your own container repositories or worry about scaling the underlying infrastructure. Amazon ECR hosts your images in a highly available and scalable architecture, allowing you to reliably deploy containers for your applications.

Pulumi makes it simple to build and publish your docker images to your own managed ECR repository.  Policies can easily be provided to the repository specifying how and when stale images should be dropped.  Built images can easily be referenced from your ECS services (both based on [EC2](https://aws.amazon.com/ec2/) or [Fargate](https://aws.amazon.com/fargate/)), allowing you to easily version both your images and your infrastructure with one simple, auditable, system.

Let's take a look at this in action.  First, let's just start with a simple Pulumi program that creates a load balanced Fargate Service that accessible to the internet, but exposes a *public* Docker image:

```ts
// A simple NGINX service, scaled out over two containers.
const listener = new awsx.elasticloadbalancingv2.ApplicationLoadBalancer("nginx")
                         .createListener("nginx", { port: 80 });

const nginx = new awsx.ecs.FargateService("nginx", {
    cluster,
    desiredCount: 2,
    taskDefinitionArgs: {
        containers: {
            nginx: {
                image: "nginx",
                memory: 128,
                portMappings: [listener],
            },
        },
    },
});

export const nginxEndpoint = nginxListener.endpoint;
```

Running this give us:

```
Updating (teststack):
     Type                                                        Name                      Status
 +   pulumi:pulumi:Stack                                         teststack                 created
 +   ├─ awsx:x:elasticloadbalancingv2:ApplicationLoadBalancer    nginx                     created
 +   │  ├─ awsx:x:elasticloadbalancingv2:ApplicationTargetGroup  nginx                     created
 +   │  │  └─ aws:elasticloadbalancingv2:TargetGroup             nginx                     created
 +   │  ├─ awsx:x:elasticloadbalancingv2:ApplicationListener     nginx                     created
... more output trimmed ***

Outputs:
    nginxEndpoint: { hostname: "********", port: 80 }

Resources:
    + 36 created

Duration: 3m19s
```

With a simple program, pulumi helped build 36 actual resources, ensuring the right connections between everything and appropriate best practices for a cloud deployment.

Here, through the use of `image: "nginx"` we are letting ECS know that we want to use [this](https://hub.docker.com/_/nginx/) publicly available Docker image.  ECS supports pulling these images for you by default and making them available to your services.   If you're using a public image, this works great and no further work is necessary on your part.

However, there are often times when you or your organization may want to use public images.  You may want to build your own images that you do not want to share with anyone for any number of reasons.  In cases like this, ECR is a valuable service that allows you to host those images up in AWS in a distributed fashion, ensuring easy and fast access by ECS when launching your services.

Let's see what that looks like:

```ts
// common code from before trimmed out
const repository = new awsx.ecr.Repository("repo");

// Invoke 'docker' to actually build the DockerFile that is in the 'app' folder relative to
// this program.  Once built, push that image up to our personal ECR repo.
const image = repository.buildAndPushImage("./app")

const service = new awsx.ecs.FargateService("service", {
    // ... common code from before trimmed out
    taskDefinitionArgs: {
        containers: {
            service: {
                image: image,
```

So let's see what happens when we actually try to run this:

