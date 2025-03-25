---
title: "Easily Deploy Applications With AWS App Runner"
date: 2021-05-18
meta_desc: "AWS App Runner configures networking, scaling, and security, letting deploy
  applications via source code or container."
meta_image: aws-app-runner.png
authors:
  - lee-zen
tags:
  - AWS
  - App Runner

search:
  keywords:
    - runner
    - aws
    - app
    - applications
    - deploy
    - easily
    - configures
---

There are loads of benefits to packaging up an application as a container. You can ensure that your application has all the required dependencies and runs in the isolated, predictable environment you expect. When it comes to running that containerized application, there are many options, including Kubernetes, Amazon Elastic Container Service (ECS), and Docker. Often, running a container application at scale requires setting up a container orchestrator and providing network infrastructure to the containers. Configuring this can be complex, especially if you’re not familiar with virtual networking concepts such as virtual private clouds, load balancers, and the like.

<!--more-->

AWS recently introduced App Runner, which allows you to easily deploy an application via either source code that lives in GitHub or container image repository. It handles all the configurations of networking, scaling, and security. In this blog post, we’ll show you how easy it is to use Pulumi to set up the necessary infrastructure to use App Runner.

In our case, we’ll build a container-based application. To create an App Runner service, we will be using Amazon's Elastic Container Registry (ECR) to create a repository to host our container images. In addition, we’ll need to push our image to the repository and ensure that App Runner has permissions to pull images from our repository.

We’ll use Go for our examples today. First, let’s setup the ECR repository:

```go
repo, err := ecr.NewRepository(ctx, "sampleapp", &ecr.RepositoryArgs{})
```

Note that we’re using Pulumi’s auto-naming support to generate the repository name.

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
