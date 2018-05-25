---
title: Module apigateway
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Account">class Account</a>
* <a href="#ApiKey">class ApiKey</a>
* <a href="#Authorizer">class Authorizer</a>
* <a href="#BasePathMapping">class BasePathMapping</a>
* <a href="#ClientCertificate">class ClientCertificate</a>
* <a href="#Deployment">class Deployment</a>
* <a href="#DocumentationPart">class DocumentationPart</a>
* <a href="#DocumentationVersion">class DocumentationVersion</a>
* <a href="#DomainName">class DomainName</a>
* <a href="#Integration">class Integration</a>
* <a href="#IntegrationResponse">class IntegrationResponse</a>
* <a href="#Method">class Method</a>
* <a href="#MethodResponse">class MethodResponse</a>
* <a href="#MethodSettings">class MethodSettings</a>
* <a href="#Model">class Model</a>
* <a href="#RequestValidator">class RequestValidator</a>
* <a href="#Resource">class Resource</a>
* <a href="#Response">class Response</a>
* <a href="#RestApi">class RestApi</a>
* <a href="#Stage">class Stage</a>
* <a href="#UsagePlan">class UsagePlan</a>
* <a href="#UsagePlanKey">class UsagePlanKey</a>
* <a href="#VpcLink">class VpcLink</a>
* <a href="#AccountArgs">interface AccountArgs</a>
* <a href="#AccountState">interface AccountState</a>
* <a href="#ApiKeyArgs">interface ApiKeyArgs</a>
* <a href="#ApiKeyState">interface ApiKeyState</a>
* <a href="#AuthorizerArgs">interface AuthorizerArgs</a>
* <a href="#AuthorizerState">interface AuthorizerState</a>
* <a href="#BasePathMappingArgs">interface BasePathMappingArgs</a>
* <a href="#BasePathMappingState">interface BasePathMappingState</a>
* <a href="#ClientCertificateArgs">interface ClientCertificateArgs</a>
* <a href="#ClientCertificateState">interface ClientCertificateState</a>
* <a href="#DeploymentArgs">interface DeploymentArgs</a>
* <a href="#DeploymentState">interface DeploymentState</a>
* <a href="#DocumentationPartArgs">interface DocumentationPartArgs</a>
* <a href="#DocumentationPartState">interface DocumentationPartState</a>
* <a href="#DocumentationVersionArgs">interface DocumentationVersionArgs</a>
* <a href="#DocumentationVersionState">interface DocumentationVersionState</a>
* <a href="#DomainNameArgs">interface DomainNameArgs</a>
* <a href="#DomainNameState">interface DomainNameState</a>
* <a href="#IntegrationArgs">interface IntegrationArgs</a>
* <a href="#IntegrationResponseArgs">interface IntegrationResponseArgs</a>
* <a href="#IntegrationResponseState">interface IntegrationResponseState</a>
* <a href="#IntegrationState">interface IntegrationState</a>
* <a href="#MethodArgs">interface MethodArgs</a>
* <a href="#MethodResponseArgs">interface MethodResponseArgs</a>
* <a href="#MethodResponseState">interface MethodResponseState</a>
* <a href="#MethodSettingsArgs">interface MethodSettingsArgs</a>
* <a href="#MethodSettingsState">interface MethodSettingsState</a>
* <a href="#MethodState">interface MethodState</a>
* <a href="#ModelArgs">interface ModelArgs</a>
* <a href="#ModelState">interface ModelState</a>
* <a href="#RequestValidatorArgs">interface RequestValidatorArgs</a>
* <a href="#RequestValidatorState">interface RequestValidatorState</a>
* <a href="#ResourceArgs">interface ResourceArgs</a>
* <a href="#ResourceState">interface ResourceState</a>
* <a href="#ResponseArgs">interface ResponseArgs</a>
* <a href="#ResponseState">interface ResponseState</a>
* <a href="#RestApiArgs">interface RestApiArgs</a>
* <a href="#RestApiState">interface RestApiState</a>
* <a href="#StageArgs">interface StageArgs</a>
* <a href="#StageState">interface StageState</a>
* <a href="#UsagePlanArgs">interface UsagePlanArgs</a>
* <a href="#UsagePlanKeyArgs">interface UsagePlanKeyArgs</a>
* <a href="#UsagePlanKeyState">interface UsagePlanKeyState</a>
* <a href="#UsagePlanState">interface UsagePlanState</a>
* <a href="#VpcLinkArgs">interface VpcLinkArgs</a>
* <a href="#VpcLinkState">interface VpcLinkState</a>

<a href="/apigateway/account.ts">apigateway/account.ts</a> <a href="/apigateway/apiKey.ts">apigateway/apiKey.ts</a> <a href="/apigateway/authorizer.ts">apigateway/authorizer.ts</a> <a href="/apigateway/basePathMapping.ts">apigateway/basePathMapping.ts</a> <a href="/apigateway/clientCertificate.ts">apigateway/clientCertificate.ts</a> <a href="/apigateway/deployment.ts">apigateway/deployment.ts</a> <a href="/apigateway/documentationPart.ts">apigateway/documentationPart.ts</a> <a href="/apigateway/documentationVersion.ts">apigateway/documentationVersion.ts</a> <a href="/apigateway/domainName.ts">apigateway/domainName.ts</a> <a href="/apigateway/integration.ts">apigateway/integration.ts</a> <a href="/apigateway/integrationResponse.ts">apigateway/integrationResponse.ts</a> <a href="/apigateway/method.ts">apigateway/method.ts</a> <a href="/apigateway/methodResponse.ts">apigateway/methodResponse.ts</a> <a href="/apigateway/methodSettings.ts">apigateway/methodSettings.ts</a> <a href="/apigateway/model.ts">apigateway/model.ts</a> <a href="/apigateway/requestValidator.ts">apigateway/requestValidator.ts</a> <a href="/apigateway/resource.ts">apigateway/resource.ts</a> <a href="/apigateway/response.ts">apigateway/response.ts</a> <a href="/apigateway/restApi.ts">apigateway/restApi.ts</a> <a href="/apigateway/stage.ts">apigateway/stage.ts</a> <a href="/apigateway/usagePlan.ts">apigateway/usagePlan.ts</a> <a href="/apigateway/usagePlanKey.ts">apigateway/usagePlanKey.ts</a> <a href="/apigateway/vpcLink.ts">apigateway/vpcLink.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Account">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/account.ts#L11">class Account</a>
</h2>

Provides a settings of an API Gateway Account. Settings is applied region-wide per `provider` block.

-> **Note:** As there is no API method for deleting account settings or resetting it to defaults, destroying this resource will keep your account settings intact

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/account.ts#L33">constructor</a>
</h3>

```typescript
new Account(name: string, args?: AccountArgs, opts?: pulumi.ResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Account(name: string, state?: AccountState, opts?: pulumi.ResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/account.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountState): Account
```


Get an existing Account resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/account.ts#L29">property cloudwatchRoleArn</a>
</h3>

```typescript
public cloudwatchRoleArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM role for CloudWatch (to allow logging & monitoring).
See more [in AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console).
Logging & monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/account.ts#L33">property throttleSettings</a>
</h3>

```typescript
public throttleSettings: pulumi.Output<{ ... }>;
```


Account-Level throttle settings. See exported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ApiKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L13">class ApiKey</a>
</h2>

Provides an API Gateway API Key.

~> **Warning:** Since the API Gateway usage plans feature was launched on August 11, 2016, usage plans are now **required** to associate an API key with an API stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L53">constructor</a>
</h3>

```typescript
new ApiKey(name: string, args?: ApiKeyArgs, opts?: pulumi.ResourceOptions)
```


Create a ApiKey resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ApiKey(name: string, state?: ApiKeyState, opts?: pulumi.ResourceOptions)
```


Create a ApiKey resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApiKeyState): ApiKey
```


Get an existing ApiKey resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L29">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The creation date of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The API key description. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L37">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Specifies whether the API key can be used by callers. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L41">property lastUpdatedDate</a>
</h3>

```typescript
public lastUpdatedDate: pulumi.Output<string>;
```


The last update date of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L49">property stageKeys</a>
</h3>

```typescript
public stageKeys: pulumi.Output<{ ... }[] | undefined>;
```


A list of stage keys associated with the API key - see below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L53">property value</a>
</h3>

```typescript
public value: pulumi.Output<string>;
```


The value of the API key. If not specified, it will be automatically generated by AWS on creation.

<h2 class="pdoc-module-header" id="Authorizer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L11">class Authorizer</a>
</h2>

Provides an API Gateway Authorizer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L69">constructor</a>
</h3>

```typescript
new Authorizer(name: string, args: AuthorizerArgs, opts?: pulumi.ResourceOptions)
```


Create a Authorizer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Authorizer(name: string, state?: AuthorizerState, opts?: pulumi.ResourceOptions)
```


Create a Authorizer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AuthorizerState): Authorizer
```


Get an existing Authorizer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L28">property authorizerCredentials</a>
</h3>

```typescript
public authorizerCredentials: pulumi.Output<string | undefined>;
```


The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L33">property authorizerResultTtlInSeconds</a>
</h3>

```typescript
public authorizerResultTtlInSeconds: pulumi.Output<number | undefined>;
```


The TTL of cached authorizer results in seconds.
Defaults to `300`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L39">property authorizerUri</a>
</h3>

```typescript
public authorizerUri: pulumi.Output<string | undefined>;
```


The authorizer's Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L44">property identitySource</a>
</h3>

```typescript
public identitySource: pulumi.Output<string | undefined>;
```


The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L51">property identityValidationExpression</a>
</h3>

```typescript
public identityValidationExpression: pulumi.Output<string | undefined>;
```


A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn't match,
the client receives a 401 Unauthorized response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L55">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the authorizer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L60">property providerArns</a>
</h3>

```typescript
public providerArns: pulumi.Output<string[] | undefined>;
```


A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L64">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L69">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```


