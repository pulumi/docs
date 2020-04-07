
---
title: "Listener"
block_external_search_index: true
---



Manages a V2 listener resource within OpenStack.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as openstack from "@pulumi/openstack";

const listener1 = new openstack.loadbalancer.Listener("listener_1", {
    insertHeaders: {
        "X-Forwarded-For": "true",
    },
    loadbalancerId: "d9415786-5f1a-428b-b35f-2f1523e146d2",
    protocol: "HTTP",
    protocolPort: 8080,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/lb_listener_v2.html.markdown.



## Create a Listener Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/loadbalancer/#Listener">Listener</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/loadbalancer/#ListenerArgs">ListenerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Listener</span><span class="p">(resource_name, opts=None, </span>admin_state_up=None<span class="p">, </span>connection_limit=None<span class="p">, </span>default_pool_id=None<span class="p">, </span>default_tls_container_ref=None<span class="p">, </span>description=None<span class="p">, </span>insert_headers=None<span class="p">, </span>loadbalancer_id=None<span class="p">, </span>name=None<span class="p">, </span>protocol=None<span class="p">, </span>protocol_port=None<span class="p">, </span>region=None<span class="p">, </span>sni_container_refs=None<span class="p">, </span>tenant_id=None<span class="p">, </span>timeout_client_data=None<span class="p">, </span>timeout_member_connect=None<span class="p">, </span>timeout_member_data=None<span class="p">, </span>timeout_tcp_inspect=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewListener<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/loadbalancer?tab=doc#ListenerArgs">ListenerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/loadbalancer?tab=doc#Listener">Listener</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Loadbalancer.Listener.html">Listener</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.LoadBalancer.ListenerArgs.html">ListenerArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed
for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the default pool with which the
Listener is associated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Tls<wbr>Container<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Insert<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The load balancer on which to provision this
Listener. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable name for the Listener. Does not have
to be unique.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic.
Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sni<wbr>Container<wbr>Refs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Client<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The client inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Member<wbr>Connect</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The member connection timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Member<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The member inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Tcp<wbr>Inspect</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The time in milliseconds, to wait for additional
TCP packets for content inspection.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed
for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the default pool with which the
Listener is associated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Tls<wbr>Container<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Insert<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The load balancer on which to provision this
Listener. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable name for the Listener. Does not have
to be unique.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic.
Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sni<wbr>Container<wbr>Refs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Client<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The client inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Member<wbr>Connect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The member connection timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Member<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The member inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Tcp<wbr>Inspect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The time in milliseconds, to wait for additional
TCP packets for content inspection.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed
for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the default pool with which the
Listener is associated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Tls<wbr>Container<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>insert<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The load balancer on which to provision this
Listener. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable name for the Listener. Does not have
to be unique.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic.
Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sni<wbr>Container<wbr>Refs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout<wbr>Client<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The client inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout<wbr>Member<wbr>Connect</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The member connection timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout<wbr>Member<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The member inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout<wbr>Tcp<wbr>Inspect</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The time in milliseconds, to wait for additional
TCP packets for content inspection.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed
for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>pool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the default pool with which the
Listener is associated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>tls_<wbr>container_<wbr>ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>insert_<wbr>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>loadbalancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The load balancer on which to provision this
Listener. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable name for the Listener. Does not have
to be unique.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic.
Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sni_<wbr>container_<wbr>refs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout_<wbr>client_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The client inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout_<wbr>member_<wbr>connect</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The member connection timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout_<wbr>member_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The member inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout_<wbr>tcp_<wbr>inspect</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The time in milliseconds, to wait for additional
TCP packets for content inspection.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Listener Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed
for the Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the default pool with which the
Listener is associated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Tls<wbr>Container<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Insert<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The load balancer on which to provision this
Listener. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Human-readable name for the Listener. Does not have
to be unique.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic.
Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sni<wbr>Container<wbr>Refs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout<wbr>Client<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The client inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout<wbr>Member<wbr>Connect</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The member connection timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout<wbr>Member<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The member inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout<wbr>Tcp<wbr>Inspect</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The time in milliseconds, to wait for additional
TCP packets for content inspection.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed
for the Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the default pool with which the
Listener is associated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Tls<wbr>Container<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Insert<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The load balancer on which to provision this
Listener. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Human-readable name for the Listener. Does not have
to be unique.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic.
Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sni<wbr>Container<wbr>Refs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout<wbr>Client<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The client inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout<wbr>Member<wbr>Connect</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The member connection timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout<wbr>Member<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The member inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout<wbr>Tcp<wbr>Inspect</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The time in milliseconds, to wait for additional
TCP packets for content inspection.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed
for the Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the default pool with which the
Listener is associated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Tls<wbr>Container<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>insert<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The load balancer on which to provision this
Listener. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Human-readable name for the Listener. Does not have
to be unique.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic.
Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sni<wbr>Container<wbr>Refs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout<wbr>Client<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The client inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout<wbr>Member<wbr>Connect</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The member connection timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout<wbr>Member<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The member inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout<wbr>Tcp<wbr>Inspect</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The time in milliseconds, to wait for additional
TCP packets for content inspection.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed
for the Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>pool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the default pool with which the
Listener is associated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>tls_<wbr>container_<wbr>ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>insert_<wbr>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>loadbalancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The load balancer on which to provision this
Listener. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable name for the Listener. Does not have
to be unique.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic.
Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sni_<wbr>container_<wbr>refs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout_<wbr>client_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The client inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout_<wbr>member_<wbr>connect</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The member connection timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout_<wbr>member_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The member inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout_<wbr>tcp_<wbr>inspect</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The time in milliseconds, to wait for additional
TCP packets for content inspection.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Listener Resource

Get an existing Listener resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/loadbalancer/#ListenerState">ListenerState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/loadbalancer/#Listener">Listener</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>admin_state_up=None<span class="p">, </span>connection_limit=None<span class="p">, </span>default_pool_id=None<span class="p">, </span>default_tls_container_ref=None<span class="p">, </span>description=None<span class="p">, </span>insert_headers=None<span class="p">, </span>loadbalancer_id=None<span class="p">, </span>name=None<span class="p">, </span>protocol=None<span class="p">, </span>protocol_port=None<span class="p">, </span>region=None<span class="p">, </span>sni_container_refs=None<span class="p">, </span>tenant_id=None<span class="p">, </span>timeout_client_data=None<span class="p">, </span>timeout_member_connect=None<span class="p">, </span>timeout_member_data=None<span class="p">, </span>timeout_tcp_inspect=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetListener<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/loadbalancer?tab=doc#ListenerState">ListenerState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/loadbalancer?tab=doc#Listener">Listener</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Loadbalancer.Listener.html">Listener</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Loadbalancer.ListenerState.html">ListenerState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed
for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the default pool with which the
Listener is associated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Tls<wbr>Container<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Insert<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The load balancer on which to provision this
Listener. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable name for the Listener. Does not have
to be unique.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic.
Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sni<wbr>Container<wbr>Refs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Client<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The client inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Member<wbr>Connect</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The member connection timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Member<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The member inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Tcp<wbr>Inspect</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The time in milliseconds, to wait for additional
TCP packets for content inspection.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed
for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the default pool with which the
Listener is associated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Tls<wbr>Container<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Insert<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The load balancer on which to provision this
Listener. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable name for the Listener. Does not have
to be unique.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic.
Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sni<wbr>Container<wbr>Refs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Client<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The client inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Member<wbr>Connect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The member connection timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Member<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The member inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Tcp<wbr>Inspect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The time in milliseconds, to wait for additional
TCP packets for content inspection.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed
for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the default pool with which the
Listener is associated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Tls<wbr>Container<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>insert<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The load balancer on which to provision this
Listener. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable name for the Listener. Does not have
to be unique.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic.
Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sni<wbr>Container<wbr>Refs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout<wbr>Client<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The client inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout<wbr>Member<wbr>Connect</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The member connection timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout<wbr>Member<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The member inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout<wbr>Tcp<wbr>Inspect</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The time in milliseconds, to wait for additional
TCP packets for content inspection.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed
for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>pool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the default pool with which the
Listener is associated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>tls_<wbr>container_<wbr>ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>insert_<wbr>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>loadbalancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The load balancer on which to provision this
Listener. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable name for the Listener. Does not have
to be unique.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic.
Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sni_<wbr>container_<wbr>refs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout_<wbr>client_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The client inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout_<wbr>member_<wbr>connect</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The member connection timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout_<wbr>member_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The member inactivity timeout in milliseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout_<wbr>tcp_<wbr>inspect</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The time in milliseconds, to wait for additional
TCP packets for content inspection.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-openstack">https://github.com/pulumi/pulumi-openstack</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

