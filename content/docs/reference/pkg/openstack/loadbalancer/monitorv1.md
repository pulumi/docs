
---
title: "MonitorV1"
block_external_search_index: true
---



Manages a V1 load balancer monitor resource within OpenStack.

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as openstack from "@pulumi/openstack";

const monitor1 = new openstack.loadbalancer.MonitorV1("monitor_1", {
    adminStateUp: "true",
    delay: 30,
    maxRetries: 3,
    timeout: 5,
    type: "PING",
});
```

{{% /example %}}
{{% /examples %}}



## Create a MonitorV1 Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/loadbalancer/#MonitorV1">MonitorV1</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/loadbalancer/#MonitorV1Args">MonitorV1Args</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">MonitorV1</span><span class="p">(resource_name, opts=None, </span>admin_state_up=None<span class="p">, </span>delay=None<span class="p">, </span>expected_codes=None<span class="p">, </span>http_method=None<span class="p">, </span>max_retries=None<span class="p">, </span>region=None<span class="p">, </span>tenant_id=None<span class="p">, </span>timeout=None<span class="p">, </span>type=None<span class="p">, </span>url_path=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewMonitorV1<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/loadbalancer?tab=doc#MonitorV1Args">MonitorV1Args</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/loadbalancer?tab=doc#MonitorV1">MonitorV1</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.LoadBalancer.MonitorV1.html">MonitorV1</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.OpenStack.LoadBalancer.MonitorV1Args.html">MonitorV1Args</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, between sending probes to members.
Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, between sending probes to members.
Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, between sending probes to members.
Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, between sending probes to members.
Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max_<wbr>retries</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expected_<wbr>codes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http_<wbr>method</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Look up an Existing MonitorV1 Resource

Get an existing MonitorV1 resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/loadbalancer/#MonitorV1State">MonitorV1State</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/loadbalancer/#MonitorV1">MonitorV1</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>admin_state_up=None<span class="p">, </span>delay=None<span class="p">, </span>expected_codes=None<span class="p">, </span>http_method=None<span class="p">, </span>max_retries=None<span class="p">, </span>region=None<span class="p">, </span>tenant_id=None<span class="p">, </span>timeout=None<span class="p">, </span>type=None<span class="p">, </span>url_path=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetMonitorV1<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/loadbalancer?tab=doc#MonitorV1State">MonitorV1State</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/loadbalancer?tab=doc#MonitorV1">MonitorV1</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.LoadBalancer.MonitorV1.html">MonitorV1</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.LoadBalancer.MonitorV1State.html">MonitorV1State</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, between sending probes to members.
Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, between sending probes to members.
Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, between sending probes to members.
Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the monitor.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, between sending probes to members.
Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expected_<wbr>codes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202". Changing this updates the expected_codes
of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http_<wbr>method</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to "GET". Changing this updates the http_method of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>retries</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Number of permissible ping failures before changing
the member's status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-openstack">https://github.com/pulumi/pulumi-openstack</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`openstack` Terraform Provider](https://github.com/terraform-providers/terraform-provider-openstack).</dd>
</dl>