The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="BasePathMapping">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L13">class BasePathMapping</a>
</h2>

Connects a custom domain name registered via `aws_api_gateway_domain_name`
with a deployed API so that its methods can be called via the
custom domain name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L41">constructor</a>
</h3>

```typescript
new BasePathMapping(name: string, args: BasePathMappingArgs, opts?: pulumi.ResourceOptions)
```


Create a BasePathMapping resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new BasePathMapping(name: string, state?: BasePathMappingState, opts?: pulumi.ResourceOptions)
```


Create a BasePathMapping resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BasePathMappingState): BasePathMapping
```


Get an existing BasePathMapping resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L33">property basePath</a>
</h3>

```typescript
public basePath: pulumi.Output<string | undefined>;
```


Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L37">property domainName</a>
</h3>

```typescript
public domainName: pulumi.Output<string>;
```


The already-registered domain name to connect the API to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L29">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The id of the API to connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L41">property stageName</a>
</h3>

```typescript
public stageName: pulumi.Output<string | undefined>;
```


The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ClientCertificate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L9">class ClientCertificate</a>
</h2>

Provides an API Gateway Client Certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L37">constructor</a>
</h3>

```typescript
new ClientCertificate(name: string, args?: ClientCertificateArgs, opts?: pulumi.ResourceOptions)
```


Create a ClientCertificate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ClientCertificate(name: string, state?: ClientCertificateState, opts?: pulumi.ResourceOptions)
```


Create a ClientCertificate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClientCertificateState): ClientCertificate
```


Get an existing ClientCertificate resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L25">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The date when the client certificate was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the client certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L33">property expirationDate</a>
</h3>

```typescript
public expirationDate: pulumi.Output<string>;
```


The date when the client certificate will expire.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L37">property pemEncodedCertificate</a>
</h3>

```typescript
public pemEncodedCertificate: pulumi.Output<string>;
```


The PEM-encoded public key of the client certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Deployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L14">class Deployment</a>
</h2>

Provides an API Gateway Deployment.

-> **Note:** Depends on having `aws_api_gateway_integration` inside your rest api (which in turn depends on `aws_api_gateway_method`). To avoid race conditions
you might need to add an explicit `depends_on = ["aws_api_gateway_integration.name"]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L61">constructor</a>
</h3>

```typescript
new Deployment(name: string, args: DeploymentArgs, opts?: pulumi.ResourceOptions)
```


Create a Deployment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Deployment(name: string, state?: DeploymentState, opts?: pulumi.ResourceOptions)
```


Create a Deployment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DeploymentState): Deployment
```


Get an existing Deployment resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L30">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The creation date of the deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L34">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L40">property executionArn</a>
</h3>

```typescript
public executionArn: pulumi.Output<string>;
```


The execution ARN to be used in [`lambda_permission`](/docs/providers/aws/r/lambda_permission.html)'s `source_arn`
when allowing API Gateway to invoke a Lambda function,
e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L45">property invokeUrl</a>
</h3>

```typescript
public invokeUrl: pulumi.Output<string>;
```


The URL to invoke the API pointing to the stage,
e.g. `https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L49">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L53">property stageDescription</a>
</h3>

```typescript
public stageDescription: pulumi.Output<string | undefined>;
```


The description of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L57">property stageName</a>
</h3>

```typescript
public stageName: pulumi.Output<string>;
```


The name of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L61">property variables</a>
</h3>

```typescript
public variables: pulumi.Output<{ ... } | undefined>;
```


A map that defines variables for the stage

<h2 class="pdoc-module-header" id="DocumentationPart">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L9">class DocumentationPart</a>
</h2>

Provides a settings of an API Gateway Documentation Part.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L33">constructor</a>
</h3>

```typescript
new DocumentationPart(name: string, args: DocumentationPartArgs, opts?: pulumi.ResourceOptions)
```


Create a DocumentationPart resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new DocumentationPart(name: string, state?: DocumentationPartState, opts?: pulumi.ResourceOptions)
```


Create a DocumentationPart resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DocumentationPartState): DocumentationPart
```


Get an existing DocumentationPart resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L25">property location</a>
</h3>

```typescript
public location: pulumi.Output<{ ... }>;
```


The location of the targeted API entity of the to-be-created documentation part. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L29">property properties</a>
</h3>

```typescript
public properties: pulumi.Output<string>;
```


A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., "{ \"description\": \"The API does ...\" }". Only Swagger-compliant key-value pairs can be exported and, hence, published.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L33">property restApiId</a>
</h3>

```typescript
public restApiId: pulumi.Output<string>;
```


The ID of the associated Rest API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DocumentationVersion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L9">class DocumentationVersion</a>
</h2>

Provides a resource to manage an API Gateway Documentation Version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L33">constructor</a>
</h3>

```typescript
new DocumentationVersion(name: string, args: DocumentationVersionArgs, opts?: pulumi.ResourceOptions)
```


Create a DocumentationVersion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new DocumentationVersion(name: string, state?: DocumentationVersionState, opts?: pulumi.ResourceOptions)
```


Create a DocumentationVersion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DocumentationVersionState): DocumentationVersion
```


Get an existing DocumentationVersion resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L25">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the API documentation version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L29">property restApiId</a>
</h3>

```typescript
public restApiId: pulumi.Output<string>;
```


The ID of the associated Rest API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L33">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The version identifier of the API documentation snapshot.

<h2 class="pdoc-module-header" id="DomainName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L24">class DomainName</a>
</h2>

Registers a custom domain name for use with AWS API Gateway.

This resource just establishes ownership of and the TLS settings for
a particular domain name. An API can be attached to a particular path
under the registered domain name using
[the `aws_api_gateway_base_path_mapping` resource](api_gateway_base_path_mapping.html).

Internally API Gateway creates a CloudFront distribution to
route requests on the given hostname. In addition to this resource
it's necessary to create a DNS record corresponding to the
given domain name which is an alias (either Route53 alias or
traditional CNAME) to the Cloudfront domain name exported in the
`cloudfront_domain_name` attribute.

~> **Note:** All arguments including the private key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L79">constructor</a>
</h3>

```typescript
new DomainName(name: string, args: DomainNameArgs, opts?: pulumi.ResourceOptions)
```


Create a DomainName resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new DomainName(name: string, state?: DomainNameState, opts?: pulumi.ResourceOptions)
```


Create a DomainName resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L33">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainNameState): DomainName
```


Get an existing DomainName resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L40">property certificateArn</a>
</h3>

```typescript
public certificateArn: pulumi.Output<string | undefined>;
```


The ARN for an AWS-managed certificate. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain` and `certificate_private_key`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L45">property certificateBody</a>
</h3>

```typescript
public certificateBody: pulumi.Output<string | undefined>;
```


The certificate issued for the domain name
being registered, in PEM format. Conflicts with `certificate_arn`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L51">property certificateChain</a>
</h3>

```typescript
public certificateChain: pulumi.Output<string | undefined>;
```


The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Conflicts with `certificate_arn`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L56">property certificateName</a>
</h3>

```typescript
public certificateName: pulumi.Output<string | undefined>;
```


The unique name to use when registering this
cert as an IAM server certificate. Conflicts with `certificate_arn`. Required if `certificate_arn` is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L61">property certificatePrivateKey</a>
</h3>

```typescript
public certificatePrivateKey: pulumi.Output<string | undefined>;
```


The private key associated with the
domain certificate given in `certificate_body`. Conflicts with `certificate_arn`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L65">property certificateUploadDate</a>
</h3>

```typescript
public certificateUploadDate: pulumi.Output<string>;
```


The upload date associated with the domain certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L70">property cloudfrontDomainName</a>
</h3>

```typescript
public cloudfrontDomainName: pulumi.Output<string>;
```


The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L75">property cloudfrontZoneId</a>
</h3>

```typescript
public cloudfrontZoneId: pulumi.Output<string>;
```


For convenience, the hosted zone id (`Z2FDTNDATAQYW2`)
that can be used to create a Route53 alias record for the distribution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L79">property domainName</a>
</h3>

```typescript
public domainName: pulumi.Output<string>;
```


The fully-qualified domain name to register

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Integration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L11">class Integration</a>
</h2>

Provides an HTTP Method Integration for an API Gateway Integration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L87">constructor</a>
</h3>

```typescript
new Integration(name: string, args: IntegrationArgs, opts?: pulumi.ResourceOptions)
```


Create a Integration resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Integration(name: string, state?: IntegrationState, opts?: pulumi.ResourceOptions)
```


Create a Integration resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IntegrationState): Integration
```


Get an existing Integration resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L27">property cacheKeyParameters</a>
</h3>

```typescript
public cacheKeyParameters: pulumi.Output<string[] | undefined>;
```


A list of cache key parameters for the integration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L31">property cacheNamespace</a>
</h3>

```typescript
public cacheNamespace: pulumi.Output<string>;
```


The integration's cache namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L35">property contentHandling</a>
</h3>

```typescript
public contentHandling: pulumi.Output<string | undefined>;
```


Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L39">property credentials</a>
</h3>

```typescript
public credentials: pulumi.Output<string | undefined>;
```


The credentials required for the integration. For `AWS` integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role's ARN. To require that the caller's identity be passed through from the request, specify the string `arn:aws:iam::\*:user/\*`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L44">property httpMethod</a>
</h3>

```typescript
public httpMethod: pulumi.Output<string>;
```


The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`, `ANY`)
when calling the associated resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L52">property integrationHttpMethod</a>
</h3>

