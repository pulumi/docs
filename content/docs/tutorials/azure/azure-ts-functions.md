---
title: "Azure Functions"
---

<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/azure-ts-functions" target="_blank">
    <img src="https://get.pulumi.com/new/button.svg" alt="Deploy" style="float: right; padding: 8px; margin-top: -65px; margin-right: 8px">
</a>

<p class="mb-4">
    <a class="btn btn-secondary" href="https://github.com/pulumi/examples/tree/master/azure-ts-functions" target="_blank"><i class="fab fa-github pr-2"></i> VIEW CODE</a>
</p>


An example Pulumi program that deploys a TypeScript function to Azure Functions.

## Running the App

1.  Create a new stack:

    ```
    $ pulumi stack init azure-fn
    ```

1.  Login to Azure CLI (you will be prompted to do this during deployment if you forget this step):

    ```
    $ az login
    ```

1.  Restore NPM dependencies:

    ```
    $ npm install
    ```

1.  Configure the location to deploy the example to:

    ```
    $ pulumi config set azure:location <location>
    ```

1.  Run `pulumi up` to preview and deploy changes:

    ``` 
    $ pulumi up
    Previewing changes:
    ...

    Performing changes:
    ...
    info: 9 changes performed:
        + 9 resources created
    Update duration: 1m20.493392283s
    ```

1.  Check the deployed function endpoint:

    ```
    $ pulumi stack output endpoint
    https://fn-app051a4f8b.azurewebsites.net/api/fn
    $ curl "$(pulumi stack output endpoint)"
    Greetings from Azure Functions!
    ...
    ```

