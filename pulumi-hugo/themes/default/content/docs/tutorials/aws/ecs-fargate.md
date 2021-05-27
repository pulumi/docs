---
title: "Running Containers on ECS Fargate"
meta_desc: This tutorial will teach you to publish a Docker container to Elastic Container Registry (ECR)
           and deploy it to a load-balanced ECS Fargate Service.
aliases: ["/docs/reference/tutorials/aws/tutorial-service/"]
---

<!--To-Do: Update github-buttons shortcode to check for existence of examples-->
<p class="mb-4 flex">
    <a class="flex flex-wrap items-center rounded text-xs text-white bg-blue-600 border-2 border-blue-600 px-2 mr-2 whitespace-nowrap hover:text-white h-8" href="https://github.com/pulumi/examples/tree/master/aws-ts-containers" target="_blank">
      <span><i class="fab fa-github pr-2"></i> View TS Code</span>
    </a>
</p>

In this tutorial, we'll build and publish a Docker container to a private Elastic Container Registry (ECR), and spin up a load-balanced Amazon Elastic Container Service (Amazon ECS) Fargate service, all in a handful of lines of code, using [Pulumi Crosswalk for AWS]({{< relref "/docs/guides/crosswalk/aws" >}}).

## Prerequisites

1. [Install Docker Engine - Community](https://docs.docker.com/install/)
1. [Install Pulumi]({{< relref "/docs/get-started/install" >}})
1. [Configure Pulumi to use your AWS account]({{< relref "/docs/intro/cloud-providers/aws/setup" >}})

## Deploy the App

### Step 1: Create a new project from a template

Create a project directory, `hello-fargate`, and change into it. Run [`pulumi new aws-typescript --name myproject`]({{< relref "/docs/reference/cli/pulumi_new" >}}) to create a new project using the AWS template for TypeScript. Replace `myproject` with your desired project name.

Run `pulumi new` to create a new project:

```bash
$ mkdir hello-fargate && cd hello-fargate
$ pulumi new aws-typescript --name myproject
```

### Step 2: Build the Dockerized app

Create a subdirectory, `app`, which will contain your sample Dockerized application. From the `app` subdirectory, add the following files:

#### **Dockerfile**

```docker
FROM nginx
COPY index.html /usr/share/nginx/html
```

#### **index.html**

```html
<html>
  <head><meta charset="UTF-8">
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
import * as pulumi from "@pulumi/pulumi";
import * as awsx from "@pulumi/awsx";

// Create a load balancer to listen for requests and route them to the container.
const listener = new awsx.elasticloadbalancingv2.NetworkListener("nginx", { port: 80 });
```

### Step 4: Define the service and publish the Docker image

Add the following lines to `index.ts`:

```typescript
// Define the service, building and publishing our "./app/Dockerfile", and using the load balancer.
const service = new awsx.ecs.FargateService("nginx", {
    desiredCount: 2,
    taskDefinitionArgs: {
        containers: {
            nginx: {
                image: awsx.ecs.Image.fromPath("nginx", "./app"),
                memory: 512,
                portMappings: [listener],
            },
        },
    },
});

// Export the URL so we can easily access it.
export const frontendURL = pulumi.interpolate `http://${listener.endpoint.hostname}/`;
```

You just created an automatic cluster in the default AWS VPC to run a Fargate service.

### Step 5: Verify your app structure

In addition to the `node_modules` directory and related npm package files, ensure you have the following directory structure:

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

To preview your Pulumi program, run [`pulumi up`]({{< relref "/docs/reference/cli/pulumi_up" >}}). The command shows a preview of the resources that will be created and prompts you to proceed with the deployment.  Note that the stack itself is counted as a resource, though it does not correspond to a physical cloud resource.

```bash
$ pulumi up
Previewing update (dev)
...
Do you want to perform this update? yes
Updating (dev)
...
Diagnostics:
  awsx:x:ecs:FargateTaskDefinition (nginx):
  ...

Outputs:
    frontendURL: "http://nginx-4c517b3-c98ba6a1e62b644e.elb.us-east-1.amazonaws.com/"

Resources:
    + 32 created

Duration: 3m39s
```

The deployment takes a few minutes. With your `pulumi up` invocation, Pulumi automatically does the following for you:

- Build and provision a container registry using ECR
- Build the Docker image
- Push the resulting image to the repository

### Step 8: Test the resulting load balancer URL

Now that you've deployed your app, confirm that the service is working via `curl`.

```bash
$ curl $(pulumi stack output frontendURL)
<html>
    <head><meta charset="UTF-8">
        <title>Hello Fargate</title>
    </head>
    <body>
        <p>Hello, containers!</p>
        <p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
    </body>
</html>
```

### Step 9: View container logs (Optional)

To view the runtime logs from the container, use the [`pulumi logs`]({{< relref "/docs/reference/cli/pulumi_logs" >}}) command. To get a log stream, use `pulumi logs --follow`.

```bash
$ pulumi logs --follow
Collecting logs for stack dev since 2021-03-26T10:49:57.000-07:00.

 2021-03-26T11:45:02.624-07:00[nginx-185c47c] 172.31.38.69 - - [26/Mar/2021:18:45:02 +0000] "GET / HTTP/1.1" 200 205 "-" "curl/7.64.1" "-"
 2021-03-26T11:48:44.585-07:00[nginx-185c47c] 172.31.38.69 - - [26/Mar/2021:18:48:44 +0000] "GET / HTTP/1.1" 200 205 "-" "Mozilla/5.0 (compatible; Nimbostratus-Bot/v1.3.2; http://cloudsystemnetworks.com)" "-"
```

## Clean Up

{{< cleanup >}}

## Summary

{{< summary >}}
<p>
    In this tutorial, we showed you how to write a Pulumi program in Typescript, and leverage
Pulumi Crosswalk for AWS (via the <a href="{{< relref "/docs/reference/pkg/nodejs/pulumi/awsx"
>}}">@pulumi/awsx package</a>) in order to build and publish a Dockerized application to a private
Elastic Container Registry (ECR), spin up an ECS Fargate cluster, and run a scalable, load balanced
service.
</p>
{{< /summary >}}

## Next Steps

For more information about containerized applications on AWS, please read these User Guides:

- [Pulumi Crosswalk for AWS Elastic Container Service (ECS)]({{< relref "/docs/guides/crosswalk/aws/ecs" >}})
- [Pulumi Crosswalk for AWS Elastic Kubernetes Service (EKS)]({{< relref "/docs/guides/crosswalk/aws/eks" >}})

For an end-to-end application also includes serverless functions, see the
[Serverless plus Containers Thumbnailer tutorial]({{< relref "video-thumbnailer" >}}).

For an example application that connects two containers, see the
[Voting App](https://github.com/pulumi/examples/tree/master/aws-ts-voting-app) sample.

The [code for this tutorial](https://github.com/pulumi/examples/tree/master/aws-ts-containers) is available on GitHub.