```typescript
public integrationHttpMethod: pulumi.Output<string | undefined>;
```


The integration HTTP method
(`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`) specifying how API Gateway will interact with the back end.
**Required** if `type` is `AWS`, `AWS_PROXY`, `HTTP` or `HTTP_PROXY`.
Not all methods are compatible with all `AWS` integrations.
e.g. Lambda function [can only be invoked](https://github.com/awslabs/aws-apigateway-importer/issues/9#issuecomment-129651005) via `POST`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L56">property passthroughBehavior</a>
</h3>

```typescript
public passthroughBehavior: pulumi.Output<string>;
```


The integration passthrough behavior (`WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`).  **Required** if `request_templates` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L61">property requestParameters</a>
</h3>

```typescript
public requestParameters: pulumi.Output<{ ... } | undefined>;
```


A map of request query string parameters and headers that should be passed to the backend responder.
For example: `request_parameters = { "integration.request.header.X-Some-Other-Header" = "method.request.header.X-Some-Header" }`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L65">property requestParametersInJson</a>
</h3>

```typescript
public requestParametersInJson: pulumi.Output<string | undefined>;
```


**Deprecated**, use `request_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L69">property requestTemplates</a>
</h3>

```typescript
public requestTemplates: pulumi.Output<{ ... } | undefined>;
```


A map of the integration's request templates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L73">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The API resource ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L77">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L81">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The integration input's [type](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/). Valid values are `HTTP` (for HTTP backends), `MOCK` (not calling any real backend), `AWS` (for AWS services), `AWS_PROXY` (for Lambda proxy integration) and `HTTP_PROXY` (for HTTP proxy integration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L87">property uri</a>
</h3>

```typescript
public uri: pulumi.Output<string | undefined>;
```


The input's URI (HTTP, AWS). **Required** if `type` is `HTTP` or `AWS`.
For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form `arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}`. `region`, `subdomain` and `service` are used to determine the right endpoint.
e.g. `arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IntegrationResponse">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L14">class IntegrationResponse</a>
</h2>

Provides an HTTP Method Integration Response for an API Gateway Resource.

-> **Note:** Depends on having `aws_api_gateway_integration` inside your rest api. To ensure this
you might need to add an explicit `depends_on` for clean runs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L66">constructor</a>
</h3>

```typescript
new IntegrationResponse(name: string, args: IntegrationResponseArgs, opts?: pulumi.ResourceOptions)
```


Create a IntegrationResponse resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new IntegrationResponse(name: string, state?: IntegrationResponseState, opts?: pulumi.ResourceOptions)
```


Create a IntegrationResponse resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IntegrationResponseState): IntegrationResponse
```


Get an existing IntegrationResponse resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L30">property contentHandling</a>
</h3>

```typescript
public contentHandling: pulumi.Output<string | undefined>;
```


Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L34">property httpMethod</a>
</h3>

```typescript
public httpMethod: pulumi.Output<string>;
```


The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L38">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L43">property responseParameters</a>
</h3>

```typescript
public responseParameters: pulumi.Output<{ ... } | undefined>;
```


A map of response parameters that can be read from the backend response.
For example: `response_parameters = { "method.response.header.X-Some-Header" = "integration.response.header.X-Some-Other-Header" }`,

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L47">property responseParametersInJson</a>
</h3>

```typescript
public responseParametersInJson: pulumi.Output<string | undefined>;
```


**Deprecated**, use `response_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L51">property responseTemplates</a>
</h3>

```typescript
public responseTemplates: pulumi.Output<{ ... } | undefined>;
```


A map specifying the templates used to transform the integration response body

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L55">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L62">property selectionPattern</a>
</h3>

```typescript
public selectionPattern: pulumi.Output<string | undefined>;
```


Specifies the regular expression pattern used to choose
an integration response based on the response from the backend. Setting this to `-` makes the integration the default one.
If the backend is an `AWS` Lambda function, the AWS Lambda function error header is matched.
For all other `HTTP` and `AWS` backends, the HTTP status code is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L66">property statusCode</a>
</h3>

```typescript
public statusCode: pulumi.Output<string>;
```


The HTTP status code

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Method">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L11">class Method</a>
</h2>

Provides a HTTP Method for an API Gateway Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L73">constructor</a>
</h3>

```typescript
new Method(name: string, args: MethodArgs, opts?: pulumi.ResourceOptions)
```


Create a Method resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Method(name: string, state?: MethodState, opts?: pulumi.ResourceOptions)
```


Create a Method resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MethodState): Method
```


Get an existing Method resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L27">property apiKeyRequired</a>
</h3>

```typescript
public apiKeyRequired: pulumi.Output<boolean | undefined>;
```


Specify if the method requires an API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L31">property authorization</a>
</h3>

```typescript
public authorization: pulumi.Output<string>;
```


The type of authorization used for the method (`NONE`, `CUSTOM`, `AWS_IAM`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L35">property authorizerId</a>
</h3>

```typescript
public authorizerId: pulumi.Output<string | undefined>;
```


The authorizer id to be used when the authorization is `CUSTOM`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L39">property httpMethod</a>
</h3>

```typescript
public httpMethod: pulumi.Output<string>;
```


The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L45">property requestModels</a>
</h3>

```typescript
public requestModels: pulumi.Output<{ ... } | undefined>;
```


A map of the API models used for the request's content type
where key is the content type (e.g. `application/json`)
and value is either `Error`, `Empty` (built-in models) or `aws_api_gateway_model`'s `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L57">property requestParameters</a>
</h3>

```typescript
public requestParameters: pulumi.Output<{ ... } | undefined>;
```


A map of request query string parameters and headers that should be passed to the integration.
For example:
```hcl
request_parameters = {
"method.request.header.X-Some-Header" = true,
"method.request.querystring.some-query-param"  = true,
}
```
would define that the header `X-Some-Header` and the query string `some-query-param` must be provided on the request, or

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L61">property requestParametersInJson</a>
</h3>

```typescript
public requestParametersInJson: pulumi.Output<string | undefined>;
```


**Deprecated**, use `request_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L65">property requestValidatorId</a>
</h3>

```typescript
public requestValidatorId: pulumi.Output<string | undefined>;
```


The ID of a `aws_api_gateway_request_validator`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L69">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L73">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="MethodResponse">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L11">class MethodResponse</a>
</h2>

Provides an HTTP Method Response for an API Gateway Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L53">constructor</a>
</h3>

```typescript
new MethodResponse(name: string, args: MethodResponseArgs, opts?: pulumi.ResourceOptions)
```


Create a MethodResponse resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new MethodResponse(name: string, state?: MethodResponseState, opts?: pulumi.ResourceOptions)
```


Create a MethodResponse resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MethodResponseState): MethodResponse
```


Get an existing MethodResponse resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L27">property httpMethod</a>
</h3>

```typescript
public httpMethod: pulumi.Output<string>;
```


The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L31">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L35">property responseModels</a>
</h3>

```typescript
public responseModels: pulumi.Output<{ ... } | undefined>;
```


A map of the API models used for the response's content type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L41">property responseParameters</a>
</h3>

```typescript
public responseParameters: pulumi.Output<{ ... } | undefined>;
```


A map of response parameters that can be sent to the caller.
For example: `response_parameters = { "method.response.header.X-Some-Header" = true }`
would define that the header `X-Some-Header` can be provided on the response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L45">property responseParametersInJson</a>
</h3>

```typescript
public responseParametersInJson: pulumi.Output<string | undefined>;
```


**Deprecated**, use `response_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L49">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L53">property statusCode</a>
</h3>

```typescript
public statusCode: pulumi.Output<string>;
```


The HTTP status code

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="MethodSettings">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L11">class MethodSettings</a>
</h2>

Provides an API Gateway Method Settings, e.g. logging or monitoring.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L39">constructor</a>
</h3>

```typescript
new MethodSettings(name: string, args: MethodSettingsArgs, opts?: pulumi.ResourceOptions)
```


Create a MethodSettings resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new MethodSettings(name: string, state?: MethodSettingsState, opts?: pulumi.ResourceOptions)
```


Create a MethodSettings resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MethodSettingsState): MethodSettings
```


Get an existing MethodSettings resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L27">property methodPath</a>
</h3>

```typescript
public methodPath: pulumi.Output<string>;
```


Method path defined as `{resource_path}/{http_method}` for an individual method override, or `*&#47;*` for overriding all methods in the stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L31">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L35">property settings</a>
</h3>

```typescript
public settings: pulumi.Output<{ ... }>;
```


The settings block, see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L39">property stageName</a>
</h3>

```typescript
public stageName: pulumi.Output<string>;
```


The name of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Model">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L11">class Model</a>
</h2>

Provides a Model for a API Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L43">constructor</a>
</h3>

```typescript
new Model(name: string, args: ModelArgs, opts?: pulumi.ResourceOptions)
```


Create a Model resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Model(name: string, state?: ModelState, opts?: pulumi.ResourceOptions)
```


Create a Model resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ModelState): Model
```


Get an existing Model resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L27">property contentType</a>
</h3>

```typescript
public contentType: pulumi.Output<string>;
```


The content type of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L39">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L43">property schema</a>
</h3>

```typescript
public schema: pulumi.Output<string | undefined>;
```


The schema of the model in a JSON form

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RequestValidator">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L8">class RequestValidator</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L24">constructor</a>
</h3>

