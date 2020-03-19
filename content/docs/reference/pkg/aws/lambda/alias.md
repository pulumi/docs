
---
title: "Alias"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Creates a Lambda function alias. Creates an alias that points to the specified Lambda function version.

For information about Lambda and how to use it, see [What is AWS Lambda?][1]
For information about function aliases, see [CreateAlias][2] and [AliasRoutingConfiguration][3] in the API docs.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const testAlias = new aws.lambda.Alias("test_alias", {
    description: "a sample description",
    functionName: aws_lambda_function_lambda_function_test.arn,
    functionVersion: "1",
    routingConfig: {
        additionalVersionWeights: {
            "2": 0.5,
        },
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_alias.html.markdown.



## Create a Alias Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#Alias">Alias</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#AliasArgs">AliasArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Alias</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>function_name=None<span class="p">, </span>function_version=None<span class="p">, </span>name=None<span class="p">, </span>routing_config=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAlias<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#AliasArgs">AliasArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#Alias">Alias</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.Alias.html">Alias</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.AliasArgs.html">AliasArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Alias resource with the given unique name, arguments, and options.

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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The function ARN of the Lambda function for which you want to create an alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]&#43;)`.
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
Name for the alias you are creating. Pattern: `(?!^[0-9]&#43;$)([a-zA-Z0-9-_]&#43;)`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#aliasroutingconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Alias<wbr>Routing<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda alias&#39; route configuration settings. Fields documented below
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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The function ARN of the Lambda function for which you want to create an alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]&#43;)`.
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
Name for the alias you are creating. Pattern: `(?!^[0-9]&#43;$)([a-zA-Z0-9-_]&#43;)`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#aliasroutingconfig">*lambda.<wbr>Alias<wbr>Routing<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda alias&#39; route configuration settings. Fields documented below
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
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The function ARN of the Lambda function for which you want to create an alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]&#43;)`.
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
Name for the alias you are creating. Pattern: `(?!^[0-9]&#43;$)([a-zA-Z0-9-_]&#43;)`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#aliasroutingconfig">lambda.<wbr>Alias<wbr>Routing<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda alias&#39; route configuration settings. Fields documented below
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
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The function ARN of the Lambda function for which you want to create an alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]&#43;)`.
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
Name for the alias you are creating. Pattern: `(?!^[0-9]&#43;$)([a-zA-Z0-9-_]&#43;)`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routing_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#aliasroutingconfig">Dict[Alias<wbr>Routing<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda alias&#39; route configuration settings. Fields documented below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Alias Output Properties

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) identifying your Lambda function alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of the alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The function ARN of the Lambda function for which you want to create an alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]&#43;)`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invoke<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)&#39;s `uri`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name for the alias you are creating. Pattern: `(?!^[0-9]&#43;$)([a-zA-Z0-9-_]&#43;)`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#aliasroutingconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Alias<wbr>Routing<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} The Lambda alias&#39; route configuration settings. Fields documented below
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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) identifying your Lambda function alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Description of the alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The function ARN of the Lambda function for which you want to create an alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]&#43;)`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invoke<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)&#39;s `uri`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name for the alias you are creating. Pattern: `(?!^[0-9]&#43;$)([a-zA-Z0-9-_]&#43;)`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#aliasroutingconfig">*lambda.<wbr>Alias<wbr>Routing<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The Lambda alias&#39; route configuration settings. Fields documented below
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) identifying your Lambda function alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of the alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The function ARN of the Lambda function for which you want to create an alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]&#43;)`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invoke<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)&#39;s `uri`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name for the alias you are creating. Pattern: `(?!^[0-9]&#43;$)([a-zA-Z0-9-_]&#43;)`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#aliasroutingconfig">lambda.<wbr>Alias<wbr>Routing<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} The Lambda alias&#39; route configuration settings. Fields documented below
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) identifying your Lambda function alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Description of the alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The function ARN of the Lambda function for which you want to create an alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]&#43;)`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invoke_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)&#39;s `uri`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name for the alias you are creating. Pattern: `(?!^[0-9]&#43;$)([a-zA-Z0-9-_]&#43;)`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routing_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#aliasroutingconfig">Dict[Alias<wbr>Routing<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} The Lambda alias&#39; route configuration settings. Fields documented below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Alias Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#AliasState">AliasState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#Alias">Alias</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>description=None<span class="p">, </span>function_name=None<span class="p">, </span>function_version=None<span class="p">, </span>invoke_arn=None<span class="p">, </span>name=None<span class="p">, </span>routing_config=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAlias<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#AliasState">AliasState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#Alias">Alias</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.Alias.html">Alias</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.AliasState.html">AliasState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Alias resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) identifying your Lambda function alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The function ARN of the Lambda function for which you want to create an alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]&#43;)`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invoke<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)&#39;s `uri`
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
Name for the alias you are creating. Pattern: `(?!^[0-9]&#43;$)([a-zA-Z0-9-_]&#43;)`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#aliasroutingconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Alias<wbr>Routing<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda alias&#39; route configuration settings. Fields documented below
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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) identifying your Lambda function alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The function ARN of the Lambda function for which you want to create an alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]&#43;)`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invoke<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)&#39;s `uri`
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
Name for the alias you are creating. Pattern: `(?!^[0-9]&#43;$)([a-zA-Z0-9-_]&#43;)`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#aliasroutingconfig">*lambda.<wbr>Alias<wbr>Routing<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda alias&#39; route configuration settings. Fields documented below
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) identifying your Lambda function alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The function ARN of the Lambda function for which you want to create an alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]&#43;)`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invoke<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)&#39;s `uri`
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
Name for the alias you are creating. Pattern: `(?!^[0-9]&#43;$)([a-zA-Z0-9-_]&#43;)`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#aliasroutingconfig">lambda.<wbr>Alias<wbr>Routing<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda alias&#39; route configuration settings. Fields documented below
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) identifying your Lambda function alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The function ARN of the Lambda function for which you want to create an alias.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]&#43;)`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invoke_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)&#39;s `uri`
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
Name for the alias you are creating. Pattern: `(?!^[0-9]&#43;$)([a-zA-Z0-9-_]&#43;)`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routing_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#aliasroutingconfig">Dict[Alias<wbr>Routing<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda alias&#39; route configuration settings. Fields documented below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### AliasRoutingConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AliasRoutingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AliasRoutingConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#AliasRoutingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#AliasRoutingConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.AliasRoutingConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.AliasRoutingConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Additional<wbr>Version<wbr>Weights</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, double&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map that defines the proportion of events that should be sent to different versions of a lambda function.
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
            <td class="align-top">Additional<wbr>Version<wbr>Weights</td>
            <td class="align-top">
                
                <code>map[string]float64</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map that defines the proportion of events that should be sent to different versions of a lambda function.
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
            <td class="align-top">additional<wbr>Version<wbr>Weights</td>
            <td class="align-top">
                
                <code>{[key: string]: number}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map that defines the proportion of events that should be sent to different versions of a lambda function.
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
            <td class="align-top">additional<wbr>Version<wbr>Weights</td>
            <td class="align-top">
                
                <code>Dict[str, Number]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map that defines the proportion of events that should be sent to different versions of a lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







