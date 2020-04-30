---
title: "Running Containers on ECS Fargate"
meta_desc: This tutorial will teach you to publish a Docker container to Elastic Container Registry (ECR)
           and deploy it to a load-balanced ECS Fargate Service.
aliases: ["/docs/reference/tutorials/aws/tutorial-service/"]
---

<!--To-Do: Update github-buttons shortcode to check for existence of examples-->
<p class="mb-4 flex">
    <a class="flex flex-wrap items-center rounded text-xs text-white bg-blue-600 border-2 border-blue-600 px-2 mr-2 whitespace-no-wrap hover:text-white h-8" href="https://github.com/pulumi/examples/tree/master/aws-ts-containers" target="_blank">
      <span><i class="fab fa-github pr-2"></i> View TS Code</span>
    </a>
</p>

In this tutorial, we'll build and publish a Docker container to a private Elastic Container Registry (ECR), and spin up a load-balanced Amazon Elastic Container Service (Amazon ECS) Fargate service, all in a handful of lines of code, using [Pulumi Crosswalk for AWS]({{< prelref "/docs/guides/crosswalk/aws" >}}).

## Prerequisites

1. [Install Docker Engine - Community](https://docs.docker.com/install/)
1. [Install Pulumi]({{< prelref "/docs/get-started/install" >}})
1. [Configure Pulumi to use your AWS account]({{< prelref "/docs/intro/cloud-providers/aws/setup" >}})

## Deploy the App

### Step 1: Create a new project from a template

Create a project directory, `hello-fargate`, and change into it. Run [`pulumi new aws-typescript --name myproject`]({{< prelref "/docs/reference/cli/pulumi_new" >}}) to create a new project using the AWS template for TypeScript. Replace `myproject` with your desired project name.

Run `pulumi new` to create a new project:

```bash
$ mkdir hello-fargate && cd hello-fargate
$ pulumi new aws-typescript --name myproject
```

### Step 2: Build the Dockerized app

Create a subdirectory, `app`, containing our sample Dockerized application. From the `app` subdirectory, add the following files:

#### **Dockerfile**

```docker
FROM nginx
COPY index.html /usr/share/nginx/html
```

#### **index.html**

```html
<html>
  <head>
    <title>Hello Fargate</title>
  </head>
  <body>
      <p>Hello AWS Fargate!</p>
      <p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
  </body>
</html>
```

### Step 3: Create the load balancer

Replace the contents of `index.ts` with the following:

```typescript
import * as awsx from "@pulumi/awsx";

// Create a load balancer to listen for requests and route them to the container.
let lb = new awsx.lb.NetworkListener("nginx", { port: 80 });
```

### Step 4: Define the service and publish the Docker image

Add the following lines to `index.ts`:

```typescript
// Define the service, building and publishing our "./app/Dockerfile", and using the load balancer.
let service = new awsx.ecs.FargateService("nginx", {
    desiredCount: 2,
    taskDefinitionArgs: {
        containers: {
            nginx: {
                image: awsx.ecs.Image.fromPath("nginx", "./app"),
                memory: 512,
                portMappings: [ lb ],
            },
        },
    },
});

// Export the URL so we can easily access it.
export const url = lb.endpoint.hostname;
```

You just created an automatic cluster in the default AWS VPC to run a Fargate service.

### Step 5: Verify your app structure

Ensure you have the following directory structure:

```
Pulumi.yaml
index.ts
app/
  Dockerfile
  index.html
```

### Step 6: Set your AWS region

Configure the AWS region you would like to use:

```bash
$ pulumi config set aws:region us-east-1
```

### Step 7: Preview and deploy your resources

To preview your Pulumi program, run [`pulumi up`]({{< prelref "/docs/reference/cli/pulumi_up" >}}). The command shows a preview of the resources that will be created and prompts you to proceed with the deployment.  Note that the stack itself is counted as a resource, though it does not correspond to a physical cloud resource.

```bash
$ pulumi up
Previewing changes:
...
Diagnostics:
    ...
    global: global
    info: Building container image 'pulum-164fa748-container': context=./app
...
Do you want to perform this update? yes
Updating stack 'container-quickstart-dev'
...

---outputs:---
url: "http://42dc3ff4-ac65d11-86a100b6e1d7f210.elb.us-west-2.amazonaws.com"

Resources:
    + 32 created

Duration: 4m6s
```

The deployment takes a few minutes. With your `pulumi up` invocation, Pulumi automatically does the following for you:

- Build and provision a container registry using ECR
- Build the Docker image
- Push the resulting image to the repository

### Step 8: Test the resulting load balancer URL

Now that you've deployed your app, confirm that the service is working via `curl`.

```bash
$ curl http://$(pulumi stack output url)
<html>
    <head>
        <title>Hello Fargate</title>
    </head>
    <body>
        <p>Hello, containers!</p>
        <p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
    </body>
</html>
```

### Step 9: View container logs (Optional)

To view the runtime logs from the container, use the [`pulumi logs`]({{< prelref "/docs/reference/cli/pulumi_logs" >}}) command. To get a log stream, use `pulumi logs --follow`.

```bash
$ pulumi logs --follow
Collecting logs for stack container-quickstart-dev since 2019-09-11T13:38:04.000-07:00.

2019-09-11T14:32:35.713-07:00[nginx-d73e16c] 172.31.61.144 - - [11/Sep/2019:21:32:35 +0000] "GET / HTTP/1.1" 200 193 "-" "curl/7.64.0" "-"
 2019-09-11T14:50:27.388-07:00[nginx-d73e16c] 95.140.20.94 - - [11/Sep/2019:21:50:27 +0000] "\xA0<\xA6\x1D\xED\xB2\xCC\xC79dH\xDCo\xED\xD6k\x02\xB6b\x05{)r\xFF5g\xC8/\xC4\xE7x~\xAB\xB8\xC8\x95\xF9\x9D?" 400 157 "-" "-" "-"
```

## Clean Up

{{< cleanup >}}

## Summary

{{< summary >}}
<p>
    In this tutorial, we showed you how to write a Pulumi program in Typescript, and leverage
Pulumi Crosswalk for AWS (via the <a href="{{< prelref "/docs/reference/pkg/nodejs/pulumi/awsx"
>}}">@pulumi/awsx package</a>) in order to build and publish a Dockerized application to a private
Elastic Container Registry (ECR), spin up an ECS Fargate cluster, and run a scalable, load balanced
service.
</p>
{{< /summary >}}

## Next Steps

For more information about containerized applications on AWS, please read these User Guides:

- [Pulumi Crosswalk for AWS Elastic Container Service (ECS)]({{< prelref "/docs/guides/crosswalk/aws/ecs" >}})
- [Pulumi Crosswalk for AWS Elastic Kubernetes Service (EKS)]({{< prelref "/docs/guides/crosswalk/aws/eks" >}})

For an end-to-end application also includes serverless functions, see the
[Serverless plus Containers Thumbnailer tutorial]({{< prelref "video-thumbnailer" >}}).

For an example application that connects two containers, see the
[Voting App](https://github.com/pulumi/examples/tree/master/aws-ts-voting-app) sample.

The [code for this tutorial](https://github.com/pulumi/examples/tree/master/aws-ts-containers) is available on GitHub.
