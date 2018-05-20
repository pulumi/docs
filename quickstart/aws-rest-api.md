---
title: "Create a Serverless REST API"
---

With Pulumi, you can combine infrastructure definitions and application code in one program. The [@pulumi/cloud] library is a set of Pulumi [components](../reference/programming-model.html#components) that provide a higher-level abstraction over AWS. So, instead of provisioning an API Gateway instance, Lambda functions, and setting up IAM roles, you can use [cloud.HttpEndpoint] and define application code at the same time as the infrastructure it depends on.

In this tutorial, we'll show how to create a simple REST API that counts the number of times a route has been hit. To implement this API, we need a key-value store, an API endpoint, and a Lambda function. 

{% include aws-resource-note.md %}
{% include aws-js-prereqs.md %}

## Create a simple REST API

1.  In a new folder `hello-http`, run `pulumi new javascript`.

1.  Replace the contents of `index.js` with the following:

    ```javascript
    const cloud = require("@pulumi/cloud-aws");

    // Create a mapping from 'route' to a count
    let counterTable = new cloud.Table("counterTable", "route");

    // Create an API endpoint
    let endpoint = new cloud.HttpEndpoint("hello-world");

    endpoint.get("/{route+}", async (req, res) => {
        let route = req.params["route"];
        console.log(`Getting count for '${route}'`);

        // get previous value and increment
        let value = await counterTable.get({ route }); // reference outer `counterTable` object
        let count = (value && value.count) || 0;
        await counterTable.insert( { route, count: ++count });

        res.status(200).json({ route, count });
        console.log(`Got count ${count} for '${route}'`);
    });

    module.exports.endpoint = endpoint.publish().url;
    ```

    The definition for `counterTable` stores a counter for each route, using [cloud.Table]. On AWS, this provisions a DynamoDB instance. To create a new API Gateway instance, we create an instance of [cloud.HttpEndpoint]. New routes can be added to this endpoint using methods like `get`, `post`, `put` etc.
       
    The function passed to `get` is the interesting part: this becomes the body of a new AWS Lambda function that is called on a GET request to the API Gateway. The body of this function can use variables defined in the main program, such as `counterTable`. This is translated to a lookup on the provisioned DynamoDB instance; there is no need to store its ARN in an environment variable.

1.  Add and install the NPM dependencies:

    ```bash
    $ npm install --save @pulumi/cloud @pulumi/cloud-aws
    ```

1.  Configure your AWS region:

    ```bash
    $ pulumi config set aws:region us-west-2
    ```

1.  Preview and deploy changes via `pulumi update`. A total of 14 resources will be created.

1.  View the endpoint URL and curl a few routes:

    ```bash
    $ pulumi stack output 
    Current stack outputs (1):
        OUTPUT            VALUE
        endpoint          https://5e8xrktey3.execute-api.us-west-2.amazonaws.com/stage/
    
    $ curl $(pulumi stack output endpoint)/hello
    {"route":"hello","count":1}
    $ curl $(pulumi stack output endpoint)/woohoo
    {"route":"woohoo","count":1}
    ```

1.  To view the runtime logs of the Lambda function, use the `pulumi logs` command. To get a log stream, use `pulumi logs --follow`.

    ```
    $ pulumi logs --follow
    Collecting logs since 2018-05-01T21:22:59.000-07:00.

    2018-05-01T22:25:05.040-07:00[           hello-world4fcc7b60] Getting count for 'hello'
    2018-05-01T22:25:05.188-07:00[           hello-world4fcc7b60] Got count 1 for 'hello'
    2018-05-01T22:25:13.562-07:00[           hello-world4fcc7b60] Getting count for 'woohoo'
    2018-05-01T22:25:13.704-07:00[           hello-world4fcc7b60] Got count 1 for 'woohoo'
    ```

## Clean up

{% include cleanup.md %}

## Next steps

For an end-to-end application with a frontend, see the [URL shortener sample](https://github.com/pulumi/examples/tree/master/cloud-ts-url-shortener).

<!-- LINKS -->
[@pulumi/cloud]: ../reference/cloud.html
[cloud.HttpEndpoint]: ../packages/pulumi-cloud/interfaces/_httpendpoint_.httpendpoint.html
[cloud.Table]: ../packages/pulumi-cloud/interfaces/_table_.table.html
<!-- END LINKS -->
