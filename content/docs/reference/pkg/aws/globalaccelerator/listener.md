
---
title: "Listener"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a Global Accelerator listener.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleAccelerator = new aws.globalaccelerator.Accelerator("example", {
    attributes: {
        flowLogsEnabled: true,
        flowLogsS3Bucket: "example-bucket",
        flowLogsS3Prefix: "flow-logs/",
    },
    enabled: true,
    ipAddressType: "IPV4",
});
const exampleListener = new aws.globalaccelerator.Listener("example", {
    acceleratorArn: exampleAccelerator.id,
    clientAffinity: "SOURCE_IP",
    portRanges: [{
        fromPort: 80,
        toPort: 80,
    }],
    protocol: "TCP",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/globalaccelerator_listener.markdown.



## Create a Listener Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/globalaccelerator/#Listener">Listener</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/globalaccelerator/#ListenerArgs">ListenerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Listener</span><span class="p">(resource_name, opts=None, </span>accelerator_arn=None<span class="p">, </span>client_affinity=None<span class="p">, </span>port_ranges=None<span class="p">, </span>protocol=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewListener<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/globalaccelerator?tab=doc#ListenerArgs">ListenerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/globalaccelerator?tab=doc#Listener">Listener</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Globalaccelerator.Listener.html">Listener</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Globalaccelerator.ListenerArgs.html">ListenerArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Listener resource with the given unique name, arguments, and options.

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
            <td class="align-top">Accelerator<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) of your accelerator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Affinity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the &#34;five-tuple&#34; properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the &#34;two-tuple&#34; properties of source (client) IP address and destination IP address to select the hash value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port<wbr>Ranges</td>
            <td class="align-top">
                
                <code><a href="#listenerportrange">List&lt;Pulumi.<wbr>Aws.<wbr>Globalaccelerator.<wbr>Listener<wbr>Port<wbr>Range<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of port ranges for the connections from clients to the accelerator. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
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
            <td class="align-top">Accelerator<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) of your accelerator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Affinity</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the &#34;five-tuple&#34; properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the &#34;two-tuple&#34; properties of source (client) IP address and destination IP address to select the hash value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port<wbr>Ranges</td>
            <td class="align-top">
                
                <code><a href="#listenerportrange">[]Listener<wbr>Port<wbr>Range</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of port ranges for the connections from clients to the accelerator. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
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
            <td class="align-top">accelerator<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) of your accelerator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Affinity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the &#34;five-tuple&#34; properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the &#34;two-tuple&#34; properties of source (client) IP address and destination IP address to select the hash value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port<wbr>Ranges</td>
            <td class="align-top">
                
                <code><a href="#listenerportrange">globalaccelerator.<wbr>Listener<wbr>Port<wbr>Range[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of port ranges for the connections from clients to the accelerator. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
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
            <td class="align-top">accelerator_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) of your accelerator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>affinity</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the &#34;five-tuple&#34; properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the &#34;two-tuple&#34; properties of source (client) IP address and destination IP address to select the hash value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port_<wbr>ranges</td>
            <td class="align-top">
                
                <code><a href="#listenerportrange">List[Listener<wbr>Port<wbr>Range]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of port ranges for the connections from clients to the accelerator. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Listener Output Properties

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
            <td class="align-top">Accelerator<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of your accelerator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Affinity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the &#34;five-tuple&#34; properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the &#34;two-tuple&#34; properties of source (client) IP address and destination IP address to select the hash value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port<wbr>Ranges</td>
            <td class="align-top">
                
                <code><a href="#listenerportrange">List&lt;Pulumi.<wbr>Aws.<wbr>Globalaccelerator.<wbr>Listener<wbr>Port<wbr>Range&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} The list of port ranges for the connections from clients to the accelerator. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
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
            <td class="align-top">Accelerator<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of your accelerator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Affinity</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the &#34;five-tuple&#34; properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the &#34;two-tuple&#34; properties of source (client) IP address and destination IP address to select the hash value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port<wbr>Ranges</td>
            <td class="align-top">
                
                <code><a href="#listenerportrange">[]Listener<wbr>Port<wbr>Range</a></code>
            </td>
            <td class="align-top">{{% md %}} The list of port ranges for the connections from clients to the accelerator. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
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
            <td class="align-top">accelerator<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of your accelerator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Affinity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the &#34;five-tuple&#34; properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the &#34;two-tuple&#34; properties of source (client) IP address and destination IP address to select the hash value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port<wbr>Ranges</td>
            <td class="align-top">
                
                <code><a href="#listenerportrange">globalaccelerator.<wbr>Listener<wbr>Port<wbr>Range[]</a></code>
            </td>
            <td class="align-top">{{% md %}} The list of port ranges for the connections from clients to the accelerator. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
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
            <td class="align-top">accelerator_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of your accelerator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>affinity</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the &#34;five-tuple&#34; properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the &#34;two-tuple&#34; properties of source (client) IP address and destination IP address to select the hash value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port_<wbr>ranges</td>
            <td class="align-top">
                
                <code><a href="#listenerportrange">List[Listener<wbr>Port<wbr>Range]</a></code>
            </td>
            <td class="align-top">{{% md %}} The list of port ranges for the connections from clients to the accelerator. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Listener Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/globalaccelerator/#ListenerState">ListenerState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/globalaccelerator/#Listener">Listener</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>accelerator_arn=None<span class="p">, </span>client_affinity=None<span class="p">, </span>port_ranges=None<span class="p">, </span>protocol=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetListener<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/globalaccelerator?tab=doc#ListenerState">ListenerState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/globalaccelerator?tab=doc#Listener">Listener</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Globalaccelerator.Listener.html">Listener</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Globalaccelerator.ListenerState.html">ListenerState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Listener resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Accelerator<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of your accelerator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Affinity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the &#34;five-tuple&#34; properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the &#34;two-tuple&#34; properties of source (client) IP address and destination IP address to select the hash value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port<wbr>Ranges</td>
            <td class="align-top">
                
                <code><a href="#listenerportrange">List&lt;Pulumi.<wbr>Aws.<wbr>Globalaccelerator.<wbr>Listener<wbr>Port<wbr>Range<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of port ranges for the connections from clients to the accelerator. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
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
            <td class="align-top">Accelerator<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of your accelerator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Affinity</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the &#34;five-tuple&#34; properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the &#34;two-tuple&#34; properties of source (client) IP address and destination IP address to select the hash value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port<wbr>Ranges</td>
            <td class="align-top">
                
                <code><a href="#listenerportrange">[]Listener<wbr>Port<wbr>Range</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of port ranges for the connections from clients to the accelerator. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
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
            <td class="align-top">accelerator<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of your accelerator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Affinity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the &#34;five-tuple&#34; properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the &#34;two-tuple&#34; properties of source (client) IP address and destination IP address to select the hash value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port<wbr>Ranges</td>
            <td class="align-top">
                
                <code><a href="#listenerportrange">globalaccelerator.<wbr>Listener<wbr>Port<wbr>Range[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of port ranges for the connections from clients to the accelerator. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
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
            <td class="align-top">accelerator_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of your accelerator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>affinity</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Direct all requests from a user to the same endpoint. Valid values are `NONE`, `SOURCE_IP`. Default: `NONE`. If `NONE`, Global Accelerator uses the &#34;five-tuple&#34; properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If `SOURCE_IP`, Global Accelerator uses the &#34;two-tuple&#34; properties of source (client) IP address and destination IP address to select the hash value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port_<wbr>ranges</td>
            <td class="align-top">
                
                <code><a href="#listenerportrange">List[Listener<wbr>Port<wbr>Range]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of port ranges for the connections from clients to the accelerator. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol for the connections from clients to the accelerator. Valid values are `TCP`, `UDP`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ListenerPortRange
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerPortRange">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerPortRange">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/globalaccelerator?tab=doc#ListenerPortRangeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/globalaccelerator?tab=doc#ListenerPortRangeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Globalaccelerator.ListenerPortRangeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Globalaccelerator.ListenerPortRange.html">output</a> API doc for this type.
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
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The first port in the range of ports, inclusive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The last port in the range of ports, inclusive.
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
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The first port in the range of ports, inclusive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The last port in the range of ports, inclusive.
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
            <td class="align-top">from<wbr>Port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The first port in the range of ports, inclusive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to<wbr>Port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The last port in the range of ports, inclusive.
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
            <td class="align-top">from_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The first port in the range of ports, inclusive.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The last port in the range of ports, inclusive.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







