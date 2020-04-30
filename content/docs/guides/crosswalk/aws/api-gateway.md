---
title: "AWS API Gateway"
meta_desc: Pulumi Crosswalk for AWS provides a significantly easier way of programming API Gateway.
linktitle: API Gateway
menu:
  userguides:
    parent: crosswalk-aws
    weight: 1

aliases: ["/docs/reference/crosswalk/aws/api-gateway/"]
---

<a href="{{< prelref "./" >}}">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[AWS API Gateway](https://aws.amazon.com/api-gateway/) is a fully managed service for creating, monitoring, and
securing APIs at scale. It acts as a "front door" for REST and WebSocket applications that use backend services,
and handles all the tasks necessary to accept and process up to hundreds of thousands of concurrent API calls,
including traffic management, authorization and access control, monitoring, and API version management. API Gateway
is inexpensive, has no minimum fees, and you only pay for the API calls you receive and the data transferred out.

## Overview

Pulumi Crosswalk for AWS provides significantly easier ways of programming API Gateway. This includes using
infrastructure as code techniques for simple, declarative APIs, including easy Lambda-based handlers.

## Defining an AWS API Gateway Endpoint and Routes

AWS API Gateway creates REST APIs that:

* Are HTTP based.
* Adhere to the [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) protocol.
* Implement standard HTTP methods such as `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`.

Each API Gateway instance defines a new API endpoint and a collection of API routes, each of which has a distinct URL.

> Internally the API Gateway resource uses a collection of supporting objects, like resources, methods, and more,
> however one of the benefits of Pulumi Crosswalk for AWS is that it hides these mechanics behind a simpler interface.

Each API Gateway deployment is associated with a so-called _stage_. A stage is simply a version of your API, such
as `stage`, `prod`, `v1`, or `v2`. For simple APIs, you will likely just have one. You can always define a custom
stage name, but if you leave it off, a default of `stage` will be chosen.

API Gateway will auto-generate a domain name with built-in HTTPS support. The stage name will also be part of this URL.
We will see later how to assign a custom domain, SSL certificate, and/or eliminate the stage name from the URL.

There are multiple ways to define APIs using Pulumi Crosswalk for AWS:

* [Lambda Function Event Handler Route](#defining-a-lambda-function-event-handler-route)
* [Static Route Served by S3](#defining-a-static-route-served-by-s3)
* [Integration Route](#defining-an-integration-route)
* [OpenAPI Specification for an Entire Endpoint](#defining-an-openapi-specification-for-an-entire-endpoint)
* [OpenAPI Specification for a Single Route](#defining-an-openapi-specification-for-a-single-route)

Multiple endpoints on the same API Gateway can be defined using a combination of these techniques.

### Defining a Lambda Function Event Handler Route

An Event Handler Route is an API that will map to a [Lambda Function](https://aws.amazon.com/lambda/). You will specify
the path, HTTP method, and the Lambda Function to invoke when the API is called. Pulumi offers multiple ways of defining
the Lambda Function and it provisions the appropriate permissions so that API Gateway can communicate with it.

An easy way to define the Lambda Function, which mimics modern REST web application frameworks in style, is to
write the application code inline with the API Gateway definition itself. This example creates an AWS API Gateway
endpoint with a single API, listening at `/` for `GET` requests, which simply returns a `200 OK` for each call:

```typescript
import * as awsx from "@pulumi/awsx";

// Define a new GET endpoint that just returns a 200 and "hello" in the body.
const api = new awsx.apigateway.API("example", {
    routes: [{
        path: "/",
        method: "GET",
        eventHandler: async (event) => {
            // This code runs in an AWS Lambda anytime `/` is hit.
            return {
                statusCode: 200,
                body: "Hello, API Gateway!",
            };
        },
    }],
})

// Export the auto-generated API Gateway base URL.
export const url = api.url;
```

By running `pulumi up`, we will provision the API Gateway, its routes, and we'll get back the URL:

```bash
$ pulumi up -y
Updating (dev):

     Type                                Name                      Status
 +   pulumi:pulumi:Stack                 crosswalk-aws-dev         created
 +   └─ aws:apigateway:x:API             example                   created
 +      ├─ aws:iam:Role                  example4c238266           created
 +      ├─ aws:iam:RolePolicyAttachment  example4c238266-32be53a2  created
 +      ├─ aws:lambda:Function           example4c238266           created
 +      ├─ aws:apigateway:RestApi        example                   created
 +      ├─ aws:apigateway:Deployment     example                   created
 +      ├─ aws:lambda:Permission         example-fa520765          created
 +      └─ aws:apigateway:Stage          example                   created

Outputs:
    url: "https://no90ji5v23.execute-api.us-west-2.amazonaws.com/stage/"

Resources:
    + 9 created

Duration: 25s
```

We can `curl` the URL to see that it is up and running:

```bash
$ curl $(pulumi stack output url)
Hello, API Gateway!
```

This example uses Pulumi Crosswalk for AWS's built-in Lambda Function support. In this example, we are
specifying the code inline, and using the default Lambda property values. We can customize aspects of this
Function such as, for example, increasing the memory size available to our Function to 256MB:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Define a new GET endpoint that just returns a 200 and "hello" in the body.
const api = new awsx.apigateway.API("example", {
    routes: [{
        path: "/",
        method: "GET",
        eventHandler: new aws.lambda.CallbackFunction("get-handler", {
            memorySize: 256,
            callback: async (event) => {
                // This code runs in an AWS Lambda anytime `/` is hit.
                return {
                    statusCode: 200,
                    body: "Hello, API Gateway!",
                };
            },
        }),
    }],
})

// Export the auto-generated API Gateway base URL.
export const url = api.url;
```

In many cases, you might want to define your application logic in a different set of files than your
API Gateway infrastructure. Using modules lets you do this easily. For instance, we might have a subdirectory
named `app/` that contains a `routes.js` file:

```typescript
import * as awsx from "@pulumi/awsx";

// Define our routes, independent from the API Gateway itself.
export async function helloHandler(
        event: awsx.apigateway.Request): Promise<awsx.apigateway.Response> {
    return {
        statusCode: 200,
        body: "Hello, API Gateway!",
    };
}
```

Then for our API Gateway infrastructure definition we can simply write:

```typescript
import * as awsx from "@pulumi/awsx";
import * as routes from "./app/routes";

// Define a new GET endpoint that just returns a 200 and "hello" in the body.
const api = new awsx.apigateway.API("example", {
    routes: [{ path: "/", method: "GET", eventHandler: routes.helloHandler }],
})

// Export the auto-generated API Gateway base URL.
export const url = api.url;
```

If you prefer to keep your application and infrastructure code in entirely separate projects, you can define
Lambdas in the usual way and consume them from the AWS API Gateway resources. For instance, if you already have a
Lambda Function provisioned in AWS, you can reference it using `aws.lambda.Function.get`:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Define a new GET endpoint from an existing Lambda Function.
const api = new awsx.apigateway.API("example", {
    routes: [{
        path: "/",
        method: "GET",
        eventHandler: aws.lambda.Function.get("get-handler", "your_lambda_id"),
    }],
})

// Export the auto-generated API Gateway base URL.
export const url = api.url;
```

For more complete information about creating Lambda Functions, please
[see the Pulumi Crosswalk for AWS Lambda documentation]({{< prelref "lambda" >}}). Any of the techniques described may be used
in combination with the `awsx.apigateway.API` class.

### Defining a Static Route Served by S3

A Static Route serves static content from [S3](https://aws.amazon.com/s3/) at an API endpoint.

To ease population of the S3 bucket to serve from, and connecting it to the API Gateway, you specify the local path --
either a file or an entire directory -- and Pulumi will upload the contents as S3 objects.

Let's say we have a directory `www` containing a single `index.html` file:

```html
<h1>Hello, AWS API Gateway + S3!</h1>
```

The following program will create an AWS API Gateway that serves this content at the `/` URL:

```typescript
import * as awsx from "@pulumi/awsx";

// Define a GET endpoint that serves an entire directory of static content.
const api = new awsx.apigateway.API("example", {
    routes: [{
        path: "/",
        localPath: "www",
    }],
})

// Export the auto-generated API Gateway base URL.
export const url = api.url;
```

After running `pulumi up`, we can `curl` the resulting endpoint:

```bash
$ curl $(pulumi stack output url)
<h1>Hello, AWS API Gateway + S3!</h1>
```

By default, any index documents will be automatically served by S3 when directories are retrieved over HTTP (in the
manner [described here](https://docs.aws.amazon.com/AmazonS3/latest/dev/IndexDocumentSupport.html)). To suppress this
behavior, simply pass `index: false` as part of configuring your static route:

```typescript
import * as awsx from "@pulumi/awsx";

// Define a GET endpoint that serves an entire directory of static content.
const api = new awsx.apigateway.API("example", {
    routes: [{
        path: "/",
        localPath: "www",
        index: false,
    }],
})

// Export the auto-generated API Gateway base URL.
export const url = api.url;
```

After making this change, the earlier `curl` command will return a 404:

```bash
$ curl $(pulumi stack output url)
{ "message": "404 Not found" }
```

We must instead request the `index.html` document explicitly:

```bash
$ curl $(pulumi stack output url)/index.html
<h1>Hello, AWS API Gateway + S3!</h1>
```

Finally, the content type for all files in a path referencing a directory is inferred. If the local path instead
points to a single file, you can specify the content type explicitly with the `contentType` property.

### Defining an Integration Route

If neither of the above route types work for you, AWS API Gateway uses so-called _integrations_ to hook up an API
Gateway endpoint to backend services that will execute code in response to requests. The above examples use
integrations internally, even if it's not evident in the simple interface exposed.

Integrations give you full control over how HTTP requests are handled, and responses served, by an API Gateway
route. If you want more flexibility than the earlier methods, to proxy HTTP requests, to integrate with
AWS services other than Lambda Functions, or to mock your APIs, you can use an Integration Route simply by
specifying the `target` property on your route.

An Integration Route is a route that will map an endpoint to a specified backend. The supported types are:

* `aws`: This type of integration lets an API expose AWS service actions, such as invoking Amazon Lambda Functions,
  Amazon DynamoDB, Amazon Simple Notification Service, or Amazon Simple Queue Service. You must set up the
  necessary data mappings between the HTTP and underlying AWS service requests/responses.
* `aws_proxy`: This type of integration lets an API expose AWS service actions, much like `AWS`, and passes
  the HTTP request information, including request headers, URL path variables, query string parameters, and
  applicable body, directly to the underlying AWS service actions.
* `http`: This type of integration lets an API expose HTTP endpoints with custom integration requests and responses.
  You must set up necessary data mappings between the HTTP and integration requests/responses.
* `http_proxy`: This type of integration lets an API expose HTTP endpoints with a streamlined integration,
  without needing to perform custom data mappings as with the `HTTP` integration type.
* `mock`: This type of integration lets API Gateway return a response without sending a request further to
  the backend. This is useful for API testing without needing to configure any backend to service requests.

The following example sets up an `http_proxy` integration type that simply passes requests/responses directly
through to another endpoint, in this case `https://www.google.com`:

```typescript
import * as awsx from "@pulumi/awsx";

// Define a GET endpoint that proxies HTTP requests to https://www.google.com.
const api = new awsx.apigateway.API("example", {
    routes: [{
        path: "/google",
        target: {
            type: "http_proxy",
            uri: "https://www.google.com",
        },
    }],
});

// Export the auto-generated AWS API Gateway base URL.
export const url = api.url;
```

For more information AWS API Gateway Integrations, visit the
[AWS documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-integration-types.html).

### Defining an OpenAPI Specification for an Entire Endpoint

AWS API Gateway supports the [OpenAPI specification](https://swagger.io/docs/specification/about/) (formerly known as
"Swagger") for defining APIs. Using OpenAPI to define your APIs eases integration with other API authoring, modeling,
and testing tools, at some added complexity cost as you will need to understand the mechanics of how API Gateway
works and what HTTP headers it uses to accomplish its integrations.

To use an OpenAPI specification to initialize your API Gateway, supply an entire OpenAPI specification as a string
in the `swaggerString` property. For example, this API invokes an existing Lambda whose ID is `your_lambda_id`:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Look up an existing Lambda Function by ID, so that we can get its ARN. (If we knew the ARN ahead
// of time, this would not be necessary, we can just use it in the URI below.)
const handler = aws.lambda.Function.get("get-handler", "your_lambda_id");

// Define a GET endpoint that invokes our Lambda Function-based handler.
const api = new awsx.apigateway.API("example", {
    swaggerString: handler.arn.apply(arn => JSON.stringify({
        "swagger": "2.0",
        "info": {
            "title": "example",
            "version": "1.0",
        },
        "paths": {
            "/": {
                "get": {
                    "x-amazon-apigateway-integration": {
                        "httpMethod": "POST",
                        "passthroughBehavior": "when_no_match",
                        "type": "aws_proxy",
                        "uri": `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/${arn}/invocations`,
                    },
                },
            },
        },
        "x-amazon-apigateway-api-key-source": "HEADER",
        "x-amazon-apigateway-binary-media-types": [ "*/*" ],
        "x-amazon-apigateway-gateway-responses": {
            "ACCESS_DENIED": {
                "responseTemplates": {
                    "application/json": "{\"message\": \"404 Not found\" }",
                },
                "statusCode": 404,
            },
            "MISSING_AUTHENTICATION_TOKEN": {
                "responseTemplates": {
                    "application/json": "{\"message\": \"404 Not found\" }",
                },
                "statusCode": 404,
            },
        },
    })),
});

// Export the auto-generated AWS API Gateway base URL.
export const url = api.url;
```

This is more complex than the above examples, but this in an escape hatch that you can use to access any API
Gateway features not yet supported by the easier abstractions in Pulumi Crosswalk for AWS API Gateway. You must manually
provide permission for any route targets to be invoked by API Gateway when using this option.

For more information about AWS API Gateway's support for OpenAPI, including exporting specifications from existing
APIs for consumption from other tools, please see [Documenting a REST API in API Gateway](
https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html)

### Defining an OpenAPI Specification for a Single Route

Being able to provide an OpenAPI specification for an entire API Gateway lets you take matters into your own
hands if you need to access a feature not supported directly by `awsx.apigateway.API`. However, if you'd like to
define just a single API using OpenAPI, you can define a Raw Data Route, by supplying a `data` property.

The `data` property is just the `x-amazon-apigateway-integration` object, which can be seen in the above example.
The route's other parameters, such as its path and method, otherwise use the same approaches seen earlier.

For instance, the same API Gateway endpoint that invokes a Lambda Function can be authored as follows:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Look up an existing Lambda Function by ID, so that we can get its ARN. (If we knew the ARN ahead
// of time, this would not be necessary, we can just use it in the URI below.)
const handler = aws.lambda.Function.get("get-handler", "your_lambda_id");

// Define a GET endpoint that invokes our Lambda Function-based handler.
const api = new awsx.apigateway.API("example", {
    routes: [{
        path: "/",
        method: "GET",
        data: {
            "x-amazon-apigateway-integration": {
                "httpMethod": "POST",
                "passthroughBehavior": "when_no_match",
                "type": "aws_proxy",
                "uri": handler.arn.apply(arn =>
                    `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/${arn}/invocations`),
            },
        },
    }],
});

// Export the auto-generated AWS API Gateway base URL.
export const url = api.url;
```

For full details on what the OpenAPI integration object may contain, please refer to the full
[x-amazon-apigateway-integration Object documentation](
https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration.html).

## Performing AWS API Gateway Request Validation

API Gateway can perform basic validations against request parameters, a request payload or both. When a
validation fails, a 400 error is returned immediately, without invoking the backend integration, and the
validation results are published to the CloudWatch Logs, eliminating unnecessary calls to the backend.

For basic validation, API Gateway verifies either or both of these conditions:

* The required request parameters in the URI, query string, and headers of an incoming request are
  included and non-blank.
* The applicable request payload adheres to the configured JSON schema request model of the method.

When enabling validation, you will choose a validation scope, in addition to validation rules.

### Assigning Validators to APIs and Methods

Validators can be assigned for an entire API or at the individual method level, such as only for `POST` on a given
route. The validators defined at a method level override any validator set at the global API level.

To enable validation, pass the `requestValidator` property on the API object or individual route. The following
validator values are available:

* `"ALL"`: Validate both the request body and request parameters.
* `"BODY_ONLY"`: Validate only the request body.
* `"PARAMS_ONLY"`:  Validate only the request parameters.

For example, this enables parameter validation on all routes, and all validation on a specific route:

```typescript
import * as awsx from "@pulumi/awsx";

const api = new awsx.apigateway.API("example", {
    requestValidator: "PARAMS_ONLY",
    routes: [
        {
            // ...
            requestValidator: "ALL",
        },
        // ...
    ],
});
```

This enables validation already specified in the underlying models. The `awsx.apigateway.API` class also
supports mechanisms to specify the validation rules in the API Gateway configuration.

### Request Parameter Validation

To validate that a given request parameter is present in each request, use the `requiredParams` route property.
This is an array where each entry defines a different parameter. Each entry specifies the parameter `name` and where
it is expected to be found (`"path"`, `"query"`, or `"header"`), using the `in` property.

For example, this ensures that the `key` querystring parameter is present on all requests:

```typescript
import * as awsx from "@pulumi/awsx";

const api = new awsx.apigateway.API("example", {
    routes: [{
        // ...
        requestValidator: "PARAMS_ONLY",
        requiredParams: [{ name: "key", in: "query" }],
    }],
})
```

For additional information about request validation, please refer to [Enable Request Validation in AWS API Gateway](
https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html#api-gateway-request-validation-basic-definitions).

### Request Body Validation

> Request body validation is currently not supported. If you have a need for it, we would love to hear from you. Please
> comment on [this open issue](https://github.com/pulumi/pulumi-awsx/issues/198) with details about your use case.

## Controlling and Managing Access to APIs

AWS API Gateway supports several mechanisms for controlling and managing access to your APIs. This includes authentication
and authorization -- e.g., resource policies, standard AWS IAM roles and policies, Cognito user pools, and Lambda
authorizers -- other access control tasks -- e.g., cross-origin resource sharing (CORS), client-side SSL certificates,
and Amazon Web Application Firewall (WAF) -- and limiting access to authorized clients through usage plans and API keys.

The `awsx.apigateway.API` class supports three specific methods of controlling access to your APIs:

* *Amazon Cognito user pools* let you create customizable authentication and authorization for your APIs.
* *Lambda authorizers* are Lambda Functions that control access to your APIs based on HTTP information
  available in headers, paths, query strings, or other request information, including bearer tokens.
* *Usage plans* let you provide *API keys* to customers, and then track and limit usage of your APIs.

Details on each is below. For those not directly supported, all of these capabilities are accessible to you in the
[AWS package]({{< prelref "/docs/reference/pkg/aws" >}}), and are described in depth in the article
[Controlling and Managing Access to a REST API in AWS API Gateway](
https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html).

### Authorizing Requests using Cognito Authorizers

[Cognito Authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html)
allow you to use [Amazon Cognito User Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)
as an Authorizer for API Gateway. With a user pool, your users can sign into your web or mobile app through
Amazon Cognito directly, or through social identity providers like Facebook or Amazon, or even through SAML
identity providers. This enables your API Gateway to offload the difficult work of security to Cognito entirely.

To require users to sign in through Cognito, use the `awsx.apigateway.getCognitoAuthorizer` function to get a
configured Authorizer object, and supply it to the `authorizers` property on your route:

```typescript
import * as awsx from "@pulumi/awsx";

// Create an Amazon Cognito User Pool.
const cognitoUserPool = new aws.cognito.UserPool("pool");

// Create an API that requires authorizes against the User Pool.
const apiWithCognitoAuthorizer = new awsx.apigateway.API("cognito-protected-api", {
    routes: [{
        path: "/www_old",
        localPath: "www",
        authorizers: [
            awsx.apigateway.getCognitoAuthorizer({
                providerARNs: [ cognitoUserPool ],
            }),
        ],
    }],
});
```

This will require that a user authenticate, obtain an identity/access token, and call your API with said token.

### Authorizing Requests using Lambda Authorizers

[Lambda Authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)
are AWS Lambda Functions that control access to an API. This allows you to use information in the request itself,
including headers, paths, query parameters, or tokens, to decide whether a request is authorized to hit the backend.

You can define a Lambda Authorizer for an Event Handler Route or a Static Route. API Gateway supports `request` or
`token` type Lambda authorizers. A `token` Lambda Authorizer uses an authorization token (i.e. a header in the form
`Authorization: Token <token>`) to authorize the user, whereas a `request` Lambda Authorizer uses the request
parameters (i.e. headers, path parameter or query parameters).

To define an Authorizer, you provide a Lambda that fulfills
`aws.lambda.EventHandler<AuthorizerEvent, AuthorizerResponse>` or you provide information on a pre-existing Lambda
Authorizer. The example below shows defining the Authorizer Lambda directly inline. See
[Pulumi Crosswalk for AWS Lambda]({{< prelref "lambda" >}}) for other ways you can define your Lambda for the Authorizer.

#### Creating a Lambda-based Request Authorizer

Below is an example of a custom `request` Lambda Authorizer. This has access to all aspects of the request and can
make a decision based on whether to permit access based on any of it:

```typescript
import * as awsx from "@pulumi/awsx";

const api = new awsx.apigateway.API("myapi", {
    routes: [{
        path: "/b",
        method: "GET",
        eventHandler: async () => {
            return {
                statusCode: 200,
                body: "<h1>Hello world!</h1>",
            };
        },
        authorizers: [
            awsx.apigateway.getRequestLambdaAuthorizer({
                queryParameters: [ "auth" ],
                handler: async (event: awsx.apigateway.AuthorizerEvent) => {
                    // --- Add your own custom authorization logic here. ---
                    // Access the headers using event.headers, the query parameters using
                    // event.queryStringParameters or path parameters using event.pathParameters
                    return awsx.apigateway.authorizerResponse("user", "Deny", event.methodArn);
                },
            }),
        ],
    }],
});
```

This example denies the request unconditionally, but you can experiment with adding your own logic that
validates the request before letting it proceed. Instead of returning `"Deny"`, you should conditionally
return `"Allow"` for requests that pass the custom verification criteria.

The above example used `awsx.apigateway.getRequestLambdaAuthorizer` to simplify defining the authorizer. You can
instead define the authorizer by specifying all the property values explicitly:

```typescript
import * as awsx from "@pulumi/awsx";

const api = new awsx.apigateway.API("myapi", {
    routes: [{
        ...
        authorizers: [{
            authorizerName: "prettyAuthorizer",
            parameterName: "auth",
            parameterLocation: "query",
            authType: "custom",
            type: "request",
            handler: async (event: awsx.apigateway.AuthorizerEvent) => {
                // --- Add your own custom authorization logic here. ---
                return awsx.apigateway.authorizerResponse(
                    "user",
                    "Deny",
                    event.methodArn);
            },
            identitySource: [ "method.request.querystring.auth" ],
        }],
    }],
});
```

If you wish to reuse an Authorizer across multiple routes, you can declare it in a variable.

For additional information about request-based AWS API Gateway Lambda Authorizers, please see the
[AWS documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html).

#### Creating a Lambda-based Request Authorizer with an Existing Lambda

In the above examples, we created a new Lambda Function inline. Instead of writing a custom Lambda Authorizer, we can
use an existing Lambda elsewhere and then reference the required values. Or, if the function already exists, we can use
the `aws.lambda.Function.get` function to look up the Lambda resource and use it:

```typescript
import * as awsx from "@pulumi/awsx";

const apiWithAuthorizer = new awsx.apigateway.API("authorizer-api", {
    routes: [{
        ...
        authorizers: [{
            authorizerName: "testing",
            parameterName: "auth",
            parameterLocation: "query",
            authType: "custom",
            type: "request",
            handler: {
                // Use aws.lambda.Function.get to look up an existing Lambda Function. The library
                // will automatically fetch the invoke URI to pass to the Authorizer.
                uri: aws.lambda.Function.get("get-handler", "your_lambda_id"),
                credentials: gatewayRole.arn,
            },
            identitySource: [ "method.request.querystring.auth" ],
        }],
    }],
});
```

A complete example of defining the Lambda Authorizer elsewhere can be found [here](
https://github.com/pulumi/pulumi-awsx/blob/61d2996b8bdb20ea625e66e17ebbaa7b62f9c163/nodejs/awsx/examples/api/index.ts#L94-L152).

#### Creating a Lambda-based Token Authorizer

In many cases, we will want to base our authorization decision on the absence, presence, or validity of an
`Authorization: Token <token>` header instead, such as a JSON Web Token (JWT) or an OAuth token. To do that, we will
use the `token` type of Lambda Authorizer.

Below is an example of a custom `token` Lambda Authorizer that validates a request using such a token:

```typescript
import * as awsx from "@pulumi/awsx";

const api = new awsx.apigateway.API("myapi", {
    routes: [{
        path: "/b",
        method: "GET",
        eventHandler: async () => {
            return {
                statusCode: 200,
                body: "<h1>Hello world!</h1>",
            };
        },
        authorizers: [
            awsx.apigateway.getTokenLambdaAuthorizer({
                handler: async (event: awsx.apigateway.AuthorizerEvent) => {
                    // --- Add your own custom authorization logic here. ---
                    const token = event.authorizationToken;
                    if (token === "Allow") {
                        return awsx.apigateway.authorizerResponse("user", "Allow", event.methodArn);
                    }
                    return awsx.apigateway.authorizerResponse("user", "Deny", event.methodArn);
                },
            }),
        ],
    }],
});
```

In this case, our boolean condition `token === "Allow"` is meant for illustration and should be customized
to suit your own application.

The above example used `awsx.apigateway.getTokenLambdaAuthorizer` to simplify defining the authorizer. You can
instead define the authorizer by specifying all the property values explicitly:

```typescript
import * as awsx from "@pulumi/awsx";

const api = new awsx.apigateway.API("myapi", {
    routes: [{
        path: "/b",
        method: "GET",
        eventHandler: async () => {
            return {
                statusCode: 200,
                body: "<h1>Hello world!</h1>",
            };
        },
        authorizers: [{
            parameterName: "Authorization",
            parameterLocation: "header",
            authType: "oauth2",
            type: "request",
            handler: async (event: awsx.apigateway.AuthorizerEvent) => {
                // Add your own custom authorization logic here.
                 return awsx.apigateway.authorizerResponse("user", "Allow", event.methodArn);
            },
        }],
    }],
});
```

For additional information about token-based AWS API Gateway Lambda Authorizers, please see the
[AWS documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html).

#### Specifying Your Authorizer's IAM Role

If your Authorizer requires access to other AWS resources to make its authorization decisions, such as looking
up entries in a database, you will need to provision the appropriate role for your AWS Lambda Function.

Instead of using inline Lambda Functions, you can do this by using `new aws.lambda.CallbackFunction`:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const callbackRole = new aws.iam.Role("callbackRole", {
    // Specify appropriate AWS permissions here.
});

const callbackFxn = new aws.lambda.CallbackFunction("callbackFxn", {
    role: callbackRole,
    callback: async (event: awsx.apigateway.AuthorizerEvent) => {
        // --- Add custom authorization logic here. ---
        return awsx.apigateway.authorizerResponse("user", "Allow", event.methodArn);
    },
});

const api = new awsx.apigateway.API("myapi", {
    routes: [{
        path: "/b",
        method: "GET",
        eventHandler: async () => {
            return {
                statusCode: 200,
                body: "<h1>Hello world!</h1>",
            };
        },
        authorizers: [{
            parameterName: "Authorization",
            parameterLocation: "header",
            authType: "oauth2",
            type: "request",
            handler: callbackFxn,
        }],
    }],
});
```

For more information about creating and managing IAM Roles, please refer to the
[Pulumi Crosswalk for AWS IAM]({{< prelref "iam" >}}) documentation.

#### Generating Authorizer Responses Easily

A helper function `awsx.apigateway.authorizerResponse` has been created to simplify generating the authorizer
response. All of the above examples use it. This can be used when defining the authorizer handler as follows:

```typescript
import * as awsx from "@pulumi/awsx";

const api = new awsx.apigateway.API("myapi", {
    routes: [{
        ...
        authorizers: [{
            header: "Authorization",
            handler: async (event: awsx.apigateway.AuthorizerEvent) => {
                // Add your own custom authorization logic here.
                const token = event.authorizationToken;
                if (token === "Allow") {
                    return awsx.apigateway.authorizerResponse("user", "Allow", event.methodArn);
                }
                return awsx.apigateway.authorizerResponse("user", "Deny", event.methodArn);
            },
        }],
    }],
});
```

If you prefer, you can return the [AuthorizerResponse](
{{< prelref "/docs/reference/pkg/nodejs/pulumi/awsx/apigateway#Authorizer" >}}) data structure explicitly.

### Tracking and Limiting Requests with Usage Plans with API Keys

After you create, test, and deploy your APIs, you can use AWS API Gateway usage plans to make them available to your
customers. These usage plans and API keys allow customers to use your API at agreed-upon request rates and quotas
that meet their business requirements and budget constraints. If desired, you can set API-level throttling limits.

To require an API Key for an API Gateway route you set the `apiKeyRequired` property equal to `true`. At the API level,
you can choose if you want the API Key source to be `HEADER` (i.e. client includes a `x-api-key` header with the API
Key) or `AUTHORIZER` (i.e. a Lambda authorizer sends the API Key as part of the authorization response). If the API
Key source is not set, then the source will default to `HEADER`:

```typescript
import * as awsx from "@pulumi/awsx";

const api = new awsx.apigateway.API("myapi", {
    routes: [{
        path: "/a",
        method: "GET",
        eventHandler: async () => {
            return {
                statusCode: 200,
                body: "<h1>Hello world!</h1>",
            };
        },
        apiKeyRequired: true,
    }],
    apiKeySource: "AUTHORIZER",
});
```

You will also need to create a usage plan (`new aws.apigateway.UsagePlan`) and an API key (`new aws.apigateway.ApiKey`)
and then associate the key with the usage plan (`new aws.apigateway.UsagePlanKey`). To simplify the creation of API
Keys associated with your API you can use `awsx.apigateway.createAssociatedAPIKeys`, which create a Usage Plan, API
Keys and associates the API Keys by creating a UsagePlanKey. Below is an example of using this helper function:

```typescript
import * as awsx from "@pulumi/awsx";

const apikeys = awsx.apigateway.createAssociatedAPIKeys("my-api-keys", {
    apis: [api],
    apiKeys: [{
        name: "test-key",
    }],
});

 // Export the API Key if desired
export const apiKeyValue = apikeys.keys[0].apikey.value;
```

`awsx.apigateway.createAssociatedAPIKeys` will return an object that contains the Usage Plan, API Keys and Usage Plan
Keys. Instead of providing the APIs, you can also specify the api stages for the Usage Plan as follows:

```ts
import * as awsx from "@pulumi/awsx";

const apikeys = awsx.apigateway.createAssociatedAPIKeys("my-api-keys", {
    usagePlan: {
        apiStages: [{
            apiId: api.restAPI.id,
            stage: api.stage.stageName,
        }],
    },
    apiKeys: [{
        name: "test-key",
    }],
});
```

For more information about Usage Plans and API Keys, refer to
[Create and Use Usage Plans with API Keys](
https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html).

## Configuring AWS API Gateway Custom Domains and SSL using Route53 and ACM

AWS API Gateway will automatically provision and assign a domain name, URL that contains the stage, and SSL
support. It will look something like `https://no90ji5v23.execute-api.us-west-2.amazonaws.com/stage/`. The host
portion of the URL refers to an API endpoint which can be edge-optimized or regional.

Although it's a great convenience to have a URL automatically created with SSL support that just works right
away, the resulting URL isn't user-friendly or very easy to remember, and may not be suitable for business
scenarios that require using company domains. To provide a simpler and more intuitive URL for your API users,
you can configure a custom domain name (e.g., `api.acmecorp.com`) as the API's host name, and customize the
base path of the URL to map to an alternative URL (e.g., one that does not include the `/stage` at the end).

For example, we may map `https://no90ji5v23.execute-api.us-west-2.amazonaws.com/stage/` instead to
`https://api.acmecorp.com/web-ordering`. In doing so, API Gateway will also set up an edge-optimized
[Amazon CloudFront Content Distribution Network (CDN)](https://aws.amazon.com/cloudfront/).

We now will walk through the various steps required to set this up.

First, we provision an `awsx.apigateway.API` in any of the ways we've seen above. We'll use something simple:

```typescript
import * as awsx from "@pulumi/awsx";

// Define a new GET endpoint that just returns a 200 and "hello" in the body.
const api = new awsx.apigateway.API("example", {
    routes: [{
        path: "/",
        method: "GET",
        eventHandler: async (event) => {
            // This code runs in an AWS Lambda anytime `/` is hit.
            return {
                statusCode: 200,
                body: "Hello, API Gateway!",
            };
        },
    }],
})
```

Let us assume we are hard-coding the domain name (although Pulumi's configuration system can be used instead):

```typescript
const domain = "acmecorp.com";
```

Although API Gateway will create a regional domain name for our API, we must now explicitly configure a DNS
zone and record to map the custom domain name to the regional domain name for API requests. For this example,
we will use [Amazon Route53's Domain Name System (DNS) Service](https://aws.amazon.com/route53/) for this task.

Add the creation of a Route53 DNS zone:

```typescript
// Create a DNS zone for our custom domain.
const webDnsZone = new aws.route53.Zone("webDnsZone", {
    name: domain,
});
```

Next we will provision an SSL/TLS certificate to use for our custom domain name. We will use
[AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) to generate
a new certificate. We could instead import one into ACM that has been issued by a third-party certificate authority.
Note that we must create this certificate in the `us-east-1` (Northern Virginia) region, per AWS rules.

```typescript
// Provision an SSL certificate to enable SSL -- ensuring to do so in us-east-1.
const awsUsEast1 = new aws.Provider("usEast1", { region: "us-east-1" });
const sslCert = new aws.acm.Certificate("sslCert", {
    domainName: domain,
    validationMethod: "DNS",
}, { provider: awsUsEast1 });

// Create the necessary DNS records for ACM to validate ownership, and wait for it.
const sslCertValidationRecord = new aws.route53.Record("sslCertValidationRecord", {
    zoneId: webDnsZone.id,
    name: sslCert.domainValidationOptions[0].resourceRecordName,
    type: sslCert.domainValidationOptions[0].resourceRecordType,
    records: [ sslCert.domainValidationOptions[0].resourceRecordValue ],
    ttl: 10 * 60 /* 10 minutes */,
});
const sslCertValidationIssued = new aws.acm.CertificateValidation("sslCertValidationIssued", {
    certificateArn: sslCert.arn,
    validationRecordFqdns: [ sslCertValidationRecord.fqdn ],
}, { provider: awsUsEast1 });
```

This code snippet not only provisions the certificate, but also uses DNS validation to eliminate any manual
steps, and to wait until the certificate is ready.

After this, we will direct API Gateway to use our new domain and a different base path than `stage/`. Without
such a mapping, API requests bound for the custom domain name cannot reach our API Gateway.

```typescript
// Configure an edge-optimized domain for our API Gateway. This will configure a Cloudfront CDN
// distribution behind the scenes and serve our API Gateway at a custom domain name over SSL.
const webDomain = new aws.apigateway.DomainName("webCdn", {
    certificateArn: sslCertValidationIssued.certificateArn,
    domainName: domain,
});
const webDomainMapping = new aws.apigateway.BasePathMapping("webDomainMapping", {
    restApi: web.restAPI,
    stageName: web.stage.stageName,
    domainName: webDomain.id,
});
```

There is one step remaining, which is to create the A record in our DNS zone that allows external traffic
to reach out new custom domain. After doing so, our AWS API Gateway will be reachable at our custom URL.

```typescript
// Finally create an A record for our domain that directs to our custom domain.
const webDnsRecord = new aws.route53.Record("webDnsRecord", {
    name: webDomain.domainName,
    type: "A",
    zoneId: webDnsZone.id,
    aliases: [{
        evaluateTargetHealth: true,
        name: webDomain.cloudfrontDomainName,
        zoneId: webDomain.cloudfrontZoneId,
    }],
}, { dependsOn: sslCertValidationIssued });
```

For more information about the options and levels of customizability available for edge-optimized AWS API Gateways
and custom domains, please refer to [Set up Custom Domain Name for an API in API Gateway](
https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

## Additional API Gateway Resources

For more details about AWS API Gateway and REST APIs, see the following resources:

* [Use AWS API Gateway to Create REST APIs](
  https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-overview-developer-experience.html#api-gateway-overview-rest)
