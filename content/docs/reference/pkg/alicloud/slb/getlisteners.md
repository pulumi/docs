
---
title: "GetListeners"
block_external_search_index: true
---



This data source provides the listeners related to a server load balancer of the current Alibaba Cloud user.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as alicloud from "@pulumi/alicloud";

const sampleDs = alicloud_slb_sample_slb.id.apply(id => alicloud.slb.getListeners({
    loadBalancerId: id,
}, { async: true }));

export const firstSlbListenerProtocol = sampleDs.slbListeners[0].protocol;
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/slb_listeners.html.markdown.





## Using GetListeners

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getListeners<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#GetListenersArgs">GetListenersArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#GetListenersResult">GetListenersResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_listeners(</span>description_regex=None<span class="p">, </span>frontend_port=None<span class="p">, </span>load_balancer_id=None<span class="p">, </span>output_file=None<span class="p">, </span>protocol=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupListeners<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#LookupListenersArgs">LookupListenersArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#LookupListenersResult">LookupListenersResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetListeners </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.GetListenersResult.html">GetListenersResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.GetListenersArgs.html">GetListenersArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by SLB listener description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Frontend<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified frontend port.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the SLB with listeners.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified protocol. Valid values: `http`, `https`, `tcp` and `udp`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by SLB listener description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Frontend<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified frontend port.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the SLB with listeners.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified protocol. Valid values: `http`, `https`, `tcp` and `udp`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by SLB listener description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>frontend<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified frontend port.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the SLB with listeners.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified protocol. Valid values: `http`, `https`, `tcp` and `udp`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by SLB listener description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>frontend_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified frontend port.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>load_<wbr>balancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the SLB with listeners.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified protocol. Valid values: `http`, `https`, `tcp` and `udp`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetListeners Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Frontend<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Frontend port used to receive incoming traffic and distribute it to the backend servers.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Listener protocol. Possible values: `http`, `https`, `tcp` and `udp`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Slb<wbr>Listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlistenersslblistener">List&lt;Get<wbr>Listeners<wbr>Slb<wbr>Listener&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of SLB listeners. Each element contains the following attributes:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Frontend<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Frontend port used to receive incoming traffic and distribute it to the backend servers.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Listener protocol. Possible values: `http`, `https`, `tcp` and `udp`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Slb<wbr>Listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlistenersslblistener">[]Get<wbr>Listeners<wbr>Slb<wbr>Listener</a></span>
    </dt>
    <dd>{{% md %}}A list of SLB listeners. Each element contains the following attributes:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>description<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>frontend<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Frontend port used to receive incoming traffic and distribute it to the backend servers.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Listener protocol. Possible values: `http`, `https`, `tcp` and `udp`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>slb<wbr>Listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlistenersslblistener">Get<wbr>Listeners<wbr>Slb<wbr>Listener[]</a></span>
    </dt>
    <dd>{{% md %}}A list of SLB listeners. Each element contains the following attributes:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>description_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>frontend_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Frontend port used to receive incoming traffic and distribute it to the backend servers.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>load_<wbr>balancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Listener protocol. Possible values: `http`, `https`, `tcp` and `udp`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>slb_<wbr>listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlistenersslblistener">List[Get<wbr>Listeners<wbr>Slb<wbr>Listener]</a></span>
    </dt>
    <dd>{{% md %}}A list of SLB listeners. Each element contains the following attributes:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Listeners<wbr>Slb<wbr>Listener</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetListenersSlbListener">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#GetListenersSlbListener">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Backend<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Port opened on the backend server to receive requests.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Peak bandwidth. If the value is set to -1, the listener is not limited by bandwidth.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ca<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the CA certificate (only required when two-way authentication is used). Only available when the protocol is `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cookie</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cookie configured by the backend server. Only available when the sticky_session_type is `server`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cookie<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Cookie timeout in seconds. Only available when the sticky_session_type is `insert`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description of slb listener.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Http2</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Whether to enable https listener support http2 or not. Valid values are `on` and `off`. Default to `on`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Established<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Connection timeout in seconds for the Layer 4 TCP listener. Only available when the protocol is `tcp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Frontend<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified frontend port.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Gzip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether Gzip compression is enabled or not. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether health check is enabled of not. Possible values are `on` and `off`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Connect<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Port used for health check.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Connect<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Amount of time in seconds to wait for the response for a health check.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Domain name used for health check. The SLB sends HTTP head requests to the backend server, the domain is useful when the backend server verifies the host field in the requests. Only available when the protocol is `http`, `https` or `tcp` (in this case health_check_type must be `http`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Http<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}HTTP status codes indicating that the health check is normal. It can contain several comma-separated values such as "http_2xx,http_3xx". Only available when the protocol is `http`, `https` or `tcp` (in this case health_check_type must be `http`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Time interval between two consecutive health checks.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Amount of time in seconds to wait for the response from a health check. If an ECS instance sends no response within the specified timeout period, the health check fails. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Health check method. Possible values are `tcp` and `http`. Only available when the protocol is `tcp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URI used for health check. Only available when the protocol is `http`, `https` or `tcp` (in this case health_check_type must be `http`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Healthy<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of consecutive successes of health check performed on the same ECS instance (from failure to success).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Idle<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Timeout of http or https listener established connection idle timeout. Valid value range: [1-60] in seconds. Default to 15.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Master<wbr>Slave<wbr>Server<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the active/standby server group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Persistence<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Timeout value of the TCP connection in seconds. If the value is 0, the session persistence function is disabled. Only available when the protocol is `tcp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified protocol. Valid values: `http`, `https`, `tcp` and `udp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Request<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Timeout of http or https listener request (which does not get response from backend) timeout. Valid value range: [1-180] in seconds. Default to 60.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scheduler</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Algorithm used to distribute traffic. Possible values: `wrr` (weighted round robin), `wlc` (weighted least connection) and `rr` (round robin).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Security status. Only available when the protocol is `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the linked VServer group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ssl<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the server certificate. Only available when the protocol is `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Listener status.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sticky<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether session persistence is enabled or not. If enabled, all session requests from the same client are sent to the same backend server. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sticky<wbr>Session<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Method used to handle the cookie. Possible values are `insert` (cookie added to the response) and `server` (cookie set by the backend server). Only available when the protocol is `http` or `https` and sticky_session is `on`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tls<wbr>Cipher<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Https listener TLS cipher policy. Valid values are `tls_cipher_policy_1_0`, `tls_cipher_policy_1_1`, `tls_cipher_policy_1_2`, `tls_cipher_policy_1_2_strict`. Default to `tls_cipher_policy_1_0`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Unhealthy<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of consecutive failures of health check performed on the same ECS instance (from success to failure).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>XForwarded<wbr>For</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For" is added or not; it allows the backend server to know about the user's IP address. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>XForwarded<wbr>For<wbr>Slb<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For_SLBID" is added or not; it allows the backend server to know about the SLB ID. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>XForwarded<wbr>For<wbr>Slb<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For_SLBIP" is added or not; it allows the backend server to know about the SLB IP address. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>XForwarded<wbr>For<wbr>Slb<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For_proto" is added or not; it allows the backend server to know about the user's protocol. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Backend<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Port opened on the backend server to receive requests.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Peak bandwidth. If the value is set to -1, the listener is not limited by bandwidth.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ca<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the CA certificate (only required when two-way authentication is used). Only available when the protocol is `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cookie</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cookie configured by the backend server. Only available when the sticky_session_type is `server`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cookie<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Cookie timeout in seconds. Only available when the sticky_session_type is `insert`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description of slb listener.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Http2</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Whether to enable https listener support http2 or not. Valid values are `on` and `off`. Default to `on`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Established<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Connection timeout in seconds for the Layer 4 TCP listener. Only available when the protocol is `tcp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Frontend<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified frontend port.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Gzip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether Gzip compression is enabled or not. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether health check is enabled of not. Possible values are `on` and `off`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Connect<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Port used for health check.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Connect<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Amount of time in seconds to wait for the response for a health check.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Domain name used for health check. The SLB sends HTTP head requests to the backend server, the domain is useful when the backend server verifies the host field in the requests. Only available when the protocol is `http`, `https` or `tcp` (in this case health_check_type must be `http`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Http<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}HTTP status codes indicating that the health check is normal. It can contain several comma-separated values such as "http_2xx,http_3xx". Only available when the protocol is `http`, `https` or `tcp` (in this case health_check_type must be `http`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Time interval between two consecutive health checks.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Amount of time in seconds to wait for the response from a health check. If an ECS instance sends no response within the specified timeout period, the health check fails. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Health check method. Possible values are `tcp` and `http`. Only available when the protocol is `tcp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URI used for health check. Only available when the protocol is `http`, `https` or `tcp` (in this case health_check_type must be `http`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Healthy<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of consecutive successes of health check performed on the same ECS instance (from failure to success).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Idle<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Timeout of http or https listener established connection idle timeout. Valid value range: [1-60] in seconds. Default to 15.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Master<wbr>Slave<wbr>Server<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the active/standby server group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Persistence<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Timeout value of the TCP connection in seconds. If the value is 0, the session persistence function is disabled. Only available when the protocol is `tcp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified protocol. Valid values: `http`, `https`, `tcp` and `udp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Request<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Timeout of http or https listener request (which does not get response from backend) timeout. Valid value range: [1-180] in seconds. Default to 60.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scheduler</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Algorithm used to distribute traffic. Possible values: `wrr` (weighted round robin), `wlc` (weighted least connection) and `rr` (round robin).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Security status. Only available when the protocol is `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the linked VServer group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ssl<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the server certificate. Only available when the protocol is `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Listener status.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sticky<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether session persistence is enabled or not. If enabled, all session requests from the same client are sent to the same backend server. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sticky<wbr>Session<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Method used to handle the cookie. Possible values are `insert` (cookie added to the response) and `server` (cookie set by the backend server). Only available when the protocol is `http` or `https` and sticky_session is `on`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tls<wbr>Cipher<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Https listener TLS cipher policy. Valid values are `tls_cipher_policy_1_0`, `tls_cipher_policy_1_1`, `tls_cipher_policy_1_2`, `tls_cipher_policy_1_2_strict`. Default to `tls_cipher_policy_1_0`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Unhealthy<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of consecutive failures of health check performed on the same ECS instance (from success to failure).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>XForwarded<wbr>For</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For" is added or not; it allows the backend server to know about the user's IP address. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>XForwarded<wbr>For<wbr>Slb<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For_SLBID" is added or not; it allows the backend server to know about the SLB ID. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>XForwarded<wbr>For<wbr>Slb<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For_SLBIP" is added or not; it allows the backend server to know about the SLB IP address. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>XForwarded<wbr>For<wbr>Slb<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For_proto" is added or not; it allows the backend server to know about the user's protocol. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>backend<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Port opened on the backend server to receive requests.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Peak bandwidth. If the value is set to -1, the listener is not limited by bandwidth.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ca<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the CA certificate (only required when two-way authentication is used). Only available when the protocol is `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cookie</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cookie configured by the backend server. Only available when the sticky_session_type is `server`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cookie<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Cookie timeout in seconds. Only available when the sticky_session_type is `insert`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description of slb listener.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Http2</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Whether to enable https listener support http2 or not. Valid values are `on` and `off`. Default to `on`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>established<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Connection timeout in seconds for the Layer 4 TCP listener. Only available when the protocol is `tcp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>frontend<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified frontend port.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>gzip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether Gzip compression is enabled or not. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether health check is enabled of not. Possible values are `on` and `off`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Check<wbr>Connect<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Port used for health check.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Check<wbr>Connect<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Amount of time in seconds to wait for the response for a health check.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Check<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Domain name used for health check. The SLB sends HTTP head requests to the backend server, the domain is useful when the backend server verifies the host field in the requests. Only available when the protocol is `http`, `https` or `tcp` (in this case health_check_type must be `http`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Check<wbr>Http<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}HTTP status codes indicating that the health check is normal. It can contain several comma-separated values such as "http_2xx,http_3xx". Only available when the protocol is `http`, `https` or `tcp` (in this case health_check_type must be `http`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Check<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Time interval between two consecutive health checks.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Check<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Amount of time in seconds to wait for the response from a health check. If an ECS instance sends no response within the specified timeout period, the health check fails. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Check<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Health check method. Possible values are `tcp` and `http`. Only available when the protocol is `tcp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Check<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URI used for health check. Only available when the protocol is `http`, `https` or `tcp` (in this case health_check_type must be `http`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>healthy<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Number of consecutive successes of health check performed on the same ECS instance (from failure to success).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>idle<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Timeout of http or https listener established connection idle timeout. Valid value range: [1-60] in seconds. Default to 15.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>master<wbr>Slave<wbr>Server<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the active/standby server group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>persistence<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Timeout value of the TCP connection in seconds. If the value is 0, the session persistence function is disabled. Only available when the protocol is `tcp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified protocol. Valid values: `http`, `https`, `tcp` and `udp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>request<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Timeout of http or https listener request (which does not get response from backend) timeout. Valid value range: [1-180] in seconds. Default to 60.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scheduler</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Algorithm used to distribute traffic. Possible values: `wrr` (weighted round robin), `wlc` (weighted least connection) and `rr` (round robin).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>security<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Security status. Only available when the protocol is `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the linked VServer group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ssl<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the server certificate. Only available when the protocol is `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Listener status.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sticky<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether session persistence is enabled or not. If enabled, all session requests from the same client are sent to the same backend server. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sticky<wbr>Session<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Method used to handle the cookie. Possible values are `insert` (cookie added to the response) and `server` (cookie set by the backend server). Only available when the protocol is `http` or `https` and sticky_session is `on`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tls<wbr>Cipher<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Https listener TLS cipher policy. Valid values are `tls_cipher_policy_1_0`, `tls_cipher_policy_1_1`, `tls_cipher_policy_1_2`, `tls_cipher_policy_1_2_strict`. Default to `tls_cipher_policy_1_0`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>unhealthy<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Number of consecutive failures of health check performed on the same ECS instance (from success to failure).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x<wbr>Forwarded<wbr>For</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For" is added or not; it allows the backend server to know about the user's IP address. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x<wbr>Forwarded<wbr>For<wbr>Slb<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For_SLBID" is added or not; it allows the backend server to know about the SLB ID. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x<wbr>Forwarded<wbr>For<wbr>Slb<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For_SLBIP" is added or not; it allows the backend server to know about the SLB IP address. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x<wbr>Forwarded<wbr>For<wbr>Slb<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For_proto" is added or not; it allows the backend server to know about the user's protocol. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>backend_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Port opened on the backend server to receive requests.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Peak bandwidth. If the value is set to -1, the listener is not limited by bandwidth.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ca<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the CA certificate (only required when two-way authentication is used). Only available when the protocol is `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cookie</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cookie configured by the backend server. Only available when the sticky_session_type is `server`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cookie_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Cookie timeout in seconds. Only available when the sticky_session_type is `insert`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of slb listener.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enable_<wbr>http2</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Whether to enable https listener support http2 or not. Valid values are `on` and `off`. Default to `on`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>established_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Connection timeout in seconds for the Layer 4 TCP listener. Only available when the protocol is `tcp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>frontend_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified frontend port.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>gzip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicate whether Gzip compression is enabled or not. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicate whether health check is enabled of not. Possible values are `on` and `off`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health_<wbr>check_<wbr>connect_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Port used for health check.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Check<wbr>Connect<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Amount of time in seconds to wait for the response for a health check.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health_<wbr>check_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Domain name used for health check. The SLB sends HTTP head requests to the backend server, the domain is useful when the backend server verifies the host field in the requests. Only available when the protocol is `http`, `https` or `tcp` (in this case health_check_type must be `http`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health_<wbr>check_<wbr>http_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}HTTP status codes indicating that the health check is normal. It can contain several comma-separated values such as "http_2xx,http_3xx". Only available when the protocol is `http`, `https` or `tcp` (in this case health_check_type must be `http`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health_<wbr>check_<wbr>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Time interval between two consecutive health checks.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health_<wbr>check_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Amount of time in seconds to wait for the response from a health check. If an ECS instance sends no response within the specified timeout period, the health check fails. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health_<wbr>check_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Health check method. Possible values are `tcp` and `http`. Only available when the protocol is `tcp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health_<wbr>check_<wbr>uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URI used for health check. Only available when the protocol is `http`, `https` or `tcp` (in this case health_check_type must be `http`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>healthy_<wbr>threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of consecutive successes of health check performed on the same ECS instance (from failure to success).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>idle_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Timeout of http or https listener established connection idle timeout. Valid value range: [1-60] in seconds. Default to 15.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>master_<wbr>slave_<wbr>server_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the active/standby server group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>persistence_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Timeout value of the TCP connection in seconds. If the value is 0, the session persistence function is disabled. Only available when the protocol is `tcp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filter listeners by the specified protocol. Valid values: `http`, `https`, `tcp` and `udp`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>request_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Timeout of http or https listener request (which does not get response from backend) timeout. Valid value range: [1-180] in seconds. Default to 60.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scheduler</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Algorithm used to distribute traffic. Possible values: `wrr` (weighted round robin), `wlc` (weighted least connection) and `rr` (round robin).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>security<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Security status. Only available when the protocol is `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server_<wbr>certificate_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the linked VServer group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ssl_<wbr>certificate_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the server certificate. Only available when the protocol is `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Listener status.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sticky_<wbr>session</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicate whether session persistence is enabled or not. If enabled, all session requests from the same client are sent to the same backend server. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sticky_<wbr>session_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Method used to handle the cookie. Possible values are `insert` (cookie added to the response) and `server` (cookie set by the backend server). Only available when the protocol is `http` or `https` and sticky_session is `on`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tls_<wbr>cipher_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Https listener TLS cipher policy. Valid values are `tls_cipher_policy_1_0`, `tls_cipher_policy_1_1`, `tls_cipher_policy_1_2`, `tls_cipher_policy_1_2_strict`. Default to `tls_cipher_policy_1_0`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>unhealthy_<wbr>threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of consecutive failures of health check performed on the same ECS instance (from success to failure).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x_<wbr>forwarded_<wbr>for</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For" is added or not; it allows the backend server to know about the user's IP address. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x<wbr>Forwarded<wbr>For<wbr>Slb<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For_SLBID" is added or not; it allows the backend server to know about the SLB ID. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x<wbr>Forwarded<wbr>For<wbr>Slb<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For_SLBIP" is added or not; it allows the backend server to know about the SLB IP address. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x<wbr>Forwarded<wbr>For<wbr>Slb<wbr>Proto</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicate whether the HTTP header field "X-Forwarded-For_proto" is added or not; it allows the backend server to know about the user's protocol. Possible values are `on` and `off`. Only available when the protocol is `http` or `https`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







