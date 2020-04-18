
---
title: "Vnic"
block_external_search_index: true
---



Provides a VMware vSphere vnic resource.

## Importing 

An existing vNic can be [imported][docs-import] into this resource
via supplying the vNic's ID. An example is below:

[docs-import]: /docs/import/index.html

```typescript
import * as pulumi from "@pulumi/pulumi";
```

The above would import the the vnic `vmk2` from host with ID `host-123`.



## Create a Vnic Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#Vnic">Vnic</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#VnicArgs">VnicArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Vnic</span><span class="p">(resource_name, opts=None, </span>distributed_port_group=None<span class="p">, </span>distributed_switch_port=None<span class="p">, </span>host=None<span class="p">, </span>ipv4=None<span class="p">, </span>ipv6=None<span class="p">, </span>mac=None<span class="p">, </span>mtu=None<span class="p">, </span>netstack=None<span class="p">, </span>portgroup=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVnic<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VnicArgs">VnicArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#Vnic">Vnic</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.Vnic.html">Vnic</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.VSphere.VnicArgs.html">VnicArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}ESX host the interface belongs to
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Distributed<wbr>Port<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Key of the distributed portgroup the nic will connect to. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Distributed<wbr>Switch<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}UUID of the DVSwitch the nic will be attached to. Do not set if you set portgroup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv4">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Vnic<wbr>Ipv4Args</a></span>
    </dt>
    <dd>{{% md %}}IPv4 settings. Either this or `ipv6` needs to be set. See  ipv4 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv6">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Vnic<wbr>Ipv6Args</a></span>
    </dt>
    <dd>{{% md %}}IPv6 settings. Either this or `ipv6` needs to be set. See  ipv6 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mac</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}MAC address of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}MTU of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netstack</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}TCP/IP stack setting for this interface. Possible values are 'defaultTcpipStack', 'vmotion', 'vSphereProvisioning'. Changing this will force the creation of a new interface since it's not possible to change the stack once it gets created. (Default: `defaultTcpipStack`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Portgroup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Portgroup to attach the nic to. Do not set if you set distributed_switch_port.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}ESX host the interface belongs to
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Distributed<wbr>Port<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Key of the distributed portgroup the nic will connect to. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Distributed<wbr>Switch<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}UUID of the DVSwitch the nic will be attached to. Do not set if you set portgroup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv4">Vnic<wbr>Ipv4</a></span>
    </dt>
    <dd>{{% md %}}IPv4 settings. Either this or `ipv6` needs to be set. See  ipv4 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv6">Vnic<wbr>Ipv6</a></span>
    </dt>
    <dd>{{% md %}}IPv6 settings. Either this or `ipv6` needs to be set. See  ipv6 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mac</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}MAC address of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}MTU of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netstack</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}TCP/IP stack setting for this interface. Possible values are 'defaultTcpipStack', 'vmotion', 'vSphereProvisioning'. Changing this will force the creation of a new interface since it's not possible to change the stack once it gets created. (Default: `defaultTcpipStack`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Portgroup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Portgroup to attach the nic to. Do not set if you set distributed_switch_port.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}ESX host the interface belongs to
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>distributed<wbr>Port<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Key of the distributed portgroup the nic will connect to. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>distributed<wbr>Switch<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}UUID of the DVSwitch the nic will be attached to. Do not set if you set portgroup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv4">Vnic<wbr>Ipv4</a></span>
    </dt>
    <dd>{{% md %}}IPv4 settings. Either this or `ipv6` needs to be set. See  ipv4 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv6">Vnic<wbr>Ipv6</a></span>
    </dt>
    <dd>{{% md %}}IPv6 settings. Either this or `ipv6` needs to be set. See  ipv6 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mac</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}MAC address of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}MTU of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netstack</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}TCP/IP stack setting for this interface. Possible values are 'defaultTcpipStack', 'vmotion', 'vSphereProvisioning'. Changing this will force the creation of a new interface since it's not possible to change the stack once it gets created. (Default: `defaultTcpipStack`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>portgroup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Portgroup to attach the nic to. Do not set if you set distributed_switch_port.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}ESX host the interface belongs to
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>distributed_<wbr>port_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Key of the distributed portgroup the nic will connect to. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>distributed_<wbr>switch_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}UUID of the DVSwitch the nic will be attached to. Do not set if you set portgroup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv4">Dict[Vnic<wbr>Ipv4]</a></span>
    </dt>
    <dd>{{% md %}}IPv4 settings. Either this or `ipv6` needs to be set. See  ipv4 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv6">Dict[Vnic<wbr>Ipv6]</a></span>
    </dt>
    <dd>{{% md %}}IPv6 settings. Either this or `ipv6` needs to be set. See  ipv6 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mac</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}MAC address of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}MTU of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netstack</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}TCP/IP stack setting for this interface. Possible values are 'defaultTcpipStack', 'vmotion', 'vSphereProvisioning'. Changing this will force the creation of a new interface since it's not possible to change the stack once it gets created. (Default: `defaultTcpipStack`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>portgroup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Portgroup to attach the nic to. Do not set if you set distributed_switch_port.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Look up an Existing Vnic Resource

