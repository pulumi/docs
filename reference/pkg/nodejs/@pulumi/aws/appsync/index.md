---
title: Module appsync
---

<a href="../index.html">@pulumi/aws</a> &gt; appsync

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ApiKey">class ApiKey</a>
* <a href="#DataSource">class DataSource</a>
* <a href="#GraphQLApi">class GraphQLApi</a>
* <a href="#ApiKeyArgs">interface ApiKeyArgs</a>
* <a href="#ApiKeyState">interface ApiKeyState</a>
* <a href="#DataSourceArgs">interface DataSourceArgs</a>
* <a href="#DataSourceState">interface DataSourceState</a>
* <a href="#GraphQLApiArgs">interface GraphQLApiArgs</a>
* <a href="#GraphQLApiState">interface GraphQLApiState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts">appsync/apiKey.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts">appsync/dataSource.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts">appsync/graphQLApi.ts</a> 


<h2 class="pdoc-module-header" id="ApiKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L9">class ApiKey</a>
</h2>

Provides an AppSync API Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L37">constructor</a>
</h3>

```typescript
new ApiKey(name: string, args: ApiKeyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ApiKey resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L25">property apiId</a>
</h3>

```typescript
public apiId: pulumi.Output<string>;
```


The ID of the associated AppSync API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The API key description. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L33">property expires</a>
</h3>

```typescript
public expires: pulumi.Output<string | undefined>;
```


RFC3339 string representation of the expiry date. Rounded down to nearest hour. By default, it is 7 days from the date of creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L37">property key</a>
</h3>

```typescript
public key: pulumi.Output<string>;
```


The API key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DataSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L9">class DataSource</a>
</h2>

Provides an AppSync DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L57">constructor</a>
</h3>

```typescript
new DataSource(name: string, args: DataSourceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DataSource resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DataSourceState): DataSource
```


Get an existing DataSource resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L25">property apiId</a>
</h3>

```typescript
public apiId: pulumi.Output<string>;
```


The API ID for the GraphQL API for the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L37">property dynamodbConfig</a>
</h3>

```typescript
public dynamodbConfig: pulumi.Output<{ ... } | undefined>;
```


DynamoDB settings. See [below](#dynamodb_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L41">property elasticsearchConfig</a>
</h3>

```typescript
public elasticsearchConfig: pulumi.Output<{ ... } | undefined>;
```


Amazon Elasticsearch settings. See [below](#elasticsearch_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L45">property lambdaConfig</a>
</h3>

```typescript
public lambdaConfig: pulumi.Output<{ ... } | undefined>;
```


AWS Lambda settings. See [below](#lambda_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A user-supplied name for the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L53">property serviceRoleArn</a>
</h3>

```typescript
public serviceRoleArn: pulumi.Output<string | undefined>;
```


The IAM service role ARN for the data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L57">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB` and `AMAZON_ELASTICSEARCH`, `NONE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="GraphQLApi">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L9">class GraphQLApi</a>
</h2>

Provides an AppSync GraphQL API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L37">constructor</a>
</h3>

```typescript
new GraphQLApi(name: string, args: GraphQLApiArgs, opts?: pulumi.CustomResourceOptions)
```


Create a GraphQLApi resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GraphQLApiState): GraphQLApi
```


Get an existing GraphQLApi resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L29">property authenticationType</a>
</h3>

```typescript
public authenticationType: pulumi.Output<string>;
```


The authentication type. Valid values: `API_KEY`, `AWS_IAM` and `AMAZON_COGNITO_USER_POOLS`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A user-supplied name for the GraphqlApi.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L37">property userPoolConfig</a>
</h3>

```typescript
public userPoolConfig: pulumi.Output<{ ... } | undefined>;
```


