
---
title: "Function"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>




## Create a Function Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#Function">Function</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#FunctionArgs">FunctionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Function</span><span class="p">(resource_name, opts=None, </span>code=None<span class="p">, </span>dead_letter_config=None<span class="p">, </span>description=None<span class="p">, </span>environment=None<span class="p">, </span>handler=None<span class="p">, </span>kms_key_arn=None<span class="p">, </span>layers=None<span class="p">, </span>memory_size=None<span class="p">, </span>name=None<span class="p">, </span>publish=None<span class="p">, </span>reserved_concurrent_executions=None<span class="p">, </span>role=None<span class="p">, </span>runtime=None<span class="p">, </span>s3_bucket=None<span class="p">, </span>s3_key=None<span class="p">, </span>s3_object_version=None<span class="p">, </span>source_code_hash=None<span class="p">, </span>tags=None<span class="p">, </span>timeout=None<span class="p">, </span>tracing_config=None<span class="p">, </span>vpc_config=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewFunction<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionArgs">FunctionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#Function">Function</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.Function.html">Function</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionArgs.html">FunctionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Function resource with the given unique name, arguments, and options.

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
            <td class="align-top">Code</td>
            <td class="align-top">
                
                <code>Archive?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path to the function&#39;s deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dead<wbr>Letter<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiondeadletterconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Dead<wbr>Letter<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block to configure the function&#39;s *dead letter queue*. See details below.
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
Description of what your Lambda Function does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code><a href="#functionenvironment">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Environment<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda environment&#39;s configuration settings. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Handler</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The function [entrypoint][3] in your code.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
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
A unique name for your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publish</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Reserved<wbr>Concurrent<wbr>Executions</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Runtime</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
See [Runtimes][6] for valid values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 bucket location containing the function&#39;s deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 key of an object containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Object<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object version containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Code<wbr>Hash</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256(&#34;file.zip&#34;)` (this provider 0.11.12 and later) or `base64sha256(file(&#34;file.zip&#34;))` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda function source archive.
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
A mapping of tags to assign to the object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tracing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiontracingconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Tracing<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functionvpcconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Vpc<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
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
            <td class="align-top">Code</td>
            <td class="align-top">
                
                <code>pulumi.<wbr>Archive</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path to the function&#39;s deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dead<wbr>Letter<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiondeadletterconfig">*Function<wbr>Dead<wbr>Letter<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block to configure the function&#39;s *dead letter queue*. See details below.
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
Description of what your Lambda Function does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code><a href="#functionenvironment">*Function<wbr>Environment</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda environment&#39;s configuration settings. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Handler</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The function [entrypoint][3] in your code.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
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
A unique name for your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publish</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Reserved<wbr>Concurrent<wbr>Executions</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Runtime</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
See [Runtimes][6] for valid values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 bucket location containing the function&#39;s deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 key of an object containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Object<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object version containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Code<wbr>Hash</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256(&#34;file.zip&#34;)` (this provider 0.11.12 and later) or `base64sha256(file(&#34;file.zip&#34;))` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda function source archive.
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
A mapping of tags to assign to the object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tracing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiontracingconfig">*Function<wbr>Tracing<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functionvpcconfig">*Function<wbr>Vpc<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
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
            <td class="align-top">code</td>
            <td class="align-top">
                
                <code>pulumi.asset.<wbr>Archive?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path to the function&#39;s deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dead<wbr>Letter<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiondeadletterconfig">lambda.<wbr>Function<wbr>Dead<wbr>Letter<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block to configure the function&#39;s *dead letter queue*. See details below.
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
Description of what your Lambda Function does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code><a href="#functionenvironment">lambda.<wbr>Function<wbr>Environment?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda environment&#39;s configuration settings. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">handler</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The function [entrypoint][3] in your code.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
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
A unique name for your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publish</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">reserved<wbr>Concurrent<wbr>Executions</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>ARN</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">runtime</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
See [Runtimes][6] for valid values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 bucket location containing the function&#39;s deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 key of an object containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Object<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object version containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Code<wbr>Hash</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256(&#34;file.zip&#34;)` (this provider 0.11.12 and later) or `base64sha256(file(&#34;file.zip&#34;))` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda function source archive.
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
A mapping of tags to assign to the object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tracing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiontracingconfig">lambda.<wbr>Function<wbr>Tracing<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functionvpcconfig">lambda.<wbr>Function<wbr>Vpc<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
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
            <td class="align-top">code</td>
            <td class="align-top">
                
                <code>pulumi.<wbr>Archive</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path to the function&#39;s deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dead_<wbr>letter_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#functiondeadletterconfig">Dict[Function<wbr>Dead<wbr>Letter<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block to configure the function&#39;s *dead letter queue*. See details below.
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
Description of what your Lambda Function does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code><a href="#functionenvironment">Dict[Function<wbr>Environment]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda environment&#39;s configuration settings. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">handler</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The function [entrypoint][3] in your code.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
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
A unique name for your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publish</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">reserved_<wbr>concurrent_<wbr>executions</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">runtime</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
See [Runtimes][6] for valid values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 bucket location containing the function&#39;s deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 key of an object containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>object_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object version containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>code_<wbr>hash</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256(&#34;file.zip&#34;)` (this provider 0.11.12 and later) or `base64sha256(file(&#34;file.zip&#34;))` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda function source archive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tracing_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#functiontracingconfig">Dict[Function<wbr>Tracing<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#functionvpcconfig">Dict[Function<wbr>Vpc<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Function Output Properties

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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) identifying your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Code</td>
            <td class="align-top">
                
                <code>Archive?</code>
            </td>
            <td class="align-top">{{% md %}} The path to the function&#39;s deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dead<wbr>Letter<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiondeadletterconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Dead<wbr>Letter<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested block to configure the function&#39;s *dead letter queue*. See details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of what your Lambda Function does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code><a href="#functionenvironment">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Environment?</a></code>
            </td>
            <td class="align-top">{{% md %}} The Lambda environment&#39;s configuration settings. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Handler</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The function [entrypoint][3] in your code.
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
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Modified</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date this resource was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publish</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Qualified<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Reserved<wbr>Concurrent<wbr>Executions</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Runtime</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} See [Runtimes][6] for valid values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The S3 bucket location containing the function&#39;s deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The S3 key of an object containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Object<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The object version containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Code<wbr>Hash</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256(&#34;file.zip&#34;)` (this provider 0.11.12 and later) or `base64sha256(file(&#34;file.zip&#34;))` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda function source archive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Code<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The size in bytes of the function .zip file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tracing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiontracingconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Tracing<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Latest published version of your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functionvpcconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Vpc<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) identifying your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Code</td>
            <td class="align-top">
                
                <code>pulumi.<wbr>Archive</code>
            </td>
            <td class="align-top">{{% md %}} The path to the function&#39;s deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dead<wbr>Letter<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiondeadletterconfig">*Function<wbr>Dead<wbr>Letter<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested block to configure the function&#39;s *dead letter queue*. See details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Description of what your Lambda Function does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code><a href="#functionenvironment">*Function<wbr>Environment</a></code>
            </td>
            <td class="align-top">{{% md %}} The Lambda environment&#39;s configuration settings. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Handler</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The function [entrypoint][3] in your code.
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
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Modified</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date this resource was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publish</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Qualified<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Reserved<wbr>Concurrent<wbr>Executions</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Runtime</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} See [Runtimes][6] for valid values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The S3 bucket location containing the function&#39;s deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The S3 key of an object containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Object<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The object version containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Code<wbr>Hash</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256(&#34;file.zip&#34;)` (this provider 0.11.12 and later) or `base64sha256(file(&#34;file.zip&#34;))` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda function source archive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Code<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The size in bytes of the function .zip file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tracing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiontracingconfig">Function<wbr>Tracing<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Latest published version of your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functionvpcconfig">*Function<wbr>Vpc<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) identifying your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">code</td>
            <td class="align-top">
                
                <code>pulumi.asset.<wbr>Archive?</code>
            </td>
            <td class="align-top">{{% md %}} The path to the function&#39;s deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dead<wbr>Letter<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiondeadletterconfig">lambda.<wbr>Function<wbr>Dead<wbr>Letter<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested block to configure the function&#39;s *dead letter queue*. See details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of what your Lambda Function does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code><a href="#functionenvironment">lambda.<wbr>Function<wbr>Environment?</a></code>
            </td>
            <td class="align-top">{{% md %}} The Lambda environment&#39;s configuration settings. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">handler</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The function [entrypoint][3] in your code.
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
            <td class="align-top">kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last<wbr>Modified</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date this resource was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publish</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">qualified<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">reserved<wbr>Concurrent<wbr>Executions</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>ARN</code>
            </td>
            <td class="align-top">{{% md %}} IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">runtime</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} See [Runtimes][6] for valid values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The S3 bucket location containing the function&#39;s deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The S3 key of an object containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Object<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The object version containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Code<wbr>Hash</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256(&#34;file.zip&#34;)` (this provider 0.11.12 and later) or `base64sha256(file(&#34;file.zip&#34;))` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda function source archive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Code<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The size in bytes of the function .zip file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tracing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiontracingconfig">lambda.<wbr>Function<wbr>Tracing<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Latest published version of your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functionvpcconfig">lambda.<wbr>Function<wbr>Vpc<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) identifying your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">code</td>
            <td class="align-top">
                
                <code>pulumi.<wbr>Archive</code>
            </td>
            <td class="align-top">{{% md %}} The path to the function&#39;s deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dead_<wbr>letter_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#functiondeadletterconfig">Dict[Function<wbr>Dead<wbr>Letter<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested block to configure the function&#39;s *dead letter queue*. See details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Description of what your Lambda Function does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code><a href="#functionenvironment">Dict[Function<wbr>Environment]</a></code>
            </td>
            <td class="align-top">{{% md %}} The Lambda environment&#39;s configuration settings. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">handler</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The function [entrypoint][3] in your code.
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
            <td class="align-top">kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last_<wbr>modified</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The date this resource was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publish</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">qualified_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">reserved_<wbr>concurrent_<wbr>executions</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">runtime</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} See [Runtimes][6] for valid values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The S3 bucket location containing the function&#39;s deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The S3 key of an object containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>object_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The object version containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>code_<wbr>hash</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256(&#34;file.zip&#34;)` (this provider 0.11.12 and later) or `base64sha256(file(&#34;file.zip&#34;))` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda function source archive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>code_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The size in bytes of the function .zip file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tracing_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#functiontracingconfig">Dict[Function<wbr>Tracing<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Latest published version of your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#functionvpcconfig">Dict[Function<wbr>Vpc<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Function Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#FunctionState">FunctionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#Function">Function</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>code=None<span class="p">, </span>dead_letter_config=None<span class="p">, </span>description=None<span class="p">, </span>environment=None<span class="p">, </span>handler=None<span class="p">, </span>invoke_arn=None<span class="p">, </span>kms_key_arn=None<span class="p">, </span>last_modified=None<span class="p">, </span>layers=None<span class="p">, </span>memory_size=None<span class="p">, </span>name=None<span class="p">, </span>publish=None<span class="p">, </span>qualified_arn=None<span class="p">, </span>reserved_concurrent_executions=None<span class="p">, </span>role=None<span class="p">, </span>runtime=None<span class="p">, </span>s3_bucket=None<span class="p">, </span>s3_key=None<span class="p">, </span>s3_object_version=None<span class="p">, </span>source_code_hash=None<span class="p">, </span>source_code_size=None<span class="p">, </span>tags=None<span class="p">, </span>timeout=None<span class="p">, </span>tracing_config=None<span class="p">, </span>version=None<span class="p">, </span>vpc_config=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFunction<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionState">FunctionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#Function">Function</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.Function.html">Function</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionState.html">FunctionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Function resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The Amazon Resource Name (ARN) identifying your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Code</td>
            <td class="align-top">
                
                <code>Archive?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path to the function&#39;s deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dead<wbr>Letter<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiondeadletterconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Dead<wbr>Letter<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block to configure the function&#39;s *dead letter queue*. See details below.
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
Description of what your Lambda Function does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code><a href="#functionenvironment">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Environment<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda environment&#39;s configuration settings. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Handler</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The function [entrypoint][3] in your code.
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
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Modified</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date this resource was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
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
A unique name for your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publish</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Qualified<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Reserved<wbr>Concurrent<wbr>Executions</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Runtime</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
See [Runtimes][6] for valid values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 bucket location containing the function&#39;s deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 key of an object containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Object<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object version containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Code<wbr>Hash</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256(&#34;file.zip&#34;)` (this provider 0.11.12 and later) or `base64sha256(file(&#34;file.zip&#34;))` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda function source archive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Code<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size in bytes of the function .zip file.
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
A mapping of tags to assign to the object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tracing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiontracingconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Tracing<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Latest published version of your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functionvpcconfig">Pulumi.<wbr>Aws.<wbr>Lambda.<wbr>Function<wbr>Vpc<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
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
The Amazon Resource Name (ARN) identifying your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Code</td>
            <td class="align-top">
                
                <code>pulumi.<wbr>Archive</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path to the function&#39;s deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dead<wbr>Letter<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiondeadletterconfig">*Function<wbr>Dead<wbr>Letter<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block to configure the function&#39;s *dead letter queue*. See details below.
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
Description of what your Lambda Function does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code><a href="#functionenvironment">*Function<wbr>Environment</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda environment&#39;s configuration settings. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Handler</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The function [entrypoint][3] in your code.
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
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Modified</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date this resource was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
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
A unique name for your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publish</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Qualified<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Reserved<wbr>Concurrent<wbr>Executions</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Runtime</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
See [Runtimes][6] for valid values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 bucket location containing the function&#39;s deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 key of an object containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Object<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object version containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Code<wbr>Hash</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256(&#34;file.zip&#34;)` (this provider 0.11.12 and later) or `base64sha256(file(&#34;file.zip&#34;))` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda function source archive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Code<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size in bytes of the function .zip file.
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
A mapping of tags to assign to the object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tracing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiontracingconfig">*Function<wbr>Tracing<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Latest published version of your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functionvpcconfig">*Function<wbr>Vpc<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
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
The Amazon Resource Name (ARN) identifying your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">code</td>
            <td class="align-top">
                
                <code>pulumi.asset.<wbr>Archive?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path to the function&#39;s deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dead<wbr>Letter<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiondeadletterconfig">lambda.<wbr>Function<wbr>Dead<wbr>Letter<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block to configure the function&#39;s *dead letter queue*. See details below.
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
Description of what your Lambda Function does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code><a href="#functionenvironment">lambda.<wbr>Function<wbr>Environment?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda environment&#39;s configuration settings. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">handler</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The function [entrypoint][3] in your code.
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
            <td class="align-top">kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last<wbr>Modified</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date this resource was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
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
A unique name for your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publish</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">qualified<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">reserved<wbr>Concurrent<wbr>Executions</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>ARN?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">runtime</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
See [Runtimes][6] for valid values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 bucket location containing the function&#39;s deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 key of an object containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Object<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object version containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Code<wbr>Hash</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256(&#34;file.zip&#34;)` (this provider 0.11.12 and later) or `base64sha256(file(&#34;file.zip&#34;))` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda function source archive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Code<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size in bytes of the function .zip file.
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
A mapping of tags to assign to the object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tracing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functiontracingconfig">lambda.<wbr>Function<wbr>Tracing<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Latest published version of your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#functionvpcconfig">lambda.<wbr>Function<wbr>Vpc<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
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
The Amazon Resource Name (ARN) identifying your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">code</td>
            <td class="align-top">
                
                <code>pulumi.<wbr>Archive</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path to the function&#39;s deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dead_<wbr>letter_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#functiondeadletterconfig">Dict[Function<wbr>Dead<wbr>Letter<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested block to configure the function&#39;s *dead letter queue*. See details below.
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
Description of what your Lambda Function does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code><a href="#functionenvironment">Dict[Function<wbr>Environment]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Lambda environment&#39;s configuration settings. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">handler</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The function [entrypoint][3] in your code.
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
            <td class="align-top">kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last_<wbr>modified</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date this resource was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
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
A unique name for your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publish</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">qualified_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">reserved_<wbr>concurrent_<wbr>executions</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">runtime</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
See [Runtimes][6] for valid values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 bucket location containing the function&#39;s deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 key of an object containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>object_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object version containing the function&#39;s deployment package. Conflicts with `filename`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>code_<wbr>hash</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256(&#34;file.zip&#34;)` (this provider 0.11.12 and later) or `base64sha256(file(&#34;file.zip&#34;))` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda function source archive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>code_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size in bytes of the function .zip file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tracing_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#functiontracingconfig">Dict[Function<wbr>Tracing<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Latest published version of your Lambda Function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#functionvpcconfig">Dict[Function<wbr>Vpc<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### FunctionDeadLetterConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FunctionDeadLetterConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FunctionDeadLetterConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionDeadLetterConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionDeadLetterConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionDeadLetterConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionDeadLetterConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Target<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of an SNS topic or SQS queue to notify when an invocation fails. If this
option is used, the function&#39;s IAM role must be granted suitable access to write to the target object,
which means allowing either the `sns:Publish` or `sqs:SendMessage` action on this ARN, depending on
which service is targeted.
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
            <td class="align-top">Target<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of an SNS topic or SQS queue to notify when an invocation fails. If this
option is used, the function&#39;s IAM role must be granted suitable access to write to the target object,
which means allowing either the `sns:Publish` or `sqs:SendMessage` action on this ARN, depending on
which service is targeted.
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
            <td class="align-top">target<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of an SNS topic or SQS queue to notify when an invocation fails. If this
option is used, the function&#39;s IAM role must be granted suitable access to write to the target object,
which means allowing either the `sns:Publish` or `sqs:SendMessage` action on this ARN, depending on
which service is targeted.
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
            <td class="align-top">target_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of an SNS topic or SQS queue to notify when an invocation fails. If this
option is used, the function&#39;s IAM role must be granted suitable access to write to the target object,
which means allowing either the `sns:Publish` or `sqs:SendMessage` action on this ARN, depending on
which service is targeted.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FunctionEnvironment
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FunctionEnvironment">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FunctionEnvironment">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEnvironmentArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEnvironmentOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionEnvironmentArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionEnvironment.html">output</a> API doc for this type.
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
            <td class="align-top">Variables</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map that defines environment variables for the Lambda function.
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
            <td class="align-top">Variables</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map that defines environment variables for the Lambda function.
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
            <td class="align-top">variables</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map that defines environment variables for the Lambda function.
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
            <td class="align-top">variables</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map that defines environment variables for the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FunctionTracingConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FunctionTracingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FunctionTracingConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionTracingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionTracingConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionTracingConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionTracingConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Can be either `PassThrough` or `Active`. If PassThrough, Lambda will only trace
the request from an upstream service if it contains a tracing header with
&#34;sampled=1&#34;. If Active, Lambda will respect any tracing header it receives
from an upstream service. If no tracing header is received, Lambda will call
X-Ray for a tracing decision.
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
            <td class="align-top">Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Can be either `PassThrough` or `Active`. If PassThrough, Lambda will only trace
the request from an upstream service if it contains a tracing header with
&#34;sampled=1&#34;. If Active, Lambda will respect any tracing header it receives
from an upstream service. If no tracing header is received, Lambda will call
X-Ray for a tracing decision.
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
            <td class="align-top">mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Can be either `PassThrough` or `Active`. If PassThrough, Lambda will only trace
the request from an upstream service if it contains a tracing header with
&#34;sampled=1&#34;. If Active, Lambda will respect any tracing header it receives
from an upstream service. If no tracing header is received, Lambda will call
X-Ray for a tracing decision.
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
            <td class="align-top">mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Can be either `PassThrough` or `Active`. If PassThrough, Lambda will only trace
the request from an upstream service if it contains a tracing header with
&#34;sampled=1&#34;. If Active, Lambda will respect any tracing header it receives
from an upstream service. If no tracing header is received, Lambda will call
X-Ray for a tracing decision.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FunctionVpcConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FunctionVpcConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FunctionVpcConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionVpcConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionVpcConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionVpcConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionVpcConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of security group IDs associated with the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of subnet IDs associated with the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of security group IDs associated with the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of subnet IDs associated with the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of security group IDs associated with the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of subnet IDs associated with the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of security group IDs associated with the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of subnet IDs associated with the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







