---
title_tag: "Configuring AWS API Gateway | Crosswalk"
title: API Gateway
h1: Amazon API Gateway
meta_desc: Pulumi Crosswalk for AWS provides a significantly easier way of programming API Gateway. Here is how.
meta_image: /images/docs/meta-images/docs-clouds-aws-meta-image.png
menu:
  clouds:
    parent: aws-guides
    identifier: aws-guides-api-gateway
    weight: 1

aliases:
- /docs/reference/crosswalk/aws/api-gateway/
- /docs/guides/crosswalk/aws/api-gateway/
---

<a href="./">
<img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[Amazon API Gateway](https://aws.amazon.com/api-gateway/) is a fully managed service for creating, monitoring, and
securing APIs at scale. It acts as a "front door" for REST and WebSocket applications that use backend services,
and handles all the tasks necessary to accept and process up to hundreds of thousands of concurrent API calls,
including traffic management, authorization and access control, monitoring, and API version management. API Gateway
is inexpensive, has no minimum fees, and you only pay for the API calls you receive and the data transferred out.

## Overview

Pulumi Crosswalk for Amazon Web Services (AWS) provides better AWS API management through significantly easier
ways of programming an API Gateway. This includes using infrastructure as code techniques for simple, declarative
APIs, including easy Lambda integration.

The examples below all use the [AWS API Gateway component](/registry/packages/aws-apigateway/) to configure API Gateway to serve several common scenarios. For more information about how to install and use this component, see its full [documentation](/registry/packages/aws-apigateway/) in the Pulumi Registry.

## Creating and configuring routes

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
You'll see later how to assign a custom domain, SSL certificate, and/or eliminate the stage name from the URL.

There are multiple ways to define APIs using Pulumi Crosswalk for AWS:

- [Lambda Function Event Handler Route](#lambda)
- [Static Route Served by S3](#s3)
- [Integration Route](#integration)
- [OpenAPI Specification for an Entire Endpoint](#openapi-full)
- [OpenAPI Specification for a Single Route](#openapi-route)

Multiple endpoints on the same API Gateway can be defined using a combination of these techniques.

### Handling requests with Lambda {#lambda}

An event-handler route is an API that will map to a [Lambda function](https://aws.amazon.com/lambda/). You specify the path, HTTP method, and the Lambda function to invoke when the API is called. Pulumi offers multiple ways of defining the Lambda function and it provisions the appropriate permissions so that API Gateway can communicate with it.

This example creates an Amazon API Gateway REST API with a single API endpoint, listening at `/` for `GET` requests and a `200 OK` for each call.

{{< example-program path="awsx-apigateway-lambda" >}}

Route paths can also be parameterized to allow for matching specific patterns:

- A literal pattern like `/pets` will only match `/pets`
- A parameterized pattern like `/pets/{petId}` will match child routes such as `/pet/123`
- A wildcard pattern specified with `{proxy+}` like `/pets/{proxy+}` will match all descendant paths such as `/pets/tagged/cuddly`

Running `pulumi up` provisions the API Gateway and its routes and returns the URL:

```bash
$ pulumi up -y

Updating (dev)

     Type                             Name                        Status
 +   pulumi:pulumi:Stack              awsx-apigateway-lambda-dev  created (25s)
 +   ├─ aws:iam:Role                  handler                     created (1s)
 +   ├─ aws:lambda:Function           handler                     created (14s)
 +   ├─ aws:iam:RolePolicyAttachment  handler-d32a66fa            created (0.82s)
 +   ├─ aws:iam:RolePolicyAttachment  handler-019020e7            created (1s)
 +   ├─ aws:iam:RolePolicyAttachment  handler-1b4caae3            created (1s)
 +   ├─ aws:iam:RolePolicyAttachment  handler-7cd09230            created (1s)
 +   ├─ aws:iam:RolePolicyAttachment  handler-b5aeb6b6            created (1s)
 +   ├─ aws:iam:RolePolicyAttachment  handler-4aaabb8e            created (1s)
 +   ├─ aws:iam:RolePolicyAttachment  handler-e1a3786d            created (1s)
 +   ├─ aws:iam:RolePolicyAttachment  handler-74d12784            created (1s)
 +   ├─ aws:iam:RolePolicyAttachment  handler-a1de8170            created (1s)
 +   └─ aws-apigateway:index:RestAPI  api                         created (6s)
 +      ├─ aws:apigateway:RestApi     api                         created (2s)
 +      ├─ aws:apigateway:Deployment  api                         created (0.42s)
 +      ├─ aws:lambda:Permission      api-fa520765                created (0.48s)
 +      └─ aws:apigateway:Stage       api                         created (0.54s)

Outputs:
    url: "https://a5yj5n7rz0.execute-api.us-west-2.amazonaws.com/stage/"

Resources:
    + 17 created

Duration: 26s
```

You can `curl` the exported URL to see that it's up and running:

```bash
$ curl $(pulumi stack output url)
{"message":"Hello from API Gateway!"}%
```

For more complete information about creating Lambda Functions, see the [Pulumi Crosswalk for AWS Lambda documentation](/docs/clouds/aws/guides/lambda/).

### Serving static files from S3 {#s3}

A Static Route serves static content from [S3](https://aws.amazon.com/s3/) at an API endpoint.

With the API Gateway component, you specify a local path (either a file or an entire directory), and the component manages the creation of the S3 bucket and the synchronization of the files to S3 objects.

Given a directory `www` containing an `index.html` file, the following program creates an API Gateway API that serves the file at the root path (`/`) of the stage endpoint:

{{< example-program path="awsx-apigateway-s3" >}}

Again, after running `pulumi up`, you can `curl` the exported URL:

```bash
$ curl $(pulumi stack output url)
<html>
    <body>
        <p>Hello from API Gateway + S3!</p>
    </body>
</html>
```

By default, any index documents will be automatically served by S3 when directories are retrieved over HTTP.
(See [Configuring an Index Document](https://docs.aws.amazon.com/AmazonS3/latest/dev/IndexDocumentSupport.html) in the AWS documentation for more information.) To suppress this behavior in the static route, set the `index` property to `false`. To use a different default document name, set `index` property to the name of the file you'd like to use, such as `default.html`.

If the local path points to a directory, the route will automatically be created as a proxy path (i.e. `/{proxy+}`) to match
all sub-directories and the content type for all files will be inferred automatically. If the local path points to a single
file, you can specify the content type explicitly using the `contentType` property.

### Integrating with other AWS services {#integration}

If neither of the above route types work for you, [Amazon API Gateway integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-integration-types.html) connect an API Gateway endpoint to backend services that will execute code in response to requests. The previous Lambda and S3 examples use API Gateway integrations internally, even if it's not evident in the simple interface exposed. Integrations give you full control over how HTTP requests are handled, and responses served, by an API Gateway route.

If you want more flexibility than the earlier methods --- e.g., to proxy HTTP requests, integrate with other AWS services, or mock your APIs --- you can create an _integration route_ by specifying the `target` property on your route.

An integration route is a route that maps an endpoint to a specified backend. Supported integration route types include:

- `aws`: Allows an API to expose an AWS service action, such as invoking Amazon Lambda Functions,
  Amazon DynamoDB, Amazon Simple Notification Service, or Amazon Simple Queue Service. You must configure the data mappings between the HTTP and underlying AWS service requests and responses.

- `aws_proxy`: Also allows an API expose an AWS service action, but instead passes the HTTP request (including headers, path, query parameters, and body) directly to the underlying action.

- `http`: Allows an API to expose HTTP endpoints with custom integration requests and responses. You must configure the data mappings between the HTTP and underlying AWS service requests and responses.

- `http_proxy`: Allows an API to expose HTTP endpoints with a streamlined integration, without requiring you to configure the custom data mappings as with the `http` type.

- `mock`: Allows API Gateway to return a response without sending a request to the backend. This is useful for API testing without needing to configure any backend to handle requests.

The following example sets up an `http_proxy` integration that passes requests directly to another endpoint, in this case `https://www.example.com`:

{{< example-program path="awsx-apigateway-http-proxy" >}}

## Controlling Access to APIs {#authorizers}

AWS API Gateway supports several mechanisms for controlling and managing access to your APIs, including authentication and authorization with resource policies, standard AWS IAM roles and policies, Cognito user pools, and Lambda authorizers. You can also configure access in other ways, such as cross-origin resource sharing (CORS), client-side SSL certificates, Amazon Web Application Firewall (WAF), and limiting access to authorized clients through usage plans and API keys.

The API Gateway component's `RestAPI` resource supports three methods of controlling access to your APIs:

- _Amazon Cognito user pools_ let you create customizable authentication and authorization for your APIs.

- _Lambda authorizers_ are Lambda functions that control access to your APIs based on HTTP information available in headers, paths, query strings, or other request information, including bearer tokens.

- _Usage plans_ let you provide _API keys_ to customers, and then track and limit usage of your APIs.

Details on each are below. For those not directly supported, all of these capabilities are accessible to you in the [Pulumi AWS package](/registry/packages/aws/), and are described in depth in the article [Controlling and Managing Access to a REST API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html).

### Cognito Authorizers

[Cognito Authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html) allow you to use [Amazon Cognito User Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) as an authorizer for API Gateway. With a user pool, your users can sign into your web or mobile app through Amazon Cognito directly, social identity providers like Facebook, or SAML identity providers like Google. This enables your API Gateway to offload the difficult work of security to Cognito entirely.

To require users to sign in through Cognito, you must specify the source of the authorization token (normally the `Authorization` header) and the ARN of the Cognito User Pool:

{{< example-program path="awsx-apigateway-auth-cognito" >}}

When deployed, this configuration will require that a user authenticate, obtain an identity/access token, and call your API with said token.

### Lambda Authorizers

[Lambda Authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html) are AWS Lambda Functions that control access to an API. This allows you to use information in the request itself, including headers, paths, query parameters, or tokens, to decide whether a request is authorized to hit the backend.

You can define a Lambda Authorizer for an event-handler route or a static route. API Gateway supports `request` or `token` type Lambda authorizers:

- Request authorizers can use any part of the request parameters (e.g., headers, path parameters, or query parameters).

- Token authorizers use an authorization token (i.e., a header of the form `Authorization: token <token>`)

To define an Authorizer, you provide a Lambda that receives an [authorizer event](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-input.html) and responds with a valid [authorizer response](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-output.html). See [Pulumi Crosswalk for AWS Lambda](/docs/clouds/aws/guides/lambda/) for other ways you can define your Lambda for the Authorizer.

Below is an example of a custom `request` authorizer. Because the authorizer has access to the content of the HTTP request, it can use any of the request's properties to determine whether to grant access to the resource requested. For demonstration, this authorizer validates the request using a single, hard-coded token. (In practice, you'd more likely have the authorizer query a database or contact another service for this purpose.)

{{< example-program path="awsx-apigateway-auth-lambda" >}}

Once deployed, the protected route only accepts requests containing the token in the `Authorization` header:

```bash
$ curl -H "Authorization: token a-good-token" $(pulumi stack output url)
<html>
    <body>
        <p>Hello from API Gateway + S3!</p>
    </body>
</html>

$ curl $(pulumi stack output url)
{"message":"Unauthorized"}
```

For additional information about API Gateway Lambda Authorizers, see the
[AWS documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html).

## Request Validation {#validation}

API Gateway can perform basic validations against the parameters of a request, the request payload, or both. When a
validation fails, a 400 error is returned immediately, without invoking the backend integration, and the
validation results are published to CloudWatch Logs, eliminating unnecessary calls to the backend.

For basic validation, API Gateway can verify either or both of these conditions:

- The request parameters of an incoming request (headers, query parameters, and path parameters) are included and non-blank.

- The request payload adheres to the configured JSON schema request model of the method.

When enabling validation, you choose a validation scope and validation rules.

### Assigning Validators to APIs and Methods

Validators can be assigned for an entire API or at the individual method level, such as only for `POST` requests on a given
route. The validators defined at a method level override any validator set at the global (i.e., API Gateway instance) level.

To enable validation, pass the `requestValidator` property either on the `RestAPI` resource itself or one or more of its individual routes. The following validator values are supported:

- `ALL`: Validates both the request body and request parameters.
- `BODY_ONLY`: Validates only the request body.
- `PARAMS_ONLY`: Validates only the request parameters.

The following example enables parameter validation on all routes, and both parameter and body validation on a specific route:

{{< example-program path="awsx-apigateway-validation-types" >}}

### Request Parameter Validation

To validate that a particular parameter is present in each request, use the `requiredParams` route property. This property is an array that defines each required parameter and where the parameter is expected to be found (`header`, `path`, `query`), using the `name` and `in` properties, respectively.

The following program uses request validation to ensure that the `q` parameter is present and non-empty on all `/search` requests:

{{< example-program path="awsx-apigateway-validation-types" >}}

For more information about request validation, see [Use Request Validation in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html#api-gateway-request-validation-basic-definitions) in the AWS documentation.

{{% notes type="info" %}}
Request body validation is not yet supported. If you have a need for it, we would love to hear from you.
Comment on [this open issue](https://github.com/pulumi/pulumi-aws-apigateway/issues/36) with details about your use case.
{{% /notes %}}

### Use API Keys to Limit Requests

After you create, test, and deploy your APIs, you can use Amazon API Gateway _usage plans_ to make them available to your
customers. Usage plans and API keys allow customers to use your API at agreed-upon request rates and quotas
that meet their business requirements and budget constraints. If desired, you can set API-level throttling limits.

To require an API key for a given route, set the route's `apiKeyRequired` property to `true`, and at the API level,
specify whether the key should be provided in a `HEADER` (specifically the `x-api-key` header) or `AUTHORIZER` (in which case a Lambda authorizer sends the API key as part of the authorization response). If unspecified, the default API key source is `HEADER`.

Setting up API key-based authorization in API Gateway involves three steps:

1. Creating the API key itself --- for example, with an `ApiKey` resource
1. Defining a usage plan for the API (which can optionally define quotas and throttling rules)
1. Associating the key and usage plan with the API Gateway instance

In the following example, an `ApiKey` resource and `UsagePlan` are provisioned and associated with a `RestAPI` instance, and the generated API key value is exported as a Pulumi stack output (and tracked as an encrypted secret):

{{< example-program path="awsx-apigateway-api-keys" >}}

Note that when using the `HEADER` API key source, requests are expected to provide the token in a header named `x-api-key`:

```bash
$ curl -H "x-api-key: $(pulumi stack output apiKey --show-secrets)" $(pulumi stack output url)
{
    "message": "Hello from API Gateway!"
}

$ curl $(pulumi stack output url)
{"message":"Unauthorized"}
```

For more information about Usage Plans and API Keys, refer to
[Create and Use Usage Plans with API Keys](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html).

## Custom Domains and SSL {#custom-domain}

API Gateway automatically provisions and assigns a domain name, URL that contains the stage, and SSL
support. Generated URLs look something like `https://no90ji5v23.execute-api.us-west-2.amazonaws.com/stage/`, where the host
portion of the URL refers to an API endpoint that can be edge-optimized or regional.

Although it's great to have a URL with SSL support that works immediately,
the resulting URL isn't user-friendly or very easy to remember, and may not be suitable for business
scenarios that require using company domains.

To provide a simpler and more intuitive URL for your API users, you can configure a custom domain name for your API Gateway instance (such as `api.example.com`) and customize the base path of the URL to be something other than `/stage`. When you configure a custom domain, API Gateway also sets up an edge-optimized [Amazon CloudFront Content Distribution Network (CDN)](https://aws.amazon.com/cloudfront/) for you.

The following example shows how to configure an API Gateway instance with a custom domain using Route53 and a free SSL certificate from [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html). (ACM also supports importing certificates issued by third-party certificate authorities.) Note that the ACM certificate is created in the `us-east-1` region (a CloudFront requirement) and validated with a `CertificateValidation` resource that verifies domain ownership through Route53 DNS.

{{< example-program path="awsx-apigateway-custom-domain" >}}

For more information about the options and levels of customizability available for edge-optimized API Gateways
and custom domains, refer to [Set up Custom Domain Name for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html) in the AWS documentation.

## OpenAPI {#openapi}

Amazon API Gateway supports the [OpenAPI specification](https://swagger.io/docs/specification/about/) (formerly known as
"Swagger") for defining APIs. Using OpenAPI to define your APIs eases integration with other API authoring, modeling,
and testing tools, at some added complexity cost as you will need to understand the mechanics of how API Gateway
works and what HTTP headers it uses to accomplish its integrations.

### Defining an Entire Endpoint {#openapi-full}

To use an OpenAPI specification to initialize your API Gateway, supply an entire OpenAPI specification as a JSON string
in the `swaggerString` property. For example, this API proxies a route through to another HTTP endpoint by setting up an `http_proxy` integration, much like the example [above](#integration):

{{< example-program path="awsx-apigateway-openapi-full" >}}

Requests for the exported URL are passed directly to the configured backend:

```bash
$ curl $(pulumi stack output url)
{
  "uuid": "afb17cf3-7a70-4c4b-9f09-7e8f23a63b2b"
}
```

This is more complex than the above examples, but an escape hatch that you can use to access any API
Gateway features not yet supported by the easier abstractions in Pulumi Crosswalk for AWS API Gateway. You must manually
provide permission for any route targets to be invoked by API Gateway when using this option.

### Defining a Single Route {#openapi-route}

Being able to provide an OpenAPI specification for an entire API Gateway lets you take matters into your own
hands when you need access to a feature that isn't supported directly by `apigateway.RestAPI`. However, you can also
define just a single API route (a "raw data" route) using OpenAPI using the `data` property.

The `data` property is just the `x-amazon-apigateway-integration` object, which can be seen in the above example.
The route's other parameters, such as its path and method, otherwise use the same approaches seen earlier.

For instance, the same API Gateway endpoint that proxies through to another API can be authored as follows:

{{< example-program path="awsx-apigateway-openapi-route" >}}

Requests are handled similarly:

```bash
$ curl $(pulumi stack output url)
{
  "uuid": "6cfb94ae-1655-4697-b413-89e541b027f4"
}
```

For more information about API Gateway's support for OpenAPI, including exporting specifications from existing
APIs for consumption from other tools, see [Documenting a REST API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html) in the AWS documentation. For full details on what the OpenAPI integration object may contain, see the
[x-amazon-apigateway-integration Object documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration.html).

## Additional API Gateway Resources

For more details about Amazon API Gateway and REST APIs, see the following resources:

- [Use API Gateway to Create REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-overview-developer-experience.html#api-gateway-overview-rest)
