---
title_tag: "Configuring AWS API Gateway | Crosswalk"
title: Configuring AWS API Gateway
meta_desc: Pulumi Crosswalk for AWS provides a significantly easier way of programming API Gateway. Here is how.
linktitle: API Gateway
menu:
  userguides:
    parent: crosswalk-aws
    weight: 1

aliases: ["/docs/reference/crosswalk/aws/api-gateway/"]
---

<a href="./">
<img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[AWS API Gateway](https://aws.amazon.com/api-gateway/) is a fully managed service for creating, monitoring, and
securing APIs at scale. It acts as a "front door" for REST and WebSocket applications that use backend services,
and handles all the tasks necessary to accept and process up to hundreds of thousands of concurrent API calls,
including traffic management, authorization and access control, monitoring, and API version management. API Gateway
is inexpensive, has no minimum fees, and you only pay for the API calls you receive and the data transferred out.

## Overview

Pulumi Crosswalk for Amazon Web Services (AWS) provides better AWS API management through significantly easier
ways of programming an API Gateway. This includes using infrastructure as code techniques for simple, declarative
APIs, including easy Lambda integration.

Full examples can be found in the [AWS API Gateway component](https://www.pulumi.com/registry/packages/aws-apigateway/) in the Pulumi Registry.

## Create and Configure Routes

AWS API Gateway creates REST APIs that:

- Are HTTP based.
- Adhere to the [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) protocol.
- Implement standard HTTP methods such as `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`.

Each API Gateway instance defines a new API endpoint and a collection of API routes, each of which has a distinct URL.

{{% notes type="info" %}}

Internally the API Gateway resource uses a collection of supporting objects, like resources, methods, and more,
however one of the benefits of Pulumi Crosswalk for AWS is that it hides these mechanics behind a simpler interface.

{{% /notes %}}

Each API Gateway deployment is associated with a _stage_. A stage is a version of your API, such
as `stage`, `prod`, `v1`, or `v2`. For simple APIs, you will likely just have one. You can always define a custom
stage name, but if you leave it off, a default of `stage` will be chosen.

API Gateway will auto-generate a domain name with built-in HTTPS support. The stage name will also be part of this URL.
We will see later how to assign a custom domain, SSL certificate, and/or eliminate the stage name from the URL.

There are multiple ways to define APIs using Pulumi Crosswalk for AWS:

- [Lambda Function Event Handler Route](#defining-a-lambda-function-event-handler-route)
- [Static Route Served by S3](#defining-a-static-route-served-by-s3)
- [Integration Route](#defining-an-integration-route)
- [OpenAPI Specification for an Entire Endpoint](#defining-an-openapi-specification-for-an-entire-endpoint)
- [OpenAPI Specification for a Single Route](#defining-an-openapi-specification-for-a-single-route)

Multiple endpoints on the same API Gateway can be defined using a combination of these techniques.

### Lambda Request Handling

An Event Handler Route is an API that will map to a [Lambda Function](https://aws.amazon.com/lambda/). You will specify
the path, HTTP method, and the Lambda Function to invoke when the API is called. Pulumi offers multiple ways of defining
the Lambda Function and it provisions the appropriate permissions so that API Gateway can communicate with it.

This example creates an AWS API Gateway endpoint with a single API, listening at `/` for `GET` requests, which returns a `200 OK` for each call.

The path can be parameterized to match specific patterns:

- A literal pattern e.g. `/pets` will only match `/pets`
- A parameterized pattern e.g. `/pets/{petId}` will match child routes such as `/pet/6sxz2j`
- A wildcard pattern specified with `{proxy+}` e.g. `/parent/{proxy+}` will mach all decendant paths such as `/parent/child/grandchild`

For more complete information about creating Lambda Functions, see the [Pulumi Crosswalk for AWS Lambda documentation](/docs/guides/crosswalk/aws/lambda/).

{{< chooser language "typescript,python,go" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as aws from "@pulumi/aws";
import * as apigateway from "@pulumi/aws-apigateway";

// Create a Lambda Function
const helloHandler = new aws.lambda.CallbackFunction("hello-handler", {
  callback: async (ev, ctx) => {
    return {
      statusCode: 200,
      body: "Hello, API Gateway!",
    };
  },
});

// Define an endpoint that invokes a lambda to handle requests
const api = new apigateway.RestAPI("api", {
  routes: [
    {
      path: "/",
      method: "GET",
      eventHandler: helloHandler,
    },
  ],
});

export const url = api.url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_aws_apigateway as apigateway

# Create a Lambda Function
# helloHandler = aws.lambda_.Function(...)

# Define an endpoint that invokes a lambda to handle requests
api = apigateway.RestAPI('api', routes=[
    apigateway.RouteArgs(path="/", method="GET", event_handler=helloHandler),
])

pulumi.export('url', api.url)
```

Create the Lambda handler:

```python
def handler(event, context):
    print(event)
    return {
        "statusCode": 200,
        "body": "Hello, API Gateway!",
    }
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Create a Lambda Function
// helloHandler, err := lambda.NewFunction(...)

// Define an endpoint that invokes a lambda to handle requests
getMethod := apigateway.MethodGET
restAPI, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
    Routes: []apigateway.RouteArgs{
        {
            Path:         "/",
            Method:       &getMethod,
            EventHandler: helloHandler,
        },
    },
})

ctx.Export("url", restAPI.Url)
```

Create the Lambda handler:

```go
package main

import (
    "github.com/aws/aws-lambda-go/events"
    "github.com/aws/aws-lambda-go/lambda"
)

func handler(request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
    return events.APIGatewayProxyResponse{
        StatusCode: 200,
        Body:       "Hello, API Gateway!",
    }, nil
}

func main() {
    lambda.Start(handler)
}
```

{{% /choosable %}}

By running `pulumi up`, we will provision the API Gateway, its routes, and we'll get back the URL:

```bash
$ pulumi up -y
Updating (dev):

     Type                                Name                    Status
 +   pulumi:pulumi:Stack                 simple-dev              created
 +   ├─ aws:iam:Role                     hello-handler           created
 +   ├─ aws:lambda:Function              hello-handler           created
 +   ├─ aws:iam:RolePolicyAttachment     hello-handler-019020e7  created
 +   ├─ aws:iam:RolePolicyAttachment     hello-handler-74d12784  created
 +   ├─ aws:iam:RolePolicyAttachment     hello-handler-7cd09230  created
 +   ├─ aws:iam:RolePolicyAttachment     hello-handler-b5aeb6b6  created
 +   ├─ aws:iam:RolePolicyAttachment     hello-handler-4aaabb8e  created
 +   ├─ aws:iam:RolePolicyAttachment     hello-handler-1b4caae3  created
 +   ├─ aws:iam:RolePolicyAttachment     hello-handler-e1a3786d  created
 +   ├─ aws:iam:RolePolicyAttachment     hello-handler-a1de8170  created
 +   ├─ aws:iam:RolePolicyAttachment     hello-handler-6c156834  created
 +   └─ apigateway:index:RestAPI         api                     created
 +      └─ aws:apigateway:x:API          api                     created
 +         ├─ aws:apigateway:RestApi     api                     created
 +         ├─ aws:apigateway:Deployment  api                     created
 +         ├─ aws:lambda:Permission      api-fa520765            created
 +         └─ aws:apigateway:Stage       api                     created

Outputs:
    url: "https://no90ji5v23.execute-api.us-west-2.amazonaws.com/stage/"

Resources:
    + 18 created

Duration: 25s
```

We can `curl` the URL to see that it is up and running:

```bash
$ curl $(pulumi stack output url)
Hello, API Gateway!
```

### Static File Serving with S3

A Static Route serves static content from [S3](https://aws.amazon.com/s3/) at an API endpoint.

With the API Gateway component, you specify a local path (either a file or an entire directory) and we will manage the creation of the S3 bucket and the synchronisation of the files to S3 objects.

If we have a directory `www` containing a `index.html` file:

```html
<h1>Hello, AWS API Gateway + S3!</h1>
```

The following program will create an AWS API Gateway that serves this content at the `/` URL:

{{< chooser language "typescript,python,go" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
// Define an endpoint that serves an entire directory of static content.
const api = new apigateway.RestAPI("api", {
  routes: [
    {
      path: "/",
      localPath: "www",
    },
  ],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Define an endpoint that serves an entire directory of static content.
api = apigateway.RestAPI('api', routes=[
    apigateway.RouteArgs(path="/", local_path="www"),
])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Define an endpoint that serves an entire directory of static content.
localPath := "www"
restAPI, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
    Routes: []apigateway.RouteArgs{
        {
            Path:      "/",
            LocalPath: &localPath,
        },
    },
})
```

{{% /choosable %}}

After running `pulumi up`, we can `curl` the resulting endpoint:

```bash
$ curl $(pulumi stack output url)
<h1>Hello, AWS API Gateway + S3!</h1>
```

By default, any index documents will be automatically served by S3 when directories are retrieved over HTTP.
(See [AWS: Configuring an Index Document](https://docs.aws.amazon.com/AmazonS3/latest/dev/IndexDocumentSupport.html).)
To suppress this behavior in the static route, set the `index` to `false` as part of configuring your static route.
Alternatively, to use a different default document name, set `index` to a string containing the file name e.g. `default.html`.

If the local path points to a directory, the route will automatically be created as a proxy path (i.e. `/{proxy+}`) to match
all sub-directories and the content type for all files will be inferred automatically. If the local path points to a single
file you can specify the content type explicitly with the `contentType` property.

### Integration Routes

If neither of the above route types work for you, [AWS API Gateway integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-integration-types.html) connect an API
Gateway endpoint to backend services that will execute code in response to requests. The previous lambda and
static examples use integrations internally, even if it's not evident in the simple interface exposed.

Integrations give you full control over how HTTP requests are handled, and responses served, by an API Gateway
route. If you want more flexibility than the earlier methods, to proxy HTTP requests, to integrate with
AWS services other than Lambda Functions, or to mock your APIs, you can use an Integration Route by
specifying the `target` property on your route.

An Integration Route is a route that will map an endpoint to a specified backend. The supported types are:

- `aws`: This type of integration lets an API expose AWS service actions, such as invoking Amazon Lambda Functions,
  Amazon DynamoDB, Amazon Simple Notification Service, or Amazon Simple Queue Service. You must set up the
  necessary data mappings between the HTTP and underlying AWS service requests/responses.
- `aws_proxy`: This type of integration lets an API expose AWS service actions, much like `AWS`, and passes
  the HTTP request information, including request headers, URL path variables, query string parameters, and
  applicable body, directly to the underlying AWS service actions.
- `http`: This type of integration lets an API expose HTTP endpoints with custom integration requests and responses.
  You must set up necessary data mappings between the HTTP and integration requests/responses.
- `http_proxy`: This type of integration lets an API expose HTTP endpoints with a streamlined integration,
  without needing to perform custom data mappings as with the `HTTP` integration type.
- `mock`: This type of integration lets API Gateway return a response without sending a request further to
  the backend. This is useful for API testing without needing to configure any backend to service requests.

The following example sets up an `http_proxy` integration type that passes requests/responses directly
through to another endpoint, in this case `https://www.google.com`:

{{< chooser language "typescript,python,go" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
// Define an endpoint that proxies HTTP requests to https://www.google.com.
const api = new apigateway.RestAPI("api", {
  routes: [
    {
      path: "/",
      target: {
        type: "http_proxy",
        uri: "https://www.google.com",
      },
    },
  ],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Define an endpoint that proxies HTTP requests to https://www.google.com.
api = apigateway.RestAPI('api', routes=[
    apigateway.RouteArgs(path="/integration", target=apigateway.TargetArgs(uri="https://www.google.com", type="http_proxy"))
])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Define an endpoint that proxies HTTP requests to https://www.google.com.
getMethod := apigateway.MethodGET
restAPI, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
    Routes: []apigateway.RouteArgs{
        {
            Path:   "/",
            Method: &getMethod,
            Target: apigateway.TargetArgs{
                Type: apigateway.IntegrationType_Http_proxy,
                Uri:  pulumi.String("https://www.google.com"),
            },
        },
    },
})
```

{{% /choosable %}}

## Controlling Access to APIs

AWS API Gateway supports several mechanisms for controlling and managing access to your APIs. This includes authentication
and authorization -- e.g., resource policies, standard AWS IAM roles and policies, Cognito user pools, and Lambda
authorizers -- other access control tasks -- e.g., cross-origin resource sharing (CORS), client-side SSL certificates,
and Amazon Web Application Firewall (WAF) -- and limiting access to authorized clients through usage plans and API keys.

The API Gateway `RestAPI` class supports three specific methods of controlling access to your APIs:

- _Amazon Cognito user pools_ let you create customizable authentication and authorization for your APIs.
- _Lambda authorizers_ are Lambda Functions that control access to your APIs based on HTTP information
  available in headers, paths, query strings, or other request information, including bearer tokens.
- _Usage plans_ let you provide _API keys_ to customers, and then track and limit usage of your APIs.

Details on each is below. For those not directly supported, all of these capabilities are accessible to you in the
[AWS package](/registry/packages/aws/api-docs/), and are described in depth in the article
[Controlling and Managing Access to a REST API in AWS API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html).

### Cognito Authorizers

[Cognito Authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html)
allow you to use [Amazon Cognito User Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)
as an Authorizer for API Gateway. With a user pool, your users can sign into your web or mobile app through
Amazon Cognito directly, or through social identity providers like Facebook or Amazon, or even through SAML
identity providers. This enables your API Gateway to offload the difficult work of security to Cognito entirely.

To require users to sign in through Cognito, you must specify the source of the authorization token (normally the `Authorization` header) and specify the ARN of the Cognito User Pool.

{{< chooser language "typescript,python,go" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
// Create a user pool to contain authorized users of the API
const userPool = new aws.cognito.UserPool("user-pool");

const api = new apigateway.RestAPI("api", {
  routes: [
    {
      path: "/",
      localPath: "www",
      // Define an authorizer which uses Cognito to validate the token from the Authorization header
      authorizers: [
        {
          parameterName: "Authorization",
          identitySource: ["method.request.header.Authorization"],
          providerARNs: [userPool.arn],
        },
      ],
    },
  ],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Create a user pool to contain authorized users of the API
userPool = aws.cognito.UserPool("user-pool")

# Define an endpoint that serves an entire directory of static content.
api = apigateway.RestAPI("api", routes=[
    apigateway.RouteArgs(
        path="/",
        local_path="www",
        authorizers=[apigateway.AuthorizerArgs(
            parameter_name="Authorization",
            identity_source=["method.request.header.Authorization"],
            provider_arns=[userPool.arn]
        )]
    ),
])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Create a user pool to contain authorized users of the API
userPool, err := cognito.NewUserPool(ctx, "user-pool", &cognito.UserPoolArgs{})

localPath := "www"
restAPI, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
    Routes: []apigateway.RouteArgs{
        {
            Path:      "/",
            LocalPath: &localPath,
            // Define an authorizer which uses Cognito to validate the token from the Authorization header
            Authorizers: []apigateway.AuthorizerArgs{
                {
                    ParameterName:  "Authorization",
                    IdentitySource: []string{"method.request.header.Authorization"},
                    ProviderARNs:   []pulumi.StringInput{userPool.Arn},
                },
            },
        },
    },
})
```

{{% /choosable %}}

This will require that a user authenticate, obtain an identity/access token, and call your API with said token.

### Lambda Authorizers

[Lambda Authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)
are AWS Lambda Functions that control access to an API. This allows you to use information in the request itself,
including headers, paths, query parameters, or tokens, to decide whether a request is authorized to hit the backend.

You can define a Lambda Authorizer for an Event Handler Route or a Static Route. API Gateway supports `request` or
`token` type Lambda authorizers:

- `token` authorizer uses an authorization token (i.e. a header in the form `Authorization: Token <token>`)
- `request` authorizer uses any part of the request parameters (i.e. headers, path parameter or query parameters).

To define an Authorizer, you provide a Lambda that recieves an
[Authorizer Event](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-input.html)
and responds with a valid [Authorizer Response](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-output.html).
See [Pulumi Crosswalk for AWS Lambda](/docs/guides/crosswalk/aws/lambda/) for other ways you can define your Lambda for the Authorizer.

#### Lambda Request Authorizer

Below is an example of a custom `request` Lambda Authorizer. This has access to all aspects of the request and can
make a decision based on whether to permit access based on any of it:

For the purpose of demonstration, the authorizer only allows a single, hard-coded token. In practice this lambda
would normally reach out to another service to validate the authorisation.

If you wish to reuse an Authorizer across multiple routes, you can declare it in a variable.

{{< chooser language "typescript,python,go" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
// Define the authorizer lambder handler
const authLambda = new aws.lambda.CallbackFunction("auth", {
  callback: async (event, context) => {
    // --- Add your own custom authorization logic here. ---
    const effect =
      event.headers?.Authorization === "goodToken" ? "Allow" : "Deny";
    return {
      principalId: "my-user",
      policyDocument: {
        Version: "2012-10-17",
        Statement: [
          {
            Action: "execute-api:Invoke",
            Effect: effect,
            Resource: event.methodArn,
          },
        ],
      },
    };
  },
});

const api = new apigateway.RestAPI("api", {
  routes: [
    {
      path: "/",
      localPath: "www",
      // Define a request authorizer which uses Lambda to validate the token from the Authorization header
      authorizers: [
        {
          authType: "custom",
          parameterName: "Authorization",
          type: "request",
          identitySource: ["method.request.header.Authorization"],
          // Delegate to the Lambda function defined above
          handler: authLambda,
        },
      ],
    },
  ],
});

export const url = api.url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Create Lambda using the handler below
# authLambda = aws.lambda_.Function(...)

# Define an endpoint that invokes a lambda to handle requests
api = apigateway.RestAPI('api', routes=[
    apigateway.RouteArgs(path="/", method="GET", local_path="www",
                         # Define a request authorizer which uses Lambda to validate the token from the Authorization header
                         authorizers=[apigateway.AuthorizerArgs(
                             auth_type="custom",
                             parameter_name="Authorization",
                             type="request",
                             identity_source=[
                                 "method.request.header.Authorization"],
                             # Delegate to the Lambda function defined above
                             handler=authLambda
                         )]),
])
```

Define the authorizer lambder handler:

```python
def handler(event, context):
    return {
        "principalId": "my-user",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [{
                "Action": "execute-api:Invoke",
                # --- Add your own custom authorization logic here. ---
                "Effect": "Allow" if event["headers"]["Authorization"] == "goodToken" else "Deny",
                "Resource": event["methodArn"],
            }]
        },
    }
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Create lambda role and policies
// authLambda, err := lambda.NewFunction(...)

localPath := "www"
authType := "custom"
authorizerType := "request"
restAPI, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
  Routes: []apigateway.RouteArgs{
    {
      Path:      "/",
      LocalPath: &localPath,
      // Define a request authorizer which uses Lambda to validate the token from the Authorization header
      Authorizers: []apigateway.AuthorizerArgs{
        {
          AuthType:       &authType,
          ParameterName:  "Authorization",
          Type:           &authorizerType,
          IdentitySource: []string{"method.request.header.Authorization"},
          // Delegate to the Lambda function defined above
          Handler:        authLambda,
        },
      },
    },
  },
})
```

Define the authorizer lambder handler:

```go
package main

import (
  "github.com/aws/aws-lambda-go/events"
  "github.com/aws/aws-lambda-go/lambda"
)

func handler(request events.APIGatewayCustomAuthorizerRequestTypeRequest) (events.APIGatewayCustomAuthorizerResponse, error) {
  var effect string
  if request.Headers["Authorization"] == "goodToken" {
    effect = "Allow"
  } else {
    effect = "Deny"
  }
  return events.APIGatewayCustomAuthorizerResponse{
    PrincipalID: "my-user",
    PolicyDocument: events.APIGatewayCustomAuthorizerPolicy{
      Version: "2012-10-17",
      Statement: []events.IAMPolicyStatement{
        {
          Action:   []string{"execute-api:Invoke"},
          Effect:   effect,
          Resource: []string{request.MethodArn},
        },
      },
    },
  }, nil
}

func main() {
  lambda.Start(handler)
}
```

{{% /choosable %}}

Instead of using a _request_ authorizer, there is also a _token_ authorizer passes only the token rather than the whole
request object to the Lambda function to validate.

For additional information about request-based AWS API Gateway Lambda Authorizers, see the
[AWS documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html).

## Request Validation

API Gateway can perform basic validations against request parameters, a request payload or both. When a
validation fails, a 400 error is returned immediately, without invoking the backend integration, and the
validation results are published to the CloudWatch Logs, eliminating unnecessary calls to the backend.

For basic validation, API Gateway verifies either or both of these conditions:

- The required request parameters in the URI, query string, and headers of an incoming request are
  included and non-blank.
- The applicable request payload adheres to the configured JSON schema request model of the method.

When enabling validation, you will choose a validation scope, in addition to validation rules.

### Assigning Validators to APIs and Methods

Validators can be assigned for an entire API or at the individual method level, such as only for `POST` on a given
route. The validators defined at a method level override any validator set at the global API level.

To enable validation, pass the `requestValidator` property on the API object or individual route. The following
validator values are available:

- `"ALL"`: Validate both the request body and request parameters.
- `"BODY_ONLY"`: Validate only the request body.
- `"PARAMS_ONLY"`: Validate only the request parameters.

For example, this enables parameter validation on all routes, and all validation on a specific route:

{{< chooser language "typescript,python,go" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const api = new apigateway.RestAPI("api", {
  requestValidator: "PARAMS_ONLY",
  routes: [
    {
      // ...
      requestValidator: "ALL",
    },
  ],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
api = apigateway.RestAPI('api',
                         request_validator="PARAMS_ONLY",
                         routes=[
                             apigateway.RouteArgs(
                                 # ...
                                 request_validator="ALL"),
                         ])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
paramsOnly := apigateway.RequestValidator_PARAMS_ONLY
requestValidatorALL := apigateway.RequestValidatorALL
restAPI, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
    RequestValidator: &paramsOnly,
    Routes: []apigateway.RouteArgs{
      {
        // ...
        RequestValidator: &requestValidatorALL,
      },
  },
})
```

{{% /choosable %}}

This enables validation already specified in the underlying models. The `awsx.apigateway.API` class also
supports mechanisms to specify the validation rules in the API Gateway configuration.

### Request Parameter Validation

To validate that a given request parameter is present in each request, use the `requiredParams` route property.
This is an array where each entry defines a different parameter. Each entry specifies the parameter `name` and where
it is expected to be found (`"path"`, `"query"`, or `"header"`), using the `in` property.

For example, this ensures that the `key` querystring parameter is present on all requests:

{{< chooser language "typescript,python,go" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const api = new apigateway.RestAPI("api", {
    routes: [
        {
            // ...
            requestValidator: "PARAMS_ONLY",
            requiredParameters: [{ name: "key", in: "query" }],
        },
```

{{% /choosable %}}

{{% choosable language python %}}

```python
api = apigateway.RestAPI('api', routes=[
    # Serve an entire directory of static content
    apigateway.RouteArgs(
        # ...
        request_validator="ALL",
        required_parameters=[apigateway.RequiredParameterArgs(name="key", in_="query")]),
])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
requestValidatorALL := apigateway.RequestValidatorALL
restAPI, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
  Routes: []apigateway.RouteArgs{
    {
      // ...
      RequestValidator: &requestValidatorALL,
      RequiredParameters: []apigateway.RequiredParameterArgs{
        {
          Name: pulumi.StringPtr("key"),
          In:   pulumi.StringPtr("query"),
        },
      },
    },
  })
```

{{% /choosable %}}

For additional information about request validation, refer to [Enable Request Validation in AWS API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html#api-gateway-request-validation-basic-definitions).

{{% notes type="info" %}}

Request body validation is currently not supported. If you have a need for it, we would love to hear from you.
Comment on [this open issue](https://github.com/pulumi/pulumi-aws-apigateway/issues/36) with details about your use case.

{{% /notes %}}

### Use API Keys to Limit Requests

After you create, test, and deploy your APIs, you can use AWS API Gateway usage plans to make them available to your
customers. These usage plans and API keys allow customers to use your API at agreed-upon request rates and quotas
that meet their business requirements and budget constraints. If desired, you can set API-level throttling limits.

To require an API Key for an API Gateway route you set the "api key required" property to true. At the API level,
you can choose if you want the API Key source to be `HEADER` (i.e. client includes a `x-api-key` header with the API
Key) or `AUTHORIZER` (i.e. a Lambda authorizer sends the API Key as part of the authorization response). If the API
Key source is not set, then the source will default to `HEADER`.

Here's an example how to configure the API and routes to use API Keys:

{{< chooser language "typescript,python,go" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const api = new apigateway.RestAPI("api", {
    routes: [
        {
            // ...
            apiKeyRequired: true,
        }
    ],
    apiKeySource: "AUTHORIZER",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
api = apigateway.RestAPI('api', api_key_source="AUTHORIZER", routes=[
    apigateway.RouteArgs(# ...
                         api_key_required=True)
])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
apiKeyRequired := true
authorizer := apigateway.APIKeySourceAUTHORIZER
restAPI, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
  ApiKeySource: &authorizer,
  Routes: []apigateway.RouteArgs{
    {
      // ...
      ApiKeyRequired: &apiKeyRequired,
    },
  },
})
```

{{% /choosable %}}

There's 3 steps to configure API Keys for the API:

1. Create the API Key (i.e. for a customer)
2. Create a usage plan for the API (which can optionally define quotas and throttles)
3. Associate the key to the usage plan.

Below is an example of using creating these components:

{{< chooser language "typescript,python,go" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
// Create an API key to manage usage
const apiKey = new aws.apigateway.ApiKey("api-key");
// Define usage plan for an API stage
const usagePlan = new aws.apigateway.UsagePlan("usage-plan", {
    apiStages: [{
        apiId: api.api.id,
        stage: api.stage.stageName,
        // throttles: [{ path: "/path/GET", rateLimit: 1 }]
    }],
    // quotaSettings: {...},
    // throttleSettings: {...},
});
// Associate the key to the plan
new aws.apigateway.UsagePlanKey("usage-plan-key", {
    keyId: apiKey.id,
    keyType: "API_KEY",
    usagePlanId: usagePlan.id,
});

export const apiKeyValue = apiKey.value;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Create an API key to manage usage
api_key = aws.apigateway.ApiKey("api-key")
# Define usage plan for an API stage
usage_plan = aws.apigateway.UsagePlan("usage-plan",
                                      api_stages=[aws.apigateway.UsagePlanApiStageArgs(
                                          api_id=api.api.id,
                                          stage=api.stage.stage_name)])
# Associate the key to the plan
aws.apigateway.UsagePlanKey('usage-plan-key',
                            key_id=api_key.id,
                            key_type="API_KEY",
                            usage_plan_id=usage_plan.id)

pulumi.export('api-key-value', api_key.value)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Create an API key to manage usage
apiKey, err := awsapigateway.NewApiKey(ctx, "api-key", &awsapigateway.ApiKeyArgs{})
if err != nil {
  return err
}
apiId := restAPI.Api.ApplyT(func(api *awsapigateway.RestApi) pulumi.StringOutput {
  return api.ID().ToStringOutput()
}).ApplyT(func(id interface{}) string {
  return id.(string)
}).(pulumi.StringOutput)
stageName := restAPI.Stage.ApplyT(func(stage *awsapigateway.Stage) pulumi.StringOutput {
  return stage.StageName
}).ApplyT(func(stageName interface{}) string {
  return stageName.(string)
}).(pulumi.StringOutput)
// Define usage plan for an API stage
usagePlan, err := awsapigateway.NewUsagePlan(ctx, "usage-plan", &awsapigateway.UsagePlanArgs{
  ApiStages: awsapigateway.UsagePlanApiStageArray{
    awsapigateway.UsagePlanApiStageArgs{
      ApiId: apiId,
      Stage: stageName,
    },
  },
})
if err != nil {
  return err
}

// Associate the key to the plan
_, err = awsapigateway.NewUsagePlanKey(ctx, "usage-plan-key", &awsapigateway.UsagePlanKeyArgs{
  KeyId:       apiKey.ID(),
  KeyType:     pulumi.String("API_KEY"),
  UsagePlanId: usagePlan.ID(),
})
if err != nil {
  return err
}

ctx.Export("api-key-value", apiKey.Value)
```

{{% /choosable %}}

If using the `HEADER` API Key Source, when making a request, set the `x-api-key` header to the exported "api key value" e.g.:

{{% choosable language "javascript,typescript" %}}

```bash
$ curl -w '\n' -H "x-api-key: $(pulumi stack output apiKeyValue --show-secrets)" "$(pulumi stack output url)"
Hello, API Gateway!
```

{{% /choosable %}}

{{% choosable language "python,go" %}}

```bash
$ curl -w '\n' -H "x-api-key: $(pulumi stack output api-key-value --show-secrets)" "$(pulumi stack output url)"
Hello, API Gateway!
```

{{% /choosable %}}

For more information about Usage Plans and API Keys, refer to
[Create and Use Usage Plans with API Keys](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html).

## Custom Domains and SSL

AWS API Gateway will automatically provision and assign a domain name, URL that contains the stage, and SSL
support. It will look something like `https://no90ji5v23.execute-api.us-west-2.amazonaws.com/stage/`. The host
portion of the URL refers to an API endpoint which can be edge-optimized or regional.

Although it's great to have a URL automatically created with SSL support that works immediately,
the resulting URL isn't user-friendly or very easy to remember, and may not be suitable for business
scenarios that require using company domains. To provide a simpler and more intuitive URL for your API users,
you can configure a custom domain name (e.g., `api.acmecorp.example`) as the API's host name, and customize the
base path of the URL to map to an alternative URL (e.g., one that does not include the `/stage` at the end).

For example, we may map `https://no90ji5v23.execute-api.us-west-2.amazonaws.com/stage/` instead to
`https://api.acmecorp.example/web-ordering`. In doing so, API Gateway will also set up an edge-optimized
[Amazon CloudFront Content Distribution Network (CDN)](https://aws.amazon.com/cloudfront/).

These are the steps required to set up a new domain for an API using Route53 and
[AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html).
We could instead import one into ACM that has been issued by a third-party certificate authority.

{{< chooser language "typescript,python,go" / >}}

First, create a Certificate in AWS ACM. A managed certificate can be created for free for use with AWS services.
   The creation and validation of the certificate can be fully automated via DNS validation:

{{% choosable language "javascript,typescript" %}}

  ```typescript
  const domain = "api.acmecorp.example";
  const awsUsEast1 = new aws.Provider("aws-provider-us-east-1", { region: "us-east-1" });
  const sslCertificate = new aws.acm.Certificate(
      "ssl-cert",
      {
          domainName: domain,
          validationMethod: "DNS",
      },
      { provider: awsUsEast1 }
  );
  ```

{{% /choosable %}}

{{% choosable language python %}}

  ```python
  domain = "api.acmecorp.example"
  aws_us_east_1 = aws.Provider("aws-provider-us-east-1", region="us-east-1")
  ssl_cert = aws.acm.Certificate("ssl-cert",
      domain_name=domain,
      validation_method="DNS",
      opts=ResourceOptions(provider=aws_us_east_1))
  ```

{{% /choosable %}}

{{% choosable language go %}}

  ```go
  domain := pulumi.String("api.acmecorp.example")
  awsUsEast1, err := aws.NewProvider(ctx, "aws-provider-us-east-1", &aws.ProviderArgs{Region: pulumi.String("us-east-1")})
  sslCertificate, err := acm.NewCertificate(ctx,
    "ssl-cert",
    &acm.CertificateArgs{
      DomainName:       domain,
      ValidationMethod: pulumi.String("DNS"),
    },
    pulumi.Provider(awsUsEast1),
  )
  ```

{{% /choosable %}}

  > If the SSL Certificate is for use with API Gateway's Cloudfront endpoints it must be created in us-east-1
  > independent to where the API is deployed.

Next, create a DNS record to prove we do own the domain. This can be automated as follows if your domain is hosted in Route53:

{{% choosable language "javascript,typescript" %}}

  ```typescript
  // Create a DNS zone for our custom domain
  const zone = new aws.route53.Zone("dns-zone", {
      name: domain,
  });
  // Create DNS record to prove to ACM that we own the domain
  const sslCertificateValidationDnsRecord = new aws.route53.Record(
      "ssl-cert-validation-dns-record",
      {
          zoneId: zone.zoneId,
          name: sslCertificate.domainValidationOptions[0].resourceRecordName,
          type: sslCertificate.domainValidationOptions[0].resourceRecordType,
          records: [sslCertificate.domainValidationOptions[0].resourceRecordValue],
          ttl: 10 * 60, // 10 minutes
      }
  );
  ```

{{% /choosable %}}

{{% choosable language python %}}

  ```python
  # Create a DNS zone for our custom domain
  zone = aws.route53.Zone("dns-zone", name=domain)
  ssl_cert_validation_dns_record = aws.route53.Record("ssl-cert-validation-dns-record",
          zone_id=zone_id,
          name=ssl_cert.domain_validation_options.apply(lambda options: options[0].resource_record_name),
          type=ssl_cert.domain_validation_options.apply(lambda options: options[0].resource_record_type),
          records=[ssl_cert.domain_validation_options.apply(lambda options: options[0].resource_record_value)],
          ttl=10*60)
  ```

{{% /choosable %}}

{{% choosable language go %}}

  ```go
  zone, err := route53.NewZone(ctx, "zone", &route53.ZoneArgs{Name: pulumi.String(domain)})
  domainValidationOption := sslCertificate.DomainValidationOptions.ApplyT(func(options []acm.CertificateDomainValidationOption) interface{} {
      return options[0]
  })
  // Create DNS record to prove to ACM that we own the domain
  sslCertificateValidationDnsRecord, err := route53.NewRecord(ctx,
      "ssl-cert-validation-dns-record",
      &route53.RecordArgs{
          ZoneId: zone.ZoneId,
          Name: domainValidationOption.ApplyT(func(option interface{}) string {
            return *option.(acm.CertificateDomainValidationOption).ResourceRecordName
          }).(pulumi.StringOutput),
          Type: domainValidationOption.ApplyT(func(option interface{}) string {
            return *option.(acm.CertificateDomainValidationOption).ResourceRecordType
          }).(pulumi.StringOutput),
          Records: pulumi.StringArray{
            domainValidationOption.ApplyT(func(option interface{}) string {
              return *option.(acm.CertificateDomainValidationOption).ResourceRecordValue
            }).(pulumi.StringOutput),
          },
          Ttl: pulumi.Int(10 * 60), // 10 minutes
      },
  )
  ```

{{% /choosable %}}

We must now wait for the certificate validation to complete before we can proceed with configuring API Gateway
(again, we always run this in the us-east-1 region - where the certificate resides):

{{% choosable language "javascript,typescript" %}}

  ```typescript
  const validatedSslCertificate = new aws.acm.CertificateValidation(
      "ssl-cert-validation",
      {
          certificateArn: sslCertificate.arn,
          validationRecordFqdns: [sslCertificateValidationDnsRecord.fqdn],
      },
      { provider: awsUsEast1 }
  );
  ```

{{% /choosable %}}

{{% choosable language python %}}

  ```python
  validated_ssl_certificate = aws.acm.CertificateValidation("ssl-cert-validation",
                                                            certificate_arn=ssl_cert.arn,
                                                            validation_record_fqdns=[ssl_cert_validation_dns_record.fqdn],
                                                            opts=ResourceOptions(provider=aws_us_east_1))
  ```

{{% /choosable %}}

{{% choosable language go %}}

  ```go
  validatedSslCertificate, err := acm.NewCertificateValidation(ctx,
      "ssl-cert-validation",
      &acm.CertificateValidationArgs{
          CertificateArn:        sslCertificate.Arn,
          ValidationRecordFqdns: pulumi.StringArray{sslCertificateValidationDnsRecord.Fqdn},
      },
      pulumi.Provider(awsUsEast1),
  )
  ```

{{% /choosable %}}

Once ACM has validated our certificate, we can configure API Gateway with the domain and SSL certificate:

{{% choosable language "javascript,typescript" %}}

  ```typescript
  const apiDomainName = new aws.apigateway.DomainName("api-domain-name", {
      certificateArn: validatedSslCertificate.certificateArn,
      domainName: domain,
  });
  const dnsRecord = new aws.route53.Record("api-dns", {
      zoneId: zone.zoneId,
      type: "A",
      name: domain,
      aliases: [{
          name: apiDomainName.cloudfrontDomainName,
          evaluateTargetHealth: false,
          zoneId: apiDomainName.cloudfrontZoneId,
      }]
  });
  ```

{{% /choosable %}}

{{% choosable language python %}}

  ```python
  api_domain_name = aws.apigateway.DomainName("api-domain-name",
                                              certificate_arn=validated_ssl_certificate.certificate_arn,
                                              domain_name=domain)
  # Create DNS record
  aws.route53.Record("api-dns",
                      zone_id=zone.zone_id,
                      type="A",
                      name=domain,
                      aliases=[aws.route53.RecordAliasArgs(
                          name=api_domain_name.cloudfront_domain_name,
                          evaluate_target_health=False,
                          zone_id=api_domain_name.cloudfront_zone_id)])
  ```

{{% /choosable %}}

{{% choosable language go %}}

  ```go
  apiDomainName, err := apigateway.NewDomainName(ctx, "api-domain-name",
      &apigateway.DomainNameArgs{
          CertificateArn: validatedSslCertificate.CertificateArn,
          DomainName:     pulumi.String(domain),
      },
  )
  _, err = route53.NewRecord(ctx, "api-dns",
      &route53.RecordArgs{
          ZoneId: zone.ZoneId,
          Type:   pulumi.String("A"),
          Name:   pulumi.String(domain),
          Aliases: route53.RecordAliasArray{
              route53.RecordAliasArgs{
                  Name:                 apiDomainName.CloudfrontDomainName,
                  EvaluateTargetHealth: pulumi.Bool(false),
                  ZoneId:               apiDomainName.CloudfrontZoneId,
              },
          },
      })
  ```

{{% /choosable %}}

Finally, we tell API Gateway which stage of the API to serve on the custom domain. This also eliminates the `stage/` prefix in the path.

{{% choosable language "javascript,typescript" %}}

  ```typescript
  const basePathMapping = new aws.apigateway.BasePathMapping(
      "api-domain-mapping",
      {
          restApi: api.api.id,
          stageName: api.stage.stageName,
          domainName: apiDomainName.domainName,
      }
  );
  ```

{{% /choosable %}}

{{% choosable language python %}}

  ```python
  base_path_mapping = aws.apigateway.BasePathMapping("api-domain-mapping",
                                                      rest_api=api.api.id,
                                                      stage_name=api.stage.stage_name,
                                                      domain_name=api_domain_name.domain_name)

  ```

{{% /choosable %}}

{{% choosable language go %}}

  ```go
  basePathMapping, err := awsapigateway.NewBasePathMapping(ctx,
      "api-domain-mapping",
      &awsapigateway.BasePathMappingArgs{
          RestApi:    apiId,
          StageName:  stageName,
          DomainName: apiDomainName.DomainName,
      },
  )
  ```

{{% /choosable %}}

For more information about the options and levels of customizability available for edge-optimized AWS API Gateways
and custom domains, refer to [Set up Custom Domain Name for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

## OpenAPI

AWS API Gateway supports the [OpenAPI specification](https://swagger.io/docs/specification/about/) (formerly known as
"Swagger") for defining APIs. Using OpenAPI to define your APIs eases integration with other API authoring, modeling,
and testing tools, at some added complexity cost as you will need to understand the mechanics of how API Gateway
works and what HTTP headers it uses to accomplish its integrations.

### Defining an Entire Endpoint

To use an OpenAPI specification to initialize your API Gateway, supply an entire OpenAPI specification as a string
in the "swagger string" property. For example, this API proxies a route through to another HTTP endpoint:

{{< chooser language "typescript,python,go" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const swaggerAPI = new apigateway.RestAPI("swagger-api", {
    swaggerString: JSON.stringify({
        swagger: "2.0",
        info: {
            title: "example",
            version: "1.0",
        },
        paths: {
            "/": {
                get: {
                    "x-amazon-apigateway-integration": {
                        httpMethod: "GET",
                        passthroughBehavior: "when_no_match",
                        type: "http_proxy",
                        uri: "https://httpbin.org/uuid",
                    },
                },
            },
        },
        "x-amazon-apigateway-binary-media-types": ["*/*"],
    })
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
swagger_api = apigateway.RestAPI("swagger-api",
                                 swagger_string=json.dumps({
                                     "swagger": "2.0",
                                     "info": {
                                         "title": "example",
                                         "version": "1.0",
                                     },
                                     "paths": {
                                         "/": {
                                             "get": {
                                                 "x-amazon-apigateway-integration": {
                                                     "httpMethod": "GET",
                                                     "passthroughBehavior": "when_no_match",
                                                     "type": "http_proxy",
                                                     "uri": "https://httpbin.org/uuid",
                                                 },
                                             },
                                         },
                                     },
                                     "x-amazon-apigateway-binary-media-types": ["*/*"],
                                 })
                                 )
```

{{% /choosable %}}

{{% choosable language go %}}

```go
swaggerAPI, err := apigateway.NewRestAPI(ctx, "swagger-api", &apigateway.RestAPIArgs{
  SwaggerString: pulumi.String(`{
    "swagger": "2.0",
    "info": {
      "title": "example",
      "version": "1.0"
    },
    "paths": {
      "/": {
        "get": {
          "x-amazon-apigateway-integration": {
            "httpMethod": "GET",
            "passthroughBehavior": "when_no_match",
            "type": "http_proxy",
            "uri": "https://httpbin.org/uuid"
          }
        }
      }
    },
    "x-amazon-apigateway-binary-media-types": ["*/*"]
  }`),
})
```

{{% /choosable %}}

This is more complex than the above examples, but this in an escape hatch that you can use to access any API
Gateway features not yet supported by the easier abstractions in Pulumi Crosswalk for AWS API Gateway. You must manually
provide permission for any route targets to be invoked by API Gateway when using this option.

For more information about AWS API Gateway's support for OpenAPI, including exporting specifications from existing
APIs for consumption from other tools, see [Documenting a REST API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html)

### Defining a Single Route

Being able to provide an OpenAPI specification for an entire API Gateway lets you take matters into your own
hands if you need to access a feature not supported directly by `awsx.apigateway.API`. However, if you'd like to
define just a single API using OpenAPI, you can define a Raw Data Route, by supplying a `data` property.

The `data` property is just the `x-amazon-apigateway-integration` object, which can be seen in the above example.
The route's other parameters, such as its path and method, otherwise use the same approaches seen earlier.

For instance, the same API Gateway endpoint that proxies through to another API can be authored as follows:

{{< chooser language "typescript,python,go" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const api = new apigateway.RestAPI("api", {
    routes: [
        {
            path: "/",
            method: "GET",
            data: {
                "x-amazon-apigateway-integration": {
                    httpMethod: "GET",
                    passthroughBehavior: "when_no_match",
                    type: "http_proxy",
                    uri: "https://httpbin.org/uuid",
                },
            },
        },
    ],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
api = apigateway.RestAPI('api', routes=[
    apigateway.RouteArgs(path="/", method="GET", data={
        "x-amazon-apigateway-integration": {
            "httpMethod": "GET",
            "passthroughBehavior": "when_no_match",
            "type": "http_proxy",
            "uri": "https://httpbin.org/uuid",
        },
    }),
])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
getMethod := apigateway.MethodGET
restAPI, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
  Routes: []apigateway.RouteArgs{
    {
      Path:   "/",
      Method: &getMethod,
      Data: map[string]interface{}{
        "x-amazon-apigateway-integration": map[string]interface{}{
          "httpMethod":          "GET",
          "passthroughBehavior": "when_no_match",
          "type":                "http_proxy",
          "uri":                 "https://httpbin.org/uuid",
        },
      },
    },
  },
})
```

{{% /choosable %}}

For full details on what the OpenAPI integration object may contain, refer to the full
[x-amazon-apigateway-integration Object documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration.html).

## Additional API Gateway Resources

For more details about AWS API Gateway and REST APIs, see the following resources:

- [Use AWS API Gateway to Create REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-overview-developer-experience.html#api-gateway-overview-rest)