```typescript
new RequestValidator(name: string, args: RequestValidatorArgs, opts?: pulumi.ResourceOptions)
```


Create a RequestValidator resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new RequestValidator(name: string, state?: RequestValidatorState, opts?: pulumi.ResourceOptions)
```


Create a RequestValidator resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L17">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RequestValidatorState): RequestValidator
```


Get an existing RequestValidator resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L21">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L22">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L23">property validateRequestBody</a>
</h3>

```typescript
public validateRequestBody: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L24">property validateRequestParameters</a>
</h3>

```typescript
public validateRequestParameters: pulumi.Output<boolean | undefined>;
```

<h2 class="pdoc-module-header" id="Resource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L11">class Resource</a>
</h2>

Provides an API Gateway Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L39">constructor</a>
</h3>

```typescript
new Resource(name: string, args: ResourceArgs, opts?: pulumi.ResourceOptions)
```


Create a Resource resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Resource(name: string, state?: ResourceState, opts?: pulumi.ResourceOptions)
```


Create a Resource resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ResourceState): Resource
```


Get an existing Resource resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L27">property parentId</a>
</h3>

```typescript
public parentId: pulumi.Output<string>;
```


The ID of the parent API resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L31">property path</a>
</h3>

```typescript
public path: pulumi.Output<string>;
```


The complete path for this API resource, including all parent paths.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L35">property pathPart</a>
</h3>

```typescript
public pathPart: pulumi.Output<string>;
```


The last path segment of this API resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L39">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Response">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L9">class Response</a>
</h2>

Provides an API Gateway Gateway Response for a REST API Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L41">constructor</a>
</h3>

```typescript
new Response(name: string, args: ResponseArgs, opts?: pulumi.ResourceOptions)
```


Create a Response resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Response(name: string, state?: ResponseState, opts?: pulumi.ResourceOptions)
```


Create a Response resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ResponseState): Response
```


Get an existing Response resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L25">property responseParameters</a>
</h3>

```typescript
public responseParameters: pulumi.Output<{ ... } | undefined>;
```


A map specifying the templates used to transform the response body.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L29">property responseTemplates</a>
</h3>

```typescript
public responseTemplates: pulumi.Output<{ ... } | undefined>;
```


A map specifying the parameters (paths, query strings and headers) of the Gateway Response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L33">property responseType</a>
</h3>

```typescript
public responseType: pulumi.Output<string>;
```


The response type of the associated GatewayResponse.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L37">property restApiId</a>
</h3>

```typescript
public restApiId: pulumi.Output<string>;
```


The string identifier of the associated REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L41">property statusCode</a>
</h3>

```typescript
public statusCode: pulumi.Output<string | undefined>;
```


The HTTP status code of the Gateway Response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RestApi">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L9">class RestApi</a>
</h2>

Provides an API Gateway REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L49">constructor</a>
</h3>

```typescript
new RestApi(name: string, args?: RestApiArgs, opts?: pulumi.ResourceOptions)
```


Create a RestApi resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new RestApi(name: string, state?: RestApiState, opts?: pulumi.ResourceOptions)
```


Create a RestApi resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RestApiState): RestApi
```


Get an existing RestApi resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L25">property binaryMediaTypes</a>
</h3>

```typescript
public binaryMediaTypes: pulumi.Output<string[] | undefined>;
```


The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L29">property body</a>
</h3>

```typescript
public body: pulumi.Output<string | undefined>;
```


An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L33">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The creation date of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L37">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L41">property minimumCompressionSize</a>
</h3>

```typescript
public minimumCompressionSize: pulumi.Output<number | undefined>;
```


Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L49">property rootResourceId</a>
</h3>

```typescript
public rootResourceId: pulumi.Output<string>;
```


The resource ID of the REST API's root

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Stage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L12">class Stage</a>
</h2>

Provides an API Gateway Stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L61">constructor</a>
</h3>

```typescript
new Stage(name: string, args: StageArgs, opts?: pulumi.ResourceOptions)
```


Create a Stage resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Stage(name: string, state?: StageState, opts?: pulumi.ResourceOptions)
```


Create a Stage resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StageState): Stage
```


Get an existing Stage resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L28">property cacheClusterEnabled</a>
</h3>

```typescript
public cacheClusterEnabled: pulumi.Output<boolean | undefined>;
```


Specifies whether a cache cluster is enabled for the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L33">property cacheClusterSize</a>
</h3>

```typescript
public cacheClusterSize: pulumi.Output<string | undefined>;
```


The size of the cache cluster for the stage, if enabled.
Allowed values include `0.5`, `1.6`, `6.1`, `13.5`, `28.4`, `58.2`, `118` and `237`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L37">property clientCertificateId</a>
</h3>

```typescript
public clientCertificateId: pulumi.Output<string | undefined>;
```


The identifier of a client certificate for the stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L41">property deployment</a>
</h3>

```typescript
public deployment: pulumi.Output<Deployment>;
```


The ID of the deployment that the stage points to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L45">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L49">property documentationVersion</a>
</h3>

```typescript
public documentationVersion: pulumi.Output<string | undefined>;
```


The version of the associated API documentation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L53">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L57">property stageName</a>
</h3>

```typescript
public stageName: pulumi.Output<string>;
```


The name of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L61">property variables</a>
</h3>

```typescript
public variables: pulumi.Output<{ ... } | undefined>;
```


A map that defines the stage variables

<h2 class="pdoc-module-header" id="UsagePlan">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L9">class UsagePlan</a>
</h2>

Provides an API Gateway Usage Plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L45">constructor</a>
</h3>

```typescript
new UsagePlan(name: string, args?: UsagePlanArgs, opts?: pulumi.ResourceOptions)
```


Create a UsagePlan resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new UsagePlan(name: string, state?: UsagePlanState, opts?: pulumi.ResourceOptions)
```


Create a UsagePlan resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UsagePlanState): UsagePlan
```


Get an existing UsagePlan resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L25">property apiStages</a>
</h3>

```typescript
public apiStages: pulumi.Output<{ ... }[] | undefined>;
```


The associated [API stages](#api-stages-arguments) of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of a usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L37">property productCode</a>
</h3>

```typescript
public productCode: pulumi.Output<string | undefined>;
```


The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L41">property quotaSettings</a>
</h3>

```typescript
public quotaSettings: pulumi.Output<{ ... } | undefined>;
```


The [quota settings](#quota-settings-arguments) of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L45">property throttleSettings</a>
</h3>

```typescript
public throttleSettings: pulumi.Output<{ ... } | undefined>;
```


The [throttling limits](#throttling-settings-arguments) of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="UsagePlanKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L9">class UsagePlanKey</a>
</h2>

Provides an API Gateway Usage Plan Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L41">constructor</a>
</h3>

```typescript
new UsagePlanKey(name: string, args: UsagePlanKeyArgs, opts?: pulumi.ResourceOptions)
```


Create a UsagePlanKey resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new UsagePlanKey(name: string, state?: UsagePlanKeyState, opts?: pulumi.ResourceOptions)
```


Create a UsagePlanKey resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UsagePlanKeyState): UsagePlanKey
```


Get an existing UsagePlanKey resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L25">property keyId</a>
</h3>

```typescript
public keyId: pulumi.Output<string>;
```


The identifier of the API key resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L29">property keyType</a>
</h3>

```typescript
public keyType: pulumi.Output<string>;
```


The type of the API key resource. Currently, the valid key type is API_KEY.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of a usage plan key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L37">property usagePlanId</a>
</h3>

```typescript
public usagePlanId: pulumi.Output<string>;
```


The Id of the usage plan resource representing to associate the key to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L41">property value</a>
</h3>

```typescript
public value: pulumi.Output<string>;
```


The value of a usage plan key.

<h2 class="pdoc-module-header" id="VpcLink">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L9">class VpcLink</a>
</h2>

Provides an API Gateway VPC Link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L33">constructor</a>
</h3>

```typescript
new VpcLink(name: string, args: VpcLinkArgs, opts?: pulumi.ResourceOptions)
```


Create a VpcLink resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new VpcLink(name: string, state?: VpcLinkState, opts?: pulumi.ResourceOptions)
```


