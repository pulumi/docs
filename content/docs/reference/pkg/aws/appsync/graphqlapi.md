
---
title: "GraphQLApi"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an AppSync GraphQL API.

## Example Usage

### API Key Authentication

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.appsync.GraphQLApi("example", {
    authenticationType: "API_KEY",
});
```

### AWS Cognito User Pool Authentication

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.appsync.GraphQLApi("example", {
    authenticationType: "AMAZON_COGNITO_USER_POOLS",
    userPoolConfig: {
        awsRegion: aws_region_current.name,
        defaultAction: "DENY",
        userPoolId: aws_cognito_user_pool_example.id,
    },
});
```

### AWS IAM Authentication

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.appsync.GraphQLApi("example", {
    authenticationType: "AWS_IAM",
});
```

### With Schema

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.appsync.GraphQLApi("example", {
    authenticationType: "AWS_IAM",
    schema: `schema {
	query: Query
}
type Query {
  test: Int
}
`,
});
```

### OpenID Connect Authentication

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.appsync.GraphQLApi("example", {
    authenticationType: "OPENID_CONNECT",
    openidConnectConfig: {
        issuer: "https://example.com",
    },
});
```

### With Multiple Authentication Providers

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.appsync.GraphQLApi("example", {
    additionalAuthenticationProviders: [{
        authenticationType: "AWS_IAM",
    }],
    authenticationType: "API_KEY",
});
```

