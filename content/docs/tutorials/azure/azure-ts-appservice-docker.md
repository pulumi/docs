---
title: "Azure App Service running Docker containers on Linux"
---

<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/azure-ts-appservice-docker" target="_blank">
    <img src="https://get.pulumi.com/new/button.svg" alt="Deploy" style="float: right; padding: 8px; margin-top: -65px; margin-right: 8px">
</a>

> <a class="btn btn-secondary" href="https://github.com/pulumi/examples/tree/master/azure-ts-appservice-docker" target="_blank" style="float: right"><i class="fab fa-github pr-2"></i> VIEW CODE</a>
> The source code for this tutorial is available [on GitHub](https://github.com/pulumi/examples/tree/master/azure-ts-appservice-docker). Ensure you have
> a copy locally and have changed into its directory before starting the tutorial's steps.


Starting point for building web application hosted in Azure App Service from Docker images.

The example shows two scenarios:

- Deploying an existing image from Docker Hub
- Deploying a new custom registry in Azure Container Registry, building a custom Docker image, and running the image from the custom registry

## Running the App

1.  Create a new stack:

    ```
    $ pulumi stack init azure-appservice-docker
    ```

1.  Login to Azure CLI (you will be prompted to do this during deployment if you forget this step):

    ```
    $ az login
    ```

1.  Restore NPM dependencies:

    ```
    $ npm install
    ```

1.  Run `pulumi up` to preview and deploy changes:

    ```
    $ pulumi up
    Previewing changes:
    ...

    Performing changes:
    ...
    Resources:
        + 7 created

    Duration: 4m56s
    ```

1.  Check the deployed endpoints:

    ```
    $ pulumi stack output helloEndpoint
    http://hello-app91dfea21.azurewebsites.net/hello
    $ curl "$(pulumi stack output helloEndpoint)"
    Hello, world!

    $ pulumi stack output getStartedEndpoint
    http://get-started15da1348.azurewebsites.net
    $ curl "$(pulumi stack output getStartedEndpoint)"
    <html>
    <body>
    <h1>Your custom docker image is running in Azure App Service!</h1>
    </body>
    </html>
    ```

