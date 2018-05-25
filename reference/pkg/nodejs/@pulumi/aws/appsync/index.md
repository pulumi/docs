---
title: Module appsync
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#DataSource">class DataSource</a>
* <a href="#GraphQLApi">class GraphQLApi</a>
* <a href="#DataSourceArgs">interface DataSourceArgs</a>
* <a href="#DataSourceState">interface DataSourceState</a>
* <a href="#GraphQLApiArgs">interface GraphQLApiArgs</a>
* <a href="#GraphQLApiState">interface GraphQLApiState</a>

<a href="/appsync/dataSource.ts">appsync/dataSource.ts</a> <a href="/appsync/graphQLApi.ts">appsync/graphQLApi.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="DataSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L9">class DataSource</a>
</h2>

Provides an AppSync DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L57">constructor</a>
</h3>

```typescript
new DataSource(name: string, args: DataSourceArgs, opts?: pulumi.ResourceOptions)
```


Create a DataSource resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new DataSource(name: string, state?: DataSourceState, opts?: pulumi.ResourceOptions)
```


Create a DataSource resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DataSourceState): DataSource
```


Get an existing DataSource resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L25">property apiId</a>
</h3>

```typescript
public apiId: pulumi.Output<string>;
```


The API ID for the GraphQL API for the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L37">property dynamodbConfig</a>
</h3>

```typescript
public dynamodbConfig: pulumi.Output<{ ... } | undefined>;
```


DynamoDB settings. See [below](#dynamodb_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L41">property elasticsearchConfig</a>
</h3>

```typescript
public elasticsearchConfig: pulumi.Output<{ ... } | undefined>;
```


Amazon Elasticsearch settings. See [below](#elasticsearch_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L45">property lambdaConfig</a>
</h3>

```typescript
public lambdaConfig: pulumi.Output<{ ... } | undefined>;
```


AWS Lambda settings. See [below](#lambda_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A user-supplied name for the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L53">property serviceRoleArn</a>
</h3>

```typescript
public serviceRoleArn: pulumi.Output<string | undefined>;
```


The IAM service role ARN for the data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L57">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB` and `AMAZON_ELASTICSEARCH`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="GraphQLApi">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L9">class GraphQLApi</a>
</h2>

Provides an AppSync GraphQL API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L37">constructor</a>
</h3>

```typescript
new GraphQLApi(name: string, args: GraphQLApiArgs, opts?: pulumi.ResourceOptions)
```


Create a GraphQLApi resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new GraphQLApi(name: string, state?: GraphQLApiState, opts?: pulumi.ResourceOptions)
```


Create a GraphQLApi resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GraphQLApiState): GraphQLApi
```


Get an existing GraphQLApi resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L29">property authenticationType</a>
</h3>

```typescript
public authenticationType: pulumi.Output<string>;
```


The authentication type. Valid values: `API_KEY`, `AWS_IAM` and `AMAZON_COGNITO_USER_POOLS`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A user-supplied name for the GraphqlApi.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L37">property userPoolConfig</a>
</h3>

```typescript
public userPoolConfig: pulumi.Output<{ ... } | undefined>;
```


The Amazon Cognito User Pool configuration. See [below](#user_pool_config)

<h2 class="pdoc-module-header" id="DataSourceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L149">interface DataSourceArgs</a>
</h2>

The set of arguments for constructing a DataSource resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L153">property apiId</a>
</h3>

```typescript
apiId: pulumi.Input<string>;
```


The API ID for the GraphQL API for the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L157">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L161">property dynamodbConfig</a>
</h3>

```typescript
dynamodbConfig?: pulumi.Input<{ ... }>;
```


DynamoDB settings. See [below](#dynamodb_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L165">property elasticsearchConfig</a>
</h3>

```typescript
elasticsearchConfig?: pulumi.Input<{ ... }>;
```


Amazon Elasticsearch settings. See [below](#elasticsearch_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L169">property lambdaConfig</a>
</h3>

```typescript
lambdaConfig?: pulumi.Input<{ ... }>;
```


AWS Lambda settings. See [below](#lambda_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L173">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A user-supplied name for the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L177">property serviceRoleArn</a>
</h3>

```typescript
serviceRoleArn?: pulumi.Input<string>;
```


The IAM service role ARN for the data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L181">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB` and `AMAZON_ELASTICSEARCH`

<h2 class="pdoc-module-header" id="DataSourceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L107">interface DataSourceState</a>
</h2>

Input properties used for looking up and filtering DataSource resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L111">property apiId</a>
</h3>

```typescript
apiId?: pulumi.Input<string>;
```


The API ID for the GraphQL API for the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L115">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L119">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L123">property dynamodbConfig</a>
</h3>

```typescript
dynamodbConfig?: pulumi.Input<{ ... }>;
```


DynamoDB settings. See [below](#dynamodb_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L127">property elasticsearchConfig</a>
</h3>

```typescript
elasticsearchConfig?: pulumi.Input<{ ... }>;
```


Amazon Elasticsearch settings. See [below](#elasticsearch_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L131">property lambdaConfig</a>
</h3>

```typescript
lambdaConfig?: pulumi.Input<{ ... }>;
```


AWS Lambda settings. See [below](#lambda_config)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A user-supplied name for the DataSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L139">property serviceRoleArn</a>
</h3>

```typescript
serviceRoleArn?: pulumi.Input<string>;
```


The IAM service role ARN for the data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/dataSource.ts#L143">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB` and `AMAZON_ELASTICSEARCH`

<h2 class="pdoc-module-header" id="GraphQLApiArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L96">interface GraphQLApiArgs</a>
</h2>

The set of arguments for constructing a GraphQLApi resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L100">property authenticationType</a>
</h3>

```typescript
authenticationType: pulumi.Input<string>;
```


The authentication type. Valid values: `API_KEY`, `AWS_IAM` and `AMAZON_COGNITO_USER_POOLS`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A user-supplied name for the GraphqlApi.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L108">property userPoolConfig</a>
</h3>

```typescript
userPoolConfig?: pulumi.Input<{ ... }>;
```


The Amazon Cognito User Pool configuration. See [below](#user_pool_config)

<h2 class="pdoc-module-header" id="GraphQLApiState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L74">interface GraphQLApiState</a>
</h2>

Input properties used for looking up and filtering GraphQLApi resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L78">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L82">property authenticationType</a>
</h3>

```typescript
authenticationType?: pulumi.Input<string>;
```


The authentication type. Valid values: `API_KEY`, `AWS_IAM` and `AMAZON_COGNITO_USER_POOLS`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L86">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A user-supplied name for the GraphqlApi.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/appsync/graphQLApi.ts#L90">property userPoolConfig</a>
</h3>

```typescript
userPoolConfig?: pulumi.Input<{ ... }>;
```


The Amazon Cognito User Pool configuration. See [below](#user_pool_config)

