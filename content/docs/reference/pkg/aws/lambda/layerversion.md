
---
title: "LayerVersion"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a Lambda Layer Version resource. Lambda Layers allow you to reuse shared bits of code across multiple lambda functions.

For information about Lambda Layers and how to use them, see [AWS Lambda Layers][1]

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const lambdaLayer = new aws.lambda.LayerVersion("lambda_layer", {
    compatibleRuntimes: ["nodejs8.10"],
    code: new pulumi.asset.FileArchive("lambda_layer_payload.zip"),
    layerName: "lambda_layer_name",
});
```

## Specifying the Deployment Package

AWS Lambda Layers expect source code to be provided as a deployment package whose structure varies depending on which `compatible_runtimes` this layer specifies.
See [Runtimes][2] for the valid values of `compatible_runtimes`.

Once you have created your deployment package you can specify it either directly as a local file (using the `filename` argument) or
indirectly via Amazon S3 (using the `s3_bucket`, `s3_key` and `s3_object_version` arguments). When providing the deployment
package via S3 it may be useful to use the `aws.s3.BucketObject` resource to upload it.

For larger deployment packages it is recommended by Amazon to upload via S3, since the S3 API has better support for uploading
large files efficiently.

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_layer_version.html.markdown.



## Create a LayerVersion Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#LayerVersion">LayerVersion</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#LayerVersionArgs">LayerVersionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">LayerVersion</span><span class="p">(resource_name, id, opts=None, </span>code=None<span class="p">, </span>compatible_runtimes=None<span class="p">, </span>description=None<span class="p">, </span>layer_name=None<span class="p">, </span>license_info=None<span class="p">, </span>s3_bucket=None<span class="p">, </span>s3_key=None<span class="p">, </span>s3_object_version=None<span class="p">, </span>source_code_hash=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewLayerVersion<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#LayerVersionArgs">LayerVersionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#LayerVersion">LayerVersion</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.LayerVersion.html">LayerVersion</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.LayerVersionArgs.html">LayerVersionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a LayerVersion resource with the given unique name, arguments, and options.

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
            <td class="align-top">Compatible<wbr>Runtimes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
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
Description of what your Lambda Layer does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layer<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for your Lambda Layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Info</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
License info for your Lambda Layer. See [License Info][3].
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
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256(&#34;file.zip&#34;)}` (this provider 0.11.12 or later) or `${base64sha256(file(&#34;file.zip&#34;))}` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda layer source archive.
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
            <td class="align-top">Compatible<wbr>Runtimes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
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
Description of what your Lambda Layer does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layer<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for your Lambda Layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Info</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
License info for your Lambda Layer. See [License Info][3].
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
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256(&#34;file.zip&#34;)}` (this provider 0.11.12 or later) or `${base64sha256(file(&#34;file.zip&#34;))}` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda layer source archive.
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
            <td class="align-top">compatible<wbr>Runtimes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
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
Description of what your Lambda Layer does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layer<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for your Lambda Layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license<wbr>Info</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
License info for your Lambda Layer. See [License Info][3].
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
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256(&#34;file.zip&#34;)}` (this provider 0.11.12 or later) or `${base64sha256(file(&#34;file.zip&#34;))}` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda layer source archive.
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
            <td class="align-top">compatible_<wbr>runtimes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
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
Description of what your Lambda Layer does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layer_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for your Lambda Layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license_<wbr>info</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
License info for your Lambda Layer. See [License Info][3].
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
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256(&#34;file.zip&#34;)}` (this provider 0.11.12 or later) or `${base64sha256(file(&#34;file.zip&#34;))}` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda layer source archive.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## LayerVersion Output Properties

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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the Lambda Layer with version.
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
            <td class="align-top">Compatible<wbr>Runtimes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Created<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date this resource was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of what your Lambda Layer does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layer<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the Lambda Layer without version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layer<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for your Lambda Layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Info</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} License info for your Lambda Layer. See [License Info][3].
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
            <td class="align-top">{{% md %}} Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256(&#34;file.zip&#34;)}` (this provider 0.11.12 or later) or `${base64sha256(file(&#34;file.zip&#34;))}` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda layer source archive.
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
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} This Lamba Layer version.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the Lambda Layer with version.
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
            <td class="align-top">Compatible<wbr>Runtimes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Created<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date this resource was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Description of what your Lambda Layer does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layer<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the Lambda Layer without version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layer<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for your Lambda Layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Info</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} License info for your Lambda Layer. See [License Info][3].
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
            <td class="align-top">{{% md %}} Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256(&#34;file.zip&#34;)}` (this provider 0.11.12 or later) or `${base64sha256(file(&#34;file.zip&#34;))}` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda layer source archive.
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
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} This Lamba Layer version.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the Lambda Layer with version.
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
            <td class="align-top">compatible<wbr>Runtimes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">created<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date this resource was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of what your Lambda Layer does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layer<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the Lambda Layer without version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layer<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for your Lambda Layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license<wbr>Info</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} License info for your Lambda Layer. See [License Info][3].
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
            <td class="align-top">{{% md %}} Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256(&#34;file.zip&#34;)}` (this provider 0.11.12 or later) or `${base64sha256(file(&#34;file.zip&#34;))}` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda layer source archive.
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
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} This Lamba Layer version.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the Lambda Layer with version.
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
            <td class="align-top">compatible_<wbr>runtimes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">created_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The date this resource was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Description of what your Lambda Layer does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layer_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the Lambda Layer without version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layer_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for your Lambda Layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license_<wbr>info</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} License info for your Lambda Layer. See [License Info][3].
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
            <td class="align-top">{{% md %}} Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256(&#34;file.zip&#34;)}` (this provider 0.11.12 or later) or `${base64sha256(file(&#34;file.zip&#34;))}` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda layer source archive.
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
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} This Lamba Layer version.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing LayerVersion Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LayerVersionState, opts?: pulumi.CustomResourceOptions): LayerVersion;
```

```python
def get(resource_name, id, opts=None, arn=None, code=None, compatible_<wbr>runtimes=None, created_<wbr>date=None, description=None, layer_<wbr>arn=None, layer_<wbr>name=None, license_<wbr>info=None, s3_<wbr>bucket=None, s3_<wbr>key=None, s3_<wbr>object_<wbr>version=None, source_<wbr>code_<wbr>hash=None, source_<wbr>code_<wbr>size=None, version=None)
```

```go
func GetLayerVersion(ctx *pulumi.Context, name string, id pulumi.IDInput, state *LayerVersionState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static LayerVersion Get(string name, Input<string> id, LayerVersionState? state = null, CustomResourceOptions? options = null);
```

Get an existing LayerVersion resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The Amazon Resource Name (ARN) of the Lambda Layer with version.
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
            <td class="align-top">Compatible<wbr>Runtimes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Created<wbr>Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date this resource was created.
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
Description of what your Lambda Layer does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layer<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the Lambda Layer without version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layer<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for your Lambda Layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Info</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
License info for your Lambda Layer. See [License Info][3].
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
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256(&#34;file.zip&#34;)}` (this provider 0.11.12 or later) or `${base64sha256(file(&#34;file.zip&#34;))}` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda layer source archive.
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
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This Lamba Layer version.
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
The Amazon Resource Name (ARN) of the Lambda Layer with version.
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
            <td class="align-top">Compatible<wbr>Runtimes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Created<wbr>Date</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date this resource was created.
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
Description of what your Lambda Layer does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layer<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the Lambda Layer without version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Layer<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for your Lambda Layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Info</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
License info for your Lambda Layer. See [License Info][3].
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
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256(&#34;file.zip&#34;)}` (this provider 0.11.12 or later) or `${base64sha256(file(&#34;file.zip&#34;))}` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda layer source archive.
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
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This Lamba Layer version.
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
The Amazon Resource Name (ARN) of the Lambda Layer with version.
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
            <td class="align-top">compatible<wbr>Runtimes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">created<wbr>Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date this resource was created.
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
Description of what your Lambda Layer does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layer<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the Lambda Layer without version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layer<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for your Lambda Layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license<wbr>Info</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
License info for your Lambda Layer. See [License Info][3].
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
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256(&#34;file.zip&#34;)}` (this provider 0.11.12 or later) or `${base64sha256(file(&#34;file.zip&#34;))}` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda layer source archive.
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
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This Lamba Layer version.
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
The Amazon Resource Name (ARN) of the Lambda Layer with version.
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
            <td class="align-top">compatible_<wbr>runtimes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">created_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date this resource was created.
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
Description of what your Lambda Layer does.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layer_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the Lambda Layer without version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">layer_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for your Lambda Layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license_<wbr>info</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
License info for your Lambda Layer. See [License Info][3].
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
Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256(&#34;file.zip&#34;)}` (this provider 0.11.12 or later) or `${base64sha256(file(&#34;file.zip&#34;))}` (this provider 0.11.11 and earlier), where &#34;file.zip&#34; is the local filename of the lambda layer source archive.
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
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This Lamba Layer version.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









