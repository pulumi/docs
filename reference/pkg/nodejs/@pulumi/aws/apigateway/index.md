---
title: Module apigateway
---

<a href="../index.html">@pulumi/aws</a> &gt; apigateway

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
* <a href="#getKey">function getKey</a>
* <a href="#getResource">function getResource</a>
* <a href="#getRestApi">function getRestApi</a>
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
* <a href="#GetKeyArgs">interface GetKeyArgs</a>
* <a href="#GetKeyResult">interface GetKeyResult</a>
* <a href="#GetResourceArgs">interface GetResourceArgs</a>
* <a href="#GetResourceResult">interface GetResourceResult</a>
* <a href="#GetRestApiArgs">interface GetRestApiArgs</a>
* <a href="#GetRestApiResult">interface GetRestApiResult</a>
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

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/account.ts">apigateway/account.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts">apigateway/apiKey.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts">apigateway/authorizer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts">apigateway/basePathMapping.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts">apigateway/clientCertificate.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts">apigateway/deployment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts">apigateway/documentationPart.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts">apigateway/documentationVersion.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts">apigateway/domainName.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getKey.ts">apigateway/getKey.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getResource.ts">apigateway/getResource.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getRestApi.ts">apigateway/getRestApi.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts">apigateway/integration.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts">apigateway/integrationResponse.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts">apigateway/method.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts">apigateway/methodResponse.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts">apigateway/methodSettings.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts">apigateway/model.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts">apigateway/requestValidator.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts">apigateway/resource.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts">apigateway/response.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts">apigateway/restApi.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts">apigateway/stage.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts">apigateway/usagePlan.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts">apigateway/usagePlanKey.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts">apigateway/vpcLink.ts</a> 


<h2 class="pdoc-module-header" id="Account">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/account.ts#L12">class Account</a>
</h2>

Provides a settings of an API Gateway Account. Settings is applied region-wide per `provider` block.

-> **Note:** As there is no API method for deleting account settings or resetting it to defaults, destroying this resource will keep your account settings intact

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/account.ts#L34">constructor</a>
</h3>

```typescript
new Account(name: string, args?: AccountArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/account.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountState): Account
```


Get an existing Account resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/account.ts#L30">property cloudwatchRoleArn</a>
</h3>

```typescript
public cloudwatchRoleArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM role for CloudWatch (to allow logging & monitoring).
See more [in AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console).
Logging & monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/account.ts#L34">property throttleSettings</a>
</h3>

```typescript
public throttleSettings: pulumi.Output<{ ... }>;
```


Account-Level throttle settings. See exported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ApiKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L14">class ApiKey</a>
</h2>

Provides an API Gateway API Key.

~> **Warning:** Since the API Gateway usage plans feature was launched on August 11, 2016, usage plans are now **required** to associate an API key with an API stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L54">constructor</a>
</h3>

```typescript
new ApiKey(name: string, args?: ApiKeyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ApiKey resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApiKeyState): ApiKey
```


Get an existing ApiKey resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L30">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The creation date of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L34">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The API key description. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L38">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Specifies whether the API key can be used by callers. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L42">property lastUpdatedDate</a>
</h3>

```typescript
public lastUpdatedDate: pulumi.Output<string>;
```


The last update date of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L50">property stageKeys</a>
</h3>

```typescript
public stageKeys: pulumi.Output<{ ... }[] | undefined>;
```


A list of stage keys associated with the API key - see below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L54">property value</a>
</h3>

```typescript
public value: pulumi.Output<string>;
```


The value of the API key. If not specified, it will be automatically generated by AWS on creation.

<h2 class="pdoc-module-header" id="Authorizer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L12">class Authorizer</a>
</h2>

Provides an API Gateway Authorizer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L70">constructor</a>
</h3>

```typescript
new Authorizer(name: string, args: AuthorizerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Authorizer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AuthorizerState): Authorizer
```


Get an existing Authorizer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L29">property authorizerCredentials</a>
</h3>

```typescript
public authorizerCredentials: pulumi.Output<string | undefined>;
```


The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L34">property authorizerResultTtlInSeconds</a>
</h3>

```typescript
public authorizerResultTtlInSeconds: pulumi.Output<number | undefined>;
```


The TTL of cached authorizer results in seconds.
Defaults to `300`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L40">property authorizerUri</a>
</h3>

```typescript
public authorizerUri: pulumi.Output<string | undefined>;
```


The authorizer's Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L45">property identitySource</a>
</h3>

```typescript
public identitySource: pulumi.Output<string | undefined>;
```


The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L52">property identityValidationExpression</a>
</h3>

```typescript
public identityValidationExpression: pulumi.Output<string | undefined>;
```


A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn't match,
the client receives a 401 Unauthorized response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L56">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the authorizer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L61">property providerArns</a>
</h3>

```typescript
public providerArns: pulumi.Output<string[] | undefined>;
```


A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L65">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L70">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```


The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="BasePathMapping">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L14">class BasePathMapping</a>
</h2>

Connects a custom domain name registered via `aws_api_gateway_domain_name`
with a deployed API so that its methods can be called via the
custom domain name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L42">constructor</a>
</h3>

```typescript
new BasePathMapping(name: string, args: BasePathMappingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a BasePathMapping resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BasePathMappingState): BasePathMapping
```


Get an existing BasePathMapping resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L34">property basePath</a>
</h3>

```typescript
public basePath: pulumi.Output<string | undefined>;
```


Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L38">property domainName</a>
</h3>

```typescript
public domainName: pulumi.Output<string>;
```


The already-registered domain name to connect the API to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L30">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The id of the API to connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L42">property stageName</a>
</h3>

```typescript
public stageName: pulumi.Output<string | undefined>;
```


The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ClientCertificate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L10">class ClientCertificate</a>
</h2>

Provides an API Gateway Client Certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L38">constructor</a>
</h3>

```typescript
new ClientCertificate(name: string, args?: ClientCertificateArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ClientCertificate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClientCertificateState): ClientCertificate
```


Get an existing ClientCertificate resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L26">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The date when the client certificate was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the client certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L34">property expirationDate</a>
</h3>

```typescript
public expirationDate: pulumi.Output<string>;
```


The date when the client certificate will expire.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L38">property pemEncodedCertificate</a>
</h3>

```typescript
public pemEncodedCertificate: pulumi.Output<string>;
```


The PEM-encoded public key of the client certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Deployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L15">class Deployment</a>
</h2>

Provides an API Gateway Deployment.

-> **Note:** Depends on having `aws_api_gateway_integration` inside your rest api (which in turn depends on `aws_api_gateway_method`). To avoid race conditions
you might need to add an explicit `depends_on = ["aws_api_gateway_integration.name"]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L62">constructor</a>
</h3>

```typescript
new Deployment(name: string, args: DeploymentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Deployment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DeploymentState): Deployment
```


Get an existing Deployment resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L31">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The creation date of the deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L35">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L41">property executionArn</a>
</h3>

```typescript
public executionArn: pulumi.Output<string>;
```


The execution ARN to be used in [`lambda_permission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `source_arn`
when allowing API Gateway to invoke a Lambda function,
e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L46">property invokeUrl</a>
</h3>

```typescript
public invokeUrl: pulumi.Output<string>;
```


The URL to invoke the API pointing to the stage,
e.g. `https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L50">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L54">property stageDescription</a>
</h3>

```typescript
public stageDescription: pulumi.Output<string | undefined>;
```


The description of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L58">property stageName</a>
</h3>

```typescript
public stageName: pulumi.Output<string>;
```


The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment. Use `""` to point at the default stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L62">property variables</a>
</h3>

```typescript
public variables: pulumi.Output<{ ... } | undefined>;
```


A map that defines variables for the stage

<h2 class="pdoc-module-header" id="DocumentationPart">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L10">class DocumentationPart</a>
</h2>

Provides a settings of an API Gateway Documentation Part.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L34">constructor</a>
</h3>

```typescript
new DocumentationPart(name: string, args: DocumentationPartArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DocumentationPart resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DocumentationPartState): DocumentationPart
```


Get an existing DocumentationPart resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<{ ... }>;
```


The location of the targeted API entity of the to-be-created documentation part. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L30">property properties</a>
</h3>

```typescript
public properties: pulumi.Output<string>;
```


A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., "{ \"description\": \"The API does ...\" }". Only Swagger-compliant key-value pairs can be exported and, hence, published.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L34">property restApiId</a>
</h3>

```typescript
public restApiId: pulumi.Output<string>;
```


The ID of the associated Rest API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DocumentationVersion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L10">class DocumentationVersion</a>
</h2>

Provides a resource to manage an API Gateway Documentation Version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L34">constructor</a>
</h3>

```typescript
new DocumentationVersion(name: string, args: DocumentationVersionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DocumentationVersion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DocumentationVersionState): DocumentationVersion
```


Get an existing DocumentationVersion resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the API documentation version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L30">property restApiId</a>
</h3>

```typescript
public restApiId: pulumi.Output<string>;
```


The ID of the associated Rest API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L34">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The version identifier of the API documentation snapshot.

<h2 class="pdoc-module-header" id="DomainName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L29">class DomainName</a>
</h2>

Registers a custom domain name for use with AWS API Gateway.

This resource just establishes ownership of and the TLS settings for
a particular domain name. An API can be attached to a particular path
under the registered domain name using
the `aws_api_gateway_base_path_mapping` resource.

API Gateway domains can be defined as either 'edge-optimized' or 'regional'.  In an edge-optimized configuration,
API Gateway internally creates and manages a CloudFront distribution to route requests on the given hostname. In
addition to this resource it's necessary to create a DNS record corresponding to the given domain name which is an alias
(either Route53 alias or traditional CNAME) to the Cloudfront domain name exported in the `cloudfront_domain_name`
attribute.

