
---
title: "App"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a Pinpoint App resource.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.pinpoint.App("example", {
    limits: {
        maximumDuration: 600,
    },
    quietTime: {
        end: "06:00",
        start: "00:00",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/pinpoint_app.markdown.



## Create a App Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/pinpoint/#App">App</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/pinpoint/#AppArgs">AppArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">App</span><span class="p">(resource_name, opts=None, </span>campaign_hook=None<span class="p">, </span>limits=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>quiet_time=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewApp<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pinpoint?tab=doc#AppArgs">AppArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pinpoint?tab=doc#App">App</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pinpoint.App.html">App</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pinpoint.AppArgs.html">AppArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a App resource with the given unique name, arguments, and options.

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
            <td class="align-top">Campaign<wbr>Hook</td>
            <td class="align-top">
                
                <code><a href="#appcampaignhook">Pulumi.<wbr>Aws.<wbr>Pinpoint.<wbr>App<wbr>Campaign<wbr>Hook<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Limits</td>
            <td class="align-top">
                
                <code><a href="#applimits">Pulumi.<wbr>Aws.<wbr>Pinpoint.<wbr>App<wbr>Limits<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
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
The application name. By default generated by this provider
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Pinpoint application. Conflicts with `name`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quiet<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#appquiettime">Pulumi.<wbr>Aws.<wbr>Pinpoint.<wbr>App<wbr>Quiet<wbr>Time<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
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
Key-value mapping of resource tags
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
            <td class="align-top">Campaign<wbr>Hook</td>
            <td class="align-top">
                
                <code><a href="#appcampaignhook">*App<wbr>Campaign<wbr>Hook</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Limits</td>
            <td class="align-top">
                
                <code><a href="#applimits">*App<wbr>Limits</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
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
The application name. By default generated by this provider
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Pinpoint application. Conflicts with `name`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quiet<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#appquiettime">*App<wbr>Quiet<wbr>Time</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
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
Key-value mapping of resource tags
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
            <td class="align-top">campaign<wbr>Hook</td>
            <td class="align-top">
                
                <code><a href="#appcampaignhook">pinpoint.<wbr>App<wbr>Campaign<wbr>Hook?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">limits</td>
            <td class="align-top">
                
                <code><a href="#applimits">pinpoint.<wbr>App<wbr>Limits?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
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
The application name. By default generated by this provider
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Pinpoint application. Conflicts with `name`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quiet<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#appquiettime">pinpoint.<wbr>App<wbr>Quiet<wbr>Time?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
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
Key-value mapping of resource tags
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
            <td class="align-top">campaign_<wbr>hook</td>
            <td class="align-top">
                
                <code><a href="#appcampaignhook">Dict[App<wbr>Campaign<wbr>Hook]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">limits</td>
            <td class="align-top">
                
                <code><a href="#applimits">Dict[App<wbr>Limits]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
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
The application name. By default generated by this provider
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Pinpoint application. Conflicts with `name`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quiet_<wbr>time</td>
            <td class="align-top">
                
                <code><a href="#appquiettime">Dict[App<wbr>Quiet<wbr>Time]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
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
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## App Output Properties

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
            <td class="align-top">Application<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Application ID of the Pinpoint App.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the PinPoint Application
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Campaign<wbr>Hook</td>
            <td class="align-top">
                
                <code><a href="#appcampaignhook">Pulumi.<wbr>Aws.<wbr>Pinpoint.<wbr>App<wbr>Campaign<wbr>Hook?</a></code>
            </td>
            <td class="align-top">{{% md %}} The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Limits</td>
            <td class="align-top">
                
                <code><a href="#applimits">Pulumi.<wbr>Aws.<wbr>Pinpoint.<wbr>App<wbr>Limits?</a></code>
            </td>
            <td class="align-top">{{% md %}} The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The application name. By default generated by this provider
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Pinpoint application. Conflicts with `name`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quiet<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#appquiettime">Pulumi.<wbr>Aws.<wbr>Pinpoint.<wbr>App<wbr>Quiet<wbr>Time?</a></code>
            </td>
            <td class="align-top">{{% md %}} The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
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
            <td class="align-top">Application<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Application ID of the Pinpoint App.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the PinPoint Application
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Campaign<wbr>Hook</td>
            <td class="align-top">
                
                <code><a href="#appcampaignhook">*App<wbr>Campaign<wbr>Hook</a></code>
            </td>
            <td class="align-top">{{% md %}} The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Limits</td>
            <td class="align-top">
                
                <code><a href="#applimits">*App<wbr>Limits</a></code>
            </td>
            <td class="align-top">{{% md %}} The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The application name. By default generated by this provider
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Pinpoint application. Conflicts with `name`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quiet<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#appquiettime">*App<wbr>Quiet<wbr>Time</a></code>
            </td>
            <td class="align-top">{{% md %}} The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
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
            <td class="align-top">application<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Application ID of the Pinpoint App.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the PinPoint Application
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">campaign<wbr>Hook</td>
            <td class="align-top">
                
                <code><a href="#appcampaignhook">pinpoint.<wbr>App<wbr>Campaign<wbr>Hook?</a></code>
            </td>
            <td class="align-top">{{% md %}} The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">limits</td>
            <td class="align-top">
                
                <code><a href="#applimits">pinpoint.<wbr>App<wbr>Limits?</a></code>
            </td>
            <td class="align-top">{{% md %}} The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The application name. By default generated by this provider
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Pinpoint application. Conflicts with `name`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quiet<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#appquiettime">pinpoint.<wbr>App<wbr>Quiet<wbr>Time?</a></code>
            </td>
            <td class="align-top">{{% md %}} The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
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
            <td class="align-top">application_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Application ID of the Pinpoint App.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the PinPoint Application
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">campaign_<wbr>hook</td>
            <td class="align-top">
                
                <code><a href="#appcampaignhook">Dict[App<wbr>Campaign<wbr>Hook]</a></code>
            </td>
            <td class="align-top">{{% md %}} The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">limits</td>
            <td class="align-top">
                
                <code><a href="#applimits">Dict[App<wbr>Limits]</a></code>
            </td>
            <td class="align-top">{{% md %}} The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The application name. By default generated by this provider
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Pinpoint application. Conflicts with `name`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quiet_<wbr>time</td>
            <td class="align-top">
                
                <code><a href="#appquiettime">Dict[App<wbr>Quiet<wbr>Time]</a></code>
            </td>
            <td class="align-top">{{% md %}} The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing App Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/pinpoint/#AppState">AppState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/pinpoint/#App">App</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>application_id=None<span class="p">, </span>arn=None<span class="p">, </span>campaign_hook=None<span class="p">, </span>limits=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>quiet_time=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetApp<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pinpoint?tab=doc#AppState">AppState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pinpoint?tab=doc#App">App</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pinpoint.App.html">App</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pinpoint.AppState.html">AppState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing App resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Application<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Application ID of the Pinpoint App.
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
Amazon Resource Name (ARN) of the PinPoint Application
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Campaign<wbr>Hook</td>
            <td class="align-top">
                
                <code><a href="#appcampaignhook">Pulumi.<wbr>Aws.<wbr>Pinpoint.<wbr>App<wbr>Campaign<wbr>Hook<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Limits</td>
            <td class="align-top">
                
                <code><a href="#applimits">Pulumi.<wbr>Aws.<wbr>Pinpoint.<wbr>App<wbr>Limits<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
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
The application name. By default generated by this provider
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Pinpoint application. Conflicts with `name`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quiet<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#appquiettime">Pulumi.<wbr>Aws.<wbr>Pinpoint.<wbr>App<wbr>Quiet<wbr>Time<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
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
Key-value mapping of resource tags
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
            <td class="align-top">Application<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Application ID of the Pinpoint App.
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
Amazon Resource Name (ARN) of the PinPoint Application
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Campaign<wbr>Hook</td>
            <td class="align-top">
                
                <code><a href="#appcampaignhook">*App<wbr>Campaign<wbr>Hook</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Limits</td>
            <td class="align-top">
                
                <code><a href="#applimits">*App<wbr>Limits</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
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
The application name. By default generated by this provider
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Pinpoint application. Conflicts with `name`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quiet<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#appquiettime">*App<wbr>Quiet<wbr>Time</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
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
Key-value mapping of resource tags
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
            <td class="align-top">application<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Application ID of the Pinpoint App.
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
Amazon Resource Name (ARN) of the PinPoint Application
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">campaign<wbr>Hook</td>
            <td class="align-top">
                
                <code><a href="#appcampaignhook">pinpoint.<wbr>App<wbr>Campaign<wbr>Hook?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">limits</td>
            <td class="align-top">
                
                <code><a href="#applimits">pinpoint.<wbr>App<wbr>Limits?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
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
The application name. By default generated by this provider
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Pinpoint application. Conflicts with `name`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quiet<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#appquiettime">pinpoint.<wbr>App<wbr>Quiet<wbr>Time?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
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
Key-value mapping of resource tags
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
            <td class="align-top">application_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Application ID of the Pinpoint App.
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
Amazon Resource Name (ARN) of the PinPoint Application
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">campaign_<wbr>hook</td>
            <td class="align-top">
                
                <code><a href="#appcampaignhook">Dict[App<wbr>Campaign<wbr>Hook]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">limits</td>
            <td class="align-top">
                
                <code><a href="#applimits">Dict[App<wbr>Limits]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
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
The application name. By default generated by this provider
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Pinpoint application. Conflicts with `name`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quiet_<wbr>time</td>
            <td class="align-top">
                
                <code><a href="#appquiettime">Dict[App<wbr>Quiet<wbr>Time]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
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
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### AppCampaignHook
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AppCampaignHook">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AppCampaignHook">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pinpoint?tab=doc#AppCampaignHookArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pinpoint?tab=doc#AppCampaignHookOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pinpoint.AppCampaignHookArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pinpoint.AppCampaignHook.html">output</a> API doc for this type.
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
            <td class="align-top">Lambda<wbr>Function<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda function name or ARN to be called for delivery. Conflicts with `web_url`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
What mode Lambda should be invoked in. Valid values for this parameter are `DELIVERY`, `FILTER`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request. Conflicts with `lambda_function_name`
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
            <td class="align-top">Lambda<wbr>Function<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda function name or ARN to be called for delivery. Conflicts with `web_url`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
What mode Lambda should be invoked in. Valid values for this parameter are `DELIVERY`, `FILTER`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Url</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request. Conflicts with `lambda_function_name`
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
            <td class="align-top">lambda<wbr>Function<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda function name or ARN to be called for delivery. Conflicts with `web_url`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
What mode Lambda should be invoked in. Valid values for this parameter are `DELIVERY`, `FILTER`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web<wbr>Url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request. Conflicts with `lambda_function_name`
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
            <td class="align-top">lambda<wbr>Function<wbr>Name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Lambda function name or ARN to be called for delivery. Conflicts with `web_url`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
What mode Lambda should be invoked in. Valid values for this parameter are `DELIVERY`, `FILTER`.  
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web<wbr>Url</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request. Conflicts with `lambda_function_name`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### AppLimits
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AppLimits">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AppLimits">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pinpoint?tab=doc#AppLimitsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pinpoint?tab=doc#AppLimitsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pinpoint.AppLimitsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pinpoint.AppLimits.html">output</a> API doc for this type.
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
            <td class="align-top">Daily</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of messages that the campaign can send daily. 
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Duration</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Messages<wbr>Per<wbr>Second</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Total</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum total number of messages that the campaign can send.
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
            <td class="align-top">Daily</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of messages that the campaign can send daily. 
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Duration</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Messages<wbr>Per<wbr>Second</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Total</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum total number of messages that the campaign can send.
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
            <td class="align-top">daily</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of messages that the campaign can send daily. 
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum<wbr>Duration</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">messages<wbr>Per<wbr>Second</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">total</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum total number of messages that the campaign can send.
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
            <td class="align-top">daily</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of messages that the campaign can send daily. 
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum<wbr>Duration</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">messages_<wbr>per_<wbr>second</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">total</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum total number of messages that the campaign can send.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### AppQuietTime
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AppQuietTime">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AppQuietTime">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pinpoint?tab=doc#AppQuietTimeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pinpoint?tab=doc#AppQuietTimeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pinpoint.AppQuietTimeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pinpoint.AppQuietTime.html">output</a> API doc for this type.
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
            <td class="align-top">End</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default end time for quiet time in ISO 8601 format. Required if `start` is set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Start</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default start time for quiet time in ISO 8601 format. Required if `end` is set
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
            <td class="align-top">End</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default end time for quiet time in ISO 8601 format. Required if `start` is set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Start</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default start time for quiet time in ISO 8601 format. Required if `end` is set
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
            <td class="align-top">end</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default end time for quiet time in ISO 8601 format. Required if `start` is set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">start</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default start time for quiet time in ISO 8601 format. Required if `end` is set
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
            <td class="align-top">end</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default end time for quiet time in ISO 8601 format. Required if `start` is set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">start</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default start time for quiet time in ISO 8601 format. Required if `end` is set
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







