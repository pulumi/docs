---
title: "Tutorial: Containers"
redirect_from:
  - /quickstart/aws-containers.html
  - /quickstart/aws/tutorial-containers-ecs-fargate.html
---

In this tutorial, we'll use TypeScript to build and deploy a simple container using the [`@pulumi/aws`]() and [`@pulumi/aws-infra`]() frameworks.  This example can be deployed to AWS on either Fargate, and can be simply updated to use ECS as well.  The [code for this tutorial](https://github.com/pulumi/examples/tree/master/aws-ts-containers) is available on GitHub.

## Prerequisites

1.  [Install Pulumi](../install.html)
1.  Configure [AWS](../aws/setup.html) credentials

## Serve an HTML file in an NGINX container

1.  Make sure [Docker](https://docs.docker.com/install/) is installed and running.

1.  Run `pulumi new`:

    ```bash
    $ mkdir container-quickstart && cd container-quickstart
    $ pulumi new aws-typescript
    ```

1.  Replace the contents of `index.ts` with the following:

    ```ts
    import * as pulumi from "@pulumi/pulumi";
    import * as aws from "@pulumi/aws";
    import * as awsx from "@pulumi/awsx";
    
    // Create an elastic network listener to listen for requests and route them to the container.
    // See https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html
    // for more details.
    let listener = new awsx.elasticloadbalancingv2.NetworkListener("nginx", { port: 80 });

    // Define the service to run.  We pass in the listener to hook up the network load balancer
    // to the containers the service will launch.
    let service = new awsx.ecs.FargateService("nginx", {
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

    // export just the hostname property of the container frontend
    export const hostname = listener.endpoint.apply(e => `http://${e.hostname}`);
    ```

    This example uses awsx.ecs.FargateService, which is a high-level, convenient interface for building containers and provisioning a fargate service in aws.

1.  Create a subfolder `app` with the following files:

    - Add the following file as `Dockerfile`:
      ```docker
      FROM nginx
      COPY index.html /usr/share/nginx/html
      ```

    - Add the following file as `index.html`:
      ```html
      <html>
        <head><title>Hello World</title><meta charset="UTF-8"></head>
      <body><p>Hello containers!</p><p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p></body>
      </html>
      ```

1.  Ensure you have the following directory structure:

    ```bash
    index.js
    Pulumi.yaml
    app/
      Dockerfile
      index.html
    ```

1.  Install the necessary NPM packages:

    ```bash
    $ npm install --save @pulumi/pulumi  @pulumi/aws @pulumi/aws-infra
    ```

1.  Configure the AWS region you would like to use:

    ```bash
    $ pulumi config set aws:region us-east-1
    ```

1.  Preview and deploy changes via `pulumi up`. This will take a few minutes. Pulumi automatically builds and provisions an ecr container registry, builds the Docker container, and pushed the image into the repository. This all happens automatically and does not require manual configuration on your part.

    ```
    $ pulumi up
    Previewing update of stack 'container-quickstart-dev'
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

1.  View the endpoint URL and run curl:

    ```bash
    $ pulumi stack output
    Current stack outputs (1)
        OUTPUT                  VALUE
        url                     42dc3ff4-ac65d11-86a100b6e1d7f210.elb.us-west-2.amazonaws.com

    $ curl $(pulumi stack output url)
    <html><head>
        <title>Hello world</title><meta charset="UTF-8">
    </head>
    <body><p>Hello, containers!</p><p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
    </body></html>
    ```

1.  To view the runtime logs from the container, use the `pulumi logs` command. To get a log stream, use `pulumi logs --follow`.

    ```bash
    $ pulumi logs --follow
    Collecting logs for stack container-quickstart-dev since 2018-05-22T14:25:46.000-07:00.
    2018-05-22T15:33:22.057-07:00[                  pulumi-nginx] 172.31.13.248 - - [22/May/2018:22:33:22 +0000]
        "GET / HTTP/1.1" 200 189 "-" "curl/7.54.0" "-"
    ```

## Clean up

{% include cleanup.md %}

## Next steps

For an end-to-end application also includes serverless functions, see the [Serverless and Container Thumbnailer](./tutorial-thumbnailer.html) tutorial.

For an example application that connects two containers, see the [Voting App](https://github.com/pulumi/examples/tree/master/aws-ts-voting-app) TypeScript sample.
