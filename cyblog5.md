Building and Publishing Docker Images to a Private Amazon ECR Repository

Amazon Elastic Container Registry ([ECR](https://aws.amazon.com/ecr/)) is a fully-managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images. Amazon ECR is integrated with Amazon Elastic Container Service ([ECS](https://aws.amazon.com/ecs/)), simplifying your development to production workflow. Amazon ECR eliminates the need to operate your own container repositories or worry about scaling the underlying infrastructure. Amazon ECR hosts your images in a highly available and scalable architecture, allowing you to reliably deploy containers for your applications.

Pulumi makes it simple to build and publish your docker images to your own managed ECR repository.  Policies can easily be provided to the repository specifying how and when stale images should be dropped.  Built images can easily be referenced from your ECS services (both based on [EC2](https://aws.amazon.com/ec2/) or [Fargate](https://aws.amazon.com/fargate/)), allowing you to easily version both your images and your infrastructure with one simple, auditable, system.

Let's take a look at this in action.  First, let's just start with a simple Pulumi program that creates a load balanced Fargate Service that accessible to the internet, but exposes a *public* Docker image:

```ts
// A simple NGINX service, scaled out over two containers.
const nginx = new awsx.ecs.FargateService("nginx", {
    cluster,
    desiredCount: 2,
    taskDefinitionArgs: {
        containers: {
            nginx: {
                image: "nginx",
                memory: 128,
                portMappings: [new awsx.elasticloadbalancingv2.ApplicationListener("nginx", { port: 80 })],
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

With a simple program, pulumi helped build 36 actual resources, ensuring the right connections between everything all with the appropriate best practices for a cloud deployment.

Here, through the use of `image: "nginx"` we are letting ECS know that we want to use [this](https://hub.docker.com/_/nginx/) publicly available Docker image.  ECS supports pulling these images for you by default and making them available to your services.   If you're using a public image, this works great and no further work is necessary on your part.

However, there are often times when you or your organization may want to use public images.  You may want to build your own images that you do not want to share with anyone for any number of reasons.  In cases like this, ECR is a valuable service that allows you to host those images up in AWS in a distributed fashion, ensuring easy and fast access by ECS when launching your services.

Let's see what that looks like with Pulumi.  First, we'll create a simple Dockerfile that starts with the basic [Alpine](https://hub.docker.com/_/alpine) image and slightly modifies it to contain our own custom `index.html` file:

The `Dockerfile`:
```Docker
FROM alpine AS build
COPY content/index.html /

FROM nginx
COPY --from=build /index.html /usr/share/nginx/html
```

The `index.html` file:
```html
<h1> Hi from Pulumi! </h1>
```

Now, let's see how we'd update our Pulumi app to build this custom Docker image, push it to ECR and reference it from our Service:

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

![ECR3](https://user-images.githubusercontent.com/4564579/59709843-8c958880-91bc-11e9-955c-56e772893577.gif)

As you can see Pulumi is actually launching the real `docker` executable locally to use the `Dockerfile` to build the image.  As `docker` runs, the output is captured and automatically shown in the real-time Pulumi update display.  When the image is finished building, it is pushed by `docker` itself to the ECR repo.  Pulumi safely passes the repo information to the `docker` executable so it can login and push the image up.  Finally, once available in ECR, the task-definition and service are appropriately updated to now reference this new image.  ECS will then ensure that the old services are spun down and the new services are spun up.  In the end we see:

![image](https://user-images.githubusercontent.com/4564579/59711938-fdd73a80-91c0-11e9-8fc2-1dee49a7173e.png)

In less than 30 seconds, Pulumi and Docker built the private image, made it available on ECR, and properly moved the Service over to using it.  This was all done with a single command, with Pulumi smartly figuring out at the end of the day exactly what changes needed to be made.  From the above we can see just the creation of the Repository components, and the updates of the Service to now use it.  A nice minimal change that exactly matches our intuition around what would happen.  If necessary, the `.buildAndPushImage` operation can also take many more options to control what's happening with `docker`.  Options around tagging and caching can be configured, and the `docker` command line can also just be augmented if necessary to handle advanced scenarios.

Now, in practice an organization may be producing and uploading many images to their private ECR repositories.  This can add up in costs as time goes on, especially when old images are stored that will never be used again.  To aid with this, Pulumi makes it easy to set up [ECR Lifecycle Policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) to control the lifetime of your images and to easily purge unneeded images based on flexible criterias to meet your needs.  As a simple example, here's a way to just remove any untagged images that are older than one week old:

```ts
// common code from before trimmed out
const repository = new awsx.ecr.Repository("repo", {
    lifeCyclePolicyArgs: {
        rules: [{
            selection: "untagged",
            maximumAgeLimit: 7,
        }],
    },
});
```

Now, you can keep your last two weeks of images around if you want them with all tagged images (like `'latest'`) being preserved.  You can continue pushing rapidly to your repo without having to worry about manually going and cleaning up the stale garbage in the future.

We've shown you now how Pulumi can tie in well to a tight developer inner loop using `docker`, building images, pushing to private ECR repos, and keeping all your services and tasks updated properly.  This can be done with flexible policies to ensure that your repos contain the images you care about and don't keep holding onto images you no longer need.  This is all possible from a single Pulumi app with simple commands to keep everything in sync.  This takes advantage heavily of our new `Crosswalk components for Aws`.  We think there's no easier way to manage using `docker` in a tight inner development loop, and we hope you think so to!

We hope these new Crosswalk for AWS APIs will be just as useful for you! For more information on `Pulumi Crosswalk for AWS` checkout other related content:

1. [Product Announcement](https://blog.pulumi.com/introducing-pulumi-crosswalk-for-aws-the-easiest-way-to-aws)
2. [Mapbox IOT-as-Code with Pulumi Crosswalk for AWS](https://blog.pulumi.com/mapbox-iot-as-code-with-pulumi-crosswalk-for-aws)
3. [Product Documentation](https://pulumi.io/reference/crosswalk/aws/)


