---
title: "Azure App Service with SQL Database and Application Insights"
---

<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/azure-ts-appservice" target="_blank">
    <img src="https://get.pulumi.com/new/button.svg" alt="Deploy" style="float: right; padding: 8px; margin-top: -65px; margin-right: 8px">
</a>

> <a class="btn btn-secondary" href="https://github.com/pulumi/examples/tree/master/azure-ts-appservice" target="_blank" style="float: right"><i class="fab fa-github pr-2"></i> VIEW CODE</a>
> The source code for this tutorial is available [on GitHub](https://github.com/pulumi/examples/tree/master/azure-ts-appservice). Ensure you have
> a copy locally and have changed into its directory before starting the tutorial's steps.


Starting point for building web application hosted in Azure App Service.

Provisions Azure SQL Database and Azure Application Insights to be used in combination
with App Service.

## Running the App

1.  Create a new stack:

    ```
    $ pulumi stack init azure-appservice
    ```

1.  Login to Azure CLI (you will be prompted to do this during deployment if you forget this step):

    ```
    $ az login
    ```

1.  Restore NPM dependencies:

    ```
    $ npm install
    ```

1. Define SQL Server password (make it complex enough to satisfy Azure policy):

    ```
    pulumi config set --secret sqlPassword <value>
    ```

1.  Run `pulumi up` to preview and deploy changes:

    ``` 
    $ pulumi up
    Previewing changes:
    ...

    Performing changes:
    ...
    info: 10 changes performed:
        + 10 resources created
    Update duration: 1m14.59910109s
    ```

1.  Check the deployed website endpoint:

    ```
    $ pulumi stack output endpoint
    https://azpulumi-as0ef47193.azurewebsites.net
    $ curl "$(pulumi stack output endpoint)"
    <html>
        <body>
            <h1>Greetings from Azure App Service!</h1>
        </body>
    </html>
    ```