In a regional configuration, API Gateway does not create a CloudFront distribution to route requests to the API, though
a distribution can be created if needed. In either case, it is necessary to create a DNS record corresponding to the
given domain name which is an alias (either Route53 alias or traditional CNAME) to the regional domain name exported in
the `regional_domain_name` attribute.

~> **Note:** All arguments including the private key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L112">constructor</a>
</h3>

```typescript
new DomainName(name: string, args: DomainNameArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DomainName resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L38">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainNameState): DomainName
```


Get an existing DomainName resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L47">property certificateArn</a>
</h3>

```typescript
public certificateArn: pulumi.Output<string | undefined>;
```


The ARN for an AWS-managed certificate. Used when an edge-optimized domain name is
desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`,
`regional_certificate_arn`, and `regional_certificate_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L53">property certificateBody</a>
</h3>

```typescript
public certificateBody: pulumi.Output<string | undefined>;
```


The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L60">property certificateChain</a>
</h3>

```typescript
public certificateChain: pulumi.Output<string | undefined>;
```


The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L66">property certificateName</a>
</h3>

```typescript
public certificateName: pulumi.Output<string | undefined>;
```


The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L71">property certificatePrivateKey</a>
</h3>

```typescript
public certificatePrivateKey: pulumi.Output<string | undefined>;
```


The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L75">property certificateUploadDate</a>
</h3>

```typescript
public certificateUploadDate: pulumi.Output<string>;
```


The upload date associated with the domain certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L80">property cloudfrontDomainName</a>
</h3>

```typescript
public cloudfrontDomainName: pulumi.Output<string>;
```


The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L85">property cloudfrontZoneId</a>
</h3>

```typescript
public cloudfrontZoneId: pulumi.Output<string>;
```


For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
that can be used to create a Route53 alias record for the distribution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L89">property domainName</a>
</h3>

```typescript
public domainName: pulumi.Output<string>;
```


The fully-qualified domain name to register

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L93">property endpointConfiguration</a>
</h3>

```typescript
public endpointConfiguration: pulumi.Output<{ ... }>;
```


Nested argument defining API endpoint configuration including endpoint type. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L99">property regionalCertificateArn</a>
</h3>

```typescript
public regionalCertificateArn: pulumi.Output<string | undefined>;
```


The ARN for an AWS-managed certificate. Used when a regional domain name is
desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L104">property regionalCertificateName</a>
</h3>

```typescript
public regionalCertificateName: pulumi.Output<string | undefined>;
```


The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L108">property regionalDomainName</a>
</h3>

```typescript
public regionalDomainName: pulumi.Output<string>;
```


The hostname for the custom domain's regional endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L112">property regionalZoneId</a>
</h3>

```typescript
public regionalZoneId: pulumi.Output<string>;
```


The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Integration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L12">class Integration</a>
</h2>

Provides an HTTP Method Integration for an API Gateway Integration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L100">constructor</a>
</h3>

```typescript
new Integration(name: string, args: IntegrationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Integration resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IntegrationState): Integration
```


Get an existing Integration resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L28">property cacheKeyParameters</a>
</h3>

```typescript
public cacheKeyParameters: pulumi.Output<string[] | undefined>;
```


A list of cache key parameters for the integration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L32">property cacheNamespace</a>
</h3>

```typescript
public cacheNamespace: pulumi.Output<string>;
```


The integration's cache namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L36">property connectionId</a>
</h3>

```typescript
public connectionId: pulumi.Output<string | undefined>;
```


The id of the VpcLink used for the integration. **Required** if `connection_type` is `VPC_LINK`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L40">property connectionType</a>
</h3>

```typescript
public connectionType: pulumi.Output<string | undefined>;
```


The integration input's [connectionType](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#connectionType). Valid values are `INTERNET` (default for connections through the public routable internet), and `VPC_LINK` (for private connections between API Gateway and a network load balancer in a VPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L44">property contentHandling</a>
</h3>

```typescript
public contentHandling: pulumi.Output<string | undefined>;
```


Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L48">property credentials</a>
</h3>

```typescript
public credentials: pulumi.Output<string | undefined>;
```


The credentials required for the integration. For `AWS` integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role's ARN. To require that the caller's identity be passed through from the request, specify the string `arn:aws:iam::\*:user/\*`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L53">property httpMethod</a>
</h3>

```typescript
public httpMethod: pulumi.Output<string>;
```


The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`, `ANY`)
when calling the associated resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L61">property integrationHttpMethod</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L65">property passthroughBehavior</a>
</h3>

```typescript
public passthroughBehavior: pulumi.Output<string>;
```


The integration passthrough behavior (`WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`).  **Required** if `request_templates` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L70">property requestParameters</a>
</h3>

```typescript
public requestParameters: pulumi.Output<{ ... } | undefined>;
```


A map of request query string parameters and headers that should be passed to the backend responder.
For example: `request_parameters = { "integration.request.header.X-Some-Other-Header" = "method.request.header.X-Some-Header" }`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L74">property requestParametersInJson</a>
</h3>

```typescript
public requestParametersInJson: pulumi.Output<string | undefined>;
```


**Deprecated**, use `request_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L78">property requestTemplates</a>
</h3>

```typescript
public requestTemplates: pulumi.Output<{ ... } | undefined>;
```


A map of the integration's request templates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L82">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The API resource ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L86">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L90">property timeoutMilliseconds</a>
</h3>

```typescript
public timeoutMilliseconds: pulumi.Output<number | undefined>;
```


Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L94">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The integration input's [type](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/). Valid values are `HTTP` (for HTTP backends), `MOCK` (not calling any real backend), `AWS` (for AWS services), `AWS_PROXY` (for Lambda proxy integration) and `HTTP_PROXY` (for HTTP proxy integration). An `HTTP` or `HTTP_PROXY` integration with a `connection_type` of `VPC_LINK` is referred to as a private integration and uses a VpcLink to connect API Gateway to a network load balancer of a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L100">property uri</a>
</h3>

```typescript
public uri: pulumi.Output<string | undefined>;
```


The input's URI (HTTP, AWS). **Required** if `type` is `HTTP` or `AWS`.
For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form `arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}`. `region`, `subdomain` and `service` are used to determine the right endpoint.
e.g. `arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IntegrationResponse">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L15">class IntegrationResponse</a>
</h2>

Provides an HTTP Method Integration Response for an API Gateway Resource.

-> **Note:** Depends on having `aws_api_gateway_integration` inside your rest api. To ensure this
you might need to add an explicit `depends_on` for clean runs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L67">constructor</a>
</h3>

```typescript
new IntegrationResponse(name: string, args: IntegrationResponseArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IntegrationResponse resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IntegrationResponseState): IntegrationResponse
```


Get an existing IntegrationResponse resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L31">property contentHandling</a>
</h3>

```typescript
public contentHandling: pulumi.Output<string | undefined>;
```


Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L35">property httpMethod</a>
</h3>

```typescript
public httpMethod: pulumi.Output<string>;
```


The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L39">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L44">property responseParameters</a>
</h3>

```typescript
public responseParameters: pulumi.Output<{ ... } | undefined>;
```


A map of response parameters that can be read from the backend response.
For example: `response_parameters = { "method.response.header.X-Some-Header" = "integration.response.header.X-Some-Other-Header" }`,

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L48">property responseParametersInJson</a>
</h3>

```typescript
public responseParametersInJson: pulumi.Output<string | undefined>;
```


**Deprecated**, use `response_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L52">property responseTemplates</a>
</h3>

```typescript
public responseTemplates: pulumi.Output<{ ... } | undefined>;
```


A map specifying the templates used to transform the integration response body

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L56">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L63">property selectionPattern</a>
</h3>

```typescript
public selectionPattern: pulumi.Output<string | undefined>;
```


Specifies the regular expression pattern used to choose
an integration response based on the response from the backend. Setting this to `-` makes the integration the default one.
If the backend is an `AWS` Lambda function, the AWS Lambda function error header is matched.
For all other `HTTP` and `AWS` backends, the HTTP status code is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L67">property statusCode</a>
</h3>

```typescript
public statusCode: pulumi.Output<string>;
```


The HTTP status code

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Method">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L12">class Method</a>
</h2>

Provides a HTTP Method for an API Gateway Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L78">constructor</a>
</h3>

```typescript
new Method(name: string, args: MethodArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Method resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MethodState): Method
```


Get an existing Method resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L28">property apiKeyRequired</a>
</h3>

```typescript
public apiKeyRequired: pulumi.Output<boolean | undefined>;
```


Specify if the method requires an API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L32">property authorization</a>
</h3>

```typescript
public authorization: pulumi.Output<string>;
```


