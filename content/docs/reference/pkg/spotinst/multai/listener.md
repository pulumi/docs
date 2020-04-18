
---
title: "Listener"
block_external_search_index: true
---



Provides a Spotinst Multai Listener.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as spotinst from "@pulumi/spotinst";

const myListener = new spotinst.multai.Listener("my_listener", {
    balancerId: "b-12345",
    name: "foo",
    port: 1337,
    protocol: "http",
    tags: [{
        key: "env",
        value: "prod",
    }],
    tlsConfig: {
        certificateIds: ["ce-12345"],
        cipherSuites: [""],
        maxVersion: "TLS12",
        minVersion: "TLS10",
        preferServerCipherSuites: true,
        sessionTicketsDisabled: false,
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/multai_listener.html.markdown.



## Create a Listener Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/spotinst/multai/#Listener">Listener</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/spotinst/multai/#ListenerArgs">ListenerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Listener</span><span class="p">(resource_name, opts=None, </span>balancer_id=None<span class="p">, </span>port=None<span class="p">, </span>protocol=None<span class="p">, </span>tags=None<span class="p">, </span>tls_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewListener<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/multai?tab=doc#ListenerArgs">ListenerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/multai?tab=doc#Listener">Listener</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Spotinst/Pulumi.Spotinst.Multai.Listener.html">Listener</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Spotinst/Pulumi.Spotinst.Multai.ListenerArgs.html">ListenerArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the balancer.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port on which the load balancer is listening.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol to allow connections to the load balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertag">List&lt;Listener<wbr>Tag<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of key:value paired tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tls<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertlsconfig">Listener<wbr>Tls<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Describes the TLSConfig configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the balancer.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port on which the load balancer is listening.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol to allow connections to the load balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertag">[]Listener<wbr>Tag</a></span>
    </dt>
    <dd>{{% md %}}A list of key:value paired tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tls<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertlsconfig">*Listener<wbr>Tls<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Describes the TLSConfig configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the balancer.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The port on which the load balancer is listening.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol to allow connections to the load balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertag">Listener<wbr>Tag[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of key:value paired tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tls<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertlsconfig">Listener<wbr>Tls<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Describes the TLSConfig configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>balancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the balancer.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The port on which the load balancer is listening.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol to allow connections to the load balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertag">List[Listener<wbr>Tag]</a></span>
    </dt>
    <dd>{{% md %}}A list of key:value paired tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tls_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertlsconfig">Dict[Listener<wbr>Tls<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Describes the TLSConfig configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Listener Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the balancer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port on which the load balancer is listening.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol to allow connections to the load balancer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertag">List&lt;Listener<wbr>Tag&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of key:value paired tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tls<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertlsconfig">Listener<wbr>Tls<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Describes the TLSConfig configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the balancer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port on which the load balancer is listening.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol to allow connections to the load balancer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertag">[]Listener<wbr>Tag</a></span>
    </dt>
    <dd>{{% md %}}A list of key:value paired tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tls<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertlsconfig">*Listener<wbr>Tls<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Describes the TLSConfig configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the balancer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The port on which the load balancer is listening.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol to allow connections to the load balancer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertag">Listener<wbr>Tag[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of key:value paired tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tls<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertlsconfig">Listener<wbr>Tls<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Describes the TLSConfig configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>balancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the balancer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The port on which the load balancer is listening.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol to allow connections to the load balancer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertag">List[Listener<wbr>Tag]</a></span>
    </dt>
    <dd>{{% md %}}A list of key:value paired tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tls_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertlsconfig">Dict[Listener<wbr>Tls<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Describes the TLSConfig configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Listener Resource

Get an existing Listener resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/spotinst/multai/#ListenerState">ListenerState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/spotinst/multai/#Listener">Listener</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>balancer_id=None<span class="p">, </span>port=None<span class="p">, </span>protocol=None<span class="p">, </span>tags=None<span class="p">, </span>tls_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetListener<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/multai?tab=doc#ListenerState">ListenerState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/multai?tab=doc#Listener">Listener</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Spotinst/Pulumi.Spotinst.Multai.Listener.html">Listener</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Spotinst/Pulumi.Spotinst.Multai.ListenerState.html">ListenerState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The port on which the load balancer is listening.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol to allow connections to the load balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertag">List&lt;Listener<wbr>Tag<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of key:value paired tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tls<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertlsconfig">Listener<wbr>Tls<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Describes the TLSConfig configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The port on which the load balancer is listening.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The protocol to allow connections to the load balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertag">[]Listener<wbr>Tag</a></span>
    </dt>
    <dd>{{% md %}}A list of key:value paired tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tls<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertlsconfig">*Listener<wbr>Tls<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Describes the TLSConfig configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The port on which the load balancer is listening.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol to allow connections to the load balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertag">Listener<wbr>Tag[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of key:value paired tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tls<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertlsconfig">Listener<wbr>Tls<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Describes the TLSConfig configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>balancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The port on which the load balancer is listening.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol to allow connections to the load balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertag">List[Listener<wbr>Tag]</a></span>
    </dt>
    <dd>{{% md %}}A list of key:value paired tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tls_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listenertlsconfig">Dict[Listener<wbr>Tls<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Describes the TLSConfig configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Listener<wbr>Tag</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#ListenerTag">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#ListenerTag">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/multai?tab=doc#ListenerTagArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/multai?tab=doc#ListenerTagOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tag's key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tag's value.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tag's key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tag's value.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tag's key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tag's value.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The tag's key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The tag's value.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Listener<wbr>Tls<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#ListenerTlsConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#ListenerTlsConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/multai?tab=doc#ListenerTlsConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/multai?tab=doc#ListenerTlsConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Certificate<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Contains one or more certificate chains to present to the other side of the connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cipher<wbr>Suites</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of supported cipher suites. If cipherSuites is nil, TLS uses a list of suites supported by the implementation.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}MaxVersion contains the maximum SSL/TLS version that is acceptable.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Min<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}MinVersion contains the minimum SSL/TLS version that is acceptable (1.0 is the minimum).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Prefer<wbr>Server<wbr>Cipher<wbr>Suites</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether the server selects the client’s most preferred ciphersuite, or the server’s most preferred ciphersuite.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Session<wbr>Tickets<wbr>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}May be set to true to disable session ticket (resumption) support.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Certificate<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Contains one or more certificate chains to present to the other side of the connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cipher<wbr>Suites</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of supported cipher suites. If cipherSuites is nil, TLS uses a list of suites supported by the implementation.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}MaxVersion contains the maximum SSL/TLS version that is acceptable.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Min<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}MinVersion contains the minimum SSL/TLS version that is acceptable (1.0 is the minimum).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Prefer<wbr>Server<wbr>Cipher<wbr>Suites</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether the server selects the client’s most preferred ciphersuite, or the server’s most preferred ciphersuite.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Session<wbr>Tickets<wbr>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}May be set to true to disable session ticket (resumption) support.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>certificate<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Contains one or more certificate chains to present to the other side of the connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cipher<wbr>Suites</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of supported cipher suites. If cipherSuites is nil, TLS uses a list of suites supported by the implementation.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}MaxVersion contains the maximum SSL/TLS version that is acceptable.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>min<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}MinVersion contains the minimum SSL/TLS version that is acceptable (1.0 is the minimum).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>prefer<wbr>Server<wbr>Cipher<wbr>Suites</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Controls whether the server selects the client’s most preferred ciphersuite, or the server’s most preferred ciphersuite.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>session<wbr>Tickets<wbr>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}May be set to true to disable session ticket (resumption) support.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>certificate<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Contains one or more certificate chains to present to the other side of the connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cipher<wbr>Suites</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of supported cipher suites. If cipherSuites is nil, TLS uses a list of suites supported by the implementation.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}MaxVersion contains the maximum SSL/TLS version that is acceptable.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>min<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}MinVersion contains the minimum SSL/TLS version that is acceptable (1.0 is the minimum).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>prefer<wbr>Server<wbr>Cipher<wbr>Suites</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether the server selects the client’s most preferred ciphersuite, or the server’s most preferred ciphersuite.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>session<wbr>Tickets<wbr>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}May be set to true to disable session ticket (resumption) support.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-spotinst">https://github.com/pulumi/pulumi-spotinst</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

