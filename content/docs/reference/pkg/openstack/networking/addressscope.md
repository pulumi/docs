
---
title: "AddressScope"
block_external_search_index: true
---



Manages a V2 Neutron addressscope resource within OpenStack.

## Example Usage

### Create an Address-scope

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as openstack from "@pulumi/openstack";

const addressscope1 = new openstack.networking.AddressScope("addressscope_1", {
    ipVersion: 6,
});
```

### Create a Subnet Pool from an Address-scope

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as openstack from "@pulumi/openstack";

const addressscope1 = new openstack.networking.AddressScope("addressscope_1", {
    ipVersion: 6,
});
const subnetpool1 = new openstack.networking.SubnetPool("subnetpool_1", {
    addressScopeId: addressscope1.id,
    prefixes: [
        "fdf7:b13d:dead:beef::/64",
        "fd65:86cc:a334:39b7::/64",
    ],
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_addressscope_v2.html.markdown.



## Create a AddressScope Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#AddressScope">AddressScope</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#AddressScopeArgs">AddressScopeArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AddressScope</span><span class="p">(resource_name, opts=None, </span>ip_version=None<span class="p">, </span>name=None<span class="p">, </span>project_id=None<span class="p">, </span>region=None<span class="p">, </span>shared=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAddressScope<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#AddressScopeArgs">AddressScopeArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#AddressScope">AddressScope</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.AddressScope.html">AddressScope</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.AddressScopeArgs.html">AddressScopeArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this
creates a new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the address-scope. Changing this updates the
name of the existing address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `region` argument of the provider is used. Changing this creates a new
address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this
creates a new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the address-scope. Changing this updates the
name of the existing address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `region` argument of the provider is used. Changing this creates a new
address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this
creates a new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the address-scope. Changing this updates the
name of the existing address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `region` argument of the provider is used. Changing this creates a new
address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this
creates a new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the address-scope. Changing this updates the
name of the existing address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `region` argument of the provider is used. Changing this creates a new
address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## AddressScope Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this
creates a new address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the address-scope. Changing this updates the
name of the existing address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `region` argument of the provider is used. Changing this creates a new
address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shared</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this
creates a new address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the address-scope. Changing this updates the
name of the existing address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `region` argument of the provider is used. Changing this creates a new
address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shared</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this
creates a new address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the address-scope. Changing this updates the
name of the existing address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `region` argument of the provider is used. Changing this creates a new
address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shared</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>ip_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this
creates a new address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the address-scope. Changing this updates the
name of the existing address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `region` argument of the provider is used. Changing this creates a new
address-scope.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shared</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing AddressScope Resource

Get an existing AddressScope resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#AddressScopeState">AddressScopeState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#AddressScope">AddressScope</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>ip_version=None<span class="p">, </span>name=None<span class="p">, </span>project_id=None<span class="p">, </span>region=None<span class="p">, </span>shared=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAddressScope<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#AddressScopeState">AddressScopeState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#AddressScope">AddressScope</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.AddressScope.html">AddressScope</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.AddressScopeState.html">AddressScopeState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this
creates a new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the address-scope. Changing this updates the
name of the existing address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `region` argument of the provider is used. Changing this creates a new
address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this
creates a new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the address-scope. Changing this updates the
name of the existing address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `region` argument of the provider is used. Changing this creates a new
address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this
creates a new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the address-scope. Changing this updates the
name of the existing address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `region` argument of the provider is used. Changing this creates a new
address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this
creates a new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the address-scope. Changing this updates the
name of the existing address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `region` argument of the provider is used. Changing this creates a new
address-scope.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.
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

