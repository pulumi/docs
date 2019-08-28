---
title: "A Static Website Hosted on Azure Blob Storage + Azure CDN"
---

<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/azure-ts-static-website" target="_blank">
    <img src="https://get.pulumi.com/new/button.svg" alt="Deploy" style="float: right; padding: 8px; margin-top: -65px; margin-right: 8px">
</a>

<p class="mb-4">
    <a class="btn btn-secondary" href="https://github.com/pulumi/examples/tree/master/azure-ts-static-website" target="_blank"><i class="fab fa-github pr-2"></i> VIEW CODE</a>
</p>


This example configures [Static website hosting in Azure Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website). One complication is the fact that the Static Website feature of Storage Accounts is not part of Azure Resource Manager, and is not configurable directly via Pulumi Azure provider.

As a workaround, a custom [dynamic provider](https://www.pulumi.com/docs/reference/programming-model/#dynamicproviders) and a dynamic resource are created. The provider delegates the setup to Azure CLI commands, while still providing Pulumi experience and lifecycle management.

In addition to the Storage itself, a CDN is configured to serve files from the Blob container origin. This may be useful if you need to serve files via HTTPS from a custom domain (not shown in the example).

## Running the App

1.  Create a new stack:

    ```
    $ pulumi stack init dev
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
        + 8 created
    Duration: 2m52s
    ```

1.  Check the deployed website endpoint:

    ```
    $ pulumi stack output staticEndpoint
    https://websitesbc90978a1.z20.web.core.windows.net/
    $ curl "$(pulumi stack output staticEndpoint)"
    <html>
        <body>
            <h1>This file is served from Blob Storage</h1>
        </body>
    </html>
    ```

