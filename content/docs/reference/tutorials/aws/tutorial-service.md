---
title: "Containers on ECS \"Fargate\""
menu:
  reference:
    parent: tutorials-aws
---

In this tutorial, we'll build and publish a Docker container image to a private Elastic Container Registry (ECR), and
spin up a load balanced Amazon Elastic Container Service (ECS) "Fargate" service, all in a handful of lines of code,
using [Pulumi Crosswalk for AWS]({{< relref "/docs/reference/crosswalk/aws/_index.md" >}}).

## Prerequisites

1.  [Install Docker Desktop](https://docs.docker.com/install/)
1.  [Install Pulumi]({{< relref "/docs/reference/install.md" >}})
1.  [Configure Pulumi to use your AWS account]({{< relref "/docs/reference/clouds/aws/setup.md" >}})

## Deploying the App and Infrastructure

To get started, we will create a project, initialize it, then run `pulumi up`:

1.  Run `pulumi new` to create a new project:

    ```bash
    $ mkdir hello-fargate && cd hello-fargate
    $ pulumi new aws-typescript
    ```

1.  Create a subfolder `app` containing our sample Dockerized application:

    - Add the following file as `Dockerfile`:
      ```docker
      FROM nginx
      COPY index.html /usr/share/nginx/html
      ```

    - Add the following file as `index.html`:
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

1.  Replace the contents of `index.ts` with the following:

    ```typescript
    import * as awsx from "@pulumi/awsx";

    // Create a load balancer to listen for requests and route them to the container.
    let lb = new awsx.elasticloadbalancingv2.NetworkListener("nginx", { port: 80 });

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

    This example creates an automatic cluster in the default AWS VPC to run our "Fargate" service.

1.  Ensure you have the following directory structure:

    ```
    Pulumi.yaml
    index.ts
    app/
      Dockerfile
      index.html
    ```

1.  Configure the AWS region you would like to use:

    ```bash
    $ pulumi config set aws:region us-east-1
    ```

1.  Preview and deploy changes via `pulumi up`. This will take a few minutes. Pulumi automatically builds and
    provisions an ECR container registry, builds the Docker container, and pushed the image into the repository. This
    all happens automatically and does not require manual configuration on your part:

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

    info: 19 changes performed:
        + 19 resources created
    Update duration: 3m53.44141303s
    ```

1.  Test the resulting load balancer URL to see that our service is working!

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

1.  (Optional) To view the runtime logs from the container, use the `pulumi logs` command. To get a log stream, use
    `pulumi logs --follow`.

    ```bash
    $ pulumi logs --follow
    Collecting logs for stack container-quickstart-dev since 2018-05-22T14:25:46.000-07:00.
    2018-05-22T15:33:22.057-07:00[                  pulumi-nginx] 172.31.13.248 - - [22/May/2018:22:33:22 +0000]
        "GET / HTTP/1.1" 200 189 "-" "curl/7.54.0" "-"
    ```

## Clean Up

{{< cleanup >}}

## Next Steps

For more information about containerized applications on AWS, please read these User Guides:

* [Pulumi Crosswalk for AWS Elastic Container Service (ECS)]({{< relref "/docs/reference/crosswalk/aws/ecs.md" >}})
* [Pulumi Crosswalk for AWS Elastic Kubernetes Service (EKS)]({{< relref "/docs/reference/crosswalk/aws/eks.md" >}})

For an end-to-end application also includes serverless functions, see the
[Serverless plus Containers Thumbnailer tutorial]({{< relref "tutorial-thumbnailer.md" >}}).

For an example application that connects two containers, see the
[Voting App](https://github.com/pulumi/examples/tree/master/aws-ts-voting-app) sample.

The [code for this tutorial](https://github.com/pulumi/examples/tree/master/aws-ts-containers) is available on GitHub.
