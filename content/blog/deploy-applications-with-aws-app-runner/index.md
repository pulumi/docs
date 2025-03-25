---
title: "How to Deploy Apps with AWS App Runner and Pulumi"
date: 2021-05-18
updated: 2025-03-24
meta_desc: "Learn how to deploy containerized apps using AWS App Runner and Pulumi. Automate scaling, networking, and security in minutes with minimal configuration."
meta_image: aws-app-runner.png
authors:
    - lee-zen
tags:
    - AWS
    - App Runner

---

There are loads of benefits to packaging up an application as a container. You can ensure that your application has all the required dependencies and runs in the isolated, predictable environment you expect. When it comes to running that containerized application, there are many options, including Kubernetes, Amazon Elastic Container Service (ECS), and Docker. Often, running a container application at scale requires setting up a container orchestrator and providing network infrastructure to the containers. Configuring this can be complex, especially if you’re not familiar with virtual networking concepts such as virtual private clouds, load balancers, and the like.

<!--more-->

[AWS recently introduced App Runner](https://aws.amazon.com/about-aws/whats-new/2021/05/aws-announces-aws-app-runner/), which allows you to easily deploy an application via either source code that lives in GitHub or container image repository. It handles all the configurations of networking, scaling, and security. In this blog post, we’ll show you how easy it is to use Pulumi to set up the necessary infrastructure to use App Runner.

In our case, we’ll build a container-based application. To create an App Runner service, we will be using Amazon's Elastic Container Registry (ECR) to create a repository to host our container images. In addition, we’ll need to push our image to the repository and ensure that App Runner has permissions to pull images from our repository.

We’ll use Go for our examples today. First, let’s setup the ECR repository:

```go
repo, err := ecr.NewRepository(ctx, "sampleapp", &ecr.RepositoryArgs{})
```

Note that we’re using Pulumi’s [auto-naming support](/docs/iac/concepts/resources/names/) to generate the repository name.

Next, let’s make sure that the App Runner service can pull images from the repository. To do so, we’ll create a role:

```go
role, err := iam.NewRole(ctx, "ecrAccessRole", &iam.RoleArgs{
    AssumeRolePolicy: pulumi.String(string(assumeRolePolicy)),
})
```

The `assumeRolePolicy` object is fairly straightforward, it’s just the JSON representation:

```go
assumeRolePolicy, _ := json.Marshal(map[string]interface{}{
    "Version": "2012-10-17",
    "Statement": []map[string]interface{}{
        {
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Sid":    "",
            "Principal": map[string]interface{}{
                "Service": []string{
                    "build.apprunner.amazonaws.com",
                },
            },
        },
    },
})
```

Finally, we assign the image pull policy to this role:

```go
pullImagePolicy, _ := json.Marshal(map[string]interface{}{
    "Version": "2012-10-17",
    "Statement": []map[string]interface{}{
        {
            "Effect": "Allow",
            "Action": []string{
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:DescribeImages",
            },
            "Resource": "*",
        },
    },
})

_, err = iam.NewRolePolicy(ctx, "ecrAccessRolePolicy", &iam.RolePolicyArgs{
    Role:   role,
    Policy: pulumi.String(string(pullImagePolicy)),
})
```

With all of that setup, we can now build and push our container. For our example, we'll create an `app` directory
within our project containing a simple `Dockerfile` and `index.html` file:

```docker
FROM nginx:latest
COPY ./index.html /usr/share/nginx/html/index.html
```

Where `index.html` is simply:

```html
<html>
   <head>
       <meta charset="UTF-8">
       <title>Hello, Pulumi</title>
   </head>
   <body>
       <p>Hello, world!</p>
       <p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
   </body>
</html>
```

To push the image, we simply use Pulumi’s Image component resource to build and push. We’ll need our ECR credentials, which we can obtain via a simple function call and pass that information as an argument to our `Image` resource:

```go
ecrCredentials, err := ecr.GetAuthorizationToken(ctx, &ecr.GetAuthorizationTokenArgs{
    RegistryId: nil,
}, nil)
if err != nil {
    return err
}

// Build and push our image into the ECR repo.
dockerImage, err := docker.NewImage(ctx, "sampleapp", &docker.ImageArgs{
    ImageName: repo.RepositoryUrl,
    Build: docker.DockerBuildArgs{
        Context: pulumi.String("./app"),
    },
    Registry: &docker.ImageRegistryArgs{
        Server:   repo.RepositoryUrl,
        Username: pulumi.String(ecrCredentials.UserName),
        Password: pulumi.String(ecrCredentials.Password),
    },
})
if err != nil {
    return err
}
```

At this point, we have everything we need to deploy our App Runner Service. Let's deploy it!

```go
appRunnerService, err := apprunner.NewService(ctx, "service", &apprunner.ServiceArgs{
    ServiceName: pulumi.String("myservice"),
    SourceConfiguration: &apprunner.ServiceSourceConfigurationArgs{
        AuthenticationConfiguration: &apprunner.ServiceSourceConfigurationAuthenticationConfigurationArgs{
            AccessRoleArn: role.Arn,
        },
        ImageRepository: &apprunner.ServiceSourceConfigurationImageRepositoryArgs{
            ImageIdentifier:     dockerImage.ImageName,
            ImageRepositoryType: pulumi.String("ECR"),
            ImageConfiguration: &apprunner.ServiceSourceConfigurationImageRepositoryImageConfigurationArgs{
                Port: pulumi.String("80"),
            },
        },
    },
})
if err != nil {
    return err
}
```

And just like that, our service is up and running, and it only took a few dozen lines of code! With this kind of setup, we don’t have to worry about load balancers or scaling or anything like that -- instead, we focused on building our application and stood up the bare minimum to have a repository image. We can export the URL of our service to visit it:

```go
ctx.Export("serviceEndpoint", appRunnerService.ServiceUrl)
```

We’re excited at how easy it is to use Pulumi to deploy applications via AWS App Runner, and we can’t wait to see what exciting things you build with it! See AWS App Runner in action in this episode of Modern Infrastructure Wednesday.

{{< youtube "XdMynboheiA?rel=0" >}}
<div>
    <div class="accordion-item text-2xl py-3 border-b-2 border-t-2">
        <input type="checkbox" class="absolute hidden" id="Transcript" />
        <label for="Transcript" class="accordion-label">
            <h5 class="mt-2 w-2/3">Video Transcript</h5>
            <div class="flex flex-grow justify-end items-center">
                <span class="closed-accordion">+</span>
                <span class="open-accordion hidden">-</span>
            </div>
        </label>
        <div class="accordion-item-body-no-animation text-base">
            <p>
                Hello, and welcome to another episode of Modern Infrastructure Wednesday. I’m your host, Lee Zen, and today we’re going to be covering how easy it is to use Pulumi to deploy an application using AWS App Runner. App Runner is a new service from Amazon that lets you deploy a container image or a source code repository as an application, without having to do too much around configuring anything. You don’t have to configure load balancers—you don’t have to configure any of that stuff you typically have to configure.
            </p>
            <p>
And so, here you can see I’m running the main.go file, and it’s going to create all the necessary resources along with, finally, the App Runner service. We’re going to go into all the source code to explain how all this works, but right now you can see what’s happening is—we’re actually doing the Docker build that’s going to publish. We’re doing the Docker build, and then after the Docker build completes, it’s pushing the image into our ECR repository. And then finally, you can see here the update succeeds, and then we actually get the service URL. So now let’s go take a look at our service. And while the service is updating—you can see it takes a little bit of time, not too much, but just a little bit of time to get going—we’re going to go in to see how our code actually works.
            </p>
            <p>
All right, so what’s actually happening here? Let’s look at our deployment.go file, which main.go actually calls. So we actually built an Automation API-based program, and you can see, you know, in the outputs, we create this image, we create these various things. And so let’s look at the code. The first thing we do is we create an ECR repository, and here we use auto-naming, so it just creates the name. Then next, we create a role so that App Runner can actually go ahead and pull the image from our repository. And so we create the role, we give it the correct policy, and then after that, we basically publish our image. You can see here we have the image resource, and there we actually just feed it the repository credentials.
            </p>
            <p>
So let’s take a quick look at the Dockerfile of the thing we’re building. It’s just copying that index.html file over—it’s a very simple file. So that’s really all there is to the infrastructure. It’s super simple. If we look at the Automation API side of things, all we’re doing is doing the usual Automation API stuff. We’re setting up a stack, we’re deploying our program. Actually, we point out the part where we’re deploying the program right up here, and as soon as we are complete, as soon as we finish deploying the program, we’re going to use the outputs of that program—namely, the image URL and the access role—and we’ll feed that to App Runner. That’ll basically invoke the Create Service API call here, and that’s actually what’s going to do the work.
            </p>
            <p>
So let’s go back to the console, and you can see here we have the app running—and voila! Exactly what we expect to see. So hopefully you enjoyed this demo. And really, yeah, like I said, just so easy to get everything running with App Runner in just a few simple lines of code and Pulumi. Thanks for watching, and have a great day.
            </p>
        </div>
    </div>
</div>
