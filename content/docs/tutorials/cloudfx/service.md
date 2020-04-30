---
title: Build & Deploy Docker to AWS or Azure
meta_desc: This tutorial will teach you how to build and deploy a Dockerized application to AWS or Azure.
aliases: ["/docs/quickstart/cloudfx/tutorial-service/"]
---

In this tutorial, we'll use JavaScript to build and deploy a simple container using the [`@pulumi/cloud`]({{< prelref "/docs/reference/pkg/nodejs/pulumi/cloud" >}}) framework.  This example can be deployed to AWS (on either Fargate or ECS) or to Azure (on ACI).  By authoring our infrastructure using the `@pulumi/cloud` framework, it can be deployed transparently to either cloud (with support for other clouds on the roadmap). The [code for this tutorial](https://github.com/pulumi/examples/tree/master/cloud-js-containers) is available on GitHub.

## Prerequisites

1. [Install Pulumi]({{< prelref "/docs/get-started/install" >}})
1. Configure [AWS]({{< prelref "/docs/intro/cloud-providers/aws/setup" >}}) and/or [Azure]({{< prelref "/docs/intro/cloud-providers/azure/setup" >}}) credentials

## Serve an HTML file in an NGINX container

1. Make sure [Docker](https://docs.docker.com/install/) is installed and running.

1. Run `pulumi new`:

    ```bash
    $ mkdir container-quickstart && cd container-quickstart
    $ pulumi new javascript
    ```

1. Replace the contents of `index.js` with the following:

    ```javascript
    const cloud = require("@pulumi/cloud");

    let service = new cloud.Service("pulumi-nginx", {
        containers: {
            nginx: {
                build: "./app",
                memory: 128,
                ports: [{ port: 80 }],
            },
        },
        replicas: 2,
    });

    // export just the hostname property of the container frontend
    exports.url = service.defaultEndpoint.apply(e => `http://${e.hostname}`);
    ```

    This example uses [cloud.Service]({{< prelref "/docs/reference/pkg/nodejs/pulumi/cloud#Service" >}}), which is a high-level, convenient interface for building containers and provisioning a container service on your target cloud.

1. Create a subfolder `app` with the following files:

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

1. Ensure you have the following directory structure:

    ```bash
    index.js
    Pulumi.yaml
    app/
      Dockerfile
      index.html
    ```

1. Install the `@pulumi/cloud` NPM package an one or both of the platform-specific implementations depending on which platform you will deploy to:

    ```bash
    $ npm install --save @pulumi/cloud  @pulumi/cloud-aws @pulumi/cloud-azure
    ```

1. If you are running on AWS, configure the provider, the region and whether to use Fargate:

    ```bash
    $ pulumi config set cloud:provider aws
    $ pulumi config set aws:region us-east-1
    $ pulumi config set cloud-aws:useFargate true
    ```

    If you are running on Azure, configure the provider and the location:

    ```bash
    $ pulumi config set cloud:provider azure
    $ pulumi config set cloud-azure:location WestUS2
    ```

1. Preview and deploy changes via `pulumi up`. This will take a few minutes. Pulumi automatically builds and provisions a container registry (ECR or ACR), builds the Docker container, and pushed the image into the repository. This all happens automatically and does not require manual configuration on your part.

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

1. View the endpoint URL and run curl:

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

1. To view the runtime logs from the container, use the `pulumi logs` command. To get a log stream, use `pulumi logs --follow`.

    ```bash
    $ pulumi logs --follow
    Collecting logs for stack container-quickstart-dev since 2018-05-22T14:25:46.000-07:00.
    2018-05-22T15:33:22.057-07:00[                  pulumi-nginx] 172.31.13.248 - - [22/May/2018:22:33:22 +0000]
        "GET / HTTP/1.1" 200 189 "-" "curl/7.54.0" "-"
    ```

## Clean up

{{< cleanup >}}

## Next steps

For an end-to-end application also includes serverless functions, see the [Serverless and Container Thumbnailer]({{< prelref "thumbnailer" >}}) tutorial.

For an example application that connects two containers, see the [Voting App](https://github.com/pulumi/examples/tree/master/cloud-ts-voting-app) TypeScript sample.