Get an existing Vnic resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#VnicState">VnicState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#Vnic">Vnic</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>distributed_port_group=None<span class="p">, </span>distributed_switch_port=None<span class="p">, </span>host=None<span class="p">, </span>ipv4=None<span class="p">, </span>ipv6=None<span class="p">, </span>mac=None<span class="p">, </span>mtu=None<span class="p">, </span>netstack=None<span class="p">, </span>portgroup=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetVnic<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VnicState">VnicState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#Vnic">Vnic</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.Vnic.html">Vnic</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere..VnicState.html">VnicState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Distributed<wbr>Port<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Key of the distributed portgroup the nic will connect to. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Distributed<wbr>Switch<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}UUID of the DVSwitch the nic will be attached to. Do not set if you set portgroup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}ESX host the interface belongs to
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv4">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Vnic<wbr>Ipv4Args</a></span>
    </dt>
    <dd>{{% md %}}IPv4 settings. Either this or `ipv6` needs to be set. See  ipv4 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv6">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Vnic<wbr>Ipv6Args</a></span>
    </dt>
    <dd>{{% md %}}IPv6 settings. Either this or `ipv6` needs to be set. See  ipv6 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mac</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}MAC address of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}MTU of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netstack</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}TCP/IP stack setting for this interface. Possible values are 'defaultTcpipStack', 'vmotion', 'vSphereProvisioning'. Changing this will force the creation of a new interface since it's not possible to change the stack once it gets created. (Default: `defaultTcpipStack`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Portgroup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Portgroup to attach the nic to. Do not set if you set distributed_switch_port.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Distributed<wbr>Port<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Key of the distributed portgroup the nic will connect to. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Distributed<wbr>Switch<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}UUID of the DVSwitch the nic will be attached to. Do not set if you set portgroup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}ESX host the interface belongs to
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv4">Vnic<wbr>Ipv4</a></span>
    </dt>
    <dd>{{% md %}}IPv4 settings. Either this or `ipv6` needs to be set. See  ipv4 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv6">Vnic<wbr>Ipv6</a></span>
    </dt>
    <dd>{{% md %}}IPv6 settings. Either this or `ipv6` needs to be set. See  ipv6 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mac</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}MAC address of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}MTU of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netstack</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}TCP/IP stack setting for this interface. Possible values are 'defaultTcpipStack', 'vmotion', 'vSphereProvisioning'. Changing this will force the creation of a new interface since it's not possible to change the stack once it gets created. (Default: `defaultTcpipStack`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Portgroup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Portgroup to attach the nic to. Do not set if you set distributed_switch_port.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>distributed<wbr>Port<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Key of the distributed portgroup the nic will connect to. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>distributed<wbr>Switch<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}UUID of the DVSwitch the nic will be attached to. Do not set if you set portgroup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}ESX host the interface belongs to
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv4">Vnic<wbr>Ipv4</a></span>
    </dt>
    <dd>{{% md %}}IPv4 settings. Either this or `ipv6` needs to be set. See  ipv4 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv6">Vnic<wbr>Ipv6</a></span>
    </dt>
    <dd>{{% md %}}IPv6 settings. Either this or `ipv6` needs to be set. See  ipv6 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mac</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}MAC address of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}MTU of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netstack</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}TCP/IP stack setting for this interface. Possible values are 'defaultTcpipStack', 'vmotion', 'vSphereProvisioning'. Changing this will force the creation of a new interface since it's not possible to change the stack once it gets created. (Default: `defaultTcpipStack`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>portgroup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Portgroup to attach the nic to. Do not set if you set distributed_switch_port.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>distributed_<wbr>port_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Key of the distributed portgroup the nic will connect to. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>distributed_<wbr>switch_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}UUID of the DVSwitch the nic will be attached to. Do not set if you set portgroup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}ESX host the interface belongs to
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv4">Dict[Vnic<wbr>Ipv4]</a></span>
    </dt>
    <dd>{{% md %}}IPv4 settings. Either this or `ipv6` needs to be set. See  ipv4 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vnicipv6">Dict[Vnic<wbr>Ipv6]</a></span>
    </dt>
    <dd>{{% md %}}IPv6 settings. Either this or `ipv6` needs to be set. See  ipv6 options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mac</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}MAC address of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}MTU of the interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netstack</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}TCP/IP stack setting for this interface. Possible values are 'defaultTcpipStack', 'vmotion', 'vSphereProvisioning'. Changing this will force the creation of a new interface since it's not possible to change the stack once it gets created. (Default: `defaultTcpipStack`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>portgroup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Portgroup to attach the nic to. Do not set if you set distributed_switch_port.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Vnic<wbr>Ipv4</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#VnicIpv4">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#VnicIpv4">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VnicIpv4Args">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VnicIpv4Output">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Use DHCP to configure the interface's IPv4 stack.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}IP address of the default gateway, if DHCP or autoconfig is not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Address of the interface, if DHCP is not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netmask</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Netmask of the interface, if DHCP is not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Use DHCP to configure the interface's IPv4 stack.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}IP address of the default gateway, if DHCP or autoconfig is not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Address of the interface, if DHCP is not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netmask</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Netmask of the interface, if DHCP is not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Use DHCP to configure the interface's IPv4 stack.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}IP address of the default gateway, if DHCP or autoconfig is not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Address of the interface, if DHCP is not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netmask</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Netmask of the interface, if DHCP is not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Use DHCP to configure the interface's IPv4 stack.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}IP address of the default gateway, if DHCP or autoconfig is not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Address of the interface, if DHCP is not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netmask</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Netmask of the interface, if DHCP is not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Vnic<wbr>Ipv6</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#VnicIpv6">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#VnicIpv6">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VnicIpv6Args">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VnicIpv6Output">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}List of IPv6 addresses
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoconfig</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Use IPv6 Autoconfiguration (RFC2462).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Use DHCP to configure the interface's IPv4 stack.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}IP address of the default gateway, if DHCP or autoconfig is not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}List of IPv6 addresses
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoconfig</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Use IPv6 Autoconfiguration (RFC2462).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Use DHCP to configure the interface's IPv4 stack.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}IP address of the default gateway, if DHCP or autoconfig is not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}List of IPv6 addresses
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoconfig</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Use IPv6 Autoconfiguration (RFC2462).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Use DHCP to configure the interface's IPv4 stack.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}IP address of the default gateway, if DHCP or autoconfig is not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}List of IPv6 addresses
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoconfig</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Use IPv6 Autoconfiguration (RFC2462).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Use DHCP to configure the interface's IPv4 stack.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}IP address of the default gateway, if DHCP or autoconfig is not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-vsphere">https://github.com/pulumi/pulumi-vsphere</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`vsphere` Terraform Provider](https://github.com/terraform-providers/terraform-provider-vsphere).</dd>
</dl>