The type of authorization used for the method (`NONE`, `CUSTOM`, `AWS_IAM`, `COGNITO_USER_POOLS`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L36">property authorizationScopes</a>
</h3>

```typescript
public authorizationScopes: pulumi.Output<string[] | undefined>;
```


The authorization scopes used when the authorization is `COGNITO_USER_POOLS`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L40">property authorizerId</a>
</h3>

```typescript
public authorizerId: pulumi.Output<string | undefined>;
```


The authorizer id to be used when the authorization is `CUSTOM` or `COGNITO_USER_POOLS`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L44">property httpMethod</a>
</h3>

```typescript
public httpMethod: pulumi.Output<string>;
```


The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L50">property requestModels</a>
</h3>

```typescript
public requestModels: pulumi.Output<{ ... } | undefined>;
```


A map of the API models used for the request's content type
where key is the content type (e.g. `application/json`)
and value is either `Error`, `Empty` (built-in models) or `aws_api_gateway_model`'s `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L62">property requestParameters</a>
</h3>

```typescript
public requestParameters: pulumi.Output<{ ... } | undefined>;
```


A map of request query string parameters and headers that should be passed to the integration.
For example:
```hcl
request_parameters = {
"method.request.header.X-Some-Header"         = true
"method.request.querystring.some-query-param" = true
}
```
would define that the header `X-Some-Header` and the query string `some-query-param` must be provided on the request, or

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L66">property requestParametersInJson</a>
</h3>

```typescript
public requestParametersInJson: pulumi.Output<string | undefined>;
```


**Deprecated**, use `request_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L70">property requestValidatorId</a>
</h3>

```typescript
public requestValidatorId: pulumi.Output<string | undefined>;
```


The ID of a `aws_api_gateway_request_validator`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L74">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L78">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="MethodResponse">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L12">class MethodResponse</a>
</h2>

Provides an HTTP Method Response for an API Gateway Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L54">constructor</a>
</h3>

```typescript
new MethodResponse(name: string, args: MethodResponseArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MethodResponse resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MethodResponseState): MethodResponse
```


Get an existing MethodResponse resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L28">property httpMethod</a>
</h3>

```typescript
public httpMethod: pulumi.Output<string>;
```


The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L32">property resourceId</a>
</h3>

```typescript
public resourceId: pulumi.Output<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L36">property responseModels</a>
</h3>

```typescript
public responseModels: pulumi.Output<{ ... } | undefined>;
```


A map of the API models used for the response's content type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L42">property responseParameters</a>
</h3>

```typescript
public responseParameters: pulumi.Output<{ ... } | undefined>;
```


A map of response parameters that can be sent to the caller.
For example: `response_parameters = { "method.response.header.X-Some-Header" = true }`
would define that the header `X-Some-Header` can be provided on the response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L46">property responseParametersInJson</a>
</h3>

```typescript
public responseParametersInJson: pulumi.Output<string | undefined>;
```


**Deprecated**, use `response_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L50">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L54">property statusCode</a>
</h3>

```typescript
public statusCode: pulumi.Output<string>;
```


The HTTP status code

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="MethodSettings">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L12">class MethodSettings</a>
</h2>

Provides an API Gateway Method Settings, e.g. logging or monitoring.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L40">constructor</a>
</h3>

```typescript
new MethodSettings(name: string, args: MethodSettingsArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MethodSettings resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MethodSettingsState): MethodSettings
```


Get an existing MethodSettings resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L28">property methodPath</a>
</h3>

```typescript
public methodPath: pulumi.Output<string>;
```


Method path defined as `{resource_path}/{http_method}` for an individual method override, or `*&#47;*` for overriding all methods in the stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L32">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L36">property settings</a>
</h3>

```typescript
public settings: pulumi.Output<{ ... }>;
```


The settings block, see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L40">property stageName</a>
</h3>

```typescript
public stageName: pulumi.Output<string>;
```


The name of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Model">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L12">class Model</a>
</h2>

Provides a Model for a API Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L44">constructor</a>
</h3>

```typescript
new Model(name: string, args: ModelArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Model resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ModelState): Model
```


Get an existing Model resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L28">property contentType</a>
</h3>

```typescript
public contentType: pulumi.Output<string>;
```


The content type of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L40">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L44">property schema</a>
</h3>

```typescript
public schema: pulumi.Output<string | undefined>;
```


The schema of the model in a JSON form

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RequestValidator">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L12">class RequestValidator</a>
</h2>

Manages an API Gateway Request Validator.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L40">constructor</a>
</h3>

```typescript
new RequestValidator(name: string, args: RequestValidatorArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RequestValidator resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RequestValidatorState): RequestValidator
```


Get an existing RequestValidator resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L28">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the request validator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L32">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated Rest API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L36">property validateRequestBody</a>
</h3>

```typescript
public validateRequestBody: pulumi.Output<boolean | undefined>;
```


Boolean whether to validate request body. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L40">property validateRequestParameters</a>
</h3>

```typescript
public validateRequestParameters: pulumi.Output<boolean | undefined>;
```


Boolean whether to validate request parameters. Defaults to `false`.

<h2 class="pdoc-module-header" id="Resource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L12">class Resource</a>
</h2>

Provides an API Gateway Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L40">constructor</a>
</h3>

```typescript
new Resource(name: string, args: ResourceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Resource resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ResourceState): Resource
```


Get an existing Resource resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L28">property parentId</a>
</h3>

```typescript
public parentId: pulumi.Output<string>;
```


The ID of the parent API resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L32">property path</a>
</h3>

```typescript
public path: pulumi.Output<string>;
```


The complete path for this API resource, including all parent paths.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L36">property pathPart</a>
</h3>

```typescript
public pathPart: pulumi.Output<string>;
```


The last path segment of this API resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L40">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Response">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L10">class Response</a>
</h2>

Provides an API Gateway Gateway Response for a REST API Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L42">constructor</a>
</h3>

```typescript
new Response(name: string, args: ResponseArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Response resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ResponseState): Response
```


Get an existing Response resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L26">property responseParameters</a>
</h3>

```typescript
public responseParameters: pulumi.Output<{ ... } | undefined>;
```


A map specifying the templates used to transform the response body.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L30">property responseTemplates</a>
</h3>

```typescript
public responseTemplates: pulumi.Output<{ ... } | undefined>;
```


A map specifying the parameters (paths, query strings and headers) of the Gateway Response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L34">property responseType</a>
</h3>

```typescript
public responseType: pulumi.Output<string>;
```


The response type of the associated GatewayResponse.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L38">property restApiId</a>
</h3>

```typescript
public restApiId: pulumi.Output<string>;
```


The string identifier of the associated REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L42">property statusCode</a>
</h3>

```typescript
public statusCode: pulumi.Output<string | undefined>;
```


The HTTP status code of the Gateway Response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RestApi">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L10">class RestApi</a>
</h2>

Provides an API Gateway REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L68">constructor</a>
</h3>

```typescript
new RestApi(name: string, args?: RestApiArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RestApi resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RestApiState): RestApi
```


Get an existing RestApi resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L26">property apiKeySource</a>
</h3>

```typescript
public apiKeySource: pulumi.Output<string | undefined>;
```


The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L30">property binaryMediaTypes</a>
</h3>

```typescript
public binaryMediaTypes: pulumi.Output<string[] | undefined>;
```


The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L34">property body</a>
</h3>

```typescript
public body: pulumi.Output<string | undefined>;
```


An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L38">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The creation date of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L42">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L46">property endpointConfiguration</a>
</h3>

```typescript
public endpointConfiguration: pulumi.Output<{ ... }>;
```


Nested argument defining API endpoint configuration including endpoint type. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L52">property executionArn</a>
</h3>

```typescript
public executionArn: pulumi.Output<string>;
```


The execution ARN part to be used in [`lambda_permission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `source_arn`
when allowing API Gateway to invoke a Lambda function,
e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j`, which can be concatenated with allowed stage, method and resource path.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L56">property minimumCompressionSize</a>
</h3>

```typescript
public minimumCompressionSize: pulumi.Output<number | undefined>;
```


Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L60">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L64">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string | undefined>;
```


JSON formatted policy document that controls access to the API Gateway. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L68">property rootResourceId</a>
</h3>

```typescript
public rootResourceId: pulumi.Output<string>;
```


The resource ID of the REST API's root

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Stage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L14">class Stage</a>
</h2>

Provides an API Gateway Stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L86">constructor</a>
</h3>

```typescript
new Stage(name: string, args: StageArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Stage resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StageState): Stage
```


Get an existing Stage resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L30">property accessLogSettings</a>
</h3>

```typescript
public accessLogSettings: pulumi.Output<{ ... } | undefined>;
```


Enables access logs for the API stage. Detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L34">property cacheClusterEnabled</a>
</h3>

```typescript
public cacheClusterEnabled: pulumi.Output<boolean | undefined>;
```


Specifies whether a cache cluster is enabled for the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L39">property cacheClusterSize</a>
</h3>

```typescript
public cacheClusterSize: pulumi.Output<string | undefined>;
```


The size of the cache cluster for the stage, if enabled.
Allowed values include `0.5`, `1.6`, `6.1`, `13.5`, `28.4`, `58.2`, `118` and `237`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L43">property clientCertificateId</a>
</h3>

```typescript
public clientCertificateId: pulumi.Output<string | undefined>;
```


The identifier of a client certificate for the stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L47">property deployment</a>
</h3>

```typescript
public deployment: pulumi.Output<Deployment>;
```


The ID of the deployment that the stage points to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L51">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L55">property documentationVersion</a>
</h3>

```typescript
public documentationVersion: pulumi.Output<string | undefined>;
```


The version of the associated API documentation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L61">property executionArn</a>
</h3>

```typescript
public executionArn: pulumi.Output<string>;
```


The execution ARN to be used in [`lambda_permission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `source_arn`
when allowing API Gateway to invoke a Lambda function,
e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L66">property invokeUrl</a>
</h3>

```typescript
public invokeUrl: pulumi.Output<string>;
```


The URL to invoke the API pointing to the stage,
e.g. `https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L70">property restApi</a>
</h3>

```typescript
public restApi: pulumi.Output<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L74">property stageName</a>
</h3>

```typescript
public stageName: pulumi.Output<string>;
```


The name of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L78">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L82">property variables</a>
</h3>

```typescript
public variables: pulumi.Output<{ ... } | undefined>;
```


A map that defines the stage variables

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L86">property xrayTracingEnabled</a>
</h3>

```typescript
public xrayTracingEnabled: pulumi.Output<boolean | undefined>;
```


Whether active tracing with X-ray is enabled. Defaults to `false`.

<h2 class="pdoc-module-header" id="UsagePlan">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L10">class UsagePlan</a>
</h2>

Provides an API Gateway Usage Plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L46">constructor</a>
</h3>

```typescript
new UsagePlan(name: string, args?: UsagePlanArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UsagePlan resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UsagePlanState): UsagePlan
```


Get an existing UsagePlan resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L26">property apiStages</a>
</h3>

```typescript
public apiStages: pulumi.Output<{ ... }[] | undefined>;
```


The associated API stages of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of a usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L38">property productCode</a>
</h3>

```typescript
public productCode: pulumi.Output<string | undefined>;
```


The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L42">property quotaSettings</a>
</h3>

```typescript
public quotaSettings: pulumi.Output<{ ... } | undefined>;
```


The quota settings of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L46">property throttleSettings</a>
</h3>

```typescript
public throttleSettings: pulumi.Output<{ ... } | undefined>;
```


The throttling limits of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="UsagePlanKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L10">class UsagePlanKey</a>
</h2>

Provides an API Gateway Usage Plan Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L42">constructor</a>
</h3>

```typescript
new UsagePlanKey(name: string, args: UsagePlanKeyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UsagePlanKey resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UsagePlanKeyState): UsagePlanKey
```


Get an existing UsagePlanKey resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L26">property keyId</a>
</h3>

```typescript
public keyId: pulumi.Output<string>;
```


The identifier of the API key resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L30">property keyType</a>
</h3>

```typescript
public keyType: pulumi.Output<string>;
```


The type of the API key resource. Currently, the valid key type is API_KEY.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of a usage plan key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L38">property usagePlanId</a>
</h3>

```typescript
public usagePlanId: pulumi.Output<string>;
```


The Id of the usage plan resource representing to associate the key to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L42">property value</a>
</h3>

```typescript
public value: pulumi.Output<string>;
```


The value of a usage plan key.

<h2 class="pdoc-module-header" id="VpcLink">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L10">class VpcLink</a>
</h2>

Provides an API Gateway VPC Link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L34">constructor</a>
</h3>

```typescript
new VpcLink(name: string, args: VpcLinkArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VpcLink resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcLinkState): VpcLink
```


Get an existing VpcLink resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the VPC link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name used to label and identify the VPC link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L34">property targetArn</a>
</h3>

```typescript
public targetArn: pulumi.Output<string>;
```


The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getKey.ts#L11">function getKey</a>
</h2>

```typescript
getKey(args: GetKeyArgs, opts?: pulumi.InvokeOptions): Promise<GetKeyResult>
```


Use this data source to get the name and value of a pre-existing API Key, for
example to supply credentials for a dependency microservice.

<h2 class="pdoc-module-header" id="getResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getResource.ts#L11">function getResource</a>
</h2>

```typescript
getResource(args: GetResourceArgs, opts?: pulumi.InvokeOptions): Promise<GetResourceResult>
```


Use this data source to get the id of a Resource in API Gateway.
To fetch the Resource, you must provide the REST API id as well as the full path.

<h2 class="pdoc-module-header" id="getRestApi">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getRestApi.ts#L13">function getRestApi</a>
</h2>

```typescript
getRestApi(args: GetRestApiArgs, opts?: pulumi.InvokeOptions): Promise<GetRestApiResult>
```


Use this data source to get the id and root_resource_id of a REST API in
API Gateway. To fetch the REST API you must provide a name to match against.
As there is no unique name constraint on REST APIs this data source will
error if there is more than one match.

<h2 class="pdoc-module-header" id="AccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/account.ts#L78">interface AccountArgs</a>
</h2>

The set of arguments for constructing a Account resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/account.ts#L84">property cloudwatchRoleArn</a>
</h3>

```typescript
cloudwatchRoleArn?: pulumi.Input<string>;
```


The ARN of an IAM role for CloudWatch (to allow logging & monitoring).
See more [in AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console).
Logging & monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.

<h2 class="pdoc-module-header" id="AccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/account.ts#L62">interface AccountState</a>
</h2>

Input properties used for looking up and filtering Account resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/account.ts#L68">property cloudwatchRoleArn</a>
</h3>

```typescript
cloudwatchRoleArn?: pulumi.Input<string>;
```


The ARN of an IAM role for CloudWatch (to allow logging & monitoring).
See more [in AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console).
Logging & monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/account.ts#L72">property throttleSettings</a>
</h3>

```typescript
throttleSettings?: pulumi.Input<{ ... }>;
```


Account-Level throttle settings. See exported fields below.

<h2 class="pdoc-module-header" id="ApiKeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L126">interface ApiKeyArgs</a>
</h2>

The set of arguments for constructing a ApiKey resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L130">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The API key description. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L134">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether the API key can be used by callers. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L138">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L142">property stageKeys</a>
</h3>

```typescript
stageKeys?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of stage keys associated with the API key - see below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L146">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


The value of the API key. If not specified, it will be automatically generated by AWS on creation.

<h2 class="pdoc-module-header" id="ApiKeyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L92">interface ApiKeyState</a>
</h2>

Input properties used for looking up and filtering ApiKey resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L96">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The creation date of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L100">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The API key description. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L104">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether the API key can be used by callers. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L108">property lastUpdatedDate</a>
</h3>

```typescript
lastUpdatedDate?: pulumi.Input<string>;
```


The last update date of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L116">property stageKeys</a>
</h3>

```typescript
stageKeys?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of stage keys associated with the API key - see below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/apiKey.ts#L120">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


The value of the API key. If not specified, it will be automatically generated by AWS on creation.

<h2 class="pdoc-module-header" id="AuthorizerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L167">interface AuthorizerArgs</a>
</h2>

The set of arguments for constructing a Authorizer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L172">property authorizerCredentials</a>
</h3>

```typescript
authorizerCredentials?: pulumi.Input<string>;
```


The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L177">property authorizerResultTtlInSeconds</a>
</h3>

```typescript
authorizerResultTtlInSeconds?: pulumi.Input<number>;
```


The TTL of cached authorizer results in seconds.
Defaults to `300`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L183">property authorizerUri</a>
</h3>

```typescript
authorizerUri?: pulumi.Input<string>;
```


The authorizer's Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L188">property identitySource</a>
</h3>

```typescript
identitySource?: pulumi.Input<string>;
```


The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L195">property identityValidationExpression</a>
</h3>

```typescript
identityValidationExpression?: pulumi.Input<string>;
```


A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn't match,
the client receives a 401 Unauthorized response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L199">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the authorizer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L204">property providerArns</a>
</h3>

```typescript
providerArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L208">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L213">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.

<h2 class="pdoc-module-header" id="AuthorizerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L115">interface AuthorizerState</a>
</h2>

Input properties used for looking up and filtering Authorizer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L120">property authorizerCredentials</a>
</h3>

```typescript
authorizerCredentials?: pulumi.Input<string>;
```


The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L125">property authorizerResultTtlInSeconds</a>
</h3>

```typescript
authorizerResultTtlInSeconds?: pulumi.Input<number>;
```


The TTL of cached authorizer results in seconds.
Defaults to `300`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L131">property authorizerUri</a>
</h3>

```typescript
authorizerUri?: pulumi.Input<string>;
```


The authorizer's Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L136">property identitySource</a>
</h3>

```typescript
identitySource?: pulumi.Input<string>;
```


The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L143">property identityValidationExpression</a>
</h3>

```typescript
identityValidationExpression?: pulumi.Input<string>;
```


A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn't match,
the client receives a 401 Unauthorized response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L147">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the authorizer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L152">property providerArns</a>
</h3>

```typescript
providerArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L156">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/authorizer.ts#L161">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.

<h2 class="pdoc-module-header" id="BasePathMappingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L102">interface BasePathMappingArgs</a>
</h2>

The set of arguments for constructing a BasePathMapping resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L110">property basePath</a>
</h3>

```typescript
basePath?: pulumi.Input<string>;
```


Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L114">property domainName</a>
</h3>

```typescript
domainName: pulumi.Input<string>;
```


The already-registered domain name to connect the API to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L106">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The id of the API to connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L118">property stageName</a>
</h3>

```typescript
stageName?: pulumi.Input<string>;
```


The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.

<h2 class="pdoc-module-header" id="BasePathMappingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L80">interface BasePathMappingState</a>
</h2>

Input properties used for looking up and filtering BasePathMapping resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L88">property basePath</a>
</h3>

```typescript
basePath?: pulumi.Input<string>;
```


Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L92">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


The already-registered domain name to connect the API to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L84">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The id of the API to connect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/basePathMapping.ts#L96">property stageName</a>
</h3>

```typescript
stageName?: pulumi.Input<string>;
```


The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.

<h2 class="pdoc-module-header" id="ClientCertificateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L92">interface ClientCertificateArgs</a>
</h2>

The set of arguments for constructing a ClientCertificate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L96">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the client certificate.

<h2 class="pdoc-module-header" id="ClientCertificateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L70">interface ClientCertificateState</a>
</h2>

Input properties used for looking up and filtering ClientCertificate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L74">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The date when the client certificate was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L78">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the client certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L82">property expirationDate</a>
</h3>

```typescript
expirationDate?: pulumi.Input<string>;
```


The date when the client certificate will expire.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/clientCertificate.ts#L86">property pemEncodedCertificate</a>
</h3>

```typescript
pemEncodedCertificate?: pulumi.Input<string>;
```


The PEM-encoded public key of the client certificate.

<h2 class="pdoc-module-header" id="DeploymentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L149">interface DeploymentArgs</a>
</h2>

The set of arguments for constructing a Deployment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L153">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L157">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L161">property stageDescription</a>
</h3>

```typescript
stageDescription?: pulumi.Input<string>;
```


The description of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L165">property stageName</a>
</h3>

```typescript
stageName: pulumi.Input<string>;
```


The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment. Use `""` to point at the default stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L169">property variables</a>
</h3>

```typescript
variables?: pulumi.Input<{ ... }>;
```


A map that defines variables for the stage

<h2 class="pdoc-module-header" id="DeploymentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L108">interface DeploymentState</a>
</h2>

Input properties used for looking up and filtering Deployment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L112">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The creation date of the deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L116">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L122">property executionArn</a>
</h3>

```typescript
executionArn?: pulumi.Input<string>;
```


The execution ARN to be used in [`lambda_permission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `source_arn`
when allowing API Gateway to invoke a Lambda function,
e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L127">property invokeUrl</a>
</h3>

```typescript
invokeUrl?: pulumi.Input<string>;
```


The URL to invoke the API pointing to the stage,
e.g. `https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L131">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L135">property stageDescription</a>
</h3>

```typescript
stageDescription?: pulumi.Input<string>;
```


The description of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L139">property stageName</a>
</h3>

```typescript
stageName?: pulumi.Input<string>;
```


The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment. Use `""` to point at the default stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/deployment.ts#L143">property variables</a>
</h3>

```typescript
variables?: pulumi.Input<{ ... }>;
```


A map that defines variables for the stage

<h2 class="pdoc-module-header" id="DocumentationPartArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L91">interface DocumentationPartArgs</a>
</h2>

The set of arguments for constructing a DocumentationPart resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L95">property location</a>
</h3>

```typescript
location: pulumi.Input<{ ... }>;
```


The location of the targeted API entity of the to-be-created documentation part. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L99">property properties</a>
</h3>

```typescript
properties: pulumi.Input<string>;
```


A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., "{ \"description\": \"The API does ...\" }". Only Swagger-compliant key-value pairs can be exported and, hence, published.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L103">property restApiId</a>
</h3>

```typescript
restApiId: pulumi.Input<string>;
```


The ID of the associated Rest API

<h2 class="pdoc-module-header" id="DocumentationPartState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L73">interface DocumentationPartState</a>
</h2>

Input properties used for looking up and filtering DocumentationPart resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L77">property location</a>
</h3>

```typescript
location?: pulumi.Input<{ ... }>;
```


The location of the targeted API entity of the to-be-created documentation part. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L81">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<string>;
```


A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., "{ \"description\": \"The API does ...\" }". Only Swagger-compliant key-value pairs can be exported and, hence, published.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationPart.ts#L85">property restApiId</a>
</h3>

```typescript
restApiId?: pulumi.Input<string>;
```


The ID of the associated Rest API

<h2 class="pdoc-module-header" id="DocumentationVersionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L88">interface DocumentationVersionArgs</a>
</h2>

The set of arguments for constructing a DocumentationVersion resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L92">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the API documentation version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L96">property restApiId</a>
</h3>

```typescript
restApiId: pulumi.Input<string>;
```


The ID of the associated Rest API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L100">property version</a>
</h3>

```typescript
version: pulumi.Input<string>;
```


The version identifier of the API documentation snapshot.

<h2 class="pdoc-module-header" id="DocumentationVersionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L70">interface DocumentationVersionState</a>
</h2>

Input properties used for looking up and filtering DocumentationVersion resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L74">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the API documentation version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L78">property restApiId</a>
</h3>

```typescript
restApiId?: pulumi.Input<string>;
```


The ID of the associated Rest API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/documentationVersion.ts#L82">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The version identifier of the API documentation snapshot.

<h2 class="pdoc-module-header" id="DomainNameArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L244">interface DomainNameArgs</a>
</h2>

The set of arguments for constructing a DomainName resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L250">property certificateArn</a>
</h3>

```typescript
certificateArn?: pulumi.Input<string>;
```


The ARN for an AWS-managed certificate. Used when an edge-optimized domain name is
desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`,
`regional_certificate_arn`, and `regional_certificate_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L256">property certificateBody</a>
</h3>

```typescript
certificateBody?: pulumi.Input<string>;
```


The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L263">property certificateChain</a>
</h3>

```typescript
certificateChain?: pulumi.Input<string>;
```


The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L269">property certificateName</a>
</h3>

```typescript
certificateName?: pulumi.Input<string>;
```


The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L274">property certificatePrivateKey</a>
</h3>

```typescript
certificatePrivateKey?: pulumi.Input<string>;
```


The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L278">property domainName</a>
</h3>

```typescript
domainName: pulumi.Input<string>;
```


The fully-qualified domain name to register

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L282">property endpointConfiguration</a>
</h3>

```typescript
endpointConfiguration?: pulumi.Input<{ ... }>;
```


Nested argument defining API endpoint configuration including endpoint type. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L288">property regionalCertificateArn</a>
</h3>

```typescript
regionalCertificateArn?: pulumi.Input<string>;
```


The ARN for an AWS-managed certificate. Used when a regional domain name is
desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L293">property regionalCertificateName</a>
</h3>

```typescript
regionalCertificateName?: pulumi.Input<string>;
```


The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.

<h2 class="pdoc-module-header" id="DomainNameState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L167">interface DomainNameState</a>
</h2>

Input properties used for looking up and filtering DomainName resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L173">property certificateArn</a>
</h3>

```typescript
certificateArn?: pulumi.Input<string>;
```


The ARN for an AWS-managed certificate. Used when an edge-optimized domain name is
desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`,
`regional_certificate_arn`, and `regional_certificate_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L179">property certificateBody</a>
</h3>

```typescript
certificateBody?: pulumi.Input<string>;
```


The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L186">property certificateChain</a>
</h3>

```typescript
certificateChain?: pulumi.Input<string>;
```


The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L192">property certificateName</a>
</h3>

```typescript
certificateName?: pulumi.Input<string>;
```


The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L197">property certificatePrivateKey</a>
</h3>

```typescript
certificatePrivateKey?: pulumi.Input<string>;
```


The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L201">property certificateUploadDate</a>
</h3>

```typescript
certificateUploadDate?: pulumi.Input<string>;
```


The upload date associated with the domain certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L206">property cloudfrontDomainName</a>
</h3>

```typescript
cloudfrontDomainName?: pulumi.Input<string>;
```


The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L211">property cloudfrontZoneId</a>
</h3>

```typescript
cloudfrontZoneId?: pulumi.Input<string>;
```


For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
that can be used to create a Route53 alias record for the distribution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L215">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


The fully-qualified domain name to register

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L219">property endpointConfiguration</a>
</h3>

```typescript
endpointConfiguration?: pulumi.Input<{ ... }>;
```


Nested argument defining API endpoint configuration including endpoint type. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L225">property regionalCertificateArn</a>
</h3>

```typescript
regionalCertificateArn?: pulumi.Input<string>;
```


The ARN for an AWS-managed certificate. Used when a regional domain name is
desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L230">property regionalCertificateName</a>
</h3>

```typescript
regionalCertificateName?: pulumi.Input<string>;
```


The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L234">property regionalDomainName</a>
</h3>

```typescript
regionalDomainName?: pulumi.Input<string>;
```


The hostname for the custom domain's regional endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/domainName.ts#L238">property regionalZoneId</a>
</h3>

```typescript
regionalZoneId?: pulumi.Input<string>;
```


The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.

<h2 class="pdoc-module-header" id="GetKeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getKey.ts#L20">interface GetKeyArgs</a>
</h2>

A collection of arguments for invoking getKey.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getKey.ts#L24">property id</a>
</h3>

```typescript
id: string;
```


The ID of the API Key to look up.

<h2 class="pdoc-module-header" id="GetKeyResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getKey.ts#L30">interface GetKeyResult</a>
</h2>

A collection of values returned by getKey.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getKey.ts#L34">property name</a>
</h3>

```typescript
name: string;
```


Set to the name of the API Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getKey.ts#L38">property value</a>
</h3>

```typescript
value: string;
```


Set to the value of the API Key.

<h2 class="pdoc-module-header" id="GetResourceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getResource.ts#L21">interface GetResourceArgs</a>
</h2>

A collection of arguments for invoking getResource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getResource.ts#L25">property path</a>
</h3>

```typescript
path: string;
```


The full path of the resource.  If no path is found, an error will be returned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getResource.ts#L29">property restApiId</a>
</h3>

```typescript
restApiId: string;
```


The REST API id that owns the resource. If no REST API is found, an error will be returned.

<h2 class="pdoc-module-header" id="GetResourceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getResource.ts#L35">interface GetResourceResult</a>
</h2>

A collection of values returned by getResource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getResource.ts#L47">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getResource.ts#L39">property parentId</a>
</h3>

```typescript
parentId: string;
```


Set to the ID of the parent Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getResource.ts#L43">property pathPart</a>
</h3>

```typescript
pathPart: string;
```


Set to the path relative to the parent Resource.

<h2 class="pdoc-module-header" id="GetRestApiArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getRestApi.ts#L22">interface GetRestApiArgs</a>
</h2>

A collection of arguments for invoking getRestApi.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getRestApi.ts#L27">property name</a>
</h3>

```typescript
name: string;
```


The name of the REST API to look up. If no REST API is found with this name, an error will be returned.
If multiple REST APIs are found with this name, an error will be returned.

<h2 class="pdoc-module-header" id="GetRestApiResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getRestApi.ts#L33">interface GetRestApiResult</a>
</h2>

A collection of values returned by getRestApi.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getRestApi.ts#L41">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/getRestApi.ts#L37">property rootResourceId</a>
</h3>

```typescript
rootResourceId: string;
```


Set to the ID of the API Gateway Resource on the found REST API where the route matches '/'.

<h2 class="pdoc-module-header" id="IntegrationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L252">interface IntegrationArgs</a>
</h2>

The set of arguments for constructing a Integration resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L256">property cacheKeyParameters</a>
</h3>

```typescript
cacheKeyParameters?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of cache key parameters for the integration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L260">property cacheNamespace</a>
</h3>

```typescript
cacheNamespace?: pulumi.Input<string>;
```


The integration's cache namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L264">property connectionId</a>
</h3>

```typescript
connectionId?: pulumi.Input<string>;
```


The id of the VpcLink used for the integration. **Required** if `connection_type` is `VPC_LINK`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L268">property connectionType</a>
</h3>

```typescript
connectionType?: pulumi.Input<string>;
```


The integration input's [connectionType](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#connectionType). Valid values are `INTERNET` (default for connections through the public routable internet), and `VPC_LINK` (for private connections between API Gateway and a network load balancer in a VPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L272">property contentHandling</a>
</h3>

```typescript
contentHandling?: pulumi.Input<string>;
```


Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L276">property credentials</a>
</h3>

```typescript
credentials?: pulumi.Input<string>;
```


The credentials required for the integration. For `AWS` integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role's ARN. To require that the caller's identity be passed through from the request, specify the string `arn:aws:iam::\*:user/\*`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L281">property httpMethod</a>
</h3>

```typescript
httpMethod: pulumi.Input<string>;
```


The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`, `ANY`)
when calling the associated resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L289">property integrationHttpMethod</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L293">property passthroughBehavior</a>
</h3>

```typescript
passthroughBehavior?: pulumi.Input<string>;
```


The integration passthrough behavior (`WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`).  **Required** if `request_templates` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L298">property requestParameters</a>
</h3>

```typescript
requestParameters?: pulumi.Input<{ ... }>;
```


A map of request query string parameters and headers that should be passed to the backend responder.
For example: `request_parameters = { "integration.request.header.X-Some-Other-Header" = "method.request.header.X-Some-Header" }`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L302">property requestParametersInJson</a>
</h3>

```typescript
requestParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `request_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L306">property requestTemplates</a>
</h3>

```typescript
requestTemplates?: pulumi.Input<{ ... }>;
```


A map of the integration's request templates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L310">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The API resource ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L314">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L318">property timeoutMilliseconds</a>
</h3>

```typescript
timeoutMilliseconds?: pulumi.Input<number>;
```


Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L322">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The integration input's [type](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/). Valid values are `HTTP` (for HTTP backends), `MOCK` (not calling any real backend), `AWS` (for AWS services), `AWS_PROXY` (for Lambda proxy integration) and `HTTP_PROXY` (for HTTP proxy integration). An `HTTP` or `HTTP_PROXY` integration with a `connection_type` of `VPC_LINK` is referred to as a private integration and uses a VpcLink to connect API Gateway to a network load balancer of a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L328">property uri</a>
</h3>

```typescript
uri?: pulumi.Input<string>;
```


The input's URI (HTTP, AWS). **Required** if `type` is `HTTP` or `AWS`.
For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form `arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}`. `region`, `subdomain` and `service` are used to determine the right endpoint.
e.g. `arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations`

<h2 class="pdoc-module-header" id="IntegrationResponseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L167">interface IntegrationResponseArgs</a>
</h2>

The set of arguments for constructing a IntegrationResponse resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L171">property contentHandling</a>
</h3>

```typescript
contentHandling?: pulumi.Input<string>;
```


Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L175">property httpMethod</a>
</h3>

```typescript
httpMethod: pulumi.Input<string>;
```


The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L179">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L184">property responseParameters</a>
</h3>

```typescript
responseParameters?: pulumi.Input<{ ... }>;
```


A map of response parameters that can be read from the backend response.
For example: `response_parameters = { "method.response.header.X-Some-Header" = "integration.response.header.X-Some-Other-Header" }`,

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L188">property responseParametersInJson</a>
</h3>

```typescript
responseParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `response_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L192">property responseTemplates</a>
</h3>

```typescript
responseTemplates?: pulumi.Input<{ ... }>;
```


A map specifying the templates used to transform the integration response body

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L196">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L203">property selectionPattern</a>
</h3>

```typescript
selectionPattern?: pulumi.Input<string>;
```


Specifies the regular expression pattern used to choose
an integration response based on the response from the backend. Setting this to `-` makes the integration the default one.
If the backend is an `AWS` Lambda function, the AWS Lambda function error header is matched.
For all other `HTTP` and `AWS` backends, the HTTP status code is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L207">property statusCode</a>
</h3>

```typescript
statusCode: pulumi.Input<string>;
```


The HTTP status code

<h2 class="pdoc-module-header" id="IntegrationResponseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L121">interface IntegrationResponseState</a>
</h2>

Input properties used for looking up and filtering IntegrationResponse resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L125">property contentHandling</a>
</h3>

```typescript
contentHandling?: pulumi.Input<string>;
```


Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L129">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L133">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L138">property responseParameters</a>
</h3>

```typescript
responseParameters?: pulumi.Input<{ ... }>;
```


A map of response parameters that can be read from the backend response.
For example: `response_parameters = { "method.response.header.X-Some-Header" = "integration.response.header.X-Some-Other-Header" }`,

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L142">property responseParametersInJson</a>
</h3>

```typescript
responseParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `response_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L146">property responseTemplates</a>
</h3>

```typescript
responseTemplates?: pulumi.Input<{ ... }>;
```


A map specifying the templates used to transform the integration response body

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L150">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L157">property selectionPattern</a>
</h3>

```typescript
selectionPattern?: pulumi.Input<string>;
```


Specifies the regular expression pattern used to choose
an integration response based on the response from the backend. Setting this to `-` makes the integration the default one.
If the backend is an `AWS` Lambda function, the AWS Lambda function error header is matched.
For all other `HTTP` and `AWS` backends, the HTTP status code is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integrationResponse.ts#L161">property statusCode</a>
</h3>

```typescript
statusCode?: pulumi.Input<string>;
```


The HTTP status code

<h2 class="pdoc-module-header" id="IntegrationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L170">interface IntegrationState</a>
</h2>

Input properties used for looking up and filtering Integration resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L174">property cacheKeyParameters</a>
</h3>

```typescript
cacheKeyParameters?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of cache key parameters for the integration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L178">property cacheNamespace</a>
</h3>

```typescript
cacheNamespace?: pulumi.Input<string>;
```


The integration's cache namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L182">property connectionId</a>
</h3>

```typescript
connectionId?: pulumi.Input<string>;
```


The id of the VpcLink used for the integration. **Required** if `connection_type` is `VPC_LINK`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L186">property connectionType</a>
</h3>

```typescript
connectionType?: pulumi.Input<string>;
```


The integration input's [connectionType](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#connectionType). Valid values are `INTERNET` (default for connections through the public routable internet), and `VPC_LINK` (for private connections between API Gateway and a network load balancer in a VPC).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L190">property contentHandling</a>
</h3>

```typescript
contentHandling?: pulumi.Input<string>;
```


Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L194">property credentials</a>
</h3>

```typescript
credentials?: pulumi.Input<string>;
```


The credentials required for the integration. For `AWS` integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role's ARN. To require that the caller's identity be passed through from the request, specify the string `arn:aws:iam::\*:user/\*`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L199">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`, `ANY`)
when calling the associated resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L207">property integrationHttpMethod</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L211">property passthroughBehavior</a>
</h3>

```typescript
passthroughBehavior?: pulumi.Input<string>;
```


The integration passthrough behavior (`WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`).  **Required** if `request_templates` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L216">property requestParameters</a>
</h3>

```typescript
requestParameters?: pulumi.Input<{ ... }>;
```


A map of request query string parameters and headers that should be passed to the backend responder.
For example: `request_parameters = { "integration.request.header.X-Some-Other-Header" = "method.request.header.X-Some-Header" }`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L220">property requestParametersInJson</a>
</h3>

```typescript
requestParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `request_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L224">property requestTemplates</a>
</h3>

```typescript
requestTemplates?: pulumi.Input<{ ... }>;
```


A map of the integration's request templates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L228">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The API resource ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L232">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L236">property timeoutMilliseconds</a>
</h3>

```typescript
timeoutMilliseconds?: pulumi.Input<number>;
```


Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L240">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The integration input's [type](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/). Valid values are `HTTP` (for HTTP backends), `MOCK` (not calling any real backend), `AWS` (for AWS services), `AWS_PROXY` (for Lambda proxy integration) and `HTTP_PROXY` (for HTTP proxy integration). An `HTTP` or `HTTP_PROXY` integration with a `connection_type` of `VPC_LINK` is referred to as a private integration and uses a VpcLink to connect API Gateway to a network load balancer of a VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/integration.ts#L246">property uri</a>
</h3>

```typescript
uri?: pulumi.Input<string>;
```


The input's URI (HTTP, AWS). **Required** if `type` is `HTTP` or `AWS`.
For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form `arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}`. `region`, `subdomain` and `service` are used to determine the right endpoint.
e.g. `arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations`

<h2 class="pdoc-module-header" id="MethodArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L196">interface MethodArgs</a>
</h2>

The set of arguments for constructing a Method resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L200">property apiKeyRequired</a>
</h3>

```typescript
apiKeyRequired?: pulumi.Input<boolean>;
```


Specify if the method requires an API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L204">property authorization</a>
</h3>

```typescript
authorization: pulumi.Input<string>;
```


The type of authorization used for the method (`NONE`, `CUSTOM`, `AWS_IAM`, `COGNITO_USER_POOLS`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L208">property authorizationScopes</a>
</h3>

```typescript
authorizationScopes?: pulumi.Input<pulumi.Input<string>[]>;
```


The authorization scopes used when the authorization is `COGNITO_USER_POOLS`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L212">property authorizerId</a>
</h3>

```typescript
authorizerId?: pulumi.Input<string>;
```


The authorizer id to be used when the authorization is `CUSTOM` or `COGNITO_USER_POOLS`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L216">property httpMethod</a>
</h3>

```typescript
httpMethod: pulumi.Input<string>;
```


The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L222">property requestModels</a>
</h3>

```typescript
requestModels?: pulumi.Input<{ ... }>;
```


A map of the API models used for the request's content type
where key is the content type (e.g. `application/json`)
and value is either `Error`, `Empty` (built-in models) or `aws_api_gateway_model`'s `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L234">property requestParameters</a>
</h3>

```typescript
requestParameters?: pulumi.Input<{ ... }>;
```


A map of request query string parameters and headers that should be passed to the integration.
For example:
```hcl
request_parameters = {
"method.request.header.X-Some-Header"         = true
"method.request.querystring.some-query-param" = true
}
```
would define that the header `X-Some-Header` and the query string `some-query-param` must be provided on the request, or

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L238">property requestParametersInJson</a>
</h3>

```typescript
requestParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `request_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L242">property requestValidatorId</a>
</h3>

```typescript
requestValidatorId?: pulumi.Input<string>;
```


The ID of a `aws_api_gateway_request_validator`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L246">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L250">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h2 class="pdoc-module-header" id="MethodResponseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L140">interface MethodResponseArgs</a>
</h2>

The set of arguments for constructing a MethodResponse resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L144">property httpMethod</a>
</h3>

```typescript
httpMethod: pulumi.Input<string>;
```


The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L148">property resourceId</a>
</h3>

```typescript
resourceId: pulumi.Input<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L152">property responseModels</a>
</h3>

```typescript
responseModels?: pulumi.Input<{ ... }>;
```


A map of the API models used for the response's content type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L158">property responseParameters</a>
</h3>

```typescript
responseParameters?: pulumi.Input<{ ... }>;
```


A map of response parameters that can be sent to the caller.
For example: `response_parameters = { "method.response.header.X-Some-Header" = true }`
would define that the header `X-Some-Header` can be provided on the response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L162">property responseParametersInJson</a>
</h3>

```typescript
responseParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `response_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L166">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L170">property statusCode</a>
</h3>

```typescript
statusCode: pulumi.Input<string>;
```


The HTTP status code

<h2 class="pdoc-module-header" id="MethodResponseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L104">interface MethodResponseState</a>
</h2>

Input properties used for looking up and filtering MethodResponse resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L108">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L112">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L116">property responseModels</a>
</h3>

```typescript
responseModels?: pulumi.Input<{ ... }>;
```


A map of the API models used for the response's content type

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L122">property responseParameters</a>
</h3>

```typescript
responseParameters?: pulumi.Input<{ ... }>;
```


A map of response parameters that can be sent to the caller.
For example: `response_parameters = { "method.response.header.X-Some-Header" = true }`
would define that the header `X-Some-Header` can be provided on the response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L126">property responseParametersInJson</a>
</h3>

```typescript
responseParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `response_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L130">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodResponse.ts#L134">property statusCode</a>
</h3>

```typescript
statusCode?: pulumi.Input<string>;
```


The HTTP status code

<h2 class="pdoc-module-header" id="MethodSettingsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L106">interface MethodSettingsArgs</a>
</h2>

The set of arguments for constructing a MethodSettings resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L110">property methodPath</a>
</h3>

```typescript
methodPath: pulumi.Input<string>;
```


Method path defined as `{resource_path}/{http_method}` for an individual method override, or `*&#47;*` for overriding all methods in the stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L114">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L118">property settings</a>
</h3>

```typescript
settings: pulumi.Input<{ ... }>;
```


The settings block, see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L122">property stageName</a>
</h3>

```typescript
stageName: pulumi.Input<string>;
```


The name of the stage

<h2 class="pdoc-module-header" id="MethodSettingsState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L84">interface MethodSettingsState</a>
</h2>

Input properties used for looking up and filtering MethodSettings resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L88">property methodPath</a>
</h3>

```typescript
methodPath?: pulumi.Input<string>;
```


Method path defined as `{resource_path}/{http_method}` for an individual method override, or `*&#47;*` for overriding all methods in the stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L92">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L96">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<{ ... }>;
```


The settings block, see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/methodSettings.ts#L100">property stageName</a>
</h3>

```typescript
stageName?: pulumi.Input<string>;
```


The name of the stage

<h2 class="pdoc-module-header" id="MethodState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L136">interface MethodState</a>
</h2>

Input properties used for looking up and filtering Method resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L140">property apiKeyRequired</a>
</h3>

```typescript
apiKeyRequired?: pulumi.Input<boolean>;
```


Specify if the method requires an API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L144">property authorization</a>
</h3>

```typescript
authorization?: pulumi.Input<string>;
```


The type of authorization used for the method (`NONE`, `CUSTOM`, `AWS_IAM`, `COGNITO_USER_POOLS`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L148">property authorizationScopes</a>
</h3>

```typescript
authorizationScopes?: pulumi.Input<pulumi.Input<string>[]>;
```


The authorization scopes used when the authorization is `COGNITO_USER_POOLS`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L152">property authorizerId</a>
</h3>

```typescript
authorizerId?: pulumi.Input<string>;
```


The authorizer id to be used when the authorization is `CUSTOM` or `COGNITO_USER_POOLS`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L156">property httpMethod</a>
</h3>

```typescript
httpMethod?: pulumi.Input<string>;
```


The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L162">property requestModels</a>
</h3>

```typescript
requestModels?: pulumi.Input<{ ... }>;
```


A map of the API models used for the request's content type
where key is the content type (e.g. `application/json`)
and value is either `Error`, `Empty` (built-in models) or `aws_api_gateway_model`'s `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L174">property requestParameters</a>
</h3>

```typescript
requestParameters?: pulumi.Input<{ ... }>;
```


A map of request query string parameters and headers that should be passed to the integration.
For example:
```hcl
request_parameters = {
"method.request.header.X-Some-Header"         = true
"method.request.querystring.some-query-param" = true
}
```
would define that the header `X-Some-Header` and the query string `some-query-param` must be provided on the request, or

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L178">property requestParametersInJson</a>
</h3>

```typescript
requestParametersInJson?: pulumi.Input<string>;
```


**Deprecated**, use `request_parameters` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L182">property requestValidatorId</a>
</h3>

```typescript
requestValidatorId?: pulumi.Input<string>;
```


The ID of a `aws_api_gateway_request_validator`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L186">property resourceId</a>
</h3>

```typescript
resourceId?: pulumi.Input<string>;
```


The API resource ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/method.ts#L190">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h2 class="pdoc-module-header" id="ModelArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L110">interface ModelArgs</a>
</h2>

The set of arguments for constructing a Model resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L114">property contentType</a>
</h3>

```typescript
contentType: pulumi.Input<string>;
```


The content type of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L118">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L126">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L130">property schema</a>
</h3>

```typescript
schema?: pulumi.Input<string>;
```


The schema of the model in a JSON form

<h2 class="pdoc-module-header" id="ModelState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L84">interface ModelState</a>
</h2>

Input properties used for looking up and filtering Model resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L88">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


The content type of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L92">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the model

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L100">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/model.ts#L104">property schema</a>
</h3>

```typescript
schema?: pulumi.Input<string>;
```


The schema of the model in a JSON form

<h2 class="pdoc-module-header" id="RequestValidatorArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L97">interface RequestValidatorArgs</a>
</h2>

The set of arguments for constructing a RequestValidator resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L101">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the request validator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L105">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated Rest API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L109">property validateRequestBody</a>
</h3>

```typescript
validateRequestBody?: pulumi.Input<boolean>;
```


Boolean whether to validate request body. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L113">property validateRequestParameters</a>
</h3>

```typescript
validateRequestParameters?: pulumi.Input<boolean>;
```


Boolean whether to validate request parameters. Defaults to `false`.

<h2 class="pdoc-module-header" id="RequestValidatorState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L75">interface RequestValidatorState</a>
</h2>

Input properties used for looking up and filtering RequestValidator resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L79">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the request validator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L83">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated Rest API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L87">property validateRequestBody</a>
</h3>

```typescript
validateRequestBody?: pulumi.Input<boolean>;
```


Boolean whether to validate request body. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/requestValidator.ts#L91">property validateRequestParameters</a>
</h3>

```typescript
validateRequestParameters?: pulumi.Input<boolean>;
```


Boolean whether to validate request parameters. Defaults to `false`.

<h2 class="pdoc-module-header" id="ResourceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L103">interface ResourceArgs</a>
</h2>

The set of arguments for constructing a Resource resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L107">property parentId</a>
</h3>

```typescript
parentId: pulumi.Input<string>;
```


The ID of the parent API resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L111">property pathPart</a>
</h3>

```typescript
pathPart: pulumi.Input<string>;
```


The last path segment of this API resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L115">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h2 class="pdoc-module-header" id="ResourceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L81">interface ResourceState</a>
</h2>

Input properties used for looking up and filtering Resource resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L85">property parentId</a>
</h3>

```typescript
parentId?: pulumi.Input<string>;
```


The ID of the parent API resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L89">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


The complete path for this API resource, including all parent paths.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L93">property pathPart</a>
</h3>

```typescript
pathPart?: pulumi.Input<string>;
```


The last path segment of this API resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/resource.ts#L97">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h2 class="pdoc-module-header" id="ResponseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L108">interface ResponseArgs</a>
</h2>

The set of arguments for constructing a Response resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L112">property responseParameters</a>
</h3>

```typescript
responseParameters?: pulumi.Input<{ ... }>;
```


A map specifying the templates used to transform the response body.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L116">property responseTemplates</a>
</h3>

```typescript
responseTemplates?: pulumi.Input<{ ... }>;
```


A map specifying the parameters (paths, query strings and headers) of the Gateway Response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L120">property responseType</a>
</h3>

```typescript
responseType: pulumi.Input<string>;
```


The response type of the associated GatewayResponse.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L124">property restApiId</a>
</h3>

```typescript
restApiId: pulumi.Input<string>;
```


The string identifier of the associated REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L128">property statusCode</a>
</h3>

```typescript
statusCode?: pulumi.Input<string>;
```


The HTTP status code of the Gateway Response.

<h2 class="pdoc-module-header" id="ResponseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L82">interface ResponseState</a>
</h2>

Input properties used for looking up and filtering Response resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L86">property responseParameters</a>
</h3>

```typescript
responseParameters?: pulumi.Input<{ ... }>;
```


A map specifying the templates used to transform the response body.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L90">property responseTemplates</a>
</h3>

```typescript
responseTemplates?: pulumi.Input<{ ... }>;
```


A map specifying the parameters (paths, query strings and headers) of the Gateway Response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L94">property responseType</a>
</h3>

```typescript
responseType?: pulumi.Input<string>;
```


The response type of the associated GatewayResponse.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L98">property restApiId</a>
</h3>

```typescript
restApiId?: pulumi.Input<string>;
```


The string identifier of the associated REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/response.ts#L102">property statusCode</a>
</h3>

```typescript
statusCode?: pulumi.Input<string>;
```


The HTTP status code of the Gateway Response.

<h2 class="pdoc-module-header" id="RestApiArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L166">interface RestApiArgs</a>
</h2>

The set of arguments for constructing a RestApi resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L170">property apiKeySource</a>
</h3>

```typescript
apiKeySource?: pulumi.Input<string>;
```


The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L174">property binaryMediaTypes</a>
</h3>

```typescript
binaryMediaTypes?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L178">property body</a>
</h3>

```typescript
body?: pulumi.Input<string>;
```


An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L182">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L186">property endpointConfiguration</a>
</h3>

```typescript
endpointConfiguration?: pulumi.Input<{ ... }>;
```


Nested argument defining API endpoint configuration including endpoint type. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L190">property minimumCompressionSize</a>
</h3>

```typescript
minimumCompressionSize?: pulumi.Input<number>;
```


Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L194">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L198">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


JSON formatted policy document that controls access to the API Gateway. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)

<h2 class="pdoc-module-header" id="RestApiState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L114">interface RestApiState</a>
</h2>

Input properties used for looking up and filtering RestApi resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L118">property apiKeySource</a>
</h3>

```typescript
apiKeySource?: pulumi.Input<string>;
```


The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L122">property binaryMediaTypes</a>
</h3>

```typescript
binaryMediaTypes?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L126">property body</a>
</h3>

```typescript
body?: pulumi.Input<string>;
```


An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L130">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The creation date of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L134">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L138">property endpointConfiguration</a>
</h3>

```typescript
endpointConfiguration?: pulumi.Input<{ ... }>;
```


Nested argument defining API endpoint configuration including endpoint type. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L144">property executionArn</a>
</h3>

```typescript
executionArn?: pulumi.Input<string>;
```


The execution ARN part to be used in [`lambda_permission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `source_arn`
when allowing API Gateway to invoke a Lambda function,
e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j`, which can be concatenated with allowed stage, method and resource path.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L148">property minimumCompressionSize</a>
</h3>

```typescript
minimumCompressionSize?: pulumi.Input<number>;
```


Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L152">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L156">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


JSON formatted policy document that controls access to the API Gateway. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/restApi.ts#L160">property rootResourceId</a>
</h3>

```typescript
rootResourceId?: pulumi.Input<string>;
```


The resource ID of the REST API's root

<h2 class="pdoc-module-header" id="StageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L213">interface StageArgs</a>
</h2>

The set of arguments for constructing a Stage resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L217">property accessLogSettings</a>
</h3>

```typescript
accessLogSettings?: pulumi.Input<{ ... }>;
```


Enables access logs for the API stage. Detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L221">property cacheClusterEnabled</a>
</h3>

```typescript
cacheClusterEnabled?: pulumi.Input<boolean>;
```


Specifies whether a cache cluster is enabled for the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L226">property cacheClusterSize</a>
</h3>

```typescript
cacheClusterSize?: pulumi.Input<string>;
```


The size of the cache cluster for the stage, if enabled.
Allowed values include `0.5`, `1.6`, `6.1`, `13.5`, `28.4`, `58.2`, `118` and `237`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L230">property clientCertificateId</a>
</h3>

```typescript
clientCertificateId?: pulumi.Input<string>;
```


The identifier of a client certificate for the stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L234">property deployment</a>
</h3>

```typescript
deployment: pulumi.Input<Deployment>;
```


The ID of the deployment that the stage points to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L238">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L242">property documentationVersion</a>
</h3>

```typescript
documentationVersion?: pulumi.Input<string>;
```


The version of the associated API documentation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L246">property restApi</a>
</h3>

```typescript
restApi: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L250">property stageName</a>
</h3>

```typescript
stageName: pulumi.Input<string>;
```


The name of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L254">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L258">property variables</a>
</h3>

```typescript
variables?: pulumi.Input<{ ... }>;
```


A map that defines the stage variables

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L262">property xrayTracingEnabled</a>
</h3>

```typescript
xrayTracingEnabled?: pulumi.Input<boolean>;
```


Whether active tracing with X-ray is enabled. Defaults to `false`.

<h2 class="pdoc-module-header" id="StageState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L147">interface StageState</a>
</h2>

Input properties used for looking up and filtering Stage resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L151">property accessLogSettings</a>
</h3>

```typescript
accessLogSettings?: pulumi.Input<{ ... }>;
```


Enables access logs for the API stage. Detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L155">property cacheClusterEnabled</a>
</h3>

```typescript
cacheClusterEnabled?: pulumi.Input<boolean>;
```


Specifies whether a cache cluster is enabled for the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L160">property cacheClusterSize</a>
</h3>

```typescript
cacheClusterSize?: pulumi.Input<string>;
```


The size of the cache cluster for the stage, if enabled.
Allowed values include `0.5`, `1.6`, `6.1`, `13.5`, `28.4`, `58.2`, `118` and `237`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L164">property clientCertificateId</a>
</h3>

```typescript
clientCertificateId?: pulumi.Input<string>;
```


The identifier of a client certificate for the stage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L168">property deployment</a>
</h3>

```typescript
deployment?: pulumi.Input<Deployment>;
```


The ID of the deployment that the stage points to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L172">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L176">property documentationVersion</a>
</h3>

```typescript
documentationVersion?: pulumi.Input<string>;
```


The version of the associated API documentation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L182">property executionArn</a>
</h3>

```typescript
executionArn?: pulumi.Input<string>;
```


The execution ARN to be used in [`lambda_permission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `source_arn`
when allowing API Gateway to invoke a Lambda function,
e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L187">property invokeUrl</a>
</h3>

```typescript
invokeUrl?: pulumi.Input<string>;
```


The URL to invoke the API pointing to the stage,
e.g. `https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L191">property restApi</a>
</h3>

```typescript
restApi?: pulumi.Input<RestApi>;
```


The ID of the associated REST API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L195">property stageName</a>
</h3>

```typescript
stageName?: pulumi.Input<string>;
```


The name of the stage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L199">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L203">property variables</a>
</h3>

```typescript
variables?: pulumi.Input<{ ... }>;
```


A map that defines the stage variables

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/stage.ts#L207">property xrayTracingEnabled</a>
</h3>

```typescript
xrayTracingEnabled?: pulumi.Input<boolean>;
```


Whether active tracing with X-ray is enabled. Defaults to `false`.

<h2 class="pdoc-module-header" id="UsagePlanArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L112">interface UsagePlanArgs</a>
</h2>

The set of arguments for constructing a UsagePlan resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L116">property apiStages</a>
</h3>

```typescript
apiStages?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The associated API stages of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L120">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of a usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L124">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L128">property productCode</a>
</h3>

```typescript
productCode?: pulumi.Input<string>;
```


The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L132">property quotaSettings</a>
</h3>

```typescript
quotaSettings?: pulumi.Input<{ ... }>;
```


The quota settings of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L136">property throttleSettings</a>
</h3>

```typescript
throttleSettings?: pulumi.Input<{ ... }>;
```


The throttling limits of the usage plan.

<h2 class="pdoc-module-header" id="UsagePlanKeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L111">interface UsagePlanKeyArgs</a>
</h2>

The set of arguments for constructing a UsagePlanKey resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L115">property keyId</a>
</h3>

```typescript
keyId: pulumi.Input<string>;
```


The identifier of the API key resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L119">property keyType</a>
</h3>

```typescript
keyType: pulumi.Input<string>;
```


The type of the API key resource. Currently, the valid key type is API_KEY.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L123">property usagePlanId</a>
</h3>

```typescript
usagePlanId: pulumi.Input<string>;
```


The Id of the usage plan resource representing to associate the key to.

<h2 class="pdoc-module-header" id="UsagePlanKeyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L85">interface UsagePlanKeyState</a>
</h2>

Input properties used for looking up and filtering UsagePlanKey resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L89">property keyId</a>
</h3>

```typescript
keyId?: pulumi.Input<string>;
```


The identifier of the API key resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L93">property keyType</a>
</h3>

```typescript
keyType?: pulumi.Input<string>;
```


The type of the API key resource. Currently, the valid key type is API_KEY.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of a usage plan key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L101">property usagePlanId</a>
</h3>

```typescript
usagePlanId?: pulumi.Input<string>;
```


The Id of the usage plan resource representing to associate the key to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlanKey.ts#L105">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


The value of a usage plan key.

<h2 class="pdoc-module-header" id="UsagePlanState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L82">interface UsagePlanState</a>
</h2>

Input properties used for looking up and filtering UsagePlan resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L86">property apiStages</a>
</h3>

```typescript
apiStages?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The associated API stages of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L90">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of a usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L98">property productCode</a>
</h3>

```typescript
productCode?: pulumi.Input<string>;
```


The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L102">property quotaSettings</a>
</h3>

```typescript
quotaSettings?: pulumi.Input<{ ... }>;
```


The quota settings of the usage plan.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/usagePlan.ts#L106">property throttleSettings</a>
</h3>

```typescript
throttleSettings?: pulumi.Input<{ ... }>;
```


The throttling limits of the usage plan.

<h2 class="pdoc-module-header" id="VpcLinkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L85">interface VpcLinkArgs</a>
</h2>

The set of arguments for constructing a VpcLink resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L89">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the VPC link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name used to label and identify the VPC link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L97">property targetArn</a>
</h3>

```typescript
targetArn: pulumi.Input<string>;
```


The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.

<h2 class="pdoc-module-header" id="VpcLinkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L67">interface VpcLinkState</a>
</h2>

Input properties used for looking up and filtering VpcLink resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L71">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the VPC link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L75">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name used to label and identify the VPC link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/apigateway/vpcLink.ts#L79">property targetArn</a>
</h3>

```typescript
targetArn?: pulumi.Input<string>;
```


The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.

