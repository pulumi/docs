---
title: "Tutorial: Containers on ECS Fargate"
redirect_from: /quickstart/aws-containers.html
---

In this tutorial, we'll use JavaScript to build and deploy a simple container to [AWS Fargate](https://aws.amazon.com/fargate/). The [code for this tutorial](https://github.com/pulumi/examples/tree/master/cloud-js-containers) is available on GitHub.

{% include aws-js-prereqs.md %}

## Serve an HTML file in an NGINX container

1.  Make sure [Docker](https://docs.docker.com/install/) is installed and running.

1.  Run `pulumi new`:

    ```bash
    $ pulumi new aws-javascript --dir container-quickstart
    $ cd container-quickstart
    ```

1.  Replace the contents of `index.js` with the following:

    ```js
    const cloud = require("@pulumi/cloud-aws");

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

    This example uses [cloud.Service](/reference/pkg/nodejs/@pulumi/cloud/index.html#Service), which is a high-level, convenient interface for building containers and provisioning an AWS container service.

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

1.  Install the `@pulumi/cloud-aws` NPM package:

    ```bash
    $ npm install --save @pulumi/cloud-aws @pulumi/cloud
    ```

1.  Configure Pulumi to use AWS Fargate. (Note: Fargate is currently available only in `us-east-1`, `us-east-2`, `us-west-2`, and `eu-west-1`).

    ```bash
    $ pulumi config set cloud-aws:useFargate true
    ```

1.  Preview and deploy changes via `pulumi update`. This will take a few minutes. Pulumi automatically builds and provisions an AWS container repository in ECR, builds the Docker container, and places the image in the repository. This all happens automatically and does not require manual configuration on your part.

    ```
    $ pulumi update
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

For an end-to-end application also includes serverless functions, see the [Serverless and Container Thumbnailer](../cloudfx/tutorial-thumbnailer.html) tutorial.

For an example application that connects two containers, see the [Voting App](https://github.com/pulumi/examples/tree/master/cloud-ts-voting-app) TypeScript sample.