Create a VpcLink resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcLinkState): VpcLink
```


Get an existing VpcLink resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L25">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the VPC link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name used to label and identify the VPC link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L33">property targetArn</a>
</h3>

```typescript
public targetArn: pulumi.Output<string>;
```


The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/account.ts#L79">interface AccountArgs</a>
</h2>

The set of arguments for constructing a Account resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/account.ts#L85">property cloudwatchRoleArn</a>
</h3>

```typescript
cloudwatchRoleArn?: pulumi.Input<string>;
```


The ARN of an IAM role for CloudWatch (to allow logging & monitoring).
See more [in AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console).
Logging & monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.

<h2 class="pdoc-module-header" id="AccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/account.ts#L63">interface AccountState</a>
</h2>

Input properties used for looking up and filtering Account resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/account.ts#L69">property cloudwatchRoleArn</a>
</h3>

```typescript
cloudwatchRoleArn?: pulumi.Input<string>;
```


The ARN of an IAM role for CloudWatch (to allow logging & monitoring).
See more [in AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console).
Logging & monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/account.ts#L73">property throttleSettings</a>
</h3>

```typescript
throttleSettings?: pulumi.Input<{ ... }>;
```


Account-Level throttle settings. See exported fields below.

<h2 class="pdoc-module-header" id="ApiKeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L127">interface ApiKeyArgs</a>
</h2>

The set of arguments for constructing a ApiKey resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L131">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The API key description. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L135">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether the API key can be used by callers. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L139">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L143">property stageKeys</a>
</h3>

```typescript
stageKeys?: pulumi.Input<{ ... }[]>;
```


A list of stage keys associated with the API key - see below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L147">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


The value of the API key. If not specified, it will be automatically generated by AWS on creation.

<h2 class="pdoc-module-header" id="ApiKeyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L93">interface ApiKeyState</a>
</h2>

Input properties used for looking up and filtering ApiKey resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L97">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The creation date of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L101">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The API key description. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L105">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether the API key can be used by callers. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L109">property lastUpdatedDate</a>
</h3>

```typescript
lastUpdatedDate?: pulumi.Input<string>;
```


The last update date of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L117">property stageKeys</a>
</h3>

```typescript
stageKeys?: pulumi.Input<{ ... }[]>;
```


A list of stage keys associated with the API key - see below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/apiKey.ts#L121">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


The value of the API key. If not specified, it will be automatically generated by AWS on creation.

<h2 class="pdoc-module-header" id="AuthorizerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L168">interface AuthorizerArgs</a>
</h2>

The set of arguments for constructing a Authorizer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L173">property authorizerCredentials</a>
</h3>

```typescript
authorizerCredentials?: pulumi.Input<string>;
```


The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L178">property authorizerResultTtlInSeconds</a>
</h3>

```typescript
authorizerResultTtlInSeconds?: pulumi.Input<number>;
```


The TTL of cached authorizer results in seconds.
Defaults to `300`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L184">property authorizerUri</a>
</h3>

```typescript
authorizerUri?: pulumi.Input<string>;
```


The authorizer's Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L189">property identitySource</a>
</h3>

```typescript
identitySource?: pulumi.Input<string>;
```


The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L196">property identityValidationExpression</a>
</h3>

```typescript
identityValidationExpression?: pulumi.Input<string>;
```


A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn't match,
the client receives a 401 Unauthorized response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L200">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the authorizer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L205">property providerArns</a>
</h3>

```typescript
providerArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L209">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L214">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.

<h2 class="pdoc-module-header" id="AuthorizerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L116">interface AuthorizerState</a>
</h2>

Input properties used for looking up and filtering Authorizer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L121">property authorizerCredentials</a>
</h3>

```typescript
authorizerCredentials?: pulumi.Input<string>;
```


The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L126">property authorizerResultTtlInSeconds</a>
</h3>

```typescript
authorizerResultTtlInSeconds?: pulumi.Input<number>;
```


The TTL of cached authorizer results in seconds.
Defaults to `300`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L132">property authorizerUri</a>
</h3>

```typescript
authorizerUri?: pulumi.Input<string>;
```


The authorizer's Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L137">property identitySource</a>
</h3>

```typescript
identitySource?: pulumi.Input<string>;
```


The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L144">property identityValidationExpression</a>
</h3>

```typescript
identityValidationExpression?: pulumi.Input<string>;
```


A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn't match,
the client receives a 401 Unauthorized response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L148">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the authorizer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L153">property providerArns</a>
</h3>

```typescript
providerArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L157">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/authorizer.ts#L162">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.

<h2 class="pdoc-module-header" id="BasePathMappingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L103">interface BasePathMappingArgs</a>
</h2>

The set of arguments for constructing a BasePathMapping resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L111">property basePath</a>
</h3>

```typescript
basePath?: pulumi.Input<string>;
```


Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L115">property domainName</a>
</h3>

```typescript
domainName: pulumi.Input<string>;
```


The already-registered domain name to connect the API to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L107">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The id of the API to connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L119">property stageName</a>
</h3>

```typescript
stageName?: pulumi.Input<string>;
```


The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.

<h2 class="pdoc-module-header" id="BasePathMappingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L81">interface BasePathMappingState</a>
</h2>

Input properties used for looking up and filtering BasePathMapping resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L89">property basePath</a>
</h3>

```typescript
basePath?: pulumi.Input<string>;
```


Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L93">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


The already-registered domain name to connect the API to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L85">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The id of the API to connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/basePathMapping.ts#L97">property stageName</a>
</h3>

```typescript
stageName?: pulumi.Input<string>;
```


The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.

<h2 class="pdoc-module-header" id="ClientCertificateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L93">interface ClientCertificateArgs</a>
</h2>

The set of arguments for constructing a ClientCertificate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L97">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the client certificate.

<h2 class="pdoc-module-header" id="ClientCertificateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L71">interface ClientCertificateState</a>
</h2>

Input properties used for looking up and filtering ClientCertificate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L75">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The date when the client certificate was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L79">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the client certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L83">property expirationDate</a>
</h3>

```typescript
expirationDate?: pulumi.Input<string>;
```


The date when the client certificate will expire.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/clientCertificate.ts#L87">property pemEncodedCertificate</a>
</h3>

```typescript
pemEncodedCertificate?: pulumi.Input<string>;
```


The PEM-encoded public key of the client certificate.

<h2 class="pdoc-module-header" id="DeploymentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L150">interface DeploymentArgs</a>
</h2>

The set of arguments for constructing a Deployment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L154">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L158">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L162">property stageDescription</a>
</h3>

```typescript
stageDescription?: pulumi.Input<string>;
```


The description of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L166">property stageName</a>
</h3>

```typescript
stageName: pulumi.Input<string>;
```


The name of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L170">property variables</a>
</h3>

```typescript
variables?: pulumi.Input<{ ... }>;
```


A map that defines variables for the stage

<h2 class="pdoc-module-header" id="DeploymentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L109">interface DeploymentState</a>
</h2>

Input properties used for looking up and filtering Deployment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L113">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The creation date of the deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L117">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L123">property executionArn</a>
</h3>

```typescript
executionArn?: pulumi.Input<string>;
```


The execution ARN to be used in [`lambda_permission`](/docs/providers/aws/r/lambda_permission.html)'s `source_arn`
when allowing API Gateway to invoke a Lambda function,
e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L128">property invokeUrl</a>
</h3>

```typescript
invokeUrl?: pulumi.Input<string>;
```


The URL to invoke the API pointing to the stage,
e.g. `https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L132">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L136">property stageDescription</a>
</h3>

```typescript
stageDescription?: pulumi.Input<string>;
```


The description of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L140">property stageName</a>
</h3>

```typescript
stageName?: pulumi.Input<string>;
```


The name of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/deployment.ts#L144">property variables</a>
</h3>

```typescript
variables?: pulumi.Input<{ ... }>;
```


A map that defines variables for the stage

<h2 class="pdoc-module-header" id="DocumentationPartArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L92">interface DocumentationPartArgs</a>
</h2>

The set of arguments for constructing a DocumentationPart resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L96">property location</a>
</h3>

```typescript
location: pulumi.Input<{ ... }>;
```


The location of the targeted API entity of the to-be-created documentation part. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L100">property properties</a>
</h3>

```typescript
properties: pulumi.Input<string>;
```


A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., "{ \"description\": \"The API does ...\" }". Only Swagger-compliant key-value pairs can be exported and, hence, published.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L104">property restApiId</a>
</h3>

```typescript
restApiId: pulumi.Input<string>;
```


The ID of the associated Rest API

<h2 class="pdoc-module-header" id="DocumentationPartState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L74">interface DocumentationPartState</a>
</h2>

Input properties used for looking up and filtering DocumentationPart resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L78">property location</a>
</h3>

```typescript
location?: pulumi.Input<{ ... }>;
```


The location of the targeted API entity of the to-be-created documentation part. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L82">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<string>;
```


A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., "{ \"description\": \"The API does ...\" }". Only Swagger-compliant key-value pairs can be exported and, hence, published.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationPart.ts#L86">property restApiId</a>
</h3>

```typescript
restApiId?: pulumi.Input<string>;
```


The ID of the associated Rest API

<h2 class="pdoc-module-header" id="DocumentationVersionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L89">interface DocumentationVersionArgs</a>
</h2>

The set of arguments for constructing a DocumentationVersion resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L93">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the API documentation version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L97">property restApiId</a>
</h3>

```typescript
restApiId: pulumi.Input<string>;
```


The ID of the associated Rest API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L101">property version</a>
</h3>

```typescript
version: pulumi.Input<string>;
```


The version identifier of the API documentation snapshot.

<h2 class="pdoc-module-header" id="DocumentationVersionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L71">interface DocumentationVersionState</a>
</h2>

Input properties used for looking up and filtering DocumentationVersion resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L75">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the API documentation version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L79">property restApiId</a>
</h3>

```typescript
restApiId?: pulumi.Input<string>;
```


The ID of the associated Rest API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/documentationVersion.ts#L83">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The version identifier of the API documentation snapshot.

<h2 class="pdoc-module-header" id="DomainNameArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L175">interface DomainNameArgs</a>
</h2>

The set of arguments for constructing a DomainName resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L179">property certificateArn</a>
</h3>

```typescript
certificateArn?: pulumi.Input<string>;
```


The ARN for an AWS-managed certificate. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain` and `certificate_private_key`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L184">property certificateBody</a>
</h3>

```typescript
certificateBody?: pulumi.Input<string>;
```


The certificate issued for the domain name
being registered, in PEM format. Conflicts with `certificate_arn`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L190">property certificateChain</a>
</h3>

```typescript
certificateChain?: pulumi.Input<string>;
```


The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Conflicts with `certificate_arn`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L195">property certificateName</a>
</h3>

```typescript
certificateName?: pulumi.Input<string>;
```


The unique name to use when registering this
cert as an IAM server certificate. Conflicts with `certificate_arn`. Required if `certificate_arn` is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L200">property certificatePrivateKey</a>
</h3>

