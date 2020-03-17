
---
title: "Authorizer"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an API Gateway Authorizer.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const demoRestApi = new aws.apigateway.RestApi("demo", {});
const invocationRole = new aws.iam.Role("invocation_role", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "apigateway.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
`,
    path: "/",
});
const lambda = new aws.iam.Role("lambda", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
`,
});
const authorizer = new aws.lambda.Function("authorizer", {
    code: new pulumi.asset.FileArchive("lambda-function.zip"),
    handler: "exports.example",
    role: lambda.arn,
});
const demoAuthorizer = new aws.apigateway.Authorizer("demo", {
    authorizerCredentials: invocationRole.arn,
    authorizerUri: authorizer.invokeArn,
    restApi: demoRestApi.id,
});
const invocationPolicy = new aws.iam.RolePolicy("invocation_policy", {
    policy: pulumi.interpolate`{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "lambda:InvokeFunction",
      "Effect": "Allow",
      "Resource": "${authorizer.arn}"
    }
  ]
}
`,
    role: invocationRole.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_authorizer.html.markdown.



## Create a Authorizer Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#Authorizer">Authorizer</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#AuthorizerArgs">AuthorizerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Authorizer</span><span class="p">(resource_name, opts=None, </span>authorizer_credentials=None<span class="p">, </span>authorizer_result_ttl_in_seconds=None<span class="p">, </span>authorizer_uri=None<span class="p">, </span>identity_source=None<span class="p">, </span>identity_validation_expression=None<span class="p">, </span>name=None<span class="p">, </span>provider_arns=None<span class="p">, </span>rest_api=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAuthorizer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#AuthorizerArgs">AuthorizerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#Authorizer">Authorizer</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.Authorizer.html">Authorizer</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.AuthorizerArgs.html">AuthorizerArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Authorizer resource with the given unique name, arguments, and options.

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
            <td class="align-top">Authorizer<wbr>Credentials</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorizer<wbr>Result<wbr>Ttl<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of cached authorizer results in seconds.
Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorizer<wbr>Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The authorizer&#39;s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `&#34;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Validation<wbr>Expression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn&#39;t match,
the client receives a 401 Unauthorized response.
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
The name of the authorizer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.
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
            <td class="align-top">Authorizer<wbr>Credentials</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorizer<wbr>Result<wbr>Ttl<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of cached authorizer results in seconds.
Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorizer<wbr>Uri</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The authorizer&#39;s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Source</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `&#34;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Validation<wbr>Expression</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn&#39;t match,
the client receives a 401 Unauthorized response.
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
The name of the authorizer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.
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
            <td class="align-top">authorizer<wbr>Credentials</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorizer<wbr>Result<wbr>Ttl<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of cached authorizer results in seconds.
Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorizer<wbr>Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The authorizer&#39;s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `&#34;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Validation<wbr>Expression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn&#39;t match,
the client receives a 401 Unauthorized response.
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
The name of the authorizer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string | Rest<wbr>Api</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.
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
            <td class="align-top">authorizer_<wbr>credentials</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorizer_<wbr>result_<wbr>ttl_<wbr>in_<wbr>seconds</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of cached authorizer results in seconds.
Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorizer_<wbr>uri</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The authorizer&#39;s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>source</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `&#34;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>validation_<wbr>expression</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn&#39;t match,
the client receives a 401 Unauthorized response.
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
The name of the authorizer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provider_<wbr>arns</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest_<wbr>api</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Authorizer Output Properties

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
            <td class="align-top">Authorizer<wbr>Credentials</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorizer<wbr>Result<wbr>Ttl<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The TTL of cached authorizer results in seconds.
Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorizer<wbr>Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The authorizer&#39;s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `&#34;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Validation<wbr>Expression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn&#39;t match,
the client receives a 401 Unauthorized response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the authorizer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.
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
            <td class="align-top">Authorizer<wbr>Credentials</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorizer<wbr>Result<wbr>Ttl<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The TTL of cached authorizer results in seconds.
Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorizer<wbr>Uri</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The authorizer&#39;s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Source</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `&#34;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Validation<wbr>Expression</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn&#39;t match,
the client receives a 401 Unauthorized response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the authorizer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.
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
            <td class="align-top">authorizer<wbr>Credentials</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorizer<wbr>Result<wbr>Ttl<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The TTL of cached authorizer results in seconds.
Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorizer<wbr>Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The authorizer&#39;s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `&#34;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Validation<wbr>Expression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn&#39;t match,
the client receives a 401 Unauthorized response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the authorizer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.
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
            <td class="align-top">authorizer_<wbr>credentials</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorizer_<wbr>result_<wbr>ttl_<wbr>in_<wbr>seconds</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The TTL of cached authorizer results in seconds.
Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorizer_<wbr>uri</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The authorizer&#39;s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>source</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `&#34;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>validation_<wbr>expression</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn&#39;t match,
the client receives a 401 Unauthorized response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the authorizer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provider_<wbr>arns</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest_<wbr>api</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Authorizer Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#AuthorizerState">AuthorizerState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#Authorizer">Authorizer</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>authorizer_credentials=None<span class="p">, </span>authorizer_result_ttl_in_seconds=None<span class="p">, </span>authorizer_uri=None<span class="p">, </span>identity_source=None<span class="p">, </span>identity_validation_expression=None<span class="p">, </span>name=None<span class="p">, </span>provider_arns=None<span class="p">, </span>rest_api=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAuthorizer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#AuthorizerState">AuthorizerState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#Authorizer">Authorizer</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.Authorizer.html">Authorizer</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.AuthorizerState.html">AuthorizerState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Authorizer resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Authorizer<wbr>Credentials</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorizer<wbr>Result<wbr>Ttl<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of cached authorizer results in seconds.
Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorizer<wbr>Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The authorizer&#39;s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `&#34;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Validation<wbr>Expression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn&#39;t match,
the client receives a 401 Unauthorized response.
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
The name of the authorizer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.
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
            <td class="align-top">Authorizer<wbr>Credentials</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorizer<wbr>Result<wbr>Ttl<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of cached authorizer results in seconds.
Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorizer<wbr>Uri</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The authorizer&#39;s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Source</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `&#34;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Validation<wbr>Expression</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn&#39;t match,
the client receives a 401 Unauthorized response.
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
The name of the authorizer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.
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
            <td class="align-top">authorizer<wbr>Credentials</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorizer<wbr>Result<wbr>Ttl<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of cached authorizer results in seconds.
Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorizer<wbr>Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The authorizer&#39;s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `&#34;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Validation<wbr>Expression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn&#39;t match,
the client receives a 401 Unauthorized response.
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
The name of the authorizer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string | Rest<wbr>Api</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.
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
            <td class="align-top">authorizer_<wbr>credentials</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorizer_<wbr>result_<wbr>ttl_<wbr>in_<wbr>seconds</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of cached authorizer results in seconds.
Defaults to `300`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorizer_<wbr>uri</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The authorizer&#39;s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>source</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `&#34;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>validation_<wbr>expression</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn&#39;t match,
the client receives a 401 Unauthorized response.
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
The name of the authorizer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provider_<wbr>arns</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest_<wbr>api</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









