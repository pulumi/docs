
---
title: "Workgroup"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an Athena Workgroup.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.athena.Workgroup("example", {
    configuration: {
        enforceWorkgroupConfiguration: true,
        publishCloudwatchMetricsEnabled: true,
        resultConfiguration: {
            encryptionConfiguration: {
                encryptionOption: "SSE_KMS",
                kmsKeyArn: aws_kms_key_example.arn,
            },
            outputLocation: "s3://{aws_s3_bucket.example.bucket}/output/",
        },
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_workgroup.html.markdown.



## Create a Workgroup Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/athena/#Workgroup">Workgroup</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/athena/#WorkgroupArgs">WorkgroupArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Workgroup</span><span class="p">(resource_name, opts=None, </span>configuration=None<span class="p">, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>state=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewWorkgroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/athena?tab=doc#WorkgroupArgs">WorkgroupArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/athena?tab=doc#Workgroup">Workgroup</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Athena.Workgroup.html">Workgroup</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Athena.WorkgroupArgs.html">WorkgroupArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Workgroup resource with the given unique name, arguments, and options.

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
            <td class="align-top">Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfiguration">Pulumi.<wbr>Aws.<wbr>Athena.<wbr>Workgroup<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with various settings for the workgroup. Documented below.
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
Description of the workgroup.
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
Name of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
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
Key-value mapping of resource tags for the workgroup.
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
            <td class="align-top">Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfiguration">*Workgroup<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with various settings for the workgroup. Documented below.
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
Description of the workgroup.
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
Name of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
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
Key-value mapping of resource tags for the workgroup.
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
            <td class="align-top">configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfiguration">athena.<wbr>Workgroup<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with various settings for the workgroup. Documented below.
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
Description of the workgroup.
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
Name of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
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
Key-value mapping of resource tags for the workgroup.
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
            <td class="align-top">configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfiguration">Dict[Workgroup<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with various settings for the workgroup. Documented below.
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
Description of the workgroup.
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
Name of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
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
Key-value mapping of resource tags for the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Workgroup Output Properties

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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the workgroup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfiguration">Pulumi.<wbr>Aws.<wbr>Athena.<wbr>Workgroup<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with various settings for the workgroup. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags for the workgroup.
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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the workgroup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfiguration">*Workgroup<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with various settings for the workgroup. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Description of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags for the workgroup.
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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the workgroup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfiguration">athena.<wbr>Workgroup<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with various settings for the workgroup. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags for the workgroup.
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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the workgroup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfiguration">Dict[Workgroup<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with various settings for the workgroup. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Description of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags for the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Workgroup Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/athena/#WorkgroupState">WorkgroupState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/athena/#Workgroup">Workgroup</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>configuration=None<span class="p">, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>state=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetWorkgroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/athena?tab=doc#WorkgroupState">WorkgroupState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/athena?tab=doc#Workgroup">Workgroup</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Athena.Workgroup.html">Workgroup</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Athena.WorkgroupState.html">WorkgroupState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Workgroup resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
Amazon Resource Name (ARN) of the workgroup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfiguration">Pulumi.<wbr>Aws.<wbr>Athena.<wbr>Workgroup<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with various settings for the workgroup. Documented below.
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
Description of the workgroup.
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
Name of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
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
Key-value mapping of resource tags for the workgroup.
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
Amazon Resource Name (ARN) of the workgroup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfiguration">*Workgroup<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with various settings for the workgroup. Documented below.
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
Description of the workgroup.
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
Name of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
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
Key-value mapping of resource tags for the workgroup.
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
Amazon Resource Name (ARN) of the workgroup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfiguration">athena.<wbr>Workgroup<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with various settings for the workgroup. Documented below.
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
Description of the workgroup.
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
Name of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
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
Key-value mapping of resource tags for the workgroup.
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
Amazon Resource Name (ARN) of the workgroup
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfiguration">Dict[Workgroup<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with various settings for the workgroup. Documented below.
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
Description of the workgroup.
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
Name of the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
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
Key-value mapping of resource tags for the workgroup.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### WorkgroupConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WorkgroupConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WorkgroupConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/athena?tab=doc#WorkgroupConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/athena?tab=doc#WorkgroupConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Athena.WorkgroupConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Athena.WorkgroupConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Bytes<wbr>Scanned<wbr>Cutoff<wbr>Per<wbr>Query</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enforce<wbr>Workgroup<wbr>Configuration</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publish<wbr>Cloudwatch<wbr>Metrics<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Result<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfigurationresultconfiguration">Pulumi.<wbr>Aws.<wbr>Athena.<wbr>Workgroup<wbr>Configuration<wbr>Result<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with result settings. Documented below.
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
            <td class="align-top">Bytes<wbr>Scanned<wbr>Cutoff<wbr>Per<wbr>Query</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enforce<wbr>Workgroup<wbr>Configuration</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publish<wbr>Cloudwatch<wbr>Metrics<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Result<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfigurationresultconfiguration">*Workgroup<wbr>Configuration<wbr>Result<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with result settings. Documented below.
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
            <td class="align-top">bytes<wbr>Scanned<wbr>Cutoff<wbr>Per<wbr>Query</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enforce<wbr>Workgroup<wbr>Configuration</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publish<wbr>Cloudwatch<wbr>Metrics<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">result<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfigurationresultconfiguration">athena.<wbr>Workgroup<wbr>Configuration<wbr>Result<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with result settings. Documented below.
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
            <td class="align-top">bytes<wbr>Scanned<wbr>Cutoff<wbr>Per<wbr>Query</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enforce<wbr>Workgroup<wbr>Configuration</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publish<wbr>Cloudwatch<wbr>Metrics<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">result<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfigurationresultconfiguration">Dict[Workgroup<wbr>Configuration<wbr>Result<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with result settings. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### WorkgroupConfigurationResultConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WorkgroupConfigurationResultConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WorkgroupConfigurationResultConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/athena?tab=doc#WorkgroupConfigurationResultConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/athena?tab=doc#WorkgroupConfigurationResultConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Athena.WorkgroupConfigurationResultConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Athena.WorkgroupConfigurationResultConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Encryption<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfigurationresultconfigurationencryptionconfiguration">Pulumi.<wbr>Aws.<wbr>Athena.<wbr>Workgroup<wbr>Configuration<wbr>Result<wbr>Configuration<wbr>Encryption<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with encryption settings. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>Location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
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
            <td class="align-top">Encryption<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfigurationresultconfigurationencryptionconfiguration">*Workgroup<wbr>Configuration<wbr>Result<wbr>Configuration<wbr>Encryption<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with encryption settings. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>Location</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
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
            <td class="align-top">encryption<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfigurationresultconfigurationencryptionconfiguration">athena.<wbr>Workgroup<wbr>Configuration<wbr>Result<wbr>Configuration<wbr>Encryption<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with encryption settings. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output<wbr>Location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
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
            <td class="align-top">encryption_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#workgroupconfigurationresultconfigurationencryptionconfiguration">Dict[Workgroup<wbr>Configuration<wbr>Result<wbr>Configuration<wbr>Encryption<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with encryption settings. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output_<wbr>location</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### WorkgroupConfigurationResultConfigurationEncryptionConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WorkgroupConfigurationResultConfigurationEncryptionConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WorkgroupConfigurationResultConfigurationEncryptionConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/athena?tab=doc#WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/athena?tab=doc#WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Athena.WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Athena.WorkgroupConfigurationResultConfigurationEncryptionConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Encryption<wbr>Option</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3), server-side encryption with KMS-managed keys (SSE-KMS), or client-side encryption with KMS-managed keys (CSE-KMS) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup&#39;s setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
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
For SSE-KMS and CSE-KMS, this is the KMS key Amazon Resource Name (ARN).
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
            <td class="align-top">Encryption<wbr>Option</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3), server-side encryption with KMS-managed keys (SSE-KMS), or client-side encryption with KMS-managed keys (CSE-KMS) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup&#39;s setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
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
For SSE-KMS and CSE-KMS, this is the KMS key Amazon Resource Name (ARN).
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
            <td class="align-top">encryption<wbr>Option</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3), server-side encryption with KMS-managed keys (SSE-KMS), or client-side encryption with KMS-managed keys (CSE-KMS) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup&#39;s setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
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
For SSE-KMS and CSE-KMS, this is the KMS key Amazon Resource Name (ARN).
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
            <td class="align-top">encryption<wbr>Option</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3), server-side encryption with KMS-managed keys (SSE-KMS), or client-side encryption with KMS-managed keys (CSE-KMS) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup&#39;s setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
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
For SSE-KMS and CSE-KMS, this is the KMS key Amazon Resource Name (ARN).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







