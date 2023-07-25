---
title: How do I set up an Amazon API Gateway to listen for webhook events?
allow_long_title: true
meta_desc: Discover step-by-step how to set up an API Gateway to listen for webhook events in our comprehensive tutorial.
type: ai-answers
date: 2023-07-24
---

To accomplish your goal of setting up an API Gateway that listens for an event from a webhook, you can use the AWS api resources.

Here's a simple Pulumi TypeScript program that sets up a REST API through AWS API Gateway using a mock integration. This is for illustrative purposes to get you started. In a real-world setup, you might have to change the integration to invoke a Lambda function or another backend based on the event received.

This example doesn't handle the webhook authentication and validation which you would need to handle based on the webhook provider's requirements. You might need a Lambda function for that.

{{< chooser language "typescript,python,go,csharp,java,yaml" />}}

{{% choosable language typescript %}}

```typescript

const myTask = new cloud.Task("myTask", {
    build: "./app", // subfolder of working directory
    ...
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create a REST API
let api = new aws.apigateway.RestApi("api", {
    description: "My API Gateway"
});

// Create a resource for the path for the webhook
let resource = new aws.apigateway.Resource("resource", {
    parentId: api.rootResourceId,
    pathPart: "webhook",
    restApi: api.id
});

// Create a method for that resource
let method = new aws.apigateway.Method("method", {
    authorization: "NONE",
    httpMethod: "POST",
    resourceId: resource.id,
    restApi: api.id
});

// Create a mock integration for the method
let integration = new aws.apigateway.Integration("integration", {
    httpMethod: method.httpMethod,
    resourceId: resource.id,
    restApi: api.id,
    type: "MOCK"
});

// Exports the API Gateway URL
export const url = api.id.apply(id => `https://${id}.execute-api.${aws.config.requireRegion()}.amazonaws.com/prod/webhook`);

});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create a REST API
let api = new aws.apigateway.RestApi("api", {
    description: "My API Gateway"
});

// Create a resource for the path for the webhook
let resource = new aws.apigateway.Resource("resource", {
    parentId: api.rootResourceId,
    pathPart: "webhook",
    restApi: api.id
});

// Create a method for that resource
let method = new aws.apigateway.Method("method", {
    authorization: "NONE",
    httpMethod: "POST",
    resourceId: resource.id,
    restApi: api.id
});

// Create a mock integration for the method
let integration = new aws.apigateway.Integration("integration", {
    httpMethod: method.httpMethod,
    resourceId: resource.id,
    restApi: api.id,
    type: "MOCK"
});

// Exports the API Gateway URL
export const url = api.id.apply(id => `https://${id}.execute-api.${aws.config.requireRegion()}.amazonaws.com/prod/webhook`);

    }
)

```

{{% /choosable %}}
{{% choosable language python %}}

```python

import pulumi
from pulumi_aws import apigateway

# Create a new REST API
api = apigateway.RestApi("api", description="API for receiving webhook events.")

# Create a resource for /webhook path
webhook_resource = apigateway("webhook_resource", rest_api=api.id, path_part="webhook", parent_id=api.root_resource_id)

# Create a HTTP method for the resource
webhook_method = apigateway.Method(
    "webhook_method",
    http_method="POST",
    authorization="NONE",
    resource_id=webhook_resource.id,
    rest_api=api.id,
)

# Export the id and url of the Rest API
pulumi.export("apiId", api.id)
pulumi.export("apiUrl", api.execution_arn.apply(lambda arn: f"https://{arn}.execute-api.{pulumi.get_stack().location}/example-stage/"))

```

{{% /choosable %}}
{{% choosable language go %}}

```go

package main

import (
    "github.com/pulumi/pulumi-aws/sdk/v4/go/aws/apigatewayv2"
    "github.com/pulumi/pulumi-aws/sdk/v4/go/aws/lambda"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)