```typescript
certificatePrivateKey?: pulumi.Input<string>;
```


The private key associated with the
domain certificate given in `certificate_body`. Conflicts with `certificate_arn`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L204">property domainName</a>
</h3>

```typescript
domainName: pulumi.Input<string>;
```


The fully-qualified domain name to register

<h2 class="pdoc-module-header" id="DomainNameState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L126">interface DomainNameState</a>
</h2>

Input properties used for looking up and filtering DomainName resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L130">property certificateArn</a>
</h3>

```typescript
certificateArn?: pulumi.Input<string>;
```


The ARN for an AWS-managed certificate. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain` and `certificate_private_key`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L135">property certificateBody</a>
</h3>

```typescript
certificateBody?: pulumi.Input<string>;
```


The certificate issued for the domain name
being registered, in PEM format. Conflicts with `certificate_arn`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L141">property certificateChain</a>
</h3>

```typescript
certificateChain?: pulumi.Input<string>;
```


The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Conflicts with `certificate_arn`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L146">property certificateName</a>
</h3>

```typescript
certificateName?: pulumi.Input<string>;
```


The unique name to use when registering this
cert as an IAM server certificate. Conflicts with `certificate_arn`. Required if `certificate_arn` is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L151">property certificatePrivateKey</a>
</h3>

```typescript
certificatePrivateKey?: pulumi.Input<string>;
```


The private key associated with the
domain certificate given in `certificate_body`. Conflicts with `certificate_arn`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L155">property certificateUploadDate</a>
</h3>

```typescript
certificateUploadDate?: pulumi.Input<string>;
```


The upload date associated with the domain certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L160">property cloudfrontDomainName</a>
</h3>

```typescript
cloudfrontDomainName?: pulumi.Input<string>;
```


The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L165">property cloudfrontZoneId</a>
</h3>

```typescript
cloudfrontZoneId?: pulumi.Input<string>;
```


For convenience, the hosted zone id (`Z2FDTNDATAQYW2`)
that can be used to create a Route53 alias record for the distribution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/domainName.ts#L169">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


The fully-qualified domain name to register

<h2 class="pdoc-module-header" id="IntegrationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L223">interface IntegrationArgs</a>
</h2>

The set of arguments for constructing a Integration resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L227">property cacheKeyParameters</a>
</h3>

```typescript
cacheKeyParameters?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of cache key parameters for the integration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L231">property cacheNamespace</a>
</h3>

```typescript
cacheNamespace?: pulumi.Input<string>;
```


The integration's cache namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L235">property contentHandling</a>
</h3>

```typescript
contentHandling?: pulumi.Input<string>;
```


Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L239">property credentials</a>
</h3>

```typescript
credentials?: pulumi.Input<string>;
```


The credentials required for the integration. For `AWS` integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role's ARN. To require that the caller's identity be passed through from the request, specify the string `arn:aws:iam::\*:user/\*`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L244">property httpMethod</a>
</h3>

```typescript
httpMethod: pulumi.Input<string>;
```


The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`, `ANY`)
when calling the associated resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L252">property integrationHttpMethod</a>
</h3>

```typescript
integrationHttpMethod?: pulumi.Input<string>;
```


The integration HTTP method
(`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`) specifying how API Gateway will interact with the back end.
**Required** if `type` is `AWS`, `AWS_PROXY`, `HTTP` or `HTTP_PROXY`.
Not all methods are compatible with all `AWS` integrations.
e.g. Lambda function [can only be invoked](https://github.com/awslabs/aws-apigateway-importer/issues/9#issuecomment-129651005) via `POST`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L256">property passthroughBehavior</a>
</h3>

```typescript
passthroughBehavior?: pulumi.Input<string>;
```


The integration passthrough behavior (`WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`).  **Required** if `request_templates` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L261">property requestParameters</a>
</h3>

```typescript
requestParameters?: pulumi.Input<{ ... }>;
```


A map of request query string parameters and headers that should be passed to the backend responder.
For example: `request_parameters = { "integration.request.header.X-Some-Other-Header" = "method.request.header.X-Some-Header" }`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L265">property requestParametersInJson</a>
</h3>

```typescript
requestParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `request_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L269">property requestTemplates</a>
</h3>

```typescript
requestTemplates?: pulumi.Input<{ ... }>;
```


A map of the integration's request templates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L273">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The API resource ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L277">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L281">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The integration input's [type](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/). Valid values are `HTTP` (for HTTP backends), `MOCK` (not calling any real backend), `AWS` (for AWS services), `AWS_PROXY` (for Lambda proxy integration) and `HTTP_PROXY` (for HTTP proxy integration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L287">property uri</a>
</h3>

```typescript
uri?: pulumi.Input<string>;
```


The input's URI (HTTP, AWS). **Required** if `type` is `HTTP` or `AWS`.
For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form `arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}`. `region`, `subdomain` and `service` are used to determine the right endpoint.
e.g. `arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations`

<h2 class="pdoc-module-header" id="IntegrationResponseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L168">interface IntegrationResponseArgs</a>
</h2>

The set of arguments for constructing a IntegrationResponse resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L172">property contentHandling</a>
</h3>

```typescript
contentHandling?: pulumi.Input<string>;
```


Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L176">property httpMethod</a>
</h3>

```typescript
httpMethod: pulumi.Input<string>;
```


The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L180">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L185">property responseParameters</a>
</h3>

```typescript
responseParameters?: pulumi.Input<{ ... }>;
```


A map of response parameters that can be read from the backend response.
For example: `response_parameters = { "method.response.header.X-Some-Header" = "integration.response.header.X-Some-Other-Header" }`,

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L189">property responseParametersInJson</a>
</h3>

```typescript
responseParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `response_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L193">property responseTemplates</a>
</h3>

```typescript
responseTemplates?: pulumi.Input<{ ... }>;
```


A map specifying the templates used to transform the integration response body

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L197">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L204">property selectionPattern</a>
</h3>

```typescript
selectionPattern?: pulumi.Input<string>;
```


Specifies the regular expression pattern used to choose
an integration response based on the response from the backend. Setting this to `-` makes the integration the default one.
If the backend is an `AWS` Lambda function, the AWS Lambda function error header is matched.
For all other `HTTP` and `AWS` backends, the HTTP status code is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L208">property statusCode</a>
</h3>

```typescript
statusCode: pulumi.Input<string>;
```


The HTTP status code

<h2 class="pdoc-module-header" id="IntegrationResponseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L122">interface IntegrationResponseState</a>
</h2>

Input properties used for looking up and filtering IntegrationResponse resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L126">property contentHandling</a>
</h3>

```typescript
contentHandling?: pulumi.Input<string>;
```


Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L130">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L134">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L139">property responseParameters</a>
</h3>

```typescript
responseParameters?: pulumi.Input<{ ... }>;
```


A map of response parameters that can be read from the backend response.
For example: `response_parameters = { "method.response.header.X-Some-Header" = "integration.response.header.X-Some-Other-Header" }`,

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L143">property responseParametersInJson</a>
</h3>

```typescript
responseParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `response_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L147">property responseTemplates</a>
</h3>

```typescript
responseTemplates?: pulumi.Input<{ ... }>;
```


A map specifying the templates used to transform the integration response body

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L151">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L158">property selectionPattern</a>
</h3>

```typescript
selectionPattern?: pulumi.Input<string>;
```


Specifies the regular expression pattern used to choose
an integration response based on the response from the backend. Setting this to `-` makes the integration the default one.
If the backend is an `AWS` Lambda function, the AWS Lambda function error header is matched.
For all other `HTTP` and `AWS` backends, the HTTP status code is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integrationResponse.ts#L162">property statusCode</a>
</h3>

```typescript
statusCode?: pulumi.Input<string>;
```


The HTTP status code

<h2 class="pdoc-module-header" id="IntegrationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L153">interface IntegrationState</a>
</h2>

Input properties used for looking up and filtering Integration resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L157">property cacheKeyParameters</a>
</h3>

```typescript
cacheKeyParameters?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of cache key parameters for the integration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L161">property cacheNamespace</a>
</h3>

```typescript
cacheNamespace?: pulumi.Input<string>;
```


The integration's cache namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L165">property contentHandling</a>
</h3>

```typescript
contentHandling?: pulumi.Input<string>;
```


Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L169">property credentials</a>
</h3>

```typescript
credentials?: pulumi.Input<string>;
```


The credentials required for the integration. For `AWS` integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role's ARN. To require that the caller's identity be passed through from the request, specify the string `arn:aws:iam::\*:user/\*`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L174">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`, `ANY`)
when calling the associated resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L182">property integrationHttpMethod</a>
</h3>

```typescript
integrationHttpMethod?: pulumi.Input<string>;
```


