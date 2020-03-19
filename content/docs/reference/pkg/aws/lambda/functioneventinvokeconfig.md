
---
title: "FunctionEventInvokeConfig"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Manages an asynchronous invocation configuration for a Lambda Function or Alias. More information about asynchronous invocations and the configurable values can be found in the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html).

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_function_event_invoke_config.html.markdown.



## Create a FunctionEventInvokeConfig Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#FunctionEventInvokeConfig">FunctionEventInvokeConfig</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#FunctionEventInvokeConfigArgs">FunctionEventInvokeConfigArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">FunctionEventInvokeConfig</span><span class="p">(resource_name, opts=None, </span>destination_config=None<span class="p">, </span>function_name=None<span class="p">, </span>maximum_event_age_in_seconds=None<span class="p">, </span>maximum_retry_attempts=None<span class="p">, </span>qualifier=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewFunctionEventInvokeConfig<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEventInvokeConfigArgs">FunctionEventInvokeConfigArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEventInvokeConfig">FunctionEventInvokeConfig</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionEventInvokeConfig.html">FunctionEventInvokeConfig</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionEventInvokeConfigArgs.html">FunctionEventInvokeConfigArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a FunctionEventInvokeConfig resource with the given unique name, arguments, and options.

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
            <td class="align-top">Destination<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration. See below for details.
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
Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Event<wbr>Age<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Retry<wbr>Attempts</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Qualifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda Function published version, `$LATEST`, or Lambda Alias name.
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
            <td class="align-top">Destination<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfig">*lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration. See below for details.
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
Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Event<wbr>Age<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Retry<wbr>Attempts</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Qualifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda Function published version, `$LATEST`, or Lambda Alias name.
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
            <td class="align-top">destination<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfig">lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration. See below for details.
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
Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum<wbr>Event<wbr>Age<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum<wbr>Retry<wbr>Attempts</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">qualifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda Function published version, `$LATEST`, or Lambda Alias name.
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
            <td class="align-top">destination_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfig">Dict[Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration. See below for details.
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
Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum_<wbr>event_<wbr>age_<wbr>in_<wbr>seconds</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum_<wbr>retry_<wbr>attempts</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">qualifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda Function published version, `$LATEST`, or Lambda Alias name.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## FunctionEventInvokeConfig Output Properties

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
            <td class="align-top">Destination<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with destination configuration. See below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Event<wbr>Age<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Retry<wbr>Attempts</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Qualifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Lambda Function published version, `$LATEST`, or Lambda Alias name.
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
            <td class="align-top">Destination<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfig">*lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with destination configuration. See below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Function<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Event<wbr>Age<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Retry<wbr>Attempts</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Qualifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Lambda Function published version, `$LATEST`, or Lambda Alias name.
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
            <td class="align-top">destination<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfig">lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with destination configuration. See below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum<wbr>Event<wbr>Age<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum<wbr>Retry<wbr>Attempts</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">qualifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Lambda Function published version, `$LATEST`, or Lambda Alias name.
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
            <td class="align-top">destination_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfig">Dict[Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with destination configuration. See below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">function_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum_<wbr>event_<wbr>age_<wbr>in_<wbr>seconds</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum_<wbr>retry_<wbr>attempts</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">qualifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Lambda Function published version, `$LATEST`, or Lambda Alias name.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing FunctionEventInvokeConfig Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#FunctionEventInvokeConfigState">FunctionEventInvokeConfigState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#FunctionEventInvokeConfig">FunctionEventInvokeConfig</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>destination_config=None<span class="p">, </span>function_name=None<span class="p">, </span>maximum_event_age_in_seconds=None<span class="p">, </span>maximum_retry_attempts=None<span class="p">, </span>qualifier=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFunctionEventInvokeConfig<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEventInvokeConfigState">FunctionEventInvokeConfigState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEventInvokeConfig">FunctionEventInvokeConfig</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionEventInvokeConfig.html">FunctionEventInvokeConfig</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionEventInvokeConfigState.html">FunctionEventInvokeConfigState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing FunctionEventInvokeConfig resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Destination<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration. See below for details.
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
Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Event<wbr>Age<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Retry<wbr>Attempts</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Qualifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda Function published version, `$LATEST`, or Lambda Alias name.
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
            <td class="align-top">Destination<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfig">*lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration. See below for details.
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
Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Event<wbr>Age<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Retry<wbr>Attempts</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Qualifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda Function published version, `$LATEST`, or Lambda Alias name.
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
            <td class="align-top">destination<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfig">lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration. See below for details.
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
Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum<wbr>Event<wbr>Age<wbr>In<wbr>Seconds</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum<wbr>Retry<wbr>Attempts</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">qualifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda Function published version, `$LATEST`, or Lambda Alias name.
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
            <td class="align-top">destination_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfig">Dict[Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration. See below for details.
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
Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum_<wbr>event_<wbr>age_<wbr>in_<wbr>seconds</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum_<wbr>retry_<wbr>attempts</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">qualifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda Function published version, `$LATEST`, or Lambda Alias name.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### FunctionEventInvokeConfigDestinationConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FunctionEventInvokeConfigDestinationConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FunctionEventInvokeConfigDestinationConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEventInvokeConfigDestinationConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEventInvokeConfigDestinationConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionEventInvokeConfigDestinationConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionEventInvokeConfigDestinationConfig.html">output</a> API doc for this type.
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
            <td class="align-top">On<wbr>Failure</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfigonfailure">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config<wbr>On<wbr>Failure<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration for failed asynchronous invocations. See below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Success</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfigonsuccess">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config<wbr>On<wbr>Success<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration for successful asynchronous invocations. See below for details.
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
            <td class="align-top">On<wbr>Failure</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfigonfailure">*lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config<wbr>On<wbr>Failure</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration for failed asynchronous invocations. See below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Success</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfigonsuccess">*lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config<wbr>On<wbr>Success</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration for successful asynchronous invocations. See below for details.
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
            <td class="align-top">on<wbr>Failure</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfigonfailure">lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config<wbr>On<wbr>Failure?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration for failed asynchronous invocations. See below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on<wbr>Success</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfigonsuccess">lambda.<wbr>Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config<wbr>On<wbr>Success?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration for successful asynchronous invocations. See below for details.
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
            <td class="align-top">on_<wbr>failure</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfigonfailure">Dict[Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config<wbr>On<wbr>Failure]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration for failed asynchronous invocations. See below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on<wbr>Success</td>
            <td class="align-top">
                
                <code><a href="#functioneventinvokeconfigdestinationconfigonsuccess">Dict[Function<wbr>Event<wbr>Invoke<wbr>Config<wbr>Destination<wbr>Config<wbr>On<wbr>Success]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with destination configuration for successful asynchronous invocations. See below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FunctionEventInvokeConfigDestinationConfigOnFailure
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FunctionEventInvokeConfigDestinationConfigOnFailure">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FunctionEventInvokeConfigDestinationConfigOnFailure">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEventInvokeConfigDestinationConfigOnFailureArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEventInvokeConfigDestinationConfigOnFailureOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionEventInvokeConfigDestinationConfigOnFailureArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionEventInvokeConfigDestinationConfigOnFailure.html">output</a> API doc for this type.
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
            <td class="align-top">Destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
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
            <td class="align-top">Destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
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
            <td class="align-top">destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
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
            <td class="align-top">destination</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FunctionEventInvokeConfigDestinationConfigOnSuccess
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FunctionEventInvokeConfigDestinationConfigOnSuccess">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FunctionEventInvokeConfigDestinationConfigOnSuccess">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEventInvokeConfigDestinationConfigOnSuccessArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEventInvokeConfigDestinationConfigOnSuccessOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionEventInvokeConfigDestinationConfigOnSuccessArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionEventInvokeConfigDestinationConfigOnSuccess.html">output</a> API doc for this type.
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
            <td class="align-top">Destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
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
            <td class="align-top">Destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
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
            <td class="align-top">destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
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
            <td class="align-top">destination</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