### Enabling Logging

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleRole = new aws.iam.Role("example", {
    assumeRolePolicy: `{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "appsync.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
}
`,
});
const exampleRolePolicyAttachment = new aws.iam.RolePolicyAttachment("example", {
    policyArn: "arn:aws:iam::aws:policy/service-role/AWSAppSyncPushToCloudWatchLogs",
    role: exampleRole.name,
});
const exampleGraphQLApi = new aws.appsync.GraphQLApi("example", {
    logConfig: {
        cloudwatchLogsRoleArn: exampleRole.arn,
        fieldLogLevel: "ERROR",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_graphql_api.html.markdown.



## Create a GraphQLApi Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#GraphQLApi">GraphQLApi</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#GraphQLApiArgs">GraphQLApiArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">GraphQLApi</span><span class="p">(resource_name, opts=None, </span>additional_authentication_providers=None<span class="p">, </span>authentication_type=None<span class="p">, </span>log_config=None<span class="p">, </span>name=None<span class="p">, </span>openid_connect_config=None<span class="p">, </span>schema=None<span class="p">, </span>tags=None<span class="p">, </span>user_pool_config=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewGraphQLApi<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiArgs">GraphQLApiArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApi">GraphQLApi</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApi.html">GraphQLApi</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiArgs.html">GraphQLApiArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a GraphQLApi resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Additional<wbr>Authentication<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovider">List&lt;Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more additional authentication providers for the GraphqlApi. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authentication<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapilogconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>Log<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing logging configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A user-supplied name for the GraphqlApi.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiopenidconnectconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>Openid<wbr>Connect<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schema</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiuserpoolconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>User<wbr>Pool<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Additional<wbr>Authentication<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovider">[]appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more additional authentication providers for the GraphqlApi. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authentication<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapilogconfig">*appsync.<wbr>Graph<wbr>QLApi<wbr>Log<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing logging configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A user-supplied name for the GraphqlApi.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiopenidconnectconfig">*appsync.<wbr>Graph<wbr>QLApi<wbr>Openid<wbr>Connect<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schema</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiuserpoolconfig">*appsync.<wbr>Graph<wbr>QLApi<wbr>User<wbr>Pool<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">additional<wbr>Authentication<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovider">appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more additional authentication providers for the GraphqlApi. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authentication<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapilogconfig">appsync.<wbr>Graph<wbr>QLApi<wbr>Log<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing logging configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A user-supplied name for the GraphqlApi.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid<wbr>Connect<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiopenidconnectconfig">appsync.<wbr>Graph<wbr>QLApi<wbr>Openid<wbr>Connect<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schema</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiuserpoolconfig">appsync.<wbr>Graph<wbr>QLApi<wbr>User<wbr>Pool<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">additional_<wbr>authentication_<wbr>providers</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovider">List[graph_<wbr>ql_<wbr>api_<wbr>additional_<wbr>authentication_<wbr>provider]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more additional authentication providers for the GraphqlApi. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authentication_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapilogconfig">Dict[graph_<wbr>ql_<wbr>api_<wbr>log_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing logging configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A user-supplied name for the GraphqlApi.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid_<wbr>connect_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiopenidconnectconfig">Dict[graph_<wbr>ql_<wbr>api_<wbr>openid_<wbr>connect_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schema</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiuserpoolconfig">Dict[graph_<wbr>ql_<wbr>api_<wbr>user_<wbr>pool_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## GraphQLApi Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Additional<wbr>Authentication<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovider">List&lt;Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more additional authentication providers for the GraphqlApi. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authentication<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapilogconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>Log<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument containing logging configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A user-supplied name for the GraphqlApi.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiopenidconnectconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>Openid<wbr>Connect<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schema</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Uris</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} Map of URIs associated with the API. e.g. `uris[&#34;GRAPHQL&#34;] = https://ID.appsync-api.REGION.amazonaws.com/graphql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiuserpoolconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>User<wbr>Pool<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Additional<wbr>Authentication<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovider">[]appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more additional authentication providers for the GraphqlApi. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authentication<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapilogconfig">*appsync.<wbr>Graph<wbr>QLApi<wbr>Log<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument containing logging configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A user-supplied name for the GraphqlApi.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiopenidconnectconfig">*appsync.<wbr>Graph<wbr>QLApi<wbr>Openid<wbr>Connect<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schema</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Uris</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} Map of URIs associated with the API. e.g. `uris[&#34;GRAPHQL&#34;] = https://ID.appsync-api.REGION.amazonaws.com/graphql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiuserpoolconfig">*appsync.<wbr>Graph<wbr>QLApi<wbr>User<wbr>Pool<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">additional<wbr>Authentication<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovider">appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more additional authentication providers for the GraphqlApi. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authentication<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapilogconfig">appsync.<wbr>Graph<wbr>QLApi<wbr>Log<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument containing logging configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A user-supplied name for the GraphqlApi.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid<wbr>Connect<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiopenidconnectconfig">appsync.<wbr>Graph<wbr>QLApi<wbr>Openid<wbr>Connect<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schema</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">uris</td>
            <td class="align-top">
                
                <code>{[key: string]: string}</code>
            </td>
            <td class="align-top">{{% md %}} Map of URIs associated with the API. e.g. `uris[&#34;GRAPHQL&#34;] = https://ID.appsync-api.REGION.amazonaws.com/graphql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiuserpoolconfig">appsync.<wbr>Graph<wbr>QLApi<wbr>User<wbr>Pool<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">additional_<wbr>authentication_<wbr>providers</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovider">List[graph_<wbr>ql_<wbr>api_<wbr>additional_<wbr>authentication_<wbr>provider]</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more additional authentication providers for the GraphqlApi. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authentication_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapilogconfig">Dict[graph_<wbr>ql_<wbr>api_<wbr>log_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument containing logging configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A user-supplied name for the GraphqlApi.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid_<wbr>connect_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiopenidconnectconfig">Dict[graph_<wbr>ql_<wbr>api_<wbr>openid_<wbr>connect_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schema</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">uris</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} Map of URIs associated with the API. e.g. `uris[&#34;GRAPHQL&#34;] = https://ID.appsync-api.REGION.amazonaws.com/graphql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiuserpoolconfig">Dict[graph_<wbr>ql_<wbr>api_<wbr>user_<wbr>pool_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing GraphQLApi Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#GraphQLApiState">GraphQLApiState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#GraphQLApi">GraphQLApi</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>additional_authentication_providers=None<span class="p">, </span>arn=None<span class="p">, </span>authentication_type=None<span class="p">, </span>log_config=None<span class="p">, </span>name=None<span class="p">, </span>openid_connect_config=None<span class="p">, </span>schema=None<span class="p">, </span>tags=None<span class="p">, </span>uris=None<span class="p">, </span>user_pool_config=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetGraphQLApi<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiState">GraphQLApiState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApi">GraphQLApi</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApi.html">GraphQLApi</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiState.html">GraphQLApiState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing GraphQLApi resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Additional<wbr>Authentication<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovider">List&lt;Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more additional authentication providers for the GraphqlApi. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authentication<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapilogconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>Log<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing logging configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A user-supplied name for the GraphqlApi.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiopenidconnectconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>Openid<wbr>Connect<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schema</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Uris</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Map of URIs associated with the API. e.g. `uris[&#34;GRAPHQL&#34;] = https://ID.appsync-api.REGION.amazonaws.com/graphql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiuserpoolconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>User<wbr>Pool<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Additional<wbr>Authentication<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovider">[]appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more additional authentication providers for the GraphqlApi. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authentication<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapilogconfig">*appsync.<wbr>Graph<wbr>QLApi<wbr>Log<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing logging configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A user-supplied name for the GraphqlApi.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiopenidconnectconfig">*appsync.<wbr>Graph<wbr>QLApi<wbr>Openid<wbr>Connect<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schema</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Uris</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Map of URIs associated with the API. e.g. `uris[&#34;GRAPHQL&#34;] = https://ID.appsync-api.REGION.amazonaws.com/graphql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiuserpoolconfig">*appsync.<wbr>Graph<wbr>QLApi<wbr>User<wbr>Pool<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">additional<wbr>Authentication<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovider">appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more additional authentication providers for the GraphqlApi. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authentication<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapilogconfig">appsync.<wbr>Graph<wbr>QLApi<wbr>Log<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing logging configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A user-supplied name for the GraphqlApi.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid<wbr>Connect<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiopenidconnectconfig">appsync.<wbr>Graph<wbr>QLApi<wbr>Openid<wbr>Connect<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schema</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">uris</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Map of URIs associated with the API. e.g. `uris[&#34;GRAPHQL&#34;] = https://ID.appsync-api.REGION.amazonaws.com/graphql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiuserpoolconfig">appsync.<wbr>Graph<wbr>QLApi<wbr>User<wbr>Pool<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">additional_<wbr>authentication_<wbr>providers</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovider">List[graph_<wbr>ql_<wbr>api_<wbr>additional_<wbr>authentication_<wbr>provider]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more additional authentication providers for the GraphqlApi. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authentication_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapilogconfig">Dict[graph_<wbr>ql_<wbr>api_<wbr>log_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing logging configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A user-supplied name for the GraphqlApi.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid_<wbr>connect_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiopenidconnectconfig">Dict[graph_<wbr>ql_<wbr>api_<wbr>openid_<wbr>connect_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schema</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">uris</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Map of URIs associated with the API. e.g. `uris[&#34;GRAPHQL&#34;] = https://ID.appsync-api.REGION.amazonaws.com/graphql`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiuserpoolconfig">Dict[graph_<wbr>ql_<wbr>api_<wbr>user_<wbr>pool_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### GraphQLApiAdditionalAuthenticationProvider
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GraphQLApiAdditionalAuthenticationProvider">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GraphQLApiAdditionalAuthenticationProvider">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiAdditionalAuthenticationProviderArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiAdditionalAuthenticationProviderOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiAdditionalAuthenticationProviderArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiAdditionalAuthenticationProvider.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Authentication<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovideropenidconnectconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider<wbr>Openid<wbr>Connect<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovideruserpoolconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider<wbr>User<wbr>Pool<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Authentication<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovideropenidconnectconfig">*appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider<wbr>Openid<wbr>Connect<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovideruserpoolconfig">*appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider<wbr>User<wbr>Pool<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">authentication<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid<wbr>Connect<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovideropenidconnectconfig">appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider<wbr>Openid<wbr>Connect<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovideruserpoolconfig">appsync.<wbr>Graph<wbr>QLApi<wbr>Additional<wbr>Authentication<wbr>Provider<wbr>User<wbr>Pool<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">authentication_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid_<wbr>connect_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovideropenidconnectconfig">Dict[graph_<wbr>ql_<wbr>api_<wbr>additional_<wbr>authentication_<wbr>provider_<wbr>openid_<wbr>connect_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing OpenID Connect configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#graphqlapiadditionalauthenticationprovideruserpoolconfig">Dict[graph_<wbr>ql_<wbr>api_<wbr>additional_<wbr>authentication_<wbr>provider_<wbr>user_<wbr>pool_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Cognito User Pool configuration. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfig.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Auth<wbr>Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being authenticated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iat<wbr>Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being issued to a user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Issuer</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Auth<wbr>Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being authenticated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iat<wbr>Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being issued to a user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Issuer</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">auth<wbr>Ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being authenticated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iat<wbr>Ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being issued to a user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">issuer</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">auth_<wbr>ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being authenticated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iat_<wbr>ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being issued to a user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">issuer</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GraphQLApiAdditionalAuthenticationProviderUserPoolConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GraphQLApiAdditionalAuthenticationProviderUserPoolConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GraphQLApiAdditionalAuthenticationProviderUserPoolConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiAdditionalAuthenticationProviderUserPoolConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiAdditionalAuthenticationProviderUserPoolConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiAdditionalAuthenticationProviderUserPoolConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiAdditionalAuthenticationProviderUserPoolConfig.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">App<wbr>Id<wbr>Client<wbr>Regex</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A regular expression for validating the incoming Amazon Cognito User Pool app client ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aws<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS region in which the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user pool ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">App<wbr>Id<wbr>Client<wbr>Regex</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A regular expression for validating the incoming Amazon Cognito User Pool app client ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aws<wbr>Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS region in which the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user pool ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">app<wbr>Id<wbr>Client<wbr>Regex</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A regular expression for validating the incoming Amazon Cognito User Pool app client ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aws<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS region in which the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user pool ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">app_<wbr>id_<wbr>client_<wbr>regex</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A regular expression for validating the incoming Amazon Cognito User Pool app client ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aws_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS region in which the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user pool ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GraphQLApiLogConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GraphQLApiLogConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GraphQLApiLogConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiLogConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiLogConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiLogConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiLogConfig.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logs<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name of the service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Field<wbr>Log<wbr>Level</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Field logging level. Valid values: `ALL`, `ERROR`, `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logs<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name of the service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Field<wbr>Log<wbr>Level</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Field logging level. Valid values: `ALL`, `ERROR`, `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Logs<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name of the service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">field<wbr>Log<wbr>Level</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Field logging level. Valid values: `ALL`, `ERROR`, `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>logs_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name of the service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">field_<wbr>log_<wbr>level</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Field logging level. Valid values: `ALL`, `ERROR`, `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GraphQLApiOpenidConnectConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GraphQLApiOpenidConnectConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GraphQLApiOpenidConnectConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiOpenidConnectConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiOpenidConnectConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiOpenidConnectConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiOpenidConnectConfig.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Auth<wbr>Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being authenticated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iat<wbr>Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being issued to a user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Issuer</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Auth<wbr>Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being authenticated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iat<wbr>Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being issued to a user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Issuer</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">auth<wbr>Ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being authenticated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iat<wbr>Ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being issued to a user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">issuer</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">auth_<wbr>ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being authenticated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iat_<wbr>ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of milliseconds a token is valid after being issued to a user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">issuer</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GraphQLApiUserPoolConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GraphQLApiUserPoolConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GraphQLApiUserPoolConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiUserPoolConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#GraphQLApiUserPoolConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiUserPoolConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.GraphQLApiUserPoolConfig.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">App<wbr>Id<wbr>Client<wbr>Regex</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A regular expression for validating the incoming Amazon Cognito User Pool app client ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aws<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS region in which the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn&#39;t match the Amazon Cognito User Pool configuration. Valid: `ALLOW` and `DENY`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user pool ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">App<wbr>Id<wbr>Client<wbr>Regex</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A regular expression for validating the incoming Amazon Cognito User Pool app client ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aws<wbr>Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS region in which the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn&#39;t match the Amazon Cognito User Pool configuration. Valid: `ALLOW` and `DENY`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user pool ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">app<wbr>Id<wbr>Client<wbr>Regex</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A regular expression for validating the incoming Amazon Cognito User Pool app client ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aws<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS region in which the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn&#39;t match the Amazon Cognito User Pool configuration. Valid: `ALLOW` and `DENY`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user pool ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">app_<wbr>id_<wbr>client_<wbr>regex</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A regular expression for validating the incoming Amazon Cognito User Pool app client ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aws_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS region in which the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>action</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn&#39;t match the Amazon Cognito User Pool configuration. Valid: `ALLOW` and `DENY`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user pool ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







