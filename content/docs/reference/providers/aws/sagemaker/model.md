
---
title: "Model"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a SageMaker model resource.

## Example Usage

Basic usage:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const assumeRole = aws.iam.getPolicyDocument({
    statements: [{
        actions: ["sts:AssumeRole"],
        principals: [{
            identifiers: ["sagemaker.amazonaws.com"],
            type: "Service",
        }],
    }],
});
const role = new aws.iam.Role("r", {
    assumeRolePolicy: assumeRole.json,
});
const model = new aws.sagemaker.Model("m", {
    executionRoleArn: aws_iam_role_foo.arn,
    primaryContainer: {
        image: "174872318107.dkr.ecr.us-west-2.amazonaws.com/kmeans:1",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_model.html.markdown.



## Create a Model Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/sagemaker/#Model">Model</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/sagemaker/#ModelArgs">ModelArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Model</span><span class="p">(resource_name, id, opts=None, </span>containers=None<span class="p">, </span>enable_network_isolation=None<span class="p">, </span>execution_role_arn=None<span class="p">, </span>name=None<span class="p">, </span>primary_container=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_config=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewModel<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelArgs">ModelArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#Model">Model</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sagemaker.Model.html">Model</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sagemaker.ModelArgs.html">ModelArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Model resource with the given unique name, arguments, and options.

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
            <td class="align-top">Containers</td>
            <td class="align-top">
                
                <code><a href="#modelcontainer">List&lt;Pulumi.<wbr>Aws.<wbr>Sagemaker.<wbr>Model<wbr>Container<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Network<wbr>Isolation</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A role that SageMaker can assume to access model artifacts and docker images for deployment.
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
The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Primary<wbr>Container</td>
            <td class="align-top">
                
                <code><a href="#modelprimarycontainer">Pulumi.<wbr>Aws.<wbr>Sagemaker.<wbr>Model<wbr>Primary<wbr>Container<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
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
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#modelvpcconfig">Pulumi.<wbr>Aws.<wbr>Sagemaker.<wbr>Model<wbr>Vpc<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
            <td class="align-top">Containers</td>
            <td class="align-top">
                
                <code><a href="#modelcontainer">[]sagemaker.<wbr>Model<wbr>Container</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Network<wbr>Isolation</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A role that SageMaker can assume to access model artifacts and docker images for deployment.
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
The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Primary<wbr>Container</td>
            <td class="align-top">
                
                <code><a href="#modelprimarycontainer">*sagemaker.<wbr>Model<wbr>Primary<wbr>Container</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
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
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#modelvpcconfig">*sagemaker.<wbr>Model<wbr>Vpc<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
            <td class="align-top">containers</td>
            <td class="align-top">
                
                <code><a href="#modelcontainer">sagemaker.<wbr>Model<wbr>Container[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Network<wbr>Isolation</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A role that SageMaker can assume to access model artifacts and docker images for deployment.
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
The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">primary<wbr>Container</td>
            <td class="align-top">
                
                <code><a href="#modelprimarycontainer">sagemaker.<wbr>Model<wbr>Primary<wbr>Container?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
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
            <td class="align-top">vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#modelvpcconfig">sagemaker.<wbr>Model<wbr>Vpc<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
            <td class="align-top">containers</td>
            <td class="align-top">
                
                <code><a href="#modelcontainer">list[model_<wbr>container]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>network_<wbr>isolation</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">execution_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A role that SageMaker can assume to access model artifacts and docker images for deployment.
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
The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">primary_<wbr>container</td>
            <td class="align-top">
                
                <code><a href="#modelprimarycontainer">dict{model_<wbr>primary_<wbr>container}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#modelvpcconfig">dict{model_<wbr>vpc_<wbr>config}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Model Output Properties

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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) assigned by AWS to this model.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Containers</td>
            <td class="align-top">
                
                <code><a href="#modelcontainer">List&lt;Pulumi.<wbr>Aws.<wbr>Sagemaker.<wbr>Model<wbr>Container&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Network<wbr>Isolation</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A role that SageMaker can assume to access model artifacts and docker images for deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Primary<wbr>Container</td>
            <td class="align-top">
                
                <code><a href="#modelprimarycontainer">Pulumi.<wbr>Aws.<wbr>Sagemaker.<wbr>Model<wbr>Primary<wbr>Container?</a></code>
            </td>
            <td class="align-top">{{% md %}} The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
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
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#modelvpcconfig">Pulumi.<wbr>Aws.<wbr>Sagemaker.<wbr>Model<wbr>Vpc<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) assigned by AWS to this model.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Containers</td>
            <td class="align-top">
                
                <code><a href="#modelcontainer">[]sagemaker.<wbr>Model<wbr>Container</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Network<wbr>Isolation</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A role that SageMaker can assume to access model artifacts and docker images for deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Primary<wbr>Container</td>
            <td class="align-top">
                
                <code><a href="#modelprimarycontainer">*sagemaker.<wbr>Model<wbr>Primary<wbr>Container</a></code>
            </td>
            <td class="align-top">{{% md %}} The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
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
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#modelvpcconfig">*sagemaker.<wbr>Model<wbr>Vpc<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) assigned by AWS to this model.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">containers</td>
            <td class="align-top">
                
                <code><a href="#modelcontainer">sagemaker.<wbr>Model<wbr>Container[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Network<wbr>Isolation</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A role that SageMaker can assume to access model artifacts and docker images for deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">primary<wbr>Container</td>
            <td class="align-top">
                
                <code><a href="#modelprimarycontainer">sagemaker.<wbr>Model<wbr>Primary<wbr>Container?</a></code>
            </td>
            <td class="align-top">{{% md %}} The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
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
            <td class="align-top">vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#modelvpcconfig">sagemaker.<wbr>Model<wbr>Vpc<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) assigned by AWS to this model.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">containers</td>
            <td class="align-top">
                
                <code><a href="#modelcontainer">list[model_<wbr>container]</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>network_<wbr>isolation</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">execution_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A role that SageMaker can assume to access model artifacts and docker images for deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">primary_<wbr>container</td>
            <td class="align-top">
                
                <code><a href="#modelprimarycontainer">dict{model_<wbr>primary_<wbr>container}</a></code>
            </td>
            <td class="align-top">{{% md %}} The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#modelvpcconfig">dict{model_<wbr>vpc_<wbr>config}</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Model Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ModelState, opts?: pulumi.CustomResourceOptions): Model;
```

```python
def get(resource_name, id, opts=None, arn=None, containers=None, enable_<wbr>network_<wbr>isolation=None, execution_<wbr>role_<wbr>arn=None, name=None, primary_<wbr>container=None, tags=None, vpc_<wbr>config=None)
```

```go
func GetModel(ctx *pulumi.Context, name string, id pulumi.IDInput, state *ModelState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static Model Get(string name, Input<string> id, ModelState? state = null, CustomResourceOptions? options = null);
```

Get an existing Model resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The Amazon Resource Name (ARN) assigned by AWS to this model.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Containers</td>
            <td class="align-top">
                
                <code><a href="#modelcontainer">List&lt;Pulumi.<wbr>Aws.<wbr>Sagemaker.<wbr>Model<wbr>Container<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Network<wbr>Isolation</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A role that SageMaker can assume to access model artifacts and docker images for deployment.
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
The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Primary<wbr>Container</td>
            <td class="align-top">
                
                <code><a href="#modelprimarycontainer">Pulumi.<wbr>Aws.<wbr>Sagemaker.<wbr>Model<wbr>Primary<wbr>Container<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
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
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#modelvpcconfig">Pulumi.<wbr>Aws.<wbr>Sagemaker.<wbr>Model<wbr>Vpc<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
The Amazon Resource Name (ARN) assigned by AWS to this model.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Containers</td>
            <td class="align-top">
                
                <code><a href="#modelcontainer">[]sagemaker.<wbr>Model<wbr>Container</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Network<wbr>Isolation</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A role that SageMaker can assume to access model artifacts and docker images for deployment.
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
The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Primary<wbr>Container</td>
            <td class="align-top">
                
                <code><a href="#modelprimarycontainer">*sagemaker.<wbr>Model<wbr>Primary<wbr>Container</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
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
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#modelvpcconfig">*sagemaker.<wbr>Model<wbr>Vpc<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
The Amazon Resource Name (ARN) assigned by AWS to this model.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">containers</td>
            <td class="align-top">
                
                <code><a href="#modelcontainer">sagemaker.<wbr>Model<wbr>Container[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Network<wbr>Isolation</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A role that SageMaker can assume to access model artifacts and docker images for deployment.
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
The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">primary<wbr>Container</td>
            <td class="align-top">
                
                <code><a href="#modelprimarycontainer">sagemaker.<wbr>Model<wbr>Primary<wbr>Container?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
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
            <td class="align-top">vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#modelvpcconfig">sagemaker.<wbr>Model<wbr>Vpc<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
The Amazon Resource Name (ARN) assigned by AWS to this model.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">containers</td>
            <td class="align-top">
                
                <code><a href="#modelcontainer">list[model_<wbr>container]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>network_<wbr>isolation</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">execution_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A role that SageMaker can assume to access model artifacts and docker images for deployment.
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
The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">primary_<wbr>container</td>
            <td class="align-top">
                
                <code><a href="#modelprimarycontainer">dict{model_<wbr>primary_<wbr>container}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#modelvpcconfig">dict{model_<wbr>vpc_<wbr>config}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ModelContainer
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ModelContainer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ModelContainer">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelContainerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelContainerOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sagemaker.ModelContainerArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sagemaker.ModelContainer.html">output</a> API doc for this type.
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
            <td class="align-top">Container<wbr>Hostname</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Model<wbr>Data<wbr>Url</td>
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
            <td class="align-top">Container<wbr>Hostname</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Model<wbr>Data<wbr>Url</td>
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
            <td class="align-top">container<wbr>Hostname</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">model<wbr>Data<wbr>Url</td>
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
            <td class="align-top">container_<wbr>hostname</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">model_<wbr>data_<wbr>url</td>
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





#### ModelPrimaryContainer
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ModelPrimaryContainer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ModelPrimaryContainer">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelPrimaryContainerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelPrimaryContainerOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sagemaker.ModelPrimaryContainerArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sagemaker.ModelPrimaryContainer.html">output</a> API doc for this type.
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
            <td class="align-top">Container<wbr>Hostname</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Model<wbr>Data<wbr>Url</td>
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
            <td class="align-top">Container<wbr>Hostname</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Model<wbr>Data<wbr>Url</td>
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
            <td class="align-top">container<wbr>Hostname</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">model<wbr>Data<wbr>Url</td>
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
            <td class="align-top">container_<wbr>hostname</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">model_<wbr>data_<wbr>url</td>
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





#### ModelVpcConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ModelVpcConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ModelVpcConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelVpcConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelVpcConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sagemaker.ModelVpcConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sagemaker.ModelVpcConfig.html">output</a> API doc for this type.
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
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnets</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnets</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnets</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnets</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







