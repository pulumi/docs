---
title: "GCP Functions"
---

<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/gcp-ts-functions" target="_blank">
    <img src="https://get.pulumi.com/new/button.svg" alt="Deploy" style="float: right; padding: 8px; margin-top: -65px; margin-right: 8px">
</a>

> <a class="btn btn-secondary" href="https://github.com/pulumi/examples/tree/master/gcp-ts-functions" target="_blank" style="float: right"><i class="fab fa-github pr-2"></i> VIEW CODE</a>
> The source code for this tutorial is available [on GitHub](https://github.com/pulumi/examples/tree/master/gcp-ts-functions). Ensure you have
> a copy locally and have changed into its directory before starting the tutorial's steps.


An example of deploying an HTTP Google Cloud Function endpoint using TypeScript.

## Prerequisites

0. [Ensure you have the latest Node.js and NPM](https://nodejs.org/en/download/)
2. [Install the Pulumi CLI](https://www.pulumi.com/docs/reference/install/)
3. [Configure Pulumi to access your GCP account](https://www.pulumi.com/docs/reference/clouds/gcp/setup/)

## Running the App

1.  Restore NPM dependencies:

    ```
    $ npm install
    ```

2.  Create a new stack:

    ```
    $ pulumi stack init gcp-fn
    ```

3.  Configure your GCP project and region:

    ```
    $ pulumi config set gcp:project <projectname> 
    $ pulumi config set gcp:region <region>
    ```

4.  Run `pulumi up` to preview and deploy changes:

    ``` 
    $ pulumi up
    Previewing changes:
    ...

    Performing changes:
    ...
    info: 6 changes performed:
        + 6 resources created
    Update duration: 39.65130324s
    ```

5.  Check the deployed function endpoint:

    ```
    $ pulumi stack output url
    https://us-central1-pulumi-development.cloudfunctions.net/greeting-function-7f95447
    $ curl "$(pulumi stack output url)"
    Greetings from Google Cloud Functions!
    ```

6. Clean up your GCP and Pulumi resources:

    ```
    $ pulumi destroy
    ...
    $ pulumi stack rm
    ...
    ```