The integration HTTP method
(`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`) specifying how API Gateway will interact with the back end.
**Required** if `type` is `AWS`, `AWS_PROXY`, `HTTP` or `HTTP_PROXY`.
Not all methods are compatible with all `AWS` integrations.
e.g. Lambda function [can only be invoked](https://github.com/awslabs/aws-apigateway-importer/issues/9#issuecomment-129651005) via `POST`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L186">property passthroughBehavior</a>
</h3>

```typescript
passthroughBehavior?: pulumi.Input<string>;
```


The integration passthrough behavior (`WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`).  **Required** if `request_templates` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L191">property requestParameters</a>
</h3>

```typescript
requestParameters?: pulumi.Input<{ ... }>;
```


A map of request query string parameters and headers that should be passed to the backend responder.
For example: `request_parameters = { "integration.request.header.X-Some-Other-Header" = "method.request.header.X-Some-Header" }`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L195">property requestParametersInJson</a>
</h3>

```typescript
requestParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `request_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L199">property requestTemplates</a>
</h3>

```typescript
requestTemplates?: pulumi.Input<{ ... }>;
```


A map of the integration's request templates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L203">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The API resource ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L207">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L211">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The integration input's [type](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/). Valid values are `HTTP` (for HTTP backends), `MOCK` (not calling any real backend), `AWS` (for AWS services), `AWS_PROXY` (for Lambda proxy integration) and `HTTP_PROXY` (for HTTP proxy integration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/integration.ts#L217">property uri</a>
</h3>

```typescript
uri?: pulumi.Input<string>;
```


The input's URI (HTTP, AWS). **Required** if `type` is `HTTP` or `AWS`.
For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form `arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}`. `region`, `subdomain` and `service` are used to determine the right endpoint.
e.g. `arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations`

<h2 class="pdoc-module-header" id="MethodArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L187">interface MethodArgs</a>
</h2>

The set of arguments for constructing a Method resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L191">property apiKeyRequired</a>
</h3>

```typescript
apiKeyRequired?: pulumi.Input<boolean>;
```


Specify if the method requires an API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L195">property authorization</a>
</h3>

```typescript
authorization: pulumi.Input<string>;
```


The type of authorization used for the method (`NONE`, `CUSTOM`, `AWS_IAM`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L199">property authorizerId</a>
</h3>

```typescript
authorizerId?: pulumi.Input<string>;
```


The authorizer id to be used when the authorization is `CUSTOM`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L203">property httpMethod</a>
</h3>

```typescript
httpMethod: pulumi.Input<string>;
```


The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L209">property requestModels</a>
</h3>

```typescript
requestModels?: pulumi.Input<{ ... }>;
```


A map of the API models used for the request's content type
where key is the content type (e.g. `application/json`)
and value is either `Error`, `Empty` (built-in models) or `aws_api_gateway_model`'s `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L221">property requestParameters</a>
</h3>

```typescript
requestParameters?: pulumi.Input<{ ... }>;
```


A map of request query string parameters and headers that should be passed to the integration.
For example:
```hcl
request_parameters = {
"method.request.header.X-Some-Header" = true,
"method.request.querystring.some-query-param"  = true,
}
```
would define that the header `X-Some-Header` and the query string `some-query-param` must be provided on the request, or

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L225">property requestParametersInJson</a>
</h3>

```typescript
requestParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `request_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L229">property requestValidatorId</a>
</h3>

```typescript
requestValidatorId?: pulumi.Input<string>;
```


The ID of a `aws_api_gateway_request_validator`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L233">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L237">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h2 class="pdoc-module-header" id="MethodResponseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L141">interface MethodResponseArgs</a>
</h2>

The set of arguments for constructing a MethodResponse resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L145">property httpMethod</a>
</h3>

```typescript
httpMethod: pulumi.Input<string>;
```


The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L149">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L153">property responseModels</a>
</h3>

```typescript
responseModels?: pulumi.Input<{ ... }>;
```


A map of the API models used for the response's content type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L159">property responseParameters</a>
</h3>

```typescript
responseParameters?: pulumi.Input<{ ... }>;
```


A map of response parameters that can be sent to the caller.
For example: `response_parameters = { "method.response.header.X-Some-Header" = true }`
would define that the header `X-Some-Header` can be provided on the response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L163">property responseParametersInJson</a>
</h3>

```typescript
responseParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `response_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L167">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L171">property statusCode</a>
</h3>

```typescript
statusCode: pulumi.Input<string>;
```


The HTTP status code

<h2 class="pdoc-module-header" id="MethodResponseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L105">interface MethodResponseState</a>
</h2>

Input properties used for looking up and filtering MethodResponse resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L109">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L113">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L117">property responseModels</a>
</h3>

```typescript
responseModels?: pulumi.Input<{ ... }>;
```


A map of the API models used for the response's content type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L123">property responseParameters</a>
</h3>

```typescript
responseParameters?: pulumi.Input<{ ... }>;
```


A map of response parameters that can be sent to the caller.
For example: `response_parameters = { "method.response.header.X-Some-Header" = true }`
would define that the header `X-Some-Header` can be provided on the response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L127">property responseParametersInJson</a>
</h3>

```typescript
responseParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `response_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L131">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodResponse.ts#L135">property statusCode</a>
</h3>

```typescript
statusCode?: pulumi.Input<string>;
```


The HTTP status code

<h2 class="pdoc-module-header" id="MethodSettingsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L107">interface MethodSettingsArgs</a>
</h2>

The set of arguments for constructing a MethodSettings resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L111">property methodPath</a>
</h3>

```typescript
methodPath: pulumi.Input<string>;
```


Method path defined as `{resource_path}/{http_method}` for an individual method override, or `*&#47;*` for overriding all methods in the stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L115">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L119">property settings</a>
</h3>

```typescript
settings: pulumi.Input<{ ... }>;
```


The settings block, see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L123">property stageName</a>
</h3>

```typescript
stageName: pulumi.Input<string>;
```


The name of the stage

<h2 class="pdoc-module-header" id="MethodSettingsState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L85">interface MethodSettingsState</a>
</h2>

Input properties used for looking up and filtering MethodSettings resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L89">property methodPath</a>
</h3>

```typescript
methodPath?: pulumi.Input<string>;
```


Method path defined as `{resource_path}/{http_method}` for an individual method override, or `*&#47;*` for overriding all methods in the stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L93">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L97">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<{ ... }>;
```


The settings block, see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/methodSettings.ts#L101">property stageName</a>
</h3>

```typescript
stageName?: pulumi.Input<string>;
```


The name of the stage

<h2 class="pdoc-module-header" id="MethodState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L131">interface MethodState</a>
</h2>

Input properties used for looking up and filtering Method resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L135">property apiKeyRequired</a>
</h3>

```typescript
apiKeyRequired?: pulumi.Input<boolean>;
```


Specify if the method requires an API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L139">property authorization</a>
</h3>

```typescript
authorization?: pulumi.Input<string>;
```


The type of authorization used for the method (`NONE`, `CUSTOM`, `AWS_IAM`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L143">property authorizerId</a>
</h3>

```typescript
authorizerId?: pulumi.Input<string>;
```


The authorizer id to be used when the authorization is `CUSTOM`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L147">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L153">property requestModels</a>
</h3>

```typescript
requestModels?: pulumi.Input<{ ... }>;
```


A map of the API models used for the request's content type
where key is the content type (e.g. `application/json`)
and value is either `Error`, `Empty` (built-in models) or `aws_api_gateway_model`'s `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L165">property requestParameters</a>
</h3>

```typescript
requestParameters?: pulumi.Input<{ ... }>;
```


A map of request query string parameters and headers that should be passed to the integration.
For example:
```hcl
request_parameters = {
"method.request.header.X-Some-Header" = true,
"method.request.querystring.some-query-param"  = true,
}
```
would define that the header `X-Some-Header` and the query string `some-query-param` must be provided on the request, or

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L169">property requestParametersInJson</a>
</h3>

```typescript
requestParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `request_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L173">property requestValidatorId</a>
</h3>

```typescript
requestValidatorId?: pulumi.Input<string>;
```


The ID of a `aws_api_gateway_request_validator`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L177">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/method.ts#L181">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h2 class="pdoc-module-header" id="ModelArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L111">interface ModelArgs</a>
</h2>

The set of arguments for constructing a Model resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L115">property contentType</a>
</h3>

```typescript
contentType: pulumi.Input<string>;
```


The content type of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L119">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L127">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L131">property schema</a>
</h3>

```typescript
schema?: pulumi.Input<string>;
```


The schema of the model in a JSON form

<h2 class="pdoc-module-header" id="ModelState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L85">interface ModelState</a>
</h2>

Input properties used for looking up and filtering Model resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L89">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


The content type of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L93">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L101">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/model.ts#L105">property schema</a>
</h3>

```typescript
schema?: pulumi.Input<string>;
```


The schema of the model in a JSON form

<h2 class="pdoc-module-header" id="RequestValidatorArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L71">interface RequestValidatorArgs</a>
</h2>

The set of arguments for constructing a RequestValidator resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L72">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L73">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L74">property validateRequestBody</a>
</h3>

```typescript
validateRequestBody?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L75">property validateRequestParameters</a>
</h3>

```typescript
validateRequestParameters?: pulumi.Input<boolean>;
```

<h2 class="pdoc-module-header" id="RequestValidatorState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L61">interface RequestValidatorState</a>
</h2>

Input properties used for looking up and filtering RequestValidator resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L62">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L63">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L64">property validateRequestBody</a>
</h3>

```typescript
validateRequestBody?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/requestValidator.ts#L65">property validateRequestParameters</a>
</h3>

```typescript
validateRequestParameters?: pulumi.Input<boolean>;
```

<h2 class="pdoc-module-header" id="ResourceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L104">interface ResourceArgs</a>
</h2>

The set of arguments for constructing a Resource resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L108">property parentId</a>
</h3>

```typescript
parentId: pulumi.Input<string>;
```


The ID of the parent API resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L112">property pathPart</a>
</h3>

```typescript
pathPart: pulumi.Input<string>;
```


The last path segment of this API resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L116">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h2 class="pdoc-module-header" id="ResourceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L82">interface ResourceState</a>
</h2>

Input properties used for looking up and filtering Resource resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L86">property parentId</a>
</h3>

```typescript
parentId?: pulumi.Input<string>;
```


The ID of the parent API resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L90">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


The complete path for this API resource, including all parent paths.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L94">property pathPart</a>
</h3>

```typescript
pathPart?: pulumi.Input<string>;
```


The last path segment of this API resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/resource.ts#L98">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h2 class="pdoc-module-header" id="ResponseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L109">interface ResponseArgs</a>
</h2>

The set of arguments for constructing a Response resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L113">property responseParameters</a>
</h3>

```typescript
responseParameters?: pulumi.Input<{ ... }>;
```


A map specifying the templates used to transform the response body.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L117">property responseTemplates</a>
</h3>

```typescript
responseTemplates?: pulumi.Input<{ ... }>;
```


A map specifying the parameters (paths, query strings and headers) of the Gateway Response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L121">property responseType</a>
</h3>

```typescript
responseType: pulumi.Input<string>;
```


The response type of the associated GatewayResponse.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L125">property restApiId</a>
</h3>

```typescript
restApiId: pulumi.Input<string>;
```


The string identifier of the associated REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L129">property statusCode</a>
</h3>

```typescript
statusCode?: pulumi.Input<string>;
```


The HTTP status code of the Gateway Response.

<h2 class="pdoc-module-header" id="ResponseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L83">interface ResponseState</a>
</h2>

Input properties used for looking up and filtering Response resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L87">property responseParameters</a>
</h3>

```typescript
responseParameters?: pulumi.Input<{ ... }>;
```


A map specifying the templates used to transform the response body.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L91">property responseTemplates</a>
</h3>

```typescript
responseTemplates?: pulumi.Input<{ ... }>;
```


A map specifying the parameters (paths, query strings and headers) of the Gateway Response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L95">property responseType</a>
</h3>

```typescript
responseType?: pulumi.Input<string>;
```


The response type of the associated GatewayResponse.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L99">property restApiId</a>
</h3>

```typescript
restApiId?: pulumi.Input<string>;
```


The string identifier of the associated REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/response.ts#L103">property statusCode</a>
</h3>

```typescript
statusCode?: pulumi.Input<string>;
```


The HTTP status code of the Gateway Response.

<h2 class="pdoc-module-header" id="RestApiArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L123">interface RestApiArgs</a>
</h2>

The set of arguments for constructing a RestApi resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L127">property binaryMediaTypes</a>
</h3>

```typescript
binaryMediaTypes?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L131">property body</a>
</h3>

```typescript
body?: pulumi.Input<string>;
```


An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L135">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L139">property minimumCompressionSize</a>
</h3>

```typescript
minimumCompressionSize?: pulumi.Input<number>;
```


Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L143">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the REST API

<h2 class="pdoc-module-header" id="RestApiState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L89">interface RestApiState</a>
</h2>

Input properties used for looking up and filtering RestApi resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L93">property binaryMediaTypes</a>
</h3>

```typescript
binaryMediaTypes?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L97">property body</a>
</h3>

```typescript
body?: pulumi.Input<string>;
```


An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L101">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The creation date of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L105">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L109">property minimumCompressionSize</a>
</h3>

```typescript
minimumCompressionSize?: pulumi.Input<number>;
```


Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/restApi.ts#L117">property rootResourceId</a>
</h3>

```typescript
rootResourceId?: pulumi.Input<string>;
```


The resource ID of the REST API's root

<h2 class="pdoc-module-header" id="StageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L157">interface StageArgs</a>
</h2>

The set of arguments for constructing a Stage resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L161">property cacheClusterEnabled</a>
</h3>

```typescript
cacheClusterEnabled?: pulumi.Input<boolean>;
```


Specifies whether a cache cluster is enabled for the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L166">property cacheClusterSize</a>
</h3>

```typescript
cacheClusterSize?: pulumi.Input<string>;
```


The size of the cache cluster for the stage, if enabled.
Allowed values include `0.5`, `1.6`, `6.1`, `13.5`, `28.4`, `58.2`, `118` and `237`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L170">property clientCertificateId</a>
</h3>

```typescript
clientCertificateId?: pulumi.Input<string>;
```


The identifier of a client certificate for the stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L174">property deployment</a>
</h3>

```typescript
deployment: pulumi.Input<Deployment>;
```


The ID of the deployment that the stage points to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L178">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L182">property documentationVersion</a>
</h3>

```typescript
documentationVersion?: pulumi.Input<string>;
```


The version of the associated API documentation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L186">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L190">property stageName</a>
</h3>

```typescript
stageName: pulumi.Input<string>;
```


The name of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L194">property variables</a>
</h3>

```typescript
variables?: pulumi.Input<{ ... }>;
```


A map that defines the stage variables

<h2 class="pdoc-module-header" id="StageState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L114">interface StageState</a>
</h2>

Input properties used for looking up and filtering Stage resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L118">property cacheClusterEnabled</a>
</h3>

```typescript
cacheClusterEnabled?: pulumi.Input<boolean>;
```


Specifies whether a cache cluster is enabled for the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L123">property cacheClusterSize</a>
</h3>

```typescript
cacheClusterSize?: pulumi.Input<string>;
```


The size of the cache cluster for the stage, if enabled.
Allowed values include `0.5`, `1.6`, `6.1`, `13.5`, `28.4`, `58.2`, `118` and `237`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L127">property clientCertificateId</a>
</h3>

```typescript
clientCertificateId?: pulumi.Input<string>;
```


The identifier of a client certificate for the stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L131">property deployment</a>
</h3>

```typescript
deployment?: pulumi.Input<Deployment>;
```


The ID of the deployment that the stage points to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L135">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L139">property documentationVersion</a>
</h3>

```typescript
documentationVersion?: pulumi.Input<string>;
```


The version of the associated API documentation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L143">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L147">property stageName</a>
</h3>

```typescript
stageName?: pulumi.Input<string>;
```


The name of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/stage.ts#L151">property variables</a>
</h3>

```typescript
variables?: pulumi.Input<{ ... }>;
```


A map that defines the stage variables

<h2 class="pdoc-module-header" id="UsagePlanArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L113">interface UsagePlanArgs</a>
</h2>

The set of arguments for constructing a UsagePlan resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L117">property apiStages</a>
</h3>

```typescript
apiStages?: pulumi.Input<{ ... }[]>;
```


The associated [API stages](#api-stages-arguments) of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L121">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of a usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L125">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L129">property productCode</a>
</h3>

```typescript
productCode?: pulumi.Input<string>;
```


The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L133">property quotaSettings</a>
</h3>

```typescript
quotaSettings?: pulumi.Input<{ ... }>;
```


The [quota settings](#quota-settings-arguments) of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L137">property throttleSettings</a>
</h3>

```typescript
throttleSettings?: pulumi.Input<{ ... }>;
```


The [throttling limits](#throttling-settings-arguments) of the usage plan.

<h2 class="pdoc-module-header" id="UsagePlanKeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L112">interface UsagePlanKeyArgs</a>
</h2>

The set of arguments for constructing a UsagePlanKey resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L116">property keyId</a>
</h3>

```typescript
keyId: pulumi.Input<string>;
```


The identifier of the API key resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L120">property keyType</a>
</h3>

```typescript
keyType: pulumi.Input<string>;
```


The type of the API key resource. Currently, the valid key type is API_KEY.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L124">property usagePlanId</a>
</h3>

```typescript
usagePlanId: pulumi.Input<string>;
```


The Id of the usage plan resource representing to associate the key to.

<h2 class="pdoc-module-header" id="UsagePlanKeyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L86">interface UsagePlanKeyState</a>
</h2>

Input properties used for looking up and filtering UsagePlanKey resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L90">property keyId</a>
</h3>

```typescript
keyId?: pulumi.Input<string>;
```


The identifier of the API key resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L94">property keyType</a>
</h3>

```typescript
keyType?: pulumi.Input<string>;
```


The type of the API key resource. Currently, the valid key type is API_KEY.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of a usage plan key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L102">property usagePlanId</a>
</h3>

```typescript
usagePlanId?: pulumi.Input<string>;
```


The Id of the usage plan resource representing to associate the key to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlanKey.ts#L106">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


The value of a usage plan key.

<h2 class="pdoc-module-header" id="UsagePlanState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L83">interface UsagePlanState</a>
</h2>

Input properties used for looking up and filtering UsagePlan resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L87">property apiStages</a>
</h3>

```typescript
apiStages?: pulumi.Input<{ ... }[]>;
```


The associated [API stages](#api-stages-arguments) of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L91">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of a usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L99">property productCode</a>
</h3>

```typescript
productCode?: pulumi.Input<string>;
```


The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L103">property quotaSettings</a>
</h3>

```typescript
quotaSettings?: pulumi.Input<{ ... }>;
```


The [quota settings](#quota-settings-arguments) of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/usagePlan.ts#L107">property throttleSettings</a>
</h3>

```typescript
throttleSettings?: pulumi.Input<{ ... }>;
```


The [throttling limits](#throttling-settings-arguments) of the usage plan.

<h2 class="pdoc-module-header" id="VpcLinkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L86">interface VpcLinkArgs</a>
</h2>

The set of arguments for constructing a VpcLink resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L90">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the VPC link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name used to label and identify the VPC link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L98">property targetArn</a>
</h3>

```typescript
targetArn: pulumi.Input<pulumi.Input<string>>;
```


The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.

<h2 class="pdoc-module-header" id="VpcLinkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L68">interface VpcLinkState</a>
</h2>

Input properties used for looking up and filtering VpcLink resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L72">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the VPC link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name used to label and identify the VPC link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/apigateway/vpcLink.ts#L80">property targetArn</a>
</h3>

```typescript
targetArn?: pulumi.Input<pulumi.Input<string>>;
```


The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.

