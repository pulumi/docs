
---
title: "Host"
block_external_search_index: true
---



Provides a VMware vSphere host resource. This represents an ESXi host that
can be used either as part of a Compute Cluster or Standalone.

## Importing 

An existing host can be [imported][docs-import] into this resource
via supplying the host's ID. An example is below:

[docs-import]: /docs/import/index.html

```typescript
import * as pulumi from "@pulumi/pulumi";
```

The above would import the host with ID `host-123`.



## Create a Host Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#Host">Host</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#HostArgs">HostArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Host</span><span class="p">(resource_name, opts=None, </span>cluster=None<span class="p">, </span>connected=None<span class="p">, </span>datacenter=None<span class="p">, </span>force=None<span class="p">, </span>hostname=None<span class="p">, </span>license=None<span class="p">, </span>lockdown=None<span class="p">, </span>maintenance=None<span class="p">, </span>password=None<span class="p">, </span>thumbprint=None<span class="p">, </span>username=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewHost<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#HostArgs">HostArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#Host">Host</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.Host.html">Host</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.VSphere.HostArgs.html">HostArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}FQDN or IP address of the host to be added.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Password that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Username that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Compute Cluster this host should
be added to. This should not be set if `datacenter` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to false then the host will be disconected.
Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter this host should
be added to. This should not be set if `cluster` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true then it will force the host to be added, even
if the host is already connected to a different vSphere instance. Default is `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>License</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The license key that will be applied to the host.
The license key is expected to be present in vSphere.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lockdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Set the lockdown state of the host. Valid options are
`disabled`, `normal`, and `strict`. Default is `disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Set the management state of the host. Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Host's certificate SHA-1 thumbprint. If not set the the
CA that signed the host's certificate should be trusted. If the CA is not trusted
and no thumbprint is set then the operation will fail.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}FQDN or IP address of the host to be added.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Password that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Username that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Compute Cluster this host should
be added to. This should not be set if `datacenter` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to false then the host will be disconected.
Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter this host should
be added to. This should not be set if `cluster` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true then it will force the host to be added, even
if the host is already connected to a different vSphere instance. Default is `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>License</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The license key that will be applied to the host.
The license key is expected to be present in vSphere.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lockdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Set the lockdown state of the host. Valid options are
`disabled`, `normal`, and `strict`. Default is `disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Set the management state of the host. Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Host's certificate SHA-1 thumbprint. If not set the the
CA that signed the host's certificate should be trusted. If the CA is not trusted
and no thumbprint is set then the operation will fail.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}FQDN or IP address of the host to be added.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Password that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Username that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Compute Cluster this host should
be added to. This should not be set if `datacenter` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If set to false then the host will be disconected.
Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter this host should
be added to. This should not be set if `cluster` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If set to true then it will force the host to be added, even
if the host is already connected to a different vSphere instance. Default is `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>license</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The license key that will be applied to the host.
The license key is expected to be present in vSphere.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lockdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Set the lockdown state of the host. Valid options are
`disabled`, `normal`, and `strict`. Default is `disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Set the management state of the host. Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Host's certificate SHA-1 thumbprint. If not set the the
CA that signed the host's certificate should be trusted. If the CA is not trusted
and no thumbprint is set then the operation will fail.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}FQDN or IP address of the host to be added.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Password that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Username that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Compute Cluster this host should
be added to. This should not be set if `datacenter` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to false then the host will be disconected.
Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter this host should
be added to. This should not be set if `cluster` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true then it will force the host to be added, even
if the host is already connected to a different vSphere instance. Default is `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>license</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The license key that will be applied to the host.
The license key is expected to be present in vSphere.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lockdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Set the lockdown state of the host. Valid options are
`disabled`, `normal`, and `strict`. Default is `disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Set the management state of the host. Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Host's certificate SHA-1 thumbprint. If not set the the
CA that signed the host's certificate should be trusted. If the CA is not trusted
and no thumbprint is set then the operation will fail.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Look up an Existing Host Resource

Get an existing Host resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#HostState">HostState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#Host">Host</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>cluster=None<span class="p">, </span>connected=None<span class="p">, </span>datacenter=None<span class="p">, </span>force=None<span class="p">, </span>hostname=None<span class="p">, </span>license=None<span class="p">, </span>lockdown=None<span class="p">, </span>maintenance=None<span class="p">, </span>password=None<span class="p">, </span>thumbprint=None<span class="p">, </span>username=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetHost<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#HostState">HostState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#Host">Host</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.Host.html">Host</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere..HostState.html">HostState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Compute Cluster this host should
be added to. This should not be set if `datacenter` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to false then the host will be disconected.
Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter this host should
be added to. This should not be set if `cluster` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true then it will force the host to be added, even
if the host is already connected to a different vSphere instance. Default is `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}FQDN or IP address of the host to be added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>License</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The license key that will be applied to the host.
The license key is expected to be present in vSphere.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lockdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Set the lockdown state of the host. Valid options are
`disabled`, `normal`, and `strict`. Default is `disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Set the management state of the host. Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Password that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Host's certificate SHA-1 thumbprint. If not set the the
CA that signed the host's certificate should be trusted. If the CA is not trusted
and no thumbprint is set then the operation will fail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Username that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Compute Cluster this host should
be added to. This should not be set if `datacenter` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to false then the host will be disconected.
Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter this host should
be added to. This should not be set if `cluster` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true then it will force the host to be added, even
if the host is already connected to a different vSphere instance. Default is `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}FQDN or IP address of the host to be added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>License</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The license key that will be applied to the host.
The license key is expected to be present in vSphere.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lockdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Set the lockdown state of the host. Valid options are
`disabled`, `normal`, and `strict`. Default is `disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Set the management state of the host. Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Password that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Host's certificate SHA-1 thumbprint. If not set the the
CA that signed the host's certificate should be trusted. If the CA is not trusted
and no thumbprint is set then the operation will fail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Username that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Compute Cluster this host should
be added to. This should not be set if `datacenter` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If set to false then the host will be disconected.
Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter this host should
be added to. This should not be set if `cluster` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If set to true then it will force the host to be added, even
if the host is already connected to a different vSphere instance. Default is `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}FQDN or IP address of the host to be added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>license</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The license key that will be applied to the host.
The license key is expected to be present in vSphere.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lockdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Set the lockdown state of the host. Valid options are
`disabled`, `normal`, and `strict`. Default is `disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Set the management state of the host. Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Password that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Host's certificate SHA-1 thumbprint. If not set the the
CA that signed the host's certificate should be trusted. If the CA is not trusted
and no thumbprint is set then the operation will fail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Username that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Compute Cluster this host should
be added to. This should not be set if `datacenter` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connected</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to false then the host will be disconected.
Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter this host should
be added to. This should not be set if `cluster` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true then it will force the host to be added, even
if the host is already connected to a different vSphere instance. Default is `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}FQDN or IP address of the host to be added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>license</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The license key that will be applied to the host.
The license key is expected to be present in vSphere.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lockdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Set the lockdown state of the host. Valid options are
`disabled`, `normal`, and `strict`. Default is `disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintenance</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Set the management state of the host. Default is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Password that will be used by vSphere to authenticate
to the host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Host's certificate SHA-1 thumbprint. If not set the the
CA that signed the host's certificate should be trusted. If the CA is not trusted
and no thumbprint is set then the operation will fail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Username that will be used by vSphere to authenticate
to the host.
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

