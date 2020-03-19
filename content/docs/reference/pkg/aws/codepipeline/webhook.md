
---
title: "Webhook"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a CodePipeline Webhook.

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codepipeline_webhook.markdown.



## Create a Webhook Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codepipeline/#Webhook">Webhook</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codepipeline/#WebhookArgs">WebhookArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Webhook</span><span class="p">(resource_name, opts=None, </span>authentication=None<span class="p">, </span>authentication_configuration=None<span class="p">, </span>filters=None<span class="p">, </span>name=None<span class="p">, </span>tags=None<span class="p">, </span>target_action=None<span class="p">, </span>target_pipeline=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewWebhook<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codepipeline?tab=doc#WebhookArgs">WebhookArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codepipeline?tab=doc#Webhook">Webhook</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codepipeline.Webhook.html">Webhook</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codepipeline.WebhookArgs.html">WebhookArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Webhook resource with the given unique name, arguments, and options.

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
            <td class="align-top">Authentication</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authentication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webhookauthenticationconfiguration">Pulumi.<wbr>Aws.<wbr>Codepipeline.<wbr>Webhook<wbr>Authentication<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#webhookfilter">List&lt;Pulumi.<wbr>Aws.<wbr>Codepipeline.<wbr>Webhook<wbr>Filter<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One or more `filter` blocks. Filter blocks are documented below.
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
The name of the webhook.
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
            <td class="align-top">Target<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Pipeline</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the pipeline.
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
            <td class="align-top">Authentication</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authentication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webhookauthenticationconfiguration">*codepipeline.<wbr>Webhook<wbr>Authentication<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#webhookfilter">[]codepipeline.<wbr>Webhook<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One or more `filter` blocks. Filter blocks are documented below.
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
The name of the webhook.
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
            <td class="align-top">Target<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Pipeline</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the pipeline.
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
            <td class="align-top">authentication</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authentication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webhookauthenticationconfiguration">codepipeline.<wbr>Webhook<wbr>Authentication<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#webhookfilter">codepipeline.<wbr>Webhook<wbr>Filter[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One or more `filter` blocks. Filter blocks are documented below.
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
The name of the webhook.
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
            <td class="align-top">target<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Pipeline</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the pipeline.
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
            <td class="align-top">authentication</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authentication_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#webhookauthenticationconfiguration">Dict[Webhook<wbr>Authentication<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#webhookfilter">List[Webhook<wbr>Filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One or more `filter` blocks. Filter blocks are documented below.
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
The name of the webhook.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>action</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>pipeline</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Webhook Output Properties

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
            <td class="align-top">Authentication</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authentication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webhookauthenticationconfiguration">Pulumi.<wbr>Aws.<wbr>Codepipeline.<wbr>Webhook<wbr>Authentication<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#webhookfilter">List&lt;Pulumi.<wbr>Aws.<wbr>Codepipeline.<wbr>Webhook<wbr>Filter&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more `filter` blocks. Filter blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the webhook.
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
            <td class="align-top">Target<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Pipeline</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Url</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CodePipeline webhook&#39;s URL. POST events to this endpoint to trigger the target.
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
            <td class="align-top">Authentication</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authentication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webhookauthenticationconfiguration">*codepipeline.<wbr>Webhook<wbr>Authentication<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#webhookfilter">[]codepipeline.<wbr>Webhook<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more `filter` blocks. Filter blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the webhook.
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
            <td class="align-top">Target<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Pipeline</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Url</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CodePipeline webhook&#39;s URL. POST events to this endpoint to trigger the target.
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
            <td class="align-top">authentication</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authentication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webhookauthenticationconfiguration">codepipeline.<wbr>Webhook<wbr>Authentication<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#webhookfilter">codepipeline.<wbr>Webhook<wbr>Filter[]</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more `filter` blocks. Filter blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the webhook.
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
            <td class="align-top">target<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Pipeline</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">url</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CodePipeline webhook&#39;s URL. POST events to this endpoint to trigger the target.
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
            <td class="align-top">authentication</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authentication_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#webhookauthenticationconfiguration">Dict[Webhook<wbr>Authentication<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#webhookfilter">List[Webhook<wbr>Filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more `filter` blocks. Filter blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the webhook.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>action</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>pipeline</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">url</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The CodePipeline webhook&#39;s URL. POST events to this endpoint to trigger the target.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Webhook Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codepipeline/#WebhookState">WebhookState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codepipeline/#Webhook">Webhook</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>authentication=None<span class="p">, </span>authentication_configuration=None<span class="p">, </span>filters=None<span class="p">, </span>name=None<span class="p">, </span>tags=None<span class="p">, </span>target_action=None<span class="p">, </span>target_pipeline=None<span class="p">, </span>url=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetWebhook<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codepipeline?tab=doc#WebhookState">WebhookState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codepipeline?tab=doc#Webhook">Webhook</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codepipeline.Webhook.html">Webhook</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codepipeline.WebhookState.html">WebhookState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Webhook resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Authentication</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authentication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webhookauthenticationconfiguration">Pulumi.<wbr>Aws.<wbr>Codepipeline.<wbr>Webhook<wbr>Authentication<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#webhookfilter">List&lt;Pulumi.<wbr>Aws.<wbr>Codepipeline.<wbr>Webhook<wbr>Filter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more `filter` blocks. Filter blocks are documented below.
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
The name of the webhook.
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
            <td class="align-top">Target<wbr>Action</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Pipeline</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CodePipeline webhook&#39;s URL. POST events to this endpoint to trigger the target.
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
            <td class="align-top">Authentication</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authentication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webhookauthenticationconfiguration">*codepipeline.<wbr>Webhook<wbr>Authentication<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#webhookfilter">[]codepipeline.<wbr>Webhook<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more `filter` blocks. Filter blocks are documented below.
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
The name of the webhook.
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
            <td class="align-top">Target<wbr>Action</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Pipeline</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Url</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CodePipeline webhook&#39;s URL. POST events to this endpoint to trigger the target.
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
            <td class="align-top">authentication</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authentication<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webhookauthenticationconfiguration">codepipeline.<wbr>Webhook<wbr>Authentication<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#webhookfilter">codepipeline.<wbr>Webhook<wbr>Filter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more `filter` blocks. Filter blocks are documented below.
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
The name of the webhook.
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
            <td class="align-top">target<wbr>Action</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Pipeline</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CodePipeline webhook&#39;s URL. POST events to this endpoint to trigger the target.
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
            <td class="align-top">authentication</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authentication_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#webhookauthenticationconfiguration">Dict[Webhook<wbr>Authentication<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#webhookfilter">List[Webhook<wbr>Filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more `filter` blocks. Filter blocks are documented below.
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
The name of the webhook.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>action</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>pipeline</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the pipeline.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">url</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CodePipeline webhook&#39;s URL. POST events to this endpoint to trigger the target.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### WebhookAuthenticationConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WebhookAuthenticationConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WebhookAuthenticationConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codepipeline?tab=doc#WebhookAuthenticationConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codepipeline?tab=doc#WebhookAuthenticationConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codepipeline.WebhookAuthenticationConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codepipeline.WebhookAuthenticationConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Allowed<wbr>Ip<wbr>Range</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secret<wbr>Token</td>
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
            <td class="align-top">Allowed<wbr>Ip<wbr>Range</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secret<wbr>Token</td>
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
            <td class="align-top">allowed<wbr>Ip<wbr>Range</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secret<wbr>Token</td>
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
            <td class="align-top">allowed<wbr>Ip<wbr>Range</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secret<wbr>Token</td>
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





#### WebhookFilter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WebhookFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WebhookFilter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codepipeline?tab=doc#WebhookFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codepipeline?tab=doc#WebhookFilterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codepipeline.WebhookFilterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codepipeline.WebhookFilter.html">output</a> API doc for this type.
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
            <td class="align-top">Json<wbr>Path</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Match<wbr>Equals</td>
            <td class="align-top">
                
                <code>string</code>
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
            <td class="align-top">Json<wbr>Path</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Match<wbr>Equals</td>
            <td class="align-top">
                
                <code>string</code>
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
            <td class="align-top">json<wbr>Path</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">match<wbr>Equals</td>
            <td class="align-top">
                
                <code>string</code>
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
            <td class="align-top">json<wbr>Path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">match<wbr>Equals</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