func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        lambdaFn, err := lambda.LookupFunction(ctx, &lambda.LookupFunctionArgs{
            FunctionName: "<your-lambda-function>",
        })
        if err != nil {
            return err
        }

        webhookAPI, err := apigatewayv2.NewApi(ctx, "Webhook", &apigatewayv2.ApiArgs{
            ProtocolType:   pulumi.String("HTTP"),
            Target:         lambdaFn.Arn,
            RouteSelectionExpression: pulumi.String(`$request.method == 'POST' && $request.path == '/webhook'`),
        })
        if err != nil {
            return err
        }

        _, err = apigatewayv2.NewStage(ctx, "WebhookAPIStage", &apigatewayv2.StageArgs{
    ApiId:     webhookAPI.ID(),
            AutoDeploy: pulumi.Bool(true),
            Name:      pulumi.String("$default"),
        })
        if err != nil {
            return err
        }

        ctx.Export("apiEndpoint", webhookAPI.ApiEndpoint)
        return nil
    })
}


```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp

using Pulumi;
using Aws = Pulumi.Aws;

class MyStack : Stack
{
    public MyStack()
    {
        // an AWS Lambda function
        var webhookHandler = new Aws.Lambda.Function("webhookHandler", new Aws.Lambda.FunctionArgs
        {
            =nodejs12.x",
           "),
 });

        // Create an Execute API Gateway
        var api = new Aws.Apigatewayv2.Api("api", new Aws.Apigatewayv2.ApiArgs
        {
            ProtocolType = "HTTP",
            RouteKey = "POST /webhook",
            Target = webhookHandler.Arn
        });

        // Export the API endpoint URL
        this.Endpoint = api.ApiEndpoint    }

    [Output]
    public Output<string> Endpoint { get; set; }
}


```

{{% /choosable %}}
{{% choosable language java %}}

```java

import com.pulumi.*;
import com.pulumi.aws.apigatewayv2.Api;
import com.pulumi.aws.apigatewayv2.Integration;
import com.pulumi.aws.apigatewayv2.Route;
import com.p.aws.lambda.Function;

class MyStack extends Stack {
    public MyStack() {
        super(new StackOptions());

        Function myLambda = ... // Create or import your lambda resource here

 httpApi = new Api("myApi", new ApiArgs()
            .setProtocolType("HTTP")
            .setTarget(myLambda.getArn()));

        Integration httpIntegration = new Integration("myIntegration", new IntegrationArgs()
            .setApiId(httpApi.getId())
            .setIntegrationType("AWS_PROXY")
            .setIntegrationUri(myLambda.getArn()));

        Route httpRoute = new Route("myRoute", new RouteArgs()
            .setApiId(httpApi.getId())
            .setRoute("$default")
            .setTarget("integrations/" + httpIntegration.getId()));
    }

    @Override
    public void registerOutputs(Output<?>... outputs) {
        super.registerOutputs(outputs);
    }
}


```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml

description: A minimal AWS API Gateway example
resources:
  - name: myHttpApi
    type: aws:apigatewayv2/api:Api
    args:
      name: my-http-api
      protocolType: HTTP
  - name: myHttpApiRoute
    type: aws:apigatewayv2/route:Route
    args:
      apiId:
        source: myHttpApi.apiId
      routeKey: POST /webhook
  - name: myHttpApiIntegration
    type: aws:apigatewayv2/integration:Integration
    args:
      apiId:
        source: myHttpApi.apiId
      integrationType: MOCK
      integrationMethod: POST
  - name: myHttpApiRouteIntegration
    type: aws:apigatewayv2/routeResponse:Route
    args:
      apiId:
        source: myHttpApi.apiId
      routeId:
        source: myHttpApiRoute.id
      integrationId:
        source: myHttpApiIntegration.id
```

{{% /choosable %}}

This code triggers the webhookHandler Lambda function when a POST request is made to the /webhook route of the API Gateway. The response from the API is a 200 status code and a message saying "Webhook received".

In the webhookHandler function, it's here that you process the details of the webhook event: payload data, sender identity, etc.

For more complex API use cases, or if the awsx library is not suitable for you, directly use the aws.apigateway from the @pulumi/aws library.

Here are links to the relevant resources in the Pulumi Registry for your reference:

* [aws:apigatewayv2/api:Api](https://www.pulumi.com/registry/packages/aws/api-docs/apigatewayv2/api/)
* [aws:apigatewayv2/route:Route](https://www.pulumi.com/registry/packages/aws/api-docs/apigatewayv2/route/)
* [aws:apigatewayv2/integration:Integration](https://www.pulumi.com/registry/packages/aws/api-docs/apigatewayv2/integration/)
