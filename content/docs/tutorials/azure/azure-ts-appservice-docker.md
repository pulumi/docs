---
title: "Azure App Service running Docker containers on Linux"
---

<p class="mb-4 flex">
    <a class="flex flex-wrap items-center rounded text-xs text-white bg-blue-600 border-2 border-blue-600 px-2 mr-2 whitespace-no-wrap hover:text-white" style="height: 32px" href="https://github.com/pulumi/examples/tree/master/azure-ts-appservice-docker" target="_blank">
        <span><i class="fab fa-github pr-2"></i> View Code</span>
    </a>

    <a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/azure-ts-appservice-docker" target="_blank">
        <img src="https://get.pulumi.com/new/button.svg" alt="Deploy">
    </a>
</p>


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

