---
title: "Defining an AWS AppSync Endpoint"
---

<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/aws-ts-appsync" target="_blank">
    <img src="https://get.pulumi.com/new/button.svg" alt="Deploy" style="float: right; padding: 8px; margin-top: -65px; margin-right: 8px">
</a>

> <a class="btn btn-secondary" href="https://github.com/pulumi/examples/tree/master/aws-ts-appsync" target="_blank" style="float: right"><i class="fab fa-github pr-2"></i> VIEW CODE</a>
> The source code for this tutorial is available [on GitHub](https://github.com/pulumi/examples/tree/master/aws-ts-appsync). Ensure you have
> a copy locally and have changed into its directory before starting the tutorial's steps.


This example shows how to setup a basic GraphQL endpoint in AWS AppSync. The endpoint contains one query and one mutation that get and put items to a Dynamo DB table.

## Deploying and running the Pulumi App

1.  Create a new stack:

    ```bash
    $ pulumi stack init dev
    ```

1.  Set the AWS region:

    ```
    $ pulumi config set aws:region us-east-2
    ```

1.  Restore NPM modules via `npm install` or `yarn install`.

1.  Run `pulumi up` to preview and deploy changes:

    ``` 
    $ pulumi up
    Previewing update (dev):
    ...

    Updating (dev):
    ...
    Resources:
        + 10 created
    Duration: 20s
    ```

1.  Check the deployed GraphQL endpoint:

    ```
    $ pulumi stack output endpoint
    https://***.appsync-api.us-east-2.amazonaws.com/graphql
    $ pulumi stack output key
    ***sensitivekey***
    $ curl -XPOST -H "Content-Type:application/graphql" -H "x-api-key:$(pulumi stack output key)" -d '{ "query": "mutation AddTenant { addTenant(id: \"123\", name: \"FirstCorp\") { id name } }" }' "$(pulumi stack output endpoint)" 
    {
        "data": {
            "addTenant": {
                "id": "123",
                "name": "FirstCorp"
            }
        }
    }
    ```

## Clean up

1.  Run `pulumi destroy` to tear down all resources.

1.  To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Console.