The Amazon Cognito User Pool configuration. See [below](#user_pool_config)

<h2 class="pdoc-module-header" id="ApiKeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L94">interface ApiKeyArgs</a>
</h2>

The set of arguments for constructing a ApiKey resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L98">property apiId</a>
</h3>

```typescript
apiId: pulumi.Input<string>;
```


The ID of the associated AppSync API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L102">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The API key description. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L106">property expires</a>
</h3>

```typescript
expires?: pulumi.Input<string>;
```


RFC3339 string representation of the expiry date. Rounded down to nearest hour. By default, it is 7 days from the date of creation.

<h2 class="pdoc-module-header" id="ApiKeyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L72">interface ApiKeyState</a>
</h2>

Input properties used for looking up and filtering ApiKey resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L76">property apiId</a>
</h3>

```typescript
apiId?: pulumi.Input<string>;
```


The ID of the associated AppSync API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L80">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The API key description. Defaults to "Managed by Terraform".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L84">property expires</a>
</h3>

```typescript
expires?: pulumi.Input<string>;
```


RFC3339 string representation of the expiry date. Rounded down to nearest hour. By default, it is 7 days from the date of creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/apiKey.ts#L88">property key</a>
</h3>

```typescript
key?: pulumi.Input<string>;
```


The API key

<h2 class="pdoc-module-header" id="DataSourceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L147">interface DataSourceArgs</a>
</h2>

The set of arguments for constructing a DataSource resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L151">property apiId</a>
</h3>

```typescript
apiId: pulumi.Input<string>;
```


The API ID for the GraphQL API for the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L155">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L159">property dynamodbConfig</a>
</h3>

```typescript
dynamodbConfig?: pulumi.Input<{ ... }>;
```


DynamoDB settings. See [below](#dynamodb_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L163">property elasticsearchConfig</a>
</h3>

```typescript
elasticsearchConfig?: pulumi.Input<{ ... }>;
```


Amazon Elasticsearch settings. See [below](#elasticsearch_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L167">property lambdaConfig</a>
</h3>

```typescript
lambdaConfig?: pulumi.Input<{ ... }>;
```


AWS Lambda settings. See [below](#lambda_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L171">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A user-supplied name for the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L175">property serviceRoleArn</a>
</h3>

```typescript
serviceRoleArn?: pulumi.Input<string>;
```


The IAM service role ARN for the data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L179">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB` and `AMAZON_ELASTICSEARCH`, `NONE`.

<h2 class="pdoc-module-header" id="DataSourceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L105">interface DataSourceState</a>
</h2>

Input properties used for looking up and filtering DataSource resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L109">property apiId</a>
</h3>

```typescript
apiId?: pulumi.Input<string>;
```


The API ID for the GraphQL API for the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L113">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L117">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L121">property dynamodbConfig</a>
</h3>

```typescript
dynamodbConfig?: pulumi.Input<{ ... }>;
```


DynamoDB settings. See [below](#dynamodb_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L125">property elasticsearchConfig</a>
</h3>

```typescript
elasticsearchConfig?: pulumi.Input<{ ... }>;
```


Amazon Elasticsearch settings. See [below](#elasticsearch_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L129">property lambdaConfig</a>
</h3>

```typescript
lambdaConfig?: pulumi.Input<{ ... }>;
```


AWS Lambda settings. See [below](#lambda_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L133">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A user-supplied name for the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L137">property serviceRoleArn</a>
</h3>

```typescript
serviceRoleArn?: pulumi.Input<string>;
```


The IAM service role ARN for the data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/dataSource.ts#L141">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB` and `AMAZON_ELASTICSEARCH`, `NONE`.

<h2 class="pdoc-module-header" id="GraphQLApiArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L94">interface GraphQLApiArgs</a>
</h2>

The set of arguments for constructing a GraphQLApi resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L98">property authenticationType</a>
</h3>

```typescript
authenticationType: pulumi.Input<string>;
```


The authentication type. Valid values: `API_KEY`, `AWS_IAM` and `AMAZON_COGNITO_USER_POOLS`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L102">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A user-supplied name for the GraphqlApi.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L106">property userPoolConfig</a>
</h3>

```typescript
userPoolConfig?: pulumi.Input<{ ... }>;
```


The Amazon Cognito User Pool configuration. See [below](#user_pool_config)

<h2 class="pdoc-module-header" id="GraphQLApiState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L72">interface GraphQLApiState</a>
</h2>

Input properties used for looking up and filtering GraphQLApi resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L76">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L80">property authenticationType</a>
</h3>

```typescript
authenticationType?: pulumi.Input<string>;
```


The authentication type. Valid values: `API_KEY`, `AWS_IAM` and `AMAZON_COGNITO_USER_POOLS`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L84">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A user-supplied name for the GraphqlApi.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/appsync/graphQLApi.ts#L88">property userPoolConfig</a>
</h3>

```typescript
userPoolConfig?: pulumi.Input<{ ... }>;
```


The Amazon Cognito User Pool configuration. See [below](#user_pool_config)

